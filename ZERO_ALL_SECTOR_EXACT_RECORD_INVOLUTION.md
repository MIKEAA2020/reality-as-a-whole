# An exact all-sector record involution: balanced incidences without exchanging unequal sectors

## Result

The proposed next test can be carried out on the **existing full sphere–clock–work circuit**, without exchanging its 158- and 96-dimensional complement sectors. There is an exact unitary involution on the retained record, work and target-memory registers which:

- preserves the specified **coherent whole state**, separately on its code and complement components, without discarding either;
- leaves the sphere labels, all 16 relative-clock labels, Bob's pointer, and the original record value fixed;
- exchanges the two values of the record–work relation `h` and the corresponding target-memory values;
- preserves the model's declared directional balances and energy charge; and
- forces **equal Born weights for the paired h incidences in every fixed combination of sector, clock label, Alice outcome, Bob outcome and original record value**, not merely in the total average.

The target memory can physically record which h value occurred because it was explicitly coupled to the joint record–work relation. The original confined record alone cannot distinguish the two h preparations. This is a concrete, causal distinction between a paired physical record and an assumed subject or automatically accessible experience.

**Scope:** this involution is a symmetry of the specified final state and readout, not of every possible preparation, nor necessarily of the complete preparation dynamics. The clock, pairing, circuit and energy charge remain stipulated. Born weights do not decide which outcomes are actual or whether any register feels anything. This result therefore develops the user's proposal but does not derive physical differentiation, actual subject plurality, felt sign, or objective cosmological energy from zero alone.

Verifier: [verification/zero_all_sector_record_involution_test.py](verification/zero_all_sector_record_involution_test.py). This continues the [all-sector circuit](ZERO_ALL_SECTOR_SPHERE_CLOCK_WORK_RECORD.md), the [subject-boundary result](ZERO_SUBJECT_BOUNDARY_REPORT_CAUSALITY.md), and the [Carreira–Gonzalo audit](CARREIRA_GONZALO_ZERO_WHOLE_COSMOLOGY_AUDIT.md).

**Branchwise continuation:** [exact branchwise balance and conditional selection](ZERO_BRANCHWISE_BALANCE_AND_CONDITIONAL_SELECTION.md) identifies two commuting physical observables with opposite sharp values in each joint branch and constructs a charge-compatible Hamiltonian selecting the symmetric work–target state at fixed record value.

## 1. Where the pairing acts

The preceding circuit keeps the two orthogonal global lab sectors: the encoded code of total weight `1/128` and its complement of weight `127/128`. The complement includes projectors `P_+` and `P_-` of ranks 158 and 96. A unitary on the same lab Hilbert space cannot exchange those projectors, because unitary conjugation preserves rank. This does not rule out more elaborate pairings with other resources; it rules out the proposed direct exchange on that space.

Instead keep both projectors fixed and act on registers already present in **each** sector:

- `R`: the two-state record copied from Bob's pointer, with `Z_R|r⟩=r|r⟩`, `r=±1`. Physically this is the record pair `|01⟩,|10⟩`.
- `W`: the active four-bit work subspace spanned by `|a⟩=|0110⟩` and `|b⟩=|1001⟩`. On this subspace `J₁=−Y_W`, the probe current defined from the standalone exchange.
- `T`: the neutral two-state target memory explicitly coupled to the relation.

Define

```text
K = Z_R J₁,
h = (I−K)/2                   [on the active work subspace],
U = −Z_R ⊗ X_W ⊗ X_T.
```

The overall minus sign fixes a convenient vector phase; conjugation and probabilities do not depend on it. `U` is Hermitian and `U²=I`. Direct operator calculation gives

```text
U K U† = −K,       U h U† = I−h,
U Z_T U† = −Z_T,   U J₁ U† = −J₁,
U Z_R U† = Z_R.
```

So a branch with a fixed original record r and h=0 is paired with one at the **same r** and h=1. The target bit and J₁ sign reverse; the original record sign does not. This acts on a different factor from the unequal lab-sector projectors, and consequently does not require them to have equal rank.

### Physical extension and balances

