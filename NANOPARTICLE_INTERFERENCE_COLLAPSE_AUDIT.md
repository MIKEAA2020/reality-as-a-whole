# Nanoparticle interference and the limits of collapse-model transfer

## Decision

[Pedalino et al., “Probing quantum mechanics with nanoparticle matter-wave interferometry,” *Nature* 649, 866–870 (2026)](https://doi.org/10.1038/s41586-025-09917-9) report strong evidence for center-of-mass matter-wave interference of sodium clusters around **172 kDa**, and stringent constraints on a **specified class** of position-sensitive macrorealist modifications. This is an important empirical constraint on physical models our framework might use. It is not evidence for experience, a unique subject, or the necessary existence of reality.

Most relevant to our previous work: **the published macroscopicity number cannot simply be used as a bound on the energy-driven cosmological collapse rate.** The collapse operators, systems, clock and parameterization are different, and the cosmology paper does not supply their laboratory mapping. An explicit operator-level control below shows why a spatial superposition can be insensitive to an energy-dephasing law even while it is sensitive to position dephasing. This is a model-scope counterexample, not a claim that the real apparatus is exactly insensitive.

Source audit: the full main article and the text of its [supplementary information](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-025-09917-9/MediaObjects/41586_2025_9917_MOESM1_ESM.pdf) were read through the web page/PDF text interface. Figure contents were assessed through captions and prose, not extracted numerical tables. The authors provide [data and code in Zenodo record 17502163](https://doi.org/10.5281/zenodo.17502163), an 88,626-byte ZIP listed with MD5 `7917961b27676f4e9df3af6d3b01c374`. The binary could not be obtained in this environment: it is outside the permitted direct-download hosts and the web page reader returned an error for the ZIP. **We did not inspect the raw scans, verify that checksum, run the authors' code, or independently reproduce their posterior.** Reported experimental results below are attributed to the authors, not presented as our own reanalysis.

## 1. What was observed

- The apparatus creates a neutral sodium-cluster beam from a cryogenic aggregation source and uses three 266 nm standing-wave gratings, each with period `d=133 nm`, spaced by `L=0.983 m`. The first and third are mainly ionizing/transmission gratings; the second is a phase grating. Surviving neutral clusters are subsequently ionized, mass filtered and counted while the third grating is scanned.
- For scans centered near **172 kDa**, the reported selected masses are approximately **143–197 kDa**, with more than 7,000 sodium atoms for a 170 kDa cluster and an estimated cluster diameter near 8 nm. Typical beam speed is around 160 m/s. Two illustrative fringes have fitted visibilities `0.10±0.01` and `0.08±0.01` (authors' 1σ fit uncertainties).
- A periodic fringe alone is not a conclusive quantum witness: a suitably described classical shadow or lensing pattern can produce one. The authors compare the variation of visibility with the second grating's laser power to both a quantum Wigner–Weyl calculation and a classical model with matched assumptions. They report agreement with the former and separation from the latter. Figure 2 applies the **same** global contrast factor `0.78` to the quantum and classical curves, while other inputs have uncertainty bands. The study supports quantum interference **against those classical alternatives**, not every conceivable hidden-variable or modified-quantum theory.
- They also observe stronger fringes at 0.4–1 MDa, but explicitly say their setup cannot distinguish the quantum and classical predictions for that mass range. It would be wrong to advertise the 1 MDa signal as a demonstrated 1 MDa quantum superposition. The suggested 25 m/s operation is a **future proposal**, not their achieved result.

The 133 nm quoted separation is the experiment's stated spatial delocalization, not the object's diameter or its de Broglie wavelength. Using the representative values, the de Broglie wavelength is `14.50 fm`, Talbot length `1.220 m`, `L/L_T=0.806`, and the two-grating-interval flight time is `12.29 ms`. These are dimensional consistency calculations, not new observations. Different existing experiments reach much greater mass in a collective oscillator mode or much greater spatial separation with single atoms; the reported measure compares tests in a particular way rather than making every other dimension a record.

## 2. What μ=15.5 means—and does not mean

The authors use the [Nimmrichter–Hornberger](https://doi.org/10.1103/PhysRevLett.110.160403) macroscopicity family and the Bayesian [hypothesis-falsification procedure](https://arxiv.org/abs/1902.11092), applied to matter-wave interferometry as in [Schrinski et al.](https://arxiv.org/abs/2004.03392). The postulated **minimal macrorealist modifications** (MMM) have a characteristic classicalization time `τ_e` and localization-scale parameters. The authors report 3,895 data points from 95 scans, a Jeffreys-prior Bayesian posterior, and at the maximizing scale `ħ/σ_q=10 nm` a posterior 5% quantile

`τ_m = 2.84×10^15 s`,  `μ = log₁₀(τ_m/1 s) = 15.45 ≈ 15.5`.

At that scale, conditional on the declared likelihood, prior, model and data analysis, the posterior gives 5% probability below `τ_m`. Because μ **maximizes over the localization scale**, it does not mean the same numerical bound holds at every scale. Nor is `τ_m` the time a nanoparticle was coherently held: the interferometer time is about 12 ms. The logarithmic number compares sensitivity to the model family, not particle mass or subjective macroscopicity. The authors' claim of an order-of-magnitude improvement refers to the underlying time-scale measure, not a factor of ten in μ itself. Posterior stabilization as more data are included is helpful but alone does not demonstrate independence from every possible prior or systematic uncertainty.

The supplementary analysis describes bounds on **CSL** (mass-density localization) and says much of Adler's proposed range is excluded interferometrically while remaining marginally compatible within its bounds. Non-interferometric bounds can be stronger under their respective assumptions. Crucially, the supplement says **this experiment is not sensitive to physically allowed Diósi–Penrose gravitational decoherence**, estimating sensitivity only at a smearing scale below about `10⁻²¹ m` for this setup. Thus the result does not establish or rule out quantum gravity, a particular gravity-collapse mechanism in its viable regime, or a universal absence of collapse.

## 3. New cross-model scope control

The most direct error to avoid would be to equate the above spatial-localization test with the [Gaona-Reyes et al. cosmological model](COSMOLOGICAL_COLLAPSE_CLASSICALITY_GATE.md), whose chosen collapse operator is proportional to a reduced cosmological Hamiltonian. This distinction is standard in the collapse literature; the following finite-dimensional check applies it explicitly to the transfer proposed by the two papers. It is **not a priority claim** for the underlying degeneracy argument.

Take orthonormal paths `|0⟩,|1⟩` inside a degenerate energy eigenspace and a third state `|2⟩`, with

`H=diag(0,0,1)`, `X=diag(−1/2,+1/2,0)`.

Consider the normalized state `(|0⟩+|1⟩)/√2` and the ensemble equations, in fixed units,

`dρ/dt = −(κ/2)[H,[H,ρ]]`  (energy dephasing),  
`dρ/dt = −(γ/2)[X,[X,ρ]]`  (position-like dephasing).

For any pair of eigenstates of the relevant operator, the off-diagonal retention is `exp[−(rate)t(Δ eigenvalue)²/2]`. With `κt=γt=1`, energy dephasing leaves the `0–1` coherence **exactly 1**, whereas position-like dephasing retains `exp(−1/2)≈0.60653`. As a positive control, energy dephasing of `0–2` also retains `exp(−1/2)`. An ideal recombination in the `±=(|0⟩±|1⟩)/√2` basis therefore gives `P(+)=1` for the energy case versus `P(+)=0.80327` for the position case.

The reason is general: a collapse operator proportional to the identity on a degenerate subspace has zero double commutator there; the associated normalized energy-collapse noise term also vanishes on a state wholly in that subspace. Spatially distinguishable alternatives need not have distinct energies. But our `X` is a finite-level **position-like** operator, not the paper's continuous-coordinate MMM kernel, and the cluster experiment is not this three-state system. Its gratings, time-dependent interactions, energy spreads, internal modes and normalization could create sensitivity even to a proposed energy-driven law. Our test proves **absence of a universal inference**, not a zero experimental bound on such laws.

To derive a real bound, one would first need a consistent local laboratory extension of the cosmological stochastic dynamics: specify the physical time or relational clock and units, collapse operator (total versus local energy, including internal modes and apparatus), noise correlations, dynamics at all three gratings, detection and postselection, and a map between the cosmological `ε` and laboratory parameter. Then calculate the raw count likelihood including mass/velocity distributions and fit the actual scans with uncertainty and background controls. Neither paper provides this map; a universal constant and a straight substitution would be an additional, testable physical hypothesis.

## 4. Independent dimensional and MMM sanity checks

The companion verifier evaluates the *authors' published equation (10)* for one representative particle, not their inference pipeline. With `m=172 kDa`, radius 4 nm, `v=160 m/s`, `L=0.983 m`, `d=133 nm`, `ħ/σ_q=10 nm`, and Fourier order 1, it obtains

`R₁ = exp(−K/τ_e)`, with `K≈9.668×10^14 s`;  
`R₁(2.84×10^15 s)≈0.7115`.

The single-particle proxy `R₁=0.78` would correspond to `τ_e≈3.89×10^15 s`. This is **not** a competing macroscopicity estimate or posterior: the authors use the raw count likelihood, different grating powers, mass and velocity distributions, and their own nuisance/error treatment. The `0.78` in the paper is a global reduction factor in the plotted comparison and is used by the authors in a separate CSL illustration; it is not a universal 95% lower confidence bound on the first-harmonic MMM factor. Differences between this oversimplified arithmetic and `τ_m` are therefore not evidence of a mistake.

Similarly, if one *assumed* a single exponential rate and an exact `0.78` retained contrast over `12.29 ms`, the arithmetic gives `Γ≈20.22 s⁻¹`. It is only an illustration of a conversion; no such experimental confidence limit follows from the reported fitted visibility without a valid unmodified prediction, treatment of the classical alternative, efficiency and uncertainty. In particular the observed absolute visibility `0.10` is not a 10% quantum survival probability.

Run `python verification/nanoparticle_collapse_scope.py` with [`verification/requirements-field-probe.txt`](verification/requirements-field-probe.txt). The [JSON](verification/nanoparticle_collapse_scope.json) records numerical constants, quadrature, toy retention and dimensional controls. These are floating-point checks of formulas and a stipulated model, not interval certification or an independent experimental test.

## 5. Framework implications

The result favors continued compatibility with standard quantum dynamics at this tested center-of-mass scale and constrains **specific** rapid, spatially localizing modifications. It does not require a consciousness-collapse hypothesis, and the nanoparticles are not evidence of conscious systems. Even if a collapse law existed, identifying its physical noise with experience or deriving finite subjects from it would require independent justification. Conversely, the experiment does not refute an intrinsically experiential, timeless whole whose physical predictions match its observations.

For the existing programme this adds an empirical constraint and an operator-matching gate, not a bridge from our field-probe bounds to measured nanoparticle counts, a physical time solution, or emergence of gravity. A serious model making an actual laboratory prediction must meet the data-and-instrument steps in section 3 before this experiment can accept or reject its parameters. The global target still requires separate arguments for necessity, genuine subjects, and strongest possibility=actuality, without an external creator, literal simulator, or mechanism that converts possibility into actuality.
