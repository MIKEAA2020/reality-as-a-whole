# A finite reservoir and reusable memory inside the sphere history

**Result.** I extended the actual internal-reference history with three independently prepared source pairs, a reusable working memory, three finite initially thermal reservoir bits, an explicit finite energy store and a cyclic relational clock. A gauge-compatible interface makes each source/reference pair carry the old conserved sphere sign. The model has an exact zero *added signed-energy constraint* at every clock reading and a separate stationary clock constraint.

In the forward segment the reservoir stores the three source readings with success probabilities **1, 3/4, 3/4**. The first memory is initially perfectly blank; later resets leave a thermal error probability 1/4. The reservoir gains `3ε/4` of energy, the working memory gains `ε/4`, and the energy store loses `ε`. The entire sequence then reverses and restores the original state and preparations. This is a concrete local arrow and resource ledger, not an irreversible whole, a derivation of consciousness, or proof of objective cosmic energy zero.

The construction is an extension of [the previous reusable-memory clock](ZERO_RELATIONAL_CLOCK_REUSABLE_MEMORY_RESOURCE.md), not a replacement for its original physical input. [The verifier](verification/zero_clock_finite_reservoir_reuse_test.py) checks all 16 old clock histories and the complete finite clock/battery dynamics.

## 1. Add independent sources—and actually connect them to the sphere

Start with the existing valid post-sign-gate state, including the sign pointer M. Its old sphere B has eigenvalues ±1 with Born weight 1/2 each. For each `i=0,1,2`, add a degenerate source qubit `Sᵢ` and a reference `Fᵢ`, initially in the independently prepared pure pair

```text
(|0⟩_Sᵢ|0⟩_Fᵢ + |1⟩_Sᵢ|1⟩_Fᵢ)/√2.
```

The reference values xᵢ are independent uniform bits in the computational readout basis. These are stipulated source preparations; uniform Born statistics are not a claim of irreducible objective chance or an inference about actual subject incidence.

Apply a unitary that flips each Sᵢ if `B=−1`, and leaves each Fᵢ alone. Let `β=0` for B=+ and `β=1` for B=−. The source labels after this interface are

```text
yᵢ = xᵢ XOR β,          Z_Sᵢ Z_Fᵢ = B.
```

Thus each *joint source/reference relation* records B. The source readings y are still independent unbiased bits and, by themselves, reveal no B. This connects the source apparatus to the actual sphere rather than simply attaching an unrelated example. B is a gauge-invariant control and the interface preserves the checked old clock/work constraints.

There is a real disturbance: the two source/reference states associated with B=± are orthogonal. If the source pairs are traced out after this interface, the complete old post-sign-gate state is dephased between its two B sectors. For every one of the 16 old histories, its fidelity with the original pure old state is **1/2**, and the trace distance is **1/2**. The old B and diagonal record statistics are unchanged, but the original full old marginal is **not** preserved. The closing inverse interface restores it when the whole program is reversed. No inhabitant is assumed able to access the source references merely because they occur in the global model.

## 2. A finite memory, Gibbs reservoir and internal energy store

Add:

- a working bit A, initially `|0⟩`, with gap ε>0;
- three reservoir bits Rᵢ, each with the same gap ε and initial excited-state probability `q=1/4`, so `βε=ln 3` for their *initial reduced Gibbs states*;
- purifiers Pᵢ, each correlated with its Rᵢ as `√(3/4)|0,0⟩+√(1/4)|1,1⟩`;
- a seven-level energy store with levels `n=0,…,6`, gap ε, initially n=3.

The reservoir bits are finite systems, initially thermal only as reduced states; their purifiers are part of the whole. They are not an infinite heat bath held forever at temperature T. The source pairs, thermal correlations, working blank and battery level are explicit low-entropy/preparation resources, not things derived from zero.

The source-controlled write is a genuine **energy-conserving unitary**: when yᵢ=1 it exchanges

```text
|A=0,n⟩  ↔  |A=1,n−1⟩,     n=1,…,6,
```

