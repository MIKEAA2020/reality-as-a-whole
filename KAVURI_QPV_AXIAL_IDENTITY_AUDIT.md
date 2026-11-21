# QPV axial union: conditional identity and follow-up

## Result and limits

The [previous numerical audit](KAVURI_QPV_ASYMMETRIC_SPATIAL_RATIO_AUDIT.md) found that the preprint's explicit comparable-classical spatial **union**, applied to its rounded timing inputs, gives a 1D ratio of **3.472897**, rather than the reported **4.48(2)**. Here an exact derivation shows that, under specific geometric and timing conditions satisfied by those central inputs, the discrepancy is not a numerical integration artifact: the comparable-classical 1D ratio must equal the ideal-classical 1D ratio **plus one**, for the same input realization.

The reported central values, **2.47(2)** and **4.48(2)**, differ by **2.01**, not one. This comparison alone is not an uncertainty calculation: the estimates may be dependent, and their underlying inputs, sampling, averaging and conventions are unavailable. The algebra applies per common input realization satisfying the conditions, not automatically to independently sampled or differently defined quantities. The ±0.05 printed-unit conditional bound in the [previous audit](KAVURI_QPV_ASYMMETRIC_SPATIAL_RATIO_AUDIT.md) remains separate from measurement uncertainty. This is an apparent definition/numerical mismatch, **not proof of an error's cause, a security failure, or experimental data replay**. The investigation and its [plan](KAVURI_QPV_AXIAL_IDENTITY_AND_AUTHOR_QUERY_PLAN.md) are retrospective, not blind or preregistered.

## Definitions and sufficient conditions

