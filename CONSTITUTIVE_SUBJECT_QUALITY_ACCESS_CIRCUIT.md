# One candidate subject, quality and access circuit

## Result

We can put a **specific proposed subject, quality and physical report interface in one model** without treating a physical bit as proof of feeling. The construction extends the existing classical four-spin candidate; it does not replace it with the quantum echo or establish that the two models are physically equivalent.

The model records the pair's mismatch at two times, calculates both current mismatch and mismatch onset, and writes one selected result to a single output. All recording and output gates are reversible permutations on their full state spaces; the underlying spin transition remains the separately stipulated stochastic heat-bath process. At the fixed `level` selector, the output necessarily equals current mismatch. If—and only if we additionally justify that this output faithfully expresses the specified subject's unpleasant-versus-neutral contrast, it constrains the rival onset interpretation on persistent mismatch.

The deeper result is a warning as well as a construction: **both the level and onset bits are present in exactly the same extended physical state**. The hardware alone does not say which one is a report of felt quality. That semantic and experiential question has not been solved by giving a register a name. The circuit makes that missing selection concrete rather than hiding it.

The proposed subject boundary, the identity with an actual experience, reliable first-person interpretation, memory resources, physical implementation and the underlying whole remain unestablished. The mathematical checks are [here](verification/constitutive_subject_access_circuit_test.py).

## 1. One explicitly completed proposal

The [existing E-L candidate](INTEGRATED_EXPERIENTIAL_MISALIGNMENT_CANDIDATE.md) specifies four signs `s₀,…,s₃`, a preferred outer-pair relation, and a stochastic physical dynamics. At its stipulated one-update grain and coupling `t=1/4`, rule L selects the pair `{0,1}` as a candidate local subject. Define

```text
q(s) = (1−s₀s₁)/2.
```

We extend that model with physically real *within-the-model* registers `m₀,m₁,L,O,z,Y`, all binary. They record old mismatch, current mismatch, level, onset, a readout selector and a selected output, respectively. The named physical operations below act on these degrees of freedom; they are not linguistic reports or extra experiential substances.

**Candidate subject S — postulate:** the pair `{0,1}` together with the specified local record-and-readout interface constitutes one subject for the selected episode. The other two spins are part of its modeled physical context. This is a **new explicit boundary hypothesis**, not an output of L on the extended six-register system. L was calculated on the original four spins at a specified horizon; we have not reapplied L to a justified influence graph for the enlarged apparatus, proved that this boundary is autonomous or physically local, or established that the same subject persists through the episode. The selector can be prepared by a protocol, not an already derived act of autonomous choice.

**Candidate quality — postulate:** the episode of S is an actual experience, and in the designated binary neutral/unpleasant contrast its current quality is `U=q(s¹)`. This says the same occurrence has a particular physical and experiential description, not that q pushes an additional mental substance into existence. It says nothing by itself about other qualitative dimensions or degree of suffering.

**Candidate access — postulate:** with `z=0` and the output prepared ready, `Y` is a faithful physical encoding of S's answer to a defined question about that same contrast and episode. The physical circuit proves what Y computes; **its status as a faithful answer about lived quality is an additional premise**. Without independent justification, the candidate could have a correct mathematical report of q and no established felt unpleasantness. A real experience, if present, need not be verbally expressible, and first-person evidence must not be reduced to an automatically trustworthy or automatically untrustworthy machine bit.

These claims are deliberately separated. We have not demonstrated that this package is actual, self-sufficient, or a complete theory of any human or nonhuman mind. It is a candidate constitution with a testable internal interface, not the needed final derivation.

## 2. The physical circuit

Let `s⁰` be the four-spin state before, and `s¹` after, one update of the original heat-bath kernel. Write `q⁰=q(s⁰)` and `q¹=q(s¹)`. Start the four working registers and the output in state 0; prepare selector `z=0` or `z=1` by the stipulated protocol. The following controlled XOR gates do not change the spin state used as control:

