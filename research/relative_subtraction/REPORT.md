# Constructive step 26: a common-regulator limit for relative conformal stress

## Result and scope

[Step 25](../conformal_stress/REPORT.md) evaluated a continuum massless point-split stress prescription. This step supplies an explicit **regulator-to-subtraction bridge for its relative state contribution**: apply one common smooth regulator to the two current distributions, subtract, and take the joint regulator/coincidence limit. A local uniform bound proves that this limit is independent of the path to zero.

A counterexample shows why this is not automatic: placing the same numerical imaginary cutoff in two differently scaled coordinate denominators can invent a finite stress even for an affine map, whose correct Schwarzian stress is zero. Merely assuming cutoff/separation tends to zero is not enough for that mismatched procedure.

This is a continuum massless relative-renormalization result. It is not a Wilson-lattice stress theorem, a massive Hadamard analysis, or a derivation of the absolute geometric anomaly. The latter still uses the explicitly specified Ward prescription of step 25. Thirty-two new checks accompany the analytic argument.

## 1. Fix the two states and the shared singular part

At midpoint u use the conformal chiral state defined by a smooth increasing map f and the reference inertial vacuum of step 25. With symmetric separation h,

\[
D_f(u,h)=\frac{f'(u-h/2)f'(u+h/2)}
{(f(u+h/2)-f(u-h/2))^2},\qquad D_0(h)=h^{-2}.
\]

These denote off-diagonal values of current distributions with the same Wightman boundary prescription. The current normalization is -1/(4π²) times this kernel and T_uu=π:JJ:, so the relative state stress will be -1/(4π) times the finite remainder.

The states, CAR positivity and kernel normalization are those specified previously; the auxiliary regulator is not a newly selected physical state. We do not claim that every mollified individual kernel itself defines a positive CAR covariance.

### Smoothness is the key input, and here it can be proved

Write

\[
f(u+h/2)-f(u-h/2)=hA(u,h),\qquad
A(u,h)=\int_{-1/2}^{1/2}f'(u+sh)ds,
\]

and B(u,h)=f'(u-h/2)f'(u+h/2). A and B are smooth and even in h, with A(u,0)=f'(u)>0 and B(u,0)=A(u,0)². Thus

\[
F_f(u,h):=D_f(u,h)-h^{-2}
=\frac{B(u,h)-A(u,h)^2}{h^2A(u,h)^2}
\]

extends smoothly and evenly through h=0 by division of a smooth even numerator vanishing to second order. Taylor expansion gives

\[
F_f(u,0)=\frac16\{f,u\},\qquad
\partial_hF_f(u,0)=0.
\]

For these conformal current states, the common boundary-value prescription cancels the singular contact part as well; it is not enough to equate off-diagonal values while permitting arbitrary extra delta distributions. For analytic maps this follows directly by the common analytic continuation below; for the smooth pulled-back current distributions the same universal singular extension is fixed by their shared Wightman prescription.

Choose a local neighborhood |h|≤R. Smoothness gives a finite C_R with

\[
|F_f(u,h)-F_f(u,0)|\le C_Rh^2.
\]

On compact midpoint sets the bound is uniform if f' stays positive and the necessary derivatives remain bounded there. This is the control absent from weak distributional or bounded-field convergence alone.

## 2. Apply one linear smoothing operator, not two incompatible cutoffs

Let η be a nonnegative even C_c^∞ function supported on [-1,1], with integral one, and define

\[
(\mathcal R_\epsilon F)(h)
=\int\eta(s)F(h-\epsilon s)ds.
\]

The same convolution is well defined on each localized current distribution. Linearity gives

\[
\mathcal R_\epsilon D_f-\mathcal R_\epsilon D_0
=\mathcal R_\epsilon(D_f-D_0)
=\mathcal R_\epsilon F_f.
\]

This is a mathematical common-regulator identity, not a suggestion to numerically integrate a singular distribution as an ordinary function. After subtraction, the smooth remainder is the stable evaluation route.

For |h|+ε<R, with m₂=∫s²η(s)ds≤1, the evenness of η gives

\[
\left|(\mathcal R_\epsilon F_f)(u,h)-F_f(u,0)\right|
\le C_R(h^2+\epsilon^2m_2).
\]

