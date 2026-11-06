# Energy conditions across the polymer bounce

[Index](README.md) | [WdW bounce](WDW_BOUNCE.md) |
[BKL stability](WDW_BKL_STABILITY.md) |
[Spectral action](SPECTRAL_ACTION_BOUNCE.md) |
[BKL rotational](WDW_BKL_ROTATIONAL_STABILITY.md)

## 1. Why this matters

Classical singularity theorems (Penrose 1965, Hawking 1967) prove geodesic
incompleteness from the energy conditions (NEC, SEC, WEC, DEC). For the
singularity to be *resolved* by quantum gravity, at least one energy
condition must fail locally near the bounce (that failure IS the quantum
repulsive effect that turns collapse around). But the violation must be
*confined* to the high-curvature/Planckian region — if NEC/WEC were
violated in the semi-classical exterior, effective field theory would
break down far from the singularity, in conflict with observation.

This note verifies that the polymer bounce constructed in [WDW_BOUNCE](WDW_BOUNCE.md)
satisfies this physical consistency requirement:
  - NEC and SEC are violated in a narrow window of proper thickness ~ 1/μ
    (Planckian) around the bounce neck, providing the repulsive quantum
    geometry that replaces the singularity with a smooth turnaround.
  - WEC, DEC, SEC, NEC all hold in the semi-classical interior (outside
    the quantum-gravity region) and in the post-bounce expanding branch,
    where EFT remains valid.

## 2. Effective stress-energy at the neck

Two contributions dominate the energy balance near the bounce:

  1. **Scalar stiff-fluid** (w = +1, p = ρ): ρ_s = μ⁴/(6π) ~ 1.2 × 10⁴,
     from [BKL stability](WDW_BKL_STABILITY.md). This is ordinary matter
     satisfying all energy conditions (ρ>0, ρ+p=2ρ>0).
  2. **Quantum-geometry / holonomy correction**: the polymer
     regularization that caps curvature at K_max = μ⁴ acts like a
     cosmological-constant-like (and briefly phantom-like) effective
     fluid with ρ_QG ~ μ⁴/π and p_QG < −ρ_QG at the neck, violating
     NEC. Away from the neck this contribution is exponentially
     suppressed (Gaussian width ~ R_b/2) and also falls off as the
     sixth power of the scale factor, restoring classical vacuum.

At the neck the total energy density and pressure are

    ρ_tot ≈ 8.7 × 10⁴,    p_tot ≈ −9.9 × 10⁴,

giving ρ+p ≈ −1.3 × 10⁴ < 0 (NEC violated) and ρ+3p ≈ −2.1 × 10⁵ < 0 (SEC
strongly violated). This is the required "quantum repulsion" for the
bounce.

## 3. Violation window is Planckian

Integrating the proper-time element dτ = dR/√|f(R)| through the region
where NEC fails gives a violation proper-time thickness

    τ_viol ≈ 0.16 ≈ 3.5/μ,

i.e., a few Compton times of the bounce scale μ, consistent with the
"quantum gravity only acts in a Planckian window around the singularity"
expectation. At R ≫ R_b (more than ~3 R_b from the neck) the quantum
geometry contribution is negligible and all energy conditions hold
(stiff-fluid scalar + small classical vacuum), so EFT is reliable.

## 4. What this means physically

  - The bounce is a NEC-violating event, as every known non-singular
    cosmological/bounce model requires (this is a theorem: any globally
    regular bounce from collapse violates NEC somewhere).
  - The violation is *not* ad-hoc exotic matter inserted by hand; it is
    the effective stress-energy of the holonomy/polymer regularization
    itself, equivalent to the inverse-volume and holonomy corrections
    in LQC that make the quantum Hamiltonian operator bounded below.
  - No energy-condition violation persists outside the ~1/μ window; in
    particular, the asymptotic future/past regions respect NEC/WEC/DEC
    (classical GR plus the dressed scalar cloud), consistent with
    observations and no exotic-matter pathologies at astrophysical
    scales.

## 5. Cross-checks with prior chain elements

  - [Hawking backreaction bound](HAWKING_BACKREACTION_BOUND.md): ΔM/M <
    5×10⁻⁷ during the neck — the energy-condition violation does not
    source large radiative losses because it is confined to the
    Planckian window.
  - [BKL stability](WDW_BKL_STABILITY.md) / [rotational](WDW_BKL_ROTATIONAL_STABILITY.md):
    the scalar stiff-fluid dominates shear/rotation *away* from the
    neck (which is where BKL applies); in the NEC-violating window
    itself the holonomy correction dominates, which is consistent with
    quiescent BKL behavior outside the quantum cap.
  - [Spectral action](SPECTRAL_ACTION_BOUNCE.md): the heat-kernel
    expansion is finite precisely because curvature caps at μ⁴; NEC
    violation is the dynamical mechanism by which that cap is enforced.

## 6. Verification

    python verification/energy_conditions_bounce.py
    python -m verification.energy_conditions_bounce

Output: [verification/energy_conditions_bounce.json](verification/energy_conditions_bounce.json).

PASS: NEC and SEC violated at neck (ρ+p < 0, ρ+3p < 0); WEC/DEC/SEC/NEC
hold in the mid-interior and post-bounce; NEC-violation proper-time
thickness ≈ 0.16 ≈ 3.5/μ (Planckian confinement).


## 6b. Extension to Kerr (rotating)

BKL rotational decoupling extends this result to all sub-extremal rotating (Kerr) black holes: near the bounce neck (α→-∞) the rotational potential is suppressed as e^{10α} relative to Kasner walls, making the bounce locally spherical. See **KERR_BOUNCE_ROTATIONAL.md** (verifier #72).

## 7. References

1. R. Penrose, *Gravitational collapse and space-time singularities*,
   Phys. Rev. Lett. 14 (1965) 57.
2. S. W. Hawking, *The occurrence of singularities in cosmology*,
   Proc. R. Soc. Lond. A 294 (1966) 511; *Singularities in the universe*,
   Phys. Rev. Lett. 17 (1966) 444.
3. M. S. Morris and K. S. Thorne, *Wormholes in spacetime and their use
   for interstellar travel: a tool for teaching general relativity*,
   Am. J. Phys. 56 (1988) 395.
4. A. Ashtekar, T. Pawlowski, P. Singh, *Quantum nature of the big
   bang*, Phys. Rev. Lett. 96 (2006) 141301, arXiv:gr-qc/0602086.
5. P. Singh, *Are loop quantum cosmos never singular?*, Class. Quantum
   Grav. 26 (2009) 125005, arXiv:0901.2750.
6. C. Rovelli and F. Vidotto, *Covariant Loop Quantum Gravity* (Cambridge
   University Press, 2014).
