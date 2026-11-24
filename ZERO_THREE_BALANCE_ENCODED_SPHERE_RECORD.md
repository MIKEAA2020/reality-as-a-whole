# Exact three-balance sphere record in an encoded system

## Result and scope

The [zero-origin audit](KAMLAPURE_ZERO_ORIGIN_LIMIT_SPHERE_AUDIT.md) found that a straightforward five-ray readout disturbs three directional zero constraints. There is an exact constructive alternative: **encode each two-level lab in a multiplicity of a local three-constraint zero sector**. A three-outcome local pointer can then record the same five-ray Born table while every pointer branch remains in the kernel of all three constraints, on each lab separately.

This is not a dilation of the earlier measurement on its original bare two-factor state. It is a **new, larger encoded realization of the same probability table**. The original question—whether that particular bare identity pair, with its finite directional references and clocks, can be measured while preserving an appropriate three-charge extension—remains distinct. The logical Bloch sphere here is the sphere of the encoded qubit, not automatically the original physical `X_n` sphere or a spatial sphere.

The construction has exact finite-dimensional conservation, an explicit pointer isometry and unitary completion, local no-signalling, and nonzero constituent-pair imbalances that cancel. It does not establish physical gravity, objective whole-energy zero, actual outcomes or felt experience.

## 1. A local zero sector with internal alternatives

Use the four-level operators from the article audit:

```text
X_i = |0><i| + |i><0|,  i = 1,2,3.
```

They are self-adjoint and noncommuting. Let `D=diag(1,-1,-1,-1)` and define the normalized two-constituent state

```text
|ω> = (|00>−|11>−|22>−|33>)/2.
```

For all i, `(X_i⊗I+I⊗X_i)|ω>=0`. Conjugating the second constituent by D changes `|ω>` into the former `|Φ₄>` and changes `+X_i` to `−X_iᵀ`: this is the earlier pairwise balance in different local coordinates.

Now put **four** four-level constituents in each lab, with additive generators

```text
G_i = X_i^(1)+X_i^(2)+X_i^(3)+X_i^(4).
```

Two different ways of pairing them give

```text
|s₁> = |ω>₁₂ |ω>₃₄,
|s₂> = |ω>₁₃ |ω>₂₄,
<s₁|s₂> = 1/4.
```

The order of tensor factors is always 1,2,3,4, even in the second pairing. Each `G_i` annihilates both states. Thus the orthonormal code

```text
|0_L> = |s₁>,       |1_L> = (4|s₂>−|s₁>)/√15
```

lies in the common kernel. Let `E` map an abstract qubit into these two vectors and let `P=EE†`. Then

```text
G_i E = 0,       E†G_i = 0,       [G_i,P]=0.
```

Every logical qubit operator `E L E†` therefore commutes with every `G_i`. This holds as an **operator identity on the full 4⁴-dimensional lab**, not merely for one state or in expectation. The different pairings are physically distinct here because the constituent tensor factors are distinguished; if their permutations were declared gauge, that assumption would need to be re-examined.

The code does not merely set every constituent to zero. Each first constituent has reduced state `I₄/4` for either code basis state, so `X_i` has outcomes +1 and −1 with probability 1/4 each, and zero with probability 1/2. The total generator is nevertheless exactly zero on the code.

## 2. Compensation inside the record branches

Write the two internal pair charges as

```text
A_i = X_i^(1)+X_i^(2),       B_i = X_i^(3)+X_i^(4).
```

For every code vector, `(A_i+B_i)|ψ>=0`: the second pair compensates the first as a vector identity for each i. But the first-pair constraint need not itself vanish. Its squared imbalance, restricted to the code, is

```text
E† (Σ_i A_i²) E = diag(0, 16/5).
```

For each of the three normalized five-ray pointer branches constructed below, its expectation is **8/5**, not zero. Hence this example does not obtain whole balance merely by making all internal contributions disappear. The pair charges need not commute, so this does not assert simultaneous classical values for all three; the exact statement is the common-kernel vector relation.

## 3. Two local labs and a finite record

Give Alice and Bob their own four-constituent code spaces, and prepare the **encoded** singlet

```text
|Ψ_L> = (|0_L>_A|1_L>_B − |1_L>_A|0_L>_B)/√2.
```

Each of the six local generators `G_i^A`, `G_i^B` annihilates this state. In particular, the sum or difference of the two labs' generators also annihilates it. The encoded singlet is a specified initial state: local zero constraints by themselves do **not** select it, since arbitrary logical states also obey those constraints.

