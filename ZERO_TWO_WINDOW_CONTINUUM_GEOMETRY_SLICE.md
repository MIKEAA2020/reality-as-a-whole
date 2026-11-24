# Geometry slices for two autonomous records: a multichannel continuum result

## Result

The [two-window model](ZERO_AUTONOMOUS_TWO_GEOMETRY_WINDOW_RECORDS.md) is a genuinely noncommuting geometry–pointer interaction, so the earlier scalar-channel slice proof cannot be copied unchanged. Nevertheless, its **complete complex geometry-slice signal**, with all pointer and memory components retained, determines its entire absolutely continuous (scattering) state for almost every α. This holds at the **actual chosen couplings**, simultaneously for both logical h levels and all four memory-y sectors. For any two such slices there is an exact unitary transport of scattering solution data, with the physical inner product transported with it.

There are also bound states: in every memory-y sector, at least one eigenvalue lies below and at least one above that sector's free band. Analytic Fredholm continuation gives no singular-continuous spectrum; any embedded eigenvalues in the band interior can occur only at a locally discrete set. What remains open is whether a single slice sees **every direction of every possibly degenerate bound eigenspace**. Thus the scattering clock switch is established, but a full-state clock switch is **not** asserted.

The result uses the complete complex solution for all scalar φ and internal components, not one finite measurement or a physically readable wavefunction. An almost-everywhere slice need not be α=0 or a monotonic observable clock. A bound state rules out a normalized real-valued globally covariant time POVM on the full sector. This is a specified constrained toy model, not a full quantum-gravity or subjective-time solution.

