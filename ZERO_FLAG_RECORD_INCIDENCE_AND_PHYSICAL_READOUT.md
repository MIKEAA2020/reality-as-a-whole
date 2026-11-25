# Zero, flag-record incidence, and a physically reversible readout

This continues [the identity-pair construction](ZERO_IDENTITY_PAIR_PHYSICAL_FLAG_AND_INCIDENCE.md), [the joint incidence/echo analysis](ZERO_JOINT_CONSTITUTION_INCIDENCE_AND_ECHO.md), and [the actual sphere–reservoir program](ZERO_SPHERE_LOCAL_CONSTITUTION_AND_RESERVOIR_ECHO.md). Its executable checks are in [the verifier](verification/zero_flag_record_algebra_echo_test.py).

## Result in brief

**Integrated continuation:** [Internal connections: record algebra, signed balance, and the relational clock](ZERO_INTERNAL_CONNECTIONS_RECORD_BALANCE_AND_CLOCK.md) connects the rule to compatible sequential records, counterpart-selected local signs, the stationary clock, and competing actual reference flags.

A sharp physical flag **does** determine a unique incidence rule for all effects compatible with that flag, if one stipulates that the two incidence types are exactly its two sectors. This is substantially stronger than choosing a free incidence parameter. In the actual echo, the relative weights update by ordinary conditionalization; they are not universally one half after a record is specified. At the midpoint, two existing records jointly identify the flag exactly, although neither the abstract availability of this joint observable nor a newly engineered readout establishes that the original confined inhabitant can access it.

A concrete four-gate extension copies that very joint record into a new neutral memory, then uncomputes it, restoring the original 20-step cycle. Its charge accounting and label dynamics are checked for every permitted input. Coherence is not destroyed globally by copying: it is distributed into correlations. If the copy is discarded, the reduced system is dephased, while a joint dressed witness remains sharp when the memory is retained.

**Scope:** these are conditional results for the specified sphere model. They do not establish that the flag labels subjects, that either sign is felt, that zero by itself selects the flag or the required algebra, or that the extra interface and blank are available to a confined subject. Those missing relations remain part of the proposed constitution, not consequences smuggled in by the calculation.

## 1. Unique incidence on a flag-compatible effect algebra

Let `P_0+P_1=I`, `P_aP_b=δ_ab P_a`, and let `A` be the effects `0≤E≤I` that commute with the two projectors. Let `ρ` be any density operator. Suppose nonnegative type weights `μ_a(E)` obey:

1. **Physical marginal:** `μ_0(E)+μ_1(E)=Tr(ρE)` for every `E` in `A`.
2. **Finite effect additivity:** if `E,F,E+F` are in `A` and `E+F≤I`, then `μ_a(E+F)=μ_a(E)+μ_a(F)`.
3. **Sharp type support:** `μ_a(E)=0` whenever `E≤P_{1-a}`.

Then necessarily, and sufficiently,

`μ_a(E) = Tr(ρ P_a E) = Tr(P_a ρ P_a E)`.

**Proof.** Because `E` commutes with the flags, `E=P_0E+P_1E`; each summand is an effect supported in its flag sector. Additivity and support give `μ_a(E)=μ_a(P_aE)`. The other type has zero weight on `P_aE`, so the physical marginal gives `μ_a(P_aE)=Tr(ρP_aE)`. The displayed formula conversely satisfies all three premises: `P_aE` is positive, and its two contributions sum to `E`. No continuity, finite-dimensional Gleason theorem, or independent choice of an incidence coefficient is needed.

For `Tr(ρE)>0`, the record-conditioned type weight is

`Pr(a | E) = Tr(ρP_aE) / Tr(ρE)`.

The equal flag probabilities in the original state make `Pr(a)=1/2`, **not** `Pr(a|E)=1/2` for every subsequent effect. A record can correlate with the flag. At zero-probability records the ratio is undefined, not assigned by the theorem.

