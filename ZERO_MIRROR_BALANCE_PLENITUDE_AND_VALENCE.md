# Opposite signs across an unselected plenitude

## Result

The preceding [measure-independent result](ZERO_MEASURE_INDEPENDENT_RELATIONAL_RECORD.md) showed that three relational readouts agree throughout the specified neutral, permutation-invariant sector, regardless of the coupling measure. Here the proposed opposite-pairing principle is applied to that **whole family of histories**, including the frozen coupling.

An explicit involution exchanges the two signed alternatives while preserving the old zero charge, permutation constraint and clock constraint. Adding a mirror register and imposing a mirror-invariant eigencondition gives one coherent whole in which:

- every retained coupling history has its opposite-sign partner;
- the positive and negative readout probabilities are equal for **any** coupling amplitudes and for **any nonzero-probability clock/coupling effect** that leaves the paired system and mirror register alone;
- the flag–record correlation can nevertheless change with the relational clock; and
- the earlier exact zero-charge and three-way record agreement remain true.

This is stronger than cancellation of an average in one chosen distribution. But the mirror register, its symmetry, the physical readout algebra and the pairing condition are inputs. The construction does **not** establish two actual subjects, equal subject incidence, an experiential sign law or objective global energy.

Verifier: [verification/zero_mirror_balanced_plenitude_subject_test.py](verification/zero_mirror_balanced_plenitude_subject_test.py).

