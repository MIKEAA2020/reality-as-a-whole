# A finite source feeding a finite gravitational program clock

## 1. The advance and the change of model

A two-level source, initially excited, can release one excitation into a **finite clock register** that autonomously executes a finite record program. The source depletion, clock preparation, gate execution and incomplete-operation outcomes follow from one positive, lapse-coupled Hamiltonian. No prescribed incoming carrier packet, polar encoding, ideal dust coordinate or externally switched gate is needed.

This is an **alternative apparatus model**, not a Hamiltonian synthesis of the earlier cosine packets. The [incoming scattering construction](INCOMING_CONSTRAINT_PREPARATION.md) remains valid for that different apparatus. Here a finite lattice clock replaces both continuous carriers. The exact solution has degenerate internal register levels; a bounded noncommuting system-Hamiltonian perturbation is included with a separate error budget.

This is a finite autonomous event/program clock; its sites indicate program progress, not a proved precision proper-time estimator. All apparatus degrees of freedom in the construction are finite. The price is a **finite readout window**, not a permanent autonomous latch. Finite closed clocks recur. The infinite half-line used below is only a comparison for a rigorously bounded finite device.

The assumed initial resource is now a single already-physical source excitation and blank finite registers. Its origin is not derived from nothing. External extraction/reset, material realization, inhomogeneous constraints and phenomenal constitution remain separate obligations.

## 2. Finite source, finite clock and local programmed hopping

Take a source qubit and K-1 clock sites, each with at most one excitation. Restrict to the conserved single-excitation sector:

    |0> = source excited, clock vacuum,
    |n> = source ground, clock excitation at site n,  1<=n<=K-1.

This is a K-dimensional clock/source Hilbert space. The underlying finite spin register has finitely many blank sites; their preparation and number are resources. It is not an infinite medium hidden behind a finite mean-energy statement.

Use the eight-qubit internal register S,D,M,E,F,R,V,G from the internal-reader report. Initially all except S,E are |0>, S is arbitrary and E is I/2. An untouched zero-energy E purifier can be included. Define the eight bond unitaries:

    U_0=I,                              source emission,
    U_1=CNOT_(S->D),
    U_2=CNOT_(D->M),
    U_3=CNOT_(M->E),
    U_4=X_F,
    U_5=CNOT_(F->V),
    U_6=Toffoli_(V,M->R),
    U_7=X_G.

For n>=8 set U_n=I. The first bond emits the source excitation without acting on S. The next seven execute recording, validation, copying and completion. Let L=8, W_0=I and

    W_n=U_(n-1)...U_0,
    W_n=W_L for n>=L.

The apparatus Hamiltonian is

    H_P=E_c I + gamma sum_(n=0)^(K-2)
          [|n+1><n| tensor U_n + |n><n+1| tensor U_n^dagger].

Each term is a local source/clock hop with a finite-register unitary. The reverse hop undoes its corresponding gate. The device has not inserted an absorbing halt rule into a unitary evolution.

Define the clock-controlled unitary

    Q=sum_n |n><n| tensor W_n.

Direct multiplication gives

    H_P=Q [(E_c I+gamma A_K) tensor I_reg] Q^dagger,

where A_K is the adjacency matrix of the K-position open chain. Therefore

    E_c-2gamma <= H_P <= E_c+2gamma.

Individual hopping interactions need not be positive; the **full** matter energy is positive when E_c>2gamma. The constant E_c is a real comoving source, not an energy offset discarded from Einstein's equation.

The initial source state has

    <H_P>=E_c, Var(H_P)=gamma^2.

It is an eigenstate of the uncoupled onsite occupation energy but not of the full always-coupled Hamiltonian. Its finite spectral coherence is an explicit preparation resource, not a free perfect-clock state.

## 3. Actual gravitational action and exact finite spectral fit

Use flat FLRW Einstein–scalar gravity with Lambda<0 and the previously declared radial measure and Friedrichs extension. A finite complex amplitude z for the joint single-excitation clock/register sector supplies a canonical matter action

    L_matter=i z^dagger zdot - N z^dagger H_P z
             - lambda(z^dagger z-1).

Equivalently one can use the finite spin clock with number-conserving controlled hops and restrict to excitation number one. The single-excitation restriction is declared and dynamically invariant, not postselection on successful completion.

Lapse variation gives

    C=H_P-A,
    A=(3/16)p_r^2+|Lambda|r^2-p_phi^2/(2r^2).

There is no dust field and no control depending on the arbitrary action parameter. Clock position itself controls the gates. The smeared internal-coordinate interpretation remains; a localized relativistic lattice is not derived.

