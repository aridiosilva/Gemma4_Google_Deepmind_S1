# R01–R72 Platform and Environment Risks in the Gemma 4 Developer Agent Challenge

**Author:** Aridio Silva · Independent Researcher, Brazil · ORCID 0009-0008-2411-6995  
**Preferred citation:** Silva, Aridio (2026), *R01–R72 Platform and Environment Risks in the Gemma 4 Developer Agent Challenge*.  
**Copyright:** © 2026 Aridio Silva. No public license has been assigned.  
**Edition:** English public edition, November 12, 2026. The [Portuguese source report](https://github.com/aridiosilva/Gemma4_Google_Deepmind_S1/blob/b41100a1618e9ee3865e3bb745deaff1dc25baae/evidence/r01-r72-risk-catalog-pt.md) was compiled on November 6, 2026, at 18:52 São Paulo time and updated at 19:10 to include W01–W25. Claude Code (Claude Opus 5.5) assisted with that source at the author's request.  
**Status:** Research catalog for the Paper Track. The evidence status is given per occurrence. Proposed checks describe how a risk could be evaluated.

## 1 Purpose and scope

This report consolidates 72 risks relevant to producing and evaluating patches in the Gemma 4 Developer Agent Challenge. R01–R64 come from the architecture catalog [1, §5]. R65–R72 come from the November 4 analysis of the official competition forum [2, §4]. The catalog helps identify whether a difficulty arises from the repair policy P, the environment, the inference stack, or the evaluation harness.

The entries cover competition constraints, library defects, model behavior, and project decisions such as relying on memory estimates or general benchmarks. The categories in Section 3 are interpretations used by this report. R01–R64 form the canonical catalog. R65–R72 are a proposed extension. The title of [2] mentions R65–R74, while its table defines R65–R72. The source review found no descriptions for R73 or R74 and no entry for R75.

Section 4 condenses the risk descriptions. W01–W25 are concrete occurrences recorded in the resource audit [4] and [1, §26]. An occurrence can be associated with more than one risk. The W entries state whether the source is a report, inspection, local reproduction, integration check, or Kaggle observation.

R65 and W01 describe the same vLLM 0.19.1 `gemma4` parser mechanism. The resource audit mapped it to R06, R20, R22, R27, R35, R37, R44, R48, and R62. The later forum analysis proposed the more specific R65 identifier. Both mappings are retained for traceability.

## 2 Source keys

| Key | Source | Context |
|---|---|---|
| G1 | A 34-page PDF of a Gemini conversation about restrictions, limitations, and errors | Page references use physical page order |
| G1-R1, G1-R3 | Excerpts recovered from the G1 conversation | Gemini responses |
| G2 | *Advanced Implementation Risks and Safeguards* | Guide generated in the same conversation |
| G4 | Gemma documentation used in [1, §5.9] | Source for R51–R64, with B2 and B11–B14 |
| A1 | Architecture proposal, October 18, 2026 | Historical design |
| U1 | Author's instructions and observations, October 19, 2026 | Includes the observed symlink failure |
| O1 | Competition overview and evaluation [5] | Official source |
| O3 | Announcement of the 12B, E4B, and E2B models [6] | Kaggle staff and participant comments |
| O4 | Official Getting Started notebook and input data [7] | Official source |
| O5, O5a | Kaggle staff comments and the discussion of lost reasoning [8, 9] | Defect confirmations and announced fixes |

R65–R72 cite topic numbers from the [official competition discussion](https://www.kaggle.com/competitions/gemma-4-developer-agent/discussion). The historical review read these topics on November 4, 2026 [2, §1].

## 3 Summary of the 72 risks

- **A** covers Kaggle platform and rules, including offline execution, packaging, images, queues, quotas, deadlines, and eligible model variants.
- **B** covers the agent and submission framework, including ADK, `adk_submission`, the agent compiler, and tool registration.
- **C** covers inference and model behavior, including vLLM, parsing, Gemma 4, reasoning, the KV cache, and adapters.
- **D** covers the competition harness, tools, and tasks, including sandboxes, the verifier, generated prompts, and task repositories.
- **E** covers project planning, methodology, and interpretation.

A risk can have two categories when the sources indicate a shared cause. Section 6 gives the category counts.

| ID | Risk | Category | Source section | W occurrences [4] |
|---|---|---|---|---|
| R01 | Offline execution | A | [1] §5.1 | — |
| R02 | Symlinks and path boundaries | A | [1] §5.1 | — |
| R03 | ZIP layout and contents | A | [1] §5.1 | — |
| R04 | Include directives and YAML syntax | B | [1] §5.1 | — |
| R05 | Tool registration and availability | B | [1] §5.1 | — |
| R06 | Python tool schemas | B | [1] §5.1 | W01, W08, W09, W13 |
| R07 | Subagents and control handoff | B | [1] §5.1 | — |
| R08 | Prompt-based and enforced control | B | [1] §5.1 | — |
| R09 | Accumulation of logs and irrelevant code | E | [1] §5.2 | — |
| R10 | Compaction loses tool results | B | [1] §5.2 | W06 |
| R11 | Reasoning lost between calls | B+C | [1] §5.2 | W02, W06, W14 |
| R12 | Flags that change reasoning mode | B+C | [1] §5.2 | W02, W06, W14 |
| R13 | Reasoning budget and seed fail to propagate | B+C | [1] §5.2 | W02, W06, W14 |
| R14 | Response limit mistaken for task limit | E | [1] §5.2 | W06 |
| R15 | Usable context window and response headroom | C | [1] §5.2 | W06 |
| R16 | Empty or unhelpful semantic search | D | [1] §5.3 | W21 |
| R17 | Missing or incompatible graph data | D | [1] §5.3 | W21 |
| R18 | Excessive search output | D | [1] §5.3 | W21 |
| R19 | Edit match failure | C+D | [1] §5.3 | W04 |
| R20 | Double encoding of tool results | B+C | [1] §5.3 | W01, W02, W09, W14, W17 |
| R21 | File line endings and encoding | D | [1] §5.3 | — |
| R22 | Repeated actions and searches without progress | C+E | [1] §5.3 | W01 |
| R23 | Mixing model variants | A | [1] §5.4 | — |
| R24 | Model selection by quality labels | E | [1] §5.4 | — |
| R25 | Estimates of weight VRAM | E | [1] §5.4 | — |
| R26 | LoRA reduces available KV cache | C | [1] §5.4 | W10, W19 |
| R27 | Hangs on long prompts | C | [1] §5.4 | W01, W10, W11, W12, W19 |
| R28 | Adapter discovery and identity | A+C | [1] §5.4 | W19 |
| R29 | Number and rank of adapters | E | [1] §5.4 | W19 |
| R30 | Assumed parallelism | E | [1] §5.4 | — |
| R31 | Unavailable dependencies | A | [1] §5.5 | W03 |
| R32 | Incompatible binary wheels | A | [1] §5.5 | W03, W05, W07, W10, W13, W15, W16, W20 |
| R33 | Interpreter and virtual-environment mismatch | A | [1] §5.5 | W03, W04, W16, W23, W24 |
| R34 | Vendoring and installation before harness startup | A | [1] §5.5 | W03, W04 |
| R35 | Mixing platform versions | A | [1] §5.5 | 20 occurrences (see Section 4.11) |
| R36 | Commands exceed remaining time | A+D | [1] §5.6 | — |
| R37 | Orphaned descendants and incomplete cancellation | D | [1] §5.6 | W01, W11, W12, W22, W23, W24 |
| R38 | System limits and isolation | D | [1] §5.6 | — |
| R39 | Accumulation of disk files and logs | D | [1] §5.6 | — |
| R40 | Host and GPU memory | A+C | [1] §5.6 | — |
| R41 | Destructive cleanup | E | [1] §5.7 | — |
| R42 | Empty or uncaptured patch | D | [1] §5.7 | — |
| R43 | Long tests or tests in the wrong environment | D+E | [1] §5.7 | W03 |
| R44 | Local pass mistaken for official resolution | D | [1] §5.7 | W01, W03, W04, W05, W16, W18, W23, W24, W25 |
| R45 | Persistence and loss of evidence | D | [1] §5.7 | — |
| R46 | Mocks and simulations mistaken for real-model results | E | [1] §5.7 | — |
| R47 | Long queues and quota consumption | A | [1] §5.8 | — |
| R48 | Opaque errors and inconsistent UI state | A | [1] §5.8 | W01, W07, W08, W11, W12, W13, W15, W20, W22, W23, W24 |
| R49 | Local speed without scorer parity | A+E | [1] §5.8 | — |
| R50 | Global limit and termination policy | A | [1] §5.8 | — |
| R51 | Confusing weight memory with peak runtime memory | E | [1] §5.9 | — |
| R52 | Inferring memory use solely from effective or active parameters | E | [1] §5.9 | — |
| R53 | Applying GGUF, Q4_0, or mobile assumptions to W4A16-CT | C | [1] §5.9 | — |
| R54 | Mixing Gemma 3 and 4 templates, tokens, or tokenizers | C | [1] §5.9 | — |
| R55 | Removing needed context within a tool turn | B | [1] §5.9 | — |
| R56 | Treating a concision instruction as a timeout or reasoning limit | E | [1] §5.9 | — |
| R57 | Assuming a tool exists because its name appears in YAML | B | [1] §5.9 | — |
| R58 | Copying sampling parameters without confirming they are applied | C | [1] §5.9 | — |
| R59 | Producing LoRA in a scorer-incompatible format | A | [1] §5.9 | — |
| R60 | Applying online, JAX, or TPU assumptions to the sandbox | A | [1] §5.9 | — |
| R61 | Depending on MTP without confirmed support or benefit | C | [1] §5.9 | — |
| R62 | Accepting a tool result under the wrong interpretation | C+E | [1] §5.9 | W01, W04, W07, W09, W17, W18, W19, W22, W23, W24, W25 |
| R63 | Using a general benchmark to predict issue resolution | E | [1] §5.9 | — |
| R64 | Using a qualitative sample or incomplete example to validate training | E | [1] §5.9 | — |
| R65 | vLLM 0.19.1 parser stalls on a malformed array | C | [2] §3.1 and §4 | same mechanism as W01 |
| R66 | JSON string quotes retained in the parsed value | C | [2] §3.2 and §4 | — |
| R67 | Backtick-terminated strings cause missing `edit_file` arguments | C | [2] §3.3 and §4 | — |
| R68 | Test reset fails before applying `test_patch` | D | [2] §3.6 and §4 | — |
| R69 | Network-sensitive tests behave differently offline | D | [2] §3.8 and §4 | — |
| R70 | Mutually exclusive skip conditions make a profile unsatisfiable | D | [2] §3.9 and §4 | — |
| R71 | Verifier conventions can reject valid repairs | D | [2] §3.10 and §4 | — |
| R72 | Harness-generated prompts can mislead the model | D | [2] §3.11 and §4 | — |

## 4 Risk descriptions

Each proposed check describes evidence that would show the risk is controlled if a corresponding experiment is undertaken [1, §5].

### 4.1 Submission and integration contracts (R01–R08)

**R01 — Offline execution (A).** The evaluation sandbox has no network. Agent dependencies must therefore be available without downloads, remote documentation, or online installation. Sources: G1, pp. 3–4, 14, 16, 19; G2, §1; O1. Proposed approach: use resources available through the official contract. Proposed check: start the agent, locate code, edit, and finish without external calls.

**R02 — Symlinks and path boundaries (A).** The author encountered symlink failures (U1). A legitimate `../` inside the tree differs from a path that escapes the authorized root. Sources: G1, pp. 4, 14, 16, 19; U1. Proposed approach: package real files and use permitted relative references. Proposed check: resolved paths stay within the allowed tree and compile in the official validator.

**R03 — ZIP layout and contents (A).** The package requires `agent.yaml` at its root and should exclude `.pyc`, `.git`, and temporary files. The “text/YAML only” recommendation in G1, p. 30, conflicts with support for scripts and adapters. Sources: G1, pp. 3, 5, 15, 30. Proposed approach: package an explicit file list consistent with the official allowlist. Proposed check: run official validation on the exact submission package.

**R04 — Include directives and YAML syntax (B).** Invalid names, indentation, or include resolution can prevent the agent from building. Sources: G1, pp. 6–8, 12–15, 31. Proposed approach: map each include to its source and final package destination. Proposed check: compile from a clean extraction with all required files inside the package.

**R05 — Tool registration and availability (B).** Examples use varying names, including `subgraph_retrieval` and names from other APIs. Sources: G1, pp. 4, 7, 28. Proposed approach: derive one tool catalog from the actual registry, including names, arguments, return values, and availability. Proposed check: every call resolves to a declared, available tool.

**R06 — Python tool schemas (B).** Gemini attributed failures to default arguments and typing issues. The material contains no reproduction supporting a universal prohibition. Sources: G1, pp. 13, 31. Proposed approach: use official tools and validate the schema of any allowed extension. Proposed check: the harness can interpret actual arguments and errors using the declared conventions.

**R07 — Subagents and control handoff (B).** Delegation alone leaves cooperation, history isolation, and structured return unverified. Sources: G1, pp. 2, 7, 12–13, 17, 20. Proposed approach: make one bounded call to the localizer and return evidence directly. Proposed check: demonstrate inputs, outputs, return to the main agent, and shared budget using the official mechanism.

**R08 — Prompt-based and enforced control (B).** The compiler examined did not receive the callback registry, and skills did not enforce passage through a guard. Sources: A1, §§2, 4–5. Proposed approach: state which limits the harness enforces and which decisions depend on the model. Proposed check: if deterministic control is essential, demonstrate the permitted interface before implementing it.

### 4.2 Context and inference (R09–R15)

**R09 — Accumulation of logs and irrelevant code (E).** Long outputs compete with useful context and may encourage repetition. Sources: G1, pp. 13, 15, 17, 19, 21. Proposed approach: use bounded reads and searches and concise localizer responses. Proposed check: measure input tokens, output volume, and loss of relevant information.

**R10 — Compaction loses tool results (B).** Gemini attributed loops to incomplete event preservation during compaction. Kaggle staff recorded an investigation, with no fix announced in the cited material. Sources: G1, pp. 27, 32; O5. Proposed approach: reduce the need for compaction and retain a short task state. Proposed check: continue after compaction without indefinitely repeating completed searches.

**R11 — Reasoning lost between calls (B+C).** The cited official discussion confirmed an ADK/vLLM incompatibility and announced a wheelhouse fix. Sources: G1, pp. 27–28; O5a. Proposed approach: record inference-stack versions and measure behavior after the fix. Proposed check: observe the path actually served at runtime.

**R12 — Flags that change reasoning mode (B+C).** Hiding reasoning can disable it in some versions. Sources: G1, pp. 6, 9, 17, 27–28. [2, §3.4] records the intentional change to `include_thoughts:false` in `adk_submission` 0.2.13. Proposed approach: distinguish mode activation, generation budget, inclusion in history, and display of the summary. Proposed check: establish propagation and an observable effect for the version used.

**R13 — Reasoning budget and seed fail to propagate (B+C).** Requested parameters may fail to reach the server. The 4,096 tokens suggested by Gemini were an estimate. Sources: G1, p. 27; O5. Proposed approach: calibrate generation within the deadline and check propagation. Proposed check: identify the requested and effective configurations and tokens used. Bit-for-bit reproducibility requires more than setting a seed.

**R14 — Response limit mistaken for task limit (E).** `max_output_tokens: 8192` limits an individual response. Sources: G1, pp. 6, 8, 18. Proposed approach: plan for the sum of calls, input, generation, and tool use. Proposed check: task-level cost estimates account for all responses.

**R15 — Usable context window and response headroom (C).** Loading weights and retaining room for history and generation have different memory requirements. Sources: G1, pp. 10–12, 27. Proposed approach: reserve space for the next response, tool schemas, and resumptions. Proposed check: complete long-context cases under the effective profile with enough headroom for compaction and generation.

### 4.3 Search and editing (R16–R22)

**R16 — Empty or unhelpful semantic search (D).** The material recommends graphs and also reports cases with no benefit. Sources: G1, pp. 1–2, 9, 28. Proposed approach: start with symbols, errors, files, and text search. Proposed check: compare time to the relevant file and resolution with and without the tool.

**R17 — Missing or incompatible graph data (D).** An optional dataset may lack coverage or return an incorrect path. Sources: G1, pp. 1, 4, 28. Proposed approach: handle missing data as a recoverable condition and avoid repeating an empty query. Proposed check: text search works as a fallback without embeddings or graphs.

**R18 — Excessive search output (D).** Large results fill the context window. Sources: G1, pp. 13, 15; O5. Proposed approach: cap results and read only relevant candidates. Proposed check: truncation retains symbol identifiers and leaves usable context.

**R19 — Edit match failure (C+D).** Indentation, spaces, and imprecise excerpts can cause `old_string not found`. Sources: G1, pp. 9, 13–15, 21; G2, §4. Proposed approach: reread the current excerpt, use a short unique anchor, and check the diff. Proposed check: failed edits trigger diagnosis and rereading, with bounded retries.

**R20 — Double encoding of tool results (B+C).** Quotes and line breaks can arrive with duplicate escaping. Kaggle staff announced a fix. Sources: G1, pp. 27, 32; O5. Proposed approach: use a compatible official stack and avoid global unescaping. Proposed check: reads and edits preserve quotes, slashes, and newlines literally.

**R21 — File line endings and encoding (D).** CRLF and LF differences can affect edit matching. Sources: G1, pp. 14–15, 31; G2. Proposed approach: inspect the actual file and avoid normalizing the entire codebase. Proposed check: the diff contains only the intended edit. A newline difference alone leaves cache corruption unestablished.

**R22 — Repeated actions and searches without progress (C+E).** The agent can repeat work without obtaining new evidence. Sources: G1, pp. 2, 13–14, 27–28; G2, §3. Proposed approach: track the hypothesis, recent actions, and the purpose of each query, then stop strategies that return the same evidence. Proposed check: a global limit ends the session and the trace distinguishes productive persistence from a loop.

### 4.4 Models and GPU memory (R23–R30)

**R23 — Mixing model variants (A).** The cited competition rule requires the same variant across agents even when two variants fit in memory. Sources: G1, pp. 4, 12, 20; G1-R1; O3. Proposed approach: use one eligible variant for the root, specialists, and adapters. Proposed check: the package uses a single variant, such as 31B throughout.

**R24 — Model selection by quality labels (E).** The cited claims of “state of the art” and “instant execution” did not include a reproducible benchmark. Sources: G1, pp. 9–12, 16–17, 20. Proposed approach: compare resolution within deadline, tool failures, and total cost. Proposed check: compare on the same tasks, budget, and evaluation stack.

**R25 — Estimates of weight VRAM (E).** Gemini's ranges were 18–22 GB for 31B, 7–9 GB for 12B, 3.5–4.5 GB for E4B, and 2.5–3 GB for E2B. They were estimates and excluded caches, activations, and adapters. Source: G1. Proposed approach: measure effective capacity and account for the distribution of the 96 GB aggregate memory. Proposed check: observe utilization and headroom in the actual service.

**R26 — LoRA reduces available KV cache (C).** Adapters use memory that could otherwise support history and concurrency. Sources: G1, pp. 27–28, 32; O5. Proposed approach: use a reference candidate without LoRA and add an adapter after measuring benefit. Proposed check: preserve context capacity and meet deadlines on long cases.

**R27 — Hangs on long prompts (C).** Long inputs can stall the inference server. Source: G1, p. 27. Proposed approach: bound context and generation, define session termination, and record the last operation. Proposed check: inference failure produces a recognizable outcome and the batch continues. R65 documents a specific mechanism. Reduced logging alone leaves server liveness unverified.

**R28 — Adapter discovery and identity (A+C).** The directory name, YAML reference, PEFT configuration, and adapter base need to match. Source: G1, p. 29. Proposed approach: check the complete identity and isolate the adapter-free path first. Proposed check: loading is confirmed and adapter weights affect execution.

**R29 — Number and rank of adapters (E).** More adapters and higher ranks increase memory reservations, cost, and failure modes. Sources: G1, pp. 28, 30. Proposed approach: defer multiple adapters and fine-tuning. Proposed check: demonstrate a real-task gain that pays for the added cost within budget.

**R30 — Assumed parallelism (E).** Four GPUs alone do not establish support for four concurrent tasks. The sources also warn about `ParallelAgent`. Sources: G1; O3. Proposed approach: execute tasks sequentially with one writer. Proposed check: demonstrate platform support and a total-time benefit before using concurrency.

### 4.5 Python and offline dependencies (R31–R35)

**R31 — Unavailable dependencies (A).** Offline execution prevents online installation of missing libraries. The evaluated repository and the agent helpers have separate dependency inventories. Sources: G1, pp. 26, 31; G2, §1. Proposed approach: prefer the standard library and official resources. Proposed check: resolve dependencies at both layers offline.

**R32 — Incompatible binary wheels (A).** A `.whl` file may be incompatible with Python, the ABI, Linux, the architecture, or native libraries. Source: G2, §1. Proposed approach: record these dependencies and coordinate upgrades to core packages. Proposed check: import and use the package in the target environment with the manifest versions.

**R33 — Interpreter and virtual-environment mismatch (A).** `python` and `pytest` on `PATH` can point to different environments. The historical public image used Python 3.13 with shims for older modules. Sources: G2, §1; O4. Proposed approach: invoke the interpreter provided for the task. Proposed check: commands and tests use the intended environment.

**R34 — Vendoring and installation before harness startup (A).** `vendor/`, private datasets, and `pip --no-index` depend on the actual contract. Source: G2. Proposed approach: demonstrate mounts, imports, transitive dependencies, and licenses, and check whether files transfer from the notebook to the sandbox. Proposed check: the scorer can access the dependency through an allowed path.

**R35 — Mixing platform versions (A).** Uncoordinated updates introduce incompatibilities. Sources: G1, pp. 28, 31; A1, §§6, 8. Proposed approach: record a coherent official dataset, wheels, and hashes. Proposed check: verify needed fixes in that stack before changing core libraries.

### 4.6 Sandbox processes and resources (R36–R40)

**R36 — Commands exceed remaining time (A+D).** A command timeout longer than the remaining session time leaves the batch exposed. Sources: G1, pp. 13–14; G2, §2. Proposed approach: cap each command by the remaining session time and reserve time to finalize. Proposed check: interrupt a slow command cleanly and still capture the patch.

**R37 — Orphaned descendants and incomplete cancellation (D).** Python timeouts, asynchronous cancellation, and termination of descendant processes have different effects. Sources: G2, §2; A1, §§2, 5, 8. Proposed approach: avoid background work and use native supervision. Proposed check: observe process termination and result persistence.

**R38 — System limits and isolation (D).** The sources mention namespaces, seccomp, and AppArmor without a concrete configuration. Source: G2. Proposed approach: check limits on processes, memory, disk, and permissions under the actual contract. Proposed check: run helpers with available privileges and diagnose failures before attributing them to isolation.

**R39 — Accumulation of disk files and logs (D).** Temporary files and captures grow during a batch. Sources: G2, §2; G1, p. 31. Proposed approach: limit captures and temporary files and preserve minimum evidence before cleanup. Proposed check: resource usage is bounded. The last 100–200 lines may omit the original failure.

**R40 — Host and GPU memory (A+C).** Large stdout, container RAM, and KV cache are separate resource constraints. Sources: G1, pp. 27, 31; G2, §4. Proposed approach: budget each resource separately. Proposed check: record which resource ran out.

### 4.7 Patches and verification (R41–R46)

**R41 — Destructive cleanup (E).** `git clean -fd` and `git checkout .` can remove new files and candidate changes. Sources: G2, §§2–3. Proposed approach: avoid global reset as a default fallback. Proposed check: valid candidates and required new files survive cleanup.

**R42 — Empty or uncaptured patch (D).** The final model message and the extracted artifact are distinct. Untracked files may be missing from the diff. Sources: G1, pp. 3, 14, 19; A1, §2. Proposed approach: use official extraction and inspect included paths. Proposed check: the persisted patch represents the intended state, including new files.

**R43 — Long tests or tests in the wrong environment (D+E).** Long tests consume time. A run that collects no cases leaves the patch unverified. Sources: G1, pp. 6–7, 15; G2, §3. Proposed approach: use relevant tests in a known environment with a time budget. Proposed check: record the command, result, and relationship to the current patch.

**R44 — Local pass mistaken for official resolution (D).** Patch production, local testing, clean application, and the official verdict are distinct states. Tests requested by the agent consume generation time. Sources: G1, p. 14; A1, §§2, 7; O1. [2, §3.12] describes the verifier's use of tests from `test_patch`, which defines the scope of a resolution. Proposed check: record each state and require an explicit pass.

**R45 — Persistence and loss of evidence (D).** The `evaluate_task` path examined did not add the persistence provided by `Evaluator.run`. Cleanup could remove artifacts such as JUnit results. Source: A1, §5. Proposed approach: identify the actual write and collect artifacts at the right time. Proposed check: the result, patch, and minimum diagnostics survive cleanup.

**R46 — Mocks and simulations mistaken for real-model results (E).** Historical tests and contract checks establish different properties from a Gemma resolution rate. Source: A1, §§3, 9. Proposed check: label evidence from simulations, substitute models, the official model, and the competition evaluation.

### 4.8 Kaggle operations and interpretation (R47–R50)

**R47 — Long queues and quota consumption (A).** Reported waits ranged from 15 to 30 hours, and some reports described blocked resubmission. The cited material describes a higher consumption rate for L4x4 quota. Sources: G1, pp. 28–30; O1. Proposed approach: leave schedule margin and check static package errors before submission. Proposed check: record waiting time, execution time, and quota charged separately.

**R48 — Opaque errors and inconsistent UI state (A).** The sources describe `Kaggle Error`, exceptions without a trace, and notebooks shown as active after backend termination. Sources: G1, pp. 29–30. Proposed approach: retain submission IDs, timestamps, and logs and distinguish queue, configuration, inference, and test issues. Proposed check: use a diagnosis before changing the agent.

**R49 — Local speed without scorer parity (A+E).** Reported RTX 4090/A100 latency of 3.8–8.7 seconds per call lacks a reproducible protocol. Sources: G1, pp. 28–29. Proposed approach: treat these figures as reports and allow for latency variation. Proposed check: measure the effective stack on the target environment.

**R50 — Global limit and termination policy (A).** The 12-hour limit makes timely artifact production a planning concern. The claim that any timeout zeroes the submission was unverified. Sources: G1, pp. 1–4, 9, 14, 19, 30; G2; O1. Proposed approach: finalize deliverable artifacts early. Proposed check: document timeout and capture behavior for the chosen version.

### 4.9 Risks derived from Gemma documentation (R51–R64)

These entries come from G4 and B2 and B11–B14 in [1, §5.9]. They describe integration, protocol, export, and multi-token prediction (MTP) risks identified from the documentation.

| ID | Risk | Proposed check |
|---|---|---|
| R51 | Confusing weight memory with peak runtime memory | Include the KV cache, buffers, adapters, and headroom in sizing |
| R52 | Inferring memory use solely from effective or active parameters | Distinguish total parameters, active parameters, and the checkpoint format |
| R53 | Applying GGUF, Q4_0, or mobile assumptions to W4A16-CT | Match the artifact and loader to the eligible variant and server version |
| R54 | Mixing Gemma 3 and 4 templates, tokens, or tokenizers | Inspect serialization and check for duplicated BOS tokens or templates |
| R55 | Removing needed context within a tool turn | Document and verify event boundaries and history policy |
| R56 | Treating a concision instruction as a timeout or reasoning limit | Identify enforceable limits and label prompt guidance as behavioral |
| R57 | Assuming a tool exists because its name appears in YAML | Match the effective registry and schema to calls and results |
| R58 | Copying sampling parameters without confirming they are applied | Record the effective configuration and cost for each comparison |
| R59 | Producing LoRA in a scorer-incompatible format | Confirm export, architecture, and loading compatibility before training |
| R60 | Applying online, JAX, or TPU assumptions to the sandbox | Use an offline resource matrix that distinguishes environments and versions |
| R61 | Depending on MTP without confirmed support or benefit | Establish artifacts, eligibility, support, and net cost |
| R62 | Accepting a tool result under the wrong interpretation | Check the evidence against the hypothesis, operation, and repository state |
| R63 | Using a general benchmark to predict issue resolution | Evaluate the full workflow and deadline under the relevant protocol |
| R64 | Using a qualitative sample or incomplete example to validate training | Show benefit and a complete export path before extrapolating from demonstrations |

### 4.10 Environment risks from the official forum (R65–R72, proposed)

The November 4 analysis reviewed about 40 forum topics and compared them with V11R6 and wheelhouse v08, which included vLLM 0.19.1, swegemma 0.2.11, `adk_submission` 0.2.13, and google-adk 1.36.1. The analysis treated participant accounts as reports and used code inspection or reproduction to establish findings for the project [2, §1]. The status table preserves the November 4 assessment and the V12 round 2 update from November 6.

**R65 — vLLM 0.19.1 parser stalls on a malformed array (C).** An array element without the `<|"|>` delimiter that contains `]`, as in `args:["Fix list[str] handling"]`, can make `_parse_gemma4_array` stop advancing. The loop runs on the server event loop and can block later work. The historical analysis identifies vLLM 0.21.0 as the first upstream version with the fix. Topics 746336, 753973, and 745138. On November 4, three inputs failed to return within five seconds under vLLM 0.19.1. `gemma4_parser_compat` returned `MALFORMED_GEMMA4_ARGUMENT_NO_PROGRESS` for all three. [Frozen parser receipt](https://github.com/aridiosilva/Gemma4_Google_Deepmind_S1/blob/433e7508f713d947b417d8522bc84b96eae1da45/evidence/parser-forum-receipt.json)

**R66 — JSON string quotes retained in the parsed value (C).** `skill_name:"my-skill"` can become `"\"my-skill\""`. A path with the extra quotes can point to a nonexistent file, consume calls, and contribute to R22. Topic 745138 cites vllm#51284 and vllm#51307. A local test confirmed the behavior [2, §3.2].

**R67 — Backtick-terminated strings cause missing `edit_file` arguments (C).** Gemma 4 31B can close a string with a backtick. The parser then combines arguments, and `old_string` or `new_string` can be lost. A participant reported 107 failures in 246 `edit_file` calls (43%). Topics 747923, 744272, and 745003. In these cases, serialization is a candidate cause of what might otherwise be classified as a P failure [2, §3.3].

**R68 — Test reset fails before applying `test_patch` (D).** `git checkout` could abort on a missing pathspec. A test edited by the agent could then make `test_patch` fail even when the repair was correct. Topic 744825. The reviewed swegemma 0.2.11 uses `git ls-tree … | xargs git checkout`. The risk records the potential for silent false negatives if the reset regresses [2, §3.6].

**R69 — Network-sensitive tests behave differently offline (D).** Topic 754586 reported that eight `requests` tasks failed with the reference patch when a test expecting a timeout instead received `Network is unreachable`. The 33-task sample included `requests_7433` and `requests_7502`. Both passed local reference-patch rehearsals with network access. Strict network isolation remains untested in those rehearsals. [Local checks](https://github.com/aridiosilva/Gemma4_Google_Deepmind_S1/blob/433e7508f713d947b417d8522bc84b96eae1da45/evidence/ref-11.md)

**Later Kaggle evidence for R69.** Both tasks were resolved in the Kaggle records through November 11. Joining SHA-256 hashes of their task IDs to the public inventory gives `requests_7433` → H31 and `requests_7502` → H33. H31 was unresolved in R4 and resolved in R5. H33 was resolved in R4. These verdicts describe the recorded Kaggle runs. [Inventory](https://github.com/aridiosilva/Gemma4_Google_Deepmind_S1/blob/433e7508f713d947b417d8522bc84b96eae1da45/evidence/kaggle-bugs-2026-11-11/inventory.csv) · [Execution records](https://github.com/aridiosilva/Gemma4_Google_Deepmind_S1/blob/433e7508f713d947b417d8522bc84b96eae1da45/evidence/kaggle-bugs-2026-11-11/executions.jsonl)

**R70 — Mutually exclusive skip conditions make a profile unsatisfiable (D).** A fixed public profile cannot accept a patch when two mandatory tests require mutually exclusive dependency versions. Topics 754586, 751487, and 755554, the last opened by the project for task 16. The `fastapi_14186` diagnostic records the conflicting Pydantic conditions and the verifier verdict. [Frozen diagnostic](https://github.com/aridiosilva/Gemma4_Google_Deepmind_S1/blob/433e7508f713d947b417d8522bc84b96eae1da45/evidence/ref-09.md)

**R71 — Verifier conventions can reject valid repairs (D).** The forum account lists `-p no:anyio`, replacement of `pytest.ini`, data `.py` files treated as targets, and JUnit output above 10 MiB. Topic 751707. `offline-test-wheels` covered the other test dependency issues reported in the same group [2, §3.10].

**R72 — Harness-generated prompts can mislead the model (D).** The reported `find … | head -150` tree omitted part of the source in 115 of 129 tasks. `read_file` was limited to 150 lines, and 18 of 129 task descriptions contained only a title and a link that could not be opened offline. Topics 745220, 755291, and 746944. P receives this harness text as supplied [2, §3.11].

| ID | November 4 status [2] | V12 round 2 update, November 6 [3] |
|---|---|---|
| R65 | The compatibility layer mitigated the reproduced trigger. A parser error could still stop the batch | The `gemma4` parsers handled the 18 responses in that round. The run did not exercise the malformed inputs |
| R66 | Open after offline diagnosis | No record in [3] |
| R67 | Open, with an offline subclass proposed | The report associates double escaping in `old_string` in three of four `edit_file` calls with R20/R67. All three edits succeeded via the tool's `unescaped` strategy |
| R68 | Mitigation in swegemma 0.2.11 | No record in [3] |
| R69 | Open for `requests_7433` and `requests_7502` | This round did not reach these tasks |
| R70 | Task 16 deferred by the author | No record in [3] |
| R71 | Latent, with no case in the sample | No record in [3] |
| R72 | Interpreted from the harness input | Observed in a task with the text “Fix ZWJ and edge cases” and two links. The agent recorded that it could not open the links |

### 4.11 Resource and harness occurrences (W01–W25)

The resource audit [4] examined original sources for 34 priority components in the harness, server, and direct dependencies, as well as local wheel metadata and code at P's key interfaces. The wheel manifest contains 246 entries. The audit covered the priority components and issues documented in [4]. W23–W25 were added from the V11R2, V11R3, and V11R4 runs [4; 1, §26.5].

The evidence levels follow [1, §26.2]: report, inspection, local reproduction, integration, and Kaggle. A local reproduction here used pinned bytes in a synthetic probe without a GPU or a scientific task. These probes establish the observed behavior under their stated conditions.

| W | Component and version | Defect | Evidence | R classes | Status and mitigation |
|---|---|---|---|---|---|
| W01 | vLLM 0.19.1 (`gemma4` parser) | Malformed input stops parser progress and can hang the server | Local reproduction: 4 of 7 inputs made no progress | R06, R20, R22, R27, R35, R37, R44, R48, R62 | Release blocker in [1, §26.1]. The project proposal rejects malformed input. Upstream PR 41991 addresses this class of defects. See R65 for the later three-case check |
| W02 | adk-submission 0.2.13 / ADK / vLLM | Reasoning lost between calls | Kaggle staff confirmation, bridge present in the wheel, and six isolated probes | R11–R13, R20, R35 | P runs with reasoning disabled. Recheck serialization if that path changes |
| W03 | swegemma 0.2.11 / test environment | Test dependencies absent in the sandbox | Forum reports | R31–R35, R43, R44 | Check dependencies for each snapshot under the effective interpreter. Classify setup errors separately |
| W04 | swegemma 0.2.11 | Tests can import the installed wheel in place of the edited repository, producing a false pass through shadowing | Report | R19, R33–R35, R44, R62 | Check the origin of the tested module. Occurrence in P's runtime remained unverified |
| W05 | Wheels in general | Same version, different content | Hash inspection | R32, R35, R44 | Record SHA-256 of the wheel and loaded file. The scorer's exact bytes remained unverified |
| W06 | google-adk 1.36.1 | `ParallelAgent` and compaction | Official ADK issue 7324 | R10–R15, R35 | Conditional. P is sequential, and adk-submission requires ADK below 2 |
| W07 | FastAPI 0.141.1 / Starlette 0.52.1 / prometheus-fastapi-instrumentator 7.1.0 | `AttributeError` in metrics routing. P's backport left incorrect labels in two of three cases | Local reproduction | R32, R35, R48, R62 | The `root_path` proposal passed all three cases and had yet to be integrated. The incorrect labels affect observation of results |
| W08 | requests 2.34.2 | `NameError` during type introspection, issue 7456 | Reproduced in four classes | R06, R35, R48 | Applicability to P's functions remained unverified. The audit discouraged a global monkey patch |
| W09 | pydantic 2.14.1 / pydantic-core 2.50.1 | Validation ignores a field under the wrong name, accepts an extra key, or overwrites a TypedDict alias | Three behaviors reproduced | R06, R20, R35, R62 | Map the schema and API before changing them. Coordinate and test upgrades. Maintainer notices cite release 2.14.2 |
| W10 | torch 2.10.0+cu128 / transformers 5.13.1 / triton 3.6.0 | cuBLAS and SDPA errors | Reports with matching versions | R26, R27, R32, R35 | Conditional. Record loaded libraries and kernel errors on the target |
| W11 | grpcio 1.84.0 | Garbage collection fails to cancel an aio call | Report | R27, R37, R48 | Conditional. P uses local HTTP |
| W12 | uvicorn 0.54.0 | Reset during shutdown with worker recycling | Report | R27, R37, R48 | Conditional. The audit did not treat this as grounds for a scientific rerun |
| W13 | pyyaml 6.0.3 | Reentrant CDumper can segfault | Report | R06, R32, R48 | The audit found no matching precondition in P |
| W14 | litellm 1.85.7 | Reasoning serialization with Groq and streaming | Report | R11–R13, R20, R35 | Applies to a different provider. A global removal of reasoning fields was outside the proposed mitigation |
| W15 | httpx 0.28.1 | Removed `proxies=` argument | Local reproduction: argument rejected | R32, R35, R48 | The audit found no consumer in P |
| W16 | Local Windows and Linux environments | Different versions of Pydantic, LiteLLM, the OpenAI SDK, and the instrumentator | Local measurement | R32, R33, R35, R44 | Development-environment difference. Linux probes use the pinned wheels |
| W17 | httpx2 2.15.1 | Cookie policy fixed in a later version | Fix report | R20, R35, R62 | Use by P remained unverified |
| W18 | swegemma 0.2.11 (`verification.py`) | Permissive JUnit matching accepts a different module, a similar function prefix, or a different parameter | Local reproduction: 3 false accepts in 9 cases | R44, R62 | Release blocker in [1, §26.3]. At the time of the audit, P's evaluator used the helper, and strict matching was proposed. The evidence is synthetic |
| W19 | LoRA in vLLM | Adapter and CUDA graph memory | Reports and staff guidance | R26–R29, R35, R62 | Conditional. P uses 31B without LoRA |
| W20 | 12B variant | Loading the 12B model | Staff fix announcement | R32, R35, R48 | Conditional. P uses 31B |
| W21 | Graph tools | Revisions to graph searches | Reports | R16–R18, R35 | Conditional. P runs without these tools |
| W22 | P harness (`audited_runtime.py`) | `_close_async_generator` suppresses the close exception | Reproduced in three probes | R37, R48, R62 | Project harness issue. Mitigation was specified and remained pending implementation |
| W23 | P harness (V11R2 guard) | Isolated policy import failed before sandbox setup | Confirmed on Kaggle and reproduced locally | R33, R35, R37, R44, R48, R62 | Project harness issue. V11R3 used an explicit path to fix it. The affected run evaluated zero tasks |
| W24 | swegemma 0.2.11 and P's classifier | P's classifier rejected swegemma's `rm -f /tmp/setup.py` | Confirmed in V11R3 | R33, R35, R37, R44, R48, R62 | Interaction between the resource and a project guard. V11R4 recognizes that exact command. The V11R3 authorization was used and the run was not retried |
| W25 | P comparator and pytest collection | The manifest identity `tests/test_cells.py::…` differs from the collected `test_cells.py::…` | Confirmed by artifacts and an isolated reproduction | R35, R44, R62 | Project harness issue. The upstream verdict remained `resolved=false`. A correction and integrated test were pending |

W01 and W18 were the resource-related blockers recorded for scientific release. The parser can stall, and the comparator can accept the result of a different test from the one required [1, §§26.1, 26.3]. The November 2 gate recorded the release decision as documentation. The integration status of these blockers in V11R6, V12, and V12R1 was outside that consolidation. W16, W22, W23, and W25 concern the project or its local environment. W24 concerns the interaction between a resource and a project guard. [Resource audit extract](https://github.com/aridiosilva/Gemma4_Google_Deepmind_S1/blob/433e7508f713d947b417d8522bc84b96eae1da45/evidence/ref-10.md) · [JUnit receipt](https://github.com/aridiosilva/Gemma4_Google_Deepmind_S1/blob/433e7508f713d947b417d8522bc84b96eae1da45/evidence/w18-synthetic-receipt.json) · [Release gate](https://github.com/aridiosilva/Gemma4_Google_Deepmind_S1/blob/433e7508f713d947b417d8522bc84b96eae1da45/evidence/release-gate.json)

The same audit records 13 changes, E01–E13, applied to the V10 controls. Those changes concern the project's own harness [4].

**Participant reports reviewed October 27, 2026.** [1, §24.1] maps these reports to existing classes: about 5.5 minutes per task (`12 h / 129 = 5.58 min`) as a planning average (R36, R43, R49, R50); validation waits above 48 hours (R47, R48); higher L4x4 quota consumption than T4x2 or P100 (R47); missing `dirty_equals`, `inline_snapshot`, or `pytest` (R31–R35, R43); `error (exit 0)` at budget exhaustion (R44, R62); an announced adapter without applied LoRA weights (R28, R35, R59, R62); and changes to generation or reasoning visibility through `include_thoughts` (R11–R13, R35, R58).

**Open issues from attempt 11 on October 27, 2026.** [1, §25.2] records `GeneratorExit` mapped to `MODEL_REQUEST_FAILED_WITHOUT_AUDITABLE_USAGE` (R44, R62), a mismatch between the internal cleanup state `VLLM_PROCESS_GROUP_NOT_GONE` and the external supervisor's record of process-tree termination and an idle GPU (R37), and `FileExistsError` on reentry (R39, R45). The review at that date found no official patch confirmation for `GeneratorExit` or the cleanup mismatch.

## 5 Source locations

| Range | Source and location | Public evidence where available |
|---|---|---|
| R01–R50 | Architecture analysis [1], §§5.1–5.8 | Competition references [5–9] |
| R51–R64 | Architecture analysis [1], §5.9 | Documentation keys listed in Section 2 |
| October 27 reports and attempt 11 | Architecture analysis [1], §§24.1 and 25.2 | Historical observations summarized in Section 4.11 |
| W01–W25, primary sources, hashes, and receipts | Resource audit [4] and architecture analysis [1], §26 | [Resource audit extract](https://github.com/aridiosilva/Gemma4_Google_Deepmind_S1/blob/433e7508f713d947b417d8522bc84b96eae1da45/evidence/ref-10.md) |
| R65–R72 | Forum analysis [2], §§3–4 | [Forum-informed checks](https://github.com/aridiosilva/Gemma4_Google_Deepmind_S1/blob/433e7508f713d947b417d8522bc84b96eae1da45/evidence/ref-11.md) |
| V12 round 2 | Round report [3] | [V12 and V12R1 evidence extract](https://github.com/aridiosilva/Gemma4_Google_Deepmind_S1/blob/433e7508f713d947b417d8522bc84b96eae1da45/evidence/ref-12.md) |

The historical catalog used the November 6 working revision of the architecture analysis. The frozen receipts above provide public sources for the observations they cover.

## 6 Scope of the evidence

The November 6 consolidation collated existing descriptions and evidence statuses. Reproductions and run observations are attributed to the relevant records. The English edition adds the later R69 outcomes from the frozen Kaggle inventory and execution records. The November 6 status table is retained as a dated record.

The resource audit records proposed mitigations for W01, W07, W18, W22, and W25. Integration in V11R6, V12, or V12R1 requires separate evidence. R01–R50 are condensed descriptions, and the categories reflect the compiler's interpretation of the sources. The summary assigns category E alone to 13 items (R09, R14, R24, R25, R29, R30, R41, R46, R51, R52, R56, R63, R64) and assigns E with another category to four (R22, R43, R49, R62). The other 55 have an external origin under A, B, C, or D. Counting each mixed entry in all of its categories gives 18 in A, 12 in B, 19 in C, and 18 in D.

The R65–R72 extension and reconciliation of R65 with W01 remain proposed changes to the canonical catalog.

## References

[1] Silva, Aridio. *Gemma 4 Challenge Constraints and Proposed Architecture Revision*. October 19, 2026. Reported update November 2, 2026. Historical architecture catalog, §§5, 24.1, 25, and 26 consulted November 6.

[2] Silva, Aridio. *Competition Environment Issues Reported in the Forum: Impact on V11R6 and Proposed R65–R74*. November 4, 2026. Historical analysis consulted November 6. [Public extract](https://github.com/aridiosilva/Gemma4_Google_Deepmind_S1/blob/433e7508f713d947b417d8522bc84b96eae1da45/evidence/ref-11.md)

[3] Silva, Aridio. *V12 Round 2 Report*. November 6, 2026. [Public extract](https://github.com/aridiosilva/Gemma4_Google_Deepmind_S1/blob/433e7508f713d947b417d8522bc84b96eae1da45/evidence/ref-12.md)

[4] Silva, Aridio. *Known Resource and Harness Bugs in Policy P*. November 2, 2026, including W23–W25 addenda. Working revision consulted November 6. [Public extract](https://github.com/aridiosilva/Gemma4_Google_Deepmind_S1/blob/433e7508f713d947b417d8522bc84b96eae1da45/evidence/ref-10.md)

[5] Kaggle. [Gemma 4 Developer Agent Competition overview](https://www.kaggle.com/competitions/gemma-4-developer-agent/overview).

[6] Holbrook, Ryan (Kaggle staff). [New Gemma 4 Models Available 12B, E4B, and E2B](https://www.kaggle.com/competitions/gemma-4-developer-agent/discussion/748287).

[7] Holbrook, Ryan. [Getting Started with the Gemma 4 Developer Agent Competition, input data](https://www.kaggle.com/code/ryanholbrook/getting-started-gemma-4-developer-agent/input).

[8] Holbrook, Ryan. [Kaggle discussion comments](https://www.kaggle.com/ryanholbrook/discussion). Mutable index.

[9] Kaggle. [Discussion of reasoning lost between calls](https://www.kaggle.com/competitions/gemma-4-developer-agent/discussion/744354).

The external URLs in [5–9] are carried over from the sources of the Portuguese report. This catalog is supporting evidence for the paper.
