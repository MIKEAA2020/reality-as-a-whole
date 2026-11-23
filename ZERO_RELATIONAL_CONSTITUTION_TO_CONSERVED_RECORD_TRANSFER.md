# From relational zero to a unique correlated state and conserved record transfer

## The non-decorative connection

This is a single conditional construction joining the prior [finite tetrahedral sphere](FINITE_SPHERE_ZERO_REFERENCE_AND_SYMMETRIC_RECORDS.md), the [conserved record exchange](ZERO_SECTOR_CONSERVED_ENERGY_RECORD_DYNAMICS.md), and the [additive-channel no-go](ABAEE_ADDITIVE_DYNAMICS_AND_EXACT_DIAMOND_RADIUS.md). It does more than give the parts similar names:

1. Three explicit relations—opposite records, record–direction agreement, and a relational coherence condition—**jointly select exactly one state** in the stipulated continuously invariant finite sector. Zero plus symmetry and record probabilities alone did not do so.
2. That unique state fixes the eight reference–record weights, the opposite local spin correlations and the previously observed joint-state purity. Those facts are consequences of the same equations, not extra independently assigned numbers.
3. A specified energy-conserving controlled swap takes those very same pointer records into opposite memory–battery transfers. In each branch, the local directional record determines **which** memory receives energy; every gain is physically paired with a loss. This is a concrete operator-level link between reference, correlation, record and transfer.
4. The relation constraints are the ground conditions of an explicitly given, continuously symmetric, gapped, positive operator. A small value of that operator bounds the distance from the selected state. A universal scalar additive on bare channels, of the sort ruled trivial by Abaee's theorem, cannot do this job.

This makes the *architecture* of the proposed connection substantially tighter. It does **not** establish that these relations themselves follow from zero's own constitution, nor that a physical record or transfer is a subject, a feeling, or signed experiential value. The representation, factorization, relations and couplings are specified. They must ultimately be accounted for rather than treated as unexplained acceptable residue. The user's stronger thesis is the target of the construction, not a result assumed false or already derived.

## 1. The same finite reference and whole

Use the four-dimensional reference subspace `C=1⊕3` from the prior 22-physical-spin model, with scalar `|s⟩` and orthonormal logical vector `|v_a⟩`, and two spin-zero encoded logical qubits `A,B`. Let

```text
|ψ⁻⟩ = (|01⟩−|10⟩)/√2,
|S⟩ = |s⟩ |ψ⁻⟩,
|T⟩ = (1/√3) Σ_(a=x,y,z) |v_a⟩ σ_a^A |ψ⁻⟩.
```

Both are normalized, orthogonal, invariant under the specified common logical `SO(3)`, and their span exhausts the invariant subspace of `C⊗A⊗B`: `(1⊕3)⊗(1⊕3)` contains two scalars. This is a **logical** symmetry inside physical spin-singlet blocks, not a derived spatial rotation or a relativistic theory. The six-spin reference sector's unused fifth singlet is excluded here, as in the specified four-label reference; including it adds another scalar and requires further constraints. Two additional logical qubits `R_A,R_B` are records and are scalars under this logical rotation. In what follows write `|01⟩`, `|10⟩` for those records.

Define on `C⊗A⊗B`

```text
P = |S⟩⟨S| + |T⟩⟨T|,       G = |S⟩⟨T| + |T⟩⟨S|,
D = |S⟩⟨S| − |T⟩⟨T|.
```

Here `D` is not an arbitrary state label: on the invariant sector it equals `2P_singlet(AB)−I`. `G` has a similarly concrete origin. For the four tetrahedral basis states `|i⟩` and unit directions `n_i`, form

```text
T_dir = Σ_i |i⟩⟨i|_C ⊗ (n_i·σ_A) ⊗ I_B.
T_dir |S⟩ = |T⟩,       T_dir |T⟩ = |S⟩,       P T_dir P = G.
```

The first identity uses the tetrahedral first and second moments; the second follows because `T_dir²=I`. Thus an actual direction-controlled spin observable, when compressed to the whole's invariant sector, becomes the scalar–vector exchange `G`. `T_dir` itself has tetrahedral rather than full continuous symmetry; `G` is continuously invariant because it exchanges two invariant vectors. This is a precise bridge between discrete directional readout and continuous symmetry of the whole, not a claim that four labels are all directions.

