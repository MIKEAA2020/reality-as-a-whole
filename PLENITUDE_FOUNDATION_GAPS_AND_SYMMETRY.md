# Necessary experiential plenitude: narrowing the foundational gaps

**Status: conditional mathematical and conceptual results, not a complete account of reality.** This develops the corrected [self-existent-plenitude candidate](SELF_EXISTENT_PLENITUDE_PLURALITY_CORRECTION.md). It does not reintroduce literal simulations, aliens, a creator, or a temporal mechanism for actualizing possibilities. The user prioritizes zero-residue intelligibility over fidelity to Bostrom's original story.

For the follow-up subject-boundary analysis on an explicit stochastic interacting system, see [Subject boundaries in one coupled physical dynamics](COUPLED_DYNAMICS_SUBJECT_BOUNDARY_GATE.md).

## 1. The target and the questions it must answer

The current working hypothesis is one self-sufficient, timeless whole, intrinsically experiential, differentiated into plural subjects. Genuine possibility is actuality, in the user's strongest sense: if something is genuinely possible it is actual, and if it is not actual it was not genuinely possible. Ordinary processes and time, if accounted for, are internal to the whole. On the user's adopted bridge from a perfect whole to the best universe, and their premise that our universe is not best, the whole is non-perfect.

We must not mistake that hypothesis for its explanation. In particular:

- Why is there concrete actuality, and why is it experiential?
- What determines genuine possibility without covertly selecting among merely possible worlds?
- How do distinct subjects, their identities and qualities follow from the experiential whole?
- How do quantum phenomena, spacetime, physical law and local time arise?
- What, if anything, determines meaningful probability or local typicality?

The following results narrow the first three questions, and identify a shared structural obstacle to the last two subject-related ones. They use familiar modal-logic and symmetry reasoning in this specific framework; neither the reasoning itself nor the finite graph is claimed as a new discovery in logic or physics.

## 2. Strong possibility = actuality: what it really buys

Use `◇` and `□` as an explicitly **conditional formal representation** of genuine possibility and necessity, not as a required ontology of separate, pre-existing possible worlds. Let `p` be a classical, globally scoped proposition about the whole. The strong premise includes the schema

```
(1)    ◇p → p
```

for `p` **and for its negation**. Assume classical contraposition and the usual duality `□p ↔ ¬◇¬p`. Then:

```
(2)    ◇¬p → ¬p            instance of (1)
(3)    p → ¬◇¬p            contraposition
(4)    p → □p              modal duality.
```

