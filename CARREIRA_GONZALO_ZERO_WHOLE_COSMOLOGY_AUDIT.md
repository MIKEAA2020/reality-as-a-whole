# Carreira and Gonzalo: zero, creation, and an open universe

**Source:** Manuel M. Carreira S.J. and Julio A. Gonzalo (eds.), *Everything Coming Out of Nothing vs. A Finite, Open and Contingent Universe* (Bentham Science, 2012), DOI [10.2174/97816080546021120101](https://doi.org/10.2174/97816080546021120101). User-supplied PDF, 128 pages, SHA-256 `f8d9628250c45dbbb3ef2d83a941f8b273b0278b7f8c76edc95b426fe159ee34`. Page numbers below are the book's printed pages; the corresponding PDF page is eight higher. This is a focused reading of the central arguments, not an independent history-of-science review.

**Thesis of this audit:** the book identifies an important distinction that the zero-whole project must meet, but its empirical case for negative curvature is model-dependent, and its argument for an external creator adds metaphysical premises. A new common calculation shows that a vanishing cosmological constraint with a positive physical clock permits both an accelerating flat universe and a decelerating open universe with exactly the same age and Hubble rate. This directly connects the book's cosmology to our relational-zero work while exposing what zero alone does not select.

## 1. The strongest objection: a balanced whole is not an empty one

In chapter 6, pp. 34–38, Carreira distinguishes *absolute nothing* from a physical vacuum governed by quantum laws. His example of opposite charges whose sum is zero makes the essential point: zero charge does not remove the charges. A vacuum, law, capacity to fluctuate, or gravitational field cannot literally be presupposed in absolute absence and then presented as something produced by it.

This objection reaches our proposal directly. It does **not** show that a self-sufficient zero-whole is impossible. It does rule out treating either `+x − x = 0`, the empty set, or a Hamiltonian constraint as already establishing that an internally differentiated actuality is identical to absolute nonexistence. A structured zero state and absolute absence are different descriptions unless an argument establishes their identity in the relevant sense.

The constructive form of the project is stronger: **the whole is externally zero, while the very constitution of that zero entails its internal physical and experiential differentiation.** Here “externally” means without an external arena or time, not that an outside observer takes a measurement. This is a proposed identity/grounding claim, not the claim that two nonzero addends somehow disappear. It must explain why the actual terms, relations, subjects, and their weights are not independent extra premises. The zero-radius point and internal sphere offer a geometric language for this, but a blow-up adds directional structure mathematically and does not by itself prove that an undifferentiated point entails it.

A changeable part need not imply a changeable whole: an internally ordered history is compatible with a whole that has no external temporal evolution. Yet timelessness does not automatically make its particular laws or contents necessary. The authors' inference from the mutability of matter to dependence on an external immutable being (ch. 12, pp. 108–110) requires a further philosophical premise; it is not a Friedmann-equation result. Conversely, rejecting that premise does not itself derive the contents of zero.

## 2. What the book actually argues

- **Physical vacuum and creator:** the physical vacuum is not nothing (ch. 6, pp. 37–38). The authors propose a creator who sustains the universe, rather than merely initiating it (introduction, p. 8; epilogue, pp. 114–115). That is their metaphysical explanation, not an observational finding of a creator.
- **Hawking and Gödel:** ch. 2, pp. 14–15, reports Hawking's compact Euclidean, no-boundary proposal as a way to avoid imposed initial boundary conditions. Not imposing a boundary condition is not the same as eliminating all laws, a measure, contour prescriptions, or the question why the construction is actual. Ch. 4, pp. 20–24, recounts Hawking's concerns about completeness. Gödel's theorems have precise hypotheses about formal systems and do not establish that every theory of nature must be metaphysically incomplete. See the [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/goedel-incompleteness/).
- **A historical case:** chs. 7–10 connect Christian intellectual history and the development of science, including medieval natural philosophers. Such historical evidence is not a deduction that theistic cosmology is true; the book's broad contrast with other civilizations is an interpretive historical claim, not established by its examples alone.
- **Cosmology:** ch. 11, pp. 90–96, uses age and expansion to argue for an open, zero-Λ model and challenges dark-energy interpretations. Its strongest numerical inference depends on restricting the model class, as shown below.
- **Anthropic reasoning and design:** ch. 12, pp. 101–110, discusses observer selection, then presents chance or design as the principal alternatives and infers a freely choosing intelligent creator. Observer selection does constrain what an observer can find; it does not by itself explain the distribution of possible universes or prove purpose. Conversely, necessity of a differentiated whole is a third proposal, not simply chance or external design. The authors' step from changeability to contingency, and from contingency to a personal, freely selecting creator, requires additional premises. Their further discussion of immortality and resurrection (pp. 110–112) is explicitly theological rather than a cosmological measurement.

The book's assertion that an infinite collection automatically realizes every possibility (p. 104) is mathematically false in general: an infinite set can omit infinitely many possibilities. Equally, our necessary-plenitude proposal must not infer either actuality or equal weights from set size alone. Its core claim is that **genuine possibility and actuality coincide**, a substantive principle to be justified; calling unwanted alternatives impossible would not independently establish it.

## 3. The age–curvature counterexample

The book gives `H₀t₀ = 0.942 ± 0.065` and claims the flat value is `2/3`, concluding that spatial curvature must be negative (ch. 11, pp. 90–92). That benchmark holds for the spatially flat, matter-only, Λ=0 Einstein–de Sitter solution, not for arbitrary flat FLRW cosmologies. With negligible radiation and normalized present scale factor,

`H(a)²/H₀² = Ωm/a³ + Ωk/a² + ΩΛ`, with `Ωm + Ωk + ΩΛ = 1`,

`H₀t₀ = ∫₀¹ da / [a H(a)/H₀]`.

The new verifier, [carreira_gonzalo_age_curvature_constraint_test.py](verification/carreira_gonzalo_age_curvature_constraint_test.py), computes the integral with 128-point Gauss–Legendre quadrature after `a=u²`. These are theoretical examples, not fits to data:

| Model `(Ωm, Ωk, ΩΛ)` | `H₀t₀` | present `q₀` |
|---|---:|---:|
| Flat dust only `(1, 0, 0)` | 0.666667 | +0.500000 |
| Flat dust + Λ `(0.3, 0, 0.7)` | 0.964099 | −0.550000 |
| Open dust only `(0.044, 0.956, 0)` | 0.940407 | +0.022000 |
| Open dust only `(0.02146070445, 0.97853929555, 0)` | 0.964099 | +0.010730 |

The second row alone refutes flat-implies-`2/3`: its age lies inside the book's quoted interval. The fourth is numerically matched to the flat example's age with the *same* H₀, but its present expansion is decelerating, unlike the flat example. This is a model-comparison result, not a claim that all open universes decelerate. The age-matched models are distinguishable in principle by independent observables. Their dimensionless luminosity distances `H₀dL/c`, and differences in distance modulus at the same H₀, are:

| redshift | flat `H₀dL/c` | open `H₀dL/c` | open minus flat modulus |
|---:|---:|---:|---:|
| 0.5 | 0.661477 | 0.623000 | −0.1301 mag |
| 1 | 1.542854 | 1.489397 | −0.0766 mag |
| 2 | 3.628414 | 3.937184 | +0.1773 mag |

These illustrative rows are not a supernova likelihood, a full CMB calculation, or a comprehensive test of the book's alternative. They show why age/Hubble agreement alone cannot establish equivalent predictions. Real analyses must include radiation, baryons, perturbations, measurement uncertainties, calibration and covariances, and combine appropriate supernova, BAO, CMB and other observations.

For a relevant modern comparison, Planck 2018 temperature, polarization and lensing plus BAO, within its specified curved ΛCDM extension, found `Ωk=0.0007 ± 0.0019` (68%): consistent with flatness, not a model-independent proof of exact flatness. [Planck Collaboration, 2020](https://www.aanda.org/articles/aa/full_html/2020/09/aa33910-18/aa33910-18.html), §7.3. This is one specified analysis, not an exhaustive 2026 constraint review. DESI's three-year analysis, combined with other probes, reported dataset-dependent hints of evolving dark energy rather than a definitive discovery; its data alone were consistent with ΛCDM. [Berkeley Lab, 2025](https://newscenter.lbl.gov/2025/03/19/new-desi-results-strengthen-hints-that-dark-energy-may-evolve/). None of these numbers determines whether reality has an external creator or a zero ground.

A finite age or finite observable region does not establish that total spatial volume or total mass is finite. Negative *local* spatial curvature also does not by itself settle global topology or volume. Similarly, observational evidence for hot early expansion is not a model-independent measurement of absolute creation from nothing.

## 4. Concrete bridge: the same zero constraint supports both examples

Take a classical homogeneous FLRW minisuperspace with pressureless dust used as a physical clock, curvature and Λ. Set `8πG=1`, normalize present `a=H₀=1`, and work per unit fiducial comoving volume. On the expanding branch choose lapse `N=1`. With `k=−Ωk`, `Λ=3ΩΛ`, and dust clock pair `(T,P_T)`, the model constraint is

`C = −pₐ²/(12a) − 3ka + Λa³ + P_T = 0`,

`pₐ = −6a²H`, `P_T = 3Ωm > 0`, and `dT/dτ = ∂C/∂P_T = 1`.

These are **stipulated classical model ingredients**: the dust clock is matter, not an external master clock or a derivation of a preferred fundamental foliation. The gauge choice `N=1` is a convenient parameterization of this homogeneous solution. Analogous physical-reference-clock constructions are discussed by [Brown and Kuchař](https://arxiv.org/abs/gr-qc/9409001); their full model is not claimed to follow from this minisuperspace calculation.

At `a=1`, the four terms `(kinetic gravity, curvature, Λ, dust)` are:

- Flat accelerating example: `(-3, 0, 2.1, 0.9)`.
- Age-matched open decelerating example: approximately `(-3, 2.935618, 0, 0.064382)`.

Both sum to zero, but they describe different internal histories, including opposite signs of present acceleration. The tests check the constraint at several values of `a`, positive dust density `ρm=3Ωm/a³`, conserved `P_T`, and consistency of Hamilton's equations with the FLRW acceleration equation. Thus one concrete zero constraint is compatible with a material relational clock, nonzero local matter and multiple cosmological histories, rather than requiring a featureless or static interior. It also explicitly demonstrates **nonuniqueness**: `C=0` and matching `H₀t₀` do not select curvature, composition or a history.

The caveat is essential: `C` generates time-reparameterization gauge and its separate terms depend on the canonical model, normalization and chosen split. A finite comoving cell is not automatically the whole universe; for an open model it need not be a closed system, and even a compact spatial topology requires its own specification. The constraint's zero is not established here as an objective global gravitational-plus-matter energy. GR has local covariant stress-energy conservation, while a general expanding spacetime does not automatically provide a unique conserved global energy; see [Sean Carroll's discussion](https://preposterousuniverse.com/blog/2004/05/31/energy-and-intelligence/). The user's stronger substantive objective-energy thesis remains a possible research target, not a consequence of this example.

## 5. What a zero-constitution explanation must do next

The book makes the load-bearing challenge sharper. The target is not merely to exhibit a balanced model, but to show how zero's constitution entails a uniquely intelligible differentiated whole without externally selected ingredients. In particular:

1. **From zero to constitution:** demonstrate that the existence and relations of the internal sectors are intrinsic to zero in the relevant ontological sense, not inserted because `+x−x=0` is consistent. Give a criterion that distinguishes such a constitutive entailment from a model simply labeled zero.
2. **From possibility to actual counterparts:** derive when sign reversal is physically realizable and when the reversed sector is genuinely distinct rather than a gauge relabeling. For four-momentum, spatial reflection reverses momentum but preserves positive energy; it is not full four-momentum negation. Neither distinct mathematical sectors nor correlations alone establish distinct subjects.
3. **From plenitude to a measure:** determine which actual incidences and weights follow, including a well-defined sum or integral if needed. Equal availability of opposite signs does not itself entail equal weights; symmetry, invariance and convergence conditions must be demonstrated rather than chosen to enforce cancellation.
4. **From physical records to lived plurality:** derive or otherwise justify the relation between a subject, its particular occurrence and the physical relational structure. A dust clock, a qubit, a record, or a vanishing constraint is not evidence that it feels anything. Preserve multiple actual subjects, not merely formal copies.
5. **Experiential balance, if experience is the globally additive quantity:** identify an actual signed quantity, its composition law, counterpart operation and measure. Negative felt valence is suffering, not the absence of feeling; pleasure does not literally erase another subject's suffering. If some counterpart balances a global quantity, local suffering remains real. Whether valence belongs to such a fundamental sum remains open.

This is a constructive narrowing rather than an argument for tolerating residue: the requirements identify what the proposed necessity must actually secure. The user's claim that such a demand is satisfiable when structural and experiential aspects are recognized remains a substantive proposal, not refuted by the book or established by the toy model.

## Verification and related work

Run `PYTHONPATH=.arena/python-deps python verification/carreira_gonzalo_age_curvature_constraint_test.py` with NumPy installed (ordinary environment NumPy also works). Seven tests cover the flat benchmark, exact matched age, nonidentical distances and acceleration, constraint balance and nonzero dust density. They test the specified equations and numerical implementation, not empirical accuracy, quantum gravity, ontology or consciousness.

Related: [FLRW constraint and energy](ZERO_TOTALITY_FLRW_CONSTRAINT_AND_ENERGY.md); [zero point and internal sphere](ZERO_POINT_INTERNAL_SPHERE_CONSTITUTION.md); [necessary plenitude and sign pairing](ZERO_NECESSARY_PLENITUDE_SIGN_PAIRING.md); [subject boundary, report and causality](ZERO_SUBJECT_BOUNDARY_REPORT_CAUSALITY.md); [previous Ciupa audit](CIUPA_ZERO_POTENTIAL_OBSERVER_ALL_SECTOR_AUDIT.md).
