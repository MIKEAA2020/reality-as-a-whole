# QPV discrepancies: what the preprint supplement adds

## Bottom line

The authors' **arXiv v2**, submitted 8 August 2026, gives a coherent account of the extended run: **103 instances, 102 successes and one failure**, with the final instance said to fail because insufficient data remained. Its main text and its detailed analysis agree. This strongly supports that ordering as the *authors' intended preprint report*, but it is not an independent replay and does not correct the supplied PDF, which says the impossible reverse.

The preprint does **not** settle the arrival-time discrepancy. Its main text says **3 ± 2 ns**, its supplement narrative says **B arrives 9 ± 2 ns after A**, and its supplement timing table lists **A at 1766 ± 1 ns, B at 1769 ± 1 ns**, nominally a 3 ns difference. A further discrepancy concerns whether the 92.8 m prover distance is from A or B. Neither can be confidently corrected without clarifying the definitions and checking the underlying measurements.

## Sources and scope

I directly inspected [arXiv:2601.16892v2](https://arxiv.org/html/2601.16892v2), particularly its main Experiment/Analysis sections, supplementary sections III.2, IV and VI.2, and the [arXiv version history](https://arxiv.org/abs/2601.16892). The version history lists v1 on 23 January 2026 and v2 on 8 August 2026, both preceding the trusted current date of 31 October 2026. The v2 HTML also displays an internal date of 24 August 2026. The two passages within that preprint are reports by the **same authors**, not independent replications. I did not check the entire supplementary security proof.

The user-supplied ten-page PDF, hash and future-dated creation metadata are described in the [preceding audit](KAVURI_QUANTUM_POSITION_VERIFICATION_SUPPLIED_PDF_AUDIT.md). Its printing of the 102/103 numbers was checked against a rendered page. The publisher page returned by the retrieval service lists an 18 November 2026 publication date, later than the trusted date; it cannot establish publication by 31 October. A previous audit described selected publisher-supplement passages, but a fresh attempt to fetch that supplement failed, so this report does not treat it as newly inspected or as an as-of-date source.

The PDF names the experimental-data DOI `10.18434/mds2-4322` and says analysis code is available from the authors on request. Fetching that DOI and candidate NIST metadata/readme pages failed in this environment, as did the DataCite API lookup. A GitHub search returned no identified matching dataset or code repository; this is not proof that no public copy exists. No file list, data size, raw records, analysis code or formal correction was obtained, so no experimental analysis was replayed. Obtaining the dataset and author code remains the way to go beyond source comparison.

## 1. Pass counts

| Source | Basic protocol | Extended protocol | Evidence type |
|---|---|---|---|
| Supplied PDF, p. 5 | 224 passes / 232 instances; prints 96.5% | **103 passes / 102 instances**; prints 99.0% | Impossible extended count in the supplied text |
| Preprint v2, main Analysis and Results | 224 / 232; prints 96.5% | **102 / 103**; prints 99.0% | Author report; same experiment |
| Preprint v2, supplement VI.2 | 232 instances, eight failures | **103 instances, all but final succeeded** | Detailed author account of the same analysis |

Arithmetic gives 102/103 = **99.0291%**, normally rounding to 99.0%, and 224/232 = **96.5517%**, normally rounding to 96.6%, not the printed 96.5%. Truncation is one possible explanation of the latter, but the rounding policy is not established. The v2 account makes a swapped numerator/denominator in the supplied PDF plausible; it does **not** prove that explanation or validate either count from the raw data.

The detailed preprint says the basic and extended days had **474** and **420** one-minute files, respectively. As a conditional arithmetic illustration, **if** the first ten chronological files were the ten fault-free calibration files, then `(474−10)/2 = 232` full basic groups and `420−10 = 102×4 + 2` files: 102 full extended groups and a possible final short group. This matches the reported pattern but is **not a reconstruction**: the source allows detector faults and says calibration uses the first ten *fault-free* files, so the actual file boundaries and numbers of recorded trials must be checked. Four extended instances had fewer than the nominal 60 million analysis trials, not just the last. Their behavior cannot be established from file counts alone.

Supplement VI.2 describes truncating excess trials to the specified per-instance count and virtually padding short runs. For the basic factor, virtual trials contribute a factor of 1. For the bounded-entanglement analysis, the unrescaled `W′` contribution of a virtual trial is 1, but the modified `W″` factor and threshold include the entanglement penalty; it would be misleading to say those virtual trials simply have no effect on every equivalent form of the extended analysis. This procedural description is not an independent check of its validity or actual implementation.

## 2. Arrival timing

All times below are reported standard uncertainties, not 95% intervals; see the relevant source for its definitions.

| Source | Stated quantity |
|---|---|
| Supplied PDF p. 4; preprint v2 main Experiment | Challenges arrive within **3 ± 2 ns** of one another at the prover. |
| Preprint v2 supplement III.2 | The narrative says `uB` arrives **9 ± 2 ns after uA** at the prover. |
| Preprint v2 supplement IV, Table 1 | `uA` in at prover **1766 ± 1 ns**, `uB` in at prover **1769 ± 1 ns**, referenced to the same sync event; nominal difference **3 ns**. |

The table nominal difference supports the main-text magnitude, not the supplement's 9 ns narrative, if the quoted events are directly comparable. It does not independently measure the offset; the values come from the authors' timing accounting. Nor can we compute a reliable uncertainty for the difference from the rounded marginal uncertainties alone: shared timing errors and covariance are not specified here. Different measurement definitions, configuration/version differences or an editing error are possible. No effect on the localization ratios has been calculated or established.

Section IV explains that verifier release/receipt event times, not all prover-side events in Table 1, determine the target-region geometry; it reports checking timings on a few datasets and assuming constancy during actual data runs. This matters: a discrepancy in a descriptive arrival offset is not automatically a change of the four verifier timing inputs or a disproof of the reported region, and resolving it requires actual timing definitions and records.

## 3. Prover-distance label

The supplied PDF p. 3 and the preprint v2 main Experiment section say the prover is **92.8 ± 0.1 m from B**. Preprint v2 supplement IV.1 Table 2 instead labels **92.8 ± 0.1 m as the A-to-prover distance projected onto the A–B line**, with A–B separation **195.1 ± 0.3 m**. The same v2 supplement III.1 also describes the hardware as about 90 m from A, while III.2 says B is closer. These statements appear mutually inconsistent if they refer to the same station and coordinates.

For a point whose A-relative axial projection is 92.8 m between verifiers separated by 195.1 m, the B-relative axial distance would be **102.3 m**, so its three-dimensional distance to B cannot be less than that projection. That is a conditional geometry check, not an independently measured position or uncertainty estimate; it is important to confirm how the table defines coordinates and whether the text and table refer to the same physical locations. The four verifier timing events and A–B distance rather than the quoted prover distance determine the target geometry, according to the supplement. The label discrepancy therefore does not by itself falsify the paper's region calculation.

## What is and is not resolved

The most defensible count statement is **“the authors' preprint reports 102 of 103”**, paired with the warning that the supplied PDF reverses those integers. It is more informative than treating the two possibilities as equally supported, but remains unverified by raw records. The **3 versus 9 ns** disagreement and the **A versus B distance** label remain unresolved. None of these source inconsistencies alone establishes that the Bell test, statistical soundness claim, or quantum advantage is wrong; equally, neither should be silently dismissed without the relevant measurements.

The [small arithmetic receipt](verification/kavuri_qpv_discrepancy_checks.json) is generated by the [checker](verification/kavuri_qpv_discrepancy_checks.py). It uses transcribed source numbers and an explicit hypothetical file allocation, not actual files or trial records. The arithmetic checks, three prior geometry tests and 45 selected project regression checks passed; they do not verify the experiment or proof. The experiential and security boundaries in the earlier [PDF audit](KAVURI_QUANTUM_POSITION_VERIFICATION_SUPPLIED_PDF_AUDIT.md) remain unchanged.
