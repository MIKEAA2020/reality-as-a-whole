# Non-dual experience, neural timescales and the one-reality program

**Subsequent theoretical connection:** [Extending the balanced orientation and opening a report boundary](ZERO_ORIENTATION_EXTENSION_AND_DYNAMIC_REPORT_BOUNDARY.md) constructs a tunable, conserved report interface and distinguishes formal sign recoverability from subjective experience. It is a mathematical analogy, not an analysis of the paper's EEG or a validated empirical mapping.

## The paper and the question

Malipeddi Saketh and colleagues, [“Non-duality in brain and experience of advanced meditators—key role for intrinsic neural timescales,” *Communications Biology* 9, 1261 (2026)](https://www.nature.com/articles/s42003-026-10473-9), investigate whether reported weakening of the self–world boundary is associated with a measurable change in brain dynamics. The original article was published on 12 June 2026; the page lists a version of record dated 28 September 2026.

This is relevant to the framework's experiential side: if experience is intrinsic to the same reality that has physical appearances, a change in how experience is organized should be investigable alongside changes in physical organization. It is **not** a test of the whole-energy hypothesis, the necessity of plenitude, the finite quantum model or the metaphysical identity of experience and matter.

The [accompanying verifier](verification/nonduality_neural_timescale_identifiability_test.py) contains **synthetic mathematical controls only**. It does not use participants' EEG, reproduce the paper's analyses, or test whether any artificial process is conscious.

## 1. What was actually studied

The main analysis reuses data from 103 healthy adults in three naturally recruited groups: 42 advanced Isha Yoga meditators, 33 novices and 28 meditation-naïve controls. The meditation-depth questionnaire was available for 70; only **53** had both clean task EEG measurements and the questionnaire and entered the principal neural–report correlation. This was not a randomized trial assigning people to become advanced meditators.

Participants performed two different tasks:

- **Eyes-closed breath watching**, treated as internal attention. They completed a questionnaire afterward, including a six-item non-duality cluster about reported experience.
- **Eyes-open visual oddball**, a cognitively demanding task with audiovisual stimuli and performance feedback, treated as external attention.

The physiological measure was the frontal EEG **autocorrelation window**, ACW-50: the first time lag where the estimated autocorrelation falls to half its maximum. Roughly, it summarizes how long aspects of the measured signal remain correlated with their earlier values. It is not itself a measurement of subjective duration, an internal/external boundary, the persistence of an individual experience, or a physical quantity of experience. The paper's analysis used 128-channel EEG, preprocessing and selected frontal electrodes based on the reported condition-related topography.

## 2. What the paper found—and the scale of the evidence

The authors report:

1. Advanced meditators had higher questionnaire non-duality scores during breath watching than novices and controls.
2. The task-related ACW difference varied by group: the mixed ANOVA group-by-condition interaction was **F(2,70) = 3.76, p = 0.028**. In the advanced group the within-group task difference was not statistically significant, whereas it was significant for the other groups. The authors associate the smaller advanced-group contrast mainly with shorter breath-watching ACW, not a demonstrated global increase in integration.
3. Across the 53 complete cases, the internal–external ACW difference and reported non-duality had **Spearman ρ = −0.31**, 95% CI [−0.54, −0.04], p = 0.02. In the 19 advanced meditators with complete data, the corresponding reported ρ was −0.40, CI [−0.73, 0.08], p = 0.09. The separate simple regression using the difference explained approximately **8.2%** of score variance; another questionnaire cluster, concentration, had a similar reported association. The observation is interesting, but neither specificity to non-duality nor within-expert association is firmly established by those figures.
4. The authors also analyzed an independent dataset of 43 experienced Vipassana meditators and found no statistically significant ACW condition difference. That dataset had **no meditation-naïve controls and did not measure non-duality**. It is useful as an additional neural analysis, but it is not an independent replication of the group comparison or the neural–phenomenological correlation.

The paper's interpretation of comparable neural timescales as “neuro-temporal non-duality” is an operational proposal. A non-significant difference is **not proof of equality**; an equivalence test with a justified margin and sufficient precision is needed for that stronger claim. The main group interaction supplies evidence of a group-dependent contrast, but does not by itself establish equal task responses in experts.

## 3. Why the connection matters without making it do too much

The paper makes an experiential fact operationally researchable: people can report less rigid division between self and environment while their brains exhibit measurable, task-dependent temporal patterns. On the one-reality view, this is compatible with a **change in the differentiation of one physical–experiential reality**, rather than a literal movement out of the world or proof that neural activity creates experience from something intrinsically non-experiential.

The constructive insight is **not** that a smaller number of milliseconds directly equals more consciousness. A more useful candidate is that the *relation* between ways the system handles bodily and environmental information changes with reported boundary character. This gives the subject-boundary program a concrete empirical target: model which dynamically available distinctions, integrations, and reports vary together in an individual, and which remain distinct.

However:

- An experience of unity is a real reported experience, not by itself evidence that the individual has become identical to every other subject or has direct access to a larger domain.
- A changed self–world boundary does not imply that sensory content, agency or all differentiation disappears. Nor does a report of unity settle whether there is a subject, how subjects are individuated, or whether two people share one incidence of experience.
- A correlation is compatible with an intrinsic/extrinsic identity hypothesis, but also with other mind–brain accounts. It does not choose an ontology or establish that ACW is the intrinsic nature of experience.
- Non-duality is not zero phenomenal valence. The paper does not measure a globally additive signed experience, show opposite experiences cancel, or imply that suffering is erased by a balancing positive value.

The paper suggests an empirical bridge worth testing; it does not by itself complete the bridge. This is consistent with taking the user's zero-whole and intrinsic-experience proposals seriously without presenting this result as a proof of them.

## 4. A precise identifiability check

The ACW-50 is a **single summary** of a time series, not its complete dynamics. Two distinct stationary Gaussian processes can have exactly the same half-decay lag while having different autocorrelation functions. For discrete lag \(k\), compare

\[
 C_1(k)=0.8^k,\qquad
 C_2(k)=0.7(0.9)^k+0.3(0.4)^k.
\]

Both first fall to or below one half at \(k=4\), yet

\[
 C_1(4)=0.4096,\qquad C_2(4)=0.46695.
\]

Both are valid autocorrelations: the second comes from a weighted sum of independent stationary autoregressive components. Equal ACW-50 is therefore not identity of even the full *single-signal* temporal structure.

A second synthetic example makes a different point. Let a stationary bivariate process have dynamics \(M=0.8I\) and covariance \(\Sigma=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}\), with innovation covariance \((1-0.8^2)\Sigma\). For \(\rho=0,0.8,-0.8\), each component has exactly the same entire marginal autocorrelation \(0.8^k\), while their cross-correlations are respectively \(0,0.8(0.8)^k,-0.8(0.8)^k\). Thus even matching *complete marginal* autocorrelations does not determine the relation between two processes. These simultaneous synthetic components are **not** the paper's two sequential experimental tasks; they illustrate a mathematical limitation, not a result about its participants.

