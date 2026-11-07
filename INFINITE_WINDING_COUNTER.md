# An infinite turning clock with a correlated cycle counter

**Result:** an idealized bilateral counter removes the *specific finite holonomy obstruction* found in [FINITE_TURNING_COUNTER_INSTRUMENT.md](FINITE_TURNING_COUNTER_INSTRUMENT.md), but it does so by supplying an unbounded unwrapped degree of freedom. An exact group-averaged construction and two reductions make the tradeoff explicit. This is an application of the existing [infinite relational-clock](INFINITE_RELATIONAL_CLOCK.md) and published quantum-clock-switching methods, not a discovery of those methods, a laboratory implementation, or a solution of the problem of time. [Exact finite-support checks](verification/infinite_winding_clock.py) validate selected algebra and numerical fractions, not the full infinite-dimensional proof or physical interpretation.

## 1. An infinite lift plus a counter

Take kinematic basis vectors `|w,r,m>⊗v`, with `w,m∈Z`, `r∈{0,1,2,3}`, and `v∈C²`. Regard r as a four-phase turning readout, `q_r=(1,0,−1,0)`, w as an unwrapped winding coordinate, and m as a second counter. Supply a unitary system step U. Define the unitary shift S by

    S |w,r,m>⊗v = |w,r+1,m>⊗Uv             (r=0,1,2),
    S |w,3,m>⊗v = |w+1,0,m+1>⊗Uv.

It is a bijection of the basis followed by a unitary on the qubit. Put

    C=(I−S)†(I−S).

The important invariant is the offset `d=m−w`. In variables

    k=4w+r,  d=m−w,

S is just `|k,d>⊗v → |k+1,d>⊗Uv`. The self-adjoint offset D, with eigenvalue d, is a strong Dirac observable: its spectral projections commute with S and C. The individual winding and counter readings w and m generally do not commute with C; they are partial-clock readings, not automatically gauge-invariant observables or persistent laboratory records.

**Supplied structure:** bilateral w and m, the wrap-controlled correlation, U, and the phase split. This does not physically build a counter, derive unbounded memory or explain its calibration. Neither k nor any chosen clock is an external time for the intended timeless absolute.

## 2. Physical space by group averaging—not a uniform clock probability

S invariance in the ordinary kinematic Hilbert space `ℓ²(Z×{0,1,2,3}×Z)⊗C²` implies, for each d, constant norm at every k. Square summability forces this norm to vanish, so the ordinary `ker C` is trivial. Similarly, a normalized normal state invariant under S would assign the same weight to every k; countable normalization is impossible. These statements apply to this translation-invariant normal-state package, not to all clock states or all relational theories.

On the dense test space of vectors with finite support in k and d, define

    η(f)_d = sum_k U^(−k) f_(k,d).

The sum is finite. As in the existing infinite-clock construction,

    η(Sf)=η(f),
    sum_(n∈Z) <f,S^n g> = sum_d <η(f)_d,η(g)_d>.

Only finitely many n contribute for test vectors. The positive quotient and completion give

    H_phys ≅ ℓ²(Z)_d ⊗ C².

A normalized physical vector is `ψ=(ψ_d)_d`, with `sum_d ||ψ_d||²=1`. Its corresponding generalized invariant history has components `U^k ψ_d`, not a normalizable uniform vector over k. No probability distribution over all clock readings has been supplied. These group-averaging ideas and infinite-clock normalization qualifications are established in [INFINITE_RELATIONAL_CLOCK.md](INFINITE_RELATIONAL_CLOCK.md); they are not being claimed as new.

## 3. Two normalized ideal reductions

At a chosen winding/phase reading `(w,r)`, the physical vector is represented in the remaining counter and qubit variables by

    (L_(w,r)ψ)_m = U^(4w+r) ψ_(m−w).

At a chosen counter/phase reading `(m,r)`, represent it in the remaining winding and qubit variables by

    (K_(m,r)ψ)_w = U^(4w+r) ψ_(m−w).

For each fixed reading, both L and K are unitary maps from H_phys onto the appropriate reduced `ℓ²(Z)⊗C²`: the relabeling of d is a bijection and the relevant qubit transport is unitary. Each slice is normalized, but the family of slices is **not** a normalized probability distribution over all w or m.

For fixed w,m and common r, the corresponding frame-change map `T=K_(m,r)L_(w,r)†` acts on the remaining counter label m′ as

    d=m′−w,     w′=m−d,
    |m′>⊗v  →  |w′>⊗U^[4(w′−w)]v.

