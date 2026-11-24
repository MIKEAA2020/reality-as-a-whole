# A zero-energy clock for the recollapsing sphere–memory model

**Sign-pairing continuation:** [necessary plenitude and identity pairing](ZERO_NECESSARY_PLENITUDE_SIGN_PAIRING.md) constructs an encoded energy-sign-reversing exchange and tests a maximally symmetric dual-pair state in this model.

## Result

We can combine the two preceding constructions **in one finite constrained system**: the actual five-ray sphere code, dynamical oscillator geometry, detector, two original memories, targeted memory B, and an internal clock with an explicitly matched positive/negative energy ledger. Every component of the constructed whole state has **exactly zero total energy eigenvalue** under the declared total operator.

To make an exact normalized finite-clock POVM possible, the oscillator model's spectrum is rounded to a fine energy grid. This **changes the rest Hamiltonian**; it is not the original window-local Hamiltonian exactly. At the Fock cutoff used below, the difference in either preparation's normalized conditional state is nevertheless bounded analytically by `|t|δ/2`, where δ is the energy grid spacing. The numerical comparison confirms that bound. The cutoff and rounding remain model assumptions, not a proof about continuum gravity.

The resulting calculation has two connected findings:

1. Under the same energy-balanced dynamics and exactly the same conditional geometry state, a B memory pre-correlated with the sphere relation has an arrow **toward** maximum mean scale on the sampled interval, while a blank B has the opposite arrow. The geometry's reduced entropy rises away from the maximum in both. The first correlation is prepared at the turn, not derived from zero.
2. A coherent and an energy-dephased **whole** can both have exact zero energy and identical clock and rest marginals. Yet the coherent whole has a recollapsing conditional geometry and a changing record; the dephased whole has a clock-independent conditional state. Thus zero total energy and those separate marginals do not determine their joint history.

The second result is a concrete constitutive target: a zero-whole account must determine or explain the full relations, not just the zero total and separate descriptions of its parts. The two states are mathematical controls, not a claim that both are genuinely possible or actual under a necessitarian theory.

This continues [Lighthouse adapted to zero energy](LIGHTHOUSE_ADAPTED_TO_ZERO_TOTAL_ENERGY.md) and [the recollapse sphere model](ZERO_RECOLLAPSE_SPHERE_RECORD_ARROWS.md). Tests are in [verification/zero_energy_recollapse_clock_test.py](verification/zero_energy_recollapse_clock_test.py).

## 1. Start with the actual coupled rest system

The active sphere code is spanned by the **actual five-ray states** `|Ψ₀⟩, |Ψ₁⟩`, with `K=1−2h` and h eigenvalues 0,1. The geometry has oscillator number N and `Q=(b+b†)/√2`; the positive scale observable is `A=exp(0.3Q)`. The other internal factors are detector D, two memories M¹,M² and targeted memory B. The explicitly coupled Hamiltonian from the recollapse report is

```text
H = N + h
  + 0.5 W_(−1)(Q) Y_D
  + 0.65 W_0(Q) P₁ᴰ Y_M¹
  + 0.65 W_1(Q) P₁ᴰ Y_M²
  + 0.4 W_1(Q) h Y_B,
W_c(Q)=exp[−(Q−c)²/(2×0.7²)].
```

This includes the geometry dependence and the joint record–work coupling; the memory does not merely follow a prescribed scale curve. The earlier calculation showed nonzero geometric backreaction. The actual full sphere states, rather than unrelated h labels, are contracted in the new verification.

At finite oscillator cutoff n define `H₀=H+2.2 I`. Since each window is between 0 and I, each spin/projector factor has norm at most 1, and `N+h≥0`, the sum of the four interaction norms is at most 2.2. Hence `H₀≥0`. This offset is a mathematical convenience, **not** a physical derivation of the zero of energy. It cancels between the two sides of the ledger below.

Now define, by spectral calculus,

```text
H_δ = δ round(H₀/δ),       δ>0.
```

Ties can be resolved by a fixed convention. Its eigenvalues are nonnegative integer multiples of δ, and `||H_δ−H₀||≤δ/2`. At finite n, the rounded operator is precisely defined and self-adjoint. It generally contains effective nonlocal/higher-body terms when expanded in the original factors: it should **not** be presented as the original Hamiltonian with unchanged local interactions. Its commutation with h and the three memory-Y operators is retained because it is a function of H₀.

## 2. An exactly zero-energy whole and a normalizable clock POVM

Let `P_k` be the spectral projector of H_δ at energy `E_k=δk`, and include each distinct energy tick k in a finite-dimensional clock C with

```text
H_C = Σ_k E_k |k⟩⟨k|,      H_total = H_C⊗I − I⊗H_δ.
```

For a normalized rest boundary vector `|ψ₀⟩`, set `|v_k⟩=P_k|ψ₀⟩` and form

```text
|Ω⟩ = Σ_k |k⟩_C ⊗ |v_k⟩_R.
```

Different `v_k` are orthogonal, and `Σ||v_k||²=1`. The exact cancellation is componentwise:

