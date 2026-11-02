# Constructive step 5: episode-first paired reconstruction

## A discriminating design, not another unity assumption

This round implements the positive direction identified by the gluing tests: begin with independently warranted episode evidence, then ask which concrete organizational account predicts its transformations.

The immediate achievement is a **reproducible identification protocol**. Three explicit physical-memory/readout mechanisms generate the same final aggregate report but different candidate presentation histories. Targeted interventions yield a conditional double dissociation between presentation-related organization and reporting.

The result is not a completed psychophysical identity. There is no actual phenomenological dataset in this workspace. Candidate presentation histories are explicitly model predictions, not measurements or conscious occurrences produced by running the simulator.

**24 new tests pass. Across the five research rounds, 126 tests pass.**

---

## 1. Three hypotheses with the same aggregate report

Present three distinct source events in sequence:

\[
A_0,\quad B_1,\quad C_2,
\]

and request a report at tick 3. The tick scale is a supplied experimental protocol, not a derived unit of phenomenal time.

Each mechanism has a report record \(M\) that accumulates source information. The final report reads that record. A separate workspace \(W\) has different update rules.

### P — Persistent presentation-buffer candidate

The workspace accumulates source information throughout the sequence:

\[
W_{t+1}=W_t\cup I_t.
\]

Its contents are the proposed jointly presented contents at that tick. Calling this a presentation is an explicit bridge hypothesis; storing several items is not, by itself, phenomenal unity.

### S — Sequential presentation plus aggregate record

The workspace contains only the current input. A separate record accumulates earlier inputs and supplies the later report.

The candidate presentation is sequential even though the report lists all three contents.

### R — Sequential presentation followed by late replay

The workspace contains current input during the sequence. At report time, it loads the accumulated record. The candidate therefore has a later joint presentation without an earlier one.

These are deliberately simple memory/readout mechanisms. They are not detailed neural models, and the persistent buffer is not claimed to be an implemented theory of phenomenal binding.

## 2. Exact baseline predictions

The candidate source-support profiles are:

| Tick | Persistent candidate P | Sequential candidate S | Late replay candidate R |
|---|---|---|---|
| 0 | A | A | A |
| 1 | AB | B | B |
| 2 | ABC | C | C |
| 3, report time | ABC | empty | ABC |
| Final report | ABC | ABC | ABC |

A later ABC report is compatible with all three candidates. It does not establish that ABC was jointly presented at tick 2, nor that no later replay occurred.

A late replay does not retroactively create an earlier joint episode. Source information retained or recovered later is not the same presentation-token merely because its content type recurs.

The model therefore separates:

- what information is available in memory;
- when the proposed joint presentation occurs;
- and what is eventually reported.

## 3. A precise minimal observation design

Assume, conditionally, that independently calibrated episode evidence can distinguish the candidate source supports at selected ticks.

Exhaustive search over the available observation times gives the smallest separating designs:

\[
\{1,3\}\quad\text{or}\quad\{2,3\}.
\]

No single tick distinguishes all three candidates:

- tick 0 distinguishes none;
- ticks 1 or 2 distinguish P from the other two;
- tick 3 distinguishes S from P and R.

The pair \(\{1,3\}\), for example, distinguishes:

- early AB and late ABC: P;
- early B and late empty: S;
- early B and late ABC: R.

This is a genuine identification result **within the specified three-model class and assumed episode-observation interface**. It is not a proof that two human reports can identify consciousness, or that no richer candidate can match the same data.

An observation inconsistent with all three rejects the current candidate set rather than forcing a winner. Uncertain episode evidence can be supplied as a set of admissible supports; the implementation returns compatible candidates without assigning likelihoods or a posterior.

## 4. The intervention double dissociation

Separate workspace clearing from report-record clearing. In both cases, the intervention occurs immediately before the third input is processed.

### Intervention W: clear the proposed presentation buffer

For P:

- the workspace loses A and B;
- C is then processed;
- the candidate presentation becomes C;
- the untouched report record still supplies ABC.

Thus:

\[
\text{candidate presentation changes},\qquad
\text{final report is unchanged}.
\]

### Intervention M: clear the report record

For P:

