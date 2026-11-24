# Recollapse, the sphere and record arrows in one constraint

## Result

We can now put **a dynamical recollapsing geometry, the actual five-ray sphere code and four autonomous detector/memory qubits in one constrained quantum model**. This is a new oscillator-geometry model, not a derivation of general relativity or a solution of Fukuyama's JT model. It replaces the geometry operator and clock constraint of the [earlier autonomous model](ZERO_INTEGRATED_SPHERE_AUTONOMOUS_INCIDENCE.md), while retaining its actual sphere states, K relation, detector, three memories and the same *forms* of their targeted and windowed couplings.

The main result is sharper than the previous disconnected toy:

* At the same turning-point boundary and with **the same Hamiltonian and exactly the same reduced geometry state at all clock readings**, two explicit preparations give opposite arrows for the B-memory's entropy and its correlation with the conserved sphere relation h. One has a perfectly correlated memory at maximum expansion; the other has a blank memory there. On the sampled intervals, correlation and B entropy increase **toward** the maximum in the first, but **away** from it in the second.
* Meanwhile the geometry's reduced entropy increases **away** from that maximum in both cases. There is no single arrow here until the subsystem, diagnostic, state and orientation are specified.
* A separate, initially uncorrelated preparation gives an expanding and a contracting reading at the **same mean scale** with very different memory information. For `⟨a⟩=1.1`, `I(h:B_z)` is about `0.00869` bits on expansion and `0.25822` bits on contraction. A scale reading alone does not specify a branch or memory state.
* A sequential B-readout calculation explicitly includes measurement backaction. It establishes finite-interval agreement, not a permanent record: measuring at t=−1 changes the unmeasured B distribution at the turning point by about 0.0532.

This makes the boundary-condition issue constructive: **the same physical geometry history does not select one record-arrow direction**. The first preparation intentionally *puts* the h–B correlation at the turn; we have not derived it from zero or claimed that qubits feel. The calculation identifies what a proposed zero-constitution law would have to determine rather than calling an arbitrary boundary condition self-explanatory.

## 1. One autonomous constraint

Use the actual orthonormal code states `|Ψ₀⟩, |Ψ₁⟩=Z_work-M₁|Ψ₀⟩` and the same operator

```text
K=Z_R₁ J₁,                h=(P_act−K)/2,
h|Ψ_h⟩=h|Ψ_h⟩,            h=0,1.
```

Their asymmetric conservation-derived five-ray state, the i/r table and the meaning of the J₁ probe are as in the [integrated sphere report](ZERO_INTEGRATED_SPHERE_AUTONOMOUS_INCIDENCE.md). The original Pauli-support and reporting limitations are in [the full-constraint boundary analysis](ZERO_SUBJECT_BOUNDARY_REPORT_CAUSALITY.md).

Introduce a geometry oscillator, with `Q=(b+b†)/√2`, `N=b†b`, and a positive scale observable

```text
A=exp(0.3 Q),       W_c=exp[−(Q−c)²/(2×0.7²)].
```

Its finite-truncation operator construction and all numerical tests use the same Q matrix to define A and the windows by spectral calculus. Let D be the detector, M¹,M² its two earlier memories and B the K-targeted memory, `P₁ᴰ=|1⟩⟨1|`. The **single** ideal-clock constraint is

```text
C = p_T + H = 0,
H = N + h
    + 0.5 W_(−1) Y_D
    + 0.65 W_0 P₁ᴰ Y_M¹
    + 0.65 W_1 P₁ᴰ Y_M²
    + 0.4 W_1 h Y_B.
```

The constraint is autonomous: no term depends explicitly on T. H is self-adjoint in each finite truncation, and `[h,H]=0`. Formally, on the corresponding ideal clock history `p_T=−i∂_T` and `|ψ(T)⟩=e^(−iHT)|ψ(0)⟩`, so `Cψ=0`. The usual reduced-system inner product is used for the deparametrized calculation. This ideal clock has generalized, non-normalizable clock states; a normalizable finite-resolution clock and a physical geometry-clock measurement are **not** constructed here. The linear constraint is not the old quadratic scalar-clock constraint, and its earlier positivity or slice-reconstruction theorems are not automatically transferred.

The geometry is dynamical, not a separately stipulated curve. The window functions act on Q and the interaction changes its motion. For example, from an oscillator coherent state with `α=−1.4` at T=0, the computed `⟨Q⟩` at T=2.2 is approximately `1.01230`; with all four interactions switched off but the same initial state it is `1.16517`. The same A is positive in the finite model. We call it a *scale observable* by analogy: it is not derived as an FLRW metric, and its minima need not be singularities. The oscillator model oscillates and can recur, rather than automatically furnishing a big-bang-to-crunch spacetime.

## 2. Two preparations at the actual turning boundary

