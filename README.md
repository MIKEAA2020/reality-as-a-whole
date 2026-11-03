# Reality as a Whole

An evolving research repository investigating a unified, fully intelligible account of physical reality, experience, and their constitution.

**Status:** working conjectures, contextual thesis audits, mathematical constructions, and explicitly bounded verification. This repository does not claim a completed theory of consciousness, an established physical–phenomenal identity law, or a solution to ultimate actuality. Passing software checks verifies the specified constructions, not their phenomenal interpretation.

## Start here

- [Necessary articulated unity](NECESSARY_ARTICULATED_UNITY.md): active constitutive proposal for qualities, finite perspectives, and their relations; fixed simplicity, privative absence, and the no-independent-selector requirement.

- [Complete awareness and finite disclosure](COMPLETE_AWARENESS_FINITE_DISCLOSURE.md): active nonproductive candidate, worked local-awareness case, finite logical witness, and perfection–privation stress test.

- [Perspective, plenitude, and one complete actuality](SIMULATION_PLENITUDE_CONSOLIDATION.md): finite disclosure without a simulator, creation, or execution; literal simulation models are separate conditional comparisons.

- [Six-criterion physics/consciousness integration](SIX_CRITERIA_PHYSICS_CONSCIOUSNESS_AUDIT.md): the updated C5–C6 requirements, candidate roles, invalid identity shortcuts, and integration tests within the existing programme.

- [Governing absolute-constitution framework and implementation plan](ABSOLUTE_CONSTITUTION_FRAMEWORK.md): strongest joint requirements, consolidated positive account, and parallel foundational, physical, phenomenal, and evaluative workstreams.

- [Cumulative synthesis](SYNTHESIS.md): consolidated surviving account and its qualifications.
- [Integrated account](INTEGRATED_ACCOUNT.md): relationships among the physical, mathematical, and constitutive projects.
- [Unified constitution map](UNIFIED_CONSTITUTION_MAP.md): how the phenomenal law must fit AQFT, quantum information, geometry, contextual methods, and effective scales.
- [Leading conjectural whole-account](CONJECTURAL_WHOLE_ACCOUNT.md): positive comparative assessment, distinguished from proof status.
- [Complete constitution research programme](CONSTITUTION_RESEARCH_PROGRAMME.md): the Gamma–chi target and criteria for genuine progress.

The governing framework contains the joint argument, dependency ledger, operational W1–W6 work register, and five completion gates. `SYNTHESIS.md` consolidates the surviving thesis; `CONSTITUTION_RESEARCH_PROGRAMME.md` specifies the local research milestones; the atlas and unified map supply cross-framework constraints. These are complementary views of one programme, not separate ontological proposals.

## Current physical–phenomenal work

- [Observation identifiability](DISCLOSURE_OBSERVATION_IDENTIFIABILITY.md): the reliability bounds needed to distinguish frozen experiential predictions, with exact rational checks and no claimed empirical calibration.

- [Frozen maintained-disclosure contrast](MAINTAINED_DISCLOSURE_CANDIDATE.md): H_M1/H_D1, independent premises, a one-slot worked case, rejection conditions, and an executable preservation/observation audit.

- [SR-inspired geometry construction](research/constitutive_geometry/REPORT.md): explicit response geometry, transformations, measurement conditions, and limitations.
- [Workspace togetherness candidate](WORKSPACE_TOGETHERNESS_CANDIDATE.md): a local hypothesis and primary protocol assessment, not a completed episode law.
- [Maintenance versus broadcast](MAINTENANCE_BROADCAST_SEPARATION.md): a controlled intervention comparison and the limits of trajectory replay.
- [Neural timing audit](NEURAL_TIMING_CONSTITUTION_AUDIT.md): source-code assessment distinguishing an analysis-derived duration from an intrinsic episode clock.
- [Realized-process candidate](REALIZED_PROCESS_CANDIDATE.md), [episode incidence](EPISODE_INCIDENCE_REFORMULATION.md), and [qualitative equivalence](QUALITATIVE_EQUIVALENCE_AUDIT.md).

## Axiology and ultimate explanation

- [Consolidated axiological assessment](AXIOLOGY_STATUS.md).
- [Privation and the Good](PRIVATION_AND_AXIARCHIC_GOOD.md).
- [Constitutive-value development](CONSTITUTIVE_VALUE_PRINCIPLE.md).
- [Axiarchic bridge audit](AXIARCHIC_BRIDGE_AUDIT.md) and [necessary occurrence](NECESSARY_OCCURRENCE_CANDIDATE.md).

## Sources and verification

- `sources/uploads/` preserves supplied discussion transcripts for the contextual audits; these are not newly collected scientific observations.
- `sources/external/` contains selected pinned primary documentation/code snapshots and provenance manifests. Third-party materials retain their own authorship and applicable terms; see the preserved license where supplied. The root license does not override third-party rights.
- `research/` contains independent finite constructions, reports, tests, diagnostic JSON, and small execution logs.
- `verification/` contains provenance records, additional checks, and historical rerun evidence. Some historical records refer to separately supplied archives; those archives are not included here.

The COGITATE source assessments are static audits. No participant recordings were downloaded or analyzed, and no published neural result was reproduced.

## Run the checks

The core research runner uses the Python standard library and runs each folder independently to avoid collisions among the local `model.py` modules:

```bash
python research/run_checks.py
```

At the current checkpoint: **1,149 tests pass across 43 folders**. The runner refreshes the retained `results.log` files and `research/check_results.json`.

Additional independent checks:

```bash
python verification/integration_overlap.py
python verification/cogitate_analysis_audit.py
python verification/workspace_intervention_audit.py
```

The COGITATE audit verifies pinned source hashes and selected static/code-semantic witnesses; it does not execute the third-party neural pipeline. The workspace audit checks reduced transition equivalence and replay counterexamples in the existing software model. These checks are separate from the 1,149-test count.

`verification/constitutive_checks.py` additionally requires SymPy and can be run separately in an environment where that dependency is installed.

Bytecode, local environments, secrets files, and editor caches are excluded by `.gitignore`. Small test logs and diagnostic outputs are intentionally retained as evidence; large raw datasets and participant recordings are not part of this checkout.
