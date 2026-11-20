# A bounded music-EEG signal and the limits of its labels

## Main result

We obtained and decoded **59,900 finite float64 samples from one channel of one trial** in the public MEEG example, using a 256 KiB compressed archive prefix rather than downloading the 96 MB archive or the full dataset. The available code declares the sampling rate as 1,000 Hz and its original first channel as Fp1; those are source claims, not independently checked acquisition facts. No labels were reached in the prefix. This is genuine numerical signal content, but it is **not a same-trial EEG–pleasantness result**, a verified montage or an independently validated raw acquisition.

A check of the pinned repository's preprocessing finds two concrete issues in its intended 50 Hz notch operation:

1. The caller invokes the per-channel filter but **discards its returned array**. On both a synthetic signal and the extracted example channel after the repository's bandpass, the exact caller returns values identical to its input.
2. The standalone helper calls SciPy's `iirnotch(50/1000, 50)` with the default normalized-frequency convention. At 1,000 Hz, that targets **25 Hz**, not 50 Hz. A separately specified `iirnotch(50, 50, fs=1000)` targets 50 Hz. This second issue concerns what the helper would do **if its output were used**; in the current caller the returned result is discarded.

These statements are about the **published code at the pinned commit**, not a proven defect in every version used to produce the paper, and do not establish the size or direction of any effect on its classifier accuracy. The preceding 1–50 Hz bandpass is still applied; saying 'the notch is ineffective' does not mean no preprocessing occurs. A single-channel check cannot identify network frustration or a subject's experience.

## Source, task and what the data establish

