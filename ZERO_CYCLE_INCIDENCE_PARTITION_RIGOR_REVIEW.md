# Autonomous cycle: normalized incidence, current and balance

## Result

This pass rechecks and strengthens the [autonomous record-cycle incidence example](ZERO_AUTONOMOUS_RECORD_CYCLE_SUBJECT_INCIDENCE.md), using the **same encoded writer, clock and memory–battery energy**. Physical pair currents obey the exact identity `J_M+J_W=0`, and every subsystem returns to its initial energy at the end of the prepared cycle. Nevertheless, one can choose two **strictly positive, complementary incidence effects**

```text
0<W_M<I,       0<W_W<I,       W_M+W_W=I,
```

that commute with the actual full pair current and still give a nonzero integrated incidence-weighted current. Thus positivity, completeness of the two tags, pair-energy conservation, a closed cycle and compatibility with a sharp current measurement are jointly insufficient to force weighted cancellation.

Conversely, other unequal complementary effects can cancel the weighted current exactly. The precise condition is an **anticommutator** equation, not equality of the weights. In the constructed cancelling example those effects do not commute with the sharp current, so its symmetrized operator should not be represented as an ordinary joint sharp-current/incidence measurement without a further instrument.

This is a conditional finite quantum construction. The incidence effects are engineered **joint clock–work operators**: they have not been shown to be local subjects, experiential occurrences or the physical–experiential identity. A complete normalized tag POVM is not a census of genuinely simultaneous subjects. Nonzero expectation of a signed current is not an observed feeling and does not disprove the proposed zero constitution. Space and time remain non-fundamental constructs; the cycle parameter is an effective description, not a fundamental external time or a derivation of experienced succession.

## 1. The original history and a general product rule

The source fixes a prepared encoded work state `|φ⟩`, a work-energy conserving writer U, and

```text
V₀=V₃=I, V₁=V₂=U,
K=Σ_t |t⟩⟨t|⊗V_t,
H=H₀+K(A⊗I)K†,       [U,H₀]=0,
P=|1⟩⟨1|+|2⟩⟨2|,    D=i[A,P],    D²=I.
```

A is the four-cycle adjacency and the coupling and ħ are one. In the invariant history span `|h_t⟩=K(|t⟩⊗|φ⟩)`, for memory j,

```text
E_M = pP,       E_W = I−pP,
J_M = pD,       J_W = −pD,
p₁=3/5,         p₂=7/8.
```

These are compressions of the full operators, and p is a Born-weighted expectation fixed by the earlier pointer preparation. Compression need not preserve spectral values or measurement instruments; the full-current calculation below avoids using `pD` as though it were automatically the actual full current's sharp measurement.

For any finite system, Hermitian energies E_a, weights W_a(t) and Hamiltonian H, define `J_a=∂_t E_a+i[H,E_a]` and the Heisenberg/material derivative `D_t W_a=∂_tW_a+i[H,W_a]`. Direct differentiation gives the quantum weighted product rule

```text
d/dt Σ_a ⟨{W_a,E_a}/2⟩
 = Σ_a ⟨{W_a,J_a}/2⟩ + Σ_a ⟨{D_t W_a,E_a}/2⟩.
```

It holds for differentiable bounded operators and the specified unitary evolution. A closed boundary term does not eliminate the second, incidence-transport term. Even Schrödinger-picture **constant** W can have nonzero material derivative when `[H,W]≠0`. This is the operator counterpart of the earlier effective-field transport correction; neither expression identifies W with an actual subject.

## 2. A normalized, compatible nonzero example on the full encoded space

Choose `0<λ<1` and define on the **full clock–work space**

```text
W_M = K[((I+λD)/2)⊗I_work]K†,
W_W = K[((I−λD)/2)⊗I_work]K†.
```

Their spectra lie in `[(1−λ)/2,(1+λ)/2]`, so both are strict effects and sum to identity. They are not stipulated to be subject-local.

Let E be the **full** memory energy and set `Δ=U†EU−E` on the encoded work space. In the K-transformed representation, `K†EK=diag(E,U†EU,U†EU,E)`. Since the writer conserves H₀ and each pair's total bare energy,

```text
K† J_M K = D⊗Δ,       K† J_W K = −D⊗Δ,
[W_M,J_M]=[W_W,J_M]=0,
{W_M,J_M}/2 + {W_W,J_W}/2 = λ K(I⊗Δ)K†.       (1)
```

