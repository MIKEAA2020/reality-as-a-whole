# Transporting an experiential mismatch test between conditions

## Aim and result

The later [history-comparison assay gate](HISTORY_MISMATCH_FIRST_PERSON_ASSAY_ERROR_GATE.md) complements this source-to-target transport bound with sharp, within-target constraints for report error and physical-history misclassification. Neither gate provides an actual experiential calibration.

A serious test of the proposed connection between misalignment and discomfort must do more than find a physical quantity that predicts a report. It must say which **experienced contrast** is being tested, how it is anchored, and whether the anchor remains valid in the new condition. This gate addresses a specific step in that chain: how much a condition-specific calibration, if independently justified, can constrain errors in another condition.

The result is an **exact finite worst-case bound** under an explicitly stipulated stable experiential-contrast kernel. In a hypothetical example where the source calibration error is at most 5%, the sharp bound in a shifted target is 15%, not 5%. It can be attained even when the same conditional relation holds in both settings. A second example shows that equal physical mismatch distributions do not guarantee equal experiential error when relevant context is omitted.

This is a conditional application of established covariate-shift and Neyman–Pearson reasoning, **not a new statistical theorem or evidence that mismatch is discomfort**. It does not manufacture first-person data: experience is accepted as a valid datum. No real experiential calibration, subject boundary, target-population transport, or physical substrate independence is established here. There is no inference about experience in the Fischer quantum circuit.

## 1. Specify one anchored contrast

The [integrated candidate](INTEGRATED_EXPERIENTIAL_MISALIGNMENT_CANDIDATE.md) stipulates, for a selected local subject in a toy domain, that physical mismatch `q=1` corresponds to one designated unpleasant contrast and `q=0` to a designated neutral contrast. Its equilibrium isolated-pair mismatch occurs with probability `1/4`. Neither the subject nor this proposed identity is established by that spin model.

Fix in advance a single subject class, episode window, physical state representation `X`, and binary encoding `E` of a carefully specified *experienced* contrast. The binary encoding is an index of a contrast, **not the felt character itself**. Let `q(X)∈{0,1}` be the candidate physical prediction; its mismatch function, preferred reference, boundary and time window must be fixed independently of the outcome. Source and target describe local records or ensembles inside the whole, not global alternatives or actualization over external time.

Write `pS(x)` and `pT(x)` for source and target physical-state probabilities, and let

```text
fS(x) = P(E ≠ q(x) | X=x, source),
fT(x) = P(E ≠ q(x) | X=x, target).
```

If, and only if, a defensible condition-stability premise gives a common error function `f(x)` on the target-relevant state space, the source and target error rates are `eS=Σ pS(x) f(x)` and `eT=Σ pT(x) f(x)`. Stability of this one error function is enough for the calculation; the stronger usual covariate-shift premise is that the complete conditional distribution of E given X is invariant. With binary E and fixed q these amount to the same thing wherever the relevant conditional distributions are defined. Neither is established simply by measuring X or by assuming a fundamental experiential whole. A theory might predict a stable kernel, but its target-domain applicability must be defended or directly challenged.

### From a communicated anchor to a source error bound

If `Y` is a physical report or other nominated source anchor, `P(Y≠q)=r` alone is not `P(E≠q)`. However, if a separate, justified source-condition bound gives `P(Y≠E)≤η`, then pointwise disagreement implies

```text
eS ≤ min(1, r + η).
```

No independence is needed. This is useful only if the anchoring bound concerns the **actual target contrast** in the source population. It must not be inferred merely from agreement among proxies or from the same disputed mismatch rule. A person's own awareness is valid evidence; communication, memory, and external interpretation can add uncertainty without making that awareness illusory. In some designs direct within-subject comparison may supply stronger evidence than an external report, but its scope and transport still have to be specified.

## 2. Exact sharp target bound under stable conditional errors

Suppose finite source and target distributions are known and `eS≤ε`, for `0≤ε≤1`. The largest possible target error consistent with only these assumptions is

```text
B(ε) = max  Σ_x pT(x) f(x)
       s.t. 0 ≤ f(x) ≤ 1,  Σ_x pS(x) f(x) ≤ ε.

     = min_{λ≥0} [ λ ε + Σ_x max(0, pT(x) − λ pS(x)) ].     (1)
```

The maximum is attained: assign error first to states with largest `pT/pS`, allowing a fractional assignment at the budget boundary. A state with `pS=0<pT` can have error 1 without consuming any source budget. The identity in (1) is the finite randomized Neyman–Pearson/linear-program tradeoff, not an original discovery; its use here identifies the *particular* calibration burden on this project's experiential candidate. The ratio need not be computed when a source probability is zero: the corresponding term remains `pT` in the dual expression.

A simple but potentially loose corollary, when `pT(x)≤M pS(x)` everywhere, is `eT≤min(1,Mε)`. If the complete conditional error function is calibrated on source support and the target has no mass outside it, the exact identity `eT=Σ pS(x)[pT(x)/pS(x)]f(x)` applies. These are population statements, not finite-sample confidence intervals. If ε, the distributions or anchor reliability are estimated, simultaneous uncertainty, dependent observations, sampling, measurement and selection errors must be included; source samples with large weights can be especially unstable.

## 3. Concrete example: more mismatch in the target

