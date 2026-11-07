# Near-horizon conformal structure: R is conformal time

The strong-field scaling in [WDW_STRONG_FIELD_SCALING.md](WDW_STRONG_FIELD_SCALING.md)
identified a critical compactness \(C_{\mathrm{crit}}\approx0.998\) where
adiabaticity and WKB normalization break down. This note analyzes the
near-horizon regime rather than treating it as a failure point: in areal gauge,
the scalar equation takes a manifestly conformal form and areal \(R\) is exactly
the **conformal time** for the KG field.

## 1. Conformal-time identity

In Schwarzschild (areal) coordinates the spatial metric factor is
\(e^\lambda=1/\sqrt{1-C(R)}\), while the lapse is \(N=\sqrt{1-C(R)}\). In proper
radial length \(dl=e^\lambda dR\), the Klein–Gordon norm uses the product
\(N\,dl\):
\[
  N\,dl=\sqrt{1-C}\cdot\frac{dR}{\sqrt{1-C}}=dR,
\]
i.e. **conformal time is exactly areal coordinate \(R\)**. This is not an
approximation—it is an exact Schwarzschild identity. So the WdW R-clock variable
does double duty: it is the relational clock far from the horizon and the
natural conformal time near the horizon where the mass gap closes.

## 2. Proper length divergence (logarithmic)

For a linear compactness ramp from \(C=0\) to \(C=C_{\mathrm{target}}\):

| \(C_{\mathrm{target}}\) | proper length \(L\) | \(L/R_m\) | \(\langle\omega\rangle\) |
|---|---|---|---|
| \(3.7\times10^{-5}\) | 22.66 | 1.000 | 22.00 |
| 0.5 | 26.54 | 1.17 | 18.96 |
| 0.9 | 34.43 | 1.52 | 15.78 |
| 0.99 | 41.19 | 1.82 | 14.80 |
| 0.998 | 43.37 | 1.91 | 14.70 |
| 0.999 | 43.92 | 1.94 | 14.68 |

Proper length diverges only logarithmically in \((1-C)^{-1}\), not as a power
law. The dressed frequency average stays above ~14.7 even at \(C=0.999\) (for a
ramp ending there), contradicting the naive expectation that the dressed
frequency collapses immediately as \(C\) grows—the logarithmic divergence of
\(dl\) means most of the proper integration still occurs in the moderately
dressed region.

## 3. Horizon-exit modes

The cosmological-mode horizon condition \(k=aH\) (where \(a=1/\sqrt{1-C}\) is
the scale factor and \(H_R=C'/(2(1-C))\) the "Hubble" parameter in conformal
\(R\)-time) gives the comoving mode that exits the sound horizon at each \(C\):

| \(C\) | \(a\) | \(H_R\) | \(k_{\mathrm{exit}}\) | \(k_{\mathrm{exit}}/\mu\) |
|---|---|---|---|---|
| 0.5 | 1.4 | 0.022 | 0.031 | \(1.4\times10^{-3}\) |
| 0.9 | 3.2 | 0.20 | 0.63 | \(2.9\times10^{-2}\) |
| 0.99 | 10 | 2.2 | 22 | \(9.9\times10^{-1}\) |
| 0.998 | 22 | 11 | 246 | 11 |
| 0.999 | 32 | 22 | 697 | 32 |

Modes with \(k\sim\mu\) (rest-mass scale) exit the horizon around \(C\approx0.99\),
consistent (within an order of magnitude) with the non-adiabatic threshold from
[WDW_STRONG_FIELD_SCALING.md](WDW_STRONG_FIELD_SCALING.md). Higher-\(k\) modes
stay inside longer; super-horizon modes become squeezed/non-adiabatic.

## 4. Interpretation

This is not a full singularity resolution, but it removes the apparent
catastrophe at the "breakdown" point:

- The WdW R-clock is not a weak-field invention; as \(C\to1\) it smoothly becomes
  the conformal time of the massless KG field in Schwarzschild coordinates.
- The non-adiabatic threshold at \(C\approx0.99\)–\(0.998\) corresponds to
  horizon exit of the scalar rest-mass modes—the standard QFT-in-curved-spacetime
  mechanism of Hawking/cosmological pair production, not a theory failure.
- The dressed quadratic theory transitions into a massless/super-horizon regime
  where particle production is real, not an error.

Behavior *at* the horizon is standard curved-QFT mode-freezing (above).
[WdW interior continuation](WDW_INTERIOR.md) shows \(R\) remains timelike
(Kantowski–Sachs cosmological time) all the way through the interior, with
quantum gravity required only in a universal short proper-time window before
\(R=0\). Trans-Planckian singularity resolution (bounce/remnant/fuzzball/…) is
the genuine remaining QG problem.

## 5. Verification

    python verification/wdw_near_horizon.py
    python -m verification.wdw_near_horizon

Output:
[verification/wdw_near_horizon.json](verification/wdw_near_horizon.json).
