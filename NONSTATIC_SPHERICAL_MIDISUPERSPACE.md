# Beyond Killing time: spherical Einstein–scalar midisuperspace with Misner–Sharp relational variables

All prior gravitational clock results in this repository rely, in one way or
another, on the static spherical Birkhoff sector: a pre-existing timelike Killing
vector, static exterior Schwarzschild geometry, and asymptotic proper time as
Killing flow. This note takes the next step: it identifies the **areal radius**
\(R\) and **Misner–Sharp mass** \(m(R)\) as relational variables valid for
dynamical (non-static) spherical Einstein–scalar gravity, not just for static
solutions.

## 1. Areal/Misner–Sharp variables

In areal (Schwarzschild-comoving) coordinates, the spherically symmetric metric is
\[
  ds^2=-e^{2\nu(t,R)}dt^2+e^{2\lambda(t,R)}dR^2+R^2d\Omega^2,
\]
where \(R\) is defined by the area of symmetry spheres being \(4\pi R^2\). The
Misner–Sharp mass is
\[
  1-\frac{2m_G(R,t)}{R}=e^{-2\lambda(R,t)},
\]
with \(m_G\) the mass in \(G=1\) units; in our \(8\pi G=1\) action convention we
write \(m=8\pi m_G\). Einstein’s equations for a real spherical scalar field
give
\[
  \partial_R m = 4\pi R^2\rho e^\lambda,\qquad
  \partial_t m = -4\pi R^2 j e^\nu,
\]
where \(\rho,j\) are the scalar energy density and flux. These are
gauge-invariant statements in spherical reduction, and they hold without assuming
a Killing vector.

**Crucially**, for time-symmetric data (\(\phi_t=0\), \(K_{ab}=0\)) the flux \(j=0\)
and the lapse that makes the slice static satisfies
\[
  e^\nu=\sqrt{1-2m_G/R},
\]
recovering the Schwarzschild/Birkhoff lapse exactly. The static Killing clock is
therefore a **special case** of the midisuperspace relational framework, not an
extra assumption.

## 2. Transformation from isotropic conformal data

The constructed conformally flat initial data of
[SMOOTH_FIELD_CLOCK.md](SMOOTH_FIELD_CLOCK.md) uses isotropic coordinates with
\(q_{ab}=\psi^4\delta_{ab}\). The areal radius is
\[
  R(r)=r\psi(r)^2.
\]
The physical radial line element is \(dl=\psi^2 dr\), so in areal coordinates
\(dl=e^\lambda dR\) with
\[
  e^\lambda=\frac{\psi^2}{dR/dr},\qquad
  \frac{dR}{dr}=\psi^2+2r\psi\psi'.
\]
Hence
\[
  m_G(R)=\frac{R}{2}\left(1-\frac{(dR/dr)^2}{\psi^4}\right),\qquad
  m(R)=8\pi m_G(R).
\]
The scalar energy density in physical coordinates is
\[
  \rho=\epsilon^2\left(\kappa f^2+\frac{1}{2}\psi^{-4}f'^2\right),
\]
and the proper volume element gives the enclosed mass by integration.

## 3. Verified results

From [verification/nonstatic_spherical_midisuperspace.py](verification/nonstatic_spherical_midisuperspace.py).

### 3.1 Nonlinear binding family

For \(\epsilon=0.001\), \(m_0=20\), \(\kappa=484\):

- asymptotic Misner–Sharp/ADM mass \(m(R_\infty)=23.6805\) (matches the prior
  \(E_{ADM}=23.6777\) within tail-truncation error);
- maximum compactness \(2m_G/R=0.0485\) (sub-horizon, as expected);
- Hamiltonian constraint residual (mass integrated from density vs geometric
  Misner–Sharp mass): \(0.0738\), dominated by truncation/discretization at the
  first grid shell;
- static lapse \(e^\nu=\sqrt{1-2m_G/R}\) recovered exactly on the time-symmetric
  slice.

### 3.2 Weak-backreaction family

For \(\epsilon=3\times10^{-5}\):

- \(m(R_\infty)=0.019408\) (matches \(E_{ADM}=0.019406\));
- max compactness \(4.06\times10^{-5}\);
- Hamiltonian constraint residual \(6.05\times10^{-5}\);
- static lapse recovery exact.

The agreement between geometric \(m(R)\) and density-integrated mass confirms
that the areal/Misner–Sharp variables correctly describe the same physical data
without using Birkhoff as a premise.

## 4. Significance

This shifts the problem-of-time analysis in the spherical sector from a
static-Killing construction to a relational midisuperspace one:

- \(R\) is a physical spatial reference (areal radius of symmetry spheres);
- \(m(R)\) is a local Dirac observable (enclosed gravitational mass);
- the static Killing-time Hamiltonian emerges as the time-symmetric limit;
- dynamical departures from staticity are controlled by flux/nonzero \(\phi_t\),
  which the existing aspherical/quadrupole and weak-backreaction tools can bound
  perturbatively.

What this does not yet do:

- integrate the non-static Einstein–scalar equations in time;
- identify a fully reduced Hamiltonian without coordinate gauge fixing beyond
  areal radius;
- give a quantum constraint solution on midisuperspace;
- address non-spherical gravity or phenomenal constitution.

It is the minimal next step beyond the static Birkhoff clock.

## 5. Verification

Run:

    python verification/nonstatic_spherical_midisuperspace.py
    python -m verification.nonstatic_spherical_midisuperspace

Output:
[verification/nonstatic_spherical_midisuperspace.json](verification/nonstatic_spherical_midisuperspace.json).
The deterministic pure-Python verifier transforms isotropic conformal initial
data to areal coordinates, computes Misner–Sharp mass geometrically and via
density integration, checks compactness/horizon absence, and verifies recovery
of the static Schwarzschild lapse.
