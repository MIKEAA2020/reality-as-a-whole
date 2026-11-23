# A concrete candidate: experiential character as a normalized relational response

## The idea in brief

**Energy-bridge continuation:** [energy-dependent normalized response](EXPERIENTIAL_ENERGY_RESPONSE_BRIDGE.md) specializes the score to a canonical energy family, derives explicit signed relative-energy values and independent conditional predictions, and distinguishes an ensemble mean from an actual whole-level total.

The [last investigation](EXPERIENTIAL_RELATIONAL_SCALE_WITHOUT_GLOBAL_SYMMETRY.md) asked for a candidate common constitutional invariant that could fix positive/negative comparisons without fitting them to a desired total. Here is a definite mathematical candidate, not a claim about established neuroscience:

> Suppose the whole has an intrinsically specified, oriented relational variation, and a normalized measure over actual experiential components. A component's signed experiential magnitude is proportional to the component's **normalized relative response** to that variation.

For a finite positive distribution `p_i(t)` this is the normalized score

```text
s_i = d(log p_i)/dt = p'_i/p_i,
I   = sum_i p_i s_i^2,
u_i = s_i / sqrt(I)                  (I > 0).
```

Because the distribution stays normalized, `sum_i p_i u_i=0`; and by construction `sum_i p_i u_i^2=1`. This produces a common dimensionless scale, nonzero local positive and negative values, and zero weighted total **without requiring a pairwise sign-reversing symmetry**. It is invariant under an orientation-preserving smooth reparameterization of the same one-dimensional variation. The second identity also shows that zero signed mean need not mean the represented differences vanish.

These are properties of a stipulated probabilistic model. The decisive proposal—that `u_i` is genuinely felt valence and that `p_i` is the right measure of actual experience—is **not established**. Normalization alone gives no subjects, suffering, objective experiential scale or physical energy. The question is whether the specified variation and measure could be aspects of one self-subsistent constitution rather than arbitrary inputs.

## 1. The construction and its exact scope

Assume a fixed finite index set of distinguished components and a differentiable family of strictly positive weights `p_i(t)` near some `t=t_0`, satisfying

```text
sum_i p_i(t) = 1.
```

At `t_0`, write `p_i=p_i(t_0)` and `p'_i=dp_i/dt|_(t_0)`. Differentiating normalization yields `sum_i p'_i=0`. Thus

```text
sum_i p_i s_i = sum_i p'_i = 0.
```

The nonnegative `I=sum_i (p'_i)^2/p_i` is the scalar Fisher information of this finite one-parameter family. If `I>0`, define `u_i=s_i/sqrt(I)`. Then

```text
sum_i p_i u_i = 0,
sum_i p_i u_i^2 = 1.
```

At least one `u_i` is positive and at least one is negative: if all had the same weak sign, positive weights and zero mean would force every term to vanish, contradicting `I>0`. Some components can have `u_i=0`. The argument uses normalized positive weights, a fixed domain and a nonzero tangent. It does not show that the actual universe has this domain or measure.

The single parameter can be an internal **configuration variation**, not necessarily time. It could describe comparison among relational configurations; whether these configurations are genuine possibilities and whether their comparative structure belongs to the actual whole must be established. Nothing assumes an external clock or a preferred foliation. A dynamical interpretation would require its own relational-clock construction.

## 2. A finite example with no opposite pairing

Take, for `-1/2 < t < 1`,

```text
p(t) = ((1+2t)/3, (1-t)/3, (1-t)/3).
```

At `t=0`, the three weights are each `1/3`, the derivatives are `(2/3,-1/3,-1/3)`, and

```text
s = (2,-1,-1),    I = 2,
u = (2,-1,-1)/sqrt(2).
```

The weighted sum is zero and the weighted square is one. There is no one-to-one sign-reversing permutation of `(2,-1,-1)`. If the three components were actual feelings and the identification with u were independently justified, the first would have positive and the other two negative contributions, all with real local magnitude; no individual experience is erased. The mathematics supplies neither that identification nor the subjects.

This is an identity for a normalized **weighted average**. It is a total over actual experiences only if the physical interpretation establishes that the `p_i` are the relevant actual-incidence weights, perhaps normalized from a finite total measure. The probabilities of alternative outcomes, an observer's credences, and a measure of simultaneously or history-wide actual occurrences are not automatically interchangeable. No cosmic subject is implied.

## 3. What is genuinely invariant—and what is not

Let `tau=f(t)` be a differentiable change of parameter with nonzero derivative at the point. Then

```text
s_i^(tau) = (dt/dtau) s_i^(t),
I^(tau)   = (dt/dtau)^2 I^(t),
u_i^(tau) = sign(dt/dtau) u_i^(t).
```

Hence positive reparameterizations leave u unchanged; reversing the orientation flips all its signs. Relabelling the components permutes the values but does not change the weighted sum, squared norm or relations among named corresponding components. An intrinsic physical/experiential orientation must therefore distinguish the sign associated with suffering. Choosing the direction after looking at feelings would not independently establish that choice.

This is **not** invariance under selecting a different variation in a multidimensional space, changing the experiential measure, or changing the underlying domain. Those operations can change u rather than merely its units. Nor is the Fisher normalization forced to be the physically or phenomenally correct unit: it is a definite convention derived from the supplied family, and might depend on the whole's global distribution. Its fitness as an intrinsic scale needs justification.

