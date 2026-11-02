# Constructive step 25: massless conformal point splitting and stress expectations

## Result and scope

[Step 24](../wilson_regulator/REPORT.md) improved a massive regulator but did not justify local composite observables. Here we perform a controlled **continuum massless** calculation: a chiral current kernel has an explicit point-split finite term, and a stated conformal Ward prescription gives a conserved curved-space stress expectation with trace anomaly and state dependence.

This is a new, restricted sector. It is not the massive gapped state of steps 22–24 with m silently set to zero, and it is not a lattice-to-renormalized-stress convergence theorem. We specify the continuum state family, current normalization, anomaly prescription, and finite normalization choices. The output is an expectation-value construction; full operator-valued composite fields, their domains and fluctuations, and massive Hadamard renormalization remain outside the result.

Thirty-two tests check the subtraction limit, Schwarzian identities, tensor covariance, conservation, anomaly, state freedom and finite counterterm. These finite calculations do not derive the continuum Ward prescription from the Wilson regulator.

## 1. The massless sector and its admissible state family

For g=exp(2σ)du dv, the conformal rescaling χ=exp(σ/2)ψ from step 22 makes the **massless** equation chiral and flat in the null coordinates. We use one complex nonchiral Dirac field. Each complex chiral current has central charge one; the common c in the formulas below is c=1. One must not add the two chiralities again and put c=2 into the trace formula. Independent additional field species would change this physical input, not count observers.

On the infinite line the massless negative-energy projection is defined almost everywhere in momentum; the single zero-momentum value has no L² weight. There is no mass gap. Circle zero modes, spin boundary conditions and Casimir constants require a separate specification and are not imported into this line construction.

For a smooth increasing null-coordinate map f, a vacuum-pulled-back chiral fermion two-point kernel has the local form

