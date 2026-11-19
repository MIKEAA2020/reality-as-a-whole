# Particle emergence, locality and the subject-boundary question

## The supplied sources and what was read

- Jonathan Bain, **“Against Particle/Field Duality: Asymptotic Particle States and Interpolating Fields in Interacting QFT (Or: Who's Afraid of Haag's Theorem?)”**, *Erkenntnis* 53, 375–406, [DOI 10.1023/A:1026482100470](https://doi.org/10.1023/A:1026482100470). The supplied [journal PDF](sources/uploads/bain2000.pdf) has 32 pages. We extracted and read text from all pages, including notes and appendix; formulas suffered font/encoding extraction artifacts, the two figures were not separately visually inspected, and the underlying mathematical proofs were not independently reconstructed. SHA-256: `f7a58319ae3e089e6de77c10238ecaa5ef50192f0a8088ac79a8e42901dfc83c`.
- David Wallace, **“Emergence of particles from bosonic quantum field theory,” [arXiv:quant-ph/0112149](https://arxiv.org/abs/quant-ph/0112149)**. The supplied [LaTeX manuscript](sources/uploads/qftlocarx.txt) was read in full, including equations, diagrams in source form and bibliography. Its title, author and abstract match the arXiv record; byte-for-byte identity to the hosted version and any later publication was not checked. The manuscript's drawings were not rendered, and this reading was not a full proof or normalization audit. SHA-256: `42965aa615b0024345d6de5c14d5c4bd8efa605ff4037347058eaa83d30eb02b`.

This supersedes the previous abstract-only status for **these two** papers. James D. Fraser, [“Towards a Realist View of Quantum Field Theory”](https://philsci-archive.pitt.edu/14716/), was subsequently supplied as an 18-page draft and read in full as text; its scope and unverified final-version status are in [the Fraser and Schneidman assessment](FRASER_SCHNEIDMAN_SCALE_DYNAMICS_SOURCE_ASSESSMENT.md).

## 1. What Bain actually argues

Bain considers a specific **one-to-one particle/field duality thesis**, not every possible use of the word “duality.” In an interacting theory, on his account:

1. The LSZ formalism describes scattering in terms of incoming and outgoing asymptotic particle states and correlators of interacting fields. Under the paper's assumptions, it uses a weak asymptotic condition rather than the problematic identification of interacting and free fields at finite time. The formal limit and physical finite-time approximations are different claims.
2. A stable asymptotic particle can be interpolated by many local fields with the appropriate transformation properties and nonzero vacuum-to-particle matrix element. Thus there is no automatic one-to-one identification of a particle with a unique field expression.
3. Bain argues that quark fields provide a contrasting example of fields without isolated asymptotic quark states, and he defends approximately localized particle descriptions against a proposed Reeh–Schlieder objection. These are arguments about specified concepts, not a proof that QFT has no particles, fields or genuine interactions.

The word **approximate** carries weight: Bain's discussion explicitly allows tails and describes asymptotic regimes. His argument is not that Reeh–Schlieder fails, that wave packets are exactly localized, or that a spacelike signal can be sent. The theorem and LSZ conditions require their hypotheses; we have not re-proved them.

Bain's confinement example should not be read as a literal prediction that the static quark–antiquark potential in full QCD rises linearly without limit. With dynamical light quarks, string breaking can produce a pair of color-neutral mesons at sufficiently large separations. For an explicit numerical study see Bali et al., **“Observation of String Breaking in QCD,” [DOI 10.1103/PhysRevD.71.114513](https://doi.org/10.1103/PhysRevD.71.114513)**; only that paper's abstract and record were inspected here, not its full simulation or data. This qualification does not imply isolated color-charged quarks have been observed.

## 2. What Wallace actually constructs

Wallace starts from a massive, linear bosonic field and studies how an effective one-particle subspace may emerge. He does **not** claim that all quantum fields or all realistic interactions have been handled. His central requirements are: sufficiently localized states span the candidate subspace; effective localization behaves appropriately under relevant superpositions; and the subspace is preserved, at least approximately, by the dynamics over the relevant timescale. The relevant spatial scale in the massive Klein–Gordon example is set by the Compton scale, in the convention used in the manuscript. A one-particle wave packet can itself be spread out; the claim is about a subspace with an effective localization structure, not that every particle state is sharply localized.

Two constructions are developed: one via coherent-state approximations to classical field solutions and extraction of the linear one-particle component; the other via linear field observables acting on the vacuum. The paper distinguishes superposition of classical field configurations from quantum superposition of particle states. It explicitly stresses limitations for massless and fermionic fields, and for strongly interacting nonrelativistic matter. It compares its construction with Haag–Ruelle scattering theory rather than claiming to replace it. Wallace himself says his construction does **not** explain why the world is observed to be particulate; the measurement problem and decoherence remain relevant.

The manuscript takes fields as its starting ontology; it does not derive ontic structural realism, the intrinsic experiential ground or subjecthood. Bain and Wallace nevertheless agree on a useful point: **real and explanatory particle-level structures need not be fundamental independent little objects**. Their arguments and starting points are distinct, not one joint theorem.

### Attribution correction

In the earlier [structural-realism note](BAIN_STRUCTURAL_REALISM_AND_RELATIONAL_EXPERIENCE.md), we used the familiar Bell states `( |00⟩ ± |11⟩ )/√2` to illustrate that identical one-subsystem states do not fix joint relations. Wallace's manuscript section “Localised states in a field ontology” **already uses these same two states** to illustrate a related point: their individual reduced states coincide, while an appropriate superposition is locally distinguishable. Our additional `X⊗X` comparison is another elementary illustration of the same states, not a novel quantum result. We had not read the manuscript when we wrote the earlier note; this is an attribution correction, not a claim of prior independent priority.

## 3. The practical locality gate

The papers sharpen, rather than settle, the project's question of how plural subjects can be constituted without fundamental isolated objects.

### Exact local structure is not the same as an effective boundary

In a relativistic local QFT, spacelike-separated local observables commute under the usual locality assumptions. The Reeh–Schlieder theorem says, under its hypotheses, that vectors obtained by local operators acting on the vacuum form a **dense** set. Wallace's localization discussion emphasizes that a state may be indistinguishable from the vacuum outside a region for a particular localization criterion, while superpositions of such states need not satisfy that criterion. None of this says that ordinary local operations create arbitrary distant states **deterministically**, or that every spacelike correlation is a signal. The preparation operators in the mathematical density statement are not all deterministic, normalized laboratory channels; postselection and resource costs matter.

For a concrete finite illustration, take the familiar Bell state `(|00⟩+|11⟩)/√2` with one qubit each for A and B. Let A's two measurement Kraus operators be

```text
K₀ = √p |0⟩⟨0|,
K₁ = √(1−p) |0⟩⟨0| + |1⟩⟨1|,      0 < p ≤ 1.
```

They satisfy `K₀†K₀ + K₁†K₁ = I`. If A **postselects** the `K₀` outcome, it occurs with probability `p/2` and B's conditional state is `|0⟩⟨0|`. But if B is not told A's result, summing both outcomes leaves B's state `I/2`, independent of `p`. Conditional steering therefore does not transmit a controllable message without communicating the result. This elementary qubit example is a sanity check, **not** a model or proof of the Reeh–Schlieder theorem in QFT.

### Boundary rule required by our framework

A serious proposed subject rule cannot simply draw a perfect, sharply isolated boundary around a region, assume all tails vanish, and then treat the resulting separateness as proved. It should specify:

- the physical observables and interventions relevant to its candidate organization, including joint correlations and interactions;
- the effective regime, coarse-graining, clock/record timescales and tolerated leakage or error, and how each is estimated;
- whether the same verdict holds under equivalent descriptions and small, physically permitted perturbations;
- a comparison with alternative proposed boundaries, independently calibrated reports where possible, and controls for shared causes and postselection.

This is a **research requirement**, not a theorem that exact or effective subject boundaries are impossible. Wallace's effective-particle criteria are an inspiration for methodological clarity, not evidence that subjects have the same criteria, timescales, or quantum localization as his particles. A report's accuracy and a mathematical localization condition are not direct measurements of experience.

### What identical access can and cannot establish

Fix a family `F` of physical preparations and measurements. If two candidate models predict the same probability distribution for every allowed experiment in `F` but assign different subject boundaries, then no experiment confined to `F` can distinguish those assignments **by its physical outcome statistics alone**. This elementary identifiability statement depends on the chosen family: additional interventions, trusted independent reports or stronger independently justified constraints might distinguish the models. It does not prove that all conceivable physical experiments are insufficient, nor that distinct experiences really occur for the same complete physical state.

The user's two-aspect identity thesis might propose that the relevant organization and experience are the very same concrete reality. The papers do not supply the identity map, the rule for how many subjects exist, or why a given organization has one quality rather than another. Nor do they establish self-sufficiency, necessary plenitude or emergent spacetime. They do not require a universal subject.

## Scope of the advance

The paper recovery changes the earlier evidence base from abstracts to full supplied texts, supplies a specific contextual alternative to naive particle/field one-to-one ontology, and exposes a concrete operational requirement for our subject-boundary research. The Bell-state and no-signalling calculations are standard illustrations; the proposed application to subject boundaries is not a demonstrated new physical law, experiment or metaphysical solution.
