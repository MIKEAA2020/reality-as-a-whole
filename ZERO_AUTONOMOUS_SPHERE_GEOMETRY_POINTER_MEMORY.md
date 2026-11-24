# Autonomous geometry–pointer–memory dynamics in the constrained sphere model

**Continuation:** [two autonomous geometry-window records](ZERO_AUTONOMOUS_TWO_GEOMETRY_WINDOW_RECORDS.md) adds a second memory inside the constraint, with no intermediate projective measurement in the primary calculation.

## Result

The previous construction had an exact geometry-slice representation but required ideal full-φ solution data and stipulated measurement checkpoints. Here the detector **and a new finite memory** interact continuously inside one φ-independent constraint. There is no externally scheduled on/off operation in this model. The Gaussian-smeared geometry window controls the interaction; the memory is a reversible qubit.

For a selected incident packet the evolved pointer and memory become correlated and retain nearly unchanged joint statistics over the tested late scalar readings. The memory substantially changes the pointer's dynamics: with memory coupling, `Pr(D=1)` at φ=100 is about **0.3667**; without it, the same initial pointer and packet give about **0.9589**. Treating memory as a passive copy would therefore be wrong.

An additional **optional ideal pointer measurement** at φ=40 yields a quantitatively defined correlation with the memory at φ=100. This extra measurement is a diagnostic intervention, not part of the unmeasured autonomous evolution. The model does not yet supply an autonomous apparatus for that earlier measurement or an irreversible memory. The scalar clock remains idealized, and the band-projected geometry-window interaction is nonlocal in α.

The previously derived full continuum slice representation extends to this larger model, provided all internal channel components are retained. The new calculation integrates clock, detector, memory and the existing sphere–record encoding without assuming that a pointer is an experiencing subject.

Code: [verification/zero_autonomous_geometry_pointer_memory_test.py](verification/zero_autonomous_geometry_pointer_memory_test.py). Earlier foundations: [autonomous detector](ZERO_SPHERE_AUTONOMOUS_CONSTRAINED_DETECTOR.md), [domain/code recovery](ZERO_DOMAIN_SECTOR_CLOCK_RECOVERABILITY.md) and [full continuum slice map](ZERO_GEOMETRY_CLOCK_FULL_CONTINUUM_SLICE.md).

## 1. One constrained system, no scheduled coupling

Retain the physical momentum band `p=p_α∈(−7,−6)`, the encoded sphere–record logical levels `h=0,1`, the scalar φ and the earlier smeared geometry-window effect E. Introduce detector D and memory M, each a qubit. Let `P₁ᴰ=(I−σ_zᴰ)/2`. Set

```text
S = λ σ_yᴰ ⊗ I_M + κ P₁ᴰ ⊗ σ_yᴹ,     λ=0.4, κ=1,
C̃ = p_φ²/2 − p²/12 + h + E ⊗ S = 0,
Θ = p²/6 − 2h − 2 E ⊗ S.
```

E acts on geometry; S acts only on D and M. The memory interaction is conditioned on detector `D=1` and the geometry window. Both couplings are time-independent in φ. On the selected positive scalar-momentum branch,

```text
p_φ=Ω=√Θ,        U(φ)=exp(iΩφ).
```

This is a self-adjoint unitary evolution on a chosen physical Hilbert space with a corresponding positive-frequency constraint solution and physical product, as in the earlier model. The physical initial state is specified at scalar reading φ=0; that choice is not a fundamental external clock. The memory is included in Θ and the constraint, rather than appended after evolution.

In the `σ_yᴹ=m=±1` basis, S has detector matrix

```text
S_m = [[0, −iλ], [iλ, κm]],
s_(m,±) = [κm ± √(κ²+4λ²)]/2.
```

For the selected numbers the four eigenvalues are approximately `1.1403124, −0.1403124, 0.1403124, −1.1403124`. Since `0≤E≤I`,

```text
Θ ≥ 4 − (1+√1.64) ≈ 1.7194 > 0.
```

The square root is therefore well-defined on this entire selected band. This is a toy interaction: E is band-compressed and nonlocal in α, and the memory has no specified free energy gap, bath or physical materials. `C̃=0` is a constraint, not by itself an objective total energy of the whole.

## 2. The previous continuum clock result survives the memory

Diagonalizing S gives independent scalar geometry channels

```text
Θ_(h,s) = p²/6 − 2h − 2s E.
```

For every channel `|2s|≤1+√1.64≈2.280625`, which is below the `3π√3/7≈2.332028` threshold in the [no-embedded-eigenvalue proof](ZERO_GEOMETRY_CLOCK_FULL_CONTINUUM_SLICE.md). It is also small enough for the preceding exterior-state uniqueness bound, and Θ stays positive. The same trace-class, smooth-kernel, Mourre, non-embedded and variational arguments therefore apply to **each fixed channel**: a multiplicity-one a.c. sector plus exactly one simple exterior bound state, no singular-continuous component, and no eigenvalue embedded in that channel's own continuum.

Consequently, for almost every α, each channel's complete complex scalar-clock slice signal recovers its full physical vector. There are finitely many h and S channels, so their common set of good α still has full measure. Pointer and memory z observables mix those channels and must be transformed with their full inter-channel operators. Frequencies from distinct labelled channels can overlap: these conclusions do not imply that tracing away the channel labels leaves an injective scalar signal.

The weak channels have `|2s|≈0.280625`. At N=40,80,160 the grid does not resolve their extremely shallow exterior levels, while it does resolve the strong-channel levels. This is not a contradiction: the continuum variational result applies for any nonzero coupling, and finite grids can miss a very shallow bound state. The grid checks therefore are not the proof of the continuum spectrum.

