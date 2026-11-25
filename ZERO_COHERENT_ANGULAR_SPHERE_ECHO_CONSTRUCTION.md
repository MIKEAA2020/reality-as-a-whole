# A coherent angular sphere record in the original quantum echo

## Result

**Stationary-clock continuation:** [the coherent angular reservoir history](ZERO_COHERENT_ANGULAR_RESERVOIR_CLOCK_ACCESS.md) composes these actual echo gates and angular states with the purified 20-step reservoir program, defines stationary clock effects, and exhibits a concrete magnitude-access obstruction when the angular register is withheld.

The preceding [angular point–sphere construction](ZERO_POINT_SPHERE_SIGNED_MAGNITUDE_ECHO_INTEGRATION.md) reproduced the echo's diagonal ledger but did not construct its continuous angular information on the original quantum vectors. The [full-quantum two-band check](ZERO_FULL_QUANTUM_ECHO_TYPE_SYMMETRY.md) connected just the band averages. This pass constructs a **coherent angular-register extension of the same original echo**, recovers the entire T–Q–T echo and its inverse on all 16 original source histories, and puts the two continuous magnitude functions into actual quantum multiplication operators.

The finite angular registers are not claimed to be identical to the complete old quantum state: recording the angular bands entangles a new degree of freedom and changes the old system's reduced coherences. The construction is also not a derivation of the angular sphere, its measure, actual experience, cosmic energy, or a zero-residue constitution. It establishes a common mathematical/physical interface in the specified model rather than a metaphysical conclusion.

The [implementation](verification/zero_quantum_angular_echo.py) and [six-test verifier](verification/zero_quantum_angular_echo_test.py) use the actual old state vectors and echo gates. A separate [relativistic access continuation](ZERO_COVARIANT_ANGULAR_RECORD_AND_COUNTERPART.md) examines the observer dependence of its angular measure.

## 1. Audit → plan → implementation

- The user's point–sphere proposal motivates retaining internal directions while the whole has no external size. The previous [blow-up](ZERO_POINT_INTERNAL_SPHERE_CONSTITUTION.md) is an exact representation of that relation, but its sphere and metric are extra structure, not already shown to follow from bare zero.
- The prior [echo](ZERO_SPHERE_LOCAL_CONSTITUTION_AND_RESERVOIR_ECHO.md) supplies coherent quantum gates and actual computed old-system branch vectors. Its charges are not established cosmic energy. Page–Wootters supplies the stationary-history organization, not the derivation of the extra angular register.
- The prior angular balance proof uses a sphere distribution and a candidate signed magnitude. It does not itself establish a coherent quantum implementation, an actual experiential incidence or a unique quality scale.
- **Plan:** attach an explicitly prepared angular register to the existing *commuting* B and pre-echo j sectors; propagate the old quantum T and Q gates without replacing them by a classical hidden path; lift the earlier physical symmetry to the register; compare the two *operators*, not just their bin averages; and state exactly what refinement changes.

This is a conditional construction motivated by the preserved inputs, not an attribution of this particular quantum register or its laws to their authors.

## 2. Finite construction and the old coherent echo

For `N=4m`, choose the midpoints

```text
u_i = −1 + (2i+1)/N,        i=0,…,N−1.
```

The first N/4 are in the old `b=−,z=−` band, the next N/4 in `b=−,z=+`, and the last N/2 in `b=+,z=+`. Let `|i⟩_A` be orthonormal states of an **added angular record** and let `|χ_bz⟩` be the normalized equal superposition of the bin states in that band's sector.

For each actual old source history x, the previous sign-pointer construction gives

```text
v_s = (x+sQx)/2,    s=±1.
```

Attach the angular register coherently through the commuting sector projectors:

```text
v_s  →  Σ_(b,z) Π_B=b Π_J=z v_s ⊗ |χ_bz⟩_A.
```

This is an isometry on the supported input: the sector projectors are mutually orthogonal, and each `χ_bz` is normalized. A controlled unitary with a prepared register can implement the map on that domain; the preparation and control are physical resources, not consequences of zero. The finite register is a quadrature of the relative angular cosine, not a physical proof of a continuous S².

Starting with the old echo memory R ready, the code applies the actual coherent `T–Q–T` operators to every angular-register slice, then applies the inverse `T–Q–T` and verifies return to the angular-recorded input. It checks **all 16 old source histories and both s values** for N=4. At tick 10, tests for all 16 histories and N=4 and 8 show that:

- every angular bin has physical weight `1/N` conditional on s;
- its B/J/R signs reproduce exactly the prior three-band ledger;
- the lifted physical swap described below fixes the complete complex state, not just its diagonal weights.

The source/reservoir additions of the 20-tick construction are not separately simulated as a dense enlarged quantum state here. Since their previously specified gates are B-controlled and do not act on the added angular register, they can be composed as in the original construction under those stated gate assumptions. The old reduced all-tick ledger is reproduced by the earlier angular verifier; this new test directly executes the **coherent echo and its inverse**, not every reservoir operation.

## 3. One continuous wavefunction, not merely convergent histograms

There is a common Hilbert space for these refinements. Map the finite bin basis to normalized interval indicators in `L²([-1,1],du)`:

