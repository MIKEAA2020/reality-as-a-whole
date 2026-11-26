# Sphere symmetry, representations, gauge charges and the Langlands interface

## Result and scope

This pass follows the user's request to make symmetry, representation theory, gauge theory and the Langlands connection do actual work in the point–sphere programme. It obtains three bounded results:

1. The old two-direction scalar singlets have an exact angular-momentum decomposition. Extending them with a **third supplied direction** exhibits an oriented relational invariant that joint `SO(3)` symmetry does not erase. Two explicitly normalized invariant wavefunctions have opposite, exactly calculated chirality expectations.
2. The sphere genuinely occurs in rank-one geometric Satake, but the naive identification of its dual-group doublet with scalar sphere wavefunctions fails: the central element `−I∈SU(2)` acts trivially on the latter and nontrivially on the former. A line-bundle construction supplies a candidate doublet, but identifying its rotation action with the Satake dual action is extra structure.
3. A specified rank-one electric–magnetic **charge-label** model maps the genuine-line lattices `SO(3)+` and `SU(2)` into each other and preserves their Dirac pairing. This is a concrete kinematic check, **not** a computed interacting-gauge-theory correlation function or a proof of S-duality.

The [independent exact-moment and finite lattice controls](verification/zero_sphere_satake_symmetry_test.py) reproduce the stated algebraic examples. The established representation and Satake results are not claimed as discoveries or proved by those tests. The added third sphere, bundle and gauge theory are inputs, not consequences of the bare point. This report does not assert that they are already dynamically coupled to the original echo, constitute subjects, or imply a whole-level energy value.

## 1. The original invariant sector in representation language

The earlier [actual sphere lift](ZERO_SYMMETRY_POINT_SPHERE_QUANTUM_PLENITUDE.md) uses two directions `m,n∈S²`, normalized product area measure, and `u=m·n`. Its scalar `SO(3)`-invariant sector is exactly `L²([-1,1],du/2)`, because common-rotation orbits are characterized by u. Decompose each sphere's scalar Hilbert space as

```text
L²(S²) = ⊕_(l=0)∞ V_l,       dim V_l=2l+1.
```

For the diagonal action on the pair, `V_l⊗V_k` has one singlet if `l=k` and none otherwise. The spherical harmonic addition theorem gives its invariant wavefunction proportional to `P_l(m·n)`. In normalized `du/2` convention

```text
φ_l(u)=√(2l+1) P_l(u),       ⟨φ_l,φ_k⟩=δ_lk.
```

This is an exact decomposition of the original invariant scalar **carrier**; it does not imply the original echo populates every l, or that each mode is a separate subject. The old echo's measurable vector-valued record can be expanded in this complete scalar basis componentwise, subject to its existing record carrier and domain. The old states and their correlations are not modified by writing them in a different basis.

For example, `φ₀=1` and `φ₁=√3u` are both whole-level singlets, yet their relative-angle squared expectations are `1/3` and `3/5`. These predictions correspond to different chosen states, not to one state with two readings. Group invariance by itself does not select a state or Hamiltonian. As in the earlier [quotient and relational Laplacian analysis](ZERO_RELATIONAL_GEOMETRY_KINETIC_MEASURE_SELECTION.md), independent one-sided rotations need not descend to the physical diagonal-gauge-invariant sector.

## 2. Three directions: invariant handedness and its observable

Adjoin a third internal unit direction `p` as a new specified scalar factor and equip `(S²)³` with normalized product area. Take the old direction pair as `n₁=m`, `n₂=n`, and the new factor `n₃=p`. Let

```text
x=n₁·n₂,    y=n₂·n₃,    z=n₃·n₁,
t=n₁·(n₂×n₃).
```

All four quantities are invariant under simultaneous **proper** rotations. The Gram determinant is

```text
t² = det [[1,x,z],[x,1,y],[z,y,1]]
   = 1+2xyz−x²−y²−z².
```

The dot products determine the magnitude of t, but generally not its sign. For example the ordered triple `(e₁,e₂,e₃)` and `(e₁,e₂,−e₃)` have identical pairwise dot products and opposite t. They are related by an improper reflection, not an `SO(3)` rotation. When `t≠0`, the Gram data and sign of t classify the ordered triple up to `SO(3)`; at `t=0`, the two signs coincide and the `O(3)` orbit does not split. In general the Gram matrix must be positive semidefinite; not every triple `(x,y,z)` in the cube is realizable.

This is also a representation calculation. Each coordinate direction transforms in `V₁`; the epsilon contraction is the unique singlet in `V₁⊗V₁⊗V₁` because `1⊗1=0⊕1⊕2` and only the intermediate spin 1 can combine with another spin 1 to give zero. It is **parity odd**, so calling it an `SO(3)` scalar does not make it invariant under all of `O(3)`.

