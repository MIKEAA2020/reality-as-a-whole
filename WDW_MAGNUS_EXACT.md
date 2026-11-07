# Exact Tomonaga propagator via Magnus integrability

> **Scope correction:** The integrated-phase propagator is exact for the stipulated fixed-number-operator family `H(l)=ω(l)(N+1/2)`. It is not established as the propagator of the earlier variable-frequency or square-root WdW Hamiltonians; the displayed variable-frequency oscillator Hamiltonians generally do not commute. See [WDW_INTERFACE_CORRECTIONS.md](WDW_INTERFACE_CORRECTIONS.md).

The self-adjointness proof in [WDW_SELF_ADJOINT.md](WDW_SELF_ADJOINT.md) guaranteed
a unique unitary Tomonaga propagator; the harmonic and radial/adiabatic results
[WDW_HARMONIC_EVOLUTION.md](WDW_HARMONIC_EVOLUTION.md)–[WDW_ANGULAR_COUPLING.md](WDW_ANGULAR_COUPLING.md)
bounded corrections. This note closes the quadratic sector completely: when the
dressing is a pure frequency shift \(\omega(l)\) acting on a fixed number
eigenbasis, the Tomonaga propagator is **exactly** the integrated-phase
exponential, with no non-adiabatic or Magnus higher-order corrections.

## 1. Commuting Hamiltonians and Magnus termination

For pure quadratic dressing the Tomonaga Hamiltonian at each internal-\(l\) slice
\[
  \hat H_{\mathrm{eff}}(l)=\omega(l)\left(\hat n+\tfrac12\right),\qquad
  \hat n=a^\dagger a,
\]
is diagonal in the harmonic-oscillator number basis. Hamiltonians at different
\(l_1,l_2\) share the same eigenbasis, so they **commute**:
\[
  [\hat H_{\mathrm{eff}}(l_1),\hat H_{\mathrm{eff}}(l_2)]=0.
\]
The Magnus expansion for the time-ordered exponential therefore terminates at
first order:
\[
  U(l_2,l_1)=\mathcal T\exp\!\left(-i\int_{l_1}^{l_2}\hat H_{\mathrm{eff}}(l')\,dl'\right)
  =\exp\!\left(-i\Phi(l_2,l_1)\left(\hat n+\tfrac12\right)\right),
\]
with the integrated phase
\[
  \Phi(l_2,l_1)=\int_{l_1}^{l_2}\omega(l')\,dl'.
\]
The second-order Magnus term \(\Omega_2=\tfrac12\iint[H(l'),H(l'')]dl'dl''\)
vanishes identically, and there are no non-adiabatic transitions between number
eigenstates because \(\langle m|\partial_l H|n\rangle=\omega'(l)(n+\tfrac12)\delta_{mn}\)
is purely diagonal.

## 2. Verified numbers

From [verification/wdw_magnus.py](verification/wdw_magnus.py), linear ramp
\(\omega(l)=\omega_0-(\omega_0-\omega_d)l/R_m\) from \(\omega_0=22\) to
\(\omega_d=21.99960\):

- commutator vanishes: true
- Magnus second-order integral: \(0.0\)
- off-diagonal \(\langle m|\partial_l H|n\rangle\) maximum: \(0.0\)
- exact integrated phase \(\Phi=498.4494\)
- static-Killing approximation \(\Phi_{\mathrm{static}}=\omega_0 R_m=498.454\)
  (error \(4.6\times10^{-3}\))
- constant-dressed approximation \(\Phi_d=\omega_d R_m=498.4449\)
- transition probability between levels: exactly zero.

The dressed-WKB phase computed semiclassically in
[WDW_SPHERICAL_R_CLOCK.md](WDW_SPHERICAL_R_CLOCK.md) was \(498.45\), matching
this exact result to within numerical accuracy of the WKB discretization. What
was presented as a semiclassical WKB estimate is actually the **exact quantum
propagator** for the quadratic-dressed sector.

## 3. Significance

This completes the quadratic-sector chain:

- The WdW physical inner product is conserved ([WDW_INNER_PRODUCT.md](WDW_INNER_PRODUCT.md)).
- Gaussian states propagate exactly under the quadratic Hamiltonian
  ([WDW_HARMONIC_EVOLUTION.md](WDW_HARMONIC_EVOLUTION.md)).
- Particle production is adiabatically negligible for monopole and radial modes
  ([WDW_PARTICLE_PRODUCTION.md](WDW_PARTICLE_PRODUCTION.md), [WDW_RADIAL_MODES.md](WDW_RADIAL_MODES.md)).
- Angular multipoles are adiabatic with power-law suppressed tensor coupling
  ([WDW_ANGULAR_COUPLING.md](WDW_ANGULAR_COUPLING.md)).
- The dressed Hamiltonian is essentially self-adjoint, generating unique unitary
  flow ([WDW_SELF_ADJOINT.md](WDW_SELF_ADJOINT.md)).
- The unitary flow is exactly the integrated phase (Magnus terminates at order
  1, no non-adiabatic corrections): WKB was exact for this dressing class.

Limitations:

- Commuting-Hamiltonians integrability relies on the dressing being a pure
  frequency scaling. [WdW anharmonic self-interaction](WDW_ANHARMONIC.md)
  quantifies the small corrections from \(\lambda\phi^4\); mode-mixing from
  angular tensor coupling is treated in [WdW angular coupling](WDW_ANGULAR_COUPLING.md).
- Weak-field regime only; strong-field collapse introduces horizon/singularity
  structure that invalidates the simple quadratic reduction.
- Phenomenal constitution remains open.

## 4. Verification

    python verification/wdw_magnus.py
    python -m verification.wdw_magnus

Output:
[verification/wdw_magnus.json](verification/wdw_magnus.json).
The deterministic pure-Python verifier constructs the linear frequency ramp,
confirms vanishing commutator numerically over a 200×200 grid, checks that
Magnus second-order term is zero, bounds off-diagonal \(\partial_l H\) matrix
elements to zero, computes the exact integrated phase, and compares to
static/constant-dressed approximations.