```text
|i⟩_A  ↦  √(N/2) · 1_([−1+2i/N, −1+2(i+1)/N))(u).
```

Let `a` and `c` be the old post-echo R-positive and R-negative vectors for fixed x,s, and `c_±=Π_J± c`. After this embedding, **every** N divisible by four represents the same vector-valued wavefunction, apart from measure-zero boundaries:

```text
                    R=+               R=−
  0<u<1             a                  0
 −1/2<u<0           0                 √2 c_−
 −1<u<−1/2          0                 √2 c_+ .
```

For the checked source states, `||a||²=||v_s||²/2` and `||c_+||²=||c_-||²=||v_s||²/4`. Hence, after normalizing by `||v_s||²`, the u density is exactly `du/2`. The program checks the N=4 and N=16 common-L² embeddings on representative source/sign cases; the band formula explains why it holds for all N=4m. Boundaries are not assigned phenomenological significance.

The complete extended old-system/R/A state is pure. But, because the angular bands record J, tracing out A in the R-negative sector removes the old `c_+ c_-†` coherence and changes that sector's normalized purity from 1 to 1/2. The old *commuting* records are unchanged; the full old reduced quantum state is not. This is a physical cost of an added record, not an unexplained disappearance of information from the enlarged state. No dissipation cost is inferred from reversible recording.

The coordinate u captures a relative angular cosine; the remaining angular directions, a physical Lorentz cone and actual spacetime are not derived or densely implemented by this L² construction.

## 4. A complete physical swap and an exact magnitude test

The old tick-10 operation uses `Q Z_M` when R is negative. Extend it by also applying the angular reflection

```text
h(u)=−1−u  for −1<u<0;       h(u)=u for 0<u<1.
```

On finite bins the negative half is reversed, and the positive half is fixed. It is an involutive, measure-preserving permutation. The original quantum identity `sQ c_+=c_-` and its inverse ensure that the **combined** old-system, pointer, R and angular operation fixes the full correlated state for all 16 source histories and both pointer signs. In the common L² representation the same identities establish invariance almost everywhere. As in the prior work, this is an operation on the larger interface, not something a j-only subject can automatically perform or access.

Define physical candidate operators on the same domain

```text
V_now  = κ Z_M J g(u),
V_echo = κ Z_M J R g(u),
```

with `g₁=|u|` and `g₂=|u(u+1)|`. On the actual `B R=+1` support the combined unitary D obeys

```text
D† V_now(g) D = V_echo(g∘h).
```

Thus equality with `V_echo(g)` requires `g∘h=g` on the relevant support. For g₂ it holds exactly; for g₁ it does not. This is checked by **applying the full operator sequence to the original quantum vectors**, not only comparing scalar bin averages.

For normalized state and κ=1, the squared norm of the operator mismatch is

```text
||[D† V_now(g₁) D − V_echo(g₁)] Ψ_N||²
       = 1/6 − 2/(3N²)  →  1/6,
||[D† V_now(g₂) D − V_echo(g₂)] Ψ_N||² = 0.
```

The finite identity follows by summing the uniformly weighted negative midpoints. The limit is the exact integral `(1/2)∫_(−1)^0 (1+2u)² du=1/6`. For κ≠1 the squared norms acquire κ². This proves the sign-only symmetry failure for g₁ is not a two-bin or cutoff artifact in this construction. On the common L² space, midpoint multiplication operators converge in operator norm to these continuous functions: the errors are at most `1/N` for g₁ and `3/N` for g₂, using their Lipschitz bounds. No assertion of convergence of unrelated Hilbert spaces is needed.

The same sign-counterpart operation as before still yields a zero **signed physical/model integral** for both g functions if the s weights are matched. Neither that integral nor D invariance establishes an actual subject or an experiential measure. If the candidate negative sign is later justified as suffering, it remains a real local occurrence rather than being erased by the positive contribution.

## 5. Consequences for the common candidate

This step converts the source-inspired angular extension from a separate coarse-grained analogy into a **coherent continuum-register realization of the old echo**. It also makes the earlier conditional incidence argument more exact: the equal-type selection may use g₂'s combined physical symmetry *if* the relevant actual incidence measure is invariant under it, whereas g₁ cannot use that very full-quality symmetry. Many other invariant g functions exist; g₂ is not derived uniquely from zero. A model state can be invariant under an active operation even when the operation changes a locally distinguishable record; it is not automatically a gauge identification or an experiential symmetry.

The stronger user's aim remains that one self-subsistent zero constitution determine actual physical and experiential reality, including subject boundaries and magnitudes, with no independently selected law or measure. This construction has **not** derived its added Hilbert space, preparation, dimensionality, gates, angular measure, physical–experiential identity or whole-level energy. Those are not accepted as permanently tolerable residues. Nor do these tests establish a formal battery pass or rule out the user's strong possibility–actuality proposal.

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_quantum_angular_echo_test \
 verification.zero_full_echo_type_swap_test \
 verification.zero_sphere_angular_echo_test -v
```

The six new tests cover the original 16 quantum histories, the actual echo and inverse, a common L² refinement, exact finite and continuum magnitude discrepancy, and the effect of tracing the record. They verify the specified model, not actual lived quality or empirical spacetime.
