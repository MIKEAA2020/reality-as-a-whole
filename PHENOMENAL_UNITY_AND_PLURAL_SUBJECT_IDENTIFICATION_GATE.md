# Can phenomenal unity identify genuinely plural subjects?

## The issue and the result

The framework needs more than a single experiential foundation: it needs **genuinely plural subjects**, not merely different descriptions, information channels, or accessible regions of the same subject. One constructive route is to ask which experienced aspects are experienced **together**, then infer subject boundaries from those relations. But that inference has hidden premises.

This note makes them explicit and supplies a **conditional identification procedure**. If a finite set of already-established experiential aspects has exclusive subjects, if same-subject membership is exactly captured by a specified relation of conjoint phenomenal unity, and if we have correct pairwise observations, then subject counts represented by those aspects reduce to a familiar constrained-partition problem. With incomplete observations, the count can remain ambiguous; with bounded errors, a set of counts rather than a single answer may be justified. If those assumptions conflict with observations, at least one must be revised.

The genuinely important limitation is not merely measurement error. **It is disputed whether phenomenal unity is transitive, whether experiences can be shared, and whether a subject always has one totally unified field.** If those conditions are dropped, the partition calculation may not apply at all. Even its ideal input presupposes the very experiential relation we seek to explain. This is therefore a constrained research interface, **not** a theory deriving subjects from an experiential ground, or a demonstration of a real person's subject count. First-person experience itself remains valid data; it is not a mere label in a graph.

A follow-up [randomized pair–triple gate](TRIPLE_UNITY_RANDOMIZED_REPORT_PARTITION_GATE.md) derives a sharp population bound under exclusive fields and shows how conditional probe-error bounds could challenge the full hypothesis package. Its target calibration and cross-arm comparability are not established.

## 1. The prior literature and its limits