[Verification](verification/zero_two_window_continuum_slice_test.py) supplies finite-grid and independent stationary-scattering checks, not the continuum proof. The operator-theoretic inputs are the standard [Kato–Rosenblum theorem](https://arxiv.org/html/1211.6694) and [analytic Fredholm theorem](https://arxiv.org/pdf/2304.03989); their application to this specific kernel is the argument below, not a claim made by those sources.

## 1. Four two-component channels—not eight independent scalar channels

Let `I=(−7,−6)`, `T(p)=p²/6`, and `h=0,1`. With the three translated positive effects `E_a` of the previous report, the positive operator is

```text
Θ_h = T−2h − 2λ E_(−5) σ_yᴰ
            − 2κ₁ E_0 P₁ᴰ σ_yᴹ¹ − 2κ₂ E_5 P₁ᴰ σ_yᴹ²,
λ=0.5, κ₁=κ₂=0.65,  P₁ᴰ=(I−σ_zᴰ)/2,  Ω_h=√Θ_h.
```

The two memory operators commute with Θ_h and with each other, even though the geometry windows do not commute and `σ_yᴰ` does not commute with `P₁ᴰ`. Write `m=(m₁,m₂)∈{−1,+1}²` for their eigenvalues. In that basis,

```text
Θ_(h,m)=T−2h+V_m,
V_m=− E_(−5) σ_yᴰ − 1.3(m₁ E_0+m₂ E_5) P₁ᴰ.
```

Each V_m is a Hermitian **2×2 matrix-valued integral operator** with entire kernel in p and q. Its two pointer components cannot generally be independently diagonalized by one constant rotation. Memory-z record probabilities mix m sectors; the conserved y-labels are a calculational decomposition, not the z-records themselves.

For every a, `E_a≥0` is trace class with `tr E_a=2/π`: its continuous positive kernel has constant diagonal `2/π` on a band of length one. Consequently every V_m is trace class. The free T is strictly monotone on I, so by Kato–Rosenblum the a.c. part of `Θ_(h,m)` has the free band `[6−2h,49/6−2h]` with multiplicity two and is unitarily equivalent to the free multiplication operator. The positive square root is a smooth strictly increasing spectral change; the same conclusion holds for Ω. Summing the four m channels gives multiplicity eight per labelled h sector. This equivalence says **nothing by itself** about the singular or point spectrum.

## 2. Why one complete slice sees the scattering sector

Write a=(−7), b=(−6), and fix a channel m and an interior momentum `k∈(a,b)`; the unshifted free energy is `T(k)`. Consider the incoming two-column generalized eigenfunction, using the outgoing resolvent sign convention

```text
ψ_k(p)=δ(p−k) I₂ − [T(p)−T(k)−i0]⁻¹ u_k(p),
u_k(p)=V_m(p,k) − ∫ V_m(p,q)[T(q)−T(k)−i0]⁻¹u_k(q)dq.
```

The following standard stationary construction can be made explicit for this particular entire finite-band kernel. On a Banach space of functions holomorphic in a complex neighborhood of `[a,b]`, the integral operator in the u equation is compact: the p-dependence is entire, with uniform bounds on a slightly larger neighborhood. For k in a neighborhood of an interior real point, subtract the value of the analytic numerator at q=k. The remaining integral is nonsingular and holomorphic in k; the subtracted part is an explicitly continued logarithm plus the on-shell residue. This gives an analytic compact operator family.

For complex k with `Im T(k)>0`, the equation is invertible: a nonzero homogeneous solution would give a non-real eigenvalue of the self-adjoint operator T+V_m. Analytic Fredholm theory then gives an inverse meromorphic in a complex neighborhood of each interior real k. Hence, except at a **locally discrete** set of k, `u_k(p)` exists and is analytic in p. Its boundary values are the usual stationary scattering eigenfunctions; equivalently, they represent the wave-operator spectral transform provided by Kato–Rosenblum. The two columns span the two incoming channels at almost every k. The h shift and monotone square root change the energy label and normalization, not these eigenvectors.

Now define the 2×2 slice matrix (an irrelevant common `1/√(2π)` is suppressed)

```text
F_m(α,k) = ∫_a^b exp(ipα) ψ_k(p) dp.
```

The integral is distributional. Because ψ_k has compact p-support, each entry of F_m is **entire in complex α**. The crucial point is that its determinant is not identically zero. Here `T′(k)<0`, so the boundary value above has a `(p−k+i0)⁻¹` singularity. Subtract `u_k(k)` and use the Riemann–Lebesgue lemma on the integrable remainder. The singular term satisfies

```text
∫ exp(ipα)[T(p)−T(k)−i0]⁻¹u_k(p)dp
    = o(1)                                      as α→+∞,
exp(−ikα) F_m(α,k) = I₂ + o(1)                 as α→+∞.
```

This is the incoming-side asymptotic; the opposite side contains the on-shell scattering matrix. The sign depends on the chosen resolvent convention and the negative slope of T. In particular, for each regular k, `det F_m(·,k)` is a nonzero entire function. Its real zeros have measure zero.

Fubini now gives, for **almost every real α**, an invertible `F_m(α,k)` for almost every k. The intersection of the good sets for four m and two h labels still has full measure. At such α, the full two-component slice signal in each m channel, for all φ, determines the two scattering amplitudes at almost every spectral value. Spectral separation of absolutely continuous and point measures prevents a bound component from mimicking the a.c. density.

This is why retaining internal labels matters: with only one pointer component, the spectral fibre is a row mapping two amplitudes to one, with a nontrivial kernel at each energy. Likewise, tracing out memory is not a harmless change of representation.

## 3. Singular spectrum and bound states

The same analytic Fredholm construction gives a further spectral classification, without assuming that all bound eigenvalues are simple. For analytic test vectors, the upper-half-plane resolvent matrix element continues meromorphically across any compact subinterval of the free-band interior: its free Cauchy transform is continued by the same subtraction, and the perturbed term uses the meromorphic inverse above. Away from its locally discrete poles its boundary value is locally bounded. The Stieltjes inversion formula then gives an absolutely continuous spectral measure there; the analytic test vectors form a dense set. Therefore no singular-continuous spectral projection is supported in the open band away from the pole set. A countable set, including the two thresholds, cannot support a singular-continuous measure. Outside the free band, compactness of V_m leaves only isolated finite-multiplicity eigenvalues, with possible accumulation at the thresholds. Thus **the singular-continuous subspace is zero**. Possible interior embedded eigenvalues are confined to the locally discrete Fredholm pole set; their absence is not claimed.

The point sector is nonempty, and actually lies on **both sides** of each channel's free band. At either endpoint the 2×2 kernel is

```text
V_m(p_edge,p_edge) = (2/π)[−σ_yᴰ − 1.3(m₁+m₂)P₁ᴰ],
det V_m(p_edge,p_edge) = −4/π² < 0.
```

It therefore has one strictly negative and one strictly positive eigenvalue. To see that each sign creates an exterior eigenvalue, choose the appropriate endpoint eigenvector v and the normalized real trial profile `f_ε(x)=c_ε/(x+ε)` for distance `0<x<δ` from that endpoint, zero elsewhere. As ε→0, `c_ε²∼ε`, the free kinetic displacement from the edge is `O(ε log(1/ε))`, and the leading interaction term is

```text
⟨v,V_m(edge,edge)v⟩ · ε log²(1/ε) + O(ε log(1/ε)).
```

The leading interaction dominates with the chosen sign. The variational principle gives one state below the lower edge and one above the upper edge. This is a continuum existence argument; it does **not** count all bound states or show their degeneracies.

For a simple eigenstate, its nonzero vector-valued slice amplitude is entire, so it is visible on almost every α. For a degenerate eigenspace one must examine the rank of the 2-component evaluation map on that eigenspace; mere analyticity of each vector does not prove simultaneous recovery. This is the remaining full-state obstruction in the present analysis. The h and m labels must also be retained when distinguishing overlapping eigenfrequencies.

Any normalizable bound eigenstate rules out a normalized POVM on the whole sector that is covariant under all real scalar translations: the associated probability measure would have to be invariant under every translation of ℝ, which no normalized probability measure is. This does not rule out finite-resolution clocks, restricted scattering-sector clocks, or a different operational time observable.

## 4. Actual clock-slice transport

Choose h,m and a scattering spectral representation `L²(J_h,dE;C²)` normalized so the physical norm is `∫||c(E)||² dE`. Absorb the smooth free density, `1/√(2π)` and the covariant-solution factor `(2Ω)⁻¹/2` into an invertible matrix `A_(h,m)(α,E)`, proportional to F_m evaluated at the corresponding k. The complex slice signal determines its a.c. Fourier density

```text
b_α(E)=A_(h,m)(α,E)c(E).
```

For two good slices α,β, define on the physical data domain

```text
b_β(E)=A_(h,m)(β,E) A_(h,m)(α,E)⁻¹ b_α(E),
||b_α||²_phys=∫ ||A_(h,m)(α,E)⁻¹ b_α(E)||² dE.
```

This is a unitary **change of representation** on the a.c. scattering subspace, not a claim that the transfer matrix is unitary in the naive Euclidean norm of b. Inverse matrices can be poorly conditioned or unbounded; the physical data domain and norm are essential. Record observables, including M_z which mixes m channels, must be transported by the full representation maps, including interchannel overlaps and frequency shifts. In particular, the memory probabilities from the original packet can be recovered from its **a.c. projection** using either slice and the same transported observables. The original packet may also contain bound components, so the reported total probabilities cannot yet be claimed to follow from this a.c.-only map.

A finite-resolution measurement of α, a finite φ interval, or probabilities rather than the full complex signal defines a different information problem. No claim is made that this mathematical map implements a practical clock or selects an outcome.

## 5. Checks and next target

[The test](verification/zero_two_window_continuum_slice_test.py) checks the exact spin-block reduction, Hermiticity, indefinite edge kernel, finite-grid exterior levels, and an independently discretized Lippmann–Schwinger equation using principal-value subtraction. It checks on-shell scattering unitarity, convergence at selected momenta and slices, incoming-side asymptotics, and a two-component transport example. None of these finite computations proves the continuum statements or identifies all exceptional slices.

Next, determine the **rank of geometry evaluation on each bound eigenspace**, including possible degeneracies and thresholds. A successful result would extend this clock switch to the full state; a rank failure would identify information genuinely unavailable to that slice. Separately, finite clocks, local interactions and subject incidence require additional physics. Neither vanishing constraint nor unitary records establish a globally signed energy or experiential total, and local suffering is not cancelled away by a proposed whole-level balance.

## Reproduce

```sh
python -m pip install --target .arena/python-deps numpy  # if needed
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest verification.zero_two_window_continuum_slice_test -v
```
