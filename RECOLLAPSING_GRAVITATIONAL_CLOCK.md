# A recollapsing Einstein–scalar clock and completed-event representations

## 1. The gravitational step actually taken

This is a genuine gravitational Hamiltonian constraint derived from the flat FLRW Einstein–scalar action, not an engineered constraint obtained by rescaling a clock derivative. A negative cosmological constant gives an exactly solvable recollapsing model. A massless scalar is monotonic, while volume grows, turns and repeats its readings. Quantization gives a self-adjoint exponential-wall problem, a common physical Hilbert space, and an exact unitary reflection map between the two oriented asymptotic geometric descriptions.

Completed event instruments can be transported through these representations **including their failure branches and post-states**. A wrong-event witness shows why retaining the same numerical event operator in a new frame changes the question. Asymptotic timestamp POVMs distinguish transporting the same event from observing the later recrossing of the same volume.

**Scope:** homogeneous minisuperspace removes spatial diffeomorphism/refoliation degrees of freedom. This is not the hypersurface-deformation algebra, an inhomogeneous gravitational solution or a derivation of the observed cosmology. Negative Lambda is chosen as an analytically controlled recollapse test; it is not asserted to be the measured cosmological constant. The gravitationally backreacting detector Hamiltonian is not supplied. Earlier nongravitational detector accuracy numbers are **not** transplanted here.

Code: [recollapsing_gravitational_clock.py](verification/recollapsing_gravitational_clock.py). Results: [recollapsing_gravitational_clock.json](verification/recollapsing_gravitational_clock.json).

## 2. Derive the constraint from Einstein–scalar dynamics

Set 8piG=hbar=1 and fix a unit fiducial coordinate cell. For

    ds^2=-N(t)^2 dt^2+a(t)^2 d(vec x)^2,

with a homogeneous massless scalar phi, the reduced Lagrangian is

    L=-3a adot^2/N + a^3 phidot^2/(2N) -N Lambda a^3.

Thus

    p_a=-6a adot/N,    p_phi=a^3 phidot/N,
    H=N[-p_a^2/(12a)+p_phi^2/(2a^3)+Lambda a^3].

On a>0 introduce canonical variables

    x=3 ln a,           p_x=a p_a/3,
    T=sqrt(3/2) phi,    p_T=sqrt(2/3) p_phi.

Multiplying the ADM constraint by the positive factor 4a^3/3 gives

    C=p_T^2-p_x^2-mu^2 exp(2x)=0,
    mu^2=4|Lambda|/3,    Lambda<0.

This multiplication is a classical lapse reparametrization on a>0. Its quantum equivalence to every possible scale-factor ordering is **not assumed**. We declare the constant-coefficient log-volume ordering below. The fiducial-cell convention and canonical units are fixed throughout.

## 3. Actual turning geometry, not a failing scalar clock

Choose p_T=-k<0, k>0, and increasing relational T. The reduced Hamiltonian is

    H_T=sqrt(p_x^2+mu^2 exp(2x))=k.

Hamilton's equations give

    x(T)=ln(k/mu)-ln cosh(T-T_*),
    p_x(T)=-k tanh(T-T_*).

The volume a^3=exp(x) reaches its maximum k/mu at T=T_*. At any x=b<ln(k/mu), there are two readings

    T_-(b)=T_*-arcosh[k/(mu exp(b))],
    T_+(b)=T_*+arcosh[k/(mu exp(b))].

The sign of p_x distinguishes them. In these conventions the p_x>0 branch expands with increasing T and p_x<0 contracts. These labels refer to the chosen scalar-time orientation; reversing the lapse/time orientation reverses the labels, not the physics.

T is global in this nonzero-p_T sector; x alone is not. For sigma=sign(p_x),

    dT/dx=sigma/sqrt[1-mu^2 exp(2x)/k^2],

which diverges at the volume turning point. Losing orientation merges two distinct events. Neither that failure nor a bad volume gauge makes the scalar-time dynamics singular. The big-bang/big-crunch small-volume limits are **not resolved** by this recollapse construction.

## 4. Quantization and the common physical norm

Use the declared constraint ordering on L2(R_T x R_x):

    C_hat=p_T^2-Theta,
    Theta=-partial_x^2+mu^2 exp(2x).

Theta is the positive, essentially self-adjoint one-dimensional exponential-wall Schrödinger operator. Both ends are limit point; no arbitrary reflecting boundary at finite volume is inserted. Its spectrum is absolutely continuous k^2, k>0. The full C_hat is the self-adjoint joint-spectral realization of p_T^2-Theta on its maximal domain, not automatically the naive intersection of the individual squared-operator domains.

Choose the positive-frequency convention

    i partial_T psi=sqrt(Theta) psi,

corresponding to p_T=-k. This is a declared frequency sector, not the removal of an unwanted second-order mode without accounting.

