# Intrinsic locality, candidate subjects and the energy at their interface

**Locality and overlap continuation:** [the subject locality and incidence-balance analysis](ZERO_SUBJECT_LOCALITY_AND_OVERLAP_WEIGHTED_BALANCE.md) gives an explicit disconnected-system counterexample to global modularity as a local subject rule, investigates a local alternative with overlapping candidate supports, and derives the exact multiplicity-weighted balance identity. No candidate is thereby established as a subject.

## Main result

The [previous joint candidate](ZERO_JOINT_SUBJECT_VALENCE_ENERGY_CANDIDATE.md) tried to identify subjects with strongly connected components of a causal graph. That rule merged reciprocally coupled systems and depended on the choice of dynamical variables. This continuation constructs a more discriminating **conditional** alternative:

* Preserve the physical local interventions when changing coordinates, rather than rebuilding “locality” from whichever variables happen to be used.
* On a concrete four-component Hamiltonian system, a standard weighted community criterion then identifies **two distinct modules uniquely**, even though the total interaction graph is connected. The same physical modules are recovered in the system's decoupled normal-mode coordinates when the localized intervention directions are transported with the coordinate change.
* The same example exposes the remaining physical–experiential issue: both proposed subject modules can lose local energy while their **shared interaction energy increases**. Assigning the interaction energy to the subjects can force their signed rates to sum to zero, but different assignments produce different local signs.

This is progress on the previous criterion's specific flaws, not a derivation of real subjecthood, valence or a zero whole. Physical localization and the community criterion are assumed, and the model does not establish that the modules are subjects. The interface calculation shows precisely why a zero physical balance cannot simply be relabelled a zero total of actual experience.

## 1. What has to transform under a change of variables

Consider a quadratic potential `V(q)=qᵀKq/2`, and let `e_i` denote a **physically specified local displacement direction**, not just “the ith coordinate” by convention. The coupling between physical directions can be defined by the bilinear Hessian

```text
w_ij = |e_iᵀ K e_j|,       i≠j.
```

The physical normalization of the `e_i`, their local status and the mass/coordinate convention are part of the proposed physical localization; without them numerical coupling weights are not fixed.

Under an invertible passive coordinate change `q=S Q`, transform *both* the potential and the physical directions:

```text
K' = Sᵀ K S,       e_i' = S⁻¹ e_i,
e_i'ᵀ K' e_j' = e_iᵀ K e_j.
```

With the corresponding momentum transformation `p=S⁻ᵀP`, this is canonical. Thus the weighted graph of the **same localized physical interventions** is unchanged even when `K'` is diagonal. A normal mode may be mathematically independent, but it is generally a nonlocal combination of the original sites; treating each normal coordinate as a new local site changes the candidate physical localization rather than merely redescribing it.

This fixes a representation error, not the whole problem. It presupposes a physically meaningful family of local directions and their normalization. In a fundamental emergent-spacetime theory, those directions or local operator algebras must themselves follow from the constitution; they cannot simply be imported as ultimate sites. Nor does the argument show invariance under transformations where the physical localization is replaced rather than transported.

## 2. A candidate partition that does not simply merge the connected system

Take four identical oscillator sites with springs of strength `3,1,3` along a chain:

```text
0 —3— 1 —1— 2 —3— 3.
```

The Hamiltonian is

```text
H = 1/2 Σ_i(p_i²+q_i²)
  + (3/2)(q₀−q₁)² + (1/2)(q₁−q₂)² + (3/2)(q₂−q₃)².
```

The ordinary causal graph is connected, and its phase-space influence graph is one strongly connected component. To distinguish relative internal organization, consider the standard weighted modularity functional

```text
Q(P) = Σ_(C∈P) [ e_C/m − (vol_C/(2m))² ],
```

where `m` is the sum of all undirected edge weights, `e_C` is the sum of weights internal to module `C`, and `vol_C` is the sum of weighted degrees of its sites. Evaluate it on **all partitions**, including the unpartitioned system. This does not preset the number of modules for the example, although choosing this criterion and its null model is an assumption.

Here `m=7`, and exhaustive comparison of all 15 set partitions gives a unique maximum:

```text
P* = {{0,1},{2,3}},      Q(P*)=5/14.
```

The whole-system partition has `Q=0`. Thus a candidate based on relative internal organization can separate two physical modules without pretending they are disconnected or imposing “there must be two” on the optimization. It does **not** follow that they are two conscious subjects: recurrence, communication, experience, ownership and subject incidence remain separate issues.