\[
S_f(u,u')=\frac{1}{2\pi i}
\frac{\sqrt{f'(u)f'(u')}}{f(u)-f(u')-i0}.
\]

The distributional boundary-value prescription fixes the orientation; the finite numerical subtraction below evaluates distinct real points, not delta functions at coincidence. A global diffeomorphism acts by a unitary half-density transformation on chiral L² data and transports the CAR vacuum covariance to a positive projection state. A map onto a proper interval instead pulls back a restriction of that vacuum: an isometric embedding/compression gives a positive contraction covariance, not necessarily a pure state or a globally unitarily implemented vacuum change.

The leading singularity is the vacuum one. Smooth increasing maps preserve the local null wavefront orientation, and conformal spinor factors are smooth and nonzero. This gives the standard massless conformal short-distance class used here. We do not claim to have proved the massive curved-background state's microlocal properties.

## 2. An explicit singular subtraction and its finite remainder

With chiral current normalization J=:χ*χ:, Wick contraction gives

\[
\langle J(u)J(u')\rangle_f
=-\frac1{4\pi^2}
\frac{f'(u)f'(u')}{(f(u)-f(u')-i0)^2}.
\]

The current Sugawara normalization is T_uu=π:JJ:. Its double-contraction singularity is 1/(8π²(u-u')⁴), the physical-stress normalization corresponding to chiral central charge c=1. These continuum CAR/current conventions are declared; they are not a stress normalization measured from lattice eigenvalue counts.

For symmetric real splitting u±h/2, define

\[
D_f(u,h)=
\frac{f'(u-h/2)f'(u+h/2)}{(f(u+h/2)-f(u-h/2))^2}-\frac1{h^2}.
\]

Taylor expansion gives

\[
D_f(u,h)=\frac16\{f,u\}+O(h^2),\qquad
\{f,u\}=\frac{f'''}{f'}-\frac32\left(\frac{f''}{f'}\right)^2.
\]

Thus the flat-coordinate normal-ordered state contribution is

\[
t_u(u)=-\frac{c}{24\pi}\{f,u\},
\]

and similarly t_v(v) from an independently specified g(v). This is an actual subtraction of the same leading singular kernel, not an assertion that a finite cutoff vacuum energy is already renormalized.

The tests use 80-digit Decimal arithmetic for cancellation of the O(h^-2) terms. Identity, affine and local Möbius maps give zero remainder; nonlinear cubic maps give the predicted Schwarzian and second-order symmetric-split error. Möbius examples are restricted to charts excluding their poles.

## 3. Specify the curved renormalization prescription

Flat-coordinate normal ordering alone is not a covariant curved stress tensor. We use the standard nonchiral conformal prescription with:

- symmetric, locally covariant stress expectation;
- covariant conservation;
- central-charge Weyl Ward identity;
- zero stress for the inertial Minkowski vacuum, before any separately declared cosmological term.

The central-charge/Weyl Ward correspondence is continuum conformal-field input here. It has not been independently derived from the massive lattice regulator. A local conformal representative of its anomalous effective action is

\[
W_{\rm anom}[\sigma;\eta]=\frac{c}{24\pi}
\int dt\,dx\,\partial_a\sigma\partial^a\sigma.
\]

For compactly supported Weyl variations, its variation is

\[
\delta W_{\rm anom}
=-\frac{c}{12\pi}\int\delta\sigma\,\Box_0\sigma\,dt\,dx
=\int\sqrt{|g|}\,\delta\sigma\,\frac{cR}{24\pi}\,dt\,dx,
\]

using R=-2exp(-2σ)Box₀σ=-8exp(-2σ)σ_uv. With the convention δW=∫sqrt(|g|)T^a_a δσ, this fixes

\[
\langle T^a{}_a\rangle=\frac{cR}{24\pi}.
\]

The conformal action above is a reference-chart representative of the universal Weyl variation, not by itself a globally specified generally covariant effective action with all Green functions, zero modes, boundary conditions and state choices fixed. A Polyakov-type covariant functional needs those extra choices. The remaining chiral state functions below encode information not selected by the anomaly.

## 4. Conservation fixes the geometric terms, not the state

For ds²=exp(2σ)du dv, g_uv=exp(2σ)/2. The anomaly gives T_uv=-cσ_uv/(12π). The two independent conservation equations are

\[
\partial_vT_{uu}+\partial_uT_{uv}-2\sigma_uT_{uv}=0,
\qquad
\partial_uT_{vv}+\partial_vT_{uv}-2\sigma_vT_{uv}=0.
\]

Integrating them gives

\[
\boxed{
\begin{aligned}
\langle T_{uu}\rangle&=\frac{c}{12\pi}(\sigma_{uu}-\sigma_u^2)+t_u(u),\\
\langle T_{uv}\rangle&=-\frac{c}{12\pi}\sigma_{uv},\\
\langle T_{vv}\rangle&=\frac{c}{12\pi}(\sigma_{vv}-\sigma_v^2)+t_v(v).
\end{aligned}}
\]

Direct substitution verifies conservation and the trace 4exp(-2σ)T_uv=cR/(24π). Changing t_u,t_v leaves the trace unchanged but changes fluxes and energies. They must depend only on their respective null variable for these conservation equations.

These Ward equations do not prove that every arbitrary pair of chiral functions is the expectation of a positive globally admissible state. The pulled-back kernel family of section 1 supplies explicit admissible examples; it does not classify every possible state.

For the previous static geometry σ=log(1+ε cos(qx)), the conformal vacuum choice t_u=t_v=0 gives

\[
T_{tt}=\frac{c}{12\pi}\left(\sigma''-\frac12(\sigma')^2\right),
\qquad T_{xx}=-\frac{c}{24\pi}(\sigma')^2.
\]

The static observer's energy density is exp(-2σ)T_tt. The same general formulas apply to the explicitly time-dependent affine-density patch of step 21; conservation and anomaly do not require staticity. They do not supply a preferred state on that patch.

## 5. Coordinate covariance requires cancellation of two anomalous pieces

For U=f(u), V=g(v), the same metric has

\[
\sigma'(U,V)=\sigma(u,v)-\tfrac12\log f'(u)-\tfrac12\log g'(v).
\]

Writing A=c/(12π), differentiation gives

\[
A(\sigma_{uu}-\sigma_u^2)
=f'^2 A(\sigma'_{UU}-(\sigma'_U)^2)+\frac A2\{f,u\}.
\]

For the **full** tensor to obey T_uu=f'^2T'_UU, the state term must therefore transform as

\[
t_u(u)=f'^2t'_U(U)-\frac{c}{24\pi}\{f,u\},
\]

with the analogous v rule. The mixed component transforms ordinarily. The Schwarzian chain rule ensures consistency under composing null-coordinate changes.

Thus t_u is not a tensor by itself. The geometric term's anomalous contribution cancels its state/normal-ordering contribution. A coordinate change of the same inertial vacuum still gives zero full stress; setting the new t'_U to zero without transforming the state would generally select a different vacuum. The tests check both the full-tensor rule and this flat-vacuum cancellation. Changing coordinates must not be mistaken for producing physical energy.

## 6. A thermal example is a state choice, not a geometry prediction

For f(u)=exp(κu)/κ, κ>0,

\[
\{f,u\}=-\kappa^2/2,\qquad t_u=\frac{c\kappa^2}{48\pi}.
\]

This map is not onto the whole null line. The state is obtained by restriction/pullback, not a globally pure vacuum reparametrization. Its fermion kernel is proportional to κ/[2sinh(κΔu/2)], with the usual boundary value. It has the fermionic imaginary-time antiperiodicity and KMS strip structure for β=2π/κ. Choosing the analogous state in both chiralities gives, in flat space,

\[
\langle T_{tt}\rangle=\frac{c\pi}{6}T_0^2,
\qquad T_0=\kappa/(2\pi).
\]

On a static conformal background, the thermal addition to the local observer's energy density is cπ(T₀/Ω)²/6, the corresponding Tolman redshift relation. The geometric vacuum-polarization contribution remains separate.

This evaluates a specified equilibrium state. It does not derive a temperature, actual horizon radiation, or state selection from the metric alone. Boundary/horizon conditions and an operational interpretation are additional physical inputs.

## 7. Finite renormalization and backreaction remain explicit

Adding Cg_ab preserves covariance and conservation. In null coordinates it changes T_uv by Cexp(2σ)/2 and shifts the trace by 2C. Minkowski-vacuum zero stress fixes this particular normalization to C=0; absent that condition, the calculation does not predict an absolute gravitational vacuum energy.

The integral of R has no bulk Einstein-tensor variation in two dimensions, so it cannot simply be used to remove the cR anomaly. The universal coefficient is discussed within the usual local covariant dimensional/power-counting prescription. If additional dimensionful higher-curvature couplings are admitted, they introduce further gravitational effective-theory terms and renormalization data; we do not claim the displayed formulas eliminate all such freedoms.

A trace anomaly is not a failure of conservation. Conversely a conserved anomalous expectation is not already a solved gravity model. In two dimensions the ordinary Einstein tensor vanishes identically, so one cannot obtain meaningful generic backreaction merely by inserting this nonzero tensor into an otherwise unmodified two-dimensional Einstein equation. A dilaton or another specified gravitational theory, its couplings, boundary conditions and solution criteria would be needed.

## 8. Verification and remaining bridges

Run `python -m unittest -v test_model.py` here, or `python research/run_checks.py` from the repository root. The 32 tests cover high-precision point splitting, Möbius/Schwarzian/chain identities, thermal normalization/redshift, Wick kernel normalization, trace and conservation, static and nonstatic metric jets, full-tensor coordinate transformation, state dependence, and the finite cosmological shift. `enumeration.json` records subtraction errors and representative stresses.

**Earned:** a concrete massless conformal composite-expectation prescription, an explicit singular subtraction with finite remainder, a conserved anomalous curved stress expectation, and clear state/coordinate/renormalization distinctions.

**Not earned:** a stress-tensor convergence theorem for either massive lattice regulator; a massive Hadamard proof; full operator-valued composites or their fluctuations; unique vacuum/state selection; an absolute vacuum-energy prediction; backreaction, empirical selection, all-framework integration, phenomenal constitution, or ultimate explanation. A central charge or stress expectation does not count observer tokens or supply a constitutive identity.

**Next bridge:** connect a specified regulator to this continuum subtraction, or specify a gravity model before claiming backreaction. The continuum Ward prescription and the earlier lattice-state theorem are now explicit neighboring results, not yet the same theorem.

## Continuation: common-regulator relative subtraction

[Step 26](../relative_subtraction/REPORT.md) proves a joint-limit regulator theorem for the relative state contribution, with explicit kernel bounds and a mismatched-cutoff counterexample. The absolute anomaly prescription remains the one specified here; no massive lattice stress theorem is inferred.
