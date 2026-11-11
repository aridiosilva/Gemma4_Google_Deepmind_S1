# Kaggle execution evidence through 11 November 2026

**Author:** Aridio Silva · Independent Researcher, Brazil · ORCID 0009-0008-2411-6995

**Preferred citation:** Silva, Aridio · **Copyright:** © 2026 Aridio Silva · **License:** Apache-2.0

**Created / last updated:** 2026-11-11 · America/Sao_Paulo (UTC−03:00)

**Status:** Public evidence supplement for the Gemma 4 Paper Track.

This supplement covers all seven recorded Kaggle rounds through S54M. It supports the study's evaluation of 87 selected Bug tasks from the public development set. One historical task was deferred. The analysis counts the last recorded execution for each historical task and the single execution for each S54M task.

| Scope | Selected tasks | Executed tasks | Execution records | Resolutions |
| --- | ---: | ---: | ---: | ---: |
| R1–R6, historical | 33 | 32 | 55 | 17 |
| S54M, one configuration | 54 | 54 | 54 | 20 |
| Study total | 87 | 86 | 109 | 37 |

The 37 resolutions equal **42.5% of the 87 selected tasks**, with the deferred task retained in the coverage denominator. Across the 86 executed tasks, 49 ended without resolution. Of those, 44 produced an applied patch that the verifier rejected, including 36 with at least one required test failure. The historical figures reflect differing configurations and selective re-exposure. S54M resolved **20/54 (37.0%, 95% Wilson interval 25.4–50.4%)** under a common configuration and a maximum of 30 model requests per task. These proportions describe the evaluated development tasks.

| S54M verifier outcome | Count |
| --- | ---: |
| Resolved with an applied patch | 20 |
| Rejected, with at least one required test failure | 23 |
| Rejected, failures identified outside the required IDs | 7 |
| Evaluation without a usable test verdict | 3 |
| Output truncated with an empty patch | 1 |

Two records classified automatically as inconclusive had usable negative test verdicts and count among the 30 rejections. For failure analysis, the audit reconciled path prefixes using the recorded collection root before matching full parametrized test IDs. A missing failure ID alone leaves the individual test's result open.

The S54M cell log spans **07:40:14–13:14:56** São Paulo time on 11 November. The batch receipt confirms completion and cleanup for the 54-task run. Two memory-guard records show that the test process trees were stopped and that their peak RSS reached the recorded limit. Those evaluations remain without a usable verdict. A third such evaluation recorded a syntax error. The fourth task without a usable test verdict had an empty patch after output truncation.

## Audit the numbers

Run **python -I -B evidence/kaggle-bugs-2026-11-11/verify.py** from the repository root. The script checks the supplement manifest and recomputes the counts, rates, task uniqueness, historical re-exposures, required-test failure intersections and guard-event checks. It uses the Python standard library and runs without network access.

- [Inventory](inventory.csv) lists 87 task aliases, cohort, upstream repository, task ID fingerprint and deferred status.
- [Execution receipts](executions.jsonl) contain 109 allowlisted records with class, patch application, verifier fields, usage, timing and source member fingerprints. The required and failed test identifiers are published as SHA-256 digests. A normalized match uses the digest of the original required ID. Failures outside the required IDs are hashed with an outside-required domain prefix.
- [Source archive catalog](source-archives.json) gives the configuration and SHA-256 of each original ZIP and its task summary.
- [Operational receipts](operations.json) give the cell boundaries, batch status and the two memory-guard events, with the original member fingerprints.
- [Supplement manifest](manifest.sha256) gives the SHA-256 of every distributed file in this directory.

For each resolved execution, the extract requires agreement among the task summary, evaluation receipt and pre-identity verdict, an applied nonempty patch and a confirmed zero test exit code. For a rejection, it requires an applied nonempty patch and a confirmed test exit code of one. The match between required and failed fingerprints then locates the failure. The coarse stage codes C2, C3, C4 and C5 correspond respectively to verifier rejection, missing usable verdict after reaching evaluation, a model limit without usable evaluation, and an empty patch.

The task aliases can be joined against a permitted local copy of the development dataset by computing SHA-256 over the UTF-8 instance ID. The archive and member hashes let a holder of the preserved originals trace the values to the underlying records. A reader with the distributed supplement can check its integrity and recalculate the published results. Replaying the runs or independently authenticating the underlying receipts requires the original artifacts and execution environment.