The assumptions do real work. In particular, identifying type with the flag is not the same as deriving subjects from it. The domain restriction is also essential: `Tr(ρP_aE)` need not even be nonnegative for a positive effect that does not commute with `P_a`. For the `|Φ+⟩` source–reference state and the rank-one effect on `( |00⟩−2|11⟩ )/√5`, the naive type-0 expression is `−1/10`. Nor do these restricted weights constitute positive flag-supported blocks summing to the original pure state on **all** quantum effects; the earlier rank-one obstruction and coherence witness still apply.

## 2. Transport through the actual sphere echo

Use `x_0∈{0,1}` for the first reference flag, `b_bit∈{0,1}` for the conserved old sphere sign (`b=(-1)^b_bit`), `z_bit` for current `j` (`z=(-1)^z_bit`), and `s=±1` for the old sign record. The stipulated identification is `x_0=0 → B` type and `x_0=1 → j` type. The original Born law gives equal flag weights and uniform `s` counterparts; the thermal reservoir has `q=1/4`. The actual seven forward operations, echo `TQT`, inverse echo `TQT`, and seven inverse operations make a 20-step cycle.

Every actual gate leaves the reference flag unchanged. If `U_t` is the unitary prefix and `ρ_t=U_tρ_0U_t†`, then for a compatible effect at tick `t`,

`μ_{a,t}(E)=Tr(ρ_t P_a E)=μ_{a,0}(U_t† E U_t)`.

This is Heisenberg transport of the same rule, not an extra assumption that the inaccessible initial flag has been physically measured. The clock-indexed dressed witness `D_t=U_t(X_S X_F)U_t†` remains sharp `+1` in the full coherent state, anticommutes with `Z_F`, and has expectation zero in the flag-dephased state. For the cycle, the block-diagonal history observable `Σ_t |t⟩⟨t|⊗D_t` commutes with the cyclic clock shift. This follows for the actual cycle algebraically because its composed unitary is the identity; the verifier explicitly constructs the analogous cyclic operator for a smaller nontrivial flag-preserving cycle, rather than claiming to have densely built the full sphere clock.

The necessary temporal distinction is important: `TQT` changes current `j` and is then reversed. The hypothesis `v_B=κsb`, `v_j=κs z_current` yields equal positive and negative mass `1/4` for each flag at every tick, and hence zero signed sum separately per type. It does **not** follow that an individual `j`-candidate's sign remains constant: relative to its initial `sj`, it is reversed at ticks 9–11 on unconditional weight `1/4` (conditional weight `1/2` within the j-flag). The `B` candidate's sign never reverses in this cycle. These are signed candidate assignments, not proof of experiences or the cancellation of suffering.

## 3. Actual record access: a conditional prediction

The calculation uses the actual coarse Born support, three source/reference pairs, `q=1/4` thermal reservoir, and the established clean auxiliary bit. Results are exact fractions; the same values also hold in the checked thermal auxiliary case. `R_0` means the first reservoir memory bit and `r` the fresh echo bit. For the indicated **joint measurement**, the optimal classical guess of the flag is:

| Tick(s) | From `R_0` alone | From `(R_0,r)` | From `(R_0,r,z_current)` |
|---|---:|---:|---:|
| 0–2 | 1/2 | 1/2 | 1/2 |
| 3–7 | 1/2 | 1/2 | 3/4 |
| 8 | 1/2 | 3/4 | 3/4 |
| 9 | 1/2 | 3/4 | 1 |
| 10 | 1/2 | 1 | 1 |
| 11 | 1/2 | 3/4 | 1 |
| 12 | 1/2 | 3/4 | 3/4 |
| 13–17 | 1/2 | 1/2 | 3/4 |
| 18–20 | 1/2 | 1/2 | 1/2 |

At tick 10, on the actual supported inputs, `R_0=y_0=x_0 XOR b_bit` and `r=b_bit`, so **`x_0=R_0 XOR r`**. The four `(R_0,r)` outcomes each have probability `1/4`; each fixes the conditional type with probability one. The sign counterpart remains balanced even within each joint-record outcome. Thus the original flag symmetry and the strongly unequal record-conditioned type weights coexist without contradiction.

