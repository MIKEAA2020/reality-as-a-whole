# A relational matter detector with gravitational backreaction

**Result.** This note replaces the previous external fixed-coordinate pointer with a declared generally covariant gravity–matter action. The model contains a dynamical clock, three dynamical rods, a signal field, and a detector field. Their energy and momentum enter the same Einstein constraints. For a concrete inhomogeneous signal and detector preparation on a three-torus, the coupled initial constraints are solved to second order and, for sufficiently small amplitude, a local implicit-function argument gives **exact classical initial data** in the stated ansatz. A short-time relational detector response can also be calculated.

This is not a gravitational-curvature detector, an explicit quantum instrument, a durable record, a numerical spacetime evolution, a discrete-gravity refinement or a solution of time. It uses a supplied classical spacetime description and a material clock; neither is asserted fundamental. The exact-existence argument is mathematical and local in parameter space; it does not produce an explicit closed-form exact solution or control global evolution.

## 1. What is established elsewhere

Physical reference fields and relational observables are existing techniques, not our invention. See [Tambornino's review](https://arxiv.org/abs/1109.0740), [Bamonti on dynamical and backreacting reference frames](https://arxiv.org/abs/2307.09338), and [Brunetti, Fredenhagen and Rejzner](https://arxiv.org/abs/1306.1058). The conformal method for Einstein–scalar initial data is also established; see [Choquet-Bruhat, Isenberg and Pollack](https://arxiv.org/abs/gr-qc/0610045). We use those ideas for a specific explicit interface and do not claim novelty or priority for the general construction.

The previous [second-order torus calculation](TORUS_SECOND_ORDER_GRAVITY_MATTER.md) showed that satisfying linearized vacuum constraints does not suffice and that fixed-coordinate curvature is not a full nonlinear observable. Here the reference system and detector are matter in the actual constraints, and the spacetime event is defined relationally. We do not pretend this constructs the outstanding discrete gravitational hypersurface-deformation algebra.

## 2. Covariant action and relational events

Take signature `(-,+,+,+)`, set `16 pi G=1`, and choose spatial topology `T³`. Let `T` be a real scalar clock; let `theta^i`, i=1,2,3, be circle-valued scalar rods of period `2pi`; and let `Phi` and `chi` be real scalar signal and detector fields. For `f>0`, `kappa>0`, real lambda, and a fixed bounded smooth function `W(T,theta)` on the **reference-field target space**, take

    S = integral d^4x sqrt(-g) [ R
        - 1/2 (grad T)^2 - f²/2 sum_i (grad theta^i)^2
        - 1/2 (grad Phi)^2 - 1/2 (grad chi)^2
        - lambda W(T,theta) Phi chi - kappa (Phi²+chi²)² ].

`W` is smooth and periodic in the rods, and can be localized in a small rod patch and a finite clock interval. It is an explicitly selected apparatus profile, not a function of background coordinate labels. The quartic term bounds the scalar potential below even with the bilinear interaction, though the potential need not be nonnegative everywhere. Normalization of fields and coupling is part of this model.

On a region where the map `X=(T,theta^1,theta^2,theta^3)` is invertible, define

    chi_rel(t,r) = chi( X^(-1)(t,r) ).

Here r lies in a rod-coordinate patch, with angles understood modulo `2pi`. Under a diffeomorphism acting on **all** fields, the point picked by the four reference values moves with the fields, so the value is unchanged. This is a classical relational spacetime scalar, subject to local invertibility and crossing/branch qualifications. It is not the fixed-coordinate curvature component criticized previously. A full canonical construction and Poisson algebra of these evolving observables is not carried out here.

The detector equation has an actual interaction source:

    box_g chi = lambda W(T,theta) Phi + 4 kappa chi (Phi²+chi²).

Thus it is a field-theoretic coupling, not just an abstract measurement gate. However, the response must still be read out and stabilized before it is an operational record. `W` selects which physical clock/rod values activate the interaction; it is a model input, not an independently derived measurement schedule.

## 3. Initial data, including the physical reference system

On an initial torus with coordinates in `[0,2pi)`, take

    g_ij = psi(z)^4 delta_ij,
    pi^ij = alpha sqrt(g) g^ij,
    T=0,             P_T=tau,
    theta^i=x^i mod 2pi,  P_theta^i=0,
    Phi=epsilon b cos(z), P_Phi=0,
    chi=0,           P_chi=epsilon p [1+cos(z)].

Here `alpha`, `tau`, b and p are real constants, `tau != 0`, and all P are canonical **densities**. The rod winding is a legitimate map `T³ -> T³`, not a single-valued real function `x^i` on the torus. The pointer preparation is inhomogeneous but not compactly supported; the coupling profile W can be localized. The signal varies in z. All matter fields, including clock and rods, are physical in this action.

The momentum constraints vanish **exactly**: `pi^ij=alpha sqrt(g) g^ij` has covariant divergence zero when alpha is spatially constant; for each scalar, `P_A partial_i A=0` on these data. The signal has gradient but zero momentum; the detector has momentum but zero gradient. This is not the same as declaring their stress energy negligible.

After dividing the Hamiltonian constraint by `sqrt(g)`, the remaining exact equation in this ansatz is

    F(psi,alpha,epsilon) = 8 psi^(-5) psi'' - (3/2) alpha²
      + (3/2) f² psi^(-4) + (1/2) tau² psi^(-12)
      + (epsilon² p²/2) [1+cos(z)]² psi^(-12)
      + (epsilon² b²/2) sin²(z) psi^(-4)
      + kappa epsilon^4 b^4 cos^4(z) = 0.

The bilinear interaction contributes zero on this initial slice because chi=0, not because it was removed from the action; the quartic potential contributes at fourth order. The identity `R[psi^4 delta]=-8 psi^(-5) psi''` gives the first term. At epsilon=0, choose

    psi=1,   alpha=alpha0,   alpha0²=f²+tau²/3,   alpha0>0.

The rods and clock have nonzero background energy, balanced by nonzero gravitational trace momentum. Hence the background slice is spatially flat but its spacetime is not asserted to be Minkowski or stationary. This avoids silently using positive-energy reference fields on the excluded time-symmetric flat-torus vacuum background.

## 4. Explicit inhomogeneous solution through second order

Fix the normalization `<psi>=1`, where `< >` is the normalized spatial average, and write

    psi = 1 + epsilon² u + O(epsilon^4),
    alpha = alpha0 + epsilon² a + O(epsilon^4),    <u>=0.

Define `L=6(f²+tau²)`. Expansion gives

    8 u'' - L u - 3 alpha0 a
      + (p²/2) (1+cos z)² + (b²/2) sin² z = 0.

The zero mode fixes the gravitational response to the combined detector and signal energy:

    a = (3p²+b²)/(12 alpha0).

The remaining pointwise terms are solved by

    u(z) = [p²/(8+L)] cos z
           + [(p²-b²)/(4(32+L))] cos 2z.

For the checkable example `f=1/2`, `tau=3/2`, `alpha0=1`, `p=1`, `b=2`,

    a=7/12,       u(z)=cos(z)/23 - 3 cos(2z)/188.

The rational verifier obtains zero for the Hamiltonian at orders zero and epsilon² at every z. The momentum constraints vanish by the exact argument above. This is a genuine coupling of signal, detector preparation, physical reference system and geometry in one initial-data problem; it is not yet their measurement evolution.

## 5. Why exact small-amplitude initial data exist in this ansatz

This paragraph is an analytical argument, not a claim that the checker numerically solved the nonlinear equation. Work with periodic Hölder spaces `C^(k+2,nu)(S¹)` and `C^(k,nu)(S¹)`, `0<nu<1`, and constrain `<psi>=1`. The displayed F is smooth near `psi=1>0`. At `(psi,alpha,epsilon)=(1,alpha0,0)`, its derivative in `(psi,alpha)` is

    (v,A) -> 8 v'' - L v - 3 alpha0 A,     <v>=0.

For any periodic source, its mean determines A because `alpha0>0`, and each nonzero Fourier mode is invertible because its eigenvalue is `-8 n²-L`, with `L>0`. Standard elliptic regularity gives the bounded inverse between the chosen spaces. The implicit-function theorem therefore provides a unique nearby normalized solution `(psi(epsilon),alpha(epsilon))` for sufficiently small epsilon. Positivity follows by continuity, and smooth data give smooth solutions by elliptic regularity. Together with the exact momentum-constraint argument, these are exact classical Einstein–matter **initial data** for this ansatz.

The theorem gives no explicit radius of validity and no guarantee of global spacetime evolution, long-lived rods, a good clock at all times, or existence for large detector amplitudes. Local smooth classical evolution requires the usual well-posedness assumptions and gauge choices; no such evolution is computed here. This claim of exact initial-data existence does not apply to the distinct earlier time-symmetric vacuum witness.

## 6. A short-time relational response, not yet a record

At the initial slice choose lapse `N=1` and shift zero. Then `dot T=tau/psi^6 != 0` and `dot theta^i=0`; the field-coordinate map is locally invertible for sufficiently small epsilon. Compare two classical solutions with the **same exact initial data**, one with coupling lambda and one with lambda zero, and fix the same coordinate gauge locally. At `T=0` the interaction vanishes in the initial constraints, so the same initial data work for both.

The interaction changes the second coordinate-time derivative of chi at that slice by `-lambda W(0,theta) Phi`. Initial reference-field accelerations agree between the two solutions because the interaction and its first reference-field derivatives contain `Phi chi=0` there. Converting to the clock reading and holding rod values fixed gives

    [partial_T² chi_rel]_lambda - [partial_T² chi_rel]_0
      = -lambda epsilon b W(0,r) cos(r_z) psi(r_z)^12 / tau²
      = -lambda epsilon b W(0,r) cos(r_z)/tau² + O(epsilon³).

For `b=2`, `tau=3/2`, the leading coefficient is `-8 lambda epsilon W(0,r) cos(r_z)/9`. The comparison is between two *different coupling choices*, not a comparison between two foliations. The relational event and response are invariant under passive/active diffeomorphism descriptions on the invertible patch, but that does not prove quantum instrument equivalence or a physical operation's foliation independence.

The detector field has a nonzero immediate, signal-dependent response. It is not a stored classical bit: we have not evolved the fields through a switching window, shown distinguishability of two prepared signal alternatives at a later clock reading, demonstrated persistence against local dynamics, or included readout/reset and noise. In particular, neither the energy of the distributed reference system nor that of a later recording apparatus can be dropped from the full constraints.

## 7. Checks, limitations and next gate

Follow-up: [RELATIONAL_SIGNAL_GEOMETRY_NO_GO.md](RELATIONAL_SIGNAL_GEOMETRY_NO_GO.md) proves a full-classical sign-symmetry obstruction to geometry-only reconstruction and calculates a tuned, finite-window relational detector response. It does not yet give a calibrated quantum or durable record.

Run [verification/relational_detector_initial_data.py](verification/relational_detector_initial_data.py); [the output](verification/relational_detector_initial_data.json) checks the displayed numerical example with exact rational polynomial arithmetic. It evaluates the Hamiltonian through epsilon², its average and the response coefficient. It also samples the full nonlinear constraint on the *truncated* data: for kappa=1, the maximum sampled residual falls from 4.11e-5 at epsilon=0.04 to 2.57e-6 at epsilon=0.02, consistent with fourth-order residual scaling. This numerical check does not solve the nonlinear equation. The momentum-constraint identity, local implicit-function existence and relational comparison are analytic arguments, not outputs of a numerical solver or quantum simulation.

The model still assumes ordinary continuum GR, chosen matter and compact topology. Its rods and clock are physical but idealized field systems and select a reference-field frame; local invertibility can fail. This model has no graviton TT witness carried over from the preceding note, and no direct measurement of gravity curvature. It has not been quantized, discretized, shown to recover a causal local net, tested under finite clock resolution, or compared across gravitational foliations. The next needed computation is finite-window detector evolution and a complete instrument with two controlled signal preparations and retained pointer records, including matter/reference backreaction and relational endpoints. Only afterward should one test discretization and refoliation consistency. Experience and the timeless absolute remain untouched by this classical matter construction.
