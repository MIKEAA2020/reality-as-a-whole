# Shared experience versus duplicated experiential tokens

## The constructive result

A plurality of perspectives does not tell us whether a similar experience appearing in two perspectives is **one numerically shared occurrence** or **two distinct but qualitatively similar occurrences**. The distinction matters to the proposed experiential ground and to the counting of subjects; it cannot be inferred merely from shared neural pathways, matching reports, or a common informational content.

Two specific results locate the gap and a possible way past it:

1. **Conditional observational equivalence.** A model with one shared experiential token and a model with two distinct, perfectly coordinated tokens can generate exactly the same physical and local-report histories, even under adaptive interventions, when the allowed operations and observation rules depend only on the specified physical and local qualitative histories. This is an explicit model construction, not a universal impossibility theorem about all experiments or all theories of consciousness.
2. **A conditional disagreement test.** If two reports can be independently calibrated to the **same specified token-intrinsic binary property in the same window**, and their total marginal error is at most `e`, then shared-token identity entails reported disagreement at most `e`. A particular duplicate-token rival that independently predicts true disagreement at least `d` entails reported disagreement at least `d−e`. These packages are separable when `d>2e`. They are not distinguished unless the physical manipulation and calibration actually warrant these assumptions.

The equivalence and bound use elementary coupling and union-bound reasoning. Their general ideas and underlying philosophical problem are prior art, not claims of novel identification methods. The contribution here is to make their **joint premises and escape route explicit for the project's shared-token question**. The examples do not show that shared or duplicated tokens occur in an actual patient, or even settle their metaphysical possibility.

## 1. Targets before measurements

Work within a single, locally specified experiential episode or window. `L` and `R` label two stipulated perspectives or perspective-associated channels; they do not by themselves establish two actual subjects. Suppose an aspect is registered in both local descriptions. Distinguish:

- **Same content or quality:** each description includes an aspect qualitatively characterized as `g`. Qualitative sameness does not imply token identity.
- **Same token:** the exact same particular experiential occurrence `G` is included in both perspectives. Whether this is coherent depends on the subject and experience ontology.
- **Same physical support:** some common physical process participates in both reports. It is not equivalent to the same experiential token.
- **Same subject:** an additional fact about a perspective/subject rule. Sharing a token need not identify its subjects, and two tokens do not automatically entail two subjects.

