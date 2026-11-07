# Spherical scalar radiation and post-causal Bondi mass loss

The non-static causality window in
[NONSTATIC_SPHERICAL_CAUSALITY.md](NONSTATIC_SPHERICAL_CAUSALITY.md) bounds the
time before any perturbation reaches the asymptotic observer. This note gives
the first post-causal result: when a spherical scalar momentum pulse is present,
the field radiates scalar energy to infinity, reducing the Bondi mass and
producing calculable post-burst dephasing and Shapiro drift. In spherical
symmetry there is no quadrupole gravitational radiation (Birkhoff); scalar
radiation is the only leading monopole energy-loss channel.

## 1. Scalar radiation and Bondi mass loss

For a spherical scalar field, at large \(R\) the outgoing wave takes the form
\[
  \phi(R,t)\sim \frac{f(t-R)}{R},
\]
and the scalar energy flux through a large sphere is
\[
  \frac{dE}{dt}=4\pi R^2\cdot\frac{1}{2}\left(\partial_t\phi+\partial_R\phi\right)^2
  \to 2\pi f'(u)^2,\qquad u=t-R.
\]
Energy conservation (in the weak-field, small-backreaction regime) implies the
total radiated Bondi mass loss is bounded by the initial scalar kinetic energy
of the perturbation:
\[
  \Delta M_{\mathrm{Bondi}}\le E_{\mathrm{kin}}=
  2\pi\int R^2\Pi^2 e^\lambda\,dR.
\]
Once the outgoing pulse passes the observer, the geometry settles to a new
Schwarzschild exterior with mass \(M-\Delta M\).

## 2. Post-burst dephasing and Shapiro drift

After the burst passes the observer:

- the new asymptotic redshift at the clock radius \(R_m\) changes by
  \(\Delta(1-N)\sim \Delta M/R_m\), giving cumulative phase drift
  \(\Delta\phi\sim \mu\,T_{\mathrm{obs}}\,\Delta M/R_m\);
- the Shapiro delay changes by \(\Delta t_{\mathrm{Shapiro}}\sim 6\Delta M\log(R_{\mathrm{out}}/R_m)\).

The observation time \(T_{\mathrm{obs}}\) covers the causal delay plus the pulse
duration: \(T_{\mathrm{obs}}\approx T_{\mathrm{causal}}+3\sigma_R\).

## 3. Verified cases

From [verification/spherical_scalar_radiation.py](verification/spherical_scalar_radiation.py),
weak-backreaction background with Gaussian Pi pulses \(\Pi=\Pi_0 e^{-R^2/R_0^2}\),
\(R_0=20\), \(\mu=22\):

### 3.1 \(\Pi_0=10^{-6}\)

- initial scalar kinetic energy \(E_{\mathrm{kin}}=7.88\times10^{-9}\)
- radiated Bondi mass loss \(\Delta M=7.88\times10^{-9}\)
- \(T_{\mathrm{causal}}=54.87\), \(T_{\mathrm{obs}}=114.87\)
- post-burst redshift dephasing: \(8.81\times10^{-7}\)
- Shapiro drift: \(9.25\times10^{-8}\) (\(3.24\times10^{-7}\) ticks).

### 3.2 \(\Pi_0=10^{-5}\)

- \(E_{\mathrm{kin}}=7.88\times10^{-7}\)
- \(\Delta M=7.88\times10^{-7}\)
- post-burst dephasing: \(8.81\times10^{-5}\)
- Shapiro drift: \(9.25\times10^{-6}\) (\(3.24\times10^{-5}\) ticks).

The post-burst drifts are tiny in the weak-field regime because the radiated
scalar energy is set by \(\Pi_0^2\). The pre-causal static error at
\(T_{\mathrm{causal}}\) (\(\sim 0.11\)) is dominated by gravitational dressing,
not radiation reaction.

## 4. Significance

This extends the causal window into the first post-signal regime:

- Spherical monopole scalar radiation is included (in spherical symmetry there
  is no GW quadrupole loss).
- Bondi mass loss is bounded by initial scalar kinetic energy.
- Post-burst redshift/Shapiro drift are computable and small in the
  weak-backreaction regime.
- The static clock error plus the radiation drift are now jointly bounded for
  times through and after the first signal.

Not yet supplied:

- detailed waveform and tail;
- scalar backreaction on the metric during propagation beyond linear order;
- non-spherical multipole radiation;
- quantum midisuperspace;
- phenomenal constitution.

## 5. Verification

Run:

    python verification/spherical_scalar_radiation.py
    python -m verification.spherical_scalar_radiation

Output:
[verification/spherical_scalar_radiation.json](verification/spherical_scalar_radiation.json).
The deterministic pure-Python verifier computes initial scalar kinetic energy
on the dressed geometry, radiated Bondi mass loss, and post-burst redshift and
Shapiro drifts.
