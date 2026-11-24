# Encoded directional balance joined to the finite sphere, clock and work

## Result

The [three-balance encoded sphere](ZERO_THREE_BALANCE_ENCODED_SPHERE_RECORD.md) can be joined exactly to the *actual finite circuit* of the earlier [sphere, relative clock and work-current model](ZERO_ENERGY_SPHERE_WORK_SUBJECT_INCIDENCE.md), not just matched to its ideal table. Replace each of that circuit's two spin qubits by the four-constituent zero-sector code, and transport the actual finite-reference instruments through the local code isometries. The resulting single specified model has:

* all three directional generators exactly zero **on each encoded lab**, including every sphere and clock-pointer branch;
* the earlier declared additive energy charge Q exactly zero, including its finite reference/clock registers and nondegenerate work occupations;
* the same finite-L clock-window probabilities, work-current relation, target-memory correlations and operational locality tests as the original circuit; and
* nonzero internal pair imbalance in the **same** conditional record/work event, exactly compensated by its partner.

These are properties of the stated finite model. The result is not a derivation of physical spacetime, real subjectivity or objective cosmic energy zero. The code, the transformed energy operators, initial state, pointer, clock spectra and interactions are specified inputs. In particular, this is an isometric encoding of the **two qubits in the earlier clock/work circuit**; it is not a demonstrated physical conversion of the former four-level bare identity-pair preparation.

The bridge also supplies an explicit preparation: four globally paired four-level systems, with a specified invariant local rotation, feed charge-preserving local flag measurements. Their correlated success branch prepares exactly the encoded singlet; the failure branch is retained and remains globally balanced. This is a conditional preparation using a substantial paired resource, not a derivation of that resource from zero.

There are two concrete costs. The encoded spin energy must be a multi-constituent interaction if all three directional generators are to be conserved; and deterministic conversion of the original bare pair with an uncorrelated local apparatus into the local zero code is impossible by local charge-preserving unitaries. Both are quantified below.

Verifier: [verification/zero_encoded_sphere_clock_work_bridge_test.py](verification/zero_encoded_sphere_clock_work_bridge_test.py).

## 1. The local isometry and the actual instruments

For each lab, let `E: C² → (C⁴)⊗4` be the isometry from the previous report, with `P_c=EE†`. Its two basis vectors are distinct four-constituent pairing states. Each lab has

```text
G_i = Σ_(k=1)^4 X_i^(k),       G_i E = 0,       i=1,2,3.
```

The `G_i` are noncommuting directional operators. Set the encoded spin energies to

```text
H_A^enc = E |1><1| E†,
H_B^enc = E (|1><1|−I₂) E†,
```

and choose zero action on the code complement. Then `H_A^enc E=E H_A`, `H_B^enc E=E H_B` for the two energy operators in the earlier finite circuit, and both commute with all three respective `G_i`. The choice of the complement is a specified extension, not a unique physical Hamiltonian.

The earlier Alice and Bob reference instruments are not replaced by a new ideal POVM. For L=4 we use their **actual energy-block unitaries** `U_A`, `U_B`, including finite reference and pointer registers, and lift each by

```text
U^enc = (I−P_c)⊗I_ref,pointer + (E⊗I_ref,pointer) U (E†⊗I_ref,pointer).
```

This is a unitary on the complete local lab plus its reference and pointer. Since the old U commutes with the corresponding spin-plus-reference energy, its lift commutes with `H^enc+N_ref` on the whole enlarged space. It also commutes with every `G_i` as an operator, including outside the code: `G_i E=E†G_i=0` and the complement is unchanged. The finite tests explicitly reconstruct the original block unitaries, test their pointer isometries and energy commutators, and check the lifted operations on full physical-lab/reference/pointer vectors.

Transporting both input spins and all their gates this way is an exact intertwining: for any earlier state `|ψ>` and circuit operation V, the encoded action on the code equals `(E_A⊗E_B⊗I) V|ψ>`. The full state is represented in factored form, avoiding a huge physical-lab-by-environment array. The test also expands a nonzero conditional event into an explicit 256×256 physical two-lab slice and verifies the charges directly.

All record, work, target-memory and clock-pointer operations act on their original retained registers. They therefore commute with the lab `G_i`; the finite relative-clock effects and work gates retain their earlier Q-conservation properties. This includes the actual active work subspace `|0110>`, `|1001>` with energy 2 and its current probe `J₁=−Y` in that subspace.

## 2. Two kinds of zero, simultaneously

With `P=|1><1|`, the encoded model's declared charge is

```text
Q_enc = H_A^enc + H_B^enc
      + N_RA − N_CA + N_RB − (N_CB + 2I) + H_work.
```

It is the earlier Q transported by E on the encoded support. Every state produced by the specified circuit and each finite clock-pointer outcome obey

