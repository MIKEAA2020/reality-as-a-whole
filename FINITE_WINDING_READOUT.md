# Finite winding clock: calibration, erasure and readout bias

**Result:** a specified finite constrained history can reproduce the previous ideal two-clock comparison on an interior window, with a finite counter, a reversible wrap flag, an explicitly complete noisy instrument and a quantified readout bias. This is an illustrative calculation using established history-state and measurement-instrument methods, not a new general result, a cold-atom prediction, an autonomous device or a solution of quantum gravity. The previous ideal construction is [INFINITE_WINDING_COUNTER.md](INFINITE_WINDING_COUNTER.md); exact rational checks are in [verification/finite_winding_noise.py](verification/finite_winding_noise.py) and [its output](verification/finite_winding_noise.json).

The chronological path and its gate schedule, uniform finite history, initial counter calibration, system unitary, readout and measurement coupling are **supplied**. The model makes those inputs and their consequences explicit; it does not derive time or the absolute from a finite register.

## 1. Finite phase history and reversible counter

Choose K≥2 and an open clock path with vertices `(w,r)`, where `w=−K,...,K` and `r=0,1,2,3`. It has `T=4(2K+1)` vertices. Define the centered root as `(w,r)=(0,0)` and q readings `q_r=(1,0,−1,0)`. Unlike a cyclic four-vertex clock, this path already distinguishes windings and has boundaries.

The counter has `M=2K+3` states labelled `c=0,...,M−1` and a flag f∈{0,1}. Its forward gate is the permutation

    G|c,f> = |(c+1) mod M, f XOR 1_(c=M−1)>.

Thus one forward wrap from `|M−1,0>` reaches `|0,1>`. G is unitary; its inverse decrements c and toggles f exactly when crossing from 0 to M−1. The one-bit flag is **not an irreversible latch**: after two complete wraps it returns to its initial value. A readout can also erase the flag. For the designated initial states and the finite clock window below, no physical wrap occurs, so no claim about an observed overflow rate follows.

Use the qubit step

    U = [[3/5,−4/5],[4/5,3/5]].

On each path edge advance the qubit by U. At edges r=3→0 also apply G; on reverse edges apply the inverses. With V_(w,r) the ordered transport from the centered root,

    C_path = sum_edges B_e B_e† ≥ 0,
    B_e = |source>⊗I − |target>⊗W_e,
    J|ψ> = (1/√T) sum_(w,r) |w,r>⊗V_(w,r)|ψ>.

As in [RELATIONAL_TIME_CONSTRUCTION.md](RELATIONAL_TIME_CONSTRUCTION.md), `ker C_path=range J`; this is the standard open-path history construction, not a new theorem. Its finite, uniform vertex weight follows from the stated J and is not a fundamental probability distribution over all time. The finite history state is normalizable and exactly satisfies its **own** open-path constraint; it is not an exactly invariant state of the distinct infinite-shift constraint.

## 2. Physical calibration sector

At the root prepare the flag as zero and counter c=`K+1+d`, with d=0 or d=1. The offset d=1 has probability λ∈[0,1]. The initial root can be a mixture or a coherent superposition of these two offset alternatives tensored with qubit |0>; the measured probabilities below are the same for both because the declared instrument records the counter.

For all vertices in the finite window, the two prepared branches stay within the counter range without wrapping:

    c = K+1+d+w,    f=0,
    qubit = U^(4w+r)|0>.

Thus the physically reported centered counter reading is `m=c−(K+1)`, and on this restricted sector `m=w+d`. The phase and counter act as partial clock readings. The path's endpoints and the counter origin remain chosen inputs; the flag gate is not demonstrated hardware.

## 3. A complete declared instrument

The reported outcomes are a phase r, a qubit result x∈{0,1}, and either a counter/flag reading `(y,f)` or erasure `?`. Given the true `(c,f)`, define classical readout probabilities

    Pr(?|c,f)=ε,
    Pr((c,f)|c,f)=(1−ε)(1−δ),
    Pr(((c+1) mod M,f)|c,f)=(1−ε)δ,