**Integrated necessity test:** [does zero's constitution determine experience and incidence?](ZERO_INTEGRATED_CONSTITUTION_EXPERIENCE_NECESSITY.md) holds this physical whole fixed, grants paired actual incidences as a conditional hypothesis, and tests whether zero, mirror and plenitude select a unique valence law or incidence measure.

## 1. A counterpart operation in the actual neutral sector

Use the previous system and its exact conditions

```text
P₀ = (I−X_P X_Q)/2,       C=X_P+X_Q=0,
P_G=+1,                   H²=P₀.
```

Here H is the normalized neutral exchange. Extend it to a unitary involution on the full system by

```text
S = H + (I−P₀),             S²=I.
```

S commutes with C, the permutation projector `P_G`, and H. In the common sector `Π=P₀P_G`, S flips each of the three previously matched readouts:

```text
S B_P S = I−B_P,
S B_Q S = I−B_Q,
S B_corr S = I−B_corr,       on Π.
```

It is thus an exact **within-sector** counterpart transformation for the specified operators. It is not a proof that an opposite sign is negative energy or opposite felt experience. Whether this model transformation corresponds to a physically accessible counterpart, or is gauge under a larger theory, also requires an independent account.

## 2. Pair every coupling without choosing its weight

For each integer k, let `|Ω_k⟩` be the earlier stationary history with coupling operator K and a fixed independent phase clock. It includes `k=0` and obeys the old neutral and permutation constraints. Add a two-state mirror register F and define

```text
|Ω_k^pair⟩ = [ |0⟩_F |Ω_k⟩ + |1⟩_F S|Ω_k⟩ ] / √2,
T = X_F S.
```

The register F is distinct from any prior internal reference bearing the same letter. The paired history is a pure coherent state, and

```text
T|Ω_k^pair⟩=|Ω_k^pair⟩,
𝒞|Ω_k^pair⟩=0,       C|Ω_k^pair⟩=0.
```

Since S commutes with H, it preserves the stationary clock constraint `𝒞=K H−H_clock`. For **arbitrary** normalized complex amplitudes `a_k`, including all full-support choices,

```text
|Ω_pair⟩ = Σ_k a_k |Ω_k^pair⟩
```

has the same properties. The `k=0` branch is paired rather than discarded. Orthogonal labels and amplitudes are not, by themselves, actual subject incidences.

The paired seed can be characterized without writing a weighted average by imposing two commuting relational eigenconditions on the flag plus neutral invariant system:

```text
T = X_F S = +1,             Z_F X_P = +1.
```

Their joint kernel of violations is one-dimensional for each k. With the prior charge, permutation and stationary-clock constraints, a single positive sum of their violation operators has exactly one paired zero history per retained k in the finite logical construction; the verifier checks the full kernel count. The amplitudes **between** different k remain free. Both relational conditions are additional inputs; the second replaces the earlier one-sided ready condition rather than silently preserving it.

## 3. Pairwise balance for arbitrary clock/coupling selections

Let E be any positive effect on the coupling and clock factors alone. It can coherently mix their labels. Because E commutes with T, whereas `X_P` changes sign under T on Π,

```text
⟨Ω_pair| E X_P |Ω_pair⟩ = 0.
```

Whenever the E-event has nonzero probability, the conditional probabilities of `X_P=+1` and `X_P=−1` are therefore exactly one half each. More finely, if f is the mirror-register Z value and x is the P sign,

```text
P(f,x | E) = P(1−f,−x | E).
```

The same sign reversal applies to Q and the matched R–V correlation readout. This conclusion does **not** depend on the amplitudes `a_k`, whether or not they are symmetric in k, or whether the clock is selected. It does depend on the whole being T-invariant and on E leaving the paired factors alone. Selecting one mirror flag without its counterpart is not such a symmetric selection and need not have balanced conditional signs.

Equal sign margins do not freeze the history. At clock phase t, the probability that the mirror flag and the P readout agree is

```text
P(agreement | t) = Σ_k |a_k|² cos²(kt).
```

It is one at t=0 and, for a full-support distribution, decreases at other readings. For the two infinite geometric distributions in the preceding report, it is `5/9` and `41/81` respectively at `t=π/2`. Thus the **sign balance is measure-independent**, while the changing flag–record correlation still carries measure-dependent information. The clock is periodic and the correlation reversible; no permanent memory follows.

The pure whole is not replaced by a mixture. The tested example has a maximally mixed reduced flag but retains off-diagonal coherence in the full flag–system density operator. Tracing out the flag is an operation, not a proof that one branch was selected.

## 4. Why mirror symmetry is doing real work

Exact `C=0`, full coupling support and opposite coupling signs do **not** alone force equal P-sign weights. For example, replace the equal amplitudes in the paired seed by

```text
√α |0⟩_F |Ω_k⟩ + √(1−α) |1⟩_F S|Ω_k⟩.
```

For `α=0.8`, all couplings can still have nonzero weight and the whole still satisfies C=0, but at the ready clock reading `⟨X_P⟩=0.6`. It is not a `T=+1` state. Thus the balance theorem follows from a **specified mirror-invariant whole**, not from the mere existence of a mathematical opposite.

The T condition can be proposed as a constitution or plenitude principle, but its necessity has not been derived. Nor has the added flag been shown to arise without extra structure. Equal Born statistics do not automatically establish equal numbers or measures of actual subjects.

## 5. The precise bridge needed for experiential cancellation

There is a clean conditional theorem. Let actual incidences form a measurable space, let `ι` be a counterpart involution, let `μ` be an incidence measure invariant under it, and let an integrable signed felt-valence function satisfy

```text
v(ιx) = −v(x),             μ(ιA) = μ(A).
```

Then a change of variables gives

```text
∫ v dμ = ∫ v∘ι dμ = −∫ v dμ = 0.
```

For a normalized finite measure and bounded valence, integrability is automatic. Infinite signed sums or σ-finite measures need independent convergence or regularization; pairwise opposite terms alone are not sufficient to justify rearrangement.

The physical construction supplies an operator counterpart and equal **specified Born readout statistics**. It does not supply the three further premises needed to apply the experiential theorem:

1. The paired physical alternatives correspond to distinct actual subject incidences rather than labels, gauge-related descriptions or unselected amplitudes.
2. Their actual incidence measure is invariant under the counterpart operation. This is not automatically the Born measure.
3. The counterpart maps a felt value v to a genuinely opposite felt value −v. A negative physical sign is not itself negative experience, and absence of experience is not suffering.

Even if those premises are established and the global sum is zero, each negative-v subject still suffers. A positive contribution elsewhere does not cancel the reality of that local suffering. Moreover `v→−v` preserves the oddness and zero-sum equations, so the formal balance alone cannot determine which physical alternative feels pleasant or painful. A complete account must address that experiential orientation as well as the measure and subject boundary.

## 6. Next dependency

This step shows how a whole-level opposite-pairing condition can fix signed physical **readout balance independently of all the previously undetermined coupling weights**, without freezing the relational record history. The next genuine task is not another symmetric bit by itself: it is to derive or constrain the correspondence between a physical counterpart, a subject boundary, an actual incidence measure and signed felt valence. Any proposed bridge must preserve the distinction between a globally zero signed sum and the reality of each local experience.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_mirror_balanced_plenitude_subject_test \
  verification.zero_measure_independent_relational_record_test \
  verification.zero_plenitude_coupling_clock_test -v
```

The eight new tests check the involution, paired kernel, full clock and charge constraints, arbitrary coherent clock/coupling effects, nontrivial record motion, an unequal-weight counterexample, and the conditional signed-measure identity. The tests do not establish conscious experience, actual outcomes, physical locality or objective global energy. NumPy is required.
