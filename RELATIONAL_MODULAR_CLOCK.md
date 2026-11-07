# A relational clock and modular flow: an exact finite model

## Result and limits

There is an exact example in which (i) a stationary constrained clock–system history has nontrivially changing clock-conditioned states, (ii) its unconditional system state is faithful and thermal, and (iii) its system modular flow reproduces the relational Heisenberg evolution after an explicit rescaling. The agreement depends on the thermal state and Hamiltonian being matched. A nonthermal counterexample shows it is not automatic.

This is a **finite-dimensional toy model**, not a derivation of time in quantum gravity, an identification with Shlaer's clock, or evidence of a UV completion. The constraint, clock readings, initial state, Hamiltonian and temperature are supplied, not derived. It is a worked application of established ingredients, not a claim of a new foundational theorem. Numerical checks: [verification/relational_modular_clock.py](verification/relational_modular_clock.py); results: [verification/relational_modular_clock.json](verification/relational_modular_clock.json). The reasoning below is analytic; numerical tests illustrate it, not establish its generality.

## 1. A finite stationary history

Take system Hilbert space S = C³, clock C = C³ with orthonormal readings |j>, j=0,1,2, and units ħ=1. Define

    H = diag(0,1,2),        t_j = 2πj/3,
    U(t) = exp(-iHt),       β = 1,
    p_n = exp(-β n) / Z,   Z = 1 + exp(-β) + exp(-2β),
    |ψ₀> = Σ_n sqrt(p_n)|n>,
    |Ψ> = (1/√3) Σ_j |j> ⊗ U(t_j)|ψ₀>.

The clock labels are deliberately calibrated by the chosen t_j; the model does not derive that calibration. For adjacent readings define D_j on a history vector with components x_j in S by

    D_j x = x_(j+1) − U(t_(j+1)−t_j)x_j,   j = 0,1,
    C = D₀†D₀ + D₁†D₁ ≥ 0.

The two propagation equations give D_j|Ψ>=0, hence C|Ψ>=0 and [C, |Ψ><Ψ|]=0. The state is stationary under exp(-iuC) in the auxiliary parameter u. This path-graph constraint is not asserted to be the Einstein constraint or a standard additive clock Hamiltonian. For the broader construction and constraint-commuting relational observables, see [RELATIONAL_TIME_CONSTRUCTION.md](RELATIONAL_TIME_CONSTRUCTION.md), especially sections 2–5.

Conditioning on |j> has probability 1/3 and gives

    ρ_j = U(t_j)ρ₀U(t_j)†,      ρ₀ = |ψ₀><ψ₀|.

Because all p_n are positive and H has distinct energies, the conditioned density matrices are not all equal. This is nontrivial relational change in a stationary history, at three discrete readings—not a globally monotonic continuum clock.

For each reading j, a constraint-compatible representative of a system observable A is

    R_j(A) = Σ_w |w><w| ⊗ U(t_w−t_j) A U(t_w−t_j)†.

It commutes with C and satisfies <Ψ|R_j(A)|Ψ> = Tr(ρ_j A). Thus the conditional expectations also have representatives commuting with the chosen constraint; the test checks both properties for a non-diagonal observable.

## 2. Why the actual marginal is Gibbs

Tracing over the clock gives

    τ = Tr_C |Ψ><Ψ| = (1/3) Σ_j U(t_j)ρ₀U(t_j)†.

The energy-basis matrix element (n,m) has the factor

    (1/3) Σ_j exp[-i(n−m) 2πj/3] = δ_nm,   n,m ∈ {0,1,2}.

Thus the off-diagonal entries vanish and

    τ = diag(p₀,p₁,p₂) = exp(-βH)/Z.

All p_n > 0, so τ is faithful on the full matrix algebra M₃(C). Importantly, the reference for modular flow is the **unconditional system marginal τ**, not any pure conditioned state ρ_j. The latter is not faithful on M₃(C), so the same full-algebra modular formula cannot simply be assigned to it.

## 3. Exact agreement, with convention and scale

Use the modular convention

    σ_s^τ(A) = τ^(is) A τ^(-is),

