# Organization through turnover: a finite comparison after Jaworski

## Result

A small exact model makes Jaworski's point about organization concrete: an arranged, actively maintained pattern can persist while every original component token is replaced. With three redundant sites, one-at-a-time replacement and ideal repair after each replacement, the original majority bit survives **all eight** possible sequences of three incoming bits. Without repair, under the same incoming sequences, it survives in **four of eight**. The difference is due to a specified change in operations, not a mysterious extra force.

This illustrates why the same inventory of components does not by itself explain a system's behavior. But because this model specifies the full site-level dynamics, it also illustrates that a real explanatory role for organization can coexist with a lower-level derivation. **It neither proves that biological organization is reducible to physics nor refutes Jaworski's hylomorphism.** It is not a biological system, an autonomously self-maintaining organism, or a model of experience. Its [plan](JAWORSKI_ORGANIZATION_TURNOVER_COMPARISON_PLAN.md) was retrospective, after Jaworski's examples and our prior assessment were known.

## 1. The setup

A system has three binary sites and a majority function `M`. Initially all sites contain the same bit, `b`, either `0` or `1`. Each site is carried by a distinct physical-token *label*; those labels distinguish old and new components in the bookkeeping. In order, sites 1, 2 and 3 are replaced with new tokens carrying bits `u₁,u₂,u₃`. These three bits are independent and fair in the probability calculations. The same initial state, replacement schedule and sequence of incoming bits are used for both arms:

- **Repair:** immediately after each replacement, set all three sites to the majority of their current values.
- **No repair:** replace each site, but leave the resulting values unchanged.

The repair operation is an idealized, externally specified controller; it is not derived from the sites, and it may reset not just the new token but other sites as well. The schedule, incoming-bit distribution, external resources, and ability to sense, decide and reset are assumptions. This is an abstract open-system computation, **not a demonstrated physical implementation or energy budget**. In particular the comparison does not isolate repair while claiming the complete physical conditions are identical: the control operations differ. It also does not establish that a biological organism has such a controller or that a living individual could survive wholesale replacement in three steps.

## 2. Exact comparison and a failure mode

For a unanimous start, any one replacement leaves at least two sites carrying `b`. The repair restores all three to `b`. By induction it does so after every replacement, independently of the incoming bits. At the end all three component-token labels are new. The functional pattern persists despite complete labeled turnover.

Without repair, the final sites equal `(u₁,u₂,u₃)`. Out of eight equally likely sequences, four have majority `b`, and only one has all three sites equal to `b`.

| Outcome after three replacements | Repair after each | No repair |
|---|---:|---:|
| Majority equals initial bit | 8/8 = 1 | 4/8 = 1/2 |
| All three values equal initial bit | 8/8 = 1 | 1/8 |
| Original component tokens still present | 0 | 0 |

These are probabilities only for the stipulated independent fair inputs. The repair success result for this schedule is stronger: it holds for **every** input sequence, not only under fairness. Retaining the pattern is not the same as retaining the particular original tokens. It is also not proof that a numerically identical organism or subject persists: those identities need their own criteria.

**Failure control.** Start at `000`, replace two distinct sites before allowing repair, and use independent fair incoming bits. If both new bits are 1, the intermediate majority is 1 and repair locks in `111`. That occurs with probability **1/4**. Thus repair depends on the rate and order of disruption relative to restoration. The ideal controller is not unlimited resilience.

## 3. When a macro-description is not closed

The majority bit alone is not always enough to predict the next majority. Both `000` and `001` have majority 0. Replace the first site with a fair incoming bit and do not repair:

- Starting at `000`, the next majority is 1 with probability **0**.
- Starting at `001`, the next majority is 1 with probability **1/2**.

Both starts have the same coarse value but different conditional future distributions. Therefore `M` alone is not an exact autonomous state description for this unrestricted replacement process: the hidden arrangement matters. This does not rule out a larger state description, an approximate closure under an appropriate distribution, or exact closure on a restricted set.

In the repair arm observed **after each repair**, and starting at `000` or `111`, the state stays in the two-state unanimous code space. On that restricted domain, `M` is constant after each completed cycle. That is an exact but conditional macro-law. It does not claim that an unrestricted system, intermediate time or a biological process obeys it. Compare the project's different [four-component diffusion construction](constitutive-reality-thesis.md#4-stable-parts-and-macro-laws-a-genuine-construction), whose aggregate law is exact for every microscopic initial state in its own stipulated model.

## 4. The environmental ledger

In the repair arm with initial `000`, all eight input sequences end in the same system state `000`; the final three sites alone cannot distinguish the histories. The [receipt](verification/jaworski_organization_turnover.json) records each incoming bit and pre/post-operation values, so the eight input sequences remain distinguishable **in that mathematical record**. This shows why loss of information from a subsystem description should not be silently described as loss from every possible larger description.

