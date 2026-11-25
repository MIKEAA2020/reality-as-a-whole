# Does zero's constitution determine experience and incidence?

## Direct answer to the test

I tried the promised integrated derivation. **The specified zero, symmetry and plenitude conditions do not yet determine the subject–experience relation or incidence measure.** This is not merely because a numerical coupling remains free: in the *same* previously constructed physical whole, I can grant the same set of actual paired incidences and the same weights, yet write two distinct opposite-valence assignments consistent with all the stated balance conditions.

That is a conditional mathematical nonuniqueness result. It is **not** a proof that the user's strongest no-residue conception is impossible, that either assignment is genuinely metaphysically possible, or that two ultimate wholes exist. In particular, neither completion has been shown self-sufficient. It shows that the currently formalized conditions are insufficient as a derivation; a stronger constitution could distinguish the candidates, identify them as physically equivalent, or require a different account of subjecthood. Any of those conclusions needs an argument, not a declaration that an inconvenient alternative is not genuinely possible.

The test also identifies a constructive discriminant: if a physically accessible report is independently established to report felt sign reliably, it can rule out one of the two candidate bridges in the example. **The report's phenomenal accuracy and the subject's access are additional premises**, not things the quantum matrix proves.

Executable test: [verification/zero_integrated_experience_necessity_test.py](verification/zero_integrated_experience_necessity_test.py). It uses the existing [mirror-paired whole](ZERO_MIRROR_BALANCE_PLENITUDE_AND_VALENCE.md), not another dynamical apparatus.

**Incidence-measure continuation:** [refinement, counting and the Born measure](ZERO_INCIDENCE_REFINEMENT_AND_BORN_MEASURE.md) applies the existing effect-algebra reconstruction to this exact ten-slot example, tests equal- and unequal-weight refinements, and separates mathematical labels from genuinely distinct subjects.

## 1. The intended derivation, stated without weakening it

The user's proposal is not merely the arithmetic equation `0=0`. The proposed zero is a self-sufficient whole, possibly with intrinsic relational constitution despite no external space or time. It is supposed to account together for

1. physical differentiation and a justified whole-level zero;
2. genuinely possible physical and experiential counterparts, with actuality following from genuine possibility;
3. actual subject boundaries and their felt signs;
4. the relation of those experiences to physical structure; and
5. incidence, measure and the observations available within the whole.

The no-residue requirement is that none of these determinate facts be an unexplained external selection or merely tolerated brute fact. The claim that no alternative framework could meet the demand if zero cannot, and the claim that the demand must be satisfiable once structural and experiential components are recognized, are substantive positions; neither is assumed proven or disproven here.

A successful derivation must therefore show not just that a mathematical zero **permits** such a structure, but why zero's own constitution **necessitates** it. Nor does “all genuine possibilities are actual” license declaring a rival not genuinely possible simply because it would spoil the preferred result. A necessary restriction would itself have to follow from the constitution.

## 2. Fix the physical whole before changing the experiential description

Use the already constructed mirror-paired history, not a new choice of dynamics. Restrict the coupling register to `k∈{−1,0,1}` as a finite test and take its previously used q=`1/2` distribution. The stationary state obeys the specified complementary-zero, neutral-charge, clock and mirror constraints. Its mirror operation changes both the mirror-flag sign `f` and the P-readout sign `s`:

```text
(f,s) ↦ (−f,−s),            f,s∈{+1,−1}.
```

The phase clock is read in the finite window `π/8≤t≤3π/8`. It has probability `1/8` under this model's clock POVM. After conditioning on the window, the fixed joint Born table is:

| coupling | weight | conditional `(f,s)` table |
|---|---:|---|
| k=0 | 1/2 | `(+, +)` and `(−, −)` each 1/2 |
| k=+1 or −1 | 1/4 each | all four combinations each 1/4 |

Thus ten triples `(k,f,s)` have positive probability. Every one has a distinct mirror partner `(k,−f,−s)` with equal probability. The table is calculated from the existing coherent state and finite-window clock instrument; it is not obtained by assuming a new classical mixture.

