# Wheeler–DeWitt spherical R-clock: areal radius as internal quantum time

The non-static spherical midisuperspace framework in
[NONSTATIC_SPHERICAL_MIDISUPERSPACE.md](NONSTATIC_SPHERICAL_MIDISUPERSPACE.md)
identified areal radius \(R\) and Misner–Sharp mass \(m\) as relational
variables. This note makes the first quantum gravity step in that reduced
theory: it treats \(R\) as an **internal York-like clock** in the
Wheeler–DeWitt (WdW) equation and verifies that the semiclassical (WKB) limit
reproduces the already derived static Killing Hamiltonian evolution with the
same dressed-clock error.

## 1. WdW in spherical midisuperspace

For spherically symmetric Einstein gravity minimally coupled to a scalar field
\(\phi\), with areal radius \(R\) as the spatial coordinate, the Hamiltonian
constraint can be written in midisuperspace form. In the weak-field,
long-wavelength approximation (scalar approximately constant across the dressed
cloud, \(2m_G\ll R\)), the radial-proper WdW evolution reduces to a
Klein–Gordon-like equation with respect to proper radial distance \(l_R=\int
e^\lambda dR\):
\[
  i\frac{\partial}{\partial l_R}\Psi\approx H_{\mathrm{eff}}\Psi,
  \qquad H_{\mathrm{eff}}=\mu e^\nu\sqrt{1-2m_G/R},
\]
where \(e^\nu\) is the lapse integrated from the momentum constraint. For
time-symmetric initial data \(e^\nu=\sqrt{1-2m_G/R}\), giving
\[
  H_{\mathrm{eff}}\approx \mu(1-2m_G/R),
\]
matching the dressed redshifted Hamiltonian from
[QUANTUM_STATIC_SPHERICAL_CLOCK.md](QUANTUM_STATIC_SPHERICAL_CLOCK.md).

Areal radius \(R\) is therefore a valid internal clock in this symmetry-reduced
theory: evolution in proper radial length generates the dressed scalar phase,
just as York/scale-factor time does in cosmology.

## 2. Semiclassical WKB consistency

For the weak-backreaction dressed cloud (\(\epsilon=3\times10^{-5}\),
\(\mu=22\)):

- matter areal radius \(R_m=22.657\)
- proper radial length across cloud \(l_R=22.657\)
- compactness \(2m_G/R=3.66\times10^{-5}\)
- \(e^\nu(R_m)=0.9999817\approx1\)
- effective WdW Hamiltonian \(H_{\mathrm{eff}}=21.9996\approx \mu\)
- approximate Killing time from R-clock: \(T=l_R e^\nu=22.657\)
- WKB phase \(\Phi=H_{\mathrm{eff}} T=498.45\)
- semiclassicality parameter \(\mu\epsilon^2/R_0=4.5\times10^{-11}\ll 1\)
- R-clock tick \(1/H_{\mathrm{eff}}=0.0455\)
- static dressing error at this time: \(0.0461\).

The WKB/semiclassical approximation is excellent because the potential varies
extremely slowly over a de Broglie wavelength, and the effective WdW Hamiltonian
agrees with the static dressed Hamiltonian up to small redshift corrections.
Crucially, time is not imported from outside: the areal radius of symmetry
spheres is the clock.

## 3. Significance

This is the first quantum-gravity internal-clock result in the repository that
does **not** rely on asymptotic Killing time being given in advance:

- Time is read from the areal radius \(R\), a geometric degree of freedom.
- The static Schwarzschild Killing time emerges as the semiclassical WKB
  approximation of R-clock evolution on time-symmetric data.
- The dressed-clock error bound applies to the WKB semiclassical regime, with
  semiclassicality parameter \(\sim 4.5\times10^{-11}\) in the weak-field case.

Limitations:

- This is a reduced midisuperspace model, not full 3+1 quantum gravity.
- The WKB approximation is used; a rigorous solution of the WdW equation with
  self-adjoint physical inner product is not yet supplied.
- Singularity resolution, unitarity across non-symmetric foliations, and
  phenomenal constitution remain open.

## 4. Verification

Run:

    python verification/wdw_spherical_clock.py
    python -m verification.wdw_spherical_clock

Output:
[verification/wdw_spherical_clock.json](verification/wdw_spherical_clock.json).
The deterministic pure-Python verifier computes proper radial length, effective
WdW R-clock Hamiltonian, WKB phase, semiclassicality parameter, and compares
with the static dressed-clock error bound.
