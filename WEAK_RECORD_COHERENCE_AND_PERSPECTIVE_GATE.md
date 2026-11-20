# Weak histories, accessible records and plural perspectives

## The question and result

Can a nonzero sequential weak value, used as an informational-observer criterion, establish that a record persists and supports one continuing perspective? In a finite quantum model it **does not establish operationally accessible record persistence**. Nor does it establish phenomenal subject identity. Conversely, a zero weak value for a coarse record does not rule out actual records in a different, explicitly specified fine-monitoring experiment. The two experiments are physically different; the point is not to combine their outcomes as if they described the same unperturbed run.

This applies a known three-path pre/post-selection example and known history-additivity distinctions to a new target: the proposed bridge from weak-history compatibility to record-based observerhood. It is a conditional counterexample to that **sufficiency inference**, not a novel theorem of weak measurement, a refutation of relational quantum mechanics, or an assertion that the example has a conscious observer.

## 1. The proposal in context

Bethany Terris, [*The Informational Observer in Relational Quantum Mechanics*](https://arxiv.org/html/2603.02978v3), distinguishes an interacting physical observer from an informational observer whose records have coherent temporal structure. The proposed criterion uses nonzero sequential weak values for sequences of record operators, with pre- and post-selected boundary conditions. Section 4 combines the proposed coherence criterion with cross-perspective links. Section 5 argues that the criterion supplies a justification for treating records as stable evidence carriers.

The paper also explicitly limits its proposal: it does not model physical protection of memory or settle metaphysical identity or subjective continuity. We do not attribute these stronger claims to it. Our narrower question is whether the weak-value condition itself licenses the operational stability that confirmation needs. We use “coherence” below in two distinct senses: a weak-history compatibility criterion and persistence/recoverability of a physical record. They are not interchangeable.

The sequential weak-measurement formalism is due to [Mitchison, Jozsa and Popescu, *Sequential weak measurement*](https://arxiv.org/html/0706.1508v2). The three-box pre/post-selection and its context dependence are familiar; see [Kastner, *The Three-Box “Paradox” and other Reasons to Reject the Counterfactual Usage of the ABL Rule*](https://arxiv.org/html/quant-ph/9807037), and the recent [Kanjilal, Wagner and Galvão, *Coherence as a resource for N-box and quantum pigeonhole paradoxes*](https://arxiv.org/html/2607.24282v1). These are not presented as original discoveries here. See the source-scope note below.

## 2. Fine histories need not survive coarse graining

Use a qutrit whose orthogonal states `|0⟩,|1⟩,|2⟩` label *candidate* record alternatives. Take stationary dynamics and

`|ψ⟩=(|0⟩+|1⟩+|2⟩)/√3`, `|φ⟩=(|0⟩−|1⟩+|2⟩)/√3`,

with `⟨φ|ψ⟩=1/3`. Denote `P_i=|i⟩⟨i|`. At two successive record positions, `P_i P_i=P_i`. Thus the ordered sequential weak values, normalized by `⟨φ|ψ⟩`, are

`w(P₀P₀)=1`, `w(P₁P₁)=−1`, `w(P₂P₂)=1`.

All three are nonzero. Define the coarse record `Q=P₀+P₁` at **both** positions. Then `Q²=Q` and `w(QQ)=0`: the nonzero `0` and `1` amplitudes cancel. The complementary coarse history `P₂P₂` has weak value 1. Therefore a criterion that declares each fine record compatible when its weak value is nonzero, and a coarse record incompatible when its value is zero, is **not stable under this coarse graining**. This is not a mere change of labels: permuting labels and transporting all operators leaves the result invariant; deleting which-alternative detail changes the question.

Nothing here says that all coarse grainings should receive the same identity, or that Terris proposes such a rule. It demonstrates that a theory which needs record or subject identity to survive a specified change of resolution must add a resolution rule and a compatibility test; nonzero weak values alone do not supply them.

## 3. Check the actual instruments

Three distinct experiments use the same preparation and final postselection; all probabilities below refer to the explicitly stated instruments:

| Intermediate protocol | Success probability | Conditional probability of record in `{0,1}` given success |
|---|---:|---:|
| No strong record measurement | `1/9` | not defined as a measured record in that protocol |
| Lüders measurement `{Q,P₂}` | `1/9` | `0` |
| Fine projective measurement `{P₀,P₁,P₂}`, later forget which of 0,1 | `1/3` | `2/3` |

For example `⟨φ|P₀|ψ⟩=1/3` and `⟨φ|P₁|ψ⟩=−1/3`. Coherent coarse-graining sums these amplitudes before squaring; fine monitoring produces distinct physical outcomes before forgetting and sums their squared amplitudes. The difference is not a violation of probability theory. The fine monitored setup can store the result in an external register; the unmonitored and coarse Lüders setups do not leave that fine record. No conditional probability from one row may be silently transferred to another.

Equivalently, including the final postselection in the history family, the off-diagonal interference term between `0` and `1` is `−1/9`. The coarse success weight `1/9+1/9−2/9=0` is not the sum of the positive diagonal weights. This connects directly to our [temporary-friend history gate](TEMPORARY_SUBJECT_RECORD_HISTORY_GATE.md): there, assigning ordinary additive projective-history weights fails for a reversal context; here, nonzero weak fine-history amplitudes can cancel on coarse graining. Neither result establishes that a person did or did not have an experience.

A second check prevents treating a Pauli product as the projector for a particular outcome sequence. With stationary `Z`, prestate `|+⟩`, poststate `|1⟩`, `w(Z³)=−1`, but the all-up sequence has `w(P₊³)=0`. In Terris's displayed example the `−1` is an eigenvalue of `Z`, **not an anomalous weak value outside its spectrum**. This does not invalidate a criterion explicitly defined for `Z³`, but the sign/product operator does not by itself specify which memory-outcome sequence was recorded; a proposed use must supply the relevant record operators and dynamics. We do not claim this alone resolves the Frauchiger–Renner scenario.

## 4. A nonzero weak history with an overwritten register

A separate two-qubit example makes the insufficiency direct. Let `M` be the accessible memory and `E` an inaccessible environment. Prepare `|ψ⟩=|+⟩_M|0⟩_E`, then swap `M` and `E`, and postselect `|φ⟩=|0⟩_M|+⟩_E`. The boundary overlap including the swap is 1. Insert `P₁` on `M` before the swap and `P₀` on `M` after it: the sequential weak value is `1/2`, nonzero. Yet after the swap the reduced state of `M` is certainly `|0⟩`: it carries no accessible distinction between inputs `|0⟩_M|0⟩_E` and `|1⟩_M|0⟩_E`. The missing bit has moved to `E`; the global unitary has not destroyed information. If `E` is made accessible the conclusion changes, so the accessibility restriction is essential.

The input comparison defines a separate controlled encoding test, not a claim that an unmeasured early bit was definite in each coherent run. The example does not show that Terris identifies the initial `1` with the final `0` as a retained same-content record: it shows that nonzero compatibility of a specified record sequence is insufficient, without a channel test, to establish retention of an earlier bit.

### Graded environmental control

Add an environment flag for each fine alternative with normalized states satisfying `⟨e₀|e₁⟩=r` (real), and `e₂` orthogonal to both; `0≤r≤1`. Apply the same final projection to the qutrit only and leave the flags unread. For the postselected branch, the coarse `{0,1}` weight and total success probability are

`p_group=2(1−r)/9`, `p_success=(3−2r)/9`,

so the group fraction is `2(1−r)/(3−2r)`. At `r=1`, the two alternatives leave identical flags and cancel; at `r=0` their flags are orthogonal, yielding the fine-monitoring value `2/3`. For equal priors and ideal optimal flag readout, the Helstrom minimum error distinguishing `e₀` from `e₁` is `(1−√(1−r²))/2`; see the formula in [Barnett and Croke, *Quantum state discrimination*](https://arxiv.org/html/0810.1970). This distinguishability statement is about the flag ensemble before the system postselection, not the biased postselected ensemble. The remaining fine-history interference magnitude is `r/9`. This provides an operational trade-off **for this model**, not a universal identity between consciousness and decoherence.

There is also a robustness problem with exact nonzero thresholding. Replace the poststate by the normalized vector proportional to `(1,−1+η,1)`. The coarse weak value is `η/(1+η)`, nonzero at every small positive `η`; with the coarse Lüders measurement, its conditional probability is `η²/(1+η²)`. At `η=1/1000` these are `1/1001` and `1/1000001`, respectively. Neither tiny nonzero value warrants a robust operational record without a separate tolerance, accessible channel and sampling assumptions.

## 5. An explicit conditional bridge—not a solution

For an actual information-bearing perspective, specify independently:

1. **Record encoding and scope.** The physical system, alternatives, instruments, environment, interventions, record times and perspective-relative boundaries. State which resolution changes preserve the intended evidence question. Avoid treating a formal history projector as proof it was measured or retained.
2. **Operational retention.** For a prior with at least two possible records, define an accessible later readout channel `K(y|i)` and a decoder with bounded error, e.g. worst-case `P(î≠i|i)≤ε<1/2`. For the two-record case, the output distributions must then have total variation at least `1−2ε`; this follows since the decoder's decision region differs in probabilities by at least that amount. Specify what resources the decoder may access. A one-value postselected ensemble provides no evidence of storage capacity.
3. **History consistency or an alternative joint law.** When assertions about earlier records and later observations are jointly made, give a consistent family, an actual monitored instrument, or an explicitly defined alternative event law. Do not replace a coherent experiment by a dephased one without accounting for the altered postselection rates.
4. **Cross-perspective readout.** Specify which other system reads which surviving degrees of freedom and the error/conditioning of their agreement. A cross-perspective link conditional on an intact record does not itself manufacture that intact record. Robustness under prescribed noise, interventions and redescription must be independently checked.
5. **Phenomenal constitution and persistence.** State a separate, substrate-independent candidate relation between the qualified physical/informational structure and experience, its subject boundaries, and an identity/continuity rule. Record retention is neither logically necessary for every possible experience nor sufficient to prove experience or continuing personal identity. Calibrated experiential tests remain unresolved; see [subject constitution interface](SUBJECT_CONSTITUTION_INTERFACE_PROTOCOL.md) and [awareness calibration](AWARENESS_CALIBRATION_AND_COGITATE_OFFSET_GATE.md).

The total-variation requirement is a useful *necessary condition for the stipulated binary operational task*, not a proposed necessary condition for subjecthood. Recordless or transient experiences remain possible on other theories. A physical readout channel with the requisite error properties is not by itself an experiential assay.

## 6. Relevance to the whole

The relational-whole proposal can accommodate genuinely plural subjects without making the whole one universal consciousness. The gate instead exposes the obligations of doing so: specify local physical and informational relationships, select a justified experiential constitution and persistence map, and explain how their record comparisons fit contextual quantum predictions. Treating the whole as timeless does not turn boundary-conditioned amplitudes into memory or experienced time. The `two positions` above are ordering labels in a laboratory model, not an external fundamental clock; extending the bridge to a timeless constraint theory and emergent clocks requires additional work.

Self-subsistence, experience as intrinsic ground, substrate independence, and actuality of genuine possibilities remain **working metaphysical commitments**, not consequences of this example. There is no deduction here of necessary existence, a unique observer measure, a global joint history, or any solution of quantum gravity.

## Reproduction and source scope

Run `python verification/weak_record_coarse_graining_gate.py`. It checks exact rational weak amplitudes, the three instrument predictions, the history interference term, 101 flag overlaps, six simultaneous label permutations, the overwrite circuit, threshold perturbation and the Pauli/projector distinction; it writes the adjacent JSON receipt. These checks apply only to the specified model and do not measure a real memory or demonstrate a subject.

Terris: full arXiv v3 HTML text and references read, but its figure not independently inspected; the [published article](https://doi.org/10.1007/s10701-026-00939-5) was subscription-preview only, so no version comparison was performed. Mitchison et al.: abstract and opening chunk of the available full preprint read, not its remaining text or figure. Kastner: opening chunk only of the available full preprint; no full argument/figure audit. Kanjilal et al.: opening chunk only of the available full preprint; the rest and its figures were not inspected. Barnett and Croke: minimum-error discrimination section (HTML chunks 1–2) inspected, not the full review or figures. These sources attribute established background, not a claim to have verified their full derivations.
