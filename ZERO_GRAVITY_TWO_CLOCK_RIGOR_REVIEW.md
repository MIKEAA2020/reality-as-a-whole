# Rigorous recheck: zero-constraint gravity, two clocks and duration

## Scope and outcome

This is a selected, independent algebraic recheck and extension of the [two-scalar FLRW formalization](ZERO_EXPERIENCE_INTRINSIC_IDENTITY_RELATIONAL_GRAVITY.md) and [zero-constraint reference analysis](ZERO_ENERGY_CONSTRAINT_REFERENCE_AND_PHYSICAL_RECOVERY.md), not a complete audit of either document or of general relativity. The user’s current programme treats space and time as **non-fundamental constructs**, with a zero-energy whole and experience intrinsic to reality. The FLRW metric below is an **assumed effective model** for testing recovery, not a fundamental spacetime arena or a derivation of the programme.

The old relational `χ[τ]`, weak `a[τ]`, lapse rescaling and sample constraint formulas check out on their declared domains. We strengthen them by deriving a second-clock comparison, a proper-duration expression and an exact Poisson bracket for clock-relative fields. These exhibit physical structure and domain restrictions in *one* model; they do not prove that its Hamiltonian constraint is the actual whole-level energy or that its scalars are subjects or experience.

## 1. Model, domains and recheck

For a flat compact FLRW region with unit fiducial coordinate volume, two homogeneous massless scalars and `κ=8πG>0`, the earlier model uses `a>0` and

    C = −κ p_a²/(12a) + (p_φ²+p_χ²)/(2a³) = 0.

Canonical brackets are `{a,p_a}={φ,p_φ}={χ,p_χ}=1`. The scalar momenta are constant, and the φ-clock sector is `p_φ≠0`. Set

    r = p_χ/p_φ,       α = −κ a p_a/(6p_φ),
    χ_φ(τ)=χ+r(τ−φ),   a_φ(τ)=a exp[α(τ−φ)].

Direct calculation yields

    {χ_φ(τ),C}=0,          {α,C}=−κ C/(2p_φ),
    {a_φ(τ),C}=−[κ(τ−φ)/(2p_φ)] C a_φ(τ).

The χ result is strong (off shell); the scale-factor and α results are weak (on `C=0`). The previous document correctly labeled this distinction, but did not give the explicit bracket of `a_φ(τ)`; it now makes the residual testable. The threshold `q_τ=1[χ_φ(τ)≥χ_ref]` is a discontinuous function, not a smooth Poisson observable at its threshold; its constancy along constraint orbits follows from the exact invariance of χ_φ without differentiating the step function.

## 2. Clock change and failure domain

In the overlap `p_φ≠0` **and** `p_χ≠0`, χ is also monotone with nonzero lapse. Define

    φ_χ(ξ)=φ+(p_φ/p_χ)(ξ−χ),
    a_χ(ξ)=a exp[α_χ(ξ−χ)],     α_χ=−κ a p_a/(6p_χ).

For any φ-reading τ, use the matching χ-reading `ξ=χ_φ(τ)`. Then, as exact functions wherever both clocks are defined,

    φ_χ(χ_φ(τ))=τ,            a_χ(χ_φ(τ))=a_φ(τ).

The matching χ-reading itself depends on the phase-space point. It is not a fixed global relabelling of τ valid for all trajectories. At `p_χ=0`, χ is constant and cannot be used as this clock, although the φ-clock remains admissible when `p_φ≠0`. At `p_φ=0`, the roles reverse. Neither chart covers the sector `p_φ=p_χ=0`, where the constraint also gives `p_a=0` for finite `a`. In this massless model no clock momentum turns along an orbit; more general potentials and interactions require a separate local/turning-point analysis.

For two φ-readings, a further exact strong bracket is

    {χ_φ(τ),χ_φ(τ′)} = (τ′−τ)(p_φ²+p_χ²)/p_φ³.

It is generically nonzero, even though **each** relational observable commutes with C. This is a classical bracket, not by itself a commutator, uncertainty relation, or experiential succession theorem. It warns against treating clock-relative observables at different readings as independent commuting classical labels when building a quantization.

## 3. Effective proper duration and cross-clock equality

Now restrict to the expanding solution branch `p_a<0` with `s=sqrt(p_φ²+p_χ²)>0`. Put `h=s sqrt(κ/6)>0`. On shell,

    p_a=−sqrt(6/κ) s/a,     α p_φ=h,
    Hubble = h/a³,           ρ=s²/(2a⁶).

Here Hubble and ρ are **effective FLRW quantities**. Along a comoving worldline, proper duration T satisfies `dT=N dλ` for an oriented positive lapse, so `dφ/dT=p_φ/a³`. For two clock readings τ₀,τ₁ on the same solution, define

    ΔT_φ(τ₀,τ₁)
      = [a_φ(τ₀)³/(3h)] [exp(3α(τ₁−τ₀))−1].

This is the signed proper-time difference. For future order, τ₁−τ₀ has the sign of `p_φ`; the result is nonnegative. Since `a_φ(τ₀)`, α and h are invariant on shell, the result is a relational quantity: changing the constraint parameter or rescaling the constraint by a nonvanishing function with compensating lapse does not itself alter it.

Let ξ_i=χ_φ(τ_i). Then `α_χ p_χ=h`, `a_χ(ξ₀)=a_φ(τ₀)` and `α_χ(ξ₁−ξ₀)=α(τ₁−τ₀)`, so on the overlapping clock sector

    ΔT_χ(ξ₀,ξ₁) = ΔT_φ(τ₀,τ₁).

This is an exact **same-solution clock-change** result, not a comparison of independently quantized reductions or a globally usable clock. It relies on the metric, massless fields and clock identification supplied by the model.

For `κ=6`, `p_φ=3`, `p_χ=4`, `a_φ(1)=1`, choose `τ₁=1+(3/5)log 2`. The scale factor doubles, and

    ΔT = (2³−1)/(3·5)=7/15,
    ρ_initial=25/2,   ρ_final=25/128,
    Hubble_initial=5, Hubble_final=5/8,
    ξ₁−ξ₀=(4/5)log 2.

The constraint remains zero along the solution. Nonzero local energy and finite internal duration therefore coexist with that particular zero **constraint**. This does not identify C with the objective energy of the total reality or derive physical seconds from zero alone.

## 4. Checks and remaining tasks

The [verification](verification/zero_gravity_two_clock_rigor_test.py) uses symbolic derivatives and exact rational arithmetic for the Poisson brackets and overlap identities; it separately checks the proper-time integral, cross-clock agreement, signs and inadmissible clock domains. It complements rather than replaces the earlier numerical/rational tests. A valid next step must compare complete physical instruments across genuinely different clock descriptions or derive a suitable effective model from the common non-spatiotemporal constitution; homogeneous classical fields and a chosen metric cannot supply that derivation by themselves. An empirical or first-person identity claim needs its own argument **within** that same constitution, not an externally imposed mental effect.
