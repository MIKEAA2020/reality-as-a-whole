# A source-coupled pointer that fails to record a gravitational turnaround

**Result.** A natural attempt to turn the previous mathematical volume-boundary reconstruction into a physical record is to couple a pointer to signed volume motion. In a specified homogeneous Einstein–scalar–oscillator extension, the pointer has positive kinetic energy and that energy **does gravitate**. Nevertheless, when the proposed coupling is a single gradient in log-volume and the pointer energy depends only on its conserved momentum, the coupling is exactly removable by a canonical/unitary transformation. Because expansion and contraction return to the same small-volume asymptote, the extra pointer shift cancels. The complete asymptotic pointer-plus-oscillator readout is exactly the same as an **energy-matched reference with the same pointer but no gradient coupling**.

This is a negative result for that explicit coupling, not a no-go theorem for all clocks, all detectors, or finite-volume interventions. It does not implement the [two-slot reconstruction](GRAVITY_VOLUME_JET_RECONSTRUCTION_AND_LIMIT.md), resolve the general problem of time, or pass B7. It adds a homogeneous pointer to the parent model: the model's matter content changes, so it is not a passive clock transformation of the original oscillator-only system. The parent action, factor ordering, continuum construction and asymptotic boundary operations are assumed, not independently verified here.

## 1. Action, source and comparison

Use the parent units `mu=1`, `Omega=0.6`, and its oscillator energy `h_D`. Add one comoving pointer with canonical coordinate `Q_0`, momentum `P`, and positive proper energy

    h_A(P) = P²/(2M),   M>0.

The pointer is a deliberately ideal homogeneous internal degree of freedom, not a localized laboratory device. In the original ADM action its first-order contribution is `P dot Q_0 - N h_A(P)`, with the same lapse as gravity and the oscillator. Its stress-energy enters the ADM constraint. After the parent's positive densitization and canonical change to `x=log V`, `T`, the reference constraint is

    C_0 = p_T² - p_x² - exp(2x) + (4/3) exp(x) [h_D+h_A(P)].

This is the parent constraint with an **additional physical energy source**; using the original oscillator-only reflection as a baseline would omit the meter's backreaction. No new external time is introduced. `T` is the parent's massless-scalar relational variable on its selected nonzero-frequency sector.

Now define a smooth real function `G(x)` with `G(-infinity)=0`, and let `g=G'`. Introduce `Q_0=Q+G(x)` in the *first-order action*. Since

    p_old dot x + P dot Q_0 = (p_old+g P) dot x + P dot Q,

put `p_x=p_old+gP`. The same action becomes

    C_g = p_T² - (p_x-g(x)P)² - exp(2x)
          + (4/3) exp(x) [h_D+P²/(2M)].

The term proportional to momentum may look like an internal velocity-sensitive detector, but this particular interaction is the above canonical transformation. The squared term, including the `g²P²` contribution, must be retained: omitting it changes the model and invalidates the conclusion. The comparison holds the pointer energy, states, reference and all other terms fixed. The lapse-coupled homogeneous matter ansatz is not derived here from a full covariant local pointer field, and the boundary preparation/readout/reset still requires physical implementation.

For the numerical control, `G=0` for `x<=-1`, `G=0.8` for `x>=1`, and between them, with `t=(x+1)/2`,

    G(x)=0.8(10t³-15t⁴+6t⁵),   g(x)=G'(x)>=0.

Thus `g` is compactly supported and nonnegative. Cancellation is **not** caused by choosing positive and negative coupling lobes whose integral vanishes. `G` need not return to zero at `+infinity`; the recollapsing channel comes from and returns to `x -> -infinity`.

## 2. Classical pointer comparison across both crossings

Define `pi=p_x-gP` and `Q_0=Q+G(x)`. These and `(x,P)` obey canonical brackets, and the constraint in `(x,pi,Q_0,P)` is `C_0`. At the same physical point,

    Q_g(T) - Q_0(T) = -G(x(T)),

provided the incoming coordinates are matched where `G=0`. This relation compares the coupled pointer to the **same-energy reference pointer**; it is not a statement that the free pointer `Q_0` is fixed. Because `P²/(2M)` is present, the free pointer may evolve and carry information in its own right.

