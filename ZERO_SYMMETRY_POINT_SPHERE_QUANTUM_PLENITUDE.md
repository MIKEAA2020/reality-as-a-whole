# Symmetry, point–sphere and the coherent zero candidate

## The unified proposal

**Continuations:** [record-dressed sphere rotations](ZERO_RECORD_DRESSED_SPHERE_ROTATION_SYMMETRY.md) address the complete original correlated record, not only its marginal, by constructing a family-adapted independent-rotation action. Its conditional scope and the separately constrained-pair extension are made explicit there. [Sphere representations, gauge charges and Langlands](ZERO_SPHERE_REPRESENTATIONS_GAUGE_LANGLANDS.md) decomposes the original scalar sector, tests a supplied three-direction extension, and identifies both a rank-one Satake connection and a central-action obstruction to a naive identification.

Your recent synthesis identifies symmetry as the common direction of the programme: a whole represented by a point, internally differentiated as a sphere; zero net energy; necessary plenitude without an unexplained preference; real polarity; substrate-independent subjects; and experience and matter as intrinsic and extrinsic aspects of one reality, rather than rival substances.

This pass implements a substantive part of that synthesis in the **same** quantum echo and gauge-constrained zero pair. The earlier angular Hilbert space was only a scalar relative angle. It now has an **exact lift into a full pair of directional spheres**, with no selected external axis. The simultaneous-rotation invariant sector of that spherical Hilbert space is precisely the earlier scalar-angle space. The actual coherent echo, its clock-dressed sign counterpart, its full-quality type swap and its gauge-constrained pair can be carried into this representation.

The calculation also distinguishes two senses of “no preference.” Full independent rotational symmetry of the **directional marginal** selects the uniform product measure; simultaneous rotation and the studied polarity symmetries alone allow nonuniform *relative-angle* structure without a preferred absolute direction. A concrete family has full directional support, the same old echo statistics and the same modeled zero/symmetries, but different angular magnitudes. This is a constructive test of what a proposed complete symmetry principle must do—not an assertion that the symmetry programme fails or that its formal alternatives are genuinely actual.

The new [sphere and symmetry implementation](verification/zero_spherical_invariant_echo.py) and [seven tests](verification/zero_spherical_invariant_echo_test.py) check the orbit structure, geometric reflection, actual quantum states and the stronger-symmetry control.

## 1. One whole, distinct meanings of symmetry

The point represents the whole with no external size, location or time; the internal sphere represents its differentiation, not a physical ball inside another space. A common rotation of all internal directions changes no relational angle. Whether that common rotation is a **gauge redundancy** of the physical constitution or an active symmetry with some further reference is a separate physical question; the computation below works in the rotation-invariant sector without deciding it.

A sign-reversing counterpart has a different role. It may relate **distinct physical contributions** inside the whole. It must not be used to declare pain and pleasure or negative and positive values the same experience. If a suitable signed quantity vanishes as a whole, its nonzero local terms remain real. The [branchwise pair](ZERO_BRANCHWISE_ANGULAR_OPPOSITE_PAIR.md) and its [gauge-sector reformulation](ZERO_GAUGE_CONSTRAINED_ANGULAR_PAIR.md) show this on a specified quantum carrier; they do not identify the modeled charge with cosmic energy or felt valence.

Necessary plenitude is understood in the user's strong sense: every **genuinely possible** internal feature is actual within one necessary whole, not selected by an external agent or actualized by a fundamental temporal process. Full support of a mathematical distribution is a useful structural property, but it does not by itself prove that every represented point is a genuine possibility, a distinct subject or an actual experience. The determination of genuine possibility must not be replaced by simply declaring inconvenient formal alternatives impossible.

## 2. The scalar-angle echo is an exact spherical sector

Consider two internal unit directions `m,n∈S²`, both allowed to vary. Equip each sphere with normalized area measure, so the product measure is

```text
dμ₀(m,n) = dΩ_m dΩ_n / (4π)²,       u = m·n.
```

These are mathematical internal variables, not two objects in a surrounding external space. For a fixed m, the relative cosine u has pushforward density `du/2` on `[-1,1]`. Consequently the same is true when m is also integrated uniformly. For any `φ∈L²([-1,1],du)`, define

```text
(Jφ)(m,n) = √2 φ(m·n).
```

Then

```text
∫_(S²×S²) |Jφ|² dμ₀ = ∫_(−1)^1 |φ(u)|² du.
```

