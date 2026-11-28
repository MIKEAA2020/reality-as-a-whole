# Zero, internal clocks and plenitude: a cross-model rigor review

## Scope and result

This batch returns to central claims in the [self-subsistence argument](ZERO_TOTALITY_SELF_SUBSISTENCE_ARGUMENT.md), [one-reality synthesis](ZERO_ONE_REALITY_NECESSARY_PLENITUDE_SYNTHESIS.md), [plenitude analysis](ZERO_PLENITUDE_NECESSITY_AND_TWO_SENSES.md), [FLRW zero-constraint model](ZERO_TOTALITY_FLRW_CONSTRAINT_AND_ENERGY.md), and [Poincaré energy argument](ZERO_LORENTZ_ENERGY_ZERO_WHY_CHAIN.md). It checks selected logical and physical claims, not every claim in those texts.

The principal new calculation uses the **same** effective Einstein–scalar model, not an unrelated toy. A regular canonical transformation changes the apparent matter/gravity split and produces a candidate clock that is usable on one constraint branch but constant on the other. The model's positive physical scalar density and relational evolution remain intact. This sharpens why neither a chosen decomposition of a zero constraint nor a formal clock change alone supplies an objective whole-energy or a globally valid physical clock.

Separately, the modal and incidence checks clarify the scope of the proposed necessary plenitude without treating mathematical alternative models as established genuinely possible alternative complete realities. Neither analysis derives the zero-energy and intrinsic-experience thesis or proves it impossible.

## 1. The same FLRW constraint in mixed variables

Take the classical spatially flat unit-fiducial-volume three-torus model of the FLRW report, with `a>0`, `κ>0`, and the scalar momentum `p_φ≠0` on the clock branch. Its phase space and constraint are

```text
{a,p_a}={φ,p_φ}=1,
C = −κ p_a²/(12a) + p_φ²/(2a³) = 0.
```

For the two momentum branches, using `σ=±1`,

```text
p_a = σ sqrt(6/κ) p_φ/a,
ρ_φ = p_φ²/(2a⁶) > 0,
da/dφ = −σ sqrt(κ/6) a.
```

All of these are stated within an assumed classical spacetime, not derived from a non-spatiotemporal constitution. The sign σ labels the branch relative to the scalar momentum, not an assumed sign of energy.

Now define a new clock candidate and its conjugate variables, for a constant λ and a fixed reference scale `a_*` merely making the logarithm dimensionless:

```text
χ = φ + λ log(a/a_*),       P_χ=p_φ,
P_a = p_a − λ p_φ/a.
```

This map is invertible and canonical on `a>0`: the symplectic one-form satisfies `p_a da+p_φ dφ=P_a da+P_χ dχ`. The same constraint becomes

```text
C = −κ P_a²/(12a) − κλ P_a P_χ/(6a²)
    + (1/2−κλ²/12) P_χ²/a³.
```

At `λ=λ_*:=sqrt(6/κ)`, the separate `P_χ²` term is exactly zero and

```text
C = −κ P_a/(12a) · (P_a+2λ_* P_χ/a).
```

This does **not** make the real scalar matter or its positive stress density disappear: the original scalar field is `φ=χ−λ_* log(a/a_*)` and `ρ_φ=P_χ²/(2a⁶)` remains strictly positive. The old “negative gravitational term plus positive scalar term” remains a meaningful decomposition when the original metric/scalar action and its variables are specified. What fails is treating the coefficients of the terms in **every canonical expression** as uniquely determined independent physical energy contributions. The mixed term encodes the variable dependence; the action and stress-tensor identification must be transported too.

## 2. An exact branchwise clock obstruction and matching domain

The new candidate χ has Hamiltonian rate

```text
{χ,C}=p_φ/a³ − λ κ p_a/(6a²).
```

On the constraint branches with `λ=λ_*`,

```text
{χ,C}=(1−σ)p_φ/a³.
```

For `σ=+1`, χ is constant on each gauge orbit: it is **not a clock there**, despite the canonical map itself being regular. For `σ=−1`, `{χ,C}=2p_φ/a³≠0`; χ is a valid local monotonic clock whenever φ is. On that branch the clock readings satisfy

```text
χ−χ₀ = 2(φ−φ₀),
a(χ)=a₀ exp[(sqrt(κ/6)/2)(χ−χ₀)].
```

This equals the original `a(φ)=a₀ exp[sqrt(κ/6)(φ−φ₀)]` after the stated change of readings. Thus the same model gives both a **successful relational comparison on the overlap** and a concrete failure of global clock coverage. It does not say φ and χ represent identical physical devices, imply their measurement instruments agree, or produce locally experienced succession. The excluded `p_φ=0` set and the branch intersection require separate treatment.

