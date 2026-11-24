# The geometry-clock question: what can a continuum slice recover?

**Continuation:** [Mourre and bound-spectrum analysis](ZERO_GEOMETRY_CLOCK_MOURRE_AND_BOUND_SPECTRUM.md) rules out singular-continuous spectrum for this model and proves that each pointer channel has exactly one exterior bound eigenvalue. Embedded-eigenvalue multiplicity remains open.

## Answer

The [preceding construction](ZERO_INTERACTING_GEOMETRY_SLICE_CLOCK_SWITCH.md) left a definite question: can an interacting geometry slice recover the physical state, or does the slice necessarily lose information? For our band-projected FLRW model, there is a stronger **continuum** answer:

> For almost every geometry value α, the full complex scalar-clock signal on that slice uniquely determines the entire **absolutely continuous (scattering) component** of every physical state. This holds simultaneously for both logical levels and both pointer channels.

This is an analytic statement for the specified model, not a conclusion drawn from the finite-grid eigenvectors. “Almost every” is with respect to Lebesgue measure in α; it does not identify whether a particular nominated value, including α=0, is good for the entire scattering sector.

There is a second explicit result: in each pointer channel the extremal bound state previously proved to exist is simple and has nonzero slice amplitude for **every |α|<π**. Thus those particular bound states are retained on all slices in that interval. Almost every slice also retains any other simple bound eigenstate, if such eigenstates exist.

This still does **not** prove a globally complete geometry clock: a possible singular-continuous sector and degenerate point eigenspaces require separate treatment; the signal used is the complete complex function of φ over the entire real line, not a finite measurement record. There is no claim of autonomous readout, physical extraction of unknown wavefunction phases from a single system, or a solution of full GR.

Verification checks and counterexamples: [verification/zero_interacting_geometry_clock_cyclicity_test.py](verification/zero_interacting_geometry_clock_cyclicity_test.py). The proof below uses the continuum spectral theorem and Kato–Rosenblum, not the grid numerics.

## 1. Precise model and slice map

The physical Hilbert space for each h,d channel is `L²(I,dp)`, with `I=(−7,−6)` and

```text
T(p)=p²/6,
Θ_(h,d)=T−2h−0.8d E,         Ω_(h,d)=√Θ_(h,d),
h=0,1;  d=+1,−1.
```

E is the same positive trace-class compressed Gaussian-window effect, with real continuous kernel

```text
E(p,q)=exp[−(p−q)²/2] sin[2(p−q)]/[π(p−q)].
```

It obeys `0≤E≤I`, and on these channels Θ≥3.2, so Ω is positive and bounded. The original physical product, positive-frequency branch and operator definitions are those in the [earlier reports](ZERO_SPHERE_INTERACTING_CLOCK_SPECTRUM_AND_BOUND_STATES.md). The other h sector shifts Θ by a constant; it has the same eigenvectors and spectral subspaces in each d channel.

For each α set `a_α(p)=exp(−ipα)/√(2π)` and define the cyclic subspace

```text
K_α = closure{ f(Ω) a_α : f bounded Borel }.
```

For a physical vector ψ, the positive-frequency covariant solution evaluated at α is

```text
Ψ_ψ(α,φ)=⟨a_α, exp(iΩφ) (2Ω)^(−1/2) ψ⟩.
```

As shown in the preceding report using its scalar spectral measure, the whole complex signal `φ ↦ Ψ_ψ(α,φ)` determines exactly `P_(K_α) ψ`, and all of `K_α⊥` is invisible to it. This is a statement about solution data, not a normalized probability density for α or φ.

## 2. The scattering sector is visible on almost every slice

### Step A: the a.c. spectrum has multiplicity one

The unperturbed T is multiplication by the strictly monotone function p²/6 on I. Its absolutely continuous spectrum is the interval `[6,49/6]` with multiplicity one. Since E is trace class, Kato–Rosenblum gives unitary equivalence of the absolutely continuous parts of Θ_(h,d) and T−2h. The positive square root is smooth and strictly monotone on the allowed positive spectrum, so Ω_(h,d) also has multiplicity-one a.c. spectrum. An a.c. spectral representation can therefore be chosen as `L²(J_h,ds)`, where

```text
J_h=[√(6−2h), √(49/6−2h)].
```

This says nothing by itself about possible singular-continuous spectrum or the multiplicity of point eigenvalues.

### Step B: the slice vectors are collectively complete

The set `{a_α : α∈ℝ}` spans a dense subspace of L²(I). Indeed, if `v∈L²(I)` is orthogonal to all a_α, then its Fourier transform vanishes for every α. Compact support implies v is in L¹ as well, and Fourier uniqueness implies v=0. The same follows using α from any countable dense subset of ℝ, since the transform is continuous.

Project the slice vectors onto the a.c. subspace and apply its spectral unitary. The projected family remains total in `L²(J_h,ds)`. Let its scalar spectral representative be A(s,α). For almost every s, A(s,α) is not identically zero as a function of α: otherwise, on a set of positive s-measure where all the countably many dense-family amplitudes vanish, a nonzero L² function supported there would be orthogonal to their total span.

### Step C: analyticity and Fubini

For complex z, the vector `a_z(p)=exp(−ipz)/√(2π)` is entire as an L²(I)-valued function, since p lies in a compact band. The a.c. projection and spectral unitary are bounded linear maps. Moreover, their Taylor coefficients have L² norms bounded by a constant times `7^n/n!`. On the finite interval J_h, their absolute series is summable in L¹ on every compact z-disk; hence, after choosing a common representative outside a null set of s, `A(s,z)` is entire in z for almost every s.

