# From supplied identity markers to derived causal transport

## 1. Constructive result

A specified physical channel can determine an operational transport relation without an input table declaring which earlier entity continues as which later entity. Four exact two-qubit examples below have identical background density matrices at both endpoints but different interventionally derived transport relations. Snapshot resemblance therefore does not determine this target.

The target is **transport of independently variable physical information**, not persistence of a material carrier, numerical personal identity, or phenomenal ownership. Replacing a supplied identity table with a derived causal relation does not establish that those different relations are identical. This is a bounded constructive step in the existing incidence/lineage programme, not a new metaphysical constitution or theorem.

The working conjecture remains one concrete reality with internally grounded physical and experiential articulation. The calculation adds a physical constraint to that conjecture: an account of continuity must distinguish carriers, causal transport, and experiential lineage rather than letting similarity or a repeated name stand for all three.

## 2. What motivated the calculation

The uploaded Simon Raphael manuscript, *Similarity Theory: A Relational Ontology of Consciousness, Structure, and Time*, includes Appendix A, Version 1.4. Its A.7 and A.11 represent continuity using an underlying entity set U and partial maps i_t: U -> V_t. These are explicitly tracking conveniences rather than a completed constitution. A.14 also acknowledges that full frame-generation dynamics remain unspecified.

The constructive question is whether a relation can instead be calculated from independently specified physical dynamics. This tests one part of the missing explanation without claiming that graph vertices are subjects or that the author offered the graph as a proof of consciousness.

The manuscript was read in full (51 PDF/printed pages). The earlier foundations document's argument that complete relation eliminates distinction does not appear in this revision and is not attributed to it here. The revision still explicitly adopts distributed consciousness rather than a single universal mind. It is a source for analysis, not silently adopted as our absolute ontology.

Source upload: `st_revised_manuscript-appendix-5yTOqQPim6MpHj25.pdf`; SHA-256 `91342a9c32a1881e474b9c0e28b91ac2b4a64a51914449ee1b2ab6bd79abd686`. The complete source PDF is not republished in this repository; no redistribution license was established. This calculation does not rely on independent reading of its cited literature.

## 3. An operational relation with independently specified inputs

Supply two input subsystems, two output subsystems, a completely positive trace-preserving channel E, and the possibility of independent input preparation. These physical factors and interventions must be justified in an application; a tensor decomposition alone is not a subject decomposition.

For input i and output j, define

    D[j,i](E) = sup (1/2) || Tr_other_output E(rho_i tensor tau)
                            - Tr_other_output E(sigma_i tensor tau) ||_1,

with the product order adjusted for i. The supremum ranges over density matrices rho_i, sigma_i and an independently fixed other-input state tau. It compares preparations of i while holding the other input fixed, rather than conditioning on a correlated observation. The trace distance measures optimal distinguishability on the output j.

Define the associated relation

    i R_E j  iff  D[j,i](E) > 0.

This is a definition of the operational target, motivated by causal intervention: can independently changing input i change accessible output-j statistics? It is not a definition of consciousness or a proposed subject-boundary threshold. The relation is derived once the channel/intervention domain is given. Its strict nonzero criterion is appropriate for this exact mathematical question, not a noise-robust empirical decision rule.

Relabelling input/output subsystems relabels the relation. Faithful local basis changes preserve the trace-distance criterion when the channel and intervention/readout domains are transformed together. Thus a mere renaming cannot create a different transport fact. Adding or removing physically accessible interventions, tracing out an environment, or changing the channel is not mere renaming.

## 4. Four processes with the same endpoint background states

Prepare the background rho_* = I_4/4. Let S be the unitary SWAP, S|a,b> = |b,a>. Compare:

    E_id(rho)    = rho
    E_swap(rho)  = S rho S^dagger
    E_sym(rho)   = (rho + S rho S^dagger)/2
    E_reset(rho) = Tr(rho) I_4/4.

All four are CPTP and fix rho_*. Identity and SWAP are unitary. The symmetric channel is their equal convex mixture. Reset has Kraus operators |a><b|/2 for a,b in the four-dimensional basis. Positive weighted Kraus terms give an exact rational representation in the verification script.

Their endpoint state descriptions and all endpoint observable expectations on that background agree. Their dynamics and counterfactual responses do not. This is **not** an example of two different targets arising from the same complete physical process: the channels are different. If a frame graph includes the full channel/intervention structure, these processes need not have the same graph. The result excludes snapshot-only sufficiency, not graph representations in general.

For product input rho tensor tau, the output marginal formulas are:

| Channel | First output | Second output |
|---|---|---|
| identity | rho | tau |
| SWAP | tau | rho |
| symmetric routing | (rho+tau)/2 | (rho+tau)/2 |
| reset | I_2/2 | I_2/2 |

Consequently, with rows indexing outputs and columns indexing inputs,

    D(E_id)    = [[1, 0], [0, 1]]
    D(E_swap)  = [[0, 1], [1, 0]]
    D(E_sym)   = [[1/2, 1/2], [1/2, 1/2]]
    D(E_reset) = [[0, 0], [0, 0]].