```text
Q_enc |Ψ> = 0,
G_i^A |Ψ> = 0,       G_i^B |Ψ> = 0,     for i=1,2,3.
```

The six local conditions imply a zero sum and a zero difference between corresponding lab generators, but are **stronger than** the old two-factor directional pairing: here each encoded lab is already locally in a zero sector. The energy Q and directional `G_i` are different declared quantities, not an identification of energy with a directional sign. At finite L, reference-dependent records remain unsharp.

The `−2` clock offset compensating the work energy, the pointer's neutral charge, the lab energy operators and the circuit schedule are explicit assumptions. Q does not include a full autonomous account of the switching/control and interaction energies; a vanishing Q constraint is not automatically the universe's objective total energy.

## 3. The same clock/work event retains internal cancellation

The relative-clock instrument uses the earlier 16 outcomes and the three-label window around zero. The window still has probability `3/16`. Conditional on it, the finite-reference sphere/record table is unchanged:

| sphere i | r=+ | r=− |
|---|---:|---:|
| 1 | 0.06917444 | 0.05582556 |
| 2 | 0.14660452 | 0.25339548 |
| 3 | 0.28422105 | 0.19077895 |

The target T perfectly records the stipulated relation `h=(P_act−Z_R J₁)/2` at the chosen pulse. For the same event discussed in the earlier report,

```text
clock window, r=+, T=1:    probability = 3/64;    h=1, J₁=−1.
```

This is a conditional quantum event, not a claim that one outcome has been selected. Inside encoded Alice's lab define

```text
A_i = X_i^(1)+X_i^(2),    B_i = X_i^(3)+X_i^(4).
```

On the entire encoded support, `(A_i+B_i)|Ψ>=0` for each i. Yet on the above clock/record/target event,

```text
<Σ_i A_i²> = 1.877128129211...,
```

so the first pair's imbalance is genuinely nonzero, and the other pair exactly compensates it. This is a quantum vector identity, not a statement that all noncommuting components simultaneously have sharp classical values. The numerical value depends on the specified preparation and finite clock window.

The earlier relational-information result also survives exactly. On the specified h-conditioned subensembles, the separate record and work reductions are both `I₂/2`, whereas

```text
ρ_RW^(h) = [I₄+(1−2h)Z_R J₁]/4.
```

Thus the joint relation distinguishes h even though neither individual marginal does. The target has access through its explicit joint coupling; a strictly record-only report does not acquire that access merely because the larger whole is balanced. The previous caveat about supplying Alice's outcome still applies. The local encoding does not turn the physical registers into experiencing subjects or determine felt valence; opposite algebraic values do not erase suffering.

The same local-isometry argument transports the earlier no-signalling result. In the fixed circuit, after tracing Alice's lab, reference and pointer, Bob's retained state is independent of Alice's nonselective pair versus triple setting, both before and after the same three-label clock-window conditioning. Bob's encoded density operators are the local-isometric images of those equal original operators. This is a tensor-product statement in the finite circuit, not a spacetime separation or a claim that inaccessible conditional labels are locally experienced.

## 4. The energy cost has real internal structure

The energy splitting is not obtainable here by assigning independent one-constituent energies while retaining all three exact local directional symmetries. Suppose

```text
H_one = Σ_(k=1)^4 h_k^(k),       [H_one,G_i]=0 for every i.
```

Partial trace over the other three constituents gives `[h_k,X_i]=0` for every k and i: the other commutator terms vanish under trace. The `X_i` generate the full 4×4 matrix algebra, so their common commutant consists of scalars. Therefore every `h_k` is scalar and `H_one` cannot split the two logical code states.

Consequently the explicitly used `H_A^enc` is necessarily a **multi-site lab interaction** in this tensor-factor model. More concretely, its Hilbert–Schmidt projection onto all constant plus one-site operators is `I₂₅₆/256`, leaving residual norm `√(255/256)`. That numerical result is tested. This does not prohibit symmetry-preserving energy exchange with additional directional reference charges, nor does it prove such an interaction is physically fundamental. It does prevent interpreting the logical 0/1 energy as if it had already been derived from four independent constituent energies.

## 5. Preparation is not free

Consider the former bare four-level identity pair, whose Alice marginal is `I₄/4`, and append an **uncorrelated** three-constituent local apparatus in any state σ. Let

```text
C_A = Σ_i (G_i^A)²,        R_i = Σ_(k=2)^4 X_i^(k).
```

Because the bare marginal has zero `X_i` mean, all cross terms vanish, giving

```text
<C_A>_initial = 3/2 + Tr[σ Σ_i R_i²].
```

