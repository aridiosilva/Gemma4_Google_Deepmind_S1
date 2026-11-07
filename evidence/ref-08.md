# Synthetic B/P pilot: receipt extract

Aridio Silva · Independent Researcher · ORCID 0009-0008-2411-6995

© 2026 Aridio Silva · Apache-2.0

Created / updated: November 7, 2026, America/Sao_Paulo.

Status: publication extract supporting paper reference [8].

This is a newly prepared public extract, not the complete private source report. Source hashes and extraction methods appear in [source-catalog.json](source-catalog.json). Receipt values are observations from the recorded configuration, not a new experiment or an independent replication.

On October 27, 2026, ONE_SHOT_13 ran B then P once each on the synthetic pagination task B01-page-boundary using Gemma 4 31B, vLLM 0.19.1 and swegemma 0.2.11. Both arms passed 2/2 tests and produced the same 214-byte patch (SHA-256 `5d6befcb58a9cd734bd603d022ffeab623c251d49584e236dba3c4bbe065ed15`). Requested seed was 0; each arm made six model requests.

| Arm | Tokens | Launcher seconds (includes evaluation) |
| --- | ---: | ---: |
| B | 14881 | 45.979808217 |
| P | 16268 | 28.490074669 |

[Selected primary receipts](pilot-receipts.json) retain verdicts, counters, cleanup status and patch/output hashes. The source ZIP's 266-file manifest was verified against every listed member. [pilot-bp.csv](../pilot-bp.csv) is unchanged from the original frozen S1.

One task, one observation per arm, and fixed order do not support a causal speedup or an effectiveness estimate. Attempt 11 is outside this extract and is no longer cited as supporting evidence in the revised paper. No competition task or benchmark success rate is inferred from this synthetic pilot.

Source identifiers: S01, S02, S03, S04, S05, S06, S07, S08, S09.
