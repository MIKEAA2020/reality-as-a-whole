# Music, quantum structure and a sharper relational test

## Source and access

The supplied LinkedIn short link leads to Bridget Queenan, [*The musical structure behind quantum physics*](https://iai.tv/articles/the-musical-structure-behind-quantum-physics-auid-3393). This is the same article already examined in the [source audit](MUSIC_QUANTUM_EXPERIENCE_SOURCE_AUDIT.md), not a new independent experiment. The IAI's [alternate page](https://iai.tv/articles/the-musical-structure-behind-quantum-physics-auid-3393?_auid=2020) returned its prose and tables through the conclusion. Some displayed equations are image-only and were **not visually inspected**; the page also displays a subscription prompt. Do not claim the image equations have been checked or that the article is a peer-reviewed empirical demonstration.

## What carries over

Queenan's constructive insight is that relations among wave modes can be salient across physically different systems and useful for mathematical intuition. This fits a relational physical aspect without implying an external creator or a universal conscious subject. It does not follow that physical relations are merely descriptions without causal reality: physical oscillations, couplings, dissipation and records are real on our two-aspect proposal.

Keep four things apart:

1. A string's boundary conditions give a discrete series of **classical normal-mode frequencies**, while each classical mode can carry continuously variable amplitude and energy.
2. A quantum oscillator's energy eigenvalues are discrete and equally spaced in that special system. Quantum theory does not imply all spectra are equally spaced.
3. A musical tuning convention selects reference frequencies and intervals; that selection is not by itself quantum energy quantization.
4. Actual human perception and liking are subject- and context-dependent observations, not entailed by either set of formulas.

The useful analogy is *shared structures of constrained oscillations*; the overreach would be to say that auditory intervals derive the quantum laws, that sound waves constitute light, or that a bare mathematical ratio has a feeling. Quantum phonons in a material are a real quantum-mechanical example, not evidence that a chord is a conscious subject. Earlier citations and quantitative unit checks are in the [audit](MUSIC_QUANTUM_EXPERIENCE_SOURCE_AUDIT.md).

A concrete unit warning: `1 eV/h` is approximately `241798924208492 Hz`, while `880×2^38 Hz` is approximately `241892558110720 Hz`. They are close but not equal. One electronvolt is a chosen reference energy; a different reference energy gives a different octave-folded number. The physical energy of a fixed system does not change when we change units. Likewise the numerical value of a **dimensionful** constant depends on units and is not meaningfully called irrational independently of a unit convention. This does not make the article's musical analogy worthless; it prevents an approximate mnemonic from being mistaken for a new fundamental law.

## A constructive counterexample: same intervals, opposite spectral overlap

Existing work already studies timbre, interference and harmonicity: see [Marjieh et al.](https://www.nature.com/articles/s41467-024-45812-z) and their citations to Helmholtz, Sethares and other prior work. Their published abstract, introduction, and selected methods/results were inspected; raw data, code and supplements were **not** downloaded or independently replayed. The example below is a transparent application and test-design aid, not a newly discovered psychoacoustic mechanism or a claimed human result.

Let the lower virtual fundamental be `f`, and use two equal-power partials per tone. The upper tone has fundamental `r f` and the same relative partial indices as the lower tone. Compare two timbres and two intervals:

- timbre A has partial indices `{2,3}`;
- timbre B has partial indices `{3,4}`;
- interval 1 has `r=3/2`; interval 2 has `r=4/3`.

The fundamentals are missing from the actual two-partial stimuli; `f` here is the greatest common divisor of each tone's component frequencies, not a promise about perceived pitch. Define `C` as the sum of products of the **stipulated** lower/upper partial powers when their frequencies are exactly equal. Each partial has power `1/2`, so one cross-tone match contributes `1/4`. This is a physical spectral overlap index, not an established measure of hearing, roughness, neural mismatch or pleasure.

| Timbre | `r=3/2` | `r=4/3` |
|---|---:|---:|
| A, partials 2 and 3 | `1/4`: `3f = 2(3f/2)` | `0` |
| B, partials 3 and 4 | `0` | `1/4`: `4f = 3(4f/3)` |

For example, with `f=200 Hz`, A at `3/2` has components `{400,600}` and `{600,900}` Hz; B at `4/3` has `{600,800}` and `{800,1066.67…}` Hz. Changing timbre reverses which interval has exact spectral overlap. Neither interval's frequency ratio changed across timbres. A model that has only the ratio as input cannot reconstruct this two-factor index.

For finite spectral resolution, replace the exact match by a Gaussian of log-frequency distance with bandwidth `σ` cents. Our [checker](verification/timbre_interval_crossover_gate.py) verifies that this constructed crossover remains at `σ=1, 10, 50` cents. The log-frequency kernel is a deliberately chosen mathematical smoothing, **not a calibrated auditory filter**. It is invariant under common frequency scaling by construction, although real hearing need not be. The example does not synthesize or present sounds, and equal stipulated component powers do not ensure equal perceived loudness or equal combined acoustic intensity: relative phase and interference at coincident components matter. Real stimuli require waveform synthesis, measured spectra and controls.

### A model-independent contrast for a future study

For four observed mean ratings `y_A,3:2`, `y_A,4:3`, `y_B,3:2`, `y_B,4:3`, define the interaction contrast

```text
D = (y_A,3:2 − y_A,4:3) − (y_B,3:2 − y_B,4:3).
```

Any model predicting one mean for each interval but **no timbre effect** predicts `D=0`. For any four proposed predictions of that type, Cauchy–Schwarz gives the finite-sample descriptive bound

```text
RMSE across the four cell means ≥ |D|/4.
```

This follows because the contrast coefficients `(1,−1,−1,1)` have norm `2`; the ratio-only predictions cancel from the contrast. For the synthetic index above `D=1/2`, the bound is `1/8`, attained by predicting each interval's mean. This arithmetic adds no statistical confidence: actual sample uncertainty, repeated measurements, missingness and scale calibration must be addressed separately. A physical overlap crossover is **not evidence** that listeners' liking, experience or brains exhibit the same crossover.

## Turning the thought into a discriminating experiment

A future controlled, ethically approved study could synthesize a predeclared `2×2` interval/timbre design, randomize trial order, record the actual waveform and calibrate sound level and spectrum. It should include additional timbres, registers and small detunings, and independent ratings of pleasantness, roughness, fusion and perceived pitch. Compare: (a) an interval-only baseline, (b) established roughness/harmonicity and familiarity models, and (c) a fixed, independently specified overlap/relational predictor. Evaluate the predeclared interaction and held-out listeners and sounds using participant-level uncertainty. Use safe levels and account for potential phase, spectrum, pitch ambiguity, loudness and cultural familiarity. This is a proposed design, not a claim that the source's study tested these exact four sounds, or that this model outperforms established models.

This test isolates an important boundary for the user's misalignment proposal. An actual **timbre-dependent rating crossover**, if established under controls, would refute a universal interval-only valence law in that tested domain. It would not refute a more elaborate, independently defined relational mismatch that includes timbre and the listener's organization. Conversely, merely allowing such extra variables after the fact would not establish that model: they must yield distinctive held-out predictions and survive rival comparisons.

## Implications for the two-aspect whole

- The same physically real interaction may be described structurally and, if the identity hypothesis is right, be part of someone's experience. There is no extra immaterial force required to move the apparatus.
- A sound's spectral structure is not itself the listener's whole experience. The source, listener, coupling, attention, history and available causal organization must be specified, not collapsed into the ratio between two notes. Similar functional/acoustic outcomes across materials suggest useful substrate-independent descriptions; they do not prove two systems have the same experience.
- Musical liking, acute pain, subject boundaries and experiential ground remain distinct questions. A scalar overlap, energy or loss cannot be equated with unpleasantness by definition. The four-spin [integrated candidate](INTEGRATED_EXPERIENTIAL_MISALIGNMENT_CANDIDATE.md) also shows that local mismatch statistics need not decide subject multiplicity.
- None of this derives the intrinsic identity hypothesis, the necessity or self-sufficiency of the whole, the laws of physics, or actuality of all genuine possibilities. The latter is the user's timeless identity thesis, not an imagined production event. Nor is there an assumption of one universal subject.

## Verification

`python verification/timbre_interval_crossover_gate.py` checks the four exact spectral entries, the contrast, the ratio-only least-squares floor and three smoothing widths. The accompanying [receipt](verification/timbre_interval_crossover_gate.json) contains the computed values. The bound is a general elementary inequality; numerical checks do not supply a human experiment or settle metaphysics.
