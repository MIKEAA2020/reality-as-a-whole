# Step 37 — Actual-event reciprocity is not mechanism feedback

## Finding

A natural proposed episode selector is:

> ΓSCC: each maximal strongly connected complex of actual events constitutes one episode.

On a strictly time-ordered causal event graph, every strongly connected component is a singleton. Consequently this rule cannot select a temporally extended multi-event episode from such a graph. Folding event occurrences into reusable mechanism labels creates feedback cycles, but changes the object to which the rule is applied.

This is a mathematical obstruction to **this specific selector**, not an empirical consciousness result, a refutation of all causal constitution, or a proof that a single event cannot be phenomenal. It advances the constitutive audit by testing an explicit Γ rather than assuming that “actual reciprocal organization” already supplies one.

## 1. The composition candidate made exact

Let G=(V,E) be a directed graph of event occurrences. Assume a time function τ such that every causal edge a→b satisfies τ(a)<τ(b). ΓSCC returns the strongly connected components of G as putative episode incidences.

**Proposition.** Every strongly connected component of G contains exactly one vertex.

**Proof.** A directed path from a to b with a≠b entails τ(a)<τ(b). A return path entails τ(b)<τ(a), a contradiction. Thus no distinct vertices are mutually reachable. ∎

The argument is not limited to the finite examples. Strict ordering suffices. No numerical coupling threshold or experimental nondetection enters it. The physical domain assumed here has no closed directed causal loops; other causal structures would need separate analysis.

If an elementary graph vertex already represents a whole extended experience, ΓSCC has not derived that grouping: it has received it in the vertex definition. Such a coarse model may be useful, but it cannot count as an explanation of the supplied incidence without an independent constitutive argument.

## 2. Recurrence survives—but at the mechanism level

Use the existing two-register source update

\[
F(x,y)=(y,x\oplus y).
\]

Its dependency graph on reusable register labels has edges y→x, x→y, y→y. It has one strongly connected component {x,y}. This is a genuine description of recurrent mechanism organization.

Unroll the same mechanism over T transitions. Vertices are occurrences (t,x),(t,y), and dependencies run from slice t to t+1. There are 2(T+1) vertices; all strongly connected components are singletons. A path from (0,x) through (1,y) to (2,x) returns to the same **register type**, not the same occurrence.

The quotient map (t,label)↦label produces the recurrent type graph. It is many-to-one and creates directed cycles absent from the event graph. The quotient is a legitimate mechanism presentation; the error would be treating its components as already established complexes of actual event tokens.

This is not a contradiction between two equivalent notations. The type quotient discards occurrence distinctions, so it is not an invertible re-presentation of the full event graph. A constitutive theory may use mechanism-level dispositions as part of its basis, but must explicitly justify how they determine the incidence of actual episodes in a history.

## 3. Two easy repairs do not finish the law

### Repair A: use weak connectivity of actual events

Ignoring edge direction gives multi-event components. But in the source example a weak component spans the supplied temporal window, expanding as the window expands. This alone selects neither an episode duration nor a privileged cutoff.

Add the passive monitor

\[
F(x,y,u,v)=(y,x\oplus y,y,x\oplus y).
\]

The type graph distinguishes the recurrent source from the downstream monitor: u and v do not influence the source. Weak connectivity of the unrolled event graph nevertheless includes later monitor-copy occurrences in components containing source occurrences. Thus this rule discards a directional causal-role distinction that the earlier intervention audit established.

This does not prove that monitors cannot be conscious or belong to an episode. It shows that the weak-connectivity rule cannot *explain their exclusion on the basis of that distinction*. Such inclusion or exclusion still needs a constitutive reason.

### Repair B: use reciprocal support of the transition law

In the rare-update family Kε=(1−ε)I+εF, the source type graph is reciprocally connected for every ε>0. Over T ticks, however, no active update occurs with probability (1−ε)^T. Conditional on that no-update history, the unrolled graph consists of independent persistence chains.

For ε=.001 and T=10, this probability exceeds .99. The law-level support graph and the realized active-event history therefore answer different questions. The former may be relevant to constitution, but it is not automatically a graph of actual interactions.

The previous weak-coupling result already showed the discontinuity of a support-based core verdict. This step adds the occurrence/type distinction: moving to actual events does not simply repair that criterion, because directed event reciprocity degenerates on a strict time order, while weak connectivity supplies a different and overly permissive grouping unless further justified.

## 4. What constraint on Γ actually follows?

A viable proposed composition law must declare its domain and temporal criterion:

1. **Occurrence-based:** specify which actual event relations compose an episode without requiring a return path to the same earlier occurrence.
2. **Mechanism/disposition-based:** specify how recurrent organization across possible histories constitutes an actual episode, including its temporal extent.
3. **Joint history-and-mechanism based:** specify how actual history and counterfactual organization jointly determine incidence, rather than switching between them when convenient.

The third is a research possibility, not a discovered sufficient law. Any proposal still owes qualitative constitution and evidence for its phenomenal application. The proposition does not select a threshold, temporal integration window, subject count, or favored physical substrate.

The independently warranted constraint is **domain consistency**: a law about actual episode incidence must not silently substitute repeated types for occurrences or transition-law support for realized interaction. This follows from the stated objects and maps, not from an assumed measurement of consciousness.

## 5. Verification and integration

`model.py` constructs dependency graphs, time-unrolled event graphs, strongly/weakly connected components, type quotients, and rare-update support/history contrasts. Twenty-four tests verify:

- recurrent source type structure versus singleton event SCCs;
- strict forward causality and absence of return to the same occurrence;
- feedback created by the many-to-one type quotient;
- directed source/monitor separation versus weak component inclusion;
- dependence of weak components on the supplied temporal window;
- positive law-level interaction support despite a possible no-update history;
- invariance under bijective relabeling, unlike a noninjective quotient.

`enumeration.json` records component counts and the probability witness. These are synthetic graph facts, not labeled consciousness examples. Passing tests support the implementation; the stated proof establishes the graph proposition.

## 6. Consequence for the unified account

The realized-process basis remains a candidate, but the literal actual-event-SCC completion does not deliver multi-event episodes in this causal domain. It is therefore not the missing composition law we sought. The inquiry has excluded one tempting mathematical formulation rather than found the true Γ.

The next candidate must distinguish genuine feedback of a temporally extended mechanism from a closed causal loop among identical event tokens, and derive its episode-duration and incidence claims rather than inherit them from chosen vertices or windows. No new content-identification law χ, phenomenal sufficiency, absolute physical selection, or zero-residue foundation follows from this exclusion.

## Continuation

[Step 38](../temporal_episode_selection/REPORT.md) tests a duration-based repair and distinguishes a physical integration time from a justified episode phase and temporal incidence law.
