# Particle production in spherical R-clock "expansion": adiabatic suppression

The positive-frequency Tomonaga–Schrödinger evolution in
[WDW_HARMONIC_EVOLUTION.md](WDW_HARMONIC_EVOLUTION.md) already showed that
Gaussian states propagate almost coherently under dressed quadratic Hamiltonians.
This note connects that fact to **cosmological particle production**, the curved
spacetime QFT effect demonstrated experimentally in the BEC simulator of Viermann
et al. (Nature 611, 260 (2022)): parametric amplification of quantum
fluctuations by a time-dependent effective scale factor \(a(t)\) produces
particle pairs and Sakharov oscillations in the correlation function.

In our spherical R-clock the areal/proper-radial coordinate \(l\) plays the role
of internal "time" for the homogeneous scalar mode, and as we move from
asymptotic flat space into the dressed region the effective scalar frequency
shifts from \(\omega_0=\mu\) to
\[
  \omega_d=\mu(1-\Delta),\qquad
  \Delta=\langle1-N\rangle+\delta_{\mathrm{curv}}/2=6.16\times10^{-5}.
\]
This is an FLRW-like expansion of the effective metric seen by \(\phi\): the
effective scale factor \(a(l)\) grows slowly with \(l\) as we cross the dressed
cloud.

## 1. Bogoliubov coefficients

For a harmonic oscillator whose frequency changes from \(\omega_0\) to \(\omega_d\)
over "time" \(T\) (proper radial length), the Bogoliubov transformation relates
in/out Fock modes. The worst-case (instantaneous quench) gives
\[
  |\beta_{\mathrm{sudden}}|=\frac{|\omega_0-\omega_d|}{2\sqrt{\omega_0\omega_d}},
  \qquad N_{\mathrm{sudden}}=|\beta|^2.
\]
For adiabatic ramps the Landau-Zener/adiabatic theorem suppresses particle
production by the adiabaticity parameter
\(\epsilon=|\dot\omega|/\omega^2\), giving \(N\lesssim\epsilon^2\).

## 2. Verified numbers

From [verification/wdw_particle_production.py](verification/wdw_particle_production.py):

- \(\omega_0=22\), \(\omega_d=21.99864\), \(\Delta=6.16\times10^{-5}\)
- sudden-quench (worst case): \(|\beta|=3.08\times10^{-5}\),
  \(N_{\mathrm{sudden}}=9.5\times10^{-10}\) particles per mode
- adiabatic ramp over our dressed-cloud proper length \(T=l=22.66\):
  - \(\dot\omega=6.0\times10^{-5}\), \(\epsilon=1.2\times10^{-7}\)
  - adiabatic bound \(N\lesssim 1.5\times10^{-14}\) particles per mode
- even at the short clock-window time \(T=0.49\), \(N\lesssim 3.2\times10^{-11}\)
- Sakharov pair correlation spreads at \(2c=2\) in internal \(l\) units; after
  crossing the full cloud, pair correlations would reach \(45.3\) units.

The particle number in dressed-clock operation is negligible: the dressing is an
extremely adiabatic "expansion," so no decoherence from particle production
threatens clock coherence. This justifies the coherent Gaussian evolution in
[WDW_HARMONIC_EVOLUTION.md](WDW_HARMONIC_EVOLUTION.md) and the preserved WKB
probability norm in [WDW_INNER_PRODUCT.md](WDW_INNER_PRODUCT.md).

## 3. Relation to experimental curved-spacetime simulators

The Viermann et al. BEC simulator implements the same class of Bogoliubov
pair-production phenomena (scale-factor ramp → density-contrast correlations with
Sakharov oscillations at twice the sound speed) in an analogue system; our
spherical R-clock provides the gravitational side of the same mechanism, with
internal areal time replacing the laboratory time of the condensate. In our
weak-field dressed cloud the expansion is too gentle to produce measurable
particle creation; stronger fields or faster collapse could produce analogue
Hawking/cosmological radiation, which remains open.

Limitations:

- Only the homogeneous monopole mode is treated; inhomogeneous/S-modes and
  angular multipoles contribute separate Bogoliubov channels.
- Massive scalar suppresses low-\(k\) particle production.
- Strong-field, non-adiabatic collapse and phenomenal constitution remain open.

## 4. Verification

Run:

    python verification/wdw_particle_production.py
    python -m verification.wdw_particle_production

Output:
[verification/wdw_particle_production.json](verification/wdw_particle_production.json).
The deterministic pure-Python verifier computes the frequency shift from our
prior dressed-background data, evaluates sudden-quench and adiabatic Bogoliubov
bounds at the relevant ramp lengths, and checks the Sakharov pair-correlation
speed.
