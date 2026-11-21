# The selected subject's context: exact relational dynamics and its limits

## Result

The subsequent [Kemeny–Snell audit](KEMENY_SNELL_REVERSIBLE_WEAK_LUMPABILITY_AUDIT.md) checks the same kernel is regular and reversible and applies the book's Theorem 6.4.8: in this specific model the non-lumpable projections cannot be made homogeneous first-order Markov by any special initial distribution. This is stronger than the original all-initializations result, but does not exclude an open subject or a history-dependent model.

In the existing E-L sector at `t=1/4`, the original one-update L rule selects two outer pairs. For the left pair, however, neither the **complete two-spin state** `(s0,s1)` nor its candidate qualitative bit `q01` determines a universal first-order stochastic evolution under the same four-spin heat-bath law. Two fine states with identical left-pair state have different probabilities of the next left mismatch. Moreover, even at equilibrium, the preceding mismatch gives information about the next mismatch beyond the current one.

There is a constructive physical repair in this particular model: retain **all three edge mismatch bits** `(q01,q12,q23)`. Their projected dynamics is an exact first-order Markov chain for every initial distribution, because the only two spin configurations with the same three bits differ by a global sign flip, a symmetry of the kernel. Among subsets of those edge bits containing `q01`, neither of the two-bit alternatives is similarly closed. This is an exact relational predictive representation, **not** a theory of phenomenal unity, an assertion that the whole is one subject, or a proof that a subject must be dynamically closed. An open subject can depend on its environment.

The contribution is an application of known Markov aggregation theory to the existing candidate, with an explicit alternative to mistaking local closure for subjecthood. It does not pass B4–B5/F2. Experience is a valid datum, and C3 remains **full structural and experiential intelligibility**, jointly with C1–C7. No real person, string vibrations, felt discomfort or physical intervention is modeled as observed here.

## 1. What is actually being tested

The [integrated candidate](INTEGRATED_EXPERIENTIAL_MISALIGNMENT_CANDIDATE.md) uses the same four-spin `P_t` and randomly chosen single-site heat-bath update analyzed in the [horizon audit](INTEGRATED_SUBJECT_HORIZON_AND_VALENCE_AUDIT.md), with `t=1/4`. One update is a specified **local model operation**, not a universal clock or a claim that the timeless whole becomes actual over time. The two left spins have an internal edge coupling `1/2`; spin 1 also couples to environmental spin 2 with `t=1/4`. Define `q_ij=(1−s_i s_j)/2` for each edge.

The proposed E-L incidence and `q=1` unpleasantness for the left pair are independent postulates. Ask only this physical question: is there one stochastic matrix on the proposed retained physical variables that reproduces the next-step projected distribution **for every fine-state initialization**? This is universal first-order predictive closure, stronger than a good approximate prediction in a particular preparation. It is not a necessary condition for being a subject, persistence, consciousness, moral standing or an experiential identity.

For a partition of fine states, the standard **strong lumpability** condition is equality of total transition probability into each output block for every two fine states in the same input block. It is necessary and sufficient for a common projected Markov kernel under every initial distribution. We apply it to the already-specified kernel; no general priority is claimed. The [fixed calculation plan](INTEGRATED_SUBJECT_CONTEXT_DYNAMICS_PLAN.md), [code](verification/integrated_subject_context_dynamics.py), [tests](verification/integrated_subject_context_dynamics_test.py), and [receipt](verification/integrated_subject_context_dynamics.json) give the details. The two-bit relational projections were added as an exploratory follow-up after the originally planned comparison; no empirical data were inspected.

## 2. A same-local-state witness and a quantitative prediction limit

Use the two initial fine states

```text
A = (−1, −1, −1, −1),    B = (−1, −1, +1, −1).
```

They have exactly the same left-pair physical state `(−1,−1)` and the same mismatch `q01=0`, but a different setting of the adjacent external spin. Under **the same unmodified heat-bath kernel**,

```text
P(next q01 = 1 | A) = 5/48,
P(next q01 = 1 | B) = 17/112,
difference              = 1/21 ≈ 0.047619.
```

The context is not merely a different encoding: spin 2's relation to spin 1 differs, changing the physical input to spin 1's update. These are conditional model probabilities for fixed initial states, not measured outcomes. If an experiment could faithfully prepare either A or B and then implement the identical model kernel, this is its hypothetical physical prediction; observational conditioning is not by itself a realized intervention.

Any single q-only or left-state-only probability prediction must give the same number for A and B. By the triangle inequality its worst absolute probability error over this pair is at least half the gap, `1/42 ≈ 0.02381`. The midpoint attains that bound for the two contexts; this is a **minimax bound for these conditional probabilities**, not a confidence interval or a bound on experience. In fact, exhaustive state comparison shows `1/21` is the maximum one-step total-variation difference for both the left-state and q-only projections in this finite model. At the disconnected control `t=0`, both maxima are zero. Disconnecting an edge in a formal control does not imply that any real subject was separated.

## 3. Even an equilibrium fit can miss memory

The stationary one-step transition of the left mismatch was already calculated in the horizon audit. Here we add a three-observation calculation using the **same stationary initialization**. All four conditioning events have positive probability:

| Previous q | Current q | P(next q=1 | previous, current) |
|---:|---:|---:|
| 0 | 0 | 2407/19824 ≈ 0.121418 |
| 1 | 0 | 1741/13776 ≈ 0.126379 |
| 0 | 1 | 8713/13776 ≈ 0.632477 |
| 1 | 1 | 15143/23856 ≈ 0.634767 |

