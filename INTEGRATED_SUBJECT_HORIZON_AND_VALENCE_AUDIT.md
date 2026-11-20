# Integrated candidate: subject horizon, valence and persistence

## Question and failure conditions

This audit challenges the **same four-spin sector** of the [integrated experiential misalignment candidate](INTEGRATED_EXPERIENTIAL_MISALIGNMENT_CANDIDATE.md), rather than introducing a separate ontology. The goal is to determine what the existing subject-and-quality proposal actually fixes.

The following would count as a failure of a strengthened proposal, not of experience itself:

1. **Horizon-independent constitution:** if a single underlying physical process is claimed to determine one horizon-independent subject decomposition *and* rule L applied at each of two admissible horizons is claimed to give that decomposition, incompatible outputs refute those combined claims.
2. **Phenomenal identification:** if a physical statistic alone is claimed to fix unpleasantness for all experiential models compatible with it, a same-physics countermodel with a different experience assignment defeats that inference. A countermodel is not an empirical disproof of a particular experience assignment.
3. **Persistence:** if persistence is claimed to follow merely from repeated selected sets or changing mismatch values, an explicit identity criterion is missing; labels and transitions alone are insufficient.

The existing candidate **already fixes a one-update convention**; it has not promised horizon independence. Thus the first test exposes a necessary additional justification, not an internal contradiction in E-L as written. Different horizons are different causal questions. They might correspond to different legitimate experiential grains; it would be wrong to demand invariance without an argument. Conversely, selecting one by convenience does not establish which one constitutes a subject.

## 1. Same system, explicitly changed causal question

Use the existing four-spin heat-bath chain with outer interaction parameters `1/2` and middle parameter `t=1/4`. Its physical state and all transition probabilities are as in [the original coupled-boundary model](verification/coupled_subject_boundary_gate.py). Each update selects one site uniformly and resamples it by the heat-bath rule.

For each input spin `j` and sign `a`, prepare `s_j=a` and randomize the other three signs independently and uniformly. This is an **instantaneous initial pulse**, followed by `n` free updates of all four spins, including `j`; it is not a sustained clamp. For output `i≠j`, define

`I_n(j→i) = Pr(s_i=+1 at n | pulse j=+1) − Pr(s_i=+1 at n | pulse j=−1)`.

For each pair set `w_n(i,j)=min(I_n(i→j),I_n(j→i))`. Apply the **existing** L rule to every subset of at least two spins: its score is the minimum sum of internal edge weights crossing a nontrivial cut, and an L winner is a strictly positive score exceeding the scores of all overlapping eligible subsets. The influence graph now includes indirect effects at longer horizons; this is intentional. The preparation distribution, random-site kernel, pulse, aggregation of indirect effects and eligible factorization are assumptions, not consequences of an experiential ground.

At `n=1`, the new pair weights are exactly one quarter of the original local-update graph, because only one of four uniformly selected sites updates. Multiplying all scores by a common positive factor does not change L's selected sets. This verifies that the extension begins at the existing candidate rather than a different starting rule.

| Free updates after pulse | L selected sets | left-pair score | whole score |
|---:|---|---:|---:|
| 1 | `{0,1}`, `{2,3}` | `5/42` | `1/21` |
| 2–8 | `{0,1}`, `{2,3}` | see exact receipt | see exact receipt |
| 8 | `{0,1}`, `{2,3}` | `23850644075/153692888832` ≈ 0.15518 | `177524852875/1210331499552` ≈ 0.14667 |
| 9 | `{0,1,2,3}` | `56672320079255/406671383849472` ≈ 0.13936 | `58735313037017/406671383849472` ≈ 0.14443 |

Each row uses the **same physical kernel** and L criterion. The verifier checks all competing subsets, strict maxima, and all 24 node relabelings at each horizon. The two descriptions do not have the same input: `n` is different. The crossing is therefore an exact finite sensitivity result, not proof that two empirical measurements should agree or that either subject count is correct. The data do not establish what happens for all horizons or other dynamics. Treating the whole at `n=9` as one subject is still a *postulate*, not a derived experiential fact. It is not a claim that the timeless absolute is a universal consciousness.

