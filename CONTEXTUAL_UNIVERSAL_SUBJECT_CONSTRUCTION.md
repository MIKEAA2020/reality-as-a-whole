# A contextual comparison construction for one universal subject

> **Status correction:** This construction tests a universal-subject rival and is not the framework's governing candidate. The user had already pivoted to the [self-existent experiential whole with plural finite subjects](SELF_EXISTENT_PLENITUDE_PLURALITY_CORRECTION.md), without assuming a universal agent. Asking whether the rival could be coherent did not reverse that pivot.

## What has been constructed

A conditional **universal-subject rival** is one genuinely agentive subject of an experiential whole, with real finite subjects but no requirement that every finite outcome be jointly accessible from its perspective. This file gives a concrete, limited probability structure for how that distinction *could* work in the existing reversible-friend scenario. Calling it the strongest overall candidate or the user's current target was an error.

The physical circuit and the mathematical relations below are explicit. The assignment of the roles “universal subject” and “friend with an experience” remains **a proposed interpretation**, not a consequence of the circuit. In particular, this is not a completed model of universal consciousness or a proof that the candidate exists. The construction does not assume that a non-agentive whole counts as a universal consciousness.

The scoped-probability strategy has antecedents in relational quantum mechanics and other contextual approaches; see [Adlam and Rovelli](https://philosophyofphysics.lse.ac.uk/articles/10.31389/pop.8) and [Cavalcanti's Wigner-bubble analysis](https://arxiv.org/html/2008.05100). The contribution here is its exact application to the **project's existing circuit**, together with an explicit test of what happens if the missing joint distribution is inserted. It is not a new interpretation of quantum mechanics or a claim that those authors endorse a cosmic mind.

## 1. The target and what must not be smuggled in

The proposed subject `G` is intended to be a single experiencing, agentive subject whose physical aspect is the whole, not a subsystem rebranded as the whole. A distinct finite subject `F` has a definite experience in its own relevant context. `G` is **not assumed** to have a definite, simultaneously comparable representation of every one of `F`'s experiences in all circumstances.

For agency, the minimum operational scaffold is an internal input–action–feedback organization: a physical process associated with `G` can respond to an input, influence an operation, and register a consequence. In the example below, an input `z` can control whether the friend memory is read or reversed. Such a controller is a physical component of the model, not automatically the whole-level subject. **Inferring that the entire composite is one agent and one experiencer from a component's control operation would be circular.** The whole-level constitution and its phenomenal unity are still owed.

Likewise, declaring `F` to be a qubit memory does not establish that a qubit thinks or feels. The finite friend's experiential reality is an additional proposal. If the user requires every finite experience to be literally shared by `G`, rather than grounded in the same whole or represented only in accessible contexts, this candidate does not yet meet that stronger requirement. It must explain shared-token incidence without reconstructing a forbidden joint account.

## 2. The common physical circuit

Use the exact circuit already specified in [the subject-identity gate](SUBJECT_IDENTITY_LOCAL_FRIENDLINESS_TEST.md): Alice's qubit `A` and Bob's qubit `B` begin in a Bell state and a memory `M` registers `A`. Alice either reads the memory (`x=1`) or reverses the registration and measures an interference observable (`x=2`). Bob chooses `y=1,2`; observed results are `a,b ∈ {−1,+1}`.

All four Alice–Bob distributions are

    P_G(a,b | x,y) = [1 + ab E_xy]/4,

with correlations

| | y=1 | y=2 |
|---|---:|---:|
| read, x=1 | 3/5 | 3/5 |
| reverse, x=2 | 4/5 | −4/5 |

`P_G` is an **operational probability table**, here taken to describe the records which the proposed `G` can jointly access after they are brought together. Their combination requires an appropriate physical communication or interaction; merely writing a joint table does not create an experiential act of comparison. For every setting the table is normalized, each single-record marginal is unbiased, and the observable Alice–Bob statistics are nonsignalling. The existing exact matrix calculation supplies these values; the new verifier checks the table against it.

Within the model one may introduce a classical internal cue `z` and the policy `x=1+z`: cue 0 selects the read operation and cue 1 selects reversal. Bob's setting and the cue are independently prepared in the stipulated test arrangement. The outcome records are feedback on the selected operation. This demonstrates a nontrivial **physical control interface**, not conscious agency, conscious choice, a global causal law, or an external creator. The two operations are mathematical alternatives and/or distinct locally realized trials; they need not be two alternatives performed on the identical individual run. Nothing in this setup creates reality from possibility.

## 3. A finite-friend scope and a read comparison

Let `c ∈ {−1,+1}` be the friend's outcome **in the friend scope**. For each `y`, introduce a second table

    P_F(c,b | y) = [1 + (3/5) cb]/4.

This matches the ideal memory–Bob statistics when those records are jointly read in the corresponding calibration/read context. Every `c` and `b` marginal is `1/2`, and it overlaps consistently with `P_G` on the declared Bob marginal. This choice treats the two appearances of `b` as the same comparable outcome in the overlapping scopes; that is a substantive part of the candidate, not something that mere notation establishes.

For a read trial, there is an explicit joint comparison:

    P_read(a,b,c | y) = δ_(a,c) P_G(a,b | x=1,y).

It is normalized, yields exactly `P_G(a,b|1,y)` and `P_F(c,b|y)`, and guarantees `a=c`. Thus an **undisturbed read** recovers agreement; it is not necessary to dismiss the friend's outcome to reproduce the ordinary comparison.

For a reversal trial, the atlas retains the separate `P_G(a,b|2,y)` and `P_F(c,b|y)` scopes but does **not** define a common `P(a,c|2,y)` as a fact available to `G`. Their common `b` marginal agrees. The attribution of the second table to a real friend during an actual reversal run is an **additional contextual hypothesis**: the memory-read calibration cannot establish it, because physically measuring the friend's record before reversal changes the experiment. Nor does the table prove that the friend can later communicate with Bob after its memory has been reversed. A complete interpretation must supply a principled event law and subject bridge for that assignment.

## 4. What happens if we force the scopes together?

Compatible overlaps do not mean that pairwise distributions cannot mathematically be extended. For each fixed reversal setting `y`, one valid joint extension is

    P_y(a,b,c) = P_G(a,b | x=2,y) [1 + (3/5) cb]/2.

It preserves both declared pair distributions. But the resulting *hidden* `(a,c)` joint distribution depends on Bob's setting, with

    TV[P(a,c|x=2,y=1), P(a,c|x=2,y=2)] = 12/25.

That dependence is not an observed signal in the model. It is a property of the **extra joint extension**, not of either scoped table separately.

One can choose a better extension: the earlier [sharp witness](SUBJECT_IDENTITY_LOCAL_FRIENDLINESS_TEST.md) achieves TV `2/5`. Its proof shows `2/5` is the minimum when exact read agreement and the stated `(b,c)` independence from Alice's choice hold. Thus **no** extension with those assumptions makes the `(a,c)` joint independent of `y`, as full Local Agency would require in the specified causal arrangement.

This is the key constructive result: the limited atlas has normalized pairwise tables, agreement where the record is read, and the required observable correlations. It does **not** have a Local-Agency-compatible, absolute, all-at-once joint extension under the stipulated single-friend/read conditions. The latter claim follows from the known Local Friendliness argument and the project's existing exact specialization, not merely from the definitions of the atlas. A different extension can preserve absolute events by dropping a relevant independence condition; the mathematics does not choose the interpretation.

## 5. Does this actually produce the universal subject?

**Not yet.** The construction identifies a possible physical/informational *interface* for the desired account and makes its omissions explicit:

1. **Subject constitution:** Why does `G` denote one experiencing agent, rather than a collection of records plus a controller? What makes `F` a distinct experiencing subject? Neither the circuit nor labels answer this.
2. **Experiential relation:** In reversal trials, is `F`'s definite experience shared by `G`, represented indirectly, or merely grounded in the same whole? These are different claims. If sharing is required, why does it not impose the missing joint scope, and how are the shared tokens identified?
3. **Contextual dynamics and agreement:** What event law assigns the friend-scope content without turning it into a physical collapse? Why is the read-comparison law valid, and what are the permitted comparisons for arbitrary operations and nested observers? The atlas only specifies this circuit; it does not derive or validate a general relational law.
4. **Persistence and agency:** How is the *same* `G` unified across contexts, and how does it act as a whole? The [two-stage persistence gate](UNIVERSAL_SUBJECT_PERSISTENCE_AND_QUANTUM_TIME.md) shows that a single subject label does not automatically supply the desired affine history. A cue-controlled local circuit is only an agency prerequisite, not sufficient evidence of a cosmic agent.
5. **Foundation:** The actual whole's self-sufficiency, intrinsic experiential nature, particular physical structure, emergence of local time, subject measure and quality still need justification. Granting that the whole is self-existent and essentially experiential entails those features; it does not establish the granting premises. This toy circuit makes no claim about a mechanism actualizing possibilities.

Under the user's adopted non-optimality bridge the whole is non-perfect; nothing here treats it as omniscient, omnipotent, or morally perfect. Also, denying `G` a joint outcome in the reversal scope is not the claim that an ordinary person's actual suffering is unreal or can be disregarded.

## 6. Verification and decision

Run [`verification/relational_friend_comparison.py`](verification/relational_friend_comparison.py), which imports the existing quantum-circuit correlators and exact sharp extension. It checks normalized overlapping scopes, read agreement, both mathematical gluing examples, and their `12/25` and `2/5` TV values. See the [receipt](verification/relational_friend_comparison.json). The script encodes **no real subjects** and checks no physiological, phenomenological or human-level observer data.

**Decision:** this is a viable finite probability scaffold for continuing the proposed no-God's-eye architecture, not proof of a universal conscious subject or an empirically complete interpretation. The next substantive bridge is not another change of perspective labels: it is an independently motivated subject–experience constitution that says what `G` is, how it is one agent, and precisely which finite experiences it directly has without imposing the joint assumptions already excluded by the two quantum tests.
