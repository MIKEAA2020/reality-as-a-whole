# A finite-window obstruction to clock–modular matching

## Status and prior work

This note tests a specific extension of [FRW_MODULAR_CLOCK.md](FRW_MODULAR_CLOCK.md), not a solution of the full gravitational problem of time. It gives an explicit finite-window witness that a proposed identification fails within a regulated minisuperspace model. The candidate contribution is the application and the quantitative witness below; a targeted search has **not established research novelty**. Time averaging, thermal modular flow, and scalar-clock FRW are established ideas, and the possibility of overlap with unexamined literature remains. The formulas are included to make the candidate falsifiable, not to claim priority for basic dephasing mathematics.

Especially relevant existing results:

- Page and Wootters, “Evolution without evolution” (1983), established relational conditional dynamics; Höhn, Smith and Lock, [The Trinity of Relational Quantum Dynamics](https://arxiv.org/abs/1912.00033) (2021), relate the Dirac, Page–Wootters and deparametrized pictures under stated conditions, including clock POVMs. Their results should be used rather than rediscovered.
- Van Neerven and Portal, [Thermal time as an unsharp observable](https://arxiv.org/abs/2306.13774) (2024), Theorem 6.1, already treat modular time and a covariant POVM for the positive-momentum part of the free massless one-dimensional Hamiltonian |D|. Our unregulated FRW branch has the **same operator up to the scale κ**. Their paper's generalized modular-time construction and its listed Tomita–Takesaki/Page–Wootters open questions must not be conflated with a normalized normal Gibbs state or claimed as our new result.
- Short and Farrelly, [Quantum equilibration in finite time](https://arxiv.org/abs/1110.5759) (2012), study finite-time averaging/equilibration; the Fourier-filter mechanism is not new.
- Chua, [The Time in Thermal Time](https://arxiv.org/abs/2407.18948) (2024), discusses why interpreting a modular flow as physical time requires more than formal modular dynamics.
- Gielen and Menéndez-Pidal, [Unitarity, clock dependence and quantum recollapse in quantum cosmology](https://arxiv.org/abs/2109.02660), analyze a different FRW model and find clock-choice-dependent quantum theories. This cautions against assuming that a result for one clock applies to all.

The search covered modular/relational time, scalar-clock cosmology, positive-momentum modular time, and finite-time averaging. It is not a systematic citation or full-text review. The question tested here is narrower: **if the actual reference state is conditioned on a finite clock window rather than a complete period, do its own modular automorphisms still reproduce the scalar-clock flow?**

## Model and finite-window state

Use the previously specified scalar-clock FRW reduction and its regulators, not the full theory. The system has distinct energy levels E_n=nω for n=1,...,N (N≥2), ω=κ2π/L>0. Pick a coherent initial state

    |ψ₀> = Σ_n sqrt(p_n)|n>,     p_n>0,   Σ_n p_n=1,

where p_n∝exp(-βE_n) is a selected preparation, β>0. Write U(φ)=exp(-iHφ) and ρ(φ)=U(φ)|ψ₀><ψ₀|U(φ)†. Let P=2π/ω be the artificial recurrence period.

For a genuine continuous periodic clock, one can take H_C=L²(S¹_P,dφ) and the normalized history Ψ(φ)=U(φ)ψ₀/√P, with clock generator -i∂_φ. This history solves (-i∂_φ+H)Ψ=0. Select a window of duration T, 0<T≤P, then discard the precise reading. The normalized system state is

    ρ_T = (1/T) ∫_(-T/2)^(T/2) ρ(φ) dφ.

This is the state **after window selection**, not the unconditional complete-clock marginal. The previous document's finite discrete clock and this continuous periodic clock share the same regulated system dynamics, but they are distinct clock regulators. The window and temperature are assumptions, not predictions. More general normalized clock-selection weights w give the same structure with the characteristic function of w in place of the sinc below.

In the energy basis, elementary finite-time averaging yields

    (ρ_T)_nm = sqrt(p_n p_m) sinc[(E_n−E_m)T/2],
    sinc(x)=sin(x)/x, sinc(0)=1.

The matrix is faithful for every T>0: for v≠0, v†ρ_Tv is the interval average of |Σ_n v_n* sqrt(p_n)e^(-iE_nφ)|², which cannot vanish identically on a nonempty interval unless all coefficients vanish. At T=P the matrix is the selected Gibbs state diag(p_n); for 0<T<P its nearest-neighbour coherence is nonzero, so it is not stationary under the relational dynamics.

## Exact witness against all reparameterizations

Let α_t(A)=U(t)†AU(t), σ_s^(ρ_T)(A)=ρ_T^(is) A ρ_T^(-is), and use the legitimate effect A=ρ_T (a density matrix lies between 0 and I). In the state ρ_T,

    Tr[ρ_T σ_s^(ρ_T)(ρ_T)] = Tr(ρ_T²)       for every real s,

because the modular flow fixes its own reference state. By contrast,

    D_T(t) := Tr(ρ_T²) − Tr[ρ_T α_t(ρ_T)]
            = Σ_(n,m) |(ρ_T)_nm|² [1−cos((E_n−E_m)t)]
            ≥ 2 p_1 p_2 sinc²(ωT/2) [1−cos(ωt)].

Thus for t=P/2 and **every** 0<T<P,

    D_T(P/2) ≥ 4 p_1 p_2 sinc²(ωT/2) > 0.

No choice of modular parameter s, linear or nonlinear, can remove this particular operational discrepancy for that state and effect. In particular, the two automorphisms are not equal on the whole system algebra. The observable depends on the chosen preparation and window but is fixed once they are selected; the mismatch does not require it to be a preferred cosmological observable.

For a Gaussian selection with standard deviation δ>0 on the scalar-clock covering line, periodized onto the clock circle, the Fourier coefficient at a gap is exp[-δ²(E_n−E_m)²/2]. The same argument yields

    D_δ(P/2) ≥ 4 p_1 p_2 exp(-δ²ω²) > 0

for every finite δ. Unlike the sharp window, no finite Gaussian width produces exact dephasing. These bounds are particular to this prepared, finite-spectrum model; they do not rule out another state, measurement algebra, clock, or independently chosen equilibrium reference.

## Scale dependence, not a continuum proof

For a sharp window, the distance to the full-period Gibbs marginal τ=diag(p_n) satisfies

    ||ρ_T−τ||²₂ = Σ_(n≠m) p_n p_m sinc²[(E_n−E_m)T/2]
                  ≤ (4/T²) Σ_(n≠m) p_n p_m/(E_n−E_m)².

This familiar finite-time dephasing estimate is useful only when the relevant energy gaps remain bounded away from zero. As the box grows, ω=κ2π/L shrinks: maintaining small coherence by this estimate requires a window growing with L. At fixed T and fixed finite N, ω→0 makes sinc[(n−m)ωT/2]→1, so the selected state approaches its corresponding coherent pure preparation, not the diagonal state. This fixed-N limit **is not** an infinite-dimensional FRW continuum limit; it demonstrates the failure of a regulator-uniform estimate, not a theorem about all continuum limits.

The separate continuum no-normal-state obstruction is documented in [FRW_MODULAR_CLOCK.md](FRW_MODULAR_CLOCK.md). Van Neerven and Portal's generalized construction is a relevant alternative mathematical starting point, but a physical clock reference, state/weight selection, actual observable algebra, and comparison with full gravitational dynamics remain to be established. In particular our window calculation neither invalidates their construction nor proves that its Page–Wootters interpretation is impossible.

## Checks and precise scope

[verification/frw_clock_window_mismatch.py](verification/frw_clock_window_mismatch.py) independently integrates the finite-window and Gaussian mixtures by quadrature, tests positivity and modular invariance, tests the witness and bound, tests complete-period recovery, and illustrates the regulator dependence. Five tests pass; [JSON results](verification/frw_clock_window_mismatch.json) retain numerical settings and examples. With β=2, ω=1/√6, N=4 and T=P/2, the witnessed expectation discrepancy is approximately 0.3027, above the analytic lower bound 0.2412. These are dimensionless model numbers, not empirical predictions.

A subsequent partial step is documented in [FRW_INTERNAL_POVM.md](FRW_INTERNAL_POVM.md): the published positive-momentum POVM is applied to an unregulated FRW branch, with an explicit scalar/geometric frame transformation and matching generalized-flow covariance. It does not derive the non-normal weight from an internal-clock instrument. Before asserting novelty, a specialist should compare both constructions and these bounds against the papers' citations and later literature.