For the same current `q=0`, the exact difference is `12/2419 ≈ 0.004961`; for current `q=1`, it is `20/8733 ≈ 0.002290`. The unconditional-in-history stationary predictions are `P(next q=1 | current 0)=41/336` and `P(next q=1 | current 1)=71/112`. Thus the process fails the **first-order Markov property even in this stationary ensemble**, not merely the stronger all-initializations condition. These small values are exact consequences of this model, not evidence that such memory is detectable in a brain. At `t=0`, both history contrasts are zero and q is strongly lumpable.

The likely mathematical explanation is hidden contextual state: past q observations alter the conditional distribution of unresolved spins/edge relations. The calculation establishes the transition dependence, not a uniquely identified mechanism in a real biological system. It does not rule out an effective approximation, an explicitly history-dependent law or a different local time grain.

## 4. Exact repair by relational context—and what it costs

The table reports the maximum one-step total-variation discrepancy between projected next-state distributions, over all pairs of fine states in the same current projected block. A zero for the finite chain establishes the strong-lumpability block condition; a positive value disproves it for that projection.

| Retained variables | `t=1/4` maximum discrepancy | `t=0` control |
|---|---:|---:|
| Left physical spins `(s0,s1)` | 1/21 | 0 |
| Left mismatch `q01` | 1/21 | 0 |
| Left and middle mismatches `(q01,q12)` | 5/42 | 1/8 |
| Left and right mismatches `(q01,q23)` | 2/21 | 0 |
| All edge mismatches `(q01,q12,q23)` | 0 | 0 |

Adding a variable can increase this maximum because the output being predicted also changes: the first two-bit row must predict the middle edge as well as the left one. Thus the numbers do **not** establish that adding information makes prediction worse on a fixed target. At `t=0`, the middle–right edge dynamics can still depend on the omitted right relation, even though the left pair is disconnected and its own q projection closes.

The three-bit result has a simple independent reason: on this chain, its edge products determine all four spins up to a simultaneous sign reversal, and the model transition law commutes with that reversal. So fine states in a common edge-bit block have identical projected transition distributions. This is a symmetry quotient for the declared model, not a general claim about all relational physics. It preserves the complete **edge-mismatch** trajectory law, not the absolute sign or every possible physical observable; for example it cannot recover which globally flipped spin state occurred. Both one-bit and two-bit subsets containing `q01` fail here, so the three-edge representation is minimal **only within this tested family of retained edge subsets**. A different macrostate, external input or memory model might be equally or more efficient.

This gives the candidate a precise choice rather than an automatic defeat:

1. Treat each selected pair as an **open** subject whose physical evolution depends on specified environmental inputs; supply a defensible theory of why that open process is one subject.
2. Use an effective **memory-dependent** local dynamics, specifying its initialization and transport conditions; do not claim an exact autonomous first-order pair law.
3. Use the exact three-edge quotient for physical mismatch prediction; explain separately whether its global context constitutes one, two, overlapping or other subjects and how local qualities attach.

The quotient does not choose among these subject answers, and adding physical information does not entail adding phenomenal unity. Conversely, a subject might encompass relations beyond an autonomous predictive subsystem. In the [nine-update quality extension](INTEGRATED_CROSS_SCALE_SUBJECT_QUALITY_GATE.md), the three edge bits calculate a stipulated whole score, but that does not make the nine-update selector physically or phenomenally correct or identify it with either one-step pair. Persistence, identity through changes, valence and subject-reference-class measure remain independent obligations.

## 5. Literature, status and reproducibility

The strong-lumpability criterion is established mathematics. Ganguly, Petrov and Koeppl, [*Markov chain aggregation and its applications to combinatorial reaction networks*](https://arxiv.org/html/1303.4532v2), state the block-sum criterion and distinguish weak from strong lumpability. **Only their abstract and introduction were read** for this application; the later proofs, case studies and figures were not inspected. Kemeny and Snell, [*Finite Markov Chains*, sections 6.3–6.4](sources/uploads/Kemeny_Snell_Finite_Markov_Chains.pdf), are the historical cited source: at the time of this calculation only search excerpts were available. The later [supplied-book audit](KEMENY_SNELL_REVERSIBLE_WEAK_LUMPABILITY_AUDIT.md) reads those sections and visually checks the key proofs, including Theorems 6.3.2 and 6.4.8; the rest of the book was not systematically inspected. Neither source is a consciousness or subject-incidence assay.

Run `PYTHONPATH=verification python -m unittest -v integrated_subject_context_dynamics_test` and `PYTHONPATH=verification python verification/integrated_subject_context_dynamics.py`. The targeted tests include an independent dense-matrix recomputation of the stationary history table and exhaustively check global-sign kernel symmetry. They verify the encoded finite model, not the truth of its assumptions or the framework's battery.

**Battery:** B4/F2 remains open because selected physical sets and stable projected dynamics do not constitute or persist as subjects by themselves. B5 remains open because the qualitative identity is postulated and the new physical memory result does not show what a state feels like. B9/F3 remains open because stationary model weights do not provide a subject measure. B10 remains open because no validated experiential assay or experiment was performed. The external foundation battery cannot be independently replayed from the unavailable original artifacts. The next required gain is an independently motivated or empirically anchored bridge that discriminates subject incidence and felt quality, not another mathematical closure criterion presented as one.
