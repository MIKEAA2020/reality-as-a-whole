# Quantum position verification and financial dynamics: source assessment

## Source hierarchy and version choice

Choose sources by the strength and relevance of their evidence, not by an arbitrary cutoff. For experimental and technical claims, start with the latest accessible primary journal article and its methods; compare the authors' preprint or supplement for proofs and explicit changes. News articles help explain context but are not independent confirmation when they repeat the same release. A later version may contain corrections or stronger results, but lateness alone does not guarantee correctness; identify the actual change where possible.

- **Kavuri et al., Bell-test QPV:** the [Nature article](https://www.nature.com/articles/s41586-026-11247-3) is the journal source; its accessible abstract confirms the main localization comparisons. The full journal text was not available through our retrieval. The [arXiv v2](https://arxiv.org/abs/2601.16892) gives the methods and proofs we could read, and its author-supplied version note says v2 has new main text, added methods and significantly improved security against entangled adversaries. This is a concrete reason to prefer v2 over v1 for detailed theory. It does **not** mean that the experiment demonstrated security against arbitrary entanglement. We did not compare all journal text against v2.
- **García Díaz et al., quantum agreement:** the [PNAS article](https://www.pnas.org/doi/full/10.1073/pnas.2613021123) is accessible and its abstract confirms the key qualitative conclusions in our existing analysis; the [arXiv v3](https://arxiv.org/html/2511.21258v3) remains useful for the checked examples. We have not performed a complete comparison for possible journal revisions.
- The Phys.org, Science News and Quantum Insider links about Kavuri et al. describe **one experiment**. Quantum Insider labels its article a press release and closely repeats the NIST release; it is not another experiment or an independent technical validation.

See [the detailed position report](QUANTUM_POSITION_VERIFICATION_AND_SUBJECT_LOCATION.md) for assumptions, soundness, numerical results and a timing/spoofing control.

## What the Leiden article adds

The [Leiden/Phys.org article](https://phys.org/news/2026-02-quantum-ways-simulating-financial.html) describes **two separate research projects**, not a link that proves financial markets are quantum.

### Kanneworff: a different position-verification setup

[Kanneworff et al.](https://doi.org/10.1088/2058-9565/adf2da), described in their [preprint](https://arxiv.org/html/2502.04125), investigated a single-photon quantum-dot source and a two-photon interference measurement towards a loss-tolerant SWAP-based QPV protocol. This is distinct research, not another report of the NIST experiment. The authors state their setup did **not** achieve a complete secure demonstration; source purity and indistinguishability limited performance, and the experimental implementation did not include the classical response channel. They tested one polarization basis whereas the full proposal contemplates multiple bases. Therefore one must not transfer a security guarantee for the complete protocol directly to these component data.

A separate [coherent-state experiment by Fan-Yuan et al.](https://www.nature.com/articles/s41567-026-03439-5) reports two verifiers approximately 2 km apart and a verification range under 75 m, with a different protocol and resource/security assumptions. It is independent work, but not a simple replication of the device-independent Bell-test implementation. Comparing range or security across them requires the complete respective assumptions, not headline numbers alone.

### Dechant: simulated quantum-inspired generative dynamics

A directly relevant primary work by [Dechant and coauthors](https://arxiv.org/abs/2507.22035) trains a generator based on parameterized quantum circuits against a classical discriminator to generate synthetic S&P 500 log-return series. Its quantum circuit was **simulated on classical hardware**, using full state-vector simulation and matrix-product-state approximations. The authors report qualitative reproduction of several distributional and temporal features, although some effects are weaker and performance depends on depth and approximation settings.

The preprint reports qualitative comparisons with a classical GAN but explicitly notes different window sizes; the comparison therefore does not establish a matched quantum advantage. Their article's journal reference is [Machine Learning: Science and Technology, DOI 10.1088/2632-2153/ae39a2](https://doi.org/10.1088/2632-2153/ae39a2); the journal page returned an error during our retrieval, so the technical account here is based on the accessible preprint and may not include changes in the journal version. We have not rerun their code or analyzed their financial data.

The news story mentions possible prediction, but reproducing selected historical statistics is **not evidence of reliable out-of-sample forecasts**, profitable trading, a quantum speedup, or quantum-mechanical market dynamics. To establish practical improvement, one would need a prospective time-ordered evaluation, strong classical baselines under matched data and compute budgets, uncertainty and transaction costs, and tests across regimes.

## A useful limit for our record-and-history program

A standard construction from [limited-independence theory](https://www.cs.ubc.ca/~nickhar/W15/Lecture13Notes.pdf) gives a sharp control. Let `n≥3`. Compare two laws on length-`n` binary histories:

- `P`: all `2^n` histories equally likely;
- `Q`: all `2^(n−1)` even-parity histories equally likely.

For **every proper subset** of the `n` positions, their joint distributions are exactly the same. In particular, all single-position frequencies and all pairwise temporal correlations agree. Nevertheless, `P(even parity)=1/2` and `Q(even parity)=1`. Once the first `n−1` bits are known, `Q` fixes the last bit while `P` still gives either value probability `1/2`.

The proof is elementary: for any chosen `k<n` coordinates and assigned values, the uniform model has `2^(n−k)` completions, whereas exactly half of those completions have even parity. After normalization both probabilities equal `2^−k`. This is a known mathematical construction, not a new theorem. Our contribution is its **application as a precise countermodel** to the project question: matching all lower-order record summaries does not establish a unique joint history law or infer a unique higher-order dependency.

The [checker](verification/temporal_marginal_parity_gate.py) exhaustively verifies all proper coordinate subsets for `n=3,…,9`; the general statement follows from the counting argument, not the finite run. This is not a reproduction of Dechant's model, not a claim that its output has a hidden parity constraint, and not a theorem about infinite histories. It illustrates why selected stylized-fact checks, however useful, cannot by themselves fix all generative structure.

**Framework consequence:** specifying local relational records and a few observed temporal correlations does not yet determine a complete multi-time law, a subject measure, or conscious experience. To strengthen the account, state the proposed whole-history law and the precise accessible marginals, identify rival laws that reproduce those marginals, and specify which higher-order or intervention-based observation can distinguish them. The counterexample does not refute plenitude: one must distinguish **which histories occur** from the **weights or selection rules** assigned to them. It also supplies no mechanism of temporal actualization; it is an operational model of records, compatible with a timeless-whole research proposal but not evidence for it.

## Verification

Run `python verification/temporal_marginal_parity_gate.py` for the finite control and `python verification/qpv_causal_records_gate.py` for the separate spacetime and sequential-Bell toy checks. Their receipts contain synthetic checks only, not a proof audit of the papers or an empirical test of experience.