It is a unitary relabeling with offset-controlled qubit transport. A physical state and an anchored effect E must both be transformed: `E_w=L E L†`, `E_m=K E K†`. Their probabilities and the corresponding transported instrument outcomes agree by unitarity. This is an idealized exact change of reductions within one clock-neutral model. [Höhn and Vanrietvelde](https://arxiv.org/abs/1810.04153), and [Höhn, Smith and Lock](https://arxiv.org/abs/1912.00033), already develop general clock-neutral reduction and switching methods; no claim of novelty for switching is made.

## 4. An explicit offset-uncertainty witness

Choose

    U = [[3/5, −4/5], [4/5, 3/5]],
    ψ = (|d=0>+|d=1>)|0>/√2.

Compare the two relational questions at phase r=0:

- At `w=0`, the conditional qubit is `|0>` for both offset branches. The bare measurement `P₀=|0><0|` gives probability 1.
- At `m=0`, the d=0 branch has w=0 and the d=1 branch has w=−1. After ignoring the remaining winding label, the bare P₀ probability is

      (1 + |<0|U^(−4)|0>|²)/2
      = 334177/390625 ≈ 0.85549312.

More generally, if offset d=1 has probability λ and d=0 has probability 1−λ, with the same qubit input, the probability at m=0 is

    p₀(m=0)=1−(112896/390625) λ.

Thus the discrepancy varies continuously with calibration uncertainty in this specified model. This is an elementary calculation, not a new universal uncertainty law.

These are **different conditional experiments**: `w=0` and `m=0` are not the same event when the offset is uncertain. The discrepancy is not an inconsistency or a new fundamental effect. In the m=0 representation, the *same anchored w=0 event* has the offset-dependent effect obtained by transporting it with K; its probability is exactly 1. Retaining the remaining winding/offset degree of freedom preserves the full frame information; discarding it produces the indicated mixed reduced description. No irreversible physical decoherence mechanism is inferred from mathematical tracing alone.

The exact rational script checks the group-averaging identity on finite-support test vectors, offset conservation on representative edges, the frame map and inverse, and these three fractions. The formulas are analytically stated for the infinite model; the finite checks do not prove generic interacting-clock covariance.

## 5. Does this generate a clock without assuming one?

No. It answers the narrower question: **a specifically declared infinite shift model admits a correlated unbounded counter and two consistent ideal reductions, at the cost of leaving the unwrapped coordinate, counter dynamics and physical state as inputs.** The conserved offset d is a relative calibration, not a demonstrated hardware record that autonomously stores every past event. The counter has an ideal bilateral spectrum and no preparation, localization, energy or reset costs are derived. The causal interpretation of the phase and the unit step are also assumptions.

Adding m therefore changes the available relational degrees of freedom; it does not obtain unbounded time from a finite cyclic phase for free. Restricting to `m≥0` or adding an initial tick can be useful for a particular experiment, but it requires an explicit boundary/preparation and cannot be imposed while retaining the exact bilateral translation model unchanged. An actual experiment would additionally need finite-resolution instruments and clock backreaction.

## 6. Connection to the rest of the programme

- The finite cyclic example's holonomy obstruction is avoided here by replacing the four-vertex closed graph with its **infinite lift**, not by proving that a sharply initialized counter exists on the original four-vertex graph.
- The counter m can label the same toy path as the accumulated `τ/a=4m+r`, relative to an assigned calibration; that statement alone does not reconstruct the entropy estimator or sampling of [Barontini's experiment](COLD_ATOM_ENTROPIC_CLOCK_AUDIT.md).
- The invariant offset supplies a concrete place to test clock-calibration uncertainty and to distinguish clock-frame changes from discarding information. It does not provide the detector Hamiltonian and local Einstein constraints required for [recollapsing gravity](RECOLLAPSING_GRAVITATIONAL_CLOCK.md).
- A conditional record or clock parameter is not a derivation of phenomenal succession or the absolute's nature. Those remain separate obligations of the [whole-account programme](PROJECT_COHERENCE_AUDIT.md).

**Finite continuation:** [FINITE_WINDING_READOUT.md](FINITE_WINDING_READOUT.md) supplies an open 20-vertex example with a seven-state reversible counter, one flag, calibration uncertainty, a complete noisy instrument and an exact conditional-bias calculation. It reproduces the ideal comparison when the readout is perfect on the selected interior window, but still assumes its clock path, uniform history and instrument. Autonomous dynamics, observed experimental rates and comparison with published clock-switching and record work remain necessary before asserting novelty.
