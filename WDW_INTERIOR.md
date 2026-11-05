# Interior Schwarzschild: WdW R-clock continues through the horizon to a finite QG window

The near-horizon result [WDW_NEAR_HORIZON.md](WDW_NEAR_HORIZON.md) showed that areal
\(R\) is conformal time for the exterior scalar and that adiabaticity fails at
\(C\approx0.99\) as rest-mass modes exit the horizon. This note continues the
description *inside* the Schwarzschild horizon (\(R<2M\)).

## 1. Interior geometry

For \(R<2M\) the Schwarzschild metric in areal coordinates becomes
\[
  ds^2=-\frac{dR^2}{f(R)}+f(R)\,dt^2+R^2\,d\Omega^2,\qquad f(R)=\frac{2M}{R}-1>0,
\]
i.e. areal \(R\) is **timelike** (monotonically decreasing from \(2M\) to 0 on any
infalling trajectory) and the former Killing coordinate \(t\) becomes spacelike.
The Klein–Gordon / Wheeler–DeWitt equation does not stop at the horizon—it
continues as a Tomonaga-style evolution in the new timelike variable \(R\), but
with a potential that diverges at the curvature singularity \(R=0\).

## 2. Proper infall and the quantum-gravity window

For a marginally bound radial geodesic (observer falling from rest at infinity):
- \(dR/d\tau=-\sqrt{2M/R}\).
- Proper infall time from horizon to singularity: \(\tau_{\mathrm{fall}}=4M/3\).
- Kretschmann curvature \(K=48M^2/R^6\), diverging as \(R^{-6}\).
- Define quantum-gravity radius \(R_{\mathrm{qg}}\) by \(K(R_{\mathrm{qg}})=\mu^4\)
  (where scalar Compton curvature is reached):
  \[
    R_{\mathrm{qg}}=\left(\frac{48M^2}{\mu^4}\right)^{1/6}.
  \]
- Proper time from \(R_{\mathrm{qg}}\) to the classical singularity:
  \(\tau_{\mathrm{qg}}=\frac{2}{3}\frac{R_{\mathrm{qg}}^{3/2}}{\sqrt{2M}}\).

Proper interior time in synchronous-\(R\) slicing (Kantowski–Sachs "cosmological"
slicing) is \(d\tau_R=dR/\sqrt{f(R)}\), giving \(\tau_R=\pi M\) total proper
interior time.

## 3. Verified numbers

From [verification/wdw_interior.py](verification/wdw_interior.json),
using \(\mu=22\):

| \(M\) | \(R_s=2M\) | \(\tau_{\mathrm{fall}}\) | \(K_{\mathrm{horizon}}\) | \(R_{\mathrm{qg}}\) | \(\tau_{\mathrm{qg}}\) | \(\tau_R\) (interior) | QG covers horizon? |
|---|---|---|---|---|---|---|---|
| 0.01 | 0.02 | 0.013 | \(7.5\times10^7\) | 0.052 | 0.056 | 0.031 | yes (sub-Compton BH) |
| 0.1 | 0.2 | 0.13 | \(7.5\times10^3\) | 0.113 | 0.056 | 0.31 | no |
| 1 | 2 | 1.33 | 0.75 | 0.24 | 0.056 | 3.08 | no |
| 10 | 20 | 13.3 | \(7.5\times10^{-5}\) | 0.52 | 0.056 | 30.8 | no |
| 22 | 44 | 29.3 | \(3.2\times10^{-6}\) | 0.68 | 0.056 | 67.8 | no |

Key observations:

- The **quantum-gravity proper-time window before the singularity is \(\tau_{\mathrm{qg}}\approx0.056\)**
  (in units of the scalar Compton time \(1/\mu\)), essentially independent of
  black-hole mass for \(M\gtrsim0.1\). This is the famous "universal" Planckian
  stretch before the classical singularity (here in units of \(\mu\), not \(l_p\),
  because we use \(\mu\) as our UV scale).
- For large black holes, the vast majority of interior proper time is *classical*
  (curvature sub-Planckian); QG only takes over in the last ~\(0.06\) Compton
  times before \(R=0\).
- Very small BHs (\(M\lesssim0.03\), i.e. \(R_s<R_{\mathrm{qg}}\)) are
  "quantum" from horizon inward—these are sub-Compton objects where the
  classical interior description never applies.
- The effective scalar frequency averaged over the synchronous interior is
  \(\langle\omega\rangle_{\mathrm{int}}=2\mu/\pi\approx14.3\), finite and
  comparable to \(\mu\); the interior evolution is not UV-divergent *before*
  the last Planckian stretch.

## 4. Significance for the problem of time

The R-clock does *not* stop at the horizon. Inside, \(R\) is still a monotonic
"time" coordinate (Kantowski–Sachs cosmological time), the WdW equation
continues to make sense as an evolution, and the theory only requires genuine
quantum gravity in a universal proper-time window \(\tau_{\mathrm{qg}}\sim1/\mu\)
before the classical singularity. This is a large restriction of the domain
where "new physics" is needed:

- The exterior problem of time (how clocks work without Killing time) is solved
  by R-clock/Tomonaga.
- The horizon-crossing problem is standard curved-QFT mode freezing
  ([WDW_NEAR_HORIZON.md](WDW_NEAR_HORIZON.md)).
- The interior is a classical cosmological evolution (Kantowski–Sachs) all the
  way down to \(R_{\mathrm{qg}}\).
- Only the final ~\(0.06\) Compton times require singularity-resolving QG.

This does **not** solve singularity resolution. It delimits where the solution
must live: quantum gravity must replace the final stretch of the classical
Kantowski–Sachs crunch, not the entire black-hole interior.

Limitations:

- Uses marginally bound geodesic and synchronous-\(R\) slicing; other foliations
  give different interior clocks (including the "river model" and Painlevé–
  Gullstrand), but the proper-time-to-singularity scaling is universal.
- QG curvature threshold set to \(\mu^4\) (scalar Compton scale); with the true
  Planck scale \(l_p\) the corresponding \(\tau_{\mathrm{qg}}\) is the standard
  ~Planck-time answer.
- No actual resolution (bounce, fuzzball, firewalls, etc.) is derived.

## 5. Verification

    python verification/wdw_interior.py
    python -m verification.wdw_interior

Output: [verification/wdw_interior.json](verification/wdw_interior.json).
