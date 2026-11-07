# Evidence for the Gemma 4 Developer Agent Paper Track

Author: Aridio Silva · Independent Researcher, Brazil
ORCID: https://orcid.org/0009-0008-2411-6995
© 2026 Aridio Silva

Repository: `Gemma4_Google_Deepmind_S1`; S1 means **Submission One**.

Version 1.0.0. This repository contains the reviewed supporting evidence for the paper *Budgeted software repair with AI agents: Termination, verifiable acceptance, and abstention in the Gemma 4 challenge*. This is an independent research submission by Aridio Silva.

| Claim | File | Scope |
| --- | --- | --- |
| Abstract-controller finite-state check | `controller-check.py` | Local finite model, independent of inference and Kaggle execution. |
| Incompatible mandatory tests for task 16 | `task16-proof.md` | Logical incompatibility and preserved R2 summary, limited to the examined public profile. |
| B/P workflow pilot | `pilot-bp.csv` | One synthetic task, one execution per arm, fixed B-then-P order. |

## Run the abstract-controller check

Use Python 3.12 and its standard library:

```text
python -I -B controller-check.py
```

Expected output (also reproduced locally with Python 3.12.10):

```text
controle: (556, 953)
mutante: iniciar -> patch -> falsa -> commit_ok
```

The source bytes are preserved from the reviewed model checker. Its finite exploration does not establish correspondence with an entire software-repair implementation. The ranking proof in the paper covers arbitrary attempt limits under the stated progress assumptions.

## Pilot provenance and limits

The CSV was checked against the preserved ONE_SHOT_13 run and evaluation receipts. Both arms passed two tests and produced the same 214-byte patch, SHA-256 `5d6befcb58a9cd734bd603d022ffeab623c251d49584e236dba3c4bbe065ed15`.

The original evidence archive has SHA-256 `27b7dcb35947826d48fbade92b9de267ea2f3b9ecea4ecfc6f8b506e92128908`. All 266 entries in its manifest were checked locally. Raw sessions and the original archive remain in the author's private evidence store. This one synthetic case does not establish general performance superiority or count toward the planned 33-of-129 competition-task sample.

The three evidence groups above are the scope of this release. The release is not a redistribution of competition datasets, snapshots, wheels, model weights, or raw execution logs, and does not independently reproduce every internal report referenced by the manuscript.

## Verify the frozen release

`MANIFEST.sha256` lists SHA-256 values for the seven other files. From the repository root on a system with sha256sum:

```text
sha256sum -c MANIFEST.sha256
```

The release tag is `paper-evidence-v1.0.0`. The paper cites the full 40-character commit SHA. The repository is intended to be archived after publication and verification so its contents remain available for reading. Use the exact commit for reproducibility.

## License

The original material in this evidence repository is licensed under the Apache License, Version 2.0; see `LICENSE` and `NOTICE`. The Kaggle Writeup is a separate publication and is not included in this evidence repository. Third-party competition resources remain governed by their own terms and are linked rather than redistributed.