### Kontorovich–Lebedev spectral transform

With z=mu exp(x), define

    e_k(x)=sqrt(2k sinh(pi k))/pi * K_(ik)(z).

The standard KL identity is

    integral_0^infinity dz/z K_(ik)(z)K_(ik')(z)
        =pi^2/[2k sinh(pi k)] delta(k-k').

Thus the transform between a(k) in L2(R_+,dk) and its x representation is unitary, with the usual generalized-eigenfunction interpretation. It diagonalizes Theta as multiplication by k^2. In the reduced scalar frame,

    psi_T(x)=integral_0^infinity dk a(k)e^(-ikT)e_k(x),
    ||psi_T||^2=integral dk |a(k)|^2.

This identity is analytic KL spectral theory, not a conclusion from a finite matrix quadrature.

### Retain the rigging Jacobian

Group averaging the original squared constraint gives, on the p_T=-k branch,

    delta(p_T^2-k^2) -> delta(p_T+k)/(2k).

For an on-shell test amplitude b(k), the physical norm is

    ||b||_phys^2=integral dk |b(k)|^2/(2k).

Set a(k)=b(k)/sqrt(2k). The group-averaged distributional history has spectral amplitude

    Psi(T,x)=integral dk [a(k)/sqrt(2k)]e^(-ikT)e_k(x).

Its positive Klein–Gordon norm is integral |a|^2. The unitary reduced state is

    psi_T=(2sqrt(Theta))^(1/2) Psi(T, .),

not simply the raw history evaluated at T with ordinary L2 norm. This distinction matters for comparing records across clock representations. Test states may be restricted away from k=0; a normalizable k=0 clock mode is not created or assumed, and inverse factors near threshold are not uniformly bounded.

## 5. Exact quantum relation between oriented geometric asymptotes

At small volume,

    K_(ik)(z) ~ (1/2)Gamma(-ik)(z/2)^(ik)
                  +(1/2)Gamma(ik)(z/2)^(-ik).

Using |Gamma(ik)|^2=pi/[k sinh(pi k)], each normalized traveling component of e_k has magnitude 1/sqrt(2pi). Write their phases as

    u_in(k)=sqrt(2pi) [sqrt(2k sinh(pi k))/(2pi)]
                       Gamma(-ik)(mu/2)^(ik),
    u_out(k)=sqrt(2pi) [sqrt(2k sinh(pi k))/(2pi)]
                       Gamma(ik)(mu/2)^(-ik).

Both have modulus one. The incoming/outgoing spectral descriptions are therefore **unitary** maps from the same physical a(k):

    a_in=u_in a,    a_out=u_out a,
    a_out=S(k)a_in,
    S(k)=Gamma(ik)/Gamma(-ik) * (mu/2)^(-2ik),
    |S(k)|=1.

There is one reflecting physical channel, not two independently selectable universes and not two alternatives assigned arbitrary probabilities 1/2. Incoming and outgoing descriptions concern opposite asymptotic ends of the same recollapsing solution.

These are exact **oriented asymptotic geometric representations**. They are not a proof that evaluating x at every finite volume defines a globally unitary clock reduction. In particular, the real standing eigenmode has zero net x flux, although both oriented components are nonzero. Treating orientation-free net flux as a probability clock loses the recollapse information.

### An explicit small-volume mode bound

The series factors multiplying the two traveling terms satisfy

    F_(+/-ik)(z)=sum_[j>=0] (z^2/4)^j/[j! (1+/-ik)_j],
    |F_(+/-ik)(z)-1|<=exp(z^2/4)-1.

This follows from |(1+/-ik)_j|>=j!. Hence the normalized eigenmode's difference from its two plane asymptotes is at most

    2/sqrt(2pi) [exp(z^2/4)-1].

It controls the mode asymptotic used here. It is **not by itself an instrument-accuracy bound for a detector at finite volume**, nor does it repair a volume-clock reduction at its turning point.

## 6. Matched completed instruments, not sharp-coordinate substitutions

Take one physical Hilbert space H_phys=L2(R_+,dk) with the norm above. Let a specified completed root instrument have Kraus family K_(r,alpha), including a not-completed/failure label, such that

    sum_[r,alpha] K_(r,alpha)^dagger K_(r,alpha)=I.

This encompasses complete finite-record instruments **if their physical coupling to this cosmology has been supplied**. The theorem below does not supply that missing gravitational coupling merely by naming an instrument.

Let V_c be a unitary physical representation: the scalar frame V_T=KL^(-1)exp(-ikT), or either oriented asymptotic phase frame. Define

    W_(d<-c)=V_d V_c^dagger,
    K_(r,alpha)^c=V_c K_(r,alpha) V_c^dagger.

Then the complete instrument transforms by unitary input/output transport. All branch probabilities, retained-reference states and normalized conditional states (when defined) agree for matched root events. Completeness includes failure; it is not restored by discarding unsuccessful branches.

For a sequence of anchored events in different frames,

    K_n^(c_n) W_(c_n<-c_(n-1)) ... K_1^(c_1) W_(c_1<-c_0)
       =V_(c_n) K_n ... K_1 V_(c_0)^dagger.

This preserves multi-event probabilities, coarse graining and feedback when the same root operations are used. It does not independently generate the physical order or detector stress energy.

If a completed implementation and its ideal instrument have half-diamond error delta on the same physical sector, **unitary frame transport preserves that error exactly**. It introduces no new clock-choice error. This conditional statement does not license using 0.00023 from the nongravitational completion model as an Einstein–scalar apparatus bound: its packet, Hamiltonian and backreaction have not been derived here.

Keeping the old numerical event matrix after changing V generally asks a different question. The finite control in the verifier uses a complete two-stage instrument with noncommuting projectors and a failure branch that halts the protocol; correct transport preserves every tested branch while the untransported procedure changes probabilities substantially. Its Fourier matrix is a finite algebra control, **not a discretized KL transform**.

## 7. Incoming and outgoing timestamps are different events

One can define normalized covariant **asymptotic timestamp POVMs** in the incoming representation. For a reference volume plane b, write

    A_in(tau)=1/sqrt(2pi) integral_0^infinity dk
                 a_in(k) exp(ikb-ik tau),
    A_out(tau)=1/sqrt(2pi) integral_0^infinity dk
                 S(k)a_in(k) exp(-ikb-ik tau).

Zero-extension to the full Fourier line and Parseval give integral |A|^2 d tau=1 for each POVM. A finite accepted timestamp window has its complementary outside-window outcome. These are asymptotic reference-plane timestamps, not a Hamiltonian-derived detector at arbitrary finite b. Compression of the Fourier PVM to k>0 gives a POVM, not a forbidden self-adjoint time operator conjugate to a semibounded energy.

The incoming event represented in the outgoing frame is S E_in(B) S^dagger. It is **not** E_out(B), which asks about the later crossing of that plane. Equal coordinate labels b do not make those two events identical.

For smooth packets supported away from k=0, their separately measured mean timestamp difference is

    <tau_out>-<tau_in>
       =integral dk |a_in(k)|^2 [d arg S(k)/dk-2b],
    d arg S/dk=2 Re digamma(ik)-2ln(mu/2).

At large k this approaches

    2ln(2k/mu)-2b,

the classical difference of the two asymptotic intercepts. The exact finite-volume classical time difference is `2 arcosh[k/(mu exp(b))]`; its logarithmic asymptote is the expression above. They must not be conflated outside the small-potential regime.

This mean difference refers to **separately prepared timestamp measurements**. It is not a joint undisturbed duration distribution. Recording both crossings in one run requires a sequential instrument and its disturbance, for which the completed-branch transport formula applies once the actual physical instruments are specified.

## 8. Verification, gains and the remaining gravitational problem

The standard-library verifier checks:

- 45 classical constraint/trajectory cases, including the recollapse and paired volume events.
- Gamma modulus/recurrence identities and the unit-modulus reflection phase.
- 16 modified-Bessel differential-equation checks using the real integral representation, and four bounded small-volume asymptotes.
- The high-energy relation between quantum reflection-phase derivatives and classical intercepts.
- Completed multi-event branch transport, a wrong-event counterexample, a retained failure branch and the rigging Jacobian.

The Bessel integrals and phase derivatives are floating numerical witnesses, not interval certificates. Essential self-adjointness, KL unitarity, domains and representation identities are analytic ingredients stated above; finite tests do not prove their continuum versions.

The substantive advance is a common constrained Hilbert space and exact oriented quantum-clock relation in an **Einstein–scalar recollapsing geometry**, with completed-record consistency conditions rather than naive coordinate substitution. Scalar time survives where volume fails; quantum reflection retains the missing branch information.

Still missing are a gravity-coupled completion detector derived from an action, finite-volume operational orientation/arrival instruments, robust storage/reset and an inhomogeneous constraint system with gravitational hypersurface-deformation consistency. The last item cannot be settled by a model with only one homogeneous Hamiltonian constraint. No singularity resolution, preferred universal clock or physical–phenomenal constitution is established.

The next direct gravitational task is to add a specified detector/matter degree of freedom to the reduced Einstein action and derive its constraint and clock reductions together, rather than attach a nongravitational instrument without its gravitational energy contribution.

**Backreacting clock continuation:** [The gravitating proper-time oscillator](GRAVITATING_PROPER_TIME_CLOCK.md) now supplies a reduced matter action, detector-dependent geometry, exact phase/readout instrument and dressed gravitational record effects. It is a smeared comoving phase probe, not the old completion apparatus transplanted into gravity; finite-time hardware and inhomogeneous constraints remain unsupplied.