The ledger is bookkeeping, not a constructed physical reservoir or proof that recording can be done without disturbance or cost. We have not specified a physical implementation, microreversibility, heat flow, energy, entropy production, or Landauer bounds. An actual self-maintaining system would require a compatible controller, resources and a physically consistent treatment of the environment and its record capacity.

## 5. What the comparison does and does not settle

| Question | What this example shows | What it does not show |
|---|---|---|
| Is organization relevant? | Under these explicit operations the maintained organization changes the outcome relative to the no-repair comparison. | That every organizational description is fundamental, or that every disruption has the same effect. |
| Must the original material tokens persist for a pattern to persist? | Not in this model: every labeled token is replaced while the bit remains stable. | That every real organism survives arbitrary replacement, or that persistence of an organism is exhausted by this bit. |
| Can site-level dynamics entail an exact macro-law? | Yes, on the specified repaired code space. | A complete physical reduction of life, or that all macro-laws are exactly closed. |
| Does preservation of information settle experiential identity? | No experiential property is specified. | Whether the pattern has a subject, a particular feeling, or one continuous experiencer. |

The distinction between **system token**, **maintained pattern**, **organism**, **episode of experience**, and **subject** is crucial. For instance, one could copy the same stored bit into two separately labeled systems. Their common pattern would not itself determine whether either has experience or whether any subject persists. If the copies are genuinely distinct, a claim that each is *numerically identical* to one original would also require a nonstandard account of identity: ordinary transitivity would make the two copies identical to each other. That logical point does not determine what actually happens to experience in a branching case.

### Competing interpretations

A **physicalist organizational realist** can regard the maintained pattern and its causal organization as real while taking the stipulated site updates and controlling apparatus to be physically implemented. A **hylomorphic interpretation** can emphasize the real organizing principle and dispute whether an actual organism's unity and powers are exhaustively accounted for by physical descriptions. Both may accept that the toy has the outcomes above; neither ontology follows from those finite outcomes. Jaworski might also argue that this abstraction omits the very biological unity at issue. This comparison does not claim to formalize his complete account or show that his full theory is empirically identical to every physicalist one.

If two explicitly specified rival interpretations use the same operational model and predict the same outcomes, the enumerated outcomes alone cannot choose between them. If a proposed hylomorphic theory adds different measurable dynamics, then a clearly specified, controlled experiment could in principle distinguish those predictions, subject to model and measurement assumptions. A lack of any extra predicted force is **not** a refutation of hylomorphism; conversely, operational agreement alone cannot establish that an additional fundamental principle is needed.

Likewise, one may append different *stipulated* labels for subject count or quality to this same toy without changing its updates. That is a demonstration of underdetermination by this toy's physical specification alone, not a proof that all possible evidence about experience is useless. A defensible experiential theory would need a justified mapping and independently credible access or calibration, as well as a way to test rival mappings without defining the target by the same behavior used to predict it.

## 6. Next empirical and theoretical obligations

A subsequent [bacterial chemotaxis audit](BACTERIAL_CHEMOTAXIS_ORGANIZATION_AND_EXPLANATION_AUDIT.md) examines a real feedback subsystem, evidence for both robust adaptation and limitations, and the remaining metaphysical underdetermination; it is not a whole-organism or experiential model.

A genuine biological comparison must define a measured capacity and system boundary, model material and energy flows, and identify a repair or regulatory pathway that can ethically be perturbed. Compare a prespecified mechanistic account against alternatives with measured inputs and matched controls; test recovery, failure rates, and timing under interventions. Record off-target effects and resource costs. An artificial error-correcting device may be more controllable, but is not evidence about the phenomenality of an organism or a machine. A successful mechanistic explanation would help with organizational function; it would not, without further premises, settle whether that function is metaphysically fundamental or explain what it feels like.

For the project's experiential constitution, a next formal test is to specify candidate incidence and quality rules separately from the operational model, identify how the rules differ under feasible independently anchored observations, and explicitly allow unresolved ties or underidentification. Neither the phrase “dynamic structure” nor the label “self-maintaining” supplies that mapping. The framework's claims about a necessary timeless whole and the actuality of genuine possibilities are likewise not decided by this finite example.

## Reproducibility

[The enumerator](verification/jaworski_organization_turnover.py) uses exact rational probabilities and enumerates all eight paired three-bit inputs for both initial bits. It saves the [receipt](verification/jaworski_organization_turnover.json), including one operation history and the burst/hidden-state cases. [Five focused tests](verification/jaworski_organization_turnover_test.py) check an independent one-step analytic formula, binomial failure counts, exact turnover, retained input histories and the macro-closure counterexample. They passed, as did the existing symbolic constitutive check and 45 selected framework regression scripts. This is a constructed mathematical illustration, not a preregistered experiment, source-data reanalysis, thermodynamic theorem or experiential measurement. The source paper and its claims are assessed separately in the [Jaworski audit](JAWORSKI_2016_BIOLOGICAL_STRUCTURE_AND_FRAMEWORK_AUDIT.md).
