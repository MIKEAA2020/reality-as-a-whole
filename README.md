# reality-as-a-whole

Working record of a project that asks whether a complete, "zero-residue" account of reality as a whole — one that leaves no brute fact — can be constructed, and what remains when the attempt is pushed as far as it will go. The material consists of audited chat transcripts, constructive research rounds with reproducible checks, and formal work packages. Nothing here claims to have reached zero residue; the recurring result is a shrinking, explicitly named residue.

## Start here

**[`Surviving_Thesis_Consolidated.md`](Surviving_Thesis_Consolidated.md)** — the project's position stated at full strength and consolidated from everything below: the thesis, the criteria in their final defensible forms, the architecture, the best argument for each component, objections and replies, standing exclusions, the typed residue, the improvement programme with success/failure conditions, the stability profile of each component across all passes, and a graded claims register. It is written to be read on its own; the material below is its evidence base.

## Contents

### 1. `workspace-01a16ed6-0438-7924-a01c-89f6870cc3b0.zip` — first chat audit and research rounds 1–6

| File | What it is |
|---|---|
| `uploads/DeepSeek_Zero-Residue-Simulation_20261024-0340.txt` | First transcript (24 Oct 2026): from Bostrom's simulation argument to a "zero-residue" necessitarian simulation hypothesis. |
| `Zero_Residue_Chat_Audit.md` | Audit of that transcript: criterion-by-criterion review, correction ledger, steelman, obligations. Verdict: a research programme, not a zero-residue account. |
| `Zero_Residue_Constructive_Research_v1.md` … `Zero_Residue_Research_v6.md` | Six constructive rounds building the lead candidate (an immanent constitutive architecture `C → Π, Σ, Q`): existence bridge (v1), factorization and subjecthood (v2–v3), quantum structure from self-presentation assumptions (v4–v5), and the residue ledger with the Actualization, Calibration and Outcome-Selection gaps and the essence trilemma (v6). |
| `zero_residue_research/` | Standard-library Python checks and results for each round. |

### 2. `workspace-01a169a5-eb9f-79d3-ac53-729ac277254b.zip` — realization tokens, WP1–WP4

| File | What it is |
|---|---|
| `realization_tokens/WP1_*.md`, `WP2_*.md`, `WP3_*.md`, `WP4_*.md` | Formal work packages on whether subject boundaries, interfaces and realization counts can be derived from causal structure alone. Results: no universal unique decomposition from bare dynamics (WP1); interfaces recoverable only conditional on a stronger structural goal (WP2); operational equivalence yields a canonical type, not a realization population (WP3); principled suspension rather than a forced point answer (WP4). |
| `realization_tokens/*.py`, `test_*.py`, `*.csv`, `*_results.txt` | Modules, tests, assumption ledgers and result tables for the work packages. |

### 3. `chat_audit_2_criteria_filter/` — second chat audit (6 Nov 2026)

| File | What it is |
|---|---|
| `uploads/DeepSeek_Experience-and-non-optimal-world_20261106-2010.txt` | Second transcript: a six-criterion filter (experience as datum; not the best possible world; full intelligibility; generativity; alignment with physics; alignment with consciousness science) applied to whole-reality accounts, ending in "DPMRS-R" and a "DPMRS-R Simulation Hypothesis" claimed to be zero-residue. |
| `Zero_Residue_Chat_Audit_2.md` | Audit of that transcript, read turn-by-turn against the criteria in force at each turn and against the prior rounds: criterion-evolution ledger, 30-row turn table, findings, source audit, mapping of the new proposal onto the existing architecture, correction ledger, steelman, obligations. Verdict: a sharper filter and a cleaner two-tier programme; the zero-residue claim is not earned, by the chat's own earlier standards. |
| `checks/audit2_checks.py` → `audit2_results.json`, `audit2_run.log` | Reproducible checks (Python 3, standard library): Leibniz modus tollens and the vacuity of "best possible world" under necessitarianism; one-world modal collapse; underdetermination of an "integration + richness" boundary functional on a toy system (nine monotone functionals, three distinct winners, a three-member Pareto front, no admissible weighted sum for one candidate); privation orderings inheriting that underdetermination. |

## Running the checks

```bash
# second audit
python3 chat_audit_2_criteria_filter/checks/audit2_checks.py

# earlier rounds (after extracting the first archive)
unzip -q workspace-01a16ed6-0438-7924-a01c-89f6870cc3b0.zip -d prior
python3 prior/zero_residue_research/round6_checks.py
```

All checks use only the Python standard library.

## Status of the project's main claims

- Experience is treated as a datum; eliminativism is excluded throughout.
- The lead candidate is a two-tier structural–experiential monism; its subject-selection rule, actualization bridge, calibration and outcome selection remain open obligations.
- Two chats have claimed zero residue; two audits have found the claim unsupported and recorded what would be needed to support it.

## License

MIT — see `LICENSE`.
