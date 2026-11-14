# Color experience and physical structure: an independently anchored test

## What is being tested

The preceding [positive construction](EXPERIENTIAL_FOUNDATION_POSITIVE_CONSTRUCTION.md) asked whether an experiential organization could carry a physical description. Here is an application to a real, independently studied phenomenal domain: **color appearance under controlled viewing**, compared with the physically measurable spectral composition of light.

The result is two-sided:

1. A single standard-observer color specification is **too coarse** to recover the spectrum of light or predict what happens after a wavelength-selective filter. That is a concrete failure of a narrowly defined proposed state, not a refutation of an experiential whole.
2. In a specified idealized model, an **ordered family of brightness matches after independently specified filters** does recover the four spectral intensities. This is a positive construction: an extended sequence of colorimetric distinctions can carry a physical distinction missing from one moment's color match. It does not yet establish that the colorimetric quantities are complete experiences or that the physical light is constituted by them.

This is an application of known colorimetry, linear algebra and observational factorization—not a new law of color vision. The quantitative pair below is calculated from published standard-observer data; it was **not** presented to people or physically built in this work.

## 1. Independent experiential and physical targets

**Experiential target.** A person may see two patches as matching in color and brightness even when the light sources have different spectra. That is an observer's visual appearance and matching judgment, not a spectrometer reading. Matching reports are evidence about perceived similarity, not a guarantee that two complete experiential episodes are intrinsically identical.

**Physical target.** A spectrometer can measure how much radiant power arrives in different wavelength bands. Different measured spectral distributions can be associated with a visual match.

