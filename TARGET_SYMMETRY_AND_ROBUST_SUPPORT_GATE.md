# Target-sensitive support: symmetry, ties and finite uncertainty

## Result

The [previous interface](EXPERIENTIAL_SUPPORT_FACTORIZATION_BRIDGE.md) left a specific question: can knowing the target truth remove the factorization ambiguity? In the same four-state example, the answer is **partly**:

1. If we require the target event to be a factor block, two candidate factorizations remain. They agree on the target's **formal minimal support**, even though no deterministic symmetry-respecting rule can choose one of those two factorizations from the stipulated symmetric input.
2. That shared support is the target event itself. It is therefore not yet an independent explanation of why the target is true, or an experiential ground.
3. Near the symmetric case, distinct exact-factorization answers can arise from arbitrarily close input kernels. A declared uncertainty budget can retain all compatible candidates instead of manufacturing a precise answer; a finite-sample lower bound makes that risk explicit for this toy.

This is a mathematical test of a particular candidate interface, **not** evidence that minds have these factors or that two actual subjects exist. The generic stabilizer obstruction is a known consequence of equivariance, not a new general theorem; see [1](https://arxiv.org/pdf/2312.09016). The sampling calculation uses standard testing and information inequalities [2](https://theinformaticists.wordpress.com/2019/08/03/3603/).

## 1. Can the target break the tie?

Use the earlier state space `Ω={00,01,10,11}`, uniform transition kernel `U(s,t)=1/4`, actual state `s=11`, and target event `P={10,11}`, the claim `x=1`. The eligible balanced partitions are `X`, `Y` and `Z`, represented by the Boolean observables `x`, `y`, and `x XOR y`. The existing factorization gate G accepts all three complete pairs `XY`, `XZ`, `YZ`.

Consider a **target-alignment proposal**: require that the selected pair contain the partition whose block is P. It leaves `XY` and `XZ`. They both give the same support family, `{{P}}`, under the [earlier support rule](EXPERIENTIAL_SUPPORT_FACTORIZATION_BRIDGE.md). Thus **uniquely identifying a full factorization is not always necessary to identify this target's formal support**. This corrects any suggestion that the previous factorization tie necessarily made every target-support answer ambiguous.

But this particular consensus is weak: `P` is the event whose truth we set out to explain. The conclusion that `P` supports `P` is true at the logical level but does not identify an independently described ground, produce experience or explain why P occurs. Target alignment is a proposed additional criterion, not a known law of nature. There may be grounds whose observables do not themselves equal P.

### The residual symmetry

Let `h` interchange `00` and `01`, leaving `10` and `11` fixed. It preserves `U`, P and the actual state, fixes partition X and exchanges Y with Z. Hence it exchanges the two target-aligned factorizations:

```text
h(XY)=XZ,    h(XZ)=XY.
```

If a deterministic selector is required to be equivariant under this admitted redescription, its unique output at an input fixed by h must itself be fixed by h. Neither aligned pair is fixed. Therefore **no such selector can uniquely choose one of those two aligned pairs from this input alone**. Returning both is equivariant; choosing either by its written name is not. The third pair `YZ` *is* fixed by h, but fails the target-alignment requirement. If h is not an admissible physical redescription, or if extra independently justified structure distinguishes Y from Z, this no-go does not apply. Conversely, this target-dependent symmetry argument is stronger than simply invoking the full symmetry of the kernel alone.

All of the input distinctions here are formal: the target can distinguish X, but cannot distinguish its two partners. There is no claim that factoring a system constitutes a subject, or that the two candidate descriptions are two actual people.

## 2. A near-symmetry robustness test

Let `0 < δ ≤ 1/8`, and define the independent-flip kernel

```text
Kδ = kernel(flip-x = 1/2 − δ, flip-y = 1/2 − 2δ),
Lδ = h Kδ h⁻¹.
```

The equality is conjugation of the complete transition kernel. In the fixed labeled candidate space, the exact factor gate selects `XY` for `Kδ` and its h-image `XZ` for `Lδ`. To see uniqueness throughout the stated interval, write `p=1/2−δ`, `q=1/2−2δ` for the independent flip bits `Eₓ,Eᵧ`. The competing factors have flip indicators `(Eₓ, Eₓ XOR Eᵧ)` or `(Eᵧ, Eₓ XOR Eᵧ)`, with respective covariances `p(1−p)(1−2q)` and `q(1−q)(1−2p)`. Both are strictly positive for `δ>0`, so the competing pairs fail the gate's conditional-independence requirement; `XY` passes. Both kernels agree with the target and state under h. Define row distance as the maximum total-variation distance across the four rows. Direct expansion gives

```text
d(Kδ,U) = d(Lδ,U) = 2δ,
d(Kδ,Lδ) = 2δ − 4δ².
```

Both inputs approach U as δ tends to zero, while their selected labeled factorizations stay different. The two kernels are conjugate: if h is a change of presentation of all physical structure, they describe the **same structure in different coordinates**, and equivariance correctly transports the answer. If instead the original labels and candidate operations are held fixed as physically interpreted observables, they are distinct candidate inputs to an inference problem. The toy does not establish that either interpretation, or either intervention, applies in a real system.

## 3. A conservative set-valued decision

Reuse the earlier defect `D_K(F)`, zero exactly when factorization F passes G. The [factorization audit](SUBJECT_CONSTITUTION_FACTORIZATION_GATE.md) proves that, for row-TV error at most `ε`, the defect of a fixed factorization changes by at most `3ε`.

Given an estimated kernel `K̂` and independently warranted bound `d(K̂,Ktrue)≤ε`, define

```text
C(K̂,ε) = {eligible F : D_K̂(F) ≤ 3ε}.
```

If the true kernel has an exact G-factorization among the declared candidates, it **must** lie in C. Thus:

- one surviving candidate gives a **conditional certificate** within the stated model and error bound;
- multiple survivors give a set of compatible candidates, not multiple verified subjects;
- no survivors means the error bound, the candidate domain, or the exact-G assumption cannot all be right.

Passing the inequality is **necessary, not sufficient**, for a candidate to be realizable within the error ball. C may therefore be conservative. At `K̂=U` it retains all three factors, including both target-aligned pairs. With the earlier asymmetric benchmark `(1/4,1/3)` and `ε=1/96`, C has one member. The algorithm does not infer that either the claimed ε or the stipulated candidates hold for a brain.

## 4. An idealized finite-sample limit

Suppose an investigator can independently prepare each of the four states exactly and observe `n` independent next-state draws per row, and the two only hypotheses are the labeled `Kδ` and `Lδ`. This is an ideal **toy experiment**, not an experiment on human subjects.

For `δ≤1/8`, every probability under `Lδ` is at least `1/16`; each row differs in two entries by `±a`, with `a=2δ−4δ²≤2δ`. Using `KL(P‖Q)≤χ²(P‖Q)`, per row

```text
KL(Kδ(row) ‖ Lδ(row)) ≤ 2a²/(1/16) ≤ 128δ².
```

Four rows with n independent observations each have joint `KL≤512nδ²`. Pinsker's inequality and the standard two-hypothesis testing bound give, for **any** test with equal prior weights,

```text
average error ≥ max(0, [1 − 16√n δ]/2).
```

For illustration, `δ=1/1000` and `n=100` per row imply **average error at least 42%** under these assumptions; hence at least one of the two hypothesis-specific error probabilities is at least 42%. This lower bound is conservative, not the measured accuracy of any algorithm or a recommended sample size. Exact preparation, independence, true hypothesis set, fixed δ and interpretability of the factor labels are strong assumptions. More observations or additional independently grounded physical information can help; the result does not declare factorization unknowable.

The [verifier](verification/target_symmetric_support_robustness.py) checks the stabilizer and ties, six exact rational δ cases, the candidate-set controls, the defect bound on selected pairs, and the illustrative KL inequality. The general symmetry and information bounds are mathematical arguments, not the outcome of those finite tests.

## 5. Framework consequences and next obligation

This advances the **quality of the gate**, not the completion of B1–B12. It distinguishes (i) uniquely determined formal support for one target, (ii) a non-identifiable completion of a factorization, and (iii) an unresolved ontological/experiential ground. A report such as “one invariant support was found” must not be translated into “one genuine subject was found.” Nor does a split factorization prove two experiential subjects.

For a substantive next test, we need a physically motivated shared process with independently specified observables, admissible transformations and operations, plus two **genuine rival incidence or quality hypotheses** that make separately anchored predictions. If those rivals agree on all accessible observations, the result is underdetermination, not a passed phenomenal gate. Establishing the necessary actuality of the whole, subjective quality, the physical theory and a measure are still separate open obligations. No inference here assumes an external clock or a temporal conversion of possibilities into actuality.
