# Smooth dynamical clock matter: constraints, backreacting initial data, and a local-algebra bridge

## 1. What is advanced

Replace the singular carried point body by a **dynamical complex scalar
multiplet** whose mass matrix contains the whole finite autonomous program.
This supplies:

1. A smooth covariant matter action and explicit classical spatial-constraint
   closure, without a prescribed coordinate smearing.
2. An existence proof for a family of smooth, asymptotically flat, nonzero-charge
   Einstein–matter constraint data, including the source's gravitational field.
3. A quantitative recovery of the finite program for a normalizable Gaussian
   preparation on a fixed flat background, with motion and unwanted frequency
   branches distinguished.
4. A region-preserving isomorphism of the corresponding local field algebras
   on a fixed globally hyperbolic background. This does not require assuming
   that a field-basis rotation is implementable in one chosen Fock representation.

This is a **smooth finite-energy field completion**, not a stable bound body,
an anomaly-free quantum Einstein theory, or a record-error theorem for the
subsequent self-gravitating evolution. It removes the point-source singularity
from the matter model and initial constraints; it does not resolve every possible
future gravitational singularity.

The new initial-data example has Lambda=0 and an asymptotically flat end.
It is not the earlier homogeneous negative-Lambda scalar-band model, and it
does not inherit that model's physical root space or inner product. It continues
[the localized construction](LOCALIZED_CONSTRAINT_CLOCK.md), whose singular
point-body source was explicitly left incomplete.

## 2. Smooth covariant matter, not an external spatial profile

Use signature (-+++), c=hbar=1 and 8 pi G=1. Let Phi have D complex components,
A=A^dagger be the finite autonomous internal Hamiltonian, and

    M = m_0 I + A > 0,    K = M^2.

The action is

    S = integral d^4x sqrt(-g) [R/2
          - (g^{mu nu} partial_mu Phi^dagger partial_nu Phi
             + Phi^dagger K Phi)/2].

Here the complex field is equivalent to 2D real fields. If Phi=u+iw, use the
real symmetric mass matrix

    K_R = [[Re K, -Im K], [Im K, Re K]].

Canonical momenta below refer to these real components, avoiding factors of two
from complex-coordinate conventions. The potential is nonnegative. The field
equation is (-Box_g+K)Phi=0. The stress tensor is

    T_mu nu = Re(partial_mu Phi^dagger partial_nu Phi)
       - g_mu nu [partial_alpha Phi^dagger partial^alpha Phi
                   + Phi^dagger K Phi]/2.

It is smooth for smooth field and metric data. There is no frozen Gaussian
stress distribution: any Gaussian used below is an initial condition for fields
that subsequently evolve, spread, and gravitate. Neither the initial profile nor
the program/source preparation has been derived from a zero-residue constitution.

All source offsets, clock hopping energies and record-system energies are
inside M. They cannot be subtracted as nongravitating phases. This realization
encodes the program in flavor mixing; it does not derive a macroscopic device
or interactions with additional quantum fields from microscopic constituents.
The finite internal dimension does not make the whole field theory finite:
spatial field and gravitational degrees of freedom remain continuous. No
ultraviolet cutoff or quantum vacuum-energy budget has been supplied.

## 3. Spatial constraints and the gradient term that closes them

Write phi for the 2D real components, pi for their momentum densities, and
q=det(q_ab). The smooth matter constraints are

    H_m[N] = integral d^3x N h_m,
    h_m = pi^T pi/(2 sqrt(q))
            + sqrt(q) [q^{ab} partial_a phi^T partial_b phi
                       + phi^T K_R phi]/2,
    D_m[xi] = integral d^3x xi^a pi^T partial_a phi.

Use the ordinary ADM gravitational constraints, with compactly supported
smearings or boundary conditions that remove the relevant boundary terms.
This is not a new proof of pure ADM closure. The matter and mixed contributions
can be derived directly. Put

    w^a = sqrt(q) q^{ab} partial_b phi,
    delta H_m[N]/delta pi = N pi/sqrt(q),
    delta H_m[N]/delta phi = N sqrt(q) K_R phi - partial_a(N w^a).

The potential and the unweighted divergence terms cancel between two lapse
orders. The remainder is

    {H_m[N],H_m[L]}
      = integral pi^T q^{ab} partial_b phi (N partial_a L - L partial_a N)
      = D_m[q^{-1}(N dL - L dN)].

Thus the dynamical gradient energy supplies the necessary momentum density;
a fixed coordinate profile with no conjugate matter momentum would not supply
this canonical mechanism.