and fixes the two unpaired endpoint states. For yᵢ=0 it does nothing. It preserves `ε(n+A)` on every input, including battery endpoints. On the actual three-source forward episode, no required write hits a blocking endpoint. A subsequent swap of A with Rᵢ preserves their combined energy because their gaps agree. The sources are degenerate in this model; a physical implementation of that assumption is not supplied.

To make the cancellation explicit, assign purifier Pᵢ the signed contribution `−ε Nᵢ` where `Nᵢ=0,1` is its occupation, and define

```text
E_added/ε = (n−3) + A + Σᵢ (Rᵢ−Pᵢ).
```

Every component of the prepared state has `Rᵢ=Pᵢ`, A=0 and n=3, so `E_added=0`. Every interface, write and swap preserves it, including on the return. This is a **specified bounded finite signed charge**: the negative purifier spectrum, battery offset and initial balancing correlation are modeling inputs. It is not a proof that an independently defined physical energy of the actual universe is zero, that gravity supplies these purifiers, or that signed experience is energy.

## 3. The whole clock history

A 14-state clock C controls the following sequence:

```text
forward: sphere–source interface,
         write y₀, swap A/R₀, write y₁, swap A/R₁, write y₂, swap A/R₂;
return:  the same seven unitary gates in reverse order.
```

Let Vₜ be the gate at tick t, and define `D=Σₜ |t+1 mod 14⟩⟨t|⊗Vₜ`. Each gate is an involution, so the full circuit is identity and `D¹⁴=I`. The normalized history `|H⟩=(1/√14)Σₜ|t⟩Uₜ|input⟩` satisfies

```text
D|H⟩=|H⟩,       (2I−D−D†)|H⟩=0,       E_added|H⟩=0.
```

D also commutes with `E_added`; its steps preserve the old gauge and the checked old constraints. Clock readings are uniform conditional labels, not a prescribed external time or a fundamental spacetime foliation. The clock, its generator and all couplings are still constructed inputs. In particular, the clock constraint and the added signed charge should not be silently identified with general relativity's Hamiltonian or an established whole-energy observable.

## 4. Forward record and energy ledger

At each write the source yᵢ is unchanged. After each following swap, the initially thermal Rᵢ retains the working-bit record and A takes the old thermal state of Rᵢ. On the specified coherent state, reading the corresponding computational registers would give

```text
R₀=y₀;        R₁=y₁ XOR P₀;        R₂=y₂ XOR P₁;
A_final=P₂.
```

The P labels refer to the initial reservoir purifications and have probability `P(Pᵢ=1)=1/4`. These equations describe quantum correlations; they are not a claim that an unobserved classical trajectory has been selected. The source records are independent uniform **in their readout statistics**, even though the full source/reference/sphere state is correlated.

| Stage | Optimal source-record success from its R bit | Mean store n | Mean A occupation | Mean total R occupation |
|---|---:|---:|---:|---:|
| initial | — | 3 | 0 | 3/4 |
| after first swap | 1 | 5/2 | 1/4 | 1 |
| after second swap | 3/4 | 9/4 | 1/4 | 5/4 |
| after third swap | 3/4 | 2 | 1/4 | 3/2 |
| after full reversal | no source record | 3 | 0 | 3/4 |

At the midpoint all three R bits jointly identify the full source triple with optimal tape-only probability **9/16**. Their reduced state is maximally mixed. With three initially pure blank R bits instead (`q=0`, a separate zero-temperature-limit preparation, not the thermal run), the same gates retain the full triple perfectly; the store's final mean level is 3/2.

There is a sharper access distinction. R₀ alone is statistically independent of the old B, even though it perfectly records y₀. A joint readout of R₀ and its source reference F₀ recovers B with probability 1; corresponding R₁/F₁ and R₂/F₂ readouts succeed with probability 3/4. The additional reference interface is essential; the sphere inhabitant is not automatically given it.

A two-qubit tape cannot perfectly recover three independent unbiased source bits without side information: for any encoding and POVM its full-label success is at most `4/8=1/2`. This differs from the earlier correlated six-label source, whose two-qubit optimum was 3/4. Access to the original source, a reference, battery or other side information changes these bounds.

## 5. Energy, entropy and the actual meaning of “heat”

Measure energies relative to the explicitly chosen initial level, in units of ε. From the initial state to the forward midpoint,

