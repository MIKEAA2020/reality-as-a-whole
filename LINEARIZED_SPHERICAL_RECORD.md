# Linearized spherical relational records beyond the frozen-geodesic approximation

[WEAK_BACKREACTION_RECORD.md](WEAK_BACKREACTION_RECORD.md) used the **initial**
conformal lapse and matter Hamiltonian to give a quasistatic record bound. That
is valid only while the geometry is treated as frozen. This continuation uses
the structure of spherical Einstein gravity to improve that bound: for
spherically symmetric data,

1. **Birkhoff’s theorem** forces the exterior vacuum metric to be the static
   Schwarzschild metric with the same ADM mass;
2. spherical symmetry forbids **linear-order quadrupole gravitational
   radiation**, so the ADM/Bondi mass is conserved in the linearized exterior;
3. interior matter evolves only on a **dynamical/free-fall timescale**, which
   can be computed from the constructed initial data.

This yields a relational record bound that is no longer tied to a frozen-geometry
assumption while still avoiding full numerical relativity.

## 1. Setup

Use the smooth conformally flat initial data from
[SMOOTH_FIELD_CLOCK.md](SMOOTH_FIELD_CLOCK.md):
\[
q_{ab}=\psi^4\delta_{ab},\quad K_{ab}=0,\quad
\Phi=\epsilon f v,\quad n\cdot\partial\Phi=-iM\Phi.
\]
The asymptotic ADM mass is
\[
M_{ADM}=16\pi C,\qquad C=\lim_{r\to\infty}r(\psi-1).
\]
The physical areal radius in isotropic coordinates is
\[
R_{\mathrm{phys}}(r)=r\psi(r)^2,
\]
and the Misner–Sharp mass is
\[
M_{MS}(R)=\frac{R}{2}\left(1-\frac{1}{(dR_{\mathrm{phys}}/dr)^2}\right).
\]
The compactness \(2M_{MS}/R_{\mathrm{phys}}\) must be checked directly in
physical areal coordinates; a naive coordinate-radius ratio overestimates it.

For the constructed Gaussian data with \(N=\psi^{-2}\), the initial lapse is
smaller than 1 inside the matter, producing redshift. The matter-weighted
initial redshift is
\[
\langle 1-N\rangle_m
=\frac{\int (1-N)\,|\Phi|^2\sqrt q\,d^3x}{\int |\Phi|^2\sqrt q\,d^3x},
\]
and the initial curved-vs-flat Hamiltonian energy shift is
\[
\delta_{\mathrm{curv}}=
\frac{|H_m(N)-H_{\mathrm{flat},0}|}{H_{\mathrm{flat},0}}.
\]

## 2. Birkhoff exterior and dynamical interior

For spherically symmetric vacuum Einstein gravity, Birkhoff’s theorem gives a
locally unique static spherically symmetric solution—the Schwarzschild geometry
of mass \(M_{ADM}\). Therefore, outside the matter support,

- the metric is **static**;
- there is **no linear-order monopole or quadrupole radiation** from a purely
  spherical configuration;
- the redshift at a fixed exterior areal radius is determined by the conserved
  mass \(M_{ADM}\).

Interior motion can change the **profile** of the redshift, but not the exterior
Schwarzschild mass at linear spherical order. Matter initially at rest in a
time-symmetric configuration evolves on the dynamical/free-fall timescale
\[
T_{\mathrm{dyn}}=\sqrt{\frac{R_m^3}{M(R_m)}},
\]
where \(R_m\) is the matter-averaged physical radius and \(M(R_m)\) is the
enclosed Misner–Sharp mass at that radius.

For \(T\ll T_{\mathrm{dyn}}\), matter displacement is \(\delta R\sim \tfrac12 a T^2\)
with acceleration \(a\sim M(R_m)/R_m^2\), so the fractional change in compactness
and redshift is of order \((T/T_{\mathrm{dyn}})^2\). Thus the relational record
error satisfies
\[
\epsilon_{\mathrm{record}}(T)\le
\min\bigl(1,\mu T s_0\bigl(1+(T/T_{\mathrm{dyn}})^2\bigr)\bigr),\tag{1}
\]
with
\[
s_0=\langle 1-N\rangle_m+\delta_{\mathrm{curv}}.
\]
The factor \(1+(T/T_{\mathrm{dyn}})^2\) is an order-unity bound on the interior
dynamical correction; the exterior redshift is fixed by Birkhoff.

