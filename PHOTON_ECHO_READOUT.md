# Asymptotic photon-echo relational readout for the static spherical clock

The quantum static spherical clock in
[QUANTUM_STATIC_SPHERICAL_CLOCK.md](QUANTUM_STATIC_SPHERICAL_CLOCK.md) gives a
physical Hamiltonian generating Schwarzschild Killing time. But an actual
record must be read **relationally** by an asymptotic observer. This note adds
the operational photon-echo readout: a photon emitted from the dressed clock
travels to infinity, and its arrival time in asymptotic proper time is a
gauge-invariant observable.

## 1. Null geodesics in the isotropic conformal metric

On the constructed conformally flat spatial slice with lapse \(N=\psi^{-2}\),
radial null geodesics satisfy
\[
  N\,dt=\psi^2\,dr_{\mathrm{phys}}=\psi^4\,dr
\]
in isotropic coordinates, because the physical radial distance is
\(dr_{\mathrm{phys}}=\psi^2 dr\). Equivalently,
\[
  \frac{dt}{dr}=\frac{\psi^4}{N}=\psi^6.
\]
Thus the asymptotic one-way travel time from coordinate radius \(r_0\) to a
distant radius \(R_\infty\) is
\[
  t_{\mathrm{out}}(r_0)=\int_{r_0}^{R_\infty}\psi^6(r)\,dr. \tag{1}
\]
Two-way echo delay is \(2t_{\mathrm{out}}\). Split this into the geometric
Minkowski travel time and the Shapiro-like gravitational delay:
\[
  t_{\mathrm{out}}(r_0)=(R_\infty-r_0)+\Delta t_{\mathrm{Shapiro}}(r_0).
\]

## 2. Echo spread versus internal tick period

The asymptotic observer sees the dressed clock’s proper frequency redshifted by
\(N(r)\). The observed period for emission at radius \(r\) is
\[
  T_{\mathrm{tick}}(r)=\frac{2\pi}{\mu N(r)}.
\]
Because emission occurs across the spatial support of the Gaussian field
profile, different regions emit with slightly different Shapiro delays and
redshifted periods. The relevant relational readout error is the
**emission-region echo jitter**, i.e. the spread in echo delays across the
matter support measured in units of the observed tick period.

Using the matter-weighted average radius \(R_m\) as reference, define the
**Shapiro-delay spread**
\[
  \Delta t_{\mathrm{Shapiro,spread}}=
  |\Delta t_{\mathrm{Shapiro}}(0)-\Delta t_{\mathrm{Shapiro}}(R_m)|,
\]
which excludes the geometric travel-time difference from finite clock size.

The **redshift dephasing over one tick** is bounded by
\[
  \Delta\phi_{\mathrm{tick}}\le \mu T_{\mathrm{tick}}\frac{\Delta N}{N}
  =2\pi\frac{\langle 1-N\rangle_m}{N_0},
\]
conservatively using the central-averaged lapse difference. Combining Shapiro
jitter and one-tick redshift dephasing gives the operational echo readout
error budget per tick.

## 3. Verified cases

From [verification/photon_echo_readout.py](verification/photon_echo_readout.py).

### 3.1 Nonlinear binding family

For \(D=12\), \(m_0=20\), \(\mu=22\), \(R_0=20\), \(\epsilon=0.001\):

- \(N(0)=0.9483806523\)
- \(N_{\mathrm{avg}}=0.9631484957\)
- one-way Shapiro delay from center: \(9.0000200401\)
- one-way Shapiro delay from averaged matter radius: \(5.6180523722\)
- Shapiro spread center-to-averaged: \(3.3819676679\)
- observed average tick period: \(0.2965267904\)
- Shapiro jitter in tick units: about \(11.405\)
- one-tick redshift dephasing: about \(0.2441\).

The nonlinear dressed configuration is not a sharp clock body: its gravitational
Shapiro spread across its own support is many tick periods. That is physically
expected for a percent-compactness field cloud.

### 3.2 Weak-backreaction case

For \(\epsilon=3\times10^{-5}\):

- \(N(0)=0.9999564376\)
- \(N_{\mathrm{avg}}=0.9999691965\)
- Shapiro from center: \(0.0070912713\)
- Shapiro from averaged radius: \(0.0044797296\)
- Shapiro spread center-to-averaged: \(0.0026115417\)
- observed average tick period: \(0.2856081299\)
- Shapiro jitter in tick units: about \(0.00914\)
- one-tick redshift dephasing: about \(1.94\times10^{-4}\).

In this regime the Shapiro echo jitter is sub-period: a single photon echo can
resolve the dressed clock’s ticks at the asymptotic observer.

## 4. Significance

This gives an explicit operational readout:

- The echo delay is computed from radial null geodesics in the actual dressed
  geometry.
- It separates geometric travel time from Shapiro gravitational delay.
- It quantifies the spread in readout due to the finite dressed-field support.
- In the weak-backreaction regime, the echo readout is sub-period and therefore
  relationally resolvable; in the nonlinear percent-compactness regime, the
  finite cloud’s Shapiro spread exceeds a tick and therefore requires
  sub-ensemble or sharper localization, which is physically correct.

This remains a spherical-symmetry readout. [The weak aspherical continuation](ASPHERICAL_QUADRUPOLE_LOSS.md)
adds leading quadrupole radiation-reaction bounds for small axisymmetric pulsations.
Still open:

- strong angular structure or non-spherical photon scattering;
- full quantum electrodynamics of photon detection;
- quantum Einstein constraints beyond the static sector;
- phenomenal constitution.

## 5. Verification

Run:

    python verification/photon_echo_readout.py
    python -m verification.photon_echo_readout

Output:
[verification/photon_echo_readout.json](verification/photon_echo_readout.json).
The deterministic pure-Python verifier recomputes the conformal metric, radial
null travel times, Shapiro delays, observed tick periods, and echo spreads.
