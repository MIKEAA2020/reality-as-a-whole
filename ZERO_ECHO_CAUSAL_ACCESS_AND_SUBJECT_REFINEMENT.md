# Causal organization, access and candidate subjects on the echo

## Outcome

The next dependency was to try a subject criterion based on physical access and causal organization, rather than introduce another arbitrary ownership partition. On the existing echo **with the explicitly added saved-J memory and comparison report**, that test produces a useful candidate and a failure mode:

* A finite intervention graph depends on the time interval: J influences R during an individual echo pulse, but not across the complete T–Q–T echo; the full echo plus inverse has identity input–output action.
* A simple local graph criterion yields **three overlapping candidate supports**, and it is stable when an entirely disconnected pair is added. Those supports are not thereby subjects, and the sign pointer needed for the earlier quality candidates is absent from all three.
* Coherently encoding J into two physical registers preserves the **entire reduced logical circuit**, including off-diagonal states, but changes the naive graph's selected supports. If the two registers are first identified as one logical intervention and parallel logical edges are coalesced, the original graph and candidates return. That quotient is a proposed equivalence rule, not a proof that every physical encoding preserves subject identity.
* The actual ready-record access structure gives four minimal ways to recover the same classical B sign: `{B}`, `{R}`, `{H}` and `{J,L}`. They implement the same logical sign on the specified code, but are not four automatically independent subjects or four copies of an arbitrary unknown quantum state.
* If the overlapping supports are counted as distinct hypothetical incidences, a signed physical-style zero need not remain zero. A reciprocal-sharing rule repairs the illustrative arithmetic only by adding a substantive incidence premise.

The executable model is [verification/zero_echo_causal_subject_criterion.py](verification/zero_echo_causal_subject_criterion.py), with [tests](verification/zero_echo_causal_subject_criterion_test.py). It uses the previous [actual report circuit](ZERO_OWNERSHIP_REPORT_SYMMETRY_AND_INCIDENCE.md), not the unmodified echo alone. The added registers and gates are specified resources. No graph or readout is assumed to experience anything.

## 1. A concrete interventional structure—not correlation alone

Use bits `0,1` for the signs `+1,−1`. B and J are the old sphere and record signs, R is the existing echo bit, L is the extra saved-J memory and H the extra comparison report. The time-ordered circuit is

```text
save:       J → L
physical echo:  J → R;  B → J;  J → R       (T–Q–T)
report:     L → H;  J → H.
```

Each arrow denotes the control and target of a specific reversible XOR/CNOT in the reduced sign action, not a finding that physical influence is symmetric. M, the sign pointer, is a spectator in this particular circuit. The old gate Q acts on more than a classical bit in the actual physical model; the reduced signs alone do not describe all phases or degrees of freedom.

For a selected interval, define `a→b` if two basis inputs differing only in bit a can give different output bit b, with all other input bits held fixed; omit self-edges. This exhaustive deterministic channel diagnostic makes its interventions and outputs explicit. It does **not** establish that every formal clamp is an accessible local operation, preserves the preparation, or is allowed by every physical gauge constraint.

| Specified interval | Cross-bit influence edges |
|---|---|
| Individual T | `J→R` |
| Individual Q | `B→J` |
| Whole T–Q–T | `B→J`, `B→R` |
| T–Q–T followed by its inverse | none |
| Save, echo and report, with all input bits varied | `B→J`, `B→R`, `B→H`, `J→L`, `L→H` |

The exact echo action is `J′=J⊕B`, `R′=R⊕B`; the two J→R contributions cancel in the stroboscopic output. The complete echo and inverse are the identity. Thus “there is no J→R edge” is true for one specified endpoint channel but false for a resolved pulse. This is reversible causal propagation, not by itself a proof of a persistent experiencing subject or of experienced time.

With arbitrary initial L and H bits, the complete displayed circuit has `L′=L⊕J` and `H′=H⊕L⊕B`. In the special ready condition `L=H=0`, the final report is B. The verifier checks all 32 reduced input configurations and directly compares B, J and R projections at all four echo checkpoints against actual complex original vectors for source labels 0, 7 and 15 and both pointer signs. It does not turn all formal input bit flips into established laboratory interventions.

## 2. A local graph candidate—and its cost

Retain all **primitive** circuit edges, discard their direction, and give each distinct edge unit weight:

```text
B—J—R,       J—L—H—J.
```

This symmetrization, binary weighting, chosen time grain and site factorization are hypotheses. In particular, it is not the reciprocal-influence graph: the primitive directed graph is acyclic and contains no reverse edge for any listed edge. A rule requiring a nontrivial strongly connected or pairwise reciprocal module would select **no multi-site module** here; whether to count individual sites is another input. The absence concerns this reduced protocol, not the full sphere, reservoir, clock, pair or all possible interventions.

