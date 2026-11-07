# V12 real run, operational log and V12R1 local validation

Aridio Silva · Independent Researcher · ORCID 0009-0008-2411-6995

© 2026 Aridio Silva · Apache-2.0

Created / updated: November 7, 2026, America/Sao_Paulo.

Status: publication extract supporting paper reference [12].

This is a newly prepared public extract, not the complete private source report. Source hashes and extraction methods appear in [source-catalog.json](source-catalog.json). Receipt values are observations from the recorded configuration, not a new experiment or an independent replication.

## One real, re-exposed development case

On November 6, Gemma 4 31B processed rich_3953 under P on Kaggle. This task had already been exposed during development. There was no B arm. The [worker extract](v12-real-worker.json) records 18 successful model requests, 324628 total tokens, 15211 output tokens, an applied 1095-byte patch, test_exit_code=1 and resolved=false. Before request 19, the context preflight recorded 29516 input tokens against a 32768-token context, 256-token margin and 3214-token minimum output reserve. It recorded backend_request_sent=false and CONTEXT_EXHAUSTED. No automatic retry was performed.

The [test summary](v12-test-summary.json) records 1 failed and 55 passed. The [JUnit identity/status extract](v12-junit-identities.json) records test_zwj as passed and test_non_printable as failed: one of the two required identities passed. Patch SHA-256 is `f1092811ae2449094ff6da33d589fa8e1fbe8e2b3f8835b4f7910a11175c5909`. The full archive's 1538 manifest members were rehashed with zero mismatches. No raw competition source, test code or reference patch is included.

## Visibility and operational evidence

[Trace metadata](v12-trace-metadata.json) contains event types and message-presence flags only. Of 21 nonempty agent-message events, 17 are thinking and four are visible text/final events. Counting all 21 as visible inflated the offline p_adherence measure. These counts do not certify P compliance. The raw thinking and messages are excluded.

The [cell progress extract](v12-progress-events.jsonl) contains 840 records, including EM_ANDAMENTO and SUPERVISAO_ATIVA heartbeats. Its [index](v12-progress-index.json) records event counts, the original log hash, extraction policy and source line numbers. Timestamps, task identity, phase, progress counters and timing fields provide operational evidence of monitoring and lifecycle events. They do not establish correct repair, productive reasoning between heartbeats, universal liveness, or a proven wall-clock bound. The complete cell log is private because it interleaves operational output with other material.

## V12R1 is a separate local configuration

V12R1 is P-only. Its [unit receipt](v12r1-unit-local.json) records 88 tests with no errors, failures or skips and no real model calls. Its [K2 receipt](v12r1-k2-local.json) records 124 passing checks and 32 scripted mock-task resolutions, no real model calls, no scientific task started and kaggle_started=false. The run uses reference-patch scripts, not model-generated successes.

Two V12R1 processing ZIPs were found and hashed. [Archive audit](archive-audit.json) identifies the final archive (59892245 bytes, SHA-256 `6d10dfb0b1952720e0f3c57230119ee2e1cccbe4cbb061b71af3b4f55edd8f17`) and pair archive (30682551 bytes, SHA-256 `0cb624c06fa5ccf790ef1ceed4a8716f9ad85f7fb8722013a94262288b3dbdd2`). The pair is embedded byte-for-byte in the final archive. They are two packages of the same local execution, not two experiments or a B/P comparison. The filename does not change their local-test classification. Neither full private archive is redistributed.

The configuration permits one agent session per task with no automatic retries; the session can contain multiple model/tool calls. This observation does not prove a simulation relation to the abstract controller or formally instantiate its M parameter. W18 reconciliation and the documentary release gate remain open. This real case does not establish effectiveness on the 129-task benchmark.

Source identifiers: S23, S24, S25, S26, S27, S28, S29, S30, S31, S32, S33, S34.