The matter Hamiltonian depends locally on q but not its conjugate momentum.
As in the carried-body calculation, delta H_g[N]/delta pi_grav is N times
a local tensor. The mixed gravitational/matter Hamiltonian terms are local
products N L antisymmetrized in N,L, and cancel. Field, momentum-density and
metric transformations together make h_m a scalar density of weight one.
Consequently, for H=H_g+H_m and D=D_g+D_m,

    {H[N],H[L]} = D[q^{-1}(N dL - L dN)],
    {D[xi],H[N]} = H[Lie_xi N],
    {D[xi],D[eta]} = D[[xi,eta]].                         (1)

The verifier checks 160 three-dimensional metric/field jets for the lapse
bracket and another 160 density-transformation identities. Residuals are below
1.2e-13. These are checks of the displayed local identities, not quantum
commutators or a lattice continuum-limit argument.

## 4. Nonlinear gravitational constraint data: an existence proof

This step does not put the Gaussian on a prescribed flat spatial metric.
Choose an initial slice R^3, zero extrinsic curvature, and

    q_ab = psi(r)^4 delta_ab,    psi -> 1 at infinity,
    Phi(r) = epsilon f(r) v,
    n^mu partial_mu Phi(r) = -i M Phi(r),
    f(r) = exp[-r^2/(2 R_0^2)],    v^dagger v=1,
    mu = v^dagger M v,    kappa = v^dagger M^2 v.

The physical normal derivative is prescribed; its canonical momentum density
therefore contains psi^6. This is a conformal initial-data ansatz, not an
assumption that arbitrary canonical product data already solve the constraints.
The matter momentum density vanishes exactly:

    Re[(n partial Phi)^dagger partial_a Phi]
       = Re[i epsilon^2 f partial_a f v^dagger M v] = 0.

