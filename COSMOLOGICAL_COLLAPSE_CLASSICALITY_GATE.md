# Cosmological collapse: what selecting λ does and does not establish

## Decision

The attached paper is relevant to the framework's **time and gravity/classicality gaps**, but it does not close them. It proposes an objective-collapse dynamics in a particular already-quantized, homogeneous cosmology with an already-chosen internal time; it is not an explanation of the timeless absolute, a derivation of experience, or a general recovery of spacetime and gravity. Nor does its choice of collapse operator follow from our experiential target. We should treat it as a **specific physical rival**, not adopt collapse as a premise.

The substantive new check below applies directly to the paper's **Dirichlet half-line model**. It shows, under explicit assumptions, that narrowing the spectral variable λ is not the same as localizing its volume variable v: as the λ variance tends to zero, the probability of finding v in any fixed bounded interval tends to zero. This is a model-specific kinematic result, not a proof that all semiclassical cosmologies or collapse models fail. In particular, an expanding classical trajectory can also move outside every fixed interval. The test sharpens what an actual classical-history proof would have to establish.

## 1. Source and fair reading

[J. L. Gaona-Reyes, L. Menéndez-Pidal, M. Faizal and M. Carlesso, “Spontaneous collapse models lead to the emergence of classicality of the Universe,” JHEP 02 (2024) 193](https://doi.org/10.1007/JHEP02%282024%29193); [arXiv:2401.08269v2](https://arxiv.org/abs/2401.08269). All 17 pages of the [user-provided PDF](sources/uploads/JHEP02%282024%29193.pdf) were read. SHA-256: `0544f943486a1f6009d42e8b2442438acfc62b24392376f71eff62fdf48029ed`.

The paper studies a flat FLRW minisuperspace with compact spatial coordinate volume, first with a perfect fluid and then in parametrized unimodular gravity. After a choice of relational clock t, its constraint and Schrödinger-type Wheeler–DeWitt equation give `H = −π_v² = −λ`. It introduces a Wiener-driven nonlinear stochastic state equation, with collapse operator `A = εH`. Here λ is associated with a fluid-energy parameter or, in the second model, a rescaled cosmological constant. Equations (4.2) give

`d⟨λ⟩ = −2ε Var(λ) dW`,  
`d Var(λ) = −4ε² Var(λ)² dt − 2ε μ₃ dW`,

where μ₃ is the third central moment. Under the paper's ideal Gaussian assumption, `Var_t = Var_0/[1+4ε²(t−t₀)Var_0]`. That is **asymptotic narrowing**, not exact localization at a finite time. Their numerics also exhibit a slow localization timescale. The actual spectrum is nonnegative and their Gaussian is restricted to λ≥0; the appendix explicitly notes that the full-Gaussian moment relations are only approximate in their numerical regime. The third moment need not remain zero for a truncated Gaussian.

The authors argue that localization selects a well-defined geometry and may explain the cosmological constant. They explicitly acknowledge clock dependence and do not claim to solve the problem of time (appendix A). A selected integration constant alone does not calculate its observed value, explain its smallness relative to vacuum contributions, give a probability for the observed range without a specified initial distribution and measure, or demonstrate a semiclassical geometry and records. Those are additional requirements, not established results of this paper.

## 2. New Dirichlet localization gate: variance in λ versus bounded v

**Assumptions.** Work in the paper's unmodified Hilbert space `L²([0,∞),dv)` with its Dirichlet extension and `L = −∂²_v ≥ 0`, so `L=λ` and `H=−L`. The continuous-spectrum generalized eigenfunctions, normalized with the paper's `1/√(2π)` spectral factor, can be taken as

`u_λ(v) = sin(√λ v)/(√π λ^(1/4))`,  `λ>0`.

The sine transform is unitary. Let `ψ` be any normalized state with finite `V=Varψ(L)` and mean `μ≥0`; let `P_R` project onto `0≤v≤R`, with finite `R>0`. We use dimensionless variables or a fixed choice of units.

**Claim.** For every `δ>0`,

`Prψ(v≤R) ≤ min{1, [sqrt((2R/π) sqrt(2δ)) + sqrt(V)/δ]²}`.

Consequently, for any sequence of normalized Dirichlet states with `V→0`, the probability of each fixed bounded volume interval tends to zero, even if their means vary. Choose, for example, `δ=V^(1/4)` in fixed units for `V>0`; both terms then tend to zero. This statement is about the mathematical v observable at the chosen clock time, not necessarily about a physically measurable volume conditioned on a realistic clock.

**Proof.** Let `Q` be the spectral projection for `I=[max(0,μ−δ), μ+δ]`. Chebyshev gives `||(1−Q)ψ|| ≤ sqrt(V)/δ`. The squared Hilbert–Schmidt norm of `P_R Q` is

`∫_I dλ ∫_0^R dv |u_λ(v)|² ≤ (R/π) ∫_I λ^(−1/2)dλ ≤ (2R/π) sqrt(2δ)`.

The last inequality uses `|I|≤2δ` and decreasing `λ^(−1/2)`; its integrable singularity at λ=0 is harmless. Thus `||P_R Qψ|| ≤ ||P_R Q||_HS` and the triangle inequality gives the bound. This uses only spectral concentration, not the stochastic law. For `V=0`, no normalized such state exists in this continuous Dirichlet spectrum.

This application and inequality were developed for the attached model; the Fourier/sine transform, Chebyshev and Hilbert–Schmidt estimates are standard and we make **no claim of priority** for the underlying energy–position delocalization principle. The point is to make the paper's particular geometry inference independently checkable. The result applies whenever a trajectory really has `Var_t→0`; the ideal full-Gaussian formula alone is not an exact proof of this for the truncated physical distribution. The formal `|λ⟩` is delta-normalized, not a normalizable vector. There can still be weak or generalized-eigenstate localization, and finite-time wavepackets can be semiclassical in an appropriate relational sense.

A concrete next gate should compute, for the actual stochastic process and normalized positive-spectrum initial states, joint relational distributions of v and a suitable momentum/expansion observable over a **moving** classical window, the probability and persistence of a narrow history, and the effect of the boundary/reflection. It must compare the width to a stated classical accuracy and include a clock and record model. Fixed-window escape alone is not a no-classicality theorem.

### Boundary-domain control

The paper uses Dirichlet `γ=∞`. For its stated Robin condition `ψ′(0)=γψ(0)`, finite `γ<0` additionally gives the normalized bound state `ψ_b(v)=sqrt(−2γ)e^(γv)` of `L=−∂²_v` with eigenvalue `−γ²`. It is normalizable and obeys the boundary condition. Therefore the positive-λ integral in appendix A is not a complete expansion of the *full* Hilbert space for those extensions; one must include this discrete sector or explicitly restrict it away and explain whether the physical constraint permits it. It does **not** invalidate the authors' actual Dirichlet calculations, and the gate above is not asserted for the bound state or other extensions. It qualifies the claim that all γ can be substituted without further spectral analysis.

## 3. Collapse, internal decoherence and observable rivals

The assertion that there is no environment *outside the universe* does not rule out decoherence of a subsystem by other degrees of freedom **inside** the universe. For example [Halliwell, “Decoherence in quantum cosmology” (1989)](https://www.osti.gov/biblio/6199683) traces inhomogeneous scalar modes in a homogeneous cosmological model. Such reduced-state decoherence alone does not select a unique outcome under every interpretation, and assigning the split and the relevant observables has its own burden. Conversely, objective collapse actually postulates extra dynamics and a stochastic ontology; it does not get selection for free from standard unitary quantum mechanics.

For the paper's Hermitian `A=−ελ`, averaging the stochastic equation gives the familiar dephasing master equation

`dρ/dt = −i[H,ρ] − (ε²/2)[λ,[λ,ρ]]`.

In an energy basis, a matrix element receives the factor `exp[−ε²(λ−λ′)²t/2]` in the interaction picture. The same reduced channel arises by averaging `exp(−i ελ W_t) ρ exp(i ελ W_t)` over Brownian phase noise. This is established random-unitary dephasing, not a newly discovered collapse mechanism; see [Preskill's open-systems notes](https://www.preskill.caltech.edu/ph219/chap3_15.pdf) and [a discussion of distinct dephasing dilations](https://arxiv.org/abs/1605.04154). A finite-dimensional equality check is included below. Equality on the subsystem channel (including an untouched reference) does not equate the conditioned collapse trajectories, noise records, environmental states, or ontologies. Nor does a measured dephasing alone prove collapse or experience. This extends the scope warning already made in the [experience-collapse identifiability gate](CONSCIOUSNESS_COLLAPSE_IDENTIFIABILITY_GATE.md).

**Two-time rival control, not an experiment.** Prepare a qubit superposition in a two-level λ analogue, remove deterministic phase, and choose one-slot coherence retention `r=0.8`. Independent Brownian increments predict retention `r²=0.64` across two equal slots. A specific alternative with the *same* Gaussian phase repeated in both slots predicts `r⁴=0.4096`. The corresponding final `+` probabilities are `0.82` and `0.7048`. A repeated, well-calibrated interference experiment could distinguish *these particular* temporal models if their preparation, slot timing and noise assumptions hold. But another ordinary Brownian dephasing rival reproduces the same multi-time reduced dynamics for system-only controls with unobserved noise, so this is not a general collapse-vs-unitarity discriminator. It is a laboratory analogue, not a direct cosmological measurement; the paper itself observes that a single cosmological realization cannot distinguish its model from a classical universe and that repeated experiments are needed.

## 4. The clock and absolute

In this construction t is a chosen relational variable, not an external universal clock. Brownian noise is defined relative to it. A useful consistency check is that under a deterministic increasing reparameterization `t=f(s)`, the drift scales by `f′(s)` while the Wiener coefficient scales by `sqrt(f′(s))`; simply writing the same numerical constant-rate stochastic law in s generally describes a different process. For instance if `t=s²`, the same event at `s=2` corresponds to `t=4`, not `t=2`. This elementary change-of-parameter control is **not** a quantum change of clock, proof of covariance, or a no-go theorem. A genuine alternative relational clock requires a transport of the clock, state, noise, boundary domains and complete relational observables, with same-event comparisons. [Gielen and Menéndez-Pidal (2022)](https://arxiv.org/abs/2109.02660) show clock-choice-dependent quantizations in another cosmological model; equivalence cannot simply be presumed.

This is compatible with the user's timeless absolute only as a provisional local, internal description; it does not derive that timeless structure or local clocks. The separate Barontini cold-atom anchor concerns a physical clock experiment and is not a universal time or validation of the cosmological noise law. The prior [time evidence audit](TIME_SOLUTION_EVIDENCE_AUDIT.md), [WDW corrections](WDW_INTERFACE_CORRECTIONS.md), and [3+1 probe/instrument work](THREE_DIMENSIONAL_QUANTITATIVE_CHANNEL_CERTIFICATE.md) remain separate conditional results. The paper does not supply a gravitating physical apparatus or close their backreaction and continuum-audit gaps.

## 5. Reproducibility and limits

Run `python -m pip install -r verification/requirements-field-probe.txt` in a suitable environment, then `python verification/cosmological_collapse_geometry_gate.py`. The saved [JSON](verification/cosmological_collapse_geometry_gate.json) checks normalized sine-transform wavepackets truncated to `0≤k≤2`, as their k widths `.2,.1,.05,.025` decrease. Their λ variances are approximately `.1632,.0402,.01001,.002501` and their probabilities for `v≤2` are `.6515,.3651,.1879,.09465`. It also checks all matrix units of the three-level dephasing channel, the two-slot counterexample, and the deterministic clock comparison. The analytic bound is deliberately very loose and evaluates to **1** for these sample parameters; the numerical trend does not itself prove the limit. Quadratures are floating-point, not interval certificates. They are consistency checks, not independent review, data, or a simulation of the nonlinear collapse trajectories.

The remaining decision is whether a concrete and testable stochastic cosmology can meet the moving-window, clock-consistency, apparatus, perturbation and cosmological-constant gates above. Even a successful physical model would leave the experiential bridge, individual subjects, necessity and strongest possibility=actuality unproved. Nothing here requires a literal simulator, a conversion from possibility to actuality, or an external creator.
