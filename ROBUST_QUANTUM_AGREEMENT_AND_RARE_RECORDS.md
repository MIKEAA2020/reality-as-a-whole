# Robust quantum agreement and rare records

## Result and scope

This note continues the [finite-certainty gate](FINITE_CERTAINTY_AND_QUANTUM_AGREEMENT_TEST_GATE.md). In a bipartite quantum box with two binary projective measurements per party, **approximate agreement of one selected pair of setting-0 outcomes and approximate correlation of the setting-1 targets bound the difference between two conditional assignments**. The bound is explicit and does not require the two measurements on either side to commute. It is a sufficient, generally non-tight bound on this **specified pair** of outcomes—not a complete theorem for every definition of approximate common certainty. A later [Q1 stability gate](QUANTUM_AGREEMENT_OPTIMAL_ROBUSTNESS_AND_Q1.md) sharpens the bound, proves exact optimality on one symmetric slice and identifies its broader applicability.

A quantum counterexample to an overly optimistic *classical* error bound shows that square-root dependence on the setting-0 error can be unavoidable. A separate classical example shows why rare selected outcomes need care. Neither example is an experiment, a model of conscious subjects, or a derivation of quantum theory from agreement.

**Literature and attribution.** [Contreras-Tejada et al. (2021)](https://doi.org/10.1038/s41467-021-27134-6) establish the exact agreement result for quantum boxes in their setting, already discuss robustness of quantum voids, and identify approximate common-certainty notions as future work. [Liu, Chung and Ramanathan (2024)](https://doi.org/10.22331/q-2024-10-02-1489), especially their [Theorem 4 and discussion](https://arxiv.org/html/2309.06304v4), give related almost-quantum Bell inequalities and an agreement proof extending to the almost-quantum set in the studied setting; they also discuss a correction to the earlier proof. The [distinct joint-property agreement paper](https://arxiv.org/html/2511.21258v3) studies robustness under its own assumptions; it is not the same box construction. This calculation uses standard Cauchy–Schwarz and known quantum probability rules; a comprehensive priority search has not been done, so **no claim of mathematical novelty is made**.

## 1. Explicit operational setup

Let `A0,A1` act on Alice's Hilbert space and `B0,B1` on Bob's. Each is a projector. Here `A0` and `B0` represent the particular selected outcomes in setting 0; `A1` and `B1` represent target outcomes in setting 1. Alice's operators commute with Bob's, but **within one party** `A0,A1` and `B0,B1` need not commute. The shared state `ρ` is normalized and positive. Define

```text
p = <A0> > 0,             s = <B0> > 0,
q_A = <A0 B1>/p,          q_B = <A1 B0>/s,
e = <(A0−B0)²>,           t = <(A1−B1)²>,
u = <A1>,                 v = <B1>.
```

Expectation brackets mean `Tr(ρ ·)`. Because the respective cross-party projectors commute, `e` and `t` are observable probabilities that the selected setting-0 indicators and target setting-1 indicators disagree. For binary outcomes, they are sums of the two off-diagonal joint probabilities. `q_A` and `q_B` are the box-conditional assignments obtained from settings `01` and `10`. No assumption is made that these are reports by actual agents.

Then

```text
|p q_A − s q_B| ≤ min( √(e v)+√(s t),  √(e u)+√(p t) ) =: U,   (1)
|q_A − q_B| ≤ ( U + |p−s| ) / max(p,s).                       (2)
```

The same bound can be clipped at 1. Replacing `u,v` by 1 gives the more conservative expression shown in the earlier chat. All quantities in (1) and (2) are model probabilities, not known exactly merely because a finite sample was collected.

### Why the bound holds

Using only cross-party commutation,

```text
A0 B1 − A1 B0 = (A0−B0) B1 + B0 (B1−A1)
                 = A0 (B1−A1) + (A0−B0) A1.
```

For any state, the operator Cauchy–Schwarz inequality gives `|<X†Y>| ≤ √<X†X> √<Y†Y>`. In the first line, the two terms are bounded by `√(e v)` and `√(s t)`; in the second, by `√(p t)` and `√(e u)`. This yields (1). Since `0≤q_A,q_B≤1`, either rewriting of `p q_A−s q_B` bounds `max(p,s)|q_A−q_B|` by `U+|p−s|`, giving (2). No common-certainty recursion is required for this inequality.

If `e=t=0`, cross-party equality of setting-0 indicators implies `p=s`, and (2) gives exact equality of assignments. That is the singleton-selected-event case, not an independent replacement for the general theorem on all finite-output common-certainty sets.

### Conditional rather than absolute errors

Let `r=<A0 B0>` and define `ε_A=(p−r)/p` and `ε_B=(s−r)/s`: conditional failure to find the other selected outcome given one's own in setting 0. Then

```text
e = p ε_A + s ε_B.
```

This identity makes explicit how first-order near-certainty relates to the unconditional error. Approximate first-order certainty by itself should not be relabeled as the infinite hierarchy of common certainty, especially in larger output spaces. Moreover, target mismatch `t` and outcome frequencies remain separate inputs to the inequality. A claim that probabilities are close needs an explicit bound that stays informative as the selected outcome becomes rare.

## 2. Quantum square-root control versus a classical inequality

If all four outcome indicators possess a single joint classical distribution, then pointwise

```text
|A0 B1 − A1 B0| ≤ 1[A0 ≠ B0] + 1[A1 ≠ B1],
```

and hence

```text
|p q_A − s q_B| ≤ e+t.                                        (3)
```

This is a standard type of Bell/locality constraint, not a new derivation of quantum theory. A quantum box need not have that single joint distribution.

Take the Bell state `(|00>+|11>)/√2`; choose both target projectors `A1=B1=|0><0|`, `A0=|+><+|`, and `B0=|b><b|`, with `|b>=cos θ |+>+sin θ |−>`. Cross-side copies of the basis projectors act on their respective systems. Direct calculation gives

```text
p=s=1/2,  t=0,  e=sin² θ,
q_A=1/2,  q_B=(1+sin 2θ)/2,
|q_A−q_B|=√[e(1−e)]  for 0≤θ≤π/4.
```

At `θ=π/12`, `e=(2−√3)/4≈0.0669873`, `q_A=0.5`, `q_B=0.75`. The weighted difference is `0.125`, larger than the classical bound `e+t≈0.0669873`. The refined quantum bound (2) is about `0.3660`, above the actual conditional difference `0.25`.

As `e→0`, the actual conditional difference scales like `√e`, not `e`. Thus an `O(e)` bound with a constant independent of `e` cannot hold for *all* such quantum boxes, even at fixed `p=s=1/2` and perfect target correlation. This example does **not** violate the exact theorem: for every nonzero θ, setting-0 certainty of the selected counterpart is imperfect. It does not establish any complete or optimal robust agreement inequality.

### The apparent new witness is already CHSH

The classical inequality (3) is loose. The stronger *directed* local constraints are

```text
D := p q_A − s q_B,
D  ≤ α+β,    α=P(A0=1,B0=0 | 00),  β=P(A1=0,B1=1 | 11),
−D ≤ α′+β′,  α′=P(A0=0,B0=1 | 00), β′=P(A1=1,B1=0 | 11).
```

For example, if `A0=B1=1` but `A1 B0=0`, then either `A0=1,B0=0` or `A1=0,B1=1`. Averaging gives the first inequality; the second is symmetric. Both therefore hold for mixtures of deterministic local assignments, and hence for local hidden-variable models with stochastic response functions as well. Since `α+α′=e` and `β+β′=t`, these imply the weaker (3).

More importantly, in the normalized two-setting binary box, each directed inequality is **exactly an ordinary CHSH inequality**, not merely analogous to one. Define `C_xy=< (2A_x−1)(2B_y−1) >`. For any no-signaling box, including quantum boxes,

```text
S+ = C00+C01−C10+C11 = 2 + 4(D−α−β),
S− = C00−C01+C10+C11 = 2 + 4(−D−α′−β′).
```

So `D≤α+β` is exactly `S+≤2`, and `−D≤α′+β′` is exactly `S−≤2`. These are relabelings of the established [CHSH inequality](https://doi.org/10.1103/PhysRevLett.23.880); the associated probability formulation is of the [Clauser–Horne type](https://doi.org/10.1103/PhysRevD.10.526). The identity uses common setting-wise marginals; if signaling or setting-dependent sampling is present, the experiment must model that rather than assume the same single-party expectations.

In the Bell-state example above, `D=−1/8`, `α′=e/2`, `β′=0`, and `S−=(3+√3)/2≈2.3660`. Thus the classical–quantum distinction we found is **ordinary Bell nonlocality in a particular agreement parametrization**. It is not a new Bell inequality or evidence for a physical law derived from epistemic agreement. The square-root stability check and rare-event accounting remain useful for the conditional-assignment question, but do not give an independently sourced quantum signature. The verifier checks both exact identities for all 4,500 sampled quantum models and the directed local inequalities for 5,000 classical mixtures.

## 3. Rare-event stress test

Let `0<η<2/3` and use a classical mixture of four deterministic indicator assignments `(A0,A1,B0,B1)`:

```text
(1,1,1,1)   weight η/2
(1,1,0,1)   weight η/2
(0,0,1,0)   weight η/2
(0,0,0,0)   weight 1−3η/2.
```

Then `p=s=η`, the jointly selected event has probability `η/2>0`, `e=η`, `t=0`, and `q_A=1`, `q_B=1/2`. The unconditional error `e` tends to zero while conditional disagreement remains `1/2`. This does **not** disprove a bound expressed in terms of small conditional certainty failures: here `ε_A=ε_B=1/2`, not small. Its point is precisely that a tiny error count or unconditional error rate can hide a poor selected-event conditional error when the reference event is rare.

In a real study, estimate the two marginal and joint probabilities as well as mismatch rates, with a preregistered joint confidence procedure and suitable treatment of no-clicks, selection, independence/memory, and multiple comparisons. One cannot insert empirical point estimates into (2) and call the result a confidence bound. A [separate synthetic CHSH example](FINITE_CERTAINTY_AND_QUANTUM_AGREEMENT_TEST_GATE.md) illustrates finite-sample accounting under explicit iid assumptions; neither calculation certifies exact zeros or phenomenology.

## 4. Global significance and next gate

1. A shared operational record and local quantum state impose measurable consistency constraints, but do not establish experiential identity or a universal subject. Separate subjects and subjective perspectives remain a **proposal**, not a corollary of these inequalities.
2. Since the exact agreement property can hold in the larger almost-quantum set, this property alone does not uniquely select quantum theory. The project cannot use it as a derivation of the Born rule, physical laws, subject measure or intrinsic experience.
3. The next defensible physical step is a predeclared comparison against stronger existing quantum and almost-quantum Bell/semidefinite constraints, with real data only if provenance and complete trial handling are available. A distinctive physical–phenomenal bridge and a subject-selection rule would still need independent justification.
4. The timeless whole, possibility-as-actuality thesis, substrate independence and experiential ground remain the global research target, not conclusions of this local test. No literal simulator, external creator or global clock is assumed here.

## Reproduction

Run `OPENBLAS_NUM_THREADS=1 python verification/robust_quantum_agreement_bound.py` after installing [`verification/requirements-framework-battery.txt`](verification/requirements-framework-battery.txt). The [receipt](verification/robust_quantum_agreement_bound.json) records 4,500 seeded random mixed-state bipartite models (dimensions 2×2, 2×3, 3×3), the Bell-state example and its square-root scaling, 5,000 classical mixtures, and the rare-event control. Random numerical checks and this finite sample do not prove a general theorem, establish tightness, or constitute a real experiment.
