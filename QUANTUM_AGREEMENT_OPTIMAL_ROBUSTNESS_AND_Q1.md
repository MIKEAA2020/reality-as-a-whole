# Optimal symmetric agreement stability and the Q1 boundary

## Main results

This note strengthens the preceding [robust-agreement gate](ROBUST_QUANTUM_AGREEMENT_AND_RARE_RECORDS.md). Its claims concern a bipartite two-setting, two-output box and **one specified pair of selected outcomes**, not every general definition of common certainty.

1. **Sharper stability bound.** If a box admits the first-level NPA (`Q1`) positive-semidefinite moment matrix, the difference between the two designated conditional estimates obeys

   ```text
   |q_A−q_B| ≤ [ √e/2 + √(min(p,s) t) + |p−s|/2 ] / max(p,s).   (1)
   ```

   This is often much tighter than the earlier bound. Definitions and proof follow below. `p,s` must be positive; all quantities are model probabilities, not sample counts. The bound also holds for quantum boxes and bipartite almost-quantum boxes, because both are contained in `Q1`.
2. **Exact symmetric optimum.** If `p=s=1/2` and the target events match perfectly (`t=0`), (1) reduces to `|q_A−q_B|≤√e`. An explicit two-qubit quantum construction **saturates this bound for every `0≤e<1`**. For nonzero `e`, the selected pair occurs with positive probability and satisfies the specified approximate-certainty recursion at tolerance `e`, while the assignment gap is `√e`. Thus an improvement to linear scaling in this tolerance is impossible in this family.
3. **Not a quantum reconstruction.** The proof uses only a `Q1` Gram matrix. It therefore cannot distinguish all quantum correlations from almost-quantum ones. We give an explicit nonquantum `Q1` box with such a matrix as a control; it is not claimed to be almost-quantum.

These are analytical calculations in the stated model, supplemented by finite checks. No research-priority claim is made without a broader literature search. Neither observer roles nor record correlations identify conscious subjects or establish intrinsic experience.

## 1. Definitions and sharpened bound

Using the [earlier notation](ROBUST_QUANTUM_AGREEMENT_AND_RARE_RECORDS.md), let `A0,B0` indicate the selected setting-0 outcomes and `A1,B1` the target setting-1 outcomes. Write

```text
p=P(A0=1)>0,    s=P(B0=1)>0,
q_A=P(B1=1 | A0=1; 01),
q_B=P(A1=1 | B0=1; 10),
e=P(A0≠B0 | 00),       t=P(A1≠B1 | 11).
```

Settings in the conditions matter. A no-signaling assumption makes the stated marginals independent of the remote setting. In the original paper's bit labels, the selected setting-0 outcomes can be denoted `a=b=0`; the indicators here take the value **1** when the corresponding selected outcome occurs. These are two notations for the same events.

### Q1 Gram proof

