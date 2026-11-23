# A candidate zero for actual experiential occurrences: relational stationarity

## Why try a different route?

The [previous investigation](EXPERIENTIAL_ENERGY_ORGANIZATION_AND_ACTUAL_INCIDENCE.md) found a gap between a zero statistical expectation and a zero sum over **actual** experiences. Here is a different constructive route: a variational relation defined directly over actual occurrences, with no probability distribution over alternatives required.

> Suppose actual experiential aspects are constitutively related through one intrinsic stationary organization. Each has a signed contribution given by its own part's response to a common admissible internal variation. If all other terms in the organization are unchanged by that variation, the actual contributions sum to zero.

This conditional principle can produce nonzero local contributions, including both signs, without assuming an ensemble frequency, a cosmic experiencer or an external time. The mathematical illustration below also derives the internal configuration from a stated functional, rather than starting from an already zero-total list.

The crucial proposed identity—such response **is** felt positive or negative character, including real suffering—is not established. Nor are the functional, actual subject incidence, stationarity or particular internal differences derived from zero-totality itself. This is a candidate for investigating the no-residue demand, not a completed derivation or a proof that it cannot be met.

## 1. The general conditional argument

Suppose a finite domain of actual aspects `i=1,...,n`, each represented by a variable `x_i` and an incidence weight `w_i>0`. Let a differentiable constitutive functional be

```text
F(x) = sum_i w_i V_i(x_i) + R(x).
```

Assume the actual configuration x is stationary along the admissible **common** variation `x_i -> x_i + epsilon`, and assume `R(x+epsilon 1)=R(x)` for sufficiently small epsilon. Then

```text
0 = d F(x+epsilon 1)/d epsilon at epsilon=0
  = sum_i w_i V'_i(x_i).
```

Define the actual signed contributions as `q_i=w_i V'_i(x_i)`. It follows that `sum_i q_i=0`. If at least one q is nonzero, there must be contributions of both signs. The weights and q's are not probabilities: in the proposed interpretation they refer directly to actual aspects and their independently fixed incidence or measure.

This argument assumes only stationarity along the common direction, not that arbitrary independent variations are admissible. If independent variations are admissible and F is stationary in all of them, the full derivatives `∂F/∂x_i` each vanish, but the **partial-term contributions** `w_i V'_i` need not vanish: the interaction derivatives can balance them. There is no contradiction between local q being nonzero and stationarity of the complete F.

The choice `q_i=w_i V'_i` and the decomposition of F are substantive. Stationarity of the full functional does not by itself say which partial derivatives are felt valence, or even provide a unique decomposition. Nor is a common-shift-invariant R implied by self-containment alone.

## 2. An explicit nontrivial finite constitution

Consider three variables on a fully connected triangle, with equal weights and

```text
F(x;a) = 1/2 sum_i (x_i-a_i)^2
       + 1/2 sum_(i<j) (x_i-x_j)^2.
```

The first term defines a local response relative to stipulated intrinsic reference values a; the second couples actual aspects relationally. Take a to be fixed under the x-variations. It is not automatically an external physical agent or a preferred frame, but its role and origin still require explanation. Independent variation gives

```text
0 = (x_i-a_i) + sum_(j != i) (x_i-x_j).
```

Thus, with `q_i=x_i-a_i`, each local response is balanced by interaction derivatives and `sum_i q_i=0`. The Hessian is positive definite (`I` plus the triangle graph Laplacian), so for every given a the stationary x is unique. If `A=sum_i a_i`, solving gives

```text
x_i = (a_i+A)/4,
q_i = (A-3a_i)/4.
```

For the explicit stipulated inputs

```text
a = (-8/3, 4/3, 4/3),
x = (-2/3, 1/3, 1/3),
q = (2, -1, -1),          sum_i q_i=0.
```

The actual response has nonzero local components and no one-to-one equal-and-opposite permutation. It is determined by the given F and a rather than by selecting q as a constraint. Nevertheless, the chosen references and their qualitative meaning are assumptions; the model does not establish that these three variables are actual experiences.

For this connected positive-coupling example, a nonzero response occurs **if and only if** the references are not all equal. If all a_i are equal, the unique stationary configuration has `x_i=a_i` and every q is zero. Conversely, if all q vanish, the stationarity equations give a zero graph Laplacian, so connectedness makes all x equal, and then all a equal. Thus the functional and zero-total result do not themselves force differentiated reference values; they allow both the trivial and nontrivial cases.

## 3. Why this is not yet a derivation from zero

The model has more content than an arbitrary after-the-fact pairing: once F and a are fixed, it determines x and q and predicts responses to changes of the inputs. For example, adding `-J sum_i x_i` to F gives, under independent stationarity,

```text
sum_i q_i = 3J.
```

This exposes the specific role of the assumed shift-invariant interaction and absence of an additional term that changes under the common variation. J is a formal source in this model, not automatically an external creator or something outside the whole. An account claiming that the actual constitution admits no such term needs a reason, not just its omission from F.

