# Timeouts and source access: explicit status

## Meaning of the test timeouts

The word **timeout** in the Claude-time workboard refers to local Python verification scripts, not failed paper downloads. Each module in the original [bounded regression batches](verification/formalization_regression_batch_01.json) was stopped if it did not finish within 12 seconds. Selected follow-ups were separately allowed 45 seconds. These limits were chosen to avoid repeating the earlier unbounded test discovery that ran for more than seven minutes and used roughly 1.36 GB without a verdict. A stopped module gives **no overall pass/fail verdict**: it does not establish an assertion failure, success, a missing source, or why it ran slowly. The runner uses quiet output, so absence of output does not imply no individual tests had completed.

Of 28 modules originally timed out in the eight batches, 23 subsequently passed a longer bounded rerun. The remaining five, with their latest recorded module-level result, are:

| Verification module | Latest bounded result | Topic, at a high level |
|---|---|---|
| [zero_dressed_history_pair_test.py](verification/zero_dressed_history_pair_test.py) | 12 s original; 45 s follow-up timed out | Dressed sphere/echo transport and constrained pairs |
| [zero_ownership_report_bridge_test.py](verification/zero_ownership_report_bridge_test.py) | 12 s original; 45 s follow-up timed out | Candidate ownership and physical report bridges |
| [zero_quantum_angular_echo_test.py](verification/zero_quantum_angular_echo_test.py) | 12 s original; 45 s follow-up timed out | Quantum angular echo, records and symmetry |
| [zero_relational_laplacian_test.py](verification/zero_relational_laplacian_test.py) | 12 s original; 45 s follow-up timed out | Relational Laplacian model |
| [zero_relational_link_symmetry_test.py](verification/zero_relational_link_symmetry_test.py) | 12 s original timed out; no later module-level rerun recorded | Relational link symmetry |

These files belong to the wider repository audit and **are not the 47 targeted tests in the φ⁴/Ising/modular group**, which completed successfully. Original and follow-up results are in [the rigor workboard](FORMALIZATION_RIGOR_REVIEW_WORKBOARD.md), with links to the machine-readable batch/follow-up JSON. The module count, 215 distinct passed modules with 1,586 tests, refers to the recorded bounded regression batches and timeout follow-ups; it is not a full-suite or a substantive-proof verdict. A timeout gives no diagnostic about which individual test is responsible unless a separately recorded verbose or isolated run shows it.

## The most recent failed fetch

On the φ⁴ pass, the page tool failed to fetch the **HTML representation** of João F. Melo, *Introduction to Renormalisation*:

- Failed URL: <https://arxiv.org/html/1909.11099>. The tool returned only `Failed to fetch page`, without a more specific HTTP cause. Do not infer that the paper or its PDF is unavailable.
- Paper record: <https://arxiv.org/abs/1909.11099>.
- PDF: <https://arxiv.org/pdf/1909.11099>.
- DOI (arXiv-issued): <https://doi.org/10.48550/arXiv.1909.11099>.

The prior review used a search result containing the relevant text; it did **not** directly read the full paper then. In this follow-up the PDF text extractor succeeded, and chunk 10 containing Eqs. (3.48)–(3.50) was read directly. It confirms the cited one-loop quartic beta coefficient and mass threshold in the stated convention. The paper has 67 pages and the extraction service parses at most 30 pages; only selected chunks, not the whole paper, were read. The review's separate derivation remains subject to its own stated approximations.

The other cited source is James M. Cline, [*Physics 198-730B: Quantum Field Theory*](https://www.physics.mcgill.ca/~jcline/qft1b.pdf), inspected via search-extracted relevant passages, not audited in full. His separately identified arXiv lecture notes [*Advanced Concepts in Quantum Field Theory*](https://arxiv.org/abs/2005.10241), DOI [10.48550/arXiv.2005.10241](https://doi.org/10.48550/arXiv.2005.10241), cover the same general subject; identity with every detail of the McGill PDF has not been established.

## Earlier identifiable access limitations

The repository's [source access and reading limits](SOURCE_ACCESS_AND_READING_LIMITS.md) is a **targeted, not exhaustive** historical log. Some earlier failures were later resolved; do not present an old failure as a current one. Examples that remain relevant or explicitly unresolved in their recorded audits:

- The original documents referred to in the Claude-time transcript as `chat-Unified Theory of Everything.txt` and `Yes. Under strict non-dualism, “why does the.txt` were not located under those filenames in the workspace; the transcript quotes them, but those quotations do not establish the contents of the complete originals. No DOI was identified. The actual [Claude-time chat](sources/uploads/DeepSeek-Claude%20time%20reconciliation%20critique.txt) **was** later supplied and preserved.
- A published quantum-chaos article's [supplement PDF](https://static-content.springer.com/esm/art%3A10.1038%2Fs41567-025-03144-9/MediaObjects/41567_2025_3144_MOESM1_ESM.pdf) and [data/code record, DOI 10.6084/m9.figshare.29069759](https://doi.org/10.6084/m9.figshare.29069759) failed in the page-fetch tool, according to the [source audit](STRUCTURAL_EXPERIENTIAL_INTELLIGIBILITY_TWO_PAPER_AUDIT.md). The supplied main article was read; its DOI is [10.1038/s41567-025-03144-9](https://doi.org/10.1038/s41567-025-03144-9). These older results have not been rechecked in this follow-up.
- The registration cited by Shelat and Giesbrecht, <https://osf.io/sev9k/>, previously redirected to sign-in and its APIs could not be accessed. No registration DOI or title was independently established. Their article DOI [10.3758/s13423-026-02930-7](https://doi.org/10.3758/s13423-026-02930-7) identifies the **article**, not a verified registration DOI; see the [specific access note](SHELAT_2026_ANALYSIS_CODE_AND_MODEL_REPRODUCTION.md).

Going forward, report the affected source or module, direct URL/DOI where known, the actual tool outcome, any successful alternative and the exact reading scope **in the user-facing answer**, not just in a file. A tool-access failure is not evidence that an item does not exist or is inaccessible to the user.
