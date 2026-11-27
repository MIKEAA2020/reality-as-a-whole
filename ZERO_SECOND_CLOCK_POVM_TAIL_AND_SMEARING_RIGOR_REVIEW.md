# Second-clock POVM, tails and centered smearing: rigor recheck

## Results and limits

This pass checks selected continuum claims in [the second-clock construction](ZERO_TWO_WINDOW_SECOND_PHYSICAL_CLOCK.md) and [the retained-clock instrument analysis](ZERO_RETAINED_CLOCK_INSTRUMENT_AMBIGUITY.md). For their **specified** semibounded clock, bin, product preparation, cursor instrument and output convention:

* The covariant clock POVM is normalized; its orbit-integrated joint memory effects are positive, normalized and invariant in the stated physical representation. A finite-bin clock effect is generally **not a projection**.
* A direct oscillatory tail estimate tightens the clock-window tail from `<0.0000177` to `<0.00000955`.
* The clock kernel is centered. Using cancellation of the first-order unitary time shift improves the stipulated smeared-instrument half-diamond comparison from the previous `<0.0388` to **`<0.03777`**. For initial P-only or Q-only inputs, the corresponding clock-smeared false/missed memory-record probability is conditionally `<0.0003416`.

These are analytic bounds for a particular altered constraint and chosen preparation; the comparison still inherits the [cursor-domain/instrument estimates](ZERO_CURSOR_DOMAIN_INSTRUMENT_RIGOR_REVIEW.md). It is not an independently implemented physical clock, a unique instrument, an operational quantum-frame switch or a derivation of effective spacetime. Space and time remain non-fundamental constructs in the current programme, and experience is intrinsic; a clock outcome or mathematical record is not thereby a subject or a felt event.

## 1. Positive-frequency POVM and weak normalization

Let `H_R=L²(R_+,dk)` and define the isometry `W:H_R→L²(R,dr)` by extending ψ by zero to negative k and applying the unitary Fourier transform

```text
(Wψ)(r)=(2π)^−1/2 ∫₀∞ e^(−ikr)ψ(k)dk.
E_R(B)=W† χ_B W,                  U_R(t)=e^(iK_R t), K_R=k.
```

The integral is defined in the L² sense. Plancherel gives `W†W=I`, hence `E_R` is a normalized positive operator-valued measure. Also

```text
W U_R(t)ψ(r)=Wψ(r−t),
∫_R dt U_R(t)† E_R(B) U_R(t) = |B| I
```

as a **weak** operator integral for any finite-measure B. Indeed, for every ψ, Tonelli and a change of variables give the quadratic form `∫_t∫_B |Wψ(r−t)|² dr dt = |B| ||ψ||²`; polarization gives all matrix elements. This does not use a normalizable uniform time state.

The compression is genuinely unsharp. For a bounded interval B of positive length, put `P_B=χ_B` and `P_+=WW†`. Then

```text
E_R(B)−E_R(B)² = W†P_B(I−P_+)P_BW ≥ 0.
```

It is nonzero: choose `ψ(k)=√2 e^(−k)`, for which `Wψ(r)=1/[√π(1+ir)]` is nowhere zero. Its truncation to B is a nonzero compactly supported L² function. Its Fourier transform is entire; it cannot vanish on all negative frequencies without vanishing identically. Thus `P_BWψ` is not in the positive-frequency subspace and the displayed quadratic form is strictly positive for this ψ. The finite-bin effect is not a sharp PVM projection. The numerical negative-frequency calculation in the [test](verification/zero_second_clock_povm_rigor_test.py) is only a control of this analytic argument.

Let `A_m(t)=U_H(t)†Π_mU_H(t)` and `E_t=U_R(t)†E_R(B)U_R(t)`. The positive integrand obeys

```text
0 ≤ A_m(t)⊗E_t ≤ I⊗E_t.
```

Hence its quadratic-form integral is finite even for an **entangled** system–clock input, and polarization defines a bounded operator

```text
F_m=(1/ℓ)∫ dt A_m(t)⊗E_t,        0≤F_m≤I,        Σ_m F_m=I.
```

Shifting t in the weak integral shows commutation with the simultaneous unitary group `U_H(s)⊗U_R(s)`; because F_m is bounded, it commutes with the generator's spectral projections and preserves its domain. This is constraint invariance in the **specified** positive-frequency representation, not a proof of a generally covariant clock theory.

For a product state `ρ_A⊗|β⟩⟨β|`, the effect probability is exactly `∫w_B(r−t)p_m(t)dt`, with the normalized bin-convolved clock density w_B. This product formula is not asserted for arbitrary clock–apparatus correlations. The normalization is the chosen relational-effect normalization, not a literal conditioning on a normalizable flat prior over an infinite scalar time.

## 2. Tail estimate using the oscillation

Write `b=5000`, `ℓ=10^−4`, and choose the source's normalized cosine frequency packet. With `y=bu` and `a=π/2`, its exact dimensionless density is

```text
w(u)/b = (π/2) cos²(y)/(y²−a²)²,
```

with removable singularities at `y=±a`. Its mean is zero and its variance after symmetric bin convolution is

```text
σ_B² = π²/(4b²) + ℓ²/12.
```

For the declared window, `d=(T_ret−T_end)/2` and `Y=b(d−ℓ/2)=25π/2−0.255 > 38.995`. Any bin-convolved reading outside the window requires the unbinned clock variable to lie outside `|y|≥Y`. For `f(y)=(y²−a²)^−2`, positive and decreasing on `y≥Y`,

