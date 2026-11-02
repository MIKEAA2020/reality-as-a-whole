# Constructive step 6: constitution versus monitoring

## Result in one paragraph

The preceding episode-first design distinguishes memory/readout mechanisms **conditional on their proposed phenomenal identifications**. This round isolates that qualification. A source and its monitor can have different causal roles while several proposed phenomenal identifications remain compatible with exactly the same public physical intervention data. A finite model proves this distinction, enumerates the surviving hypotheses, and specifies the additional contrast evidence that would identify a target within the model. It also shows how assuming report faithfulness can silently supply the desired answer. This is an identification audit, not an empirical discovery or a general impossibility theorem about consciousness.

**24 new tests pass; all 150 tests across the six research rounds pass.**

## 1. Separate physical organization from its proposed phenomenal identification

Use a deliberately small physical circuit:

\[
C=X,\qquad M=C,\qquad R=C.
\]

Here:

- X is a binary input;
- C is a source register;
- M is a monitor copying C;
- R is a report reading C directly, bypassing M.

An intervention can override C or M, and an emission gate can suppress R. These are stipulated operations on a toy circuit, not demonstrated selective interventions on a brain.

This circuit makes the causal difference unambiguous. Overriding M does not change C or R. Overriding C changes the unconstrained M and R. The monitor is causally dispensable for this reporting task.

Now ask a different question: which organization determines a binary phenomenal **target contrast** E?

Consider every Boolean function

\[
E=f(C,M).
\]

There are 16 possible truth tables. These are competing identifications of one physical system, not 16 observers or additional physical processes. The target is a supplied binary contrast, not a representation of an entire episode or subject.

## 2. Exact public intervention equivalence

There are 36 protocol settings:

\[
2\text{ inputs}\times3\text{ C override choices}\times
3\text{ M override choices}\times2\text{ emission settings}.
\]

The override choices are no override, force 0, and force 1.

For every candidate f and every setting, the complete modeled physical outcome (X,C,M,R) is identical across candidates. The phenomenal annotation changes no physical equation.

### Conditional equivalence proposition

If candidate interpretations share the same physical transition/intervention law, and an observation is a function only of the resulting physical history, their predictions for that observation are identical.

**Proof.** Each intervention produces the same physical history under each interpretation. Applying the same observation function to equal histories produces equal observations. The same reasoning extends to stochastic laws with identical interventional history distributions by taking their pushforward distributions. ∎

The code exhaustively verifies the deterministic instance for all 16 candidates and 36 settings.

### What this does—and does not—establish

It establishes a limitation of this evidence/model pair. It does not prove that actual phenomenal constitution is arbitrary, that all annotations are metaphysically possible, that consciousness is causally inert, or that richer physical theories cannot explain experience.

E is an annotation here, not an extra causally inert substance introduced alongside the circuit. Under E=C or E=M, the identified physical register retains its ordinary causal powers. Those powers differ. What remains undecided is whether either proposed identification is warranted.

The annotation-only model deliberately leaves constitutive constraints unspecified. Its underdetermination identifies what those constraints must accomplish; it does not prove that no such constraints exist.

## 3. Baseline calibration leaves four candidates

Suppose independently warranted calibration establishes the following target values in ordinary copying conditions:

\[
E(0,0)=0,\qquad E(1,1)=1.
\]

These are stipulated synthetic calibration facts in this implementation. No actual experience data have been collected.

They leave exactly four candidates:

| Candidate | E(0,0) | E(0,1) | E(1,0) | E(1,1) |
|---|---:|---:|---:|---:|
| Source: E=C | 0 | 0 | 1 | 1 |
| Monitor: E=M | 0 | 1 | 0 | 1 |
| Conjunction: E=C AND M | 0 | 0 | 0 | 1 |
| Disjunction: E=C OR M | 0 | 1 | 1 | 1 |

Ordinary conditions cannot distinguish them because C=M. More repetitions of those same conditions add no new exact identification constraint.