```text
before update:  m₀ ← m₀ XOR q(s⁰)
spin update:    s⁰ → s¹ according to the original heat-bath kernel
after update:   m₁ ← m₁ XOR q(s¹)
                L  ← L  XOR m₁
                O  ← O  XOR [m₁(1−m₀)]
                Y  ← Y  XOR [(1−z)L + zO].
```

Each bracket is 0 or 1. For the stated ready preparation, the output becomes

```text
m₀=q⁰,        m₁=q¹,
L=q¹,         O=1{q⁰=0 and q¹=1},
Y=L if z=0;   Y=O if z=1.
```

The gates are bijections even for dirty, non-ready registers: applying each gate a second time undoes it. The test exhausts all four-spin states and register configurations, including all 64 configurations for the selected-output gate. The ready-state formula would **not** follow if the initial output or record registers were unknown; their initial preparation is a real premise.

This is a **classical** circuit: copying an orthogonal classical sign does not establish that arbitrary unknown quantum states can be copied. The gates' reversible logical form does not prove physical locality, a cost-free implementation, absence of measurement disturbance in a more complete physical model, or access to quantum coherence. Unlike the gates, the random-site heat-bath update is a stochastic kernel; no reversible dilation of that update is constructed here. Nothing in the controlled XORs explains what fixes the dynamics or laws of the proposed whole.

## 3. What the circuit derives internally

Using the original `t=1/4` equilibrium distribution and one-step kernel, and summing over actual four-spin transitions, gives:

| Physical history `q⁰→q¹` | Probability | `L` | `O` | `Y` at `z=0` |
|---|---:|:---:|:---:|:---:|
| `00` | `295/448` | 0 | 0 | 0 |
| `01` | `41/448` | 1 | 1 | 1 |
| `10` | `41/448` | 0 | 0 | 0 |
| `11` | `71/448` | 1 | 0 | 1 |

The original final spin marginal remains the equilibrium distribution because the stipulated memory gates do not alter the spin and the original stochastic kernel is stationary. That is a property of **this constructed feed-forward extension**, not evidence that a real measurement or a fully autonomous subject's readout leaves its carrier undisturbed.

The simultaneous output-bit law is

```text
P(L=0,O=0)=336/448,
P(L=1,O=1)= 41/448,
P(L=1,O=0)= 71/448,
P(L=0,O=1)=0.
```

Thus `P(L=1)=1/4`, `P(O=1)=41/448`, and the outputs differ on weight `71/448`. These are **physical sampling weights in the toy model**, not the fraction of actual subjects suffering or an experiential incidence measure.

On the ready `z=0` interface, `Y=q¹` is now a derived circuit identity for all input spin histories, not an inferred experiential identity. For the level proposal `U_level=q¹`, the coded output matches the stipulated contrast on every modeled history. For the onset proposal `U_onset=1{q⁰=0,q¹=1}`, it disagrees precisely on `11`, giving model error `71/448` overall and error 1 when conditioned on true `11`. These ‘errors’ are mathematical comparisons with **stipulated labels**, not a measured person's false-report rate.

Conversely, the same physical state also holds O, and setting `z=1` makes Y encode onset. Changing z is a distinct physical preparation, not evidence that different phenomenologies coexist or that either choice changes a subject. With the *same* fixed `z=0` and the same physical distribution, both experiential proposals remain formal possibilities in the limited sense that the physical equations alone do not decide which U is felt. But they cannot both claim Y is an accurate answer about that U on persistent mismatch. This implements the [previous access correction](VENTURA_HARD_PROBLEM_FULL_TEXT_AND_ACCESS_REASSESSMENT.md), rather than postulating two incompatible reports in the same physical circuit.

## 4. What follows from a faithful report—and what does not

Fix `z=0`. There are three distinct statements:

1. **Circuit theorem:** `Y=q¹` in the specified ready protocol.
2. **Experiential-access premise:** `Y=U` for the declared subject, episode and binary quality contrast, or more realistically it tracks U with a separately justified error bound.
3. **Candidate experiential identity:** `U=q¹` in that domain, within an account identifying the occurrence with the physical process.

