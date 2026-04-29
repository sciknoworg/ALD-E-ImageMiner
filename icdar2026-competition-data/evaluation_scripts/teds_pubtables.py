from bs4 import BeautifulSoup
from rapidfuzz import fuzz

# ---------------------------------------------------------------------
# 1. Convert Markdown → minimal HTML table
# ---------------------------------------------------------------------
def markdown_to_html(md):
    lines = [line.strip() for line in md.splitlines() if "|" in line]
    if len(lines) < 2:
        raise ValueError("Invalid markdown table")

    header = [c.strip() for c in lines[0].strip("|").split("|")]
    rows = []

    for line in lines[2:]:
        parts = [c.strip() for c in line.strip("|").split("|")]
        rows.append(parts)

    html = "<table><thead><tr>"
    for h in header:
        html += f"<th>{h}</th>"
    html += "</tr></thead><tbody>"

    for r in rows:
        html += "<tr>"
        for c in r:
            html += f"<td>{c}</td>"
        html += "</tr>"

    html += "</tbody></table>"
    return html


# ---------------------------------------------------------------------
# 2. Convert HTML → Tree of nodes (official format)
# ---------------------------------------------------------------------
class TNode:
    def __init__(self, tag, text="", attrs=None):
        self.tag = tag
        self.text = text.strip()
        self.attrs = attrs or {}
        self.children = []

    def add(self, node):
        self.children.append(node)


def build_tree(html):
    soup = BeautifulSoup(html, "html.parser")
    root = soup.find("table")
    return build_node(root)


def build_node(bs_node):
    if bs_node.name is None:
        # text node
        return None

    node = TNode(bs_node.name, bs_node.get_text(strip=True), dict(bs_node.attrs))

    for child in bs_node.children:
        if getattr(child, "name", None) is None:
            continue
        cnode = build_node(child)
        if cnode:
            node.add(cnode)

    return node


# ---------------------------------------------------------------------
# 3. Zhang–Shasha Tree Edit Distance (official TEDS algorithm)
# ---------------------------------------------------------------------
def labels_equal(a: TNode, b: TNode):
    """Structural nodes match if tag name & attributes match."""
    if a.tag != b.tag:
        return False

    # compare structural HTML attributes like rowspan/colspan
    a_attrs = {k: a.attrs.get(k, None) for k in ["rowspan", "colspan"]}
    b_attrs = {k: b.attrs.get(k, None) for k in ["rowspan", "colspan"]}

    return a_attrs == b_attrs


def cell_replace_cost(a: TNode, b: TNode):
    """
    Official TEDS rules:
    - Non-text nodes: replace cost = 0 if tags match, else 1
    - Text nodes (<td>, <th>): replace cost = 0 if identical, else fuzzy cost
    """
    if a.tag not in ("td", "th") or b.tag not in ("td", "th"):
        return 0 if labels_equal(a, b) else 1

    # content-aware replacement using fuzzy ratio
    sim = fuzz.token_sort_ratio(a.text, b.text) / 100
    return 1 - sim


# ---------------------------------------------------------------------
# Recursive TED (Zhang–Shasha)
# ---------------------------------------------------------------------
def ted(a: TNode, b: TNode):
    """Tree edit distance between two TNode trees."""

    # simple memoized DP cache by identity
    cache = {}

    def _ted(x, y):
        key = (id(x), id(y))
        if key in cache:
            return cache[key]

        # If one is missing → cost = size of subtree
        if x is None:
            return tree_size(y)
        if y is None:
            return tree_size(x)

        # Children lists
        A = x.children
        B = y.children
        m, n = len(A), len(B)

        # matrix for forest edit distance
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] + tree_size(A[i-1])
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] + tree_size(B[j-1])

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = min(
                    dp[i-1][j] + tree_size(A[i-1]),     # delete subtree
                    dp[i][j-1] + tree_size(B[j-1]),     # insert subtree
                    dp[i-1][j-1] + _ted(A[i-1], B[j-1]) # replace child subtree
                )

        # Replace cost of the root
        rep_cost = cell_replace_cost(x, y)

        result = dp[m][n] + rep_cost
        cache[key] = result
        return result

    return _ted(a, b)


def tree_size(node: TNode):
    """Number of nodes in a subtree (each counts as cost 1)."""
    if node is None:
        return 0
    return 1 + sum(tree_size(c) for c in node.children)


# ---------------------------------------------------------------------
# 4. Official TEDS score
# ---------------------------------------------------------------------
def teds_pubtables_official(md1, md2):
    html1 = markdown_to_html(md1)
    html2 = markdown_to_html(md2)

    tree1 = build_tree(html1)
    tree2 = build_tree(html2)

    dist = ted(tree1, tree2)
    denom = tree_size(tree1) + tree_size(tree2)

    return 1 - dist / denom
