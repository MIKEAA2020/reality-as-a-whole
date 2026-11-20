# From Kent-like histories to observed quantum statistics

## 1. The outstanding problem

The proposed whole is timeless and self-sufficient, with experience accepted as a datum, genuinely plural subjects and the actuality of every genuinely possible local reality. Kent's [2015 construction](KENT_LORENTZIAN_QUANTUM_REALITY_FULL_PAPER_AUDIT.md), by contrast, specifies a Born-weighted distribution over final boundary conditions and takes one history to be actual. Could a different model include multiple Kent-like beable histories within the whole and recover a particular subject's observed quantum statistics?

**Present result:** even if a local quantum sector and its Born weights are granted, there are two additional, separable questions: (i) does the local beable actually contain a definite, recoverable record, and (ii) how are eligible subject-occurrences weighted across histories? Below is an exact compatibility criterion combining both. It is an application of elementary selection and error bounds to this interface—not a novel derivation of the Born rule, a demonstrated feature of Kent's physical theory, or an empirical test. The criterion makes a proposed account falsifiable *if* its subject weights and record-recovery error can be independently specified and calibrated. They currently cannot.

This extends the earlier [subject-measure gate](SUBJECT_MEASURE_AND_QUANTUM_OBSERVATION_GATE.md), which already gave the perfect-record selection formula and inverse bound. The additional step here is to separate record loss or wrong beables from unequal occurrence weighting and to track their combined effect under the **same** selected reference class. Both use recognized probability mathematics.

## 2. Prior work and source scope

