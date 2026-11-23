# An autonomous zero-spin record cycle and its subject boundary

## Result in brief

The preceding [conserved-energy record model](ZERO_SECTOR_CONSERVED_ENERGY_RECORD_DYNAMICS.md) used a specified interaction interval to write a memory. This continuation incorporates that same interaction into a **time-independent, closed clock–record Hamiltonian**. A four-phase encoded clock correlates its own states with blank, written, maintained and reset memory states. All blocks remain in physical spin-zero sectors, and each memory–battery pair conserves its bare energy.

This permits a sharper joint test:

- A definite clock condition can correlate with a nonblank record whose three Born weights are the earlier conserved-ray fractions. The complete unitary state nevertheless does not itself select a definite experienced record or a classical sequence of ticks.
- A concrete candidate subject rule—minimal subsystems closed under the writing unitary's bare-energy exchange—selects the two memory–battery pairs. If a subject's signed value is identified with its **net** energy change, each selected pair contributes zero, even during internal transfer. The rule therefore supplies plurality in this model but not the desired nonzero subject-level valence.
- A bounded positive, clock-related incidence operator can make a weighted current sum nonzero over the complete cycle, although the unweighted physical current and each component's net energy change balance. Thus even an autonomous cycle does not make the physical conservation law an actual experiential-incidence law by itself.

These are conditional results about a specified finite quantum model. The cycle is recurrent, not an established biological or experiential self-maintaining system; its physical construction, initial state, subject rule and phenomenal interpretation are not derived from zero.

## 1. One closed Hamiltonian for writing, storage and reset

Retain the previous model's encoded systems: logical `A,B` (four spins each), a three-label pointer `R` (six spins), memories `M₁,M₂` and batteries `W₁,W₂` (four spins each). Its record-writing unitary `U` conserves the positive bare energy

```text
H₀=N_M₁+N_W₁+N_M₂+N_W₂,
[U,H₀]=0,
```

and writes the three labels as memory patterns `(1,0)`, `(0,1)`, `(1,1)`, using energy taken from corresponding initially excited batteries. For the specified logical singlet and conserved-ray POVM, the pointer labels have weights

```text
q=(1/8, 2/5, 19/40).
```

The recording unitary and the identification of those weights remain assumptions as detailed in the earlier report.

Add a six-spin zero-sector clock `C`. Use four of its five orthogonal singlet basis states, labelled `0,1,2,3`; the fifth is unused. The full model thus has **36 physical spins**. On the clock and work space define

```text
V₀=I,      V₁=U,      V₂=U,      V₃=I,
K=Σ_(t=0)^3 |t⟩⟨t|_C ⊗ V_t,
A=Σ_(t=0)^3 (|t+1 mod 4⟩⟨t| + |t⟩⟨t+1 mod 4|),
H=H₀ + g K(A⊗I)K†,       g>0.
```

The four oriented clock links carry, respectively, `U`, `I`, `U†`, `I`; their product around the loop is `I`. All are fixed terms of one **time-independent** Hamiltonian: no outside agent switches the writing interaction on or off. Each `V_t` commutes with `H₀`, so `[H,H₀]=0`. Clock operators and encoded work operators are rotational scalars on their physical singlet sectors, extended appropriately to the full physical space; the initial state and every clock-conditioned branch therefore retain exact physical total spin zero.

This is an exact finite construction, not a demonstration that these many-body terms are spatially local, physically natural, self-generated or uniquely required. `H₀` is positive and equals 2 in the prepared work state; the clock–interaction term is part of the full Hamiltonian. No objective zero of the whole's energy follows from choosing a reference value.

## 2. The clock–record correlations

Let `|φ⟩` be the normalized prior `ABR` post-instrument state together with blank memories and excited batteries. Set the clock initially to `|0⟩`. Write

```text
|h_t⟩ = |t⟩_C ⊗ V_t|φ⟩.
```

The four `|h_t⟩` are orthonormal, and their span is invariant under `H`; there `H₀=2I` and the nontrivial dynamics is the adjacency matrix `gA`. Clock-conditioned work states are

| Clock label | Conditioned work state | Memory status |
|---|---|---|
| 0 | `|φ⟩` | blank |
| 1 | `U|φ⟩` | written |
| 2 | `U|φ⟩` | maintained in the same record state |
| 3 | `|φ⟩` | reset |

In units `g=1`, dropping the common `e^(−2it)` phase, the exact clock amplitudes from `|h₀⟩` are

```text
α₀=cos²t,       α₁=−i sin t cos t,
α₂=−sin²t,      α₃=−i sin t cos t.
```

At `t=π/2` the state is entirely in clock sector 2 and the record is written; at `t=π` it returns to sector 0 and the initial work state. These statements are about the model's mathematical evolution parameter. More intrinsically, **whenever a clock label with nonzero probability is conditioned on**, the corresponding row above gives the work state. The quantum clock can occupy a superposition of labels, is periodic and provides no globally monotonic time. Conditioning does not demonstrate a single actual tick sequence, resolve definite outcomes, or derive spacetime; no preferred cosmic foliation is postulated.

In the written sectors, the memory reads the pointer and has the same three outcome weights `q`. The unconditioned logical state of `B` is `I/2` in both blank and written clock sectors. This is equality of reduced states in the model, not a claim that conditioning on the clock is a freely controllable spacelike operation.

## 3. What energy conservation does for candidate subjects

Within a written clock sector, the expected energy changes from the blank preparation are

```text
ΔE_M₁=+3/5,      ΔE_W₁=−3/5,
ΔE_M₂=+7/8,      ΔE_W₂=−7/8.
```

These are Born-weighted means, not four definite experiences. Each conditional pointer branch also has exact opposite memory–battery changes, as shown in the preceding construction. Across the complete cycle, each block's bare energy returns to its initial value. At every time the two physical current pairs obey the operator identities