**Conditional incompatibility.** Suppose the same process and occurrence have exactly one fixed set of subject boundaries `S`, and both the one-step and nine-step graphs are equally admissible representations to which L must return `S`. Then `S` must be both the two-pair family and the singleton whole-family, which is impossible. At least one of those extra commitments must be revised. Alternatives include a justified distinguished horizon, an explicit multigrain ontology, a compatibility/identity map across grains, or a different constitution rule. Each is additional work. Comparing the raw scores across horizons to pick the largest is not automatically justified: response magnitude changes with the query, and an optimization criterion and eligible horizons would themselves need independent support. Nor does an external universal clock follow from choosing a local dynamical horizon in this toy.

The connected-subject rival C also selects the full set for this weakly coupled system, including at the original one-update horizon. C is an experience-respecting rival: it stipulates experience rather than denies it. Its agreement with L at nine updates does not establish either rule; their original disagreement remains at one update. The original neutral-ground N-L rival likewise accepts experience and shares the chosen physical law. Same-kernel equality is stipulated, not a universal impossibility of empirical discrimination.

## 2. Quality and readout are separate from structure

For the left pair, `q=(1−s_0 s_1)/2`. E-L proposes that `q=1` is unpleasant and `q=0` neutral. That assignment is *not* established by the spin dynamics, the cut score, being an experiential ground, or the mathematics of mismatch. Consider two deliberately explicit rival packages on the same one-step selected pair and identical physical transition law:

- A: the pair has an experience and `q=1` is unpleasant while `q=0` is neutral.
- B: the pair has an experience and `q=0` is unpleasant while `q=1` is neutral.

These are stipulated rival experience assignments, not a finding that valence is inverted in nature. They agree on every distribution of physical spin histories and every physical readout computed from those histories **because they have been assigned the same kernel and readout rule**; they differ phenomenally at every state. An observer who genuinely knows the relevant felt quality can in principle distinguish the assignments. A reliable report that changes with it could also distinguish them, but neither a report channel nor its calibration has been derived here. If a theory entails a particular causal feedback of experiences into reports, that entails additional law and could make its predictions differ; the matched-kernel construction does not rule this out. Our prior [subject/readout interface](SUBJECT_CONSTITUTION_INTERFACE_RESULTS.md) and [calibration transport result](EXPERIENTIAL_MISMATCH_CALIBRATION_TRANSPORT_GATE.md) remain conditional on their specified error and transport assumptions.

The E-L quality proposal is defined for the L-selected outer pairs, not for the nine-step whole. In particular it does **not** supply a whole-subject qualitative state at `n=9`. Extending it requires an actual content/ownership rule, not simply applying the same pair labels to the whole.

## 3. Physical transition versus identity

In the unperturbed equilibrium chain at `t=1/4`, the exact joint probabilities for left-pair `q` at consecutive updates are:

| earlier `q` | later `q` | probability |
|---:|---:|---:|
| 0 | 0 | 295/448 |
| 0 | 1 | 41/448 |
| 1 | 0 | 41/448 |
| 1 | 1 | 71/448 |

Both changes occur with positive probability. L's one-update graph and pair selection remain the same when the stationary law and parameters remain fixed, but it does not follow that the same *subject* persists through either change. A persistence account must say what identifies an experiencer across changing contents, whether branching/merging is possible, and how any relation between horizons affects identity. It must not identify two earlier distinct subjects with one later subject by transitivity without addressing the resulting contradiction. On the timeless-whole proposal, these are relations among local records or ordered stages, not evidence of an external actualization process. The [persistence and redescription audit](SUBJECT_TIES_PERSISTENCE_REDESCRIPTION_GATE.md) sets out related unresolved constraints.

## 4. What could make this a real bridge?

A usable successor to E-L needs **all** of the following, rather than another success score on a toy:

1. **Specification:** give a noncircular rule fixing physical variables, interventions, background distribution, temporal grain and boundaries in a relevant system; or explicitly define a multigrain ontology and compatibility relation. State how ties and overlapping fields work, and how subject identity is tracked across changing records.
2. **Experiential anchor:** articulate why the identified structure constitutes a unified subject and why a specified relation is *felt* as a particular quality. Fit to the accepted datum that experience occurs is necessary but does not determine that bridge. Experience-respecting non-mismatch and alternative-constitution rivals must be treated symmetrically.
3. **Independent assay and predictions:** in an appropriate human or other evidence-supported domain, specify a feasible physical intervention, state/context measurements and independently justified report or behavioral/physiological readout; distinguish a physical q proxy from a calibrated phenomenal target. Pre-register competing predictions and a held-out evaluation, report measurement uncertainty, control for attention, arousal and non-experiential downstream effects, and test whether a calibration transports. Demonstrating a causal effect on report alone does not prove numerical subject identity or qualitative identity.
4. **Integration:** show how the rule and its physical dynamics arise in the candidate's self-sufficient experiential whole, rather than adding the dynamics to both competing grounds by hand; address plurality and phenomenal persistence without asserting universal consciousness. Extend to the requested quantum, local-time and gravitational domains separately.

These are requirements, not a claim that the toy spin chain already models a nervous system or that a particular experiment has been performed. Evidence against a specified candidate prediction can be decisive for that candidate under its assay assumptions; data cannot by themselves establish an entire metaphysics. No value of `q` has been shown to be an actual string vibration or actual discomfort.

## 5. Prior work and source scope

Sensitivity of causal measures to spatiotemporal grain is **not a new general discovery**. Hoel, Albantakis and Tononi, [*Quantifying causal emergence shows that macro can beat micro*](https://doi.org/10.1073/pnas.1314922110), analyze effective information at spatial and temporal scales; its abstract and introduction were read, not the complete paper, proofs, figures or supplements. Hoel, Albantakis, Marshall and Tononi, [*Can the macro beat the micro? Integrated information across spatiotemporal scales*](https://doi.org/10.1093/nc/niw012), discusses selecting an integrated-information grain; search excerpts were inspected, while the publisher page extraction returned navigation only. Its full text, derivations, figures and supplements were not inspected for this audit. Oizumi, Albantakis and Tononi, [*From the Phenomenology to the Mechanisms of Consciousness: Integrated Information Theory 3.0*](https://doi.org/10.1371/journal.pcbi.1003588), explicitly postulates experience/structure identities and exclusion; the abstract and author summary were read for this audit, not the full article, mathematical derivations, figures or supplement. These are scope limitations, not claims that the full texts are inaccessible. IIT's measures and exclusion claims are not identical to L, and we do not import them as established phenomenal bridges or adopt their non-overlap postulate.

The concrete calculation above is a new **application within this repository's specified candidate**, not a claim of novelty for temporal-grain dependence in general. No exhaustive novelty search was performed.

## 6. Battery status and reproduction

The result strengthens the diagnosis of **B4/F2**: L needs a justified intervention/scale and a subject-identity law. It sharpens **B5**: the physical mismatch and even an experiential-ground label do not fix valence. Neither bridge is supplied, so both remain open; **full structural and experiential intelligibility** (C3) remains unmet jointly with the other criteria. The external foundation-battery preregistration, program and freeze artifacts remain unavailable for independent replay, and its admission conditions are not inferred from this test. The other gates, including modality, quantum physics, local time/gravity and measure, remain as in the [focused battery assessment](FORMAL_BATTERY_STATUS_AND_FOCUSED_RESEARCH_PLAN.md). This is a concrete negative/conditional result, not the non-incremental positive breakthrough needed for a battery pass.

Run `python verification/integrated_subject_horizon_audit.py`; its [receipt](verification/integrated_subject_horizon_audit.json) records exact rational influences and scores at horizons 1–9, 24 relabelings per horizon and the equilibrium mismatch transition law. It relies on the existing heat-bath and L implementations. A successful run checks the stated finite mathematical claims, not empirical subjecthood, felt quality, persistence, or the formal battery.