For the **semantic test only**, make unusually favorable additional assumptions: every one of those ten triples is an actual subject incidence, the same subject boundary can access the indicated f and s readouts, and the displayed Born weights give its incidence measure. This assumes no randomly selected single outcome. It also does not claim to cover all genuinely possible subjects or experiences in reality. Subjecthood, access and identification of Born weight with incidence are granted here so that the next question is not evaded by pointing to their absence.

The fixed physical state, physical operators, labels, actual incidence set, measure and mirror map are held constant in the next section. If subjective facts are themselves physical in the final theory, then the **complete** physical–experiential wholes below are different; the common state here is only their fixed physical restriction. The test does not assume that the physical restriction exhausts reality.

## 3. Two opposite-experience laws, same paired incidences

Let the signed felt value be ±κ with `κ>0`, provisionally assuming both signs are real felt states. Compare these two candidate bridge laws on the very same incidences:

```text
A: v(k,f,s) = κs,
B: v(k,f,s) = κf.
```

Both are deterministic functions of the specified physical readouts. Both assign positive and negative experiences. Both satisfy the *same* odd counterpart law and the same global zero:

```text
v(k,−f,−s) = −v(k,f,s),
Σ_incidence μ v = 0.
```

But they do not describe the same relation between physical record and experience. On the `k=+1` subpopulation in the window, f and s are independent and unbiased:

```text
                     law A          law B
⟨s v/κ⟩                 1              0
P(v ≠ κs)               0             1/2
```

The zero total remains true under either law, and negative-valued incidences have positive weight under both. Cancellation therefore does not make suffering unreal. The difference is not just a global reversal of the sign convention: even the absolute correlation `|⟨s v/κ⟩|` differs, one versus zero. If the physical sign labels or operators are not genuinely distinguishable in the true observable algebra, that could change the interpretation; the test assumes the displayed f and s readouts are fixed and distinguishable, and does not declare this a fundamental fact.

The comparison proves the following *limited* statement: from the explicit physical model, this incidence set and measure, mirror oddness and zero signed total, neither A nor B follows uniquely. It does not establish that both are genuine possibilities under the user's full necessity principle. Conversely, excluding one as impossible requires a criterion beyond the conditions displayed; calling it impossible is not itself that criterion.

## 4. A report constraint can discriminate—but cannot create the bridge

Suppose that, on this very subpopulation, an actual subject has access to the P record and produces a physical report R=s. Add the independent psychophysical premise that this report is a reliable report of the **sign actually felt**.

- Under A, the report agrees with the assigned felt sign in every incidence.
- Under B, it disagrees in half of them.
- For ±1 signs, a report error bound ε implies `⟨R v/κ⟩ ≥ 1−2ε`; B's correlation is zero and is incompatible with any `ε<1/2` in this stipulated situation.

This gives a concrete way to test a proposed physical–experiential identity rather than treating all assignments as equally acceptable. It is conditional: the present model does not show that a subject exists, that it has the required interface, that the report is truthful, or that this abstract apparatus has a local spacetime realization. If f is outside a confined subject's domain, B may fail an appropriate local-report test; it is not legitimate to assume the subject registers it. Conversely, a genuine possibility of an inaccurate report cannot be excluded merely because a proposed bridge requires accurate reporting.

If the subjective law changes what a subject veridically reports, the resulting **complete physical histories may differ**; the same fixed physical report cannot be kept while asserting that both assignments are always reported accurately. This is exactly why the physical restriction, the first-person interpretation and the report channel must be specified together.

## 5. Even granting actual incidences does not fix their measure

Keep the same physical whole, all ten actual incidence labels, the same mirror and either valence law. The Born-based incidence weight in the table gives total weight `1/2` to k=0. As a second *hypothetical incidence measure*, double the weight of every k=0 incidence and renormalize. Then

```text
μ₁(k=0) = 1/2,       μ₂(k=0) = 2/3.
```

Both measures have strictly positive weight on **exactly the same ten incidences**, preserve the mirror pairing, and give zero total signed valence under either A or B. They give different self-location weights. μ₂ is not the physical Born rule of the fixed state. If incidence measure is required to equal the Born weights, μ₂ is excluded—but that identification is precisely an additional rule that must be derived or justified, not a consequence of full support alone.

