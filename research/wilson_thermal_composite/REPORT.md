# Constructive step 28: a relative composite limit from Hamiltonian thermal states

## Result and scope

[Step 27](../cell_current_limit/REPORT.md) constructed a lattice composite in states imported by continuum compression. This step instead starts with an **independently specified massless Wilson Hamiltonian** on the infinite spatial lattice. Its ground and finite-temperature quasifree states determine the covariance directly. Exact kernel formulas then control a relative current-product limit and its agreement with the separately computed thermal Hamiltonian energy density.

The main result uses a mesoscopic split: a→0, h→0, and h/a→infinity. It recovers one chiral relative stress π/(12β²); the sum of both chiralities agrees with relative energy π/(6β²). A mixed-chirality diagnostic vanishes in that limit. At fixed site count, both a normalization factor and a mixing artifact survive.

This is a massless, translation-invariant rescaled-field thermal result, not the previous massive curved ground-state theorem. On a static conformal background it supplies the relative thermal contribution in the chosen conformal/Killing-time state, not the absolute geometric anomaly. It establishes neither full stress operators nor gravitational backreaction. Thirty-two tests accompany the analytic calculations.

## 1. Hamiltonian and state selection are now source inputs

Use the infinite lattice H_a=ℓ²(Z,C²), with θ=ka in [-π,π). For Wilson parameter r=1 and m=0,

\[
h_a(\theta)=\frac{\sin\theta}{a}Z+
\frac{1-\cos\theta}{a}X,
\qquad E_a(\theta)=\frac{2|\sin(\theta/2)|}{a}.
\]

This is the nearest-neighbor continuous-time Hamiltonian of step 24 in its massless limit. It has one low-energy zero at θ=0 and no low-energy zone-edge doubler. It is gapless, so the earlier positive-mass uniform-gap proof is **not** being used.

Specify the ground covariance and thermal covariance by functional calculus:

\[
C_{0,a}=1_{(-\infty,0)}(H_a),\qquad
C_{\beta,a}=(I+e^{\beta H_a})^{-1},\quad\beta>0.
\]

The zero at a single momentum has zero spectral measure on the infinite lattice, so its assigned value does not change C₀. The thermal value is 1/2 at zero. Each covariance is a positive contraction, defines a gauge-invariant quasifree CAR state, and commutes with H_a. The thermal occupation obeys f(E)/(1-f(E))=exp(-βE), the free CAR equilibrium/KMS condition. No finite global density matrix or partition function on the infinite lattice is assumed.

Temperature is an explicit state input. Neither the geometry nor the lattice chooses β. Unlike step 27, no continuum conformal covariance is compressed to define these states.

## 2. Exact ground kernels resolve the ultraviolet structure

At nonzero θ the ground projector is

\[
C_{0,a}(\theta)=\frac12\left[I-
\operatorname{sgn}(\theta)\cos(\theta/2)Z
-|\sin(\theta/2)|X\right].
\]

Its thermal version multiplies the two matrix-vector terms by tanh(βE_a/2). Both spin components have diagonal site occupation 1/2. Fourier integration gives for n≥1

\[
(C_{0,a})_{\uparrow\uparrow}(n)
=-\frac{i}{2\pi}\frac{n}{n^2-1/4},\qquad
(C_{0,a})_{\uparrow\downarrow}(n)
=\frac1{4\pi(n^2-1/4)}.
\]

The down-down kernel is the conjugate of the up-up one. The off-diagonal spin kernel demonstrates that the chiral components are not independent at finite spacing; Wilson's X term mixes them.

These formulas are properties of the Hamiltonian projection, not continuum cell averages. The shape factor will therefore differ from step 27. As a control, the massless central regulator instead has an up-up kernel proportional to (1-(-1)^n)/n, with a zone-edge/parity contribution. It cannot simply be substituted into the Wilson estimates below.

## 3. A thermal kernel remainder with a uniform integrable bound

Set

\[
F_\beta(p)=1-\tanh(\beta p/2)=\frac2{e^{\beta p}+1},
\qquad q_a(p)=\frac2a\arcsin(ap/2),\quad0\le p\le2/a.
\]

The variable p is the positive Wilson energy. Changing variables p=2sin(θ/2)/a in the Fourier kernel gives, with h=na,

\[
(C_{\beta,a})_{\uparrow\uparrow}(n)
=-\frac{ia}{2\pi}\kappa_{\beta,a}(h),
\]

where

