# Resource defects and documentary release gate

Aridio Silva · Independent Researcher · ORCID 0009-0008-2411-6995

© 2026 Aridio Silva · Apache-2.0

Created / updated: November 7, 2026, America/Sao_Paulo.

Status: publication extract supporting paper reference [10].

This is a newly prepared public extract, not the complete private source report. Source hashes and extraction methods appear in [source-catalog.json](source-catalog.json). Receipt values are observations from the recorded configuration, not a new experiment or an independent replication.

The November 2 resource audit distinguished pure local reproductions from real model/task execution. No scientific task or model call was made by that audit.

The [original author-generated W18 receipt](w18-synthetic-receipt.json) contains all nine synthetic JUnit documents, requirements and observed helper/proposal outcomes. The swegemma 0.2.11 helper incorrectly accepted three mismatches: wrong module, wrong function prefix and wrong parameter. The proposed comparator rejected these cases. This is a pure-function test, not validation of all real task identities or the final integrated worker.

The [parser receipt extract](parser-audit.json) records the pinned vLLM parser and the seven local cases. The audit used an isolated pure-parser reproduction with a deterministic non-progress guard; it did not run a GPU server. The later real-parser timeout observations are supplied separately in reference [11].

The [release-gate extract](release-gate.json) records SCIENTIFIC_RELEASE_BLOCKED_KNOWN_DEPENDENCY_DEFECT, motivated by W01 and W18, with enforcement DOCUMENTED_REVIEW_GATE_NOT_YET_WIRED_TO_FROZEN_RUNTIME. This is a documentary review block, not evidence of automatic executor enforcement. Subsequent integration of an identity gate does not by itself reconcile this audit with all nine original cases. That reconciliation remains open in the paper.

Source identifiers: S13, S14, S15, S16, S17.