Set T=0 at a symmetric local maximum, and prepare geometry in the coherent state `|α=+1.4⟩`, D=M¹=M² in `|0⟩`, and sphere amplitudes `( |Ψ₀⟩+i|Ψ₁⟩ )/√2`. Compare two states **under the same H**:

```text
blank:   (|Ψ₀⟩|0⟩_B + i|Ψ₁⟩|0⟩_B)/√2
seeded:  (|Ψ₀⟩|0⟩_B + i|Ψ₁⟩|1⟩_B)/√2.
```

The other factors are the same. The h-conditioned rotation `V=(1−h)+h exp(−iπY_B/2)` maps blank to seeded and commutes with H on the active code. It is a joint h–B operation, not an operation on the confined record alone. Since the two orthogonal h sectors are traced when calculating geometry, and V acts only on B in each sector, **their geometry reduced density operators agree exactly at every T**. So do their geometry–D–M¹–M² reductions. This equality is structural, not just agreement of a few mean-scale numbers.

In the finite model the antiunitary `Z_D Z_M¹ Z_M² Z_B` followed by complex conjugation preserves H (with an appropriate conjugation in the sphere code basis). Each h sector of these preparations is invariant up to a phase. Therefore the joint h/B_z probabilities and both reduced entropies below are even in T. The selected local maximum and monotonicity over the tabulated interval are checked numerically, not asserted for all times. T is an internal clock reading, not an external absolute time or preferred foliation.

At Fock cutoff 32, with entropy and mutual information in bits:

| `|T|` | mean scale `⟨A⟩`, both | `I(h:B_z)` seeded | `I(h:B_z)` blank | `S(B)` seeded | `S(B)` blank | `S(geometry)`, both |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1.852377 | 1.000000 | 0 | 1.000000 | 0 | 0 |
| 1 | 1.410225 | 0.837281 | 0.029765 | 0.966081 | 0.128834 | 0.062462 |
| 2 | 0.802978 | 0.654216 | 0.089066 | 0.890016 | 0.281300 | 0.207621 |

For example, at `|T|=1` the seeded h/B_z table is

```text
              B=0          B=1
h=0           0.500000     0
h=1           0.029135     0.470865
```

For the blank state the h=1 row is reversed. The table is the distribution of **commuting h and B_z readouts at one time**, not an inserted earlier measurement. B=1 still certifies h=1 in both of these preparations, because h=0 has no B coupling and starts in B=0; however, B=0 misses h=1 with state-dependent probability. A separate B-rotated preparation changes even this specificity.

**Interpretation:** if one orients both branches toward T=0, the seeded B diagnostic rises toward maximum expansion, and the blank diagnostic falls. With orientation away from zero the signs reverse. But the geometry entropy rises away from the maximum for *both*. The seeded memory has not been shown to be formed as the maximum is approached: its initial correlation is explicitly specified at that boundary. Reversible unitary evolution makes a two-sided high-correlation boundary mathematically consistent, but does not explain why the whole has that boundary. In particular, symmetry, zero constraint and identical geometry density do not by themselves make the arrow unique.

## 3. Same mean scale, different branches and memory

Now use a different preparation at T=0: `α=−1.4`, `D=|+y⟩`, both M's and B zero, with the same equal-prior sphere superposition. This matches the earlier integrated model's **internal detector and memory preparation**, while the geometry dynamics is new. The mean scale starts small, rises to a local maximum near T=3.2258 (`⟨A⟩≈1.84936`) and later falls. The maximum's shift relative to the free-oscillator π is another consequence of coupling.

At the two numerically located readings with mean scale 1.1:

| branch | T | `d⟨A⟩/dT` | `I(h:B_z)` bits | `S(B)` bits | `S(geometry)` bits |
|---|---:|---:|---:|---:|---:|
| expansion | 1.76647 | +0.64175 | 0.008690 | 0.058479 | 0.302983 |
| contraction | 4.72274 | −0.60104 | 0.258223 | 0.578143 | 0.670163 |

The respective h/B_z joint tables are approximately

```text
expansion                  contraction
          B=0      B=1                B=0      B=1
h=0       0.50000  0                  0.50000  0
h=1       0.49136  0.00864            0.28486  0.21514
```

The same mean scale does not fix the state of the memory. Branch-labelled maps `T→⟨A⟩` are locally invertible wherever their derivative is nonzero, but they cease to be valid at the turning point. Relabelling a state with a decreasing scale coordinate cannot itself reverse the physical sequence of readouts: e.g. on contraction the coordinate derivative of a quantity has the opposite sign to its T derivative.

**Clock limitation:** this is a comparison at equal expectation values, not projection onto an exact quantum scale eigenvalue. The scale distributions have standard deviations about 0.2706 and 0.3173 at those readings; their full scale-readout distributions also differ (total variation ≈0.1157 at cutoff 32). Therefore we cannot treat the mean as a sharp clock, claim that both branches occupy the same full geometric state, or infer a probability law conditioned on an actual quantum A measurement. A branch-resolving instrument would require an explicit measurement and treatment of its disturbance. Our T clock is well-defined across the mean-scale maximum but is an idealized deparametrization, not a proof of a universal clock.

