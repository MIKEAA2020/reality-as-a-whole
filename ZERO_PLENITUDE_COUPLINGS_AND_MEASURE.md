# A single zero whole containing frozen and changing couplings

## What this resolves

The preceding [balanced-exchange solve](ZERO_NEUTRAL_EXCHANGE_FROM_BALANCE.md) left a choice: its nontrivial coupling b can be zero or nonzero. Instead of choosing one, this report constructs **one coherent stationary state containing every integer coupling**, including b=0, while retaining exact charge balance and the earlier complementary-zero sector.

This is a precise finite-model version of the user's plenitude proposal: do not discard the frozen alternative merely to obtain change. The result is substantive but also exposes a further dependency:

- All coupling values can occur with nonzero amplitude in the **same** exact zero-constrained whole.
- Two such wholes, with the same coupling support, the same ± symmetry, the same Hamiltonian and the same constraints, give different clock-relative **and clock-unselected** record statistics.
- Requiring equal weights for an infinite set of couplings does not fix the issue: no normalized countably additive distribution can give every integer the same weight.

Thus *support for every possibility* and *a measure over them* are mathematically different. This does not disprove the user's thesis that genuine possibility and actuality coincide. A nonzero amplitude or a mathematical label does not by itself establish a genuinely possible, actually experienced subject; nor must actuality mean equal Born weight.

Verifier: [verification/zero_plenitude_coupling_clock_test.py](verification/zero_plenitude_coupling_clock_test.py). The exact infinite argument is given below; the executable checks use normalized finite truncations with analytic tail bounds.

**Measure-independent continuation:** [what zero balance fixes without choosing a coupling measure](ZERO_MEASURE_INDEPENDENT_RELATIONAL_RECORD.md) derives exact reference-record agreement throughout the full invariant neutral sector, without selecting a history or distribution, and tests whether the remaining weights can be reconstructed from relational readouts.

## 1. One coupling operator instead of one chosen coupling

Let H be the normalized neutral exchange from the prior report, with

```text
C = X_P+X_Q,          P₀ = I−C²/4,
H²=P₀,                [H,C]=0.
```

All states below lie in `P₀`, where `H²=I`. The initial system vector `|ψ₀⟩` is the previous invariant state with exact `C=0` and `B_P=0`. Its spin multiplicity embeds into the earlier common complementary-zero kernel. This state and these representations are still stipulated.

Introduce a coupling register G and an independent clock Cₗ, each with orthonormal integer basis:

```text
K|k⟩_G = k|k⟩_G,             H_clock|ℓ⟩ = ℓ|ℓ⟩,     k,ℓ∈ℤ,
H_system = K ⊗ H,
𝒞 = H_system − H_clock.
```

K is a **single operator**, not a chosen eigenvalue. The integers are dimensionless coupling strengths relative to the stipulated clock spacing. A real-continuum coupling, a physical clock and the choice of this lattice are not derived here. In particular, changing units alone is not evidence that different dimensionless ratios are physically identical.

With `P_±=(P₀±H)/2`, define a normalized branch

```text
|Ω_k⟩ = |k⟩_G [ |k⟩_clock P_+|ψ₀⟩ + |−k⟩_clock P_-|ψ₀⟩ ].
```

For `k=0` the two clock kets coincide and the expression is simply `|0⟩_G|0⟩_clock|ψ₀⟩`. The `|Ω_k⟩` are mutually orthogonal because of G; each is normalized and satisfies

```text
𝒞|Ω_k⟩=0,       C|Ω_k⟩=0,
```

as well as the specified permutation and older complementary conditions. The interaction is frozen in the k=0 branch and changes the system for nonzero k.

For **any** normalized sequence `a_k`,

```text
|Ω_a⟩ = Σ_{k∈ℤ} a_k |Ω_k⟩,       Σ_k |a_k|²=1,
```

is one normalized, coherent, unselected stationary whole satisfying these same zero conditions. Sequences with nonzero `a_k` for every integer include all the mathematical coupling branches, including zero. This is a pure vector; it is not a flag-dephased classical mixture.

One can express the construction as the kernel of one positive constraint: use `𝒞²`, the old charge and permutation-violation projectors, and the clock-dressed ready projector from the prior report, extended by the coupling register. Each `|Ω_k⟩` is in that kernel, so it has at least countably infinite dimension. The two geometric families below have finite second moments, so they lie in the usual domain of the displayed unbounded clock and coupling operators. The positive constraint is not identified with objective cosmic energy.

## 2. An independent relational clock

The clock has the standard phase POVM on `t∈[0,2π)`. Its generalized Fourier phase kets are not normalizable individual states; their effects define a normalized density. Conditioning the whole on a clock phase gives, up to the uniform density factor,

```text
|ψ(t)⟩ = Σ_k a_k |k⟩_G e^(−iktH)|ψ₀⟩.
```

The phase density is `1/(2π)` because the coupling labels are orthogonal and every conditional system evolution has unit norm. This clock is fixed across all k, so k controls the rate **relative to that clock**; the clock frequency is not separately rescaled to hide differences in k.

Let `B_P=(I−X_P)/2` and `B_Q=(I+X_Q)/2`. Their values agree in the neutral sector, while the underlying signed X values are opposite. Let `B_corr` be the invariant R–V comparison from the previous report. If `p_k=|a_k|²`, the probability of the `B_P=1` outcome at a phase reading t is

