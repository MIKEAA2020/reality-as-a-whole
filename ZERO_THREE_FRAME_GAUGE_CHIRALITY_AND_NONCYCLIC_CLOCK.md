# Three local frames, chirality and noncyclic record retention

## Result

**Continuation:** [a finite clock and chirality–holonomy joint instrument](ZERO_GAUGE_CLOCK_JOINT_INSTRUMENT_AND_READOUT.md) specifies coherent clock and loop sensors, computes conditional finite-shot statistics, and quantifies how clock readout changes the noncyclic constraint residual. A later [biochemical chirality audit](ZERO_RELATIONAL_CHIRALITY_AND_BIOLOGICAL_HOMOCHIRALITY.md) calibrates this invariant to an idealized labeled alanine stereocenter and tests a modified Frank-type amplification network, without claiming a derivation of real chemistry or Earth's specific handedness.

This pass implements the next two tests proposed after the [clocked chirality record](ZERO_CLOCKED_CHIRALITY_RECORD_AND_RETENTION.md): an explicit three-frame gauge model, and a noncyclic clock alternative. It finds:

1. With **two** supplied comparison links, the three directions can have independent local `SO(3)` frames. The existing relative angle, relational chirality, neutral-memory write, old pair constraints and clocked record have an exact gauge-invariant lift. Gauge fixing both links gives the previous common-frame construction, and normalized product Haar/area measures give an isometric lift of its scalar physical sector.
2. Adding a **third** link introduces loop holonomy. The tree observables do not determine it. A positive state family can have the same separate chirality and holonomy marginals as a reference state while having a nonzero gauge-invariant chirality–holonomy correlation. The written chirality memory can expose that correlation.
3. An ideal bilateral clock can write once and retain the record without a cyclic wipe. Its exact stationary histories, however, are non-normalizable on the declared `ℓ²(Z)` clock carrier. A normalized finite-window history can approximate stationarity; its minimum possible constraint residual for N consecutive clock readings is exactly `√[2−2cos(π/(N+1))]`.

These are controlled mathematical models. Links, round measures, memory, switching and the infinite clock remain inputs; they are not a derived spacetime gauge field or a physically local device. The tests verify exact formulas with rational moments, quadrature, gauge transformations, the old quantum vectors and a matrix-free clock calculation; they do not establish experience, global energy, a Yang–Mills law, or the actual existence of the proposed clock. Code: [three-frame geometry](verification/zero_three_frame_chirality.py), [noncyclic clock](verification/zero_noncyclic_chirality_clock.py), [nine tests](verification/zero_three_frame_chirality_test.py).

## 1. Independent frames and the tree gauge action

Take three independent unit vectors `n_i∈S²`, each written in its own oriented local frame, and introduce two `SO(3)` comparison links:

```text
L₁₂ : frame 2 → frame 1,       L₁₃ : frame 3 → frame 1.
```

For independent frame changes `R₁,R₂,R₃∈SO(3)`, define

```text
n_i  → R_i n_i,
L₁₂ → R₁ L₁₂ R₂⁻¹,
L₁₃ → R₁ L₁₃ R₃⁻¹.
```

The transported vectors `v₁=n₁`, `v₂=L₁₂n₂`, `v₃=L₁₃n₃` all transform by `R₁`. Thus the old relative angle and the added relational handedness are genuine invariants of **independent frame changes**:

```text
u = v₁·v₂,           t = v₁·(v₂×v₃).
```

Likewise `v₂·v₃` and `v₃·v₁` are invariant. The scalar triple product uses proper rotations; it changes sign under a simultaneous improper reflection. Treating reflections as gauge would change which observables are physical and is not assumed here.

Choosing `R₁=I`, `R₂=L₁₂`, `R₃=L₁₃` fixes both links to the identity and takes the directions to `(v₁,v₂,v₃)`. The remaining transformations are simultaneous rotations. Therefore the tree quotient is exactly the previously studied three-sphere diagonal-rotation quotient, not an additional arbitrary identification. The pairwise Gram data plus the sign of t classify its generic `SO(3)` orbits; they obey the Gram-determinant condition described in the previous pass.

This is a mathematical local-frame gauge model, not yet a gauge field over physical spacetime. In particular, independently rotating a direction **while holding its link fixed** is not the gauge transformation above and can change u or t; the verifier includes this negative control.

## 2. Exact Hilbert-space lift and the old echo

Equip each direction with normalized round area and each link with normalized Haar measure. Let the tree kinematic carrier be

```text
H_tree = L²((S²)³ × SO(3)², dΩ₁ dΩ₂ dΩ₃ dL₁₂ dL₁₃) ⊗ H_old ⊗ H_M,
```

with the conventional `4π` normalization implicit in each area measure. In this specified scalar model the independent frame changes act on directions and links; old records and the new neutral memory are spectators. For every common-rotation invariant three-direction vector-valued wavefunction `ψ(v₁,v₂,v₃)`, define

