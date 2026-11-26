# Why the type-symmetric kinetic repair adds a long edge

## The issue and result

The [earlier quotient kinetic construction](ZERO_RELATIONAL_GEOMETRY_KINETIC_MEASURE_SELECTION.md) found an unexpected conflict: its free nearest-neighbor relative-angle kinetic operator does not commute with the proposed type swap, although each preserves the uniform echo. Averaging with the swap fixes the commutator but creates a non-neighbor connection. Is that just an N=4 discretization artifact?

**No, under the stated refinement.** At every N divisible by four, exact type symmetry, strict locality on the original interval-bin path, and connectedness are incompatible. The new connection persists and strengthens under refinement. The deeper cause is that the proposed type swap is not continuous in the original quotient topology: it sends points approaching zero from the negative side to points approaching −1, while leaving points approaching zero from the positive side near zero. The original round-sphere quotient regards −1 and 0 as distinct.

There is a **conditional repair**: use a different relational topology, a loop joined to a tail, identifying the endpoints −1 and 0 at a graph vertex. The same reflection is then continuous and can preserve a local graph kinetic form. This is not a proof that the quotient actually has that topology; it trades the original interval geometry and the continuity of the angle coordinate for symmetry-compatible graph locality. The finite N=4 dressed operator is already checked on the existing echo, but a continuum graph echo, its physical accessibility, and the correct physical symmetry remain to be established.

## 1. The failure survives refinement

Put N=4k midpoint bins on [−1,1], `m=N/2`, and let R reverse indices `0,...,m−1` while fixing `m,...,N−1`. Let Q have transitions only between consecutive indices. Since R maps `m−1` to 0 and fixes m, `QR=RQ` forces

```text
Q[m−1,m] = Q[0,m] = 0.
```

The second entry vanishes by strict path locality. Thus the only crossing from the negative to the positive half disappears: the graph is disconnected. This argument is independent of the particular nearest-neighbor rates and does not require positivity. For a conservative positive graph generator, disconnection gives at least two independent constant sector zero modes, so the earlier connected, unique scalar constant mode is lost.

For the particular finite-volume round operator, symmetrization gives *both* `m−1 ↔ m` and `0 ↔ m` rate `N²/8`. The second pair has midpoint angles `−1+1/N` and `1/N`, separated by exactly 1 for every N. It is not becoming short in the original angle coordinate. At N=4 its rate is 2, exactly the previously reported connection. The implementation and [tests](verification/zero_type_reflection_continuum_root_test.py) check N=4 through larger refinements, commutation, constant mode and connectedness. The all-N statements follow algebraically rather than from the sample tests.

## 2. The continuum obstruction, not just a graph picture

Ignoring the measure-zero band junction, the continuum involution is

```text
r(u) = −1−u,  −1<u<0;
       u,        0<u<1.
```

It preserves `du/2` and is a unitary composition operation on `L²`. But it is not continuous at 0 in the interval topology: its left and right limits are −1 and 0. The ordinary smooth relational observable `f(u)=u` belongs to the free round kinetic form domain, while `f∘r` has a jump of size 1 at an interior point and does not belong to that domain. A unitary commuting with a self-adjoint kinetic operator must preserve its quadratic-form domain, so this type swap cannot commute with the original free interval operator. Changing the single value assigned to r(0) cannot remove the jump.

There is also a quantitative discrete witness. With normalized form `E_N(f)=−(1/N) fᵀQ_sym f`, the single long edge contributes

```text
(N/8) [f(1/N)−f(−1+1/N)]².
```

For `f(u)=u`, this is `N/8`, so E_N diverges even though the original free energies approach `2/3`. More generally any bounded-energy sequence must make the amplitudes at those two connected bins asymptotically equal, at least at order `N^(−1/2)`. This is evidence of an emergent gluing constraint, not a full proof of convergence of operators or forms.

## 3. A local graph alternative and its price

Replace the interval topology by a metric graph with a loop parameterized by `−1≤u≤0`, attached to a tail `0≤u≤1`: the loop's two endpoints and the tail's initial endpoint are a single vertex. This is **not** merely a coordinate change on the old interval. The swap reverses the loop and fixes the tail, so it is now a continuous graph automorphism.

