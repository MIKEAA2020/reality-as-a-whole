# Point–sphere, signed experiential candidates and the common echo

## Direct result

**Coherent quantum continuations:** [the full echo symmetry](ZERO_FULL_QUANTUM_ECHO_TYPE_SYMMETRY.md) implements a physical two-band record and repaired joint swap. The later [coherent angular construction](ZERO_COHERENT_ANGULAR_SPHERE_ECHO_CONSTRUCTION.md) builds a common continuous scalar-angle Hilbert-space extension of the actual quantum echo, and [covariant transport](ZERO_COVARIANT_ANGULAR_RECORD_AND_COUNTERPART.md) distinguishes changes of observer from passive coordinates. Neither is a full S² carrier or a derivation of spacetime.

This pass brings the user's **point–sphere, zero, experiential cancellation, necessity and relational-clock proposals** into the already implemented stationary sphere–echo interface. The aim is not to identify a mathematical sign with experience; it is to give the zero constitution a more specific common physical–experiential construction to explain.

A new rotationally invariant angular extension recovers the old echo's **entire reduced sign distribution at every tick**, including the same claim/target controls and two-clock statistics. It also supplies continuous nonzero signed candidate magnitudes, paired by a sign-reversing operation. Within the stated model and invariant measure, each opposite pair has zero total while each nonzero contribution survives locally.

The integration reveals an important qualification to the [previous incidence-symmetry result](ZERO_SOURCE_INTEGRATION_STATIONARY_SUBJECT_INCIDENCE.md): a transformation exchanging **quality signs** need not exchange their **full magnitudes**. One natural angular magnitude fails that symmetry even though the old binary test passes; another explicitly constructed magnitude satisfies it. Thus the earlier conditional equal-incidence result is not automatically secured by a sign-only symmetry once the interface becomes richer. The positive route survives if the full physical–experiential symmetry is independently established.

This is a **new model extension** of the prior reduced echo, not a derivation of the actual internal sphere, zero's own differentiation, subjecthood, cosmic energy or felt experience. Matching its diagonal record statistics does not establish equality to the original full quantum state or reproduce all its coherences. Nor does the calculation require an external space/time or a simulator.

Implementation: [angular extension](verification/zero_sphere_angular_echo.py), [nine tests](verification/zero_sphere_angular_echo_test.py).

## 1. Audit the source ideas and plan their use

