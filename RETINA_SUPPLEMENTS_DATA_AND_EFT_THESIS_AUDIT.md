# Retinal data, supplementary figures and the EFT thesis

## What was recovered

The user supplied [supplement 1](sources/uploads/41586_2006_BFnature04701_MOESM1_ESM.pdf), [supplement 2](sources/uploads/41586_2006_BFnature04701_MOESM2_ESM.pdf), [spike times](sources/uploads/Data_Spike_Trains.txt), [the raster display](sources/uploads/Display_Spike_Trains.pdf), and [a thesis](sources/uploads/stamped9022.pdf). The user also linked [supplement 3 in the repository's main branch](https://github.com/MIKEAA2020/reality-as-a-whole/blob/main/41586_2006_BFnature04701_MOESM3_ESM.doc); its exact bytes were obtained through GitHub's contents API and preserved [here](sources/uploads/41586_2006_BFnature04701_MOESM3_ESM.doc). All five supplied files and the linked document are preserved, subject to the user's authorization to include uploads in the public repository. Hashes are in the [source register](FRAMEWORK_SOURCE_REGISTER.md) and the data receipt.

The supplied `stamped9022.pdf` is **not Fraser's published chapter**. It is Dimitrios Athanasiou's [*Effective Field Theories: A Philosophical Appraisal*](https://ir.lib.uwo.ca/etd/8493), a 283-page thesis. We extracted text from all pages, read its abstract, contents, and the effective-realism discussion on printed pages 75–85 (PDF pages 87–97); this is not a full reading or proof audit of the thesis, its hierarchy/cosmological-constant arguments, or its figures. It cites James D. Fraser but does not replace Fraser's final chapter. The [publisher's record](https://doi.org/10.1093/oso/9780198814979.003.0014) remains accessible as a record, but the published chapter's complete text was not recovered for comparison.

The three supplementary plots were **visually inspected**. Figures 1 and 2 were rendered from the supplied PDFs. Figure 3's embedded PNG was extracted from the legacy Word OLE `Data` stream and inspected along with the caption available at the [publisher](https://www.nature.com/articles/nature04701). This checks the visual content of the embedded figure, not every detail of Word layout. The 40-cell raster PDF was rendered and visually inspected. None of these figures has been independently digitized.

## 1. What the supplementary plots do and do not show

- **Figure 1:** For ten-cell groups, plots for bin widths 5, 20 and 50 ms largely overlap at higher measured multi-information; there is visibly greater scatter and some substantially lower ratios at low multi-information. This concerns the studied sample and the ratio in the plot, not universal insensitivity to any time resolution.
- **Figure 2:** The displayed subgroup sizes are **3 through 10 cells**, with means near the upper part of the scale and error bars (caption: standard deviations over 250 groups per size). It does not demonstrate that pairwise accuracy persists unchanged for arbitrarily large networks or hundreds of neurons.
- **Figure 3:** The plotted average local and interaction fields change with group size from 2 to 10 cells. This is a pattern in the fitted statistical model, not a measurement of causal synapses, energy of distress, or a person's experience.

These plots sharpen rather than overturn the prior assessment. In particular, the pairwise statistical model is observational; the ferromagnetic intervention gate remains an independently stipulated physical model.

## 2. Data integrity and the repeat-count discrepancy

The [Princeton data record](https://dataspace.princeton.edu/handle/88435/dsp015425kd84r) says the dataset was used in Schneidman et al. Its [README](https://dataspace.princeton.edu/bitstream/88435/dsp015425kd84r/7) describes a 26.5-second movie, **145 repeats** and 3,842.5 seconds. Our full-file parse finds:

```text
40 named cells; 172,521 timestamp lines
first timestamp 0.01130000036 s; last 3179.55080032 s
no timestamp at or beyond 3180 s
```

These numbers agree exactly in cell and spike counts, and are consistent in elapsed time, with the **120-repeat, 3,180-second** dataset described in section 3.2 of Cocco and Monasson, [“Fast Inference of Interactions in Assemblies of Stochastic Integrate-and-Fire Neurons from Spike Recordings”](https://arxiv.org/abs/1102.5171). We inspected that paper's relevant section, not its full data or code. The 145-versus-120 difference is **unresolved**: a truncation, subset or other preparation difference is possible, but cannot be inferred conclusively from timestamps alone (including the possibility of an unrecorded or entirely silent tail). We do not silently use the README's 145 repeats.

For the bounded analysis below we use exactly **120 presumed repeat slots**, with 100 for fitting and the last 20 for checking, and 20 ms bins. Thus there are 132,500 training and 26,500 test bins. Movie phase, spike sorting, missing silent time and experiment duration were not independently established from the original acquisition files. Binning collapses multiple spikes of one cell in one bin: 172,521 spike timestamps become 151,939 occupied cell-bins across the chosen window.

## 3. A small independent held-out analysis

The [checker](verification/retina_spike_maxent_audit.py) implements a standard maximum-entropy fit directly; it does **not** claim to be the paper's original software. It uses five ten-cell groups: the first ten listed cells plus four groups from a fixed random seed. For each, it fits first and pairwise binary moments on the first 100 repeated presentations, summing exactly over all 1,024 possible patterns, then evaluates the last 20 presentations. The independent comparator has the same training single-cell rates. The 55-parameter fits match training single and pairwise moments to within `3.6e-8` in this run.

| Check | Result across five groups |
|---|---|
| In-sample `(S_independent − S_pairwise)/(S_independent − S_empirical)` | 0.910–0.947 |
| Held-out cross-entropy improvement of pairwise over independent | 0.034–0.097 bits per 20 ms bin |
| Held-out improvement divided by independent cross-entropy minus empirical test entropy | 0.781–0.891 |

Entropies here are **plug-in estimates without the paper's finite-sample correction**. The last row is explicitly a held-out predictive score relative to a saturated empirical test distribution; because the independent model is fitted on training data, its denominator is not exactly the test-set total correlation if single-cell rates drift. It should not be equated with the original paper's reported 90% metric. Both models are trained on the same movie, the held-out bins are temporally dependent, group selections overlap, and the test is not on a new movie, animal, neural population or intervention. No standard errors, uncertainty intervals or population-wide generalization are claimed.

A separate all-40-cell descriptive comparison gives a held-out probability of **0.04347** for at least five cells spiking in the same 20 ms bin, versus **0.002249** for a product-Bernoulli distribution using training firing rates. This is a comparison to a model of independence, not evidence of a causal mechanism or a conscious subject. Trial-level confounding by the shared repeating stimulus is possible. We have not reproduced every panel, bin-width/group-size comparison, cultured-neuron result, supplementary figure or error-correction extrapolation in the article.

Run from the repository with NumPy and SciPy installed:

```sh
OPENBLAS_NUM_THREADS=1 python3 verification/retina_spike_maxent_audit.py
```

The [JSON receipt](verification/retina_spike_maxent_audit.json) includes group identities, fit convergence, source hash, exact train/test convention and limitations. This is an exploratory robustness check, not a preregistered clinical result or a proof that 90% applies to all neural populations.

## 4. The code search: useful related software, not the original replay

We found the public [Maoz and Schneidman `maxent_toolbox`](https://github.com/orimaoz/maxent_toolbox), an MIT-licensed MATLAB toolbox whose README explicitly supports pairwise MaxEnt models and cites the original paper. The inspected repository HEAD was `82b4528675fed43beb1d90a1c06b43189afe023e`; its README and root listing were inspected, not a full source-code or executable audit. Its [Zenodo record](https://doi.org/10.5281/zenodo.191625) describes a later toolbox. We have **not** established that this is the original 2006 analysis code, have not run it, and cannot substitute its existence for an original-method reproduction. The Python checker above is a separate implementation of the established MaxEnt model, not novel authorship of the mathematical method.

## 5. What the thesis adds to the framework

In the passages inspected, Athanasiou develops a qualified effective realism: descriptions may refer to stable structures within particular regimes, even without access to a fundamental ontology. He also discusses Ruetsche's worry that coarse-graining may show robustness only inside a chosen space of candidate theories, leaving future theories outside that space unconstrained; a related empiricist challenge asks whether robust empirical structures by themselves establish a distinctively realist ontology.

For our framework this is a useful restraint on the substrate-independent experiential proposal. A preservation claim needs to state **which** physical observables, interventions, scales, and mappings are preserved, and separately why they preserve experiential identity. A well-fitting retinal model and an effective QFT both leave open that bridge. These sources do not derive necessary actuality, a timeless experiential ground, plural subjects, or the emergence of spacetime. The thesis's broader claims about naturalness, hierarchy and the cosmological constant have not been audited here and should not be presented as established conclusions of this note.