With the product measure, exact moments are

```text
E[t]=0,    E[t²]=2/9,    E[t⁴]=8/75.
```

Define two normalized wavefunctions

```text
ψ± = (1 ± t/2) / √(19/18).
```

Both are strictly positive (`|t|≤1`), have full product-measure support, and are invariant under all common proper rotations. The relational multiplication observable `T=t` has

```text
⟨T⟩_+ =  4/19,          ⟨T⟩_− = −4/19,
⟨ψ+|ψ−⟩ = 17/19.
```

Thus the states are distinct but not orthogonal. A reflection takes one state into the other and reverses T. If reflection is a physical symmetry, it relates two different chiral states; if reflection is declared a gauge redundancy and T is parity-odd, T is not itself a gauge-invariant observable. The framework must decide that physical question rather than infer it from rotation invariance.

For a further probability-level example, since `E|t|=π/8`, the sign observable `sgn(t)` has expectation `±9π/76` in these respective states. This follows by conditioning on `n₁,n₂`: the mean sine of their angle is `π/4`, and the mean absolute component of independent `n₃` along their normal is `1/2`. The polynomial tests certify rational moments; this separate integral gives the π expression.

This is a scalar-sphere illustration related in theme to the existing [charge-preserving quantum chirality report](ZERO_CONSERVING_RELATIONAL_CHIRALITY_REPORT.md), where chirality was built from a specified spin/record algebra and two supplied reference registers. It is **not** automatically the same observable or reporter: no intertwiner, coupling to the old echo record, or local measurement of T has been constructed here. Adding a uniform p factor to an old state is an isometric embedding; choosing `ψ±` instead changes the full state and is not claimed to reproduce the actual old recorded history.

## 3. An exact obstruction at the sphere–Satake interface