## 2. Three relations select the state

Restrict first to `P⊗I_R` and define

```text
K = G Z_R_A,                    Q = D X_R_A X_R_B,
E_same = (I + Z_R_A Z_R_B)/2.
```

Products across factors are tensor products. `E_same=0` says the two records are opposite; `K=+1` links the directional spin readout to the sign of the A record; and `Q=+1` fixes the coherence between opposite record branches relative to the AB singlet/triplet character. The third is a measurable joint relational condition, not merely a label for a phase: flipping it changes the expectation of the explicitly specified observable `Q`. It is **not**, by itself, a phenomenal coherence principle.

On the invariant sector `G²=D²=I` and `{G,D}=0`. As `Z_R_A` anticommutes with `X_R_A X_R_B`, the two sign changes give

```text
[K,Q] = 0,       [K,E_same] = [Q,E_same] = 0.
```

Hence the relations are jointly sharp. On the record-opposite sector, `K=+1` alone leaves two dimensions:

```text
(|S⟩+|T⟩)|01⟩/√2,      (|S⟩−|T⟩)|10⟩/√2.
```

`Q` exchanges these two vectors. Requiring `Q=+1` fixes the normalized state, up to overall phase, to

```text
|Ω⟩ = 1/2 [(|S⟩+|T⟩)|01⟩ + (|S⟩−|T⟩)|10⟩].
```

This is exactly the prior recorded tetrahedral whole, not a newly invented state that merely resembles it. Equal branch amplitudes, the relative coherence and the scalar/vector mixture are now derived from the three stated relations. The formal alternative `|Ω₀⟩=|S⟩(|01⟩−|10⟩)/√2` has the same record-zero condition and prior record statistics, but `⟨K⟩=0`, `Q=−1`, so it fails the new conditions. A second control preserves `K=+1` and record zero but reverses the relative branch phase; it has `Q=−1`. Thus both the matching and coherence relations do necessary work. These alternative states are mathematical controls, not assertions about genuinely possible complete worlds.

## 3. One zero-penalty Hamiltonian and a robustness theorem

Let `P̃=P⊗I_R` and extend `K,Q` by zero outside its range. Set the energy scale to one and define

```text
H_rel = (I−P̃) + P⊗E_same + (P̃−K)/2 + (P̃−Q)/2.
```

Each summand is a commuting projector: the first penalizes leaving the invariant sector, the others penalize failure of a stated relation. `H_rel` is continuously logically rotation-invariant and has a **unique zero-energy ground state** `|Ω⟩`, with exact spectral gap 1 in the stipulated encoded Hilbert space. Its uniqueness follows from the commuting relations above, not from assuming an outer product of the target state as the Hamiltonian. The operators are nevertheless nonlocal, many-body and constructed using the chosen representation, `P`, and relational conditions. Zero ground penalty is a zero of this chosen positive operator; it is not an objective proof that the energy of the universe vanishes.

The gap gives an actual error theorem. For any density operator `ρ` in this encoded space, write `F=⟨Ω|ρ|Ω⟩`. Since

```text
H_rel ≥ I−|Ω⟩⟨Ω|,       F ≥ 1−Tr(ρ H_rel),
```

a total relation-violation expectation at most `ε` implies fidelity at least `1−ε`. If `ρ` is supported in `P̃` and the records are exactly opposite, then the sharper operational form is

```text
F ≥ 1 − [(1−⟨K⟩) + (1−⟨Q⟩)]/2.
```

These statements concern a fixed finite model and dimensionless penalties; they are not estimates for a real apparatus. The operator is a **state-sensitive joint Hamiltonian**, not the universally defined composition-additive scalar channel action in the no-go theorem. Its terms are correlations among components; it need not assign a nontrivial additive scalar to each CPTP endochannel. The connection to Abaee is therefore an explicit mathematical division of labor, not an evasion by renaming an action.