For almost every s the entire function is not identically zero, so its real zeros have Lebesgue measure zero. Fubini then implies that, for almost every real α, `A(s,α)≠0` for almost every s in J_h.

In a multiplicity-one L² spectral representation, a vector is cyclic precisely when its representative is nonzero almost everywhere. Therefore the projection of a_α is cyclic in the a.c. sector for almost every α. Since the a.c. and singular spectral parts can be separated by spectral projections on disjoint measure supports, the full K_α actually **contains** the a.c. sector for those α. The finite union of the exceptional null sets for the four h,d channels is still null.

**Consequence:** for almost every α, two physical states with the same complex slice signal have the same a.c. component in every channel. Any component invisible to that α slice belongs to the singular spectral sector. This does not assert that the exceptional set is empty or provide a numerical test for α=0.

## 3. The two extremal bound states are visible throughout a central interval

The earlier variational argument proves the existence of an eigenvalue of `Θ_(0,+)` below 6 and an eigenvalue of `Θ_(0,−)` above 49/6. Because `|p−q|≤1` and `sin(2x)/x>0` for `0<|x|≤1`, E(p,q) is **strictly positive** throughout the band.

Consider the lowest eigenvalue of `T−0.8E`. Taking the absolute value of a trial function leaves its T quadratic form unchanged and cannot increase its energy; strict positivity of E makes equality for an eigenvector possible only when its phase is constant almost everywhere. The eigenvalue equation then forces a nonnegative lowest eigenvector b to be strictly positive almost everywhere:

```text
b(p) = 0.8 (E b)(p) / [T(p)−θ_low] > 0.
```

Two linearly independent lowest eigenvectors could be chosen orthogonal, but each would have constant phase and be strictly positive, which is impossible. The lowest eigenvalue is therefore simple. Applying the same argument to `−(T+0.8E)` proves the highest eigenvalue of `Θ_(0,−)` is simple and its eigenvector can also be chosen strictly positive. The same eigenvectors apply for h=1.

For either normalized positive extremal b, write `u=p+6.5`, so |u|<1/2. Its geometry-slice amplitude is

```text
⟨a_α,b⟩ = exp(−i6.5α)/√(2π) ∫_I exp(iuα) b(p) dp.
```

For `|α|<π`, `cos(uα)>0` throughout I. Hence

```text
|⟨a_α,b⟩| ≥ cos(|α|/2) ⟨a_0,b⟩ > 0,     |α|<π.
```

Both extremal bound states are therefore contained in K_α on **every** slice in this interval, including α=0, irrespective of the almost-everywhere a.c. qualification. For any other simple eigenstate b, its compact-band Fourier transform is a nonzero entire function, so the values of α at which it is invisible form at most a discrete set. Since a separable Hilbert space has at most countably many distinct eigenvalues, almost every α sees all simple eigenstates. A degenerate eigenspace may still have directions orthogonal to `P_e a_α`, which one scalar slice cannot recover.

Finite-grid checks reproduce the expected positive edge vectors and their nonvanishing central overlaps. At N=80 the two α=0 overlap magnitudes are about 0.18684 and 0.16484. These numbers illustrate the proof; they are not continuum error estimates.

## 4. What remains and what this does not mean

The mathematical result locates the remaining obstruction more sharply. In this model it is **not** necessary to discard the entire scattering sector, nor the known extremal bound states. For almost every slice in the central geometry interval, both are recoverable from the exact complex solution data. The unresolved complement consists of whatever singular-continuous directions or degenerate point-spectrum directions the slice fails to see. We have not proved that those parts exist or that they are absent.

This is not equivalent to saying a finite detector measures a complete quantum state: it assumes the exact complex signal for all scalar φ and the physical spectral measure, and inverse reconstruction can be unstable. It is not a globally covariant real-valued clock POVM; the prior no-go from a bound eigenstate still holds. The window-first-reading instrument is a different, finite, backreacting protocol. The current proof does not show that an instantaneous local geometry-clock Hamiltonian exists, that the α=0 a.c. sector is fully visible, or that independently quantized clock choices coincide.

The model remains homogeneous, momentum-band-projected and nonlocal in α. It does not establish the inhomogeneous constraint algebra, actual experiences, a fundamental whole energy or zero's derivation of the chosen ingredients. No physical or experiential cancellation is inferred from the spectral theorem, and local suffering is not erased.

## 5. Next calculation

The decisive remaining spectral task is to analyze the actual analytic-kernel operator for **singular-continuous spectrum and eigenvalue multiplicity**, and to determine whether particular useful slices, especially α=0, are cyclic on the a.c. sector. If the full spectrum is simple and has no singular-continuous part, the argument above would give a full-state slice map for almost every α; this conditional implication is not a proof of those premises. Then transport the entire first-reading instrument through the continuum map, including channel overlaps and domain-changing operations, and replace ideal all-φ data and scheduled checkpoints with a genuinely physical clock/detector model.

## Reproduce

```sh
python -m unittest verification.zero_interacting_geometry_clock_cyclicity_test -v
```

The tests check kernel positivity, finite edge vectors, the central-interval overlap bound, totality of a finite Fourier family, a free-sector control and a multiplicity-two counterexample. They do **not** establish continuum cyclicity, uniqueness of all bound modes or absence of singular-continuous spectrum; those are analytically argued or explicitly left open above.