These targets are not inventions of our finite model. [Shi et al. (2024)](https://doi.org/10.1364/OE.543789), *Optics Express* 32, 48051–48071, studied individual color matches from 100 observers and fitted cone-sensitivity models; 30 observers' matches came from earlier work and 70 were additional. The paper reports inter-observer differences, including greater inter-observer variability among older participants. Its experimental matches are related to, but are **not** the four-line synthetic pair computed here; their raw data were not reanalyzed. The paper's model does not establish identity of whole experiences, nor does an individual match establish a universal subject.

The calculation uses the CIE 1931 2° standard-observer XYZ color matching functions, not an actual individual's measured cone sensitivities. XYZ coordinates are colorimetric coordinates, not direct recordings of experiences or raw L/M/S signals. Equal XYZ predicts a standard-observer color match in the model; it is not proof that any particular real person's complete experiences coincide. The conditions of the underlying color-matching model—field size, adaptation, viewing context and relevant photoreceptors—matter.

## 2. Reproducible four-wavelength example

Choose ideal narrow spectral lines at **450, 500, 550 and 600 nm**, with relative *integrated radiant powers* in those bands. From four rows of the published CIE 1931 table, form a 3×4 matrix `C` whose columns are the XYZ matching-function values. For an intensity vector `p`, the standard-observer prediction is `q = C p`. The two positive, deliberately synthesized spectra are approximately:

| Wavelength (nm) | Spectrum A | Spectrum B |
|---:|---:|---:|
| 450 | 0.878970 | 1.121030 |
| 500 | 1.800000 | 0.200000 |
| 550 | 0.626224 | 1.373776 |
| 600 | 1.187143 | 0.812857 |

Using the **unrounded** values calculated from the table, both have the same XYZ vector, approximately

```text
(X, Y, Z) = (1.8367499, 1.9869501, 2.053659999).
```

The printed spectrum entries are rounded and will not produce exactly identical XYZ if recomputed from the displayed values. The included [verifier](verification/cie_metamer_experiential_gate.py) performs rational arithmetic using the four rounded source-table rows, constructs an exact null direction `v`, and takes `p_A = 1 + 0.8v`, `p_B = 1 − 0.8v`. It verifies `Cp_A = Cp_B` exactly **relative to those tabulated decimals**, not relative to an unrounded physiological truth. All four powers remain positive.

The calculation is an instantiation of standard metamerism, not a claim that these exact ideal spectral lines or powers were used in the cited experiment. Real sources have bandwidth, finite precision and optical context; matching must be individually checked.

**Source and provenance.** The four rows were retrieved from [pdbuchan/colorimetry](https://github.com/pdbuchan/colorimetry/blob/b542bec75fdc7946a380071dc1c450bf4e7d5687/data/CIE_xyz_1931_2deg.csv) at commit `b542bec75fdc7946a380071dc1c450bf4e7d5687`, Git blob `9b4e3f73b4bb412a762a6d03cb8060bfea652a6e`, full-file SHA-256 `fa663e3535a7e0763a745993a1f0a192eb0275ac46ad2d1befd7626841e713c1`. That repository identifies CVRL as its source. We independently checked the downloaded blob hash; this does not certify the underlying data against the official CIE publication. The verifier embeds only the four table rows needed, not the full source dataset. Its [JSON receipt](verification/cie_metamer_experiential_gate.json) records inputs and results.

## 3. Failure of the momentary color proxy

A spectrometer measuring only the 500 nm line obtains relative powers **1.8** and **0.2**: a difference of **1.6**, or a 9:1 ratio. Therefore the physical band-power function does not factor through the single XYZ vector `q`: two spectra with identical `q` have different physical band power.

There is also a successor-state failure. Place an ideal filter before the standard observer that passes only the 500 nm line. The two new XYZ predictions are

```text
A: (0.00882, 0.5814, 0.4896)
B: (0.00098, 0.0646, 0.0544).
```

The filtered predictions have the same chromaticity in this ideal calculation but differ ninefold in `Y`, the standard photopic luminance coordinate. Thus equal initial `q` does not determine the subsequent `q` under this specified filtering operation. This applies the exact factorization criterion to a source-based colorimetric model, with no external universal clock.

The inference has a clear boundary. `q` is a **standard-observer proxy**, not the complete present qualitative organization of a real person. The filter operation changes the physical stimulus and viewing conditions. Two actual matching judgments do not establish exact equality of all visual, bodily, contextual or whole-level experiences. Thus this is a decisive failure of **one explicitly defined model state**, not an empirical disproof of whole-level experiential closure or of experience's intrinsic priority.

## 4. Positive construction: an organized sequence can recover the spectrum

Assume a stable source drawn from exactly these four ideal bands, calibrated filters that independently transmit one band at a time, and a standard observer whose `Y` values are obtained by matches to a fixed brightness standard. The four filter settings and their order are part of the specified relational experiment. For each setting `i`, the modeled brightness match obeys

```text
Y_i = ȳ(λ_i) p_i.
```

Each of the four `ȳ(λ_i)` values in the table is positive. Therefore the four band powers are recoverable by the **fixed, independently given** map

```text
p_i = Y_i / ȳ(λ_i).
```

For the displayed pair, the 500 nm setting alone distinguishes them in the ideal model. All four measurements recover the full four-component spectrum in that model. The observable target—band powers—and the measurement arrangement—four filters and brightness matches—are separately specified; the reconstruction is an inverse of the physical color-matching model, not an identity inserted by renaming the answer.

This is stronger than claiming a single color impression reveals the source. It illustrates how **organized relations across multiple local appearances and interventions** can contain physical information absent from any one appearance. But it has explicit costs: the filter setting, its calibration, a brightness reference, source stability, comparability across matches, and the validity of the standard observer are inputs. If those are changed or unavailable, the inference must be redone. The calculation does not establish that all physical information is recoverable from actual appearances, that the settings are experiential, or that the observer retains a perfectly faithful phenomenal history.

In a real experiment, filter bandwidths could be represented by calibrated spectral response functions. If the resulting four-by-four measurement matrix is full rank, its inverse recovers the four source coefficients within calibration and measurement error; near-singularity can make the inversion unstable. Additional spectral degrees of freedom need additional independent constraints. No physical experiment, uncertainty analysis or subject calibration was done here.

## 5. Implications for the whole-first account

The single-color failure does **not** force a neutral substrate. A local person's present view may omit distinctions carried elsewhere in the actual whole, by other subjects, contextual relations, or later internal observations. Nor can the framework automatically assume that those distinctions are already phenomenal simply because they are part of the whole. Both the subject selector and the experiential constitution of the relevant relationships remain to be shown.

The positive construction sharpens the program:

- **Candidate:** the relevant base is a structured, genuinely experiential whole whose internally related appearances, rather than one person's momentary color, carry the required physical relations.
- **Needed:** independently specify what the experiential organizations, intersubject relations and admissible internal operations are; identify their physical counterparts without choosing them after seeing the answer.
- **Test:** determine whether the proposed experiential description is sufficient for a physically specified family of records and operations, including relevant contexts. Distinguish failure of a coarse momentary description from failure of a history-rich or whole-level one.
- **Still metaphysical:** even perfect operational reconstruction does not by itself show that the physical facts are *constituted by* experiences, that the whole is self-existent, or that it is one agentive universal subject. A neutral account may reproduce the same measurements and owes its own constitution argument.

This analysis is compatible with the user's strongest possibility = actuality: spectral examples and filters are specified as local model configurations, not as a claim that two unactualized complete wholes are metaphysically possible. The frozen foundation battery, physics/time, plurality, quality and measure gates remain incomplete.