The original factorization makes the obstruction transparent: `P_a=0` is the σ=+1 branch, while `P_a=−2λ_*P_χ/a` is the σ=−1 branch. A globally invertible kinematical coordinate transformation is not the same thing as a globally good time variable.

### Constraint normalization and relational observables

Let `C'=fC` for smooth, nowhere-zero f on an open region. For any smooth F,

```text
{F,C'} = f{F,C}+C{F,f}.
```

On `C=0`, the gauge vector fields have the same tangent directions; when f is positive their local orientations agree. For a clock T with `{T,C}≠0`,

```text
(dF/dT)|_{C=0} = {F,C}/{T,C} = {F,C'}/{T,C'}  on C=0.
```

This is local classical on-shell equivalence. It requires nonzero clock rates and regular rescaling; it does not establish global completeness, equality of boundary charges, quantum ordering, physical-clock instruments, or identity of C with a unique whole-energy. Phase-space-dependent lapse redefinitions and off-shell terms require the usual constrained-system care. The zero constraint is preserved while its off-shell coefficients and separation into terms can change.

## 3. Why the Poincaré and compact-cosmology routes are not yet one proof

The Poincaré review's conditional character argument is valid in its declared setting: an invariant normalized ray for a strongly continuous honest representation of the connected Poincaré group has zero generators if the group character is trivial, and the perfect Lie algebra supplies that triviality. This relies on a global action and on identifying its translation charge with the relevant whole energy; it is not obtained from local Lorentz covariance of arbitrary curved spacetime.

The FLRW model's spatial three-torus gives a simple precise obstruction to simply transferring the **global** boost assumption. Even for a flat static torus with a noncompact time direction, a spatial identification vector `(0,L,0,0)` is sent by an x-boost to a vector with time component `−γβL`. For nonzero β that is not an element of the purely spatial identification lattice. Hence a generic continuous boost does not descend to a global symmetry of that quotient. A local tangent-space Lorentz transformation remains meaningful, but it is not thereby an active global Poincaré symmetry of the complete toroidal cosmology. The full dynamical FLRW model has additional curvature and symmetry issues.

The two analyses can be consistent without being identical: one concerns a compact generally covariant constraint, the other a global group representation and its charges. A candidate recovery map must specify the underlying carrier, an appropriate regime or boundary limit, the physical translation generator, and a correspondence with the relevant gravitational and matter quantities. No such map follows just from setting both symbols equal to zero.

A related stress-energy ambiguity is concrete. With metric signature `(−,+,+,+)`, let a vacuum contribution be `T^vac_{μν}=−ρ g_{μν}` and suppose the field equation is

```text
G_{μν}+Λ g_{μν}=κ(T^matter_{μν}−ρ g_{μν}).
```

The same equation can be written with `Λ_eff=Λ+κρ`. The simultaneous change `ρ→ρ+δ`, `Λ→Λ−κδ` preserves `Λ_eff` and the displayed equation. This is a **parameterization/renormalization freedom when both terms are allowed to vary**, not a claim that vacuum energy has no gravitational effects or that an observed effective cosmological constant is arbitrary. Keeping Λ fixed while changing ρ generally changes the field equations. Lorentz invariance of a stress tensor by itself permits the coefficient ρ; identifying its value with a global charge requires additional boundary and physical input.

## 4. Necessity, plural internal occurrences and measure

For a global proposition p, classical modal duality and the strong schema `◇q→q` applied to `q=¬p` imply

```text
p → ¬◇¬p → □p.
```

If actuality implies possibility, the biconditional form `◇q↔q` also gives `□p↔p`. This is a genuine conditional consequence of the user's stated global thesis, not a deduction of the thesis from a symbol or of a unique phenomenal constitution from its modal form. It does not assume a universal subject and is distinct from a temporal initial-value determinism.

The proposition language is consequential. In a Kripke **logical control**, let two distinct semantic points see each other but agree on all atoms in a restricted language. By induction they agree on every formula built from those atoms, Boolean operators and the modal operators; `◇p↔p` can hold throughout that language even though the semantic points are distinct. If instead every subset of the point set is expressible and the current point is accessible from itself, the schema rules out any *other accessible point*: the singleton proposition true only at that other point would be possible but false here. This is the language-scope distinction already noted in the [existing plenitude tests](verification/zero_plenitude_necessity_test.py), made explicit rather than a new discovery. Semantic points are formal devices; neither construction establishes distinct genuinely possible physical wholes, nor does it refute a necessarily unique whole.