Choose the earlier triple effects on Alice's logical qubit,

```text
F_i = q_i (I+n_i·σ),       q = (1/8, 2/5, 19/40),
K_i = √F_i = F_i/√(2q_i),  Σ_i K_i†K_i = I.
```

The supplied `n_i` and Bob's axis are exactly those of the earlier [five-ray model](ZERO_SPHERE_CONSERVATION_RECORD_CURRENT_SINGLE_SYSTEM.md). A neutral three-state pointer starts in `|0>_P`. The isometry

```text
|ψ>_L |0>_P  ↦  Σ_i K_i|ψ>_L |i>_P
```

has an explicit 6×6 unitary completion `U_L` in the verifier. On the whole physical lab and pointer set

```text
U_A = (I−P)⊗I_P + (E⊗I_P) U_L (E†⊗I_P).
```

This is unitary and `[U_A,G_i^A⊗I_P]=0` on the entire lab–pointer Hilbert space. Pointer projectors `I⊗|i><i|` commute with the constraints too. Thus **each selected pointer branch**, not only the unselected state, satisfies all three local constraints. Bob can analogously measure his encoded spin with a neutral pointer using a unitary of the same form; his operation commutes with all his generators and with Alice's local operations.

By the finite-dimensional spectral theorem one can choose a Hermitian logarithm of `U_L`, embed it in the same code, and obtain a time-independent local interaction generating this readout at a specified interaction parameter. That establishes an interaction generator commuting with the declared `G_i`; it does not supply a physical clock, show that its energy vanishes, or account for switching, preparation and every interaction. No preferred spacetime foliation is assumed by the finite algebra.

## 4. Retained sphere statistics and locality

With the encoded singlet and Bob's logical axis, the exact joint table is

```text
                  Bob +       Bob −
pointer 1          3/40        1/20
pointer 2          1/10        3/10
pointer 3         13/40        3/20.
```

The pointer marginal is `q`, and Bob's is `(1/2,1/2)`. Alice's complete unread instrument leaves Bob's reduced logical state `I₂/2`, even though Bob's state conditioned on Alice's pointer differs between outcomes. Therefore no message is available to Bob from Alice's choice without communication. The result uses the usual tensor-product locality of this finite model; it is not a constructed spacelike experiment or a demonstration of relativistic causal structure.

The pointer is a quantum record in the operational sense that its orthogonal states correlate with the instrument's outcomes. Its neutrality is explicitly **stipulated**: all three charge operators act trivially on that pointer. The model does not establish stable decoherence, thermodynamic irreversibility, a uniquely selected outcome, or a subject who experiences the label. A conditioned branch is not by itself a reported experience, and no local suffering is cancelled or erased by naming these algebraic signs.

## 5. What this adds to the zero proposal

The construction answers a narrower but real interface problem affirmatively: an apparatus-inclusive, finite local measurement can retain nontrivial internal cancellation, preserve three noncommuting directional balances **exactly and branch by branch**, and reproduce the previous ideal table. It does so by moving the informational degree of freedom into a **multiplicity inside the common zero sector**. Zero constraint need not mean a one-dimensional or inert space once the system has internal constituents.

The trade-off is equally exact. In the earlier two-factor model the chosen three balances select a unique state. After adding constituents, the common zero sector has at least two local dimensions, and conservation alone leaves many logical states and measurements available. Thus the desired five-ray state, axes, pairing, tensor factors, pointer and dynamics are not derived from bare zero. Nor does equality of the numerical table show that the two constructions have identical physical geometry or local subject organization.

A productive next step is to connect the encoded zero-sector instrument to the **actual earlier sphere/reference/clock and work-current system**, rather than infer equivalence from matching probabilities. In particular, one must derive or implement a charge-preserving map between the specified preparations, track any reference and control charges, and test whether the encoded pointer can be linked to the earlier strict local-report condition. A relation between these signs and actual experiential valence remains an independent, substantive task; equal-and-opposite algebraic charges do not establish equal experiential incidence or make suffering disappear.

## Reproduce

```sh
python -m pip install --target .arena/python-deps numpy  # if needed
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_three_balance_encoded_sphere_record_test -v
```

The verifier constructs the code vectors, all three 256×256 lab charges, a concrete 6×6 readout unitary, each branch, the internal-pair compensation, the joint table and Bob's reduced state. Operator conservation of the full 768×768 unitary follows analytically from the tested `G_i E=0` and `[G_i,P]=0`; the verifier need not allocate the full unitary. Numerical tests supplement rather than establish the physical or experiential interpretation.
