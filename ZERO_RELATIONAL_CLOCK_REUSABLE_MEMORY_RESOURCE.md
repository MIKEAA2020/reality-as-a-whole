# A reusable memory inside one constrained clock history

**Result.** Starting from each of the actual 16 internal-reference histories, I added a finite clock, one reusable working bit and three initially blank tape bits. The resulting 12-tick cyclic history is an exact stationary state of a specified constraint, and its gates preserve the previous dressed gauge and checked clock/work constraints. The memory records the existing disturbed-record sign z, conserved sphere sign b and pointer sign s; it later uncomputes those records and returns all auxiliary memory to blank.

At the midpoint the tape stores all three signs perfectly. Their actual joint Born distribution has **six** supported outcomes and entropy **2.5 bits**. Two tape qubits cannot identify all six labels perfectly: even with arbitrary quantum encoding and measurement, the best full-label success is **3/4**, provided the decoder has no other side information. Three qubits suffice. The complete reversible history then removes the tape records by using the unchanged sources; it does not destroy the information from the whole, establish a heat cost, or create an irreversible universal arrow.

This is a concrete extension of the [internal-reference gate](ZERO_INTERNAL_CONTEXTUAL_REFERENCE_AND_RECORD_TRADEOFF.md), motivated by [Bryan and Medved's causality and clock proposal](BRYAN_MEDVED_PROBLEM_OF_TIME_CAUSALITY_AND_ZERO.md). It is not an identification of a quantum register with a subject. The exact checks are in [the verifier](verification/zero_relational_clock_reusable_memory_test.py).

## 1. Input: the actual signs, not three invented independent events

First apply the existing valid-sector sign gate W to any one of the 16 old relative-clock histories. Let z=±1 denote the current physical j-record sign, b=±1 the conserved sphere sign B, and s=±1 the written sign-pointer M value. These three observables commute with each other and the stipulated dressed gauge. Summing over Alice's record, the actual post-W Born distribution is

| z | b | each s | joint weight for each s |
|---:|---:|---:|---:|
| + | + | + or − | 1/4 |
| + | − | + or − | 1/8 |
| − | − | + or − | 1/8 |

All other z,b pairs have zero weight. The verifier constructs these probabilities from the original quantum vectors for **every** old clock label, and verifies the old constraints and dressed gauge on the projected components. Here s is independent of the pair b,z, while z and b are correlated. These are three different *readouts of one previously prepared state*, not three independent new events or three independent bits of entropy. Born weights are not assumed to be the actual measure of subjects.

## 2. The closed relational-clock extension

Add an auxiliary 12-state clock `C`, one working qubit A and a three-qubit tape `T₀,T₁,T₂`, all memory initially in `|0⟩`. The old sign pointer M is retained; it is not the new working bit A. On each source, define a controlled NOT onto A using its sign: z controls the first copy, b the second, s the third. Alternate these copies with swaps between A and the corresponding fresh tape slot:

```text
forward operations:  copy z, swap A/T₀, copy b, swap A/T₁, copy s, swap A/T₂
return operations:   the same six gates in reverse order.
```

Each gate is its own inverse. The forward and return products therefore compose to identity on the **entire** extended source/memory space, not just on the prepared state. The source signs are not changed by these gates. The z and b controls commute with the old gauge and checked constraints; the pointer s, A and tape are neutral on the old factors. The verifier checks these commutators and the whole gate permutation, including all source-sign and memory-basis inputs.

Make the clock part of the model rather than drive the circuit from outside. For `t=0,…,11`, let `V_t` be the listed operation, and define the unitary

```text
D = Σ_t |t+1 mod 12⟩⟨t|_C ⊗ V_t,
H_clock = 2I − D − D†.
```

For the actual post-W input `|ψ⟩`, with all new memory ready, let `U₀=I` and `U_t=V_{t−1}⋯V₀`. Then

```text
|History⟩ = (1/√12) Σ_t |t⟩_C ⊗ U_t|ψ,0000⟩,
D|History⟩ = |History⟩,       H_clock|History⟩ = 0.
```

Conditioning on a clock label gives the corresponding normalized circuit state; the clock-label weight is 1/12. The old valid-sector constraints and dressed gauge continue to hold, because the new gates commute with them. The verification compresses each **actual** orthogonal `(z,b,s)` sector to a basis label only after checking its physical vector and weight, so it does not replace the old ensemble with a different preparation.

This is an engineered finite cyclic constraint and a chosen clock/factorization, not a derivation of spacetime, a preferred fundamental foliation, a realistic clock or the objective energy of the whole. The clock, its generator, gates, initial blanks and sector selection are inputs. The original W was completed before this added 12-tick episode; the extension is not claimed to have existed in the old history without modification.

## 3. Record reliability and finite resources

The tape state is diagonal in the record basis after the source and other factors are traced out. Thus the classical optimal guessing values below are also optimal for arbitrary POVMs **on the tape alone**, for the binary source labels at the indicated clock reading. A blank tape can still produce a better-than-chance guess of z because z is biased; similarly a stored z gives partial information about b.

| clock reading | A | tape `(T₀,T₁,T₂)` | tape entropy, bits | best tape-only guesses `(z,b,s)` |
|---:|---|---|---:|---|
| 0 | blank | blank | 0 | `(3/4, 1/2, 1/2)` |
| 1 | z | blank | 0 | `(3/4, 1/2, 1/2)` |
| 2 | blank | `(z,0,0)` | 0.8113 | `(1, 3/4, 1/2)` |
| 3 | b | `(z,0,0)` | 0.8113 | `(1, 3/4, 1/2)` |
| 4 | blank | `(z,b,0)` | 1.5 | `(1, 1, 1/2)` |
| 5 | s | `(z,b,0)` | 1.5 | `(1, 1, 1/2)` |
| 6 | blank | `(z,b,s)` | **2.5** | `(1, 1, 1)` |
| 7 | s | `(z,b,0)` | 1.5 | `(1, 1, 1/2)` |
| 8 | blank | `(z,b,0)` | 1.5 | `(1, 1, 1/2)` |
| 9 | b | `(z,0,0)` | 0.8113 | `(1, 3/4, 1/2)` |
| 10 | blank | `(z,0,0)` | 0.8113 | `(1, 3/4, 1/2)` |
| 11 | z | blank | 0 | `(3/4, 1/2, 1/2)` |
| 12 ≡ 0 | blank | blank | 0 | `(3/4, 1/2, 1/2)` |

Here `0.8113` is `h₂(1/4)≈0.811278`. The A and tape entries denote correlations in the corresponding clock-conditioned quantum state, not a claim of collapse into a hidden trajectory. At tick 7, for example, s is no longer in the tape but is still perfectly recoverable from A; at tick 8 it has been coherently uncomputed from A using the still-present original pointer. A subject's access to tape, A, original sources or clock is a separate interface postulate.

The 2.5-bit joint entropy is less than the sum of the three individual tape entropies, `h₂(1/4)+1+1≈2.8113` bits. The difference, about `0.3113` bit, is the z–b correlation. This is the entropy of the **reduced tape** and the classical information it can carry about the chosen labels. It is not the von Neumann entropy of the closed whole, nor necessarily heat, felt experience or a count of subjects.

### A sharp two-qubit limit

The six supported source labels have probabilities `1/4,1/4,1/8,1/8,1/8,1/8`. Suppose a decoder gets only a two-qubit tape, with no source register, clock side channel beyond the known tick, or additional memory. Even allowing any four-dimensional quantum encoding and any POVM `{E_i}`,

```text
P(correct) = Σ_i p_i Tr(ρ_i E_i) ≤ sum of the four largest p_i = 3/4.
```

Indeed `Tr(ρ_i E_i)≤min(1,Tr E_i)` and `Σ_i Tr E_i=4`; maximizing these bounded terms gives the four largest priors. Four orthogonal codewords assigned to the four most probable labels attain the bound. This is a single-shot statement about identifying the *complete triple*. It does not contradict perfect recovery of a particular sign, use of the original sources as side information, or approximate/collective asymptotic compression. Perfectly encoding six alternatives needs dimension at least six, so two qubits are insufficient and three are enough.

## 4. The arrow and the meaning of reset

The forward half increasingly deposits records in the tape; the second half reverses them. The working bit is blank after each forward swap, but this is not an information-free reset: the tape has retained the corresponding record. Later, the controlled inverse clears A only because the relevant original source is still present. At the end all auxiliary memories are blank and the source information remains in the old system. Total unitary information has not been destroyed.

This gives an explicit local record-building direction **within a chosen segment**, followed by its exact reversal. The programmed 12-tick cycle cannot have strictly increasing tape entropy around the whole loop. It does not prove that an emergent macroscopic arrow is impossible: a longer-lived arrow could require different boundary conditions, many independent source events, discarded environmental degrees of freedom, or a thermodynamic reservoir. None is derived here. In particular, nothing in this circuit supplies a temperature, heat-flow calculation or unlimited supply of blank memory. Resetting A via a clean tape slot transfers the resource demand; it does not by itself prove a Landauer heat payment.

## 5. Mirror symmetry survives the actual memory history

There is also a direct connection to the whole-zero programme. At the input, the old reference-spin exchange combined with flipping the sign pointer maps s to −s while leaving b,z fixed; the actual branch vectors transform into their counterparts up to a common phase. Let `K₀` be that involution, and transport it through the program:

```text
K_t = U_t K₀ U_t†,      K = Σ_t |t⟩⟨t|_C ⊗ K_t.
```

Because the full program closes, K is an involution and **commutes with D**, hence with the new constraint. It maps the stationary constructed history to itself. The transported action is not always just the original sign-pointer flip: after the s copy, it also flips whichever working or tape bit contains the s record. Treating the untransported input symmetry as if it still acted on the written memory would be incorrect. This is a modeled counterpart transformation, not an established physical time-reversal law.

Compare the two prior conditional quality assignments, using the sign stored in `T₀` as r₀:

```text
v_B   = κ s b,          v_T = κ s b r₀.
```

Assuming the same Born-weighted incidence identification as before, both signed means vanish at **every** clock reading. They nevertheless disagree on weight 1/4 at ticks 2 through 10, and agree at ticks 0, 1 and 11 (and after the return), because T₀ is then blank. The counterpart symmetry and cancellation therefore persist through record formation **and its reversal**, but still do not choose the phenomenal bridge. Calling either rule a felt quality, identifying paired branches as actual subject incidences, or equating Born weights with experiential measures remains an additional premise. A positive contribution elsewhere would not erase local suffering.

## 6. Consequence

This construction puts an actual disturbed sphere history, a gauge-compatible sequence of causal interfaces, a finite memory budget, a clock constraint, a reversible return and a transported counterpart in **one** explicit model. It establishes a real quantitative boundary between what the selected tape can and cannot retain. It does not yet supply the dynamical subject boundary or derive the clock, original records, incidence measure, actual experience or physical arrow from zero's own constitution.

A substantive next extension would replace the three already-existing correlated signs with a longer stream of genuinely new source interactions inside the constraint, and compare a finite tape with a separately modeled reservoir or renewable low-entropy supply. That requires a specified subsystem interface, actual energy/heat accounting and a clock good enough for the relevant interval; it must not smuggle an infinite blank tape or external driver into the proposed closed whole.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps \
 python -m unittest verification.zero_relational_clock_reusable_memory_test -v
```

Seven tests check the source controls and constraints, all 16 physical input histories, the full cyclic shift and stationary constraint, transported counterpart, all 13 displayed conditional resource/readout points, and the two-qubit success bound. They do not establish a conscious subject, actual incidence, universal time arrow or objective whole-energy.
