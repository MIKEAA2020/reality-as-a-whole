# A sphere, autonomous memories and competing experiential relations in one constraint

**Boundary continuation:** [higher-body coupling and report causality](ZERO_SUBJECT_BOUNDARY_REPORT_CAUSALITY.md) tests the full constraint's record–work interaction and the locality conditions on reporting the rival J-quality.

## Result

We can connect the previously separate five-ray sphere–record construction, its candidate subject pairs and current probe, and the autonomous geometry-clock apparatus **in one specified constrained quantum model**. The connection produces both a warning and a constructive correction.

1. The original two late memories share about **0.425 bits** with each other, but at φ=100 their mutual information with the sphere's record–current relation K is only about **0.00000012 bits**. They are good records of a different correlation, not automatically of the relation used by the proposed experiential bridges.
2. Adding a third, targeted memory B **inside the same autonomous constraint** gives `I(K:B)≈0.5831 bits` at φ=100. In this ideal model B=1 certifies K=−1, though it misses some K=−1 cases. It changes the other two memories' distribution, so the new record is not passive.
3. On the very same physically specified event, two candidate signed-experience rules assign **opposite qualities** to each of the two candidate subjects, while both pair totals are zero under equal-incidence assumptions. Thus even this stronger common system and conditional pairwise balance do not by themselves select the physical–experiential relation.

The result is an explicit physical model and a comparison of **conditional experiential hypotheses**, not evidence that qubits feel, that a readout is selected, or that all mathematical alternatives are genuinely possible. The mathematical and numerical details are in [sphere-clock verification](verification/zero_integrated_sphere_clock_experience_test.py) and [targeted-memory verification](verification/zero_integrated_targeted_memory_test.py).

## 1. The same sphere state and the same constrained clock

Start with the actual asymmetric five-ray construction in [one system](ZERO_SPHERE_CONSERVATION_RECORD_CURRENT_SINGLE_SYSTEM.md). The conservation-derived weights are `q=(1/8,2/5,19/40)` and the specified POVM, singlet, record interaction and work preparation give

| Sphere outcome i | record `01` (r=+1) | record `10` (r=−1) |
|---|---:|---:|
| 0 | 3/40 | 1/20 |
| 1 | 1/10 | 3/10 |
| 2 | 13/40 | 3/20 |

Let `J₁,J₂` be the two work-register observables defined as currents for the **standalone** exchange generator G in that construction. As operators, `J₂=−J₁`. Let `P_act` project onto its two-state active work sector and set

```text
K = Z_R₁ J₁,       h = (P_act−K)/2.
```

K is a Bob-lab operator on the first record and work factors, not an operator acting only on the candidate subject. On the active support, `K²=1` and h projects onto K=−1. Extend h by zero outside that support. The original state `|Ψ₀⟩` has K=+1; the physical Bob-local phase flip `Z_work-M₁` produces the orthogonal `|Ψ₁⟩` with K=−1. Both have exactly the same i,r table and the same candidate-subsystem reduced state. Their relative superposition is prepared here as

```text
(|Ψ₀⟩ + i|Ψ₁⟩)/√2,
```

which is the earlier h-superposition, now explicitly identified with the **actual five-ray state**, not an unrelated abstract two-level register. It can be obtained by the fixed Bob-local unitary `exp(iπ Z_work-M₁/4)` acting on `|Ψ₀⟩`.

On this support define the **single** rescaled constraint

```text
C̃ = p_φ²/2 − p²/12 + h
     + E_(−5) (0.5 σ_yᴰ)
     + E_0 (0.65 P₁ᴰ σ_yᴹ¹)
     + E_5 (0.65 P₁ᴰ σ_yᴹ² + 0.4 h σ_yᴮ),
Θ = p²/6 − 2h − 2[0.5 E_(−5)σ_yᴰ
     + 0.65 E_0 P₁ᴰσ_yᴹ¹ + 0.65 E_5 P₁ᴰσ_yᴹ²
     + 0.4 E_5 h σ_yᴮ],
p_φ=Ω=√Θ,                 U(φ)=exp(iφΩ).
```

Here `p∈(−7,−6)`, D is the earlier detector, M¹,M² its original two memories, and B the new targeted memory. They start as `|+y⟩_D|000⟩_(M¹M²B)` with the incident packet centered near α=−15. The window effects and the constraint are independent of φ. The targeted term uses the **joint physical projector h**, and hence explicitly couples B to a record–work relation; this is a chosen interface, not a consequence of confinement or zero.

A slightly sharper norm estimate than the sum of coupling magnitudes proves positivity. For the original detector/memory terms, the detector-block bound is

```text
M=[1.3+√(1.3²+1)]/2≈1.470061.
```

The new term adds at most 0.4. Because `T≥6` and `h≤1`,

```text
Θ ≥ 4−2(M+0.4) ≈ 0.259878 > 0.
```

