# A moving-window test of the cosmological collapse model

## Result and its scope

The previous [fixed-volume gate](COSMOLOGICAL_COLLAPSE_CLASSICALITY_GATE.md) did **not** show that the paper's collapse model cannot yield a semiclassical expanding volume. Here we test a more relevant moving window in the **same Dirichlet minisuperspace and the actual proposed stochastic law**, for a restricted class of normalized initial states.

**Conditional result, proposed for independent mathematical review:** on almost every collapse-noise path in this class, λ narrows with variance `~1/(4ε²t)` and, at each late clock time, the volume distribution becomes concentrated *relative to* a moving center `v_c(t) ~ 2√λ_* t`. Its absolute width is order `√t`, but its fractional width is order `1/√t`. An explicit Gaussian limit gives the fraction inside any window `v_c(t)±B√t`.

This is a genuine positive counterbalance to our previous fixed-window bound: both statements hold simultaneously. It is **not** a proof of a persistent classical history, a physical spacetime, covariance, cosmological data agreement, or the existence of an observable noise record. The moving center uses the model's stochastic information process, and repeated interventions may disturb that process. This result concerns conditional one-time states; it does not assign a joint probability distribution to measurements at different times.

## 1. Model, inputs and prior art

Use [Gaona-Reyes et al., JHEP 02 (2024) 193](https://doi.org/10.1007/JHEP02%282024%29193), their equation (4.1) and Dirichlet extension: `H=−L`, `L=−∂²_v≥0` on the positive half-line, and `A=−εL`, with constant `ε>0` and initial time `t=0`. Units are those of the paper. λ is the spectral value of L, and the chosen t is a relational clock variable, not a time external to the universe.

For a concrete class take the initial λ-space wavefunction `Q₀(λ)=sqrt(p₀(λ))` with zero phase, where `p₀` is a normalized bounded probability density with compact support `[λ_min,λ_max]⊂(0,∞)`, continuous and strictly positive throughout its interior. The endpoints may have jumps, as in the numerical uniform prior below. Then the sampled `λ_*` lies in the interior almost surely. Other initial phases, λ near zero, negative Robin-bound-state sectors, different Hamiltonians, clocks, and finite-time cosmological preparations are not covered.

Energy-driven state reduction and its exact filtering/information-process representations are **established**; see [Brody and Hughston, “Quantum noise and stochastic reduction”](https://doi.org/10.1088/0305-4470/39/4/008) and [Brody et al., “Exactly solvable quantum state reduction models with time-dependent coupling”](https://arxiv.org/abs/quant-ph/0511046). We do not claim to invent those methods or the standard Gaussian/Fourier asymptotics. The contribution here is their explicit application to this paper's half-line volume variable, with a moving-window limit and comparison to the previous gate; priority for such an application has not been established.

## 2. Exact positive-spectrum stochastic state

Let `λ_*` be an auxiliary random variable with density `p₀`, independent of standard Brownian motion `B_t`, and define

`Y_t = −2ελ_*t + B_t`,  `c_t = −Y_t/(2εt)` for `t>0`.

The normalized conditional spectral density and wavefunction are

`p_t(λ) = p₀(λ) exp[−2ελY_t − 2ε²λ²t] / Z_t`,

`Q_t(λ) = sqrt(p_t(λ)) exp(iλt)`.

A path-dependent global phase is immaterial. Completing the square gives `p_t ∝ p₀(λ) exp[−2ε²t(λ−c_t)²]`. The latent `λ_*` is a mathematical representation of the process, not a new physical hidden-variable premise. With `μ_t=∫λp_t dλ`, the innovations process `W_t=Y_t+2ε∫₀ᵗ μ_s ds` is Brownian in the observation filtration. Standard filtering/Itô calculus then gives the same normalized stochastic equation as the paper, including `dμ_t=−2ε Var_t(λ)dW_t`. This uses the correct **physical probability measure**; treating `Y_t` as an independent zero-drift Brownian motion under that measure would be wrong.

Because `B_t/t→0` almost surely, `c_t→λ_*` almost surely. For every such path with `λ_*` in the support interior, Gaussian concentration and continuity of `p₀` yield

`Var_t(λ) = [1+o(1)]/(4ε²t)`,  `μ_t→λ_*`.

This is a positive-spectrum, normalized asymptotic result for the stated class; it does not rely on the paper's full-line Gaussian approximation. Its endpoint λ state is generalized, not a normalizable exact eigenstate. It also does not assert the same formula for every initial state or for ε=0.

## 3. Moving volume distribution

Write `k=√λ` and `k_t=√c_t` once `c_t>0`. The Dirichlet sine transform gives

`ψ_t(v)=sqrt(2/π) ∫₀∞ dk f_t(k) e^(ik²t) sin(kv)`,

where `f_t(k)=sqrt(2k p_t(k²))`. Define the **path-dependent** moving center and rescaled volume

`v_c(t)=2k_t t`,  `X_t=(v−v_c(t))/√t`.

For a fixed path as above, set `a=4ε²λ_*>0`. Then, in the Born distribution of v at time t,

`X_t ⇒ Normal(0, s²)`, where `s²=(a²+1)/a`.

Equivalently, for every fixed `B>0`,

`Pr_t(|v−v_c(t)|≤B√t) → erf[B/(√2 s)]`.

The arrow is weak convergence of the **one-time conditional Born distributions** along an almost-sure path, not convergence of a sequence of physically recorded outcomes. Hence for any desired coverage below one, an appropriate finite B gives that coverage asymptotically; and since `v_c(t)/t→2√λ_*`, the same conditional distributions obey `v/t→2√λ_*` in probability. The absolute width increases, but the relative width shrinks. This conclusion coexists with escape from every fixed volume interval.

### Derivation and status of the approximation

The positive-spectrum posterior implies that, with `q=√t(k−k_t)`, the normalized k-space envelope after rescaling converges in `L¹` and `L²` to

`f(q)=(2a/π)^(1/4) exp(−a q²)`.

The compact support of `p₀` and the positive limiting center justify concentrating on a neighborhood of `k_t`; Gaussian tails control the complement. Insert `v=2k_t t+x√t`. In the sine transform, the outgoing exponential has phase, up to an irrelevant global factor, `q²−qx`. The incoming exponential has an additional frequency `4k_t√t` in q and vanishes locally by the Riemann–Lebesgue lemma. Thus the limiting scaled density is

`|(1/√(2π)) ∫_ℝ dq f(q) exp(iq²−iqx)|²`.

The standard Gaussian transform makes this the normalized Gaussian with variance `(a²+1)/a`; its total mass is one by Plancherel. Local convergence plus total normalization establishes weak convergence, including tightness. The incoming/outgoing split is a mathematical decomposition of a Dirichlet sine wave, not independent half-line momentum superselection sectors. These steps are a proposed analytical proof and need independent review; finite quadrature below is not that review.

For `ε=0.5`, `λ_*=1`, `a=1` and `s=√2`. At `B=4`, the limiting coverage is `erf(2)≈0.995322`. A window of this width is `±4√t` around `2t`: a fractional half-width `2/√t`. The relative window therefore becomes narrower even though the absolute window grows. The observation-centered path has a stochastic shift of order Brownian fluctuations relative to `2√λ_*t`, so replacing `c_t` by the unobserved λ_* at `√t` precision is not generally justified. The law of large numbers only guarantees their centers agree after division by t.

## 4. A simultaneous one-time check, not yet a history

Let `E` project onto the path-dependent volume window and `Q` onto a fixed-width λ interval `[c_t−η,c_t+η]`, with `η>0`. Consider the explicitly specified **ideal sequential instrument**: first the projective yes/no measurement E, then the projective yes/no measurement Q. For a normalized conditional state write `d_v=||(1−E)ψ||²` and `d_λ=||(1−Q)ψ||²`. Then

`Pr(E yes, Q yes) = ||QEψ||² ≥ 1−d_v−(sqrt(d_λ)+sqrt(d_v))²`.

This follows from the triangle inequality applied to `(1−Q)Eψ`; the bound is clipped at zero if necessary. Along the asymptotic paths, `d_λ→0` and `d_v→1−erf[B/(√2s)]`. Therefore choosing B sufficiently large makes this lower bound arbitrarily close to one. This is a weak but explicit **joint single-time** test of localized volume and λ, allowing for the disturbance from the specified first measurement. It does not assert that v and λ commute, or that a signed momentum on the half-line is self-adjoint. The unmeasured positive observable `√L` gives a magnitude, not a complete expansion-direction observable.

Critical qualifications: the projections are mathematical idealizations, their energy/work and gravitational backreaction are not budgeted, and choosing a window from `Y_t` presupposes access to a record of that process. The paper does not construct such a record. Nor does this single-time sequential instrument establish a jointly localized **multi-time history**: each intervention changes the state and future noise law. A real next gate must specify clock, readout, records and repeated instruments, propagate their disturbances with the stochastic dynamics, and estimate the probability of a persistent expanding path with calibrated errors. A moving window cannot simply be called an observed geometry.

## 5. Numerical controls and what they do not show

Run `python verification/collapse_moving_window.py` with [`verification/requirements-field-probe.txt`](verification/requirements-field-probe.txt). The [saved output](verification/collapse_moving_window.json) uses `p₀` uniform on `[0.5,2]`, `ε=0.5`, and the deterministic conditional control `Y_t=−t` (hence `c_t=1`). It performs the half-line sine integral directly, without replacing the spectrum by the full real line.

| t | `t Var(λ)` | `Pr(|v−2t|≤4√t)` |
|---:|---:|---:|
| 25 | 0.955587 | 0.991289 |
| 100 | 0.999993 | 0.995196 |
| 400 | 1.000000 | 0.995293 |
| 1600 | 1.000000 | 0.995315 |

The asymptotic targets are 1 and 0.995322. A denser quadrature at t=400 changes the window probability by about `4.3×10⁻⁸`. A separate seeded 2,000-sample filtering check at t=40 yields mean posterior λ `1.2626`, compared with the prior mean `1.25`; this is a coarse stochastic consistency control, not an uncertainty-certified test. The deterministic path is not claimed to be a typical full Brownian trajectory. Floating-point quadrature, the finite sample and the assertions are not interval certificates or independent verification of the theorem.

## 6. Implications for the whole-framework programme

This result strengthens the **particular collapse rival** rather than our metaphysical conclusion: a model can exhibit asymptotic relative one-time localization even though exact λ eigenstates are nonnormalizable and fixed-window probability vanishes. It still assumes homogeneous FLRW geometry, a chosen clock, the stochastic law and an initial distribution. It does not explain the observed cosmological-constant scale, demonstrate inhomogeneous gravity, recover a clock-independent history, or identify the collapse noise with experience. Nor does it establish necessary existence, genuine subjects, or strongest possibility=actuality. No external creator, literal simulator or conversion from possibility to actuality is required by this analysis.
