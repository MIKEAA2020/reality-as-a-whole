# Evidence-driven concept revision without complete history

## Result

The [previous control](ZERO_SELF_REVISION_CONSCIOUSNESS_NECESSITY_CONTROL.md) let an external command supply the new classification. This pass makes the learner do more: it receives labeled examples, evaluates a finite set of candidate rules against them, preserves the candidates compatible with the evidence, and internally selects a current rule. Its selected rule can change without an external instruction telling it which rule to select.

For two fixed, independent contexts, if all labels are correct and each underlying rule remains fixed, the learner **never loses consistency with an observed example**, and an update in one context never changes the other context's candidate set. Once it has seen both possible inputs in a context, its selected rule is exactly correct on that entire input domain. These are conditional mathematical results, not measured behavior or an argument that the learner is conscious or unconscious.

Nevertheless, the state stores **no complete history** and updates are generally **not reversible**. There are exponentially many possible accurate evidence histories leading to the same state, even when the initial state, final input, time, and true rule are known. This strengthens the narrow engineering counterexample; it still does not refute a necessity claim for the paper's richer task, in which reliable rollback and other safeguards are explicitly required.

Verification: [finite version-space checks](verification/zero_version_space_revision_test.py). Source under assessment: Barzin Lotfabadi, [*Consciousness as Architectural Necessity*, v1.4](https://doi.org/10.5281/zenodo.18566266), especially §§2.1–2.4 and 3.1–3.2.

## 1. Explicit system

There are two contexts `c∈{0,1}`. In each, input `x∈{0,1}` has output label `y∈{0,1}`. Each of the four possible Boolean rules is encoded by `h∈{0,1,2,3}`:

```text
fₕ(x) = (h >> x) & 1

h=0: (f(0),f(1))=(0,0)    h=1: (1,0)
h=2: (0,1)                h=3: (1,1).
```

The whole retained mutable state is `(H₀,H₁)`, where each `Hc` is a four-bit mask representing a set of candidates. Initially both sets contain all four rules. On observing `(c,x,y)`, the fixed update evaluates every surviving rule and replaces

```text
Hc  ←  {h ∈ Hc : fₕ(x)=y};          H₁₋c is unchanged.
```

The active rule is the lowest-numbered remaining candidate, if any. The selected rule is computed from the current set, not requested in the incoming observation. For example, in context 0, `(x,y)=(0,1)` changes the selected rule from `h=0` to `h=1` while retaining `{1,3}`; a later `(1,1)` narrows this to `{3}` and changes the selected rule to `h=3`. Thus the system revises its own current hypothesis based on evidence. It also retains compatible alternatives rather than immediately erasing them merely because one active rule was selected.

This is modest **evidence-driven internal rule revision**, not general-purpose autonomous intelligence: the environment chooses context and sample, provides the label, and the candidate family and selection convention are fixed in advance. The learner does not discover its hypothesis language, independently test its environment, protect arbitrary goals, perform open-ended conceptual change, or implement rollback. Selection while multiple rules remain possible is an arbitrary prediction policy; it does not satisfy the paper's whole ambiguity-gating specification merely because the version space stores compatible candidates.

## 2. What follows, and under which assumptions

Assume each context has a fixed true rule from the four candidates and every label is correct. Induction gives:

1. **Exact version space:** `Hc` contains precisely the rules consistent with all examples observed in context `c`.
2. **No forgetting of observed labels:** the true rule remains in `Hc`; therefore `Hc` is nonempty, and the active rule agrees with every prior observed example in that context.
3. **Cross-context noninterference:** the other context's entire candidate set—and hence its active rule—remains unchanged by the update.
4. **Eventual exact identification given coverage:** once both `x=0` and `x=1` have been observed in a context, exactly one of the four truth tables remains, namely that context's true rule.

The guarantee is about retaining **observed input–output constraints**. It does not preserve all previous predictions on inputs that were not observed: an active rule may change its prediction for an unseen input as new evidence comes in. Nor is eventual complete identification guaranteed if the environment never supplies both inputs. The learner cannot certify, using the given state alone, that a fixed-rule or accurate-label assumption is true.

The test enumerates all 16 pairs of true functions and all 1,365 context/input schedules of lengths 0–5 per pair: **21,840 runs**. It checks the exact version space, correct retention, noninterference, and nonemptiness after each step. The arbitrary-finite-horizon result follows from the update rule by induction; the enumeration is a regression check, not the proof of the unrestricted-length claim.

## 3. Internal necessity has a price

For the very strong requirement of reconstructing the **entire ordered input history**, a history record or equivalent information really is necessary under a specified information boundary. This is a genuine internal information constraint, not an external cause imposed on the learner.

Fix context 0's true rule as `h=0`, so every label is `0`. Consider histories of length `T≥3`, with the final input fixed to `x=0`, and at least one earlier `x=1`. All are accurate and all yield the identical final state `({0},{0,1,2,3})`. There are

```text
2^(T−1) − 1
```

such distinct input histories, including different orderings. Even if the decoder knows the initial state, `T`, the true rule, and the final observation, the current candidate sets cannot distinguish them. A fixed-size auxiliary record that always reconstructs the exact history must therefore have at least `T−1` bits in this family: fewer bits distinguish at most `2^(T−2)` cases, fewer than the histories. An external log, an intentionally constrained schedule, or a weaker reconstruction goal changes the accounting; the bound is not a claim that all learning requires unlimited internal memory.

The update is also non-injective for a known observation: the full candidate set and the already-filtered set `{0,2}`, when both receive `(x,y)=(0,0)`, result in `{0,2}`. It is impossible to recover which prior state occurred from that final state and observation alone. This precludes **guaranteed exact rollback** without other retained information or access to it. Some specific changes can be reversible, and adding a suitable log can enable rollback; neither makes the stated state-only update invertible.

This illustrates both sides of the issue fairly. Full traceability or rollback can impose real architectural information requirements. But those requirements arise from the *specified guarantees*: exact retention of correct examples and complete history reconstruction are different tasks.

## 4. The failure controls matter

- **Contradictory labels:** if the learner observes `(x,y)=(0,0)` and later `(0,1)` in the same context, its candidate set becomes empty. It can detect this as the absence of an active rule but cannot recover a previous set from its stored state. Subsequent filtering does not restore it.
- **Wrong but temporarily consistent label:** the learner can preserve and act on a constraint that happens to be false. For example, a first `(0,1)` excludes true rule `h=0` from the retained set; later contradictory input can empty the set but cannot restore that rule. Consistency with observations is not truth.
- **Changing world:** if the true rule changes, earlier correct labels may conflict with later correct labels. Without forgetting, reset, temporal modeling, rollback or some other adaptation, the same guarantee is not available.
- **Fixed representation:** the four-rule family is supplied in advance, and the task uses trusted discrete inputs. There is no demonstration of abstraction discovery or generalization to unbounded new situations.

These weaknesses are reasons why history, uncertainty handling, controlled forgetting and rollback may be indispensable for **stronger** tasks. They do not establish that the paper's particular seven invariants are each necessary for every useful self-revising system.

## 5. What this does to the paper's argument

In §2.1 the [paper](https://zenodo.org/records/18566266/files/consciousness_architectural_necessity_v1_4.pdf?download=1) treats rollback, identifying revision candidates, evaluating revisions and coherent transitions as features of genuine abstraction revision. The present system comes closer on candidate representation and evaluation than the previous fixed-table control, but it lacks general rollback, broad autonomous agency and guarantees under error or environmental change. It is therefore **not a countermodel to Proposition 1** about maintaining the specified invariants, nor to a theorem whose task definition explicitly requires rollback.

The model does show that a useful, precisely characterized combination—internal hypothesis change, candidate evaluation, preservation of consistent alternatives and exact retention of previous examples in a static noiseless environment—does not logically require complete provenance or arbitrary rollback. If the paper means its seven safeguards are necessary for a narrower and stronger class of work, that class and its success conditions need to be stated explicitly. If it includes this learner's task, the strong universal claim needs qualification.

Whether this machine has a *self-model* is not resolved by its code alone. Its masks represent candidate rules about its environment; the update mechanism accesses and changes those masks. Whether that counts as representing its own representational structure depends on a nontrivial definition. An expansive definition may include the learner, while a more restrictive explicit metamodel criterion may exclude it. Either criterion should be specified before claiming its necessity or its equivalence to experience. Nothing in this control determines phenomenal presence or absence.

## 6. Relation to constitutive identity

This exercise is in the spirit of the [relativity analogy](ZERO_SR_ANALOGY_EXPERIENCE_STRUCTURE_IDENTITY_EVALUATION.md), not an objection to it. The version-space guarantees, the information bound, and non-invertibility follow internally from a specified structure. They need no additional causal force. Likewise, a successful experience–structure identity would not need an external agent to attach a second thing to the structure.

The question is **which internal relation has actually been established**. Here, the proven relations concern candidates, evidence, current state and possible histories. They do not by themselves establish what is experienced, by whom, or with what quality. As in the [common echo](ZERO_ECHO_CONSTITUTIVE_MODES_AND_COHERENCE.md), a structural identity can be exact while the identification of an observable with a particular lived valence remains to be justified. This is not a claim that the identity must be false or analytic, and it is not an inference that there are physically identical worlds with different experiences.

A constructive next step would specify a stronger revision task with explicit fault and recovery requirements, prove the corresponding minimum retained information, then investigate separately whether the architecture's distinct features map to independently supported differences in conscious quality, ownership or access. A full identity proposal should explain all three together rather than assuming that a useful self-monitoring function already determines phenomenal character.
