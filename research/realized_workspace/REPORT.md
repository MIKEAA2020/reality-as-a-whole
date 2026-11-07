# Step 41 — A minimal implemented global-workspace access architecture

## Result

A small executable causal model realizes specialist competition, selective workspace entry, maintenance, multiple distinct uses, control feedback, and a separate report route. It distinguishes global functional availability from mere storage, a passive copy, and a matching readout.

Two interventions give a functional double dissociation:

- block report: memory, task action, comparison, and control feedback remain available;
- block distribution: the stored content and readout remain, but the other consumer uses and their feedback disappear.

This is a GWT-directed **architecture test**, not evidence that the model experiences anything. It is not a detailed neural global-workspace model, a simulation of ignition, or a test of every version of GWT. The model is implemented in Python; that does not establish that its program variables instantiate a phenomenally sufficient physical organization.

## 1. What is implemented

Two specialists, named visual and auditory, each supply a binary local content and a salience. Those names identify input channels; no actual seeing or hearing is assigned to them.

The model has:

1. **competitive selection:** a single candidate wins entry using salience and a declared control bias;
2. **one-slot workspace:** selected content is retained in the absence of new input when maintenance is enabled;
3. **memory consumer:** stores the available content;
4. **action consumer:** applies either a copy or invert rule supplied by the task context;
5. **comparison consumer:** compares the same content with a supplied target;
6. **control feedback:** a successful action biases the next selection toward the previously used specialist;
7. **report channel:** separately enabled or disabled;
8. **passive monitor:** copies workspace state but has no outgoing causal role in the declared transition law.

The feedback bias is .25 salience units; the tie rule favors the visual channel. These are explicit toy parameters, not derived neural constants or a constitutive threshold. One-slot capacity and the discrete update schedule are also stipulated. A different GWT implementation could use different mechanisms.

The consumers are separate causal variables and update functions within the model, not independent empirical specialist brains. Their access is tested by interventions. The construction is richer than a buffer that merely contains several labels, but remains a deliberately small functional architecture.

## 2. Update equations and interventions

Let w be the selected or maintained content, b the distribution gate, and g the report gate. On an available binary value v:

\[
\text{memory}'=w,\qquad
\text{action}=f_{\mathrm{task}}(v),\qquad
\text{comparison}=1[v=\text{target}],\qquad
\text{report}=v.
\]

The first three updates require b=1; report instead requires g=1. If no content is distributed, the existing memory is retained rather than overwritten with a fictitious content. Retained memory alone does not make current action/comparison available in this model.

Action feedback records the contributing specialist when the route is enabled and action occurs. It changes subsequent competition, so it is a causal loop through time rather than a passive transcript. Strong enough new input can override the feedback bias.

The entry gate, distribution gate, maintenance, report, action, and feedback can each be interrupted. Surgical interventions can also set the workspace or monitor independently. These operations are explicitly in the toy intervention domain; clean corresponding interventions in an actual brain are not assumed to exist.

## 3. Exact functional dissociations

For a fresh state, present visual value 1 with salience 2 and auditory value 0 with salience 1. Use the copy task and comparison target 1.

| Condition | Workspace/readout content | Memory update | Action | Comparison | Report |
|---|---|---|---|---|---|
| Normal | visual 1 | visual 1 | 1 | true | 1 |
| Report disabled | visual 1 | visual 1 | 1 | true | absent |
| Distribution disabled | visual 1 | none from fresh memory | absent | absent | 1 |
| Entry disabled | absent | none from fresh memory | absent | absent | absent |

Local specialist values remain available in the local-output record when entry is disabled. The model therefore distinguishes local discrimination from workspace entry and distributed use.

The normal and distribution-disabled conditions have identical workspace state, monitor value, and report in this example. Their broader consumer outcomes differ. Thus those readouts alone cannot identify functional global availability in the declared domain.

