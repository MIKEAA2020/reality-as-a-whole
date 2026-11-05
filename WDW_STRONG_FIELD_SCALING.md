# Strong-field compactness scaling: where the dressed R-clock breaks down

The weak-field spherical WdW chain
([WDW_SPHERICAL_R_CLOCK.md](WDW_SPHERICAL_R_CLOCK.md)–[WDW_ANHARMONIC.md](WDW_ANHARMONIC.md))
proves a rigorously defined, self-adjoint, exactly integrable (in the quadratic
sector) quantum internal-time description valid for our dressed cloud
(\(C=2M/R=3.66\times10^{-5}\)). This note maps out where those approximations
break down as compactness is increased toward the black-hole threshold \(C=1\).

## 1. Adiabaticity vs compactness

The dressed scalar frequency is \(\omega_d=\mu\sqrt{1-C}\), and the adiabaticity
parameter for a linear "ramp" across the cloud of size \(R_m\) is
\[
  \epsilon=\frac{1-\sqrt{1-C}}{R_m\mu(1-C)}.
\]
For small \(C\), \(\epsilon\approx C/(2R_m\mu)\sim10^{-8}\). As \(C\to1\) the
denominator \(1-C\) drives \(\epsilon\to\infty\): the dressed frequency
collapses to zero and the ramp is no longer slow compared to \(\omega_d\).
Particle production \(N\sim\epsilon^2\) (adiabatic regime) grows to \(O(1)\)
when \(\epsilon\sim1\), marking the non-adiabatic/strong-field threshold. The
WKB amplitude \(A=1/\sqrt{\omega_d}\) diverges as \((1-C)^{-1/4}\), signaling
breakdown of the positive-frequency WKB normalization.

## 2. Verified thresholds

From [verification/wdw_strong_field_scaling.py](verification/wdw_strong_field_scaling.py):

| \(C\) | \(N=\sqrt{1-C}\) | \(\omega_d\) | \(\epsilon\) | \(N_{\mathrm{part}}\) | \(A_{\mathrm{wkb}}\) |
|---|---|---|---|---|---|
| \(3.7\times10^{-5}\) | 1.000 | 22.00 | \(3.7\times10^{-8}\) | \(10^{-15}\) | 0.213 |
| 0.01 | 0.995 | 21.89 | \(1.0\times10^{-5}\) | \(10^{-10}\) | 0.214 |
| 0.1 | 0.949 | 20.87 | \(1.1\times10^{-4}\) | \(10^{-8}\) | 0.219 |
| 0.5 | 0.707 | 15.56 | \(1.2\times10^{-3}\) | \(10^{-6}\) | 0.254 |
| 0.9 | 0.316 | 6.96 | 0.014 | \(2\times10^{-4}\) | 0.38 |
| 0.99 | 0.100 | 2.20 | 0.18 | 0.03 | 0.67 |
| 0.998 | 0.045 | 0.98 | 0.96 | 0.92 | 1.01 |
| 0.999 | 0.032 | 0.70 | 1.9 | 1 | 1.2 |
| 0.9999 | 0.010 | 0.22 | 20 | 1 | 2.1 |

Critical compactness (root search for \(\epsilon=1\)):
\(C_{\mathrm{crit}}=0.9981\), with \(N_{\mathrm{crit}}=0.044\),
\(\omega_{d,\mathrm{crit}}=0.96\).

## 3. Interpretation

- The dressed WdW R-clock remains a valid adiabatic quantum clock across
  **four orders of magnitude** of compactness (\(10^{-5}\) up to \(0.1\)) with
  negligible particle production, and continues to function with moderate
  corrections up to \(C\approx0.99\) (99% of the Schwarzschild radius).
- Breakdown occurs at \(C\approx0.998\)—within 0.2% of the classical horizon.
  That is where adiabaticity fails, WKB normalization diverges, and particle
  production becomes order-unity.
- The quadratic dressed framework is therefore not a merely weak-field result;
  it remains a sensible effective theory until deep in the trans-Planckian
  (or in our units, trans-radius) near-horizon regime.
- Below \(C_{\mathrm{crit}}\) all prior WdW results
  ([inner product](WDW_INNER_PRODUCT.md), [self-adjointness](WDW_SELF_ADJOINT.md),
  [exact propagator](WDW_MAGNUS_EXACT.md), [radial/angular/anharmonic
  corrections](WDW_RADIAL_MODES.md)–[WDW_ANHARMONIC.md](WDW_ANHARMONIC.md))
  apply with quantitatively controlled errors.
- Beyond \(C_{\mathrm{crit}}\) the theory needs genuine strong-field quantum
  gravity (singularity/horizon resolution). This remains open.

## 4. Verification

    python verification/wdw_strong_field_scaling.py
    python -m verification.wdw_strong_field_scaling

Output:
[verification/wdw_strong_field_scaling.json](verification/wdw_strong_field_scaling.json).