\[
\kappa_{0,a}(h)=\frac{W_n}{h},\quad
W_n=\frac{n^2}{n^2-1/4},\qquad
\delta\kappa_a(h):=\kappa_{\beta,a}-\kappa_{0,a}
=-\int_0^{2/a}\sin(hq_a(p))F_\beta(p)dp.
\]

The crucial estimate is q_a(p)≤πp/2. Therefore

\[
\left|\frac{\sin(hq_a(p))}{h}F_\beta(p)\right|
\le\frac\pi2 pF_\beta(p),
\]

an integrable majorant independent of a,h. At every fixed p, q_a(p)→p and sin(hq_a)/h→p as a,h→0. Dominated convergence gives

\[
\frac{\delta\kappa_a(h)}h\longrightarrow-I_1,
\quad I_1=\int_0^\infty pF_\beta(p)dp=\frac{\pi^2}{6\beta^2}.
\]

This is the needed short-distance control, derived from the Hamiltonian thermal kernel rather than inferred from convergence on fixed bounded fields.

### A quantitative version

On p≤1/a, q_a-p≤a²p³/12 and |sin(hq_a)/h-q_a|≤h²q_a³/6. Splitting the tail at 1/a yields

\[
\left|\delta\kappa_a/h+I_1\right|
\le\left(\frac{\pi^3h^2}{48}+\frac{a^2}{12}\right)I_3
+(1+\pi/2)\,2e^{-\beta/a}
\left(\frac1{a\beta}+\frac1{\beta^2}\right),
\]

where I₃=7π⁴/(60β⁴). The exponential tail bounds use Fβ≤2exp(-βp). This estimate controls the joint coincidence/spacing limit and does not require a fictitious mass gap.

## 4. The actual lattice current product

For up modes at sites j,j+n define

\[
J_{j,\uparrow}^a=(c_{j,\uparrow}^*c_{j,\uparrow}-1/2)/a,
\qquad O_{a,n}=\pi J_{j,\uparrow}^aJ_{j+n,\uparrow}^a.
\]

The same even self-adjoint operator is evaluated in the two Hamiltonian states. It has norm π/(4a²). Its relative expectation is exactly

\[
\Delta S_{a,n}=-\frac1{4\pi}
\left(2\frac{W_n}{h}\delta\kappa_a+(\delta\kappa_a)^2\right).
\]

The finite two-mode Fock density construction from step 27 realizes the appropriate positive covariance compression. Matrix traces agree with this Wick expression. The code evaluates δκ/h first to avoid cancellation and amplification of two singular numerical squares.

Let t_β=I₁/(2π)=π/(12β²). Then:

- If a,h→0 and n=h/a→infinity, **ΔS_a,n→t_β**, without a finite normalization adjustment.
- At fixed n, **ΔS_a,n→W_n t_β**, not t_β.
- Dividing this same-chirality observable by W_n gives the target at fixed n, but does not by itself repair all mixed or tensor observables.

Writing r=δκ/h, the useful finite-error bound is

\[
|\Delta S_{a,n}-W_nt_\beta|
\le\frac{W_n}{2\pi}|r+I_1|
+\frac{h^2}{4\pi}(\pi I_1/2)^2.
\]

For the mesoscopic raw observable add (W_n-1)t_β, with W_n-1=1/(4n²-1). This gives explicit control of both the thermal kernel and finite-separation normalization.

## 5. A mixing artifact survives fixed site count

The thermal change of the mixed-spin kernel is

\[
\delta C_{\uparrow\downarrow}(n)
=\frac{a^2}{4\pi}\int_0^{2/a}
\frac{p\cos(hq_a(p))F_\beta(p)}{\sqrt{1-(ap/2)^2}}dp.
\]

Splitting at p=1/a controls the integrable endpoint factor: the low part is dominated by (2/sqrt3)pFβ and the high-angle part is exponentially small. It follows that

\[
\delta C_{\uparrow\downarrow}/a^2\longrightarrow I_1/(4\pi)
\]

in the same joint a,h→0 limit. The relative mixed-current product therefore has fixed-n limit

\[
\pi\Delta\langle J_{j,\uparrow}^aJ_{j+n,\downarrow}^a\rangle
\longrightarrow-\frac{t_\beta}{4n^2-1}.
\]

At n→infinity this vanishes; the remaining quadratic term also vanishes as a². Thus the mesoscopic limit suppresses this explicit chirality-mixing artifact, while a same-chirality fixed-n calibration alone does not.

The mixed current product is a diagnostic, **not an asserted definition of T_uv**. Its vanishing does not prove restoration of every axial Ward identity or full stress-operator algebra. It does prevent silently treating the two lattice chiralities as independent before taking the controlled limit.

## 6. Compare with the independently defined Hamiltonian energy