These are exact optima, not fitted scores. In each marginal, varying one input changes the output by c(rho-sigma), where c is the corresponding table entry. Since the trace distance of density matrices is at most 1, D <= c. Orthogonal input states attain c, proving equality. Neither an input identity label nor a phenomenal assignment enters this derivation.

This yields four transport structures: straight routing, exchanged routing, both-to-both operational dependence, and no transmission of the varying input. They cannot be inferred from the common background state or its perfect self-similarity.

The reset output is still a physical state. An empty transport relation does not mean that its carrier ceased to exist, that nothing caused it, or that all information vanished from a larger closed world. It means its specified output statistics are independent of the varied input. A dilation may retain information in an environment.

## 5. Why a unique identity matching can be an extra selector

The symmetric channel has independent input- and output-SWAP symmetries:

    E_sym(S rho S^dagger) = E_sym(rho)
    S E_sym(rho) S^dagger = E_sym(rho).

Suppose a rule based only on this channel returns a unique bijection from the two input tokens to the two output tokens, and is covariant under relabelling. There are just two candidate matchings: straight and exchanged. Swapping only output names leaves the channel unchanged but exchanges these matchings. Neither is invariant. Therefore no such deterministic, bijective, symmetry-respecting selector exists on this basis.

The many-to-many causal relation is invariant and has no such problem. An equal probability distribution over the two bijections is also invariant, so the obstruction does not prohibit stochastic descriptions. A conditioned routing record in an enlarged environment can break the ambiguity. If that record is physically available and relevant, including it is an enlargement of the basis, not an arbitrary identity label.

The conclusion is deliberately relative to the supplied effective process. It does not prove that the complete concrete reality has indeterminate identity, that subjects merge, or that a full realization/dilation cannot ground a particular continuation. The same reduced channel can conceal realization details important to a different target. The warrant of the basis must match the target.

This gives a precise reason for the repository's existing separation of lineage from numerical identity: causal support need not have the structure of a bijective identity stream. Whether experiential continuation does is still to be established.

## 6. Correlation is not the derived transport relation

For a separate control, use the state

    rho_corr = (|00><00| + |11><11|)/2

and identity dynamics. Its Z correlations are perfect. Nevertheless, replacing the first input by either |0> or |1> while keeping the second marginal I_2/2 leaves the second output unchanged. There is no cross-input influence under that intervention.

Conditioning on the first value predicts the second. Independently setting the first value does not control the second. A correlation-based graph would conflate these targets; the specified transport criterion does not.

The relevant interventions are physical replacement/preparation operations, not deletion of inconvenient evidence. This control is mathematical, not a claim that equivalent interventions are available on human neural or phenomenal states.

## 7. What the positive constitution candidate gains

There are now three separately specified continuity questions:

1. **Carrier continuity:** what physical realization or token persists?
2. **Causal/content transport:** which independently variable distinctions influence which later organizations?
3. **Experiential continuation:** what grounds an episode's or subject's relation to a later episode?

The calculation supplies a rule and worked cases for question 2. It does not derive 1 or 3. Hardware may remain in place while a SWAP changes content transport. A reset may remove input dependence without removing the hardware. Copying may transmit a record to multiple carriers without multiplying a warranted subject. These distinctions prevent a structural tracking map from being mistaken for a subject constitution.

The strengthened conjecture is therefore:

> Finite scope and continuity belong to the actual maintained organization, including how distinctions are causally retained, transformed, exchanged, or lost from particular readouts. They are not fixed by resemblance of snapshots, repeated entity names, or correlation alone. A phenomenal constitution must explain why a specified maintained organization is qualitative acquaintance and how its continuation relates to these physical distinctions.

The final sentence remains the missing bridge. The universal D>0 relation is not proposed as Gamma: tiny couplings can make it dense; the definition supplies no integration threshold, episode grain, ownership, or qualitative identification. An actual GWT-like maintenance process is a candidate domain for further constitution work, not validated by these register examples.

Within the absolute account, these channels describe conditional internal physical organization, not production of another reality, external simulation, or an absolute becoming ignorant. The chosen laws, subsystem basis, and preparations are not derived from the absolute. Perfection, omniscience, and necessary actuality have not been proved.

## 8. Verification and integration

Run:

    python verification/causal_record_lineage.py

The [script](verification/causal_record_lineage.py) and [diagnostics](verification/causal_record_lineage.json) check CPTP Kraus normalizations and full matrix-unit channel actions, the four common background states, exact Pauli-preparation response differences, relabelling covariance, the symmetric-channel matching obstruction, and the correlation/intervention distinction. All arithmetic is rational complex. The supremum formula is justified analytically in section 4, not by declaring a finite sample exhaustive over states.

This is standard quantum-channel and symmetry reasoning applied constructively to the manuscript's identity-tracking gap. It is not claimed as a novel theorem, empirical finding, phenomenal identification, or the requested non-incremental metaphysical breakthrough. No historical core test counts or governing work queues change.

Related: [contextual disclosure](CONTEXTUAL_DISCLOSURE_CONSTITUTION.md), [incidence and lineage](EPISODE_INCIDENCE_REFORMULATION.md), [common constitution and target factorization](COMMON_CONSTITUTION_CLOSURE.md), [constitution research programme](CONSTITUTION_RESEARCH_PROGRAMME.md).
