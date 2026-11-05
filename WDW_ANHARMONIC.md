# Anharmonic self-interaction as a Kato perturbation of the quadratic WdW sector

The quadratic dressed sector is exactly solved by [WDW_MAGNUS_EXACT.md](WDW_MAGNUS_EXACT.md).
This note adds the first anharmonic correction: a scalar self-interaction
\(\lambda\phi^4\) treated as a Kato–Rellich perturbation of the dressed harmonic
oscillator. In one dimension, \(\phi^4\) is infinitesimally bounded with respect
to \(-d^2/d\phi^2+\omega^2\phi^2\) (by Nelson's criterion for semibounded
polynomials), so self-adjointness is preserved and perturbation theory converges
for weak coupling.

## 1. Perturbation estimates

For a harmonic oscillator ground state with \(\langle\phi^2\rangle_0=1/(2\omega)\),
\(\langle\phi^4\rangle_0=3/(4\omega^2)\). With nominal self-coupling \(\lambda=1\):

- ground-state energy shift \(\Delta E_0=\lambda\langle\phi^4\rangle_0=1.5\times10^{-3}\)
- relative shift \(\Delta E_0/E_0=1.4\times10^{-4}\)
- resolvent correction \(\|\Delta R\|\approx \Delta E_0/|E_0-i|\approx1.4\times10^{-4}\)
- \(\langle 2|\phi^4|0\rangle=3\sqrt2/(4\omega^2)=2.2\times10^{-3}\)
- transition probability \(|0\rangle\to|2\rangle\) (off-resonant):
  \(|\lambda\langle2|\phi^4|0\rangle/(2\omega)|^2\approx2.5\times10^{-9}\)
- Magnus second-order phase correction \(\Omega_2\sim\lambda\Phi/\omega^3\approx4.7\times10^{-2}\),
  comparable in size to the static-dressing phase error from
  [WDW_SPHERICAL_R_CLOCK.md](WDW_SPHERICAL_R_CLOCK.md) and
  [WDW_MAGNUS_EXACT.md](WDW_MAGNUS_EXACT.md).

## 2. Interpretation

Even with order-unity \(\lambda\):

- Self-adjointness is preserved (Kato–Rellich applies in 1D).
- The ground-state energy shift is \(10^{-4}\), far below dressed-clock error
  budgets.
- Transition probabilities are ~\(10^{-9}\): negligible decoherence/pair creation
  from anharmonicity in weak field.
- Magnus corrections (~0.05) are comparable to the dressed phase error, so they
  are part of the known bounded correction, not a new threat.

For \(\lambda\ll1\) (e.g. weak self-interaction in the effective theory) all
corrections shrink linearly with \(\lambda\).

## 3. Verification

    python verification/wdw_anharmonic.py
    python -m verification.wdw_anharmonic

Output:
[verification/wdw_anharmonic.json](verification/wdw_anharmonic.json).

Limitations:

- Perturbation theory in \(\lambda\); non-perturbative \(\phi^4\) effects
  (instantons, false vacuum decay) are not treated.
- 1D quantum-mechanical perturbation (homogeneous mode); multi-mode \(\phi^4\)
  can drive mode–mode energy transfer in higher dimensions, though suppressed
  by the same \(\lambda/\mu^2\) factor per mode.

[WdW strong-field scaling](WDW_STRONG_FIELD_SCALING.md) maps the compactness
threshold where weak-field adiabaticity fails near the horizon (\(C\approx0.998\)).
Sub-horizon singularity resolution and phenomenal constitution remain open.
