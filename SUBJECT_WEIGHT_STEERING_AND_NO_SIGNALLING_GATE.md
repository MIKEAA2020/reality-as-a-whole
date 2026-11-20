# Subject weights, steering and no-signalling

## Result

A proposed measure over plural experiences must be compatible not only with ordinary local quantum probabilities but also with **no-signalling between separated laboratories** if it is claimed to predict their unconditionally observed records.

For a specific entangled two-qubit model, giving occurrences associated with one remote outcome three times the weight of occurrences associated with the other would give the local observer a `3/4` versus `1/2` outcome probability depending on the distant measurement setting. **If** those numbers were also the frequencies in an unconditional, locally observable communication protocol, the proposal would permit signalling. Under that explicit operational premise, no-signalling forces the two weights to be equal for this model and comparison.

There is an important alternative: the same arithmetic is ordinary **postselection** in standard quantum mechanics. In that case the local observer cannot know which trials were selected without receiving the remote success record, and their unconditional marginal remains `1/2`. A self-locating credence or a distribution on selected occurrences is not automatically an experimentally available signalling channel. This distinction is the point of the gate.

This is a conditional calculation applying established quantum steering, no-signalling and selection ideas to our proposed subject-measure interface. It is not a new derivation of the Born rule or a universal constraint on every theory of experience.

## 1. Literature and reading scope