- the workspace retains ABC;
- the record loses A and B and then records C;
- the final report becomes C.

Thus:

\[
\text{candidate presentation is unchanged},\qquad
\text{final report changes}.
\]

For R, clearing the report record also changes the later replay, because replay depends on that record.

### Conditional predictions

| Condition | P presentation at tick 2 | P final report | R presentation at tick 3 |
|---|---|---|---|
| Baseline | ABC | ABC | ABC |
| Clear workspace before C | C | ABC | ABC |
| Clear record before C | ABC | C | C |
| Block recording C | ABC | AB | AB |
| Block only outward emission | ABC | no emitted report | ABC |

These are consequences of the specified physical update rules plus each candidate's presentation bridge.

They do not establish that a real brain has cleanly separable buffers, that a real intervention is selective, or that the modeled workspace is phenomenal. Those are empirical and constitutive obligations.

The significance is narrower and constructive: **the same final report can survive a predicted presentation change, and a report can change without a predicted presentation change**. This supplies explicit contrasts that a report-equals-experience account would miss.

## 5. Blocking report does not establish preserved experience

A gate that suppresses outward emission leaves the internal calculations unchanged in the model. Its failure to emit anything therefore does not select a presentation hypothesis.

This is an important control. The experiment must not reason:

> The report was blocked, so the predicted experience must have persisted.

Nor should it infer absence of experience from absence of a report. With the selected output channel unavailable, other independently justified evidence is needed. Later reports, memory, and physiological proxies each introduce their own dependencies.

The code verifies only the stipulated emission gate and resulting candidate profiles. It is not an empirical no-report validation.

## 6. Episode-first means independent evidence, not a privileged output variable

In this construction, the physical simulation produces a proposed presentation readout. Writing that readout into the code does not give it first-person warrant.

The paired reconstruction has two distinct inputs:

1. a model predicting candidate organization and its transformations;
2. evidence about an actual episode, characterized independently enough to test those predictions.

If the second input is simply defined as whatever the first predicts, the identification succeeds trivially and explains nothing about experience.

An actual study must therefore state what supports claims about immediate co-presence, temporal integration, and replay. Direct comparative first-person evidence is relevant but fallible. A later remembered judgment can concern an earlier presentation or be formed during a later reconstruction; that distinction is part of the investigation, not a premise to ignore.

The exact observation interface used in the finite identification test is a mathematical specification of what would discriminate candidates. It is not a claim that we already possess that interface experimentally.

## 7. Source provenance is not presentation identity

The model records three different kinds of identity:

- **source event:** the particular occurrence that supplied information;
- **presentation token:** a candidate content-occurrence at a particular run and tick;
- **reported quality label:** a possibly lossy label such as A.

A retained A source at ticks 0 and 1 is associated with different candidate presentation tokens. Their source information overlaps; their numerical occurrence identity is not assumed to persist.

Likewise, a later replay of A is not automatically the original A experience. Two inputs both labeled A have distinct source-event identifiers; reducing the report to the set of quality labels loses that distinction.

These distinctions protect against the previous false-amalgamation problem. Shared source information or repeated labels do not themselves create a shared phenomenal occurrence.

They also leave a genuine question open: whether retained contents form a continuous episode, a series of episodes, or another temporal organization. The simulator does not identify continuing subjects from its tick indices.

## 8. Realization-token safeguards

The new design retains the earlier constraints:

- Different runs can have identical candidate content profiles but distinct occurrence-token witnesses.
- A passive source-event renaming transports predictions rather than adds an occurrence.
- Repeated source identifiers are rejected where the protocol claims distinct input occurrences.
- Multiple model hypotheses are not multiple simultaneously existing observers.
- Candidate presentation supports are not observer counts.
- A timing-sensitive test does not erase the chosen temporal protocol.
- No observer measure, indifference principle, or ego-allocation mechanism is derived.

The supplied run identifiers and source anchors are witnesses used for bookkeeping. Their actuality and phenomenal relevance are not inferred from the data structure.

A protocol can also fail to discriminate. If all three inputs are simultaneous, P and R have the same profile in this limited test. The design search returns no separating observation set rather than inventing an observation that is absent from the protocol.

