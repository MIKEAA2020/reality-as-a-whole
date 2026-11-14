# Can experiential organization do the work of a physical basis?

## Aim and result

A promising way to advance the self-existent experiential-whole proposal is to stop asking only whether experience *could* be fundamental and ask a more demanding constructive question:

> Can an independently specified organization of actual experiential distinctions carry the physical relations and local regularities we need, without an additional independently varying neutral state?

There is a precise conditional answer. For a specified physical model, if its relevant observable quantities and internal transitions factor through a proposed experiential organization, that organization can carry an **operationally complete description of that model**. The construction does not require a second physical state to generate its predictions. If the factorization fails, the proposed experiential organization is too coarse for that role. It may be repaired by an independently warranted richer experiential organization, or the proposed model must be abandoned.

This is a **sufficiency criterion, not a proof of experiential ontology**. Operational completeness does not prove that the physical structure is constituted by experience, that the experiential organization is self-existent, or that the real world satisfies the criterion. Conversely, failure for one coarse description does not refute a richer experiential whole.

The mathematical ingredient is established, not a new discovery: deterministic state quotients and, for finite Markov chains, Kemeny and Snell's [lumpability criterion](https://www.math.pku.edu.cn/teachers/yaoy/Fall2011/Kemeny-Snell_Chapter6.3-4.pdf), theorem 6.3.2. [Shalizi and Crutchfield](https://csc.ucdavis.edu/~cmg/compmech/pubs/cmppss.htm) develop predictive causal states and minimal sufficient statistics; their predictive result must not be confused with proof of metaphysical grounding. The contribution here is to apply these ideas as a **two-sided constraint on this particular whole-account**, and to distinguish dynamical economy from constitution.

## 1. Set up without an external clock

Take a specified, finite model of a **local relational situation inside the whole**. Its states form a set `X`; these are modeling labels, not independent universes. A transition represents one defined local step or relation between records, not the passing of time outside the timeless whole. Let:

- `q : X → S` assign each state its proposed relevant experiential organization. `S` is not just an arbitrary list of numbers: for the intended ontology, its distinctions must be independently claimed to correspond to real qualitative or subject-organizational distinctions.
- `F : X → O` give the modeled physical observable or family of observables.
- `T_a : X → X` give the transition for each specified setting `a`. The settings may represent allowed internal operations; they do not assume anyone can directly intervene on experience itself.

Write `x ~ y` when `q(x) = q(y)`. The construction asks whether the same observable and successor distinctions are determined by the organization `q`, not whether humans can currently measure them.

### Exact criterion

There are maps `f : S → O` and `t_a : S → S` satisfying

```text
F = f ∘ q                  q ∘ T_a = t_a ∘ q    for every specified a
```

on the image of `q` **if and only if**, for all model states `x, y`:

```text
q(x) = q(y)  implies  F(x) = F(y),
q(x) = q(y)  implies  q(T_a(x)) = q(T_a(y))    for every specified a.
```

The first condition says that the physical quantity factors through the proposed organization. The second says that the organization remains well-defined after each modeled operation. When both hold, one may set `f(q(x)) = F(x)` and `t_a(q(x)) = q(T_a(x))`; the conditions make those definitions independent of the choice of representative. Conversely, either factorization immediately gives the corresponding condition. Only the image of `q` is needed; unused elements of `S` are irrelevant.

By induction, any finite sequence of the specified operations and the resulting `F` outputs can be reproduced from `q(x)` alone. This is a coherent **operational construction**, not a claim that the map has been found for actual physics or that phenomenal character is reducible to numerical labels. With more observations, input settings, or different accessibility assumptions, the test must be run again.

This exact one-step closure is a useful sufficient construction, but it is **not necessary for every possible experiential account**: non-Markovian laws, relational histories, a different coarse-graining, or a relevant organization that includes memory may also reproduce physical records. In particular, failure of this specific `q` does not show that all experiential accounts fail.

## 2. A worked construction and a control

Assume, for the toy only, that an actual experiential organization has two separately distinguishable features with values `a,b ∈ {−1,+1}`. These values are **labels for stipulated phenomenal distinctions**, not a claim that experience really consists of binary bits. Let the modeled physical quantity be the jointly specified readout `F = a+b`. Suppose a local operation transforms both features as `(a,b) → (−a,−b)`.

The construction yields two nontrivial consequences for every allowed state:

```text
F_after = −F_before,
(a b)_after = (a b)_before.
```

For a uniformly weighted four-state ensemble, stipulated for this example, the two-step readout correlation is `⟨F_before F_after⟩ = −2`. The readout, transition, and ensemble were **assumed**; the sign reversal, invariant product, and correlation follow. This is not a derivation of a known physical law from experience alone and does not calibrate a phenomenal state. Nor is `ab` automatically pleasantness, discomfort, or the user's proposed vibrational alignment. Connecting such structure to valence requires an independently justified quality map and empirical constraints.

Now add a neutral model label `h ∈ {−1,+1}` and keep the proposed experiential organization `q(a,b,h)=(a,b)` and physical output `F=a+b`. Consider two alternative transition rules:

- **Redundant-label rule:** `(a,b,h) → (−a,−b,h)`. Both factorization conditions hold. The quotient `(a,b)` reproduces the output and its transitions without tracking `h`.
- **Dynamically relevant-label rule:** `(a,b,h) → (h a,h b,h)`. States `(1,1,+1)` and `(1,1,−1)` have the same `q` and the same initial `F=2`, but their next readouts are respectively `+2` and `−2`. Thus both the successor organization and the next physical output differ, and this `q` cannot give a closed deterministic account of the example.

