# Energy, organization and the actual experiential total

## The next step

The [previous bridge](EXPERIENTIAL_ENERGY_RESPONSE_BRIDGE.md) associated signed experience with an energy-dependent score. It gave zero **in an ensemble average**, but left open whether actual experiences have that distribution. It also made the proposed contribution depend only on an energy value within the specified ensemble.

This continuation tests a more general candidate. Add an independently specified feature of physical organization to energy and use their joint response to define a signed scale. This can distinguish configurations with the same bare energy. However, the generalized quantity is still a centered score: its ensemble mean is automatically zero, and its identification with experience and actual incidence must be established independently.

Two further results sharpen the task:

1. The same local energy can acquire **opposite score signs in different global contexts**. If phenomenal character is fixed by a local constitution that is unchanged between those contexts, the unqualified global-score identity cannot hold in both. A whole-dependent account could avoid that conflict, but must explain how the relevant relations enter the experience.
2. Even if the ensemble score really is experiential, its zero mean implies an actual whole-level zero only with an additional fact about actual incidence. Approximate frequencies bound the *average* mismatch; they do not automatically give exact cancellation or a finite history total.

Both are conditional controls, not measurements of experience or proof against zero-totality.

## 1. A joint energy–organization candidate

For a fixed finite configuration set, let `E_i` be a stipulated physical energy and `L_i` an independently defined feature of organization. For example, a concrete theory might specify a relational coupling or pattern of interaction; simply assigning labels called L does not make them physical or experiential. With a fixed coefficient `g`, suppose

```text
A_i = E_i + g L_i,
p_i(beta) = exp(-beta A_i)/sum_j exp(-beta A_j).
```

The units of `g L_i` must match energy. In an actual canonical interpretation, `A_i` would have to be an independently justified effective Hamiltonian or other energy-like potential, not merely a name for an experiential score. The domain, g and the way beta varies are specified before examining valence. This is a finite equilibrium model, not a claim that a closed universe has an external bath or that this is its fundamental measure.

With `mu_A=sum_i p_i A_i` and `sigma_A^2=sum_i p_i (A_i-mu_A)^2>0`, differentiation at fixed E, L and g gives

```text
u_i = -(A_i-mu_A)/sigma_A,
sum_i p_i u_i = 0,
sum_i p_i u_i^2 = 1.
```

The candidate identity would be: `u_i` is the signed felt contribution of the corresponding actual experiential aspect, and p supplies its appropriate incidence weight. These are additional hypotheses, not consequences of the distribution. Negative u is not automatically pain, and neutral u is not absence of experience.

### A concrete contrast

Choose

```text
E=(2,2,2),  L=(-1,0,1),  g=1,  beta=ln(2).
```

Then `A=(1,2,3)`, `p=(4/7,2/7,1/7)` and

```text
u=(4,-3,-10)/sqrt(26).
```

Equal **bare** energy E no longer forces identical u: the organization term distinguishes the three cases. This is a mathematical illustration of an additional feature, not evidence of a phenomenal difference or of the existence of the proposed L. Nor does it escape dependence on a single scalar altogether: in this model `u` depends on `A=E+gL`. Distinct configurations with equal A in the same distribution get the same score, regardless of their other features. A richer physical organization could require further terms or a different map, each with its own grounding and testable consequences.

Adding a feature does not solve circularity. If `L_i` or g is chosen after observing the desired signs and balance, it can absorb the answer. An independently defined L should constrain other observations and produce out-of-sample predictions; the thermal assumptions, weights, subject incidence and mapping to felt valence must also be justified. This remains an energy-based proposal only if the effective potential and its relationship to the physical energy account are actually specified. It does not identify the zero of u with a gravitational or cosmological energy zero.

## 2. Context dependence: a conditional locality test

In the simple energy-only model at `beta=ln(2)`, compare two stipulated configuration sets:

```text
A: energies (1,2,3),  mean 11/7,  score for E=2:  -3/sqrt(26)
B: energies (2,3,4),  mean 18/7,  score for E=2:  +4/sqrt(26)
```

Both have `p=(4/7,2/7,1/7)` and variance `26/49`. Here the E=2 configuration is the second entry in A and the first in B. The sign reverses because its relation to the other available configurations changes. The entire spectrum has been shifted between the two examples, but **the compared E=2 occurrence has the same stated energy**; the examples do not claim the whole physical configuration is identical.

Suppose, additionally, that a genuinely identical local physical–experiential constitution can occur in both specified contexts, that its same fixed E is the relevant local value, and that its felt signed character is fully determined by that unchanged local constitution. Then identifying its felt character with the global normalized score in both contexts predicts two opposite signs, contrary to that locality assumption. Thus those assumptions cannot all hold together.