Fix radial level n=0 and scalar band 0.05<=p_phi<=0.25. With omega_g=1 and Lambda=-4/3,

    epsilon_0(p)=1+nu(p),
    nu(p)=sqrt(1/4-8p^2/3).

Let E_c be the center and W the half-width of this gravitational window:

    E_c=1+[nu(0.05)+nu(0.25)]/2 = approximately 1.3909817104,
    W=[nu(0.05)-nu(0.25)]/2 = approximately 0.1023065758.

Choose gamma=1/64. Then the **entire** apparatus spectrum lies strictly inside the gravitational window since 2gamma=0.03125<W. Every register state, not just the mean source energy, fits. There is no spectral filtering or polar inverse.

The gravitational ordering, restricted scalar band and endpoint condition are still assumptions. This does not establish equivalence with the earlier KL/Morse quantization or physical singularity resolution.

## 4. Physical norm for a finite apparatus spectrum

The exact apparatus energies are

    E_j=E_c+2gamma cos[pi j/(K+1)],  j=1,...,K,

with register degeneracy. Each has a unique scalar momentum p_j inside the band, determined by epsilon_0(p_j)=E_j. Let a label the corresponding finite degeneracy. Group averaging gives

    ||eta f||_phys^2=sum_(j,a) |f_(j,a)(p_j)|^2/J(p_j),
    J(p)=|epsilon_0'(p)|=8p/(3nu)>0.

After f_(j,a)(p_j)=sqrt(J(p_j)) psi_(j,a), the physical root space is precisely the finite clock/register Hilbert space with its usual norm. Its dimension is K times 256, before an optional purifier or untouched reference.

The physical initial state |0> tensor ready register is therefore allowed **exactly**. In the apparatus eigenbasis its clock coefficients are sqrt[2/(K+1)] sin[pi j/(K+1)]. They determine the corresponding gravitational correlations through p_j and the rigging factor. An independently selected geometry is not tensored onto that source.

Here the discrete apparatus spectrum changes the reduced measure to a finite sum. Normalizability is in the physical norm. This does not license delta-normalized scalar packets in the older models whose physical measure was continuous dp, nor does it create a normalizable kinematic zero-constraint vector.

The relational representative evolves as exp(-iH_P t). The label t is the gravitational–scalar spectral phase representation, not a new matter clock or an externally switched control. The finite readout-window theorem is conditional on those representatives; it does not supply a sharp physical global timestamp or a uniform prior over t.

## 5. Autonomous source emission and exact programmed states

Because W_0=I, the actual state starting at the excited source is

    Psi(t)=sum_(n=0)^(K-1) a_n^(K)(t) |n> tensor W_n |psi_ready>.

This holds for arbitrary S/reference entanglement and purified E. The exact amplitudes are

    a_n^(K)(t)=exp(-iE_c t) [2/(K+1)] sum_(j=1)^K
       sin(theta_j) sin[(n+1)theta_j] exp[-2i gamma t cos(theta_j)],
    theta_j=pi j/(K+1).

No incoming packet has been assumed: the carrier excitation is emitted by the source bond. Preparation and use form one autonomous process, rather than first synthesizing an arbitrarily prescribed free wave packet.

The source energy is E_c times its excitation projector. The clock onsite energy is E_c times excitation away from site zero. Thus

    <H_source(t)>=E_c |a_0(t)|^2,
    <H_clock,onsite(t)>=E_c[1-|a_0(t)|^2].

For the exact program model, the mean hopping energy stays zero: its initial value is zero and H_P=E_c I+H_hop. The source's lost onsite energy is exactly the clock's gained onsite energy. Hopping correlations and their variance remain part of the Hamiltonian; they have not been discarded as free work.

This is depletion and possible return of a finite excitation, not irreversible heat dumping. No reset cycle or thermodynamic minimum is claimed.

## 6. Complete instrument: preparation pending, program pending, completed record

Define the mutually exclusive clock sectors

    source pending: n=0,
    program pending: 1<=n<L,
    completed: L<=n<K.

For completed positions W_n=W_L. Tracing E after W_L implements the exact Z-measurement record channel: D=M=R=d, F=V=G=1, and the S map is rho -> P_d rho P_d for each d. All other free register Hamiltonians are zero in this exactly solvable benchmark.

Measure the source/program/completed sectors and, on completion, the R bit. These operations define CP maps whose probabilities sum to one. Completion probability

    p_done(t)=sum_(n=L)^(K-1) |a_n^(K)(t)|^2

is independent of the S input. The completed subinstrument is **exactly p_done times the ideal recorded instrument**, even with entangled references. The incomplete maps retain the actual intermediate W_n states. No state-dependent renormalization hides pending source or program amplitude.

