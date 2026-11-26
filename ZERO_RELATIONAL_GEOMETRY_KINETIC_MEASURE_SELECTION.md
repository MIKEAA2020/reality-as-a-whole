# Relational geometry, a zero mode and the measure problem

## Main result

The [previous pass](ZERO_META_SYMMETRY_RELATIONAL_MAGNITUDE_ROOT_CAUSE.md) distinguished an actual change of relative angle from a change of internal reference frames. Following that distinction through the **physical gauge quotient** reveals a further constraint: a one-sided rotation of the original two-sphere coordinates does not in general act within the gauge-invariant quantum state space. The earlier record-dressed independent rotations were valid on the larger, unquotiented Hilbert space and fixed the particular uniform history, but preservation of the opposite-pair constraint alone did not establish that they preserve *every* frame-gauge physical state.

There is a constructive alternative. The round sphere supplies a natural relational Laplacian on the quotient angle. Its zero mode is constant, its associated area measure is `du/2`, and its finite-bin version has an exact spectrum and can be **dressed with the actual original record and constrained opposite pair**. The resulting positive operator has the original uniform coherent echo as a zero mode; its clock-controlled extension is stationary and maintains the pair's zero constraint. No external time or random cosmic process is needed to state this zero-mode condition.

This advances a candidate principle: **a free, isotropic relational constitution selects the canonical angular state as its zero kinetic mode**. The free operator does not preserve the earlier type swap, but a second explicit, type-symmetric operator retains the same zero mode by adding a non-neighbor angular connection. It is not yet a derivation from zero alone. The round metric, the absence of a relational potential, the physical status of the kinetic operator and the reference record are assumptions that must themselves be accounted for. In particular, other positive gauge-compatible operators have different zero modes; a concrete counterexample below prevents the new construction from silently equating “zero” with “uniform.”

The [implementation](verification/zero_relational_laplacian.py) and [tests](verification/zero_relational_laplacian_test.py) check the finite spectrum, the gauge-sector issue, the constrained original quantum vectors and the counterexamples.

## 1. What actually descends to the quotient?

After choosing the link gauge `L=I`, the residual frame gauge rotates both m and n together. Physical scalar wavefunctions on the original sphere pair have the form `φ(m·n)`. The quotient is the interval `u∈[−1,1]`, including its two distinct endpoint configurations.

Apply an active rotation R to n alone while keeping the link fixed. It maps

```text
φ(m·n)  ↦  φ(m·R⁻¹n),
```

which is generally **not** a function only of `m·n`. Therefore this operation does not map the full scalar frame-gauge-invariant vector sector to itself. One can average it over the frame group to project it back, but the projected map is generally not unitary and does not satisfy the same group composition law. In particular, for the normalized `l=1` state `ψ=√3(m·n)`, gauge projection gives

```text
P_gauge P_(I,R) ψ = [tr(R)/3] ψ.
```

A rotation through `2π/3` has trace zero: the projected vector vanishes even though the rotated vector has norm one. A rotation through `π/2` leaves only `1/9` of the squared norm in this projected component. The code checks these identities using the exact second-moment average of 24 proper signed-permutation rotations; the analytic Haar result follows because the average of `AᵀRA` is `(tr R/3)I`.

This is a correction of **scope**, not a retraction of the earlier unitary formula or its fixed-state check. The earlier rotations act unitarily on the larger sphere/record/pair Hilbert space and fix the specific constant-reference dressed state. The new link formulation imposes an additional frame-gauge physical sector. Since the dressing depends only on u, it is itself frame-gauge invariant; conjugating a generic one-sided rotation by that dressing does not cure this sector-preservation problem. The pair constraint, the frame-gauge constraint and invariance of one state are different requirements. A density operator commuting with gauge transformations is also not automatically supported in the trivial gauge sector.

### The topological reason

This is not just a bad choice of matrix. No nontrivial connected compact group can act continuously on a closed interval by homeomorphisms. To see why, every element of such a group is orientation preserving. For normalized Haar measure define

```text
h(x) = ∫_G g(x) dg.
```

Every g is strictly increasing, so h is strictly increasing and hence injective. Haar invariance gives `h(kx)=h(x)` for every k, so injectivity implies `kx=x`. The action is trivial. Consequently the compact connected independent-rotation group cannot act transitively on this interval as physical point transformations. Quantum unitaries may of course mix functions of u or act on additional physical degrees of freedom; this theorem does not prohibit them. It prohibits identifying the transitive pre-quotient action with a nontrivial point action on this particular relational quotient.

## 2. Geometry supplies a non-arbitrary candidate selector

For a function of `u=m·n`, the round-sphere Laplace–Beltrami operator acting on n reduces to

```text
L φ(u) = d/du [(1−u²) dφ/du].
```

This expression is coordinate-covariant: the relative angle and the round metric are invariant under the internal-frame changes, so it is a well-defined operator on the quotient. With regular/no-flux endpoint conditions, `−L` is nonnegative on `L²([−1,1],du/2)` and its eigenfunctions and eigenvalues are