This is not a proof that phenomenal character must be local or that such contexts are physically realizable. The relevant subject might depend constitutively on wider relations, memory, environment or global structure; then the local constitution is not actually unchanged in the sense required. Alternatively, the theory might define u with a subject-specific distribution. Each option requires an account of which relations constitute a subject and why; it does not license treating an arbitrary choice of statistical reference class as a change in someone's feeling. The same point applies to `A=E+gL` if its centering distribution is global.

## 3. From the ensemble to actual occurrences

Fix a single specified distribution p and its corresponding score u. Let actual finite occurrences have normalized incidence fractions `r_i`, with `r_i>=0` and `sum_i r_i=1`. If those occurrences genuinely have experiential contributions u_i and all are counted with the stated weights, their actual average is

```text
Q_actual/N = sum_i r_i u_i
           = sum_i (r_i-p_i) u_i,
```

because `sum_i p_i u_i=0`. Exact equality `r=p` is sufficient for actual balance, but it is not necessary: some distinct r also give zero. A law of actual zero might instead constrain r to the zero-score hyperplane, if independently grounded; simply imposing it to obtain zero would not explain why it holds.

For the example above, take seven equally weighted, actual stipulated occurrences:

```text
counts (4,2,1): r=p,  total score = 0;
counts (3,3,1): r!=p, total score = -7/sqrt(26).
```

This compares two possible finite lists under the model, not two observed histories. Even when probabilities are correct for independent draws, the expected total is zero but individual realizations can be nonzero. With N independent draws from p of the fixed normalized score u, `E[sum u]=0` and `Var(sum u)=N`. Independence and probabilistic repetition are additional assumptions, not facts about the whole. The standard deviation of the sample *average* is `1/sqrt(N)`, but a small average does not mean the actual unnormalized sum is exactly zero; it also says nothing by itself about an infinite sum.

### A quantitative robustness bound

For finite normalized r and p and `TV(r,p)=(1/2) sum_i |r_i-p_i|`,

```text
|sum_i r_i u_i| <= 2 max_i |u_i| TV(r,p).
```

Therefore a justified close match of actual incidence to p would limit the discrepancy in the **normalized average**. It neither proves exact zero nor controls the unnormalized total without also accounting for N and how the mismatch scales. The measure and weighting needed for the user's whole—across subjects, mixed experiences, relational histories and possibly infinitely many occurrences—are still open.

## 4. What would a non-fitted bridge require?

A productive candidate should determine together, rather than merely list:

- the physical–experiential organization that makes an occurrence a real experience of a particular subject;
- the appropriate domain, E, L, coupling and oriented variation, with independently checkable physical consequences;
- the relation between the resulting score and actual positive, negative, neutral and mixed felt character;
- the actual incidence measure r and why it has the required relationship to the model's p, without assuming that alternative possibilities are all experienced or postulating a cosmic subject;
- the relation, if any, between the experiential balance and a properly defined global energy or constraint, with gravitational and boundary terms derived rather than introduced just to cancel;
- an account of internal time and records, not an externally preferred clock or foliation, and of sums or measures if the domain is infinite.

A restricted empirical programme could preregister the organization feature and energy-dependent response, then compare predicted relative valence with separately collected, ethically obtained reports and rival models. An observational mismatch challenges the stated mapping together with its measurement assumptions; a match does not prove metaphysical identity or that the actual whole has zero total. Reports are not direct third-person access to another's qualitative state.

## 5. Foundational status

The positive direction remains that one physical–experiential constitution might fix organization, subject incidence and a balance relation together, without an external creator or independent calibrator. The construction shows how a **specific** joint energy–organization response could yield a nontrivial signed scale and a conditional zero, and pinpoints the actual-incidence bridge needed to apply it to reality.

It does not establish that these mathematical ingredients follow from zero's nature or that the whole contains exactly the needed experiences. The context test is conditional on a strong locality assumption, not a refutation of a relational ontology. Nor does any failure of this particular model rule out a different additive or non-additive zero-totality, or establish that complete intelligibility is impossible. Genuine suffering remains real regardless of a proposed global balance.

## Verification

`python -m unittest verification.experiential_actual_incidence_test -v` checks the joint-feature model, opposite context scores, actual-count examples, total-variation bound and the finite independent-sampling expectation/variance. It verifies finite formulas only, not physical or experiential facts.

Related: [energy-response bridge](EXPERIENTIAL_ENERGY_RESPONSE_BRIDGE.md), [normalized response candidate](EXPERIENTIAL_SCORE_INVARIANT_CANDIDATE.md), and [subject plurality correction](SELF_EXISTENT_PLENITUDE_PLURALITY_CORRECTION.md).