The thermal-minus-ground expectation of H_a per coordinate length is obtained directly from its dispersion and Fermi occupations:

\[
\Delta\varepsilon_a
=\frac1{\pi a}\int_0^\pi E_a(\theta)F_\beta(E_a(\theta))d\theta
=\frac1\pi\int_0^{2/a}
\frac{pF_\beta(p)}{\sqrt{1-(ap/2)^2}}dp.
\]

On p≤1/a use the same integrable domination; the high-energy portion is bounded by 4a^-2exp(-β/a), which vanishes. Hence

\[
\Delta\varepsilon_a\longrightarrow\frac{I_1}{\pi}
=\frac{\pi}{6\beta^2}=2t_\beta.
\]

The two mesoscopic chiral current contributions agree with the Hamiltonian relative energy in the limit. No continuum covariance was used to define either Hamiltonian state. This is an actual source-to-composite bridge in the specified equilibrium sector.

At finite a we do not assert an operator identity between H_a and the sum of these two separated Sugawara products. The Wilson term and mixed correlations make that identification nontrivial. Relative thermal energy is also not an absolute vacuum-energy prediction: the zero-temperature sea contribution has been subtracted in the same regulator.

## 7. Static conformal geometry and what remains unproved

For the massless physical field on a static conformal metric, χ=Ω^(1/2)ψ has the translation-invariant generator pZ. Choosing the χ thermal state at inverse Killing-time temperature β therefore gives a compatible continuum interpretation of this relative limit. The local observer's thermal addition is

\[
\Delta T_{\hat0\hat0}=\frac{2t_\beta}{\Omega^2}
=\frac\pi6\left(\frac1{\beta\Omega}\right)^2.
\]

The same-background thermal-to-ground comparison leaves the previously specified geometric anomaly term unchanged; relative stress has zero trace and is conserved in the continuum equilibrium prescription. This is the Tolman-redshifted thermal contribution, not a derivation of β or a preferred physical state.

The curved **absolute** stress and cR anomaly still require the prescription of step 25. A thermal-minus-vacuum comparison cancels state-independent geometric terms, so it cannot determine them. Nothing here proves the massive static Wilson ground-state stress limit, a non-equilibrium conformal-state theorem, or a time-dependent curved vacuum selection. Nor does this expectation-value calculation establish an operator-valued stress distribution, its fluctuations, backreaction, or interacting universality.

The underlying Hamiltonian is continuous-time and still has nonzero lattice tails outside a strict cone, as earlier. All limiting interpretations remain relative to the admitted geometry, CAR and coupling choices, not deductions of actual laws from order alone.

## 8. Reproducibility and numerical scope

Run `python -m unittest -v test_model.py` here, or `python research/run_checks.py` from the repository root. The 32 tests cover Hamiltonian spectral occupations/stationarity, ground-kernel Fourier integrals, the energy-variable transformation, Fermi moments, the explicit error bound, fixed-n and mesoscopic alternatives, mixed-spin artifacts, direct finite Fock expectations, Hamiltonian energy, and curved relative interpretation. The state construction is on the infinite lattice; these are not finite-circle Gibbs matrices.

Numerical energy integrals use Simpson quadrature on p≤K=min(1/a,40/β). For δκ/h the omitted contribution is bounded by πexp(-βK)(K/β+1/β²), and is below the reported tolerances in the sampled regime. Mixed and energy tails are exponentially bounded by the corresponding arguments above. Quadrature refinement is checked separately. The analytic theorem uses the exact integrals up to 2/a and then their controlled tails; numerical truncation is not treated as an exact identity. Representative data are in `enumeration.json`.

**Earned:** an independently specified Hamiltonian-state relative composite limit; explicit short-distance estimates; agreement with thermal energy; control of one finite-spacing chirality-mixing contribution.

**Not earned:** general massive/non-equilibrium composite convergence, an absolute lattice anomaly/stress theorem, a full operator stress algebra, physical state selection, gravitational dynamics, empirical confirmation, all-framework integration, phenomenal constitution, or ultimate explanation. A Hamiltonian-selected mathematical state still does not establish an actual realization or observer token.

**Next bridge:** move from this soluble thermal difference to state-independent local subtraction or a nonconstant-state kernel estimate. Those are the ingredients needed before claiming the absolute curved stress has emerged from the lattice regulator.

## Continuation

[Step 29](../wilson_nonthermal_universality/REPORT.md) removes the thermal assumption within a compact-energy stationary quasifree class and exhibits distinct states sharing the same limiting stress. It does not remove stationarity or homogeneity.
