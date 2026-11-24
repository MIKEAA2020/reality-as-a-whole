# Interacting geometry slices: a regulated clock-perspective construction

## Result

We can now construct **geometry-slice data for the interacting model**, rather than reusing its free clock transformation. At a fixed α=ln(a), evaluate the interacting covariant solution as a function of the scalar clock φ; resolve its scalar-frequency components; and equip those components with the physical inner product induced by the original constrained theory. On a finite momentum regulator and at the checked slices α=0,2,4, this gives an invertible map for every state, including the regulated bound modes. The map between slices preserves the induced physical norm and composes exactly.

Transporting the actual first-geometry-reading instrument and pointer observable into these slice spaces reproduces **all** the prior scalar-clock first-reading and repeated-history probabilities. This is more than comparing two eigenbases: the data are the value of the actual interacting covariant solution *on a geometry slice*. But the equality is a consequence of an explicitly constructed pullback on the regulated common state space; it is **not** an independent quantization, a local α-evolution Hamiltonian, or a demonstrated continuum clock switch. It therefore does not solve the general multiple-choice problem.

Code: [verification/zero_interacting_geometry_slice_clock_test.py](verification/zero_interacting_geometry_slice_clock_test.py). The physical sector and probabilities transported here are those in [the first-reading construction](ZERO_INTERACTING_GEOMETRY_FIRST_READING_CLOCK.md); the interacting operator and spectral caveats are in [the interacting-spectrum report](ZERO_SPHERE_INTERACTING_CLOCK_SPECTRUM_AND_BOUND_STATES.md).

## 1. Construct the interacting α-slice data

Retain the same scalar-clock physical branch:

```text
Θ_(h,d) = p²/6 − 2h − 0.8d E,       Ω_(h,d)=√Θ_(h,d),
U(φ)=exp(iΩφ),                        h=0,1,  d=±1.
```

The geometry window effect E is nonlocal in p, so the eigenmodes of Θ are not the free momentum modes. For a finite N-point Nyström discretization let `v_(d,j)(p_i)` be the real orthonormal eigenvectors of `Θ_(0,d)` with eigenvalues `θ_(d,j)`; then

```text
ω_(h,d,j)=√(θ_(d,j)−2h),
χ_(h,d)(p_i,φ) = Σ_j c_(h,d,j) v_(d,j)(p_i) exp(i ω_(h,d,j) φ).
```

The coefficients have norm `Σ_(h,d,j)|c_(h,d,j)|²=1`. In the earlier chosen positive-frequency Klein–Gordon physical representation, the **covariant** solution differs from the reduced χ by the mode factor `1/√(2ω)`. With Δp=1/N, its Fourier value at α is

```text
Ψ_(h,d)(α,φ) = Σ_j r_(h,d,j)(α) c_(h,d,j) exp(iω_(h,d,j)φ),
r_(h,d,j)(α) = [√(Δp)/(√(2π)√(2ω_(h,d,j)))]
                × Σ_i exp(i p_i α) v_(d,j)(p_i).
```

All h,d components remain separately labelled; even coincident frequencies in different labelled channels would not by themselves erase the channel label. Within each tested channel the finite-grid frequencies are distinct. Define `w_(h,d,j)(α)=r_(h,d,j)(α)c_(h,d,j)`. The components w are precisely the Fourier–Bohr coefficients of the α-slice function in scalar φ: the infinite symmetric time average of `exp(−iω_j φ) Ψ(α,φ)` isolates w_j. This is an exact identity for a finite sum of distinct frequencies, not a claim that a finite-duration clock measurement extracts them perfectly.

If each r_j on a slice is nonzero, the map `c → w=R_α c` is invertible. Its **physical** inner product is not the unweighted norm of w:

```text
⟨w,w′⟩_α = Σ_(h,d,j) w*_(h,d,j) w′_(h,d,j) / |r_(h,d,j)(α)|².
```

This is positive and gives `⟨w,w⟩_α=Σ|c|²`. The inverse factors are fixed by the selected physical representation; they are not an independently derived probability law at an α crossing. A zero r_j loses that mode and prevents this particular map from being invertible. Very small factors can make recovery unstable in an unweighted data norm.

## 2. Propagation between geometry slices

On two slices where the map is invertible,

```text
w_j(α₂) = [r_j(α₂)/r_j(α₁)] w_j(α₁).
```