There is a constructive alternative in this finite example. **If each of the ten labels denotes exactly one distinct actual incidence and each incidence counts once**, normalized counting uniquely gives weight `1/10` to each and `P(k=0)=2/10=1/5`. Mirror balance then follows from the bijection; no separate equal-pair-weight choice is needed. This is a genuine determination *given those premises*. It differs from the table's Born-based `1/2`, so the account must explain whether and why unit counting, Born weighting, or another measure is the appropriate self-location rule. In particular, it must derive the incidence individuation and show that the ten labels are neither redundant descriptions nor multiple descriptions of one subject.

This is a finite test. It does not rely on an infinite totality, a uniform distribution over infinity, a simulator, or irreducible objective chance. A necessitated incidence measure would still be a measure; its necessity alone would not imply a randomly selected outcome.

## 6. What if both bridge laws are themselves included?

To respect the plenitude proposal, do not assume that A or B must be discarded. **If** both really are genuine possibilities and can coexist as distinct subject incidences, introduce an incidence-type label λ∈{A,B} and include every previously allowed incidence at both labels. The label represents a hypothesized real distinction, not an automatically physical flag or an established new subject.

For any `0<γ<1`, assign fraction γ of the weight at each incidence to λ=A and the remainder to λ=B. Both types and their mirrors are present with positive weight, and the total signed valence remains zero. Yet in the `k=+1` subpopulation,

```text
⟨s v/κ⟩ = γ.
```

For example, γ=`1/4` and γ=`3/4` contain the same labelled incidences and both preserve the same counterpart balance, but yield different relational incidence statistics. The two values are not claimed to be equally genuine or self-sufficient. The point is that **including both mathematical alternatives does not alone provide their relative incidence measure**. If the distinction λ is redundant or gauge, that must be established from the full physical–experiential algebra; if both are genuine, their co-actualization and measure must be accounted for without unexplained selection.

## 7. Where the direct derivation stands

The integrated test has a definite outcome:

| Dependency | What the explicit construction establishes | What is not derived |
|---|---|---|
| Zero and physical counterpart | Exact neutral constraint and a sign-reversing operator in the stipulated model | That these constitute objective whole energy or follow uniquely from zero |
| Plenitude | A coherent physical family retaining the specified alternatives; finite test grants all its positive-support labels actual | Which complete physical–experiential possibilities are genuinely possible, and why |
| Subject | Conditional incidence models can be evaluated | That the physical factors define actual subject boundaries or accessible interfaces |
| Felt opposite | Both A and B are odd under the same mirror and have zero sum | Which physical relation, if any, is felt sign; whether the counterpart really feels the opposite |
| Measure | Mirror-symmetric weights cancel an odd integrable value | Why the actual incidence measure equals any particular weighting or the Born rule |
| Necessity/no residue | The tested formal conditions permit inequivalent completions | A criterion that establishes or rules out their self-sufficiency |

The result is **not** a demonstration that zero cannot meet the demand. The strongest proposed constitution has not been axiomatized or derived, and the two conditional completions above cannot be advertised as satisfying its no-residue requirement. The result is that the available formal structure does not yet deliver the promised conclusion. Nor is another ungrounded mirror flag or fitted distribution a derivation.

A substantive continuation would have to derive a criterion that acts on the *combined* physical and experiential structure: it must fix or justify subject individuation, discriminate or identify the bridge laws, and determine the incidence measure, while explaining why any excluded possibilities are not genuine. Reliable report constraints provide one empirical/logical discriminator where their premises hold; they are not by themselves an account of first-person reality.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_integrated_experience_necessity_test \
  verification.zero_mirror_balanced_plenitude_subject_test \
  verification.zero_measure_independent_relational_record_test -v
```

The seven new checks calculate the finite-window table from the existing quantum state, compare the two bridge laws on the same positive-support incidence labels, verify mirror and zero-valence balance, construct the two measures and the conditional two-law plenitude, and check the report discriminator. They verify the conditional mathematics, not actual experiences, physical accessibility, a no-residue ontology or metaphysical possibility.
