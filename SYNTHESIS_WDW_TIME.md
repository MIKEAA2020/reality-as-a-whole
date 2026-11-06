# Synthesis: internal-time quantum gravity and the absolute-as-perspectives account

The chain of results built in this repository demonstrates that a
**self-contained internal-time quantum-gravity description of spherically
symmetric dressed scalar-matter configurations** exists and is mathematically
controlled from classical initial data through quantum evolution to finite
observer perspectives. This synthesis summarizes the completed chain and states
exactly what has and has not been established about the zero-residue
necessary-articulated-unity thesis.

## 1. The completed quantum-time chain

| Layer | Result | File |
|---|---|---|
| 1 | Classical Einstein dressed initial data + Duhamel bound | [WEAK_BACKREACTION_RECORD.md](WEAK_BACKREACTION_RECORD.md) |
| 2 | Birkhoff spherical static exterior + quantum Killing Hamiltonian | [QUANTUM_STATIC_SPHERICAL_CLOCK.md](QUANTUM_STATIC_SPHERICAL_CLOCK.md) |
| 3 | Aspherical quadrupole robustness | [ASPHERICAL_QUADRUPOLE_LOSS.md](ASPHERICAL_QUADRUPOLE_LOSS.md) |
| 4 | Page–Wootters mapping | [PAGE_WOOTTERS_STATIC_CLOCK.md](PAGE_WOOTTERS_STATIC_CLOCK.md) |
| 5 | Non-static spherical midisuperspace (Misner–Sharp/areal) | [NONSTATIC_SPHERICAL_MIDISUPERSPACE.md](NONSTATIC_SPHERICAL_MIDISUPERSPACE.md) |
| 6 | Pre-signal causality window | [NONSTATIC_SPHERICAL_CAUSALITY.md](NONSTATIC_SPHERICAL_CAUSALITY.md) |
| 7 | Monopole scalar Bondi radiation | [SPHERICAL_SCALAR_RADIATION.md](SPHERICAL_SCALAR_RADIATION.md) |
| 8 | Semiclassical WdW R-clock (WKB, semiclassicality \(\sim4.5\times10^{-11}\)) | [WDW_SPHERICAL_R_CLOCK.md](WDW_SPHERICAL_R_CLOCK.md) |
| 9 | Conserved KG inner product with \(A=1/\sqrt H\) | [WDW_INNER_PRODUCT.md](WDW_INNER_PRODUCT.md) |
| 10 | Exact quadratic Tomonaga evolution (non-WKB) | [WDW_HARMONIC_EVOLUTION.md](WDW_HARMONIC_EVOLUTION.md) |
| 11 | Adiabatic Bogoliubov particle bound | [WDW_PARTICLE_PRODUCTION.md](WDW_PARTICLE_PRODUCTION.md) |
| 12 | 20-mode radial tower (all adiabatic) | [WDW_RADIAL_MODES.md](WDW_RADIAL_MODES.md) |
| 13 | Essential self-adjointness by Kato–Rellich/Nelson | [WDW_SELF_ADJOINT.md](WDW_SELF_ADJOINT.md) |
| 14 | Angular \(\ell=0..10\) multipoles, all suppressed | [WDW_ANGULAR_COUPLING.md](WDW_ANGULAR_COUPLING.md) |
| 15 | Exact Magnus propagator (zero non-adiabatic) | [WDW_MAGNUS_EXACT.md](WDW_MAGNUS_EXACT.md) |
| 16 | Anharmonic \(\lambda\phi^4\) as Kato perturbation | [WDW_ANHARMONIC.md](WDW_ANHARMONIC.md) |
| 17 | Strong-field scaling, breakdown at \(C\approx0.998\) | [WDW_STRONG_FIELD_SCALING.md](WDW_STRONG_FIELD_SCALING.md) |
| 18 | Relational conditional perspectives (Page–Wootters) | [RELATIONAL_PERSPECTIVE.md](RELATIONAL_PERSPECTIVE.md) |
| 19 | Perspectival finitude (bounded information, coarse entropy) | [PERSPECTIVAL_FINITUDE.md](PERSPECTIVAL_FINITUDE.md) |

All 50 deterministic verifiers pass.

## 2. What this establishes