Xiao et al., [*MEEG and AT-DGNN: Improving EEG Emotion Recognition with Music Introducing and Graph-based Learning*](https://arxiv.org/abs/2407.05550), describe 32 student participants, 20 one-minute classical-music excerpts and 32-channel EEG at 1,000 Hz. Their paper says the EEG was annotated based on the **arousal and valence of the music**. This does not by itself establish that each label is a same-trial self-report of the listener's felt experience. The manuscript gives no independently verified subject-level rating instrument or rating-to-signal mapping in the parts read. Its claim that participant selection ensures emotional changes were *solely* due to music is stronger than the design alone warrants; context and individual variation remain possible.

The [repository at commit `9136727`](https://github.com/xmh1011/AT-DGNN/tree/9136727e6a1d7370cf0cd8fbf057a7662efd17fc) says `example/sample_1.dat` is MEEG participant 1. The compressed example is a Git blob of 96,062,569 bytes. We deliberately stopped the API response after 262,144 compressed bytes and locally decompressed its prefix. The tar member `sample_1.dat` advertises 306,688,410 bytes; the readable pickle header declares a `(20, 32, 59900)` little-endian float64 array. The first 59,900 numbers are contiguous in that array and finite. Their byte SHA-256 is `9b9ffdae1cff24a9466e45755c6cd2fe5ab387cc7d664c9b89adde3b5da8fe83`. **We did not execute the pickle**: the verifier checks the header and reads only numeric bytes. It did not reach `labels`, inspect remaining channels or authenticate the full archive against the Git blob hash. A prefix hash establishes what we used, not that the complete archive has been verified.

The GitHub source repository supplies an Apache code license; we have not established a separate data/recording license or the exact signal provenance. The binary prefix and raw samples are not committed. The source full dataset is linked via Google Drive, outside this runtime's allowed outbound hosts; we did not attempt a bulk transfer or use the other example, which is claimed to be DEAP.

## 1. Exact code and bounded experiment

The pinned [`train/prepare_data.py`](https://github.com/xmh1011/AT-DGNN/blob/9136727e6a1d7370cf0cd8fbf057a7662efd17fc/train/prepare_data.py) contains the operative pattern:

```python
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        self.notch_filter_per_channel(data[i, j, :], fs, Q)
return data

# inside notch_filter_per_channel:
w0 = Q / fs
b, a = signal.iirnotch(w0, Q)
param = signal.filtfilt(b, a, param)
return param
```

`filtfilt` returns a new array; the caller does not assign it back. With `fs=1000` and `Q=50`, the helper sets normalized `w0=0.05`. Without an `fs` argument SciPy uses its normalized convention (Nyquist = 1), so the center is `0.05 × 500 = 25 Hz`. See [SciPy `iirnotch` documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.iirnotch.html) for the established convention; the local numerical experiment checks its application, rather than re-deriving filter theory. If the 50 Hz noise is already controlled upstream, this code fact does not show it is present in the data.

Our verifier runs the **exact extracted source method bodies**, after verifying their SHA-256, on a synthetic 25+50 Hz mixture and on the example's first channel after the source's specified 1–50 Hz Butterworth bandpass. It compares against a deliberately explicit 50 Hz, Q=50 notch applied forward and backward. Relative Welch PSD at the named frequency is after/before; it is **not** a band-integrated power or a claim about statistical uncertainty.

| Input and operation | Output identical to input? | 25 Hz power ratio | 50 Hz power ratio |
|---|---:|---:|---:|
| Synthetic mixture, upstream caller | yes | 1 | 1 |
| Synthetic mixture, standalone upstream helper | no | 0.000373 | 0.999649 |
| Synthetic mixture, explicit 50 Hz notch | no | 0.999640 | 0.0000149 |
| Example channel after upstream bandpass, upstream caller | yes | 1 | 1 |
| Example channel after upstream bandpass, standalone helper | no | 0.092375 | 0.999649 |
| Example channel after upstream bandpass, explicit 50 Hz notch | no | 0.999639 | 0.002677 |

The corrected filter is only a diagnostic contrast, not a validated preprocessing recommendation or a revised classifier result. Power ratios vary with spectral content, filtering and estimation. We do not attribute either spectral peak to neural or mains sources, assume calibrated units or infer individual affect from them.

## 2. Evaluation design: outer trials versus inner segments

The paper describes trial-wise outer 10-fold and nested 4-fold cross-validation. In the pinned [`train/cross_validation.py`](https://github.com/xmh1011/AT-DGNN/blob/9136727e6a1d7370cf0cd8fbf057a7662efd17fc/train/cross_validation.py), `n_fold_CV` loops **subject by subject** and performs outer `KFold` on the first dimension of preprocessed trial/segment arrays. `prepare_data` then concatenates the segments of outer-training trials and fits per-channel normalization using that outer-training data; it applies those parameters to the held-out outer test. Thus, assuming the array has the documented `(trial, segment, …)` shape and code follows this path, **the outer split keeps segments of each trial together**. It is a within-subject, held-out-trial evaluation, not a test of a previously unseen participant. We have not reproduced the full trained model, so do not claim the paper's scores are caused by leakage.

The same code then passes the **flattened** training segments into `first_stage`, which creates `KFold(n_splits=3, shuffle=True)` and selects a candidate on segment-level validation. Segments from the same outer-training trial can appear in both inner training and inner validation; normalization also precedes the inner split. A synthetic witness in the verifier has disjoint outer trials but all three inner-training trials represented on both sides of an inner split. That witness proves possibility for the code path, not the actual overlap count in the authors' unknown seeds and saved results. The source uses three inner folds, whereas the paper describes four; the repository version may differ from the experiment code. The paper also says its table uses 'optimal values among ten trials with distinct random seeds'; the specific selection rule was not independently verified, so the extent of any selection bias is unknown.

The paper's reported 86.01% valence accuracy is therefore an **author-reported result under its stated task and evaluation**, not proof of unseen-person generalization, a trial-level felt-valence decoder, a physical channel-frustration measure, or a cross-dataset transfer of one fitted model. The paper's comparison with DEAP does not alone show that music causes emotions more effectively than videos: datasets, labels, populations and protocols differ.

## 3. Consequences and next step

The bounded signal clears one narrow access hurdle: actual signal bytes exist through an allowed GitHub endpoint, and the first source-described channel can be decoded without downloading the full archive. It does **not** clear the target requirement: we still lack independently documented individual felt-valence reports and a verified same-trial join. The public paper and prefix do not justify relabeling a music category as a participant's experience. A real positive next step is to find an accessible report-bearing dataset or independently documented MEEG rating files, verify stimulus/trial/person keys and recording timing, then compare neural candidates with stimulus and established spectral predictors on the same held-out units. Do not download the whole MEEG corpus just to guess label semantics.

Even a well-powered result would be evidence about a physical–report association, not an experiential identity theorem. We retain experience as a valid datum, plural subjects, substrate-independence as a preferred constraint, and **full structural and experiential intelligibility** as C3 alongside C1–C7. B4–B5 and B10 remain open.

## Reproduction and source scope

The [fixed plan](MEEG_BOUNDED_SIGNAL_AND_PREPROCESSING_FIXED_PLAN.md) was written after inspecting the paper, code and compressed/header prefix but before inspecting signal values. It is retrospective, not preregistration. Run the [script](verification/meeg_bounded_signal_audit.py) and [tests](verification/meeg_bounded_signal_audit_test.py); the [receipt](verification/meeg_bounded_signal_audit.json) records prefix and sample hashes, library versions, counts and aggregate spectral ratios. Use pinned source only: the script compiles three AST-extracted methods after checking the exact file hash; it never unpickles data. A truncated gzip prefix is intentional.

```sh
mkdir -p .arena/meeg/train
# The pipe closes after 256 KiB; do not remove head and inadvertently fetch the whole archive.
gh api 'repos/xmh1011/AT-DGNN/git/blobs/09359f5e5466a93010d8471d2e5f04d6252912c0' \
  -H 'Accept: application/vnd.github.raw+json' | head -c 262144 > .arena/meeg/sample1-prefix.gz
gh api 'repos/xmh1011/AT-DGNN/contents/train/prepare_data.py?ref=9136727e6a1d7370cf0cd8fbf057a7662efd17fc' --jq .content | base64 -d > .arena/meeg/train/prepare_data.py
python -m pip install --target .arena/meeg-deps 'numpy==2.4.3' 'scipy==1.17.1'
PYTHONPATH=.arena/meeg-deps python -m unittest discover -s verification -p 'meeg_bounded_signal_audit_test.py' -v
PYTHONPATH=.arena/meeg-deps python verification/meeg_bounded_signal_audit.py
```

We read all seven chunks of the arXiv v4 HTML prose, rendered formulas and captions for Xiao et al.'s [MEEG paper](https://arxiv.org/html/2407.05550v4), but not its figure images, publisher version, raw acquisition logs, complete sample archive, model checkpoints or dataset documentation on Google Drive. The GitHub README, run/parameter documents, dataset preprocessing, cross-validation and relevant training code were inspected; architecture implementation and full training were not replayed. The paper and repository are not established to be identical experiment versions. The SciPy frequency convention above was checked against the local `iirnotch` behavior and the linked documentation's complete HTML text; its example image was not inspected. Brookshire et al., [*Data leakage in deep learning studies of translational EEG*](https://doi.org/10.3389/fnins.2024.1373515), had previously been read only through its abstract and opening, not its complete study, figures or code. These access boundaries are part of the result.
