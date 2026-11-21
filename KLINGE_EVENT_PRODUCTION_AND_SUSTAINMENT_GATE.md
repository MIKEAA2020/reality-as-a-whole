# Klinge: producing an event is not the same as sustaining it

## Result

Klinge proposes that a longer conscious state is sustained by repeated causal production of short phenomenal events. In a deliberately simple temporal model, **a produced event can remain active after its specified producing base has disappeared**. Repeated production therefore does not, by itself, entail that the base accompanies every active part of every event. The distinction survives an additional model restriction requiring events to occur successively rather than overlap.

This is a conditional clarification, **not a refutation of Klinge’s theory**. His account can prohibit the illustrated histories, posit that the event terminates with its base, or interpret the relevant dependence differently. Each response needs an explicit condition beyond “the event is short-lived” and “the base produced it.” Nor does the finite model establish that experiences really come in fixed-duration events.

## 1. The textual question

In [*Panpsychism and the Emergence of Consciousness*](https://doi.org/10.1007/978-3-662-62258-2), printed pp. 74–75, Klinge contrasts ordinary causal products that can survive their cause with an emergent `E` that vanishes if its base `B` ceases. On pp. 91–92 he characterizes emergence as producing and sustaining its result, but then distinguishes short phenomenal events from a longer phenomenal state. His proposed resolution is that an event, once produced, can exist independently for roughly **100 ms**, while a continuing state consists of a succession of events and depends on their continuing production. On p. 182 he qualifies the survival of longer experiences in terms of **functional disintegration** of a base, allowing its microscopic constituents to be replaced.

These passages invite a question, not a quick declaration of inconsistency: **is the dependence thesis about each individual event throughout its duration, about a longer series, or about the continued functional organization rather than particular constituents?** The second and third interpretations may be intended; they are not identical to instantaneous dependence of each event on a particular base.

The model below concerns accompaniment by one **specified functional base**, represented by a bit. It does not formalize Barnes’ broader definition, quoted by Klinge on p. 74, under which dependence concerns accompaniment by *some* other concrete contingent objects. Loss of the specified base would not by itself show absence of all concrete objects, or failure of that broader definition. Nor does it decide which entities constitute the actual base. The previous [Klinge audit](KLINGE_EMERGENT_PANPSYCHISM_AND_CAUSAL_CLOSURE_AUDIT.md) records the uploaded book’s bibliographic details and selected-reading scope. This follow-up additionally examined selected portions of §§4.4–4.7 and 7.2.2; it is not a full-book audit.

## 2. A fixed, deliberately limited model

The [plan](KLINGE_EVENT_SUSTAINMENT_FIXED_PLAN.md) was written before the initial enumeration. Use finite local time slots and a chosen duration `d≥1`; these are modeling conventions, not an external clock or a measurement of experience.

- `B_t=1` means the **specified functional base** is present in slot `t`.
- `P_s=1` means a candidate event starts in slot `s`; production requires `P_s≤B_s`.
- Each started event remains active for `d` slots, without early termination. The coarse indicator `E_t=1` means **at least one** produced event is active in slot `t`.

There are no births before the first observed slot in the finite-horizon calculation. These are formal assumptions. A bit does not produce consciousness; the event label does not create or identify a subject; and a continuing indicator does not establish phenomenal unity.

### Simplest unrestricted comparison

First suppose `P_t=B_t`, and consider a complete window of `d` production slots. Then

```text
E_t = OR(P_t, P_{t−1}, …, P_{t−d+1}).
```

If `d=1`, `E_t=B_t`. If `d≥2`, choose `B_t=0` but a prior `B=1` within the window: an event is still active even though the specified base is now absent. Exactly `2^(d−1)−1` of the `2^d` formal windows have `E_t=1, B_t=0`: the current bit must be zero and at least one earlier bit one. For `d=3`, this is **3 of 8** formal windows. These are counts of mathematical inputs, **not** probabilities of real events or claims that every history is possible.

For `d≥2`, two windows can have the same present `B_t=0` but different `E_t`, depending on whether there was an earlier start. Thus a current **base-presence bit** does not determine event occupancy. This is not a failure of supervenience on a complete physical state: a complete state might retain the relevant history or an event-supporting trace. `B` is not claimed to be such a complete state.

The assumption `P=B` can produce overlapping event tokens when `d>1`. Klinge speaks of **successive** events; applying this first model to him would need further justification. Therefore, after inspecting the first results and before calculating the additional strata, the plan was amended to check nonoverlapping starts separately.

### A sequential-event control

Take `d=3` and the following six-slot formal history, allowing `P≤B`:

```text
slot:             0 1 2 3 4 5
base B:           1 1 1 1 0 0
event starts P:   1 0 0 1 0 0
active events:    1 1 1 1 1 1
```

The first event occupies slots 0–2 and the second 3–5; they **do not overlap**, and each starts while the base is present. Nevertheless the second event is still active in slots 4–5 after the designated base has ceased. This is an admissible history of the **toy**, not a claim that Klinge’s causal laws or nature permit the actual base to disintegrate in that way.

The example also separates an unbroken activity indicator from a **single event**: two events produce a continuous sequence of ones. Continuity of the indicator cannot itself decide whether the events belong to one experiential field, one subject, one continuing person, or none of those. Those relations require an independently justified incidence or lineage rule, as emphasized in the [episode-incidence](EPISODE_INCIDENCE_REFORMULATION.md) and [field-lineage](FIELD_LINEAGE_PERSISTENCE_AND_FISSION_GATE.md) analyses. This qualification does not deny experienced temporal unity.

## 3. What additional condition repairs simultaneous accompaniment?

Within the model with `P≤B` and untruncated events, requiring `E_t⇒B_t` throughout a finite observed horizon is **equivalent** to requiring that each event’s active slots inside that horizon are all covered by the specified base:

- If an active event has a slot with no base, `E=1` and `B=0` there.
- If every event’s active slots are base-covered, any slot with `E=1` necessarily has `B=1`.

This is an elementary equivalence for the defined variables, not a metaphysical principle. It gives Klinge a precise conditional repair: ensure each base lasts through every event it produces, or use another law that brings event activity to an end when the base ceases. The latter changes the untruncated-event model; it may be a **causal** termination mechanism and need not be a separate metaphysically primitive sustainment relation. Alternatively, the dependence claim could apply only to an appropriately defined longer state, or to some broader supporting reality rather than the particular functional base. Each choice changes what must be explained.

The [checker](verification/klinge_event_sustainment.py) exhausts six-slot histories with `(B,P)∈{(0,0),(1,0),(1,1)}`—**729** histories for each duration. It verifies the equivalence above for each history. As a post-result control it restricts starts to be at least `d` slots apart:

| Event duration in slots | Nonoverlapping histories | Base accompanies activity at all observed slots | Of those, events extend beyond the horizon |
|---:|---:|---:|---:|
| 1 | 729 | 729 | 0 |
| 2 | 448 | 239 | 70 |
| 3 | 352 | 161 | 64 |
| 4 | 304 | 137 | 61 |

The final column matters: passing the **observed six-slot** check does not establish coverage after the recording ends. The numbers are finite combinatorial counts, not observations, base-failure rates, estimates of subjects or scientific evidence for a particular temporal grain.

## 4. Implications for the framework

The useful distinction applies symmetrically to competing proposals:

1. **Past causal production** answers what brought a modeled occurrence about. It is not automatically the same as a presently necessary constituent or support.
2. **Continuous local activity** can be defined from a succession, but a first-personal field and its temporal unity are not obtained by naming the resulting Boolean sequence an experience.
3. **A persisting person** is a further question about identity or lineage, not the numerical identity of distinct event tokens. The framework should not manufacture extra subjects merely by changing time windows.
4. **A timeless whole** need not undergo a global production process. If local causal emergence is considered within it, local ordering, the base/event relation, and any connection to felt succession must still be specified and justified.

Klinge’s causal-emergence proposal remains a serious experience-respecting rival. It offers a way to avoid literal subject-summing but posits microphenomenal powers and a production law; the field-first candidate instead owes a warranted incidence and quality bridge. Neither has been shown to give full structural **and experiential** intelligibility. This calculation supplies no physical `q` assay, subject count, empirical timing result or substantive battery pass: C3, B4–B5/F2, B9/F3 and B10 remain open.

## 5. Reproduction

```sh
PYTHONPATH=verification python -m unittest -v klinge_event_sustainment_test
python verification/klinge_event_sustainment.py
```

The [receipt](verification/klinge_event_sustainment.json) contains counts and explicitly formal example bit sequences, not participant data. Tests cover base loss, one-slot support, overlapping and sequential events, finite boundaries, invalid inputs and exhaustive finite equivalence. The [previous causal-interface check](verification/klinge_causal_emergence_interface.py) is separate; neither script tests Klinge’s metaphysical premises or any real neural process.