The active `X_W` is the exchange of `|0110⟩` and `|1001⟩`. Extend it by identity on the other 14 four-bit work states. The resulting four-bit operator is a Hermitian involution and commutes on the **whole** 16-dimensional work space with the total work number, as well as the indicated work-pair number sums checked by the verifier. Unlike an unrestricted four-bit `X⊗X⊗X⊗X`, this full extension commutes with total work energy off the active subspace too. Individual occupations need not be conserved.

The operation acts trivially on the physical labs, their directional generators and lab/reference energy operators; R and T are neutral under the stipulated charges. It therefore commutes with those directional balances and the full declared energy charge, not just their expectation values. It need not commute with every local occupation or with the interaction that prepared the state. This algebraic implementation is not yet an account of the costs, spacetime locality, or controlled execution of an operation across separate laboratories.

On inactive work states, the extended relation is `h=(P_act−Z_R J₁)/2` and `U h U†=P_act−h`. All specified circuit states lie in the active sector, where `P_act=I`.

## 2. The actual final state has the symmetry

Let `|ψ_C⟩` be the fully evolved normalized code component and `|ψ_D⟩` the corresponding normalized complement component, with their respective physical isometric embeddings as in the all-sector construction. Each has its original lab, references, clocks, sphere pointers, R, W and T. Direct application gives

```text
U|ψ_C⟩ = |ψ_C⟩,       U|ψ_D⟩ = |ψ_D⟩.
```

Consequently the specified coherent physical whole, schematically

```text
|Ψ⟩ = √(1/128)|ψ_C⟩ + √(127/128)|ψ_D⟩,
```

is also invariant. This uses the fixed physical embeddings and any explicit correlated flags of the previous construction; the two pieces are orthogonal. It does **not** replace the coherent state by a classical mixture. In fact, because U fixes both vectors separately, it fixes any coherent superposition of them. No relative phase is removed by this inference.

The clock instrument acts on other factors and commutes with U. For **each** of the 16 actual relative-clock readout labels ℓ, including those outside the previously considered three-label window, its unnormalized branch obeys

```text
U|ψ_(sector,ℓ)⟩ = |ψ_(sector,ℓ)⟩,
U P_h=0|ψ_(sector,ℓ)⟩ = P_h=1|ψ_(sector,ℓ)⟩.
```

The target's perfect h record makes these paired branch vectors orthogonal. They are not merely a relabeling of the same target projector: U conjugates the physically specified target projectors `|0⟩⟨0|` and `|1⟩⟨1|` into one another, and those states are distinguishable by the target's Z readout. This makes the operation nontrivial on the model's observable algebra; it does **not** by itself settle whether a fundamental theory should treat the transformation as gauge or whether the branches are actually experienced.

## 3. Equal incidence weights with all relevant conditions retained

Let `F` be any effect acting on the other retained factors and/or diagonal in the original R value, which commutes with U. This includes fixed sphere outcome i, Bob pointer j, original record r, a specified sector flag, and a specified relative-clock label ℓ. For the state `ρ=|Ψ⟩⟨Ψ|`, invariance and `U P₀ U†=P₁` imply

```text
tr(ρ F P₀) = tr(ρ F P₁).
```

The verifier checks this equality **individually** for every combination of the two sectors, all 16 clock labels, i, j and r, including zero-weight combinations. For either normalized sector, the probability of each clock label and h value is `1/32`. For the three-label window, `P(window,h=0)=P(window,h=1)=3/32`; the target is perfectly correlated with h. The prior event `P(window,r=+,T=1)=3/64` applies to the full specified state, not only to the code.

In particular, define three distinct signed readouts on a simultaneous R–W–T measurement:

```text
q_R = κ r,
q_J = κ j₁ = κ r (1−2h),
q_T = κ (1−2h),                    κ>0.
```

Here `j₁=±1` is the J₁ eigenvalue. The new U reverses `q_J` and `q_T` but **not** `q_R`. Thus the modeled sums of q_J and q_T vanish in every fixed `(sector,ℓ,i,j,r)` cell; no assumption of equal weight across the unequal lab sectors is needed. This is a physical/mathematical signed-readout result. It is not yet a statement that q_J or q_T is felt valence.

The distinction matters: the full three-label-window sphere table has

