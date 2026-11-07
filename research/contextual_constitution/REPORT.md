# Constructive step 2: contrast-complete constitutive scope

## The advance

The first round proposed a bridge between a concrete content-transition organization and independently characterized phenomenal contrasts. It separated content from downstream reporting and tested basic realization-token safeguards.

This round tests whether that bridge's local scope is sufficient when context changes.

**Result:** the earlier content-only description can remain adequate for its restricted content relations while being inadequate for a richer episode. An affect-sensitive extension is compatible with all the earlier content observations and can introduce an additional phenomenal distinction. Nothing in the original content interface selects between those interpretations.

A necessary principle can now be stated more precisely:

> **Contrast-complete constitutive scope:** if a description claims to account for an experiential target over a specified domain of admissible contextual changes, it must preserve every independently warranted contrast in that target throughout that domain. Contextual variation that leaves the description unchanged but changes the target demonstrates incompleteness of that description for that target.

This is independently justified as a condition of explanatory sufficiency. It is not a proof that a chosen physical description constitutes experience. Its value is that it can defeat a proposed sufficiency claim and specify the least repair relative to a model, without treating every cause as part of a subject.

The new suite has **24 passing tests**. Both rounds rerun successfully: **54 tests total**.

---

## 1. What was at risk in the first proposal

The first model contained four content states and a proposed four-way phenomenal contrast structure. Its noise calculation showed that a genuinely downstream report channel could lose discrimination while preserving the content-transition graph.

Two readings must remain distinct:

1. **Restricted claim:** that organization explains specified content relations in the modeled circumstances.
2. **Comprehensive claim:** that organization is sufficient for the entire experience, whatever else varies outside it.

The first round explicitly did not establish the second. This extension is a stress test against promoting the first into the second without further argument. It does not retroactively refute the restricted content result.

The important new question is:

> Can an otherwise identical content process participate in different affective or contextual experiences that the original readout does not distinguish?

The model below tests the logical adequacy of the proposed scope. It supplies no new human experimental evidence.

## 2. A finite context-extension model

Use states

\[
s=(q,v,r,z),
\]

where:

- \(q\in\{0,1,2,3\}\): content;
- \(v\in\{0,1\}\): candidate affective context;
- \(r\in\{0,1\}\): reporting setting;
- \(z\in\{0,1\}\): hidden memory.

The full product has 32 states. Permitted interventions hold the state, increment or decrement \(q\), or flip one of \(v,r,z\).

In the uncoupled version, changing \(v,r,z\) does not alter \(q\)'s transition structure. The projection

\[
\pi_Q(s)=q
\]

therefore preserves the complete selected content behavior under every allowed finite intervention history—not merely the sample histories checked by tests. This follows because its transition update depends only on \(q\) and the intervention, and then by induction on history length.

Compare two candidate phenomenal interpretations:

\[
H_Q:\quad E(s)=q,
\]

\[
H_{QV}:\quad E(s)=(q,v).
\]

Here the notation is deliberately interpretive. It is not a discovery that an automaton has experience or that the variable named `v` is really pleasantness or unpleasantness.

On a calibration slice \(v=0\), both interpretations reproduce the original content distinction pattern. They disagree when \(v\) changes while \(q\) remains fixed.

Both can also be attached to the **same physical report function**. Allowing the model to produce an affect label does not settle whether the label reports an actual feeling or only a representation. The code's equal-report check records this deliberately shared implementation; it is not independent evidence for either interpretation.

Thus complete agreement at the original content interface does not establish complete phenomenal sufficiency.

## 3. The exact adequacy theorem

Let \(X\) be a specified domain of cases, \(\pi:X\to Q\) a proposed constitutive description, and \(E:X\to\mathcal E\) a specified target.

There exists a function \(f:Q\to\mathcal E\) on the image of \(\pi\) such that

\[
E=f\circ\pi
\]

**if and only if**

\[
\pi(x)=\pi(y)\Longrightarrow E(x)=E(y)
\quad\text{for all }x,y\in X.
\]

Equivalently, \(\ker\pi\subseteq\ker E\).

**Proof.** If the factorization exists, equal descriptions give equal target values. Conversely, define \(f(q)\) as the target value at any case with description \(q\). The implication makes this independent of the chosen representative. ∎

This is elementary factorization, not a novel consciousness theorem. Its application is useful because it identifies an exact burden hidden in “the process is sufficient.”

For the richer candidate, take

\[
a=(0,0,0,0),\qquad b=(0,1,0,0).
\]

Then

\[
\pi_Q(a)=\pi_Q(b),\qquad E_{QV}(a)\ne E_{QV}(b).
\]

The richer target cannot factor through content alone.

If an independently warranted experiential contrast really has this form, the content-only **comprehensive** account is refuted for that domain. Without such warrant, the model demonstrates a conditional counterexample, not an actual psychophysical falsification.

