# A detector-information bound and a stronger-coupling counterexample

## Decision point

The previous [quantum field readout](QUANTUM_FIELD_RECORD_EMBEDDING.md) was nearly uninformative. Was that a fundamental obstruction, or a bad choice of detector?

**It was not a general obstruction.** Within the same regulated quadratic field model, an optimized Gaussian pointer and stronger prescribed couplings yield **71.67%** equal-prior success under a selected *initial-energy proxy* that the weak-coupling design cannot meet. A fixed-coupling uncertainty bound explains why preparation alone cannot fix the weak design.

However, the stronger calculation also exposes why this is **not yet a gravity solution**: its retained field energy becomes large compared with the classical reference background during the protocol. The calculation keeps that geometry fixed, does not price the switching or reference/memory systems, and does not solve quantum gravitational constraints. The initial-energy proxy is not a bound on gravitational backreaction.

The uncertainty relation and contractive/squeezed pointer preparations are established techniques; see [Yuen's contractive states](https://doi.org/10.1103/PhysRevLett.51.719). The bound and optimization below are specific applications to our regulated model. No general research-priority claim is made.

## 1. Precisely defined scope and energy proxy

Retain the finite-mode, quadratic model, diagonal-sign reference qubit, two neutral memory bits and Gaussian readout of [the previous note](QUANTUM_FIELD_RECORD_EMBEDDING.md). At the initial `a=1` slice, encode the two signal hypotheses by displacements `q_Phi,1=±A`, with no momentum displacement, and use the sign of `q_D,0` at `T=0.8` as the underlying readout. The initial Gaussian state is centered before the signal displacement and has a covariance invariant under simultaneous signal/detector sign reversal. The reference qubit is initially independent, with polarization `r=0.6`; the memory bits undergo independent flip channels with `q=0.1`.

Define the deliberately narrow initial budget

    E_s = A²/2,
    E_D = Var(p_D,0)/2,
    E_s + E_D <= B.

These terms are the coherent signal displacement energy and initial readout zero-mode kinetic energy in the free finite-mode Hamiltonian at `a=1`. We **do not** count other-mode vacuum energies, energy of preparing the contractive state, the reference or memories, the clock/rod control fields' response, omitted modes or renormalized stress-energy. In a closed universe there is no independent positive total ADM energy of this form: `B` is a regulator- and slicing-dependent diagnostic, not a general relativity constraint.

The classical clock/rod reference energy on the chosen initial background is

    E_ref = (2pi)^3 (3 f² + tau²)/2 = 372.0753202.

We compare B with this number only as a transparent scale. Actual gravitational backreaction depends on local stress-energy and solving the constraints and evolution, not just this ratio.

## 2. A rigorous bound inside the fixed model

For fixed pulse functions and couplings, let the exact finite-mode symplectic propagator have coefficients

    K = S_(D0,Phi1),             u = S_(D0,D0),
    Q_out = u q_D,0 + ... .

In each reference block, the output mean has magnitude `|K| A`; the two blocks have equal variances under the stated Gaussian symmetry. The omitted terms may contain any other initial quadratures and correlations. Canonical commutation gives

    [Q_out,p_D,0] = i u.

The uncertainty relation therefore implies, for any allowed Gaussian covariance and any intermode correlations,

    Var(Q_out) >= u²/[4 Var(p_D,0)] = u²/(8 E_D).

With this encoding and Gaussian sign readout, the conditional distributions are equal-variance Gaussian mixtures, and their optimal equal-prior decision is the sign threshold. Including the two specified memory-noise channels,

    P_success <= 1/2 [1 + r(1-2q) erf(sqrt(2) |K| B/|u|)].       (1)

We used `E_s E_D <= B²/4`. This is a **necessary upper bound for this family**, not a bound on non-Gaussian encodings, other observables, different Hamiltonians or couplings, or all gravitational detectors. It requires `u != 0`. The analytic inequality is exact for exact propagator coefficients; the numerical coefficients below are approximated.

## 3. Can optimized preparation saturate it?

Keep the other modes in the previously specified product Gaussian states. Let their contribution to final readout variance be `v_other`, and let `w=S_(D0,p_D0)`. For a chosen `E_D>0`, the centered pure Gaussian with

    Var(p_D,0)=2 E_D,
    Cov(q_D,0,p_D,0)= -w Var(p_D,0)/u,
    Var(q_D,0)= (w/u)² Var(p_D,0) + 1/[4 Var(p_D,0)]

saturates the zero-mode uncertainty contribution. It is a contractive state tailored to the chosen final readout time. The remaining variance is

    V = v_other + u²/(8 E_D).

Setting `E_s=B-E_D` and optimizing over `E_D` gives, with `c=u²/8`,

    E_D* = B / [1+sqrt(1+v_other B/c)].

This is the optimum **within this specified product-Gaussian family**. It is generally below bound (1), which allowed the other-mode noise to be eliminated for free. The state must itself be prepared and maintained; its preparation cost and the effects of the dropped quartic interaction have not been calculated.

## 4. Weak coupling: a genuine restriction of that design

For the original `lambda=g=0.01`, the numerically evaluated coefficients are

    K=0.0001414190,  u=0.9997752,  v_other=0.000100728.

| Initial proxy B / E_ref | Bound (1) on success | Best specified Gaussian-family success |
|---:|---:|---:|
| 0.01 | 0.5002016 | 0.5002014 |
| 0.10 | 0.5020156 | 0.5020007 |
| 1.00 | 0.5201195 | 0.5188062 |
| 10.00 | 0.6697949 | 0.6241211 |

Reaching 70% in this fixed-coupling family requires at least `B≈4,889` by the optimistic bound—about 13.1 times the initial reference energy. In the explicit product-Gaussian family it takes `B≈9,705`, about 26.1 times the reference energy. This improves substantially on the prior crude strategy of increasing the signal alone, but does not make the weak coupling useful under the chosen small proxy budget.

## 5. Stronger coupling reverses the conclusion

Keep the **same pulse shapes** and select `lambda=g=0.2`; this is a different Hamiltonian, so the weak-coupling bound does not apply with its old K and u. With modes `0–4`, numerical evolution gives

    K=0.0561964,  u=0.9101086,  v_other=0.0545574.

Choose `B=0.1 E_ref=37.2075`. The explicit optimized preparation has

    E_s=30.4906,    E_D=6.7169,    A=7.8090,
    Var(q_D,0)=4.1578,  Var(p_D,0)=13.4338,
    Cov(q_D,0,p_D,0)=-7.4568.

The final readout variance is `0.069972`, and **P_success=0.716692** with r=0.6 and q=0.1. The q/p covariance saturates the Gaussian uncertainty determinant. Repeating with modes `0–3`/800 steps and modes `0–6`/1,600 steps gives the same displayed success to the reported digits; this is a limited convergence check, not an infinite-mode theorem.

This explicitly disproves the inference that high success in this toy framework *necessarily* requires an initial signal energy hundreds of thousands of times the background reference energy. That earlier number was for an unoptimized pointer and much weaker couplings. It does **not** disprove a more complete energy–backreaction limit.

## 6. The strong-coupling catch

For the strong candidate, including the retained other-mode bare Gaussian energies, the initial total free-field energy is `52.46`, or `14.1%` of the clock/rod background energy—not just the 10% proxy. At `T=0.8`, when both pulses are off, the retained free-field energy on the **fixed** background is `195.17`, while the clock/rod energy evaluated on that background is `240.46`, a ratio of **0.812**.

These are finite-cutoff, unrenormalized, slice-dependent energy bookkeeping figures. Their change combines cosmological time dependence and the prescribed switching; it is not separately calculated switching work. The comparison is **not** a rigorous estimate of metric error. It does, however, remove any basis for claiming that small initial B alone guarantees negligible backreaction throughout the interaction. At minimum, a self-consistent test must account for the full time-dependent stress tensor, switching/control system, reference, and memory, not merely initial signal energy. The quadratic approximation also omitted the stabilizing quartic field interaction without an error estimate.

## 7. Reproduce and interpret

Run [verification/field_readout_energy_bound.py](verification/field_readout_energy_bound.py); [the JSON](verification/field_readout_energy_bound.json) lists both bounds, optimized covariances, field energies and convergence controls. The program integrates the finite-mode quadratic symplectic ODE and evaluates the analytic formulas. It checks the uncertainty determinant and energy accounting. It does not simulate nonlinear Einstein evolution, physical clock fluctuations, quantum gravitational constraints, a local reference field, or a durable memory.

**Locality follow-up:** [CROSS_FRAMEWORK_CAUSALITY_RECORD_TEST.md](CROSS_FRAMEWORK_CAUSALITY_RECORD_TEST.md) shows that the same kind of low cosine cutoff can create a spurious causal dependence between nominally disjoint operations. Its witness is a different experiment, so its error cannot be numerically subtracted from the 71.67% result. It does show that numerical mode convergence by itself is not a local-QFT certification.

**Next decisive test:** impose an actual constraint on stress-energy throughout the pulse—including an explicit physical switching/reference system—and solve or bound the induced geometry. Then repeat the complete instrument comparison at fixed relational events. Until then, 71.67% is a useful counterexample *inside the regulator*, not an established operational prediction or a solution of the problem of time.