| Preserved input | Retained and adapted | Correction needed |
|---|---|---|
| [Zero/energy/intelligibility exchange](sources/uploads/DeepSeek_Experience-and-non-optimal-world_20261123-0207.txt), [performance/no-residue continuation](sources/uploads/DeepSeek_Experience-and-non-optimal-world_20261123-2.txt) | A zero whole may have real inner differentiation; an articulated determination is not **automatically** an unexplained residue. Demand a single self-subsistent physical–experiential constitution rather than choosing a tolerable remainder. | A zero signed sum, a formal self-referential circle or a closed conserved system does not by itself establish a self-subsisting actual structure. The assistant's historical assertion that structure is necessarily brute was not proved. |
| [Experience/energy correction](sources/uploads/DeepSeek_Experience-and-non-optimal-world_20261123-3.txt) | The user meant **experience**, not awareness, and asks what can cancel experience if experience is fundamental. Suffering is real negative felt valence, not absence. Develop both signs and their magnitudes without erasing local negative occurrences. | Gravitational negative energy does not by itself derive a signed experiential quantity. Valence is one candidate feature, not automatically the entirety or quantity of experience, and ordinal labels alone do not fix additive magnitudes. |
| [Necessity and spacetime continuation](sources/uploads/DeepSeek_Experience-and-non-optimal-world_20261123-4.txt) | Prefer a necessary whole with relational/emergent time and no assumed fundamental preferred foliation. Conditional statistical weights may be meaningful without irreducible open chance. | Necessitated weights alone do not necessitate a particular outcome, and a formal possible record is not automatically a genuinely possible or actual subject incidence. |
| [User's point–sphere proposal](ZERO_POINT_INTERNAL_SPHERE_CONSTITUTION.md), [paired plenitude](ZERO_NECESSARY_PLENITUDE_SIGN_PAIRING.md), [universal-principles export](sources/uploads/DeepSeek_Evaluate-universal-principles_20261125-0858.txt) | Treat an external zero point and internal relational differentiation as two aspects of the proposed one whole; investigate distinct, opposite contributions. Separate additive balance from trigger, count and persistence. | The blow-up and angular metric add mathematical structure, not proven intrinsic contents of a bare zero. The original numbered principles are absent from the export's opening, so its summaries are not treated as the user's verbatim list. |

**Plan:** give the existing `(b,z,s)` support a common, rotation-invariant sphere representation; propagate its exact old echo gates rather than inventing a separate dynamical example; define signed candidate magnitudes and explicit opposite pairing; then verify that the previous *type-swapping* operation preserves, or fails to preserve, the full candidate quantity. Finally use the **same** previously constructed clocks and discrepancy event to compare their predictions.

## 2. Construct the internal angular extension

Model three internal directions `m,n,k∈S²` with independent rotationally invariant area measures. They are relational directions in the construction, not three external spatial points around an actual whole. Let

```text
u = n·m,       s = sign(k·m).
```

For independent uniform n and m, u has density `du/2` on `[−1,1]`; `s=±1` is independent and has equal measure. A common rotation of all directions leaves u and s unchanged. The required sphere, metric, area measure and independence are **specified model inputs**, not already derived from zero.

Define the pre-echo B and j signs on open bands (the exceptional boundaries have area measure zero):

```text
b = sign(u),             z = sign(u + 1/2).
```

This gives exactly the original physical ledger:

| Angular band u | `(b,z)` | Area weight |
|---|---|---:|
| `(0,1)` | `(+,+)` | 1/2 |
| `(−1/2,0)` | `(−,+)` | 1/4 |
| `(−1,−1/2)` | `(−,−)` | 1/4 |

The `−1/2` threshold is uniquely determined **within this chosen one-threshold cap family** by asking that the B-negative, z-negative event have weight `1/4`: `(τ+1)/2=1/4`. It is not a derivation that this family, the two records or their target weights are necessary. Geometrically the threshold is an angle of 120 degrees between n and m; no preferred absolute axis is required.

Start the old echo in `(b,j,r,s)=(b,z,+,s)` and apply exactly the existing 20-step reduced permutation sequence. Coarse-graining the angular variables reproduces the old `(b,j,r,s)` table at **every** tick, including the fixed B target, ready/inverted controls, normal claim and the `(C,D)` claim/quality-disagreement table. This is a common-interface extension, not proof of a unique embedding: other angular partitions could give the same old table. The sphere is not established to be an actual physical subsystem; independently checking the old coherent quantum construction still matters.

## 3. Continuous signs and opposite partners

Introduce two deliberately different nonnegative magnitude functions of the *same* angle:

```text
g₁(u) = |u|,                   g₂(u) = |u(u+1)|.
v_now = κ s j g(u),            v_echo = κ s j r g(u),      κ>0.
```

Both are rotationally invariant relational functions, and are nonzero almost everywhere under the area measure. They are mathematical candidates for a signed physical–experiential quantity **only if** their units, magnitude and felt interpretation are justified. The quantity could be richer than felt valence; neither function establishes what experience fundamentally is.

This richer proposal changes the **boundary requirement**. For example `u=−1/4` and `u=−1/8` give exactly the same old `(b,j,r,s)` record at every tick, but different `g₁` and `g₂` values. The old M–j–E sign algebra alone therefore cannot determine either magnitude. A real subject with locally determined magnitude would need an actual angular carrier/access relation, or a different rule expressed solely in its own accessible algebra. The extension does not grant such access by fiat. The original constant-κ ready calibration must likewise be modified to `κ s z g(u)` for this extension; the earlier Boolean sign-selection theorem does not by itself select g.

Let `P` send `k→−k` while holding m and n fixed. It flips s, leaves u, b, z, the clock and all old gates unchanged, preserves the chosen angular measure, and gives

```text
v_port(Px) = −v_port(x),       |v_port(Px)|=|v_port(x)|.
```

Consequently the signed integral vanishes, including in any fixed old-record or clock cell that does not select s. If—and only if—both related points denote distinct **actual** eligible experience incidences and the incidence weights are transported by this operation, it is a candidate accounting of genuine opposite experiential contributions. If P is merely gauge and identifies the same occurrence, a nonzero scalar felt value cannot be both odd and gauge-invariant. Equal area weights are not by themselves an actual first-person incidence measure.

Either way, **zero does not erase a negative local value**. If later justified as suffering, the negative occurrence remains real; neither averaging nor adding a positive counterpart removes or morally excuses it. The argument is an explicit conditional route from actual pairing to zero, not a derivation that every formal angle is genuinely possible or actual. No preferred temporal direction is used to select a partner.

## 4. Where the binary symmetry does—and does not—extend

The previous pass found the reduced tick-10 active map

```text
D(b,j,r,s) = (b,jr,r,s),
```

which exchanges the two signs. On this angular extension it is realized (away from measure-zero boundaries) by

```text
u ↦ h(u) = −1−u   for −1<u<0,       h(u)=u for 0<u<1.
```

It exchanges the two equal-area negative bands, is its own inverse and preserves `du/2`. Holding the azimuth around m fixed implements it as a measure-preserving map of n's sphere, almost everywhere; the two-sign state at tick 10 is exactly the old `D` image. Since it acts on the initial angular label and the echo orbit is then propagated, its history lift commutes with the clock shift **on this modeled history support**. It changes u and is not established as a symmetry of the original full physical system. Its endpoints and cap boundaries are negligible for the stated integrals, not silently given a physical value.

In order for the combined physical-and-type exchange to preserve the **full signed candidate value**, its magnitude must satisfy

```text
g(h(u)) = g(u) almost everywhere.
```

For `g₁`, this fails: at `u=−1/4` its magnitude is `1/4`, while at `h(u)=−3/4` it is `3/4`. At these points the sign exchange still works, but a purported magnitude-preserving experiential symmetry does not. Thus physical invariance of the binary reduced record and an equal sign count do **not** by themselves justify the previous type-weight selection for this richer quality law.

For `g₂`, `u(u+1)` is unchanged by `u→−1−u`, so the full typed signed value **is** preserved by the combined exchange. Under the previous pass's additional assumptions—two actual incidence types, the strong product/all-effect physical-marginal extension, and invariance of their incidence measure under the combined physical/type operation—equal type weight follows for g₂. Those premises remain substantive; our construction does not establish actual incidences or that this physical operation is an experiential symmetry. The mathematical choice of g₂ is not a proof that zero selects it, and many other invariant magnitude functions exist.

The two functions are not distinguished by the previous signed-zero test, or even by their unconditional absolute first moment: both have `∫g du/2=1/2`. Their conditional predictions differ:

| Sector | `P(b,z)` | `E[g₁ | b,z]` | `E[g₂ | b,z]` |
|---|---:|---:|---:|
| `(+,+)` | 1/2 | 1/2 | 5/6 |
| `(−,+)` | 1/4 | 1/4 | 1/6 |
| `(−,−)` | 1/4 | 3/4 | 1/6 |

These are calculated angle-function moments, not empirical predictions of felt intensity until a calibrated experiential relation and accessible instrument are justified. Equal global balance and equal overall mean magnitude are compatible with different local distributions.

## 5. The same two clocks now distinguish magnitude as well as signs

Use the previously stipulated four-state reference `R=q t mod 4`, with q=1 or 2, and the same event `D=(v_now and v_echo have opposite signs)`, equal to `r=−` except on the measure-zero set where g vanishes. For `R=2`, the earlier tests found `P(D)=1/10` for q=1 and `1/20` for q=2. The angular extension adds:

| Clock | `P(D | R=2)` | `E[g₁ 1_D | R=2]` | `E[g₂ 1_D | R=2]` | `E[g₁ | D,R=2]` | `E[g₂ | D,R=2]` |
|---|---:|---:|---:|---:|---:|
| q=1 | 1/10 | 1/20 | 1/60 | 1/2 | 1/6 |
| q=2 | 1/20 | 3/80 | 1/120 | 3/4 | 1/6 |

For q=1 the discordant cases are the whole B-negative sector at tick 10; for q=2 they lie in the z-negative band at ticks 9 and 11. The clock selects different physical subensembles; it does not cause the user’s confined surface inhabitant to access a richer realm. The clock correlations are stipulated and their registration can alter unconditioned clock coherences, as previously documented. Zero-probability clock events cannot be conditioned on.

This gives a concrete joint target for the next physical–experiential bridge: an independently supported magnitude/report map could distinguish g₁ from g₂ on the *same* cases, rather than only comparing their already balanced signs. A reliable report, its access channel and connection to felt magnitude would themselves need to be established; no experiment is claimed here.

## 6. What this contributes toward the stronger constitution

The result carries several sources through **audit, adaptation and implementation on one candidate**, and it repairs an overbroad possible reading of the earlier type-symmetry result. It shows a precise way an internally differentiated spherical representation can contain local opposite contributions and old echo records while preserving a modeled zero; it also shows why a genuine physical–experiential symmetry must preserve **magnitude**, not only sign.

The main explanatory demand is unchanged: show that the whole's own zero constitution necessitates its directional structure, state, dynamics, actual subjects, real qualitative values and measure, and that its physically meaningful whole-level energy and relevant experiential quantity have the required zero. `g₁`, `g₂`, uniform sphere area and the signs have not been derived from bare zero; their formal compatibility is neither ultimate self-subsistence nor a formal battery pass. A stronger constitution may determine or replace them; no inference here declares these formal candidates to be separate genuinely possible complete realities.

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_sphere_angular_echo_test \
 verification.zero_stationary_subject_incidence_test \
 verification.zero_stationary_clock_claim_quality_test \
 verification.zero_stationary_battery_bridge_test -v
```

The checks use exact rational angular integrals and all 20 reduced tick tables, with a separate numerical rotation sanity check. They verify the defined model only, not actual phenomenal constitution or external-battery eligibility.
