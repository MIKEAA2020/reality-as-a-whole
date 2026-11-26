# Transporting echo-mode instruments through the clocked history

## Result

The [previous pass](ZERO_ECHO_CONSTITUTIVE_MODES_AND_COHERENCE.md) found two constitutive sign modes on the same echo: `S=(N+K)/2` and `T=(N−K)/2`. Here their **effects and ideal instruments**, not only their numerical labels, are transported through the echo and its 20-step cyclic clock.

A fixed anchor question can be represented at every checkpoint by a transported projector. Its probabilities and conditional Lüders states agree when the complete physical transformation is applied. A superficially similar question using the instantaneous S operator at every checkpoint is **not** the same question: its probabilities change, and the corresponding reduced clock effect is not invariant.

On a finite representation of the existing `B,J,R` record algebra, the transported coarse and refined projectors can be assembled into clock-invariant Lüders instruments and written into a distinct-ready pointer without breaking the stationary constraint. These are explicitly supplied global operations, not a derivation of locality, autonomous control, energy cost, an experiencer or access by one. The tests also check the transported conditional vectors against selected actual complex echo branches; the reduced clock calculation does not simulate the full purified apparatus. [Code](verification/zero_echo_mode_clock_transport.py), [tests](verification/zero_echo_mode_clock_transport_test.py).

## 1. Anchor modes and the difference between transport and replacement

At the post-echo anchor, with sign-pointer slice `M=s=±1`, let

```text
N=sJ,     K=sJR,     S=sJ(1+R)/2,     T=sJ(1−R)/2.
```

The binary record operators B, J and R commute. We follow the actual T–Q–T gates from the prior echo, writing the **gate** as `𝒯` to distinguish it from mode T:

```text
𝒯:  (B,J,R) → (B,J,JR),
 Q:  (B,J,R) → (B,BJ,R)       on the specified valid physical sector.
```

Both transformations are invertible there. The full implementation uses the old Q's declared unitary extension off that sector. Four checkpoints `c=0,1,2,3` are immediately before 𝒯, after 𝒯, after Q, and after the final 𝒯. The remaining circuit maps the current record values to the **same fixed anchor** values as follows:

| Current checkpoint c | Anchor J in current variables | Anchor R in current variables |
|---:|---:|---:|
| 0 | BJ | BR |
| 1 | BJ | BJR |
| 2 | J | JR |
| 3 | J | R |

These identities are obtained by conjugating the anchor effects through the gates, not by assuming that the same bare observable at different times has the same meaning. In particular, at c=0 the anchor event `S=0`, equivalent to anchor `R=−1`, is represented by `(I−BR)/2`. On the stipulated ready state `R=+1`, it is exactly `B=−1`. The **instantaneous** initial S, however, has R=+1 and is never zero. Knowing the future protocol and measuring the relevant earlier correlation is not retrocausation; an actual earlier measurement can disturb the state and must be included as an intervention.

The table is a Heisenberg transport identity for the declared gates and sector. It does not identify B or the transported event with a subjective report, and a different protocol would have different transported effects.

## 2. The actual complex vectors and the instruments

At anchor let `P_o` be either the three projectors for `S=−1,0,+1`, or the four joint projectors for the nonzero `(S,T)` pairs. Let `U_(c→3)` be the specified unitary taking checkpoint c to the anchor. The transported projectors and Lüders operations are

```text
P_o(c) = U_(c→3)† P_o U_(c→3),
ρ → P_o(c) ρ P_o(c)             [unconditional outcome branch].
```

Consequently, after evolving the branch to the anchor, its unnormalized conditional state is exactly `P_o U_(c→3)ρU_(c→3)† P_o`. This is stronger than equality of a single probability. It holds for arbitrary valid inputs under the stated unitary transport; the supporting test checks complex state vectors from original source labels 0 and 15, both signs, forward and return checkpoints 7–13, and coherent combinations of the actual bin branches. It compares the transported coarse `S=0` and refined `(S,T)=(0,+1)` conditional **vectors** with separately built B/J/R projectors. The test does not establish that the combined branches, transport or measurement is locally available to a subject.

For comparison, on the original positive-pointer sign slice the probabilities of an **instantaneous** unscaled `S=0` query are

```text
checkpoint:             0       1       2       3
P(instantaneous S=0):   0      1/4     1/4     1/2.
```

For the consistently transported anchor event the probability is `1/2` at every one of these checkpoints. There is no contradiction: one sequence changes the question while the other transports the same anchor question. The original signs and gates, including their physical unitary action, account for both.

## 3. A complete reduced 20-step clock instrument

Represent the commuting record algebra on the eight logical basis labels `(B,J,R)`, with the actual record actions above. This representation retains the echo's record transitions but not all old-system phases, angular factors, source references or the purified reservoir. Let `F_t` be the record evolution to clock reading t, with `F_20=I`; the six nontrivial transitions are `𝒯,Q,𝒯,𝒯,Q,𝒯` over ticks 7→13. Construct

```text
W = Σ_(t=0)^19 |t+1 mod 20⟩⟨t| ⊗ F_(t+1) F_t†.
```

