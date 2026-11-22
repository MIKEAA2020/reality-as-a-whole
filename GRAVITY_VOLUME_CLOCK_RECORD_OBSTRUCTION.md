# A volume-clock obstruction for the backreacting gravitational record

**Result.** In the existing two-channel Einstein–scalar–oscillator model, a natural but naive operation—evaluate the constrained history at a fixed volume and then treat the normalized result as a passive clock-frame change—fails. Its positive-frequency volume-evaluation map has spectral nodes **inside the previously calibrated `2 <= k <= 8` domain**. It is a state-dependent filter, has no bounded inverse there, and can substantially change the probability of the *same transported record*. This is a precise failure of that proposed reduction, not a no-go theorem for every possible volume clock. An orientation-resolved instrument or different quantum reduction might succeed; it is not constructed here.

This directly tests the next gate in [the finite-range calibration](GRAVITY_CLOCK_FINITE_RANGE_CALIBRATION.md), using [the same gravitating oscillator](GRAVITATING_PROPER_TIME_CLOCK.md), not a newly designed constraint. The [turning-clock atlas](TURNING_CLOCK_ATLAS.md) and [clock-choice equivalence](CLOCK_CHOICE_EQUIVALENCE.md) already demonstrated successful switches in other models. Neither makes this interacting gravity reduction automatically unitary. The parent action, ordering, Morse transform, rigging prescription, scattering phases and two-channel physical sector are assumed, not independently proved in this note. The model is homogeneous and has no full gravitational refoliation algebra.

## 1. Two different classical turning surfaces

Fix `mu=1`, `Omega=0.6`, hence `kappa_0=0.2`, `kappa_1=0.6`, and `k=-p_T>0`. The parent constraint for fixed oscillator energy is

    k² = p_x² + V² - 2 kappa_n V,    V=exp(x)>0.

In a chosen scalar-time orientation, the turning volume is

    V_max,n(k) = kappa_n + sqrt(k²+kappa_n²).

The classical volume chart has two branches, expanding and contracting, when `0<V<V_max,n`. With `R_n=sqrt(k²+kappa_n²)` and an orbit-dependent scalar-time origin `T_*`, the parent trajectory gives

    T_±(V;k,n) = T_* ± arcosh[(k²/V+kappa_n)/R_n].

A volume value alone does not choose `±`; the derivative of this expression diverges as its argument approaches 1. These are classical trajectories for fixed energy—not a branch decomposition of an arbitrary quantum superposition.

At `k=2`, the two maxima are approximately `2.209975` and `2.688061`. On the whole spectral band `2 <= k <= 2.01`, the volume `V=2.4` lies above the first maximum and below the second. Therefore one **cannot** use a single real, classically allowed volume crossing there as a common two-channel clock event. There are still quantum amplitudes in classically forbidden regions: this observation does not set the first channel's quantum wavefunction to zero, establish a superselection rule, or rule out a quantum clock. It does demonstrate that the two detector-energy branches gravitate differently, so the old spectator-clock atlas cannot simply be copied to both without a domain and event analysis.

## 2. The actual physical space and candidate evaluation

The parent's continuum physical space in the incoming representation is

    H_phys = L²((0,infinity),dk) tensor C²,

with negative auxiliary Morse bound modes excluded by the real-frequency constraint. For this test restrict to the invariant physical band `B=[2,8]`. Let `f_(n,k)(x)` be the **real**, continuum-normalized Morse scattering eigenfunction of

    Theta_n = -d²/dx² + exp(2x) - 2 kappa_n exp(x),
    Theta_n f_(n,k) = k² f_(n,k).

It is proportional to `z^(-1/2) W_(kappa_n,ik)(z)`, `z=2 exp(x)`, with the parent's normalization. Let `u_in,n(k)` be its unit-modulus incoming plane-wave coefficient; it changes with n. For incoming spectral amplitudes `a_n(k)`, the parent positive-frequency group-averaged history, with one harmless overall Fourier convention, is

    Psi_n(T,x) = (2pi)^(-1/2) integral_B dk
                   a_n(k) [f_(n,k)(x)/u_in,n(k)] exp(-ikT)/sqrt(2k).