Thus the positive branch is well-defined and closed unitary evolution includes B. The choice of constraint, projector, interactions, packet and preparation remains substantive input. A vanishing constraint is not automatically a proof of objective whole-energy zero.

**Current qualification:** J₁ is the operator which was a sharp work current for the original standalone generator G. It remains a well-defined conserved probe observable under the new Ω because it commutes with h and the remaining factors, but the actual full constrained current `i[Ω,N_work]` is generally a different operator. The experiential J-candidate below concerns this specified J-probe, not a demonstrated identity with the full clock current.

## 2. What the unmodified memories do—and miss

First set the B coupling to zero, retaining the original two-window model. K commutes with Θ, so an optional ideal K readout at a fixed scalar reading can be jointly compared with a memory-z readout; no intermediate measurement is inserted in the unmeasured evolution. The following N=80 results use the actual sphere-state identification above:

| Reading φ | `I(K:M²)` | `Pr(K=−1 | M²=1)` |
|---:|---:|---:|
| 30 | 0.024791 bits | 0.738962 |
| 100 | 0.000000117 bits | 0.499762 |

Yet at φ=100 `I(M¹:M²)≈0.424712` bits. The two original memories correlate with each other, but they almost fail to retain **which K relation** obtained in this preparation. The early correlation is finite and later largely disappears. This is a quantitative, model-specific result, not a claim that record correlations never encode K. The equal h priors and pointer input are specified choices.

The full confined record pair R and the complete detector/memory system are in a product reduced state for this encoded evolution. The sphere outcome i and record r joint table is also statistically independent of the unmeasured external memories. The tests contract the **actual five-ray amplitudes**, not an assumed independent record. Thus the two memories' changing state does not imply that the confined R subsystem registers it. A richer joint observable such as K nevertheless can correlate with the external memories, because K uses work degrees of freedom outside R.

## 3. An autonomous memory of the relation itself

Now use the `0.4 E_5 h σ_yᴮ` interaction. It is nondemolition for h: `[h,Θ]=0`, and B starts at zero. The h=0 sector never flips B; h=1 may flip it as the geometry packet interacts with E_5. This directly addresses the K relation rather than hoping the detector's memories happen to encode it.

At φ=100, the N=80 unmeasured state gives the joint readout table

| K / h | B=0 | B=1 |
|---|---:|---:|
| K=+1 / h=0 | 0.500000 | 0 |
| K=−1 / h=1 | 0.110644 | 0.389356 |

Therefore

```text
I(K:B) ≈ 0.583127 bits,
Pr(K=−1 | B=1) = 1,
Pr(K=−1 | B=0) ≈ 0.181192,
Pr(B=1 | K=−1) ≈ 0.778712.
```

The unit conditional specificity of B=1 follows exactly from the controlled interaction and its initial state; the other figures are finite-grid values. B=0 is not conclusive and no finite record is perfect. With the equal specified priors, the rule B=1 → K=−1, B=0 → K=+1 succeeds with probability about 0.889356.

B is not a spectator. At φ=100 the total-variation distance between the M¹,M² distribution with B coupled and the matched B-decoupled model is about **0.01539**. The targeted model gives `I(M¹:M²)≈0.4530` bits, rather than 0.4247. These are different physical Hamiltonians, not different descriptions of one experiment. Between φ=100 and φ=150 the K/B table changes by less than 0.00002 per entry in the N=80 sample; this is finite-interval persistence, not permanent or irreversible recording.

The exact code-decoupling theorem continues to hold: for this prepared sector the confined record pair R and all external detector/memory degrees have a product reduced state. Direct full-vector contraction checks R together with all three memories. Coupling B to h is a **chosen richer joint interface**, not an interaction making a confined inhabitant register B.

## 4. Same event, different experiential assignments

The prior [subject comparison](ZERO_SUBJECT_EXPERIENCE_BRIDGE_COMMON_DOMAIN_TEST.md) introduced two candidate pairs `S₁={H₁,R₁}` and `S₂={R₂,H₂}` and two fixed reference blocks. The prior graph selector is a hypothesis, not an established subject law. In particular, the full new constraint contains record–work and geometry interfaces that were not included in that selector's original four-node graph; its output has **not** been rederived from the complete coupled Hamiltonian.

For a joint ideal readout of r, K and B at φ=100, consider the event `r=+1, B=1`. Its N=80 probability is about `0.194678`. B=1 implies h=1, hence K=−1. On that physical event the two competing conditional hypotheses say:

| Hypothesis | proposed signed values `(S₁,S₂)` |
|---|---|
| Record-relative R | `(+κ,−κ)` |
| Work-current-probe J | `(−κ,+κ)` |
| Mismatch-only M | `(0,−κ)` |