This is not an empirical example of unconscious truthful report. The model has no phenomenal target variable. It is a physical/functional counterexample to equating a particular matching readout with the entire access architecture.

## 4. Source versus passive representation

Forcing the workspace from visual 1 to auditory 0 changes memory, action, comparison, report, and the source used by feedback, without changing the original specialist proposals.

Forcing the passive monitor to auditory 0 changes the monitor but none of those outputs or the next causal state. Its ordinary agreement with the workspace therefore does not establish equivalence under the intervention domain.

This is the realized-process distinction sought in the synthesis: a description or copied value does not acquire the source's functional role merely by matching it. Conversely, the model does not prove that a differently implemented system with the same complete causal architecture would differ phenomenally. It makes no substrate-independence or biological-exclusivity verdict.

The report route itself is causally effective. Calling it a report does not make it phenomenal evidence by definition, and calling the monitor passive does not establish that passivity rules out every possible experience. Those would be extra constitutive claims.

## 5. Flexible use and recurrent control

The same workspace value supports different action rules without changing its content: copy yields 1 and invert yields 0 in the baseline. A comparison target change alters the comparison outcome without altering the selected content. Both specialists can supply the content in the finite task family.

A selected auditory content produces control feedback. At the next equal-salience competition, auditory wins. Disabling feedback restores the declared visual tie winner. Disabling the distribution route prevents the action-generated feedback, so the later choice changes even when the earlier report was identical.

These are limited instances of context-sensitive distributed use and return influence, not general intelligence or demonstrated human conscious access. The architecture contains no model of rich semantic understanding, neural ignition, variable binding, or a continuum of perceptual qualities.

## 6. What this contributes to the candidate unified account

The proposed architecture can give content to one part of the account:

> An actual selected content participates in a common functional organization when it can be used by multiple relevant processes and can affect their ongoing coordination—not merely because a register displays its label.

This is a definition and implementation of the claimed **functional availability**. It is not yet a definition of experience. The active causal role explains the modeled coordination, task use, maintenance, and feedback without an additional inner reader or homunculus.

The wider non-additive hypothesis can now be stated more concretely: perhaps phenomenal access is constituted by an appropriately realized organization of this kind. The model does not establish that identity. Its remaining obligations include:

- independently warranted evidence linking this functional access to a specified phenomenal contrast;
- whether broadcast, recurrence, or maintenance is necessary or sufficient in the claimed phenomenal domain;
- why a selected content has a particular qualitative character;
- why coordinated consumers belong to one episode or subject;
- which implementation differences preserve constitution;
- actual physical law and realization, and the ultimate explanatory foundation.

One workspace slot does not prove one subject. A report lesion does not prove experience persists. A distribution lesion does not prove it disappears. Those claims must not be read into the test names or outputs.

## 7. Comparison with the earlier exclusion proxy

No integration score is used. The distinctions are derived from the causal role of signals under the specified interventions. A physical weak link does not automatically count as global availability; its actual ability to carry content into the relevant task/control organization would need to be modeled.

This better matches the immediate source/monitor, content/use, and access/report questions in the synthesis than the earlier finite exclusion proxy. It is not comparative empirical evidence that GWT is true or IIT false. The two models address different explicitly declared mechanisms and neither establishes qualitative constitution.

The earlier episode-first buffers were storage/readout hypotheses. This model adds the distributed uses and feedback they lacked; it does not retrospectively turn those earlier tests into GWT evidence.

## 8. Verification and status

`model.py` implements the transitions and interventions. Twenty-four tests check competitive entry, both input sources, maintenance, flexible task use, report/distribution dissociation, preserved local discrimination, workspace-versus-monitor interventions, selective consumer lesions, and next-step feedback. `enumeration.json` records the main conditions and intervention signatures.

All labels describe functional model variables. No conscious/unconscious truth labels or scalar consciousness score are supplied. Passing tests confirms the declared architecture and its counterfactual distinctions, not empirical GWT, phenomenal identity, or the completed unified account.