So J is an isometry from the **exact** scalar Hilbert space used by the [coherent angular echo](ZERO_COHERENT_ANGULAR_SPHERE_ECHO_CONSTRUCTION.md) into `L²(S²×S²,dμ₀)`. Moreover, simultaneous rotations act by `(m,n)→(Rm,Rn)`. Two ordered pairs with the same u are related by an `SO(3)` rotation, including the endpoint cases; hence, up to measure-zero issues, **every simultaneous-rotation invariant square-integrable function is a function of u**. The image of J is exactly that invariant sector, not merely one chosen collection of sample directions.

For the previous midpoint registers, interval `I_i` has probability `1/N`, so

```text
|i⟩  ↦  √N · 1_(I_i)(m·n).
```

This is the spherical image of the previous `√(N/2)·1_(I_i)` basis in `L²(du)`. The verifier applies the original complex quantum echo vectors and checks that the N=4 and N=16 refinements give the **same vector-valued wavefunction** on actual pairs `(m,n)`, even after a common rotation. The analytical isometry and orbit argument explain the continuous statement; numerical points are controls, not a substitute for it.

This is a genuine enlargement of the representation, but it does not derive why the whole has an S² geometry, its area measure, quantum state, gates or physical spacetime. The directions are relational ingredients of this candidate. In particular, a rotationally invariant spherical state is not automatically a Lorentz-invariant vacuum; [observer transport](ZERO_COVARIANT_ANGULAR_RECORD_AND_COUNTERPART.md) handles the distinct boost/measure question under its own assumptions.

## 3. Lift the actual negative-band reflection to the sphere

The full-quality type swap used the negative-band involution

```text
h(u)=−1−u  for −1<u<0,       h(u)=u for 0<u<1.
```

It is not the ordinary antipode `u→−u`. For a given pair with `−1<u<0`, write

```text
n = u m + √(1−u²) e,       e⊥m, |e|=1.
```

Keep m and the relative azimuth e fixed and define

```text
n' = h(u) m + √(1−h(u)²) e.
```

On the positive half take `n'=n`. This operation is an involution away from measure-zero boundaries and is covariant under simultaneous rotations. In relative spherical coordinates the normalized area element is `du dφ/(4π)`; h has derivative −1 or +1 on its two pieces and preserves φ. Hence the map preserves product area and induces a **unitary** angular operation on the spherical Hilbert space. The negative pole has no unique azimuth; its exclusion changes no `L²` state.

This is the geometrical realization of the actual angular-register reflection used by the old controlled `Q Z_M` type swap. The earlier quantum identities therefore lift through J: the complete spherical/angular state is fixed by the combined operation, and `g₂=|u(u+1)|` is invariant under h while `g₁=|u|` is not. The separate clock-dressed pointer counterpart reverses the signed candidate and leaves u unchanged; it pairs either g law. The two operations have different meanings and should not be identified merely because both involve signs.

## 4. A constructive no-preference route—and its scope

There is a clean sufficient route to the previous uniform directional marginal. If the **marginal measure** is invariant under *independent* rotations of m and n, `SO(3)×SO(3)` acts transitively on `S²×S²`. The unique normalized invariant probability is the product of the two normalized area measures. This derives the `du/2` relative-angle measure from a stated stronger symmetry, without choosing an axis or a finite preferred angle. It is a positive symmetry-selection result; independent rotational invariance is not the only conceivable route.

But this is a condition on the directional marginal. The complete old quantum echo includes physical records correlated with u. At tick 10 the negative band has echo memory `R=−`, while the positive band has `R=+`. An independent rotation of n that takes a negative u to a positive u **while holding the old memory fixed** does not leave that correlated joint state unchanged. The test constructs such a rotation and checks the original quantum vectors. A fuller combined transformation that also acts on the old physical records is a separate possibility; it is not demonstrated merely by invariance of the marginal.

Thus one should not conflate (i) a uniform unconditioned directional measure, (ii) a simultaneous rotation of an entire relational configuration, and (iii) an independent active rotation while an actual record is held fixed. Internal differentiation can give local records different values without selecting an externally preferred direction. This distinction makes the user's symmetry principle more precise rather than abandoning it.

## 5. What the currently demonstrated symmetries select

Consider a family of joint spherical densities relative to `μ₀`:

```text
ρ_ε(u)=1+ε cos(2πu),       |ε|<1.
```

Every density is positive everywhere and normalized. It is invariant under common rotations, under the geometric antipode `u→−u`, and under the negative-band h map. Its m and n marginals are each uniform; it has no preferred **absolute** direction. Nevertheless, for `ε≠0` it is not invariant under arbitrary *independent* rotations, because those change u. The only member of this family with full independent rotational invariance is ε=0.