The script also constructs artificial groups with zero within-group correlations but a strong pooled correlation. This does not establish that the real study's correlation is confounded in that way; it shows why the pooled association alone does not establish a within-person, within-group or causal relationship. All examples are synthetic and analytically specified.

In particular, a zero contrast \(\tau_{\rm breath}-\tau_{\rm task}=0\) is a comparison of two **positive** timescales. It is not a zero total energy, a signed experiential sum, or a physical realization of the finite model's orientation constraint. A formal zero can connect ideas, but its meaning has to be justified in each case.

## 5. A stronger test arising from the synthesis

A useful next empirical design would compare competing predictions, rather than fitting an unrestricted “unity” interpretation after the fact:

1. **Within-person state variation:** preregister repeated meditation and matched control sessions, recording phenomenology close to each period. Include suitable task-matched controls, counterbalanced order, eye-state controls and behavioral/arousal measures. Do not presume the same subjective state during the visual task, which the present questionnaire did not directly establish.
2. **Dynamical specificity:** preregister the ACW contrast and its uncertainty, then test whether fuller temporal, cross-channel and task-response measures predict boundary reports out of sample beyond the ACW alone. Cross-channel data must be analyzed within a common period; cross-condition comparisons require appropriate models, not literal simultaneous cross-correlations of different sessions.
3. **Group and state separation:** estimate both between-group and within-person effects, with explicit handling of missing observations, group differences and multiple comparisons. Use an independent region of interest or independently validate data-driven electrode selection. If equality is the claim, preregister a physically and clinically meaningful equivalence margin.
4. **Experiential discrimination:** independently measure boundary dissolution, attention, wakefulness, emotional valence and suffering. Test whether the proposed signatures distinguish these rather than treating them as synonyms. Include approaches and populations beyond one tradition and seek an independent sample that measures both EEG and experience.

A useful theory would make **risk-bearing predictions** about such data: for example, that a preregistered relational neural measure improves held-out prediction of reported boundary character over individual ACW and attention/arousal measures. Failure to improve prediction, or disappearance of the within-person association under appropriate controls, would count against that specific proposed bridge. It would not by itself refute the one-reality ontology or prove a competing metaphysics. Conversely, successful prediction would support the operational bridge without establishing intrinsic identity or signed-valence cancellation.

## Sources, limitations and reproduction

The article states that the raw human EEG is not public for ethical/privacy reasons; numerical data for figures are in its supplementary information. This note relies on the article's reported results and methods, not an independent examination of the raw data. The authors report spectral covariate analyses that retain the group-by-condition interaction, so eye-state or spectral differences should not be asserted as having been shown to explain the result; they remain important design considerations.

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps \
  python -m unittest verification.nonduality_neural_timescale_identifiability_test -v
```

The tests check only the synthetic identifiability examples and distinction between a zero difference and zero components. They do not validate, refute or reproduce the neuroscientific study.
