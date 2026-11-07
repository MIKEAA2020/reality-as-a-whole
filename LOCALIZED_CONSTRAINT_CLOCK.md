# A localized finite clock and the spatial constraint algebra

## 1. Direct result, and its exact boundary

A finite autonomous clock/record program can be carried by a localized massive
body without adding an external time-dependent source to Einstein's constraints.
Its complete internal Hamiltonian contributes to its rest mass. The resulting
matter Hamiltonian and momentum constraints satisfy the classical
hypersurface-deformation identities, including the spatial-metric structure
function. The mixed gravity/matter terms cancel. This is a spatially local
extension, not a second homogeneous lapse constraint.

There is also a conditional quantum preservation result: the internal unitary
dressing used for the autonomous program preserves whatever quantum constraint
algebra and domains a consistent **free carried-body gravitational theory** has.
It cannot manufacture such a baseline theory or repair its anomalies.

Two limits are essential:

* Point-body coupling is treated as a distributional canonical model on smooth
  ADM kinematic data. A self-gravitating point source has singular-field and
  regularization problems. No finite-body Einstein solution is supplied here.
* The explicit quantum evolution calculation below is on a fixed flat
  background. Neither an anomaly-free quantum Einstein algebra nor a full
  gravitational physical Hilbert space has been constructed.

This continues [the finite-resource program](CORRELATED_PUMP_CERTIFICATION.md)
by addressing spatial constraints rather than adding another verification layer.
Unlike [the earlier two-clock example](MULTI_CLOCK_CONSTRAINT_CLOSURE.md), the
structure function here is the inverse spatial metric of ADM gravity. This is
a changed, spatially inhomogeneous model: the earlier homogeneous scalar-band
root space and physical inner product are not automatically inherited.

## 2. Covariant localized apparatus

Use signature (-+++), c=hbar=1, and a timelike worldline X^mu(u), where u is an
arbitrary parameter. Let z have D complex internal amplitudes, z^dagger z=1.
A constant Hermitian matrix A is the **whole** autonomous internal Hamiltonian:
clock, source, system, reference ladders, controls, pointers, and stored records
as appropriate. Define

    M(z) = m_0 + z^dagger A z,    m_0 + min spec(A) > 0.

A covariant first-order worldline action, added to Einstein–Hilbert gravity, is

    S_body = integral du [P_mu Xdot^mu + i z^dagger zdot
               - e/2 (g^{mu nu}(X) P_mu P_nu + M(z)^2)
               - nu (z^dagger z - 1)].

The internal symplectic convention is {z_j,z_k^*}=-i delta_jk. The number
constraint generates an irrelevant common internal phase. In that phase gauge,

    ds/du = e M,
    i dz/ds = A z,
    dM/ds = 0.

Thus the autonomous program evolves in the body's proper time at the classical
worldline level. No switching function of coordinate time u has been inserted.
The offset m_0, the internal source offset, and all internal energies gravitate;
none may be removed from M as a harmless phase subtraction.

This is a monopole worldline model of a carried apparatus. The working system
and registers are internal to the same body. Couplings to independently
distributed quantum fields, finite-size stresses and higher multipoles require
additional dynamical terms; they have not been derived from this action.

The amplitude formulation is a classical internal symplectic model. Quantizing
D oscillator modes in the one-boson sector yields C^D and the mass operator
M_hat=m_0 I+A. Choosing the quantum mass-shell operator with M_hat^2 is a
specified ordering, not a proof that all quantizations of the classical squared
mass coincide. No microscopic derivation of the internal modes is asserted.

## 3. ADM constraints and the momentum-sign issue

Write the metric as

    ds^2 = -N^2 dt^2 + q_ab (dx^a + N^a dt)(dx^b + N^b dt).

Take a worldline crossing each slice once, with canonical {X^a,p_b}=delta^a_b,
and select the future, positive-mass branch. Put

    E = sqrt(q^{ab}(X) p_a p_b + M^2),
    H_body[N] = N(X) E,
    D_body[xi] = -p_a xi^a(X).