## 3. Explicit cases

Verified in
[verification/linearized_spherical_record.py](verification/linearized_spherical_record.py)
using the Misner–Sharp mass in isotropic coordinates.

### 3.1 Nonlinear binding family

For \(D=12\), \(m_0=20\), program mass \(\mu=22\), \(R_0=20\), \(\epsilon=0.001\):

- \(E_{ADM}=23.6776572000\)
- \(E_{\mathrm{proper}}=24.1265757846\)
- binding \(=-0.4489185846\)
- classical charge \(=1.0966586189\)
- \(\max(2M_{MS}/R_{\mathrm{phys}})=0.1005740923\)
- no apparent horizon
- \(R_m=23.1139223934\)
- \(T_{\mathrm{dyn}}=190.4723484781\)
- \(\langle 1-N\rangle_m=0.0368515044\)
- \(\delta_{\mathrm{curv}}=0.0777725260\)
- \(s_0=0.1146240304\)
- quasistatic \(T_{\mathrm{rel}}\) for \(1\%\) budget: \(0.0039655337\)
- Birkhoff-corrected \(T_{\mathrm{rel}}\): \(0.0039655337\)

The dynamical correction is completely negligible at this percent budget because
\(T_{\mathrm{rel}}\ll T_{\mathrm{dyn}}\).

### 3.2 Weak-backreaction case

For \(\epsilon=3\times10^{-5}\):

- \(E_{ADM}=0.0194060790\)
- binding \(=-2.9889399\times10^{-7}\)
- \(\max(2M/R)=8.712\times10^{-5}\)
- \(T_{\mathrm{dyn}}=6465.0986467\)
- \(\langle 1-N\rangle_m=3.080\times10^{-5}\)
- \(\delta_{\mathrm{curv}}=6.161\times10^{-5}\)
- quasistatic \(T_{\mathrm{rel}}\) for \(0.1\%\) budget: \(0.4918625070\)
- Birkhoff-corrected \(T_{\mathrm{rel}}\): \(0.4918625041\)

Again, the frozen-geometry bound is essentially unchanged over the record-fidelity
window because the dynamical time is far longer than the budget-limited record
time.

## 4. What this adds

The improvement over the earlier quasistatic bound is conceptual and structural:

- The exterior metric is **not assumed frozen by hand**; its stationarity follows
  from spherical Einstein gravity via Birkhoff.
- There is a **physical reason** linear quadrupole GW loss does not relax the
  redshift for spherical data: such radiation cannot exist at linear order.
- The matter interior can move, but only on a computed free-fall time; the
  correction is explicit and negligible for the regimes in which percent/permille
  records survive.
- Horizon checks use the **Misner–Sharp/areal-radius compactness**, not a naive
  coordinate-radius ratio.

Still not supplied in the classical spherical analysis:

- Non-spherical data, where quadrupole radiation and angular momentum are
  possible.
- Strong-field collapse beyond the linear/dynamical-time estimate.

[The quantum static spherical continuation](QUANTUM_STATIC_SPHERICAL_CLOCK.md)
constructs a symmetry-reduced physical Hilbert-space/Hamiltonian pair and
proves a quantum relational bound in that sector; full quantum Einstein
closure and phenomenal constitution remain open.

## 5. Verification

Run:

    python verification/linearized_spherical_record.py
    python -m verification.linearized_spherical_record

Output:
[verification/linearized_spherical_record.json](verification/linearized_spherical_record.json).
The deterministic pure-Python verifier recomputes the conformal factor,
Misner–Sharp mass, areal compactness, horizon check, matter-averaged redshift,
dynamical time, and both quasistatic and Birkhoff-corrected relational bounds.
It does not perform numerical Einstein evolution.
