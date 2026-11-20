# Contextual plenitude and the identity of records

## Result and scope

The strong proposal that all genuinely possible local occurrences are actual does **not** require assigning every observable a single context-independent value for the entire whole. Indeed, a standard quantum contextuality example shows that a proposed *single common value assignment* cannot reproduce all its ideal context correlations. Context-indexed record occurrences can avoid this contradiction while preserving compatible observable marginals.

This is a **conditional constraint and an explicit finite bookkeeping construction**, not a proof of plenitude, a solution of quantum foundations, or a demonstration of experiential subjecthood. It does not assume a universal subject. A record label is not automatically a subject or an experience. Nor does the example imply that an electron literally has outcomes for measurements that were never made.

The relevant results are established. The Peres–Mermin square is a standard state-independent Kochen–Specker construction; original references include Peres, [*Incompatible results of quantum measurements*](https://doi.org/10.1016/0375-9601(90)90172-K), and Mermin, [*Simple unified form for the major no-hidden-variables theorems*](https://doi.org/10.1103/PhysRevLett.65.3373). Their bibliographic identities were checked, not their full original texts. Context-labelled random variables and comparison through couplings are already developed in Dzhafarov, Kujala and Cervantes, [*Contextuality-by-Default: A Brief Overview of Ideas, Concepts, and Terminology*](https://arxiv.org/abs/1504.00530v6): its abstract and retrieved sections on maximal coupling were inspected, not the full paper. Massé's [*From the problem of Future Contingents to Peres-Mermin square experiments*](https://arxiv.org/html/2105.13821v1) discusses precisely this square and quantitative coupling bounds; its introduction and search-retrieved relevant sections were inspected, not all 35 HTML chunks or the experimental reanalysis. The contribution here is the **application to the project's explicit actuality, record-identity and plural-subject commitments**, with a reproducible finite realization—not a claim to have discovered contextuality, its coupling formalism or the bound.

## 1. The project question

Say the whole contains local experimental occurrences. A proposition such as “outcome +1” must specify **which occurrence and which measurement context**. Different records from different local experiments can coexist without making the same occurrence both +1 and −1.

The stronger proposal would identify all appearances of an observable across incompatible joint-measurement contexts with one value attached to one underlying preparation. That is a substantive **noncontextual counterfactual identity rule**. It does not follow from a single whole, a relational ontology, or the thesis that genuine possibilities are actual.

Conversely, context labels alone do not prove that all context–outcome combinations are genuinely possible or physically actual. The formal construction below stipulates records. The project still owes a criterion of genuine possibility, a physical realization, and a rule connecting records to experience.

## 2. The standard quantum constraint

Use the following two-qubit observables, where `X,Y,Z` are Pauli matrices, `I` is identity, and tensor products are implicit:

```text
 XI     IX     XX
 IY     YI     YY
 XY     YX     ZZ
```

Within each row or column, all three observables commute. The product of each row and the first two columns is `+I`; the product of the last column is `−I`. For each context, a jointly measured triple of outcomes must have the corresponding product. Each observable appears once in a row and once in a column. These operator relations hold for every input state; the concrete probabilities below use the maximally mixed state `ρ=I/4`.

The cited Peres–Mermin result rules out assigning each of the nine observables one ±1 value that satisfies all six product requirements. In the [reproducible finite check](verification/contextual_plenitude_record_gate.py), all 512 such assignments are enumerated: 96 fail one context, 320 fail three, and 96 fail five; none satisfies all six. This is a check of the known theorem in a particular representation, not a replacement derivation or a general claim about every hidden-variable theory.

For `ρ=I/4`, each context has exactly four allowed triples, each with Born probability `1/4`; the other four have probability zero. The verifier calculates all 48 joint spectral-projector probabilities as well as the commutators and products. Shared single-observable marginals are all 50/50 in both contexts. Nevertheless, there is no probability distribution over the nine noncontextual values that reproduces all six ideal context distributions: any positive-weight value assignment would have to satisfy all six perfect parity conditions, and none does.

## 3. A consistent record catalogue—and its limit

Construct a formal record catalogue with 24 labels `(c,o)`: six contexts `c`, each with its four allowed triples `o`. Within each context assign the four labels equal conditional weights `1/4`. On a separate declared protocol, one may set equal weights `1/6` for the six context choices, giving 24 records with weight `1/24`. These are mathematical occurrence slots; neither their actuality nor their weights are derived from plenitude.

The catalogue is locally consistent. For example, `+1` for `XX` in one occurrence and `−1` for `XX` in another are not contradictory: they concern different records. The quantum statistics don't require those records to be experiences. Actual laboratory experiments use distinct trials and require specified preparations, instruments and selections.

The subtlety is that **matching local marginal distributions does not imply a globally consistent identification** of the row and column values across counterfactual contexts. A global valuation adds an identity relation across contexts that the contextual catalogue did not contain. Likewise, declaring all local records actual does not entail that the outcomes of mutually incompatible measurements all occur as one joint event for the same observer or system.

### A reversible record-forming instrument

The catalogue need not be treated as a mere table of numbers. For each specified context, attach three initially-zero pointer qubits. For each commuting observable `O`, apply a Hadamard gate to its pointer, apply controlled-`O` from that pointer to the two-qubit system, and apply a second Hadamard to the pointer. This is a standard Hadamard-test-style indirect measurement, not a new measurement scheme; see [*Methodology for replacing indirect measurements with direct measurements*](https://arxiv.org/abs/1901.00015) (retrieved description and selected excerpts only). The resulting unitary correlates each pointer bit with the ±1 eigenvalue. For all three pointers, reading their computational-basis bits gives the joint projector distribution for that context.

The verifier constructs each of these six 32-dimensional system-plus-pointer circuits. It reproduces the four `1/4` record probabilities per context for `ρ=I/4` independently of the projector calculation. It also applies each circuit's inverse to all 32 basis vectors—192 recovery checks—and recovers the original combined state to numerical precision. This realizes a **temporary coherent pointer correlation** in an idealized circuit, not a permanently stored macroscopic outcome. Once a record has irreversibly leaked to an unmodeled environment, reversing only these qubits need not erase it; reading, decoherence, apparatus costs and repeatability are not modeled. The reversible correlation is not proof of an intermediate experience or of its absence.

## 4. A quantitative coupling diagnostic

A coupling is a mathematical joint distribution for contextual versions of the outcomes that has the correct distribution in each context; it need not describe an experiment in which all six incompatible contexts were measured on one system. Give each grid entry two ±1 variables, `R_ij` for its row context and `C_ij` for its column context. Let `ε_k` be the probability that context k violates its target product and `δ_ij=Pr(R_ij ≠ C_ij)` within the chosen coupling. The six parity relations and nine cross-context identifications cannot all hold on one complete table. Therefore every coupling satisfies the conditional bookkeeping bound

```text
sum_k ε_k + sum_ij δ_ij ≥ 1.
```

This is a union-bound consequence of the standard parity obstruction, closely related to existing contextuality-by-default bounds, not a new general contextuality theorem. The verifier checks that the number of parity failures plus mismatches is odd in all `2^18 = 262,144` context-indexed tables. The bound concerns **hypothetical coupled variables**. A mismatch probability is not an observed frequency of the same particle being measured simultaneously in incompatible contexts. Equal single-observable marginals do not fix the coupling.

In the ideal maximally mixed example, every `ε_k=0`, so the total of the nine mismatch probabilities is at least 1. The finite checker supplies one saturating construction: choose one of the nine grid entries and flip its column-context value relative to its row-context value; for each choice there are 16 value tables satisfying all six context products. Uniformly weighting these 144 abstract tables reproduces every ideal context distribution, with exactly one mismatch per table and `δ_ij=1/9` at every entry. This is a contextual *response-table coupling*: it is neither a demonstration of an underlying mechanism nor a count of physical subjects. It is not an optimality claim for other contextuality measures or for sequential-measurement simulations.

As a finite noise control, the uniform mixture of the 96 context-independent tables that fail exactly one parity constraint gives a symmetric model with error `ε=1/6` in every context and correct context outcomes uniformly distributed within each parity class. Under the specific parity-error model, common context-independent values require `6ε≥1`; this construction meets the bound at `1/6`. This is not an experimental threshold independent of implementation, sampling, identification, instrument disturbance or operational equivalences. For empirical testing, see Krishna, Spekkens and Wolfe, [*Deriving robust noncontextuality inequalities from algebraic proofs of the Kochen-Specker theorem*](https://doi.org/10.1088/1367-2630/aa9168), and Gühne et al., [*Compatibility and noncontextuality for sequential measurements*](https://doi.org/10.1103/PhysRevA.81.022121). Their abstracts and selected retrieved excerpts were inspected, not their full proofs or experiment datasets. In particular, the former criticizes relying naively on the ideal parity inequality as an experimentally robust test.

## 5. Consequences for the whole-account

1. **Admissibility must be context sensitive where physics requires it.** A local statement needs its scope and operational context, rather than an assumption that every locally meaningful proposition belongs to one context-independent global valuation. This is consistent with treating all genuinely possible occurrences as actual, but does not establish that thesis.
2. **Shared physics is not identical subjecthood.** The same formal observable occurring in two contexts does not establish that the corresponding records are one experience, two experiences, or experiences at all. Conversely, rejecting the global valuation does not show that no single observer can participate in successive compatible experiments. Subject incidence and persistence need separate criteria.
3. **Relationality needs constraints, not arbitrary labels.** A successful ontology must explain when two records are genuinely different events, when they are two descriptions of one event, and when physically meaningful contexts can be related without a forbidden valuation. Contextual coupling alone does not supply that ontology.
4. **Compatibility with hidden variables remains open under other assumptions.** Contextual response mechanisms, nonlocal models, or other approaches are not refuted by the Peres–Mermin argument alone. Blasiak's [*Classical systems can be contextual too*](https://arxiv.org/html/1310.4990v3) proposes a particular classical analogue; only its abstract and introduction were inspected. Such constructions are limited models, not automatic full reproductions of quantum physics.
5. **Neither weights nor local time are derived.** The `1/4` distribution is calculated using the Born rule; the catalogue and coupling do not derive it. Their labels do not constitute an emergent clock, a necessary existence argument or proof of an experiential ground.

The concrete next step is not to equate each quantum context or record with a subject. The unitary instrument is a useful starting point, but a complete candidate needs a physical implementation with an independently justified experience/persistence rule, then a check that the rule transports correctly between equivalent descriptions while respecting contextual and interference constraints. The [timeless joint-event gate](TIMELESS_CLASS_OPERATORS_DECOHERENCE_AND_JOINT_EVENTS.md), [subject identity/redescription gate](SUBJECT_TIES_PERSISTENCE_REDESCRIPTION_GATE.md), and [observation-selection gate](SUBJECT_MEASURE_AND_QUANTUM_OBSERVATION_GATE.md) address different pieces of that obligation; none establishes the missing experiential bridge.

## Reproduction

Run `python verification/contextual_plenitude_record_gate.py`; see its [JSON receipt](verification/contextual_plenitude_record_gate.json). The operator arithmetic, ideal projector probabilities, reversible pointer circuits, 512 assignments, 144-table coupling and 96-table noise control use the Python standard library. The script is a finite regression check and does not inspect any empirical data or prove the framework.