The `1/sqrt(2k)` is the parent rigging Jacobian, not an optional clock probability. Strictly, this is a generalized physical history; evaluation at a fixed x is defined here on smooth compact-band amplitudes and then extended by boundedness on `B`. Fourier transform in scalar T identifies its fixed-volume output with a multiplication map on `L²(B) tensor C²`:

    (E_b a)_n(k) = g_n(k;b) a_n(k),
    g_n(k;b) = f_(n,k)(b)/[sqrt(2k) u_in,n(k)].

The convention is `V=exp(b)`. The continuous mode is bounded on this compact k band, so `E_b` is bounded there. The choice `b=0` below means `V=1`, not the turning volume. This map is a **trace/evaluation prescription**, not an apparatus derived from the action, not automatically a normalized volume POVM, and not a proof that an actual detector reads volume. No uniform probability over all values of `T` or `b` is assumed. Other choices of relational event, including an orientation-sensitive measurement, need their own physical derivation.

Because `E_b† E_b=diag(|g_0|²,|g_1|²)` depends on k and n, its normalized output is generally a state-dependent filter, not an ideal unitary frame. Even where it is one-to-one as a map of L² equivalence classes, that does not make its inverse bounded or its normalization a passive redescription. The phase factors `u_in,n` must be retained in a change of representation; their moduli do not affect the node argument.

## 3. Analytic node and unbounded-inverse result

At `b=0`, a zero `f_(1,k)(0)=0` occurs precisely when the solution decaying at `x -> +infinity` is an eigenfunction of the Dirichlet half-line operator

    H_D = -d²/dx² + exp(2x)-1.2 exp(x),  x in (0,infinity),
    f(0)=0.

This is an auxiliary half-line boundary-value problem used to locate zeros of the **full-line continuum mode**; it is not a new boundary condition imposed on the universe. The potential is smooth, increases on `x>=0`, and confines at infinity. Thus `H_D` has compact resolvent and simple discrete eigenvalues. Its second eigenvalue `lambda_2` lies in `(4,64)`:

- Split at `x=1` with a Neumann boundary on both sides. Neumann bracketing is a form lower bound. On `[0,1]` the potential is at least `-0.2`, so the second Dirichlet–Neumann eigenvalue is at least `9pi²/4-0.2 > 4`. On `[1,infinity)` the potential is at least `e²-1.2e > 4`. Consequently the decoupled operator, and hence `H_D`, has **at most one** eigenvalue at or below 4.
- For an upper bound, use as a two-dimensional trial subspace the first two Dirichlet eigenfunctions on `[0,1]`, extended by zero. The potential there is at most `e²-1.2e`; the min–max principle gives `lambda_2 <= 4pi²+e²-1.2e < 64`.

Therefore a positive continuum spectral node `k_*=sqrt(lambda_2)` lies strictly inside `B`. The sign-changing numerical root `k≈2.4965462151` below is an illustrative independently checked node; the analytic existence conclusion does not depend on floating-point root finding or on identifying which root the bracketing proof bounds.

By continuity of `g_1(k;0)`, normalized wavepackets supported in successively smaller neighborhoods of `k_*`, with all amplitude in oscillator channel 1, have `||E_0 a|| -> 0` although `||a||=1`. Hence `E_0` has **no bounded left inverse** on this band. The isolated nodes have zero spectral measure, so they do not by themselves annihilate a nonzero L² packet; the map may be injective while its range is not closed. No nonzero state-independent success probability for an exact bounded reversal follows on the entire band. This is an operator/domain statement, not a claim that a normalizable eigenstate exists at exactly `k_*`.

The formal polar decomposition `E_0=V_0 |E_0|` still yields a unitary phase representation `V_0` on the band, since the isolated zeros are null sets. Defining that representation and transporting all observables is legitimate mathematics. But extracting it from a physical evaluation would require undoing `|E_0|`; the required inverse is unbounded on this sector. A unitary polar factor alone does not show that a realizable volume reading has performed an information-preserving clock switch.

## 4. Same record, filtered state: a finite packet witness

Use the parent's asymptotic gravitational record, with joint reflection `U(k)=diag(S_0(k),S_1(k))` and incoming physical effect

    F_+(k) = U(k)† |+><+| U(k),   |+>=(|0>+|1>)/sqrt(2).

This is a legitimate bounded physical record effect in the assumed parent model; `F_- = I-F_+`. Consider a *specified alternative preparation*, not the product preparation in the preceding calibration:

    a(k) = h(k) U(k)† |+>,
    integral_B |h(k)|² dk=1.