This recovers a recurring issue in the constructive programme: calibration on a restricted context can hide dependence on an additional coordinate.

## 4. The missing contrasts are exact

The two off-diagonal states are:

\[
(C,M)=(0,1),\qquad(C,M)=(1,0).
\]

For the four calibrated candidates:

- either off-diagonal target observation alone leaves two candidates;
- both target observations together identify one candidate;
- exhaustive search shows that these two states form the unique smallest separating state set.

For example, target values 0 at (0,1) and 1 at (1,0) select E=C within this class. Opposite values select E=M. Values 0 at both select conjunction; values 1 at both select disjunction.

**Crucial distinction:** forcing the physical registers into those states does not, by itself, measure E. The target values must have independently warranted phenomenal significance.

The implementation includes an idealized target-evidence interface precisely to show the needed contrasts. It is not an implemented phenomenal sensor.

If the rival interpretations are genuinely equivalent for all public physical observations in the model, adding another public physical readout alone cannot break the equivalence. An E-sensitive sensor would require a justified observation bridge or changed physical predictions; it cannot be smuggled in as a free measurement of E.

## 5. How report faithfulness can select the answer by assumption

Across emitted-report settings, this circuit has R=C.

If we impose

\[
E=R
\]

throughout the intervention domain, the full set of 16 candidates collapses to E=C.

This is mathematically correct but not an independent derivation of constitution. Universal report faithfulness supplied the missing off-diagonal E values.

It would be equally wrong to conclude that reports can never provide evidence about experience. Reports can be informative under justified reliability conditions. The issue is whether those conditions survive precisely the intervention being used to distinguish the source from its monitor.

For example, a proposed E=M account predicts a mismatch with this particular R channel when M is independently overridden. Rejecting that account requires a reason to trust R about the target in those conditions, or another warranted constraint—not merely the existence of the report.

Report reliability is neither globally guaranteed nor globally denied by this analysis.

## 6. The constructive distinction we can now make

There are three different achievements:

### A. Identify a causal role

The physical intervention table establishes that M is dispensable for producing R in this circuit. That is a genuine causal result.

### B. Identify determination of a target contrast

With warranted off-diagonal target evidence, E=C can be selected from the supplied Boolean class. The minimal coordinate support of that selected target is then {C}; M is unnecessary for this target over the full four-state domain.

This remains relative to the target, domain, and candidate class. A different target could depend on M or on both coordinates.

### C. Explain phenomenal constitution

Even successful B does not explain why C constitutes a phenomenal contrast, why its particular states have that qualitative character, or why there is an actual episode rather than only an abstract circuit specification.

Thus:

\[
\text{causal role}\ne\text{target determination}\ne
\text{constitutive explanation}.
\]

These distinctions are not demands for three separate substances. They are different explanatory obligations that an eventual identity theory may discharge together—but cannot discharge merely by using the word “identity.”

## 7. What survives from the previous episode-first design

The previous double dissociation remains valid as a result about specified update rules and candidate presentation profiles. It did not yet identify a phenomenal buffer.

This round sharpens its interpretation:

> Dissociating a workspace from reporting can rule out a particular report-only causal architecture. It identifies the workspace as phenomenal only with further warranted constraints linking the independently characterized episode to that workspace rather than to a monitor, replay, or other correlate.

In particular:

- temporal episode evidence must not be defined by the tested buffer state;
- selectively perturbing a register must not be assumed to leave the observation channel faithful;
- causally upstream does not automatically mean constitutive;
- causally dispensable for a selected report does not automatically mean phenomenally irrelevant;
- a model may be rejected by inconsistent target evidence rather than rescued by relabeling its registers.

## 8. A usable bridge-validation rule

The independently justified methodological requirement is **contrast accountability**:

> A constitutive identification must disclose which independently warranted target contrasts distinguish it from rival identifications, or which independently justified constitutive constraint excludes those rivals. A successful report prediction cannot silently serve as both the proposed bridge and its validation.