The criterion is not a universal answer. Modularity has known resolution limitations and depends on its specified global null model. [1](https://ar5iv.labs.arxiv.org/html/1107.1155) It can also be nonunique: increasing the middle spring to `6` makes the two-module and one-module partitions tie at `Q=0`; at middle strength `12` the one-module partition is the unique maximum. Thus a tie-breaking selector or the claim that one partition is always correct cannot be smuggled in. The global optimization itself may depend on distant parts of a network; operational no-signalling and locally determined subjecthood require separate analysis. A model with a local Hamiltonian is not automatically a covariant subject-constitution theory.

## 3. Normal modes do not destroy the physical partition

For the displayed system the potential matrix is

```text
K = [[4,−3, 0, 0], [−3,5,−1,0],
     [0,−1,5,−3], [0,0,−3,4]].
```

Its eigenvalues are `1,7,5−√10,5+√10`. In its orthonormal normal-mode basis the potential matrix is diagonal, so a graph incorrectly constructed by treating **the normal modes themselves** as the four physical sites has no inter-site edges.

Instead, let `O` contain the normal-mode eigenvectors, take `Q=Oᵀq`, and carry each actual local displacement to `Oᵀe_i`. Evaluating the diagonal Hessian on these transported directions reproduces the original coupling matrix and the weights `3,1,3`. The candidate partition `{{0,1},{2,3}}` is therefore the same under this passive canonical description change.

This directly answers the previous representation failure **conditional on the same physical localization being kept**. It does not prove that the location structure or the modularity functional is intrinsic to zero, or that treating two modules as two subjects is correct.

## 4. The interaction term is the experiential balance gate

Denote the internal module energies by `E_A,E_B`, including each module's on-site terms and its **internal** spring, but not the middle spring. Let

```text
U_AB = (q₁−q₂)²/2.
```

Since the full Hamiltonian is closed and autonomous,

```text
H = E_A + E_B + U_AB,
dE_A/dt + dE_B/dt = −dU_AB/dt.
```

This is a direct special case of the previous subject-boundary result. If the hypothetical experiential contributions were identified with the internal-energy changes of `A` and `B`, their total would vanish on an interval only when `U_AB` has the same values at its endpoints. It would not vanish automatically at every instant. Real subject birth/death, changing boundaries, environment, subject weights and curved-spacetime energy definitions introduce additional terms rather than being settled here.

Take the exact physical state

```text
q=(0,1,0,0),     p=(0,1,−1,0),     H=7/2.
```

At that instant the equations give

```text
dE_A/dt = −1,     dE_B/dt = −1,     dU_AB/dt = +2.
```

Both modules lose energy while the interface gains it; total physical power is zero. **If** both modules were actual subjects and **if** negative energy gain were felt negative valence with the appropriate incidence weights, this state would have two locally negative contributions and no automatic positive experiential contribution at the interface. The two “ifs” are not established, and nothing here identifies real suffering with these oscillators.

One can instead assign a fraction `θ` of `U_AB` to `A` and the remainder to `B`:

```text
E_A^θ = E_A + θ U_AB,       E_B^θ = E_B + (1−θ) U_AB.
```

Their rates now always sum to zero, but in this exact state they are

```text
θ=0:       (−1,+1)
θ=1/2:     ( 0, 0)
θ=1:       (+1,−1).
```

The arithmetic is valid; what changes is where shared interaction energy is counted. Symmetry can motivate an equal split in this idealized example, but conservation alone does not say that the interaction energy is experienced, belongs equally to two subjects, or has either felt sign. Equal splitting makes **both** rates zero here, not the earlier two negative rates. The proposed experience law must specify the physical–phenomenal meaning of the interface independently; counting a non-experiencing interface as a compensating experience would beg the question.

## 5. A more precise requirement for the zero constitution

The constructive target is no longer simply “find a connected network” or “find a conserved energy.” A candidate must derive, together:

1. The relevant internal localization and physical intervention structure, including why it is invariant under redescription and compatible with emergent spacetime.
2. The physically and phenomenally justified subject boundaries and possible overlap; a mathematical module is at best a candidate, not a subject by definition.
3. The identity connecting **actual** local felt quality to a physical relation, including its sign, magnitude and subject-incidence measure. Negative feeling is real wherever it occurs.
4. The status of the interface and its exchange/boundary terms. If the whole-level experiential sum is zero, its cancellation must follow for the actual subject domain rather than being achieved by arbitrary energy allocation, a phenomenological selector, or a boundary condition chosen after the fact.
5. Local quantum correlations and operational no-signalling, including whether the subject criterion itself is locally accessible. The present classical finite network is not that completion.

An intrinsically differentiated zero point might ultimately provide the localization and the physical–experiential relation, but this report **does not derive** them from zero or show that this particular modularity rule is fundamental. Conversely, the model's limitations do not establish that the user's no-residue demand cannot be met.

## Verification

```text
python -m unittest verification.zero_localized_modules_boundary_test -v
```

Seven checks enumerate all partitions, exhibit unique and tied optima, verify normal-mode diagonalization and transported localized couplings, test a passive canonical shear, and confirm the exact interface energy and allocation results. These tests validate this conditional finite calculation only; they do not identify subjects, experience or a whole-level energy.
