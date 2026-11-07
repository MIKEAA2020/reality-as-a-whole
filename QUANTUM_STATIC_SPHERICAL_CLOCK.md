# Quantum static spherical clock: a reduced physical Hamiltonian in gravitational symmetry reduction

The prior classical results in
[SMOOTH_FIELD_CLOCK.md](SMOOTH_FIELD_CLOCK.md),
[WEAK_BACKREACTION_RECORD.md](WEAK_BACKREACTION_RECORD.md), and
[LINEARIZED_SPHERICAL_RECORD.md](LINEARIZED_SPHERICAL_RECORD.md) constructed
smooth self-gravitating initial data and bounded relational records against
asymptotic proper time. This note makes the quantum step for the spherically
symmetric sector: it identifies a **physical Hamiltonian** that generates
Schwarzschild Killing time, thereby solving a small but genuine piece of the
problem of time in symmetry-reduced quantum gravity.

## 1. Why spherical symmetry matters

In full Einstein gravity, the Hamiltonian constraint
\[
H=0
\]
appears to forbid a preferred global time, because refoliations relate different
slices. But in the **spherically symmetric, asymptotically flat** sector,
Birkhoff’s theorem gives a rigid exterior:

- vacuum spherical geometry is locally the **Schwarzschild geometry**;
- there is a unique **Killing vector field** asymptotically aligned with
  stationary observer proper time;
- the **ADM mass** is conserved and generates translations along that Killing
  field.

Therefore, after spherical reduction, the ADM Hamiltonian is not just a
gauge-constraint remnant: it is a **physical Dirac observable** on the reduced
phase space, whose flow corresponds to asymptotic relational proper time. The
problem of “no external time” is resolved in this sector by the physical Killing
structure implied by Birkhoff, not by imposing an external background.

## 2. The static Hamiltonian and perturbation

For the constructed time-symmetric data, the physical Hamiltonian is the dressed
ADM Hamiltonian
\[
  H_{\mathrm{phys}}=N(H_g+H_m)+N^i D_i,
\]
restricted to the spherically symmetric reduced phase space. On the prepared
one-body scalar sector, write
\[
  H_{\mathrm{phys}}=H_0+V,
\]
where \(H_0\) is the flat free one-body Hamiltonian
\(\sqrt{p^2+\mu^2}\), and \(V\) is the gravitational perturbation from lapse and
spatial curvature.

For self-adjoint \(H_0,V\), Duhamel’s principle gives
\[
  \bigl\|e^{-iTH_{\mathrm{phys}}}\psi-e^{-iTH_0}\psi\bigr\|
  \le \min\bigl(2,T\|V\|\bigr)
\]
for normalized states. On the prepared smooth Gaussian, bound \(\|V\|\) using

1. the **central lapse redshift**
   \(\mu\max(1-N)\) as a worst-case bound;
2. the **matter-support-averaged redshift** \(\mu\langle 1-N\rangle_m\);
3. the **relative spatial-curvature energy shift**
   \(\delta_{\mathrm{curv}}\), so that the energy perturbation is bounded by
   \(\mu\delta_{\mathrm{curv}}\).

Thus
\[
  \epsilon_{\mathrm{quantum}}(T)\le
  \min\bigl(1,\,T\|V\|\bigr),\tag{1}
\]
with
\[
  \|V\|\le \mu\bigl(\langle 1-N\rangle_m+\delta_{\mathrm{curv}}\bigr),
\]
and the central bound replacing the averaged redshift for a more pessimistic but
still rigorous estimate. The cap to \(1\) applies to normalized-vector/trace
distance; for small times the linear bound dominates.

## 3. Verified cases

From [verification/quantum_static_spherical_clock.py](verification/quantum_static_spherical_clock.py),
using the same Picard data and integrands as the earlier classical reports.

### 3.1 Nonlinear binding family

For \(D=12\), \(m_0=20\), \(\mu=22\), \(R_0=20\), \(\epsilon=0.001\):

- \(\max(1-N)=0.0516193477\)
- \(\langle 1-N\rangle_m=0.0368515043\)
- \(\delta_{\mathrm{curv}}=0.0777725260\)
- central \(\|V\|\le 2.8466212220\)
- averaged \(\|V\|\le 2.5217286666\)
- for a \(1\%\) quantum vector-error budget,
  \(T_{\mathrm{rel}}\approx 0.00397\) (averaged), \(0.00351\) (central).

This agrees with the classical weak-backreaction slope. The dressed gravitational
clock is not a flat clock; its quantum relational time is short at the percent
level because the dressing itself is percent-scale.

### 3.2 Weak-backreaction case

For \(\epsilon=3\times10^{-5}\):

- \(\max(1-N)=4.356\times10^{-5}\)
- \(\langle 1-N\rangle_m=3.080\times10^{-5}\)
- \(\delta_{\mathrm{curv}}=6.161\times10^{-5}\)
- central \(\|V\|\le 0.00231\)
- averaged \(\|V\|\le 0.00203\)
- for \(0.1\%\) budget, \(T_{\mathrm{rel}}\approx 0.492\) (averaged),
  \(0.432\) (central).

The flat internal-mass-shift reference bound for the same Gaussian radius and
mass band gives a program-motion bound of about \(1.57\times10^{-5}\) over the
flat program time \(t_{\pi/a}\approx 12978\). The gravitational quantum bound
does not contradict that: it is a shorter-time bound because it includes the
full gravitational redshift and curvature, not just the finite internal mass
splitting on a flat background.

## 4. What this proves

A real, if limited, piece of the problem of time is solved here:

- In the **spherically symmetric asymptotically flat** sector, there is a
  physical, gauge-invariant Hamiltonian.
- Asymptotic proper time is not smuggled in as a background; it is the flow of
  the **ADM mass** along the Birkhoff Killing vector.
- The prepared one-body dressed clock state has a provable quantum record-error
  bound against that relational time.
- The bound includes both lapse redshift and spatial curvature, and it does not
  require freezing the geometry by hand.

This does **not** prove:

- a general solution to the problem of time without symmetry reduction;
- unitarity across arbitrary refoliations in full quantum GR;
- quantum Einstein constraints beyond the static spherical sector;
- phenomenal constitution or derivation of the prepared state from the absolute.

It is a constructive existence proof for a symmetry-reduced quantum
gravitational relational clock, not the final theory. [The asymptotic photon-echo
readout](PHOTON_ECHO_READOUT.md) adds a concrete operational record using radial
null geodesics in the dressed geometry. [The Page-Wootters synthesis](PAGE_WOOTTERS_STATIC_CLOCK.md)
connects this derived Killing Hamiltonian to PaW magnetic-clock and black-hole-clock models.

## 5. Verification

Run:

    python verification/quantum_static_spherical_clock.py
    python -m verification.quantum_static_spherical_clock

Output:
[verification/quantum_static_spherical_clock.json](verification/quantum_static_spherical_clock.json).
The deterministic pure-Python verifier recomputes the conformal factor,
classical Hamiltonian energies, averaged/central redshift, and both central and
averaged quantum Duhamel relational bounds, and compares with the flat
internal-mass-shift reference.
