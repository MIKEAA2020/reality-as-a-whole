# Two reports: agreement, accuracy and reversible records

## Decision

The previous [two-subject selector](TWO_SUBJECT_REVERSIBLE_SELECTOR_MODEL.md) stipulated that two subject labels agree with a binary record while the record can be reversed. This step asks a narrower, physical question: **what can two readable report registers actually establish?**

In an exact five-qubit model, two reports can agree **100% of the time** while each agrees with the friend record only **64% of the time**. Their errors are the same error, copied from a common source. In that same model, the probability of the interference result `X=+` after reversing the friend memories, while leaving the two reports outside the reversal, is **98%**.

This does not realize the earlier selector's *perfect* subject–record agreement at perfect interference. Rather, it demonstrates why **intersubjective-looking agreement, faithful correlation with the target, and recoverable interference are three separate constraints**. The registers are not conscious subjects. No claim is made that an experience must generate an external report.

## Prior work and what is new here

The underlying visibility–distinguishability relation is established, particularly [Englert's 1996 inequality](https://doi.org/10.1103/PhysRevLett.77.2154). [Chiou and Hsu's quantum-circuit treatment](https://arxiv.org/abs/2207.03946) applies complementarity and erasure in a circuit. [Zurek's quantum Darwinism](https://arxiv.org/abs/0903.5082) and [non-ideal environmental records](https://arxiv.org/abs/0911.4307) already study redundant information, objectivity and imperfect records. We are not deriving these ideas anew or proposing a new general law.

The restricted contribution is an **explicit comparison of two record architectures plugged into our previous subject-selector circuit**: a single noisy signal copied to both report registers versus two conditionally independent noisy probes. It separates consensus from calibrated fidelity in the very place where our model needs a subject-to-report bridge. It does not replace the literature's information-theoretic definitions of redundancy. In particular, common-source noisy reports are not a refutation of quantum Darwinism; the point is that mere numerical agreement is not by itself a calibration of what the records track.

## 1. Common experimental preparation

Prepare system qubit `S`, friend-memory registers `F,G`, and report registers `P,Q` in

```
|+>_S |0>_F |0>_G |0>_P |0>_Q.
```

CNOT `S→F` and `S→G` create

```
(|000>_SFG + |111>_SFG)/√2 ⊗ |00>_PQ.
```

All gates are standard quantum operations. Take real `a,b≥0`, `a²+b²=1`, `a≥b`. Define report states

```
|e0> = a|0>+b|1>,    |e1> = b|0>+a|1>,    r=<e0|e1>=2ab.
```

A controlled unitary uses `F` as control to prepare the corresponding state of `P`. It leaves the `F` basis states undisturbed. Two distinct architectures then produce two report registers:

- **Shared signal:** CNOT `P→Q`. The two branch-conditional report states are `a|00>+b|11>` and `b|00>+a|11>`. This copies the **computational-basis record**, not an arbitrary quantum state.
- **Independent probes:** instead apply the same controlled unitary from `F` to `Q`. The branch-conditional report states are `|e0>|e0>` and `|e1>|e1>`.

In the shared-signal setup, the two readouts can be stored separately, but their noise comes from the same initial signal. In the independent-probe setup, the two computational-basis readout errors are conditionally independent **given a Z-basis branch preparation or Z readout**. They are not generally independent without conditioning: the branch value is shared.

## 2. Read versus reverse

Use separately randomized trials with the **same report-writing circuit**:

1. **Read arm:** read `F,P,Q` in the Z basis. `F` is the target record; `P,Q` are reports. Estimate report agreement, each report's agreement with `F`, and their joint errors.
2. **Reverse arm:** undo `S→G` and `S→F`, but leave `P,Q` and any copies of their readouts outside the reversal. Measure `X` on `S`. Estimate the unconditional `P(X=+)`.

Report outcomes may be measured in Z and retained, or traced out, before the X measurement: without feedback on `SFG` the unconditional X marginal is the same in this setup. Do not combine a read-arm value of `F` and a reverse-arm `X` as though both had been measured in one run. Their statistics are comparisons across the specified procedures, not proof that a definite Z value and an X result jointly existed in each run.

For these circuits standard quantum mechanics gives:

| Statistic | Shared signal | Independent probes |
|---|---:|---:|
| `P(P=F)=P(Q=F)` in read arm | `a²` | `a²` |
| `P(P=Q)` in read arm | `1` | `a⁴+b⁴` |
| `P(P≠F and Q≠F)` in read arm | `b²` | `b⁴` |
| `P(X=+)` in reverse arm | `(1+2ab)/2` | `(1+(2ab)²)/2` |

The interference factors are the overlaps of the two joint report states: `r` for the common signal and `r²` for independent probes. Copying an already noisy basis signal does not improve its calibration; it creates two correlated readouts. Two separate couplings give additional branch information but leave a smaller unconditional interference factor in this ideal model. This is the known information–interference tradeoff in a specific form, not a newly discovered limit.

## 3. A concrete exact witness

Choose `a=4/5` and `b=3/5`. Then `r=24/25`:

| Statistic | Shared signal | Independent probes |
|---|---:|---:|
| Each report matches `F` | `16/25 = 64%` | `16/25 = 64%` |
| Reports agree with one another | `1 = 100%` | `337/625 ≈ 53.92%` |
| Both reports disagree with `F` | `9/25 = 36%` | `81/625 ≈ 12.96%` |
| `P(X=+)`, reports outside reversal | `49/50 = 98%` | `1201/1250 = 96.08%` |

The striking result is deliberately modest: **two agreeing reports can be copies of one fallible signal**. It does not follow that either report is a conscious subject, or that real human agreement has this architecture. Conversely, independent coupling need not be diagnosed merely by how often two reports agree. The causal architecture and independent calibration matter.

As an endpoint, if `a=b=1/√2`, two copied reports still agree perfectly but have only 50% accuracy about `F`, and `P(X=+)=1`: their common bit conveys no information about the friend record. If `a=1,b=0`, the shared reports perfectly track `F` and the X probability falls to `1/2` when they remain outside the reversal. These are analytic endpoints; the rational-amplitude verifier checks the perfect-record endpoint and four rational cases, not the irrational no-information endpoint.

## 4. Can an exact accessible selector preserve full interference?

Only under an additional, specified physical reporting condition can this be turned into a complementarity constraint. Suppose a proposed subject selector says that:

- its selected value is faithfully represented by a separately readable report of the friend-record alternative;
- the report is created by the same branch-preserving controlled interaction in both arms; and
- the report and its relevant physical traces remain outside the reversal, with no conditional feedback or postselection.

Then in the present shared-signal family, perfect calibration requires `a=1,b=0`, and the reverse arm yields `P(X=+)=1/2`, not `1`. More generally, for equally weighted two-path preparations under a specified branch-preserving report coupling, the established Englert bound is

```
D² + V² ≤ 1,
```

where `D` is the optimal distinguishability of the retained report states and `V` is the corresponding unconditional fringe visibility. A perfect record has `D=1` and hence `V=0` under those assumptions. The unconditioned `X` probability in our phase-aligned circuit is `(1+V)/2`.

This gives a directly usable **conditional operational gate**. For balanced branch preparations, if a specified retained report predicts the read-arm value `F` with accuracy `A≥1/2`, then `D≥2A−1`. With the same coupling and no postselection or feedback,

```
P(X=+) ≤ 1/2 + √[A(1−A)].
```

The shared-signal witness saturates this bound: `A=16/25` permits `P(X=+)≤49/50`. This does not assume that the two arm outcomes are jointly observed. It does require that the report states in the calibrated read and interference trials arise from the same declared interaction, and it does not identify the reported bit with an experience. Conditional quantum-eraser subensembles, feedback, altered interactions, or bringing all report carriers inside the reversal are **different protocols** and need separate analysis.

This does not refute a subject ontology whose events lack an external persistent report, or one that changes the physical laws. It is also not a theorem that the existence of an experience entails collapse. It says that a specific proposal for a **durably accessible, faithful quantum record** must pay the associated interference cost in this circuit. The earlier hidden `λ` table did not furnish such a reporting instrument, and the current quantum instruments **do not reproduce** its perfect-agreement/perfect-interference joint claims.

Before any report is measured or copied to an uncontrolled environment, the report-writing unitaries can themselves be coherently undone, followed by the friend-memory reversal. The verifier checks that the entire state then returns to its initial form and `P(X=+)=1`. This recovery resets `P,Q`: it is **not** a way to retain their readable values while also preserving the full interference. If actual readout has left further traces, those carriers must also be included in whatever quantum reversal is claimed.

## 5. Bridge to real subjects and empirical work

A test of an experience theory would require independently specified answers to all of the following:

1. **Target:** what physical operation, if any, connects a report to the candidate subject's experience rather than merely to a computational record `F`?
2. **Accuracy:** on which trials and by which independent standard is the mapping calibrated? Perfect agreement between two reports is not itself that standard.
3. **Dependence:** are the two reports independent probes, copies of one source, or neither? Calibrate common-mode errors and uncontrolled copying.
4. **Reversal:** exactly which memories, probes and later traces remain outside it? Check state preparation and read/reverse procedures across randomized trials.
5. **Prediction:** what quantitative difference does the subject proposal make from ordinary quantum mechanics and plausible background decoherence? The [collapse-identifiability gate](CONSCIOUSNESS_COLLAPSE_IDENTIFIABILITY_GATE.md) explains why observing reduced coherence alone does not identify a consciousness-triggered mechanism.

Even a successful engineered-qubit experiment would test the declared circuit and any added physical prediction; it would **not** establish phenomenal consciousness in those qubits. The two subject slots, their identity, the Born/self-location measure and the reality of a particular experience remain open. Likewise, nothing here settles Local Friendliness, nonlocality, relativity, emergent spacetime or the problem of time.

## Verification

Run [`verification/shared_vs_independent_reports.py`](verification/shared_vs_independent_reports.py). It calculates five-qubit amplitudes using exact rational arithmetic, directly checks the joint `F,P,Q` read laws and X statistics, and verifies coherent recovery **before readout**. Its [JSON receipt](verification/shared_vs_independent_reports.json) includes all four checked rational cases. The continuum formulas follow for the specified controlled rotations; these finite checks do not prove a general theorem about observers or experience.