Thus `M_(α₂←α₁)=R_α₂ R_α₁⁻¹` has the composition property and is unitary **between the two α-dependent inner products**. It generally is not unitary in an unweighted coefficient norm. This is a solution-data transfer: no claim is made that α increases along every history or that all states pass through each geometry reading. The transferred function still contains the full scalar-frequency information, including discrete bound modes.

For N=40, all four channels have nonzero r_j at α=0,2,4. The incident sphere–record/pointer packet has:

| α | Unweighted `Σ|w|²` | Induced physical `Σ|w/r|²` |
|---:|---:|---:|
| 0 | 0.00063250 | 1 |
| 2 | 0.00069079 | 1 |
| 4 | 0.00079665 | 1 |

The change in the unweighted expression is **not** loss of physical probability; the norm requires the induced metric. The N=40 ratio `max|r|/min|r|` over all four channels at α=0 is about 6.99; at N=80 and 160 it is about 10.34 and 15.55. These raw finite-grid numbers depend on discretization and the chosen data norm. Their growth warns against assuming uniform stability, but does not by itself prove or disprove a continuum inverse.

A single spacetime point can have a node even while the full φ-dependent slice remains informative. The test explicitly constructs normalized physical data with Ψ(α=0,φ=0)=0 but nonzero frequency-resolved slice data. Therefore a node at one φ is **not** proof that the whole slice map fails. Conversely, a vanishing r for a particular energy mode would make that mode unrecoverable in this construction.

## 3. Transport the same operational question

For any physical operation A represented in the interacting spectral basis, its geometry-slice representative is

```text
A_α = R_α A R_α⁻¹.
```

Its adjoint is taken with respect to the induced α-dependent physical inner product, not the ordinary Euclidean adjoint. For our yes and no operators Y=E and N=√(I−E²), this gives a complete instrument in every checked slice space. The scalar-reading interval evolution and all three operations are transported in the same way.

The detector z projectors mix d=+ and d=−. Since these channels have different interacting eigenvectors, their α-slice representatives require the cross-Gram matrix between those eigenvectors **and** the appropriate r factors. Identifying spectral indices or applying the ordinary Euclidean pointer matrix would change the question.

The tests calculate the first-yes/pointer effects and all eight repeated yes/no histories in each slice α=0,2,4 and in the original p representation. Every probability agrees to numerical precision. In particular, at N=40, the first-yes probabilities are approximately

```text
φ=30: 0.1779462;  φ=40: 0.1033704;  φ=50: 0.0149562;
no yes at the three attempts: 0.7037273.
```

These are the same regulated, instrument-dependent probabilities reported before. This calculation checks the **same** sequential event from different solution-data representations; it does not assert equality between this instrument and a different natural geometry-time measurement. The instrument still uses specified scalar checkpoints and has the backaction and no-reading outcomes described in the prior note.

## 4. An exact continuum result: what a slice can see

There is also an exact construction in the actual continuum Hilbert space, without discretizing or assuming a particular spectral type. For one fixed h,d channel, let `P(ds)` be the spectral measure of the strictly positive, bounded Ω and define the band-limited geometry-evaluation vector

```text
a_α(p) = exp(−ipα)/√(2π),
μ_α(B) = ⟨a_α, P(B) a_α⟩,
K_α = closure{ f(Ω)a_α : f bounded Borel }.
```

Here `K_α` is the cyclic subspace generated by a_α. Spectral theory gives a unitary map `f(Ω)a_α ↔ f(s)` from K_α to `L²(μ_α)`. For physical data `ψ∈K_α`, write `ψ=f(Ω)a_α` and define `g(s)=f(s)/√(2s)`. The actual covariant solution's slice is

```text
Ψ(α,φ) = ⟨a_α, exp(iΩφ) (2Ω)^(−1/2) ψ⟩
        = ∫ exp(isφ) g(s) μ_α(ds),
||ψ||²_phys = ∫ 2s |g(s)|² μ_α(ds).
```

The complex measure `g μ_α` is finite by Cauchy–Schwarz and the positive lower bound on Ω. Its Fourier transform on all real φ uniquely determines it; therefore the entire φ-dependent α-slice determines g, and hence ψ, **within K_α**. This is a continuum partial slice map, with an exact induced physical inner product. It handles continuous spectrum, bound-state atoms and any singular spectral part in one measure. If b is a bound eigenstate with frequency s_b, its slice measure has an atom `μ_α({s_b})=||P({s_b})a_α||²`; the atom sees b only if their overlap is nonzero. Degenerate eigenspaces can retain directions invisible to one evaluation vector.