By the standard first level of the [NPA hierarchy](https://arxiv.org/abs/0803.4290), a `Q1` box admits a positive-semidefinite moment matrix indexed by the identity and the four selected one-party projectors. Equivalently, there are vectors `|ψ>, |a0>, |a1>, |b0>, |b1>` such that

```text
||ψ||²=1,   ||a0||²=<ψ|a0>=p,   ||b0||²=<ψ|b0>=s,
||a0−b0||²=e,             ||a1−b1||²=t,
<a0|b1>=p q_A,            <b0|a1>=s q_B.
```

The same projector identities hold for `a1,b1`; the visible cross-party inner products are real joint probabilities. The vectors can be complex and same-party inner products need not be observable.

Define `D=p q_A−s q_B`. The algebraic identity

```text
D − (p−s)/2 = <a0−b0 | b1−ψ/2> + <b0 | b1−a1>
             = <a0 | b1−a1> + <a0−b0 | a1−ψ/2>
```

holds exactly; intermediate unobserved same-party inner products cancel. Projector normalization gives `||b1−ψ/2||=||a1−ψ/2||=1/2`. Cauchy–Schwarz in the Gram space, using the better of the two decompositions, yields

```text
|D − (p−s)/2| ≤ √e/2 + √(min(p,s)t).                           (2)
```

If `p≥s`, then `p(q_A−q_B)=D−(p−s)q_B`; if `s≥p`, then `s(q_A−q_B)=D−(p−s)q_A`. Since both assignments are between zero and one, the remaining coefficient relative to `1/2` has magnitude at most `1/2`, giving (1). Clip its right side at 1 if desired.

The proof is valid for **any** `Q1` moment completion with these observed entries; it does not require an underlying quantum state to realize the Gram vectors. The familiar hierarchy and macroscopic-locality connection are established results, not proposed here: see [Navascués and Wunderlich](https://arxiv.org/abs/0907.0372) and [Navascués et al. on almost-quantum correlations](https://doi.org/10.1038/ncomms7288). For two parties, almost-quantum `Q1+AB` lies inside `Q1`.

## 2. A saturating quantum construction

Let the shared state be `|Φ+>=(|00>+|11>)/√2` and let both target projectors be `|0><0|` on the respective qubits. For `0≤θ<π/2`, set

```text
|a> = cos(π/4−θ/2)|0> + sin(π/4−θ/2)|1>,
|b> = cos(π/4+θ/2)|0> + sin(π/4+θ/2)|1>,
A0=|a><a|, B0=|b><b|.
```

Direct Born-rule calculation gives

```text
p=s=1/2,             t=0,
e=sin²θ,              P(A0=1,B0=1 | 00)=(1−e)/2,
q_A=(1+sin θ)/2,      q_B=(1−sin θ)/2,
|q_A−q_B|=sin θ=√e.                                          (3)
```

Therefore (1) is attained for all `0≤e<1`, with a positive joint selected event. This is an **exact optimum only for the stated symmetric slice**; no optimality is claimed for general `p,s,t`.

For `0<e<1`, each observer's other setting-0 outcome has the complementary target probability, so the initial assessment sets are the singletons containing their respective selected outcomes. In the [previously specified approximate recursion](FINITE_CERTAINTY_AND_QUANTUM_AGREEMENT_TEST_GATE.md), replace certainty 1 by probability at least `1−ε`; with `ε=e`, each singleton assigns probability `1−e` to the other at setting `00`, so both are fixed points. This is an illustrative approximate-common-certainty convention, not a claim that it is the only or canonical approximation. The same box has **perfectly correlated target events** but a `√ε` gap. It follows that no universal `O(ε)` upper bound can hold for this convention and slice as `ε→0`.

At `e=0`, assessments coincide and their initial sets are not singletons; the exact agreement conclusion is recovered. For `e>0`, the 2021 theorem's *exact* common-certainty premise fails, so this construction is no counterexample to it.

## 3. Explicit Q1 box beyond quantum

The `Q1` scope is not merely formal. Use outcome values `±1` with single-party means and correlators

```text
<a0>=1/10,   <a1>=0,   <b0>=<b1>=1/(10√2),
E00=E01=E10=1/√2,      E11=−1/√2.
P(a,b|x,y)=[1+a<a_x>+b<b_y>+ab E_xy]/4.
```

All 16 entries are positive (the smallest is about `0.05555`) and the four rows normalize; the marginal formula makes the box no-signaling. It reaches the **exact** maximal quantum CHSH value `2√2` while Alice's first marginal is biased.

Here is an explicit `Q1` completion. In real three-dimensional space, let

```text
ψ=(1/10, 0, √99/10),  v_a0=(1,0,0),  v_a1=(0,1,0),
v_b0=(v_a0+v_a1)/√2,  v_b1=(v_a0−v_a1)/√2,
|a_x>=(ψ+v_ax)/2,     |b_y>=(ψ+v_by)/2.
```

All four observable vectors and `ψ` are unit vectors. Their Gram matrix for `ψ,a0,a1,b0,b1` is positive semidefinite, has the required projector diagonals and reproduces all joint probabilities. Complementary-outcome vectors are `ψ−a_x` and `ψ−b_y`; they extend it to the full first-level outcome matrix. Thus the box is in `Q1`.

It is **not quantum**: exact maximal CHSH violation self-tests the maximally entangled two-qubit strategy up to local isometries and ancillary degrees of freedom, so all four measured binary marginals are unbiased. The `1/10` bias violates that conclusion. This uses the established [CHSH rigidity/self-testing result](https://ar5iv.labs.arxiv.org/html/1209.0448); the numerical eigenvalue check alone does not prove nonquantumness. We do **not** claim this particular box is in `Q1+AB` or almost quantum.

Conversely, the noisy PR box of the preceding note with `δ=0.2` has `p=s=1/2`, `e=t=0.1`, `|q_A−q_B|=0.8`, while (1) gives about `0.76344`; it violates a necessary `Q1` constraint. Its CHSH value is `3.2`, so this is **not an independent improvement on the established CHSH test** for that box.

## 4. Consequences for the wider account

- **Do not reinvent the wheel.** Moment positivity, macroscopic locality, CHSH and rigidity are established. This is an application and a sharpened calculation in the project's selected-outcome language, not a claimed new physical principle or a complete priority survey.
- **The separation matters.** The stronger inequality holds for the entire `Q1` outer relaxation; passing it cannot establish quantum realizability, let alone a uniquely necessary quantum law. It also holds for the bipartite almost-quantum set. A real attempt to discriminate the latter from quantum theory requires additional constraints and a validated experimental protocol.
- **Rare records still matter.** The denominator is conditional on a positive outcome probability; unconditional small mismatch alone does not establish small conditional disagreement when those probabilities vanish. The [explicit classical counterexample](ROBUST_QUANTUM_AGREEMENT_AND_RARE_RECORDS.md) remains valid.
- **No metaphysical closure.** Operational box observers are not independently established conscious subjects. These inequalities do not derive an experiential ground, select subject boundaries, justify a subject measure, solve time or make the whole self-existent. The intended whole remains timeless, relational, intrinsically experiential and plural as a research proposal, without a universal subject or external simulator assumed.

The separate [quantum position-verification gate](QUANTUM_POSITION_VERIFICATION_AND_SUBJECT_LOCATION.md) applies a different set of causal, trust and adversary assumptions to timed records. Its synthetic sequential-CHSH control illustrates conditional finite-evidence certification; neither that control nor this agreement inequality proves a person or subject is at a location.

## Reproduction

Install [`verification/requirements-framework-battery.txt`](verification/requirements-framework-battery.txt) and run `OPENBLAS_NUM_THREADS=1 python verification/q1_agreement_stability_gate.py`. The [receipt](verification/q1_agreement_stability_gate.json) records 4,500 seeded random finite quantum controls, five exact-family controls including saturation, the explicit `Q1` Gram matrix construction, and the noisy-PR contrast. The random checks are not a proof of the analytical argument, a global tightness result, a test of almost-quantum membership for the constructed box, or experimental evidence.
