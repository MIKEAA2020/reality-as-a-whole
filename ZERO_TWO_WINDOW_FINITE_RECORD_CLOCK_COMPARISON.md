# Finite records and clock descriptions in the two-window model

## Result and correction

The central limitation is **not** that an ideal continuum change of description has never been constructed. The existing [full-state two-window result](ZERO_TWO_WINDOW_FULL_SLICE_CLOCK.md) gives full reconstruction from the complete complex scalar-clock signal on almost every 13-tuple of geometry slices, including bound states; [its predecessor](ZERO_TWO_WINDOW_CONTINUUM_GEOMETRY_SLICE.md) gives almost-everywhere single-slice reconstruction for the scattering sector. A later [three-memory extension](ZERO_INTEGRATED_SPHERE_AUTONOMOUS_INCIDENCE.md) gives a sufficient 26-slice bound for a changed constraint. These are ideal all-φ signals, with internal labels and phase retained—not a finite set of detector clicks. I incorrectly understated the two-window result in the initial diagnosis; that diagnosis is now corrected.

Here we use the **same two-window constraint**, not a new theory. We add a specified unsharp geometry measurement at one scalar reading and read both existing memory qubits later. In a finite regulator, transforming the preparation, propagators, measurement operations and postmeasurement states by the same unitary gives the same complete outcome table. However, sampling the complex slice at only three scalar readings loses enough information that two normalized states with identical samples can predict substantially different memory records—even if the same extra geometry instrument is then applied. The example makes the ideal-to-operational gap explicit; it is not a no-go for every restricted preparation or every practical clock.

Code and tests: [verification/zero_two_window_finite_record_clock_test.py](verification/zero_two_window_finite_record_clock_test.py). Model, physical inner product and original autonomous records: [two-window report](ZERO_AUTONOMOUS_TWO_GEOMETRY_WINDOW_RECORDS.md).

## One physical intervention, two finite coordinate representations

Retain the original positive-frequency two-window constraint, its momentum band `(−7,−6)`, pointer D, memories M₁ and M₂, and logical h=0,1. Use the original incident packet and balanced pointer, with memories initially zero and the logical levels equally weighted. The original φ-independent interaction remains active throughout. The extra intervention is explicitly **not** autonomous: it is an ideal Lüders instrument at scalar reading φ=40, with

```text
K₀ = sqrt(I − E₀),       K₁ = sqrt(E₀),
```

where E₀ is the same band-compressed finite-width geometry-window effect used in the constraint. At φ=100 measure both memories in the z basis. The full unnormalized branch state and probability are

```text
ψ_(z,a,b) = P_(M₁=a,M₂=b) U(60) K_z U(40) ψ₀,
p(z,a,b)  = ||ψ_(z,a,b)||²,       z,a,b ∈ {0,1}.
```

The h sectors are propagated separately and averaged with weight 1/2; this is valid for these h-diagonal operations, not a general assertion that logical coherence is absent. All eight outcomes are retained. The no-click outcome z=0 is **not** proof of no geometry crossing: this effect has finite resolution and tails, and a single snapshot cannot count crossings. Nor are the two memory bits an exact first-hit or multiple-crossing history; their unitary coupling can flip them repeatedly. Those histories would require a separately defined record-retaining instrument, including its additional backaction.

At N=80 momentum samples, the following joint probabilities are obtained (rounding only):

| z | M₁=0, M₂=0 | M₁=0, M₂=1 | M₁=1, M₂=0 | M₁=1, M₂=1 |
|---|---:|---:|---:|---:|
| 0 | 0.391486 | 0.052307 | 0.067182 | 0.329469 |
| 1 | 0.114162 | 0.011628 | 0.005405 | 0.028361 |

The hit probability is 0.159556. With this intervention, `Pr(M₁=1)=0.430417`; without it, keeping the original constraint and preparation, `Pr(M₁=1)=0.432712`. The difference, about −0.002295, is a finite-regulator effect of the *specified intervention*, not evidence of disagreement between clocks. At N=24 and 40 the hit probabilities are 0.159569 and 0.159560; the largest difference between individual entries is under 0.0003. This is a convergence check, not a continuum error bound.

