# Page–Wootters conditional time and the static spherical gravitational clock

The paper “Magnetic clock for a harmonic oscillator” (Coppo, Cuccoli, Verrucchi,
PRA 109, 052212, 2024; arXiv:2310.13386) implements the Page–Wootters (PaW)
relational-time mechanism using two non-interacting, entangled quantum
subsystems: a spin-\(J\) magnetic clock \(C\) and a harmonic oscillator
\(\Gamma\). Their more recent preprint “Quantum model for black holes and clocks”
(arXiv:2601.07437) applies the same conditions to identify a Schwarzschild black
hole as a “perfect clock,” with Hawking-like bosonic modes as the clock
subsystem. This note connects that literature to the symmetry-reduced
gravitational clock already constructed in this repository.

## 1. What the magnetic-clock paper proves

The PaW mechanism postulates a global stationary state
\[
  H_C\otimes I+I\otimes H_\Gamma=0,\qquad
  |\Psi\rangle\!\rangle=\int dt\,|t\rangle_C\otimes e^{-itH_\Gamma}|\psi_0\rangle_\Gamma.
\]
Conditioning on the clock “eigenstate” \(|t\rangle_C\) gives the evolving state
of \(\Gamma\). Coppo et al. realize \(C\) as a normalized spin-\(J\) system
with Hamiltonian \(H_C=B\hat J_0/J\) and \(\Gamma\) as a harmonic oscillator,
using generalized coherent states to show that as \(J\to\infty\) the conditional
description becomes classical phase-space dynamics.

Their key scaling: with clock frequency \(B\), system frequency \(\Omega_\Gamma\),
a finite-\(J\) clock introduces errors of order
\[
  \epsilon_J\sim\frac{\Omega_\Gamma^2}{4JB^2}, \tag{1}
\]
so macroscopic clocks (\(J\to\infty\)) reproduce Schrödinger evolution, while the
fully classical limit also requires coherent states for \(\Gamma\).

## 2. The gravitational static clock does not assume non-interaction

Our static spherical construction in
[QUANTUM_STATIC_SPHERICAL_CLOCK.md](QUANTUM_STATIC_SPHERICAL_CLOCK.md) is **not**
a PaW model with two postulated non-interacting subsystems. Its time structure
is derived from symmetry reduction:

- Birkhoff’s theorem gives a static exterior Schwarzschild geometry;
- the ADM mass is a **physical Dirac observable** generating translations
  along the asymptotic Killing vector;
- no bipartite tensor-product ansatz is imposed by hand.

The result is that one can **read** the gravitational reduced dynamics as a PaW
conditional-state structure: let
- clock \(C\) be the asymptotic Killing-time degree of freedom, conjugate to
  the ADM Hamiltonian with unit rate \(\Omega_C=1\) in proper-time units;
- system \(\Gamma\) be the dressed scalar one-body sector, with Hamiltonian
  \(H_{\mathrm{phys}}=H_0+V\).

Then the PaW history state conditioned on Killing time returns the dressed
Schrödinger evolution, with the gravitational dressing error bound already
computed by Duhamel:
\[
  \epsilon_{\mathrm{grav}}(T)\le T\|V\|\le T\mu(\langle 1-N\rangle_m+\delta_{\mathrm{curv}}).
\]

Crucially, the “interaction” is not removed: \(V\) is the gravitational dressing
of the field itself, and the clock is not an ancilla artificially decoupled from
gravity. It is the asymptotic structure of the actual gravitational field.

## 3. Magnetic-clock analogy and macroscopicity requirement

If one modeled the asymptotic clock as a finite-spin magnetic clock analogous to
Coppo et al., one would require
\[
  J\gtrsim \frac{\Omega_\Gamma^2}{4B^2\epsilon}
\]
to achieve error budget \(\epsilon\). With \(\Omega_\Gamma=\mu=22\),
\(B=\Omega_C=1\), and \(\epsilon=10^{-3}\), this gives
\(J\gtrsim 1.21\times 10^5\). The actual asymptotic ADM clock is a continuous
ideal clock (not a finite-\(J\) spin), so this finite-spin error is absent in the
ideal limit; the physical error is the gravitational dressing bound, not a
finite-\(J\) artefact.

Verified in
[verification/page_wootters_static_clock.py](verification/page_wootters_static_clock.py):
- \(\Omega_C=1\), \(\Omega_\Gamma=22\),
- \(V_{\mathrm{avg}}=0.00203\), \(T_{\mathrm{rel}}=0.492\) for \(0.1\%\) budget,
- required \(J\) for magnetic analog: \(1.21\times 10^5\),
- ideal ADM clock error: \(0\), dressing error saturates budget.

## 4. Black-hole clock comparison

Coppo, Pranzini, Verrucchi (2026) identify Schwarzschild black holes as “perfect”
PaW clocks via Hawking-like bosonic modes. That is a model built on the PaW
ansatz, not a derivation of Einstein gravity. Our weak-field dressed field
clouds do **not** form horizons (max compactness \(2M/R\approx0.10\) in the
nonlinear example), so they are complements rather than competitors:

- Their work uses PaW conditions to model a BH as clock;
- our work derives a physical Hamiltonian from Birkhoff-reduced Einstein gravity
  and photon-echo readout, then notes that the result is consistent with PaW
  conditioning rather than assuming it.

Our model does not have Hawking radiation or horizon thermality. The aspherical
quadrupole losses computed in
[ASPHERICAL_QUADRUPOLE_LOSS.md](ASPHERICAL_QUADRUPOLE_LOSS.md) are ordinary
slow-motion gravitational radiation from mechanical pulsations, not Hawking
flux.

## 5. What is gained

- Explicit connection between PaW relational-time literature and
  symmetry-reduced Einstein gravity;
- the difference between **postulated non-interacting bipartite clocks** and
  **derived gravitational Killing clocks** is made precise;
- the magnetic-clock macroscopicity scaling is mapped to our parameters,
  showing that a finite-spin emulation would require \(J\sim 10^5\) for a
  \(10^{-3}\) budget, while the continuous ADM clock has no such cutoff error;
- the result respects the already-proved gravitational bounds on dressing,
  Shapiro delay, and quadrupole loss.

Not supplied:

- a PaW treatment of full (non-spherical) quantum GR;
- Hawking evaporation or black-hole thermodynamics;
- phenomenal constitution or source derivation from the absolute.

## 6. Verification

Run:

    python verification/page_wootters_static_clock.py
    python -m verification.page_wootters_static_clock

Output:
[verification/page_wootters_static_clock.json](verification/page_wootters_static_clock.json).
The deterministic verifier records the clock/system identification, compares
the gravitational dressing error with the finite-\(J\) magnetic-clock error
scale, and maps the construction to Coppo/Cuccoli/Verrucchi 2024 and
Coppo/Pranzini/Verrucchi 2026.
