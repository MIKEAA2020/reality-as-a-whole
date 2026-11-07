# Two finite clocks and a validated internal reference event

## 1. Result: the readout is an internal interaction, not a sampled epoch

The [finite-carrier gravitational construction](FINITE_REFERENCE_GRAVITY.md) removed ideal dust but described local record extraction at a phase-indexed epoch. Here a **second normalizable quadratic carrier physically initiates a readout operation**. Its gates validate the recorder's completion, copy its memory when valid, and mark completion of the reader's own schedule.

Both carriers, the original recorder, the new reader and every gate energy enter the same lapse constraint. There is no externally switched interaction, no prescribed probability density over interrogation times, and no uniform time prior. The actual readout is a finite-duration quantum interaction, not an average of sharp-time projective measurements.

A complete conserved outgoing instrument records success, invalidity, noncompletion and escape failure. A uniform error estimate connects it to the finite register operation. Changing the relative timing of the two carriers changes the answer: an early reader is demonstrably invalid, even though its own completion flag fires. Changing the origin of the common relational phase does not change the conserved record probabilities.

**Bounded claim:** homogeneous constrained mechanics with engineered internal degrees of freedom, a declared gravitational domain and spectrally encoded preparations. The construction supplies an internal record-transfer mechanism, not a human observer, a reset engine, the Hamiltonian preparation of the encoding, full refoliation, or a physical–phenomenal identity law.

## 2. Matter action and positive source

Use the same flat FLRW Einstein–scalar action, r=a^(3/2), negative Lambda, radial ordering and subcritical scalar sector as in the preceding report. Add two internal canonical pairs X,P and Q,P_Q. X transports the recorder; Q transports the reader. They are smeared comoving **internal apparatus coordinates**, not positions of localized cosmological particles.

The matter part is

    L_matter = P Xdot + P_Q Qdot + i z^dagger zdot
               - N [P^2/(2m)+P_Q^2/(2M)+z^dagger h(X,Q)z]
               - lambda(z^dagger z-1).

The one-boson register now has eight qubits, dimension 256:

    S,D,M_mem,E,F,R,V,G.

M_mem is the old memory (the carrier mass M is unrelated). R is the readout memory, V the validity bit, and G the reader-completion flag. Initially D,M_mem,F,R,V,G are |0>, E is I/2, and S is arbitrary, including reference entanglement. An E purification may be included as an untouched zero-energy ancilla. All register free Hamiltonians other than omega X_S are zero by model choice. Exact degeneracy and the initialized bits are apparatus assumptions, not a derivation of robust material memory.

Write

    h=E_b I + omega X_S + v K_X(X)+u K_Q(Q),
    K_X=sum_(j=1)^4 kappa_j(X) B_j,
    K_Q=sum_(j=1)^3 chi_j(Q) C_j.

The old B_j perform S-to-D, D-to-M_mem, M_mem-to-E, and F flip. The reader projectors are

    C_1=P_1,F (I-X_V)/2,
    C_2=P_1,V P_1,M_mem (I-X_R)/2,
    C_3=(I-X_G)/2.

All B_j,C_j are positive projectors. Each spatial profile has width ell_X or ell_Q, nonoverlapping gaps in its own coordinate, sine-squared shape and area pi. For example,

    chi_j(q)=(2pi/ell_Q) sin^2[pi(q-q_j)/ell_Q]

inside its region and zero outside. The reader performs F-to-V, a V-and-M_mem controlled flip of R, then a flip of G. **V is a finite-window sample of F, not a claim of an instantaneous truth value at a sharp arrival time.** G certifies only the reader schedule.

The full constraint is

    C=H_2-A,
    H_2=P^2/(2m)+P_Q^2/(2M)+h(X,Q),
    A=(3/16)p_r^2+|Lambda|r^2-p_phi^2/(2r^2).

For E_b>=omega,

    H_2 >= E_b-omega >=0.

