# One experiential whole and finite perspectives: an explicit access test

## Why this step belongs to the whole plan

The user's proposal is that one timeless absolute has an intrinsic nature identical to experience; finite perspectives are real articulations of that same actuality, not independently fundamental experiencers added to it. To make progress on [M0/M4 of the global plan](GLOBAL_COHERENCE_AND_DECISION_PLAN.md), we must explain how a single reality can contain distinct, limited access **without pretending that limited access itself is a phenomenal subject**.

This note gives one small but concrete intermediate result: limited, asymmetric access and a more complete whole-description can arise from an explicitly specified internal causal process rather than from a hand-written mask. It also identifies what that result still cannot explain. It does not establish universal consciousness, necessary existence, or a neuroscience model.

This is a finite classical control, not a new theory of knowledge. Local-state indistinguishability and distributed information are established methods; see [Halpern and Moses, *Knowledge and Common Knowledge in a Distributed Environment*](https://arxiv.org/abs/cs/0006009). The scope distinction was already illustrated in [Complete Awareness and Finite Disclosure](COMPLETE_AWARENESS_FINITE_DISCLOSURE.md); the specific addition here is a reproducible causal mechanism, an intervention test, and a joint-record control on the same simple process. It is not a claim of literature novelty. Cosmopsychist accounts and their finite-perspective problem are also prior art; see the [Stanford Encyclopedia discussion](https://plato.stanford.edu/entries/panpsychism/) and [Shani and Keppler](https://www.cambridge.org/core/journals/journal-of-the-american-philosophical-association/article/beyond-combination-how-cosmic-consciousness-grounds-ordinary-experience/DBFAD5F0F70A4ACE5E3FD464581B2FF5). Their proposals differ from one another and are not assumed to be identical to the user's view.

## 1. A scope error worth avoiding

Suppose the same absolute is referred to as `S` in both a whole-wide and a local description. If we write an **unindexed** predicate `K(S,p)` and assert both `K(S,p)` and `not K(S,p)` in the same respect, we have a contradiction; declaring S to be one subject does not change substitutivity of identity.

The candidate needs a distinction in the predicate, not a second fundamental subject:

    available(S, whole_scope, p)
    not available(S, local_scope, p).

Those statements are compatible because they concern different scopes. This is a logical consistency observation, not a solution of the constitution problem: merely adding an index does not explain which local scopes exist, how they arise, or whether anything is phenomenally present there. Whole-wide information, propositional knowledge, qualitative acquaintance and local report remain distinct.

## 2. Physical process: local records derived from dynamics

Let X and Y be independent fair input bits, and N an independent noise bit with `Pr(N=1)=q`, where `0<=q<=1/2`. In a declared internal order, send X through the channel

    M = X xor N.

At the specified readout stage the physical records are:

    A-record = X,
    B-record = (Y, M),
    full-description = (X, Y, N).

A and B are **record locations**, not names of experiencing subjects. The channel copies and corrupts a classical record; the full description includes the noise resource. The binary protocol and its internal order are supplied. They are not claimed to be fundamental matter, an external clock for the absolute, or a model of an actual brain.

The probability space is an illustrative ensemble of possible **descriptions of this experiment**. It is not a multiverse, a measure over universal observers, or an ontological assertion that all assignments are actual. For the illustrative actual history take `(X,Y,N)=(1,0,0)`. This value is an explicitly supplied control, not observational data.

For each record scope, form its equivalence class of ensemble descriptions with the same record. A proposition is *record-determined* at that scope if it has the same truth value across that class. This is an idealized operational criterion, not automatically a conscious subject's knowledge. Full description has a singleton class; A and B obtain their classes by evaluating the actual record functions, not by declaring a desired answer for each proposition.

## 3. A controlled result

For `q=1/10`, at the chosen history:

- The full description determines both X=1 and Y=0.
- The A-record determines X=1, but not Y=0.
- The B-record determines Y=0, but does not determine X=1: both `(1,0,0)` and `(0,0,1)` give the same B-record `(0,1)`.
- Nevertheless B can *guess* X from M correctly with probability `9/10` under the declared ensemble. Confidence is not certainty or phenomenal access.
- Combining A's and B's records determines `(X,Y,N)`, because `N=X xor M`. This is **distributed information** in the records, not proof that a physical process actually pools it or that the whole is conscious.

The asymmetry is more than passive correlation. Under independently specified interventions setting X=0 versus X=1, B's joint record distributions have total-variation distance `1-2q = 4/5`. Setting Y=0 versus Y=1 leaves A's record distribution unchanged: TV=0. These are causal claims **within this structural model** and under the supplied independent-noise assumption. They do not establish which human interventions are feasible.

Controls: if `q=0`, B's message determines X exactly; if `q=1/2`, B's message has zero information about X and the X-intervention TV is zero. For `q=1/10`, `I(X;M | Y)=1-h₂(q)≈0.5310` bits. The global description still contains X and Y at all three noise settings. The [verifier](verification/perspective_access_from_circuit.py) and [output](verification/perspective_access_from_circuit.json) enumerate the support and compute these quantities. Exact fractions are used except for the displayed logarithmic entropy.

## 4. What this does—and does not—do for the user's hypothesis

**What it shows conditionally:** if the experiential whole has an appropriate constitution whose physical aspect includes such scoped processes, a difference between local access and the complete description is not automatically contradictory, and the scope need not be an independently fundamental observer. Here the relevant local information differences are constrained by the specified channels and resources, rather than by the arbitrary act of calling a set a perspective.

**What it does not show:** the circuit does not determine which record constitutes a *lived* perspective, what either bit feels like, what joins contents in an experience, or that the whole has phenomenal acquaintance with every part. The whole-description is not automatically a knower; and an operational access distinction is not automatically experiential ownership. Treating one channel output as a perspective solely because it is local would simply replace one stipulation with another. Moreover, selecting A and B as the relevant records and choosing the causal protocol are supplied inputs: their ultimate origin and physical applicability remain open.

Two candidate accounts can accept the very same record predictions: one may identify finite experiences as articulations of one universal subject, while another may propose distinct subjects or another constitution. **For this model alone**, their operational predictions are identical unless additional, discriminating bridge assumptions are specified. This does not prove that all such accounts are permanently empirically indistinguishable.

A single global subject need not make every local content accessible in every local scope. Nor does lack of cross-access prove independent subjects. We must avoid the converse error too: a physical network's common origin does not by itself prove numerical subject identity or experiential unity.

## 5. Bridge to the actual research programme

Use this result as an explicit interface rather than another independent toy universe:

1. **Phenomenal anchor:** the [reported-content rivalry case](REPORTED_CONTENT_REFERENCE_CASE.md) provides source-designated content reports, but no paired neural basis or intervention-valid assay. It is not this binary circuit and its observed records are not fitted here.
2. **Candidate physical basis:** the [maintained-disclosure hypotheses](MAINTAINED_DISCLOSURE_CANDIDATE.md) already give two rival local constitution claims. Identify an actual process and establish the required maintenance-preserving / distribution-removing intervention; no assumed equivalence to A and B above.
3. **Evidence interface:** the [identifiability audit](DISCLOSURE_OBSERVATION_IDENTIFIABILITY.md) requires a target-specific, intervention-valid observation relation. A message error rate such as q is **not** an assay's false-positive/false-negative rate for experience. Confusing them would falsely make the rival test decisive.
4. **Whole-to-local obligation:** propose a mode of the one experiential absolute that corresponds to the independently specified physical basis and the anchored content, and justify why it is actually acquainted with that content—not merely why its physical record contains information. Test preservation, disruption and loss of access separately.
5. **Physics and time:** any real implementation must specify local interactions, resource costs and relational timing. The regulated field and Barontini benchmarks are separate constraints; neither is identified with this hypothetical process or the rivalry data.

### Check an actual no-report experiment against that contract

[Cohen, Ortego, Kyroudis and Pitts (2020)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7326348/) compared EEG responses to animal/object drawings in report and no-report conditions, with masking and, in a second experiment, without masks. They report a prominent P3b in the report condition and no corresponding P3b in no-report, with retrospective incidental-memory evidence offered in support of perception of the no-report stimuli. The authors also note that no trial-wise direct experience report was available and that EEG/P3b cannot rule out other frontoparietal activity or spontaneous postperceptual processing.

This is an empirical reason to distinguish a **particular report-associated signal** from consciousness. It is not the H_M1/H_D1 separating intervention:

| Required premise | What this paper gives | Decision |
|---|---|---|
| P3: candidate maintenance basis and its causal powers preserved | No independently established identity of that nominated basis across the two task conditions; condition and attention demands differ. | Not established. |
| P4: the particular multi-consumer distribution removed, without replacement | No-report instruction and a missing P3b difference, not a demonstration that all specified distribution pathways are absent; other activity and spontaneous processing remain possible. | Not established. |
| P6: valid measurement of the same qualitative target in the no-report condition | Retrospective memory and task controls give relevant but indirect evidence; no direct trial-by-trial report or validated error bounds for the frozen target. | Not established. |

The authors' null P3b result is not, without an equivalence analysis, proof that its true effect is exactly zero. Nor is P3b itself interchangeable with the prescribed distribution feature. In experiment 1, the fixed order of no-report blocks followed by report blocks adds a potential order confound to cross-condition interpretation; images are counterbalanced across participants, not literally the same image in both task conditions for each participant. We have not independently reanalysed their data, and no comparison of an individual target interval across conditions is asserted. The paper itself explicitly says it does not disprove the broad cognitive and higher-order theories.

**Decision:** promising evidence against a simple 'the measured P3b is always required' reading, but **inconclusive for H_M1 versus H_D1** and no test of whether one universal consciousness exists. The [intervention and calibration follow-up](INTERVENTION_CONSCIOUSNESS_CALIBRATION.md) checks a paired human gaze/report study and a separate TMS study against all three gates, and quantifies why accuracy and correlated repeats do not suffice. The next experiment must separately verify maintenance, removal, and observation—not treat the no-report instruction as accomplishing all three. A successful operational access result is useful, but it does not close the phenomenal or ultimate-existence bridges.