Apply the earlier [local candidate rule](ZERO_SUBJECT_LOCALITY_AND_OVERLAP_WEIGHTED_BALANCE.md): a nonempty support S qualifies when its internal edge weight `e(S)` exceeds its outgoing boundary weight `b(S)`, and no proper nonempty subset also qualifies. Exhaustive enumeration gives exactly

```text
S₁ = {J,L,H},
S₂ = {B,J,L,R},
S₃ = {B,J,H,R}.
```

Each has `e=3`, `b=2`. They are overlapping supports, not a partition. The verifier checks that all 120 permutations of the five sites transport the candidates with the graph: a passive relabeling is not a physical change. Adding a disconnected two-site system `X—Y` with weight 1, 17 or 100 leaves all three original supports unchanged and adds only `{X,Y}`. In general a minimal qualifying support cannot straddle disconnected components: if the whole has `e>b`, at least one component already satisfies the inequality, contradicting minimality. This directly avoids the particular global-modularity failure diagnosed earlier.

The price is visible. J belongs to every candidate, while the sign pointer M is isolated in this reduced circuit and is selected by none. But the two candidate quality signs both depend on M. If a proposed experience requires direct access to that sign, these supports do not supply it as stated; simply adding M to them would be a new rule. Likewise, the graph is for a protocol modified by L and H. Including the omitted old-carrier, apparatus, clock, angular or pair interactions could change its candidates. The criterion has neither established experience nor derived its own physical localization, intervention grain or treatment of singletons.

We can make that concern concrete rather than just list it. Add a separate ready report bit K and, at the anchor, write `M⊕J` to K using two controlled-NOTs; this reports `Q_now`. Alternatively also control K on R, reporting `Q_echo`. The reduced circuit test verifies both readout identities for all bit inputs with K ready. Adding the first report's edges `M—K` and `J—K` changes the same minimal-support rule from three candidates to **ten**, with none of the original three retained exactly; five of the ten contain M. Adding the extra R—K edge for the echo report gives **five** candidates, two containing M. The detector couplings are genuine changes to the physical circuit, not passive redescriptions; it could matter physically whether such an instrument is present, and a recording can disturb coherence. The finding is not that a real subject necessarily changes when measured. It is that a rule tied to the post-interaction graph cannot automatically be used to infer the unmeasured subject, and the two report protocols require distinct subject/report hypotheses. The earlier [candidate parity-report analysis](ZERO_INTERNAL_REFERENCE_SUBJECT_VALENCE_COMPARISON.md) checks the corresponding sharp physical sign observables; here the additional report circuit is tested only in the reduced sign model.

## 3. Logical encoding exposes refinement sensitivity

Introduce a second physical register `J₂` and encode the old J sign as the code subspace

```text
V|j⟩ = |j⟩_(J₁)|j⟩_(J₂).
```

This is a coherent isometry on a specified code; on a superposition it produces an entangled encoding, not two independent arbitrary quantum states. The encoded circuit uses J₂ to write L, J₁ to write R and H, and B to flip **both** J₁ and J₂ during Q. The two J registers remain equal on the code. On the full five-bit reduced logical input space the verifier constructs the 32-to-64-dimensional isometry V and the two reversible circuit matrices U and U′, and checks exactly

```text
V†V=I,        U′V=VU,        U′†U′=I.
```

Consequently the logical transformation is preserved for arbitrary coherent inputs and for inputs entangled with a reference, not only for diagonal probabilities. Additionally, the original complex source histories are checked directly: applying the actual old Q and the controlled flip to the added J copy agrees with encoding after Q; using the copied J to control the T write agrees with the original J-controlled T on the tested supported vectors. These are supported-sector checks; they do not assert a physical equality on the entire unconstrained old Hilbert space or that the extra encoding has no energy/locality cost.

If the raw physical factors and distinct primitive edges are instead fed straight into the same undirected unit-edge rule, the refined graph has four minimal candidates:

```text
{B,J₁,J₂,R},   {B,H,J₁,R},
{B,H,J₂,L},    {H,J₁,L,R}.
```

Collapsing J₁ and J₂ **after** selecting them does not recover the original three supports. By contrast, if an independently justified logical-site rule first identifies J₁ and J₂, treats the two B controls as one logical relation, discards any internal self-edge and only then applies the criterion, the original five-edge graph and three candidates are recovered. This quotient is checked exactly.

This is not a proof that a physical extra register cannot add a subject or experience. The new register is a real factor in a different physical implementation, and its admissible local operations can differ. Nor can one flip J₁ alone and remain within the equal-J code; a logical J intervention flips both. The result establishes a precise fork: a constitution claiming invariance under *this* code-preserving implementation must transport the specified logical intervention structure, whereas a constitution treating the extra factor as phenomenally relevant must justify how and why. Blindly rebuilding a graph from names of physical factors makes that decision implicitly.