Both sets of spatial potentials can be nonzero simultaneously as operators; an upper bound must include **both** peaks:

    h <= E_b+omega+v(2pi/ell_X)+u(2pi/ell_Q).

H_2 is self-adjoint on H^2(R^2) tensor C^256. The bounded matrix potentials occupy strips in (X,Q), not one compact two-dimensional region. Total H_2 is conserved. Kinetic energy of either carrier and internal energy can exchange; no pulse work is supplied by an omitted clock field. The gravitational constraint identifies this entire source with A.

## 3. Physical Hilbert space and two-carrier encoding

Keep 0<p_lo<=p_phi<=p_hi<sqrt(3/32) and a fixed radial level n. The Friedrichs spectrum and Jacobian are

    epsilon_n(p)=omega_g[2n+1+nu(p)],
    nu(p)=sqrt(1/4-8p^2/3),
    omega_g=sqrt(3|Lambda|)/2,
    J(p)=8 omega_g p/(3nu)>0.

For I=[epsilon_n(p_hi),epsilon_n(p_lo)], group averaging C=H_2-A gives

    ||eta f||_phys^2
       = integral_I d mu_2(E) ||f(p(E),E)||^2/J(p(E)).

Thus the physical root Hilbert space is Pi H_2_space, Pi=1_I(H_2), after rescaling by sqrt(J). The formula includes spectral multiplicities and any atomic contributions; no outgoing completeness assumption deletes other sectors.

Start with a product comparison encoding V_0. Each carrier is a boosted normalized compact cos-squared packet, centered at -d_X and -d_Q, with half-widths a,b, speeds v,u and masses m,M. Define

    f_1X=pi/(sqrt(3)a), f_2X=pi^2/(sqrt(3)a^2),
    f_1Q=pi/(sqrt(3)b), f_2Q=pi^2/(sqrt(3)b^2).

Both initial packets lie left of their gates. With

    E_c=E_b+mv^2/2+Mu^2/2,
    sigma_2=v f_1X+f_2X/(2m)+u f_1Q+f_2Q/(2M)+omega,

one has ||(H_2-E_c)V_0||<=sigma_2. For I=[E_c-W,E_c+W], the spectral theorem gives leakage norm at most epsilon_2=sigma_2/W. If epsilon_2<1,

    V_I=Pi V_0 (V_0^dagger Pi V_0)^(-1/2)

is an isometry into the physical root space, with

    ||V_I-V_0||<=2epsilon_2=:alpha_2.

This is the two-carrier version of the previously proved polar encoding, not reuse of the previous one-carrier preparation. The initial clocks and register become correlated; V_I is not a postselected product packet. The estimate is uniform for all S/reference inputs.

The physical states are normalizable and have bounded total source energy. Their probability outside the comparison localization rectangles is at most alpha_2^2, but sharp spectral filtering need not preserve finite RMS position variance. A preparation Hamiltonian for V_I remains unsupplied. Energy-centering error delta_cal is covered by replacing sigma_2 with sigma_2+|delta_cal|; the tabulated calibration formulas specify exact mathematical targets, not independently certified physical precision.

The previous radial ordering, positive scalar band and endpoint extension remain explicit inputs. No singularity-resolution theorem or equivalence with other scalar-clock quantizations is inferred.

## 4. An internally timed, finite reference window

Let

    L_X=4ell_X+3d_Xgap,
    L_Q=3ell_Q+2d_Qgap.

For the transport comparison, the recorder's earliest entry and completed epoch are

    t_X^-=(d_X-a)/v,
    T_X=(L_X+d_X+2a)/v.

The reader has

    t_Q^-=(d_Q-b)/u,
    T_Q=(L_Q+d_Q+2b)/u.

Choose t_Q^->T_X, with a finite separation margin. Every component of the **comparison** X packet then completes the recorder before any component of the Q packet enters its reader region. Each Q gate is traversed over a window of width (ell_Q+2b)/u; the complete reader active window used in the bound is (L_Q+3b)/u. These widths describe the calibrated comparison, not exact support of the spectrally encoded quantum arrival distribution.