The minus sign is necessary in this convention. Fields transform by their Lie
derivative under D_grav[xi], while a coordinate location transforms as
{X^a,D_body[xi]}=-xi^a(X). Keeping the point fixed while transforming the
metric would not define a spatially covariant apparatus.

The full constraints are

    H[N] = H_grav[N] + H_body[N],
    D[xi] = D_grav[xi] + D_body[xi].

A cosmological constant can be retained in H_grav; it does not alter the
identities below. We assume the usual classical ADM gravitational identities
and boundary conditions under which boundary terms vanish (for example compact
spatial slices and smooth smearings). The new derivation concerns the added
localized matter and its mixed terms, not a fresh derivation of pure ADM.

Hamilton's equations give

    Xdot^a + N^a = N q^{ab}p_b/E,
    ds/dt = N M/E,
    i zdot = (N M/E) A z                 [up to the number-constraint phase].

Clock motion and gravitational redshift therefore change the coordinate rate;
the internal proper-time equation is unchanged. In general the finite clock's
site coordinate is not itself a precision proper-time estimator.

## 4. Explicit closure with spatially varying lapse and shift

All expressions in this section are equalities of smeared classical functionals
on smooth positive-metric kinematic data, with the particle evaluation defined.
No product of two delta distributions is required in these bracket identities.
This does not establish well-posed evolution on singular constrained data.

### Two lapse deformations

Let v^a=q^{ab}p_b. Then

    partial_{p_a} H_body[N] = N v^a/E,
    partial_{X^a} H_body[N] = (partial_a N) E + N partial_a E.

The spatial-metric derivative terms cancel between the two orders. The internal
bracket also vanishes: the internal dependence is through the same M, so it is
proportional to {M,M}=0. Therefore

    {H_body[N],H_body[L]}
       = p_a q^{ab}(L partial_b N - N partial_b L)
       = D_body[beta],
    beta^a = q^{ab}(N partial_b L - L partial_b N).

This has the correct spatial-metric structure function, not an engineered
clock-rate rescaling.

### Mixed gravitational Hamiltonian terms

H_body depends on q but not on its momentum pi. In ADM,
delta H_grav[N]/delta pi^{ab} is N times a local tensor. Meanwhile

    delta H_body[L]/delta q_ab(x)
       = -L(X) v^a v^b/(2E) delta(x-X).

The mixed contribution is proportional to N(X)L(X), antisymmetrized in N,L;
it cancels. Combining this with the pure-gravity identity gives

    {H[N],H[L]} = D[q^{-1}(N dL - L dN)].                 (1)

Spatial derivatives in the gravitational potential do not spoil this argument:
that potential contains no pi and H_body contains no pi either.

### Shift versus lapse: the term that cannot be omitted

The particle-coordinate bracket alone is

    {D_body[xi],H_body[N]}
      = E xi^a partial_a N + N xi^a partial_a E
        - (N/E) p_b v^a partial_a xi^b.

This is **not** H_body[xi^a partial_a N]. The metric itself also transforms:

    {D_grav[xi],H_body[N]}
      = N v^a v^b (Lie_xi q)_ab/(2E).

Using partial_c q^{ab}=-q^{ai}(partial_c q_ij)q^{jb}, the metric-gradient and
shift-gradient terms cancel the two unwanted particle terms exactly. Thus

    {D[xi],H[N]} = H[Lie_xi N].                          (2)

Finally the particle canonical bracket gives D_body[[xi,eta]], the gravitational
one gives D_grav[[xi,eta]], and the cross terms vanish:

    {D[xi],D[eta]} = D[[xi,eta]].                        (3)

The internal number constraint commutes with these constraints. Equations
(1)–(3) show that the finite program, when included through its positive mass,
does not add a classical obstruction to refoliation in this canonical model.
They are not a proof of refoliation-independent quantum record probabilities.