Here `κ>0` is a stipulated common unit. The R rule uses the record/reference mismatch; the J rule uses the richer J-probe. R and J both sum to zero for this event if the two actual incidences have equal weights, but they disagree about **which candidate feels which sign**. Both remain oppositely signed for the other r and K combinations. The M rule gives a pair total `−κ` under the same equal-incidence assumption.

This has a precise consequence: **pairwise zero plus the common physical state does not, by itself, choose between R and J**. Ruling out M would additionally require that these two candidates exhaust the relevant whole and that this pair itself must sum to zero; whole-level zero alone does not imply that. If the two weights are unequal, even R and J have nonzero pair totals. None of the rules, equal incidence, common cardinal scale, actual subjects or outcome selection has been derived here.

If one interprets the negative sign as genuinely felt suffering, it remains locally real. A positive contribution elsewhere does not erase or justify it. Neither rule is established as a law of consciousness. The comparison does not claim that incompatible phenomenal assignments are genuinely possible worlds; it shows that the specified physical equations and stated balance condition alone have not selected between these formal candidates.

## 5. No-signalling and clock representations

For the original pair and triple sphere instruments, the **complete Bob-lab reduced state** agrees. This is checked not only for Ψ₀, but for all four cross operators `Tr_A(|Ψ_h⟩⟨Ψ_g|)`. The same Bob-local h, fixed preparation and Bob+geometry+memory evolution are applied in both cases. Therefore Bob's entire output density operator is identical for the two Alice settings; B and the joint K probe cannot reveal that setting. This is no-signalling for the stated tensor split and fixed physical operation, not a proof of spatial locality or of an arbitrary experience-dependent reporting law.

The new B coupling changes the clock operator, so the old 13-slice theorem cannot merely be reused. It does, however, admit the same proof strategy with a new bound. The conserved `σ_y` labels of M¹,M²,B decompose each h into eight two-component D channels. For h=1 the matrix potential is

```text
V_(m₁,m₂,b)=−E_(−5)σ_yᴰ−1.3(m₁E_0+m₂E_5)P₁ᴰ−0.8 b E_5 Iᴰ.
```

Each channel is an entire-kernel trace-class perturbation of T. The earlier analytic Fredholm and incoming-wave arguments apply channel by channel: no singular-continuous spectrum and a.c. reconstruction on almost every slice, with the full internal labels retained. For the point spectrum, using the derivative bounds `L_0=√(28/3)/π` and `L_5=√(328/3)/π`, the divided-difference operator of the previous [full-slice proof](ZERO_TWO_WINDOW_FULL_SLICE_CLOCK.md) obeys

```text
||B_k||²_HS ≤ [2L_5²+(0.8L_5)²+(1.3L_0+2.1L_5)²]/4
             ≈ 24.3422 < 25.
```

Hence an eigenvalue in the closed band has multiplicity at most 24. For an exterior eigenvalue choose the nearest edge p*: subtracting `V(p*,q)` leaves the same divided-difference bound, while the discarded term has rank at most two. Restricting an eigenspace by those two linear conditions leaves at most 24 dimensions, so its full dimension is at most **26**. The h=0 channels have the previous smaller bound. Applying the same analytic-evaluation and countable-intersection argument gives full-state reconstruction from **almost every 26-tuple** of slices, including tuples in any nonempty open interval.

This is a conservative sufficient bound, not a minimum or an explicit good tuple. It retains all h,m,b labels and the full complex φ signal. It is not a single-reading clock, a realistic local apparatus, an operational finite-time measurement, or a preferred foliation. As before, observables and their interchannel coherences must be transported with the state and physical inner product.

## 6. What this advances

The important integration is now concrete: a conservation-derived sphere outcome and correlated record, an actual sphere–work state, an internal geometry clock, two generic memories, and a targeted memory of the physically specified K relation all belong to **one constraint and one state**. The model distinguishes a record that happens to be strongly correlated with another record from a record that actually carries the relation used in a proposed experiential law.

It also locates the next constitutive problem: derive why an actual subject would have either R's or J's quality, how its incidence is defined under the full coupled dynamics, and whether a globally meaningful signed sum balances. A physical zero, two opposite probes, a fixed graph or a successful K memory does not determine that bridge. The directional sphere, conservation instrument, interaction and quantum state are not derived here from zero's constitution, and the point–sphere proposal is neither established nor refuted by this test. There is no claim of full gravity, global energy zero, irreversible memory, actual experience or resolution of necessity and quantum outcomes.

## Reproduce

```sh
python -m pip install --target .arena/python-deps numpy  # if needed
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_integrated_sphere_clock_experience_test \
  verification.zero_integrated_targeted_memory_test -v
```

Numerics use N=40,80,160 momentum meshes, polynomial-degree comparison and an independent small-grid dense Hermitian diagonalization. The calculated probabilities are finite-grid results without certified continuum errors. The 26-slice statement is analytical and uses the earlier continuum scattering/Fredholm argument; the grid checks do not prove it.