This is a requirement on explanatory justification, not a sufficient psychophysical law. It earns its authority from the ordinary difference between testing an identification and assuming it.

For each claimed bridge, record:

1. **Target warrant:** what supports the phenomenal contrast, including uncertainty and temporal provenance?
2. **Physical intervention:** which concrete variable was changed, and what validates intervention selectivity?
3. **Rival predictions:** do the alternatives actually disagree about an accessible target contrast?
4. **Access reliability:** why should the measurement or report still track that target after intervention?
5. **Constitutive premise:** what, beyond correlation or report production, licenses the proposed identity?

If public predictions are exactly equivalent, report the equivalence. The remaining argument must concern additional justified constraints, not an imaginary discriminating physical dataset within the unchanged model.

This is stricter than maximizing predictive fit, but it does not require infallible access or nonphysical instruments. It requires acknowledging which empirical, first-person, and theoretical commitments do the work.

## 9. Realization and scope controls

No enumeration here counts observers. The 16 tables are hypotheses; the 36 settings are protocols. Neither is a population of actual experiencers.

The circuit values are abstract state types. Running the tests does not establish that C or M is conscious. The model does not infer subject boundaries, temporal continuity, actual occurrence, observer measures, or substrate-independent phenomenal sufficiency.

The physical equation R=C is deliberately different from the previous round's aggregate report equation. This is a new controlled countermodel, not a claim that the previous implementation had this wiring.

The finite Boolean function class also assumes a context-independent instantaneous binary target depending only on C and M. Real alternatives may involve history, context, hidden variables, richer phenomenal structure, or a different factorization. Identification within this class cannot exclude those alternatives.

## 10. The next constructive task—not another annotation exercise

The standing request is still stronger than what has been achieved: an independently justified constitutive principle explaining something on both the physical and phenomenal sides.

The completed sequence has now exposed a precise failure mode: **an arbitrary state-to-experience annotation can reproduce a calibration without explaining constitution.** More annotated toy mechanisms will not fix that.

The next productive task is to formulate and audit a structural identity claim whose restrictions are motivated independently on both sides—for example, comparing physically specified intervention/contrast structure with independently characterized phenomenal contrast structure. Such a claim must address:

- why the structures correspond beyond the calibration cases;
- what excludes physically redundant monitors or transformed readouts;
- whether correspondence determines qualitative character or only relations;
- how the claim applies to actual realization occurrences, not merely isomorphic types;
- and whether any residual choice is a substantive psychophysical postulate.

This reconnects to the initial contrast-covariance proposal with a sharper acceptance criterion: **a structure match alone is not enough if the source and its monitor inherit the same structure.** The distinguishing proposal must explain why the relevant concrete causal organization, rather than an arbitrary copied representation, is constitutive.

No such complete principle is claimed in this round. The positive achievement is an exact separation of causal identification, target identification, and constitution, together with the minimal missing contrasts and a non-circular bridge-validation rule.

## Reproducibility

- `model.py`: circuit, interventions, 16 candidate target functions, evidence filtering, minimal contrast designs, coordinate-support analysis.
- `test_model.py`: 24 tests, including all physical signatures, candidate elimination, report-faithfulness assumptions, uncertain evidence, and restricted-domain ambiguity.
- `results.log`: actual test output.
- `enumeration.json`: machine-generated candidate tables and physical-equivalence summary.

```bash
# This round
cd research/constitution_monitoring
python -m unittest -v test_model.py

# All six rounds, from repository root
python research/run_checks.py
```

**Observed verification:** 24 new tests pass; 150 tests pass across the six research rounds. These tests verify the finite model and conditional identification results, not consciousness, empirical report reliability, or zero-residue metaphysical completion.

## Subsequent structural test

[Constructive step 7](../interventional_core/REPORT.md) tests a stronger proposal: implementing an interventionally closed transition organization rather than merely copying its synchronized state trajectory. It distinguishes a source from a passive monitor physically while retaining explicit temporal, encoding, and phenomenal-bridge limitations.