At completion, the reference gates give

    F=1 -> V=1,
    R=M_mem,
    G=1.

After E is traced, the reader's record is classical in the computational basis. If rho_pre is the S/reference input freely evolved to t_X^-, the ideal recorded instrument is

    rho_pre -> sum_d W_S P_d rho_pre P_d W_S^dagger
        tensor |d,d,1,d,1,1><d,d,1,d,1,1|_(D,M_mem,F,R,V,G),

where W_S includes the free S evolution restored after T_X. The comparison suppresses omega X_S only during [t_X^-,T_X]; the actual H_2 never switches. All later reader gates commute with X_S, so no additional omission of S dynamics is needed.

This reference construction is used to bound the actual two-carrier unitary, not to assign it a classical random event time. In particular, replacing the reader by integral dt w(t) times a sharp-time measurement is **not** part of the argument.

## 5. Joint finite-mass error estimate

Set, for i=X,Q,

    k_i=2pi/ell_i, k'_i=2pi^2/ell_i^2,
    C_i=f_2i+2k_i f_1i+k'_i+k_i^2,
    t_i^active=T_i-t_i^-.

Choose a common comparison epoch T after both devices, with clearances

    D_X=vT-d_X-L_X>2a,
    D_Q=uT-d_Q-L_Q>2b.

During X registration the Q potentials vanish on the reference support. During Q readout the X packet has completed its gates; their completed product is independent of initial X position. Thus the reference second-derivative bound in each coordinate is C_i during its own active interval and f_2i otherwise. There are no mixed second derivatives in the physical kinetic Hamiltonian. Duhamel's inequality gives

    delta_tr = [T f_2X+t_X^active(C_X-f_2X)]/(2m)
             + [T f_2Q+t_Q^active(C_Q-f_2Q)]/(2M)
             + omega t_X^active.

Adding alpha_2 covers the spectrally encoded physical preparation. Both carriers' spreading, recoil, gate overlap tails and reflection amplitudes are included in this estimate; their neglect is not an additional assumption about the physical evolution.

After T compare with the actual quadratic outgoing generator

    H_out=P^2/(2m)+P_Q^2/(2M)+E_b+omega X_S.

For each coordinate use the Fourier/Cook constants from section 7 of the [one-carrier derivation](FINITE_REFERENCE_GRAVITY.md), evaluated with that carrier's own a_i,m_i,v_i,ell_i,D_i. Explicitly let A_i be its two-integration-by-parts tail constant and

    eta_i=2 f_1i/(m_i v_i),
    E_i=2 v_i k_i A_i/[sqrt(3)(v_i/4)sqrt(D_i)].

Here E_i denotes an escape **norm bound**, not energy. The notation is separate from E_b and the spectral variable E. Let eta=eta_X+eta_Q and E_escape=E_X+E_Q. The potential strips require summing the two tail bounds; applying a compact-two-dimensional-potential estimate would be incorrect.

The product momentum cutoff removes norm at most eta. At T both reference carriers factorize from the completed internal gate product, so the free tail estimates apply in each coordinate uniformly over internal/reference states. For every s>=0,

    ||exp[-iH_2(T+s)]V_I
       -exp[-iH_out s]V_ref(T)||
       <=alpha_2+delta_tr+2eta+E_escape=:Delta_2.

This bounds the complete extracted register channel in half-diamond distance, capped at one, uniformly for entangled inputs. If success means V=1,G=1, then

    Pr(V=0 or G=0)<=min(1,Delta_2^2),
    Pr(R!=M_mem)<=min(1,Delta_2^2).

Their union also has the same squared-vector bound, since it annihilates the ideal output. These are single late interrogations of unmonitored evolution, not continuous first-click histories or a repeated-read noise guarantee.

## 6. Complete source-compatible instrument without an interrogation-time prior