- Kent's [*Lorentzian quantum reality: postulates and toy models*](https://doi.org/10.1098/rsta.2014.0241), the user-supplied nine-page article, was read in full in the [audit](KENT_LORENTZIAN_QUANTUM_REALITY_FULL_PAPER_AUDIT.md). This does not make a many-history adaptation his own view.
- Butterfield and Marsh, [*Non-locality and quasiclassical reality in Kent’s formulation of relativistic quantum theory*](https://arxiv.org/abs/1902.01294), were read as complete extracted HTML text and figure captions; the seven diagram images were not visually inspected. They identify possible record delay when photons re-scatter or are shielded, discuss the distinction between outcome and parameter independence, and outline a future-light-cone amendment whose spacetime-history probability measure they acknowledge remains to be defined. These are objections and proposed directions, not proofs that all real observations fail to have definite records. Their paper leaves Kent's parameter independence unresolved; a light-cone-shaped definition is not by itself a proof of Bell locality.
- Sebens and Carroll, [*Self-locating Uncertainty and the Origin of Probability in Everettian Quantum Mechanics*](https://doi.org/10.1093/bjps/axw004), were read here only in the abstract, introduction, selected sections on epistemic separability and mixed uncertainties; the full derivation, appendices and figures were not inspected. Their proposed epistemic separability principle and mixed-uncertainty treatment are relevant prior art; their stronger principle is a substantive, debated assumption, not established by our model. A finite observation-weighting distinction also appears in Page's [*Born's Rule Is Insufficient in a Large Universe*](https://arxiv.org/abs/1003.2419); only its abstract was revisited here, and the earlier project comparison records a generalized-measurement reply. Neither is a refutation of standard laboratory quantum mechanics.
- Kent's earlier [*A Solution to the Lorentzian Quantum Reality Problem*](https://doi.org/10.1103/PhysRevA.90.012107) was read here only in its abstract, introduction, and selected relativistic construction/discussion; not all sections, equations or proofs were inspected. The later [*Quantum Reality via Late Time Photodetection*](https://doi.org/10.1103/PhysRevA.96.062121) and Marsh's [*Depictions of Quantum Reality in Kent's Interpretation of Quantum Theory*](https://arxiv.org/abs/1811.08950) were accessed only at abstract level, not their methods, figures or calculations. Vilenkin's [*A quantum measure of the multiverse*](https://arxiv.org/abs/1312.0682) was read only through its abstract and introduction; its claimed conditional Born-rule result and detailed assumptions were not independently checked. Its mathematical watcher is not assumed to be a physical universal subject.

## 3. One fixed measurement, three different structures

Consider one specified preparation and measurement context, not all conceivable quantum experiments at once. Let `(Ω, μ)` be a **normalized physical reference distribution** over final boundary conditions or regulated histories; for a Kent-inspired adaptation its connection to the late Born distribution is assumed, not derived. A history `ω` is a mathematical label, not automatically a subject or a distinct universe. Different labels with the same underlying occurrence may require quotienting or mass-preserving pushforward.

Assume for this model that an independently specified physical target record `A(ω)∈{0,1}` exists and has `p = μ(A=1)`, with `0<p<1`. In realistic quantum histories this requires an actual, well-defined, mutually exclusive instrument or decoherent record event; it cannot be presumed for arbitrary incompatible observables. For now, `p` is the *given* Born target. Agreement of μ with the relevant Born probability is an assumption to be demonstrated by the candidate—not a consequence of taking all histories to be actual.

Let `F(ω)∈{0,1,⊥}` be a proposed local decoder of the beable record. `⊥` means no definite readable result. Its relation to `A` must be specified by actual physical variables or a calibrated model, not postulated simply because a final boundary has a Born weight. Define `E={F≠A}`; both wrong answers and `⊥` count as failures. Finally let `s(ω)≥0` be the *aggregate eligible occurrence weight* assigned to that history by a separately specified subject/reference-class rule. Assume `0<Z=∫s dμ<∞`. Then

```text
ν(dω) = s(ω) μ(dω) / Z,
Q₁ = ν(F=1),
ε = ν(F≠A).
```

`ν` is a proposed measure or self-location credence on an explicitly chosen class, not a physical lottery over which whole is created. Here `Q₁` includes all eligible occurrences in its denominator, including `⊥`. If an actual protocol keeps only definite outputs, condition on `F≠⊥` and redo the entire calculation with the correspondingly selected measure and its own error bound; one must not silently normalize away indeterminate records. An actual occurrence need not have positive ν-weight. `s` is neither a measured number of subjects nor necessarily an integer; it folds together subject eligibility, multiplicity, persistence/grain and reference-class weighting. A valid constitution and phenomenal bridge are not supplied by defining it.

Define `s_j = Eμ[s | A=j]`, assuming both are positive and finite. The target outcome weight *after* occurrence selection but *before* decoder errors is

```text
p_sel = ν(A=1) = p s₁ / [(1−p)s₀ + p s₁].                (1)
```

If `s₀=s₁`, then `p_sel=p`; if they differ, it generally does not. This is the earlier gate's result, applied to final-condition histories. Sector-normalized allocation among independently identified centers is another possible rule; it can preserve `p`, but is not forced by actuality or by this algebra.

## 4. Record recovery plus selection: a joint bound

The events `{F=1}` and `{A=1}` can disagree only on `E`. Hence, with the same ν in both terms,

```text
|Q₁ − p_sel| ≤ ε,                                         (2)
|Q₁ − p| ≤ ε + |p_sel − p|.                              (3)
```

The first is a standard coupling/indicator bound; it is sharp given only `p_sel` and an upper bound on ε: the allowable range for Q₁ is `[max(0,p_sel−ε), min(1,p_sel+ε)]`. This is an identification interval under minimal assumptions, not a proof that a particular physical decoder realizes every endpoint. Equation (3) isolates two reasons for failure: wrong/indefinite local records and an altered reference-class measure. Successful final-boundary weighting alone does not ensure either term is small.

**Calibration transport.** Suppose a proposed independent calibration establishes `μ(E)≤ε₀`. If, additionally, `s/Z≤κ` μ-almost everywhere for a finite known κ, then

```text
ε = ∫(s/Z) 1_E dμ ≤ min(1, κ ε₀).                        (4)
```

Without a justified bound on how selection concentrates on errors, a small error under μ can coexist with a large error under ν. The bound requires absolute continuity, finite normalization, and the same event, context and decoder under calibration and use. In particular, past operational detector reliability is not automatically an error estimate for a hypothetical final-boundary beable or for phenomenal experience.

If the physical target distribution itself differs from the Born target `p_B` by at most β in the same context, then replacing p in (3) gives the conservative bound

```text
|Q₁ − p_B| ≤ ε + |p_sel − p| + β.
```

Here β is a proved or independently calibrated physical record-recovery error, not an arbitrary rounding term. For a multi-outcome model, total-variation distance obeys the analogous triangle bound, with decoder disagreement bounding the distance between selected decoder and selected target distributions. No assumption that individually incompatible measurement outcomes all coexist is needed.

## 5. Numerical diagnostic, not an empirical finding

Take a hypothetical binary case with `p=1/4`, `s₀=1`, `s₁=3`. The physical target is still 1/4, while (1) gives `p_sel=1/2`; `Z=3/2` and `κ=2`. If the same model has `μ(E)≤0.01`, (4) gives `ε≤0.02`, so (2) places its selected decoder probability in `[0.48, 0.52]`. If an **independently measured and correctly matched reference class** instead yielded a valid interval `[0.22,0.28]`, this candidate would be incompatible with both stated bounds. All numbers are hypothetical; no real experimental or phenomenal calibration is claimed.

Conversely, given the same p, a selected outcome interval `Q₁∈[0.22,0.28]` and an independently justified `ε≤0.02` imply `p_sel∈[0.20,0.30]`. For `r=s₁/s₀`, solve (1):

```text
r = (1−p) p_sel / [p (1−p_sel)].
```

Thus `3/4 ≤ r ≤ 9/7`. This rules out r=3 **only for this reference class and these assumptions**. The bounds are for combined eligible weight; they cannot determine whether a discrepancy arises from the number of subjects, subject-duration conventions, actual selection, or other factors. Nor should the bound be imposed on a different question, such as an ordinary fixed observer in a single laboratory, when `[0.22,0.28]` describes some other sample.

## 6. Joint records and Bell consistency

Repeat the specification separately for each actual measurement context `(x,y)`. To recover a Bell experiment, the candidate needs one joint local-record distribution `Q(a,b|x,y)` for each chosen context, agreement with the quantum joint statistics at the declared tolerance, and appropriately normalized observable marginals. Definite values for all unperformed settings are not assumed.

Postselection can break operational no-signalling even when the underlying unselected data are no-signalling. For example, suppose an underlying local binary record has probability 1/2 at either remote setting `y=0,1`. Set eligible weights to `(s₀,s₁)=(1,1)` at `y=0` and `(1,3)` at `y=1`. The selected probability for local 1 is then 1/2 versus 3/4. This is a statistical example of context-dependent selection, not evidence for physical faster-than-light communication. To obtain controllable signalling one would additionally need the remote choice to affect a locally accessible selection/output mechanism; conditioning on inaccessible remote information or comparing data later does not show that. The model illustrates why the selected measure must be checked, not merely the underlying Born distribution.

Butterfield and Marsh distinguish dependence of a final-boundary variable on a setting it can record from illicit assumptions about an independent past hidden variable. One must state the causal/conditional model before applying a no-conspiracy or parameter-independence conclusion; neither covariance of the geometric construction nor failure of a Bell-local factorization alone answers every signalling question.

## 7. What would advance the battery?

For the *same* proposed physical and experiential sector:

1. Define the admissible history family and identify which distinctions are physical versus redundant descriptions; justify a normalized, regulator-stable base measure, not merely positive support.
2. Specify local record events and a beable decoder F with allowed `⊥`; show target-record recovery in models that include re-scattering, imperfect environments, and appropriate spacetime and field-theoretic limits.
3. Derive or defend an experiential subject-incidence rule and a local reference class, and determine whether the resulting effective `s₀,s₁` are equal for a fixed laboratory observer. Include memory, persistence, overlaps and non-reporting centers. Do not infer these weights just from neural or behavioral correlations.
4. Prove or independently calibrate the two errors on the *selected* class; test all joint measurement contexts and operational no-signalling. Any uncertainty in p, β, κ, or ε must be propagated jointly. Give a specific rival and a prospectively fixed, measurable contrast.
5. Explain why the selected structure has the phenomenal character it does. An empirically successful record decoder or normalized measure would not explain its intrinsic experience, much less establish **full structural and experiential intelligibility**.

This is a targeted constraint at the B4/B5/B6/B9/B10 interface. The conditional inequality is rigorous, but none of those substantive gates is passed: the required subject rule, experience bridge, physical record recovery and measure remain open. Strong actuality is not inferred from mathematical support or used to presume every consistent description is genuinely possible.