```text
P(B_P=1 | t) = Σ_k p_k sin²(kt).
```

B_P agrees with both B_Q and B_corr in this readout at every t. These are joint Born statistics under the specified interfaces, not actual subject incidences. The coherent phases between coupling branches remain in the whole but are not detected by this particular coupling-diagonal readout.

## 3. Same plenitude, different predictions

Consider two explicitly normalized, full-support, sign-symmetric distributions:

```text
p_k(q) = (1−q)/(1+q) · q^|k|,          0<q<1.
```

For every k, including zero, `p_k(q)>0`, and `p_k(q)=p_−k(q)`. Choose real positive amplitudes `a_k=√p_k(q)`. Both choices below define pure whole states satisfying **the same** exact zero constraints and using **the same** K and H:

| Quantity | q=1/2 | q=4/5 |
|---|---:|---:|
| Frozen-branch weight `p₀` | 1/3 | 1/9 |
| `P(B_P=1 | t=π/2)` | 4/9 | 40/81 |
| `P(B_P=1)` with clock ignored | 1/3 | 4/9 |

At `π/2`, `sin²(kπ/2)` is one for odd k and zero for even k, giving `2q/(1+q)²`. Ignoring the clock averages every nonzero integer frequency to one half, while k=0 remains unflipped, giving `(1−p₀)/2`.

Both states include every k and its negative. Both have exact P–Q charge zero, not just zero expected charge; both have equal ±k weights. Nevertheless, the specified readout predictions differ. Therefore the combination **zero constraint + full support + sign pairing** does not, by itself, mathematically determine this measure or these predictions. It remains possible that an additional necessity principle uniquely determines them; such a principle is not supplied by this construction.

These tables do not settle whether different k labels represent distinct physical possibilities, whether a coupling-register readout is available to a confined subject, or how observers should be counted. They also do not identify `X_P` or `X_Q` with experiential valence. A formal opposite sign would not erase anyone's suffering.

## 4. Why equal weighting over all integers is not a solution

Suppose a normalized countably additive probability gives each k∈ℤ the same weight c. If `c>0`, the sum diverges; if `c=0`, the sum is zero. Thus no such probability exists. Finite uniform distributions on `−N,…,N` have per-branch weight `1/(2N+1)` tending to zero; they do not converge to a normalized uniform probability on ℤ. This is a proof about a specific infinite set and normalization rule, not a reason to reopen the user's settled case against infinity as a whole-level quantity.

The history constraint itself admits a shift operation on the neutral subspace:

```text
|k,ℓ⟩⊗|h=±1⟩  →  |k+1,ℓ±1⟩⊗|h=±1⟩.
```

It maps `|Ω_k⟩` to `|Ω_(k+1)⟩` and preserves the zero constraint. If one **additionally** demands a normalized distribution invariant under this shift, its weights must all be equal, so none exists. The verifier checks this shift on finite interior histories; the infinite conclusion uses countable additivity.

Crucially, a symmetry of a constraint is not automatically gauge. The shift also transforms the clock/system relation, so fixed-clock readouts need not be invariant under it. Whether the shifts represent physical equivalence is a separate issue; this calculation does not assume they do.

For comparison, suppose instead that a *dimensionless* real coupling r were required to have a normalized probability invariant under `r→2r`. Every positive dyadic interval `[2^n,2^(n+1))` would have the same weight, as would every negative counterpart. Countable additivity forces all of those weights to zero; the only normalized invariant probability is `δ(r=0)`. This is a conditional measure theorem, not a claim that scale invariance is physically required. If a rescaling is merely a change of units, dimensionless ratios do not transform this way and the theorem cannot be invoked.

## 5. What would count as the next genuine advance

This construction avoids choosing between a frozen and a changing coupling by including both in one whole. It does not derive the integer spectrum, amplitudes, reference or clock. Full support alone does not determine a self-location measure, and equal infinite weights are unavailable under ordinary normalization. An advance beyond this would have to do at least one of the following **constructively**:

1. Derive the relevant observable algebra and show which coupling differences are genuine rather than gauge, without simply declaring inconvenient alternatives impossible.
2. Derive a normalized incidence measure from a necessary structure, or show that the needed predictions are independent of any admissible measure.
3. Derive the coupling/clock spectrum and the required reference resources from the proposed constitution of zero, rather than inserting them.
4. Connect any resulting physical distinctions to actual subject incidences and a defensible signed experiential quantity; the spin and charge signs here do not provide that connection.

These are dependencies of the user's no-residue proposal, not a proof that it cannot be met. The example shows exactly why simply placing all allowed Hamiltonians in a superposition is not yet enough.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_plenitude_coupling_clock_test \
  verification.zero_neutral_exchange_from_balance_test \
  verification.zero_minimal_symmetry_reference_record_test -v
```

The seven new tests check the stationary eigencondition for each retained coupling, full support and ± symmetry, distinct clock-relative and unselected predictions, the zero-coupling branch and the history-shift identity. For truncation at `|k|≤N`, the exact discarded probability is `2q^(N+1)/(1+q)`, which bounds the difference of any bounded probability readout from the corresponding infinite result. NumPy is required.