- Carroll and Sebens, [*Many Worlds, the Born Rule, and Self-Locating Uncertainty*](https://arxiv.org/html/1405.7907v3): all seven HTML chunks, including the section on mixed quantum/classical self-location, were read. The figures and the authors' longer companion paper were not audited. Their epistemic separability principle is a substantive assumption about a specified observer/system; it is not established merely by this model. Their section on multiple observers does allow occurrence weighting, so the present argument should **not** be read as refuting their account.
- Page, [*Born's Rule Is Insufficient in a Large Universe*](https://arxiv.org/html/1003.2419v1): both HTML chunks were read, including the distinction between volume weighting and observational averaging; this was not an independent proof or publication-version audit. Page's restricted projection-operator claim is not a general empirical refutation of the quantum formalism; compare [Cooperman's generalized-measurement discussion](https://doi.org/10.1088/1475-7516/2011/02/014), not reread in full for this gate.
- Brunner et al., [*Bell nonlocality*](https://arxiv.org/html/1303.2849v3): abstract, introduction and selected passages read, not its full 60 chunks or proofs. Standard no-signalling and local-factorization background is established literature.
- [*Quantum probability assignment limited by relativistic causality*](https://www.nature.com/articles/srep22986): abstract and introductory/search excerpts inspected; its full ten chunks and equation images were not audited. In particular, it distinguishes no-signalling from stronger causal assumptions. We do not use its broader claimed Born-rule derivation as a result of this gate.

Related earlier project analyses are [the subject-measure interface](SUBJECT_MEASURE_AND_QUANTUM_OBSERVATION_GATE.md), [effect-algebra probability reconstruction](OPERATIONAL_PROBABILITY_RECONSTRUCTION.md), and [the eraser/Bell/selection gate](QUANTUM_ERASER_BELL_AND_SELECTION_MEASURE_GATE.md). Here we combine **remote measurement choice** with the specific occurrence-weighting rule and explicitly separate its two interpretations.

## 2. A familiar physical setup

Let Alice `A` and Bob `B` share a Bell state

```text
|Φ⁺> = (|00>+|11>)/√2.
```

Bob measures `Z`, obtaining `b=±1`. Alice chooses either `Z` or `X` and obtains `a=±1`; write `x=Z,X` for her chosen setting. Assume the standard local quantum measurement law for this **effective two-qubit comparison**. Then

```text
P(a,b | Z) = (1+ab)/4,
P(a,b | X) = 1/4.
```

In each case Bob's unconditioned distribution is `P(b=+1|x)=1/2`. Alice's `Z` result is perfectly correlated with Bob's `Z` result, while her `X` result is independent of it. This is standard quantum theory, not evidence for any specific interpretation, phenomenal subject or fundamental spacetime.

## 3. The particular occurrence-weight candidate

Now **separately stipulate** that, in the relevant reference class, the eligible Bob-located occurrences associated with Alice's result `a=+1` receive total weight `s₊>0` per unit joint physical weight, and those associated with `a=−1` receive `s₋>0`. Assume the same weights for Alice's two choices, with all eligibility, observation, and reference-class conventions otherwise held fixed. These may represent combined occurrence, duration or inclusion weights; they are **not** measured counts of real conscious observers.

Define the weighted joint distribution

```text
Q(a,b | x) = P(a,b | x) s_a / [∑_(a',b') P(a',b' | x) s_a'].
```

Each denominator is positive; Alice's marginal is balanced for both choices. The induced Bob marginals are

```text
Q(b=+1 | x=Z) = s₊/(s₊+s₋),
Q(b=+1 | x=X) = 1/2.
```

For `s₊=3` and `s₋=1`, these are `3/4` and `1/2`. More generally their absolute difference is

```text
Δ = |s₊−s₋| / [2(s₊+s₋)].
```

If a theory additionally asserts that these `Q` values describe the distribution of Bob's **unconditionally available physical records in the same communication protocol**, changing Alice's spacelike setting changes Bob's observed distribution. With an established spacelike arrangement and reliable independent repetitions, the two settings could then be statistically distinguished without a classical message from Alice. Such a claim is incompatible with operational no-signalling in this setup unless `s₊=s₋`.

The inference explicitly assumes a local physical outcome at Bob, the same reference class in both settings, Alice's settings controllable independently of the source and the ordinary assumptions needed to interpret the claimed `Q` as observed frequencies. No unrestricted claim about quantum gravity or actual superluminal technology is made. A raw measure over all experiences does **not** automatically supply that operational-frequency bridge.

Nor does this argument require every observation-weighting proposal to have this form. The weights can depend on the full condition, the reference class may be different, a theory may use sector-normalization rather than occurrence-counting, and some global selections are intentionally conditional. Such proposals have their own consistency obligations; the equality condition is not a theorem for all possible subject measures.

## 4. The ordinary postselection control

The same `3:1` weighted table arises in entirely standard, no-signalling quantum mechanics. After Alice's measurement, let a local filter keep a `+` result with probability `1` and a `−` result with probability `1/3`. The success probability is `2/3` for both `Z` and `X`. Standard joint probabilities conditioned on **Alice's success** exactly equal the `Q` table above:

```text
P(B=+ | success, Z) = 3/4,
P(B=+ | success, X) = 1/2.
```

Yet before Bob learns which runs Alice kept,

```text
P(B=+ | Z) = P(B=+ | X) = 1/2.
```

The kept subset is determined using Alice's local result, not by an accessible selection flag at Bob. Bob cannot assemble that subset from his own local outcomes alone. Communicating the success labels requires a causal channel; conditioning does not create an unconditioned signal. Equal success rates at the two settings also do not make the conditioned Bob distributions identical.

Thus an empirical claim of superluminal signalling cannot be established from the **conditioned** difference. Conversely, if a proposed experiential measure assigns the weighted law to Bob's locally available, unconditioned observations, treating it merely as this standard filter fails to explain how Bob obtains the selection without the remote record. Those are different hypotheses with different observable content.

## 5. A quantitative audit contract

Write `r=s₋/s₊`. If an independently justified operational bound states that, for this exact protocol and same unconditionally sampled Bob reference class,

```text
|Q(B=+|Z) − Q(B=+|X)| ≤ ε,    0≤ε<1/2,
```

then this model requires

```text
(1−2ε)/(1+2ε) ≤ r ≤ (1+2ε)/(1−2ε).
```

For an **illustrative, not measured** `ε=1/100`, this interval is `[49/51,51/49] ≈ [0.9608,1.0408]`. It constrains only the model's **combined relative weight**. It does not count subjects or separate occurrence multiplicity from duration, experience, selection and report factors. An experimental confidence interval would need to cover all relevant settings jointly, handle setting randomness, missing trials, drift, clustering, spacelike separation and finite-sample statistics, and demonstrate that the sampled Bob population is the one to which the model applies.

If `Q=3/4` versus `1/2` really were unconditionally observable and each trial independent, a midpoint threshold at `5/8` would need only `119` trials for each one-sided Hoeffding error bound to be below `0.025`. This is a hypothetical power illustration **conditional on the signalling model**, not a proposal or a result from a real experiment. It is irrelevant to the postselected standard-quantum control unless the remote success flags are available.

## 6. What this contributes to the whole-account

The positive design requirement is a **local-observation interface**: for a given subject, evidence and laboratory record, specify which physical effects and weighting law enter its credence; distinguish any conditioning on remote facts from an unconditioned local prediction. If a candidate makes such weighting operationally testable, it must recover no-signalling within the applicable relativistic domain. This is a useful filter on proposed measures, not a derivation that there is a unique correct measure.

The framework still lacks a justified subject constitution, a general reference class and an independent account of which experiences exist and how they are weighted. Equal `s` in this toy says nothing about whether there is one subject or many, and neither Born statistics nor no-signalling proves the intrinsically experiential nature or necessity of the whole. The example uses local experimental records and effective spacetime relations, not an external master clock or a temporal mechanism creating possibilities.

## Reproduction

Run `python verification/no_signalling_subject_measure_gate.py`. The [exact rational verifier](verification/no_signalling_subject_measure_gate.py) calculates two-qubit joint probabilities for `Z`, `X` and an intermediate axis, checks the weighted distribution and the standard success/failure control, tests 147 rational weighting/setting cases, verifies the illustrative ratio interval on a finite grid, and computes the conditional IID bound. The [receipt](verification/no_signalling_subject_measure_gate.json) records the results. The general formula is algebraic within the stated model; this is not a data reanalysis or an experiment.