Merely changing the name of a description or its output cannot repair the failure. The description must retain the relevant difference, or defend why the target, admissible domain, or empirical calibration was mistaken.

## 4. A controlled repair—and why it is not a theory of subjects

In the specified model, the richer target factors through

\[
\pi_{QV}(s)=(q,v).
\]

Exhaustive enumeration of coordinate subsets identifies \(\{q,v\}\) as the unique inclusion-minimal coordinate support for that supplied target. Reporting setting and hidden memory need not be included.

This provides a bounded positive result:

> A phenomenal account can require contextual enrichment without absorbing every external variable or every piece of reporting machinery.

However, its mathematical minimality is relative to:

- the supplied target \(E_{QV}\);
- the allowed state domain;
- the chosen coordinate/intervention structure;
- and the claim that those distinctions are adequate to the episode.

Because the target is defined to depend on \(q,v\), recovering those variables is not an independent derivation of their phenomenal importance. The genuine test is whether independently established experiential constraints have that dependence.

Nor must the least sufficient description be a literal spatial or causal subsystem. Other coordinate representations or latent descriptions may encode the same information. A jointly needed pair of variables can describe one experience, two experiences and a relation, or part of a larger organization. Functional sufficiency does not determine which.

**Explanatory relevance is not identical to constitutive membership.** A variable can supply necessary predictive context without being part of the subject. This round therefore does not announce that affective context belongs “inside” an observer merely because it enters a sufficient description.

## 5. Counterfactual and temporal scope matter too

A current-state test is insufficient when the target concerns an episode unfolding over time.

Introduce a feedback version in which a hold step updates

\[
q'=(q+v)\pmod4.
\]

Now two cases with the same current content can differ on the next content step. For the target “content now and under future interventions”:

- current content alone has four equivalence classes;
- including one possible future hold step requires eight;
- the stable future-content partition in this model also has eight.

In the uncoupled model, future content retains four classes. For the richer \((q,v)\) target, it has eight even without feedback.

These are exact conditional results. They explain why neither the instantaneous state nor an unspecified “complete process” is an adequate phrase by itself. The account must state which interventions and temporal extent its sufficiency covers.

They also prevent a common dodge: calling a disturbance “external noise” does not make it irrelevant. If it changes relevant future organization, the nuisance assumption fails. Conversely, its being causally influential at some later time does not establish current phenomenal membership.

A finite-time episode may have a different relevant domain from a continuing subject. Those targets must not be silently exchanged.

## 6. What is genuinely independent here

There are three levels:

### A. General explanatory obligation

If an account claims to explain a determinate contrast, it cannot leave that contrast varying freely while all of its relevant explanatory resources remain the same. This follows from what explanatory sufficiency claims, without choosing physicalism, idealism, or neutral monism.

### B. Independently characterized experiential evidence

To apply the principle to phenomenality, there must be warrant that the proposed contrast is experiential. First-person comparative acquaintance may supply such evidence for a subject; reports, interventions, and other records can support intersubjective investigation with uncertainty.

“Independent” means that the contrast was not defined into the candidate physical model. It does not mean infallible access or a publicly readable phenomenal oracle.

### C. The proposed constitutive realization

The account must then establish why the relevant physical/intrinsic organization suffices, rather than merely covaries. This is still open.

A successful factorization from supplied phenomenal data earns determination within that model. It does not alone earn numerical identity or the explanation of feeling. The distinction from the previous synthesis is preserved.

## 7. Realization-token constraints retained

The new model does not use its state classes as observer counts.

- **Same type, multiple occurrences:** two supplied occurrence witnesses can have identical \((q,v)\) profiles without becoming one occurrence.
- **Hidden copies:** the selected local profile does not determine the total supplied realization list.
- **Passive renaming:** transporting the state description preserves the relevant partitions.
- **Shared context:** a common \(v\) need not merge distinct processes into one subject.
- **Changing storage:** the first round's moving-lane construction remains valid; enriching the target does not convert storage locations into identities.
- **Temporal grain:** current and future target partitions are explicitly different where coupling makes them so.
- **Reporting versus feeling:** a readout cannot be declared constitutive merely because it is labeled a report of affect.

The new occurrence-list helper is deliberately modest: it preserves a list of supplied actual-role witnesses. It does not discover witnesses from dynamics. Its duplicate checks verify bookkeeping under that assumption, not the actual existence of subjects.

Neither a probability over observers nor equal self-location weights follow.

## 8. The two-sided explanatory gain

The same extended model yields a concrete separation of three effects:

| Intervention | Public content effect | Candidate phenomenal effect |
|---|---|---|
| Flip report setting \(r\) | Reports change; content stays fixed | Neither supplied target changes |
| Flip context \(v\), no feedback | Content behavior stays fixed | No change under \(H_Q\); change under \(H_{QV}\) |
| Change \(v\), with feedback | Future content changes | Future contrast accounting must preserve the resulting distinction |