and the usual system Heisenberg evolution

    α_t(A) = U(t)† A U(t) = exp(iHt) A exp(-iHt).

Since log τ = -βH - log Z I,

    σ_s^τ(A) = exp(-iβsH) A exp(iβsH) = α_(-βs)(A).

The minus sign follows from the explicit convention above; reversing the convention reverses it. For any system observable A at the actual clock reading j,

    Tr(ρ_j A) = Tr(ρ₀ α_(t_j)(A))
              = Tr(ρ₀ σ^τ_(-t_j/β)(A)).

So the modular formula reproduces *every* clock-conditioned system expectation at those readings. The equality of the two automorphism groups is valid for every real t; however, the constructed clock itself has only the three specified readings. The stationary marginal τ does not conflict with changing conditional states: its modular flow leaves τ invariant, while the conditional states have energy coherences.

## 4. When the agreement fails

The thermal matching is not cosmetic. In any finite dimension, with faithful density τ, Hermitian H, β>0, the identity

    σ^τ_(-t/β)(A) = α_t(A)   for all real t and all A ∈ M_d(C)

holds **if and only if** τ = exp(-βH)/Tr exp(-βH). Proof: sufficiency follows as above. For necessity, differentiate at t=0:

    [log τ + βH, A] = 0  for all A ∈ M_d(C).

The center of M_d(C) consists of scalars, so log τ + βH = cI; normalization gives the Gibbs form. This statement applies to the full matrix algebra and all real t; it is stronger than agreement at just finitely many readings. It need not hold as stated on a restricted observable subalgebra, whose commutant may be nontrivial.

For an explicit failure, keep the same H and t_j, but set q=(0.5,0.3,0.2) and |ψ₀>=Σ_n sqrt(q_n)|n>. The same phase average makes the actual marginal diag(q), which is faithful. Equal H gaps would require equal log-probability gaps for a Gibbs state at any one β; instead log(q₀/q₁)=log(5/3) differs from log(q₁/q₂)=log(3/2). Calibrating the modular scale to the first transition therefore fails on the second. The test computes that mismatch. Both dynamics exist, and the histories have the same clock readings; matching their flows is an additional condition.

## 5. What remains open and prior art

A subsequent [scalar-clock FRW calculation](FRW_MODULAR_CLOCK.md) derives a reduced gravitational Hamiltonian, constructs a regulated counterpart of this example, and identifies an obstruction to a normal Gibbs state in the unregulated continuum.

This construction uses known history-state/relational-clock and finite Gibbs modular identities. Page and Wootters introduced stationary-state relational dynamics; Connes and Rovelli proposed thermal time. Related prior work by [van Neerven and Portal, *Thermal time as an unsharp observable* (2024), arXiv:2306.13774](https://arxiv.org/abs/2306.13774), studies thermal time and clock observables for the oscillator. No exhaustive novelty review has been made; this example should be treated as an explanatory demonstration, not a claimed discovery.

The construction does not establish agreement with Shlaer's Λ–χ dynamics: that would require an actual mapping of constraints, clock observables, states and reduced dynamics. Nor does it establish the infinite-dimensional/type III case, a dynamically constructed local gravitational algebra, a continuous physical clock, or equivalence among different physical choices of clock. In the finite algebra used here all modular automorphisms are inner; quotienting by inner automorphisms therefore loses the nontrivial flow, rather than selecting a unique physical time. Extending the example requires independent arguments rather than extrapolating its PASS result.

References:

- D. N. Page and W. K. Wootters, “Evolution without evolution: Dynamics described by stationary observables,” *Phys. Rev. D* 27, 2885 (1983).
- A. Connes and C. Rovelli, “Von Neumann algebra automorphisms and time-thermodynamics relation in general covariant quantum theories,” [arXiv:gr-qc/9406019](https://arxiv.org/abs/gr-qc/9406019).
- J. van Neerven and P. Portal, “Thermal time as an unsharp observable,” [arXiv:2306.13774](https://arxiv.org/abs/2306.13774), *J. Math. Phys.* 65, 032105 (2024).