An explicit invariant, nonnegative graph form, with the original normalized measure `du/2` on the edges, is

```text
E(f) = (1/2) ∫[−1,0] (1/2−u−u²) |f′(u)|² du
     + (1/2) ∫[0,1]  (1−u²)     |f′(u)|² du.
```

The loop coefficient is the average of `1−u²` and its reflected value and is strictly positive, including value `1/2` at each loop endpoint. Functions are continuous at the common vertex; the associated natural vertex condition is conservation of the sum of outgoing weighted derivatives. At the degenerate tail endpoint use the natural finite-energy/Friedrichs condition, not an assumed separate physical boundary source. The reflection preserves both measure and form. Zero energy forces a constant on each edge and vertex continuity then forces a single constant: the scalar zero mode is unique. The normalized constant still gives `du/2` along the two edges. Other reflection-invariant graph weights and vertex conditions are possible; this form is a candidate, not a unique consequence of symmetry.

A nonconstant compatible control is `f(u)=sin(2πu)` on the loop and 0 on the tail. It is continuous at the vertex, odd under R, and its outgoing loop fluxes cancel. Its graph form is exactly `2π²/3−1/8`. The finite symmetrized energies of midpoint samples approach that value in the tested refinements, which checks a nontrivial mode rather than only the constant ground state. It is not a general spectral or operator-limit theorem. The original angle function u is no longer graph-continuous: its values at the identified ends differ. It remains a bounded measurable label almost everywhere, but it is not an admissible continuous graph coordinate or a finite-energy test function in this graph form.

## 4. Why was the conflict present? Why accept the repair?

1. **Why the added edge?** The original path has one boundary-crossing edge, but the swap takes its negative endpoint to the remote end of the negative band. Symmetry demands the reflected edge too.
2. **Why does refinement not fix this?** The swap approaches a discontinuous interval map; the partner of the boundary remains one unit away in angle, and the finite-volume rate scales as N².
3. **Why can the graph fix it?** It changes which limits are neighbors: both loop ends meet the tail. Locality is relative to the chosen topology and Dirichlet form, not a property of a matrix without a specified configuration space.
4. **Why choose this symmetry and topology?** The earlier swap was constructed to exchange types while preserving a particular coherent echo. Fixing one state does not establish it as a symmetry of all dynamics, all admissible states, or actual subject incidence. Conversely the round quotient follows from a specified two-sphere relational construction; it is not forced by bare zero. There is presently no independent derivation selecting either the graph topology or full dynamical type symmetry.
5. **Meta-level issue.** The constitution must specify together which distinctions are physical, which transformations are genuine symmetries, and which neighborhood/dynamical structure is intrinsic. One cannot infer the full structure just from a balanced scalar, from the invariance of one state, or by renaming a shortcut local. A unified principle could in principle determine them jointly; this analysis does not establish or rule out such a principle.

Other coherent choices remain: keep the interval/free dynamics and treat the type swap as a state-level or partial relation rather than a global dynamical symmetry; retain the swap and accept the long interval edge; drop connectedness; or enlarge the configuration space and derive a suitable continuous action and its effective quotient. A global interval reflection would be a *different* action, not automatically the existing type exchange. Enlarging the space, like graph gluing, requires justification and must not be treated as free ontology.

## 5. Scope and reproduction

The N=4 noncommutation and repair were checked on the actual old-record/pointer vectors and constrained pair, and the dressed full-carrier operator is a chosen extension; the preceding report documents those checks. The N>4 family here refines the scalar angle model only. It does not construct new N-bin original-record vectors, prove an echo continuum limit, establish spacetime nonlocality, demonstrate actual subjecthood or experience, derive a physical Hamiltonian, or settle zero's self-sufficiency. Loop identification must not erase physically meaningful endpoint distinctions without an independent argument.

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_type_reflection_continuum_root_test \
  verification.zero_relational_laplacian_test -v
```