with `0≤ε,δ≤1`; the flag is correctly reported when the result is not erased. These are **assumed readout error rates**, not fitted or measured. The slip here is a reporting error, not the G gate. Let `P_(c,f)` project on the counter/flag state and `P_x` on the qubit result. A valid physical-root Kraus family is

    K_(j,c,f,y,x) = sqrt[Pr(y|c,f)/T] · V_j† (P_(c,f)⊗P_x) V_j,

where j=(w,r), and Pr includes the three outcome types above. Group j,c,f as hidden Kraus labels and report only `(r,y,x)`. Summing `K†K` over all j,c,f,y,x gives I. The hidden record stores more than the user-facing result; its preparation and later disposal are not free resources supplied by a physical device. Lifting the root Kraus operators with J and adding `I−JJ†` as an off-physical-sector outcome gives a complete finite kinematic instrument. This is one declared implementation; the same effects could have other backaction.

For a coherent initial offset superposition, the hidden counter record makes the nonselective reduced offset state diagonal in d. For equal amplitudes, its trace distance from the initial pure offset state is 1/2. Thus discarding the record here is not an innocuous change of notation. It is not a theorem that every clock readout destroys this coherence.

## 4. The exact comparison with the infinite idealization

Set phase r=0 and report `(y,f)=(K+1,0)`, i.e. reported centered m=0. Because K≥2, the two true counter values that can produce this report, m=0 and m=−1, are inside the declared window for both d=0 and d=1. Define

    p₁ = |<0|U^(−4)|0>|² = 277729/390625,
    p₂ = |<0|U^(−8)|0>|² = (164833/390625)².

Conditioned on this non-erased report, the qubit result x=0 has probability

    p_noisy = (1−δ)[(1−λ)+λ p₁]
             + δ[(1−λ)p₁+λ p₂].

The first bracket is the perfect-counter result, identical on this window to the corresponding [infinite-clock example](INFINITE_WINDING_COUNTER.md). The second arises when the true reading was m=−1 but slipped upward to 0. This is the declared noisy instrument applied to a *particular reported-clock event*, not an assertion that distinct physical events are identical.

For K=2, λ=1/2, δ=1/10 and ε=1/5:

- perfect-readout conditional probability: `334177/390625 ≈ 0.85549312`;
- noisy conditional probability: `621334959941/762939453125 ≈ 0.81439616`;
- change: approximately **−0.041097**;
- joint probability of phase 0 and this non-erased report: `(1−ε)/T = 1/25`;
- overall erasure probability: `ε=1/5`.

The factor `1−ε` cancels from this conditional comparison because the assumed erasure rate is independent of the counter state; ε=1 gives no non-erased event and the conditional probability is undefined. State-dependent erasure, additional counter noise or different clock weights can change the result. For the above p₁,p₂ and any λ∈[0,1],

    |p_noisy−p_ideal| ≤ δ(p₁−p₂) ≈ 0.53292547 δ.

The bound is attained at λ=1 for this model. It is not a universal clock-noise bound or a statistical confidence interval.

## 5. What a flag and an apparent clock discrepancy do—and do not—show

For the separately prepared boundary state `|M−1,0>`, **one** G application yields `|0,1>`. If the above erasure readout is applied immediately, the flag is correctly visible with probability `1−ε` and the result is unknown with probability ε; a counter-label slip does not change the flag in this model. Two full wraps can reset the flag, and the prepared λ-sector on the finite path never wraps at all. Nothing here derives permanent storage, true overflow frequency, apparatus energy, independent calibration, or a reset procedure.

A noisy counter report selects a mixture of clock events. It can shift an inferred conditional statistic even though the underlying system evolution is unchanged. For the same *anchored* physical event, states, effects and instruments still have to be transported together as in [CLOCK_CHOICE_EQUIVALENCE.md](CLOCK_CHOICE_EQUIVALENCE.md); the difference above compares different reported-clock selections and is not a violation of that equivalence.

The model connects bounded history, calibration uncertainty, a finite reversible counter and a complete quantum instrument. It does **not** establish an observer-independent universal clock, a unique entropic time, a Barontini data fit, finite detector backreaction in gravity, or phenomenally experienced succession. The next empirical step is a predeclared uncertainty-aware comparison using actual experimental observables and their acquisition process; the released Barontini traces do not independently reconstruct the entropy estimator. An autonomous finite-memory clock and its energy/record dynamics remain a distinct physical construction.
