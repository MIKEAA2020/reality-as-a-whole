# Subject locality and the cost of overlapping experiences

**Constructive continuation:** [the conservation–incidence frame construction](ZERO_CONSERVATION_INCIDENCE_FRAME_CONSTRUCTION.md) derives reciprocal-multiplicity sharing from explicit local accounting and equal-response premises, and shows that the same frame normalization recovers the earlier sphere POVMs. Its subject, incidence and phenomenal assumptions remain unproved, and noncommuting observables require an explicit joint or sequential account.

## What this continuation establishes

The last [localized-module construction](ZERO_LOCALIZED_SUBJECT_MODULES_AND_INTERFACE_ENERGY.md) used a global modularity maximum to select candidate subject supports. I tested its warning about distant dependence and found an exact failure:

> A **completely disconnected** physical system can change the preferred partition of the original system, even though no local interaction in the original changes.

A simple alternative rule based on each candidate region and its own boundary avoids that particular dependence. But it introduces a different, consequential issue: its candidate supports can overlap. If overlapping supports are interpreted as distinct subject incidences, the physical conservation sum acquires **multiplicity weights**. A zero physical total need not remain zero when summed over those incidences.

These are precise constraints on subject constitution and actual experience weighting, not a demonstration that the toy systems are conscious. Neither criterion is derived from zero. The results do not require a literal simulation, an external agent, or a fundamental preferred foliation.

## 1. The earlier global criterion fails a locality check

Take the earlier weighted physical chain

```text
0 —3— 1 —1— 2 —3— 3.
```

Preserve its physical localized intervention directions and all its couplings. Add a **disconnected** pair `4—M—5`, and apply the same standard global weighted-modularity optimization to the complete six-site graph. Exhaustive comparison of all `203` set partitions gives:

```text
M=17:  unique optimum {{0,1}, {2,3}, {4,5}}; Q=53/128.
M=18:  unique optimum {{0,1,2,3}, {4,5}};  Q=252/625.
```

Only the coupling inside the disconnected pair changes. Nevertheless, the criterion changes the original four-site subsystem from two modules into one.

This is not a computational tie or a coordinate transformation. The reason is that global modularity's null model normalizes by total edge weight, which includes the disconnected pair. In general, the modularity change on merging `A={0,1}` and `B={2,3}` is

```text
ΔQ_merge = e_AB/m − vol_A vol_B/(2m²)
         = 1/m − 49/(2m²),      m=7+M.
```

It is negative at `m=24` and positive at `m=25`. The exact comparison of all partitions establishes that the displayed optima really are global maxima in these two finite examples.

If one **identifies** such optimal modules with actual subjects, their proposed count in the original subsystem changes in response to an entirely disconnected graph. That violates a natural disjoint-union stability requirement on a local subject criterion. It is **not automatically an operational superluminal signal**: that would additionally require a physical intervention with suitable causal separation and a locally distinguishable experiential/readout consequence. Nor do the two formal graphs assert that two incompatible complete wholes are genuinely possible. The result is a mathematical failure of this particular global individuation rule, not a metaphysical impossibility proof.

The construction's behavior illustrates a known limitation of global modularity objectives. [1](https://ar5iv.labs.arxiv.org/html/1107.1155)

## 2. A local replacement—and its own assumptions

For a nonempty set of localized sites `S`, define using only physical edges touching `S`:

```text
e(S) = total coupling weight on edges with both ends in S,
b(S) = total coupling weight on edges with exactly one end in S.
```

As a concrete research candidate, call `S` a **minimal local module** if

```text
e(S) > b(S)
and no nonempty proper subset of S also satisfies that inequality.
```

On the `3—1—3` chain the minimal modules are exactly `{0,1}` and `{2,3}`. Adding or changing the disconnected `4—M—5` pair does not change either original module, because `e(T)` and `b(T)` are unchanged for every `T⊆{0,1,2,3}`. This follows generally for an added disconnected system, not only for the tested weights.

This repairs the specific disconnected-system dependence without a global modularity maximum. It is **not** a derived consciousness rule: the localized directions, edge weights, the comparison `e>b`, the inclusion-minimality requirement and the scale/timescale of the graph are assumed. Its graph locality does not itself prove relativistic causality or the absence of signalling through all possible hidden or experiential variables. Nor do minimum modules automatically have an experience, a subject identity, or a particular felt quality.

### It can give overlapping candidates

For a uniform four-site chain `0—1—2—3` with unit weights, the same local rule gives

```text
S₁={0,1,2},       S₂={1,2,3}.
```

