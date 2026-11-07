# Separating content maintenance from broadcast: a controlled intervention audit

## Direct result

A distribution lesion in the existing workspace model is **not a pure intervention on access**: it also removes feedback and can change later selected content. A fixed replay can match one trajectory without preserving the counterfactual organization. A new content-sensitive feedback replacement preserves a precisely declared **reduced core transition law** while keeping distribution disabled.

This supplies an explicit way to formulate a discriminating comparison between maintenance-sufficiency and distribution-necessity hypotheses. It does not select either as true, identify a phenomenal episode, or establish a neural intervention.

## 1. Why this matters for the constitution programme

The recurrent-access candidate combines content maintenance with distributed use and feedback. To determine what belongs to constitution, one must distinguish the roles rather than infer necessity from a lesion that changes several at once.

Two restricted rival hypotheses are useful:

- **H_M:** an independently identified content-maintaining organization is sufficient for the anchored experiential organization; additional distribution to consumers is not constitutive in that domain.
- **H_D:** distribution into specified multiple consumer uses is additionally necessary for that experiential organization.

These are proposed comparisons, not exhaustive definitions of consciousness theories. H_D is not asserted to be the position of every version of GWT. H_M does not assume that every isolated memory register is conscious.

The narrow question is whether an intervention can preserve the basis asserted by H_M while removing the extra feature asserted by H_D. Without specifying that preservation, an outcome cannot discriminate the hypotheses cleanly.

## 2. The physical model and declared reduced core

Reuse the existing [workspace model](research/realized_workspace/model.py). Its state includes workspace content W, consumer memory M, and selection feedback F. On each step, candidate content is selected using current F; the selected content is distributed to consumers when gate B is enabled.

For this audit only, declare the reduced core

    C = (W, F).

Its update has the form

    W' = S(W, F, input, entry/maintenance settings),
    F' = source(W') if W' exists and feedback and action are enabled,
         None otherwise,

in the ordinary configuration with B enabled.

Consumer memory, action, comparison, report, and the detailed physical feedback pathway are not included in this reduced core. That omission is explicit and hypothetical. No argument here establishes that C is a sufficient phenomenal basis. If one of the omitted structures is constitutively relevant, the comparison must be enlarged accordingly.

## 3. The ordinary lesion is confounded across time

Prepare an auditory content. In the normal and distribution-disabled conditions, the current workspace content and report match.

But in the normal case, the action-supported feedback records auditory. In the disabled case, it is absent. At the next equal-salience competition:

- normal feedback makes auditory win;
- the lesion restores the model's visual tie winner.

Thus the intervention changes the proposed maintaining core's subsequent evolution, not only its consumer access. The earlier model already displayed this functional effect. The present audit makes its consequence for candidate discrimination explicit.

If a later experiential contrast changed under such an intervention, H_M could attribute it to changed core dynamics, while H_D could attribute it to loss of distribution. That observation alone would not identify the constitutive role.

Conversely, matching the first report would not establish preserved qualitative character or unity.

## 4. Fixed replay is not counterfactual preservation

Suppose a replay supplies the auditory feedback value recorded in the normal baseline. The reduced state can now match the baseline despite the lesion.

Force the workspace instead to visual content:

- the normal system updates feedback to visual;
- the fixed replay continues supplying auditory.

The baseline match therefore conceals a difference in how the system responds to an allowed perturbation. A trajectory is not its full transition structure.

This is directly relevant to neural replay arguments: reproducing a recorded signal does not by itself reproduce the original process's organization or response repertoire. It does not show that every possible replay is phenomenally inadequate; the question is what the replay preserves.

## 5. A content-sensitive replacement

Construct a new feedback route that reads the actual current workspace content and supplies

    F'_replacement = source(W')

when the ordinary feedback/action conditions permit it, otherwise None. Keep B disabled, so the original memory, action, and comparison consumers remain disconnected from current content.

In the software audit, this is an explicitly implemented post-update feedback controller. It is not a discovered neural implementation or an extra phenomenal force.

### Conditional transition-equivalence proof

Given equal initial reduced states, the same local inputs, and the same declared entry/maintenance/workspace interventions:

1. The ordinary and replacement systems compute W' from the same W, F, and input.
2. Their W' therefore agrees.
3. The replacement computes the same reduced F' function that the ordinary system computes with B enabled.
4. Their next reduced state C' agrees.
5. Induction yields equal reduced-state trajectories for every sequence of those declared inputs and interventions.