For the specified three-site representation the smallest eigenvalue of `Σ_i R_i²` is 1, as verified by finite-dimensional numerical diagonalization. Hence `<C_A>≥5/2` for this representation; the weaker `<C_A>≥3/2` also follows analytically from positivity alone. The encoded zero sector has `<C_A>=0`. Any unitary that preserves each `G_i^A` also preserves `C_A`; therefore **no such Alice-local unitary can perform this preparation from an uncorrelated local apparatus**, regardless of its state. The corresponding statement applies to Bob with the appropriate parity convention.

This is not a no-go for all preparations. Initially correlated compensating resources, exchange of directional charge with an extended reference, or operations conserving only a larger global charge are different cases. The result identifies what a genuine preparation bridge must supply instead of silently treating the mathematical isometry as a free physical gate. It also does not refute the user's proposal of necessary internal pairing; it specifies a condition any concrete implementation of that proposal must meet.

## 6. Explicit globally balanced preparation, with failure retained

There is a concrete way around the deterministic local-preparation obstruction—using an explicit paired resource rather than pretending it is free. Give each lab four four-level constituents and start from the four cross-lab identity pairs

```text
|Φ₂₅₆> = (1/16) Σ_(a=0)^255 |a>_A |a>_B.
```

Let `R=[[0,−1],[1,0]]` act on the logical code and define Bob's specified invariant unitary `V=E R E†+(I−P_c)`. The actual input is

```text
|Ω> = (I_A⊗V_B)|Φ₂₅₆>.
```

This is an explicitly correlated global resource. `V` commutes with Bob's three directional generators. Since the generators here are real and symmetric, the state satisfies `(G_i^A−G_i^B)|Ω>=0`. With the encoded lab energies defined above it also satisfies `(H_A^enc+H_B^enc)|Ω>=0`. Supplement it with the same paired references/clocks and work-energy-2 initial state as the earlier circuit; their specified charge contributions still cancel. These initial correlations and the choice of V are inputs, not consequences derived from bare zero.

On each lab, use a neutral flag initially in `|0>` and the local unitary

```text
U_flag = (I−P_c)⊗I_flag + P_c⊗X_flag.
```

It commutes with all three local `G_i` and the lab's declared energy, and records whether that lab lies in the code. The two flags agree perfectly on this input:

```text
flags 0,0:  probability 127/128,
flags 1,1:  probability   1/128,
flags 0,1 or 1,0: probability 0.
```

Conditional on flags 1,1, the normalized physical state is **exactly the encoded logical singlet** required by the finite sphere/clock/work circuit. Every flag branch preserves the global directional balances and energy zero. In the successful branch the three directional balances vanish separately in each lab; the failure branch need not have locally zero generators and is **not discarded from the whole**. For example, Alice's initial `<ΣG_i²>=6`; it is 0 on success and `768/127` on failure, giving the same overall average 6. This is how conditional local zero is compatible with conservation and with the preceding no-free-preparation bound.

The flags can coherently control the subsequent prescribed circuit on the success sector; the failure sector can remain present without being mislabeled as an encoded success. With the prior reference/clock and work preparation, the unconditional Born weight of success followed by the clock window and `r=+,T=1` is

```text
(1/128) × (3/64) = 3/8192.
```

This multiplies specified conditional probabilities; it does not explain which outcome is actual. Alice's unread flag leaves Bob's reduced state unchanged, so the correlated flags do not send a message. The construction presupposes the cross-lab paired state, V, code projectors, neutral flags and later controlled interactions. It is not a deterministic, resource-free conversion of the single bare pair, nor a preparation of the original bare-state instrument with all of its directional constraints.

## 7. Consequence and next construction

This integration establishes that finite clock/work statistics, exact noncommuting directional balances and an explicit conditional preparation can coexist in one specified encoded circuit. The previous matching-table result was not the whole connection. A local zero sector has relational multiplicity, its useful energy splitting is interacting, and preparation transfers a particular already-paired global resource into a locally balanced success branch while retaining the balanced failure branch.

The next constructive problem is to explain the initially paired resource and interaction structure within the proposed constitution, and to relate this controlled finite circuit to the original physical rather than merely encoded directional observables. The physical identification of Q and the rule relating actual subject–quality incidence to the structure also remain to be justified. The formal R-versus-−R experiential ambiguity in the earlier report remains; neither local signs nor their balanced sum determine which experience is felt.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_encoded_sphere_clock_work_bridge_test -v
```

The verifier constructs the two actual finite sphere unitaries, tests their isometric physical lifts and energy/directional commutation, rechecks Q on all compressed clock branches and one explicit full-constituent slice, verifies the work/target and no-signalling results, and checks the interaction and preparation bounds. It also constructs the paired input and both local-flag branches, including the success state and failure-sector charge variance. The large clock/work physical tensor is handled exactly through the isometry rather than allocated in full. These finite tests establish the declared algebraic model, not the metaphysical or experiential claims.