An internal-feature version asks a different, constructive question: which predicates F are **genuinely admissible as occurrences within the one whole**, and does each such predicate have an actual witness there? Plenitude of internal witnesses can coexist with different, mutually exclusive qualities at **different** incidences; it does not make every logically expressible feature genuinely admissible, nor place incompatible qualities on the same incidence. Defining admissible to mean “already witnessed” would make the condition tautological; the necessary constitution must supply an independent criterion if it is to explain plenitude rather than rename it.

Even an exhaustively specified finite incidence set and its possible/actual support need not determine normalized weights. For two stipulated distinct incidences with both weights positive, `(1/4,3/4)` and `(3/5,2/5)` have the same support and normalization but different first-incidence probabilities. This mathematical comparison does **not** assert two genuinely possible complete physical–experiential realities: the stronger actual constitution may fix a unique measure. It shows that support, qualitative labels, and plenitude alone do not mathematically select that measure without further structure. Nor does an abstract sign label by itself prove pleasure, suffering, or a subject.

## 5. A sharper limit on the canonical opposite

The self-subsistence argument correctly observes that, in a specified additive group A, a balance equation `x+y=0` has the unique solution `y=−x`. But a unique additive inverse need not be **distinct** from x: in the nontrivial group `Z/2Z`, `1=−1` and `1+1=0`. More generally any nonzero element with `2x=0` is self-inverse. This is an algebraic equality of values, not a claim that two differently indexed occurrences are automatically the same subject.

To infer a real signed opposition one needs further structure. For example, in an ordered abelian group with translation-invariant order, `x>0` implies `−x<0` and in particular `x≠−x`. This is a sufficient mathematical condition **if** the order is justified; it does not itself identify an order with felt value. There is also a useful obstruction: if `v:A→R` is an additive homomorphism and x has finite order n, then `n v(x)=v(nx)=0`, so `v(x)=0`. Thus every additive real-valued homomorphism from a finite group is trivial. A finite set of real ± labels is still possible, but must not be confused with a nontrivial additive homomorphism on a finite group; one may use a different structure or relax additivity.

The inverse theorem therefore removes a separate *algebraic matching choice given A*; it does not entail a distinct opposite experience, a real valence scale, or a nontrivial group. This strengthens the existing caution without assuming experience must be an additive scalar or making any real suffering disappear.

## 6. One constitution: the remaining common recovery task

The checked pieces preserve rather than bypass the user's aim. A fundamentally timeless and spaceless constitution is not excluded because the superseded universal-consciousness ontology was rejected. The present framework calls for emergent physical spacetime, real plural subjects and internally experienced succession; it does not assume a cosmic subject or an external physical embedding.

A non-circular unification must supply, within one candidate constitution:

1. **An objectively defined quantity and its scope:** explain its zero, relation to effective constraints, physical local stress and, where applicable, boundary or Poincaré charges. A constraint's algebraic zero and its coordinate-dependent decomposition alone do not do so.
2. **A clock and spacetime recovery map:** derive the effective geometry and admissible clock charts, specify where changes of clock fail, and compare actual instruments and observations—not just the reparameterized classical orbit.
3. **Actual physical–experiential constitution:** explain which organized occurrences are genuinely plural subjects and what qualities they have, without identifying a mathematical record with experience or adding an external experience-producing mechanism.
4. **Possibility, actual incidence and measure:** give a non-circular criterion for genuine admissibility and a measure compatible with redescription, physical access and relevant quantum probabilities. The support control shows why more than a list of occurrences is required.
5. **Self-subsistence:** derive nontrivial differentiation and the foregoing connections from the whole's own nature rather than inserting them under a common name. The elementary group inverse and conditional modal conclusion are useful but do not supply that missing derivation.

No one of the existing FLRW, global Poincaré or finite modal models provides all five. Failure to have the recovery map is an open explanatory gap, not a proof that the user's complete framework is false or that the richer actual constitution cannot fix these inputs.

## Verification

[Cross-model tests](verification/zero_foundation_cross_model_rigor_test.py) check the canonical brackets, transformed constraint, branchwise clock rates and overlap, on-shell rescaling identity, vacuum-parameter shift, torus boost obstruction, self-inverse group values, and finite modal/measure controls. The symbolic checks use the stipulated classical equations; they do not establish the physical universe's energy, a subject or a no-residue derivation. Existing FLRW, modal and gravity-clock tests are run alongside these focused checks in the review workboard.