```text
P_l(u),       l(l+1),       l = 0,1,2,...
```

The unique scalar zero mode is constant. Normalizing it selects the angular probability `du/2`; no particular finite, nonzero angle is chosen. The overall positive scale of the Laplacian changes nonzero eigenvalues but **not** the zero mode or the selected distribution. This uses the round geometry and a free kinetic criterion; it does not show that geometry and criterion follow from zero.

A mathematically equivalent diagnostic is the heat equation `∂_τ ρ=Lρ`: its no-flux stationary probability is uniform, and the first nonzero eigenvalue is 2 in the displayed units. Here τ can be a mathematical smoothing parameter, not external time, an irreversible fundamental evolution, or objective chance. We do not infer that the universe actually relaxes to a state. The timeless zero-mode condition is the relevant constructive proposal.

## 3. An exact finite realization

Take N equal bins of width `h=2/N`, centers `u_i=−1+(i+1/2)h`, and edge weights `p_(i+1/2)=1−(−1+(i+1)h)²`. The finite-volume operator is

```text
(Q_N f)_i = [p_(i+1/2)(f_(i+1)−f_i)
             − p_(i−1/2)(f_i−f_(i−1))] / h²,
```

with zero edge weights at the endpoints. Q_N is real symmetric, has nonnegative off-diagonal entries, row sum zero and a connected nearest-neighbor graph. Thus `−Q_N` is positive, its sole scalar zero eigenvector is constant, and the unique stationary bin law is uniform. Its spectrum is **exactly**

```text
0, 2, 6, 12, ..., (N−1)N.
```

The exactness is not just a numerical coincidence. On the N midpoint values, Q_N maps polynomials of degree k to polynomials of at most degree k, with leading coefficient `−k(k+1)`. Degrees `0,...,N−1` form a basis of the N-dimensional function space, so the distinct diagonal coefficients are all eigenvalues. The tests verify this for N=4, 8, 16 and 24, along with positivity and stochasticity of the finite heat kernel. N=4 has edge rates 3, 4, 3 in the displayed normalization.

## 4. Dress the operator with the existing quantum history

Use the [full-clock/pair construction](ZERO_DRESSED_ROTATIONS_FULL_CLOCK_AND_OPPOSITE_PAIR.md). At a fixed anchor let

```text
D_i = E_i V_i,
H_free = D [ (−Q_4) ⊗ I_record,pair,apparatus ] D†,
D = Σ_i |i⟩⟨i| ⊗ D_i.
```

The E_i are the full pair-basis permutations, and V_i are the actual record-span dressings. This unitary conjugation is defined on the entire four-bin quotient carrier with the enlarged record and pair factors, including unphysical pair states; it is not a new claim about every state of the larger unreduced two-sphere Hilbert space. The constrained pair projector is `D(I⊗P₀)D†`, because the record operations commute with the reference-pair projector P₀. It therefore commutes with H_free. In the physical sector H₁+H₂ remains exactly zero; the kinetic operator is not being identified with either individual model charge or with cosmological energy.

The earlier common-frame construction showed that, after removing D_i, the actual old-record vector is the **same reference vector in all four bins**, for all 16 source labels and both sign pointers. Consequently their uniform coherent superpositions are zero modes of H_free. The new code applies the full four-bin matrix to the original complex old/R vectors and explicitly encoded constrained pair, at anchor 10 and another clock tick, checking a positive and a negative sign. It also checks the nonconstant u-weighted mode has eigenvalue 2. These are original quantum vectors, not only a classical probability table.

For the complete clock and purified apparatus use the already established actual prefixes K_t:

```text
H^(t) = K_t H_free K_t†,
H^(clock) = Σ_t |t⟩⟨t| ⊗ H^(t).
```

As the clock advances by the actual gate, `H^(t)` is transported to `H^(t+1)`; cyclic closure implies that the clock-controlled operator commutes with the stationary clock shift. The independent reference clock is a spectator. The full coherently recorded/purified/pair-constrained history is a zero mode by the preceding source-frame identity and linearity. The verifier applies the old/R-plus-pair portion explicitly; the apparatus and full clock follow by the previous prefix-conjugation proof, not a newly materialized huge matrix.

In the continuum, multiplication by the piecewise record/pair dressing D(u) likewise defines a unitary conjugate of the radial kinetic operator. Its operator domain is the dressed domain: a step in the original record components is allowed when `D†ψ` is regular. This is a mathematically precise connection across record boundaries, not proof that the corresponding nonlocal transformations are accessible gates or that the fundamental physical Hamiltonian has been found.

## 5. What this does—and does not—select

**What is selected.** In a fixed reference record fiber, the free round-sphere operator uniquely selects the constant angular amplitude, hence `du/2`, without a nonzero angle parameter. The finite construction preserves the actual pair constraint and allows local nonzero opposite contributions. Gauge transformations leave those contributions invariant; the kinetic operator, by contrast, can relate different physical u values and does not need to commute with an individual magnitude. There is no inconsistency in distinguishing a physical change from a reference change.