It is a normalizable packet and is a `+` eigenstate of the same root record at every k, so its root probability is exactly 1. The preparation itself is an assumed boundary operation.

The correctly transported record in the polar output representation is `F_+^b=V_b F_+ V_b†`. Put `r_n(k)=|g_n(k;b)|`. If a hypothetical, explicitly supplied filter instrument proportional to `E_b` succeeds, then its normalized output's probability for this **transported** effect is

    p(+ | filter success)
       = 1/2 + [integral |h(k)|² r_0(k) r_1(k) dk]
                 / [integral |h(k)|² (r_0(k)²+r_1(k)²) dk].

The overall instrument normalization cancels. This is not a contradiction between clock descriptions: the successful filter is an **additional conditional operation** that generally disturbs the record. Comparing its conditional output against the unfiltered root state as if it were passive re-expression changes the experiment. The transport of the effect, including its phases, is essential; retaining the old numerical matrix in the new frame is a different event. A physically constructed instrument would also have to retain its failure branch and associated output.

For `V=1`, the parent mode functions numerically give a channel-1 node at `k≈2.4965462151`; the channel-0 response there is approximately `0.1872743` in this evaluation convention. For the normalized uniform spectral packet `h` on `[2.49,2.50]`, numerical integration gives

    root record probability                 1
    transported record after filter success  0.5085204.

For uniform packets centered on the node with widths `0.01`, `0.002`, and `0.0004`, the conditional values are `0.5077793`, `0.5015561`, and `0.5003112`: they approach `1/2` rather than 1. All are finite-width packets, not assigned probabilities for nonnormalizable energy eigenstates. These numerical numbers witness the specified **constructed filter**, not an empirical experiment or a Hamiltonian-derived volume detector. The previous response-calibration confidence bound still holds for its original unfiltered Ramsey protocol under its original assumptions; inserting this additional selection changes its preparation and requires a new analysis.

## 5. What a restricted recovery can and cannot show

On any compact spectral interval avoiding zeros of both channels, `|E_b|` has a positive lower bound `m^(1/2)` and finite upper bound. After choosing a normalization `A=c E_b` making `A†A<=I`, it can mathematically be completed by a failure Kraus operator `(I-A†A)^(1/2)`. If `m=inf spec(A†A)>0`, the correct output-to-root success operator is

    R = sqrt(m) |A|^(-1) V_b†,
    R A = sqrt(m) I,
    R†R <= I.

The recovery is completed by its own failure outcome. The joint success probability is `m` for any normalized input. Both filter and recovery are mathematical instruments, not an implemented measurement or freely available gravitational coupling. As the admitted interval approaches a node, its lower bound tends to zero, so there is no nonzero uniform `m` over `B`. This restricted statement extends the criterion in [CLOCK_CHOICE_EQUIVALENCE.md](CLOCK_CHOICE_EQUIVALENCE.md); it does not resolve the volume turning point or show that physical branch information is accessible.

## 6. Verification and the remaining gate

[The verifier](verification/gravity_volume_clock_obstruction.py) computes Morse modes, sign-bracketed nodes, finite-packet integrals and the classical turning volumes. [Its receipt](verification/gravity_volume_clock_obstruction.json) records the results; [four tests](verification/gravity_volume_clock_obstruction_test.py) check the normalizable packet, explicit transported versus untransported record phases, domains and turning-volume control. A separate 50-digit `mpmath 1.3.0` Whittaker evaluation reproduced the first listed roots (`2.8179060899355448` and `2.4965462151361800`); this is a cross-check, not an interval proof. Simpson results with 512 and 1024 subdivisions agree to `2e-8` for the reported packet. The analytic min–max argument, not these samples, establishes a node in `[2,8]`.

**B7 remains open.** No orientation-resolved volume-clock POVM or joint multi-event instrument through the turn has been derived, and no treatment of finite-volume readout, controls or apparatus reference from the parent action is supplied. Classical forbidden regions are not a quantum no-go. Future work must either derive such an instrument on a common physical Hilbert space, including both orientations, all success/failure outputs, backreaction and overlap domains, or show a valid obstruction for a clearly stated broader class. It must preserve the same anchored event and joint probabilities rather than postselecting away an inconvenient branch. No local inhomogeneous gravity constraints, emergent spacetime or phenomenal passage follows from this result.
