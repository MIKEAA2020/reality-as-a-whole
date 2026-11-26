# Can the echo's physical report diagnose subject persistence?

## The concrete problem

The existing [ownership-report construction](ZERO_OWNERSHIP_REPORT_SYMMETRY_AND_INCIDENCE.md) can reversibly write a physical comparison bit `H=zj=B=R` on the supported echo. Two proposed subject-ownership rules give **opposite** answers to “are the tick-7 and tick-10 occurrences owned by the same subject?” while leaving that physical report unchanged. The preceding [local-access analysis](ZERO_ECHO_ACCESSIBLE_MARGINAL_INCIDENCE_ROOT_CAUSE.md) also showed why a type-sensitive report cannot simply be assumed.

The root issue is not that reports are worthless or that first-person knowledge is unavailable. It is that *physical accuracy relative to B* and *accuracy about subject identity* are different claims. An independently warranted identity witness or report calibration can discriminate the two candidates; the B correlation alone cannot supply that calibration.

The analysis below gives a precise error threshold, a witness comparison that tolerates correlated errors within each trial, and a repeated-error control. The numerical witnesses are hypothetical. The original coherent physical report and both candidate ownership maps are verified on the existing carrier; no actual identity witness is produced by the finite model.

## 1. Same physical echo, opposite proposed ownership

The reduced clock ledger transports the same physical seed from tick 7 to tick 10. At the anchor, the separately added saved-J memory and ready report bit implement

```text
H = z j = B = R.
```

The [new tests](verification/zero_echo_ownership_witness_diagnostic_test.py) check the original complex recorded quantum branches for source labels 0, 7 and 15, both pointer signs: B has physical weights 1/2 and 1/2, and H agrees with B on the supported branches. These are selected checks on the previously constructed report circuit; L and H are extra resources and no actual experience is inferred.

The existing opposite ownership hypotheses state, for the two clock slots on one transported seed,

```text
bridge A: same owner exactly when B=+,
bridge B: same owner exactly when B=−.
```

The verifier checks that they disagree on every seed of the specified reduced clock ledger, for both candidate pair-factor labels. Both are stipulated ownership rules, not established subjects, exhaustive options, or two independently realized worlds. The underlying physical echo and H circuit contain neither rule as a causal input. Thus, holding the physical state, gates, and permitted physical effects fixed, `(B,H)` statistics agree under both hypotheses. Saying “H is a physical B report” does not decide what an identity answer should be.

## 2. An identity-calibration threshold, not an assumption of infallibility

Suppose there is an additional or independently interpreted binary identity answer Y, with `Y=+` meaning “same owner,” and let O be the actual answer to that specified ownership question. A report may be physical, first-person, or a combination; its connection to O must be justified for the target reporter and time window, not merely equated to B. Let independently supported error bounds be

```text
P(Y=+ | O=−) ≤ f,        P(Y=− | O=+) ≤ g.
```

Let `q₊=P(Y=+|B=+)` and `q₋=P(Y=+|B=−)`, in a population or intervention regime where both B sectors are available and these bounds apply. Under the two stated ownership bridges, the exact compatibility conditions are

```text
A:  q₊ ≥ 1−g  and  q₋ ≤ f,
B:  q₋ ≥ 1−g  and  q₊ ≤ f.
```

If `f+g<1`, these rectangles are disjoint: the two bridges cannot both satisfy the calibration for the same observed conditional report law. In particular, bridge A requires `q₊−q₋ ≥ 1−f−g`, and bridge B requires the opposite inequality. An observed law can instead be incompatible with **both**: the two bridges are not exhaustive.

The threshold is sharp for this two-candidate test. When `f+g≥1`, choose any `q∈[1−g,f]` and set `q₊=q₋=q`: the same conditional report law is compatible with both bridges and both stated bounds. This does not prove that every possible experiment is uninformative; it identifies when these two error bounds alone cannot guarantee separation.

### The physical comparison bit as a hypothetical identity answer

On the ideal supported echo, reading H with `+` interpreted as “same” gives `(q₊,q₋)=(1,0)`. If an independent calibration established `f+g<1` for H **as an identity answer**, it would exclude bridge B under the stated target, support and scope. Merely demonstrating H=B does not establish that calibration: under bridge A the ideal H has zero identity error, while under bridge B it is wrong on every supported sector. The identical physical record is consistent with either assignment until some further fact about O and reporting is warranted.