A ground-state selector is not a preparation protocol: closed unitary evolution generated by this stationary Hamiltonian cannot, without further resources or special initial conditions, take every initial state into its unique ground state. The prior tailored preparation remains a separate stipulated operation. Neither ground-state selection nor the chosen gap derives an actual history, a law of nature or self-subsistence.

## 4. What the selected relations force

For each tetrahedral label `i` and each of the two opposite record values, the squared amplitude is `1/8`. Conditional on `(i,R_A,R_B)=(i,0,1)`, the A directional spin along `n_i` is `+1` and B is `−1`; conditional on `(i,1,0)` the signs reverse. Thus the same reference direction, opposite spin readout, and opposite records agree branch by branch. These are Born-rule conditional statements, not assertions that the unitary state itself chooses one experienced branch.

Tracing out the reference and records gives

```text
ρ_AB = (1/2) P_singlet + (1/6)(I_AB−P_singlet),
Tr(ρ_AB²)=1/3,       ρ_A=ρ_B=I/2.
```

So the correlation distinguishing this whole from `|Ω₀⟩` is now fixed by the relational conditions. The local marginals are still identical: neither a marginal alone nor a zero record expectation specifies a nonzero definite local feeling. The equality of local marginals also does not prevent conditional correlations; no accessible local feeling is assumed to reveal a remotely chosen decomposition.

## 5. The very same records drive conserved exchanges

Add two memory–battery pairs `M₁,W₁` and `M₂,W₂`, each qubit encoded in its own four-spin physical singlet block, initially

```text
|0,1,0,1⟩_(M₁,W₁,M₂,W₂).
```

The full construction now uses **38 physical spins** within the specified encoded factors. With `N=|1⟩⟨1|`, define

```text
H₀ = N_M₁+N_W₁+N_M₂+N_W₂,
W = |0⟩⟨0|_R_A SWAP_(M₁,W₁) + |1⟩⟨1|_R_A SWAP_(M₂,W₂).
```

The conditional gates commute with `H₀` and with each pair total. They also preserve all encoded physical-spin-zero blocks. Since records are logical rotation scalars, `W` commutes with the continuous logical rotations. The output `|Ξ⟩=W(|Ω⟩⊗|0101⟩)` has the following *same* eight reference/record branches:

| `R_A,R_B` | conditional A spin along `n_i` | `(M₁,W₁,M₂,W₂)` | memory gains | battery changes |
|---|---:|---|---|---|
| `0,1` | `+1` | `1,0,0,1` | `(+1,0)` | `(−1,0)` |
| `1,0` | `−1` | `0,1,1,0` | `(0,+1)` | `(0,−1)` |

In either row the probability for each `i` is `1/8` under the Born rule. Each memory gain is an actual model energy change relative to the specified initial energy eigenstate, and the corresponding battery loss is equal and opposite. More tightly, on `|Ξ⟩` the exact state equations are

```text
(N_M₁−N_M₂)|Ξ⟩ = Z_R_A|Ξ⟩,
(T_dir ⊗ I_records ⊗ (N_M₁−N_M₂))|Ξ⟩ = |Ξ⟩,
ΔN_Mj + ΔN_Wj = 0                       (operator identity).
```

The second equation says that *which memory is energized* is correlated with the A spin along the direction selected by the reference; it is not merely a coincidence of averages. Writing also transports the coherence relation: `(W Q W†)|Ξ⟩=|Ξ⟩`, while the original bare `Q` has expectation zero in `|Ξ⟩` because the energy records now distinguish its branches. Coherence has moved into a joint pointer–memory–battery relation, not disappeared from the pure whole. The Δ operators are `W†N W−N`, and their sum vanishes for every state. `H₀=2` in the prepared state and remains 2; it is a conserved bare energy, not a derived zero-energy universe.

The controlled swap can be generated by a time-independent interaction, not only stipulated as a gate. For any chosen `τ>0`, set

```text
H_write = π/(2τ) [ |0⟩⟨0|_R_A (I−SWAP₁)
                    + |1⟩⟨1|_R_A (I−SWAP₂) ].
```

Then `exp(−iτH_write)=W` and `[H_write,H₀]=0`. Using `H₀+H_write` gives the same final vector up to a common phase on the initial `H₀=2` sector. This is an explicitly specified finite-time interaction; it does not autonomously switch itself off or establish robust irreversible memory. It is not asserted to be spatially local.

