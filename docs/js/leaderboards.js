const PRIMARY_LABELS = {
  f1_score: "F1",
  weighted_score: "Weighted score",
};

function scoreMap(submission) {
  return submission?.scores ?? {};
}

function formatScore(value) {
  const number = Number(value);
  if (!Number.isFinite(number)) {
    return value ?? "";
  }
  return number >= 10 ? number.toFixed(2) : number.toFixed(2);
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

function renderResultCard(task) {
  const winner = task.submissions[0];
  const primary = task.primary_metric;
  const card = document.createElement("article");
  card.className = "result-card";

  const top = document.createElement("div");
  const label = document.createElement("p");
  label.className = "winner-label";
  label.textContent = task.name;

  const team = document.createElement("p");
  team.className = "winner-team";
  team.textContent = winner?.team || winner?.owner || "No public submissions";

  const score = document.createElement("p");
  score.className = "winner-score";
  score.textContent = winner ? formatScore(scoreMap(winner)[primary]) : "-";

  const scoreLabel = document.createElement("p");
  scoreLabel.className = "score-label";
  scoreLabel.textContent = PRIMARY_LABELS[primary] ?? primary;

  top.append(label, team, score, scoreLabel);

  const list = document.createElement("ol");
  list.className = "top-list";
  task.submissions.slice(1, 4).forEach((submission) => {
    const item = document.createElement("li");
    const name = document.createElement("span");
    name.textContent = submission.team || submission.owner;
    const value = document.createElement("strong");
    value.textContent = formatScore(scoreMap(submission)[primary]);
    item.append(name, value);
    list.append(item);
  });

  const link = document.createElement("a");
  link.href = task.codabench_url;
  link.target = "_blank";
  link.rel = "noopener noreferrer";
  link.textContent = "Open Codabench task";

  card.append(top, list, link);
  return card;
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
    grid.replaceChildren(...data.competitions.map(renderResultCard));
    status.textContent = `Synced from Codabench on ${formatDate(data.generated_at)}.`;
  } catch (error) {
    status.textContent = "Could not load the local Codabench snapshot. Use the task links for current results.";
    console.error(error);
  }
}

main();