Since G flips only on the final programmed bond, on the reachable history states G=1 is equivalent to completed clock position. The hardware completion bit can therefore flag success without assuming a sharp arrival-time observable. Reading it repeatedly is a different monitored process.

For the complete instrument, including a distinct incomplete label, the half-diamond distance to the ideal always-completed instrument is exactly

    1-p_done(t).

This is stronger than squaring or tracing away an uncontrolled vector error: success has exactly the desired channel, while the incomplete output lies under an orthogonal label. It is not a guarantee of success at every finite time.

### Constraint-compatible meaning of the instrument

These are physical-root instruments, not bare app-only projectors commuting with H_P. A strong constraint-compatible lift exists explicitly. In energy-normalized gravitational coordinates E_g, write residual c=E_j-E_g. Since every E_j lies strictly inside the gravitational window, choose delta>0 smaller than their common spectral margin. The kinematic strip |c|<delta is

    L^2((-delta,delta),dc) tensor H_root,
    C=c I.

Lift any root Kraus matrix B as I_c tensor B on this strip and zero outside. It strongly commutes with C. A complete root instrument sums to the identity on the strip; adding an outside-strip complement completes the kinematic instrument if desired. At c=0 it gives exactly the stated physical instrument, with the correct rigging rescaling.

Such a lift changes gravitational and apparatus energies together. It must not be identified with a literal instantaneous app-only projection at fixed geometry. This establishes mathematical constraint compatibility, **not an extra Hamiltonian implementing external extraction for free**.

## 7. Uniform finite-window theorem with a finite clock

Use an infinite half-line only as a proof comparison. For its source-localized initial state, with tau=gamma t,

    a_n^infinity(t)=exp(-iE_c t)(-i)^n
       [J_n(2tau)+J_(n+2)(2tau)]
     =exp(-iE_c t)(-i)^n (n+1)J_(n+1)(2tau)/tau.

The integer-order Bessel integral representation gives |J_m(z)|<=1 for real z. Consequently

    p_source,infinity(t)<=1/tau^2,
    p_pending,infinity(t)<=S_L/tau^2,
    S_L=sum_(m=1)^L m^2=L(L+1)(2L+1)/6.

Here L=8 and S_L=204. These are analytic envelopes, not maxima over a sampled time grid.

Embed the finite chain in the half-line and delete the bond connecting K-1 to K. Starting from site zero, the first K-1 powers of the two adjacency matrices agree. Their norms are at most two. For z=2gamma t and K>z, the exponential series and a Poisson-tail estimate give

    ||Psi_K(t)-Psi_infinity(t)||
      <=2 sum_(k=K)^infinity z^k/k!
      <=2(ez/K)^K =:epsilon_K(t).

The same bound holds for every S/reference input after the program gauge transformation. It does not assume that the finite clock never reflects.

For a desired window T_min<=t<=T_max, choose K and epsilon_b>0 so epsilon_K(T_max)<=epsilon_b. Then uniformly throughout the window,

    p_source,K(t)<=[1/(gamma T_min)+epsilon_b]^2,
    1-p_done,K(t)<=[sqrt(S_L)/(gamma T_min)+epsilon_b]^2=:B.

B bounds the complete instrument's half-diamond error. It also gives a source-depletion certificate with the separate first inequality. This is an unmonitored-evolution plus single-query theorem, not a continuous first-passage distribution or a repeated-read retention result.

A sufficient resource choice is K>=4e gamma T_max and K>=log_2(2/epsilon_b). At fixed ratio T_max/T_min, reaching incomplete probability eta uses finite duration and clock size of sufficient order

    gamma T_min=O(L^(3/2)/sqrt(eta)),
    K=O(L^(3/2)/sqrt(eta)+log(1/epsilon_b)).

These are construction costs, not universal lower bounds. The hardware size grows even though the single-excitation energy band stays bounded.

## 8. Noncommuting system energy: a controlled extension, not silent omission

The exact gauge solution used a degenerate free S. To include a genuinely noncommuting measured-system Hamiltonian, take the actual autonomous model

    H_omega=H_P+omega X_S.

It still conserves excitation number, has positive source energy when E_c>2gamma+omega, and its entire spectrum still fits the same gravitational window when 2gamma+omega<W. Its physical root remains the full finite apparatus space by the same atomic rigging argument; no new polar preparation is needed.

Duhamel gives the uniform state-isometry estimate

    ||exp(-iH_omega t)-exp(-iH_P t)||<=omega t.

For t in the readout window, put d_omega=omega T_max. The complete instrument is within half-diamond distance at most

    min(1,B+d_omega)

of the ideal initial-S Z measurement. Its incomplete probability is at most

    min(1,[sqrt(B)+d_omega]^2).