With reflexivity, `□p → p`; hence `p ↔ □p` and `◇p ↔ p` for global propositions covered by the schema. This is **modal collapse**. It is a consequence of the assumed formalization, not a separate mechanism or a proof of the premise. See [standard modal logic](https://plato.stanford.edu/entries/logic-modal/) for the background; the application to this target was already discussed in the [earlier construction](NECESSARY_PLENITUDE_PLURAL_SUBJECTS_SIMULATION.md).

**Conditional gain.** If experience actually occurs (`E`), and `E` is a global proposition to which (1) applies, then `□E`. Thus the strong schema plus the experiential datum makes *some experience* necessary; there is no need to infer experience from a bare abstract truth. Nor does this entail that every description of experience is accurate. Accepting experience as a datum and accepting the strong schema are separate commitments. Whether experiencing is necessarily concrete in the intended sense, and why the schema is true, are not resolved.

**Important scope correction.** The two-world countermodel in [the earlier nothingness audit](NOTHINGNESS_TRUTH_AND_EXPERIENTIAL_NECESSITY.md) shows that necessary existence of *some* subject alone need not entail the necessary existence of a particular subject. It is **not** a countermodel when unrestricted global (1) is also assumed for propositions about rigidly identified subjects: under that additional assumption any actually true such global proposition is necessary as well. This does not reveal which subjects actually exist, establish rigid identity across the formal alternatives, or derive plurality from the bare fact of experience.

### Why this is not a derivation of existence from the schema alone

There are two simple reflexive singleton semantic models:

- In `M0`, the experiential atom `E` is false.
- In `M1`, `E` is true.

Each satisfies (1) for every Boolean proposition in its one-point language, because each `◇p` has the same truth value as `p` there. In `M0` experience is not necessary; in `M1` it is necessary. The formal contrast shows **the schema alone does not entail actual experience**. It does not establish that an experience-free reality is genuinely possible: `M0` is a semantic countermodel to an inference, not a discovery about metaphysical possibility. Our own experience supplies the relevant actual datum on the candidate view; why that datum and the proposed modality obtain remains to be explained.

## 3. What can plenitude include without contradiction?

If globally scoped `p` and `¬p` were both genuinely possible, (1) would imply both are actual. Under classical consistency that cannot happen. So the strong principle does **not** mean that every logically describable complete global alternative is actual. It requires an explanation of why, for incompatible complete global claims, at most one is genuinely possible. Simply saying “the actual one” makes the biconditional easy to state but does not by itself explain the whole's content.

In contrast, `Alice experiences warmth` and `Bob experiences cold` are compatible, as are two local regions with differently specified effective laws, provided those facts are coherently embedded in one totality. Likewise a mathematical account can *describe* inconsistent alternatives without asserting they are genuinely possible or actual. Local variety therefore does not resolve contradictions between exhaustive global claims, and mathematical consistency alone is not yet shown to entail concrete existence.

The research question shifts from **“Which alternative is selected for actualization?”** to **“What makes this whole's differentiated content necessary and self-intelligible, including why purported incompatible global alternatives are not genuinely possible?”** No external selection or temporal realization is being reintroduced. Naming the whole “maximal” or “all structures” would not settle this: the scope, compatibility and ontology of the claimed structures still need justification, and an unrestricted collection may face set-theoretic difficulties.

## 4. A common symmetry gate for subject, quality and measure

Here is a finite diagnostic showing why several apparently separate gaps cannot be closed by saying only “the answer must be invariant.” It is a deliberately restricted mathematical model, not a model of a human brain.

Take an **unpointed** four-vertex graph consisting of a triangle `A={a,b,c}` and an isolated vertex `B={d}`. Its six automorphisms permute `a,b,c` and fix `d`. We impose just one modest condition: an assignment described as determined solely by this graph must be invariant under its graph automorphisms. Any further intrinsic structure, law, phenomenal fact, evidence or explanatory principle would be additional input and could change the result.

### 4.1 Subject incidence

Let a binary selector `s(v)` represent a proposed assignment of which vertices count as subject-locations; this is a bookkeeping device, **not** an assumption that vertices really are subjects. Invariance implies `s(a)=s(b)=s(c)`, while `s(d)` may independently be 0 or 1. There are four invariant selectors: none, `B` only, `A` only, or all four. Even adding the stipulation that some subject exists leaves three.

**Result:** symmetry constrains subject incidence but does not by itself fix it or derive plurality. A theory may use richer relational/dynamical information and a substantive constitution rule to do more; this example does not rule that out.

We can also give two explicit, invariant **subject-composition rules on the very same graph**, now stipulating that every vertex belongs to exactly one subject:

- **Vertex rule:** every vertex is a separate subject: four subjects.
- **Component rule:** each connected component is a subject: two subjects, one comprising the triangle and the other the isolated vertex.

Both partitions transform into themselves under every graph automorphism, despite disagreeing about subject count and boundaries. To compare a limited class of observations, give each vertex a local report bit `q=(1,1,1,0)` and define the report after a binary intervention `u` by `r_i = q_i XOR u_i`. The report rule does not use the subject partition. Consequently, for **all 16** possible input vectors, both rules yield identical reports; the verifier checks each one. This explicitly exhibits two candidate constitution rules and a shared intervention/report table, rather than inferring subjects from number of reports.

The assumptions do all the work here: the rules and reports are stipulated, neither partition is proved conscious, and a shared triangle-subject is not independently shown to have a unified experience. The example does **not** show that every pair of subject theories is empirically indistinguishable. A richer dynamical model could make different predictions, and independent evidence might support a particular constitution principle. Persistence, overlap and reports that express *joint* experience are not modeled.

### 4.2 Qualitative/valence assignment

Now suppose, separately, that every vertex has already been stipulated to be a subject-location and that a binary valence label means pleasant versus unpleasant. An invariant assignment is constant on `A` and independently chosen on `B`. Even if one additionally assumes that both labels occur, two assignments remain: `A` unpleasant and `B` pleasant, or the reverse. Thus these graph symmetries alone do not determine which property is felt as unpleasant.

This is not a proof that *all* structural or functional theories cannot identify phenomenal qualities. A richer structure could distinguish roles, and substantive psychophysical identities plus independently anchored observations might discriminate models. The point is that an automorphism constraint by itself does not supply the missing content, nor does assigning a symbol `unpleasant` explain why it feels that way.

### 4.3 Indexical measure

If all four locations are eligible, every graph-invariant normalized measure has the form

```
μ(a)=μ(b)=μ(c)=p/3,    μ(d)=1−p,    0 ≤ p ≤ 1.
```

For all four weights strictly positive, `0<p<1`, so nonzero support also leaves a continuum. For example `p=3/4` gives equal weight `1/4` per vertex, while `p=1/2` gives `1/6,1/6,1/6,1/2`. Both are normalized and invariant but give different probabilities of locating in `A`.

**Result:** symmetry fixes equality *within* each orbit, not relative weight *between* distinct orbits. Equal weight per vertex is a further principle. A different graph with one transitive finite orbit and the same assumptions does have a unique invariant normalized measure, but this does not establish that actual subject-locations form such an orbit, that counting is the right reference measure, or that finite reasoning extends to infinite populations. Probability is uncertainty about location within the actual whole, not a process selecting reality.

### 4.4 The constructive lesson

A viable account needs **additional, justified constitution and measure principles**, not just relabeling invariance. They need not be external laws or brute additions: the target is to show why they follow from the whole's intrinsic nature. But this is a demand on an argument, not something the graph proves attainable. The three decisions are coupled: defining a reference class presupposes a subject/center criterion; evidence and valence assignments affect which locations are compatible with a subject's observations; the measure must be compatible with the chosen ontology. Do not infer any of the three from an uncalibrated structural toy.

[`verification/plenitude_foundation_symmetry_gates.py`](verification/plenitude_foundation_symmetry_gates.py) exhausts the finite examples, including all 24 vertex permutations and all binary maps. [Receipt](verification/plenitude_foundation_symmetry_gates.json). These are elementary consistency checks of the claims above, not evidence that the universe is such a graph or that the remaining gaps are impossible to solve.

## 5. How the other work bears on these gates

### A. Concrete actuality, non-existence and intrinsic experience

The experiential datum plus the global schema conditionally yields `□E`, as shown above. This is stronger than deriving only `E` but weaker than deriving the whole framework: it cannot tell us why that schema holds, why experience has its particular organization, or why distinct subjects exist. The [truthmaker audit](NOTHINGNESS_TRUTH_AND_EXPERIENTIAL_NECESSITY.md) isolates another route: if necessary truth requires an experiential ground in every genuine possibility, experience is necessary. The burden is the grounding premise; neither validity nor the word “ground” proves it. Compare these routes without counting either conditional argument as a completed self-explanation.

### B. Subject incidence and empirical probes

The [two-subject model](TWO_SUBJECT_REVERSIBLE_SELECTOR_MODEL.md) stipulates two subjects; it demonstrates compatible bookkeeping, not their real individuation. [Latent-identifiability analysis](EXPERIENCE_ASSAY_LATENT_IDENTIFIABILITY.md) shows that structural assumptions can identify a modeled latent variable without automatically identifying it as experience. The [random-audit bridge](RIVALRY_RANDOM_AUDIT_EXPERIENCE_BRIDGE.md) specifies measurable conditions under which independent report and neural probes could narrow some operational alternatives. None is yet a derivation of subject ontology or the complete phenomenal bridge.

**Next gate:** replace the two explicit finite partition rules above and their stipulated report table with competing, independently defined subject-constitution rules on the *same physically motivated dynamics*. Work out when they disagree about subject boundaries, persistence or a prespecified report/intervention. If all observational predictions coincide, record underdetermination rather than claim a decisive experiment. If they differ, specify realistic instruments, calibration and confounds before treating a dataset as a test.

### C. The user's discomfort idea

The [phase-frustration audit](VIBRATIONAL_DISSONANCE_EXPERIENCE_TEST.md) separates incompatibility of preferred phase relations from synchrony, stored mismatch, and dissipation; a frustrated triangle can be at a stationary minimum. This rules out simple equivalences *in that model*, not the user's wider idea that a relevant mismatch is unpleasantness. The symmetry example adds a separate issue: even a correctly estimated structural variable needs an anchored explanation of which experiential quality it is.

**Next gate:** specify the relevant coupled dynamics, subject boundary, independent measurement of interaction preferences, and a fixed competing hypothesis; pre-register held-out tests using separately anchored unpleasantness reports and controls. Current data cited in the audit do not measure the proposed frustration variable. Such a test could constrain a predictive identity candidate; a successful fit alone would not prove intrinsic identity or fundamental string physics.

### D. Time and physics

The timeless whole is not an external clock. Existing [relational clock work](TIME_RESEARCH_ROADMAP.md) and [time evidence audit](TIME_SOLUTION_EVIDENCE_AUDIT.md) provide restricted constructions, not a solution of the quantum-gravitational problem of time. The gravitational, quantum-field and cutoff gates remain model-specific. A real bridge must specify a compatible underlying structure, derive relational dynamics and observer records, recover tested quantum and gravitational limits, control approximations and yield discriminatory predictions. A modal or symmetry theorem does not deliver these equations.

### E. Measure and Bostrom's transformed role

A justified self-location rule may preserve an abstract feature of Bostrom's reasoning, but the original simulated/nonsimulated count and trilemma are not the present framework. The finite graph demonstrates why **invariance alone** is insufficient even before infinite cutoffs arise. A proposed rule must explain its reference class, within-orbit and between-orbit weights, evidence conditioning, and infinite limits; see [the corrected candidate](SELF_EXISTENT_PLENITUDE_PLURALITY_CORRECTION.md) and [cutoff gate](CUTOFF_INSTRUMENT_UNIFORMITY.md). No empirical probability has been derived here.

## 6. Dependency-driven next steps

1. **Foundation:** assess whether a proposed intrinsic grounding principle is independently defensible and entails both actual experiential occurrence and the strong global schema; test it against empty/experience-free *formal* countermodels without confusing formal with genuine possibility.
2. **Composition:** give competing explicit subject and persistence rules on one common dynamics; show which distinctions come from physics, which from experiential constitution, and where underdetermination remains.
3. **Phenomenal quality:** operationalize the dissonance conjecture independently of the target report, and specify competing fixed identity/prediction maps and calibrated empirical gates.
4. **Physics and time:** connect an explicit underlying dynamics to relational clocks, quantum records and gravitational constraints; retain all approximations and test against observed physics.
5. **Measure:** only after subject/center individuation, test whether a proposed intrinsic rule uniquely selects weights and is invariant under equivalent descriptions and controlled cutoffs.
6. **Global synthesis:** check the result against actual suboptimality, non-perfection, logical consistency, empirical predictions and parsimony; distinguish exact results, working postulates, observations and remaining unknowns.

These are interdependent, not a claim that a future proof is guaranteed. The present advance is a sharper conditional necessity result and a common finite underdetermination gate—not a complete zero-residue framework.
