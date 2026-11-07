# Contextual disclosure: a worked quantum constitution of record scope

## Result and status

A concrete quantum construction supplies part of the proposed disclosure architecture: compatible record statistics, conditional agreement, and restricted physical access can belong to one nonclassical state without a global loss of coherence. A separate exact obstruction shows why complete knowledge must not be defined as a context-independent definite value for every sharp observable.

This is a positive construction of **physical record scope**, not an identification of record scope with experiential acquaintance. The missing subject/quality constitution is not filled by the word disclosure. The mathematics is standard quantum theory, not a new theorem, experiment, or zero-residue breakthrough. Its application constrains the existing intrinsic-articulation conjecture rather than introducing another ontology or work queue.

The constructive candidate is now more precise:

> Investigate finite experience as the qualitative occurrence of an actually maintained, context-sensitive organization within one concrete reality. Physical scope must be grounded in its interactions and counterfactual powers, not in deletion of globally known facts. Compatible records must agree where their physical comparison establishes agreement; incompatible measurement contexts must not be forced into a common noncontextual value assignment. Neither record agreement nor contextuality alone constitutes a subject.

The first two requirements have a worked quantum scaffold below. The final qualitative and ownership identification remains conjectural.

## 1. Independent premises and meanings

The calculation assumes, rather than derives:

1. Finite complex Hilbert spaces, tensor composition, standard observables and unitary operations.
2. Born probabilities, including joint probabilities for commuting observables.
3. For a proposed noncontextual assignment, each sharp observable has the same pre-existing value in every context containing it; products of commuting observables respect their operator product identities.
4. For the record example, a specified preparation and two specified interactions.

Premise 3 describes the target of the obstruction, not a commitment of quantum theory or of our absolute account. Rejecting it need not reject complete knowledge. The record operations are ideal mathematical descriptions of possible physical interactions; no empirical realization is reported.

Distinguish four notions:

- **A quantum state:** a positive normalized functional assigning expectations to observables; not itself a mind or an actual outcome list.
- **A compatible context:** a commutative observable algebra with a joint probability distribution.
- **An operational record scope:** the observables made readable by the specified interaction/readout arrangement.
- **An experiential scope:** directly present qualitative content and its ownership. No equality with any of the preceding notions is assumed.

## 2. One common state, consistent contexts, no common noncontextual valuation

Use the two-qubit Peres--Mermin square, with juxtaposition denoting tensor product:

| | | |
|---|---|---|
| XI | IX | XX |
| IY | YI | YY |
| XY | YX | ZZ |

Here X, Y, Z are Pauli matrices. Within each row and each column the three operators commute, and each operator squares to I. Row products are all +I. The first two column products are +I; the third is -I.

If each of the nine observables has one context-independent value in {+1,-1}, the three row equations require the product of all nine values to be +1. The three column equations require that same product to be -1. No such assignment exists.

This is not merely a restriction on a particular preparation. The operator identities make the contradiction state-independent under the stated value-assignment assumptions.

There is nevertheless a perfectly good **single quantum state** supplying all six compatible-context distributions. Choose rho = I_4/4. For context observables O1,O2,O3 and signs s1,s2,s3, their joint projector is

    P_s = [(I+s1 O1)/2][(I+s2 O2)/2][(I+s3 O3)/2].

Each context has four nonzero rank-one joint projectors, each with probability 1/4, and four zero projectors. The allowed outcomes obey the context's product sign. Every shared observable has marginal probabilities 1/2,1/2 in its two contexts. Thus the distributions agree on overlaps. They arise from one positive quantum state but not from a single probability distribution over noncontextual assignments of all nine values: any such distribution would have to be supported on assignments satisfying all six parity constraints, and there are none.

### Consequence for complete awareness

Complete knowledge of every actual fact does not entail the existence of all the context-independent values assumed above. Omniscience must not be confused with a joint value assignment that the physical theory does not permit.

This does **not** prove an aware absolute, refute every hidden-variable theory, or exclude a global inventory of context-indexed actual facts. Contextual hidden-variable theories do not satisfy the refuted assumption. Nor does it show that incompatible contexts are all actually measured in one run. The construction includes counterfactual measurement alternatives; it does not declare every alternative outcome actual.

The earlier finite Boolean witness in [complete awareness and finite disclosure](COMPLETE_AWARENESS_FINITE_DISCLOSURE.md) remains a valid witness about its stipulated compatible propositions. It must not be extrapolated to a Boolean inventory of context-independent values for all quantum observables.

## 3. A physically generated record scope, rather than a stipulated knowledge mask

Let S be a measured qubit, A a first register, and B a register reading A. Prepare

    |+>_S |0>_A |0>_B,
    |+> = (|0>+|1>)/sqrt(2).

Apply CNOT(S,A), then CNOT(A,B). This specifies an actual interaction pattern in the mathematical model, not merely a list of which propositions an observer is allowed to know. The resulting state is

    |Psi> = (|000> + |111>)/sqrt(2).

The record projectors for A and B generate the commuting algebra

    R = alg(I_S tensor Z_A tensor I_B, I_S tensor I_A tensor Z_B).

Restriction of the global state to R gives

    P(A=0,B=0)=1/2,
    P(A=1,B=1)=1/2,
    P(A=0,B=1)=P(A=1,B=0)=0.