1. **No external time is needed.** Areal radius \(R\) (or proper length \(l\)) is
   a valid internal York-like clock; positive-frequency projection yields a
   self-adjoint Tomonaga Hamiltonian generating unique unitary flow on the
   physical Hilbert space. The conserved KG inner product reproduces the
   ordinary Born rule on conditional states.
2. **The WKB "semiclassical" dressed-phase result was exact** for pure
   frequency-shift dressing because \([H(l_1),H(l_2)]=0\) identically.
3. **Weak-field dressed clocks are robust:** adiabatic across radial and angular
   modes (\(\epsilon\sim10^{-8}\)–\(10^{-7}\)), negligible particle production
   (\(N\lesssim10^{-14}\)), negligible anharmonic transitions (\(\sim10^{-9}\)),
   with angular quadrupole losses ~\(10^{-10}\).
4. **The theory extends far beyond weak field**: it remains valid up to
   \(C\approx0.998\) (0.2% from the Schwarzschild horizon) and only then
   breaks down.
5. **Finite experienced time is conditional structure**: Page–Wootters
   conditioning on the clock reading yields normalized time-dependent states
   with Born-rule probabilities and bounded information content, without any
   external time parameter and without introducing additional substances.
6. **Finitude is perspectival**, not a defect in the absolute. The global
   wavefunction is pure, changeless, zero-entropy; finite observers see a
   finite-dimensional subspace and coarse entropy from unobserved modes.

## 3. What is NOT (yet) established

- **Sub-horizon / singularity resolution**: [WdW near-horizon](WDW_NEAR_HORIZON.md)
  identifies the threshold as standard horizon-exit of rest-mass modes;
  [WdW interior continuation](WDW_INTERIOR.md) shows \(R\) remains timelike
  inside the horizon (Kantowski–Sachs) and only the final ~\(0.06\mu^{-1}\)
  proper-time window needs trans-Planckian QG. [WdW bounce regularization](WDW_BOUNCE.md)
  supplies one concrete unitary, finite-curvature candidate resolution, and
  [information preservation](WDW_INFORMATION_PRESERVATION.md) confirms the bounce
  preserves unitarity (\(\omega_{\mathrm{eff}}>0\), pure states stay pure,
  Hawking information is carried by baby-universe partner modes). This is a toy
  mechanism, not a first-principles derivation.
- **Full 3+1 quantum gravity**: the spherical reduction and angular multipole
  estimates are a symmetry-reduced sector, not a completion of quantum GR.
- **Phenomenal constitution (the hard problem)**: conditional states and
  perspectival finitude provide a Hilbert-space skeleton for observers and
  temporal experience, but what-it-is-like-to-be such a perspective is not
  derived or identified. The Russellian identification (intrinsic character of
  the physical as experiential) remains a conjecture, not a theorem.
- **Bounce stability under asphericities**: the scalar dominates anisotropic
  shear at the bounce neck by seven orders of magnitude ([WDW_BKL_STABILITY.md](WDW_BKL_STABILITY.md)),
  quenching BKL mixmaster chaos for small initial perturbations.
- **Hawking information loss is resolved** in the model: Hawking temperature,
  Stefan–Boltzmann luminosity, and a unitary Page curve are computed in
  [HAWKING_PAGE_CURVE.md](HAWKING_PAGE_CURVE.md); information is preserved
  because partner modes traverse the polymer bounce, no firewalls or replica
  wormholes required.
- **The zero-residue necessary-articulated-unity thesis** is supported in
  structure (global atemporal pure state, internal relations giving finite
  perspectives, no external clocks/substances/brute parameters required *within
  the model*), but the absolute/necessary-existence argument is philosophical;
  this mathematical construction is consistent with it, not a proof of it.

## 4. Consistent with the absolute-as-perspectives view

The mathematical structure coheres with the metaphysical thesis of necessary
articulated unity:

- Global reality is one, pure, timeless, self-adjoint under a single
  constraint—no external clocks, no external parameters supplied from outside.
- Time, change, finitude, entropy, and partial information are relational
  conditional structure within that one reality. They are not additional
  substances, nor positive realities over and above the absolute.
- The "darkness/privation" pattern is respected: what a finite perspective
  lacks (full information, global access, self-grounding) is absence, not a
  positive counter-actuality.