```text
(Jψ)(n₁,n₂,n₃,L₁₂,L₁₃) = ψ(n₁,L₁₂n₂,L₁₃n₃).
```

`Jψ` is gauge invariant. Haar invariance of sphere area at fixed links implies `||Jψ||=||ψ||`. Conversely, every gauge-invariant `L²` function is, almost everywhere, determined by its gauge-fixed representative and invariant under the remaining simultaneous rotations. With the normalized quotient measure induced by this construction, J is therefore a unitary identification of the prior diagonal-invariant carrier with the tree gauge-invariant sector. This applies componentwise to the supplied old record/pair/memory carrier. It is not a proof that the Haar/area measure or the local-frame model follows from a bare point.

The prior memory unitary now uses the invariant `t` above; the old angular-bin index uses invariant u. Consequently its clock-controlled write, hold and erase commute with every independent frame transformation, as do the original pair matching and zero-sum constraints, provided the old gates act on the declared old fibers and leave links/directions unchanged. The 40-clock construction transfers under J, including its finite retention and eventual erase; the old-only rotational-singlet backaction remains a statement about the corresponding **gauge-fixed subsystem**, not an independently local observable without a specified reference.

The verifier explicitly transports representative original post-echo quantum vectors at source/sign pairs `(0,+)` and `(15,−)`, their finite constrained pair, the qutrit gate and the reduced stationary clock history through sampled independent frame changes. The general group, norm and conjugation statements above follow analytically; the finite sampled checks are not a dense simulation of all carriers.

## 3. A third link adds physical holonomy

Now add a third link `L₂₃ : frame 3 → frame 2`, transforming as `L₂₃→R₂L₂₃R₃⁻¹`. The closed comparison is

```text
H = L₁₂ L₂₃ L₁₃⁻¹,       H→R₁ H R₁⁻¹.
```

Hence `χ(H)=tr H` is gauge invariant, as is `v₁·H v₁`. Tree gauge fixing sends the remaining link to H. After fixing, both the three vectors and H are acted on by the residual common rotation. Therefore H is not generally characterized by its trace alone when it is correlated with the vectors; relative axis information may also matter.

The extra link is not determined by the tree data. Set the three gauge-fixed vectors to the coordinate axes and `L₁₂=L₁₃=I`. Whether `L₂₃=I` or a quarter turn about the third axis, the tree dot products are all zero and `t=1`; yet `tr H` is respectively 3 or 1. These configurations are not gauge related. Thus a loop is more than another way to write the same tree.

If one **adds** the flatness condition `H=I`, the loop carries no independent holonomy and reduces to the tree model. But this is a further constraint. In the unconstrained Haar-`L²` loop carrier, the flat subset has measure zero; it is not a nonzero ordinary `L²` subspace obtained by simply demanding wavefunctions be supported there. One must specify a different reduced measure, a distributional/rigged treatment, or another appropriate constraint construction. Gauge invariance alone does not select flatness.

## 4. An observable correlation invisible to the separate marginals

Give the independent loop link normalized Haar measure. After tree gauge fixing, H has normalized Haar measure and is independent of the reference three-direction variables in the product model. For `χ=tr H` and the uniform three-sphere preparation,

```text
E[χ]=0,      E[χ²]=1,      E[t]=0,      E[t²]=2/9.
```

The Haar character moments follow, for example, from the angle distribution `(2/π)sin²(θ/2)dθ` on `0≤θ≤π` and `χ=1+2cos θ`.

Consider the strictly positive gauge-invariant reweighting

```text
ρ_ε = 1 + (ε/3) t χ,       |ε|<1.
```

It is normalized, since the original `E[tχ]=0`; positivity follows from `|t|≤1`, `|χ|≤3`. In this **new chosen state**, each entire tree-direction marginal and the entire H marginal remain as in the reference product state, because `E_H χ=0` and `E_tree t=0`. But their joint structure changes:

```text
E_ε[tχ] = (ε/3) E[t²] E[χ²] = 2ε/27.
```

This is a correlation between gauge-invariant observables, not a hidden-frame artifact. It also demonstrates why imposing the old marginal statistics does not select a unique enlarged state. In particular, the reweighted loop state is an alternative supplied preparation, not a passive gauge transform of the old product state. Its full quantum coherences and loop resources differ.

The written qutrit has conditional sign mean `E[B|t]=λt`, with `B=±1` on written outcomes. A joint observation of the written memory and holonomy therefore yields

```text
E_ε[B χ | written] = 2λε/27.
```

