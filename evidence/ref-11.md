# Forum-informed local checks and their limits

Aridio Silva · Independent Researcher · ORCID 0009-0008-2411-6995

© 2026 Aridio Silva · Apache-2.0

Created / updated: November 7, 2026, America/Sao_Paulo.

Status: publication extract supporting paper reference [11].

This is a newly prepared public extract, not the complete private source report. Source hashes and extraction methods appear in [source-catalog.json](source-catalog.json). Receipt values are observations from the recorded configuration, not a new experiment or an independent replication.

Participant forum reports motivated checks; their statements are not treated as verified results for our configuration. The author report separates external reports, code inspection, reproduced cases and proposals.

The [November 4 parser receipt](parser-forum-receipt.json) records three malformed-array cases that did not return within five seconds under the stock vLLM 0.19.1 parser. The V11R6 compatibility layer returned MalformedGemma4ToolCall with MALFORMED_GEMMA4_ARGUMENT_NO_PROGRESS for each. A correctly delimited array control returned under both parsers. Plain JSON string quotes were still retained; that issue was not fixed by this check. These are local parser tests, not a Gemma benchmark.

The [V12 unit-test extract](v12-unit-local.json) records 73 tests and zero real model calls. The [V12 K2 extract](v12-k2-local.json) records local infrastructure checks with a scripted fake server: 32 mock tasks, 32 recorded resolutions, denominator 33 and fastapi_14186 deferred. requests_7433 and requests_7502 passed reference-patch rehearsals with network available. No isolated-network success is established. K2 does not demonstrate GPU, Gemma, real vLLM server behavior, Kaggle parity or scientific effectiveness. The later real V12 run did not reach these tasks.

R65 (parser non-progress) and R69 (network-sensitive tests) identify entries in the author's proposed risk-catalog extension. The evidence here supports the limited observations above, not universal mitigation of those risks.

Source identifiers: S18, S19, S20, S21, S22.