## 4. Does the memory persist when read twice?

For the seeded turning-boundary preparation, explicitly measure B_z at T=−1, project, evolve each outcome under the **same H**, and measure B_z at T=0. Tracing h gives the two-time table

```text
                 second B=0    second B=1
first B=0        0.526576      0.002559
first B=1        0.026576      0.444290
```

The two readings agree with probability about `0.970865`; the first reading is therefore predictive over this specified interval. But the first measurement is invasive: after it, the probability of B=1 at T=0 is `0.446849`, rather than `0.5` in the unmeasured history. The unmeasured T=−1 and T=0 tables in §2 cannot simply be multiplied or interpreted as this sequential experiment. The result is interval- and instrument-specific, not an irreversible record, a continuously existing classical fact, or evidence of an experiencer.

## 5. What happens to the sphere and the proposed experience bridge?

The test contracts the actual five-ray states with the full geometry/D/M¹/M²/B amplitudes. In the protected code, at the checked readings the **full reduced record-pair/B state factors** as

```text
ρ_(R₁R₂,B) = ½(|01⟩⟨01|+|10⟩⟨10|) ⊗ ρ_B.
```

The factorization follows from the sphere-code partial traces and the h-controlled apparatus evolution; the test checks the actual full vector, including the seeded state. Thus a strong B correlation with the *joint* record–work operator K does not make B accessible to the confined record subsystem. This preserves the room/surface distinction rather than allowing an inhabitant to register a richer-domain interface merely because it exists.

At `|T|=1` in the seeded preparation, the event `r=+1,B=1` has probability about `0.235433`; it implies h=1 in this model. On that event the prior conditional proposals give record rule `( +κ,−κ )` and J-probe rule `( −κ,+κ )` for the two candidate subjects. Both cancel only under their specified equal-incidence and common-scale assumptions; they assign the signs oppositely. This comparison uses J₁ as the earlier **specified probe**, not necessarily the physical current generated by the present H. The mismatch-only candidate and the local-report objection from the full-constraint report remain relevant.

Consequently, even adding a dynamical turning geometry and a two-sided record profile does not select between these proposed physical–experiential relations. In the strict local-report setting, the R-only subsystem still cannot distinguish the two code states; a reliable report of the J-rule needs a richer physical interface or a revision of the locality assumptions. There is no claim of actual reports, subjects, phenomenal valence, spacelike embedding or faster-than-light signalling. In particular, a hypothetical globally balanced signed experiential sum would not erase any local suffering.

## 6. What the construction establishes—and what would advance it

The result is an explicit **compatibility and underdetermination test within one chosen physical model**. The seeded and blank preparations are formal candidate states, not a claim that both are genuinely possible or actual under the user's necessitarian thesis. That thesis could select a unique complete state for reasons not represented by this constraint. Conversely, merely asserting that selection does not calculate it. Here the geometrical reduced state and the dynamics demonstrably do not determine the h–B boundary relation; a constitutive rule would need to supply it or derive it from a more complete whole.

This construction also distinguishes three proposed arrows: geometry entropy, a specific h/B readout correlation, and B entropy. Their different behavior shows why Fukuyama's coherence-width arrow cannot automatically be identified with memory or experience. It does **not** replicate Fukuyama–Morikawa's influence functional or establish a four-dimensional arrow theorem. There is no derivation of the sphere, the couplings, the initial state, a Born rule, subject incidence, signed experiential weights or objective whole-energy cancellation from zero. `C=0` is a gauge constraint, not itself a whole-energy ledger.

A consequential next step is to replace the hand-prepared h–B turning correlation by a boundary relation derived from a proposed *whole-state constitutive principle*, then see whether the full-coupling subject-boundary and local-report constraints select an experiential relation. A candidate must produce the geometry, records, incidences and signed sum together, and show how it preserves nonzero local suffering—not merely match this toy's chosen expectation curve. If it selects a unique state, it must also explain outcome/self-location probabilities without calling fixed outcomes irreducibly random.

## Reproduction and accuracy

```sh
python -m pip install --target .arena/python-deps numpy  # if necessary
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_recollapse_sphere_memory_test -v
```

The tests use exact diagonalization in the eight conserved `(Y_M¹,Y_M²,Y_B)` channels for each h sector, check the constraint differential equation against finite differences, unit norm, time-reversal symmetry, backreaction, actual sphere-vector contractions, same-scale branch matching, boundary controls and sequential projective measurement. Cutoffs 24 and 32 agree within `2×10⁻⁵` for the stated observables at the selected times; this is convergence evidence, not a certified continuum error bound. Entropies are von Neumann entropies of the specified reduced subsystems; `I(h:B_z)` is classical mutual information for the two specified readouts, not entropy production or a proof of thermodynamic irreversibility.