The verifier evaluates 240 independent three-dimensional metric/lapse/shift
jets, checking 720 matter bracket identities and the mixed cancellation.
Omitting the metric's shift action gives a residual as large as 1.151 in these
cases; including it reduces the maximum residual below 8e-15. These numerical
checks illustrate the analytic identities, not a lattice continuum-limit proof.

## 5. What the autonomous dressing transfers to quantum constraints

The earlier finite autonomous programs have

    A = Q A_0 Q^dagger,
    A_0 = H_clock + H_f,

where Q is a finite internal controlled unitary built from gate prefixes. It
depends on the internal clock site, not on the body's spatial position, spatial
metric, lapse or shift. Let U=I_external tensor Q. Then U commutes with the
spatial metric and the bare spatial diffeomorphism generators. Formally and,
whenever defined self-adjointly, by spectral calculus,

    sqrt(q^{ab}p_a p_b + (m_0+A)^2)
      = U sqrt(q^{ab}p_a p_b + (m_0+A_0)^2) U^dagger.

For an available baseline constrained quantum model define every dressed
constraint and its domain by

    C_alpha = U C_alpha^0 U^dagger,
    Dom(C_alpha) = U Dom(C_alpha^0).

Common invariant cores and commutators transport under the same U. Since the
metric structure operators commute with U, a baseline hypersurface-deformation
identity, with its specified ordering, transports unchanged. Any baseline
anomaly transports too: **dressing neither creates nor cures it**. The same
qualification applies to the physical inner product and observable domains.
If a baseline rigging form eta_0 exists, its transported form is
eta(f,g)=eta_0(U^dagger f,U^dagger g); the bare kinematic norm is not
a substitute for that physical construction.

This is a conditional domain-preservation theorem. It does not assume that
formal quantum ADM expressions already possess the necessary self-adjoint
realizations, common cores or positive physical inner product. The missing
baseline is quantum gravity coupled to the free carried mass sectors; it is
not supplied by the finite-dimensional internal program.

Q specifies the interacting autonomous Hamiltonian; it is not an uncharged
instantaneous pulse that must be applied at some external start time. The
initial clock state and bare record observables are kept fixed, so calling
this a gravitational gauge transformation would erase the physical comparison.

## 6. Worked finite program and quantum-motion limitation

For a small explicit example, take three clock sites and two degenerate record
bits R,B. Use clock hopping gamma=.05, internal source offset E_c=2, and

    A_0 = E_c I + gamma (|0><1| + |1><2| + h.c.) tensor I_RB,
    Q = diag(I_RB, I_RB, CNOT_{R->B}),
    A = Q A_0 Q^dagger.

This is an autonomous copying stage, not a replacement for the earlier
fixed-gap measurement/reference construction. Its mass-coupling argument
applies to that larger finite A as well, but the explicit 12-dimensional test
only copies a degenerate bit. It does not supply microscopic apparatus matter.

In the body's rest frame, at proper duration

    s_* = pi/(sqrt(2) gamma) = 44.4288293816,

|0>_clock |+>_R |0>_B evolves, up to a global phase, to
-|2>_clock (|00>+|11>)/sqrt(2). The quantum record is retained, not collapsed.
The complete program returns to its initial state at 2s_* up to global phase:
this finite closed apparatus is not a permanent latch. The internal mean energy
is E_c before and after the copy. With m_0=20 the full mass spectrum lies in
[21.92928932,22.07071068].

### A moving quantum apparatus need not have one proper-time rate

On a fixed flat background, in the canonical positive-frequency representation
L2(R^3,d^3p) tensor C^D, choose the one-body Hamiltonian

    H_flat(p) = sqrt(p^2 + (m_0+A)^2).

