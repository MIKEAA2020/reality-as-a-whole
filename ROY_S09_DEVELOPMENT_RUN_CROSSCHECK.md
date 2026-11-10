# S09 EEG rule: development-run cross-check and next decision

## Result

As a further **post-hoc diagnostic**, I reapplied the same POz rule and two baselines using only the three original development runs. In each fold, the model is fit on two of scans 1–3 and evaluated on the third; no data from scans 5 or 7 were loaded or used in this check. The training and held-out runs remain recordings from one participant, already examined in earlier work.

| Held-out development scan | Fit scans | Pure-clean windows | EEG rule | Training-majority baseline | Timing-only baseline |
| --- | --- | ---: | ---: | ---: | ---: |
| 1 | 2, 3 | 33 | 20/33 = 60.6% | 18/33 = 54.5% | 12/33 = 36.4% |
| 2 | 1, 3 | 30 | 21/30 = 70.0% | 18/30 = 60.0% | 16/30 = 53.3% |
| 3 | 1, 2 | 33 | 13/33 = 39.4% | 21/33 = 63.6% | 18/33 = 54.5% |

The EEG rule exceeds these baselines in two folds but falls below both in scan 3. This reinforces the earlier [later-run result](ROY_S09_EEG_REPORT_TRANSFER_RESULTS.md): performance varies substantially by run. It does **not** establish that the rule or the frequency-tag method generally fails; there are few dependent windows, prior inspection and one participant. Folds share training data, so they are not independent replications. This check is not preregistered and provides no population p-value or experience accuracy.

## Interpretation and boundary

The inherited evaluation selects only two-second windows whose *recorded report* stays pure throughout and has no `bad_epoch` samples. That selection uses the report retrospectively and is not a deployable mixed-state detector. All other windows are failures under the deliberately conservative full-grid report-agreement score; they are not necessarily wrong experiences. Here, only **33/105, 30/105 and 33/105** windows are pure-clean in scans 1, 2 and 3. The EEG full-grid failure fractions are **80.95%, 80.00% and 87.62%**, respectively, under that convention.

The findings do not authorize selecting a better electrode, threshold or window size on these runs and then treating scans 5 and 7 as untouched tests: their outcomes have already been seen. Further S09 model development can be informative only if labeled exploratory, and it cannot deliver a person-independent result. No EEG–fMRI alignment or causal experiential link was inferred.

## Recommended next step

The most informative next test is a **different participant**, not another pass over these nine S09 runs. Before seeing that person's outcomes, freeze a report-decoding protocol and its comparison with timing-only and training-majority baselines. The existing model fitted on S09 scans 1–3 is one possible fixed transfer benchmark; it should not be tuned on the new person's reports. Independently verify the new participant's scan labels, signal schema, frequency mapping and any replay-source relationships; report all eligible and unresolved denominators and all scan-level results. One additional person is still a feasibility check, not population validation or report-to-experience calibration. A genuinely multi-participant test is needed for the latter empirical generalization, while an independent report–experience error bound remains a separate conceptual and empirical problem.

To respect the user's bounded-download request, no other subject has been downloaded. If another participant's **small EEG scan files** are supplied or selected, work on those without downloading their entire MRI subject archive. Author timing/volume information remains relevant to a separate EEG–fMRI analysis, not necessary for this EEG-only diagnostic.

## Reproduction and tests

The [script](verification/roy_s09_development_run_crosscheck.py) reuses the previous extraction, training and scoring functions unchanged. The [machine-readable output](verification/roy_s09_development_run_crosscheck.json) includes the full fold-specific confusion matrices, model parameters and conservative scores. Three S09 EEG files were re-fetched and their SHA-256 hashes checked against prior inventories; raw EEG and metadata remain outside Git.

```sh
PYTHONPATH=/your/deps python verification/roy_s09_development_run_crosscheck_test.py
PYTHONPATH=/your/deps python verification/roy_s09_development_run_crosscheck.py /private/path/S09_scan{1,2,3}_filtered_gac_cbc.mat
```

Synthetic tests verify run exclusion, scoring and stop rules; they do not validate human-report truth. The data release requests research/noncommercial use and citation of [Roy et al.](https://doi.org/10.1016/j.neuroimage.2017.02.041) and [Jamison et al.](https://doi.org/10.1016/j.jneumeth.2015.01.024).