These states are entries in a local finite model; they are not asserted to be alternative genuinely possible complete wholes. The first rule illustrates a **positive reconstruction**; the second is a concrete failure control. If `h` also has a separately justified experiential manifestation, a richer `q` could include it and close the model. Merely renaming the hidden label “experience” without such justification would not be an advance.

### What the control tells us about parsimony

Under the first rule, `h` is dynamically redundant **relative to the stipulated outputs and operations**. We can dispense with it in that operational model. It does not follow that the real world has no additional intrinsically neutral aspect, that the quotient has no unmodeled consequences, or that `h` cannot be relevant to a larger physical or subject-constitution theory. Conversely, in the second rule, an experiential account cannot ignore the distinction while still predicting the indicated outputs. A neutral-ground account would need the same predictive adequacy and a separately defensible account of why experience is present.

This is a more discriminating use of elegance than counting ontology names: compare independently specified qualitative commitments, laws, measurements, and unexplained constitution rules at the **same scope**. Even exact equality of predictive economy would not by itself decide which account is fundamental.

## 3. The whole-account bridge is stronger than operational closure

The positive proposal has four distinct layers:

1. **Actuality:** some experience is directly present. This is not a claim that all of reality is one experience.
2. **Sufficiency:** a proposed organization of experience carries the relevant physical/relational structure, as illustrated by the factorization test. This is model-relative and needs actual phenomenal and physical identification.
3. **Constitution:** the physical structure and finite subjects are *in virtue of* the experiential organization, not merely correlated with it. Neither a quotient nor necessary co-occurrence establishes this direction of grounding.
4. **Whole and self-existence:** the intrinsically experiential whole is self-existent and self-sufficient in the user's full sense. Once that is established, no external cause of its existence is required; a dynamical quotient does not establish it.

The positive argument for layer 3 is that an intrinsically experiential foundation has the actual qualitative presence available from the outset, while layer 2 could show that it has sufficient structure to do physical work. The remaining objection is that a neutral foundation might claim to constitute the very same presence and structure. **An operationally redundant neutral variable is not the same thing as an independently established failure of all neutral constitution.** One must give a non-circular account of why a neutral constitution cannot establish presence, or present another reason to select the experiential foundation.

In the opposite direction, phenomenality cannot simply be pasted onto a quotient. An abstract pattern of labels has no demonstrated qualitative character. This issue is related to the structural-underdetermination discussion in [Chalmers, “Phenomenal Structuralism”](https://philarchive.org/archive/CHAPST-5); such concerns are contested and do not themselves prove that a neutral basis is genuinely metaphysically possible. Our labels must be anchored in proposed real phenomenal distinctions, and their correspondence with physical structure must be argued independently rather than copied from the desired answer.

The user's global possibility–actuality principle can be retained throughout. The two model rules are descriptions used to test explanatory sufficiency, not a claim that both incompatible complete worlds are genuinely possible. The principle does not by itself tell us which proposed constitution is true, nor show that predictive equivalence is grounding equivalence.

## 4. A concrete route from the toy to an actual test

The next construction must meet these requirements together, rather than treating another finite pass as closure:

1. **Independent phenomenal specification:** specify a real candidate organization with its subjects, qualitative contrasts and individuation conditions. Give reasons to regard those contrasts as experiential, not labels inferred solely from physical equations. State whether it includes only local experience or the proposed whole; do not infer whole-experience from one human report.
2. **Independent physical target:** select a bounded relational physical observable and a genuinely specified model of its dynamics or response to interventions. Use an internal clock or record relation; no external universal clock is introduced.
3. **Factorization stress test:** check whether states identical in the candidate organization produce identical target outputs and successor organizations across the specified operations. For stochastic finite models, use the cited Kemeny–Snell criterion on transition probabilities into each experiential block, with its all-initial-distributions scope; predictive equivalence or non-Markovian histories may require different methods.
4. **Calibrated comparison:** distinguish true qualitative sameness from equality of reports or uncalibrated proxies. A report decoder cannot establish that two subjects have the same experience. Test alternatives and confounding; no existing Roy data establish the needed calibrated assay.
5. **Grounding and plurality:** explain why the successfully reconstructed organization is intrinsically experiential, how genuinely distinct subjects are constituted, and—only if claimed—what makes the whole itself a universal agent. A non-agentive experiential structure is not the requested universal consciousness. Preserve the separately stated conditional tension between a perfect whole and a non-optimal world.

A result at step 3 would be a concrete advance on **structural sufficiency**, not a proof of steps 1, 4 or 5. A full account additionally owes physics/spacetime emergence, measure, empirical discrimination and the self-existence bridge. The frozen foundation battery remains incomplete.

## 5. Relationship to prior work

[Self-presence and no-nothingness unification](SELF_PRESENCE_AND_NO_NOTHINGNESS_UNIFICATION.md) showed that, conditional on the user's global strongest-possibility principle and actual experience, both absence-of-experience and absence-of-concrete-actuality are excluded. That result does not identify the ground of actuality. This construction addresses a different task: what experiential structure would need to do to **carry** a physical description. It does not derive the global principle or solve constitution.

[Experiential support factorization](EXPERIENTIAL_SUPPORT_FACTORIZATION_BRIDGE.md) and the [grounding rival battery](EXPERIENTIAL_GROUNDING_RIVAL_BATTERY_GATE.md) already emphasize support, symmetry and competing interpretations. The present local quotient is not claimed as a novel mathematical theorem or independent evidence; its added value is a positive explicit reconstruction, a nearby failure control, and a clear separation between operational redundancy and metaphysical elimination.