The slice map uses the **complete complex solution**, not finite observed data. The bound-state no-go for a normalized real-valued globally covariant clock POVM still applies, and a good slice need not be a monotonic physical clock.

## 3. Pointer–memory correlations and disturbance

Prepare the same translated normalizable packet used previously, centered initially at α≈−15; take the encoded logical superposition `(|0⟩+i|1⟩)/√2`, and initialize D and M in z=0. The following joint probabilities are obtained from the closed unitary state at φ=100, using N=80 momentum points:

| Detector D | Memory M=0 | Memory M=1 |
|---|---:|---:|
| 0 | 0.4629544 | 0.1703617 |
| 1 | 0.0512695 | 0.3154143 |

The z-readout mutual information is about **0.2534 bits**. In this joint distribution,

```text
Pr(M=1 | D=1) ≈ 0.8602,
Pr(M=1 | D=0) ≈ 0.2690,
Pr(M=D)        ≈ 0.7784.
```

This is a meaningful but imperfect **same-reading pointer–memory correlation**. It is not a proof that memory faithfully copied a pre-existing definite D value, selected an outcome or recorded subjective experience. The D=1 projector does not commute with the λσ_yᴰ detector term: the measurement-like coupling is not quantum-nondemolition with respect to D_z.

The coupled M changes the detector: `Pr(D=1)≈0.366684` at φ=100, while the otherwise matched κ=0 control gives `≈0.958879`. In the N=80 numerical evolution, the geometry-window expectation `⟨E⟩` is about 0.28974 at φ=40, 0.00266 at 60 and 0.000130 at 100. Joint D–M probabilities vary by less than 0.001 in total absolute change between φ=100 and either 150 or 200. These are finite-interval numerical observations, not a proof of perfect permanent storage, irreversibility or zero interaction after φ=100.

For a matched receding packet centered at α≈+15, `Pr(M=1)≈0.000266` at φ=100, compared with `≈0.485776` for the incident packet. The model can therefore distinguish these two specified preparations by memory readout, subject to their initial priors; it does not establish an actual observation or perfect geometry-crossing detection.

### Numerical convergence and independent propagation

At N=40,80,160 the φ=100 `Pr(D=1,M=1)` values are approximately `0.3154360, 0.3154143, 0.3154089`. Spectral propagation also agrees with an independent Chebyshev polynomial propagation at representative φ=40 and 100. The former retains the cross-channel eigenbasis transformations; matching eigenvector indices across different S channels would be incorrect. These checks are numerical evidence of convergence for the specified packet, not continuum error bounds.

## 4. Does memory correlate with an earlier pointer reading?

To distinguish present correlation from a claim about a past record, apply an **extra ideal projective measurement of D_z at φ=40**, evolve the resulting branch with the same closed-system Hamiltonian, then query M_z at φ=100. At N=80:

| Measured D at φ=40 | Later M=0 | Later M=1 |
|---|---:|---:|
| 0 | 0.5190661 | 0.1642069 |
| 1 | 0.0483489 | 0.2683781 |

This explicitly specified two-time intervention gives a mutual information of about **0.2480 bits** and `Pr(M=D_40)≈0.7874`. The additional early projection is not part of the autonomous memory coupling: it changes the subsequent memory marginal from about 0.485776 without the projection to about 0.432585 with it. Thus this is evidence for an operationally defined time-separated correlation **under that instrument**, not a license to assign an unmeasured definite D_40 in the original unprobed state. An explicit apparatus that stores the earlier D result and its energy/constraint accounting would require another closed interaction.

## 5. The confined sphere sector remains distinct

The existing code identifies h=0,1 with the actual orthogonal sphere–record logical states. The earlier environment-isometry proof says the confined subsystem S has the same reduced state for arbitrary logical density operators, even when the logical state is correlated with a reference. Since the new Θ acts on that logical index and on geometry, D and M, but not on the confined label itself, the same code identity implies that the confined S/reference state remains `ρ_S⊗ρ_reference` for these encoded operations. A selected momentum/memory projection is checked using the actual prior environment vectors; the general statement follows from the prior code theorem, not that sample alone.

This is an engineered, potentially nonlocal encoding. The confined subsystem does not automatically register D, M or the richer evolution. It is not assumed to be a subject. The surface-restricted traveler's position remains A during room travel and changes to B on return; the traveler/player remains distinct from any confined inhabitant or game piece.

## 6. What next?

The memory is now included in an autonomous constraint, and it demonstrably changes the dynamics while carrying correlation. The next decisive improvement is a **closed sequential-record construction**: introduce a second finite record coupled to the pointer without applying the optional projective operation from outside, and measure how well it preserves a past pointer correlation while including its backaction. Then replace the nonlocal band-projected window and ideal scalar reading with a localized, finite-resolution mechanism, and investigate the inhomogeneous constraint algebra or an emergent replacement.

None of these constructions derives the chosen action, coupling strengths, encoding, actual subjects or experiential incidence from zero. Nor does the constraint establish objective whole energy or an experiential cancellation law. If a justified whole-level signed total vanishes, locally felt suffering remains real.

## Reproduce

```sh
python -m unittest verification.zero_autonomous_geometry_pointer_memory_test -v
```

The tests check positivity and the spectral bounds, closed unitary probabilities, the receding control, pointer–memory correlations and disturbance, the optional sequential intervention, finite late-time stability, spectral versus Chebyshev evolution, on-branch constraint cancellation, and a confined-reference reduction. Finite grids do not prove the continuum theorems or a permanent record.