This argument is general for the stated transition equations. The finite checks below verify the implementation on a declared domain; the general conclusion is not inferred from their number.

The comparison allows other consumer outputs to differ. In the baseline witness, ordinary action and comparison are present while both are absent under replacement, despite matching C and matching report.

## 6. What the replacement does not preserve

This is **not full physical equivalence**. The ordinary route passes through distribution and action; the replacement uses a different path. An intervention on an omitted internal consumer variable need not have the same effect in the two implementations.

The proof establishes a reduced controlled-transition equivalence for the declared local intervention family. It does not establish equivalence of the entire localized state/dynamics/intervention structure required by the stronger realized-process candidate.

One must therefore defend why the reduced organization is sufficient, rather than treating its stipulated boundary as already the phenomenal boundary. A new controller could itself become part of a larger constitutive organization. The experiment's physical realization must be examined before claiming that it removed all relevant broadcast or recurrent access.

This distinction prevents the repair from becoming a disguised identity assumption.

## 7. Predictions and the remaining evidence problem

Subject to their explicit sufficiency/necessity commitments:

| Intervention | H_M | H_D |
|---|---|---|
| Distribution lesion without core preservation | May change experience through altered core dynamics | May change experience through loss of distribution |
| Fixed replay matching one baseline | Does not guarantee preservation under perturbation | Does not restore the required distribution |
| Proper core-preserving replacement, distribution genuinely absent | Predicts preservation of the anchored experiential organization | Predicts failure of the distribution-dependent experiential organization |

The third row is discriminating only if the claimed preservation and absence are established in the actual implementation and domain. In the software construction, the preservation is only the reduced equivalence just proved.

The direct report can remain intact in both physical conditions. It is not an automatic referee between the experiential predictions. Its evidential reliability under the intervention requires a model and independent warrant; otherwise a preferred theory can be selected by assuming report faithfulness or unfaithfulness as needed.

Likewise, a changed response or task performance is not automatically a changed experience. Empirical content and incidence evidence remain necessary. No such evidence was generated here.

## 8. Relation to the primary neural timing audit

The [timing audit](NEURAL_TIMING_CONSTITUTION_AUDIT.md) separated an intrinsic boundary from an analysis-derived threshold crossing. This audit adds a parallel causal requirement: preserving a measured content signal is not automatically preserving its sustaining organization.

A responsible empirical comparison needs both:

- a calibrated observation relation between neural records and the candidate process;
- an intervention model specifying which state, dynamics, and counterfactual powers remain intact.

A model trained to reproduce stimulus-duration correlations alone cannot establish either preservation claim. The inspected COGITATE code and protocol do not themselves implement the intervention described here, and no result from those sources is being attributed to this audit.

## 9. Verification

[The audit script](verification/workspace_intervention_audit.py) imports only the repository's own workspace model. It executes the lesion and replay witnesses, a multi-step report-disabled comparison, and 64,800 one-step comparisons covering:

- 75 syntactically valid prepared model states;
- nine declared proposal sets;
- 16 entry/maintenance/action/feedback configurations;
- six workspace intervention choices, including the unforced case.

These prepared states are allowed by the model's state constructor; no claim is made that all arise naturally from one unperturbed initial condition. The finite proposal set does not exhaust every numerical salience choice. The transition-equivalence argument above identifies why the result extends within the stated model and intervention interpretation.

[Diagnostics](verification/workspace_intervention_audit.json) record the exact witnesses and scope. The count is a number of finite comparisons, not additional consciousness tests or empirical confirmations. This script is separate from the 43-folder research runner, whose established total remains 1,149 tests.

## 10. Current result for the complete constitution

The central new constraint is:

> A proposed separating intervention must preserve the rival's declared constitutive basis across its relevant counterfactuals, not merely match a baseline trajectory or one signal.

This improves the design of a candidate test. It does not discover Gamma or chi. The leading common-constitution architecture remains plausible, and the question whether maintenance, distributed access, or a richer intrinsic organization is constitutive is now more sharply specified.

The next empirical target is not merely showing that a neural feature persists or disappears. It is establishing a genuinely separating intervention and warranted experiential contrast, while defending the proposed physical basis. If that cannot be established, the alternatives remain unresolved rather than one being selected by synthetic labels.

Related: [constitution programme](CONSTITUTION_RESEARCH_PROGRAMME.md), [workspace candidate](WORKSPACE_TOGETHERNESS_CANDIDATE.md), [realized-process sufficiency](REALIZED_PROCESS_CANDIDATE.md).