```text
H_total |Ω⟩ = 0,
⟨H_C⟩ = ⟨H_δ⟩,             ⟨H_total⟩=0.
```

For the n=24, δ=0.02 example below, the clock has 380 distinct ticks and the two opposing expectation contributions are approximately `+4.66114` and `−4.66114` in the chosen units. The clock is **constructed to mirror the rest spectrum**; this is not derived from zero and its dimension is not fixed by the proposal. `H_total` is an explicitly declared objective candidate in this finite model, not a proof that gravitational energy has this form in our universe.

A periodic clock POVM is

```text
|t⟩ = d^(−1/2) Σ_k exp(−iE_k t)|k⟩,
E_C(dt) = (d/P) |t⟩⟨t| dt,          P=2π/δ.
```

The k are distinct integers, so integration over one period gives the identity. These clock states are generally **nonorthogonal**: this is a normalized, covariant phase POVM on a finite clock, not a sharp ideal external clock. With the matched state the probability density of its reading is uniform over the period. The normalized rest state conditional on t is

```text
|ψ_δ(t)⟩ = Σ_k exp(+iE_k t)|v_k⟩ = exp(+iH_δ t)|ψ₀⟩.
```

The plus sign follows from the chosen negative rest contribution to H_total and the definition of `|t⟩`. This is a conditional relation in a stationary whole; it does not require the whole to evolve in external time. A physical implementation of the clock measurement and its energy cost is not supplied, and a reading cannot be taken as a perfectly sharp or permanent clock record.

## 3. Controlled relation to the original recollapse calculation

For each finite n and initial state, spectral rounding gives the exact vector bound

```text
|| exp(iH_δ t)|ψ₀⟩ − exp(iH₀ t)|ψ₀⟩ || ≤ |t| δ/2.
```

It follows directly from the spectral theorem and `|exp(ix)−exp(iy)|≤|x−y|`. The old report used `exp(−iHt)`; the comparison here uses its state at `−t` and includes the harmless phase from the shift 2.2. This bound is for the **normalized conditional rest vectors**, not a bound on all possible clock instruments or on a continuum-gravity approximation. For any bounded rest observable O, the associated expectation-value difference is at most `|t|δ ||O||`; the full conditional probability distributions of a fixed POVM differ in total variation by at most the vector bound.

For n=24, δ=0.02 and `|t|=2`, the bound is 0.02 and the computed vector error is approximately 0.01270. At t=1, refining δ to 0.01 reduces the vector error from 0.00635 to 0.00282. This is a constructive finite-model approximation; spectral rounding does not become a physically local interaction simply because the conditional vectors are close.

## 4. Opposite memory arrows, same geometry and same energy ledger

At the turning boundary t=0 choose oscillator coherent state `α=+1.4`, `D=M¹=M²=0`, and equal amplitudes for the actual sphere states. Compare the same preparations as before:

```text
seeded:  (|Ψ₀⟩|0⟩_B + i|Ψ₁⟩|1⟩_B)/√2,
blank:   (|Ψ₀⟩|0⟩_B + i|Ψ₁⟩|0⟩_B)/√2.
```

All other factors, H_δ and H_C are the same. The h-controlled B rotation carrying blank to seeded commutes with H, hence with H_δ. It follows that the two constructions have identical clock energy weights, identical clock marginals, and **identical conditional reduced geometry density matrices** at every t. They differ in h–B correlations. The selected antiunitary symmetry of the underlying model is preserved by spectral rounding; the table is the same at ±t. The maximum and monotonic behavior are established on the stated sampled interval, not globally for all times.

For n=24, δ=0.02:

| `|t|` | `⟨A⟩`, both | `I(h:B_z)` seeded | `I(h:B_z)` blank | `S(B)` seeded | `S(B)` blank | `S(geometry)`, both |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1.852377 | 1.000000 | 0 | 1.000000 | 0 | 0 |
| 1 | 1.409946 | 0.836845 | 0.029874 | 0.965888 | 0.129066 | 0.062498 |
| 2 | 0.802639 | 0.652774 | 0.089652 | 0.889252 | 0.282553 | 0.209123 |

Numbers are bits except the scale. Approaching t=0 from either side, the seeded memory's correlation increases and the blank memory's decreases. Geometry entropy goes the other way for both. This is a comparison of specified readout and reduced-state diagnostics, not a derivation of thermodynamic entropy production or a claim that the memory forms itself at the maximum. The seed is an explicit boundary correlation; it is exactly what a complete zero-constitution law would need to explain.

The geometry is quantum and its scale is an expectation value. It is not a sharp measurement of scale, a globally monotonic geometric clock, or a 4D FRW solution. The matching clock POVM is an additional clock, not a proof that any clock choice gives equivalent conditional observables.

## 5. A stronger coherence control: identical marginal states, different geometry history

Using the **same seeded boundary and energy operators**, compare the pure zero-energy whole with its dephasing in the clock energy basis:

