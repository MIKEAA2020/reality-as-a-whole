# Step 38 — An intrinsic duration does not select an episode phase

## Result and scope

A proposed repair to the event-connectivity problem is to use a mechanism's intrinsic integration or recurrence time as the duration of an episode. This supplies a duration, but does not necessarily supply its start and end points.

**Conditional result:** if the constitutively relevant input is invariant under one-step time translation, a deterministic, translation-equivariant rule cannot partition it into disjoint, contiguous, finite episodes containing more than one event. A duration parameter alone does not break this symmetry.

This is not an empirical assertion that conscious activity is time-homogeneous, that episodes must be disjoint, or that time cannot have intrinsic physical landmarks. It is a constraint on a particular proposed completion of Γ. The earlier architecture explicitly left overlap and temporal extent open; this test does not silently impose a partition on every theory.

## 1. The candidate being tested

Consider events indexed by the integer line Z. The proposed law assigns a partition into contiguous episode intervals. It is required to be:

1. deterministic for the specified constitutive input;
2. equivariant under a change of time origin;
3. based on input that has no distinguished temporal phase;
4. capable of selecting disjoint finite multi-event intervals.

The third condition is substantive. It can hold for a homogeneous actual process with a time-homogeneous mechanism, even if its dynamics have a characteristic response time. It does not automatically hold for an oscillating history with a distinguished phase marker, a preparation transient, or an internal event singled out by the candidate theory.

The fourth condition is a candidate requirement, not an independently established fact about phenomenology. The result tells us that these four requirements cannot all be met in the stated domain.

## 2. Symmetry obstruction

Let B⊆Z be the selected boundaries between adjacent events. Changing the time origin by one step sends B to B+1. For homogeneous input X, translation equivariance gives

\[
\Gamma(X)=\Gamma(TX)=T\Gamma(X),
\qquad\text{hence}\quad B=B+1.
\]

If B contains any integer, it contains every integer by repeated translations. If it contains none, it is empty. Thus the only translation-invariant boundary sets are all boundaries or no boundaries: singleton intervals or one unbounded interval. Neither is a partition into finite multi-event episodes.

Equivalently, an invariant equivalence relation with contiguous classes either separates every adjacent pair or relates every adjacent pair and hence the entire line. This is a statement about the specified partition structure, not a proof that experience has either of those forms.

If a theory returns no episodes on such input, there is no contradiction. It has instead declined to satisfy requirement 4 in that domain. Whether that is phenomenally correct needs independent evidence.

## 3. Why an intrinsic period does not always solve it

Suppose a mechanism supplies a preferred duration L>1. Partitions

\[
\{[r+jL,r+(j+1)L):j\in\mathbb Z\},\qquad r=0,\ldots,L-1,
\]

all have that duration. Without a phase anchor, the inputs do not distinguish them. Shifting time by one cycles through these L choices. A mathematical coordinate origin can choose r, but then the episode incidence depends on the description rather than the realized process.

The implementation represents periodic **boundary masks**, not cyclic physical time. It enumerates masks to confirm that only the two constant masks are invariant under a unit shift and that equal-length nontrivial partitions have L distinct phases. No causal loop is introduced into the actual-event graph of step 37.

A full physical oscillator can provide additional phase information. For example, a physically distinguished internal event or preparation record may anchor intervals. In that case the input is no longer invariant under every time translation, and the obstruction does not apply. But the constitutive theory must still justify why that physical marker defines an episode boundary rather than merely a convenient observation marker.

This is a separation between a physical timescale, an actual phase marker, and its proposed phenomenal significance—not a denial that any of them can exist.

## 4. The legitimate alternatives

The calculation leaves several possibilities open:

- **Physically anchored intervals:** specify an actual symmetry-breaking event and justify its constitutive role. Moving the experimental observation origin must not by itself change the episodes.
- **Overlapping temporal incidences:** all sliding windows of a specified duration can form a translation-covariant family. They are not a partition and cannot be counted as independent subjects merely because the windows overlap.
- **An ongoing episode without forced internal cuts:** a maximal interval or stream might have no constituent episode boundaries of the tested type. This still needs a spatial/compositional criterion and a phenomenal justification.
- **A stochastic boundary process:** a stationary distribution can be translation invariant even though particular realized cuts are not. This introduces a probability law and realization question; a random phase cannot be declared physically actual merely because it restores symmetry in distribution.
- **No episode in the homogeneous domain:** consistent with the mathematical assumptions, but not established by them.

None is selected here. Introducing overlap also does not automatically solve individuation: a family of windows is an incidence proposal, not a count of subjects or proof of qualitative unity.

## 5. Combined consequence with step 37

[Step 37](../event_composition_obstruction/REPORT.md) separated mechanism feedback from reciprocal paths among actual occurrences. This step separates an intrinsic duration from a physically and constitutionally justified temporal phase.

Together they rule out two shortcuts:

1. actual-event strong connectivity does not automatically recover a temporally extended episode on a strict causal time order;
2. specifying an integration time does not automatically supply unique finite disjoint episode intervals.

A viable Γ must therefore state what its incidences are—partition blocks, overlapping episodes, a stream, or something else—and how actual history and mechanism organization determine them. Representation invariance is a warranted consistency requirement, but it does not by itself pick the phenomenal incidence law.

This suggests a disciplined revision of the minimal candidate: **do not assume that finding an integration timescale entails finding discrete episode boundaries.** Keep temporal incidence unresolved until the theory and phenomenal evidence justify its form.

## 6. Verification and explanatory status

`model.py` implements periodic boundary masks, translation actions, phase orbits, equal-length partitions on integer event indices, and sliding-window families. Twelve tests verify the invariant-mask enumeration, phase multiplicity, partition changes under phase selection, anchored covariance, and overlap alternatives. `enumeration.json` records witnesses. The infinite-line symmetry argument is proved above; the finite enumeration is a check of the implementation, not an experiment on experience.

The result supplies a conditional obstruction and a clearer constitutive requirement, not a true Γ or χ. It does not establish the temporality of human episodes, select an integration threshold, derive qualitative identity, or complete the physical/phenomenal bridge. The whole-account and zero-residue objectives remain unfulfilled.
