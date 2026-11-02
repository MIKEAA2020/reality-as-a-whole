# Step 29 — Nonthermal stationary universality and state nonidentifiability

## Result and scope

The mesoscopic relative current limit of step 28 is not specifically thermal. For a controlled family of stationary quasifree excitations of the same infinite massless Wilson Hamiltonian, its value depends only on a first energy moment. Distinct nonthermal states can have identical limiting stress and energy while differing in occupation functions, higher moments, and finite-spacing energy.

This is a homogeneous stationary extension, **not** a theorem for spatially varying states, time-dependent excitations, an absolute stress tensor, or phenomenality. The physical state-selection problem remains: proving a universal limit does not select the state realized in nature.

## 1. Actual Hamiltonian states, not imported continuum data

Use the Hamiltonian and spectral projections of [step 28](../wilson_thermal_composite/REPORT.md):

\[
h_a(\theta)=a^{-1}[\sin\theta\,Z+(1-\cos\theta)X],\qquad
E_a(\theta)=2|\sin(\theta/2)|/a.
\]

For a measurable occupation \(0\leq\eta(p)\leq1/2\), define the gauge-invariant quasifree covariance fibre

\[
C_{a,\eta}=\eta(E_a)P_+ +[1-\eta(E_a)]P_-.
\]

Its eigenvalues lie in [0,1], so it defines a positive CAR state; it commutes with the Hamiltonian and is translation invariant and stationary. The zero-energy fibre is measure zero. No thermal detailed-balance condition is imposed. These are particle/hole symmetric excitations, not all stationary quasifree states.

Assume compact energy support [0,L] and restrict to aL≤1. Write

\[
F(p)=2\eta(p),\qquad M_j=\int_0^L p^j F(p)\,dp,
\qquad t_\eta=M_1/(2\pi).
\]

The analytic estimates below apply to any such measurable occupation. Numerical examples use a continuous triangular family to avoid quadrature across jumps:

\[
\eta_{A,L}(p)=A(1-p/L)_+,\quad 0\leq A\leq1/2,
\qquad M_j=\frac{2AL^{j+1}}{(j+1)(j+2)}.
\]

The quasifree state of this covariance is not in general a classical mixture of thermal many-body states. Positivity is established directly by its spectral eigenvalues.

## 2. Composite estimate without a thermal assumption

Put h=na, n≥1, q_a(p)=2 asin(ap/2)/a, and W_n=n²/(n²−1/4). The Fourier change of variables used in step 28 now gives exactly

\[
r_{a,h}=-\int_0^L \frac{\sin(hq_a(p))}{h}F(p)\,dp,
\qquad
\Delta S_{a,n}=-\frac{2W_n r_{a,h}+h^2r_{a,h}^2}{4\pi}.
\]

This is the expectation difference of the actual two-mode observable π(n_j−1/2)(n_k−1/2)/a², not a definition of stress chosen to force the target. Wick's rule supplies the quadratic expression. The observable norm still diverges as π/(4a²); weak-* fixed-observable convergence alone does not prove this result.

On the occupied band ap≤1, q_a≤πp/2 and |q_a−p|≤a²p³/12. Using |sin x−x|≤|x|³/6 yields

\[
|r_{a,h}+M_1|\leq B_{a,h}
=\left(\frac{\pi^3h^2}{48}+\frac{a^2}{12}\right)M_3.
\]

Also |r|≤πM₁/2, hence

\[
|\Delta S_{a,n}-W_n t_\eta|
\leq \frac{W_n B_{a,h}}{2\pi}
+\frac{h^2(\pi M_1/2)^2}{4\pi}.
\]

Thus a→0, h→0, n→∞ gives ΔS→tη. Fixed n instead gives W_n tη. The same ground-state normalization artifact persists independently of the chosen occupation. There is no numerical tail truncation in these compact-support integrals; quadrature error is separate from the analytic bounds and checked by refinement, not certified by Simpson's rule alone.

## 3. Independent Hamiltonian energy and mixed-current control

The spectral Hamiltonian relative energy per coordinate length is

\[
\Delta\epsilon_a=\frac1\pi\int_0^L
\frac{pF(p)}{\sqrt{1-(ap/2)^2}}\,dp.
\]

For 0≤x≤1/4, (1−x)^(−1/2)−1≤x. Therefore

\[
0\leq\Delta\epsilon_a-2t_\eta\leq\frac{a^2M_3}{4\pi}.
\]

The two mesoscopic chiral composite expectations consequently sum to the independently computed energy limit. This remains an expectation-level limit, not a finite-spacing operator identity.

The mixed covariance correction obeys

\[
\frac{\delta C_{\uparrow\downarrow}(n)}{a^2}
=\frac1{4\pi}\int_0^L
\frac{p\cos(hq_a(p))F(p)}{\sqrt{1-(ap/2)^2}}\,dp
\longrightarrow\frac{M_1}{4\pi}.
\]

Dominated convergence applies because the denominator is bounded below by √3/2. Combining this with the Wilson ground mixed kernel gives the fixed-n mixed-current limit −tη/(4n²−1); it vanishes when n→∞ jointly with h→0. This is a regulator-mixing diagnostic, not a derivation of a mixed stress component or an axial Ward identity.

## 4. Equal stress does not identify the state

Compare (A,L)=(1/2,1) and (1/8,2), in the same energy units. Both have M₁=1/6 and tη=1/(12π), but M₃ is respectively 1/20 and 1/5. Their occupations differ, including their support, while both limiting chiral stresses and total energy agree. Positive-temperature Fermi occupations have nonzero tails at every finite energy, so neither compactly supported state is a finite-temperature Gibbs state.

At nonzero spacing the independent energy distinguishes them. In fact, uniformly on a fixed compact support,

\[
\Delta\epsilon_a=\frac{M_1}{\pi}+\frac{a^2M_3}{8\pi}+O(a^4M_5).
\]

Their leading energy difference is 3a²/(160π). This supplies an explicit loss of information under the stress/energy limit, not merely a verbal warning about coarse-graining. It does not imply that all local observables or the full continuum states coincide.

## 5. Verification and integration

`model.py` implements spectral occupations, analytic moments, exact compact-band integral formulas evaluated numerically, bounds, and two-mode covariances. `test_model.py` contains 24 checks: positivity and stationarity, nonthermal support, moments, bounds, mesoscopic and fixed-site limits, mixed artifacts, independent energy, equal-stress/different-state witnesses, actual finite-CAR expectation, and refinement/validation. `enumeration.json` records examples.

The architecture now has a state-family-uniform relative composite bridge on a controlled stationary spectral class. It cannot infer thermal equilibrium or a unique microscopic realization from limiting stress alone. Spatially varying/nonstationary states, state-independent local subtraction, absolute geometric anomaly, massive composites, interactions, and backreaction remain further mathematical obligations; physical actuality and phenomenal constitution remain separate explanatory obligations.

## Continuation

[Step 30](../wilson_wavepacket_composite/REPORT.md) removes homogeneity and stationarity for a compact-band positive-energy rank-one excitation, with a controlled local current limit.