**What is not selected.** The kernel of `H_free` contains a constant angular amplitude for **every** admissible reference record vector. The old source, pair/gate structure, clock, magnitude law, actual subjects, incidence and physical–experiential identity are not uniquely fixed. Zero total of H₁+H₂ does not imply the free zero-mode condition; the latter is an additional candidate principle. Neither mathematical diffusion nor quantum amplitudes by themselves establish actual outcomes or objective chance.

To see why the free principle is substantive, let `f(u)>0` be a nonconstant smooth gauge-invariant amplitude and define

```text
H_f = −L + (L f)/f.
```

Its quadratic form is `∫(1−u²) f² |(ψ/f)'|² du/2`, so H_f is nonnegative and has `f` as a zero mode under the corresponding regular boundary conditions. For `f=√(1+ε cos 2πu)`, it gives the earlier full-support nonuniform law. Its finite analogue `−Q_N+diag(Q_N f/f)` is also positive with f as its unique zero ground, as the verifier checks for N=8. That particular example retains the same four coarse-bin masses in the midpoint discretization. Choosing f and its induced relational potential is an explicit **input**, not a rival claimed to be an actually possible whole. It shows only that positivity, zero ground and frame gauge do not logically force the free operator.

There is another compatibility condition. The earlier negative-band type reflection swaps the two negative N=4 bins but leaves the positive bins fixed. This permutation fixes the uniform vector, yet it does **not** commute with Q_4: it changes which negative bin is adjacent to the positive region. The scalar reflection is also discontinuous at a band boundary in the continuous coordinate. We checked more than the scalar permutation: on both signs of an actual original source, the old Q/pointer type swap maps each negative-bin record into its actual reflected record; lifting those branches through the constrained-pair isometries gives the same swap on the four-dimensional recorded subspace. On its bin-0 vector the squared norm of the commutator with the dressed free kinetic operator, divided by the original source norm, is exactly 8 in the displayed units. Thus the natural pair lift of the existing type swap is **not** a symmetry of the free kinetic operator, even though both fix the uniform history.

### A constructive compatibility repair, and its cost

Let R denote that four-bin involution. There is a concrete positive, connected alternative:

```text
Q_sym = (Q_4 + R Q_4 R†)/2,
H_sym = D [ (−Q_sym)⊗I ] D†,
S_sym = D [ R⊗I ] D†.
```

`H_sym` commutes with `S_sym` on the full four-bin quotient carrier, preserves the pair constraint, and has the same uniform angular zero mode. The type action S_sym agrees with the earlier physical Q/pointer type swap on the explicitly checked original source-record subspace after its pair lift; it is a chosen full-carrier extension, not a proof that the historical operator has identical action on all other states. Clock-prefix conjugation carries both operators through the same stationary clock. On the actual constrained record vectors the verifier checks both the original nonzero commutator and its vanishing for the symmetrized operator, for both signs.

In the stated units, `−Q_sym` has eigenvalues `0, 6−2√3, 8, 6+2√3`, so the constant zero mode remains unique in the scalar sector. This repair has a definite structural price: a new direct transition connects the first negative bin to the first positive bin. In fact, **any** four-bin nearest-neighbor operator commuting with R has its middle connection zero: symmetry forces `Q[1,2]=Q[0,2]`, but strict nearest-neighbor locality sets `Q[0,2]=0`. The graph then disconnects and has multiple stationary sectors. Thus one cannot simultaneously retain this exact type reflection, the original nearest-neighbor angular graph and a unique connected no-preference zero mode within that class. The averaged operator preserves the symmetry by adding a non-neighbor relation. This is nonlocality in the model's **relative-angle bin graph**, not a demonstrated violation of spacetime locality. Its continuous limit, physical accessibility and relation to a derived Hamiltonian require separate work; neither this finite repair nor the free operator is forced by zero.

## 6. Relation to the larger objective

The construction makes a nontrivial route available: a frame-independent relational geometry has a distinguished zero mode, and that mode can coexist with the **actual** coherent records, stationary clock and locally nonzero cancelling pair. It avoids both an arbitrary preferred angle and the mistake of using a transitive action that does not descend to the physical quotient.

The route remains conditional. The user's aim is not merely a normalized model or an attractive measure, but one self-sufficient physical–experiential whole without unexplained residue. The further task is to determine whether zero's own constitution yields the round geometry, free rather than weighted kinetic form, allowed record/pair coupling, genuine possibilities, real subject incidences and intrinsic/extrinsic identity as one necessity. The present counterexample neither proves that this is impossible nor permits one to dismiss a formal alternative by decree. It specifies which apparently independent inputs must be unified or derived.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_relational_laplacian_test -v
```

Analytic claims above use the stated round-sphere and boundary assumptions; the tests check selected finite spectra, original-state vectors and controls, not empirical gravity, consciousness or a full external foundation battery.
