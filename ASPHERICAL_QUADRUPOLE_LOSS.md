# Weak aspherical quadrupole losses beyond perfect spherical symmetry

The static spherical results in
[LINEARIZED_SPHERICAL_RECORD.md](LINEARIZED_SPHERICAL_RECORD.md),
[QUANTUM_STATIC_SPHERICAL_CLOCK.md](QUANTUM_STATIC_SPHERICAL_CLOCK.md), and
[PHOTON_ECHO_READOUT.md](PHOTON_ECHO_READOUT.md) rely on Birkhoff’s theorem, which
forbids linear-order spherical radiation. Real clocks are not perfectly
spherical. This note quantifies the leading correction from **small aspherical
pulsations** via the Einstein quadrupole formula.

## 1. Mechanical, not rest-mass, radiation frequency

A subtle point: gravitational radiation is sourced by time variation of the mass
quadrupole at the frequency of **mechanical motion**, not the scalar’s rest
frequency \(\mu\). In geometric units, quadrupole power scales as
\[
  \frac{dE}{dt}\sim \frac{G}{c^5}\dddot Q_{ij}\dddot Q_{ij}\sim Q^2\omega^6.
\]
The mechanical pulsation frequency is set by the free-fall/dynamical time
\(T_{\mathrm{dyn}}=\sqrt{R_m^3/M_m}\):
\[
  \omega_{\mathrm{mech}}=\frac{2\pi}{T_{\mathrm{dyn}}}.
\]
For the weak-backreaction cloud with \(R_m\approx22.57\),
\(M\approx0.0194\), this gives \(T_{\mathrm{dyn}}\approx1053.7\), so
\(\omega_{\mathrm{mech}}\approx0.00596\). That is much smaller than the scalar
rest mass \(\mu=22\), and it is the correct GW frequency for slow pulsations of
the dressed cloud.

## 2. Axisymmetric deformation and quadrupole formula

Take a fractional axisymmetric quadrupolar deformation
\[
  \delta\rho_2(r)=\alpha\,\frac{r^2}{R_0^2}\,e^{-r^2/R_0^2}\,\kappa\epsilon^2\psi^6
\]
on top of the spherical rest density. The axisymmetric quadrupole moment is
\[
  Q_{zz}=\sqrt{\frac{16\pi}{5}}\int_0^\infty r^4\,\delta\rho_2(r)\,dr,
\]
with \(Q_{xx}=Q_{yy}=-Q_{zz}/2\). For pulsation \(Q(t)=Q_0\cos(\omega_{\mathrm{mech}}t)\),
the Einstein quadrupole formula gives averaged radiated power
\[
  \frac{dE}{dt}=-\frac{1}{5}\langle\dddot Q_{ij}\dddot Q_{ij}\rangle
  =-\frac{3}{20}Q_0^2\omega_{\mathrm{mech}}^6. \tag{1}
\]
Integrated energy loss over observation time \(T_{\mathrm{obs}}\) is
\[
  \Delta E=\left|\frac{dE}{dt}\right|T_{\mathrm{obs}}.
\]
This mass loss changes the asymptotic redshift and Shapiro delay:

- redshift drift: \(1-N\sim M/R\), so the cumulative phase drift over \(T_{\mathrm{obs}}\) is
  \(\Delta\phi\approx \mu T_{\mathrm{obs}}\,\Delta M/R_m\);
- Shapiro echo delay drift: \(\Delta t_{\mathrm{Shapiro}}\sim 6\Delta M\log(R_\infty/R_m)\).

## 3. Verified cases

From [verification/aspherical_quadrupole_loss.py](verification/aspherical_quadrupole_loss.py).

### 3.1 One-percent quadrupole deformation, 10-time-unit observation

For \(\alpha=0.01\), \(T_{\mathrm{obs}}=10\):

- \(M_{\mathrm{total}}=0.019406\)
- \(R_m=22.568\)
- \(T_{\mathrm{dyn}}=1053.68\), \(\omega_{\mathrm{mech}}=0.00596\)
- \(Q_0=0.07345\), \(Q/MR^2\approx 0.00743\)
- \(dE/dt=-3.64\times10^{-17}\)
- \(\Delta E=3.64\times10^{-16}\)
- fractional mass loss: \(1.87\times10^{-14}\)
- integrated redshift dephasing: \(3.55\times10^{-15}\)
- Shapiro echo drift: \(4.54\times10^{-15}\), i.e. \(1.59\times10^{-14}\) ticks.

Quadrupole losses are negligible at the weak-field scale because of the severe
\(\omega^6\) suppression from the long free-fall time.

### 3.2 Smaller deformation, longer observation

For \(\alpha=0.001\), \(T_{\mathrm{obs}}=100\):

- \(\Delta E=3.64\times10^{-17}\)
- fractional mass loss: \(1.87\times10^{-15}\)
- Shapiro drift: \(4.54\times10^{-16}\), \(1.59\times10^{-15}\) ticks.

Even over one hundred asymptotic time units, sub-percent aspherical pulsations
produce no measurable loss in this weak-field regime.

## 4. Domain of validity

This bound applies when:

- the background is weak-field static Schwarzschild (small compactness);
- the aspherical amplitude \(\alpha\ll 1\);
- motion is slow, \(v\sim R\omega_{\mathrm{mech}}\ll1\);
- radiation reaction does not substantially alter the background over
  \(T_{\mathrm{obs}}\).

For the weak-backreaction example \(R\omega_{\mathrm{mech}}\approx 0.135\), which
is safely slow. This is a **leading-order aspherical correction**, not a
strong-field or merger calculation. It shows that the spherical static clock
result is robust against small realistic asphericities in this regime.

Still not supplied:

- non-axisymmetric or resonant aspherical modes;
- strong-field collapse with horizon formation;
- scattering of the readout photons off aspherical structure;
- full quantum Einstein constraints;
- phenomenal constitution.

## 5. Verification

Run:

    python verification/aspherical_quadrupole_loss.py
    python -m verification.aspherical_quadrupole_loss

Output:
[verification/aspherical_quadrupole_loss.json](verification/aspherical_quadrupole_loss.json).
The deterministic pure-Python verifier recomputes the background, quadrupole
moment, mechanical frequency, radiated power, integrated mass loss, redshift
dephasing, and Shapiro drift.