The physical claims follow from the transition rules. The phenomenal column is conditional on the indicated bridge, not experimentally measured.

This makes the disagreement tractable. A real test needs to distinguish:

1. degraded reporting with preserved experience;
2. a genuine experiential change missed by the old content description;
3. a context intervention that changes later content through feedback;
4. a change in belief or report about experience without the proposed experiential change.

A one-number integration measure or a globally fixed report metric cannot settle those distinctions by itself.

The constructive advance is therefore not “more variables explain consciousness.” It is a criterion for testing **which omitted contrasts defeat a proposed sufficiency claim**, together with a model showing how a limited repair can avoid including irrelevant machinery.

## 9. A sharper empirical target

A suitable candidate is a distinction between sensory content/intensity and affective character. That is a research target, not an empirical result established here.

A disciplined protocol would:

1. Predeclare the episode, candidate neural/process variables, contextual interventions, and report pathways.
2. Obtain independently characterized experiential contrasts rather than infer them solely from accuracy, avoidance behavior, or an affect label.
3. Match or monitor the proposed content variables across contextual conditions. Practical measurement error must be modeled rather than declaring exact equality from an imperfect proxy.
4. Test whether a reliable experiential difference remains at matched content organization.
5. If so, reject the comprehensive content-only claim; determine whether an enriched organization predicts held-out contrasts under further interventions.
6. Use different report modalities or delayed judgments as controls while explicitly recording their memory and inference assumptions.
7. Check whether the enriched state merely fits labels, predicts genuine new relations, or depends on an arbitrary contextual selector.

There is no collected dataset in this work. The present conclusion is about the required logic of the test and its demonstrated finite-model behavior.

## 10. The revised constitutive candidate

The first round's contrast covariance should now be stated with stronger scope protection:

> **An experiential contrast structure is to be explained by a concrete organization that is contrast-complete across the independently justified contextual and temporal domain of the episode. Covariance under redescription and purportedly nonconstitutive changes is admissible only after those changes have been shown to preserve that relevant organization.**

Two components are independently justified necessities:

- no unexplained contrast within the claimed explanatory scope;
- no substitution of representational invariance for an accounted-for physical change.

The substantive sufficiency remains to establish: which actual concrete nature constitutes the contrasts and their unity?

Importantly, the revised principle is not a universal subject selector. It does not infer unity from a sufficient support, or deny experience whenever the available model lacks a selector. Nor does it make the global actuality problem disappear.

## 11. What should happen next

The new bottleneck is exact:

> **Can a constitutive account explain why the independently warranted contrasts belong to one episode, rather than merely provide a sufficient joint description of them?**

A next round should distinguish co-presence/unity evidence from joint predictability. Two separate processes can share an affective controller or support a joint report without constituting one experience. Conversely, one process can have multiple differentiated contents without being many subjects.

The useful next formal test is therefore a **joint-readout versus co-presence test**: construct systems with identical joint contrast predictions but different supplied occurrence organization, and identify what additional constitutive principle—not another count or integration score—could distinguish phenomenal unity.

If the existing contrast constraints do not determine that distinction, the result should remain a specified family. An independently warranted co-presence relation may narrow it, but its interpretation must not be hidden in the formal definition.

## Reproducibility and status

- `model.py`: 32-state context-extension model; current and counterfactual target factorization; minimal coordinate support search; occurrence-witness bookkeeping.
- `test_model.py`: 24 tests, including expected failures of content-only sufficiency, target-dependent alternatives, feedback, restricted-domain masking, renaming, and hidden-copy limits.
- `results.log`: actual run, **24 tests passed**.
- `../run_checks.py`: runs both research rounds in separate processes to avoid module-name collisions.
- `../check_results.json`: combined execution record; **30 + 24 tests passed**.

Run both rounds from the repository root:

```bash
python research/run_checks.py
```

No external dependencies or new fundamental numerical thresholds are introduced. The variable choices, target maps, intervention domain, and occurrence witnesses are substantive model inputs; being parameter-free does not make them derived.

### Verdict

> The programme now has a stronger necessary constitutive test: **contrast completeness across context and time**. The original content-only description survives as a restricted relational proposal but cannot claim comprehensive sufficiency merely because it reproduces all of its selected local behavior. A context-sensitive repair is mathematically available without swallowing report machinery or hidden memory. Its adequacy and unity as an actual experience remain to establish. This is a narrowed, testable route forward—not a newly declared foundation or proof that the original ambition is impossible.

## Subsequent unity test

[Constructive step 3](../episodic_unity/REPORT.md) distinguishes joint prediction, pairwise co-presence, higher-order presentation, and occurrence multiplicity. A conditional overlap-amalgamation theorem yields maximal-support partitions, but its phenomenal authority is not inferred from shared hardware.