The work of [Bayne and Chalmers](https://consc.net/papers/unity.html), [Schwitzgebel and Nelson](https://faculty.ucr.edu/~eschwitz/SchwitzPapers/CountingSubjects-250528.pdf), and [Lopez](https://doi.org/10.1007/s11098-025-02339-3) is analyzed, with precise reading limits, in the [three-paper audit](THREE_UNITY_PAPERS_READING_AND_FRAMEWORK_AUDIT.md). Lopez's global/local distinction is a possible phenomenal interpretation, not proof of a shared token. Her duplicated-global-representation alternative also need not entail distinct experiential tokens without further assumptions.

Related philosophical work is explicit about the same problem. Cochrane's [*A Case of Shared Consciousness*](https://philarchive.org/archive/COCACO-6v1), abstract and introduction inspected, distinguishes token sharing from distinct streams and argues that behavioral evidence alone is compatible with duplication; he proposes a further neural-locality principle. We do not treat that principle or his case-specific conclusion as established here. Bostrom's [*Quantity of Experience: Brain-Duplication and Degrees of Consciousness*](https://nickbostrom.com/papers/experience.pdf), abstract and initial duplication discussion inspected, distinguishes numerically distinct from qualitatively identical experiences and separates experience identity from person identity. His duplication and ethical arguments are not assumed, and actual simulations are not a premise. Mørch's [*Why Consciousness Can't Overlap*](https://philarchive.org/archive/MRCWCC), abstract and introduction plus selected passages inspected, challenges overlap on substantive and deflationary subject views. These three additional sources were **not fully read** for this gate; their remaining arguments, notes, figures and cited primary evidence were not systematically checked.

## 2. A precise split/merge observational equivalence

Fix a set of physically possible histories and a finite or countable sequence of allowed actions. Let each next physical record and pair of local report records be drawn from a specified conditional kernel of the past **observed** history and the current action. Actions may depend adaptively or randomly on all previously observed records. The kernel may include shared causes and correlated report errors; it is not assumed that reports are conditionally independent or infallible.

For each history, define two *interpretations of the same physical and report process*:

- **S:** one phenomenally stipulated aspect token `G`, present in local views `V_L={L,G}` and `V_R={G,R}`.
- **D:** two numerically distinct phenomenally stipulated aspect tokens `G_L,G_R`, with identical local qualitative attributes for each matched history, present in `V_L'={L,G_L}` and `V_R'={G_R,R}`. Both may depend on the same physical causes and can change together under every allowed action.

The views may have other local aspects and relations, provided the properties used by the observation kernel are the same under the map sending `G_L` and `G_R` to `G`. This local correspondence does **not** preserve token cardinality, nor does it claim that the total experiential structures are isomorphic. Subject status, whether these fields are maximally unified, and whether partial sharing is metaphysically coherent are deliberately additional premises.

**Proof of operational equivalence in this model class.** Couple the initial physical state, the actions, and every draw from the common kernel between S and D. At each step, identical prior observed histories give the adaptive policy the same input and hence, under coupled randomization, the same next action. The common kernel then yields the same next observable record. Induction gives identical full observed-history distributions for any finite horizon, including any conditional report correlations and any permitted adaptive intervention. This is an equality of observable laws by construction, not an assertion that all experiential facts coincide. A report that directly and validly reveals cross-view token identity would violate the observation restriction and is therefore not covered.

Identical qualitative appearances need not prevent someone from experiencing their own actual experience. The point is narrower: access to each local view and the physical/report history, under this stipulated mapping, does not determine whether the two views contain one token or duplicates. Statistical uncertainty about a known finite partition is a different issue from metaphysical indeterminacy of identity.

**What would break the equivalence?** A warranted identity-sensitive measurement, or a theoretically and independently justified intervention restriction that forces divergent phenomenal properties in the duplicate case but not the shared case, removes this constructed equivalence. Merely adding more interventions, subjects, neural channels, better behavioral prediction or higher report agreement does not do so if both interpretations are still allowed to use the same kernels. Conversely, causal latent-variable identification can work under informative restrictions: Zhang and colleagues, [*Identifiability Guarantees for Causal Disentanglement from Soft Interventions*](https://arxiv.org/html/2307.06250v3), establish results up to an equivalence class under specific mixing, intervention and generalized-faithfulness assumptions. Only the abstract and introduction were read here; proofs and full paper were not checked. Their results concern latent causal variables, not phenomenal identity, and do not contradict the construction above.

## 3. A sharp bounded-error gate

Let `T_L,T_R∈{0,1}` be truth values for the **same preselected, token-intrinsic property** in a matched, simultaneous window, and let `R_L,R_R∈{0,1}` be the corresponding report records. This property must be defined so that if the same token is present at both perspectives, it has the same value in both: `T_L=T_R`. A perspective-relative relation—such as whether the token is central *to L* rather than *to R*—does not satisfy this premise merely because its words sound the same. If the target can differ by context, time, viewpoint or part, its differing values do not establish token distinctness.

Write

```text
δ = P(T_L ≠ T_R),    D = P(R_L ≠ R_R),
P(R_L ≠ T_L) ≤ e_L,  P(R_R ≠ T_R) ≤ e_R,
e = e_L + e_R.
```

All quantities refer to the **same randomized condition, eligible population and episode window**. They are probabilities over the specified trial distribution, not averages of arbitrarily combined experimental arms. From the union bound,

```text
max(0, δ − e) ≤ D ≤ min(1, δ + e).
```

Reason: if true and reported disagreement differ, at least one report is wrong. The inequalities hold without independence of errors or of the two perspectives. Both endpoints are sharp with only these marginal error bounds: arrange erroneous reports on disagreement trials to remove as many disagreements as possible, or on agreement trials to create as many as possible, splitting the allocation between the two channels. Perfectly correlated common errors can instead leave disagreement unchanged. Thus error dependence cannot be ignored, but is not needed for this conservative bound.

The assumptions lead to different, precise statements:

- **Shared-token package S:** if both properties truly apply to the same token and are intrinsic in the above sense, `δ=0`, so `0≤D≤min(1,e)`.
- **A specified duplicate package D(d):** distinct tokens alone do **not** imply any positive disagreement. If an additional theory of the manipulation independently implies `δ≥d`, then `D≥max(0,d−e)`.
- **Separation:** for common valid bounds, `d>2e` gives disjoint predicted ranges. If an accurately estimated `D>e`, at least one premise of package S fails; this does not itself prove duplication. If `D≤e`, sharing is not established: perfectly synchronized duplicates can also agree. If `d≤2e`, these two coarse bounds cannot separate the packages, although other valid information might.

This is not the previous pair–triple incidence test: here the target is numerical identity of a particular putatively shared *aspect*, not whether a pair or triple is jointly experienced. Nor does this gate decide whether `L` and `R` are distinct subjects or whether the whole has a subject.

## 4. What would count as a real test?

A credible intervention would need an independently justified model of how a permitted, safe manipulation changes the designated property in the two candidate constitutions. For example, one might propose that a particular intervention affects only the left duplicate with probability at least `d`, while leaving the right duplicate unchanged. But that selective action, persistence of both tokens and lack of compensating synchronization are **substantive assumptions**, not consequences of labeling an intervention “left-sided”. A shared token might instead be altered for both, cease to exist, split into two tokens, or be replaced; the S prediction requires identity and the target property to remain well-defined in the very window measured. Exclude or explicitly model token loss, replacement, switching, and no experience; do not code any of them as simple agreement.

A practical protocol would predefine: the matched target and window; how the two report channels refer to it rather than different local contents; randomization and concealed stimuli; timing, fixation, sensory spillover, cross-cueing and common-cause controls; the intervention's effect on report, attention and memory; and nonresponse. Nonresponse may be imputed to a binary category only if the probability bound on **misstatement or nonresponse** includes every imputed trial; otherwise use a separate third outcome and explicit missing-data bounds. Correlated errors are allowed, but the two numerical marginal error bounds must be justified for the intervention condition itself. Calibration cannot be based solely on report agreement, the same disputed identity premise, or a physical proxy assumed to be experience.

A matched-control condition and independent manipulation checks can challenge particular coordination or pathway models. They cannot on their own establish token-intrinsic meaning, same-episode report access, a numerical phenomenal error rate, or a lower bound on true divergence. The status of an unavailable second report must not be represented as evidence of absent consciousness. Studies, if feasible, require informed consent, accessible communication, minimizing burden, and no invasive intervention for the purpose of this metaphysical test. No safe method for isolating the required pathway or independently validating the two experiential reports is established here.

**Hypothetical only.** Let `e_L=e_R=0.05`, `e=0.10`, and let D(d) predict `d=0.50`. Then S gives `D≤0.10`, D(d) gives `D≥0.40`. With `100` independent identically distributed trials and threshold `0.25`, the one-sided Hoeffding bound on either conditional decision error is `exp(−2·100·0.15²)≈0.0111`. This is not a real sample-size recommendation or a bound on total scientific error. It assumes the assigned model, report calibration, valid window, eligibility and iid sampling; uncertainty or failure in those assumptions needs its own budget. Rare clinical cases and repeated measures may not allow the assumed sample or independence.

## 5. Implications for the whole

A substrate-independent experiential theory must explain which transformations preserve token identity, not just which preserve a qualitative pattern or behavioral input–output map. Identity should be invariant under mere redescription, but two distinct realizations are not necessarily related by a harmless relabeling. A proposed theory must also say whether shared parts are compatible with its subject rule, whether relations and contextual phenomenal character are intrinsic or perspective-relative, and how real plurality differs from multiple descriptions.

For this project, the ground is intrinsically experiential, not a universal mind or a literal simulation. This choice does not by itself decide shared versus duplicated tokens, establish subject boundaries, provide a selective manipulation, or produce a metric of experiential error. Plenitude within the timeless whole likewise does not determine which model is genuinely possible or how its instances are individuated. C3 remains **full structural and experiential intelligibility**, required together with the other six criteria; the gate does not claim to satisfy it.

## Reproduction and scope

Run [`verification/shared_token_disagreement_gate.py`](verification/shared_token_disagreement_gate.py). The [receipt](verification/shared_token_disagreement_gate.json) checks all `2,024` grid triples across denominators 1–8 for sharp bounded-error endpoints, using exhaustive finite distributions of truth-disagreement and two error indicators. It also checks all 32 deterministic two-stage adaptive policies in a small physical/report model with one versus two identically valued tokens. The general coupling argument and bound above do not follow from finite enumeration; the script verifies only these constructed examples. No human data, actual experience or subjecthood was simulated.
