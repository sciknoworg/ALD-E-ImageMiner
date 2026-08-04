const TASK_COLUMNS = {
  classification: ["accuracy", "precision", "recall", "f1_score"],
  data_extraction: ["rms", "teds", "weighted_score"],
  summarization: ["rouge1", "rouge2", "rougeL", "bertscore_f1", "weighted_score"],
  vqa: [
    "weighted_score",
    "factoid_exact_match",
    "yesno_f1_score",
    "paragraph_bertscore_f1",
    "list_set-based-f1",
  ],
};

const COLUMN_LABELS = {
  accuracy: "Accuracy",
  precision: "Precision",
  recall: "Recall",
  f1_score: "F1",
  rms: "RMS",
  teds: "TEDS",
  rouge1: "R1",
  rouge2: "R2",
  rougeL: "RL",
  bertscore_f1: "BERT-F1",
  weighted_score: "Weighted",
  factoid_exact_match: "Factoid EM",
  yesno_f1_score: "Yes/No F1",
  paragraph_bertscore_f1: "Paragraph BERT-F1",
  "list_set-based-f1": "List F1",
};

function formatNumber(value) {
  const number = Number(value);
  if (!Number.isFinite(number)) {
    return value ?? "";
  }
  return number.toFixed(number >= 10 ? 2 : 2);
}

function formatDate(value) {
  if (!value) {
    return "";
  }
  return new Intl.DateTimeFormat("en", {
    year: "numeric",
    month: "short",
    day: "numeric",
  }).format(new Date(value));
}

function cell(text, className = "") {
  const td = document.createElement("td");
  td.textContent = text;
  if (className) {
    td.className = className;
  }
  return td;
}

function renderLeaderboard(task) {
  const shownColumns = TASK_COLUMNS[task.slug] ?? task.columns.map((column) => column.key);
  const primaryKey = task.primary_metric;
  const article = document.createElement("article");
  article.className = "leaderboard-card";

  const header = document.createElement("header");
  const title = document.createElement("h3");
  title.textContent = task.name;
  const link = document.createElement("a");
  link.href = task.codabench_url;
  link.textContent = "Codabench";
  link.target = "_blank";
  link.rel = "noopener noreferrer";
  header.append(title, link);

  const meta = document.createElement("div");
  meta.className = "meta";
  meta.textContent = `${task.phase_name} phase · ${task.count} submissions · primary metric: ${COLUMN_LABELS[primaryKey] ?? primaryKey}`;

  const wrap = document.createElement("div");
  wrap.className = "table-wrap";
  const table = document.createElement("table");
  const thead = document.createElement("thead");
  const headRow = document.createElement("tr");
  ["#", "Team", ...shownColumns.map((column) => COLUMN_LABELS[column] ?? column), "Date"].forEach((label) => {
    const th = document.createElement("th");
    th.textContent = label;
    headRow.append(th);
  });
  thead.append(headRow);

  const tbody = document.createElement("tbody");
  task.submissions.slice(0, 5).forEach((submission) => {
    const tr = document.createElement("tr");
    tr.append(cell(String(submission.rank)));
    tr.append(cell(submission.team || submission.owner, "team-cell"));
    shownColumns.forEach((column) => {
      tr.append(cell(formatNumber(submission.scores[column]), column === primaryKey ? "metric-primary" : ""));
    });
    tr.append(cell(formatDate(submission.created_when)));
    tbody.append(tr);
  });

  table.append(thead, tbody);
  wrap.append(table);
  article.append(header, meta, wrap);
  return article;
}

async function main() {
  const status = document.querySelector("#leaderboard-status");
  const grid = document.querySelector("#leaderboard-grid");

  try {
    const response = await fetch(`data/leaderboards.json?ts=${Date.now()}`, { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const data = await response.json();
    grid.replaceChildren(...data.competitions.map(renderLeaderboard));
    status.textContent = `Last synced from Codabench: ${formatDate(data.generated_at)}.`;
  } catch (error) {
    status.textContent =
      "Could not load the local leaderboard snapshot. Use the Codabench task links for live results.";
    console.error(error);
  }
}

main();