Hence the momentum constraint is satisfied, while normal energy density is

    rho = epsilon^2 [kappa f^2 + psi^(-4) (f')^2/2].

The Hamiltonian constraint is R^(3)=2 rho. Since
R^(3)=-8 psi^(-5) Delta psi, it becomes

    Delta psi = -epsilon^2 [psi (f')^2 + 2 kappa psi^5 f^2]/8.             (2)

### A contraction on the whole radial half-line

For S_psi=psi(f')^2+2 kappa psi^5 f^2 define

    T psi(r) = 1 + epsilon^2/8 [ (1/r) integral_0^r s^2 S_psi(s) ds
                                + integral_r^infinity s S_psi(s) ds ].

At r=0 use the continuous limit. Nonnegative radial Newton potentials have
their maximum at the origin. On the closed sup-norm strip 1<=psi<=1+b,

    ||T psi - 1||_infinity
      <= epsilon^2 [(1+b)+2 kappa R_0^2 (1+b)^5]/16 = B_map,

    ||T psi - T chi||_infinity <= L ||psi-chi||_infinity,
    L = epsilon^2 [1+10 kappa R_0^2 (1+b)^4]/16.

These use the exact Gaussian integrals
integral s(f')^2 ds=1/2 and integral s f^2 ds=R_0^2/2.
If B_map<=b and L<1, Banach contraction gives a unique solution **in this
strip**. The integral equation gives psi'(0)=0 and the correct asymptotic end;
elliptic regularity bootstraps it to a smooth positive metric and smooth source.
Uniqueness outside the strip or uniqueness of reality is not inferred.

For the 12-dimensional copying program of the localized report,

    gamma=.05, E_c=2, m_0=20,
    v=|clock 0> |+>_R |0>_B,
    mu=22, kappa=484.0025.

Choose R_0=20, epsilon=.001, b=.1. Then

    B_map = .0389746121 < .1,
    L = .1771570776 < 1.

Thus existence is analytic, independent of trusting a radial numerical solution.
It is not a fixed-background test-particle initial condition: the solved psi
is nonconstant and its ADM energy is nonzero.

### Energy, charge, and regularity accounting

Asymptotically psi=1+C/r plus decaying terms, where

    C = epsilon^2/8 integral_0^infinity r^2
                    [psi(f')^2 + 2 kappa psi^5 f^2] dr.

Its rigorous strip bounds are

    epsilon^2/8 [3 sqrt(pi) R_0/8 + kappa sqrt(pi) R_0^3/2] <= C
    <= epsilon^2/8 [(1+b) 3 sqrt(pi) R_0/8
                         + (1+b)^5 kappa sqrt(pi) R_0^3/2].

For 8 pi G=1, E_ADM=16 pi C (geometric mass G E_ADM=2C). Proper matter
energy and positive U(1) charge, with charge convention -Im(Phi^dagger n dPhi),
are

    E_proper = 4 pi epsilon^2 integral r^2
                 [psi^2(f')^2/2 + kappa psi^6 f^2] dr,
    Q_charge = 4 pi epsilon^2 mu integral r^2 psi^6 f^2 dr.

In particular,

    E_proper - E_ADM = 4 pi epsilon^2 integral r^2
       [(psi^2-psi)(f')^2/2 + kappa(psi^6-psi^5)f^2] dr > 0.

The negative binding contribution has not been omitted. This is classical
charge, not a claim that the data are a one-particle quantum state or that their
stress fluctuations justify semiclassical gravity.

Also psi'=-epsilon^2 integral_0^r s^2 S_psi ds/(8r^2). Thus

    1 + 2r psi'/psi >= (1-b)/(1+b) > 0.

There are no marginal round spheres on this time-symmetric initial slice.
This is not a no-collapse or global-singularity theorem.

The radial Picard estimates, at 8192 steps out to 8R_0, are:

| Quantity | Estimate |
|---|---:|
| psi(0) | 1.0268540555 |
| C | .4710547067 |
| ADM energy | 23.67779210 |
| Proper matter energy | 24.12671582 |
| ADM minus proper energy | -.44892372 |
| Positive classical charge | 1.09665932 |

The analytic C bounds are [.4289377092,.6908076217]. Gaussian tail truncation
and quadrature are not used to prove existence. Three resolutions are compared;
the radial numbers and discrete Green residuals are **estimates**, not interval
certificates for the continuum solution. The source has Gaussian tails and finite
total energy, not a sharp finite spatial boundary or a demonstrated bound state.

## 5. Recovering the program without a sharp-momentum assumption

### Quantum one-body benchmark on fixed flat spacetime

In the canonical positive-frequency representation
L2(R^3,d^3p) tensor C^D take

    H(p) = sqrt(p^2 + M^2),
    delta=A-E_c I, a=||delta||, m=m_0+E_c, M_min=m-a>0,
    E_0(p)=sqrt(p^2+m^2).

Prepare a normalized spatial Gaussian

    g_R(x) = (pi R^2)^(-3/4) exp[-r^2/(2R^2)],
    <p^4> = 15/(4R^4).

Compare the actual joint motion/internal unitary with
exp[-it E_0(p)] exp[-it delta]. The center-of-mass comparison is allowed to
spread; the spatial profile is not held fixed. For every eigenvalue lambda of
delta, integrate the mass derivative to obtain

    |sqrt(p^2+(m+lambda)^2)-sqrt(p^2+m^2)-lambda|
       <= a [1-M_min/sqrt(p^2+M_min^2)]
       <= a p^2/(2 M_min^2).

Consequently, for the fixed Gaussian preparation and arbitrary internal input
(including an input ancilla), joint vector error is at most
B_motion=|t| a sqrt(15)/(4 M_min^2 R^2). Trace distance and the
half-diamond error of that initialized channel satisfy

    epsilon_motion <= min(1, B_motion).                                (3)

The cap applies to channel/trace distance, not to raw vector error.

This uses the full Gaussian moment; no uncounted momentum tails or mean-momentum
substitution occur. At the copy duration t=pi/a=44.42882938, R=20, it is
1.5813442e-5. The explicit spectral quadrature estimates vector error
1.1110050e-5. At this duration the ideal internal output is the retained copied
record from the preceding report; its center-of-mass wavefunction has evolved.

For an internal complete instrument with error epsilon_internal, contraction
adds at most epsilon_motion. This is a flat-background composition statement,
not a theorem about the self-gravitating solution of section 4.

### Classical initial phase is not exactly a positive-frequency condition

The section-4 prescription n dPhi=-iM Phi is local. On flat spacetime the exact
positive-frequency condition instead uses E(p)=sqrt(p^2+M^2). For the same
classical Gaussian configuration, the two frequency coefficients are

    Phi_+(p) = (I+M/E(p)) Phi_0(p)/2,
    Phi_-(p) = (I-M/E(p)) Phi_0(p)/2.

The negative-frequency coefficient obeys

    ||Phi_-||_L2 / ||Phi_0||_L2 <= sqrt(15)/(8 M_min^2 R^2).

The complete classical configuration at time t therefore differs, in relative
L2 configuration norm, from the same Gaussian carrier times the ideal internal
program by at most

    epsilon_configuration <= (1+|t|a) sqrt(15)/(4 M_min^2 R^2).           (4)

For this example the negative-branch bound is 2.5167874e-6 and (4) is
2.0847017e-5. The estimates are respectively 2.5006656e-6 and 1.1273405e-5.

These L2 configuration norms are **not** particle probabilities or quantum
trace distances. The classical Cauchy field and the canonical one-body Gaussian
are separate preparations; energy-dependent conversions between Klein–Gordon
and canonical one-body normalizations must not be suppressed. The estimates
show a controlled flat limit, not that classical gravitational data constitute
a quantum one-body state.

## 6. Exact dressing and the AQFT connection

Let A=Q A_0 Q^dagger as in the finite autonomous construction. Q is a constant
internal unitary, not a spacetime-dependent transformation. Then

    M=Q M_0 Q^dagger, K=Q K_0 Q^dagger,
    Phi=Q Phi_0.

Kinetic and gradient terms are unchanged, and the stress tensors agree pointwise:

    T[g,Q Phi_0;K] = T[g,Phi_0;K_0].

Thus any **classical** coupled Einstein–multiplet solution for K_0 transfers to
one for K with the same geometry. The transformation preserves classical
constraints and any available existence/regularity result; it does not by
itself calculate the geometry or the quality of its relational records.

On a fixed globally hyperbolic spacetime, use real components and the constant
orthogonal representative Q_R. For P_K=-Box_g+K_R, retarded and advanced
propagators and their causal difference satisfy

    E_K = Q_R E_0 Q_R^T.

This follows either from uniqueness of the Green operators or by decomposing
into mass eigenvalues. Each scalar Klein–Gordon propagator has causal support;
constant internal mixing preserves that support. Therefore test-function
rotation f -> Q_R^T f preserves both their spacetime support and the symplectic
pairing integral f^T E_K g. It induces a local Weyl-algebra isomorphism

    W_K(f) -> W_0(Q_R^T f).

In particular, each region's algebra maps to the **same region's** algebra;
spacelike commutativity is preserved. Suitable states can be pulled back through
this isomorphism; constant internal rotation also preserves the Hadamard
wavefront condition on a fixed background when it holds initially.

This is a concrete local-field/AQFT compatibility bridge, not an identification
of local algebras with conscious subjects, and not an AQFT construction of
quantum spacetime. A finite internal matrix is not enough to assert unitary
implementability in one fixed infinite-dimensional Fock representation. A
Fock implementer requires the appropriate representation condition, or an
explicitly transported representation/complex structure. The algebraic
isomorphism does not depend on making that extra assertion.
The isomorphism transports states and observables together. Holding bare
preparation and clock/record effects fixed is a different physical comparison;
the algebraic map is not a cost-free externally applied gate.

The verifier checks the mass rotation and 16 Fourier causal-propagator matrix
identities. Causal support is an analytic field-theory statement, not something
established by those Fourier samples. Renormalized quantum stress-energy and
quantum Einstein constraint domains require additional work; classical closure
is not silently promoted to quantum closure.

## 7. Verification and the next direct problem of time

Run:

    python verification/smooth_field_clock.py
    python -m verification.smooth_field_clock

Output: [smooth_field_clock.json](verification/smooth_field_clock.json).
The deterministic pure-Python verifier checks local bracket jets, radial Picard
estimates at three resolutions, Gaussian spectral integrals, and finite matrix
propagator dressing. The contraction and algebraic proofs are given above;
the estimates are not a numerical spacetime evolution.

The constructive gain is a nonsingular matter model with nontrivial
self-gravitating constraint data and a compatible local field algebra—not just
an instruction to smooth a point source. Classical constraint consistency and
flat-limit clock operation are supplied separately and without conflating them.

**Still unsupplied:** a stable finite-size apparatus, controlled record quality
through the actual coupled Einstein–multiplet evolution, a gravitational
physical inner product and quantum constraint baseline, source-state derivation,
and phenomenal constitution. Initial-data existence alone does not make a
reliable self-gravitating clock, and fixed-background AQFT does not supply a
quantization of refoliations.

[Weak-backreaction relational records](WEAK_BACKREACTION_RECORD.md) give the
quasistatic dressing bound, and [linearized spherical records](LINEARIZED_SPHERICAL_RECORD.md)
use Birkhoff’s theorem and Misner–Sharp areal compactness to justify a static
exterior Schwarzschild metric with zero linear-order spherical radiation loss.
Non-spherical/non-perturbative coupled evolution and a quantum
Einstein-constraint physical norm remain open.
