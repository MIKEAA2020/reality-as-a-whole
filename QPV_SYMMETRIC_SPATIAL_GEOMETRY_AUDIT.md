# Quantum position verification: a symmetric geometry control

## Bottom line

In a simplified, symmetric timing model, a single stationary responder must lie in the **intersection of two balls**, while the classical spoofing locus defined by the paper's Methods becomes a **prolate ellipsoid**. For an invented 200 m separation and a timing allowance corresponding to `R = 110 m`, the respective axial lengths are **20 m** and **220 m**; the classical-to-single-responder ratios are **11** for length, about **12.84** for projected area and **14.4375** for volume.

These are synthetic geometric calculations, **not** the experiment's 2.47, 4.48 or 4.53 ratios, nor an independent proof of its security. Geometry alone cannot establish that an attacker is excluded by a Bell test. The goal is to make the distinction between a geometrical single-location constraint and a colluding-adversary constraint explicit.

## Setup and assumptions

This follows the target-region definitions in the Methods of the [supplied PDF](KAVURI_QUANTUM_POSITION_VERIFICATION_SUPPLIED_PDF_AUDIT.md), but is an independently calculated special case. Place verifiers at `A=(-a,0,0)` and `B=(a,0,0)`, so their separation is `2a`. Both challenges are released at time zero and both replies must arrive by the same time `T`. Use vacuum light speed `c`, stationary locations, negligible processing time, isotropic propagation, and let

```text
R = cT/2,       R > a > 0,
dA = distance to A,       dB = distance to B.
```

This is not the real setup's asymmetric positions, coaxial propagation or actual timing model. The locus concerns possible **spatial positions of a stationary responder**, obtained by eliminating operation time subject to the deadlines; it is not a four-dimensional spacetime volume. The precise experimental target-region comparison and security proof require the paper's full timing, measurement, error and adversary analyses.

## Derivation

For a **single** responder to obtain both challenges and return a suitable result to both stations by `T`, its location must satisfy

```text
dA ≤ R,       dB ≤ R,       dA + dB ≤ 2R.
```

The last inequality follows from the first two. Hence the spatial region is the lens `E = ball(A,R) ∩ ball(B,R)`. These are timing constraints on a single location, assuming the task actually depends on both inputs; they do not by themselves exclude a distributed response or establish a Bell violation.

In the paper's Methods, the classical region for the corresponding two-colluder spoofing construction is the union of `(ball A ∩ ellipsoid)` and `(ball B ∩ ellipsoid)`. Under the equal-time symmetry the two ellipsoids coincide:

```text
H = { dA + dB ≤ 2R },
E_classical = (ball(A,R) ∩ H) ∪ (ball(B,R) ∩ H) = H.
```

The last equality is special to this symmetric case. To see it, write `ρ²=y²+z²` and `b²=R²−a²`. At axial coordinate `x`, the ellipsoid has `ρ² ≤ b²(1−x²/R²)` for `|x|≤R`, while the nearer ball allows `ρ² ≤ R²−(|x|−a)²`. The nearer-ball bound minus the ellipsoid bound is `2a|x|−a²x²/R² ≥ 0` over this range. Thus every ellipsoid point lies in at least one ball. Conversely, the classical union is explicitly intersected with the ellipsoid.

The intuition is that a colluder at a point in the ellipsoid and a partner at the nearer or opposite verifier, as appropriate to the sphere in the union, can relay the two classical inputs and meet these deadline constraints. For example, if the point is in A's ball, an accomplice at B can send B's input toward it and receive A's input back; the local round trip to A and cross-path to B both fit. This is a specific classical construction for a public two-input task, not a claim that the point alone can spoof it or that it defeats the quantum protocol under the latter's restrictions.

## Length, projected area and volume

The ellipsoid has semi-major axis `R` and transverse semi-axis `b = sqrt(R²−a²)`. The single-responder lens has half-length `R−a`. For 2D projection onto a plane through the verifier axis and for the stationary 3D spatial loci:

```text
length(E) = 2(R−a)                        length(H) = 2R
area(E)   = 2R² arccos(a/R) − 2a sqrt(R²−a²)
area(H)   = πR sqrt(R²−a²)
volume(E) = (2π/3)(2R+a)(R−a)²           volume(H) = (4π/3)R(R²−a²)

length ratio = R/(R−a)
volume ratio = 2R(R+a) / [(2R+a)(R−a)]
```

These are classical/single-responder ratios. The 2D areas are the projections of the corresponding solids, not cross sections of a four-dimensional target region. As `R→a` from above, the lens shrinks to the midpoint and the ellipsoid collapses onto the segment between verifiers; the positive-volume ratios diverge in the limit, but at `R=a` both spatial volumes are zero, so the volume ratio itself is undefined. As `R/a→∞`, the ratios approach one. At `R≥2a`, the lens itself includes the verifier locations; then the single-responder target is no longer remote from the verifiers. These limiting observations do not establish feasibility or quantum security.

## Numerical toy and checks

For `a=100 m`, `R=110 m`, the deadline is `T=220/c ≈ 733.84 ns`. On the verifier axis the lens is `[−10,10] m` and the classical ellipsoid is `[−110,110] m`. A central responder can finish at `200/c ≈ 667.13 ns`; so can two colluders at the verifier locations in the simpler XOR example described in the [earlier gate](QUANTUM_POSITION_VERIFICATION_AND_SUBJECT_LOCATION.md). Both verifier positions lie in the classical region but outside the lens.

| Synthetic stationary spatial quantity | Single responder `E` | Classical locus `H` | Classical / single |
|---|---:|---:|---:|
| Axial length | 20 m | 220 m | 11 |
| 2D projected area | 1,233.58 m² | 15,836.24 m² | 12.8376 |
| 3D volume | `(64,000/3)π` m³ | `308,000π` m³ | 231/16 = 14.4375 |

The [checker](verification/qpv_symmetric_geometry.py) evaluates the sphere and ellipsoid memberships at 5,145 exact-rational on- and off-axis points, checks the volume formulas against separately integrated quadratic cross sections, and checks scale invariance and invalid parameters. The [test suite](verification/qpv_symmetric_geometry_test.py) independently integrates the projected widths numerically, checks off-axis membership, the loss of remoteness at `R≥2a`, selected limits and the exact ratios. All three focused tests and 45 selected project regression checks passed; these are not evidence of the physical or philosophical claims. The [machine-readable receipt](verification/qpv_symmetric_geometry.json) contains only synthetic geometry. A grid is not a proof of continuous containment; the algebra above supplies that proof for the ideal model.

## Interpretation and limits

The lesson is not that the lens must be the true location simply because responses fit its timing. Classical collusion can generate consistent records while operating outside it. The quantum protocol adds a statistically evaluated Bell-based record and a security argument for particular classes of adversaries, along with trusted labs, timing, settings and other assumptions; our geometrical calculation does not verify those assumptions, that argument or any experimental data. Neither a classical spoof nor an admitted honest device by itself determines the identity or location of its human operator.

For the wider framework, a physical access region, the identity of an operator, and a phenomenal subject are distinct claims. A successful conditional location certificate does not measure experience, prove a unique subject, or settle the alternatives in the [private nested-fields comparison](PRIVATE_NESTED_FIELDS_AND_EXPERIENTIAL_CONTENT_COMPARISON.md). It also assumes effective spacetime and causal propagation rather than deriving them. See the [supplied-PDF audit](KAVURI_QUANTUM_POSITION_VERIFICATION_SUPPLIED_PDF_AUDIT.md) for its unresolved reporting and source-date discrepancies.
