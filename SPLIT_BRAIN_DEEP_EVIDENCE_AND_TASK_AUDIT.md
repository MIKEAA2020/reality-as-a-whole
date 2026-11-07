# Split-brain evidence: deeper source and task audit

**Scope:** literature review and exact analysis of a simplified task—not an analysis of patient-level data, a subject-count result, or a completed theory. This extends the [joint-access decision gate](JOINT_ACCESS_COMMON_SOURCE_DECISION_GATE.md). It also corrects an omission: the distinction between behavioral/action unity and experiential unity, and the danger of unilateral task shortcuts, have substantial prior literature. Our earlier gate is a project-specific integration of those issues, not their discovery.

## 1. What the deeper search changes

The live scientific issue is **not simply whether the hemispheres communicate**. There are distinct questions:

1. Is information delivered primarily to one visual field and how is fixation controlled?
2. What can each side process, compare, or convey through motor and sensory routes?
3. Do multiple response modalities behave as one coordinated action system?
4. Are two contents experienced together, by one subject, and do they remain so over time?

Results at one level constrain the others but do not automatically settle them. Most importantly, a successful response can use **less information than the task description appears to demand**. The correct null is the best explicitly specified shortcut under the actual stimulus distribution—not always 50%.

## 2. Empirical evidence and serious alternatives

### 2017: cross-response is a genuine finding, not a settled ontology

