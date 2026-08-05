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
  const primary = task.primary_metric;
  const card = document.createElement("article");
  card.className = "result-card";

  const label = document.createElement("p");
  label.className = "result-label";
  label.textContent = task.name;

  const scoreLabel = document.createElement("p");
  scoreLabel.className = "score-label";
  scoreLabel.textContent = `Ranking metric: ${PRIMARY_LABELS[primary] ?? primary}`;

  const header = document.createElement("div");
  header.append(label);

  const link = document.createElement("a");
  link.href = task.codabench_url;
  link.target = "_blank";
  link.rel = "noopener noreferrer";
  link.textContent = "Open Codabench task";

  if (!task.submissions.length) {
    const empty = document.createElement("p");
    empty.className = "empty-leaderboard";
    empty.textContent = "No public submissions";
    card.append(header, empty, scoreLabel, link);
    return card;
  }

  const table = document.createElement("table");
  table.className = "leaderboard-mini";
  table.setAttribute("aria-label", `${task.name} leaderboard top teams`);

  const thead = document.createElement("thead");
  const headerRow = document.createElement("tr");
  ["", "Team", PRIMARY_LABELS[primary] ?? primary].forEach((heading, index) => {
    const th = document.createElement("th");
    th.textContent = heading;
    if (index === 0) {
      th.setAttribute("aria-label", "Rank");
    }
    headerRow.append(th);
  });
  thead.append(headerRow);

  const tbody = document.createElement("tbody");
  task.submissions.slice(0, 5).forEach((submission, index) => {
    const row = document.createElement("tr");
    const rankCell = document.createElement("td");
    const medal = document.createElement("span");
    medal.className = `rank-medal rank-${index + 1}`;
    medal.textContent = index + 1;
    medal.setAttribute("aria-label", `Rank ${index + 1}`);
    rankCell.append(medal);

    const teamCell = document.createElement("td");
    const name = document.createElement("span");
    name.className = "team-name";
    name.textContent = submission.team || submission.owner;

    const valueCell = document.createElement("td");
    const value = document.createElement("strong");
    value.textContent = formatScore(scoreMap(submission)[primary]);
    valueCell.append(value);

    teamCell.append(name);
    row.append(rankCell, teamCell, valueCell);
    tbody.append(row);
  });
  table.append(thead, tbody);

  card.append(header, table, scoreLabel, link);
  return card;
}

async function main() {
  const status = document.querySelector("#leaderboard-status");
  const grid = document.querySelector("#leaderboard-grid");

  try {
    const leaderboardUrl = new URL(`data/leaderboards.json?ts=${Date.now()}`, document.baseURI);
    const response = await fetch(leaderboardUrl, { cache: "no-store" });
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