```text
ΔE_store = −1,        ΔE_A = +1/4,        ΔE_R = +3/4,
ΔE_store + ΔE_A + ΔE_R = 0.
```

The purifiers' signed energies are unchanged. Each initially thermal Rᵢ receives mean energy `Qᵢ=ε/4`; this is the explicitly defined energy gain of that finite reservoir bit, not a claim that an infinite bath stays at fixed temperature. The energy store is internal, and all gates commute with the defined charge. But its final energy is distributed over levels 0–5 and its reduced entropy rises to about **2.119 bits**. Its average energy loss is therefore not automatically fully usable thermodynamic work: correlations and energy quality matter.

Each A–R swap begins with A uniformly distributed and a fresh Rᵢ in the Gibbs state q=1/4. A's local entropy drops from 1 bit to `h₂(1/4)≈0.8113` bits. With natural-log entropies, the exact finite-reservoir identity here is

```text
βQᵢ = (ln 2 − h(1/4)) + D(I/2 || diag(3/4,1/4))
     = (ln 2 − h(1/4)) + (1/2) ln(4/3)
     = (1/4) ln 3.
```

The reset does not make A pure: its error is 1/4. The local A/R reduced input is a product for each fresh swap, although the thermal R bit is correlated with its purifier in the larger pure whole. The three-bit R entropy increases from `3h₂(1/4)≈2.434` bits to 3 bits. These are reduced-state and energy-transfer statements, not an increase of the global fine-grained entropy, which remains zero for the pure conditional whole.

The reservoir is finite and has been used: after the forward episode its R marginal is maximally mixed, not the initial q=1/4 preparation. It is also correlated with sources, references and the energy store. One cannot call it a freshly thermal, uncorrelated reservoir again without an additional re-preparation process and its resources. After the programmed inverse, the correlations, initial Gibbs marginals, working blank, battery level and old sphere state are all restored; intermediate local entropy and energy gains are reversed. No indefinite arrow follows from this finite cycle.

## 6. Comparison and what it establishes

- **Uncompute using the source:** apply each energy-conserving write twice. A and the battery return to their starting states, but no durable record remains.
- **Retain with pristine blanks:** swap into three pure prepared bits. All three independent source labels remain recoverable, at the cost of consuming their prepared blank state and transferring energy from the finite store.
- **Reset into finite initial Gibbs bits:** A is reusable only approximately, the retained later records are noisy, the R bits' energy and entropy rise, and the battery loses energy and becomes mixed/correlated.

These are unitary alternatives in one specified finite model. A restricted subsystem with access only to its records could describe the forward segment as an irreversible-seeming history; the whole retains the purifiers and inverse operations. The model supplies an explicit mechanism for that distinction, not an actual subjective experience or a demonstration that the full universe follows the finite program.

The earlier reference-spin exchange combined with a flip of the old sign pointer still pairs s=± at each B value: the new gates act on B only as a conserved control and do not use the sign pointer. On the modeled input each s,b pair has weight 1/4. If those Born weights are *also* taken as the measure of distinct actual incidences, the prior `κ s b` assignment has zero signed mean at every tick. This does not follow merely from `E_added=0`, nor does the arithmetic establish an experiential bridge, physical time reversal or cancellation of local suffering.

It also locates the remaining constitutive demand precisely. The old sphere/source interface, degenerate sources, independent entangled pairs, energy gaps, thermal purifications, negative signed terms, blank memory, store level, clock and its ordering are not consequences of bare zero. A self-sufficient framework would have to account for these structures and for the choice of admissible physical and experiential interfaces, rather than accept them as unexplained residue. Nothing here refutes the user's proposal that zero's own constitution can do so; this test makes the required derivation more concrete.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps \
 python -m unittest verification.zero_clock_finite_reservoir_reuse_test -v
```

Eight tests check the finite-battery unitary and energy conservation, actual sphere interface and old-state disturbance across all 16 histories, stationary 14-tick constraint and signed-charge balance, pristine and uncompute controls, finite-reservoir fidelity and sphere access, entropy and energy ledger, reversal, and the two-qubit dimension bound. They do not derive global physical energy, physical time reversal, an actual subject, felt valence or necessary plenitude.
