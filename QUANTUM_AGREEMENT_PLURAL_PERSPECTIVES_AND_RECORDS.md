# Quantum agreement, disagreement and plural perspectives

## Answer to the two links

The headlines appear contradictory, but the results concern **different ways of specifying the event and the observers' measurements**. They are compatible.

- [Contreras-Tejada et al. (2021)](https://www.nature.com/articles/s41467-021-27134-6) study two observers of no-signaling boxes, estimating **perfectly correlated events** on opposite sides. Under their precise definition of common certainty, quantum boxes cannot exhibit disagreement. Some postquantum no-signaling boxes can.
- The [Phys.org article](https://phys.org/news/2026-11-quantum-limits-theorem.html) describes a model where each observer estimates a **joint property that can fail to commute with one observer's measurement**. A pair of local observer measurements may commute with each other while one fails to commute with that property. In this different setting, common certainty of different probability assignments is possible in quantum mechanics.

The second result does **not** undo the first, nor does it say observers can assert arbitrary contradictory facts. In the model, both start from the same state but condition separately using their own local outcomes. The detailed measurement history is not included in their information states. The authors' explicit comparison of the two settings is in the [September 20, 2026 version of García Díaz, Brandenburger and Scarpa's preprint](https://arxiv.org/html/2511.21258v3), which is the primary technical source used below.

**Date discrepancy:** the supplied Phys.org page displays November 17, 2026, and its linked [PNAS page](https://www.pnas.org/doi/10.1073/pnas.2613021123) displays online publication November 12, 2026. Both dates are later than this session's date, October 31, 2026, even though the page contents were returned by the web tool. Do not treat those displayed publication dates as independently verified past events. The authors' arXiv v3 is dated September 20, 2026 and already contains the results and example discussed here; we rely on that version, not on an assumption that the future-dated journal publication has occurred.

## 1. What “common certainty” actually means

The classical reference is Aumann's agreement theorem: agents with a **common prior**, conditioning on their respective information, cannot have common certainty of different probabilities for the same event. Common certainty is an infinite hierarchy: Alice is certain of Bob's assessment, Bob is certain of Alice's, each is certain of the other's certainty, and so on. This is much stronger than “they told each other what they think,” and it concerns probability assignments, not direct phenomenological access to another subject's experience.

In the 2021 paper, the two target events are perfectly correlated in a designated measurement context. Alice and Bob estimate the other side's event using local box outcomes. Quantum no-signaling correlations satisfy the authors' agreement theorem in that setting; a Popescu–Rohrlich box gives a postquantum contrast. The paper also excludes a defined extreme or “singular” disagreement for quantum boxes. It does **not** say that any two quantum observers always assign the same state or the same probability in every possible protocol.

In the second paper's finite-dimensional tripartite setting, a common prior state `ρ` and local projective measurements are given. Each agent calculates an estimate by a Born–Lüders update on their own outcome. If both agents' measurement projectors commute with each other **and with the target projector**, common certainty implies equal estimates. The noncommutative counterexample changes the target: it is a joint property of Alice's subsystem and the third system, not an independently measured remote property of the earlier no-signaling-box setup. The local measurements of Alice and Bob still commute with one another. This distinction is why the two results fit together.

The preprint also proves, in its own setting, that an outcome with positive probability cannot make Alice certain of an event **and** certain that Bob is certain of its negation, with these assessments defined relative to the same state. This is a carefully qualified 0–1 impossibility result, not proof that all Wigner's-friend paradoxes or interpretive disagreements have been solved.

## 2. The authors' explicit example

Use their qutrit–qubit–qubit model. Write

```text
|u> = |0>_A |0>_B |0>_C,      |v> = |1>_A |0>_B |1>_C,
ρ_t = (|u><u|+|v><v| + t|u><v| + t|v><u|)/2,   0≤t≤1,
|φ>_AC = (|00>+|11>+|20>)/√3,     E = |φ><φ|_AC ⊗ I_B.
```

Alice measures A in its basis; Bob measures B in his. The two local measurements commute, and Bob's measurement commutes with `E`; Alice's does not. For each of Alice's positive-probability outcomes, her conditional estimate is `q_A=1/3`. Bob's sole positive-probability outcome leaves coherence between `u` and `v`, giving `q_B=(1+t)/3`. The appropriate certainty operators stabilize immediately with weight one. At `t=1`, Alice assigns **1/3**, Bob **2/3**, and their differing estimates satisfy the formal common-certainty criterion.

Why not an ordinary contradiction? Bob's calculation conditions the common prior on **his** local outcome; it does not incorporate Alice's physical measurement. There is no explicit common record saying which measurement has already happened. If Alice's measurement is performed and incorporated as an unread Lüders measurement, the state dephases in her basis and Bob's estimate becomes **1/3**. In the preprint's classical-register construction, the agents use the recorded state and, under recorded common certainty, their recorded estimates agree. Bob need not learn Alice's particular outcome in this example.

This comparison changes the physical/epistemic conditions: one cannot treat `2/3` and `1/3` as two predictions for the same fully specified postmeasurement protocol. Merely having a record is not a universal guarantee that arbitrary people, with different priors or unreliable instruments, agree.

## 3. A partial-record extension and a quantitative gate

The preprint itself analyzes complete recording and an explicit uncertainty about whether a measurement was performed. The following **application** adds a different, limited control: an imperfect coherent which-branch record. It uses the authors' example and the established [Englert visibility–distinguishability relation](https://doi.org/10.1103/PhysRevLett.77.2154); it is not a new general complementarity theorem.

Let a separate record system `R` start in a fixed state. A branch-controlled interaction writes normalized pure tags `|r_0>` and `|r_1>` for `u` and `v`, respectively, while preserving those branches. Let

```text
γ = <r_1|r_0>,        D = 1/2 || |r_0><r_0| − |r_1><r_1| ||_1
  = √(1−|γ|²)             [equal prior branch weights, pure tags].
```

`D` is the optimal physical distinguishability of the two tag states when the record is measured, not a consciousness measure. Keep the target `E`, Alice's and Bob's local measurements, and the authors' separate-update convention; neither assessment conditions on a readout of `R`. The tagged joint state carries off-diagonal terms `t |u,r_0><v,r_1|/2` and its adjoint. Direct evaluation gives

```text
q_A = 1/3,            q_B = (1+t Re γ)/3,
|q_B−q_A| = t |Re γ|/3 ≤ (t/3) √(1−D²).              (1)
```

For this model the original positive-probability Alice outcomes and Bob outcome are unchanged, and their certainty recursion remains at a positive-weight fixed point. When `t Re γ ≠ 0` this gives common certainty of unequal estimates according to the paper's formal definition. The extension's use of nonorthogonal tags is a modeling choice; if the observers actually access or condition on the tag record, or use another measurement protocol, their information states and certainty operators must be recalculated.

| Initial coherence `t` | Tag overlap `γ` | Distinguishability `D` | Alice | Bob | Interpretation within this setup |
|---:|---:|---:|---:|---:|---|
| 1 | 1 | 0 | 1/3 | 2/3 | No which-branch information in the tag; reproduces authors' example |
| 1 | 1/2 | √3/2 | 1/3 | 1/2 | Partially distinguishable tags and reduced gap |
| 1 | 0 | 1 | 1/3 | 1/3 | Orthogonal tags; coherence disappears on ignoring `R` |
| 1 | `0.6i` | 0.8 | 1/3 | 1/3 | Agreement for this target despite nonzero remaining coherence |

The last row matters: **agreement need not mean absence of coherence**. Here the surviving coherence is out of phase with this particular target. A different target or phase-sensitive measurement can be needed to detect it. Nor does a retained distinguishable record by itself prove that anyone has read it or is conscious.

The [verifier](verification/quantum_agreement_record_gate.py) checks the full `3×2×2×2` density matrices, Lüders updates, projectors, commutators, stabilized certainty operators, tag trace distances and post-Alice dephasing for 15 cases, including complex overlap. It confirms the named example and these controls numerically. Equation (1) and the pure-tag identity are analytical within this specified family; **finite numerical checks are not a proof of the papers' general theorems**.

## 4. What this changes for the whole-account

These papers supply an important constraint on our research program, not a proof of its ontology.

1. **Plural perspectives and a shared whole are compatible.** Distinct local probability assignments can be well defined relative to distinct information and operations. But this is a structural compatibility result, not a derivation of genuinely plural conscious subjects or of an intrinsically experiential ground.
2. **Perspective is not unconstrained private truth.** A proposed account must specify target events, system boundaries, measurement operations, common information and record relations. Different assignments may track different update histories; simply saying “truth is relative” does not make incompatible claims about one and the same defined record true.
3. **Records are physical interventions.** A cross-perspective comparison must include what was recorded, by what instrument, and whether those records or their traces were reversed. Our earlier [two-report gate](TWO_REPORTS_CONSENSUS_AND_REVERSAL.md) separately shows that two reports can agree perfectly while both track a target poorly. Numerical agreement, faithful calibration and preserved interference are distinct.
4. **Neither paper proves awareness is needed for collapse.** “Observer” is a formal role associated with a local measurement and inference; neither result supplies an experiential assay, a subject-constitution law, or an argument that a quantum system is conscious. Ordinary unitary interaction and modeled decoherence suffice for the record discussion.
5. **No derivation of physical law or the whole's self-existence.** The arguments assume quantum Hilbert-space structure, the Born–Lüders rule and specified operators. They neither derive quantum mechanics from plenitude nor show that its probability law supplies the [subject-occurrence measure](SUBJECT_MEASURE_AND_QUANTUM_OBSERVATION_GATE.md). They also do not establish that a universal subject exists; none is assumed here.
6. **Time and actuality remain separate.** The modeled sequence of measurement and record operations is a local operational order, not an external clock for the timeless absolute or a mechanism that turns mere possibilities into actualities. Establishing such local order from the whole remains open.

The practical next gate is to apply these operator and record distinctions to any proposed cross-perspective subject rule *before* asserting intersubjective agreement or a contradiction: specify a common physical question and prior, accessible records, operations and their order, and the independently motivated relation between a physical record and an experience. Existing conditional quantum checks do not supply that last bridge.

## Reproduction and sources

Install the existing [`verification/requirements-framework-battery.txt`](verification/requirements-framework-battery.txt), then run `OPENBLAS_NUM_THREADS=1 python verification/quantum_agreement_record_gate.py`. The aggregate [receipt](verification/quantum_agreement_record_gate.json) records all 15 checks. The earlier 2021 theorem and the September 2026 preprint are cited rather than re-derived; the source discrepancy and the distinction between the original result and the partial-record application are explicit above.
