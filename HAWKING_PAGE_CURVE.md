# Hawking temperature, evaporation, and Page curve for bouncing black holes

The thermal-time identification ([THERMAL_TIME.md](THERMAL_TIME.md)) derived the
Hawking temperature as the KMS temperature of the modular flow at the horizon.
Combined with the polymer bounce ([WDW_BOUNCE.md](WDW_BOUNCE.md)) and unitarity
([WDW_INFORMATION_PRESERVATION.md](WDW_INFORMATION_PRESERVATION.md)), we can now
compute a concrete toy Page curve showing entanglement entropy of Hawking
radiation rising and then falling back to zero as information is recovered via
partner modes that traverse the bounce.

## 1. Hawking radiation and evaporation

From thermal-time / surface-gravity arguments:

- Hawking temperature \(T_H=\kappa/(2\pi)=1/(8\pi M)\).
- Bekenstein–Hawking entropy \(S_{\mathrm{BH}}=A/4=4\pi M^2\).
- Stefan–Boltzmann luminosity for a single scalar species:
  \(P=g\sigma A T_H^4=1/(15360\pi M^2)\) (scalar greybody factor \(g=1\),
  \(\sigma=\pi^2/60\)).
- Evaporation lifetime \(t_{\mathrm{evap}}=M^3/(3P_0)=5120\pi M^3\) where
  \(P_0\) is \(P(M=1)\).
- Page time \(t_{\mathrm{Page}}\approx0.6\,t_{\mathrm{evap}}\) (Page 1993):
  entropy of radiation equals remaining Bekenstein–Hawking entropy at this point.

## 2. Bounce vs evaporation timescales

Crucially, the proper-time-to-bounce \(\tau_{\mathrm{bounce}}=4M/3\) is vastly
shorter than evaporation time \(t_{\mathrm{evap}}\sim M^3\) for all astrophysically
relevant \(M\):

| \(M\) | \(T_H\) | \(S_{\mathrm{BH}}\) | \(P\) | \(t_{\mathrm{evap}}\) | \(t_{\mathrm{Page}}\) | \(\tau_{\mathrm{bounce}}\) | bounce first? |
|---|---|---|---|---|---|---|---|
| 1 | 0.040 | 12.6 | \(2.1\times10^{-5}\) | \(1.6\times10^4\) | \(9.7\times10^3\) | 1.3 | yes |
| 10 | 0.0040 | \(1.3\times10^3\) | \(2.1\times10^{-7}\) | \(1.6\times10^7\) | \(9.7\times10^6\) | 13 | yes |
| 22 | 0.0018 | \(6.1\times10^3\) | \(4.3\times10^{-8}\) | \(1.7\times10^8\) | \(1.0\times10^8\) | 29 | yes |

The bounce completes in ~\(M\) proper time while evaporation takes ~\(M^3\):
collapse → bounce completes long before any appreciable mass is lost to Hawking
radiation. The infalling Hawking partners go through the bounce neck into the
baby-universe branch; they do not hit a singularity, so the global state remains
pure.

## 3. Toy Page curve

Using the standard Page-curve ansatz \(S_{\mathrm{ent}}(t)=\min(S_{\mathrm{rad}},S_{\mathrm{BH}}-S_{\mathrm{rad}})\)
with \(S_{\mathrm{rad}}(t)=S_{\mathrm{BH}}(0)-S_{\mathrm{BH}}(t)\) (Hawking
evaporation carries away entropy equal to BH entropy loss):

- Entanglement entropy rises as pairs are produced, reaching peak
  \(S_{\mathrm{peak}}=S_{\mathrm{BH}}/2\approx2\pi M^2\) at the Page time.
- After the Page time, \(S_{\mathrm{ent}}\) decreases as outgoing Hawking
  quanta become purified by late-time correlations with the partner modes
  that traversed the bounce (baby-universe / white-hole side information).
- At end of evaporation \(S_{\mathrm{ent}}\to0\); information is fully
  recovered in principle, as required by unitarity.

Numerically for \(M=1\): \(S_{\mathrm{peak}}=6.2\) (half of \(S_{\mathrm{BH}}=12.6\)),
at \(t_{\mathrm{peak}}\approx1.0\times10^4\) (consistent with \(t_{\mathrm{Page}}=9.7\times10^3\)).

## 4. Interpretation

The Hawking information paradox is resolved in this model by the following
conjunction:

1. **Unruh/Hawking effect is physical and thermal** (thermal-time KMS).
2. **No singularity** (bounce caps curvature at \(\mu^4\)).
3. **Interior partners traverse the bounce** rather than hitting a singularity
   (they exist on the baby-universe branch, not destroyed).
4. **Global state remains pure** (self-adjoint unitary propagator through
   bounce).
5. **Asymptotic observers see Hawking radiation** that is thermally distributed
   but entangled with bounce-partner modes; the Page curve is unitary because
   the partners are not destroyed.
6. **Firewalls are not required**: infalling observers cross the smooth horizon
   (equivalence principle holds) and encounter finite curvature at the bounce
   neck, not a Planckian firewall at the horizon.

This matches the Page-curve/island-program expectation (information preserved,
Page curve turns over) but without islands or replica wormholes—instead, the
bounce provides the "other side" where partners live.

Limitations:

- Stefan–Boltzmann evaporation with scalar greybody factor is a toy; real
  Hawking radiation includes all particle species with appropriate greybody
  factors and backreaction.
- The bounce is a polymer regularization, not a derived LQG/SFT result.
- "Late-time correlations" with baby-universe partners are asserted via
  unitarity; an explicit S-matrix is not computed.
- The late-time evaporation process itself must be studied in a dynamical
  spacetime that includes backreaction on the metric, which is beyond the
  static/kinematic setup.

## 5. Verification

    python verification/wdw_page_curve.py
    python -m verification.wdw_page_curve

Output: [verification/wdw_page_curve.json](verification/wdw_page_curve.json).
