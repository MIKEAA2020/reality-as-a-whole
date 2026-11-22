# A finite orientation-record protocol in the existing dust-clock model

**Result.** In the repository's existing homogeneous Einstein–scalar–dust model, a specified finite-duration, gravity-dependent quantum control can copy the sign of a **code-projected dilation observable** to a three-outcome register. Two explicit normalized scalar-wavepacket preparations have identical volume distributions but opposite signs of the free volume slope. The idealized record distinguishes these preparations, with both outcomes and an outside-code outcome retained. The control's energy is included in the constraint, and the declared code retains a positive relational dust-energy bound.

This is more than interpreting the earlier spin flip as a direction label, but it is **not** the requested same-constraint crossing-triggered detector. It switches to [the pre-existing dust quantization](DUST_CLOCK_RECORD.md), which adds ideal proper dust and uses a different ordering/domain from [the oscillator scattering model](GRAVITY_NONCOMMUTING_POINTER_SCATTERING.md). No equivalence between them has been shown. The pulse is scheduled by ideal dust, addresses nonlocal spectral projectors and is counter-rotated using the gravitational operator. It is a stipulated bounded Hamiltonian, not a derived local laboratory apparatus. The protocol measures an anchored, code-projected observable, not a generally calibrated sharp crossing. B7 and the full problem of time remain open.

## 1. Fixed gravitational sector and a real orientation observable

Use the dust model's self-adjoint Friedrichs quantization, `Lambda=-0.75`, `r=a^(3/2)>0`, `V=a³=r²`, and scalar-momentum fibers `|p_phi|<=0.1`. As in the parent, `omega_g=0.75`, `beta=2` and

    nu(p)=sqrt(1/4-8p²/3),
    A_p f_(n,p)=omega_g(2n+1+nu(p)) f_(n,p),
    f_(n,p)(r) proportional to r^(nu+1/2) exp(-beta r²/2) L_n^nu(beta r²).

The normalized radial modes are chosen **real**. A continuous scalar p eigenstate is not normalizable; preparations below use normalized wavepackets over the band. The band restriction, Friedrichs endpoint condition and ideal dust are model choices, not a singularity resolution or a derivation of the parent Morse model's quantum theory.

On `L²(R_+,dr)` define the self-adjoint dilation generator

    D = (r p_r+p_r r)/2 = -i(r partial_r+1/2).

The unitary change `y=log r`, `phi(y)=exp(y/2) psi(exp y)` sends D to `-i partial_y`; its sign has a well-defined spectral projection even though a self-adjoint canonical momentum on the half-line is not assumed. Between pulses the dust-time Hamiltonian is `-A+E_b`. On the finite combinations considered here,

    d <V>/d tau = i <[-A,V]> = -(3/4)<D>.

Thus negative `<D>` means the **mean volume initially increases** in this dust-time orientation, and positive means it decreases. This derivative is a quantum expectation statement, not a claim that every state has a definite classical trajectory or an instantaneous sharp momentum.

Use the code of radial levels `n=6,...,15` for every p in the band, with projector `P_code`. The ten-dimensional compression `D_code=P_code D P_code` has the exact entries

    (D_code)_(n+1,n) = -i sqrt((n+1)(n+nu+1)),
    (D_code)_(n,n+1) = +i sqrt((n+1)(n+nu+1)),

with the remaining entries zero. This follows from the Laguerre recurrences, not from treating a volume derivative as a classical bit. The even-dimensional irreducible tridiagonal matrix has no zero eigenvalue. Let `Pi_E` and `Pi_C` be its negative- and positive-eigenvalue projectors, extended by zero outside the code, and let `Pi_?=I-P_code`. They are complete orthogonal projections. `Pi_E`/`Pi_C` are **not** asserted to equal the spectral projections of the full D: compression and taking the sign do not generally commute.

## 2. Matched wavepackets and an analytic sign check

Prepare either of the two normalizable physical root states, using the same uniform scalar packet on `[-0.1,0.1]` and coefficients

    w_j^(E) = sqrt[2/11] sin[(j+1)pi/11] i^j,
    w_j^(C) = (w_j^(E))* ,       j=0,...,9,

on `f_(6+j,p)`. At each p the modes are real, so the two radial wavefunctions are complex conjugates. Consequently **their complete initial volume distributions coincide**, as do their diagonal gravitational-energy distributions. The two states nevertheless have opposite dilation means and opposite free mean-volume slopes. They are model preparations, not states reconstructed from an observed universe.

An analytic band-uniform calibration is possible without a sampled minimum. For `0<=nu<=1/2`, the ladder factors obey

    n+1 <= sqrt[(n+1)(n+nu+1)] <= n+5/4.

Inserting these bounds into the finite sums for the full D mean and second moment gives `|<D>| > 21.10` and `<D²> < 483.3` throughout the scalar band. A one-sided Cantelli inequality then bounds the probability of the *opposite sign* in a **separate ideal measurement of full D** by less than `0.079` for either preparation. The same argument applies to `D_code`: its mean agrees on a code state and its second moment cannot exceed that of full D. These are conservative analytic bounds; they are not interval certifications of the numerical probabilities below.

For the declared uniform packet, numerical diagonalization gives a code-record probability of about `0.999997452` for its corresponding label and `0.000002548` for the opposite label. This is **state-discrimination performance for these two stipulated preparations**, not a universally calibrated measurement of the sign of full D. `D_code` and the full sign-of-D observable need not be jointly measurable; the two separate sign guarantees above do not manufacture a joint distribution or a general detector-error bound.

## 3. A finite pulse and all three register outcomes