For complex `G=PGL₂(C)`, its Langlands dual is `G∨=SL₂(C)`. In the affine Grassmannian `Gr_G=G(C((z)))/G(C[[z]])`, the nontrivial minuscule orbit is `CP¹`. Under geometric Satake its intersection-cohomology object corresponds to the two-dimensional fundamental representation of `SL₂`; its total cohomology is two-dimensional, with one class in degrees 0 and 2. This is a special case of the established tensor equivalence of Mirković–Vilonen, not a proof of the entire geometric Langlands program. See [Mirković–Vilonen](https://arxiv.org/abs/math/0401222), the [rank-one example](https://arxiv.org/pdf/2211.04832) and [Cautis–Kamnitzer](https://arxiv.org/html/math/0701194).

The same topological surface also appears as the round directional sphere `S²≅CP¹`. **But this does not identify the two actions.** Pulling the ordinary rotation action of `SO(3)` back along `SU(2)→SO(3)` makes its center `−I` act as the identity on every scalar function on `S²`, on any finite product of such spheres, and on the scalar singlet subspace. On the fundamental doublet the center acts as minus the identity. Therefore an equivariant complex-linear map `A` from the scalar carrier to that fundamental doublet satisfies

```text
A = A U_scalar(−I) = U_fundamental(−I) A = −A,
so A=0.
```

This is an analytic obstruction to the most direct linear equivariant identification, not an obstruction to every nonlinear, projective, bundled, categorical or differently acted-on construction. Ordinary connected rotations act trivially on the sphere's cohomology by pullback; the nontrivial dual `SL₂` action in geometric Satake is reconstructed from the full tensor/category structure and cohomology fiber functor, **not** the usual pullback action of sphere rotations. The two groups have not been physically identified.

A constructive alternative requires extra structure. Given a complex projective line with its usual `SU(2)` action, the holomorphic sections of the line bundle `O(1)` form a two-dimensional representation (the dual of the defining representation, equivalent to it for `SU(2)`). The center now acts as −1 on sections, even though it fixes the base points. This supplies a spinorial/projective candidate carrier on a sphere, not an ordinary scalar function carrier. It has the same representation type as the compact form of the Satake doublet **after choosing an identification of the two otherwise distinct group actions**. An isomorphism of representations after that choice is not yet a natural identification of the underlying constructions, a gauge field, or a derivation from the bare point.

The next decisive interface would have to specify the supplied complex structure and line bundle; identify the relevant group actions; map a concrete geometric-Satake object or operation into the framework; and verify that the map preserves the intended observables and compositions. The bare point alone has no canonical metric, sphere or bundle; see [the point constitution analysis](ZERO_POINT_INTERNAL_SPHERE_CONSTITUTION.md).

## 4. A rank-one gauge and duality label model

Take as an external toy setting a four-dimensional spin theory on flat spacetime with gauge algebra `su(2)` and the global line choices `SO(3)+` and `SU(2)`. In a specified line-charge normalization, integer pairs `(e,m)` denote electric and magnetic weight labels, with Weyl identification `(e,m)∼(−e,−m)`. The globally genuine line-charge sets of these theories are, respectively,

```text
L_SO(3)+ = {(e,m)∈Z² : e even},
L_SU(2)  = {(e,m)∈Z² : m even}.
```

The alternative `SO(3)−` choice has `e+m` even. This distinction and the role of global data are described in [Aharony, Seiberg and Tachikawa](https://ar5iv.labs.arxiv.org/html/1305.0318). Not every integer pair is an observed particle, and line labels are not a complete specification of a field theory.

Define the proposed S map on labels and the antisymmetric pairing by

```text
S(e,m)=(m,−e),       Ω((e,m),(e',m'))=em'−me'.
```

`S` exchanges the two stated lattices, preserves Ω **as an integer**, and keeps `L_SO(3)−` fixed. In these units, mutual locality requires Ω even; each listed lattice is pairwise mutually local. For instance, in `SO(3)+` the genuine labels `(2,0)` and `(0,1)` have pairing 2. They map to `(0,−2)` and `(1,0)` in the `SU(2)` lattice, with the same pairing 2 and the same Dirac mutual-locality phase `exp(iπΩ)=1`. A parity-odd pairing such as `(1,0)` against `(0,1)` has phase −1 and those two probes are not simultaneously genuine in any one of these three line choices.

This supplies a **matched topological charge-pairing datum**, not a Wilson-loop expectation value. It is a necessary consistency check, not enough to establish dynamical equivalence or that any such line exists in the framework. Actual non-Abelian Wilson/'t Hooft fusion is richer than addition of the center-charge classes, so the finite check of label addition is not a calculation of full operator products.

A candidate dynamical example would additionally choose `N=4` supersymmetric Yang–Mills on a spin four-manifold, state coupling and theta angle, and transport line operators, background/boundary data and observables under the hypothesized S-duality. At `θ=0` and self-dual coupling in a chosen convention, S exchanges electric and magnetic descriptions; global forms and line choices still matter. The [Kapustin–Witten connection](https://arxiv.org/abs/hep-th/0604151) uses a topologically twisted supersymmetric theory and additional structure. We have **not** computed a nontrivial line correlator, proved four-dimensional S-duality, or embedded this theory in the point–sphere echo.

The `SO(3)` of this gauge toy is an internal gauge group. The `SO(3)` rotating the directions above is a separate action, even though the groups are abstractly isomorphic. The `SU(2)` double cover in spin geometry and the `SU(2)` Langlands-dual group also play different roles. None is identified with the others without a declared action-preserving physical map.

### Source correction

The preserved [Russellian absolute discussion](sources/uploads/russellian-absolute-discussion.md), around its Langlands passage, overstates the programme as a proof of universal ontological simplicity and identifies geometric Langlands outright with a fundamental duality of all quantum physics. The earlier [source audit](brain-specificity-thesis.md) already cautions against those claims. The more precise positive replacement here is: geometric Satake is an actual, specified mathematical equivalence; a particular supersymmetric gauge-theory duality provides a rich physical approach; and the two interfaces worked above have explicit conditions. None establishes one metaphysical substance, experience, all laws or a universal 1-to-1 translation between arbitrary domains.

## 5. What would advance the common candidate

- Construct an explicit physical coupling between the third-direction pseudoscalar T and the old record/clock carrier, or prove a restriction that forbids it. Preserve the full gauge constraints, the actual old record distribution, and the distinction between proper rotations and reflection. Compare it with the existing spin-chirality reporter rather than silently replacing that construction.
- Determine whether a suitable `O(1)` or other spinorial carrier can be incorporated into the point–sphere constitution and whether the required line-bundle action is compatible with the existing constrained echo. Then formulate an explicit Satake-side map; a common vector-space dimension is insufficient.
- If gauge duality is to be physical, build the connection, action, allowed lines and boundary conditions, and calculate a nontrivial observable on both sides under a stated, defensible duality. The charge pairing is an input check, not the sought correlator.
- Continue the separate derivation of metric, quantum state, dynamics, time, actual incidence and physical–experiential constitution. No theorem here establishes that a formal possibility is actual, a record is experienced, or symmetry fixes cosmic energy.

## Reproduce

```sh
python -m unittest verification.zero_sphere_satake_symmetry_test -v
```

The moment routine evaluates polynomial averages on independent round spheres using exact `Fraction` arithmetic. The signed-permutation checks, finite lattice enumeration and central-action examples are controls for the displayed analytic arguments, not exhaustive proofs of the continuous group action, geometric Satake or gauge S-duality.