## 4. The actual access sets do not count subjects

At tick 10 with ready R, L and H, the report construction gives

```text
J=bz,      R=b,      L=z,      H=b,
Q_now=M J,       Q_echo=M J R=M L.
```

On the actual reduced source distribution with equal pointer signs, exhaustive comparison of the specified **commuting sign readouts** gives these inclusion-minimal perfect access sets:

| Target | Minimal sets of available sign values |
|---|---|
| B | `{B}`, `{R}`, `{H}`, `{J,L}` |
| `Q_now` | `{M,J}`, `{M,B,L}`, `{M,R,L}`, `{M,H,L}` |
| `Q_echo` | `{M,L}`, `{M,B,J}`, `{M,R,J}`, `{M,H,J}` |

These are counterfactual capabilities under the explicit preparation, not proof that all readouts occur or are jointly available to a confined observer. With every B/J/R/L/H sign but **without M**, the optimal guess for either quality sign is exactly `1/2` in this state. A global analyst cannot silently grant M to a j-only subject. Conversely, equivalence on the code does not mean that all the corresponding operators agree on arbitrary unready states.

There is a stronger operational comparison for B. Let W be the reduced physical isometry from inputs `(B,J)` and ready `(R,L,H)` to the report-circuit output. On that code,

```text
Z_B W = Z_R W = Z_H W = (Z_J Z_L) W = W Z_B(logical).
```

These are different physical implementations of the same **classical logical sign** on the given code, including its coherent superpositions. As a quantum control, fix logical J and encode B in either `|+⟩` or `|−⟩`. The reduced density matrix on each of `{B}`, `{R}`, `{H}` and `{J,L}` is identical for those two inputs. Each support can read the logical Z sign but none can recover that phase distinction in this input family. Thus multiple classical records do not clone an arbitrary unknown qubit. This explicit echo example implements the same distinction between recoverable content and multiple regions emphasized by the earlier [quantum-access subject-count gate](QUANTUM_ACCESS_STRUCTURES_AND_SUBJECT_COUNT_GATE.md).

Four accessible implementations of B do not imply four B experiences or four subjects. Nor does logical equality show that two genuinely different subjects cannot access one common content. Deciding ownership, actual access and qualitative character still requires a separate bridge.

## 5. Overlap and signed incidence on this very graph

The three candidate supports have multiplicities

```text
m_B=2, m_J=3, m_R=m_L=m_H=2.
```

For a deliberately specified **formal signed flow**, take `h_B=−1`, `h_J=+1`, and all other rates zero. The unweighted site sum is zero, but summing the same local value on all three candidate supports yields

```text
S₁: +1,     S₂: 0,     S₃: 0;       subject-style sum = +1.
```

These h values are an abstract accounting control on the gate graph, **not** a computed physical energy flow of the quantum echo or a felt valence. If one additionally assumes that all three supports are distinct actual incidences, have equal incidence weight, and share each site's value equally among its occurrences, division by m yields

```text
S₁: +1/3,    S₂: −1/6,    S₃: −1/6;    sum = 0.
```

The exact arithmetic follows from the earlier overlap identity. But equal sharing, actual subjecthood, the identification of h with an experience, and the incidence weights have not been established. An exclusive normalized POVM also cannot simply be treated as a census of potentially coexisting subjects; the earlier [normalization/locality correction](ZERO_INCIDENCE_NORMALIZATION_LOCALITY_CORRECTION.md) remains applicable. Cancellation would not erase a genuinely negative experience.

## 6. What to do next

This pass improves the constructive interface: it puts an intervention diagnostic, a local support criterion, a physical record-access calculation, a coherent code refinement and the overlap accounting on **one specified echo protocol**. It also shows that the local rule is not yet the user's requested constitution: it is grain- and factorization-sensitive, excludes the pointer needed for the candidate qualities, permits overlaps without an ownership law, and depends on an unproved quotient of physical implementations.

The next feasible upstream test is to formulate an **operationally typed subject candidate** that combines an actually maintained process, its physically accessible logical algebra and its record/clock interval, then compare alternative candidates under code-preserving transport and genuine ancillary interactions. Any experiential meaning and report-truth calibration must remain separate explicit requirements. Only after an ownership and incidence bridge is justified can the signed-total, locality, physical-energy and ultimate zero/necessity claims be assessed as consequences rather than installed by definition.

Reproduce:

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_echo_causal_subject_criterion_test \
  verification.zero_ownership_report_bridge_test \
  verification.zero_subject_locality_overlap_balance_test -v
```