Use the toy's source mismatch frequency `P_S(q=1)=1/4`, with `X=q` **for this illustration only**. Suppose a different target population or condition has `P_T(q=1)=3/4`; the integrated four-spin equilibrium family does **not** produce that change merely by varying its middle coupling. Imagine, without claiming real data, that an independently anchored procedure supplies `eS≤1/20`, and that `P(E|q)` is truly unchanged.

The worst case allocates all the source error to `q=1`: `f(0)=0`, `f(1)=1/5`. Thus

```text
source: (3/4)·0 + (1/4)·(1/5) = 1/20 = 5%,
target: (1/4)·0 + (3/4)·(1/5) = 3/20 = 15%.
```

Both distributions are normalized, both conditional errors lie in `[0,1]`, and the *same* conditional kernel produces both. The bound is attained, so one cannot infer a target error below 15% from these premises alone. For comparison, a perfect same-domain 5% bound would not automatically transport unchanged, even with stable conditional errors. The optimistic case `f(0)=f(1)=0` is also compatible with the upper bound: the calculation does not say actual target error is 15%.

A source bound might, for illustration, be obtained from `r=3%` and a separately valid `η=2%`; the numbers are invented. Calibration by a report is only as sound as the independently justified η and the interpretation of E. Neither that η nor an actual 5% source error has been established.

## 4. The same observed mismatch distribution can conceal failure

The integrated spin example already shows that the joint physical mismatch table for its two pairs stays fixed while middle coupling changes. That fact **does not itself imply** that experience or a valid assay changes. The following separate countermodel shows why equality of a coarse physical distribution cannot prove stability.

Let both settings have `q=0,1` with probability 1/2. Add a physical context bit `h` with `h=0` in the source and `h=1` in the target, and stipulate the single context-sensitive assignment

```text
E = q XOR h.
```

Then the mismatch q distribution is identical in both settings, but the candidate `E=q` has source error 0 and target error 1. The rule `E=q XOR h` is an illustrative rival, not a claim that a bit feels unpleasant or that the actual four-spin chain has this assignment. If X includes h, the source has no support on the target context, which equation (1) correctly flags. If X contains only q, the inferred conditional relation `P(E|q)` changes; **marginal equality of q does not establish its invariance**. A valid target experiential anchor would distinguish the two assignments, and other experimentally justified invariances may exclude the countermodel. Physical measures alone need not exclude it.

This same problem matters for substrate independence: identical coarse q statistics across two media are not enough to establish preserved phenomenology. A proposed equivalence must transport the relevant physical operations, contexts and subject boundaries, as well as a justified experiential relation. Conversely, a substrate change need not destroy experience; the point is that the mapping must be defended, not chosen by naming.

## 5. Allowing some condition drift

If a common extension `f(x)` satisfies the source constraint, but the target error function may differ and a **separately justified** target-weighted bound is available,

```text
Σ_x pT(x) |fT(x) − f(x)| ≤ κ,
```

then `eT≤min(1,B(ε)+κ)`. This is a conservative triangle-inequality bound, not claimed sharp for every set of distributions. Where the source has zero mass, the extension is unobserved and must be included in the worst-case optimization; it cannot be estimated from source labels alone. A numerical κ is not supplied here. With no stability or nontrivial drift bound, the target error can be 1 even with zero source error and identical X distributions, by changing the conditional relation.

For a genuine experiment, subject inclusion, q construction, E contrast, causal intervention and report channel must be specified in both settings. Evidence of physical overlap does not by itself calibrate the phenomenal target. A target anchor, experimentally supported transport assumption, or bounded drift could strengthen the inference; adding more unanchored source samples cannot by itself resolve target-only states or unrestricted drift. Failure to establish transport is an **inconclusive test**, not evidence against the reality of experience.

## 6. What this does and does not advance

This gives the local misalignment candidate a concrete requirement for advancing from a positive source-domain fit to an independently constrained target prediction: a defended anchor, explicit overlap, and a stable or bounded-drift experiential contrast. A valid failure of the specified q prediction in a correctly anchored target would challenge that **specific** bridge; the proposal might still be revised with a predeclared, independently warranted context or a different physical mismatch. Passing a binary contrast would not explain why the contrast feels as it does, supply all qualitative contents, establish plural subjects or persistence, reconstruct physics, or prove a self-sufficient experiential ground. **Full structural and experiential intelligibility** and all seven criteria remain jointly unmet.

The [bounded verifier](verification/experiential_mismatch_transport_gate.py) enumerates finite rational distributions, comparing the allocation rule to the dual and independent polytope-vertex enumeration; see the [receipt](verification/experiential_mismatch_transport_gate.json). Run `python verification/experiential_mismatch_transport_gate.py`. This checks the formulas in finite cases, not the empirical premises or broad philosophical claims.

### Source scope

- Standard covariate-shift background: Zhang, Xie and Zhang, [Handling covariate shift by model averaging](https://arxiv.org/html/2608.14025v1), abstract and introduction, chunk 0 of 29 read; full article, technical proofs and figures **not read**. Their estimator is not implemented here.
- Neyman–Pearson background: [Lecture 10: Neyman–Pearson lemma and asymptotic testing](https://courses.cit.cornell.edu/econ620/lect10.pdf), first chunk of two read, including the lemma; remaining material and figures **not inspected**. The formula above is used as a finite application of the established lemma and linear optimization.
- Park et al., [Calibrated Prediction with Covariate Shift via Unsupervised Domain Adaptation](https://proceedings.mlr.press/v108/park20b.html): abstract/landing page read; full paper and supplementary PDF **not read**. Cited only as related prior work, not as evidence for the present experiential assumptions.