Equation (1) is an operator identity on the full stipulated encoded space, not only a compression. Δ need not be positive there. In the **prepared** state, however, `⟨φ|Δ|φ⟩=p`. The K-frame evolution factorizes into the clock cycle and a common work phase because `H₀|φ⟩=2|φ⟩`. Therefore for every effective time t

```text
⟨{W_M,J_M}/2 + {W_W,J_W}/2⟩_t = λp,
∫₀^π dt ⟨{W_M,J_M}/2 + {W_W,J_W}/2⟩ = λpπ.
```

For λ=1/2, the first pair gives `3π/10`; the second gives `7π/16`. Unweighted pair current is identically zero, and each pair member's unweighted integrated current is zero. The [checks](verification/zero_cycle_incidence_partition_review_test.py) reconstruct the actual encoded U, H₀, both memory energies and the history vectors; they verify (1) on sampled full-space vectors as well as the exact four-clock identities. The general factorization above is the proof; sampling is not.

Since W_M and W_W commute with J_M, a joint POVM exists: combine the two effect tags with the spectral PVM of the **actual full** J_M. The value assigned to a memory tag is its measured current and to a battery tag the opposite current. Its mean is the left-hand side of (1). In the compressed history model one may also inspect the simpler `pD` current and its two eigenvalues, but that compressed measurement is not assumed identical to the full current PVM. Measurements at separate t values can be estimated on separately prepared copies; repeatedly measuring the system throughout a single cycle would generally disturb the evolution.

## 3. Where the cycle's missing term goes

For the normalized effects above, their compressions are `(I±λD)/2`. On the four-history space,

```text
D_t W_M = λ(I−2P),        D_t W_W = −λ(I−2P),
Σ_a ⟨{W_a,J_a}/2⟩ = λp,
Σ_a ⟨{D_tW_a,E_a}/2⟩ = λ⟨−I+2(1−p)P⟩.
```

Starting at clock label 0, `⟨P⟩_t=sin²t`; thus the transport term integrates to `−λpπ`, exactly canceling the nonzero weighted-current integral in the product rule. The weighted energy expectation at the two endpoints is the same. There is no violation of energy conservation: weighting and dynamics do not commute, and the current–incidence correlations supply the remainder.

This also clarifies the continuum energy-locked construction's scope: a transport condition can remove its own correction term only under its specified effective-field and boundary assumptions. Neither the continuum marker nor these clock–work effects is thereby shown to be actual experiential incidence.

## 4. Unequal weights that do cancel, and measurement compatibility

For any two opposite Hermitian currents `J_W=−J_M=−J` and complementary Hermitian effects `W_M+W_W=I`,

```text
{W_M,J}/2 + {W_W,−J}/2 = {2W_M−I,J}/2.
```

So weighted cancellation as an operator is **equivalent** to `{2W_M−I,J}=0`. Equal half-weights are sufficient, but not necessary if J has opposite spectral values. In the same encoded model, take

```text
W_M^phase = K[((I+η(2P−I))/2)⊗I]K†,
W_W^phase = I−W_M^phase,          0<η<1.
```

Because `{2P−I,D}=0` and `K†JK=D⊗Δ`, these unequal strict effects produce an exactly zero symmetrized weighted current **on the full encoded space**. They do not commute with the nonzero current. This is a structural alternative, not a phenomenological identification or an assertion that the realized system selects these weights.

There is a separate operational restriction: a sharp PVM for J can have a joint POVM with an effect W only if W commutes with J. Indeed each joint effect subordinate to a current spectral projection is supported in that projection, so the W marginal is block diagonal across all J eigenspaces. Hence the phase-effect cancellation above cannot be implemented as a joint measurement of those noncommuting effects with **sharp** current. Unsharp-current or different instruments may be possible but require their own analysis. The commuting nonzero example in §2 does have a joint POVM.

## 5. What follows and what remains

The results pinpoint a substantive constitutive gate: energy-conserving closed dynamics plus normalized, positive incidence is not enough; a theory needs the actual incidence/current compatibility and its physical–experiential meaning. Conversely, a formal nonzero weighted sum does not refute the user's self-sufficient zero proposal, whose actual constitution and admissible subject incidences are not specified by the toy. No claim is made that the source's batteries or tags are subjects, or that compensating values erase suffering.

Next examine whether any independently motivated subject-organizing degrees of freedom realize the required compatibility on a common physical carrier; connect the continuum transport/boundary condition with a quantum, constraint-compatible instrument; and establish real physical energy, effective spacetime, subject persistence and felt qualities. The encoded writer, record preparation, global K interaction and signed incidence assignment remain inputs, not a no-residue derivation.
