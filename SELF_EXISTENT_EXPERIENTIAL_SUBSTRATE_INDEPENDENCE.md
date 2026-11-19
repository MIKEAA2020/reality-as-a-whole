# Self-existent experiential reality and substrate-independence

## 1. The proposal and the question it answers

A literal simulation might suggest a simulator or creator distinct from the simulated world, although a simulator need not be a god or outside reality as a whole. The user's proposed replacement is more radical: **reality as a whole is self-existent rather than a product made real by someone or something else.** There is no external creator, machine, substrate, clock, or act that turns a merely possible whole into an actual one.

The current working candidate is:

> A timeless, self-existent, intrinsically experiential whole is relationally articulated into real plural subjects and local physical structures. All genuinely possible realities are actual within the whole. Relevant kinds of subject and experience may be realized by more than one material substrate when the right organization is concretely present.

“Self-actualization” here means *self-existence*, not an event in which something first nonexistent causes itself to exist. The whole's self-existence, if established, is not in need of an external cause; the unfinished question is **why and how the self-existent constitution is experiential, articulated, and necessary**, not what created a self-sufficient whole. The strongest rejection of absolute nothingness is part of the existing programme ([foundation unification](SELF_PRESENCE_AND_NO_NOTHINGNESS_UNIFICATION.md)), but does not by itself establish this particular constitution.

The user prefers both experiential grounding and substrate-independence; we adopt them as research commitments, not empirical discoveries or proven consequences of one another. The [hair and intrinsic-nature assessment](HAIR_EXPERIENCE_INTRINSIC_NATURE_AND_STRUCTURE.md) tests a possible objection: the apparent absence of a hair-level subject challenges indiscriminate subject attribution, but does not establish either the truth or falsity of a fundamental experiential ground. It also clarifies that an internal relational structure can be intrinsic to a composite without being an absolutely non-structural ground. This is a refinement of the prior [substrate-independence audit](substrate-independence-thesis.md) and [plurality correction](SELF_EXISTENT_PLENITUDE_PLURALITY_CORRECTION.md), not a fresh claim to have solved the known implementation and consciousness problems.

## 2. Two senses of substrate, not one contradiction

**Material substrate** means a local physical realization—say a biological or other physically possible organization. Material substrate-independence means the relevant organization could in principle be realized in more than one such medium without a change of the relevant experience. It does **not** imply that every medium can realize every organization, nor that a behavioral imitation suffices.

**Experiential ground** means the intrinsic nature of reality in the candidate ontology. Saying that there is an experiential ground is not saying that there is one privileged *material* such as biological neurons. It is therefore consistent in form to say:

1. all actual local physical realizations are articulated within an intrinsically experiential whole;
2. some different local material realizations share the organization relevant to a type of experience;
3. when that organization is appropriately realized, the experience is real—not a copy of a feeling occurring elsewhere.

These are assumptions or conditional commitments. The fact that every realization is grounded in an experiential whole does **not** establish that every process is an independent subject, or that the intrinsic nature is a universal subject. Nor does intrinsic experience alone tell us which higher-level organization determines an episode. Conversely, substrate-independence does not prove that the whole is experiential or self-existent: functionalists can endorse material multiple realizability under different metaphysics.

Our universe is not taken to be optimal; on the separately adopted bridge `perfect whole → best universe`, it follows conditionally that the whole is not perfect. Experience and suffering are real, not dismissed as numerical features of code.

## 3. A specific principle, with its remaining choice visible

Let `r` be an **actual local realization** with an explicitly specified boundary, local state, time grain, admissible operations and readouts. Let `O(r)` be a candidate organization, including whatever fine-grained dynamics and relations are claimed to matter. Let `≈` mean a justified equivalence preserving that organization and its relevant operations. Let `Q(r)` be the *type* of experience, including an independently anchored qualitative organization; `⊥` denotes no subject at this boundary.

The **strong organizational-invariance candidate** is:

```
O(r₁) ≈ O(r₂)  ⇒  Q(r₁) = Q(r₂).
```

It applies only where `r₁` and `r₂` actually realize the organization; a mathematical description or a hypothetical possibility alone is not an experience. Under strongest possibility=actuality, genuinely possible realizations have actual counterparts *somewhere in the whole*, not necessarily in our local universe or in the same compatible circumstances. A formal countermodel below is only a comparison of mathematical rules, not an assertion that its alternative laws are genuinely possible realities.

