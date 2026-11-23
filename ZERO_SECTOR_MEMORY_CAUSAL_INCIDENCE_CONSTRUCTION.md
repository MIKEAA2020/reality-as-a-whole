# Zero-sector memory, causal roles and experiential incidence

## Result in brief

The preceding [zero-sector instrument](ZERO_INVARIANT_SPHERE_STEERING_INSTRUMENT.md) correlated a pointer with the conserved-sphere measurement without leaving physical total-spin zero. This continuation adds memory to that same model and tests what follows for subjects and signed incidence.

The constructive result has three parts:

1. A second zero-spin register can copy the three possible pointer labels. The two records agree exactly; the pointer locally decoheres; and a rotationally invariant storage Hamiltonian has an energy gap against their mismatch. All of this stays within physical total-spin zero.
2. A **directed record-copying relation** supplies distinguishable source and receiver roles. Assigning equal and opposite signed observables to those roles gives exact cancellation **in each record branch**, not merely an average over possible outcomes. The opposite contributions remain individually nonzero.
3. That cancellation is conditional on an incidence and sign rule. The equal-time source and receiver records are exchange-symmetric; a rule depending only on their individual present record states assigns them the same sign, not opposite signs. Causal history can distinguish the roles, but neither its identification with experience nor which orientation feels positive is fixed by the physical construction.

An additional selective memory exposes another issue: conservation-weighted zero can become nonzero when record occurrences are counted with different multiplicities. This is an explicit test of a proposed subject-counting rule, **not evidence that memory registers are subjects**. The result preserves the user's distinction between real local suffering and a signed whole-level sum; a compensating term does not erase anyone's experience.

## 1. One system from conservation through memory

Use the prior asymmetric five-ray example `0,1,3,i,2i`. Its conserved triple has intrinsic energy fractions and directional values along a chosen pair-ray axis

```text
q = (1/8, 2/5, 19/40),
s = (−1/5, 1/2, −7/19),
Σ_i q_i s_i = 0.
```

These are physical center-frame quantities from the previous construction, not valence measurements. The pair-ray role and its orientation are specified; the signed direction reverses if that orientation is reversed.

As before, encode logical systems `A,B` in separate four-spin zero sectors, prepare their logical singlet, and encode pointer `R` in a six-spin zero sector. The logical POVM effects are `F_i=2q_iΠ_i` and `K_i=√(2q_i)Π_i`. A specified invariant unitary yields

```text
|Ψ⟩_ABR = Σ_i (K_i⊗I)|Ψ⁻_L⟩_AB |i⟩_R,
Pr(i) = q_i.
```

The pointer basis `|i⟩` consists of orthogonal six-spin singlets. Their correspondence with the conserved-ray labels and the state preparation remain assumptions. The probabilities are Born weights for this stipulated state and measurement, not automatically empirical frequencies or actual experiential incidence.

Add two further six-spin zero-sector registers, `M` and `N`, both initially `|0⟩`. All five blocks are in physical spin-zero sectors; the model contains **26 spins**. Each register below uses an orthonormal five-state singlet basis. On the encoded spaces define reversible controlled shifts

```text
C_RM: |i⟩_R |j⟩_M ↦ |i⟩_R |j+i mod 5⟩_M,
C_RN: |i⟩_R |j⟩_N ↦ |i⟩_R |j+δ_(i,1) mod 5⟩_N.
```

Each is a permutation unitary on the encoded sector. Extend it by the identity on the orthogonal complement of the two six-spin zero sectors. Since physical rotations act trivially within those sectors and preserve the complement, each extended operation commutes with physical total spin. Thus all stages, and each selected pointer branch, remain in exact spin zero. A logarithm of each unitary supplies an invariant interaction for that stage; switching the stages and implementing them with local, few-body interactions are not derived here. The order may be read relative to an operational clock; no fundamental preferred foliation is asserted.

After both copies the joint state is

```text
Σ_i (K_i⊗I)|Ψ⁻_L⟩_AB |i⟩_R |i⟩_M |δ_(i,1)⟩_N.
```

`M` records the complete three-valued pointer label. `N` is only a **selective flag** for outcome 1, not a full independent copy of the three-valued record. The first operation alone already makes `R` and `M` perfectly correlated. Repeated ideal sharp readings of both labels return the same `i` in a conditioned branch.

