# Essential self-adjointness of the dressed WdW Tomonaga Hamiltonian

A unitary Tomonaga–Schrödinger evolution in internal \(l\)-time requires the
effective Hamiltonian \(\hat H_{\mathrm{eff}}\) to be self-adjoint on the
positive-frequency physical Hilbert space. For the quadratic dressed scalar
sector, essential self-adjointness follows from Kato–Rellich and Nelson's
analytic-vector theorem, with norm-resolvent convergence to the undressed
harmonic oscillator as dressing goes to zero.

## 1. Setup

After positive-frequency projection of the WdW constraint, the quadratic
Tomonaga Hamiltonian on each \(l\)-slice is the dressed harmonic oscillator
\[
  \hat H_{\mathrm{eff}}(l)=-\frac{d^2}{d\phi^2}+\omega(l)^2\phi^2
\]
(acting on the one-particle positive-frequency Hilbert space obtained from the
square-root WdW constraint; the self-adjointness argument applies identically
to the positive-frequency square-root form). The dressed frequency
\(\omega(l)=\mu\,N(l)\), with lapse/curvature giving
\(\omega_0=\mu=22\), \(\omega_d=21.99864\), and
\(V_{\mathrm{op}}=\omega_0-\omega_d=1.36\times10^{-3}\).

## 2. Essential self-adjointness

The operator \(-d^2/d\phi^2+\omega^2\phi^2\) is the quantum harmonic oscillator,
essentially self-adjoint on \(\mathcal S(\mathbb R)\) (or the Hermite basis) by
Nelson's analytic-vector theorem. The dressing perturbation
\(V(\phi)=(\omega_d^2-\omega_0^2)\phi^2\) is a quadratic potential, which by
Kato–Rellich is infinitesimally bounded with respect to the unperturbed
oscillator, with relative bound
\(b=V_{\phi}/(2\omega_0^2)=6.2\times10^{-5}\ll1\). Hence \(\hat H_{\mathrm{eff}}(l)\)
is essentially self-adjoint and varies norm-resolvent continuously in \(l\).

## 3. Verified bounds

From [verification/wdw_self_adjoint.py](verification/wdw_self_adjoint.py):

- ground-state energy \(E_0^{(d)}=10.9993>0\)
- resolvent norm at \(z=-i\): \(||(H+i)^{-1}||=0.0905\), dressed to \(0.09054\)
- Kato relative bound: \(6.16\times10^{-5}\)
- norm-resolvent difference \(||R_d(-i)-R_0(-i)||\le5.6\times10^{-6}\)
- first 11 eigenvalues shift uniformly by \(V_{\mathrm{op}}(n+\tfrac12)\),
  preserving equidistant harmonic spectrum.

## 4. Consequence: unique unitary Tomonaga flow

By Stone's theorem, the self-adjoint \(\hat H_{\mathrm{eff}}(l)\) generates a
unique strongly continuous unitary propagator
\[
  U(l_2,l_1)=\mathcal T\exp\!\left(-i\int_{l_1}^{l_2}\hat H_{\mathrm{eff}}(l')\,dl'\right).
\]
This is a rigorous quantum evolution law in internal R-time, justifying the
exact Gaussian propagation in [WDW_HARMONIC_EVOLUTION.md](WDW_HARMONIC_EVOLUTION.md)
as the unique quantum flow of the dressed Hamiltonian.

Limitations:

- Quadratic dressed sector; anharmonic/self-interacting potentials are not yet
  treated (Kato–Rellich covers bounded/semibounded polynomial perturbations
  under mild conditions).
- One-/multi-mode radial Hamiltonians, not full 3+1 quantum gravity.

[WdW angular coupling](WDW_ANGULAR_COUPLING.md) treats non-spherical/angular
sectors at multipole level, finding strong suppression in weak field, and
[WdW exact Magnus propagator](WDW_MAGNUS_EXACT.md) proves the quadratic dressed
flow is exactly the integrated phase with no non-adiabatic corrections. Strong-field
singularity resolution and phenomenal constitution remain open.

## 5. Verification

    python verification/wdw_self_adjoint.py
    python -m verification.wdw_self_adjoint

Output:
[verification/wdw_self_adjoint.json](verification/wdw_self_adjoint.json).