For the second description let Q be the normalized discrete Fourier transform on the momentum grid, tensored with the internal identity. We explicitly use `Qψ₀`, `QUQ†`, `QK_zQ†` and `QP_(a,b)Q†`. The unnormalized branch vectors then equal Q times the original vectors and each joint probability agrees, numerically to better than 10⁻¹² in the test. No outcome is dropped and the conditional state is transported whenever its probability is nonzero. This is an exact finite-dimensional **basis change** within one theory. It is not a construction of a continuum geometry-slice clock, not independent quantization with a different clock, and not a demonstration that two operational clock instruments have been equated.

## Finite samples: a concrete loss of information

Work in h=0 and keep all eight D/M components. In the finite model define R to output the complex, positive-frequency weighted geometry-slice amplitude at α=0 for φ=0,40,100. These are **ideal unmeasured solution amplitudes**, not outcomes of the above instrument; the intervening instrument changes the solution, so the samples describe the unperturbed run. In N=24 the physical space has dimension 192 and R has 24 complex outputs and numerical rank 24. Its kernel therefore has dimension 168. The test constructs x and y, orthogonal unit vectors in this kernel, chosen to minimize and maximize the later `M₁=1` probability; v is a unit vector orthogonal to the kernel with nonzero Rv. Define

```text
ψ = (v+x)/sqrt(2),       χ = (v+y)/sqrt(2).
```

Both are normalized, share the same **nonzero** three complex slice samples, and have different physical states. Without the extra instrument their φ=100 `M₁=1` probabilities are 0.25 and 0.75. With the same intervening E₀ instrument and its outcomes summed, the probabilities are approximately 0.250490 and 0.751612. They are deliberately constructed general states in the full h=0 sector, **not** the original incident preparation; in particular their memories are not required to start in zero. Thus they demonstrate information loss on the unrestricted domain, not failure to predict for the one fixed known preparation. The kernel has dimensions 104 and 232 at N=16 and 32, respectively, with the same 24 independent outputs in these tests. The actual witness vectors are regulator-dependent; no convergence of those vectors to continuum states is claimed.

There is also a straightforward **continuum noninjectivity statement** for the same type of data. The two-window h=0 physical space contains the infinite-dimensional band-limited momentum space with eight internal components. For any finite number of α/φ pairs, each component of the complex weighted slice is a bounded linear functional: the band is finite, `exp(iΩφ)` is unitary and Ω is bounded away from zero. Their combined map has finite-dimensional range and hence an infinite-dimensional kernel. If the map is nonzero, choose a unit v in the kernel's orthogonal complement and distinct unit kernel vectors x,y; `(v+x)/sqrt(2)` and `(v+y)/sqrt(2)` have identical nonzero samples and are distinct physical rays. If the map is zero, noninjectivity is immediate. This proof does **not** show those continuum states differ in this particular memory event, nor does it establish experimental distinguishability of arbitrary states. The finite numerical witness establishes that additional fact only in its regulator.

There is no conflict with full-state 13-slice reconstruction: that theorem uses infinitely many φ values and their full complex dependence, not just a finite list. Nor is this a claim about recovery with stronger prior restrictions, additional measurements, multiple copies or an approximation tolerance. For generic unrestricted states, recovering an entire state from finitely many linear samples cannot be injective; practical inference about selected observables may nevertheless succeed with much less.

## What remains

* A geometrical clock-switch test must compare the same intervention in the established continuum slice-data representation, specify its domain and usable finite data, and bound errors. The DFT calculation alone is not that test.
* The finite full-space calculation retains all regulator modes but does not isolate continuum bound versus scattering contributions, establish rates of convergence, or decide whether one full complex slice recovers every bound direction. The existing 13-slice theorem covers both sectors in its own ideal-data setting.
* Neither the snapshot no-click nor finite reversible memory bits identify zero, one or multiple crossings. An explicit history instrument with records, repeated readout backaction and the applicable clock domain remains to be constructed and compared.
* The ideal scalar clock, band projection, detector, memory and initial state are chosen. None is derived from zero, nor do their correlations establish actual subjects, experience, a thermodynamic arrow, general covariance or a solution of quantum gravity.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_two_window_finite_record_clock_test -v
```

The tests check finite-state sample loss, refinement, all transported branch states and probabilities, and intervention backaction. The continuum kernel argument is analytic and is not proved by the finite computation.