Tracing `M` out makes the reduced pointer density matrix diagonal in the record basis. This is ordinary decoherence by entanglement, not destruction of global coherence. Applying the inverse shifts restores the pre-copy state. No irreversible selection or experience follows from it.

## 2. A storage mechanism, with its limits

Within the five-by-five encoded `R,M` sector, define

```text
H_store = Δ [I_RM − Σ_(i=0)^4 |ii⟩⟨ii|],      Δ>0.
```

Extend by zero outside that sector. It is a physical rotation-invariant positive Hamiltonian. The five matched states have energy zero, and the twenty mismatched label states have energy `Δ`; its normalized form is a projector. The copied state is an eigenstate with energy zero, so under this isolated storage Hamiltonian the correlations persist for any duration of this idealized stage. A mismatch costs energy within the stipulated model.

This is stronger than a correlation at one instant, but it is not a complete theory of durable memory. Simultaneously changing both labels preserves the matched subspace and its energy; the test constructs such an error explicitly. Thermal noise, active correction, natural spatial locality, autonomous clocking and macroscopic irreversibility are not established. The chosen `Δ`, storage interaction and energy reference are inputs; this is not a derivation of the whole's objective energy zero.

## 3. Branchwise signed zero from the causal relation

The copy operation itself gives the two registers distinguishable **causal roles**. If the input of `M` is fixed, intervening on the encoded input label of `R` changes the output label of `M`. If the input of `R` is fixed, changing the encoded input of `M` does not change the output of `R`. This direction is defined by the specified intervention and preparation, not by calling one register a subject. It is relative to the physical process and its ordering, not a preferred cosmic time.

On the record subspace define two signed operators

```text
V_R =  Σ_i s_i |i⟩⟨i|_R,
V_M = −Σ_i s_i |i⟩⟨i|_M.
```

The other two unused basis labels can be assigned zero. On the state after copying,

```text
(V_R + V_M)|Ψ_after⟩ = 0.
```

More strongly, in every nonzero branch `i` the sharp values are `s_i` and `−s_i`; all three `s_i` are nonzero. Thus the cancellation holds for each conditional record, regardless of the weights `q_i`. This is a different and stronger mathematical fact than `Σq_i s_i=0`, which averages over alternative measurement outcomes. The selective flag does not alter the identity for `R,M`.

One candidate interpretation would regard the directed interaction as a single relational event with oppositely oriented incidences at its source and receiver. That offers a **specific joint constitution hypothesis**: if, independently of the desired result, these incidences are actual subjects and these signed values are their felt valences, the model gives a branchwise zero while preserving two nonzero local terms. But assigning `+s_i` to the source and `−s_i` to the receiver is an explicit proposed bridge, not a consequence of copying. Reversing both signs leaves the physical dynamics and zero unchanged. Nor has the model shown that both nodes are subjects rather than records in an unexperienced apparatus.

The sign rule is not morally or phenomenologically neutral: a real negative experience would be real for its subject even if an opposite signed contribution existed elsewhere. The algebra does not make pain disappear or show that positive feeling literally cancels suffering.

## 4. Why causal history matters—and what it does not settle

After the copy, the *present* joint state is invariant under exchanging `R` and `M`. Their individual reduced states are equal, and in a conditioned branch both are the same pure record state `|i⟩`. The storage Hamiltonian above is also exchange-symmetric. Therefore a common rule assigning felt value solely as the same function of each register's present reduced state must give the **same** value to both. It cannot yield opposite nonzero values.

The causal preparation is not exchange-symmetric: `R` controlled the update and `M` started blank. Hence a constitution sensitive to actual causal history can distinguish their roles without changing the final local record states. That is a constructive candidate for obtaining an intrinsic orientation, not proof that causal direction fixes phenomenology. A reversal of the sign convention still gives the same physical histories and conservation facts. A stronger physical–experiential principle must establish why one orientation corresponds to a particular felt quality rather than its opposite, as well as why this organization constitutes a subject at all.

This conditional symmetry argument does not rule out criteria involving the whole interaction history, other local variables, biological organization, or additional physically grounded structures. Conversely, naming source and receiver is not enough to derive felt character.

## 5. Memory multiplicity can change a weighted balance