The completed conditional channel is no longer asserted exact. For source-pending probability use [sqrt(B_source)+d_omega]^2. The mean energy balance also retains the changing S energy:

    <H_hop(t)>+omega<X_S(t)>=omega<X_S(0)>.

The source/clock onsite energies still sum to E_c. This extension is conservative but explicit: it does not cover the previous fixed omega=0.1 with useful long-window bounds. Nor does longer waiting give arbitrary accuracy at fixed nonzero omega under this estimate. A nonperturbative program compatible with a fixed system gap is a further task, not a term that may be dropped.

## 9. Three finite devices, one gravitational window

Use gamma=1/64, the fixed gravitational parameters above and T_max=2T_min. The exact program has eight bonds including source emission. Use the positive conservative boundary cap epsilon_b=1e-12; the actual analytic log bounds are far smaller, but are not rounded to a claimed exact zero.

| Clock/source positions K | Readout window | Source still excited, at most | Complete-instrument error B, at most |
|---:|---:|---:|---:|
| 4096 | [8192,16384] | 6.104e-5 | 0.012452 |
| 16384 | [32768,65536] | 3.815e-6 | 0.00077820 |
| 65536 | [131072,262144] | 2.385e-7 | 0.000048638 |

The source energy is approximately 1.39098 and its initial total-energy standard deviation is gamma=0.015625. These are formal homogeneous model units, not observed cosmological parameters. The clock has K-1 actual sites; all are counted, and the internal register and source are finite.

For omega=1e-12 the additional complete-channel bounds are respectively 1.6384e-8, 6.5536e-8 and 2.62144e-7. The strongest noncommuting example therefore has complete-instrument error below 4.8900e-5 in its stated finite window. This does not convert the exactly degenerate conditional-channel theorem into an exact theorem for omega>0.

Finite-chain spectral sums also give much smaller pending probabilities at sampled epochs. Those samples are consistency checks, **not** substitutes for the uniform bound in the table.

## 10. Why no permanent depletion or eternal completion is claimed

The full device is finite dimensional. Its finitely many energy phases recur arbitrarily close to their initial values. Thus the source-localized ready state returns arbitrarily closely at sufficiently late epochs: source excitation approaches one again and G approaches zero. The verifier includes a three-position clock whose exact return occurs at gamma t=2pi/sqrt(2).

Consequently no small all-future incomplete-probability bound holds for this closed finite device. Enlarging K delays boundary returns and extends a controlled finite readout window; it does not create an irreversible latch. This differs from the earlier infinite-carrier escape theorem, not a contradiction of it. Additional environmental or thermodynamic resources would have to be counted for robust longer-lived memory or reuse.

This is a limitation of the specified finite closed apparatus, not a theorem against time, physical preparation, the complete absolute or ultimate intelligibility.

## 11. Verification and the next direct time target

Run:

    python verification/finite_source_clock.py
    python -m verification.finite_source_clock

The verifier writes [finite_source_clock.json](verification/finite_source_clock.json). It checks 36 history-channel matrix units, including all four completed S matrix units; 2048 programmed-edge gauge identities; eight small-chain spectral unitarity/energy checks; three finite-device spectral/window/resource designs; nine finite-chain pending/source samples; 15 gravitational spectral inverse/Jacobian cases; noncommuting perturbation budgets; and an exact finite recurrence witness. No large clock/register matrix is stored. The analytic arguments, not the samples, establish the uniform-window theorem and physical norm. Floating evaluations are not interval certificates or experimental observations.

**Supplied:** a finite source excitation, finite positive-energy clock, autonomous emission and exact programmed record operation, a globally fitting gravitational spectrum, complete pending/completed instruments, quantified source depletion and finite-window error, and a controlled noncommuting extension. The specially shaped incoming packet and polar controller are absent from this alternative construction.

**Still open:** the initial physical source excitation and blank resources as boundary data; a Hamiltonian for external extraction/reset; noise protection and a nonperturbative fixed-gap system; localized stress energy and inhomogeneous constraints; physical justification of the gravitational domain; and phenomenal constitution. This model does not synthesize the previous continuous-carrier wave packet or deliver permanent finite-clock memory.

A [fixed-gap finite-reservoir extension](FIXED_GAP_SOURCE_CLOCK.md) now supplies an energy-conserving lifted measurement with H_S=0.1 X_S unchanged at every clock position. The additional finite reference pays energy and coherence costs; its one-use reduced-instrument error does not grow as omega T after the actual free S output rotation is retained. Its energy requires a newly fitted gravitational window, and its initial preparation, disturbance and reuse/reset remain explicit. This removes the perturbative gap restriction in that relational measurement model, not finite-clock recurrence or the need for a microscopic external extraction mechanism.
