# Actuality, interventions and Bell experiments

## The issue

The framework takes seriously the user's claim that **genuine possibility in the strongest sense is actuality**. Under its previously stated unrestricted global interpretation, every actual global truth is necessary. That raises a consequential question for the rest of the research program:

> Can there still be informative experiments, causal comparisons and quantum-physical constraints if an alternative complete actuality is not genuinely possible?

**Yes, conditionally—but not for free.** Different experiments and different local situations can occur *within the one actual whole*. Empirical comparisons can concern those actual differences without saying that the same uniquely identified event genuinely happened two incompatible ways. Mathematical models can also evaluate substitutions not actually realized; their usefulness does not make those substitutions genuine possibilities or actual simulations. But interpreting a nonactual token-level intervention as a substantive counterfactual needs additional semantics and justification. The strong modality principle alone does not supply it.

This matters directly to the earlier color-filter example, the microtubule intervention proposal, subject-constitution tests, and the physics and measure gates. It corrects any impression that the phrase “possible intervention” in a model automatically means **genuinely possible** in the user's strongest sense.

## 1. Three distinct statements

Let `i` and `j` identify distinct local experimental occurrences within one complete actual whole, with setting `X` and record `Y`.

1. **Actual contrast:** occurrence `i` has `X=0`, and occurrence `j` has `X=1`. Both statements can be actual global truths together. Their outcomes can be compared, subject to controls on the differences between occurrences.
2. **Same-token counterfactual:** occurrence `i` in fact has `X=0`, but we ask what would have happened **at that same identified occurrence** if `X=1`. On the unrestricted strong interpretation, the full contrary token description is not genuinely possible. Its mathematical evaluation and its metaphysical truth are separate questions.
3. **Model substitution:** a specified mathematical rule `Y=f(X,U)` can be evaluated at `X=1` while its input `U` is fixed, even if that combination is not actual. The resulting number is a property of the rule. It is not an observation, a new occurrence, a real simulation, or a proof that the physical system would have produced that outcome.

Actual contrast does not, just by itself, identify the causal effect on one token: different cases can differ in hidden conditions or carryover. Randomization, controls, causal structure and transport assumptions can make comparisons informative, but none can be skipped merely because both cases are actual.

The user's principle does not itself provide a rule saying which model substitutions correspond to correct causal claims. In some familiar possible-world accounts of counterfactuals, an impossible antecedent makes the conditional vacuously true; alternative non-vacuous analyses are contested. See [SEP, Impossible Worlds](https://plato.stanford.edu/entries/impossible-worlds/) and [SEP, Causation and Manipulability](https://plato.stanford.edu/entries/causation-mani/). One may use non-vacuous mathematical or counterpossible reasoning without asserting that imagined worlds exist. But the identification of a mathematical output with a **true physical counterfactual** remains an additional interpretive commitment.

### A conditional, practical replacement

For empirical physics, define a **local actual-context rule** for a declared class of records and settings:

> Among the actual, adequately controlled occurrences in the class, the observed setting–outcome relationships follow the declared rule, within specified uncertainty.

This is an ordinary claim about actual occurrences. It can be false and experimentally challenged. It is weaker than the assertion that the rule correctly describes all unperformed interventions at a specific token, all contexts, or all members of an infinite mathematical domain. A theory can propose the stronger rule; evidence and defensible invariance assumptions are then needed to extrapolate it.

The previously calculated CIE pair and ideal filter illustrate **model substitution**, not two measured human episodes. If a real laboratory realizes two such sources at different positions or times and measures them, their records would be an actual contrast. Whether their original experiences match is a separate empirical and phenomenal question.

## 2. A concrete physics constraint: Bell correlations

Bell experiments give a nontrivial example where **actual records from different setting pairs** constrain a class of models. For settings `x,y ∈ {0,1}`, outcomes `a,b ∈ {−1,+1}`, and correlations `E_xy`, the established CHSH bound is

```text
S = |E_00 + E_01 + E_10 − E_11| ≤ 2.
```

