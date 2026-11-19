# Timeless class operators, decoherence, and joint events

## Source and scope

J. J. Halliwell's [*Probabilities in Quantum Cosmological Models: A Decoherent Histories Analysis Using a Complex Potential*](https://arxiv.org/html/0909.2597v1), [published-paper DOI](https://doi.org/10.1103/PhysRevD.80.124032), was fully text-read as arXiv v1 HTML in all 21 chunks, including the appendix, references and figure captions. The eight figures were not visually inspected; equations were read as HTML/LaTeX text and selected ones compared to the [arXiv PDF extraction](https://arxiv.org/pdf/0909.2597), not systematically rendered. This is not a complete independent proof, numerical or figure audit. The published journal article has not been fully compared with the preprint. This supersedes the earlier partial-coverage note in [the detector assessment](HALLIWELL_TIMELESS_DETECTORS_AND_ORDERED_RECORDS.md).

The paper builds on established histories, arrival-time and complex-potential work, not a method invented here. In particular, it cites [Echanobe, del Campo and Muga](https://doi.org/10.1103/PhysRevA.77.032112) for an approximate projection-string/absorber connection; we have not independently read that full article. Its own [older detector-model paper](https://arxiv.org/abs/gr-qc/0008046) was fully text-read in a prior step, with limits recorded in the linked assessment.

## What the paper actually establishes or proposes

Halliwell studies reduced minisuperspace models and histories entering configuration-space regions without an external clock. In the chosen formulation, a complex absorbing potential defines a non-entry class operator as a scattering operator, with entry defined as its complement. When the relevant limits and domains exist, this is constructed to commute with the constraint. The absorber is part of a **class-operator construction**; it is not automatically a literal dissipative apparatus in the universe or a consciousness-triggered collapse.

Repeated arbitrarily frequent projections can create a quantum Zeno effect instead of the intended crossing behavior. The finite-strength absorber avoids using that limiting string in the same way, but one cannot take its approximations for granted. In a one-dimensional example the paper requires `1/τ ≪ V₀ ≪ E`: the potential must be strong enough over the crossing duration to suppress transmission while weak relative to the energy to keep reflection small. These inequalities can be jointly satisfied only if `Eτ ≫ 1`; in the given free-particle example this is a large-region/short-wavelength regime. This is not a universal numerical error bound or an implementation-energy budget.

For a single region, the paper relates the operator in a semiclassical regime to incoming flux through the boundary; its clean derivation assumes no more than two boundary intersections. It proposes a more general exact complex-potential expression for multiple crossings, but the simple flux approximation should not be extrapolated to repeated returns. For two regions it obtains a symmetrized product of intersection-number operators under stated approximations; the extension to arbitrary `n` is presented as a **guess**, not as a demonstrated general theorem.

The decoherence condition is separate from constraint commutation: class operators sum to the identity, but their branch probabilities become consistently additive when the relevant off-diagonal decoherence functional is sufficiently suppressed. For oscillatory WKB states and suitable coarse regions, the paper argues that crossing/non-crossing branches are approximately orthogonal and recover an ingoing-flux rule; for superpositions it relies on phase separation and averaging. It argues that exponentially varying WKB states generally lack the same mechanism, and suggests environmental decoherence for finer resolutions. These are model-dependent arguments, not a universal theorem that every large region or arbitrary state decoheres.

For continuous spectra, physical normalization uses an induced inner product rather than the divergent naive kinematic norm. Its Klein–Gordon appendix derives the sign-adjusted relation in a flat-space frequency-decomposable setting and flags the distributional subtlety in equating matrix elements at equal eigenvalue. One cannot generalize this to arbitrary constraints, spectra, boundary conditions or cosmologies by simply deleting a delta function.

## One apparent coefficient inconsistency

The arXiv HTML equation (122), also PDF-text equation (5.11), uses `Q=p√(1+iV₀/E)` and contains `(Q−p)/(2Q)` in the `x<y` term. For small `ε=V₀/E`, this factor is `iε/4 + O(ε²)`. The following HTML equation (123), PDF-text equation (5.12), prints `4iε` for the corresponding factor, a leading coefficient **16 times** larger. Both terms have the same overall minus sign in the surrounding expression. The [numerical coefficient check](verification/halliwell_green_coefficient_gate.py) and [receipt](verification/halliwell_green_coefficient_gate.json) support the expansion. This is an apparent inconsistency in the inspected preprint text; the PDF equation image and published version have not been visually checked. It does not negate the qualitative claim that this term is small as `V₀/E→0`, nor does it by itself invalidate the class-operator analysis.

## Finite joint-event gate

The paper's two-region formula makes an important requirement precise for the whole-account: **invariance and symmetry alone do not guarantee that candidate joint events have a probability interpretation.** The following exact toy applies the algebraic issue; it is not Halliwell's absorber, a counterexample to his specified WKB approximation, or a new decoherent-histories theorem.

Let the constraint be `H=diag(0,0,1)` and use its two-dimensional zero eigenspace. Within it take noncommuting projectors `P=|0⟩⟨0|` and `Q=|+⟩⟨+|`, where `|+⟩=(|0⟩+|1⟩)/√2`. Both commute with `H`. Define a symmetric joint candidate `J=(PQ+QP)/2`, inspired by the **form** of Halliwell's two-region expression, and take the normalized physical state `|ψ⟩=(|0⟩−3|1⟩)/√10`.

Construct four Hermitian candidate class operators: `C₁₁=J`, `C₁₀=P−J`, `C₀₁=Q−J`, `C₀₀=I−P−Q+J`. They all commute with the constraint and sum to `I`. Nevertheless:

| Quantity | `11` | `10` | `01` | `00` | Sum |
|---|---:|---:|---:|---:|---:|
| Linear expectation `Tr(Cρ)` | −1/10 | 1/5 | 3/10 | 3/5 | 1 |
| Branch norm `Tr(CρC†)` | 1/80 | 13/80 | 17/80 | 29/80 | 3/4 |

The linear joint value is negative and cannot be a probability. The four branch norms are nonnegative but sum to `3/4`, not 1: the omitted off-diagonal interference sums to `1/4`, with for example `D(11,10)=−3/80`. This is why completeness of the class operators does not itself imply additivity. The negative joint value remains `−3/100` after mixing in 20% uniform noise within the physical subspace. If `Q=P`, the commuting control has a decoherent, normalized family.

Performing an actual unread projective `P` measurement before `Q` is a different experiment: it gives sequential `P=yes, Q=yes` probability `1/20` but changes the `Q` marginal from `1/5` to `1/2`. Measurement cannot silently be inserted as if it preserved the original coherent situation. The [exact rational verifier](verification/timeless_symmetrized_class_gate.py) and [receipt](verification/timeless_symmetrized_class_gate.json) check all the displayed numbers, constraint commutators and the commuting control.

## Implication for a plural experiential whole

An internally relational account must identify (1) physical event operators or actual measurement instruments, (2) the physical state and inner product, (3) which event families satisfy an appropriate decoherence or alternative consistency criterion, and (4) a separately justified map from those physical structures to experiences and subject identity. Commutation with a constraint addresses a symmetry requirement; it does not supply the latter three tasks. The [earlier cyclic ordered-record example](HALLIWELL_TIMELESS_DETECTORS_AND_ORDERED_RECORDS.md) used mutually commuting effects; the present example shows why that success cannot be extended to arbitrary invariant questions.

This result neither denies real experiences nor demands consciousness collapse. A theory may use consistent histories, different contextual descriptions, a physical intervention, or another explicitly specified interpretation. Each has to preserve the relevant quantum predictions and explain which comparisons are meaningful. No universal subject or universal clock is assumed, and neither timelessness, necessary plenitude, a subject measure nor the emergence of spacetime is solved here.
