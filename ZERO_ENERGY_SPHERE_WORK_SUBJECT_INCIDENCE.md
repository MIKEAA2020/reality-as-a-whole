# Energy-balanced sphere, work relation and candidate incidence

## Result

**Directional-balance continuation:** [the encoded sphere–clock–work bridge](ZERO_ENCODED_SPHERE_CLOCK_WORK_DIRECTIONAL_BRIDGE.md) transports this circuit into local three-generator zero sectors and provides an explicitly resourced conditional preparation, without identifying its declared Q with objective cosmic energy.

The requested integration can be made explicit in one finite quantum circuit. It joins the [energy-conserving sphere and relative-clock interface](ZERO_DUAL_PAIR_SPHERE_ENERGY_CONSERVING_INSTRUMENT.md) to the earlier **actual record–work operator** `K=Z_R₁J₁` and a targeted memory M. The four work qubits have nondegenerate local occupation energies; they are not made individually energy-degenerate to obtain the result.

On the specified finite relative-clock window:

* The target memory records h perfectly in this idealized circuit: `h=0` gives M=0 and `h=1` gives M=1, with one bit of mutual information.
* The **record pair alone** and the **work register alone** have the same reduced density matrix for h=0 and h=1. Their *joint* state distinguishes h perfectly. The targeted memory obtains that joint relation through the explicit h interaction; confinement does not grant either component automatic access to the other.
* The previous record-relative and J-probe experiential proposals give opposite signs on the same event `r=+1, M=1`; the event has probability `1/4` conditional on the relative-clock window. Both pair sums vanish under their specified equal-incidence hypothesis. A strictly record-local report cannot reliably reproduce the J-probe assignment in the relevant h comparison.
* Every circuit operation preserves an explicitly declared additive charge Q, and the chosen initial and final states, including the finite relative-clock pointer, lie in its **exact zero eigenspace**. This includes the work qubits' nondegenerate local energies and a compensating clock spectrum. However, Q is a stipulated bookkeeping operator; the time-dependent gates, their controls and interaction energies are not incorporated into a complete autonomous physical Hamiltonian. We cannot therefore conclude that the actual universe's objective total energy is zero.

The circuit uses the same singlet and five-ray weights, but its finite-reference sphere instrument is unsharp. Its full state is **not** the earlier ideal five-ray `|Ψ₀⟩` unchanged; the exact `K` code relation is rebuilt behind the new finite interface. The memory and record bits are physical registers, not established experiencing subjects. No spacelike embedding or preferred foliation is assumed.

Verification: [verification/zero_energy_sphere_work_incidence_test.py](verification/zero_energy_sphere_work_incidence_test.py).

## 1. The complete specified system

Start with the previous energy-conserving sphere circuit: qubits A and B in their singlet, two reference/clock pairs, Alice's three-outcome pointer, Bob's two-outcome pointer, and the joint 16-outcome relative-clock pointer. Its spin and reference/clock contributions are

```text
H_A=P_A,                         H_B=P_B−I,
N_RA−N_CA,                       N_RB−N_CB.
```

Here `P=|1⟩⟨1|` and each N has eigenvalues 0,…,L−1. Add a two-qubit record pair R, four work qubits in the order `(M₁,W₁,M₂,W₂)`, and a target-memory qubit T. The record and target registers have zero assigned charge in this model. Each work qubit, however, has occupation energy 0 or 1:

```text
H_work = n_M₁+n_W₁+n_M₂+n_W₂.
```

The clock paired with Bob's reference has physical energy labels `n+2`, with negative contribution to Q. Thus define

```text
Q = H_A+H_B + N_RA−N_CA + N_RB−(N_CB+2I) + H_work.
```

The initial work state is `|a⟩=|0110⟩`, so `H_work|a⟩=2|a⟩`. The two reference/clock identity pairs contribute 0 and −2, respectively; the spin singlet contributes 0. Therefore the initial state has `Q=0` exactly. The offset is a **specified negative clock-energy resource**, not a derivation of a cosmological energy reference. A model-independent zero cannot be established by adding an arbitrary compensator.

The initial singlet and the earlier three q-values are the same as before. Alice and Bob's finite-reference instrument acts as in the preceding report. Bob's pointer is then coherently copied to the record pair:

```text
Bob pointer + → R₁R₂=01 (r=+1),
Bob pointer − → R₁R₂=10 (r=−1).
```

Copying here means a reversible unitary in a specified basis, not cloning an arbitrary unknown state. Bob's pointer and R are retained as distinct registers. The finite sphere instrument changes the ideal outcome correlations, but the construction below does not rely on their being ideal.

## 2. Actual work exchange and targeted relation

Use the same active work states and exchange as the earlier model:

```text
|a⟩=|0110⟩,    |b⟩=|1001⟩,
P_act=|a⟩⟨a|+|b⟩⟨b|,
G=|a⟩⟨b|+|b⟩⟨a|,
J₁=i[G,n_M₁],      J₂=−J₁.
```

Both active states have work energy 2. G conserves the sum of all four occupation energies and, more specifically, each memory–battery pair's total and the aggregate memory and battery occupations. The r-controlled preparation and `exp(−iπG/4)` give a state with

```text
K=Z_R₁J₁,       K=+1 on the prepared active support,
h=(P_act−K)/2,  h=0 on that support.
```

These are the **actual four-work-qubit G and J₁ operators** from the earlier construction, checked against their two-dimensional active representation. Apply the specified phase operation `exp(iπ Z_M₁/4)`. It produces equal-norm h=0 and h=1 components. This is a chosen preparation, not an outcome selection or a derivation of equal incidence.

The targeted interaction is

```text
U_T(τ)=exp(−iτ h Y_T),
```

with T initially `|0⟩`. h is a projector on the active code and commutes with `H_work`; T has zero assigned charge. Hence this operation, the record copy, work preparation and exchange all preserve Q. At `τ=π/2`:

```text
h=0 → T=0,       h=1 → T=1.
```

At `τ=π/4`, the conditional table is instead

```text
             T=0    T=1
h=0          1/2      0
h=1          1/4    1/4,
```

so `I(h:T)=0.311278` bits. This shows the perfect result is an ideal pulse in a particular finite circuit, not a generic assertion that a memory always records K. The target memory is charge-degenerate and its pulse is prescribed; the model does not calculate a realistic energetic cost, a stable macroscopic record or an autonomous control schedule.

### The J-probe is not automatically the full interaction current

J₁ was defined as the current generated by the **standalone** exchange G. The h–T coupling changes the actual current during the target operation. On the active work basis `(|a⟩,|b⟩)`, `J₁=−Y_W` and `n_M₁=(I−Z_W)/2`. If the target generator is `g h Y_T`, then its contribution is exactly

```text
i[g h Y_T, n_M₁] = (g/2) Z_R₁ X_W Y_T.
```

Thus the sharp J₁ observable used below is a specified probe, not an unqualified identity with the current of the complete interaction. This distinction matters to any experiential rule based on “current.”

## 3. The finite clock and the changed sphere table

Use L=4 references and the same 16-outcome joint relative-clock pointer as in the preceding report. Group its three labels centered on zero; the window has probability `3/16`. The relative-clock measurement and all the newly added operations preserve Q. Their order is prescribed in the circuit; no fully autonomous clock-control mechanism is supplied.

Conditional on the window, the finite-interface distribution of sphere outcome i and record r is

| i | r=+1 | r=−1 |
|---|---:|---:|
| 1 | 0.069174 | 0.055826 |
| 2 | 0.146605 | 0.253395 |
| 3 | 0.284221 | 0.190779 |

The row sums remain `(1/8,2/5,19/40)`; each r has total probability 1/2. The table's total-variation distance from the original ideal table is about `0.093209`. For this construction and the same clock window, L=2,4,8 give distances `0.152537`, `0.093209`, `0.054646`, respectively. These are explicitly finite-reference results, not a universal limit or a measured cosmological probability.

The h preparation is balanced for each i,r in this circuit. At `τ=π/2`, T=0 and T=1 each receive half of every entry in the table. In particular

```text
Pr(r=+1,T=1 | window)=1/4,
Pr(window,r=+1,T=1)=3/64.
```

T=1 implies h=1 exactly within this prescribed code. The clock window is an outcome of the explicitly constructed joint relative-clock instrument; it is not an exact classical clock reading. Access to this joint interface is not assumed for a confined record inhabitant.

## 4. Where is the information about h?

On the specified state, after the target interaction and conditioned on the finite clock window, the complete encoded record and work reductions for either h are

```text
ρ_R^(0)=ρ_R^(1)=I₂/2,
ρ_W^(0)=ρ_W^(1)=I₂/2,
ρ_RW^(h)=[I₄+(1−2h)K]/4.
```

The two-dimensional R space here is the encoded physical record pair `01,10`; the two-dimensional W space is the active work subspace `|a⟩,|b⟩`. The trace distance of the two joint `ρ_RW` states is 1, while the distance of either pair of single-subsystem reductions is 0. Thus this is not merely an average that cancels: **the h distinction is entirely relational for the specified single-subsystem reductions**. An ideal joint K measurement or the explicitly coupled T memory distinguishes it; a measurement on R alone or W alone does not.

In fact, in this particular preparation the whole reduced record–target-memory state is

```text
ρ_RT = (I₂/2)⊗(I₂/2).
```

