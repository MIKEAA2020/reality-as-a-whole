# Complete cutoff-to-continuum instrument: a restricted common-space result

## Result

For the **specified one-dimensional even-cosine free-field model**, the cutoff source and ideal sign-readout instruments can be put on one common infinite-mode Fock space and compared directly with a specified continuum instrument. Under a common **normal-ordered oscillator-energy bound**, both source/readout orders converge to their continuum counterparts in an unhalved energy-constrained channel norm. The bound includes the retained field, both noisy record bits, every subnormalized outcome and arbitrary entanglement with a reference.

This is a substantive step beyond the earlier [finite-cutoff order comparison](CUTOFF_INSTRUMENT_UNIFORMITY.md): the two sides now have the **same input and output space**, and each cutoff instrument is compared to a continuum instrument. It is **not** a proof for the earlier kinetic-only energy class, a physically implemented probe, 3+1-dimensional QFT, gravitational backreaction, emergent spacetime or the whole framework. The proof uses standard bosonic field, Sobolev and channel estimates; energy-constrained channel metrics and their limitations are established work, e.g. [1](https://arxiv.org/abs/1706.00361) and [2](https://arxiv.org/abs/1712.10267).

A key issue is that an ideal sharp Lüders measurement can produce an output with **infinite total energy**. The measurement-first estimate below avoids assuming otherwise: the cutoff measurement acts on low modes only, and its nonselective operation preserves the energy in the untouched high modes. The full physical cost of performing that ideal measurement remains unmodeled. A subsequent [finite-strength pointer control](FINITE_STRENGTH_POINTER_CONTINUUM_GATE.md) has a finite calculable nonselective field-energy cost, but is a different instrument and still not a constructed physical spacetime probe.

## 1. Common model and constraint

Use the same even-cosine, equal-slice model, normalized triangular source `f` centered at zero and readout `h` centered at `π/2`, half-width `d=0.4`, as in [the original cutoff test](CROSS_FRAMEWORK_CAUSALITY_RECORD_TEST.md). The even extensions of the two supports are disjoint. Let

```text
w_n = sinc²(n d/2),
f_0 = h_0 = 1/√(2π),
f_n = w_n/√π,                h_n = w_n cos(nπ/2)/√π,  n≥1.
```

On the bosonic Fock space over the countable mode basis define canonical `q_n,p_n`, with frequencies `ω_0=1/2` and `ω_n=n` for `n≥1`. Impose the **one common positive energy**

```text
H = Σ_{n≥0} ω_n a†_n a_n,    Tr(ρ H) ≤ E,
q_n=(a_n+a†_n)/√(2ω_n),    p_n=i√(ω_n/2)(a†_n−a_n).
```

The zero-mode oscillator is an explicit infrared/energy-constraint regulator. Its vacuum has `Var(q_0)=1`, `Var(p_0)=1/4`, matching the previously specified Gaussian preparation. But this bound is **not** identical to the previous kinetic-only constraint: it adds a zero-mode confining term and normal-orders the infinite-mode energy. The new energy class is an additional assumption, not a demonstrated equivalence of domains or a complete physical energy budget. **Subsequent correction:** if this oscillator energy is also used as the dynamical Hamiltonian while the nonzero modes remain massless, it produces a spatially global zero-mode restoring force. The [smooth-switching test](SMOOTH_SWITCHING_ZERO_MODE_LOCALITY_GATE.md) finds an explicit nonzero spacelike commutator. The equal-slice results here remain valid, but must not be generalized to local spacetime evolution under this regulator.

On this common space, finite-mode operators act as the identity on the tail:

```text
Q_N = Σ_{0≤n≤N} h_n q_n,       P_N = Σ_{0≤n≤N} f_n p_n,
Q   = Σ_{n≥0} h_n q_n,         P   = Σ_{n≥0} f_n p_n,
U_N = exp(−i g P_N),           U = exp(−i g P).
```

The coefficient bounds below give the standard Fock-space field operators and their Weyl unitaries on the finite-particle core and by closure. The disjoint even smear supports imply `[Q,P]=0` on the common core, with commuting Weyl operators. This is the equal-time continuum statement in this model, not a full local-spacetime measurement construction.

Let `J_N` and `J` be the complete sign-measurement instruments of `Q_N` and `Q`: retain the field, record the sign in two classical bits, and independently flip each bit with the same fixed probability as before. The measurement has its ideal Lüders update. The four subnormalized outcome maps sum to a channel; the common record Hilbert space is four-dimensional. We compare

```text
source first:       J_N ∘ Ad(U_N)     vs     J ∘ Ad(U),
measurement first:  Ad(U_N) ∘ J_N     vs     Ad(U) ∘ J.
```

Each output includes the **entire infinite field**, not a discarded or vacuum-replaced tail. The norm below is the supremum of output trace distance over input field–reference states with field energy at most E, with no reference-energy bound. The term “diamond” here describes that explicit energy-constrained supremum; it does not invoke a compact-spectrum theorem. `H` has a legitimate Fock vacuum with zero energy, unlike the divergent sum of the unrenormalized infinitely many kinetic zero-point energies.

## 2. Measurement comparison

Set

```text
B₀ = 1/(2π),
Cₕ = ω₀ B₀ + Σ_{n≥1} ω_n h_n²
   ≤ ω₀ B₀ + 24/(πd⁴),
A_N = 16/(5πd⁴N⁵),       T_N = 4/(πd⁴N⁴),
M(E) = √(2E/B₀) + √(Cₕ/(2B₀²)),
D_N(E) = 4E A_N + T_N.
```

The two tail estimates are `Σ_{n>N} h_n²/ω_n² ≤ A_N` and `Σ_{n>N} h_n²/ω_n ≤ T_N`. They use `|w_n|≤4/(n²d²)` and the integral test; the upper bound for `Cₕ` uses `Σn⁻³≤3/2`. These are loose, but finite and explicit.

For any normalized joint field–reference vector with field energy at most E, standard creation/annihilation bounds give

```text
||(Q−Q_N)ψ||² ≤ D_N(E),
||P_h,N ψ|| ≤ M(E),
P_h,N := (Σ_{n≤N} h_n p_n)/(Σ_{n≤N} h_n²),   [Q_N,P_h,N]=i.
```

To see the first bound, the two relevant one-particle norms are `Σtail h_n²/ω_n²` and `Σtail h_n²/ω_n`; applying the annihilation and creation estimates and `(a+b)²≤2a²+2b²` yields the displayed constants. The second uses `Σ_{n≤N}h_n²≥B₀` and `Σ_{n≤N}ω_n h_n²≤Cₕ`. These statements hold with all other field modes and the arbitrary reference carried along.

`Q_N` and `Q−Q_N` strongly commute. For a positive threshold `t`, the sign projections of `Q_N` and `Q` can differ only when `|Q_N|≤t` or `|Q−Q_N|≥t`. The vector-valued one-dimensional Sobolev estimate and Markov's inequality yield

```text
Pr(sign differs) ≤ 4t M(E) + D_N(E)/t².
```

At `t=(D_N(E)/(2M(E)))^(1/3)`, this is at most `R_N(E)=3(4M(E)²D_N(E))^(1/3)`, capped at one. For the two complementary ideal projections, the difference of their outcome isometries has squared norm twice the sign-disagreement probability. Trace-distance contraction under dephasing and bit-flip noise gives the **complete instrument** bound

```text
||J_N − J||_{⋄,E} ≤ Jbound_N(E)
Jbound_N(E) := min{2, 2√[2 min{1, R_N(E)}]} = O(N^(−2/3)).
```

This bound includes arbitrary reference entanglement and the field's post-measurement state, not just probabilities in the vacuum. It does not bound an unnormalized output's **energy** after a sharp measurement.

## 3. Source comparison and the two orders

Define

```text
F_N = 16/(3πd⁴N³),       G_N = 8/(πd⁴N²),
Sbound_N(E) = min{2, 2|g|[√(2E F_N)+√(G_N/2)]}.
```

Here `Σtail f_n²≤F_N` and `Σtail ω_n f_n²≤G_N`. The same bosonic estimates and `|| (e^(−igX)−I)ψ ||≤|g| ||Xψ||` give

```text
||Ad(U_N) − Ad(U)||_{⋄,E} ≤ Sbound_N(E) = O(N⁻¹).
```

The source's coherent displacement has energy

```text
E_src = g²/2 Σ_{n≥0} ω_n² f_n² = g²(1/d³ + 1/(16π)).
```

The nonzero-mode identity follows from Parseval for the declared triangular function. The zero-mode term reflects the **new** oscillator regulator. The source-transformed input is bounded by

```text
E⁺ = (√E + √E_src)².
```

Consequently, telescoping the source-first comparison on the common space gives

```text
||J_N∘Ad(U_N) − J∘Ad(U)||_{⋄,E}
    ≤ min{2, Sbound_N(E) + Jbound_N(E⁺)}.
```

For the measurement-first comparison, telescope using `J_N` as the intermediate measurement. Although its total output energy may be infinite, its spectral projections act only on modes `≤N` and commute with the **tail** Hamiltonian. Summing all ideal outcomes—and then adding the classical noise—leaves expected tail energy no greater than the input E. Thus the source-tail estimate still applies to the joint field, record and reference, giving

```text
||Ad(U_N)∘J_N − Ad(U)∘J||_{⋄,E}
    ≤ min{2, Sbound_N(E) + Jbound_N(E)}.
```

Both right sides vanish at fixed finite E. Since the continuum source and readout commute in this particular equal-slice disjoint-smear model, the two continuum ordered instruments agree. This is a common-space convergence result for **both complete ordered instruments**, not a gravitational refoliation theorem.

Each individual subnormalized outcome and the nonselective field channel inherit the bound by postprocessing. Normalized conditional states need a separate positive lower bound on the corresponding outcome probability: if one relevant probability is at least `λ>0` and its subnormalized trace-distance error is at most `η`, a `2η/λ` upper bound follows for the normalized states when both are defined.

## 4. Numerical controls and scope

For `E=100`, `g=1`, and the illustrative unhalved norm target `.01`, the conservative formulas give **N=459,854** for both order bounds; at N−1 the source-first bound is just above `.01`. This is a sufficient integer for these **loose inequalities**, not a physical cutoff requirement or proof that smaller N fails the true criterion. `E⁺≈194.752` in these model units. The corresponding bound changes the energy constraint from the earlier finite-N kinetic-only calculation, so its numerical N cannot be read as a direct revision of the earlier N=722 order-comparison number.

The [verifier](verification/continuum_complete_instrument_bound.py) checks coefficient majorants, the explicit zero-mode source-energy term, the two bounds and cutoff arithmetic. As nontrivial controls it compares the ideal complete sign instruments for the original Gaussian vacuum at N and finite M=20,000: commuting Gaussian sign correlations give their exact vacuum classical–quantum output trace distance, which is below the analytic bound for the listed N. It also checks the source-tail bound against the exact coherent-vacuum overlap. Finite-M numerical checks do **not** prove the all-state infinite-mode inequalities; the reasoning above provides that conditional argument.

## 5. Remaining gates

- This idealized **even-cosine 1D free field** is not the 3+1 covariant probe instrument of [Fewster and Verch](https://arxiv.org/abs/1810.06512), nor a detector with compact spacetime coupling, a clock or realistic readout hardware. Triangular smears are not smooth; no stress tensor renormalization or full apparatus/switching cost is included.
- The normal-ordered oscillator-energy constraint and zero-mode regulator are explicit additional inputs. We have not proved convergence for the entire earlier kinetic-only class, and an ideal sharp measurement can carry infinite output energy.
- No metric dynamics, gravitational constraint algebra, backreaction estimate or continuum Einstein evolution is derived. Equal-slice commutation is not a refoliation test.
- No subject, quality, necessary actuality or experiential truthmaking follows. The battery's broad B6–B8 and other framework gates remain open, though the common-space L3 **subproblem passes in this restricted model** under the stated constraint.
