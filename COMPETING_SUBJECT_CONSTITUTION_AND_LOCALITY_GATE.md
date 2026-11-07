# Competing rules for subjects: an explicit construction and locality test

## Result

We can now put two candidate subject rules on the **same** physical dynamics, specify what they say is experienced, and distinguish subject persistence from causal lineage. They disagree about whether a weakly coupled system contains one subject or two, even while giving exactly the same physical and report statistics. The difference is a stipulated physical–phenomenal bridge, not a discovery about brains.

The comparison exposed a more specific defect. A global-maximization rule can remove the subject assigned to one isolated subsystem when a separate, physically disconnected subsystem becomes stronger, even though the first subsystem is unchanged. If isolated-component stability is required, that particular rule fails. A **local-overlap repair** passes this isolation test and a specified weak-link example, but produces unresolved ties in another benchmark. It is a better-behaved *candidate diagnostic*, not a demonstrated theory of experience.

The executable checks are in [competing_subject_constitution_rules.py](verification/competing_subject_constitution_rules.py), with [receipt](verification/competing_subject_constitution_rules.json). The [standalone framework](CURRENT_FRAMEWORK_BATTERY_DOSSIER.md) remains frozen.

## 1. What already exists

This is a continuation of our [causal influence gate](CAUSAL_INFLUENCE_SUBJECT_CONSTITUTION_GATE.md), [tie and persistence audit](SUBJECT_TIES_PERSISTENCE_REDESCRIPTION_GATE.md), and [episode-incidence analysis](EPISODE_INCIDENCE_REFORMULATION.md), not a claim to have invented causal integration or theories of conscious unity. Relevant prior work includes [IIT 4.0](https://doi.org/10.1371/journal.pcbi.1011465), which has its own detailed state-dependent causal measures, exclusion rule, quality postulates and tie procedure; the simplified cut score below is **not IIT**. [Lopez's layered unity model](https://doi.org/10.1007/s11098-025-02339-3) is an existing account of partially unified split-brain phenomenology. The [COGITATE adversarial study](https://doi.org/10.1038/s41586-025-08888-1) tested specific IIT and global-workspace predictions, not the toy rules below. The standard Ising/heat-bath machinery and the prior score computation are reused, not presented as a new derivation.

Our contribution here is the exact **comparison, remote-component counterexample, conditional repair, and report-calibration test**, in this specific construction. We do not know whether the same issue has appeared elsewhere in the literature; it should not be represented as a new general theorem of consciousness.

## 2. One physical world, two explicit phenomenal completions

### Physical substrate

Take four classical spins `s₀,…,s₃∈{−1,+1}` in a line `0—1—2—3`, with ferromagnetic edge parameters `tanh(K)` equal to `1/2, t, 1/2`. At a fixed local step a randomly selected spin is updated by the standard heat-bath rule; a time-dependent edge setting can be externally specified between steps. For a fixed `t`, the equilibrium distribution is proportional to

`(1 + s₀s₁/2)(1 + t s₁s₂)(1 + s₂s₃/2)`.

The local steps order events **inside this finite model**; they are not a fundamental external clock, a theory of spacetime, or an account of duration in experience.

We reuse the previous interventional graph: clamp a neighboring spin to either sign, randomize the other neighboring inputs uniformly, and take the difference in the local-update probability; define the undirected edge weight as the smaller of the two directional effects. This choice of manipulation, background distribution, and time grain is a substantive modeling convention. The graph does not automatically recover neural causation or an intrinsic ontology.

An additional **eligibility mask** marks which vertices a rule may select. It is an explicitly supplied physical-model input, not an experience measurement; it is not inferred from the spin state. Scores use the original full-network intervention weights restricted to eligible vertices, even if another vertex is ineligible. For the isolated-pair example below the excluded pair has no cross-edge, so there is no claim that masking an interacting neighbor leaves physical responses unchanged. The mask has no realistic anesthesia or lesion calibration.

### Subject and content postulates

Fix once and for all a qualitative symbol `qᵢ(sᵢ)` for each spin and sign. This is a **stipulated content label**, not an explanation of redness, pain, a human sensation, or why a physical sign feels like anything. Both proposals use the same labels and the same full physical kernel:

- **C — connected-subject completion.** Each connected component of eligible vertices in the positive-influence graph, provided it contains at least two vertices, is one experiencer. At a local step its episode contains the tuple of the `qᵢ` labels on that component. A connected component of one vertex and ineligible vertices receive no toy subject.
- **M — global-maximal-cohesion completion.** For each eligible subset `S` of at least two vertices, score it by the minimum sum of edge weights over nontrivial cuts *inside* `S`. Choose the positive globally maximal score; among ties choose the largest cardinality. Each nonoverlapping selected set is one experiencer and its episode contains that set's labels. If equally sized maxima overlap, the rule returns **unresolved**, not an arbitrary selection. Vertices not in a selected set receive no toy subject.

Each rule explicitly postulates that its selected set's label tuple is **one joint experience**; different selected sets have different subjects. This bridges causal graph to phenomenal incidence by assumption. Neither coupling, a label, nor a report supplies that identity. Even an accurate mathematical selector would not answer why these labels possess a particular qualitative nature. The whole-as-intrinsically-experiential thesis is compatible with leaving the omitted toy vertices without *these candidate local subjects*; no conclusion about all fundamental experience follows from the mask or size restriction.

These rules are not full physical theories. In particular, the graph and chosen spin factorization are assumed given. Transporting these designated units, admissible interventions and scores under a relabeling preserves the results; invariance under arbitrary encodings, coarse-graining, changing temporal scale, gauge transformations or quantum descriptions is not established. See the [factorization gate](SUBJECT_CONSTITUTION_FACTORIZATION_GATE.md) for why that matters.

## 3. Same dynamics, different answers

All four vertices are eligible unless noted. `t` is a parameter of the toy coupling, not an estimate of callosal connectivity.

| Model regime | C subjects | M subjects | What is genuinely established |
|---|---|---|---|
| `t=1/2` | `{0,1,2,3}` | `{0,1,2,3}` | Both *postulate* one joint tuple. M's size rule resolves a six-way score tie in favor of the full set. |
| `t=1/4` | `{0,1,2,3}` | `{0,1}`, `{2,3}` | One versus two subjects from the same physical model. |
| `t=0` | `{0,1}`, `{2,3}` | `{0,1}`, `{2,3}` | Both split in the exact disconnected, symmetric toy. |
| `t=3/4` | `{0,1,2,3}` | `{1,2}` | M discards the two outer vertices from all toy subjects: a consequential pathology, not a fact about experience. |
| `t=0`, only `2,3` eligible | `{2,3}` | `{2,3}` | Both assign one toy subject to the eligible pair, by the input mask. |
| no eligible vertices | none | none | Both give no *toy* subject because of their definitions, not because neuroscience has established unconsciousness. |

At `t=1/4` the reciprocal internal edge weights are `10/21` and the cross-edge is `4/21`. C sees a connected graph; M selects the two internally stronger pairs. At `t=1/2` all three weights are `2/5`; the six connected intervals of length at least two tie, and the size convention selects the four-spin set. The published [earlier calculation](CAUSAL_INFLUENCE_SUBJECT_CONSTITUTION_GATE.md) supplies the influences and cut scores.

### Application to the requested real cases: constraints, not diagnoses

The table is a deliberately crude **structural analogy**; there is no fitted mapping from any patient or human brain to `t`, the four spins, the eligibility mask, the content labels or the scoring rule.

- **Ordinary waking:** reportable experience warrants at least the reporting person's experience; neither rule's choice of full connected graph has been shown to be its neural substrate or its subject count.
- **Dreaming:** both rules can postulate an episode when the modeled system remains eligible but has no current external input. They do not explain dream imagery or predict recall. Anesthesia and sleep can involve reports of experience or no experience; our [cross-condition audit](HEMISPHEROTOMY_ANESTHESIA_AND_SUBJECT_BOUNDARIES.md) explains why unresponsiveness is insufficient to fix the mask.
- **Callosotomy:** weak coupling versus exact zero shows how the rules could disagree or agree in an idealized disconnection. Actual surgery, residual pathways, visual fields and time scales differ, and none of the toy counts is a patient result. See the [task audit](SPLIT_BRAIN_DEEP_EVIDENCE_AND_TASK_AUDIT.md).
- **Hemispherectomy:** the one-eligible-pair case illustrates a surviving connected subsystem, not a model of developmental reorganization, brainstem support, or an adult hemisphere. Preserved report does not establish the mask or rule.
- **Hemispherotomy:** the separated-pair case could be *descriptively* compared with retained isolated tissue, but postulating that the isolated side is eligible versus ineligible changes the answer before observation. EEG and fMRI do not presently calibrate that choice or the supposed local subject. The connected patient's report is not a report from the isolated cortex.

## 4. Persistence is an additional rule

For these models **only**, stipulate that a subject persists strictly from one local step to the next exactly when the same transported carrier subset is selected at both steps. Otherwise, the old subject ceases and any newly selected subset is a new subject. A separate directed **lineage** link exists for each pair of successive selected subsets that overlap in at least one transported physical carrier. It is not numerical identity. These arbitrary rules are intentionally explicit: they are not entailed by the instantaneous score or shown to be true of actual persons.

Now let the physical coupling be changed from `t=1/2` to `t=1/4`:

- **C:** the same full carrier remains selected, so its toy subject persists.
- **M:** the full-carrier subject ceases; two new pair-subjects begin. Each has overlap lineage from the previous subject, but neither is numerically identical to it.

If coupling is then set to zero, C's full subject ceases and two pair-subjects begin; M's existing pair-subjects persist. If reversed, these rules stipulate the corresponding cessation/new-subject events. No appeal is made to temporal identity by merely putting all stages in one undirected connected component. This avoids the identity contradiction of equating a single subject with two distinct successors, but the cost is a drastic discontinuous birth/death rule. A different rule could preserve one successor or allow indeterminacy, at the expense of additional assumptions and the symmetry constraints in the [persistence audit](SUBJECT_TIES_PERSISTENCE_REDESCRIPTION_GATE.md).

## 5. New stress test: does an isolated subject vanish for a remote reason?

Adopt this **candidate locality criterion**, not a proven metaphysical necessity:

> If two physical components have no causal edges between them, and the second component's complete relevant dynamics, state, eligibility and constitutive inputs remain fixed, changing only the first component should not alter the second component's subject assignment.

For two disconnected two-vertex components, take edge weights `w₀₁=w₂₃=1/2` and all cross weights zero. C and M each select both pairs. Now change only the first component to `w₀₁=3/5` while leaving `w₂₃=1/2` and all cross weights unchanged. Such independent-pair weights can arise in the same heat-bath family; there is no intervention on the second pair.

- C still selects `{0,1}` **and** `{2,3}`.
- Global M selects only `{0,1}`: its score `3/5` beats the second pair's `1/2`. The other pair is unassigned, despite no change in its local dynamics.

Thus **M fails the stated isolated-component stability criterion**. If one rejects that criterion and proposes a nonlocal constitutive law, M is not logically refuted; it must instead explain why an entirely causally disconnected remote change removes this local subject. This result is specific to our global-max, unnormalized cut-score rule, not IIT's local complex selection. A global maximum over a finite toy universe is especially dangerous to transplant into an unbounded whole: a maximum need not exist, and distant unrelated systems can dominate it.

### A repair, and why the first repair is not enough

A simple repair applies M separately inside each connected component. It returns both pairs when the cross edge is exactly zero. But for weights `w₀₁=3/5`, `w₂₃=1/2`, and `w₁₂=ε`, the whole graph is one component for every `ε>0`. For any `0<ε<1/2`, the global score inside that component selects only `{0,1}`. At `ε=0` it selects both pairs. The script checks `ε=1/100` and `1/10000`; the stated interval follows because every subset spanning the weak link has a cut of at most `ε`, while the separate pairs score `3/5` and `1/2`. Componentwise maximization fixes *exact* independence, not robust weak independence.

### A constructive alternative: overlapping-local maxima

Define **L**, a candidate incidence diagnostic using the same positive minimum-cut score:

1. For each positive-scoring eligible subset `S`, compare its score with every **overlapping** positive-scoring candidate `T≠S`.
2. Select `S` only if its score is strictly greater than every such `T`.
3. If no overlapping candidate has a greater score but at least one has an equal score, retain `S` as an **unresolved competing tie**, not an additional definite subject. Candidates beaten by an overlapping higher score are not selected.

Strict winners are automatically nonoverlapping: two overlapping winners would each have to score strictly more than the other. This is a local-exclusion idea related to established approaches, including IIT's complexes, but it uses our elementary score, has different definitions and does not calculate IIT. The incidence rule and qualitative postulate remain unsupported assumptions. A persistence rule and how to interpret unresolved ties are still needed.

L has two specific advantages in the present toy:

- **Exact disjoint-extension stability:** for nonnegative weighted graphs with no edges between two components, every mixed subset has zero minimum-cut score. The positive competitors overlapping a subset in one component are unchanged when an independent component is added or changed. Therefore its strict winners and unresolved local ties are unchanged. This is a conditional mathematical property of this score and candidate set, not a theorem that nature must satisfy this criterion.
- **Weak-link benchmark:** with the `3/5` and `1/2` pairs and `0<ε<1/2`, L selects both pairs; each is stronger than any overlapping set that crosses the weak edge. It agrees with the exact-zero result, unlike componentwise global M in that example. This is not a general continuity result for all graphs.

L also exposes a cost. For the uniform `t=1/2` four-spin case, the same six connected subsets tie and overlap, so L finds **no strict winner** and records six unresolved candidates. This does **not** say there is no experience; it says this partial rule cannot decide. The size convention M used to select the full set would be an added tie rule, and the existing [symmetry counterexample](SUBJECT_TIES_PERSISTENCE_REDESCRIPTION_GATE.md) shows that not every tie can be resolved by a deterministic nonoverlapping, nonempty, symmetry-respecting choice. L does not supply a complete ontology, eliminate grain dependence, or show that its score tracks experience.

## 6. How could any observation distinguish the completions?

### Same physical law means same physical observations

Both C and M add labels to the **same** spin state, interventions, dynamics and report apparatus. For every intervention permitted by that apparatus they therefore give the same physical transcript distribution. For example, with all vertices eligible and equilibrium at `t=1/4`, both give

`P(s₀=s₃)=17/32`.

This is a physical correlation, not phenomenal unity. Adaptive repetitions also have identical transcript laws if the starting distribution, physical transition/readout kernels and policy are held fixed. The script verifies the equilibrium arithmetic and permutation properties, not all possible adaptive policies; equality for arbitrary finite adaptive policies follows by induction from the stipulated identical kernels. The point is not that all subject theories must be empirically indistinguishable, but that these particular labels add no new physical law.

### The explicit report bridge and its burden

At `t=1/4` define a phenomenal yes/no target `Z`: whether the labels on endpoints 0 and 3 occur together in **one** episode. By the candidates' *own stipulations*, `Z_C=1` and `Z_M=0`. Let `R` be an answer to a fixed question about that exact target; set nonresponse aside and do not treat it as no experience. For the same physical answer channel, write `q=P(R=1)` in that target condition. Then

`error_C=P(R≠Z_C)=1−q`,  `error_M=P(R≠Z_M)=q`,  hence  `error_C+error_M=1`.

This is an elementary consequence of complementary labels on the same answered trials. For the verifier's **fictional** common reporter, `q=3/4`, so the respective errors are `1/4` and `3/4`. A reporter could calculate or assert a combined answer from a shared comparator without its answer having been generated by one joint phenomenal episode; the [common-source gate](JOINT_ACCESS_COMMON_SOURCE_DECISION_GATE.md) gives explicit examples. This does not establish that human reporting works that way.

Suppose, as a **separate and independently justified** bridge assumption, that the relevant report error is at most `r<1/2` in the target condition. Then the two **packages** make separated observable predictions:

- C plus bridge: `q≥1−r`.
- M plus bridge: `q≤r`.

For illustration `r=0.1` means `q≥0.9` versus `q≤0.1`; intermediate observations challenge at least one assumption in *each* package. These predictions are not derived from C and M alone, and no measured `r=0.1` is claimed. If an observation contradicts a package, it need not uniquely falsify the underlying constitution rule: the measurement model, target definition, physical model and error calibration are also responsible candidates.

**Why source calibration cannot simply be transported:** at `t=1/2` both rules say `Z=1`. An always-yes reporter has zero error in that source regime under both rules, yet at `t=1/4` it has zero error under C and error one under M. Thus even perfect source-condition agreement does not, by itself, establish target-condition validity. This is a constructed domain-shift counterexample, not evidence of the error rate in people. The critical problem is how to anchor `Z` independently where report, memory and behavior may be dissociated; postulating a low error in exactly that domain simply assumes away the disagreement.

A real comparison would predefine the phenomenal question and time window, recruit appropriate report-accessible controls, check cue leakage and common-source mechanisms, preregister analysis and report missingness, and independently justify how error bounds transport to the target condition. Causal interventions and physiology may rule out *physical* models; they do not by themselves identify the phenomenal label. In the isolated hemisphere direct behavioral access may be unavailable, so even that conditional report test need not be possible. None of this is a recommendation for clinical intervention.

## 7. What this advances—and what it does not

**Conditional gain.** If the locality criterion is adopted, M's global maximization is inadequate. L demonstrates that a strictly local candidate comparison can repair that exact defect and the chosen weak-link case while keeping overlapping ties explicitly unresolved. This provides an actionable constraint for a genuinely plural-subject theory: remote, causally disconnected structure should not accidentally erase a subject solely because a larger unrelated score exists, unless a nonlocal phenomenal law is independently defended.

**No winning phenomenal rule yet.** C merges systems for any positive path, even arbitrarily weak coupling. M has remote and strong-center pathologies. L inherits dependence on the cut score, factorization and interventions; it can leave tied cases unresolved and may leave vertices outside any candidate. None explains *why* its tuples feel like anything, fixes valence or establishes that a selected subset has a first-person perspective. The quantitative report bridge makes the empirical burden explicit rather than solving it.

**Relation to the whole.** The working hypothesis is a self-sufficient, necessarily actual, intrinsically experiential whole with genuinely plural local subjects, not an agentive universal subject. Strongest possibility = actuality is not modeled as selection or a mechanism. No literal simulation or simulator is assumed. A physically disconnected *finite local toy* is not an assertion that a globally separate possible world exists. The current work leaves the intrinsic nature of the whole, the qualitative constitution law, subject measure, imperfect-world argument's premises, quantum theory, emergent spacetime and local time open. It does not establish zero residue.

**Next decisive task:** seek a principled experiential and empirical basis for either an admissible local-exclusion relation or a different incidence law. In parallel test L against heterogeneous sizes, overlapping structures, coarse-graining and time histories, and look for independently validated target-domain reports or physical consequences. If the bridge remains unanchored, record underdetermination rather than choosing a winner for elegance alone.

## Reproduction

Run `python verification/competing_subject_constitution_rules.py` from the repository root. It imports the two existing standard-library verifiers, computes the four-spin subject outputs and equilibrium correlation, checks 1,536 combinations of parameter, eligibility mask and vertex relabeling, checks the disconnected-component repair and fission under 24 relabelings, and writes the linked JSON receipt. It also checks two weak-link values and the six-way unresolved tie. The all-`ε` weak-link and disconnected-extension claims above follow from the cut definitions; the script is not an exhaustive proof over all graphs. These are finite mathematical checks, not experimental data or confirmation of consciousness.
