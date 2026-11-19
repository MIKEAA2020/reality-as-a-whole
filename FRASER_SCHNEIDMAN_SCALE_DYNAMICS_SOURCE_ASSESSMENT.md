# Effective physical structure, collective activity and subject boundaries

> **Follow-up:** The earlier statement that recordings had not been obtained or replayed remains true, but an original-paper-associated 40-cell spike-train archive has now been found and its README and first text chunk inspected. The published Fraser chapter has also been identified. See [source follow-up](FRASER_SCHNEIDMAN_SOURCE_FOLLOWUP.md) for exact access, versions, and remaining limits.

## Sources and scope

The supplied files resolve two earlier abstract-only limitations:

1. James D. Fraser, **[“Towards a Realist View of Quantum Field Theory”](sources/uploads/Towards%20a%20Realist%20View%20of%20QFT%20draft%202.pdf)**, an 18-page chapter draft for *Scientific Realism and the Quantum*. We read text extracted from all pages and inspected the majority-rule blocking figure. The PDF is a **draft**, not verified against any final published chapter. SHA-256: `a53792b9c2f867e242249abe34c38753ee2492f08e0f801f54f9a807b832ce99`.
2. Schneidman, Berry, Segev and Bialek, **[“Weak pairwise correlations imply strongly correlated network states in a neural population”](sources/uploads/schneidman2006.pdf)**, *Nature*, [DOI 10.1038/nature04701](https://doi.org/10.1038/nature04701). We read the six-page journal article's extracted text and inspected its five main figures. SHA-256: `1221edc23d32c1086ac330102619d4f43de0fcb2c341b01aa8209b2237ca0267`.

Extracted text may contain symbol/font errors; reading is not an independent proof audit or data reproduction. The Nature page links three supplementary figure files. Their **captions** were retrieved, but the plots within them were not visually inspected. The study's raw recordings, analysis code and model fits were not obtained or replayed. Any numerical experimental statements below are the authors' reported results, not our reanalysis.

## 1. Fraser: real effective structure without a claim of ultimacy

Fraser addresses a tension: perturbative QFT produces highly successful predictions, while mathematical and interpretive questions remain about what exactly the corresponding theories describe. He discusses Wilsonian renormalization: a lower-resolution description can absorb the effects of inaccessible higher-energy degrees of freedom into effective parameters. In suitable regimes, different high-energy descriptions can yield very similar low-energy predictions and correlation structure.

His proposed **selective realism** is not “only predictions are real.” It treats some large-scale, non-fundamental structure as genuinely descriptive of reality, while withholding commitment to details that successful low-energy observations cannot distinguish. Nor does he claim that renormalization solves everything: the chapter acknowledges limited domains of rigorous results, concerns about unconceived alternatives, the challenge of characterizing non-fundamental ontology, and quantum interpretation and measurement issues. The quoted universality picture must not be read as a blanket theorem for arbitrary underlying theories or a completed construction of quantum gravity.

This strengthens a distinction in our proposal: a person, a particle or a record need not be fundamental to be physically real. But agreement between physical descriptions at an effective scale does **not** by itself establish that their realizations have identical experiences, or that either is the necessarily actual experiential ground. A proposed substrate-independence principle needs its own equivalence criteria and phenomenal bridge. An effective theory's cutoff is a modeling device or scale choice in the stated setting, not proof that spacetime is fundamental or that a temporal creation event occurred.

## 2. Schneidman et al.: strong collective patterns, with important limits

The authors record retinal activity and fit maximum-entropy distributions constrained by single-cell spike rates and pairwise correlations. Their main illustration contains 40 simultaneously recorded salamander retinal ganglion cells, binned in typical 20 ms windows; the methods describe 95 cells from four salamanders and 35 cells from two guinea pigs overall. They also analyze spontaneous activity in a cultured cortical network from another laboratory. These are biological measurements, but they are not recordings of subjects reporting conscious experience.

In the authors' analysis, an independent-cell model badly misses some collective patterns, even though many individual pairwise correlations are weak. A maximum-entropy model fitted to pairwise statistics performs much better for the examined groups; the reported roughly **90%** figure is the fraction of the chosen multi-information captured in the analyzed ten-cell groups, not a 90% accuracy guarantee for every pattern, brain, task or intervention. Commonly occurring pattern rates were reported as well predicted for their example. The comparison is observational; correlations may include common stimulus effects.

The paper makes three distinctions directly relevant to our previous toy gate:

- The fitted Ising `J_ij` parameters describe a **static maximum-entropy distribution**. They are not automatically synaptic strengths, directed causal effects or the intervention-specific weights of our graph.
- Fitted couplings include both signs; the paper illustrates frustrated triplets and reports roughly 40% of the triplets in its analysis as frustrated. This does not equate frustration with discomfort or any conscious quality. In particular, it does not justify our previous **all-positive ferromagnetic** assumption for a brain.
- The paper's discussion of roughly 200 cells is an **extrapolation** of trends from smaller analyzed networks, not a direct demonstration that exactly 200 cells form a subject or perfectly error-correcting system. In the reported example, sampled multi-information was estimated directly only for smaller populations, with further model-based analysis and extrapolation for larger sizes.

A good pairwise maximum-entropy fit in the reported settings neither proves that all higher-order effects are absent nor validates a particular dynamic heat-bath rule. Conversely, our earlier higher-order counterexample does not refute their empirically useful pairwise model.

## 3. A concrete correction to the previous intervention test

In [the previous note](COLLECTIVE_INTERVENTION_SUBJECT_CONTEXT_GATE.md) we derived a total-external-influence bound for an **assumed**, finite, ferromagnetic heat-bath dynamics with complete collective interventions. That derivation remains conditional as written. Schneidman et al.'s paper is evidence that a certain *static statistical model* can fit certain measured activity patterns; it is **not** evidence that its fitted parameters satisfy our intervention assumptions or certify a subject boundary.

The distinction can be made explicit with the exact same four-spin equilibrium distribution already used in the project. Keep the distribution and all local heat-bath resampling probabilities fixed, but change how often each spin is chosen to update in a fixed time bin:

```text
A: update probabilities (1/4, 1/4, 1/4, 1/4)
B: update probabilities (1/100, 49/100, 49/100, 1/100).
```

Both dynamics satisfy detailed balance with **the same complete 16-state equilibrium distribution**. Consequently they agree on every equal-time observable of that distribution, including all singles, pairs and higher-order moments. This is a standard consequence of allowing different state-independent update rates, not a new theorem about neural data.

Now specify a *different* intervention convention from the previous note: clamp input `j`, initialize target `i` to `−1`, randomize its other neighbors as before, run **one fixed random-site update** (a selected clamped site idles), and read the target. Define the directed graph weight by the difference between the two clamp conditions and symmetrize as previously. For this protocol the response is the old **target-selected** influence multiplied by the target's update probability.

| Dynamics | Edges `0—1`, `1—2`, `2—3` | `L` winners |
|---|---|---|
| A, uniform | `5/42`, `1/21`, `5/42` | `{0,1}`, `{2,3}` |
| B, faster central updates | `1/200`, `7/75`, `1/200` | `{1,2}` |

The [exact-arithmetic checker](verification/static_ising_kinetics_boundary_gate.py) verifies both stationary laws, detailed balance, intervention differences and selector results. It does not replay Schneidman's data or establish that this is a biological mechanism.

**Essential qualification:** under our *earlier* convention, which conditions on the target being selected for update, the two models have identical influences and the earlier result does **not** change. The new table uses a fixed-bin intervention convention. Its point is that equal-time data do not specify an update schedule or tell us which temporal/interventional convention captures a proposed subject. Time-resolved observations and suitable interventions can in principle distinguish these dynamics; this is not a claim of permanent empirical indistinguishability. Nor does either selector result establish that one, two or any subjects exist.

## 4. Joint implications for the whole

Fraser and Schneidman point in complementary directions. A useful effective physical description can be robust and real in its domain, but neither a good effective fit nor shared low-level statistical structure automatically identifies the same dynamics, subject or experience. For our relational, intrinsically experiential proposal, the required bridge is therefore more demanding than a common mathematical form:

1. State which physical preparations, timescales, counterfactual operations and observables the proposed description preserves.
2. Test the physical model against held-out temporal and multi-input interventions where feasible, rather than treating an equal-time Ising fit as intervention validation.
3. Define a candidate subject rule and test how it changes under justified coarse-grainings and time grains; if outputs differ, explain which description is constitutively relevant rather than silently selecting one.
4. Independently justify how the relevant physical organization is identical to an experience and how genuine plurality and qualities are fixed. A report, fitted distribution, effective field or minimum cut does not supply that identity by definition.

None of these papers derives a self-sufficient whole, necessary plenitude, emergent spacetime or a universal subject. Strong possibility=actuality remains a timeless thesis about the whole, not a physical event that selects or manufactures possible worlds. The sources constrain and improve our physical modeling while leaving those foundational questions open.

## Verification

Run `python verification/static_ising_kinetics_boundary_gate.py`; the [receipt](verification/static_ising_kinetics_boundary_gate.json) records the two exact finite-state checks. The shared equilibrium law and the computation are model facts under the specified update and intervention protocol; they are not a new result from the uploaded experiment, a full physical theory, or an experiential assay.