```text
∫_Y∞ cos²(y) f(y)dy
 = (1/2)∫_Y∞ f(y)dy + (1/2)∫_Y∞ cos(2y)f(y)dy,
|∫_Y∞ cos(2y)f(y)dy| ≤ f(Y).
```

The last line follows by integration by parts and `∫|f′|=f(Y)`. Since `f(y)≤[y⁴(1−(a/Y)²)²]^−1`,

```text
τ_B ≤ π/[3Y³(1−(π/(2Y))²)²] · [1/2+3/(2Y)]
     < 0.00000955.
```

The [rational test](verification/zero_second_clock_povm_rigor_test.py) uses `Y>7799/200` and `π<22/7` to verify the strict threshold without fitting the tail. Numerical quadrature is a separate control, not its proof.

## 3. Centered clock error is quadratic, not merely linear

For the **specified ideal recorded support instrument**, let `L_t` denote projection onto the P/Q outcomes followed by `e^(iΩt)` on the retained system. Put `u=t−r`. The symmetric cosine packet and symmetric bin make `w_B(u)` even, with mean zero and second moment `σ_B²`. The centered ideal mixture is therefore

```text
∫w_B(u) L_(r+u)du − L_r
 = Ad_(e^(iΩr)) ∫w_B(u)[Ad_(e^(iΩu))−I−iu ad_Ω] L_0 du.
```

On trace-class operators, including an untouched reference, `||ad_Ω||≤2||Ω||`. The unitary Duhamel remainder gives

```text
||Ad_(e^(iΩu))X−X−iu[Ω,X]||₁ ≤ 2||Ω||²u² ||X||₁,
(1/2)|| ∫w_B(u) C_L(r+u)du − C_L(r)||_diamond
    ≤ ||Ω||² σ_B².
```

This uses the **whole centered distribution**, not a truncated distribution whose first moment need not vanish. Compare the full actual mixture to the full ideal mixture: use the cursor δ(t) bound inside the window and a worst-case channel distance of 1 on the tails; then compare the full ideal mixture to L_r using the quadratic bound. Thus no tail is discarded or assumed centered by itself.

Substitute the prior `c_*<0.412/(2×1.3)`, verified cursor constants, `||Ω||<3.251`, `σ_B<0.000316`, `τ_B<0.00000955`, and the existing product-preparation/reduction assumptions into the full-channel error budget. Exact rational arithmetic checks

```text
(1/2)||C_J−C_L(r)||_diamond < 0.03777.
```

The old linear `||Ω||σ_B` estimate remains valid but is needlessly loose here. A biased or asymmetric clock kernel generally has a nonzero first moment and can have a first-order error; the new bound must not be transferred to such a clock without recentering or an additional bias term.

On a P-only or Q-only input, the earlier cursor comparison gave `<0.000332` for false/missed memory probability throughout the window. Adding the full out-of-window tail gives `<0.0003416` for the R-smeared memory outcome. This is a sector-specific probability estimate, not a poststate bound; the full-channel estimate remains the appropriate control for general coherent inputs.

## 4. Exact dephasing control and retained-output ambiguity

For the cosine frequency packet, the unsmeared clock characteristic function at a frequency separation Δ is the compact-support autocorrelation

```text
C(u) = (1−|u|/2) cos(π|u|/2) + sin(π|u|/2)/π,  |u|≤2,
C(u) = 0,                                            |u|≥2,
u=Δ/b.
```

The finite bin multiplies this by `sinc(Δℓ/2)`. Thus a comparator qubit with gap Δ=b has residual coherence `sinc(bℓ/2)/π`, and one with gap at least 2b is fully dephased by this ideal clock mixture. These are **separate comparator controls**: the actual two-window Ω spectrum is bounded on the declared band, and no such large gap is asserted for it. Smearing is not generally a sharp clock reading or a fundamental irreversibility law.

The retained-clock report's `K_m(t)=ℓ^−1/2 U(t)†[Π_m⊗√E_R(B)]U(t)` defines a specific complete instrument: the weak identity `Σ_m∫K_m†K_m dt=I` makes `ψ↦(m,t)↦K_m(t)ψ` an isometry into an auxiliary outcome-label space. Partial trace of that label gives CP operations with effects F_m. This is a **choice** of dilation/operation, not a consequence of the effects alone; the abstract Lüders and feedback alternatives in the source can have the same effects but different retained states. The auxiliary orbit label is not a demonstrated physical clock record, and a fiber-dependent scalar-slice identification is an additional convention. The present result neither equates raw retained poststates nor proves a physically implemented R-relative switch.

## 5. Verification and next work

The [new tests](verification/zero_second_clock_povm_rigor_test.py) check the rational tail and improved channel arithmetic, oscillatory tail quadrature, an exponential-clock weak-twirl control, nonprojectivity control, exact cosine-packet autocorrelation and the centered-versus-biased distinction. They do not establish the continuum identities or physical validity merely by executing. The analytic argument depends on the stated Fourier convention, product preparation, finite bin, fixed cursor state and bounded old-system Ω.

Next audit the actual retained/fiber-transport operation and its loss of information, and test clock–apparatus correlations, biased kernels, turning/interacting clocks, state preparation errors and locality. The original constrained model, real physical energy accounting, subject incidence and felt succession remain open.