## 9. What the design earns on both sides

The public physical side now has explicit intervention consequences: workspace erasure, record erasure, write blocking, and emission blocking are different operations with different causal effects.

The phenomenal side has explicit, distinguishable **predictions** about timing and joint presentation. These remain conditional on the candidate bridge but are not just restatements of the final report.

This moves the programme beyond a generic “integration produces unity” claim. It asks which physical organization predicts the independently characterized appearance of unity, and under which interventions the correspondence survives or fails.

It does not yet answer why the selected organization feels, why the episode exists, or why the relevant laws obtain. A correct predictive identification would still need the determination/identity/explanation distinctions preserved in the synthesis.

The most valuable intermediate success would be a validated dissociation that rules out a report-only explanation while supporting a more specific constitutive process. It would be evidence for that process, not a complete metaphysical derivation.

## 10. A prospective validation protocol

A defensible empirical translation should be specified before collecting confirmatory data:

1. **Define the target episode and competing descriptions.** Do not equate an aggregate answer with earlier unity.
2. **Calibrate phenomenological distinctions separately.** Immediate co-presence, sequential integration, and remembered jointness need not be the same evidence.
3. **Establish intervention selectivity.** Workspace, recording, replay, and emission cannot be declared separate merely because the toy model separates them.
4. **Choose informative timing conditions.** The finite model explains why a single endpoint observation can be insufficient and why early-plus-late evidence is useful.
5. **Withhold conditions from model fitting.** Test the dissociation predictions under timing or intervention combinations not used to define the candidate state.
6. **Represent uncertain observations explicitly.** Return an identification set where the evidence does not discriminate. Do not convert uncertainty into equal probabilities over models.
7. **Audit perturbation effects.** An early query can itself affect attention, memory, or presentation; a late query may reconstruct. Either effect can invalidate a supposedly passive observation interface.
8. **Retain alternative models.** Another organization can match these predictions. Model identification is always relative to the tested class and evidence.

No participant data, neurophysiological data, or actual neural interventions are supplied here. Therefore this round establishes an executable design and conditional predictions, not an empirical selection of P, S, or R.

## 11. Next constitutive obligation

The next substantive task is to justify why one candidate presentation variable is not merely another internal readout.

The hypothesis to test is:

> The concrete organization responsible for the validated episode transformations constitutes that episode, rather than merely recording or predicting it.

A useful next formal step is an **intervention-equivalence audit**: determine whether a phenomenally irrelevant internal monitor can reproduce the same tested dependencies. If it can, identify which additional independently justified contrast separates constitution from monitoring—or record that the present evidence supports dependence without identifying constitution.

This is the next load-bearing inference. Adding more memory variables or counting more successful simulations will not establish it.

## Reproducibility

- `model.py`: three memory/readout mechanisms, candidate presentation profiles, intervention protocols, provenance-sensitive token bookkeeping, exact and set-valued identification, minimal temporal-design search.
- `test_model.py`: 24 tests.
- `results.log`: actual run.
- `predictions.json`: machine-generated baseline and intervention predictions.

Run this round:

```bash
cd research/episode_reconstruction
python -m unittest -v test_model.py
```

Run the entire branch:

```bash
python research/run_checks.py
```

**Observed result:** 24 new tests pass; 126 tests pass across the five research rounds. Test execution verifies these finite mechanisms and their specified interpretations, not actual experience or the ultimate sufficiency of the constitutive candidate.

### Final constructive verdict

> Episode-first reconstruction now has a concrete discriminating design: separate ongoing joint presentation, sequential presentation with aggregate memory, and later replay; test workspace and report-record interventions independently; preserve source and presentation provenance. The model proves why final reports are insufficient and identifies an exact temporal observation design within its candidate class. The next bridge is constitution rather than monitoring. It requires independently grounded episode evidence and a stronger causal/constitutive argument, not an identification imposed by the code.

## Subsequent constitution/monitoring audit

[Constructive step 6](../constitution_monitoring/REPORT.md) makes the bridge obligation explicit: distinct causal roles do not alone identify a phenomenal target. It tests physically equivalent rival annotations, the minimal missing target contrasts, and the extra assumption introduced by universal report faithfulness.