Therefore h→0 and ε→0 may follow **any joint path**, and the iterated limits agree. No artificial hierarchy ε=o(h²) is needed for this properly shared smoothing of the relative distribution. Different normalized kernels in this class give the same limit.

The resulting relative stress is

\[
\Delta\langle T_{uu}(u)\rangle
=-\frac1{4\pi}\lim_{h,\epsilon\to0}(\mathcal R_\epsilon F_f)(u,h)
=-\frac1{24\pi}\{f,u\}.
\]

The analogous result holds in the v sector. This establishes the previous subtraction as the limit of a specified regulator family, rather than just the value of a formal Taylor coefficient.

## 3. A nontrivial exact remainder avoids numerical cancellation

For the global increasing map f(u)=u+αu³, α≥0, direct algebra gives

\[
F_f(u,h)=
\frac{\alpha-6\alpha^2u^2+\tfrac12\alpha^2h^2}
{(1+3\alpha u^2+\alpha h^2/4)^2}.
\]

This expression is regular at zero and exactly equals the difference of the singular real kernels away from zero. It permits stable evaluation without subtracting two numbers of order h^-2. The code compares it with the high-precision direct split of step 25.

Put A=1+3αu², B=α/4, N₀=α-6α²u² and N₂=α²/2. Then

\[
F_f(u,z)-F_f(u,0)
=z^2\frac{N_2A^2-2N_0AB-N_0B^2z^2}
{A^2(A+Bz^2)^2}.
\]

On |z|≤R with BR²<A, this yields the explicit real/complex bound

\[
|F_f(u,z)-F_f(u,0)|
\le |z|^2\frac{N_2A^2+2|N_0|AB+|N_0|B^2R^2}
{A^2(A-BR^2)^2}.
\]

The tests check both real and complex points against this bound. The mollifier numerics use normalized midpoint quadrature of the smooth remainder with two smooth bump profiles. This quadrature approximates the continuum convolution; its finite sampling is not used as a definition of convolution on the original singular distributions.

## 4. A second matched regulator for analytic maps

For a real-analytic map, evaluate the **whole** point-split expression at the same complex source separation z=h-iε: both f arguments and both Jacobians are analytically continued, and the reference is 1/z². The subtracted result is precisely F_f(u,z), not an expression obtained by adding an unrelated cutoff only after changing coordinates.

For the cubic example the bound above proves

\[
|F_f(u,h-i\epsilon)-F_f(u,0)|
\le C_R(h^2+\epsilon^2).
\]

It has the same joint limit, including h=0 first or ε much larger than h while both go to zero. Intermediate complex values are auxiliary Wightman regularizations; the coincidence limit is real. General smooth maps need not admit a chosen holomorphic extension, so the real common-mollifier construction is the more general result here.

This regulator-independence is local and relative, for the declared state class and common singular prescription. It is not a theorem that all possible cutoffs, orderings, or local counterterms give the same absolute stress.

## 5. A false finite stress from mismatched coordinate cutoffs

The affine map f(u)=au, a>0, has zero Schwarzian and represents the same line vacuum for this calculation. Suppose instead one uses

\[
D_{f,\epsilon}^{\rm bad}(h)=\frac{a^2}{(ah-i\epsilon)^2},
\qquad D_{0,\epsilon}^{\rm bad}(h)=\frac1{(h-i\epsilon)^2}.
\]

The same numerical ε is a length in two different coordinate scales. These are not the same finite-resolution smoothing operator on the source distribution. Their separate boundary values are correct, but moving-point coincidence evaluation is not a continuous operation justified just by distributional convergence.

For the Hermitian real part and ε/h→0,

\[
\operatorname{Re}(D_{f,\epsilon}^{\rm bad}-D_{0,\epsilon}^{\rm bad})
=3(1-a^{-2})\frac{\epsilon^2}{h^4}
+O(\epsilon^4/h^6).
\]

Taking ε=λh² gives the spurious finite limit 3λ²(1-a^-2), even though ε/h→0 and the correct answer is zero. With a=2,λ=1 it is 9/4. A slower cutoff removal can diverge; ε=o(h²) suffices to suppress this affine real-part artifact. Controlling the full complex difference would require the stronger ε=o(h³) for its leading imaginary term. These hierarchies repair this particular bad path; they are not universal laws of point splitting.

