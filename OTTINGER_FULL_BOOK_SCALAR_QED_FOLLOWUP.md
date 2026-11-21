# Öttinger’s full book: scalar and QED follow-up

## Decision and scope

The newer user-supplied PDF contains the chapters missing from the [earlier excerpt audit](OTTINGER_DISSIPATIVE_QFT_UPLOADED_EXCERPT_AUDIT.md). It gives substantially more than a programmatic introduction: explicit perturbative scalar calculations, a Schwinger-model treatment and QED benchmarks. It **does not establish** a complete nonlinear, gauge-invariant, Lorentz-covariant, interacting 3+1-dimensional dissipative QFT, nor an experiential or metaphysical bridge. Several of the book’s own later calculations use simplified or reversible dynamics and the author identifies key open problems.

An independent, narrow check below recovers the stated high-energy angular and partial-cross-section formulas from the book’s *quoted* zero-friction annihilation amplitude. It also exposes a nonuniform forward-angle limit. This is a consistency check, not a new derivation of the amplitude or a test of dissipative QFT. The book’s numerical comparison has a significant electron-mass unit/axis inconsistency that must be corrected before using the plotted comparison quantitatively.

## 1. Source and access

Hans Christian Öttinger, [*A Philosophical Approach to Quantum Field Theory*](https://doi.org/10.1017/9781108227667), Cambridge University Press, 2017. The new attachment has 275 PDF pages and SHA-256 `9cf7570651354c897c965db9a0213e88e34992a8613ed8b9c72f4262f7d90559`. It contains the main text through printed p. 228, appendices, bibliography and index through p. 260, and appears to be the complete printed book. The file is temporary and not committed; no permission to republish its copyrighted content was established. Printed page references below differ from the PDF page number by 15 in the main body.

We examined extracted text for the later chapters, appendices and bibliography. Image-only pages 117–118, 131, 134–135, 201–202, 206, 208–211 and 230 were visually inspected; earlier image-only pages were inspected in the excerpt audit. We did not independently reproduce every formula or audit every bibliography item, figure, numerical calculation or cited experiment. Claims about the contents are attributed to the book; the calculations in §4 are the only new independent check here.

The book’s reference [153] is the [DELPHI 2004 LEP-2 annihilation study](https://doi.org/10.1140/epjc/s2004-01990-2); its abstract reports a Born cross-section derived from data at centre-of-mass energies 161–208 GeV in agreement with QED. We consulted the abstract, not its full analysis or data tables. Thus the book’s reconstruction and experimental uncertainties are not independently validated here.

## 2. What the later chapters actually establish or propose

| Material | What is done in the source | Correct boundary |
|---|---|---|
| Scalar field, pp. 110–135 | Uses simplified irreversible dynamics (SID) for selected correlation functions; calculates terms through second order, chooses counterterms and discusses the finite-lattice and continuum limits. At p. 125, eq. (2.51), the author reports numerical evidence but explicitly asks for estimates and clarification of the volume/dissipation limit interchange. | This is conditional, low-order perturbation work; SID drops terms of the full thermodynamic equation. Numerical evidence for one sum does not establish all-orders convergence or the full dynamics. |
| Scalar covariance, pp. 126–131 | A Fourier/symmetrized second-order continuum propagator is rearranged using the covariant integral representation (2.57), and the author presents a finite expression (2.59). | The continuum rearrangement and covariance claim concern this selected expression and its limiting/contour assumptions. Do not erase the separate unresolved finite-lattice question on p. 125; we have not independently justified its analytic continuation, convergence or interchanges. |
| Scalar scattering, pp. 134–135 | Defines a primary correlation and explicitly notes that `s → 0` and `γ → 0` do not commute, choosing the latter limit last. | This is a specific prescribed construction, not a claim all limits commute. The previous free-sector counterexample is consistent with the need to specify the prescription; it does not disprove the book’s chosen observable. |
| Interacting QED, pp. 169–176 | Discusses BRST structure and finite-dissipation coupling choices in a signed-inner-product formalism, with symmetry recovery sought in appropriate limits. | Algebra in an indefinite auxiliary space is not automatically positivity of physical probabilities, BRST invariance at every order, or existence of a physical interacting limit. |
| Schwinger model, pp. 176–197 | Treats the 1+1-dimensional massless model reversibly, deriving the familiar `e₀/√π` mass and discussing the physical sector and bosonization. | A valuable lower-dimensional check, but not a demonstration of the dissipative regulator or a solution of 3+1 QED. We have not independently reconstructed its derivation. |
| QED observables, pp. 200–219 | Develops lowest-order electron–positron annihilation, Ward cancellation and the electron magnetic-moment correction. The annihilation calculation explicitly uses vanishing dissipation (p. 204); the magnetic calculation also uses the zero-friction limit. | Agreement with familiar QED at those orders is a benchmark, not an empirical discrimination of finite dissipation or a full gauge-invariant construction. The stochastic demonstration discussed here uses momentum cutoffs rather than a demonstrated full dissipative interacting simulation. |
| Perspectives, pp. 225–228 | Lists open questions including finite-lattice convergence and interchange, zero-temperature limits, relativistically covariant dissipation, SID validity, Schwinger terms and measurement. | These are work items, not conclusions already achieved. Ontology, gravity and full weak/strong-interaction extensions are proposals. |

In particular, the author’s continuum expression and the outstanding finite-lattice estimates are **not the same claim**. Nor is a comparison with conventional-QED data evidence for finite nonzero damping unless a distinct finite-damping prediction and its uncertainties are computed.

## 3. Framework interface

1. **Continuum and locality:** [smooth-probe causality](THREE_DIMENSIONAL_SMOOTH_PROBE_CAUSALITY_GATE.md) and [complete instrument continuum](THREE_DIMENSIONAL_COMPLETE_INSTRUMENT_CONTINUUM.md) apply to their stated reversible models. Neither transfers to nonlinear interacting thermodynamic dynamics. For any proposed dissipative model, specify algebras, finite-regulator positivity, renormalized observables and cutoff/temperature/time limits; prove appropriate observable or instrument convergence and spacelike commutator or no-signalling bounds. The [quasilocal lattice result](research/quasilocal_limit/REPORT.md) is not a continuum QFT theorem.
2. **Gauge and physical state space:** exhibit a well-defined BRST-compatible regulator/evolution and physical sector, positivity and normalization of observables, and quantitative restoration of Ward identities and Lorentz covariance as limits are taken. An indefinite auxiliary inner product or a lowest-order cancellation is not enough.
3. **Time and ontology:** thermodynamic irreversibility may be a model of effective dynamics or a proposed fundamental law; a preferred unraveling is not automatically a unique sequence of physical events. The book’s space-time postulate differs from the project’s timeless-whole hypothesis, and neither derives the other.
4. **Experience and individuation:** particle/field dynamics, even if established, do not by themselves determine what experience is like, which system is a subject, or persistence across fission. See the [first-personal audit](FIRST_PERSONAL_GIVENNESS_AND_FIELD_INDIVIDUATION_AUDIT.md), [subjective-character bridge](SUBJECTIVE_CHARACTER_AND_NONCIRCULAR_FIELD_BRIDGE.md), and [lineage/fission gate](FIELD_LINEAGE_PERSISTENCE_AND_FISSION_GATE.md). No experiential evidence or metaphysical necessity follows merely from the formal calculations.

## 4. Independent gate: angular limit and forward nonuniformity

We start from the book’s **already derived** unpolarized, normalized zero-friction result (3.289), not from the QED Lagrangian or Dirac traces. Set `x=p/m ≥ 0`, `u=cos θ`, `|u|≤1`, and `F=|M|²/(4e₀⁴)`. In the book’s normalization,

```text
D(x,u) = 1 + x²(1-u²)
F(x,u) = [3 + x²(1+u²)]/D(x,u) − 2/D(x,u)².
```

The equivalent eq. (3.288) follows algebraically by substituting `q²=E_p²=m²(1+x²)` and `(p·q)²=m⁴ x²(1+x²)u²` and cancelling common factors. The accompanying [verifier](verification/ottinger_annihilation_gate.py) checks the equality exactly on 36 rational pairs, not universally by enumeration. Algebraic substitution establishes the displayed identity for the specified domain; the program also checks sample nonnegativity. Neither proves positivity for the full gauge theory.

At threshold, `F(0,u)=1`: isotropy. At each **fixed** `|u|<1`,

```text
F(x,u) → (1+u²)/(1-u²)       as x → ∞.
```

This matches p. 207. But at the forward endpoint `F(x,1)=1+2x²`, while the limiting expression diverges there. More strongly, for the interior sequence `u_x=1−1/x²` (`x>1`), direct substitution gives

```text
F(x,u_x)/x² → 2/3.
```

Thus convergence is not uniform on the whole angular interval: the two functions become unbounded in the forward region, even though fixed-angle convergence holds away from it. This does not contradict the book, which explicitly notes the high-energy partial expression diverges as `z→1` whereas the finite-energy total is finite. It does show why a fixed-angle asymptotic formula cannot simply be substituted into the full angular integral up to `z=1`.

Using the book’s cross-section normalization (3.290), `e₀²=4πα` and `q/p→1`, the fixed-`z<1` high-energy result is

```text
dσ/dΩ ~ α²/(4E_p²) · (1+u²)/(1-u²)
σ(z) = 2π ∫₀ᶻ (dσ/dΩ) du
     ~ πα²/(2E_p²) · [ln((1+z)/(1−z)) − z].
```

Here `z` is fixed strictly below 1 and `E_p=√(p²+m²)`; the integration domain follows the book’s treatment of indistinguishable photons. The antiderivative is elementary: `(1+u²)/(1−u²)=2/(1−u²)−1`. On every fixed interval `[0,z]`, denominators stay bounded away from zero relative to `x²`, giving uniform convergence there, so termwise integration is justified. The derivative/integration and factor reproduce (3.295), conditional on the source’s amplitude and normalization. Simpson quadrature independently checks four cutoffs; for `z=0.742`, the dimensionless integral is approximately `1.16782957249`. Finite-`x` samples approach this value. These checks do not independently reproduce the book’s full Dirac-trace result, flux normalization, radiative corrections, or data fit.

## 5. A numerical source warning: electron-mass units

On printed p. 209 the book states the electron mass is `0.511 GeV` and gives `1/m² = 1.4912×10⁹ pb`. The [2022 CODATA values published by NIST](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=958143) give approximately `m_e c²=0.510999 MeV`, i.e. **`0.000510999 GeV`**, not `0.511 GeV`. The stated mass is 1,000 times too large; the quoted area conversion is consistent with using the larger mass, and using the physical electron mass would make `1/m_e²` about one million times larger in the same units.

The figure’s abscissa is labelled `E_p/m` and plotted approximately 80–220. For the DELPHI abstract’s centre-of-mass energies 161–208 GeV, `E_p=√s/2` and the true electron `E_p/m_e` is roughly 158,000–204,000, not 158–204. If the data coordinates use the stated `0.511 GeV` mass, the scale is off by a factor of 1,000. We have not reconstructed the points, so this is an **axis/unit consistency finding**, not a claim that the experimental cross-sections or the leading `1/E_p²` physics are wrong. Correcting the mass and corresponding dimensionless axis together can leave a curve expressed in physical energy unchanged. The book’s error bars and fit require a separate comparison against the actual experimental tables.

## 6. Reproduction and next decisive work

- `python verification/ottinger_annihilation_gate.py` writes [results](verification/ottinger_annihilation_gate.json); `PYTHONPATH=verification python -m unittest ottinger_annihilation_gate_test` runs five focused tests. Exact rational comparisons and numerical quadrature support the stated limited checks; tests do not establish QFT or consciousness.
- A subsequent [scalar lattice regulator gate](OTTINGER_SCALAR_LATTICE_TIME_REGULATOR_GATE.md) proves finiteness for a specified grouped proper-time prescription at fixed positive mass and volume. Its [universal-gap follow-up](OTTINGER_SCALAR_REGULATOR_UNIVERSAL_GAP.md) derives the exact limiting difference from a common-exponential prescription and its convergence. Neither proves the original sharp-cutoff convergence or any friction/volume interchange. A gauge-compatible finite-regulator physical instrument and bounds through the proposed limits also remain to be formulated.
- Any empirical extension should reconstruct the DELPHI table, acceptance, radiative corrections and physical-energy axis, then compare a quantitatively specified nonzero-dissipation prediction with uncertainty. Conventional QED agreement alone cannot isolate that prediction.

**Status:** the full-book upload changes the evidential scope of the earlier excerpt audit, not the project’s unresolved formal and experiential status. C3 remains full structural *and* experiential intelligibility; B4–B5/F2, B9/F3 and B10 remain open. No external or complete framework pass is claimed.
