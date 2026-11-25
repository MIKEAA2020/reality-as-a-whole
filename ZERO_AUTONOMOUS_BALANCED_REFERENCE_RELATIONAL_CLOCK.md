# Autonomous balanced-reference preparation with a relational clock

## Result and status

The [topological preparation program](ZERO_BALANCED_REFERENCE_PREPARATION_TOPOLOGICAL_PROGRAM.md) constructed three charge-preserving gates `E`, `D`, `T` but supplied their ordering and timing. This round embeds **the same gates and seed** into one finite, time-independent program Hamiltonian. A separate finite internal reference clock produces an exactly stationary zero-constraint state whose conditional readings recover the autonomous history.

- The program Hamiltonian preserves the original declared lab/work charges and the new orientation charge. It acts on the actual full physical work register, and retains both coherent lab sectors and all 16 earlier relative-clock outcomes.
- At an ideal relational clock reading `τ=π`, the program reaches its fourth state with certainty and the work–record–target–reference subsystem is exactly the previously derived balanced final state, up to a global phase.
- With a finite-resolution clock window `π±π/4`, the program is at its final site with probability **0.863268 conditional on that window**. If that site is actually read and found, the conditional operation on the previous subsystem is exactly `TDE`. The joint probability of the clock window and final-site event is **0.215817**.
- Crucially, the **unselected complete history is not the final state**. After ignoring both clock and program readouts, the four program stages have weights `(5,3,3,5)/16`; its state has fidelity `27/64` and trace distance approximately `0.61627` from the final target. The complementary zero/eigencondition holds on the final branch, not on the whole unselected history.

This is an explicit autonomous, charge-preserving **finite construction**, not a derivation of the particular interactions or of actuality from the self-sufficient zero. The program clock, separate phase-reference clock, their joint stationary state, the balanced seed, the couplings and the phase POVM are specified. The vanishing constraint is not established as objective cosmological energy zero. No system is thereby an experiencing subject.

Verifier: [verification/zero_autonomous_balanced_reference_clock_test.py](verification/zero_autonomous_balanced_reference_clock_test.py).

## 1. From three gated operations to one Hamiltonian

Let `U₁=E`, `U₂=D`, `U₃=T` be the exact unitaries from the prior construction. Introduce a four-level program register with orthogonal position states `|n⟩`, `n=0,1,2,3`. It is an explicit internal resource, not the earlier relative-clock label or an external laboratory time. Define

```text
H_prog = Σ_(n=0..2) J_n [ |n+1⟩⟨n| ⊗ U_(n+1)
                        + |n⟩⟨n+1| ⊗ U_(n+1)† ],
(J₀,J₁,J₂) = (√3/2, 1, √3/2).
```

This is a single time-independent Hermitian operator. It contains the entire ordered sequence in its static couplings: no classical agent switches E, D or T at successive times. The terms nevertheless contain **specified** potentially multibody operators, and the program register, coupling strengths, energy scale and initial state have not been derived from zero.

For `G₀=I`, `G₁=E`, `G₂=DE`, `G₃=TDE`, the block unitary

```text
V = Σ_n |n⟩⟨n|⊗G_n
```

transforms the Hamiltonian into `V(J_x⊗I)V†`, where `J_x` is the spin-3/2 nearest-neighbor matrix with the three coefficients above. Its spectrum is `−3/2,−1/2,+1/2,+3/2`, each repeated across the internal circuit. Starting with program `|0⟩` and any internal seed,

```text
exp(−iτ H_prog)(|0⟩⊗|seed⟩)
 = Σ_n c_n(τ)|n⟩⊗G_n|seed⟩,
|c_n(τ)|² = binomial(3,n) cos(τ/2)^[2(3−n)] sin(τ/2)^(2n).
```

At `τ=π`, `c₃=i` and the other coefficients vanish. The resulting state is `i|3⟩⊗TDE|seed⟩`.

The coefficient **ratio** can be derived within a specified design class: a positive reflection-symmetric four-site nearest-neighbor path with couplings `(a,b,a)` has equally spaced spectrum `±s/2,±3s/2` exactly when `b/a=2/√3`, with `s=b`. The selected J values are this solution in units `s=1`. The line topology, reflection symmetry, equal spacing and scale are additional assumptions; perfect transfer can also occur in other designs. Zero by itself has not been shown to require this path or ratio.

## 2. Charge preservation on the physical work register

Each `U_i` has a full extension to the physical 16-state work register. The verifier builds the resulting `4×2×16×2×2=512`-dimensional program–R–work–target–F generator and directly checks

```text
[H_prog, J_W+Z_F] = 0,
[H_prog, N_total work] = 0,
[H_prog, N_pair] = 0
```

for each previously specified work-pair number. H_prog acts trivially on the pre-existing lab factors, so it commutes with their declared directional generators; program and F are neutral under the **old** declared energy assignment. The balanced seed obeys those old constraints, and every `G_n|seed⟩` does too. Therefore their coherent superposition retains them exactly. The commutator is an operator result for the specified finite extensions, not merely a zero expectation on a single branch.

The phase-reference clock below adds its own charge term to a **new constraint**. Its negative sign is part of the construction and is not a derived negative gravitational energy. None of these finite statements settles whether the actual universe has a unique objective conserved global energy.

## 3. A stationary whole and relational time readings