For `k=-p_T>0` and an oscillator energy `E_n`, put

    kappa = (2/3)[E_n+P²/(2M)],
    V(T)=k²/[sqrt(k²+kappa²) cosh(T-T_*)-kappa],
    pi(T)=-k sqrt(k²+kappa²) sinh(T-T_*) /
               [sqrt(k²+kappa²) cosh(T-T_*)-kappa].

With the scalar-time orientation and a matched reference,

    d(Q_g-Q_0)/dT = -g(x) dx/dT,
    dx/dT=pi/k.

The interaction's added shift is the **same** at the two visits to any fixed `x`, and returns to zero as `x -> -infinity`. A finite-time device that copies the pointer on the way in could change that conclusion, but such a latch, its trigger, energy and failure branches are absent here; it is not valid to pretend that the final pointer has already stored that earlier reading.

For the explicit model `k=2`, `P=0.4`, `M=1.3`, `n=0`, the gravitating source gives `kappa≈0.241026` and turning volume `≈2.25550`. At `x=-0.25` the two scalar readings are approximately `-1.63785` and `+1.63785`; the **additional** shift relative to the matched free pointer is `-0.220166` at each. The return shift is zero analytically. These are classical comparison values, not observed records; finite-cutoff numerical integration only approximates the endpoint.

## 3. Exact quantum cancellation on the physical sector

Work in `L²(R_x) tensor L²(R_Q) tensor C²_D` and set `p_x=-i partial_x`, `P=-i partial_Q`. Fix the reference Morse/direct-integral realization of the parent ordering; for each pointer momentum p and oscillator level n its potential parameter is

    kappa_n(p) = (2/3)[Omega(n+1/2)+p²/(2M)].

The reference spatial operator is `Theta_0=p_x²+exp(2x)-(4/3)exp(x)(h_D+h_A)`. Each fixed-p Morse fiber is semibounded, but the unrestricted direct integral need not be bounded below uniformly as `|p|` grows; take the self-adjoint maximal direct integral and do not assert a global positive square root. Define

    U = exp[i G(x) P],
    Theta_g = U Theta_0 U†,
    U p_x U† = p_x-g(x)P,
    C_g = U C_0 U†.

The equality fixes the ordering, including the derivative-of-g term hidden in the square. Define the interacting operator on the transported domain `U D(C_0)`. This is self-adjoint when the reference joint-spectral realization is; no unproved equality of naive unbounded domains is needed. `U` commutes with `p_T`, `P` and `h_D`, so it preserves the scalar-frequency and conserved-pointer sectors. For each `(n,p)`, the same real-spectrum constraint excludes negative auxiliary Morse bound modes, exactly as in the parent; they are not omitted detection failures. The full physical group-averaged sector is transported by U with the same `1/(2k)` rigging factor. Tests may use packets supported in `k in [2,2.01]`, `p in [-0.6,0.6]`; no nonnormalizable p eigenstate is presented as an experiment.

For any generalized positive-continuum mode `f_(n,p,k)(x)`, the interacting mode is `exp[iG(x)p] f`. Since `G=0` at the entire incoming/outgoing small-volume asymptote, the incoming **and** outgoing amplitudes agree with the energy-matched reference. Hence on the physical incoming representation

    S_g(k,n,p) = S_0(k,n,p)
               = S_Morse(k,kappa_n(p)),

including phases, not just reflection probabilities. Therefore **all** outgoing density matrices and all specified asymptotic POVM/instrument statistics agree for arbitrary input states, even with reference entanglement. This statement is about the added gradient coupling, not about whether the freely gravitating pointer can itself become correlated with the geometry or oscillator. The proof requires the stated asymptotic identification, the matched pointer source and ordering, and no extra interaction/readout in between. It is not a theorem about noncommuting meter Hamiltonians or other dynamics.

## 4. A complete pointer-and-Ramsey boundary readout

To make “no extra asymptotic record” an actual conditional prediction, assume a normalized incoming product with oscillator `|+>`, uniform `k` packet on `[2,2.01]`, and

    chi(p) = sqrt[15/(16a)] [1-(p/a)²] for |p|<=a, else 0,
    a=0.6,  M=1.3.