For an even tighter static integration, define

```text
H_aux = N_M₁ + (I−N_W₁) + N_M₂ + (I−N_W₂),
H_joint = W (H_rel⊗I_aux + I⊗H_aux) W†.
```

`H_aux` has the unique zero vector `|0101⟩` and gap 1. By unitary conjugation `H_joint` is positive, has **unique zero ground state `|Ξ⟩` and gap 1**, and commutes with `H₀`. It is continuously logically invariant. Consequently the same fidelity bound applies to `|Ξ⟩`. The physical constraint, record correlation, and energy-exchange pattern are thus enforced together in one operator, rather than copied as separate analogies. This construction is tailored and potentially highly nonlocal; the equality between its zero ground penalty and cosmological or experiential zero is not established. `H_joint` is not a relaxation mechanism or a derivation of its own interaction terms.

## 6. Where the experiential connection is still substantive

The table describes physical signs: **gain versus loss**, and which of two memory registers is activated. It is not evidence that either register or battery is an experiencing subject, that its sign is pleasurable or painful, or that the two real feelings cancel. The same physical equations allow a proposed phenomenological sign assignment and its reversal; they also do not decide whether the relevant subject is a memory, a memory–battery pair, a larger organization, or none. In particular, assigning valence from net pair energy would give each pair zero despite its internal transfer, as the [autonomous cycle analysis](ZERO_AUTONOMOUS_RECORD_CYCLE_SUBJECT_INCIDENCE.md) showed. That is a testable failure of one specific proposed bridge, not a proof that no bridge is possible.

As a concrete bridge candidate, suppose (not infer) that each memory is an actual subject on a definite record and that its signed felt value is `v_j=2N_Mj−1`. The written branches would then give `(v₁,v₂)=(+1,−1)` or `(−1,+1)`, exactly zero per branch, while the unconditional expectation of each value is zero. This is mathematically coherent as a conditional assignment, but it fails as an established constitution: it stipulates that a *blank* memory feels negatively, rather than deriving suffering or even experience, and the unitary does not itself select an experienced branch. The negative sign is not being interpreted as mere absence; rather, the unjustified identification of a blank physical bit with a real negative feeling is precisely the problem. The candidate shows how the physical construction could carry such a bridge, and what evidence or constitutive argument would be needed to make the bridge non-arbitrary.

The necessary next bridge must therefore connect **actual organized subject incidence** to these physical relations and explain why its signed contributions obey the whole-level balance. It must discriminate subject boundaries and felt quality, preserve the reality of local suffering, and explain the actual incidence measure rather than count unexperienced batteries as subjects just to make the sum vanish. If negative experience is the relevant fundamental signed quantity, its counterterm needs its own account; absence of experience and pleasure cancelling away pain are not assumed. No choice of foliation, literal simulations, or irreducibly open chance is introduced. The Born weights above remain probabilities in a specified quantum model, not a derivation of actual occurrence or its necessity.

The construction thus provides a stronger **conditional** answer to the user's programme: a zero relation can be part of a mathematically integrated constitution that selects correlations and generates paired transfer. The specified zero alone still does not select the other relations, the dynamical law, actual subjects or phenomenal character. To establish the strongest thesis without residue, the challenge is to derive these jointly from the point/whole's own constitution, not declare the remaining choices fundamental and stop there.

## Verification

```text
python -m unittest verification.zero_relational_stabilizer_constitution_test -v
```

The 14 standard-library tests verify invariant scalar/vector basis and sampled rotations, `T_dir` compression, commuting relations, unique selector and gap via simultaneous-projector structure, both counterexamples, eight conditional directional records, AB purity, unitary pairwise-conserving controlled swaps over every encoded basis state, the correlated written state, the lifted ground state and selected commutator controls, and sampled fidelity inequalities. The continuous symmetry, full spectrum, fidelity inequality and all-state energy conservation are established analytically by the displayed identities; sampling alone would not prove them. Prior tests establish the physical-spin-singlet encodings. Neither these tests nor this finite construction establish actual consciousness or cosmological energy.