There is also an exact circularity control. For **any** already chosen triple q with `sum_i q_i=0`, setting

```text
a_i = -4 q_i/3
```

makes `sum_i a_i=0` and yields that q in the triangle model. If references are chosen this way after seeing desired experiences, the calculation merely reconstructs an assumed balance. The candidate has explanatory force only if the functional, reference relations, incidence weights and their relation to actual experience have independent constitutional warrant or discriminating implications.

The zero is not the value of F. In the displayed example, `F=4`, while `sum q=0`. Nor does stationarity of this static finite functional establish a physical Hamiltonian constraint, a vanishing global energy, an energy–experience identity, or evolution in time. A formal derivative is not an actual feeling or a force unless a physical and phenomenal theory gives it that role.

## 4. Is the construction genuinely relational?

The interaction term depends only on differences `x_i-x_j`. Simultaneously replacing every `x_i` and every `a_i` by the same shifted values leaves F and q unchanged. This removes dependence on a *common origin* of their descriptions. It does **not** eliminate the actual relative reference values `a_i-a_j`, nor prove they follow from zero. Shifting x alone while holding a fixed is the varied physical direction in the stationarity calculation; it is not the same operation as the joint change of origin. Neither operation is automatically a gauge symmetry of nature.

For the full independent stationarity equations, set `f_ij=-(x_i-x_j)`, with `f_ji=-f_ij`. Then

```text
q_i = sum_(j != i) f_ij.
```

The example therefore connects the [intrinsic accounting proposal](ZERO_TOTALITY_INTRINSIC_RELATIONAL_ACCOUNTING.md) to an explicit stationary functional: for a chosen F and a, the interface terms follow from x rather than being introduced separately. The older accounting result already showed that a divergence representation can always be fitted to any zero-sum list on a connected graph. Here too, the existence of such a representation or a unique stationary point does not, by itself, derive the needed constitution from zero.

The common variation can be an atemporal comparison of internal configurations; it is not necessarily a temporal process or intervention. Genuine relational or emergent time would require an additional physical account of clocks, histories and records. For infinite domains or continuous histories, admissible variations, boundaries, convergence and exchanges of derivatives and sums must be justified; the finite result alone cannot be extended by cancellation of infinities.

## 5. What would make the candidate experiential?

The positive proposal is that the local response and the felt aspect could be **the same real physical–experiential determination**, viewed in different ways, rather than a mathematical number creating a feeling. To make that proposal substantive, one must explain:

1. **Subject and actuality:** what constitutes an actual aspect, why it is present to a particular subject, and how distinct subjects or mixed and neutral experiences are represented without double counting. A graph node is not automatically a subject.
2. **Phenomenal direction and scale:** why `V'_i` has the sign and magnitude of positive or negative felt character, and what fixes its common unit and weights across aspects and subjects. A positive derivative is not inherently pleasure, and a negative derivative is not inherently suffering.
3. **Constitutional necessity:** why the functional and relative references are aspects of the whole's own nature and why this common variation is admissible and stationary, rather than extra inputs or an equation selected to produce zero.
4. **Nontriviality:** why determinate differences such as unequal a arise from that nature. Stationarity and zero themselves permit the equal-a, no-response solution.
5. **Physical significance:** what physical organization realizes the terms and what the model predicts independently of the global zero. The present F is not identified as the universe's energy; arbitrary relabelling would not establish that it is.
6. **Ethics and pluralism:** actual pain remains someone's real pain, regardless of other terms in a sum. The balance neither erases suffering nor proves it justified, and no universal subject is assumed.

One possible way forward is to seek a physically grounded action or constraint whose independently defined internal variations have observable local consequences and whose subject-level interpretation can be separately examined. That would still have to show why these structures are constitutive of experience and how their presence is intelligible without an unexplained residue; a mathematical stationary point alone does neither.

## 6. Result

This route closes one limited gap in the earlier **model**: under explicit assumptions it obtains a zero sum directly over stipulated actual aspects, not merely an ensemble expectation. It gives nontrivial local responses with no preferred external clock and provides a concrete test of how its law could be fitted after the fact.

The remaining question is precisely the user's central one: whether the stationarity, nontrivial differences, experiential character and their determinate organization are all consequences of one self-subsistent zero nature. They have not yet been derived here. Nor has any impossibility been shown, or the demand for complete structural and experiential intelligibility relaxed.

## Verification

`python -m unittest verification.actual_experience_variational_zero_test -v` checks the exact triangle solution, local derivatives and total, nontriviality controls, common-origin invariance, the source contrast and reconstruction from arbitrary zero-sum triples. The tests verify specified finite arithmetic, not experience, physical energy or self-subsistence.

Related: [actual incidence and energy](EXPERIENTIAL_ENERGY_ORGANIZATION_AND_ACTUAL_INCIDENCE.md), [intrinsic relational accounting](ZERO_TOTALITY_INTRINSIC_RELATIONAL_ACCOUNTING.md), and [zero-totality self-subsistence](ZERO_TOTALITY_SELF_SUBSISTENCE_ARGUMENT.md).