The individual B and χ means remain zero. On the prior 40-step uniform-anchor protocol conditioned on `r=2`, take B=0 while blank. Since the old and memory steps leave H fixed, the clock fractions from that construction give `8λε/135` for q=1 and `λε/18` for q=2. These are model predictions for the specified reweighted state and the stated joint effects, not a measured physical Wilson loop or evidence for electromagnetic duality. The polynomial moments and an independent numerical product quadrature check the single-written-slice result.

## 5. A bilateral clock: retention without cyclic uncomputation

Replace the finite cyclic clock with the specified carrier `ℓ²(Z)`. Let the old unitary at step n be the old 20-step gate repeated as `U_(n mod 20)`, including the four-state reference shift where desired. Define a time-independent controlled shift on the clock-plus-system carrier:

```text
W_∞ = Σ_(n∈Z) |n+1⟩⟨n| ⊗ V_n U_(n mod 20),
V_n = V_λ(T) if n=9, and I otherwise.
```

This is a well-defined unitary bilateral shift because every fiber map is unitary. Its switch is controlled by the clock coordinate, not by an external time parameter, but the clock, the special control at 9, the gate and their resources are stipulated. Since `T` is now the three-frame gauge-invariant multiplication operator, every step preserves that gauge sector and the transported old pair constraint. At n=10 the memory is recorded; on every subsequent forward slice there is no second write or erase, so the same record persists through arbitrarily many repetitions of the old echo. This is an ideal unitary retention statement on conditional history slices, **not** a fault-tolerant or dissipative physical memory.

There is an essential trade-off. If `W_∞ Ψ=Ψ` for a vector in `ℓ²(Z,H_system)`, unitarity of each step implies `||Ψ_n||=||Ψ_(n−1)||` for every integer n. Square summability then forces every slice to vanish. Thus there is **no nonzero normalizable exactly stationary vector** for this clock shift on the declared Hilbert space. One may formally discuss generalized stationary histories, but that requires a separate physical-inner-product or rigged-Hilbert-space construction; it is not supplied by the ordinary normalized state below.

### An optimal finite-support approximate history

Choose N consecutive readings `n=0,…,N−1`, with their old, reference and memory states following the specified unitary steps, and set

```text
f_n = √[2/(N+1)] sin[π(n+1)/(N+1)],
|Ω_N⟩ = Σ_(n=0)^(N−1) f_n |n⟩ |φ_n⟩.
```

It is normalized and has exact residual

```text
||(W_∞−I)|Ω_N⟩|| = √[2−2cos(π/(N+1))].
```

This is the minimum over **all normalized vectors supported on those N clock positions**, not only over this prepared history. Conjugating the unitary fiber evolution to a plain shift reduces the minimization to the lowest eigenvalue of the N-site Dirichlet discrete Laplacian; vector-valued degeneracy does not improve it. For comparison, a uniform clock window has residual `√(2/N)`. This norm is a constraint residual, not a bound on all experimental predictions without an additional operational theorem.

For the specified source and write at n=9, the clock probability of being on a written slice is `Σ_(n=10)^(N−1)|f_n|²`:

| N | residual | probability of a written clock slice |
|---:|---:|---:|
| 20 | 0.14946 | 0.50000 |
| 40 | 0.07661 | 0.90310 |
| 80 | 0.03878 | 0.98616 |

In this normalizable state, claims about the record at an individual reading are **conditional** on a reading in its support. It has no conditional slice beyond `N−1`. The underlying bilateral evolution has retained states at later readings if one evolves the initial data further, but that does not create nonzero support there in this fixed finite-window history. Increasing N supplies a wider ideal clock, not free energy, locality or an independently validated measurement.

The old reference-clock conditional protocol for this new noncyclic construction is not yet built as a normalized invariant twirl: a uniform average over infinitely many anchors is not a probability distribution. Bare clock-slice conditioning here is a stated model calculation, not a claim that a bare clock projector is a Dirac observable. The prior finite cyclic twirl remains valid for the separate 40-clock model.

## 6. Remaining work

- Derive or physically justify the frame links, their dynamics, allowed holonomy and measures; decide whether a tree, flat loop or nonflat loop is appropriate rather than selecting by convenience.
- Specify local access to the holonomy and pointer and construct an actual joint instrument, including backreaction and coupling resources. The `tχ` witness is an exact model observable, not automatically a locally measurable event.
- Develop an operational treatment of the noncyclic approximate constraint, clock readout and memory errors, or a justified generalized physical inner product; do not promote a small residual alone to exact stationarity.
- Revisit the balanced spinorial/Satake lift with these actual link variables. The three-frame `SO(3)` model is not by itself a non-Abelian Yang–Mills theory, and the loop trace is not an experimentally computed gauge-theory correlator.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_three_frame_chirality_test -v
```

The frame and carrier assumptions, independent link/Haar choices, comparison states, memory gate, clock shift and old finite echo are specified inputs. Numerical samples supplement the stated gauge, moment and discrete-Laplacian arguments; they do not establish a unique constitution or complete time.