Both satisfy the criterion, neither has a satisfying proper subset, and they overlap at sites `{1,2}`. Neither declaring them two different subjects nor declaring them one shared subject follows from the graph. The rule has replaced global optimization with a **specific incidence question**, not solved it. A real account must also handle ties, changing supports, persistence and physically meaningful local interventions.

## 3. Exact balance with overlapping subject supports

Let `F_ij=−F_ji` be signed physical exchange into site `i` from site `j`, and let

```text
h_i = Σ_j F_ij,        Σ_i h_i = 0
```

for a closed finite graph. Now, **only as a test hypothesis**, assign a subject-supported signed value by summing the same local physical `h_i` over each candidate support `S_s`. Let `a_s>0` be its independently specified incidence/aggregation weight. Define the total incidence multiplicity at site `i`:

```text
m_i = Σ_s a_s 1[i∈S_s].
```

Then the proposed subject total is exactly

```text
Q_subject = Σ_s a_s Σ_(i∈S_s) h_i
          = Σ_i m_i h_i
          = Σ_(i<j) (m_i−m_j) F_ij.
```

The equality is algebraic and makes the problem visible. Internal physical exchange cancels in the **unweighted** sum, but if the actual experiential measure counts its endpoints unequally, a residue remains.

A uniform `m_i` on each connected physical component is sufficient for `Q_subject=0` for every flow. If the edge flows can be varied independently over the real numbers in the *formal class being tested*, this is also necessary: choose a nonzero flow on a single edge joining unequal multiplicities. A particular necessarily actual history could still have zero through its own correlations or boundary conditions; the theorem does not assert that all formal flow variations are genuinely possible or physically realizable.

## 4. Exact overlapping example

Use the two minimal supports above, give each the stipulated weight `1`, and consider the positive-energy four-oscillator chain at

```text
q=(1,0,0,0),     p=(0,1,0,0),     H=3/2.
```

With the prior symmetric interaction-energy convention, the instantaneous site rates are

```text
h=(−1/2, +1/2, 0, 0),       Σ_i h_i=0.
```

The candidate-support multiplicities are `m=(1,2,2,1)`. Therefore

```text
Σ_(i∈S₁) h_i = 0,
Σ_(i∈S₂) h_i = +1/2,
Q_subject = +1/2.
```

This happens even though **every site is in at least one candidate support**, because the shared sites are counted twice under the stipulated subject-sum rule. The graph and rates do not show that either support is conscious, that the shared site is one shared experience or two private experiences, or that energy rate is valence. The example shows why an actual subject-incidence law matters to the proposed identity.

One can enforce a physical accounting zero by dividing each site's contribution by its total multiplicity before summing:

```text
Σ_s a_s Σ_(i∈S_s) h_i/m_i = Σ_i h_i = 0      (m_i>0).
```

But that is a **new sharing rule**, not a derivation of subjective incidence or felt intensity. It might be right for one shared occurrence; it might be wrong for distinct experiences realized on overlapping physical supports. It cannot be adopted solely to obtain the target zero. A complete constitution has to determine whether incidences are shared, distinct or otherwise related, and why their actual weights have the required form.

## 5. Consequence for the point–sphere programme

The next candidate must join three things that these calculations now separate:

1. **Local subject organization:** an intrinsic rule that survives physical redescription and does not depend spuriously on disconnected systems. The local inequality is a test candidate, not yet that rule.
2. **Subject identity and overlap:** whether physical overlap constitutes shared or distinct experiential occurrences, including their persistence and actual measures. The mere existence of a graph overlap does not decide it.
3. **Physical–experiential balance:** a relation under which the **actual** subject incidence weights make the signed total zero, including interfaces and changes of subject domain. Local physical conservation alone gives the weighted edge formula above, not the desired result.

The point–sphere idea could in principle ground all three as facets of a single intrinsic constitution. This analysis has not derived that constitution, subjective feeling, the incidence measure, quantum no-signalling or whole-level zero. It has shown why neither a global optimization nor an unweighted energy identity is a sufficient substitute. The failure of those candidates does not refute the user's stronger thesis; accepting an unexplained selector or defining away real suffering would not complete it either.

## Verification

```text
python -m unittest verification.zero_subject_locality_overlap_balance_test -v
```

Seven standard-library tests enumerate all six-node partitions, check the disconnected-system sensitivity and the local alternative, verify its overlapping supports, and test the exact weighted-flow formula and the conditional multiplicity-sharing identity. They test finite mathematics, not actual subjects or a phenomenal law.