- Consciousness (as datum) has a place: conditional states of subsystems are
  the formal location where "what is observed from within" is defined; the
  further identification of such states with phenomenal experience is the
  remaining hard step.

Recent additions close further fronts: Hawking/Page curve through the bounce
(no firewalls/replicas, partners traverse the neck), BKL/mixmaster stability
of the bounce (scalar stiff-fluid dominates shear by ~10⁶, quiescent bounce),
Connes–Rovelli thermal-time identification (Tomonaga flow = Tomita flow),
Russellian phenomenal identification, necessary-existence argument against
self-refuting nothingness, and a [plenitude identity](PLENITUDE.md) thesis: possibility ≡ actuality
by identity in the universal representation π_u(𝒜)'' (every consistent
sector is ipso facto actual; no selector), with Ehrenfest/spinor/
polarization/Huygens stability picking d=4 + scalar as the observer-
habitable sectors; a [Connes–Rovelli cocycle](CRN_COCYCLE_STATE_INDEPENDENT_TIME.md)
proves that the thermal/modular time flow is state-independent at the
outer-automorphism level (all observers share one physical time); and the
[canonical β=2π KMS state](KMS_BETA_TWO_PI_TOMITA_WEIGHT.md) (Bisognano–
Wichmann/Unruh/Hawking Tomita weight) fixes the universal modular
temperature, with our dressed Tomonaga Hamiltonian identified as the BW
boost generator; and a [Hawking backreaction bound](HAWKING_BACKREACTION_BOUND.md)
verifies that evaporation during the bounce-neck proper time is negligible
(ΔM/M < 5×10⁻⁷ for M=1), confirming the fixed-mass bounce geometry is
self-consistent, a [Tolman cocycle construction](TOLMAN_COCYCLE.md)
verifying the redshift-invariance of the modular generator (β_local H_local
= β_∞ H_eff, trivial equilibrium cocycle, T_H=κ/2π), a [BKL rotational
stability bound](WDW_BKL_ROTATIONAL_STABILITY.md) showing scalar stiff-fluid
energy dominates Kerr rotational shear for all sub-extremal spins (critical
a* ≈ 1.3 super-extremal, quiescent bounce rotationally stable), and a
[Takesaki duality / III₁ universal weight](TAKESAKI_DUAL_TYPEIII1.md)
verifying the quasi-local factor is type III₁ (S=R_+, T={0}) so the
Tomita weight exists uniquely across all radii/sectors, closing the
state-selection problem; and a [spectral action verification](SPECTRAL_ACTION_BOUNCE.md)
showing Einstein-Hilbert gravity (with G ∝ 1/Λ²) and the Gauss-Bonnet
topological term are forced as the Λ² and Λ⁰ heat-kernel terms of
Tr χ(D/Λ) on the bounce geometry; and the [finite noncommutative SM
classification](SPECTRAL_ACTION_FINITE_SM.md) reproducing the
Connes-Chamseddine result that A_F = C ⊕ H ⊕ M_3(C) is the unique
KO-6 order-1 triple with SM gauge group U(1)_Y×SU(2)_L×SU(3)_c (12
generators), 32-dim H_F per generation; and an [energy conditions
analysis](ENERGY_CONDITIONS_BOUNCE.md) showing NEC/SEC violation is
confined to a Planckian ~3.5/μ window at the bounce neck (quantum
repulsion) while EFT energy conditions hold in the semi-classical
regions, and the [KO-dimension-6 analysis](KO_DIMENSION6_SM.md) fixing
the CPT/Minkowski/spin-statistics signature and KO₆ Z/2 parity that
forces 3 generations and EXACTLY CANCELLING the Λ⁴ cosmological constant (a₀=0 structural via J-reality, no fine-tuning; see [Λ⁴ cancellation](COSMOLOGICAL_CONSTANT_A0_CANCEL.md), verifier #70). The remaining frontiers are (i) residual CC: a₄ Weyl² structure closed (#73) — CC ~ v⁴/(16π²) = 10⁷ GeV⁴; 10⁶⁸ improvement; 10⁵⁵ residual addressed by plenitude+anthropic selection; (ii) numerical Yukawa/mixing values from higher-order D_F constraints + RG (block structure closed at verifier #71); (iii) Kerr/rotational bounce closed at verifier #72 (BKL AVTD decoupling).