For the standard locally causal hidden-variable model, the bound follows when a common distribution of hidden variables applies across setting pairs, and outcomes factor locally conditional on those variables. One common expression of the relevant setting-independence assumption is `P(λ | x,y) = P(λ)` for appropriately defined source-relevant `λ`, together with the local factorization and other experiment-specific assumptions. The bound is established literature, not a new derivation here; see [Hensen et al. (2015)](https://doi.org/10.1038/nature15759). A finite sample's estimate can exceed 2 by chance even under a null model; the finite-sample inference is statistical.

Hensen and colleagues reported **245** event-ready trials with stations about **1.3 km** apart, `S = 2.42 ± 0.20` and `p ≤ 0.039` for their stated local-realist null, using an analysis allowing memory in devices. This is their reported result, not a raw-data reanalysis. Their [second experiment](https://doi.org/10.1038/srep30289) reported 300 trials, `S = 2.35 ± 0.18` and `p = 0.061` under its complete analysis; the same group combined the runs in subsequent analyses. Do not substitute the second run's smaller conventional-analysis p-value for its complete-analysis value. “Loophole-free” refers to the addressed detection and locality issues under the experiment's assumptions, not the elimination of every conceivable dependence or statistical assumption.

These are local, operational spacetime and timing relations in an effective physical description. They do not introduce an external clock for the timeless whole, establish how spacetime emerges, or show that observation by a conscious subject causes collapse.

### Why a fixed whole does not automatically violate setting independence

Use the actual trial index `i` as a way to select records within one fixed collection; it is not an external time or a variable selecting another total universe. A deterministic collection could contain each combination of `(x,y,r) ∈ {0,1}³` once. Define the trial-level hidden variable `λ=r` and records `a=b=(−1)^r`. With equal weights on these eight indexed records:

```text
P(λ=r | x,y) = 1/2 = P(λ=r),  for both r and all x,y;
E_00 = E_01 = E_10 = E_11 = 1,  so S = 2.
```

Every listed record is fixed in this mathematical example, yet setting independence holds for the **specified trial-level λ**. Thus “all records belong to one actual whole” does not logically entail that the experiment's settings are statistically dependent on every relevant local hidden variable. It also does not prove that independence holds in a real experiment. Probabilities here are normalized frequencies over this stipulated finite collection, not a derived fundamental measure on all subjects or the whole.

One must define `λ` and the sampled index carefully. If `λ` is taken to include the settings themselves, setting independence fails trivially; if it is a constant encoding the whole, treating it as the only trial-level variable can hide relevant dependencies. The Bell premise is about the distribution of **appropriately specified variables across the experimental trials**, not whether the one totality is caused by something external or whether an experimenter has libertarian free will.

### Conversely, determinism does not establish independence

As an algebraic control, index eight records by `(x,y,r)` again, but let `λ=(x,y,r)`, and use local response functions with `a=(−1)^r` and `b=(−1)^(r ⊕ xy)`. Each setting pair occurs twice and both local marginals are balanced; the resulting correlations have `S=4`. The full hidden variable contains the settings, so `P(λ|x,y) ≠ P(λ)`. This deterministic, no-signalling-at-the-level-of-marginals table is a **formal superquantum example**, not a physical model or a claim about the Hensen apparatus. It illustrates why measurement dependence can evade the usual bound even when observed local marginals look innocent.

More generally, whether a specific setting-dependent local model can reproduce quantum correlations with acceptable simplicity, dynamical explanation and independent empirical constraints is a substantive research question. Such a model cannot be inferred from modal necessity, nor ruled out simply by asserting metaphysical free will. See the discussion and explicit setting-dependent model in [Ciepielewski, Okon and Sudarsky](https://ar5iv.labs.arxiv.org/html/2008.00631); the authors themselves raise substantial objections to their model's simplicity and viability. A candidate must identify its hidden variables, explain their dependence on settings, and meet the same predictive and calibration standards as its rivals.

## 3. What this does—and does not—contribute to the experiential foundation

The constructive gain is a compatibility constraint on the larger framework:

- The strongest possibility–actuality principle does not erase actual local variation or automatically turn empirical inference into a mechanism that actualizes possibilities.
- Its unrestricted version does make the interpretation of same-token counterfactuals more demanding. Actual comparisons, extrapolated model rules and strong metaphysical counterfactuals must not be conflated.
- Recorded Bell correlations impose conditional, experimentally grounded constraints on local factorizable physical models. A proposed experiential whole must recover the observed correlations **with explicit assumptions**, not simply announce that all results are already actual.
- Neither Bell violation nor the existence of actual reports identifies physical structure with experience, establishes one universal agent, or selects an experiential ground over a neutral ground. A subject/report interface remains an independent requirement.

This also exposes the measure problem in a concrete form. A normalized frequency over a specified finite set of actual laboratory records is unproblematic arithmetic. An experimental p-value additionally uses a declared statistical null and sampling/randomization model; it is neither the probability that the null is true nor automatically a fundamental chance assigned by the whole. A measure over all subjects, experiences or sectors remains unjustified. A completed theory must explain which statistical and causal assumptions are warranted in the contexts where they are used.

## 4. Revisions to how previous constructions should be read

- The idealized filter operation in [the color example](COLOR_METAMER_PHENOMENAL_PHYSICAL_BRIDGE.md) is a mathematical operation on a model. No exact filter or synthetic pair was tested on humans. Actual trials with different filters would give local records; extrapolation beyond them adds assumptions.
- The `do(Q)` and `do(S)` manipulations in the [microtubule gate](MICROTUBULE_QUANTUM_CAUSAL_DISCRIMINATION_GATE.md) specify mathematical intervention contrasts in stipulated models. They are not evidence that every contrast is physically feasible or genuinely possible, and they do not establish a quantum effect on conscious experience.
- The adopted global strong possibility schema remains **unproved**. This note does not derive self-sufficiency, experiential intrinsic nature, local time, Bell correlations from first principles, a quantum-gravity theory, a universal subject, or a measure. It prevents a modal commitment from being mistaken for either a refutation of experiments or a solution to those gates.