Consequently, conditional on either record value a,

    P(B=a | A=a)=1.

Agreement is derived from the interaction and preparation, not added as an independent agreement axiom. Each register alone has zero Z expectation, whereas the joint expectation of Z_A Z_B is 1. Correlation and individual certainty are different facts.

The Born conditional state for a recorded A=a is

    rho_a = E_a rho E_a / Tr(rho E_a),
    E_a = I_S tensor |a><a|_A tensor I_B.

It predicts B=a with certainty. This is a conditional prediction given a result, not a derivation that this particular result occurs. Conditioning cannot be used as a hidden outcome selector.

### What this actually explains

- Which record alternatives the specified coupling correlates.
- Which comparison outcomes have zero probability.
- How conditioning on one record constrains a later reader.
- Why a limited record algebra can belong to a larger coherent state.

It does not explain why A or B is a subject. Indeed, these bare registers provide no independently warranted reason to identify either as one. Adding a label such as internal representation would not change that.

## 4. Restricting access is not deleting the rest of reality

For the coherent final state,

    <X_S X_A X_B> = 1.

If one instead applies the unselective pinching operation

    D(rho) = sum_a E_a rho E_a,

the state becomes

    D(rho) = (|000><000| + |111><111|)/2,

and its XXX expectation is 0. All statistics in the record algebra R remain unchanged. The two states are nevertheless physically distinguishable by a suitable joint coherence test.

Therefore **restriction to R and replacing the global state by D(rho) are not the same operation**. Restriction computes the original state's statistics on a smaller domain; it does not destroy global coherence. The pinching channel really changes the global state, although a restricted observer cannot distinguish that change using R alone.

This supplies a physical example of bounded readout without global subtraction. It does not establish that any global state is awareness, or that every unmeasured quantity has a concealed definite value. The global state here is a mathematical quantum state, not the proposed absolute identified by another name.

This ideal copying model contains no environmental decoherence model, long-term robustness proof, neural realization, or irreversible classicalization. Both correlated components survive globally. It cannot demonstrate single-outcome actualization, or independently establish the ontology of relational facts. Consistent conditional records are the achieved result.

## 5. What has changed in the constitution proposal

A proposal in which finite perspectives merely hide parts of an already definite, context-independent value inventory is too restrictive if it includes all the observables above. There is no such inventory to hide. A compatible classical record domain can, however, be physically generated and consistently embedded within a larger quantum description.

The positive physical scaffold is consequently:

    one noncommutative observable/state/dynamics organization
       -> specific interactions and physically available readouts
       -> compatible record domains and their joint statistics
       -> conditional agreement when records are compared.

The arrows in this finite example are explicit calculations, not phenomenal identifications. At least part of what previously appeared as an arbitrary knowledge mask can be replaced by a specified causal organization. Other algebras remain mathematically available; the readout arrangement selects the operational domain, not a uniquely privileged algebra of all reality.

This does not finish the scaffold at the ultimate level: the interactions, preparation, algebra and Born rule are inputs. Nor is an operational domain automatically a maximally integrated or locally owned episode. The remaining incidence/quality target is still

    F(P) = (Gamma(P), chi_P).

No existing neural hypothesis is validated by these quantum examples. GWT remains a candidate account of access organization, not a phenomenal sufficiency premise.

### A sharper constructive burden

A successful continuation must identify an actual maintained organization that constitutes directly present qualitative content, while explaining why its scope is neither every correlated record nor an arbitrary mathematical restriction. It must preserve context-sensitive physical predictions and account for record comparisons without using phenomenal labels to choose the desired organization.

The proposal does not require one globally selected classical history merely because the absolute is one. Conversely, unity does not prove that all decohered alternatives are actual. Both questions require a substantive constitution. The present witnesses settle neither.

## 6. Verification and provenance

Run:

    python verification/contextual_disclosure.py

The [script](verification/contextual_disclosure.py) uses exact rational-complex arithmetic from the existing probability verification module. The [result](verification/contextual_disclosure.json) checks all 512 candidate noncontextual value assignments, all 48 context-outcome probabilities, joint-projector identities and overlapping marginals, followed by the specified unitary record construction, conditional agreement, and the coherence/pinching distinction. These are mathematical regression checks, not extra empirical evidence or additions to the historical 1,149-test core.

The contextuality construction is the standard Peres--Mermin parity argument: A. Peres, "Incompatible results of quantum measurements," Physics Letters A 151 (1990), 107–108; N. D. Mermin, "Simple unified form for the major no-hidden-variables theorems," Physical Review Letters 65 (1990), 3373–3376, DOI 10.1103/PhysRevLett.65.3373. The operator calculation is supplied here directly; independent reading of those original articles is not claimed.

Motivation came from the supplied Hearst ESR/ESO papers and Lotfabadi's self-modelling and world-as-instrument papers. Neither author is being credited with, or blamed for, the new application to this repository's absolute/disclosure conjecture. Earlier source assessments remain separate from this calculation.

Related: [necessary articulated unity](NECESSARY_ARTICULATED_UNITY.md), [unified constitution map](UNIFIED_CONSTITUTION_MAP.md), [effect-to-state probability reconstruction](OPERATIONAL_PROBABILITY_RECONSTRUCTION.md), [common constitution and closure](COMMON_CONSTITUTION_CLOSURE.md).