Use the spatial sets and event definitions of [arXiv v2 supplement IV.2](https://arxiv.org/html/2601.16892v2#S4), with fixed verifiers at `A = −L/2`, `B = +L/2`, `L > 0`, speed `c > 0`, releases `sA,sB` and responses `rA,rB`. Let

```text
RA = c(rA − sA)/2,       RB = c(rB − sB)/2
M3 = c(rA − sB),         M4 = c(rB − sA)
E = SA ∩ SB ∩ H3 ∩ H4
C1 = SA ∩ H3,            C2 = SB ∩ H4,       C = C1 ∪ C2
```

Here `SA, SB` are the round-trip balls of radii `RA, RB`, while `H3, H4` are the two-focus ellipsoids with major-axis lengths `M3, M4`. For this proof assume:

1. Positive round-trip radii `RA,RB > 0`, and nondegenerate ellipsoids `M3,M4 > L`.
2. Releases and responses each have separation at least as large as their light-travel-time difference: `c|sA − sB| ≤ L` and `c|rA − rB| ≤ L`. Equality is allowed (lightlike boundary). This means each event pair is spacelike or lightlike, not that both pairs have a common global simultaneity frame.
3. `RA + RB > L`, giving a quantum axial interval of positive length under the other assumptions. This excludes empty or point-only intersections and ensures a finite ratio.

These are **sufficient**, not claimed necessary; the grid below includes a case where the release condition fails but the identity still holds. Degenerate, empty and zero-length cases need separate treatment. The result assumes the cited region and projection conventions, fixed verifier positions, and the same `L` and inputs for both comparators.

## Proof

Write `a = L/2`. On the verifier axis, the two balls have intervals `[-a−RA, −a+RA]` and `[a−RB, a+RB]`; the ellipsoids have intervals `[-M3/2,M3/2]` and `[-M4/2,M4/2]`. All cross-sections are centered on the axis, so an x-coordinate belongs to a projected intersection exactly when its axis point does; these interval intersections thus correctly give projected axial sets.

The release condition selects the endpoints

```text
C1 = [−M3/2, −a + RA]
C2 = [ a − RB, M4/2].
```

For example, `−M3/2 ≥ −a−RA` is equivalent to `c(sA−sB) ≤ L`, and `−a+RA ≤ M3/2` is equivalent to `c(sB−sA) ≤ L`; the two analogous inequalities select the endpoints of `C2`. The response condition ensures `−M3/2 ≤ a−RB` and `−a+RA ≤ M4/2`, equivalently `c(rB−rA) ≤ L` and `c(rA−rB) ≤ L`. With `RA+RB>L`, the inner endpoints overlap. Hence

```text
E = C1 ∩ C2 = [a−RB, −a+RA],       length(E) = RA + RB − L
C = C1 ∪ C2 = [−M3/2, M4/2],       length(C) = (M3+M4)/2 = RA + RB
length(C) = L + length(E)
length(C)/length(E) = 1 + L/length(E).
```

The intersection equality `E=C1∩C2` follows set-theoretically, but positive axial overlap does not guarantee the above endpoint order without the stated conditions. Here the **ideal classical** axial length is `L` as defined in the supplement. Counting both interval lengths without subtracting their overlap would add one quantum length and give ratio `2 + L/length(E)` in this regime; its numerical proximity is an example, **not evidence that the authors did this**. An analogous additive identity for projected area or spatial volume does not follow: their cross-sectional radii vary with position and the overlap volume is not the axial length times a common constant. The independently computed 2D and 3D results remain separate numerical checks.

## Exact checks and counterexamples

The [exact-rational script](verification/kavuri_qpv_axial_identity.py) directly intersects and unions intervals, rather than using the derived formula to compute their lengths. It exhaustively enumerates `c=1`, `sA=0`, integer `L=1..6`, `sB=−8..8`, `rA=1..18`, `rB=−7..19`; translation of all event times is immaterial. It excludes nonpositive radii, degenerate/invalid ellipsoids and zero-measure or empty quantum intervals. Out of the remaining cases, **4,854/4,854** satisfying both light-cone inequalities obey the identity, including boundary equalities; **12,376/16,241** cases outside those sufficient conditions fail it. Finite enumeration is a cross-check, not a general proof. The [receipt](verification/kavuri_qpv_axial_identity.json) records the category counts and examples.

For instance, `L=1, c=1, sA=0, sB=−1, rA=1, rB=3` has positive radii, nondegenerate ellipsoids and quantum length 1, but response separation 2 exceeds L; the comparable-classical union length is 3, not `L+1=2`. Conversely, `L=1, c=1, sA=0, sB=−8, rA=1, rB=2` violates the release condition yet has quantum length 1 and union length 2. Thus failure of a sufficient condition does not by itself prove failure of the identity. The [focused tests](verification/kavuri_qpv_axial_identity_test.py) explicitly check boundary equality, a point-only intersection, degenerate ellipsoid, nonpositive radii, interval union and the counterexamples; rejected cases are not assertions about the identity outside its domain.

For the reported rounded inputs, `c|sA−sB|=41.4013384498 m` and `c|rA−rB|=39.7524799308 m`, both below `L=195.1 m`. Both ellipsoids are nondegenerate, and `RA+RB−L=78.8953169891 m > 0`. Exact decimal-rational arithmetic gives comparable-classical length `273.9953169891 m` and ratios **2.4728970926** and **3.4728970926**. This is not a reconstruction of the authors' unrounded inputs or an empirical uncertainty estimate.

Seven new focused unit tests, the exact enumeration, four asymmetric and three symmetric geometry test methods, the QPV arithmetic checker, and all 45 selected project regression scripts passed. These tests verify only their encoded mathematics and computations, not the source measurements, security proof or wider framework.

## Next step

A [neutral query to the authors](KAVURI_QPV_DRAFT_AUTHOR_QUERY.md) requests the precise 1D conventions, geometry code and timing inputs, as well as clarification of the separately documented count, timing and labeling inconsistencies. It is a draft only and has **not been sent**. None of the geometry results establishes a human operator's identity, phenomenal subject unity or awareness; cryptographic conclusions remain conditional on the paper's trust and adversary assumptions.
