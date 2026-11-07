# Frozen paper evidence: supplemental edition

Aridio Silva · Independent Researcher · ORCID 0009-0008-2411-6995

© 2026 Aridio Silva · Apache-2.0

Created / updated: November 7, 2026, America/Sao_Paulo.

This edition adds publication extracts and selected processing receipts supporting paper references 8–12. These documents are the publicly inspectable cited sources; they are not claims that the full private reports or processing archives are public. The repository is archived read-only after publication.

The original Submission One snapshot is preserved at tag `paper-evidence-v1.0.0`, commit `44c82db889d551ce0c0256209b6c9c95e16911e2`. The supplemental edition uses a new commit and tag `paper-evidence-v1.1.0`. No original tag is moved. The controller checker, pilot table and task 16 diagnostic retain their original bytes.

| Paper reference | Public document | Scope |
| --- | --- | --- |
| 8 | [Synthetic B/P pilot](evidence/ref-08.md) | One synthetic task, B then P, real model |
| 9 | [Task 16](evidence/ref-09.md) | Fixed public profile, local mock rehearsal |
| 10 | [Resource defects and gate](evidence/ref-10.md) | Pure synthetic checks; documentary block |
| 11 | [Forum-informed local checks](evidence/ref-11.md) | Parser reproduction and mocked V12 K2 |
| 12 | [V12 and V12R1](evidence/ref-12.md) | One real re-exposed V12 case; V12R1 local only |

The [source catalog](evidence/source-catalog.json) fingerprints originals and ZIP members. The [archive audit](evidence/archive-audit.json) records inspected processing ZIPs. Source hashes document provenance; without the excluded originals they cannot independently authenticate the extracts. The evidence supports inspection of reported counters, verdicts, identity cases and operational events, not end-to-end reproduction of the private harness.

The [progress event extract](evidence/v12-progress-events.jsonl) supplies allowlisted cell heartbeat/lifecycle fields without reasoning or tool bodies. No competition snapshot, dataset entry, reference patch, wheel, credential, private session or raw reasoning is distributed.

Run `python verify-evidence.py` using Python 3.12+ to verify the distributed file manifest and receipt consistency, then `python controller-check.py` for the abstract model check. These are local checks; they do not invoke Gemma, Kaggle or a GPU. A passing check confirms file integrity and stated arithmetic, not independent authenticity of source runs or implementation correspondence.

All new text, extracts and verification code in this repository are author-generated supporting material under Apache-2.0. External names and fingerprints do not grant rights to omitted third-party material. The separately delivered manuscript retains its stated CC BY 4.0 license. See LICENSE and NOTICE.
