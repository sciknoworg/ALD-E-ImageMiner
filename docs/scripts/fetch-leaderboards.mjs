#!/usr/bin/env node

import { mkdir, writeFile } from "node:fs/promises";
import { dirname } from "node:path";
import { fileURLToPath } from "node:url";

const TASKS = [
  {
    slug: "classification",
    name: "Classification",
    competitionId: 12901,
    url: "https://www.codabench.org/competitions/12901/#/results-tab",
  },
  {
    slug: "data_extraction",
    name: "Data Table Extraction",
    competitionId: 12902,
    url: "https://www.codabench.org/competitions/12902/#/results-tab",
  },
  {
    slug: "summarization",
    name: "Summarization",
    competitionId: 12909,
    url: "https://www.codabench.org/competitions/12909/#/results-tab",
  },
  {
    slug: "vqa",
    name: "Visual Question Answering",
    competitionId: 12908,
    url: "https://www.codabench.org/competitions/12908/#/results-tab",
  },
];

const API_ROOT = "https://www.codabench.org/api";
const DEFAULT_OUTPUT = new URL("../data/leaderboards.json", import.meta.url);

function outputPath() {
  const index = process.argv.indexOf("--out");
  if (index !== -1 && process.argv[index + 1]) {
    return process.argv[index + 1];
  }
  return DEFAULT_OUTPUT;
}

async function fetchJson(url) {
  const response = await fetch(url, {
    headers: {
      Accept: "application/json",
      "User-Agent": "ALD-E-ImageMiner-GitHub-Pages-Leaderboard-Updater",
    },
  });
  if (!response.ok) {
    throw new Error(`${response.status} ${response.statusText} while fetching ${url}`);
  }
  return response.json();
}

function evaluationPhase(phases) {
  const sorted = [...phases].sort((a, b) => Number(a.index ?? 0) - Number(b.index ?? 0));
  return (
    sorted.find((phase) => /evaluation/i.test(phase.name ?? "")) ??
    sorted[sorted.length - 1]
  );
}

function scoresByKey(scores) {
  return Object.fromEntries(scores.map((score) => [score.column_key, Number(score.score)]));
}

function displayTeam(submission) {
  return submission.organization?.name || submission.owner || "Anonymous";
}

async function taskSnapshot(task) {
  const competition = await fetchJson(`${API_ROOT}/competitions/${task.competitionId}/`);
  const phase = evaluationPhase(competition.phases ?? []);
  if (!phase) {
    throw new Error(`No phase found for competition ${task.competitionId}`);
  }
  const leaderboard = await fetchJson(`${API_ROOT}/phases/${phase.id}/get_leaderboard/`);
  const columns = (leaderboard.tasks?.[0]?.columns ?? []).sort((a, b) => a.index - b.index);
  const primaryColumn = columns.find((column) => column.index === leaderboard.primary_index) ?? columns[0];

  return {
    slug: task.slug,
    name: task.name,
    competition_id: task.competitionId,
    codabench_url: task.url,
    phase_id: phase.id,
    phase_name: phase.name,
    primary_metric: primaryColumn?.key ?? "",
    columns: columns.map((column) => ({
      key: column.key,
      title: column.title,
      index: column.index,
      sorting: column.sorting,
      precision: column.precision,
    })),
    count: leaderboard.count ?? leaderboard.submissions?.length ?? 0,
    submissions: (leaderboard.submissions ?? []).map((submission, index) => ({
      rank: index + 1,
      id: submission.id,
      team: displayTeam(submission),
      owner: submission.owner,
      created_when: submission.created_when,
      profile_url: submission.slug_url
        ? new URL(submission.slug_url, "https://www.codabench.org").toString()
        : "",
      scores: scoresByKey(submission.scores ?? []),
    })),
  };
}

const snapshots = await Promise.all(TASKS.map(taskSnapshot));
const payload = {
  generated_at: new Date().toISOString(),
  source: "Public Codabench phase leaderboard APIs",
  competitions: snapshots,
};

const out = outputPath();
await mkdir(dirname(out instanceof URL ? fileURLToPath(out) : out), { recursive: true });
await writeFile(out, `${JSON.stringify(payload, null, 2)}\n`, "utf8");
console.log(`Wrote ${out}`);
