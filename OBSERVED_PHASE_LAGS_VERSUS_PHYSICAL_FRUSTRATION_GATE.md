# Observed phase lags are not preferred interactions

## The decisive interface

A proposed route from music EEG to the user's relational misalignment idea might calculate phase differences between channels, treat their **observed mean lags** as each pair's *preferred* interaction offsets, and then calculate the minimum incompatible-cycle cost `F`. This route fails as an identification procedure in two opposite ways:

1. Perfect phase locking can make the inferred `F` **zero even when the stipulated physical interaction triangle is frustrated**.
2. Mean phase lags can produce a **positive** inferred `F` from an observational distribution equally compatible with a system having **no direct interactions at all**.

These are exact controls on a specific estimator and a specific model class, not a proof that experiential misalignment is false or that neural coupling can never be reconstructed. They turn the [MET label screen](MET_MUSIC_VALENCE_LABEL_AND_NEURAL_ACCESS_AUDIT.md)'s next-step requirement into a concrete stop rule: **do not name observed-phase-lag cycle incompatibility physical frustration unless interaction preferences, channels and their uncertainties have been independently identified.** An explicitly named descriptive statistic may still be studied as a predictor; prediction alone does not validate its physical interpretation or an experiential identity.

The starting point is the existing [frustration/channel-identifiability gate](FRUSTRATION_CYCLE_IDENTIFIABILITY_GATE.md), which already distinguishes channel preferences from net forces and allows independently identified channels to certify a lower bound. We are not claiming to have discovered phase-locking value, latent-common-cause confounding, or oscillator frustration. The new application below shows exactly why the tempting **substitution of observed EEG lags for those independent preferences** fails, including both false-positive and false-negative directions.

## 1. Three different quantities

For locally defined oscillatory phases `φ_i`, an independently specified interaction model may assign an edge weight `k_ij≥0` and preferred lag `a_ij`:

```text
E(φ) = Σ_(ij) k_ij [1 − cos(φ_i − φ_j − a_ij)],
F = min_φ E(φ),          D(φ) = E(φ) − F.
```

`F` is the minimum incompatibility of **those specified channels**; `D` is the additional current cost. Neither is an experience merely by being calculated. This potential model assumes reciprocal cosine interactions and a meaningful phase domain; non-potential, directed, hidden, higher-harmonic, forced and cross-frequency dynamics need different analyses.

A phase-locking statistic instead computes, over specified samples/windows or trials,

```text
C_ij = mean exp(i(φ_i − φ_j)),       PLV_ij = |C_ij|,
observed mean lag b_ij = arg C_ij,   only if C_ij ≠ 0.
```

`b_ij` describes the observed **marginal phase difference**, not automatically the direct channel's `a_ij`. `PLV` measures concentration, not interaction strength `k`. Setting `a_ij=b_ij` or `k_ij=PLV_ij` is an extra model assumption. It can be a defined index, but it is not independently verified energy or preference. Phase extraction, common reference and volume conduction, signal-to-noise ratio, latent input and sample size all matter.

