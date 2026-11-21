# QPV reported timings: an asymmetric spatial-geometry check

## Bottom line

Using the verifier timing events and region definitions in the authors' [arXiv v2 supplement](https://arxiv.org/html/2601.16892v2#S4), I independently computed central-value spatial ratios. The **2D projected-area ratio (~4.021)**, **3D volume ratio (~4.523)** and **1D ideal-classical ratio (~2.473)** are close to the reported 4.02, 4.53 and 2.47. However, the explicit union of the comparable-classical regions gives a **1D ratio of ~3.473**, not the reported **4.48**. The latter cannot be obtained from these rounded central inputs using that union definition.

This is an **apparent internal numerical/definition inconsistency**, not a correction to the paper, a replay of its measured data or a proof that its Bell test or security theorem fails. Counting the overlap of the classical components twice gives ~4.473, numerically close to 4.48, but we do not have the authors' geometry code or a correction and **cannot establish that this is what they did**. The [plan](KAVURI_QPV_ASYMMETRIC_GEOMETRY_CHECK_PLAN.md) was written with the reported results already known; the overlap diagnosis was added after the 1D mismatch appeared.

## Inputs and scope

The preprint's supplement IV reports the following event times relative to its synchronization reference (ns):

| Event | `sA` challenge out | `sB` challenge out | `rA` response in | `rB` response in |
|---|---:|---:|---:|---:|
| Reported central time | 1291.0 | 1429.1 | 2340.3 | 2207.7 |

The reported separation is `L = 195.1 m`; we use exactly defined `c = 0.299792458 m/ns`. The calculation takes the listed response times as the acceptance times for the paper's geometry, consistent with its description, but we have not inspected the actual timing records or any unrounded acceptance thresholds. It uses neither the disputed 3-vs-9 ns prover-side arrival offset nor the disputed A/B prover-distance label. Those discrepancies remain open; their absence here does not validate them.

Let the verifier positions be `A=−L/2` and `B=+L/2` on the x-axis. Following the article, define spheres `SA`, `SB` and ellipsoids `H3`, `H4` with both verifiers as foci:

```text
radius(SA) = c(rA − sA)/2 = 157.2861 m
radius(SB) = c(rB − sB)/2 = 116.7092 m
major axis(H3) = c(rA − sB) = 273.1709 m
major axis(H4) = c(rB − sA) = 274.8197 m

E  = SA ∩ SB ∩ H3 ∩ H4
C1 = SA ∩ H3
C2 = SB ∩ H4
C  = C1 ∪ C2
```

`E` is the spatial projection of the paper's quantum target; `C` is the paper's comparable-classical target. These are three-dimensional **spatial** sets; the area and length are their projections along the common verifier axis, not 4D spacetime volumes. The preprint's separately displayed Table 3 values are `157.3`, `116.7`, `273.1`, `274.8` m; our timing-derived `H3` value would round to 273.2 m rather than 273.1 m. Its reported standard uncertainty is 0.2 m, but the reason for the central-value difference is not established. Repeating the calculation using the separately rounded Table 3 values instead gives a 1D ratio of **3.472**, not 4.48.

## Central-value results

For a fixed axial coordinate, all shapes have concentric circular transverse sections. Their intersection uses the smallest allowed radius and their union the largest; the classical components must not be added without subtracting overlap. We integrate the section width for area and disk area for volume. The values below are calculated from the **rounded central timings**, not Monte Carlo means or uncertainties.

| Quantity | Quantum `E` | Comparable classical `C` | Calculated ratio | Authors' reported ratio |
|---|---:|---:|---:|---:|
| Axial length | 78.895 m | 273.995 m | **3.473** | **4.48(2)** |
| Projected area | 10,277.99 m² | 41,332.40 m² | 4.0214 | 4.02(3) |
| Spatial volume | 1,169,456 m³ | 5,289,725 m³ | 4.5232 | 4.53(5) |
| 1D ideal classical comparator | 78.895 m | 195.1 m | 2.4729 | 2.47(2) |

Parentheses in the authors' reported values indicate one standard uncertainty; we have not independently reproduced their uncertainty propagation. Their comparison figures derive from a Monte Carlo over measurements, not necessarily the ratio at rounded central inputs. Accordingly, the small 3D difference is not itself evidence of an error. The larger 1D mismatch requires clarification, not a naive significance test against the quoted 0.02.

### Independent one-dimensional check

The axial intervals in metres, relative to the A–B midpoint, are:

```text
E  = [ −19.1592,   59.7361 ]      length  78.8953
C1 = [−136.5854,   59.7361 ]      length 196.3216
C2 = [ −19.1592,  137.4099 ]      length 156.5691
C1 ∪ C2 = [−136.5854, 137.4099]   length 273.9953
```

Their intersection is exactly `E`, so the sum of the two component lengths, **352.8906 m**, double-counts **78.8953 m**. Dividing that sum by the quantum length gives **4.4729**, one greater than the union ratio. This numerical resemblance to the published 4.48 is an **illustrative possible mechanism**, not evidence of the actual calculation used. Other differences in definitions, inputs or implementation might exist.

There is also a simple independent bound: both classical components lie within the larger ellipsoid, whose axial length here is **274.8197 m**. Even allowing every displayed timing and distance central value to vary by ±0.05 of its printed unit, conservative interval arithmetic gives a quantum length of at least **78.8153 m** and a larger-ellipsoid length of at most **274.8498 m**. Thus the classical/quantum length ratio from the stated union is at most **3.4873** within those rounding intervals. This is a bound on rounding perturbations **conditional on the stated inputs and definitions**, not a confidence interval, a bound on measurement error or on other possible definitions.

We also evaluated the 32 corners of those rounding intervals: the same-latency 1D ratios range from **3.4698 to 3.4761** at those sampled corners. These corner ranges are sensitivity illustrations, not proven global extrema or uncertainty estimates. Full results are in the [aggregate receipt](verification/kavuri_qpv_asymmetric_geometry.json).

## Verification and limitations

The [implementation](verification/kavuri_qpv_asymmetric_geometry.py) evaluates radial profiles using all four shapes, explicitly unions the classical axial intervals, splits integration at profile crossings, uses exact-for-quadratics Simpson integration for volume, and adaptive numerical quadrature for area. The [tests](verification/kavuri_qpv_asymmetric_geometry_test.py) compare the symmetric case against the earlier analytic formulas; verify interval overlap, union and ellipsoid bounds; and independently approximate areas and volumes by a direct-distance membership/bisection calculation and midpoint integration. All seven focused geometry tests, the existing QPV arithmetic checks and 45 selected project regression checks passed. The numerical checks use Python with NumPy 2.4.6 and SciPy 1.17.1; these do not validate the source measurements or security proof. Integration-error estimates are numerical diagnostics, not experimental uncertainty.

The consistency between the rounded-input 2D/3D calculations and the reported values is a useful check on the spatial geometry, not independent empirical replication. The 1D mismatch does not determine whether the paper's authors used a different comparator, an unpublished convention, or a mistaken computation or label. Resolving it requires their geometry/plot code, precise definitions and preferably unrounded timing data. The separate impossible pass count and timing/distance discrepancies are assessed in the [source follow-up](KAVURI_QPV_PREPRINT_SUPPLEMENT_DISCREPANCY_FOLLOWUP.md). Device-independence still depends on the specified timing, setting, trust and adversary assumptions. Nothing in these spatial ratios establishes a person's identity, their awareness or phenomenal subject unity.