```text
J_M₁+J_W₁=0,        J_M₂+J_W₂=0.
```

Here is a **testable candidate**, not a declaration of subjecthood: among the four energy-bearing logical blocks, take a subject to be a nonempty inclusion-minimal subset whose total bare energy is preserved by `U`. Exact enumeration of all 16 subsets gives four energy-closed subsets: the empty set, `{M₁,W₁}`, `{M₂,W₂}`, and all four blocks. The two nonempty minimal sets are the two pairs.

This criterion avoids calling either battery a separate subject merely to cancel a memory, and gives two disjoint minimal energy-closed units in this specific encoding. But if the candidate felt value of each such unit is identified with **its net energy change**, both values are zero throughout: internal transfer makes one member gain what the other loses. The rule does not thereby explain actual nonzero positive or negative experience. Internal current may be nonzero, but identifying one direction or internal relation with a felt sign requires an additional account.

Other hypotheses yield different answers on the same physical model:

- Treat each of the four blocks as a separate subject with valence equal to its energy change: the values are opposite in pairs and sum to zero, but battery subjecthood and the identity are assumed.
- Treat only the two memories as subjects under that identity: their written-sector mean sum is `59/40`, and the compensating physical change is outside the chosen subjects.
- Treat each energy-closed pair as one subject: their net values are `(0,0)` under that identity, although each contains nonzero internal transfers.

This is not a proof that the true subject criterion must be one of these. The minimal-closure rule presupposes the physical block decomposition, energy localization and an operator criterion; it ignores the pointer and clock as candidates. A criterion using causal history, internal organization and felt quality might behave differently. The calculation shows precisely why **energy closure alone is insufficient** to do all those jobs.

## 4. A whole cycle does not automatically fix incidence

There is a stronger issue than merely comparing energy changes at one phase. Set `g=1` and work in the four-dimensional invariant history subspace. Let `P` project onto written clock labels `1,2`, and put

```text
D = i[A,P].
```

Direct calculation gives `D²=I` and

```text
⟨P⟩_t=sin²t,       ⟨D⟩_t=sin(2t).
```

For memory `M_j`, let `p₁=3/5`, `p₂=7/8`. Because the history subspace is invariant under the Hamiltonian, compressing the memory current to this subspace gives `p_j D`; the associated battery current compresses to `−p_j D`. Thus each component's **unweighted** expected current integrates to zero over `t∈[0,π]`.

Now consider a conditional incidence operator on this history subspace

```text
W = I + λD,      0<λ<1.
```

It is strictly positive, with eigenvalues `1±λ`; `W/2` is a valid effect. It can be extended to the larger clock–work space by conjugating the clock operator with the same `K`; it is generally a **joint clock–work operator**, not established as an observer-local subject property. In this history subspace it commutes with the compressed current. The symmetrically weighted memory contribution is

```text
½{W,p_j D} = p_j(D+λI).
```

If the battery receives weight `I` instead, the weighted pair contribution is `λp_j I`, and its expectation integrates over a full cycle to

```text
∫₀^π ⟨½{W,J_Mj}+J_Wj⟩ dt = λp_j π ≠ 0.
```

This is an exact mathematical counterexample to the inference from *physical cyclic conservation alone* to *zero under arbitrary positive incidence weighting*. The result depends on a deliberately specified, unequal weighting rule. Its global extension and the full uncompressed currents need not commute, so a complete operational joint-incidence measurement is not asserted. Moreover, this is an expectation of a weighted quantum operator, **not** automatically an actual subject-weighted experiential sum. The constant term comes from current–weight correlations: in general `⟨WJ⟩≠⟨W⟩⟨J⟩`.

If the **same** `W` is applied to both ends, their weighted operator contributions still cancel exactly. A theory could instead supply a justified common local budget or another incidence mechanism; merely choosing weights to force cancellation would be circular. A nonzero formal counterexample does not disprove the user's stronger zero constitution.

## 5. Necessity, frequencies and what remains to be derived

The unitary history contains correlations between clock, pointer, memory and batteries. It does not by itself give actual subject boundaries, selected records or felt qualities. A globally necessary complete history could contain definite records without irreducibly open chance in the user's sense, but that necessity is not derived by the clock Hamiltonian. The conserved-ray fractions are Born probabilities in the stipulated quantum state. They do not alone fix a complete ordered sequence or establish actual observer incidence: even 40-record blocks with counts `(5,16,19)` can have different orders. Such formal alternatives are not asserted to be genuinely possible complete worlds.

The next constitutive demand is therefore sharper than simply constructing a longer cycle: explain why zero's own constitution entails a physically meaningful subsystem/subject rule, how actual causal organization has its specific felt character, and why the **actual** incidence of those subjects satisfies a whole-level zero. The example also exposes the physical requirements: an autonomous clock and its many-body interactions are specified rather than derived, the cycle is reversible and periodic, and the pre-existing record instrument was prepared by assumption. It does not yet supply robust self-repair, empirically grounded consciousness, spacetime emergence, a real cosmological energy zero or a non-circular experiential identity.

## Verification

```text
python -m unittest verification.zero_autonomous_clock_record_subject_test -v
```

Twelve standard-library tests check the actual encoded writing unitary and cyclic clock–work propagation, the Schrödinger amplitudes and clock-conditioned record, conserved bare energy and recurrent currents, positive incidence and its nonzero weighted-cycle control, enumeration of minimal energy-closed subsets, and the distinction between weights and record order. The physical spin-zero encoding and detailed prior writing Hamiltonian are verified by the preceding instrument and energy-exchange tests. These finite checks do not establish selected experiences or empirical phenomenology.