This strong principle is a substantive candidate, **not a theorem**. The user's preference supports investigating it, but does not settle whether ordinary causal-computational organization is sufficient, what its correct grain is, or whether supplementary experiential relations matter. A weaker position only says that *some* experience-bearing organizations are multiply realizable; the strong principle says that **every pair** equivalent in the specified relevant organization has the same experiential type. The latter carries a greater burden.

[Chalmers's account of organizational invariance](https://consc.net/papers/precis.html) argues for preservation of types of phenomenal states under suitably fine-grained functional organization, using fading- and dancing-qualia arguments. That is an important existing argument, not our discovery and not a settled proof of the strong principle. It is compatible as an organizational thesis with multiple metaphysical accounts, including ones unlike ours.

### Type is not token

If two independent actual realizations both instantiate the same experiential type, they may be **two distinct experiential occurrences and two distinct subjects**, not numerically the same episode or person. Conversely, organizational similarity alone does not specify which transitions preserve one continuing subject during replacement or branching. A substrate-independent quality criterion cannot silently answer the separate persistence and incidence questions. It also does not assume an actual upload, artificial person, simulator, or a real-world instance in any specific medium.

## 4. What counts as the same organization? A bounded interface

The prior [subject-factorization gate](SUBJECT_CONSTITUTION_FACTORIZATION_GATE.md) established that a rule should transport observables and operations under redescription and that symmetry may prevent unique selection. We now apply the same discipline to a small input/state organization. The accompanying [verifier](verification/substrate_self_existent_interface.py) checks its arithmetic; this is a local finite illustration, not a model of brains or fundamental physics.

Let an abstract system have a bit `x`, an input bit `i`, output `x`, and local-step update:

```
x_next = x XOR i.
```

A physical encoding uses a bit `b` with `x=b XOR k`, where `k` is `0` or `1`, and updates `b_next=b XOR i`. For either coding and every `(b,i)`, decoding after the update gives the abstract update. A clamp of `x` to `a` is represented by setting `b=a XOR k`; it too must be transported. This is an exact **representation/encoding check**, not evidence that a biological or silicon system exists with the requisite organization. Two genuinely different media would need independently verified physical realizations, including their relevant operations, context and dynamics; merely writing a second encoding is not a new substrate.

**Observed-trace failure control.** A rival rule `x_next=x` matches four successive observations starting at `x=0` when all inputs are `0`. Nevertheless it disagrees with the target for both states when `i=1`. Matching one observed trajectory therefore does not show that the input-dependent organization is realized. In an actual experiment, the two interventions must be physically available and their mapping independently justified.

This conclusion does not require a realm of unactualized possibilities. The four input/state pairs specify a finite formal comparison; an intervention is meaningful when actually implemented or justified by a supported physical model. Strong plenitude is not an instruction to treat every mathematical table as metaphysically possible. More generally, matching a finite set of interventions is a useful check, but **does not solve implementation triviality** or establish that the selected operations, mapping, grain or boundary are uniquely relevant. See [Sprevak's survey of triviality arguments](https://marksprevak.com/publications/triviality-arguments-about-computational-implementation-2018/) and the existing [operational factorization work](EXPERIENTIAL_SUPPORT_FACTORIZATION_BRIDGE.md).

### A symmetry test for subject counting

Suppose, additionally, the candidate boundary set consists of two separate copies `L` and `R`, with fully symmetric inputs and no supplied feature distinguishing them. A selector that is a function of that input and respects exchange symmetry can select `{}` or `{L,R}`, but **cannot select exactly one**. This follows because a singleton changes under exchange; the verifier enumerates all four candidate subsets.

If an independent premise says at least one of those two candidates is a subject and no other candidates are allowed, both must be selected. Without that premise the empty answer remains available. If a whole-system subject is also an admissible candidate, the conclusion must be reconsidered: this toy does not exclude it. Symmetry alone does not prove there are two subjects, prove exclusivity, or resolve whether a whole and its parts can share episodes. It does show why a material-independent rule cannot arbitrarily choose one of two indistinguishable candidate copies and claim that the choice is structural.

### A separate quality-underidentification control

On the same abstract organization let two stipulations assign independently anchored labels by `q₁(0)=A, q₁(1)=B` and `q₂(0)=B, q₂(1)=A`. Both transport consistently between the two encodings. If `A` and `B` have independently fixed distinct phenomenal reference, the two mappings are different candidate identifications; if they are merely interchangeable names, their exchange may be only notation. The program verifies the algebra, **not** the existence or reference of any actual qualities. Invariance alone does not settle which interpretation applies, nor establish that either assignment represents a genuine possibility. This is the earlier [qualitative-equivalence distinction](QUALITATIVE_EQUIVALENCE_AUDIT.md) applied to the new substrate interface.

## 5. From DPMRS-R/DSH to the revised project

The source's DPMRS-R proposes a neutral ground and a subject selector `F=f(Φ,R)`; DSH then calls reality's structure a simulation and asserts the functional is derived. Neither the proposed `F` nor zero residue follows from unity and richness ([two-transcript analysis](TWO_EXPERIENCE_AND_REALITY_TRANSCRIPTS_SYNTHESIS.md)). The user's experiential-ground preference differs from an intrinsically non-experiential neutral ground, though a neutral *description* might describe an experiential ground. That compatibility must be argued, not assumed.

The revised proposal keeps the non-creator insight but replaces simulation as an account of the whole with self-existence. It **does not require** that reality fundamentally computes. If a local physical system implements a process, the separate question is whether that process has the organization sufficient for an experience. A description of rain is not thereby wet; whether a given organized process is itself an experience is precisely the constitution question, not something settled by the word “simulation.”

The computational model and the material realization must not be confused with the self-existent whole. The former depends on how the latter is articulated; treating the universe as information does not create information or prove that information exists concretely. “The whole is self-existent” and “its constitution explains why it is self-existent” also remain distinct: the former is the working thesis, the latter is the demanded completion.

## 6. Work needed to turn the preference into an account

The follow-up [context and subject-boundary gate](SUBSTRATE_INDEPENDENCE_CONTEXT_AND_SUBJECTS.md) tests whether a boundary verdict can depend on external coupling while the subsystem's entire stipulated local input/state organization remains unchanged. It separates boundary-local invariance from context-qualified invariance and examines the fragility of an exact-connectivity rule; it does not establish either rule as a true theory of subjects.

1. **Foundation (B1–B2):** strengthen the existing non-nothingness and experiential-foundation arguments into a non-circular case for *this* self-existent, intrinsically experiential constitution. A failure of an external-creator explanation does not by itself prove that candidate.
2. **Implementation:** specify the physical state variables, internal causal/relational structure, admissible operations, organization-preserving mappings, robustness and boundary/context before examining candidate realizations. Test changes of material and grain without assuming that superficial input-output matching fixes experience. Some matched systems may not be physically realizable.
3. **Incidence and quality:** independently argue for the subject rule and the bridge from actual organizational/experiential relations to anchored felt qualities. Then use the [subject interface](SUBJECT_CONSTITUTION_INTERFACE_RESULTS.md) to compare rivals; the idealized assay there is assumed, not calibrated. Do not let the desired answer enter as a label on the physical model.
4. **Local physics and time:** derive or recover the relevant local dynamics, records and time from the whole instead of taking the toy's update steps as fundamental. Our earlier clock and field work remains conditional, not a solution of quantum gravity or experienced passage.
5. **Plenitude and measure:** define which concrete local organizations are genuinely possible/actual and how distinct subject occurrences are individuated and weighted. Common organizational type does not fix token counts or probabilities. [Relational plenitude and measure](RELATIONAL_PLENITUDE_HISTORY_AND_MEASURE.md) shows why actual support does not supply a measure.
6. **Empirical discrimination:** specify a physically realizable pair of candidate systems, matched interventions, a rival that predicts a different target, and an independently warranted experiential/readout link. The comparison might constrain a **package** of implementation, subject rule and assay, but it would not automatically distinguish an experiential from a neutral metaphysical ground with identical records. Existing Roy data do not provide the missing timing anchor or calibrated assay.

The current [frozen battery](CURRENT_FRAMEWORK_BATTERY_DOSSIER.md) remains incomplete in B1–B2, subject and quality constitution, physics/time, measure and empirical discrimination. The verifier below checks only a finite formal illustration; it is not a new measurement, subject discovery, or complete account.

## Reproduction

Run `python verification/substrate_self_existent_interface.py`. Its [receipt](verification/substrate_self_existent_interface.json) records eight encoded transition cases, sixteen clamp checks, the two untested-input failures of the trajectory-only rival, the two exchange-invariant candidate sets, and the two stipulated quality maps. The general symmetry inference is analytical; enumeration checks the specified two-copy toy only.
