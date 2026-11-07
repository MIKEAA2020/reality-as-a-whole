# Does a subject's experience need an indelible physical record?

## Decision

**No such requirement follows merely from subject plurality or physical supervenience.** But if a proposed subject–event selector *does* require a particular outcome to be recoverable from an external record that Alice cannot reverse, the record's distinguishability constrains the interference available in the proposed Wigner's-friend experiment.

In a specific ideal four-qubit model, a perfect external record removes the Local Friendliness/CHSH violation for the selected operations. A partially distinguishable record does not necessarily remove the violation: a record from which the branch can be guessed 90% of the time is compatible with a CHSH value of `2.16` for the fixed settings used below. Including the record in a coherent reversal restores the original `2.8` in that circuit, but erases the record's distinguishability.

This is a **conditional constraint on a physically specified record model**, not a demonstration that real experiences require such records, that experience is absent when a record is erased, or that a subjective ontology is refuted. It does not solve the subject-selection problem.

## Established work and our limited contribution

This is an application of known complementarity, not a new discovery of the visibility–distinguishability principle. [Englert (1996)](https://doi.org/10.1103/PhysRevLett.77.2154) gives the standard two-path visibility/which-way information inequality. [Elouard et al. (2021)](https://doi.org/10.22331/q-2021-07-08-498) specifically discuss quantum erasure of a Wigner's-friend memory and distinct experimental contexts. For the optimization of CHSH over two-qubit states, see [Horodecki, Horodecki and Horodecki (1995)](https://doi.org/10.1016/0375-9601(95)00214-N). What we add here is an explicit **application and exact check** for our prior circuit, together with a declared candidate criterion for a subject selector. We make no claim of literature-wide novelty or a new physical law.

## 1. Candidate selector condition, stated before outcomes

Consider a proposed theory that, **in addition to** associating experiences with physical processes, asserts:

> **External record condition Rε.** For the relevant two possible friend-record values, there is a specified physical register `E` outside Alice's reversal operation. Its states can be distinguished with average error at most `ε`, for equal prior branch preparations, by a stated measurement. The association between those preparations and the selected subject/event is fixed independently of Alice's eventual outcome.

This is intentionally stronger than generic physical supervenience. A thought might have had local physical correlates during an interval without leaving a separately readable external record afterward; some accounts also treat the thought as relational rather than a unique absolute branch event. Neither Rε nor its failure settles those possibilities. A selector also needs a justified map from the physical record to **which subject and which experience**. Rε by itself supplies no such map.

If a proposed account makes **no** claim like Rε, the following record bound cannot be used to rule it out. If it does make that claim, the bound gives an operational consistency test for the specified model.

## 2. The record model

Extend the circuit in [the subject-identity gate](SUBJECT_IDENTITY_LOCAL_FRIENDLINESS_TEST.md). Write the registers as `A,M,B,E`: Alice's measured qubit, friend memory, Bob's qubit and an external record. After the friend's coherent registration, take

`|Ψ⟩ = (|000⟩_AMB |e₀⟩_E + |111⟩_AMB |e₁⟩_E)/√2`.

For simplicity choose normalized pure record states with real overlap `r=⟨e₀|e₁⟩`, `0≤r≤1`. The record is **not** acted on by Alice's normal reversal. The preparation can be viewed as a controlled, potentially reversible interaction; no literal definite friend thought is assumed in the superposition. Branch-conditional record states and their distinguishability are properties of the specified preparations.

Alice either reads `Z_M` (`x=1`), or reverses the `A→M` CNOT and measures `X_A` (`x=2`). Bob measures `B₁=(3Z+4X)/5` or `B₂=(3Z−4X)/5`. Ignore `E` when computing Alice–Bob's unconditional correlations. They are

| | Bob 1 | Bob 2 |
|---|---:|---:|
| Read | `3/5` | `3/5` |
| Reverse | `4r/5` | `−4r/5` |

Hence `S_fixed=(6+8r)/5`; these **fixed** settings violate the bound 2 exactly when `r>1/2`. The `r=1` case reproduces the preceding gate's `S=14/5`.

For equal priors, the standard optimal binary state-discrimination probability is `p_guess=(1+D)/2`, where `D=(1/2)|| |e₀⟩⟨e₀|−|e₁⟩⟨e₁| ||₁=√(1−r²)`. Thus `D²+r²=1`. For the optimized *symmetric* Bob settings `B₁=cosθ Z+sinθ X`, `B₂=cosθ Z−sinθ X` with Alice's operations fixed,

`S_sym,max = 2√(1+r²) = 2√(2−D²)`.

The maximum follows by maximizing `2(cosθ+r sinθ)`. It is an optimum **within this specified measurement family**, not a bound claimed for arbitrary physical theories, experiments, postselection or unrestricted subject selectors.

## 3. Numerical witness and an explicit recovery

Choose `|e₀⟩=|0⟩` and `|e₁⟩=(3/5)|0⟩+(4/5)|1⟩`. Then

- `r=3/5`, `D=4/5`, `p_guess=9/10`;
- the fixed-setting correlations are `(3/5,3/5,12/25,−12/25)`;
- `S_fixed=54/25=2.16`.

So **a 90%-distinguishable external record and a violation coexist** in this ideal model. The condition is not “any record destroys interference.” A perfectly distinguishable external record has `r=0`, and the maximum in the declared symmetric family is `2`; for our fixed settings it is `6/5`.

In this toy circuit the record is created by a controlled rotation on `E`. If Alice is allowed to control **both** `E` and the friend lab, she can undo that controlled rotation and then undo the friend's CNOT. The state becomes `(|0000⟩+|1010⟩)/√2` in `A,M,B,E` order: `E` is reset to `|0⟩` for both components, and `S_fixed=14/5` is restored. This is a unitary computation in the script. It does **not** say a macroscopic record, a human brain, or a measurement copied to an uncontrolled observer can be reversed in practice: all carriers of the relevant information would have to be brought under appropriate coherent control, including any copied readout. The comparison is unconditional; conditional quantum-eraser/postselection protocols are separate procedures.

## 4. Quantitative gate for the proposed Rε

For `0≤ε≤1/2`, if Rε holds in this pure-state model, then `D≥1−2ε`, so `r≤2√[ε(1−ε)]` and

`S_sym,max ≤ 2√[1+4ε(1−ε)]`.

This is **not** an inequality between a consciousness measurement and CHSH. It compares the independently specified distinguishability of a physical record with the circuit's interference. If `ε=0`, then `S_sym,max≤2`. If `ε=0.1`, the model permits `S_sym,max≤2√34/5 ≈ 2.332`, and the preceding witness achieves `S_fixed=2.16` at the fixed angles. A proposed selector cannot simultaneously require `ε=0` for an untouched external branch record and claim a greater-than-2 violation for this controlled circuit and the specified measurements.

Conversely, if an experiment reports `S_sym>2` under these circuit assumptions, a proposed untouched external record's average minimum error cannot be arbitrarily small. This statement requires independently validating the state-preparation and coupling model; simply reading out `S` does not prove what record exists or how subjective states supervene on it.

## 5. What this does—and does not—say about subjects

| Proposed subject–event relation | What the circuit tells us | Remaining gap |
|---|---|---|
| Experience requires a perfectly readable untouched external outcome record | In this circuit it excludes a CHSH violation under the specified operations | Why an experience would require that strong external record |
| Experience has a local, reversible physical correlate | A later reversal can erase that correlate while restoring interference | A theory of how a definite or relational episode exists during the interaction |
| Experience has an absolute event value but no accessible external record | This record bound does not rule it out | Must satisfy or revise the single-event and Local Agency assumptions in the [previous gate](SUBJECT_IDENTITY_LOCAL_FRIENDLINESS_TEST.md) |
| Multiple indexed subjects/events | Multiple labels alone do not select a physical record or determine outcome probabilities | A non-circular, representation-consistent subject selector and account of comparisons |

A temporary physical correlate can be perfectly distinguishable *inside the lab* even though Alice subsequently reverses it. Its later absence does not, by itself, show that an earlier subjective episode did not occur. Conversely, quantum coherence and an erased memory do not prove that such an episode did occur. The difference between a physically correlated memory and a real experience remains an independent empirical and metaphysical issue.

## 6. A discriminating follow-up, not an assumed result

For an engineered circuit, pre-register:

1. The two branch preparations, the record register `E`, which operations are inside and outside Alice's reversal, and the permitted measurements and time window.
2. A calibration estimating or bounding the distinguishability of the **same prepared conditional record states**; include statistical and systematic uncertainty. State explicitly why calibration trials and interference trials have the same controlled interaction. Prepare/read branches on separate randomly selected trials if the branch label needed for calibration is not jointly available with the interference outcome.
3. The Alice–Bob correlators from the no-record-readout/interference protocol, and compare their confidence bounds to the declared record model's bound. Do not postselect or alter operations without deriving the corresponding new bound.
4. If claiming a subject-selector test rather than merely a circuit test, supply separate evidence that `E` faithfully tracks the selected subject/event, not just a computational bit. No such evidence currently exists for this toy circuit.

Disagreement with the bound would challenge this declared record/preparation/operation model, or its calibrations—not by itself identify the correct interpretation of quantum theory. Reproducing the bound would check known complementarity, not confirm an experience theory.

## 7. Verification and next dependency

Run [`verification/reversible_friend_record_tradeoff.py`](verification/reversible_friend_record_tradeoff.py). It checks 90 rational overlap/record-state cases by four-qubit matrix operations, including the `0.9`/`2.16` witness, and verifies the coherent recovery in each case. The analytic identity and symmetric-angle maximization hold for the continuum in the stated model; the finite checks are not a proof of general quantum foundations or phenomenology.

The next dependency is no longer merely “invent a subject selector.” It is to **specify what observable physical dependence that selector entails**, decide whether it requires a retained record or only a temporally local/relational correlate, and test the resulting proposal against both this complementarity gate and the Local Friendliness assumptions. A subsequent [temporary-record history gate](TEMPORARY_SUBJECT_RECORD_HISTORY_GATE.md) tests a fixed intermediate memory projector using known histories tools; its sequential Born weights fail to reproduce the unchanged reversal experiment. This does not rule out other event laws or show the qubit is conscious. No proposed subject selector has yet passed the combined test.