In this reduced model `W²⁰=I`. For an anchor-10 projector `P_o`, the unnormalized clock twirl of the **single** anchor effect is

```text
Π_o = Σ_(k=0)^19 W^k (|10⟩⟨10|⊗P_o) W^(−k)
    = Σ_t |t⟩⟨t|⊗ F_t F_10† P_o F_10 F_t†.
```

There is no missing factor of 20: a single anchor is carried to each clock block once. For either the three coarse or four refined outcomes, the `Π_o` are orthogonal projectors summing to I and commute with W. Therefore the ideal operations `ρ→Π_oρΠ_o` preserve the W=1 subspace outcome by outcome. A bare anchor effect `|10⟩⟨10|⊗P_o` does not commute with W; nor does the clock-diagonal effect formed by placing the **same instantaneous** `P_o` at every clock reading. The tests check the complete reduced matrices and the cyclic twirl, rather than inferring stationarity from a state-specific numerical equality.

This is an invariant **global relational measurement**, not a demonstrated clock-local laboratory switch. Its action uses clock-conditioned effects and is not automatically spatially local, energetically free, or accessible within a proposed subject. A clock/time-record protocol with a physically localized write has additional control and retention requirements.

## 4. A ready-pointer realization and coherence cost

For the m projectors `Π_o`, introduce a memory with m+1 orthogonal states: a distinct `|ready⟩` and one `|o⟩` per outcome. Let `V_o` swap `|ready⟩` and `|o⟩`, and set

```text
U_write = Σ_o Π_o ⊗ V_o.
```

Because the Πs are mutually orthogonal and complete, `U_write` is unitary. Because they commute with W, it commutes with `W⊗I_memory`. On a ready pointer it writes the outcome coherently and preserves the joint W=1 constraint. The test constructs this unitary explicitly for both instruments and checks its action on a stationary history. Distinct ready and output states let one tell that a write occurred; they do not make the pointer irreversible or permanent.

Use the reduced representative of the original positive-sign branch: the two distinct negative-B records each have weight `1/4`, while the shared positive-B mode has weight `1/2`. For the uniform stationary history built from this state, the outcome probabilities are the same as in the anchor calculation. After writing and tracing out the memory, fidelity with the original pure history is

```text
coarse S write:               1/2,
refined (S,T) write:          3/8.
```

The extra loss in the refined instrument is the cost, for this specified state and ideal instrument, of resolving more than S. It is not a universal lower bound on all possible instruments or an energy-cost calculation. The finite representative merges the two identical positive-mode record categories into one normalized vector; it reproduces the stated record probabilities, not the full angular/phase apparatus state. The separate full-vector checks above anchor the transported effects to actual echo branches.

A **separate sharp measurement of the 20 clock readings** dephases their mutually orthogonal history components. In this example its nonselective output has fidelity `1/20` with the original pure history. If combined with the corresponding transported mode measurement, fidelities are `1/40` for coarse and `3/160` for refined. The dephased state is invariant under `ρ→WρW†`, because W permutes its clock blocks, but it is not fully supported on the **W=1 constraint subspace**: its weight there is only `1/20`. Invariance under conjugation must not be confused with satisfying the state constraint. These figures concern the declared cyclic history and sharp instruments, not every operational way of reading time.

## 5. Why-chain and remaining work

1. **Why do the anchor results persist across clocks?** A unitary carries the *whole effect and its Lüders map* with the history. The invariance is an internal relation of the declared circuit, not an external agent forcing equal numbers.
2. **Why do bare instantaneous results differ?** They ask about different checkpoint observables. Holding a formula fixed while changing the physical slice is an active change of target, not automatically a passive clock transformation.
3. **Why can a stationary readout still disturb?** A constraint-preserving unitary can entangle the history with a pointer; discarding the pointer loses coherence. The clock-invariant mode write and a sharp clock read have distinct operational and constraint consequences.
4. **Why is this not yet a subject or experience?** These are physical record effects and a mathematically specified pointer. The reporter's correspondence to a subject, the phenomenal meaning of S and T, the accessibility of the global operation, joint reference calibration and the actual occurrence measure remain unestablished. A zero scalar is not absence of experience, and balanced model values do not erase real negative experience.
5. **Why this clock, record algebra and admissible instrument?** The construction answers within the stated echo; it does not derive the complete physical–experiential constitution of the self-sufficient whole. Continue seeking an internal identity of those ingredients rather than an external coercer, while preserving genuinely plural or overlapping subjects.

Next, extend the global reduced-clock instrument to the **full** source, pair and purified apparatus or derive a controlled obstruction to such an extension; quantify the resources and recoverability of a clock-local write, and relate any actual accessible effect to the earlier joint quality/ownership calibration conditions.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_echo_mode_clock_transport_test -v
```

Tests cover the exact finite record logic, complete reduced clock PVM and twirl, a distinct-ready global pointer write, time-dephasing controls, and transported conditional vectors on selected actual complex echo branches. They do not establish a full apparatus realization, subjective reports or foundational necessity.