```text
ρ_coh = |Ω⟩⟨Ω|,
ρ_deph = Σ_k |k⟩⟨k| ⊗ |v_k⟩⟨v_k|.
```

Both are supported in the zero eigenspace. Because the `v_k` are orthogonal, tracing out R gives the same clock state `Σ_k ||v_k||² |k⟩⟨k|` in both cases. Tracing out C gives the same rest state `Σ_k |v_k⟩⟨v_k|` in both cases. Both have uniform clock-reading distributions. But the **conditioned rest state** differs:

```text
ρ_R|t (coh)  = |ψ_δ(t)⟩⟨ψ_δ(t)|,
ρ_R|t (deph) = Σ_k |v_k⟩⟨v_k|, independent of t.
```

At the same cutoff and δ, the dephased state has `⟨A⟩≈1.114608`, `I(h:B_z)≈0.311278` bits and `S(geometry)≈2.468676` bits at **every** clock reading. Compare the changing coherent values in the table. The dephased memory can have a static h/B correlation; the point is that it does not form the same conditional history.

This is not an assertion that an actually measured clock dephased itself, nor that a particular external agent created the mixture. It compares two rigorously specified whole density operators. It shows that even the full geometry-plus-memory **rest marginal**, not merely its geometry reduction, does not fix conditional recollapse: the clock/rest correlations matter. This is exactly the issue anticipated by the Lighthouse's distinctions between state, interface and duration, adapted here to a whole whose declared energy is zero.

## 6. The sphere–experience constraint still applies

The code contracts the clock-conditioned state with the actual five-ray vectors. For both boundary preparations at t=0,1,2, the reduced record pair R and B factor:

```text
ρ_(R₁R₂,B) = ½(|01⟩⟨01|+|10⟩⟨10|) ⊗ ρ_B.
```

So B can access the richer h relation without the confined record subsystem automatically accessing it. In the seeded case at `|t|=1`, `Pr(h=1,B=1)≈0.470761`, and the event `r=+1,B=1` has probability approximately `0.235380`. On that h=1 event, the earlier conditional R- and J-probe experience proposals assign opposite signs to the same candidate pair, despite both summing to zero under their stipulated equal-incidence assumptions. J₁ is the earlier defined probe, not automatically the full present Hamiltonian's physical current.

An energy cancellation, or even an exact record of h, therefore does not select a phenomenal sign, define an actual subject, or prove an experiential sum. A physical interface from the full constrained interaction and a justified law of incidence are still needed. A locally negative felt experience would remain real regardless of a whole-level cancellation; it is not absence and is not erased by a positive contribution. No claim is made that the qubits feel, that a result is selected, or that inaccessible richer-domain activity is registered by a confined inhabitant.

## 7. What this establishes for the zero proposal

We now have a single, reproducible finite system in which **exact total-energy cancellation, nontrivial internal geometry, changing clock-conditioned records and the actual sphere code coexist**. This is genuine compatibility, not merely a restatement that zero can contain opposites. It also identifies the structure that must be made necessary: the spectral match, the energy-zero reference, the complete whole-state coherence, the boundary correlation, the scale, the clock and the subject interface.

The construction does not establish that these inputs follow from zero itself. In particular:

* The negative term is a deliberately chosen contribution to H_total, not independently measured gravitational energy; ordinary matter positivity and a covariant whole-energy recovery map remain to be shown. Adding a constant to a Hamiltonian can be a conventional energy shift unless a physical reference is specified.
* The mirrored clock, Fock cutoff, rounding spacing, initial coherent geometry and state are chosen. The spectral rounding changes the interaction and need not preserve spatial locality. Finite-dimensional boundedness does not resolve possible instabilities if an unbounded negative sector is extrapolated.
* `H_total=0` can be regarded as a constraint, but a vanishing constraint is not automatically the objective energy of an actual universe. Relational clock covariance, Lorentz invariance, 4D gravity, Born outcomes, experiential incidence and a globally justified signed valence are not derived.
* The coherent and dephased states show underdetermination by these **specific physical inputs**; they do not refute the user's claim that the genuinely possible and actual coincide or that a deeper self-sufficient zero constitution fixes one complete history.

The most consequential continuation is not another arbitrarily matched clock: find a physical, covariant principle that derives the energy matching **and the whole-state correlation** while recovering local energy and the relevant subject interfaces. The coherence/dephasing pair above is a concrete test: any proposed principle must explain why its predicted conditional geometry and record structure obtains rather than leaving those relations as ungrounded inputs.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_energy_recollapse_clock_test -v
```

The verification checks all occupied rounded spectral bins against their matched energies, the clock POVM normalization, the analytic rounding bound for both preparations at selected times, Fock cutoffs n=24 and 32 at δ=0.02, the two boundary arrows, actual five-ray record/B contractions and the dephased control. Fock refinement at fixed δ is numerical evidence, not a certified continuum limit. The exact matching, positivity bound, clock normalization and phase-error inequality are finite-model analytical statements; they do not establish a gravitational energy theorem or actual experience.