```text
              r=+          r=−
i=1          0.06546799    0.05953201
i=2          0.17625608    0.22374392
i=3          0.25827593    0.21672407
```

The record sign is biased at fixed i, even though h and target signs are exactly paired **within each fixed i and r**. Balancing one physically defined sign cannot be transferred to another just because both are called “opposites.” The table is a Born probability table conditional on the joint clock window; it is not evidence of an experienced distribution.

## 4. Does either confined register access the relation?

For the specified original preparations, with all 16 clock labels retained, normalized reductions satisfy

```text
ρ_R | h=0 = ρ_R | h=1 = I/2,
ρ_W | h=0 = ρ_W | h=1 = I/2,
ρ_T | h=0 = |0⟩⟨0|,
ρ_T | h=1 = |1⟩⟨1|.
```

The first two equalities are for the unconditioned sphere records; giving an observer additional information such as Alice's result can change a reduced-state comparison. The target can distinguish h precisely because the specified gate couples it to the joint R–W relation. This is an actual causal interface in the finite circuit, not a claim that every confined record has it. The earlier locality objection still holds: a report of J's sign cannot be generated from R alone for the relevant equal-reduction preparations without further access or assumptions.

One may consistently propose **as an additional hypothesis** that target states have signed felt values `q_T=±κ`, or that a subject spanning the relevant interface has values proportional to `q_J`. Neither proposal follows from the quantum state, record, unitary or symmetry. Moreover `q_T` and `−q_T` are equally compatible with the same physical equations and pairing; a law connecting physical organization to *which* sign is felt is not supplied by U. A single target register at two alternative outcomes is not automatically two actual subjects, and a superposition or Born weight is not by itself an actual-incidence ontology. If actual distinct subjects and an incidence measure are independently established, an opposite contribution cannot make a particular subject's suffering unreal.

## 5. Why this is not yet a derivation from zero

The pairing is exact but its source matters. In the supplied circuit, the `π/4` work phase pulse and perfect target interaction create the state that U fixes. Changing only the work phase to α gives

```text
P(h=0)=cos²α,    P(h=1)=sin²α,
||U|ψ_α⟩−|ψ_α⟩||² = 2−2 sin(2α).
```

At α=0 the h weights are 1 and 0, though the same declared charges are conserved. At α=π/8 they are approximately 0.853553 and 0.146447. Only the specified α=π/4 gives this particular symmetry. Similarly, replacing the full target pulse with the earlier partial pulse breaks the stated U invariance. U sends h to `I−h`, so it is not automatically a symmetry commuting with the chosen h interaction generator. These are explicit controls, not a claim that no deeper constitution could select the symmetric preparation.

The progression is therefore precise:

1. **Existing mathematical fact:** one full, coherent all-sector final state has an explicit charge-preserving involution and equal paired Born weights at a much finer resolution than the original sector split.
2. **Constitutive task:** derive this preparation, target coupling, physical algebra and the active—not merely passive or gauge—pairing from zero's own necessary structure, rather than select them as circuit inputs.
3. **Experiential task:** derive actual subject incidence and a signed felt quantity that transforms under the physical pairing, including its measure. A target report is a physical interface, not proof of feeling. An assignment with the opposite overall felt orientation is currently equally compatible with the tested physical relations.
4. **Cosmological task:** connect the declared finite charge to any genuinely objective whole-level quantity; a zero Hamiltonian constraint or finite circuit charge is not automatically global energy in GR.

The work replaces the failed direct `158 ↔ 96` sector exchange with a stronger, constructive **within-sector record pairing**. It also shows exactly where the proposal has gained a physical consequence and where the demand for a no-residue account must do further work.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_all_sector_record_involution_test -v
```

NumPy is required. The checks cover the full 16-dimensional physical work extension, state-vector symmetry in both sectors and all 16 clock labels, per-cell equal weights, target/record/work reductions, conserved work charges, and preparation controls. The statement about all combinations of physical sector embeddings follows from the exact isometries and block construction verified in the preceding all-sector tests. No test purports to establish consciousness, actual outcomes, subject boundaries, continuum gravity, or a proof of metaphysical necessity.
