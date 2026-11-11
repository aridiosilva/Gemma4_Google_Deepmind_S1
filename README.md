# Frozen evidence for the Gemma 4 Developer Agent Paper Track

Aridio Silva · Independent Researcher, Brazil · [ORCID 0009-0008-2411-6995](https://orcid.org/0009-0008-2411-6995)

© 2026 Aridio Silva · Apache-2.0

Created November 7, 2026 · Updated November 11, 2026 · America/Sao_Paulo (UTC−03:00)

## Cite and verify v1.2.0

Use [`paper-evidence-v1.2.0`](https://github.com/aridiosilva/Gemma4_Google_Deepmind_S1/tree/paper-evidence-v1.2.0), commit [`433e7508f713d947b417d8522bc84b96eae1da45`](https://github.com/aridiosilva/Gemma4_Google_Deepmind_S1/commit/433e7508f713d947b417d8522bc84b96eae1da45), for reference [10] in *Budget-Bounded Software Repair with AI Agents*. The [permanent supplement](https://github.com/aridiosilva/Gemma4_Google_Deepmind_S1/blob/433e7508f713d947b417d8522bc84b96eae1da45/evidence/kaggle-bugs-2026-11-11/README.md) covers seven rounds on the public development profile.

| Rounds | Selected tasks | Executed tasks | Execution records | Resolutions |
| --- | ---: | ---: | ---: | ---: |
| R1–R6 | 33 | 32 | 55 | 17 |
| S54M | 54 | 54 | 54 | 20 |
| Total | 87 | 86 | 109 | 37 |

The historical rounds use each task's last recorded outcome and include selective reruns under different configurations. S54M uses one execution per task under a common configuration. One historical task was deferred and remains in the selected-task denominator.

From the root of a checkout of `paper-evidence-v1.2.0`, use Python 3.12 or later:

```text
python -I -B evidence/kaggle-bugs-2026-11-11/verify.py
```

The verifier checks the distributed files against the supplement manifest and recomputes the task and execution totals, resolutions, required-test failure counts, and S54M results from the public extracts. The extracts also support inspection of patch application, verifier verdicts, and recorded operational events. SHA-256 fingerprints of the seven original ZIPs and selected members record provenance and let a holder of the preserved originals compare their bytes with the catalog. Independent authentication of the underlying receipts requires access to the originals. Replaying the experiments also requires the original execution environment and harness.

`python -I -B verify-evidence.py` checks the root manifest and earlier receipts. `python -I -B controller-check.py` checks the abstract finite-state model. All three checks run locally without invoking Gemma, Kaggle, or a GPU.

## November 7 evidence

The original Submission One snapshot is available at [`paper-evidence-v1.0.0`](https://github.com/aridiosilva/Gemma4_Google_Deepmind_S1/tree/paper-evidence-v1.0.0). The [`paper-evidence-v1.1.0`](https://github.com/aridiosilva/Gemma4_Google_Deepmind_S1/tree/paper-evidence-v1.1.0) edition adds public extracts and selected processing receipts from the November 7 evidence. These include the [synthetic B/P pilot](evidence/ref-08.md), the [task 16 diagnostic](evidence/ref-09.md), [resource defects and JUnit identity experiments](evidence/ref-10.md), [forum-informed local checks](evidence/ref-11.md), and [V12 and V12R1 receipts](evidence/ref-12.md). The [source catalog](evidence/source-catalog.json) fingerprints original files and ZIP members. The [progress extract](evidence/v12-progress-events.jsonl) contains selected cell heartbeat and lifecycle fields.

## License

The original supporting text, evidence extracts, and verification code in this repository are covered by [Apache License 2.0](LICENSE). See [NOTICE](NOTICE). The historical CC BY 4.0 notice refers to the separate November 7, 2026 manuscript edition, *Budgeted software repair with AI agents*. Licensing of the November 11 REV1 manuscript is a separate decision for the author.