[Bayne and Chalmers, *What Is the Unity of Consciousness?*](https://consc.net/papers/unity.html) distinguish access unity from phenomenal unity: being jointly accessible for reasoning or report is not automatically the same claim as there being something it is like to experience the aspects together. They discuss the unity thesis and a subsumption account, while acknowledging controversy. The introduction and selected sections on unity and subsumption were read; the remaining text was not systematically inspected.

[Schwitzgebel and Nelson, *When Counting Conscious Subjects, the Result Needn’t Always Be a Determinate Whole Number*](https://faculty.ucr.edu/~eschwitz/SchwitzPapers/CountingSubjects-250528.pdf), discuss nontransitive phenomenal unity, possible sharing of experience, and the risks of counting overlapping fields as separate subjects. The opening and selected passages on intransitivity and countability were read; other sections and figure images were not systematically inspected. Their view is not a settled result about actual people and does not require us to deny actual experience. We retain the user's plural-subject target rather than adopting any illusionist denial.

[*A layered unity model of split-brain consciousness*](https://doi.org/10.1007/s11098-025-02339-3) argues for a particular combination of global unity and localized disunity. Its abstract and selected sections were read; the entire article, figures and underlying clinical experiments were not independently audited. It is an interpretive proposal, not proof of a particular subject count after surgery. The project's [hemispherotomy audit](HEMISPHEROTOMY_ANESTHESIA_AND_SUBJECT_BOUNDARIES.md) likewise warns against identifying motor or cross-report access with phenomenal unity.

The mathematical problem of clustering with pairwise positive and negative relations is established. Bansal, Blum and Chawla, [*Correlation Clustering*](https://doi.org/10.1023/B:MACH.0000033116.57574.95), study minimizing disagreement in a complete signed graph, including inconsistent positive-positive-negative triangles. The user-supplied full text has since been read; the [full-paper audit](CORRELATION_CLUSTERING_FULL_PAPER_AND_SUBJECT_CERTIFICATE.md) specifies figure and proof-audit limits and develops a separate-budget certificate based on the paper's packing idea. The graph and coloring construction below is an application of standard constraint logic, not a new clustering algorithm or a literature-wide novelty claim. Unlike their optimization objective, our error-budget version retains **all** compatible partitions and their counts.

## 2. A deliberately strong exclusive-field candidate

Take a finite nonempty set `V` of **already-occurring**, distinguishable experiential aspects within a specified local window. “Aspect” is a bookkeeping term: this model does not decide whether experiences literally have experiential parts. Each label must refer to a token or aspect occurrence, not merely a repeatable content type: two people can both see red without thereby sharing one numerically identical experience. The window is a local relation inside the whole, not a universal clock. No aspect is declared an entire subject merely because we can name it.

Adopt the following **test candidate**, not established metaphysical facts:

1. Each aspect belongs to exactly one subject-occurrence in the target window.
2. Two aspects are in the same subject-occurrence **if and only if** they have the specified conjoint phenomenal-unity relation. This is stronger than saying they are correlated, accessible by the same controller, or reportable together.
3. The relation and the occurrences being compared are stable across the measurement procedure. If a probe alters the episode, a later observation is not automatically a second reading of the same token.
4. Pairwise records are, under independently warranted bounds, informative about this relation in the target setting. Neither a physical causal edge nor a successful task is automatically such a record.

Then same-subject membership is an equivalence relation, in particular transitive. Its equivalence classes partition `V`. This model counts **subject-occurrences represented by V**, not all subjects in the world: a subject with no represented aspect is invisible to the count. Nor does the count establish numerical identity across local windows or imply that persistent persons split or merge. Completeness about a larger system would require an independently justified coverage premise.

The biconditional in item 2 is substantive. A theory with disunified experiences belonging to the same subject, nontransitive unity, or genuinely shared experiential tokens is not necessarily incoherent: it lies outside this candidate. Likewise some theories reject decomposing experience into well-defined tokens at all. The finite construction does not choose among these views.

## 3. Exact but incomplete pairwise information

Let `P` and `N` be disjoint sets of distinct unordered pairs, respectively asserted to be jointly phenomenally unified and not unified. Section 3 assumes these assertions correct; the next section permits errors. Unlisted pairs are **unknown**, not negative. Under the exclusive-field candidate, any valid partition must place every pair in P in the same block and every pair in N in different blocks.

First join all vertices connected by positive edges; call the resulting components `C1,…,Cc`. If any negative edge has both endpoints in the same component, no partition satisfies the records and candidate assumptions together. Otherwise build a simple graph `G` whose vertices are these components, with an edge between two components whenever at least one N pair joins them. If `χ(G)` is the graph's chromatic number, the exact possible subject-count set is

```text
{χ(G), χ(G)+1, …, c}.
```

A proper coloring assigns each positive component to one block without joining a forbidden pair, and any admissible partition is such a coloring. Starting with a minimum coloring, split color classes until each component has its own block; splitting cannot violate a cannot-link edge. This gives every intermediate count. The result is standard graph-coloring reasoning; it is exact **conditional on the candidate and correct pairwise records**, not a proof of phenomenal unity or the number of subjects in reality.

For example, three aspects with `A` separate from `B`, and `B` separate from `C`, but no information on `A` versus `C`, admit both `{A,C}|{B}` and `{A}|{B}|{C}`: the represented count is **2 or 3**, not uniquely 2. The graph is not completed by assuming whatever yields a preferred number.

## 4. What changes under bounded assessment errors?

When pair records may be wrong, define a candidate partition's mismatch counts as follows:

- `FP`: recorded-positive pairs placed in **different** blocks;
- `FN`: recorded-negative pairs placed in the **same** block.

Suppose separately justified target-window error budgets assert that the actual number of false-positive pair records is at most `a` and false-negative pair records at most `b`. Enumerate every partition satisfying both bounds. Their set of block counts is the **sharp finite identification set within this model**: every listed count is achieved by an admissible partition, and no unlisted count is. “Sharp” is relative to the listed pair records, admissible partitions and deterministic error budgets; it does not mean that the budgets are empirically established. No interval formula is assumed for the error-budget case. If no partition is admissible, do not conclude that experience is absent: some combination of token identification, error budgets, stability, exclusivity, unity biconditional or measurements has failed.

### Example: a robust conditional two-subject certificate

For four stipulated aspects A, B, C, D let the positive pairs be `AB` and `CD`, and all four cross-pairs `AC, AD, BC, BD` be negative. Within the exclusive-field model:

| Allowed FP `a` | Allowed FN `b` | Compatible represented counts |
|---:|---:|---|
| 0 | 0 | {2} |
| 1 | 0 | {2, 3} |
| 2 | 0 | {2, 3, 4} |
| 0 | 1 | {2} |
| 0 | 4 | {1, 2} |

With no false positives, both within-pair links must be retained. Merging the two resulting blocks requires all **four** cross-negative records to be false negatives. Therefore one false negative does not defeat the two-block certificate, but allowing one false positive can split a block. This illustrates why separate false-positive and false-negative budgets matter. These are **hypothetical simultaneous error counts**, not estimated human-study performance.

### An inconsistency is informative, but not a verdict on experience

For three aspects, suppose `AB` and `BC` are positive, while `AC` is negative. No error-free exclusive partition exists. If at most one positive is false and no negative is false, only **two** represented blocks are possible; if no positive is false and one negative may be false, only **one** is possible. With zero allowed errors the assumptions conflict. A live alternative is a genuinely nontransitive or overlapping unity structure; another is erroneous or noncomparable observations. The graph alone cannot decide which explanation is correct.

These counts are for a single stipulated local comparison. Repeated or separately collected pair tests need not refer to the same occurrences; standard error rates or confidence intervals do not automatically provide a deterministic bound on **the total number of wrong labels in this particular data set**. A probabilistic simultaneous coverage claim requires a specified sampling design and dependence model or a valid joint error guarantee; correlated errors cannot be ignored.

## 5. An explicit nonexclusive alternative

Take aspects A, B, C and compare two abstract families of maximally joint sets:

```text
F1 = {ABC}             F2 = {AB, AC, BC}.
```

Both induce the same complete **pairwise** relation: each pair appears together in at least one set. But F1 contains one maximal joint set and F2 contains three pair sets with no stipulated triple joint set. The latter requires the same abstract aspect label to occur in multiple overlapping sets; interpreting this as genuinely shared token experience is a further controversial premise. Alternatively it may just reveal that the chosen aspects or sense of “together” were too coarse. These are mathematical alternatives, not shown genuine possibilities or real experiences.

If a proposal defines a subject-occurrence as a maximal jointly experienced set, it would return one for F1 and three for F2. That **conditional count is not a proof** that overlapping sets really constitute three subjects; the subject/field relation is exactly what is in question. The example nevertheless shows that a binary pair table alone cannot identify higher-order joint incidence if nonexclusive overlapping families are admitted. Merely counting maximal cliques silently assumes an additional rule that every pairwise-compatible clique is jointly realized. Nor does it refute Bayne–Chalmers: their specific subject-indexed and subsumption principles add constraints that this deliberately weaker relation does not.

The earlier [quantum-access gate](QUANTUM_ACCESS_STRUCTURES_AND_SUBJECT_COUNT_GATE.md) found that overlapping recovery regions need not be separate copies or subjects. The present issue is different: it concerns a **stipulated phenomenal** incidence structure, not a quantum access structure. Neither result converts an operational channel into experience.

## 6. Where this leaves a constructive account

A viable account should supply, in order or in a justified joint construction:

1. **Ontology and tokenhood:** what experiential occurrences or aspects are real, how they are individuated, and what local window is being discussed. The existence of experience is a datum; its full inventory is not given.
2. **Unity and incidence:** whether subjecthood entails a total field, whether the same occurrence may belong to multiple subjects, and why the chosen co-experience relation has the required closure. Do not assume a subject count in order to derive that count.
3. **Physical interface:** a common independently specified physical situation, allowed transformations and interventions, plus a proposed constitution map. Redescription must transport the physical operations and phenomenal claims together; mere relabeling invariance does not establish substrate independence.
4. **Experiential anchoring:** specify whose first-person datum is available, how it relates to the questioned conjunction, and how it is communicated. Calibration must be valid under the target intervention and account for common causes, attention, memory, report loss and changes induced by probing. First-person occurrence and externally recorded report must not be conflated.
5. **Rival predictions and failure conditions:** compare exclusive, overlapping and other plausible models without assigning truth by definition. Prespecify which joint or triple indicators would count against a candidate, and retain indeterminacy if assumptions or error bounds are not justified.
6. **Persistence and coverage:** handle unrepresented subjects, continuity, fission and overlapping windows separately. A partition in one window is not a theory of a person's identity through time.

The most immediate constructive opportunity is to state an actual **experience-respecting** subject rule and its rival on the *same* physical and phenomenal domain, including nonexclusive cases, and show why its phenomenally meaningful premises should hold. The present gate provides conditions under which an idealized unity observation would or would not constrain the represented count; it does not produce that observation or derive the required rule from the experiential ground. Thus C3—**full structural and experiential intelligibility**—and the other jointly required criteria remain open. No universal subject, external creator, literal simulation or temporal actualization is introduced.

## Reproduction and source scope

Run `python verification/phenomenal_unity_partition_gate.py`. Its [receipt](verification/phenomenal_unity_partition_gate.json) exhausts all 760 signed partial graphs on one through four vertices for the exact-feasibility and count-interval checks, checks the tabulated bounded-error cases and the two higher-order families, and tests the four-aspect example under all 24 relabelings. General graph statements follow from the explicit argument above, not from finite enumeration. The script uses no observed data and its successful exit is not a philosophical or clinical battery pass.

Source limitations are stated in section 1. In addition: [Stanford Encyclopedia, *The Unity of Consciousness*](https://plato.stanford.edu/entries/consciousness-unity/) was read only in selected introductory and metaphysical sections; other sections and cited underlying works remain unaudited except where explicitly noted. The attempted publisher PDF fetch of *Correlation Clustering* failed, but the user supplied its full PDF and the [subsequent audit](CORRELATION_CLUSTERING_FULL_PAPER_AND_SUBJECT_CERTIFICATE.md) supersedes that access limitation.