On the free sector with **both** momenta positive, define the joint outgoing wave operator

    Omega_++=strong-limit_(s->infinity) exp(iH_2 s)exp(-iH_out s).

The two integrable strip-tail bounds construct it on a dense set of smooth right-moving product packets and finite sums thereof. Isometric extension supplies the outgoing sector and intertwines the Hamiltonians; asymptotic completeness is not assumed.

Let P_rvg be all eight free projectors for bits R,V,G. They commute with H_out and the positive-momentum sector. Define

    L_rvg=Omega_++ P_rvg Omega_++^dagger,
    L_perp=I-Omega_++ Omega_++^dagger.

They are orthogonal projections whose sum is I. They commute strongly with H_2 and therefore, acting trivially on gravity, with C=H_2-A. They preserve Pi and define on the physical root space

    J_y(rho)=L_y rho L_y,  y in {eight bit strings,perp}.

The sum is trace preserving. Successful readout has y=(r,1,1), retaining both memory values r. All other bit strings, including reader noncompletion, and the non-joint-outgoing complement are retained as separate outcomes or may be coarse-grained into failure. There is no state-dependent normalization by success.

Comparing to the normalized product-cutoff outgoing packet yields

    Delta_out=alpha_2+delta_tr+4eta+E_escape/(1-eta).

This bounds the outgoing record channel relative to the ideal completed reader. The probability outside the joint right-outgoing sector is at most

    [alpha_2+delta_tr+2eta+E_escape/(1-eta)]^2.

For conditional S-output comparisons, use Omega_++^dagger on success and an orthogonal failure output; tracing bare S inside an interaction region is a different instrument.

These exact conserved effects connect to a finite internally generated event through the explicit error estimate. They do not assert that bare finite-time bits commute exactly with the interacting Hamiltonian. Their eventual external extraction/reset is still not a microscopic apparatus derivation.

### Phase-origin invariance, not indifference to the reference event

For every physical density operator and every conserved outcome,

    Tr[L_y exp(-iH_2 theta)rho exp(iH_2 theta)] = Tr[L_y rho].

Consequently the outgoing bit probabilities require no privileged sharp phase epoch and no integral over a uniform prior. The gravitational–scalar phase representation remains useful in the proof, but no gate or definition of the final probabilities is conditioned on a sampled value of it. Conditional S states covary with free evolution; the invariance claim here concerns the conserved record probabilities.

Advancing **only Q relative to X** is different. It changes the physical preparation, not merely the common phase origin. The next section supplies a worked distinction.

## 7. Early reference events are detected, not relabelled as successes

Suppose the reader completes before the recorder starts: T_Q<t_X^-. Then in the transport comparison,

    F=0 when the reader operates,
    V=0, R=0, G=1 after the reader,
    F=1 only after the later recorder completes.

Thus G=1 alone would falsely certify a usable record. The added V bit correctly reports invalidity. For an ideal recorder bit 1 the late output has R=1,V=1,G=1; the early output has R=0,V=0,G=1 even though M_mem later becomes 1.

This is not merely an ideal gate counterexample. The same two-coordinate derivative proof applies with the nonoverlapping gate order reversed: the reader commutes with the S Hamiltonian, and its completed product is independent of initial Q position before recorder dynamics begin. Recompute the common clearance and Cook constants for the early preparation. If its bound is Delta_early, then at every later single interrogation

    Pr(V=0,G=1)>=1-Delta_early^2,
    Pr(V=1,G=1)<=Delta_early^2.

The physical spectral encoding changes with the early preparation and is bounded anew. No late-schedule error number is simply reused. Invalidity is a real complete-instrument outcome, not an unobserved absence of experience or an assertion of failed dynamics.

## 8. Fixed gravity, six finite resource witnesses

