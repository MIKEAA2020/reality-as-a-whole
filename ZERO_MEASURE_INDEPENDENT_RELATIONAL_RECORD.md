# What zero balance fixes without choosing a coupling measure

## Result

The [plenitude construction](ZERO_PLENITUDE_COUPLINGS_AND_MEASURE.md) retained frozen and changing couplings together but found that their weights affect record frequencies. The next question is whether **anything nontrivial follows for all admissible weights**.

Yes. In the existing reference model, a perfect three-way relational agreement follows directly from the symmetry and exact zero-charge sector. It needs **no chosen coupling distribution, no particular initial vector, and no particular Hamiltonian**. It also survives arbitrary operations and postselection confined to the coupling and clock factors.

This does not fix how often the two values occur. In the plenitude history, those frequencies encode the coupling weights: under idealized readout assumptions, a time series can reconstruct them. Thus the same construction separates a robust structural consequence from the unresolved measure problem.

Everything here is conditional on the previously specified Hilbert spaces, permutation action and charge; none is derived from the bare number zero. A joint quantum record is not thereby a subject or an actual experienced outcome.

Verifier: [verification/zero_measure_independent_relational_record_test.py](verification/zero_measure_independent_relational_record_test.py).

## 1. The two exact operator identities

Use the earlier R–P–Q–V system:

- R is the multiplicity reference, V is the two-dimensional spin-zero multiplicity.
- P is the parity reference, Q its compensator.
- `P_G` projects onto simultaneous permutation-invariant states.
- `C=X_P+X_Q`, and `P₀=(I−X_P X_Q)/2` projects onto `C=0`.
- `B_P=(I−X_P)/2`, `B_Q=(I+X_Q)/2`.
- `B_corr=I−|Φ⟩⟨Φ|_RV`, with `|Φ⟩_RV` the canonical D*⊗D invariant vector.

Direct operator calculation yields

```text
(B_P − B_Q) P₀ = 0,
(B_P − B_corr) P_G = 0.
```

These are stronger than equality of expectation values. The first follows from exact opposite X charges. The second follows from the specified symmetry: the `X_P=+1` component is paired with the trivial R–V representation `|Φ⟩`, while the `X_P=−1` component must be paired with the orthogonal sign representation. The verifier checks the complete operators, not just selected examples.

Since `P₀` and `P_G` commute, put `Π=P₀P_G`. Its rank is two, and on this entire sector

```text
B_P = B_Q = B_corr       (as operators acting on Π).
```

The common zero and one sectors each have rank one. For **any density operator supported on Π**, including one entangled with further factors,

```text
P(B_P=B_Q=B_corr)=1.
```

In terms of the underlying signed charges, a joint X readout gives `X_P=−X_Q` in either value. This agreement is fixed even if one value has probability zero, and even if the system never evolves. It is therefore a robust *constraint correlation*, not by itself a temporal record, an actual event, or proof of subjective access.

## 2. Independence from clock, coupling and their measure

The identities in section 1 do not contain H, a clock, an initial state, or any `p_k`. In particular they apply to the whole family of coherent coupling histories constructed previously, for **any** normalized amplitudes and relative phases, not just symmetric geometric weights.

More generally, let an arbitrary quantum operation or postselected effect act only on additional coupling and clock factors. Because those operations commute with all three system readouts and with Π, the post-operation system remains supported on Π whenever the conditioning event has nonzero probability. The three readouts still agree with probability one. The tests include effects that **coherently mix** coupling and clock labels, not merely diagonal selections.

This invariance does not cover interventions on R, P, Q or V that take the system out of Π. It also does not establish that a confined observer can access `B_corr`: that projector is a joint R–V comparison. The formal structure is real within the stipulated quantum model, but its physical implementation, locality and experiential significance remain open.

## 3. Plenitude gives strict bounds, not a unique weight

For the previous integer-coupling history with a fixed independent relational phase clock, let `p_k=|a_k|²` and

```text
p(t) = P(B_P=1 | t) = Σ_k p_k sin²(kt).
```

If every integer has positive weight, then `p₀>0` and `p₁>0`. Consequently, whenever `t` is not an integer multiple of π,

```text
0 < p(t) < 1.
```