For any `ψ_⊥∈K_α⊥`, the entire α-slice function is zero for every φ, because K_α reduces Ω and its functional calculus. Thus **K_α⊥ is exactly the information invisible to this slice construction**. Two normalized states with the same K_α component and different phases on an orthogonal invisible component give the same slice. We do not assume K_α⊥ vanishes. The construction is repeated separately for all four labelled channels; the pointer can mix them, so its full effect must be transported with the corresponding inter-channel operators.

For an event effect F on the complete physical space, states in K_α have probabilities `⟨ψ|P_K F P_K|ψ⟩`, which can be evaluated in the slice representation. This is the correct pullback of the **complete** event, including all intermediate evolution and measurements. One cannot in general project each intermediate operation separately: the dynamics or an instrument might leave K_α and later return. Likewise, a postmeasurement state need not stay in K_α. Our preceding first-reading effect can be compressed in this way for inputs in the common cyclic domain, but we have not evaluated the relevant continuum spectral measures, proved that every operation preserves the domain, or demonstrated an autonomous geometry clock. This exact partial result does not assert a normalized real-outcome covariant clock POVM and therefore does not conflict with the bound-state no-go.

The finite-grid calculation above is its nondegenerate atomic analogue: μ_j is `|⟨α|v_j⟩|²`, w_j is the jth atomic weight of `g μ`, and nonzero slice overlaps make the finite cyclic subspace the whole regulated channel. The tests verify the induced norm and a separate noncyclic degenerate example.

## 5. Why the remaining continuum problem is substantive

This construction must not be promoted automatically to full continuum quantum gravity:

* **Continuous and discrete scalar frequencies.** In the continuum the interacting operator has an absolutely continuous sector and at least one normalizable bound state. A bound state's φ dependence is a plane wave, not an L²(ℝ,dφ) function. A geometry-slice construction that uses only an ordinary scalar-wavefunction L² norm can therefore lose or mishandle bound states. A continuum proof needs the actual mixed spectral measure, possible multiplicities and generalized eigenfunctions, plus the nodal and inverse-domain conditions.
* **Nonlocality in α.** The selected band makes `E=Π M_g Π` in α-space, where Π is band projection and `g` is the smeared window. Its integral kernel is not supported only at α=β. Accordingly the constraint is nonlocal in the geometry coordinate; an ordinary local Cauchy equation in α cannot simply be assumed. The regulated ratio map transfers already-specified global solutions, not a separately justified local geometry-clock Hamiltonian.
* **What counts as a clock reading.** A mathematical slice of a solution is not automatically a detector outcome or an always-advancing time. The preceding instrument supplies one specific finite-window protocol, with missed and repeated readings. The scalar checkpoints and measurement couplings are stipulated, not an autonomous local measurement process.
* **General covariance and uniqueness.** This homogeneous selected branch has one reduced constraint, not the full inhomogeneous gravitational constraint algebra. No preferred foliation is postulated, but that alone is not a proof of refoliation invariance. Pulling an operator through an invertible map does not establish equivalence of independently chosen quantizations or resolve the general multiple-choice problem.

## 6. Next step

Determine whether the cyclic subspaces K_α equal the full interacting channels at useful α, or explicitly identify their invisible complements. Evaluate the spectral measures, bound overlaps and pointer cross-channel transforms, then compute the same first-reading effects in the continuum slice representation. Also determine when the α=0,2,4 cyclic domains coincide and whether the resulting transfer maps are stable in physically meaningful norms. In parallel, replace the stipulated checkpoints and nonlocal band-projected apparatus with a clock-controlled interaction whose records and constraint are part of a closed model.

These steps advance a concrete physical realization of relational time. They do not yet derive the chosen constraint, packet, measurement, subject or the actuality of experience from the point–sphere zero proposal, nor do they identify the constraint with objective whole energy. A global signed balance, if established, would not erase locally felt suffering.

## Reproduce

```sh
python -m unittest verification.zero_interacting_geometry_slice_clock_test -v
```

The tests check the covariant-solution Fourier slice and frequency reconstruction, the weighted physical norm, composition across slices, bound-mode inclusion in the finite regulator, full first-reading and history-instrument transport, and a one-point node. Continuum injectivity and spectral completeness are not numerically proved.