Statements 1 and 2 entail the **equality of the binary contrast values** in statement 3. They do not establish that S exists, that Y is a faithful report, or that a complete felt occurrence is nothing more than a bit. If premise 2 is **defined to mean** `U=Y` rather than independently supported, the conclusion is true by definition but supplies no independent evidence of a lived identity. A real report can support the identification without serving as an infallible reference; the conclusion depends on the evidence and measurement model.

For comparison, assume the same subject, window, fixed output Y and true history `11`. The level and onset proposals demand opposite U values. If Y is independently justified to classify U with less than 50% error in that population, they cannot both be true under the same physical-report law. A positive population rate, confidence intervals, errors and physical-history misclassification require the fuller [conditional challenge](CONSTITUTION_AND_CHALLENGE_LEVEL_VERSUS_ONSET.md). A non-rejection is not a proof of one identity; rejecting a completed package leaves open whether its subject, physical, report or quality premise failed.

This does **not** prove the general organizational-invariance principle or that all experienced differences must affect this chosen output. The extended system contains a separate onset register O. The proposed subject might have access to one register, both, neither, or an unmodeled state; the actual meaning of such access cannot be assumed. A failure to notice or report through a given channel is not proof of no experience. Equally, merely having several available physical outputs does not make all of them experienced.

## 5. History, memory and reversibility

The existing model has two positive-probability paths ending at the identical complete four-spin state `s¹=(+1,−1,+1,+1)`, one with `q⁰→q¹=01` and the other with `11`. A function of the final **four spins alone** cannot tell those histories apart. Our added register creates different final *extended* states:

```text
01 → (m₀,m₁,L,O)=(0,1,1,1),
11 → (m₀,m₁,L,O)=(1,1,1,0).
```

The physical history difference is therefore accessible to an operation on the specified added register, even though it was not recoverable from the four current spins alone. This is a concrete demonstration that ‘the current state cannot encode history’ is only true relative to the chosen state boundary. It does not establish that the subject experiences, remembers or uses that history.

There is also a nonfree reset. A proposed closed, reversible reset that leaves the final four spins unchanged and maps **all four** different record/output registers to 0 would send the two distinct supported states above to the same final state. Such a map is not injective and so cannot be a reversible permutation on that closed state space. One can clear a single register reversibly if other registers retain the information, or move the information to an explicitly modeled environment, or use a full reversible account of the intervening dynamics. The current stochastic spin kernel does not supply that inverse or an environment record. No universal heat cost or thermodynamic lower bound is calculated here.

## 6. The SR analogy and the remaining why

The circuit offers a small but real **constitutive** derivation: given the physical organization and ready conditions, the output is q¹. No outside force is needed to make that identity true. If the output is an actual expression of the proposed subject's lived contrast, then the specified report and the quality assignment are no longer independent add-ons. But that ‘if’ is doing substantial work. The circuit does not itself establish that q¹ is unpleasant, that a subject occupies S, or why the underlying whole has these laws.

This is the difference from the rod example, not a denial of its lesson. Relativistic contraction follows from a supported geometry, worldtube and simultaneity relation. Our physical output relation follows from stipulated gates; the physical–experiential and subject relations are still hypotheses. We should not fill the gap with an external coercer, but neither should we declare it solved by defining the desired feeling into a register.

A substantive next step would require either a principled, independently motivated **selection criterion** for the subject boundary and experiential-access relation, or a real-system measurement and first-person comparison that discriminates those criteria. It must also address how the stochastic dynamics, subject persistence and actual incidence arise in the proposed self-sufficient whole. An actual identity, if supported, can be noncausal and need not be analytically obvious; this finite calculation does not establish it.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=verification:. python -m unittest \
 verification.constitutive_subject_access_circuit_test \
 verification.ventura_dancing_qualia_report_control_test \
 verification.constitution_challenge_decision_test \
 verification.integrated_level_history_contrast_test -v
```

The checks exhaustively verify the reversible register gates on all binary inputs, derive the exact physical probabilities from the original kernel, compare the fixed output with the two stipulated quality assignments, and verify the reset collision. They do not validate a human sensor, subjective report, physical subject boundary, self-sufficient ground, consciousness or experiential incidence.