Choose both masses q^8, both speeds 100, a=b=10/q^2, ell_X=ell_Q=20/q and both gaps 10/q, for q=100,1000,10000. Let d_X=1. Use the same fixed gravitational model as before:

    omega_g=10^28, Lambda=-4 omega_g^2/3,
    p_lo=0.05, p_hi=0.25, omega=0.1.

The spectral center now includes **both** kinetic means. With K_tot=mv^2/2+Mu^2/2, choose

    n=max(0,ceil([(K_tot+omega)/omega_g-1-nu_mid]/2)),
    E_c=omega_g(2n+1+nu_mid), E_b=E_c-K_tot,
    W=omega_g[nu(p_lo)-nu(p_hi)]/2.

The radial levels are 0,0,50000000. The rest source E_b is retained. These enormous formal resources and negative Lambda are not realistic cosmological fits or universal optimality bounds.

For a late reader choose its earliest reference entry 0.01 after the recorder's comparison clearance at D_X=1. Choose the final epoch so the reader has D_Q=1; the recorder is then farther away.

| q | Reader active window | Common clearance T | Complete late record error Delta_2 | Invalid/incomplete probability bound |
|---:|---:|---:|---:|---:|
| 100 | 0.008030 | 0.059010 | 0.020458 | 4.186e-4 |
| 1000 | 0.0008003 | 0.0419001 | 0.00031085 | 9.663e-8 |
| 10000 | 0.000080003 | 0.040190001 | 0.000013018 | 1.695e-10 |

The last row is slightly less accurate than the one-carrier construction: adding a finite reader has a calculated cost rather than being treated as free. Spectral encoding costs are approximately 7.09e-22, 7.09e-20 and 7.09e-18; the table assumes the exactly specified energy centering. Calibration error is covered as in section 3.

For the early reader set t_Q^-=0.001. In all three designs its full comparison schedule precedes t_X^-. Recomputing both clearances gives:

| q | Early-schedule channel error | Probability of failing to report V=0,G=1, at most |
|---:|---:|---:|
| 100 | 0.022523 | 5.073e-4 |
| 1000 | 0.00033005 | 1.090e-7 |
| 10000 | 0.000013207 | 1.745e-10 |

The table gives six finite conditional-model witnesses, not an arbitrarily accurate fixed-bandwidth limit. Finite energy does not make exact control calibration, reference preparation, noise immunity or thermodynamic reuse free.

## 9. Verification and remaining direct time target

Run:

    python verification/internal_reference_event.py
    python -m verification.internal_reference_event

The verifier writes [internal_reference_event.json](verification/internal_reference_event.json). It checks seven gate permutations on all 256 register basis states; all four system matrix units through the full late protocol and all four through the early protocol, tracing E; six independently computed spectral/source/transport/escape designs; and 16 entries of a degenerate-energy record-covariance witness. The analytic arguments establish the continuum estimates and constraint properties; no gravitational PDE or observed cosmology is simulated, and floating checks are not interval certificates.

**Gain:** finite-reference readout is now an actual interaction inside the constrained matter model. Completion is distinguished from validity, relative-clock errors have controlled consequences, and conserved outcome probabilities do not require a sharp interrogation epoch or an unnormalizable time prior.

**Remaining:** a dynamical preparation of the correlated physical encoding, source-accounted external extraction/reset and noise models, justification of the gravitational ordering/endpoint, localized apparatus with inhomogeneous constraints, and phenomenal constitution. Exact bare finite-time permanence is not restored by the new carrier.

An [on-shell incoming scattering preparation](INCOMING_CONSTRAINT_PREPARATION.md) now replaces the assumed polar controller for this same Hamiltonian. Smooth finite momentum bands fit the free gravitational window, the incoming wave operator preserves the actual constraint and source energy, and finite-upstream readiness bounds supply a revised preparation cost. This specifies physical incoming boundary data with controlled finite readiness; it does not yet supply finite-duration source synthesis or explain the boundary data. The internal reader and the preparation result close distinct conditional-model gaps, not the ultimate preparation problem.