Take a qutrit register initialized in `|0>`; reserve `|1>` for E and `|2>` for C. Let `S_01,S_02` exchange the named qutrit basis states and define positive projectors

    b_E=(I-S_01)/2,   b_C=(I-S_02)/2,
    B = Pi_E tensor b_E + Pi_C tensor b_C.

`B` is bounded, `0<=B<=I`, and vanishes outside the code. Let `U_0(tau)=exp(i A tau)`, the free geometry propagation, and specify the internal control

    h(tau) = E_b I + g(tau) U_0(tau) B U_0(tau)†,
    g(tau) = (2pi/ell) sin²(pi tau/ell) on [0,ell], else 0,
    E_b=1, ell=1.

The actual interaction is geometry-dependent and does not generally commute with A. The dust-coordinate dependence is internal to the constraint, but it is an **ideal, precisely programmed, nonlocal counter-rotating control**. Its dependence on spectral projectors, p, and the full operator A has not been derived from a local matter Lagrangian. The chosen sign observable is anchored at `tau=0` by the control; this is not a volume-triggered device that autonomously locates an unknown crossing.

In the interaction picture the pulse is simply `g(tau) B`, and its area is pi. The unitary swaps `|0>` to `|1>` on `Pi_E`, to `|2>` on `Pi_C`, and leaves it at `|0>` on `Pi_?`. Up to the common free propagation and phase, the induced geometry Kraus operators are

    K_E = exp(i A ell) Pi_E,
    K_C = exp(i A ell) Pi_C,
    K_? = exp(i A ell) Pi_?,
    sum_(E,C,?) K†K = I.

Thus all outcomes and their poststates are specified. `?` is an outside-code/ambiguous outcome, not an assumed hardware failure rate; on these two inputs it is exactly zero in the ideal model. The nonselective operation dephases the state in the three projector sectors and is **not** a passive frame change. The qutrit readout is a supplied ideal operation. Once the pulse is over, the pointer projectors commute with the free Hamiltonian, so their dressed physical record effects are conserved in this ideal model. No noise tolerance, finite reference packet, reset or macroscopic readout has been demonstrated.

## 4. Self-adjoint constraint and source budget—including the correction

The quantum constraint is the dust model's linear-clock form with the newly stipulated bounded coupling:

    C = p_tau - A + h(tau).

The code is invariant under A and the control. The latter is bounded and strongly continuous; the propagator of `-A+h(tau)` defines the transported self-adjoint constraint domain exactly as in the parent dust model. This is not a naive assumption that a time-dependent unbounded differential expression is self-adjoint on every intersection domain. The physical inner product is the common root-space norm; a uniform normalizable dust-time prior is not introduced.

Here **A is not conserved during the measurement**: unlike the parent register-only controls, the new geometry-sensitive projectors do not commute with A. The exact balances are

    d<A>/d tau = i<[h,A]>,
    d<h>/d tau = <partial_tau h> + i<[h,A]>,
    d<A-h>/d tau = -<partial_tau h>.

The dust source exchanges energy with the geometry/control. It would be wrong to reuse the parent dust note's `d<A>/d tau=0` for this interaction.

Nevertheless, on the invariant calibrated code the operator inequalities remain valid for every pulse time:

    A_min = 0.75[13+nu(0.1)] = 10.104436...,
    A_max = 0.75[31+0.5] = 23.625,
    1 <= h(tau) <= 1+2pi = 7.283185...,
    2.821250... <= A-h(tau) <= 22.625.

Thus the **relational** dust-energy operator is positive and bounded on this code; this does not imply positive spectral support for bare kinematic `p_tau` or a finite normalizable dust clock. For the uniform p-packet example, the nonselective measurement numerically increases mean A by about `0.000213605`; since h returns to `E_b I`, mean relational dust energy `A-h` increases by the same amount. The gravitational contribution to the constraint is `-A`, so its change has the opposite sign. This small number is input-specific, not a general apparatus cost or a claim that backreaction vanishes.

## 5. What is tested, and what still blocks B7

[The code](verification/dust_orientation_record.py), [receipt](verification/dust_orientation_record.json), and [five tests](verification/dust_orientation_record_test.py) use NumPy/SciPy from the pinned [isolated requirements](verification/requirements-gravity-spin-pointer.txt). They evaluate the exact finite spectral matrices, a normalizable p-packet, the full-D first two moments including leakage to levels just outside the code, matched volume densities, both sign projectors, the noncommutator with A, and the complete three-level record. A numerical integration of the **actual time-dependent** 30-dimensional Schrödinger equation agrees with the analytically controlled pulse to about `3.3e-11` in the reported sample. The radial recurrence is checked independently by finite differences. Numerical quadrature and solver tolerances are not interval proofs; the stated positivity and Cantelli bounds are analytic, given the parent quantization and specified control.

The result establishes a direction-sensitive **mean-slope preparation witness** and a complete record of the code sign in this ideal dust theory. It does not demonstrate a localized `V=b` crossing instrument, a single-run classical direction for arbitrary quantum states, or equivalence to the noncommuting oscillator-pointer scattering model. In particular, exact equality of the two *initial* volume distributions does not itself supply a recorded joint volume-and-direction event. An energy-matched but physically realizable local control, a finite reference with errors and failures, and a demonstrably equivalent map between the two different quantizations are still needed before the previous same-constraint crossing gate can be passed.

There is no proof here of the inhomogeneous gravitational constraint algebra, emergent spacetime, phenomenal succession, or the rest of the formal battery. The external foundation battery remains unreplayable without its reported preregistration, program, JSON and freeze materials. Passing model tests is not a B7 or full-battery pass.
