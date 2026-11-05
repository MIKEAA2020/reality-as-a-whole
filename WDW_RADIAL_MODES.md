# Inhomogeneous radial WdW modes: multi-mode adiabaticity on dressed background

The homogeneous monopole WdW results ([WDW_SPHERICAL_R_CLOCK.md](WDW_SPHERICAL_R_CLOCK.md),
[WDW_INNER_PRODUCT.md](WDW_INNER_PRODUCT.md),
[WDW_HARMONIC_EVOLUTION.md](WDW_HARMONIC_EVOLUTION.md),
[WDW_PARTICLE_PRODUCTION.md](WDW_PARTICLE_PRODUCTION.md)) treated \(\phi\) as a
single mode. This note extends to inhomogeneous radial perturbations, lifting
the minisuperspace restriction one step: the scalar field is decomposed into a
tower of radial standing-wave modes on the dressed spherical geometry.

## 1. Mode decomposition

On the dressed cloud of proper radial extent \(l_{\mathrm{total}}\approx R_m=22.66\),
radial modes have standing-wave momenta
\[
  k_n=\frac{n\pi}{l_{\mathrm{total}}},\qquad n=1,2,\dots
\]
with dressed frequencies (Dirichlet-like toy; Bessel basis in the full curved
problem):
\[
  \omega_n(0)=\sqrt{k_n^2+\mu^2}\ (\text{flat}),\qquad
  \omega_n(R_m)=\sqrt{k_n^2+(\mu\,N)^2}\ (\text{redshifted}),
\]
where \(N=e^\nu\sqrt{1-2m_G/R}=0.99998\) is the dressed-lapse factor.

## 2. Verified adiabaticity

From [verification/wdw_radial_modes.py](verification/wdw_radial_modes.py), for
\(n=1,\dots,20\) (covering \(k\) from \(0.14\) to \(2.77\)):

- curvature potential scale: \(3.6\times10^{-5}\)
- all modes satisfy \(\epsilon_n=|\dot\omega_n|/\omega_n^2<3.7\times10^{-8}\)
- adiabatic particle bound \(N_n\lesssim 1.3\times10^{-15}\) per mode
- worst-case sudden-quench bound \(N_n<8.4\times10^{-11}\) per mode
- maximum \(\epsilon\) occurs at the lowest modes (mass-dominated)
- high-\(k\) modes become kinetically dominated, redshift affects only the mass
  term, so \(\delta\omega_n\) decreases slightly with \(n\)

All 20 modes are **extremely adiabatic**: the dressed-cloud "expansion" is
gentler than a slow laboratory adiabatic ramp by many orders of magnitude.
Coherence is preserved across the full radial tower.

## 3. Significance

This lifts the earlier monopole-only conclusion:

- The dressed-clock coherence bound holds not just for the minisuperspace mode
  but for a whole tower of radial inhomogeneous modes.
- Multi-mode QFT-in-curved-spacetime in internal \(l\)-time is well-defined for
  weak dressing: each mode evolves unitarily with negligible Bogoliubov mixing.
- Cosmological particle production in this weak-field system is genuinely
  negligible, not an artifact of restricting to one mode.

Limitations:

- Dirichlet standing waves are a toy basis; Bessel/curved-laplacian eigenmodes
  should be used for quantitative curvature-coupling.
- Only radial (monopole angular sector) inhomogeneities; \(\ell\geq1\) angular
  multipoles couple to tensor/vector gravitational modes (quadrupole GW etc.).
- Strong-field collapse and phenomenal constitution remain open.

## 4. Verification

Run:

    python verification/wdw_radial_modes.py
    python -m verification.wdw_radial_modes

Output:
[verification/wdw_radial_modes.json](verification/wdw_radial_modes.json).
The deterministic pure-Python verifier constructs the radial mode tower,
computes dressed frequencies at both ends of the cloud, and evaluates
sudden-quench and adiabatic Bogoliubov particle-number bounds per mode.