With a stipulated physical bit-flip channel of accuracy 9/10, the same physical conditional law is `(q₊,q₋)=(9/10,1/10)`. With independently justified identity bounds `f=g=1/10`, it is compatible with A and incompatible with B. This is a conditional illustration, **not** an observed identity report or a proof that physical bit-flip accuracy equals experiential accuracy. One must not calibrate identity by presupposing the B-dependent rule one is trying to test.

## 3. Compare an independently supported witness without assuming independent errors

A constructive alternative is to seek a separate witness W of O, retaining the physical B-report H. W might include a genuine first-person observation and a reporting channel, but it must refer to the same subject, target interval and question; this finite echo has not supplied one. Suppose in a common population

```text
P(H≠B) ≤ e,          P(W≠O) ≤ d.
```

Under bridge A, `O=B`, so disagreement between H and W can only occur when at least one of those two errors occurs. Under bridge B, `O=−B`, so agreement can only occur when at least one occurs. The union bound therefore gives

```text
A: P(H=W) ≥ 1−e−d,
B: P(H=W) ≤ e+d.
```

Clamp the lower bound at 0 and the upper bound at 1. These bounds make **no independence assumption between the two errors within a trial**. If `e+d<1/2`, their agreement ranges are disjoint; an observed joint agreement rate, with appropriate uncertainty, can distinguish the two hypotheses under the stated premises. If the ranges overlap, agreement alone is not guaranteed to discriminate; additional observables or stronger constraints may still help.

For `e=d=1/10`, bridge A requires agreement at least 4/5, while bridge B permits at most 1/5. These are sharp: correlated error events can attain the endpoints. The verifier constructs exact rational joint distributions with the same physical `(B,H)` law for both bridges and arbitrary allowed overlap between the two error events. The proposed W channel differs according to the assumed identity truth, so it is an **additional truth-sensitive interface**, not a report already present in the unchanged physical circuit. If W is physically recorded, its construction and any disturbance must be included in the physical model.

The guarantee is conditional on the target, population, calibration and bridge hypotheses. A truthful direct first-person observation can be strong evidence for its own occurrence without first being reduced to a physical bit; translating it into W, estimating d, associating it with the proposed model signs, and generalizing across occurrences are further tasks. Conversely, a simulated numerical report is not a first-person witness.

## 4. Repetition does not automatically fix calibration

Suppose each identity-witness report has error probability 1/10, but all repetitions in a run share one latent error: with probability 1/10 they are **all** wrong, and otherwise all correct. Every individual error rate is still 1/10, yet the majority of 3, 9, or 99 reports is wrong with probability 1/10. The test constructs this exact joint distribution.

This does not invalidate a genuinely independent-trial analysis. It shows why per-report accuracy alone cannot be exponentiated into an arbitrarily small error: independence or another defensible dependence model must be established. An internal clock or repeated record is not, by itself, such an independence proof. Statistical sampling uncertainty and selection of comparable reporters also remain separate from the structural identities above.

## 5. Root cause and the next question

1. **Why does the original comparison fail as an ownership diagnostic?** Its two control gates determine `zj`, a physical parity already equal to B and R on the prepared support. The competing ownership maps are not inputs to that circuit.
2. **Why doesn't improving physical B accuracy fix it?** Perfect measurement of B cannot decide whether “same owner” means B=+ or B=−. The missing link is target-specific identity calibration, not additional precision about the wrong target.
3. **What would make a report discriminating?** A well-defined occurrence and reporter, a justified relation between their identity truth and the report, error bounds valid in the tested conditions, and an accessible record or direct witness. The threshold above tells us exactly what those premises would buy; it does not manufacture them.
4. **Why isn't a formal subject label enough?** A label added to the model neither gives a physical channel nor establishes an experienced identity. Conversely, a real subject's direct acquaintance should not be dismissed merely because a third-person circuit alone is ambiguous.
5. **Meta-level target:** derive or independently ground, within one physical–experiential constitution, the actual subject/occurrence relation, its persistence and plurality, and the admissible interventions and incidence measure. A positive witness for one subject does not exclude additional subjects. No choice of formal calibration constant derives that constitution or establishes the whole's objective zero.

The useful next step is to identify a *real or rigorously specified* identity witness and its available physical/first-person interface, rather than continue treating the existing B report as if it already read ownership. Preserve the possibility of genuine plural subjects and of real negative experience; a balanced model does not erase suffering.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_echo_ownership_witness_diagnostic_test \
  verification.zero_ownership_report_bridge_test \
  verification.zero_echo_accessible_marginal_root_test -v
```

These tests establish the stated finite-circuit and conditional-probability results, not the existence or reliability of an actual identity report, subject, physical–experiential bridge, or self-sufficient zero constitution.