Existing work makes related distinctions. Canolty et al., [*Detecting event-related changes of multivariate phase coupling in dynamic brain networks*](https://doi.org/10.1152/jn.00610.2011), contrast bivariate phase locking with a multivariate phase-coupling estimator and discuss hidden-variable limitations; its abstract and search-retrieved PDF passages were inspected, not its complete proof, data or figures. Bastos and Schoffelen's [*A Tutorial Review of Functional Connectivity Analysis Methods and Their Interpretational Pitfalls*](https://doi.org/10.3389/fnsys.2015.00175) discuss common references, field spread, common input and sample size; only its first two HTML chunks and search excerpts were read. These established results, not our toy, motivate the interpretational caution. Multivariate fits may recover parameters in a suitable model; no finite fitted distribution automatically identifies the causal channel structure in the presence of arbitrary hidden variables.

## 2. False negative: fully locked but physically frustrated

Take three unit-weight edges, all independently specified to prefer antiphase: `a_ij=π`. Their total cost is

```text
E(φ) = Σ_edges [1 + cos(φ_i − φ_j)]
     = 3/2 + (1/2)|exp(iφ₀)+exp(iφ₁)+exp(iφ₂)|².
```

The identity uses all three edges of the triangle. It gives `F=3/2`, attained for phases `(0, 2π/3, 4π/3)`: no assignment makes all three pairs antiphase. This familiar frustrated-triangle minimum is included as a control, not claimed as a new physics theorem.

Now suppose the observed phase configuration remains locked at that minimum. Each pair's PLV is 1, and each observed lag is just the corresponding difference of the three actual phases. If those three lags are inserted as preferred offsets, the same phases satisfy all three fitted edges simultaneously, giving **`F_fitted=0`**. The true-model configuration has `E=F=3/2` and `D=0`: it is a minimum, not an excited state. Strong phase concentration therefore does not establish absence of structural frustration, and minimum frustration is not the same hypothesis as state excess.

This example presupposes the antiphase edges; the observations alone do not establish them. It is not evidence that any human EEG has these channels or that any locked state feels unpleasant.

## 3. False positive: a cycle from averaging without direct edges

Use a separate exact binary-phase example, with `s_i∈{−1,+1}` denoting phases 0 or π. A common sinusoidal carrier may be multiplied by the signs; each realization yields three observable phase channels. Consider two explicit generators:

- **A, frustrated direct-channel model:** three antiferromagnetic binary edges with cost `H(s)=Σ(1+s_i s_j)/2`, in equilibrium with weight `2^(−H)`. Its minimum channel cost is **1**.
- **B, common-input model:** one latent variable samples the *same* eight-state joint distribution as A and supplies the three outputs; there are no direct pair channels, so by the stated absent-channel cost convention its pair-channel frustration is **0**. This deliberately constructed latent source can have a complex distribution; its existence is a formal rival, not evidence of a real brain circuit.

A's six states with two signs alike have cost 1 and probability `2/13` each; its two all-equal states have cost 3 and probability `1/26` each. Every observed pair has

```text
C_ij = E[s_i s_j] = −3/13,    PLV_ij = 3/13,    b_ij = π.
```

The same full **joint** probability of all three phase outputs, not just the pairwise moments, is stipulated in B. A 26-sample deterministic frequency table realizes the distribution exactly. In every sample, the three simultaneous relative-phase factors multiply to 1, because they telescope. Nevertheless, calculating each pair's mean first yields three negative resultants; their fitted phases sum to `π` modulo `2π`. These two facts are consistent because **the product of three averages is not the average of their pointwise product**. For a cosine triangle with inferred offsets `π`, plugging in equal unit weights reports `F_fitted=3/2`; setting each weight to the PLV `3/13` reports `9/26`. Both are properties of the stipulated *fitting convention*, not measured cost or coupling strengths. The PLV is modest in this example; an actual analysis must address uncertainty and any selection thresholds.

The true channel models here use binary interaction energies, whereas the naive fitted diagnostic uses a continuous cosine potential. Their numerical `F` values are **not directly comparable energy estimates**. The point is that a positive observed-lag diagnostic occurs even in B's no-direct-edge generator, and that even the complete binary observational distribution cannot determine the binary channel cost. Changing units or assigning the same phase-statistics to a richer biophysical model requires a new analysis.

### Exact identification limit and an intervention that distinguishes these examples

For any estimator `F̂` that uses only repeated observations from these stipulated identical distributions, A and B give it the same sampling distribution. With channel-cost values 1 and 0,

```text
E_A |F̂−1| + E_B |F̂−0| ≥ 1,
max(E_A |F̂−1|, E_B |F̂|) ≥ 1/2.
```

This is the elementary two-point identification bound, not a new general statistics theorem. The result persists with arbitrarily many observational samples under these two models; it does not say every possible intervention or measurement has the same distribution. An estimator can be accurate on both only after restricting the model class or adding information that distinguishes them.

For example, define a clamp that sets `s₀=+1`. In A, retain the same direct-channel energy and re-equilibrate the other two signs. In B, replace only the first output while leaving the latent source distribution unchanged. Then

```text
Pr_A(s₁=+1, s₂=+1 | clamp s₀=+1) = 1/13,
Pr_B(s₁=+1, s₂=+1 | clamp s₀=+1) = 5/26,
TV(the two remaining-sign distributions) = 3/26.
```

This distinguishes the specified generators *in principle*, not necessarily with feasible sample sizes. It is not the passive conditional distribution: conditioning on `s₀=+1` gives the same conditional statistics under both observational models. Nor is it an endorsed human EEG intervention. A real perturbation can alter couplings, common drive or measurement; its causal assumptions, ethics and side effects must be evaluated. Observing a mismatch in an intervention does not automatically identify a unique network.

## 4. Why high phase locking makes this shortcut self-defeating

There is also a general diagnostic for a triangle when all three means use **the same sample set and weights**. Let `u_ij=C_ij/|C_ij|`, `r_ij=|C_ij|>0`, and `H=arg(u₀₁u₁₂u₂₀)` be their wrapped cycle phase. In each sample, the product of the three unit relative-phase factors is 1. Write `v_ij=exp(i(φ_i−φ_j))/u_ij`. The product `v₀₁v₁₂v₂₀=exp(−iH)` is constant. For unit complex numbers, telescoping products and Cauchy–Schwarz give

```text
2 |sin(H/2)| ≤ Σ_edges sqrt[2(1−r_ij)].                  (1)
```

Indeed, `E|1−v_ij|²=2(1−r_ij)`. Thus if all three PLVs approach 1, their inferred cycle holonomy must approach zero, independently of the real interaction preferences. For equal PLVs exceeding `7/9`, the bound excludes the **exact** antipodal cycle `H=π`; it does not guarantee a small error in `F`, establish connectivity, or identify a true physical lag. If pairs are averaged over different windows or have different missingness/weights, the common-sample premise fails and (1) cannot simply be applied. A near-zero resultant also has an unstable or undefined mean angle, so thresholding needs predeclared, uncertainty-aware treatment.

A high-PLV state may be physically frustrated as in section 2. A nonzero inferred cycle can instead reflect heterogeneous phase states, common input, leakage, noise or genuine interactions. Those alternatives are not distinguished by the cycle angle alone.

## 5. What would make a real test admissible?

1. **Target:** pick a documented felt-affect question or, where only general valence exists, report that limitation. Match participants, trials and stimulus onsets to actual signal files; MET's nominal keys alone are not signal verification.
2. **Physical identification:** define sources or sensors, reference, frequency band, time horizon and channel model independently of held-out ratings. Use established multivariate inference as an alternative to bivariate plug-ins, report hidden-input sensitivity, uncertainty, goodness of fit, simulated controls and experimentally defensible perturbations or independent physical constraints where possible. If admissible models include both positive and zero channel `F`, report **unidentified**. Phase-lag-insensitive metrics mitigate some instantaneous-mixing artifacts but can discard genuine zero-lag effects and do not remove common inputs or prove causation.
3. **Predictive comparison:** when actual EEG is available, compare an honestly named observational index, independently identified physical candidates, established spectral/connectivity measures, and stimulus/category/familiarity baselines on identical participant/song-disjoint folds. Keep all windows of a trial together; compute uncertainty by participant and stimulus. If an index predicts ratings without channel identification, retain that limited association, not a physical-energy claim.
4. **Experience:** reports are valid evidence, not proof that experience is illusory. Even well-identified physical `F` or `D` must be anchored independently to qualitative character and subject identity. Experience, plurality and substrate-independence remain commitments or targets, not outputs of an EEG calculation. The required C3 remains **full structural and experiential intelligibility**, jointly with C1–C7. B4–B5 and B10 remain open.

## 6. Bounded data-access follow-up and a label hazard

The MET signals remain Git-annex links in the pinned mirror; no EEG samples were obtained here. A search found a separate [third-party DEAP classifier repository at commit `8f6fc99`](https://github.com/SiddhantGupta07/EEG-Based-Emotion-Classification/tree/8f6fc99b234e7cf42e1948de50c31be90c23860b), whose code claims wavelet features from DEAP. I inspected its README, license, `load_deap.py`, `creating_vector.py` and `svm_clas.py`, **not** its feature CSV, labels, original recordings or actual execution. The code assigns `x['labels'][tr][0]` to `labels_0.dat`, `[1]` to `labels_1.dat`, and `[2]` to `labels_2.dat`, yet the classifier calls `labels_1` valence and `labels_2` arousal. The [official DEAP description](https://www.eecs.qmul.ac.uk/mmv/datasets/deap/readme.html), available here only through search excerpts because page fetching returned HTTP 500, lists the four array labels in order **valence, arousal, dominance, liking**. If the linked scripts describe the actual files and use the documented source order, those classifier names are shifted: its 'valence' is arousal and its 'arousal' is dominance. The data artifacts and execution have not been checked, so this is a **conditional code-audit warning**, not a verified label correction.

The same loader opens `features_raw.csv` with write mode inside every trial while appending computed vectors elsewhere; the final raw file would ordinarily contain the last successfully written trial, not all trials, if that exact script completed normally. Its classifier fits and scores on the same `train_x` rows. These are code facts, not proof that the distributed artifacts were produced by that version. The repository's MIT code license does not establish rights to DEAP data or derivatives. The [official DEAP access page](https://www.eecs.qmul.ac.uk/mmv/datasets/deap/download.html) was available only as a search excerpt and describes an academic-research-only application and EULA. We did not download or analyze the data or assert that the third-party release is authorized.

## Reproduction and scope

Run `python verification/phase_observation_preference_gate.py`; the [receipt](verification/phase_observation_preference_gate.json) records exact rational probabilities, the clamp comparison, and continuous-phase checks. The stated triangle identity, two-point bound and inequality (1) are analytic; the code is a regression check, not a proof of the empirical premises. The earlier [selective-channel certificate](SELECTIVE_CHANNEL_CERTIFICATE_AND_HARMONIC_ALIAS.md) supplies a conditional positive route if channels can actually be identified.

Sources not fully read: besides Canolty and Bastos above, [Nolte et al., *Identifying true brain interaction from EEG data using the imaginary part of coherency*](https://doi.org/10.1016/j.clinph.2004.04.029), publisher abstract and introduction only, not full article, proofs or figures; [Olivares et al., *Phase Delays between Mouse Globus Pallidus Neurons Entrained by Common Oscillatory Drive Arise from Their Intrinsic Properties, Not Their Coupling*](https://doi.org/10.1523/ENEURO.0187-24.2024), abstract and opening only, not complete methods, data or figures; and [Vinck et al., *The pairwise phase consistency: a bias-free measure of rhythmic neuronal synchronization*](https://doi.org/10.1016/j.neuroimage.2010.01.073), abstract/search excerpts only, not full proofs or experimental data. The latter addresses sample bias of a phase statistic, not identification of physical channel preferences. No cited neural result has been independently reproduced here.
