# Angular scalar–tensor coupling: adiabatic decoupling of non-spherical modes

The radial mode tower in [WDW_RADIAL_MODES.md](WDW_RADIAL_MODES.md) treats only the
\(\ell=0\) spherical-harmonic sector. This note extends to angular multipoles
\(\ell=0,\dots,10\), estimating scalar-tensor coupling (radiation reaction via
gravitational tensor/vector modes) using multipole radiation theory.

## 1. Setup

A spherical-harmonic mode with angular momentum \(\ell\) experiences a centrifugal
barrier \(\ell(\ell+1)/R^2\) giving dressed frequency
\[
  \omega_\ell(l)=\sqrt{(\mu N(l))^2+\frac{\ell(\ell+1)}{R_m^2}}.
\]
Coupling to gravitational radiation at mechanical pulsation frequency
\(\omega_{\mathrm{mech}}=2\pi/T_{\mathrm{dyn}}=6\times10^{-3}\) (from
[ASPHERICAL_QUADRUPOLE_LOSS.md](ASPHERICAL_QUADRUPOLE_LOSS.md)) produces
radiation-reaction loss with multipole suppression
\(\Delta E/E \sim C(v/c)^{2\ell+2}\) (Weinberg multipole formula), where
\(C=2M/R=3.66\times10^{-5}\) is compactness and \(v/c=\omega_{\mathrm{mech}}R_{\mathrm{source}}=0.135\).

## 2. Verified numbers

From [verification/wdw_angular_coupling.py](verification/wdw_angular_coupling.py):

| \(\ell\) | \(k_\ell=\sqrt{\ell(\ell+1)}/R_m\) | \(\omega_\ell\) | \(\delta\omega\) | \(v/c\) | loss fraction \(\Delta E/E\) |
|---|---|---|---|---|---|
| 0 | 0.000 | 22.0000 | \(4.0\times10^{-4}\) | 0.135 | 0 (monopole Birkhoff) |
| 1 | 0.062 | 22.0001 | \(4.0\times10^{-4}\) | 0.135 | \(1.2\times10^{-8}\) |
| 2 | 0.108 | 22.0003 | \(4.0\times10^{-4}\) | 0.135 | \(2.2\times10^{-10}\) |
| 3 | 0.153 | 22.0005 | \(4.0\times10^{-4}\) | 0.135 | \(3.9\times10^{-12}\) |
| 4 | 0.197 | 22.0009 | \(4.0\times10^{-4}\) | 0.135 | \(7.1\times10^{-14}\) |
| 5 | 0.242 | 22.0013 | \(4.0\times10^{-4}\) | 0.135 | \(1.3\times10^{-15}\) |
| 10 | 0.463 | 22.0049 | \(4.0\times10^{-4}\) | 0.135 | \(2.5\times10^{-24}\) |

All modes have adiabaticity \(\epsilon=|\dot\omega|/\omega^2=3.7\times10^{-8}\)
— extremely adiabatic. Quadrupole (\(\ell=2\)) loss \(\Delta E/E\approx 2\times10^{-10}\)
is consistent with the earlier aspherical quadrupole bound \(dM/M\sim1.9\times10^{-14}\)
per observation window after integrating over \(T_{\mathrm{obs}}\). Higher
multipoles are power-law suppressed.

## 3. Significance

This extends the dressed-clock coherence conclusion beyond the monopole and
radial sectors:

- \(\ell\geq1\) angular modes are adiabatic with negligible tensor-coupling
  losses in weak field.
- No decoherence from angular scalar–tensor mixing threatens clock coherence
  for our dressed-cloud parameters.
- The spherical symmetry approximation underlying Birkhoff/Killing derivations
  is stable against small angular perturbations, confirming the
  [ASPHERICAL_QUADRUPOLE_LOSS.md](ASPHERICAL_QUADRUPOLE_LOSS.md) robustness
  result at the WdW quantum level.

Limitations:

- Multipole radiation formula is leading-order; full Regge–Wheeler tensor
  propagation with dressed metric is not solved.
- Strong-field collapse (where \(v/c\to1\) and multipole suppression fails) and
  phenomenal constitution remain open.

## 4. Verification

    python verification/wdw_angular_coupling.py
    python -m verification.wdw_angular_coupling

Output:
[verification/wdw_angular_coupling.json](verification/wdw_angular_coupling.json).