For example, at the same actual weights `(1/3,1/3,1/3)`, the derivative `(2/3,-1/3,-1/3)` gives score `(2,-1,-1)`, while `(-1/3,2/3,-1/3)` gives `(-1,2,-1)`. Both are valid normalized-family tangents. Actual weights alone do not determine which component is positive. A distinguished tangent, not just a normalized state, is an essential premise.

## 4. The risk of making zero automatic

This construction derives zero **as a normalization identity**, not as a consequence of zero's self-subsistence. In fact its freedom is much greater than it might first appear. Given any finite positive normalized weights and any signed list `v_i` with weighted mean zero, the family

```text
p_i(t) = p_i(0) [1 + t v_i]
```

is positive for sufficiently small t, normalized, and has score `v_i` at zero. Thus, if one starts with an already balanced list and then chooses the family to reproduce it, the score is just a repackaging. If a list is unbalanced for the independently specified weights, no normalized score can reproduce it exactly; choosing weights or a tangent after the fact may still manufacture an apparent fit.

A non-circular use therefore requires the **same oriented variation, measure, domain and scale convention** to be specified on independent constitutional or observational grounds before comparing their u-values with experiential valence. The mapping should have consequences beyond the automatically zero weighted sum. In particular, it would predict relative local signed responses, including which signs occur and their ratios. It may also fail if independently constrained valence and the proposed score disagree, subject to the uncertainties of measuring experience.

## 5. A testable contrast and an important coarse-graining issue

At `t_0`, a specified score predicts the first-order distribution change

```text
p_i(t_0+delta) = p_i(t_0) + delta p_i s_i + o(delta).
```

For positive delta, positive-score weights initially rise and negative-score weights fall. A concrete physical theory could specify an independently accessible relational control, predict these changes, and separately posit a mapping to valence reports or other pre-registered proxies. Observational support for this mapping would require checks against alternative response and reporting models; reports are imperfect and do not provide direct third-person access to felt intensity. Testing must be ethically designed and need not induce suffering. No finite experiment measures the entire whole or establishes metaphysical necessity.

Partition the indices into groups A, with `P_A=sum_(i in A) p_i`. The group's unnormalized score is

```text
S_A = P'_A/P_A = sum_(i in A) p_i s_i / P_A.
```

Its weighted total is still zero, but `sum_A P_A S_A^2 <= I`: grouping can erase internal contrasts. The group's normalized score would use its *own* Fisher information if nonzero, and thus is generally not the weighted average of the original normalized scores. If every group response is zero, that group-level normalization is undefined. This matters: changing how components and subjects are carved up can change the proposed magnitudes and even conceal suffering. A theory needs a physically and experientially justified domain, not a convenient coarse-graining.

## 6. What would make this an experiential constitution?

The hypothesis needs all of the following, not merely the score identity:

1. **Actual incidence:** establish what is experienced, by which subjects, and why the p-weighting refers to actual occurrences or aspects rather than unrealized alternatives. Separately explain neutral and mixed experiences and avoid double counting. No universal observer is assumed.
2. **Intrinsic direction:** identify a real oriented variation fixed by the whole's physical–experiential nature, not retrospectively chosen from the desired valence pattern. A formal tangent is not yet a physical possibility, an event or an experience.
3. **Phenomenal identity:** explain why normalized relative response *is* the positive or negative felt character of the component, rather than merely a correlation with report or a mathematical label. A negative response is not in itself pain.
4. **Appropriate total:** justify the incidence weights and additive aggregation, including how the whole's non-subject aspects enter its constitution. For infinite domains, specify differentiability, integrability, finite nonzero I and legitimate interchange of derivative and integral; normalization alone is not an unrestricted infinite-sum license.
5. **Energy and time:** derive a relationship to the user's global physical energy proposal if one exists. Fisher information is not energy merely because both can have units or express constraints; nor does this construction show equivalence to a gravitational constraint or establish emergent lived time.
6. **No unexplained residue:** show how the direction, domain, measure, subject incidence, qualitative identity and physical structure are all necessary aspects of one self-subsistent zero-totality. They might ultimately be unified, but they are supplied rather than derived here. Simply renaming them “zero's constitution” would not establish that unity.

A different fundamental relation, an unnormalized or non-additive experiential quantity, or zero without probabilistic weights remains possible. This candidate supplies a concrete target and a strong circularity test; it neither proves nor disproves the user's thesis that complete structural and experiential intelligibility can be achieved without residue.

## Verification

`python -m unittest verification.experiential_score_invariant_test -v` checks the rational score identity, Fisher normalization, reparameterization, distinct tangents, reconstruction of an already-balanced list, and information loss on coarse-graining. It checks a finite formal construction, not actual experience, a physical theory or self-subsistence.

Related: [relational experiential scale](EXPERIENTIAL_RELATIONAL_SCALE_WITHOUT_GLOBAL_SYMMETRY.md), [intrinsic relational accounting](ZERO_TOTALITY_INTRINSIC_RELATIONAL_ACCOUNTING.md), and [the physical zero-constraint example](ZERO_TOTALITY_FLRW_CONSTRAINT_AND_ENERGY.md).