Both correlated readout values have nonzero Born probability at those readings, **independently of the full-support measure**. At `t∈πℤ`, `p(t)=0`. This remains a statement about possible readout statistics, not a demonstration that both outcomes are actual subjects.

The strict bounds are not uniform over full-support measures. At `t=π/2`, take any fixed sign-symmetric full-support distribution q and form

```text
p^(low)  = (1−ε)δ₀ + εq,
p^(high) = (1−ε)(δ₁+δ₋₁)/2 + εq.
```

Both have positive weight at every integer and preserve k↔−k symmetry. As ε tends to zero, `p^(low)(π/2)` approaches 0 and `p^(high)(π/2)` approaches 1. So plenitude forces neither a uniform positive lower bound nor a particular frequency. The perfect-agreement mutual information is the binary entropy `h₂(p(t))`; it is nonzero for each full-support distribution at the nontrivial readings, but has no distribution-independent positive lower bound.

## 4. The measure is not invisible if these readouts are physical

Define the Hermitian invariant current-like observable

```text
J = i[H,B_P],          H = [(Y_PY_Q+Z_PZ_Q)/2] Y_V.
```

It commutes with C and with the stipulated simultaneous permutations. For the particular prior history family,

```text
j(t) = ⟨J⟩_t = Σ_k p_k sin(2kt).
```

This is an additional joint observable, not the same measurement as B_P and not automatically available to a subject. Under the specified antiunitary Θ of the earlier model, `J` is odd. Thus interpreting its sign requires a physically meaningful relational orientation; if that reversal is gauge, the corresponding sign distinction cannot simply be asserted as observable.

Under the idealization that the chosen clock phase and both B_P and J can be measured over the whole interval, Fourier orthogonality reconstructs the **entire diagonal coupling distribution**, even without k↔−k symmetry. Write `⟨f⟩=(1/π)∫₀^π f(t)dt`. For `n≥1`,

```text
p₀ = 1 − 2⟨p⟩,
s_n = p_n+p_−n = −4⟨p(t) cos(2nt)⟩,
d_n = p_n−p_−n =  2⟨j(t) sin(2nt)⟩,
p_±n = (s_n ± d_n)/2.
```

If only B_P is available, the even combinations `p_n+p_−n` are determined, but their signed differences are not. The verifier recovers a deliberately asymmetric finite distribution, with arbitrary coherent coupling phases, from these formulas. For an infinite normalized distribution the series converge absolutely; the integrals are an ideal mathematical reconstruction. Finite clock resolution, finite sampling and inaccessible interfaces can prevent practical recovery.

These two readouts are diagonal in the coupling label after the register is ignored: they do **not** recover relative phases between `a_k`, nor do they establish that k and −k are distinct actual experiences. They do show that treating all weight choices as physically equivalent would require an additional gauge or observability argument; it does not follow merely from the zero constraint.

## 5. Consequence for the zero program

The result removes one apparent dependency: within this model, the *agreement* between the parity reference, its compensator, and the R–V correlation does not need a selected coupling, coupling measure, or special prepared history. It follows from the specified symmetry and zero sector themselves. This is a concrete structural relation in the whole, even when its rate distribution remains undetermined.

It does not derive the group, charge, representations or reference from zero, and the agreement is not a derivation of actual subjecthood or oppositely felt valence. The inferred measure is a Born distribution for stipulated mathematical branches, not an independently established incidence measure. Exact local signed cancellation does not make an individual's suffering unreal.

The next substantive dependency is therefore sharper: derive or justify the symmetry/charge representation and establish what relational observables and subject incidences are physically available. Alternatively, a successful plenitude principle must determine the remaining distribution or demonstrate that its differences are unobservable under the true physical algebra. Neither follows simply from declaring all possibilities present.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_measure_independent_relational_record_test \
  verification.zero_plenitude_coupling_clock_test \
  verification.zero_neutral_exchange_from_balance_test -v
```

The six new tests cover the operator identities on the full invariant/neutral sector, arbitrary sector states and coherent clock/coupling postselection, current symmetry and reversal, exact finite Fourier reconstruction, and the strict-but-not-uniform full-support bounds. NumPy is required.
