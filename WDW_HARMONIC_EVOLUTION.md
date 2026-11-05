# Non-semiclassical WdW evolution: dressed harmonic-oscillator Gaussian states

The conserved positive-frequency inner product in
[WDW_INNER_PRODUCT.md](WDW_INNER_PRODUCT.md) defined a quantum Hilbert space for
the spherical R-clock, but the evolution was presented in WKB form. This note
gives an **exact non-semiclassical** evolution for the dressed harmonic scalar
mode: after positive-frequency projection of the WdW constraint, the internal-R
Tomonaga–Schwinger equation becomes
\[
  i\frac{\partial\Psi}{\partial l}=\hat H_{\mathrm{eff}}\Psi,\qquad
  \hat H_{\mathrm{eff}}=\sqrt{-\frac{d^2}{d\phi^2}+\mu^2\phi^2+V_{\mathrm{grav}}(\phi)}.
\]
For weak dressing \(V_{\mathrm{grav}}\) the effective Hamiltonian is a
**slightly frequency-shifted harmonic oscillator**,
\(\hat H_{\mathrm{eff}}\approx\omega_d(\hat n+\tfrac12)\), with
\(\omega_d=\mu(1-\Delta)\). Gaussian/coherent states of harmonic oscillators
propagate exactly under quadratic Hamiltonians—no WKB approximation needed.

## 1. Effective frequency shift

For the weak-backreaction cloud:

- redshift frequency shift \(\Delta_N=\langle 1-N\rangle_m=3.080\times10^{-5}\)
- curvature shift \(\Delta_c=\delta_{\mathrm{curv}}/2=3.080\times10^{-5}\)
- total operator perturbation \(V_{\mathrm{op}}=\mu(\Delta_N+\Delta_c)=0.001355\)
- dressed frequency \(\omega_d=21.998645\)
- ground-state width \(\sigma_0=1/\sqrt{2\omega_0}=0.15076\), \(\sigma_d=0.15076\).

The dressed and undressed Hamiltonians differ by a small quadratic perturbation
(frequency detuning). Ground-state overlap after propagation to proper radial
distance \(l=T\) is controlled by the width mismatch (negligible, since
\(\sigma_d-\sigma_0\sim 10^{-9}\sigma_0\)) and the accumulated phase difference
\(\Delta\phi=(\omega_0-\omega_d)T/2\).

## 2. Verified exact propagation

From [verification/wdw_harmonic_evolution.py](verification/wdw_harmonic_evolution.py):

| \(T=l\) | ground-state overlap | phase error | vector error | Duhamel bound \(V_{\mathrm{op}}T\) |
|---|---|---|---|---|
| 0.492 | \(1.0-2.4\times10^{-10}\) | \(3.33\times10^{-4}\) | \(3.33\times10^{-4}\) | \(6.67\times10^{-4}\) |
| 5.0 | \(1.0-2.4\times10^{-10}\) | \(3.39\times10^{-3}\) | \(3.39\times10^{-3}\) | \(6.78\times10^{-3}\) |
| 22.66 | \(1.0-2.4\times10^{-10}\) | \(1.54\times10^{-2}\) | \(1.54\times10^{-2}\) | \(3.07\times10^{-2}\) |

The vector error is exactly half the Duhamel operator bound (pure detuning
produces phase error bounded by \(\|V\|T/2\) for unitary rotation), well within
the dressed-clock bound. The width/squeezing contribution is essentially zero
(\(1-\mathrm{overlap}\sim 10^{-10}\)).

## 3. What is non-semiclassical here

- The evolution is not a WKB phase estimate but an **exact solution** of the
  quadratic Tomonaga–Schrödinger equation.
- Wavefunction width is preserved up to corrections \(10^{-10}\) because the
  dressing is weak, not because of a WKB approximation.
- The inner product from [WDW_INNER_PRODUCT.md](WDW_INNER_PRODUCT.md) is the
  conserved positive-frequency KG probability; no external Hilbert space is
  imposed by hand.
- This is the first genuinely quantum (non-WKB) propagation in the R-clock
  framework.

Limitations:

- Dressing is treated as an exactly quadratic frequency shift; higher-order
  anharmonic corrections are not included.
- The minisuperspace reduction assumes the spherical homogeneous mode;
  inhomogeneous/Kaluza-Klein modes are not propagated.
- Non-perturbative solutions, singularity resolution, and phenomenal
  constitution remain open.

## 4. Verification

Run:

    python verification/wdw_harmonic_evolution.py
    python -m verification.wdw_harmonic_evolution

Output:
[verification/wdw_harmonic_evolution.json](verification/wdw_harmonic_evolution.json).
The deterministic pure-Python verifier constructs the dressed harmonic
oscillator parameters, propagates Gaussian states exactly, computes overlap,
phase error, and vector error, and compares to the Duhamel operator bound.