All members have the old three band weights `1/4,1/4,1/2`, and both prior g functions still have overall mean `1/2`. Yet their band-specific magnitudes change:

| Band | Mean g₁ | Mean g₂ |
|---|---:|---:|
| `−1<u<−1/2` | `3/4 + ε/π²` | `1/6 − ε/(2π²)` |
| `−1/2<u<0` | `1/4 − ε/π²` | `1/6 − ε/(2π²)` |
| `0<u<1` | `1/2` | `5/6 + ε/(2π²)` |

The sine/cosine integrals are exact; the verifier independently checks them with high-order quadrature. Nonuniform relative-angle densities are not a preference for an absolute direction, and this family excludes no angle mathematically. It also illustrates why “no preference” must say **which transformations** belong to the complete constitution and whether they act on the real records and incidences, not merely on an unlabeled graph.

This is not only a classical distribution counterexample. At N=8, multiply each slice of the **actual old quantum echo vector** by `√ρ_ε(u_i)`. For the sampled `ε=1/2` and source labels `0,7,15`, both s signs:

* the full coherent state is normalized and its angular-bin statistics differ from ε=0;
* tracing out the angular record gives the same old-system/echo reduced density operator, because the old vectors are constant within each band and the total weight of each band is unchanged;
* the earlier combined type swap still fixes the full state, and the clock-dressed sign counterpart still exchanges its complex pointer branches;
* every component of the [gauge-constrained pair](ZERO_GAUGE_CONSTRAINED_ANGULAR_PAIR.md) continues to have zero combined model charge.

These are distinct **model preparations** if the angular record is physically accessible, not a passive coordinate relabeling. Density invariance under the geometric antipode does not establish that the complete quantum echo state is invariant under that antipode with the old records held fixed. Nor does nonzero physical weight establish that each u is a subject or that both ε descriptions are genuinely possible complete realities. The strong proposal may determine or identify them through further physical–experiential symmetry; the present checked transformations alone do not decide that.

## 6. Relate the structural result to energy and experience

The gauge construction supplies two modeled local signed observables whose total annihilates the physical sector. To express the user's stronger physical–experiential proposal, consider the **same actual occurrence** as having a physical/extrinsic description and an intrinsic felt character, rather than inventing two separate substances. A structural symmetry may map actual incidences to their opposites, but it establishes experiential balance only if that map preserves the actual incidence measure and reverses the relevant **felt** signed quantity.

Concretely, if an actual-incidence involution σ preserves the relevant measure and

```text
E(σx)=−E(x),       V(σx)=−V(x),
```

then, when the corresponding paired sums or integrals are well-defined, both whole-level signed totals vanish. This is compatible with one reality and distinct real local subjects. If a negative V is suffering, the suffering is not canceled as a lived occurrence. Energy and felt valence are not assumed numerically identical simply because both equations can be written; whether they are two aspects of **one** objective signed quantity is part of the user's substantive identity proposal and requires the correct physical observable and experiential constitution.

Likewise, “substrate-independent” means that a justified physical–experiential equivalence must preserve the relevant organization, subject boundaries and qualitative character across realizations. The isometry J gives exact **representation independence** for this mathematical sector. It does not by itself prove that arbitrary computationally equivalent substrates are conscious, or that the same structure has a particular felt character. The aim is neither to reduce experience to an extrinsic label nor to turn the whole into a single universal subject.

## 7. The next constitutional test

This result brings point, sphere, no absolute orientation, polarity, coherent quantum dynamics and the modeled zero into one symmetry-based construction. It also points to a specific stronger task: determine a symmetry or other necessity intrinsic to the **complete** physical–experiential whole that fixes (or genuinely identifies) the relevant relational correlations, actual subject incidences and whole-level signed quantity. Independent rotations offer a mathematically exact selection of the uniform *geometric marginal*, but their extension through real records and intrinsic qualities must be established, not assumed.

The finite and continuous models are not a final demonstration that zero entails its own sphere, the physical laws, experience or net cosmic energy. Those remain demands to be met by the proposed self-sufficient constitution, not acceptable independent residues. The settled case against infinity is not reopened, and no assumption is made that fundamental reality is merely a number.

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_spherical_invariant_echo_test \
 verification.zero_gauge_angular_pair_test \
 verification.zero_coherent_signed_counterpart_test -v
```