These are operational statements about specified commuting joint readouts of an ensemble, not automatically simultaneous hidden histories. In particular, adding `z_current` to the readout requires an additional interface to the current sphere observable. The original surface-confined subject is not assumed to reach the reservoir, echo memory, reference, or all three; the table is not evidence that it does. `R_0` by itself contains no flag information, despite carrying the source bit at the appropriate times. The records are relational to the model's clock and not evidence for an external preferred time.

## 4. An explicit reversible flag record

The tick-10 identity permits a new construction without directly interacting with the reference. Add a **fresh, neutral** memory `L=0` and insert four controlled-NOTs between ticks 10 and 11:

1. `L←L XOR R_0`;
2. `L←L XOR r` — now `L=x_0` on the supported input;
3. `L←L XOR r`;
4. `L←L XOR R_0` — now `L=0` again.

Resume the original program and its inverse. This is a 24-operation cycle with 25 recorded configurations; it returns all tested labels, including `L`, to their initial values. Each controlled-NOT is a unitary, and steps 3–4 are exactly the inverse of steps 1–2, so the insertion is the identity on **every** joint quantum state, not merely on the checked label support. It does not change `R_0` or `r`, touches no old charge register, and `L` is stipulated neutral. Both constructed reservoir charge ledgers therefore remain zero branch by branch; this is not a derivation of zero cosmological energy, a claim that the blank costs nothing, or an implementation of actual cognition. The tests exhaust all source, reservoir, auxiliary, `b` and `z` labels and use the separately verified coherent `T/Q` pulse for the old sphere.

At the moment after step 2, the controlled unitary has the action of a flag copy **on the actual input support**, because the two-record parity equals the flag there. It need not equal a direct flag-controlled NOT on arbitrary off-support states. Retaining `L` allows the copy to be reversed; discarding it does not. Resetting or exporting it would require extra physical assumptions and resources. This record is a newly stipulated access route between two realms, not an implication that the original inhabitant already has it.

## 5. Conditioning versus measurement, exactly

Mathematical conditionalization uses the same coherent `ρ` and the restricted weights above; no operation is performed. A physical record is an interaction. For a neutral ready memory and ideal controlled copy,

`|Ψ⟩|0⟩_L → P_0|Ψ⟩|0⟩_L + P_1|Ψ⟩|1⟩_L`.

The complete system including `L` remains pure. If `D` exchanges the flag sectors and `D|Ψ⟩=|Ψ⟩`, then `D⊗X_L` remains a sharp `+1` witness for the ideal copy. If `L` is traced out, the pre-existing system instead has `Δ_F(ρ)=Σ_a P_aρP_a` and the bare coherence witness has expectation zero. This is a reduced-state change, not global destruction of coherence; retaining the record and applying the inverse restores the original state.

For the actual balanced pure flag state, including any purifying degrees of freedom in the system being compared, `1/2 ||ρ−Δ_F(ρ)||_1 = 1/2`. The optimal single-shot discrimination probability with equal priors is therefore `3/4`. These numbers apply to that full pre-existing pure system, not automatically to an arbitrarily restricted local subsystem or a mixed state from which purifiers have already been omitted. The dressed observable is likewise a **joint** witness; its formal existence does not establish confined access.

## 6. What this advances, and what would finish the constitutive step

The free incidence parameter has been eliminated **conditionally**: the physical marginal plus sharp type support force one rule on every compatible record. The construction also supplies a concrete empirical distinction between global coherence, physical recording and purely mathematical conditioning, and computes a nontrivial joint-record prediction in the preserved sphere history. Neither a global zero sum nor a passive relabeling supplies the hypotheses on its own.

For a genuine no-residue account, the next constitutive task is to obtain, rather than stipulate, (i) the physically relevant flag and its two type meanings, (ii) the subject boundary and felt-quality map including why signed physical counterparts are actual opposite valences, and (iii) why the compatible incidence algebra is the correct self-location domain despite coherent effects outside it. The construction identifies exactly which assignments must be justified together; it does not equate a finite neutral charge ledger with felt-valence balance or claim a no-go theorem against zero's capacity to determine them.