This pointer packet is normalizable, has finite momentum spread and finite Q variance. The support is a preparation restriction, **not** a claim that a sharply momentum-bounded subspace carries a globally self-adjoint canonical Q. The physical pointer is defined on the full `L²(R_Q)`; its Q measurement need not preserve the input momentum band.

For outgoing pointer coordinate q let

    A_n(k,q)=(2pi)^(-1/2) integral dp exp(ipq) chi(p) S_n(k,p),
    K_(sigma,q)(k) = |sigma><sigma| diag(A_0(k,q),A_1(k,q)),
    sigma in {+,-}.

These are boundary readout Kraus densities on the oscillator and geometry, after the specified pointer preparation. The corresponding complete instrument integrates over q and retains the oscillator outcome. Parseval, `|S_n|=1`, `integral |chi|²=1`, and `sum_sigma |sigma><sigma|=I` give `sum_sigma integral dq K†K=I` on the incoming sector. Coarse-grain q into `[-4,4]` and its complement: **all four** `(sigma, inside/outside)` outputs are retained. The oscillator and pointer readout and the preparation are assumed asymptotic operations, not a finite-volume source-coupled device with modeled readout failure.

The finite-band numerical values, identical in the coupled and matched-reference theories by the exact argument above, are approximately:

| Outcome | Probability |
|---|---:|
| `+`, inside | 0.516512 |
| `+`, outside | 0.057563 |
| `-`, inside | 0.383777 |
| `-`, outside | 0.042147 |

These probabilities are a **model calculation**, not data. They are not all concentrated inside the accepted q window, and discarding the outside outcomes would change the operation. The gap phase depends on pointer energy: at `k=2`, the illustrative spectral response `p_+` changes from approximately `0.576407` at `p=0` to `0.558740` at `p=0.6`. Those are spectral response functions, not probabilities assigned to exact momentum eigenstates. They underscore why a pointer-free comparison would mistake its real gravitational effect for a direction signal.

## 5. What could evade the failure, and what would count

The exact cancellation rests on `h_A` commuting with `P`. A pointer with an additional position-dependent energy, for example `h_A=(P²+omega_A² Q²)/(2M)` with declared units, does not satisfy the same equivalence while holding the potential fixed: `U Q U†=Q+G(x)`. The transformed reference contains the **shifted** pointer potential. This observation does not prove such a pointer records direction; it identifies a concrete class for a further calculation, with different dynamics and additional source energy.

A useful next test must specify a single noncommuting energy or a finite-time internal latch in the action, its self-adjoint constraint and positive-frequency physical domain, a normalizable input and **complete** pointer outcomes. The reference must retain the same pointer energy and initialization. A predeclared crossing-record statistic must distinguish the coupled from that matched reference by more than controlled numerical/analytic error, including output failure and any mid-trajectory intervention. If it does not, the detector has failed its target. If it does, one must still determine whether the record actually distinguishes the two orientations, rather than only elapsed time or the pointer's source-dependent phase. Neither result alone would close full gravity or B7.

## 6. Checks and battery status

[The verifier](verification/gravity_gradient_pointer_gate.py) checks the covariant Morse ODE at 108 parameter points, the two classical crossings and turning trajectory, positive-pointer-energy backreaction, and the complete finite-packet boundary readout. Its [JSON receipt](verification/gravity_gradient_pointer_gate.json) records the inputs and results. The [tests](verification/gravity_gradient_pointer_gate_test.py) include nonnegative localized coupling, same-volume cancellation, pointer-energy and outside-window controls. At the midband point, 128- and 256-panel quadrature results differ by at most `5.0e-9`; this is convergence evidence, not an interval-certified bound or a proof of the parent model. The exact cancellation follows from the canonical/unitary transformation and asymptotic identification, not numerical sampling.

The internal B7 time/gravity gate remains open, as do B6/B8, the experiential and measure bridges, and the other substantive gates except B3's conditional inference. The external battery's reported preregistration, program, JSON and freeze were not supplied, so it cannot be replayed. Regression-script exits are not formal research-gate passes.
