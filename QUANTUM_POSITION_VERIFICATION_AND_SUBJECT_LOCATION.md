# Quantum position verification: records, location and subjects

## Current source-status update

The user has now supplied the full ten-page PDF, inspected in the [PDF-specific audit](KAVURI_QUANTUM_POSITION_VERIFICATION_SUPPLIED_PDF_AUDIT.md). It prints the extended-run counts as **102 instances, 103 passed**, which is impossible; the earlier 102/103 claim below came from the previously inspected preprint, not the supplied PDF, and remains unverified against the raw data. The PDF also prints 224/232 as 96.5%, whereas ordinary rounding gives 96.6%. It states 3(2) ns for challenge arrivals; an earlier inspected supplement was reported as stating 9(2) ns. Neither discrepancy is resolved.

The PDF's metadata gives a creation date of 2026-11-07, later than the trusted current date 2026-10-31, and its publication date field is `xx xx xxxx`. Some external links and version claims in this historical report are also dated after the trusted date. Treat them as previously retrieved or supplied material, **not independent proof that publication or those versions were available as of 2026-10-31**. The PDF is the evidence examined here; its provenance and version-of-record status are not independently established.

## The linked reports (historical source account)

The [Phys.org/NIST report](https://phys.org/news/2026-11-quantum-physics-person.html), [Science News article](https://www.sciencenews.org/article/quantum-physics-location-security), and [Quantum Insider article](https://thequantuminsider.com/2026/11/18/quantum-physics-can-verify-a-persons-location-nist-researchers-show/) discuss the **same NIST-led experiment**, not independent replications. Quantum Insider labels its text a press release and repeats NIST's account. The primary source is Kavuri and colleagues' [Nature article](https://www.nature.com/articles/s41586-026-11247-3), supplemented for detailed derivations by their [extended preprint, arXiv:2601.16892v2](https://arxiv.org/html/2601.16892v2). The accessible Nature abstract agrees with the preprint on the central comparisons; our numerical and security details below are drawn from the preprint. The full journal text was not available through our retrieval, so we have not completed a line-by-line comparison or ruled out journal-specific corrections.

The user subsequently supplied [a LaTeX main manuscript](sources/uploads/quantum_position_verification_main.txt) for this QPV paper, not the IAI debate. It agrees with arXiv v2 on the key points inspected, but has unresolved macros, editorial annotations and references to separate figures and supplementary proofs; its relationship to the journal version is not verified. The arXiv v2 main section and supplement differ on the stated challenge-arrival timing (`3 ± 2 ns` versus `9 ± 2 ns`); the [published supplement](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-026-11247-3/MediaObjects/41586_2026_11247_MOESM1_ESM.pdf) also states `9(2) ns` in S3B. We have not reconciled those statements or checked the raw timing records, and the published main text remains unavailable. Only selected supplement passages were inspected; the PDF text interface is limited to the first 30 pages, not a full security-proof audit. The published notice lists [NIST experimental data](https://doi.org/10.18434/mds2-4322), updating the supplied manuscript's on-request statement; neither the data nor analysis code has been replayed. See the [source-access audit](SOURCE_ACCESS_AND_READING_LIMITS.md) for scope and limitations.

The separate [source assessment](QUANTUM_POSITION_AND_FINANCIAL_DYNAMICS_SOURCE_ASSESSMENT.md) covers the revised preprint, an independent coherent-state experiment, the separate Leiden work and simulated quantum financial models.

**Bottom line:** the experiment gives a conditional, statistically quantified way to certify that a suitable quantum operation occurred within a spacetime target region. It is impressive evidence that **physical records and causal constraints can authenticate where information processing occurred**, even when the internal workings of the quantum hardware are untrusted. It does *not*, by itself, certify a person's identity, the location of their awareness, or a subject-constitution rule.

## 1. What the experiment did

Two trusted verifier stations send independently generated classical challenges towards a prover. The prover computes a function of the challenges—an XOR in the implementation—and uses it to select a measurement setting on one photon. A quantum verifier measures the other photon using its own setting. The prover's outcome is returned to both verifiers; recorded timing and the trial-by-trial correlations are used for a security test.

The paper's explanation is more precise than “a photon tells us where a person is”: a successful protocol constrains **where an input-conditional quantum action occurred**, relative to verified challenge and response events and a declared adversary model. The roles “prover” and “verifier” may be implemented by hardware; they are not measurements of consciousness. Repeated timing alone can localize a *single* honest responder, but colluding responders can spoof that assumption. The Bell-test analysis plus causal/adversary constraints addresses that stronger question.

The authors report:

- verifier separation `195.1 ± 0.3 m`, approximately `250,000` trials per second, and measured detection efficiencies above `81%` at both relevant measurement stations;
- two and four minutes per protocol instance in the two experimental analyses, with nominally 30 million and 60 million trials respectively;
- 224 passes of 232 basic instances; the previously inspected preprint was reported as 102 passes of 103 bounded-entanglement instances, but the newly supplied PDF prints the reverse and is internally inconsistent. At issue is a **per-instance soundness target** `δ=2^−64` against the stated adversary class, not independent confirmation of the counts;
- a one-dimensional region `2.47 ± 0.02` times smaller than the ideal classical comparator, and a **three-dimensional volume** `4.53 ± 0.05` times smaller than the same-latency classical comparator. The same-latency one-dimensional factor is `4.48 ± 0.02`. These are different comparisons; the 4.53 volume ratio should not be reported as the 1D length ratio.

These are authors' reported measurements and analyses; we have not downloaded their raw records or independently reproduced their experiment. Passing a statistical test at a chosen error threshold is not a posterior probability that a named person is at a location.

## 2. What “device-independent” and “secure” mean here

The quantum measurement devices and source need not be trusted internally. However, the security claim still assumes, among other things:

- trusted and physically secured verifier laboratories, known verifier locations, classical computing and sufficiently accurate event timing;
- the stated treatment of interfaces, settings distributions, independence, trial boundaries and light-speed causal constraints;
- a declared class of adversaries, including restrictions on entanglement **already shared at the relevant trial boundary**.

For the simplest case, adversaries have no prior shared entanglement. In the implemented weak-entanglement analysis the paper sets the allowed **average robustness of entanglement** to `8×10^−6` across trials. This is a particular entanglement measure, **not** a count of ebits, not the probability of an attack, and not a measurement proving that arbitrary attackers satisfy the assumption. The authors' revised preprint additionally proves conditional security for stronger adversaries under more complex challenges and other specified resource bounds; those longer-challenge settings should not be conflated with the demonstrated single-bit XOR implementation.

The authors describe an attack against the experimentally implemented version using adversaries sharing two appropriately prepared qubit pairs. More generally, [Buhrman et al.](https://arxiv.org/abs/1009.2490) give impossibility results for unrestricted pre-shared entanglement in the standard position-verification model. Thus “any manipulation makes the test fail,” “unconditionally secure against every attacker,” and “no-cloning alone proves location” are too broad. An adversary can also cause denial of service without successfully spoofing the target. A comparison with a classical protocol is conditional on the specified geometry, signal latencies and adversary model; the paper notes that its classical comparator's security does not require the same restriction on adversary entanglement.

## 3. Why timing and records are not redundant

Consider a **different synthetic** 1D toy, not the experiment: verifiers lie at `x=0` and `x=200 m`, emit challenges simultaneously, and accept responses by `T=(200+20)/c`. With light-speed signals and instantaneous processing, a single station able to receive both challenges and return to both verifiers lies in `[90,110] m`. A station at `100 m` can compute XOR and return both responses after `200/c ≈ 667.13 ns`.

But two colluders at `0` and `200 m`, each outside that target interval, can exchange the classical challenges, compute the XOR separately and send matching local responses at the *same* time `200/c`. For all four possible challenge pairs, their timing and answer records match the single-station toy. The formal checker enumerates those four cases. This is a specific classical spoofing strategy, not a proof about every possible protocol, and it does not simulate the experiment's photon, Bell statistic or adversary bound.

The conclusion is useful for our framework: **a consistent pair of records and a common output do not themselves establish a unique processing site**. A causal model must rule out distributed ways of producing those records. Likewise, if an authorized device inside a certified region responds on behalf of a remote operator, the physical protocol can certify the device operation while the operator is elsewhere. An identity or human-presence claim needs an independently defended access-control or person/device binding; it does not follow merely from a successful position test.

This is a conditional operational observation, not a demonstration that actual apparatus was remotely controlled or that human experience is nonlocal. It also does not assert that two subjects are one, or that a device is a subject.

## 4. Finite evidence without pretending certainty

The paper uses **test factors**: nonnegative trial statistics with conditional expected value at most 1 under every adversary in the specified null class, even given the past. Their product is therefore a nonnegative supermartingale. If the declared protocol passes only when the product reaches `1/δ`, the chance of a false pass is at most `δ` under the premises. This is a standard e-value/test-factor construction used by the authors, not a new method from us. It allows soundness arguments that do not simply assume adversarial trials are iid; its validity depends on the conditional bound and the defined adversary class.

For a simple independently checkable **illustration**, the accompanying verifier uses an ideal uniform CHSH game. Local hidden-variable strategies win with probability at most `3/4` per trial under the stated independent-setting assumption. If `0≤λ≤1/3`, use a factor `1+λ` for a win and `1−3λ` for a loss. Its conditional expected value is at most 1 for any local strategy, including one that depends on past trials. Choosing `λ=(√2−1)/3` and 2,000 idealized trials, a product threshold of `2^64` requires at least 1,678 wins. Under an **iid ideal quantum CHSH** win rate `(2+√2)/4`, the illustrative pass probability is about `0.968`; the supermartingale false-pass bound for the declared local class is `2^−64`.

This is **not** the NIST experiment's test factor, trial count, physical noise model, adversary reduction, data, or security certificate. In particular, an ordinary Bell violation alone does not establish the QPV spacetime-security reduction. Its purpose is to make the distinction between conditional soundness, honest-device success and exact certainty concrete.

## 5. What this contributes to the whole-account

1. **Operationally local, not fundamentally spatial.** The protocol presupposes spacetime, light cones, signals and calibrated clocks. It gives a conditional local-spacetime constraint; it does not derive emergent spacetime from a timeless absolute or introduce a universal external clock.
2. **Records constrain but do not constitute experience.** The result motivates explicit record provenance, a target region, accessible information and adversary models in cross-perspective comparisons. It does not decide which physical processes are experienced, explain felt qualities, or establish a physical-to-phenomenal bridge.
3. **Agreement is not identity.** Matching records, common challenge-response behavior and a sound location certificate are separate from common subjective identity. The [earlier two-report gate](TWO_REPORTS_CONSENSUS_AND_REVERSAL.md) and [quantum-agreement analysis](QUANTUM_AGREEMENT_PLURAL_PERSPECTIVES_AND_RECORDS.md) remain relevant, but their assumptions differ from this experiment's.
4. **Do not infer a creator or simulator.** The protocol tests operations *within* an assumed physical world; it does not establish that our reality is simulated or created, or that possibility becomes actuality in time.

**Research implication:** when proposing a local subject or a cross-perspective link, state four separable targets: (i) physical-operation location, (ii) source/device authentication, (iii) agent or person binding, and (iv) independently justified experiential constitution. QPV can conditionally support (i); additional premises and experiments are needed for the rest. That is a sharper interface requirement, not a solution to the remaining foundation or subject-measure gaps.

## Reproduction and scope

Run `python verification/qpv_causal_records_gate.py`. The [receipt](verification/qpv_causal_records_gate.json) contains the idealized classical-spoofing/identity control and a separately defined synthetic sequential-CHSH test-factor calculation. They do not reproduce the authors' spacetime circuit proof, detector treatment, test factors or observations, and are not security certifications for deployment.
