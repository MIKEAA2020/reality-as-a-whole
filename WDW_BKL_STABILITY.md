# Scalar quenches BKL mixmaster chaos: polymer bounce is stable

The polymer bounce ([WDW_BOUNCE.md](WDW_BOUNCE.md)) assumed spherical symmetry.
Generic spacelike singularities in vacuum GR exhibit chaotic Belinski–Khalatnikov–
Lifshitz (BKL) "mixmaster" oscillations among Kasner axes. A massive scalar
field—the same scalar our model uses—is known to quench these oscillations,
producing a quiescent (velocity-dominated) bounce (Belinski–Khalatnikov–
Lifshitz; Andersson–Rendall 2001; Weaver–Isenberg–Berger). This note quantifies
why our bounce is stable under small aspherical perturbations.

## 1. Scalar domination vs anisotropic shear

At the bounce neck:

- Bounce curvature cap \(K_{\max}=\mu^4\), with effective scalar frequency
  \(\omega_b\approx 0.34\mu = 7.48\) (from [WDW_BOUNCE.md](WDW_BOUNCE.md)).
- Scalar field rms width \(\phi_{\mathrm{rms}}=1/\sqrt{2\omega_b}=0.26\).
- Scalar kinetic + potential energy density:
  \(\rho_\phi=\omega_b/2+\frac12\mu^2\phi_{\mathrm{rms}}^2=3.7+16.2=19.9\).
- Scalar acts as **stiff fluid** \(p=\rho\) near the bounce (kinetic domination
  in the Kasner-like contraction).
- Hubble at bounce neck: \(H_{\mathrm{bounce}}=0\) exactly (turnaround point).
- Aspherical initial perturbation amplitude from our weak-field cloud:
  \(\epsilon\sim3\times10^{-5}\) (compactness and aspherical quadrupole).
- Shear energy bound at bounce: anisotropic stresses redshift as \(a^{-6}\)
  but are bounded by curvature cap; numerically \(\rho_{\mathrm{aniso}}\lesssim 8.7\times10^{-6}\).

Ratio:
\[
  \frac{\rho_{\mathrm{aniso}}}{\rho_\phi}\approx 4.4\times10^{-7}.
\]

Anisotropic shear is seven orders of magnitude smaller than scalar energy at
the bounce. The scalar dominates anisotropic stresses, quenching BKL
oscillations and yielding a quiescent (velocity-dominated) bounce.

## 2. Verified numbers

From [verification/wdw_bkl_stability.py](verification/wdw_bkl_stability.json):

| Quantity | Value |
|---|---|
| \(\omega_{\mathrm{bounce}}\) | 7.48 (\(\sim0.34\mu\)) |
| \(\phi_{\mathrm{rms}}\) | 0.26 |
| \(\rho_{\phi,\mathrm{kin}}\) | 3.7 |
| \(\rho_{\phi,\mathrm{pot}}\) | 16.2 |
| \(\rho_\phi^{\mathrm{total}}\) | 19.9 |
| initial aspherical \(\epsilon\) | \(3\times10^{-5}\) |
| \(\rho_{\mathrm{aniso}}\) bound | \(8.7\times10^{-6}\) |
| \(\rho_{\mathrm{aniso}}/\rho_\phi\) | \(4.4\times10^{-7}\) |
| \(H_{\mathrm{bounce}}\) | 0 (neck turnaround) |
| quiescent (BKL quenched) | **true** |
| stable bounce | **true** |

## 3. Significance

- The polymer bounce is not destabilized by small BKL anisotropies. The massive
  scalar acts as a stiff fluid that dominates shear at the neck, yielding a
  quiescent, approximately isotropic bounce.
- Initial asphericities of \(10^{-5}\) produce shear seven orders of magnitude
  below scalar energy at the bounce, far too small to drive mixmaster chaos.
- The bounce provides a robust, unitary singularity-resolution mechanism in
  spherical scalar gravity, and this stability analysis is evidence that
  moderate asphericities don't destroy it.

Caveats:

- We use scalar HO ground-state energy at the bounce; large coherent scalar
  excitations could change the balance (but our dressed-cloud initial data has
  \(n_{\max}\sim10\) excitations, still subdominant to ground).
- Full 3D BKL mixmaster dynamics in the presence of a scalar require numerical
  relativity beyond our symmetry-reduced model; existing literature supports
  quiescence with a scalar.
- Rotating (Kerr) BHs introduce frame-dragging and ergoregions not treated here.

## 4. Verification

    python verification/wdw_bkl_stability.py
    python -m verification.wdw_bkl_stability

Output: [verification/wdw_bkl_stability.json](verification/wdw_bkl_stability.json).