There is another candidate rule: count each record-bearing occurrence equally. To make it explicit, count the pointer and full memory as two occurrences in each branch, and stipulate that the selective flag is an additional occurrence **only when activated**. The resulting multiplicities are

```text
m = (2, 3, 2).
```

If each counted occurrence is assigned the same signed value `s_i`, then the Born-weighted record sum across the outcome distribution is

```text
Σ_i q_i m_i s_i = 1/5,
Σ_i q_i m_i     = 12/5,
(Σ_i q_i m_i s_i)/(Σ_i q_i m_i) = 1/12.
```

Both differ from the original `Σq_i s_i=0`. The normalized expression is a **size-biased record-sampling distribution**: it samples from a pooled ensemble of hypothetical record occurrences. It is not automatically an observer's locally accessible experience, and it is not the signed value of one actual branch. Counting the activated flag as a subject or experience is precisely the hypothesis being tested, not an established fact. This example is distinct from section 3: there the two copies were given opposite signed roles; here all counted occurrences are assigned the same sign. Those are competing rules, not two simultaneous conclusions.

For arbitrary multiplicities, zero along this one chosen axis is equivalent to

```text
−m₀ + 8m₁ − 7m₂ = 0.
```

Uniform multiplicity is sufficient, but not necessary: `(9,2,1)` also balances this one axis. By contrast, because the three directions are non-collinear and their unique linear dependence is the positive `q` relation, requiring the **vector** balance `Σq_i m_i n_i=0` forces `m₀=m₁=m₂`. This distinguishes a one-component cancellation from full directional balance. Neither criterion determines actual subject incidence.

The local density matrix of `R` is identical before and after adding the selective flag, as is that of `M`; their individual record probabilities do not change. Their **joint** reduced state does change: the selective flag removes coherence between flagged and unflagged sectors. Thus this is not a claim that the entire physical situation is unchanged, nor that a distant choice signals. The gate is a stipulated interaction controlled by `R`; its spacetime localization is not modeled.

The prior [local incidence/current construction](ZERO_LOCAL_INCIDENCE_QUANTUM_CURRENT_CONSTRUCTION.md) obtains cancellation under an independently imposed local budget and compatibility assumptions. It could inform an alternative allocation here, but it does not prove that the flag, pointer or memory has a particular experiential weight. Avoid using reciprocal multiplicity merely to force the desired zero.

## 6. Necessary records and weights

The formal Born weights in this example are rational: a 40-record block with counts `(5,16,19)` matches `q`. Many different ordered blocks have those same counts, so those weights alone do not identify a complete record history. That is a logical distinction, not an assertion that all such blocks are genuinely possible worlds, a physical selection mechanism, or a derivation of empirical frequency. Relational ordering rather than a fundamental external time would be required in a completed theory.

Under the user's proposal, a complete actual history may itself be necessary; if so, its actual records are not irreducibly open chance in that sense. The Born weights still need a justified relation to the incidence of observers and observed frequencies. A normalized pointer density matrix or one matching finite block does not supply that relation. Bell/contextual and no-signalling constraints from the earlier work remain applicable.

## What this establishes

The integrated model now supports **zero-preserving measurement, redundant records, an ideal storage gap, a directional causal distinction and a branchwise signed-zero candidate** in the same stipulated quantum system. It gives a substantive target for the next constitutive step: derive, rather than simply choose, the subject criterion, the causal-role-to-felt-quality identity, and the actual incidence measure. It does not show that zero itself entails the spins, their organization, the signed rule, actual experiences, spacetime or an objective global energy zero.

## Verification

```text
python -m unittest verification.zero_sector_memory_incidence_test -v
```

Fourteen standard-library tests check the asymmetric ray values, invariant-sector logical copy permutations and norms, ideal record agreement and reduced-state decoherence, the storage gap and its logical-error limitation, branchwise opposite signed observables and exchange symmetry, directional interventions, record multiplicity, sign reversal and the distinction between weights and record order. Physical-spin-sector invariance uses the encoded singlet bases checked in [the preceding instrument tests](verification/zero_invariant_sphere_instrument_test.py); the new tests operate in those encoded logical spaces. Floating-point comparisons use tolerances. None verifies an experiential identity or empirical memory mechanism.
