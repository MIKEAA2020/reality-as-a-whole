# Perspectival finitude: why finite observers see limited information

[RELATIONAL_PERSPECTIVE.md](RELATIONAL_PERSPECTIVE.md) constructed conditional
states for observers within the timeless WdW wavefunction. This note quantifies
the **finitude** of those perspectives: a finite-energy observer has access to a
finite-dimensional Hilbert subspace, a finite number of distinguishable clock
ticks, and an irreducible entropy of unobserved degrees of freedom, even though
the global wavefunction is pure and changeless.

## 1. Finite observer model

Take a bound-state observer with scalar excitation budget \(n_{\max}=10\) (i.e.
the observer's subsystem has energy budget \(E_{\mathrm{obs}}=(n_{\max}+1/2)\mu=231\),
eleven accessible harmonic levels including ground). The clock is localized with
width \(\sigma_R=R_{\mathrm{tick}}=0.0455\) (from [WDW_SPHERICAL_R_CLOCK.md](WDW_SPHERICAL_R_CLOCK.md)).

## 2. Verified bounds

From [verification/perspectival_finitude.py](verification/perspectival_finitude.py):

- Ground-state energy \(E_0=\mu/2=11\), level spacing \(\omega=22\).
- Phase resolution \(\Delta\phi=H\sigma_R\approx1.0\) radian per clock tick
  (cannot resolve sub-tick phases).
- Margolus–Levitin orthogonalization time
  \(t_{\perp}=\pi/(2E_{\mathrm{obs}})=6.8\times10^{-3}\).
- Distinguishable ticks within \(R_m\): \(N_{\mathrm{ticks}}=R_m/t_{\perp}=3331\).
- Accessible Hilbert-space dimension \(N_{\mathrm{eff}}=n_{\max}+1=11\).
- Maximum von Neumann entropy of accessible subsystem:
  \(S_{\max}=\ln N_{\mathrm{eff}}=2.40\) nats.
- Unobserved modes (20 radial × 11 angular = 220): coarse-grained entropy
  \(S_{\mathrm{unobs}}\approx N\ln 2\approx152\) nats.

## 3. Significance

- Global reality (the WdW wavefunction) is **pure**: zero entropy, changeless,
  complete.
- Any finite-energy conditional perspective sees **finite information**:
  bounded clock resolution, finite Hilbert space, positive entropy from
  unobserved modes.
- This formalizes the "finite disclosure" idea from the constitutional
  framework without introducing any separate created substance: finitude is
  perspectival structure within the one complete actuality, not a positive
  addition or privative substance. It is a *relational limit on accessible
  information*, consistent with the absolute's completeness and perfection.
- The gap between \(S_{\max}\) for a simple observer (2.4 nats) and the
  coarse-grained entropy of unobserved modes (152 nats) is what makes
  observation partial: a finite perspective cannot condition on all degrees of
  freedom simultaneously.

Limitations:

- Observer model is a 1D HO bound state with arbitrary \(n_{\max}=10\); real
  observers have vastly more structure (but the scaling bounds hold: finite
  energy ⇒ finite accessible information).
- Coarse entropy estimate uses one qubit per unobserved mode; rigorous
  entropic bounds would require proper thermal/subsystem decomposition.
- Phenomenal consciousness (what-it-is-like-to-be such a perspective) is not
  derived; this is an information-theoretic skeleton for finitude, not an
  answer to the hard problem.

## 4. Verification

    python verification/perspectival_finitude.py
    python -m verification.perspectival_finitude

Output:
[verification/perspectival_finitude.json](verification/perspectival_finitude.json).