This benchmark uses an inertial coordinate duration, not an external timing
prior for the full constrained gravitational theory. Put delta=A-E_c I,
a=||delta||, m=m_0+E_c, and assume m>a, as in the worked example.
Here p denotes momentum magnitude, and a finite band is a radial momentum
shell; p_0 is its nominal magnitude. Define

    E_0(p)=sqrt(p^2+m^2),  alpha(p)=m/E_0(p),  s_0=t alpha(p_0).

For a normalizable momentum packet supported in a declared band B, compare the
actual **joint motion/internal** unitary with

    exp[-it E_0(p)] tensor exp[-i s_0 delta].

Taylor's theorem and the positive mass lower bound m-a give the uniform
operator-error bound, hence also a half-diamond bound on the supported space,

    epsilon_move <= min(1, |t| [a sup_B |alpha(p)-alpha(p_0)|
                   + (a^2/2) sup_B p^2/(p^2+(m-a)^2)^(3/2)]).             (4)

Here the cap at 1 is for channel/trace distance; the uncapped expression bounds
the raw unitary operator difference. The center-of-mass comparison phase is
retained. This is not a bound obtained by tracing away motion or replacing its
momentum by a mean without error control. It also holds for states entangled
with an external reference.

Even at a sharp nonzero momentum, the square-root mass dependence is nonlinear
in A; exactly replacing the program by A at one classical proper time is in
general incorrect. At p=0 with positive mass it is exact. A sharp-momentum row
is a spectral benchmark, not a normalizable localized packet. Finite momentum
bands permit normalizable spatially spread packets, not compact position
support; no spatial-resolution claim is inferred from these rows.

For s_0=s_* and p_0=11 the explicit 12-dimensional example gives:

| Momentum half-width | Bound (4) | Maximum sampled full-state trace distance |
|---:|---:|---:|
| 0 (spectral benchmark) | .001017573 | .000504880 |
| .01 | .001590167 | .000648252 |
| .1 | .006752755 | .004080261 |

If an internal complete instrument at s_0 has error epsilon_internal, contraction
and the triangle inequality give the fixed-background bound
min(1, epsilon_move + epsilon_internal), for initializations covered by both
premises. This composes the motion estimate with the earlier finite-source
record bounds; it does not transfer those bounds to unsolved quantum geometry.

The band bounds are analytic; the sampled errors do not certify the interval.
The full-state distances are before tracing the internal clock or record. The
nominal coordinate duration is 49.672941329. Rest copying, finite recurrence,
energy conservation and the exact spectral evolution are also checked.
Increasing the body's mass can suppress motion-induced errors on a fixed
background, but that mass gravitates. It is not a free precision limit in the
self-gravitating theory.

## 7. Reproducibility and the next obstruction

Run:

    python verification/localized_constraint_clock.py
    python -m verification.localized_constraint_clock

Output: [localized_constraint_clock.json](verification/localized_constraint_clock.json).
The verifier is pure Python and deterministic. It checks local bracket jets,
finite dressed mass dynamics and a flat-background spectral calculation;
it does not evolve a numerical spacetime or solve Einstein's equations.

**Supplied:** a covariant localized finite-program coupling, explicit classical
spatial constraint closure including mixed terms, a conditional quantum dressing
preservation theorem, and a joint quantum-motion/program error bound.

**Not supplied in the point-body model:** a finite-size stress-energy completion,
its self-gravitating constrained solutions, an anomaly-free quantum baseline,
physical relational local record probabilities in that baseline, or a derivation
of prepared sources or phenomenal constitution. These are omissions, not proofs
that the larger account is false.

[Smooth dynamical clock matter](SMOOTH_FIELD_CLOCK.md) now provides the
scalar-multiplet continuation: a covariant action and classical spatial closure,
a contraction proof of smooth self-gravitating initial data, normalizable
Gaussian flat-limit program bounds, and a region-preserving local field-algebra
isomorphism. It is a smooth finite-energy field model, not a stable bound
apparatus. The next direct target is relational record control through actual
coupled gravitational evolution; neither the point-body result nor its smooth
completion supplies a quantum Einstein constraint baseline.