Introduce a separate four-dimensional reference clock with orthonormal energy labels `|k⟩_R` and the same four eigenvalues `e_k∈{−3/2,−1/2,1/2,3/2}`. Let `P_k` be the corresponding spectral projections of H_prog. Define the isometry

```text
W|ξ⟩ = Σ_k |k⟩_R ⊗ P_k|ξ⟩,
C = I_R⊗H_prog − H_R⊗I,
H_R|k⟩_R=e_k|k⟩_R.
```

Then `W†W=I` and `CW=0` as exact operator identities. Applied to the initial program–subsystem state, this gives a normalized stationary constraint state. Because W is an isometry on **arbitrary input**, it also preserves any entanglement with the coherent code/complement flags, earlier clocks and other environment factors.

For the normalized reference phase states

```text
|τ⟩ = (1/2) Σ_k exp(i e_k τ)|k⟩_R,
E(dτ) = 4|τ⟩⟨τ| dτ/(2π),     0≤τ<2π,
```

the effects resolve the identity. Contracting the whole with `⟨τ|` yields exactly half of `exp(−iτ H_prog)|ξ⟩`; after normalizing, the conditional state is the autonomous history in §1. The clock's phase density is uniform `1/(2π)` for the specified state. This uses a **nonorthogonal finite phase POVM**: an exact real-valued reading has probability density, not a finite-probability sharp outcome. The operator construction does not supply a physical detector that reads the POVM or prove that an inhabitant confined to a different subsystem can access it.

The parameter τ is a relational reference-clock label, not an assumed fundamental spacetime foliation. The finite clock is periodic, so the program later evolves away from site 3; there is no claim of irreversible progress, permanent memory, or an inexhaustible clock.

## 4. Finite-resolution reading and retained histories

For an actual finite clock window `τ∈[π−δ,π+δ]`, its probability is `δ/π`. If the program site is then read, the conditional probability of site 3 is

```text
p₃(δ) = [10 + 15 sin(δ)/δ + 3 sin(2δ)/δ + sin(3δ)/(3δ)]/32.
```

For `δ=π/4`, `p₃≈0.8632677755`; the joint probability is `p₃/4≈0.2158169439`. In the site-3 branch, its operator amplitude is `c₃(τ)TDE` for **every** τ, so the normalized subsystem output is exactly the old balanced target, even after integrating over the window. This is a **heralded** statement: it requires the specified clock and program readouts, and neither observation nor a definite actual outcome is inferred from the quantum state.

No program sector is discarded in the construction. If both clock and program are unobserved, tracing them gives the fully specified reduced history channel

```text
ρ ↦ (5 G₀ρG₀† + 3 G₁ρG₁† + 3 G₂ρG₂† + 5 G₃ρG₃†)/16.
```

The coherent physical code/complement state remains included; the direct-sum calculation is performed on the whole pure superposition, not by first flag-dephasing it. For the actual specified seed, comparison with the final pure target gives

```text
fidelity = 27/64 ≈ 0.421875,
trace distance ≈ 0.616267.
```

The unselected state has `⟨S⟩=5/16` and `⟨C₁²⟩=11/8`, where the earlier final-state eigencondition was `S=+1` or equivalently `C₁=0`. Thus the full unselected history cannot honestly be called the final common-zero eigenstate. The old orientation charge and old lab/energy constraints remain exact throughout; the *additional* final complementary balance is not conserved by the preparation sequence.

This matters for the user's core demand. If that complementary balance is to be a **fundamental whole-level constraint at every internal reading**, this history model does not yet satisfy it; the right next task is not to call its final branch the whole, but to find a history construction compatible with the constraint at every reading or to derive a different relational expression of it. If instead it is an emergent final-record relation, the present mechanism realizes it conditionally but has not derived why it is fundamental.

## 5. What has and has not been derived from zero

The finite dependency chain is now concrete:

```text
specified balanced product seed
  → charge-preserving program Hamiltonian
  → exact stationary constraint state with an internal clock
  → conditional balanced state and eigencondition at a reading.
```

The derivation removes externally scheduled gate switching, but **not** the choice of seed, three gate operators, program graph, reference clock, POVM or spectrum. It also does not derive the earlier complementary algebra from the ontology of zero. A matching physical observer, localized control, reference-clock preparation and cost accounting remain open; the exact reference–program correlations were built into W. The program and clock are cyclic, not a proof of an irreversible history or single actual outcome.

A subject/experience bridge is likewise absent. No qubit, program site, clock outcome or target record is identified as a subject or a felt value. Even if a future zero-level experiential accounting pairs opposite signed contributions, a local negative felt experience remains suffering; it is not erased by its counterpart.

The next most feasible step in topological order is to test whether an autonomous **constraint-preserving history** can keep the proposed complementary-zero condition exact at all program readings, while still generating nontrivial, locally accessible record correlations. Its result must distinguish a genuinely conserved whole-level zero from a transported or branch-dependent redefinition. Only after that should one try to derive the interaction algebra, seed, actual subject incidence and objective whole quantity from zero's constitution.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_autonomous_balanced_reference_clock_test -v
```

Nine tests check the static program Hamiltonian and conditional coupling ratio, full physical work-charge commutators, exact stationary constraint/isometry and normalized finite phase POVM, the coherent all-sector target and every earlier clock label, finite-window success, and the unselected-history controls. They do not establish fundamental dynamics, operational locality, actual outcomes, experience, or a universal/global energy law.
