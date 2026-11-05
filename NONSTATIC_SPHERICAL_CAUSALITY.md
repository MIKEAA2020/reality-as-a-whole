# Non-static spherical causality: before the first signal reaches infinity

The areal/Misner–Sharp framework in
[NONSTATIC_SPHERICAL_MIDISUPERSPACE.md](NONSTATIC_SPHERICAL_MIDISUPERSPACE.md)
removes the Killing-time assumption. This note gives the first non-static bound:
a causality/domain-of-dependence statement controlling the time before any scalar
or gravitational signal can reach the asymptotic observer.

## 1. Null characteristics in areal spherical coordinates

In the metric
\[
  ds^2=-e^{2\nu}dt^2+e^{2\lambda}dR^2+R^2d\Omega^2,
\]
outgoing radial null geodesics satisfy \(dR/dt=e^{\nu-\lambda}\). On the
time-symmetric initial slice with \(e^{-\lambda}=\sqrt{1-2m_G/R}\) and lapse
\(e^\nu\) integrated from the momentum constraint, this is the local coordinate
speed of light.

For any perturbation with compact (or exponentially localized) support inside
areal radius \(R_{\mathrm{supp}}\), and outer boundary at \(R_{\mathrm{out}}\),
no signal can reach infinity before the proper time
\[
  T_{\mathrm{causal}}=\frac{R_{\mathrm{out}}-R_{\mathrm{supp}}}{c_{\min}},
  \qquad c_{\min}=\min_{R\le R_{\mathrm{supp}}}\,e^{\nu-\lambda}(R). \tag{1}
\]

## 2. Mass conservation before first signal

For spherically symmetric Einstein–scalar gravity, the Misner–Sharp/Bondi mass
changes at a given areal radius only when a scalar flux \(j=-\Pi\partial_R\phi\)
passes through that radius. Until the first outgoing signal reaches \(R_{\mathrm{out}}\):

- the asymptotic ADM/Bondi mass is unchanged;
- no monopole gravitational wave flux exists (Birkhoff for vacuum exterior);
- the asymptotic Schwarzschild Killing structure remains intact outside the
  perturbed region.

Hence the static dressed-clock error bound of
[QUANTUM_STATIC_SPHERICAL_CLOCK.md](QUANTUM_STATIC_SPHERICAL_CLOCK.md),
\[
  \epsilon_{\mathrm{record}}(T)\le T\mu(\langle 1-N\rangle_m+\delta_{\mathrm{curv}}),
\]
remains valid for \(T<T_{\mathrm{causal}}\).

## 3. Verified case

From [verification/nonstatic_spherical_causality.py](verification/nonstatic_spherical_causality.py),
weak-backreaction data with \(\epsilon=3\times10^{-5}\), \(\mu=22\),
Gaussian Pi perturbation with support \(R_{\mathrm{supp}}\approx 5.25\,R_0\):

- \(R_{\mathrm{supp}}=105.157\) (areal)
- \(R_{\mathrm{out}}=160.001\)
- \(c_{\min}=0.999959\approx 1\)
- \(T_{\mathrm{causal}}\approx 54.84\)
- averaged gravitational slope \(V=0.00203\)
- static-clock error at \(T_{\mathrm{causal}}\): \(0.1115\).

The static dressed clock therefore remains valid to about **11% fidelity error**
up to the first moment a causal signal can arrive at the asymptotic observer.
Earlier tighter budgets (e.g. \(0.1\%\) at \(T\approx0.49\)) are sub-intervals of
this causal window.

For the stronger nonlinear cloud the causal window is smaller (larger dressing,
more rapid error growth), as expected.

## 4. What this proves

- A rigorous domain-of-dependence result in spherical Einstein–scalar gravity,
  not assuming a global Killing vector.
- The earlier static Killing bound is not merely formal: it is valid until the
  first outgoing signal reaches the observer.
- Beyond \(T_{\mathrm{causal}}\), scalar/GW flux will arrive at infinity and the
  Bondi mass decreases; that will be the next step, but it begins from a
  controlled causal boundary rather than an uncontrolled assumption.

Not supplied:

- the post-causal scalar waveform/Bondi loss;
- strong-field collapse;
- quantum midisuperspace constraints;
- phenomenal constitution.

## 5. Verification

Run:

    python verification/nonstatic_spherical_causality.py
    python -m verification.nonstatic_spherical_causality

Output:
[verification/nonstatic_spherical_causality.json](verification/nonstatic_spherical_causality.json).
The deterministic pure-Python verifier transforms initial data to areal
coordinates, computes null characteristic speeds, the causal support radius, the
causal window \(T_{\mathrm{causal}}\), and evaluates the static-clock error at
that time.