The target can contain h while the confined record remains uncorrelated with it. The h–T coupling itself is a nonlocal record–work interaction, not an operation confined to R. The equal W marginals above also rely on **tracing Alice's outcome i**. If the richer interface supplies `i=1`, the two conditioned W states have trace distance about `0.106791`; that postselection does not give W access to Alice's outcome by itself. Information flow in other preparations can differ too: the previous [full-constraint analysis](ZERO_SUBJECT_BOUNDARY_REPORT_CAUSALITY.md) found a coherent-record preparation outside the protected code where the interaction can affect R. This result should not be promoted into an absolute subject-boundary theorem.

## 5. One event, three conditional incidence rules

For comparison with the earlier candidate model, we can tensor in the two fixed reference blocks `H₁=H₂=0` and **hypothesize**, without deriving it, candidate subjects `S₁=(H₁,R₁)` and `S₂=(R₂,H₂)`. Their previous graph selector did not include the present full record–work and target interactions; it is not being claimed to select subjects here.

On `r=+1,T=1`, h=1 and `J₁=r(1−2h)=−1`. For a common positive unit κ, consider:

| Conditional experiential proposal | candidate values `(S₁,S₂)` | pair sum with equal incidence |
|---|---|---:|
| R: record-relative | `(+κ,−κ)` | 0 |
| J: work-probe-relative | `(−κ,+κ)` | 0 |
| −R: reversed record-relative | `(−κ,+κ)` | 0 |

R and J disagree on which candidate has which sign on this event. More generally J and −R are not the same rule for all h: J agrees with R at h=0. The signs and equal actual incidence are **hypotheses**, not derived feelings. If a negative value corresponds to suffering, the opposite value does not erase it.

The local-report test removes one proposed *package* under a definite condition. The h-labelled states here are conditional subensembles; obtaining that label operationally would itself require an appropriate joint measurement or preparation. Since their full R reductions are the same, no R-only quantum instrument with an initially uncorrelated reporting ancilla can distinguish them. A reliable J-sign report together with r would distinguish them, because `J₁=r(1−2h)`; it therefore cannot be supplied by that strictly R-local interface. A joint RW or external T interface can distinguish h, but assuming such access changes the subject-boundary proposal. This is not a claim of actual reports or superluminal signalling.

Even imposing strict record locality and equal-weight pair balance does **not** select R over −R. Thus this integrated physical calculation narrows the candidate bridge but does not determine what is actually felt or derive the experiential pairing. The differing formal assignments do not assert that incompatible complete realities are genuinely possible under necessary plenitude.

## 6. No-signalling and conservation scope

Compare Alice's finite pair and triple instruments with all subsequent Bob-side gates fixed. The test retains Bob's spin, both clocks, Bob's reference and pointer, R, the active work register and T; Alice, her reference and her pointer are traced out. The two complete retained density matrices agree, as checked through their low-rank Gram matrices. The same remains true **after applying and conditioning on the same three-label relative-clock window**. The mathematical no-signalling result follows from fixed local nonselective operations, not from interpreting inaccessible ensemble labels as feelings. The joint relative-clock pointer is an additional interface and no actual spacelike arrangement is constructed.

The Q accounting is also deliberately limited. Every declared circuit unitary commutes with Q and the chosen states lie in `ker Q`, including the nondegenerate local work occupations. But a sequence of prescribed gates does not supply a fully autonomous Hamiltonian, control system or the energy cost of switching interactions. If the gates are generated by physical interaction Hamiltonians, those interaction/control energies must be included before identifying Q with objective total energy. A constraint or convenient offset is not automatically the universe's energy. The compensating `−2` in Bob's clock spectrum, the initial paired state, all interactions, and T's degeneracy are specified model inputs.

## 7. Consequence for the user's proposal

This is a concrete *same-system* advance: an exact paired zero charge, finite relational-clock readout, the actual work-current probe, a targeted relation memory, and an operational subject-boundary test now coexist. The actual opposite local work changes are not erased by their balanced total. The relation h can be objectively encoded in a joint physical correlation without existing in either subsystem's marginal alone.

It does not show that zero necessarily produces the stated circuit, that these registered distinctions are actual experiences, or that experiential values and incidences pair globally. The R/−R ambiguity is a test that a deeper constitution must resolve, not evidence that incompatible phenomenal worlds are genuinely possible. A serious next step is a **single autonomous** model that generates this instrument and the target interaction with all interaction and control energies included, then derives a subject–quality rule that survives the demonstrated local-report condition. No fundamental preferred foliation or literal simulator is required by this finite construction.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_energy_sphere_work_incidence_test -v
```

The tests check the actual four-qubit work operators and nondegenerate local occupations, exact Q=0 through the prescribed circuit and relative-clock pointer, finite-window and reference-size controls, h and target-memory distributions, individual versus joint reduced states, the extra target-interaction current, and full-lab no-signalling. They do not prove a physical total-energy definition, autonomous control, actual subjects, Born incidence, irreversible records or quantum gravity.
