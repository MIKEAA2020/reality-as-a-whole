# From exact quantum agreement to finite evidence

## Decision

The [previous comparison](QUANTUM_AGREEMENT_PLURAL_PERSPECTIVES_AND_RECORDS.md) reconciled two quantum agreement results. This step asks what can be inferred from finite observations rather than exact idealized probabilities.

**Main result:** an arbitrarily small, explicitly specified noise perturbation can destroy the 2021 paper's *exact* common-certainty condition and its perfect-correlation premise, even though the two assigned probabilities remain almost maximally different. Therefore, “we saw no violations” cannot by itself establish exact common certainty. Conversely, under a specified noise model, ordinary Bell statistics can robustly distinguish a sufficiently postquantum example from the quantum set **without** establishing exact common certainty.

These statements are about a finite binary box model and a hypothetical experiment. No human or quantum experiment was performed here; the boxes and counts are **synthetic**. The underlying results—common-certainty recursions, Popescu–Rohrlich boxes, the [Tsirelson bound](https://ar5iv.labs.arxiv.org/html/1209.0448), and finite-sample [Hoeffding bounds](https://www.cs.mcgill.ca/~colt2009/papers/012.pdf)—are established work, not discoveries claimed here. The new application supplies an explicit noise/recursion calculation and a test gate for the framework.

## 1. What must be distinguished

[Contreras-Tejada et al. (2021)](https://doi.org/10.1038/s41467-021-27134-6) define the relevant estimates and common-certainty recursion for a shared no-signaling box. Their exact quantum exclusion applies when the **target events are perfectly correlated**, the stated common-certainty condition holds, and the distribution is quantum in their sense. Their paper already observes that experimental noise makes exact zeros small rather than zero, notes robustness of the quantum void around the relevant ideal boxes, and identifies approximate common certainty as a research direction. We are not claiming to have discovered that problem.

A later, distinct [finite-dimensional preprint](https://arxiv.org/html/2511.21258v3) treats Lüders updates for a joint property, proves a commuting-case result and analyzes approximate certainty in its own setting. Its common-certainty construction and bounds do not automatically apply to the different box recursion used below. See the [previous comparison](QUANTUM_AGREEMENT_PLURAL_PERSPECTIVES_AND_RECORDS.md) for the difference and the source-date caveat.

Exact common certainty is a property of a **specified model**; in a fixed finite model a recursion can stabilize after finitely many steps. It does not require real agents literally to transmit infinitely many messages. But data alone cannot generally establish all the exact zeros, the full model, its common prior, and the agents' actual information states. Model structure or independently justified physical constraints may establish some of these exactly; lack of finite empirical proof does not make the mathematical result useless. For background on common knowledge and common p-belief, see the [Stanford Encyclopedia discussion](https://plato.stanford.edu/entries/common-knowledge/).

## 2. A fixed noisy PR family

Let the inputs and outputs be bits `x,y,a,b`. Choose the PR-box relabeling

```text
P_PR(a,b|x,y) = 1/2  if a XOR b = xy XOR x;  otherwise 0.
P_δ = (1−δ) P_PR + δ/4,       0 ≤ δ ≤ 1.
```

All four outputs get the `δ/4` white-noise term. This family is normalized and no-signaling for every δ. It is only a formal comparison, not a claim that a PR box or its postquantum perturbation exists in nature. For `x=y=1`, the target outputs agree at `δ=0`, as required by the 2021 setup. At `x=y=0`, the event `a=b=0` has probability `1/2−δ/4`, hence is nonzero.

Adopt the paper's definitions at that event:

```text
q_A = P_δ(b=1 | a=0, x=0, y=1) = δ/2,
q_B = P_δ(a=1 | b=0, x=1, y=0) = 1−δ/2.
```

For `0≤δ<1`, the probability-assignment sets for those exact numerical values are `α₀={a=0}`, `β₀={b=0}`. At `x=y=0`, however,

```text
P_δ(b=0 | a=0) = P_δ(a=0 | b=0) = 1−δ/2.
```

Consequently:

- At `δ=0`, both probabilities are exactly 1 and the sets stabilize at `{0}`: common certainty of the unequal assignments holds, and the target events are perfectly correlated. This is the familiar ideal PR example, already recognized by the authors.
- At **any** `0<δ<1`, the paper's exact certainty recursion eliminates both sets at the next step. Exact common certainty fails. Moreover, the probability that the target outputs disagree at `x=y=1` is `δ/2`, so the theorem's perfect-target-correlation premise also fails. Nonetheless `q_B−q_A=1−δ`.

| Noise `δ` | `q_A` | `q_B` | Target mismatch at `11` | Cross-certainty failure at `00` | Exact common certainty |
|---:|---:|---:|---:|---:|---|
| 0 | 0 | 1 | 0 | 0 | Yes |
| 0.0001 | 0.00005 | 0.99995 | 0.00005 | 0.00005 | No |
| 0.2 | 0.1 | 0.9 | 0.1 | 0.1 | No |

These are probabilities conditional on declared box inputs and outputs, not direct measurements of people's beliefs. In particular, for nonzero δ the two target events are **not identical or perfectly correlated**. One cannot apply the exact theorem while silently treating them as the same event, or claim this family is a quantum counterexample.

### A specifically defined approximate recursion

As a **local convention for this example**, replace each “probability exactly 1” test in the original recursion by “probability at least `1−ε`,” retaining the exact sets of numerical assessments. Then for `ε=δ/2` and `0≤δ<1`, both `{0}` sets are fixed points of the resulting approximate recursion. This is an explicit useful approximation to the paper's recursion—not a claim to have solved the general problem of defining approximate common certainty, nor the same theorem as the separate Lüders-update paper. Approximate target correlation must also be recorded, here with error `δ/2`.

## 3. A robust, operational Bell boundary

For each input pair, define `e_xy` as the probability that the PR parity rule above **fails**. Put `E_xy = Σ_ab (−1)^(a+b) P(a,b|x,y)` and define the signed CHSH expression

```text
S = E_00 + E_01 − E_10 + E_11 = 4 − 2 Σ_xy e_xy.
```

The established quantum bound is `S≤2√2`, assuming the standard bipartite quantum measurement setting. Equivalently,

```text
Σ_xy e_xy ≥ 2−√2 ≈ 0.585786.                            (1)
```

For our isotropic family, each `e_xy=δ/2`, so `S=4(1−δ)`. If `δ<1−1/√2≈0.292893`, the box is provably postquantum by the standard bound. This is **not** a new Bell inequality; it is an explicitly oriented CHSH test for the same noisy family. It is also not a test of an individual person's beliefs or phenomenology.

Within this *particular* isotropic family the boundary is sharp: at visibility `v=1−δ≤1/√2`, take a suitable mixture of a Bell pair with white noise and fixed Pauli measurements. The resulting correlations have the same unbiased marginals and `E_xy=v(−1)^(xy XOR x)`. The [numerical checker](verification/finite_agreement_bell_gate.py) constructs the endpoint and two interior quantum states; the remaining interval follows from the stated mixture. Above the bound no quantum box in the standard setting can reproduce the whole table. This does **not** imply that every box outside our family is characterized by CHSH alone.

### A hypothetical fixed-sample decision

Before data collection, fix all four settings and the parity rule. Suppose there are `n=10,000` complete trials per setting, with independent identically distributed trials within each setting, and **1,000 observed parity failures in each setting**. These numbers are invented for illustration, not reported measurements.

For an overall one-sided error rate `α=0.05`, Hoeffding plus a union bound over the four fixed settings gives simultaneous upper limits

```text
 e_xy ≤ ê_xy + √[log(4/α)/(2n)] = 0.1+0.014802...
 Σ e_xy ≤ 0.45921...,     S ≥ 3.08158... > 2√2.
```

Under the sampling assumptions and the standard quantum-test model, this hypothetical dataset would reject that quantum bound at the stated familywise confidence level. It does **not** certify exact common certainty: all four empirical error rates are positive. It also does not establish that actual observations are postquantum; ordinary quantum experiments are expected to remain within the bound up to statistical fluctuations.

A real implementation needs a prespecified, defensible treatment of losses and no-clicks; event-ready selection must not depend on later settings in a way that biases the conditional sample. In a nonlocal experiment, control setting independence, timing, signaling and detection loopholes. The simple calculation assumes iid per setting, no optional stopping or post-hoc choice of sign/settings, and the specified event definitions. If there is drift or memory, use an appropriate validated sequential or martingale analysis, not this iid bound. An actual Bell test and its more careful treatment of locality, loss, settings and memory are discussed by [Shalm et al.](https://physics.aps.org/featured-article-pdf/10.1103/PhysRevLett.115.250401).

## 4. Why zero observed failures are not exact zeros

Suppose `δ=0.0001`. In each of settings `00` and `11` the failure probability is `0.00005`. Under independent trials, if we run 1,000 trials in each setting, the probability of seeing **no failure in either setting** is

```text
(1−0.00005)^2000 ≈ 0.904835.
```

This box has neither exact cross-certainty nor perfect target correlation, yet zero observed failures in those 2,000 trials are unsurprising. We have not used the other two settings here, so this is not a full box test.

For one preselected setting with `n=1000` iid trials and zero failures, the exact one-sided 95% binomial upper confidence limit is `1−0.05^(1/1000)≈0.002991`, not zero. This is a per-setting bound; simultaneous claims across settings need a multiplicity adjustment. Confidence coverage is a long-run property under the assumed sampling process, not a posterior probability that the fixed rate lies in the interval. The point is limited: finite observations do not **alone** prove a probability zero, although a separately established physical law or model may imply one.

## 5. Consequences for our framework

1. **Do not turn formal observers into subjects.** The models specify operational assignments and records, not an independent assay of conscious experience or a subject-constitution rule. Passing or failing a box test would not settle whether the whole is intrinsically experiential.
2. **Do not read agreement as identity.** Common records can constrain compatible claims while distinct experiential perspectives remain possible; neither agreement nor disagreement, by itself, proves a universal subject or rules out plural subjects.
3. **Keep all premises on the ledger.** A real proposal must identify the event on each side, prior, instruments, order, physical records, calibration, and errors. A small but nonzero mismatch in target events is not the exact same-event theorem. Distinguish zero counts from zero probabilities.
4. **Do not multiply explanatory machinery without payoff.** Inequality (1) recovers a familiar CHSH boundary and does not independently derive quantum physics from rational agreement. In this family, the empirical witness is just Bell data. A claim that the whole explains quantum weights needs additional non-circular premises and a distinct derivation or test; our subject-measure and experiential bridges remain open.
5. **Preserve the timeless scope.** Input labels and experimental order are local operational relations, not an external clock or a mechanism that brings possibilities into existence. No literal simulation or external creator is assumed.

## Reproduction

Install [`verification/requirements-framework-battery.txt`](verification/requirements-framework-battery.txt), then run `OPENBLAS_NUM_THREADS=1 python verification/finite_agreement_bell_gate.py`. The [receipt](verification/finite_agreement_bell_gate.json) records exact rational no-signaling, assessment and recursion checks at five noise levels; three explicit quantum controls; and the synthetic sampling calculations. These finite checks do not prove the cited general results or validate the assumptions in a real experiment.