Taking ε→0 first at fixed h gives zero, whereas taking h→0 first at fixed ε gives -(a²-1)/ε². The noncommuting limits are explicit. Transporting the affine cutoff correctly as aε in the transformed denominator instead gives exactly zero for every h,ε. The general common-regulator constructions above avoid this coordinate mismatch from the outset.

A finite regulated difference is therefore not by itself a renormalized observable. Counterterm matching, a common geometric resolution, and limit control matter.

## 6. What this adds to the curved stress calculation

On the same admitted background g=exp(2σ)du dv, keep the geometric terms and finite normalization prescribed in step 25. The relative subtraction supplies the state additions Δt_u(u), Δt_v(v). Its trace is zero and its crossed derivatives vanish, so it changes neither the anomaly nor conservation:

\[
\Delta T_{uu}=\Delta t_u(u),\quad
\Delta T_{uv}=0,\quad
\Delta T_{vv}=\Delta t_v(v),
\qquad \nabla^a\Delta T_{ab}=0.
\]

The relative tensor transforms ordinarily when **both physical states** are transformed. Each individual normal-ordering state function has the same coordinate Schwarzian term, which cancels in their difference. Resetting the reference to a different chart vacuum would instead change the state being compared.

Any common finite cosmological term Cg_ab also cancels in the relative difference. That makes relative state comparisons better determined than absolute gravitational energy. It does not select C or derive the geometric cR/(24π) anomaly: those remain renormalization inputs of the absolute prescription. A chart-based smoothing operator need not be covariant at finite ε; the relative coincidence limit has the tensor transformation law just established.

The code verifies the full prescribed curved stress limit after adding the independently specified geometric terms, on both static and time-dependent metric jets. This checks compatibility of the two constructions, not a new derivation of the absolute Ward prescription from the regulator.

## 7. The lattice bridge is still a distinct problem

Neither a Wilson spatial cutoff a nor a central-difference ground-state theorem automatically gives the common distributional smoothing used here. To identify one with this composite limit one would need, at minimum:

1. a concrete regulated current/stress operator and its matched reference/parametrix;
2. estimates on its short-distance kernel remainder, not just fixed smeared CAR expectations;
3. control of the coincidence or derivative limit jointly with a→0, including any contact terms;
4. restoration of the intended covariance, conservation and anomaly, with finite normalization choices fixed.

The massive gap proof of steps 23–24 cannot simply be invoked in the present massless sector, and the Wilson axial-breaking term cannot be dropped before an ultraviolet-sensitive calculation without justification. This step earns a genuine continuum regulator-to-subtraction map while leaving that harder source identification visible.

## 8. Reproducibility and explanatory ledger

Run `python -m unittest -v test_model.py` here, or `python research/run_checks.py` from the repository root. The 32 tests cover the exact smooth remainder, local real/complex bounds, common convolution and analytic joint limits, direct off-diagonal linearity, two smoothing profiles, the affine fake-stress witness, unsafe/safe paths, relative covariance/conservation/counterterm cancellation, and compatibility with the previous curved expectation. Singular cancellations use Decimal precision where needed. `enumeration.json` records errors and the false finite affine limit.

**Earned:** a specified common-regulator convergence theorem for a nontrivial massless relative composite expectation, with explicit uniform error control and a counterexample to weaker cutoff matching.

**Not earned:** a massive or massless Wilson stress-tensor theorem, a universal absolute subtraction without renormalization conditions, operator-valued stress fluctuations, backreaction, empirical selection, all-framework integration, phenomenal constitution, or ultimate explanation. Neither a regulated finite number nor a regulator-independent prediction identifies an actual observer or constitutive realization token.

**Next obligation:** construct the corresponding local kernel estimates for a genuinely spatial lattice/current regulator, or specify a gravitational dynamics before attempting backreaction. Common labels or fixed-observable convergence cannot substitute for that estimate.

## Continuation: an actual spatial-CAR composite

[Step 27](../cell_current_limit/REPORT.md) constructs finite cell modes, positive lattice states and a current-product observable, with a kernel estimate for its relative stress limit. A fixed-cell-count shape factor distinguishes this from simply sampling the continuum formula. The states are explicit continuum compressions, not independently identified Wilson or Floquet ground states.