Pinto and colleagues [3](https://academic.oup.com/brain/article/140/5/1231/2951052) reported that two callosotomy patients could detect and localize stimuli across visual fields using verbal and manual responses, while other tests showed strong differences between fields and limitations on cross-field matching. This challenges a simple account in which response hand rigidly reveals which field contains a stimulus. The work also includes first-person reports and confidence measures, which deserve weight; neither should be dismissed merely because they are reports.

The interpretation is contested. Volz and Gazzaniga [2](https://academic.oup.com/brain/article/140/7/2051/3892700) discuss cross-cueing and other interpretive challenges. Pinto and colleagues [1](https://academic.oup.com/brain/article/140/11/e68/4157882) argue against cross-cueing using task differences, reaction times and controls. The 2020 multidisciplinary review [5](https://link.springer.com/content/pdf/10.1007/s11065-020-09439-3.pdf) considers residual connections, patient variability and multiple accounts. A proposed cue is not automatically an observed cue; conversely, no one control establishes zero residual communication. An absence of a statistically significant response-by-field interaction is also not by itself an equivalence test.

### The 1994 one-sided-strategy warning was already explicit

Seymour, Reuter-Lorenz and Gazzaniga [1](https://people.psych.ucsb.edu/gazzaniga/PDF/The%20disconnection%20syndrome.pdf) examined cross-field numerical comparisons and reported that a **one-sided strategy** could obtain about **78%** in a particular previously used design. Their paper discusses testing strategies and patient differences. This is directly relevant prior art for our task gate, not a novel methodological insight introduced here. It does not establish that the same strategy explains Pinto's later task: the designs and participants differ.

The search retrieved substantial indexed excerpts of the 1994 paper; the page-fetch tool did not return the complete PDF text. Treat the claim above as an **excerpt-based source check**, not a full independent reanalysis or a reproduction of the paper's 78% calculation. The [article DOI](https://doi.org/10.1093/brain/117.1.105) identifies the paper.

### Results differ across tasks and patients

Cronin-Golomb [2](https://pubmed.ncbi.nlm.nih.gov/3816237/) reported above-chance nonverbal cross-field matching in three commissurotomy patients under prolonged presentation; the abstract interprets this as cognitive transfer via subcortical pathways. Later work, including the 1994 study above, reported failures to reproduce other proposed high-level transfer effects with different patients and tests. These results should not be compressed into “no information can cross” or “all semantic information crosses.” Presentation duration, response design, controls, lesion details and patient history differ. The 1986 statement here is based on its indexed PubMed abstract, not a replay of its dataset or an independently established subcortical pathway.

### 2023 and 2024: behavior and anatomy are separate constraints

Pinto et al. [1](https://pmc.ncbi.nlm.nih.gov/articles/PMC10667445/) studied one patient in both a simultaneous same/different task and a sequential query task. They reported across-field accuracy of **80.8% overall** in the latter and **68.7%** on its question-mark trials. The authors explicitly discuss the possibility that the interval allows cross-cueing and argue for a different interpretation. These are important observations, but the participant's second stimulus is an instruction; the task is not our previous XOR experiment. The [earlier article audit](JOINT_ACCESS_COMMON_SOURCE_DECISION_GATE.md) gives stimulus timing, fixation controls and limits. The raw trials were not obtained; the article says they are available from the authors on request.

Marcantoni et al. [2](https://pmc.ncbi.nlm.nih.gov/articles/PMC11133720/) studied resting-state fMRI in six callosotomy patients: five were reported to have total callosal resection and one a partial posterior resection. They observed residual interhemispheric functional connectivity in some networks, with individual differences, and proposed possible extracallosal contributors. Resting-state correlation does **not** itself demonstrate a directed, content-carrying route, its capacity, a particular task's performance, or one unified subject. Their [data statement](https://pmc.ncbi.nlm.nih.gov/articles/PMC11133720/#data-availability-statement) points to article/supplement material and further inquiries; no raw fMRI analysis was performed here. Do not assume a match between any patient's labels across papers without verified identity.

## 3. Theoretical distinctions are established prior art

Bayne and Chalmers distinguish phenomenal and access unity [3](https://consc.net/papers/unity.pdf). Schechter and Bayne [1](https://research.monash.edu/en/publications/consciousness-after-split-brain-surgery-the-recent-challenge-to-t/) distinguish agency-based and experience-based accounts and argue that the interpretation of cross-response depends on additional assumptions. Schechter's 2025 [action-unity proposal](https://philosophymindscience.org/index.php/phimisci/article/view/11812/12129) explicitly asks whether motor-based action unity constitutes a kind of conscious unity, while separating that question from phenomenal perspective and subject identity. Lopez's 2025 [layered-unity proposal](https://link.springer.com/article/10.1007/s11098-025-02339-3) offers a different model with local and global experiential layers. These are competing interpretations, not experimentally established subject rules.

This matters for our framework: **one ontological whole**, coordinated behavior, a single agent, one phenomenal perspective, and a plural population of subjects are different claims. In particular, a non-agentive whole is not the user's earlier agentive universal consciousness. Nor may “partially unified” silently mean that a single subject or an overlapping population has been demonstrated.

## 4. An idealized baseline tailored to the 2023 query task

This is a new application of a familiar shortcut-control idea to a **simplified version** of the task, not a reanalysis of its data.

- Draw `X∈{0,1}` (the first shape) and `Y∈{query,stop}` independently and uniformly.
- If `Y=query`, the correct response is the shape `X`; if `Y=stop`, it is `STOP`.
- A strategy must respond in `{0,1,STOP}` and has no leaked information about the input that it is assumed not to receive. Pre-shared randomness is independent of the fresh inputs. Missing responses are not included in this idealized model.

Exact enumeration of all deterministic strategies gives:

| Information available to the response strategy | Best overall accuracy | Why |
|---|---:|---|
| First shape `X` only | `1/2` | It can always report `X`, but cannot know whether it was asked to stop. |
| Instruction `Y` only | `3/4` | It answers `STOP` on stop trials and guesses the binary shape on query trials. |
| Both inputs | `1` | It follows the instruction and supplies the shape when queried. |

Randomization independent of the inputs cannot improve these maxima: any randomized strategy is a mixture of deterministic strategies. The best **one-input** baseline is therefore **75%**, not 50%, under these exact assumptions. This is an operational shortcut bound, not a claim that either hemisphere in the experiment had exactly one input, that the patient used a shortcut, or that cross-field cognition requires a single subject.

A further warning: a strategy that **always reports the first shape** can be correct on 100% of query trials without accessing the instruction, while failing every stop trial. Therefore query-only performance by itself cannot prove use of both inputs. Pinto et al. also report overall performance and discuss the stop-trial issue; this observation is not an accusation that they relied only on the selected subset. Overall performance can constrain that particular shortcut, provided the post-exclusion joint trial distribution and response mapping are known.

### What the reported 80.8% does—and does not—tell us

The reported 80.8% point estimate is above the idealized 75% one-input benchmark. It is **not automatically a statistically established excess over 75%**: the actual post-exclusion shape/instruction frequencies, denominators, possible dependencies and analysis determine the relevant uncertainty and bound. The article's significance comparison cannot simply be repurposed as a test of this new null, nor can its 68.7% selected-trial value be pooled with 80.8% to infer a stop-trial rate without the actual weights. We do not know that the idealized assumptions or exact 75% benchmark hold for the original data.

For scale only, in a **fictional IID** experiment with 65 successes in 80 trials, accuracy is 81.25%, yet the exact one-sided binomial tail under a fixed success probability of 75% is approximately `0.121`. These are **not** the study's counts and are not its p-value. They show why a point estimate slightly above a demanding shortcut baseline cannot replace the relevant data and uncertainty analysis. If conditional trial success probabilities can vary by history but remain bounded by 75%, an appropriate martingale or other sequential bound—not an unqualified binomial assumption—would be needed.

### What question-trial accuracy could bound, conditionally

Suppose, for a fixed task context, shapes are truly balanced on eligible query trials and the response is used to estimate the first shape. Fano's binary inequality implies that if the **true**, rather than estimated, query accuracy is `A≥1/2`, the reporting transcript contains at least `1−h₂(1−A)` bits about that shape. Plugging in the reported rounded value `0.687` as a *hypothetical true probability* gives about `0.1034` bits. This is **not a confidence lower bound**, because the point estimate, actual denominators and sampling error are not resolved here. It is also an information statement about the output transcript—not proof of a particular interhemispheric route, concurrent experience, or subject unity. Existing [Fano methods](https://doi.org/10.1002/047174882X) are used, not re-derived as new theory.

## 5. A separate subject-identity constraint

The literature's partial-unity options affect the proposed constitution rule. Let `a,b,c` denote three **hypothetical** experiential tokens and let `R` mean “phenomenally unified with,” with `R(a,b)` and `R(b,c)` but not `R(a,c)`. Such nontransitivity is a stipulated formal possibility here, **not an experimental finding** about these patients.

If the theory demands both that each token has exactly one owner and that `R(a,b)` holds **if and only if** their owners are identical, then `R` must be transitive. The stipulated pattern cannot be represented. Two possible responses are:

- allow an experiential token to belong to more than one distinct subject—for example owners `{A}`, `{A,B}`, `{B}`, with `R` meaning shared ownership; or
- retain unique owners but distinguish the co-consciousness relation from simple sameness of owner, specifying what different relation constitutes it.

Either choice needs substantive philosophical and physical justification; the toy is not evidence that shared experiential tokens exist. It is also not a proof that all subject relations are nontransitive or that two subjects are present in a particular patient. This test prevents an implementation from silently assuming that a scalar connectivity score, single-agent behavior, and an equivalence-class partition of experiences are the same relation. Partial and layered unity are prior proposals, as cited above.

## 6. What a genuine next empirical step would require

A request to the authors for permitted trial-level data should specify stimulus identities and order, response and confidence, block/trial timing, visual-field locations, eye tracking, exclusions and the exact aggregation; raw video or physiological recordings may not exist or may be inaccessible. No request has been sent. With authorized data, a **clearly labeled post-hoc** reanalysis could:

1. reconstruct the actual full contingency table, missingness and post-exclusion trial distributions;
2. compute the best one-input strategy using those distributions, with held-out strategy selection or valid multiplicity adjustment;
3. compare observed performance and relevant confidence intervals with that bound, accounting for serial dependence and small samples;
4. examine only actually recorded cue channels and quantify their detection limits; and
5. distinguish physical information access from the separately anchored report of simultaneously experienced content.

An unrecorded cue cannot be excluded retrospectively by inspecting available data. A prospective task could randomly generate the two inputs, use full-factorial stimulus controls and prespecify timing and cue monitoring, but must be designed with appropriate clinical oversight, participant consent and burden limits. It is not yet an identified practical intervention that cleanly isolates all neural paths while preserving an alleged subject's experience.

## 7. Verification and remaining gap

Run `python verification/split_brain_query_strategy_gate.py`; its [receipt](verification/split_brain_query_strategy_gate.json) exhausts the small strategy class, checks the conditional example and hypothetical ownership relation, and calculates the illustrative binomial tail and entropy expression. These are independent finite calculations. The code does not use real trial records, determine brain pathways, verify reported percentages or establish consciousness.

The research conclusion is **more structured uncertainty**, not a neutral erasure of evidence: preserved cross-response and some delayed performance constrain oversimplified disconnection accounts; cross-matching failures, shortcut alternatives and residual pathways constrain overconfident unity claims. No listed paper derives the subject-constitution rule, the experiential nature of the whole, a self-location measure or the framework's physics. The frozen [v1 framework](CURRENT_FRAMEWORK_BATTERY_DOSSIER.md) is unchanged.
