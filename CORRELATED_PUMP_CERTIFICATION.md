# Correlated finite sources: a complete-instrument robustness theorem

## Result and scope

The finite gravitational clock/readout construction no longer requires perfectly
prepared, mutually independent pump packets. Quantitative **pure-target marginal
fidelity bounds** suffice, even for arbitrarily correlated source batches. The
comparison controls the complete retained record instrument, not just individual
readout probabilities or successful verification branches.

This is a conditional robustness theorem for the existing constrained model. It
does not derive the source states, turn swap-test agreement into an absolute phase
certificate, prove a finite-sample confidence statement, or solve local quantum
Hamiltonian-constraint closure. It preserves the finite autonomous clock,
nonzero fixed system gap, used pumps, anchors, verification flags, and gravitational
energy accounting of [the pump construction](FINITE_REFERENCE_PUMP.md).

## 1. Pure marginal targets control a correlated batch

Let P contain all working-reference, pump, and verification-anchor ladders. For
ladder i fix the finite target packet tau_i = |b_i><b_i| and suppose

    Tr[(I - tau_i) sigma_i] <= epsilon_i,
    E = min(1, sum_i epsilon_i),   tau_P = tensor_i tau_i.

No independence between sources is assumed. The local projectors commute, and

    I - tensor_i tau_i <= sum_i (I - tau_i).

Consequently the joint target overlap p = Tr(tau_P sigma_P) is at least 1-E.
With trace distance D(rho,sigma) = ||rho-sigma||_1/2, purity of tau_P gives

    D(sigma_P, tau_P) <= sqrt(E).                         (1)

If the batch is independent of the unknown system input, initializing the batch
with sigma_P rather than tau_P changes **any subsequent complete CPTP
instrument**, including retained verification flags and all records, by at most
sqrt(E) in half-diamond distance. Ancillas entangled with the input are allowed.
This follows by tensoring the fixed source replacement with the arbitrary input
and applying trace-norm contraction. Subsequent source-source independence is
not needed; in particular, full swaps need not yield independent block channels
for the actual batch. The ideal comparison still has the earlier block factors.

### Sources initially correlated with the system and old records

For an arbitrary rho_PR, with the same marginal fidelity premises, the stronger
statement needed is decoupling from the **actual** R marginal:

    D(rho_PR, tau_P tensor rho_R) <= delta_dec,
    delta_dec = min(1, sqrt(E) + E).                      (2)

Proof: put Pi = tau_P tensor I_R, Q=I-Pi, eta=Tr(Q rho)<=E.
The Pi block is tau_P tensor A_R with Tr A_R=1-eta; the Q block
has trace eta. Writing rho_R=A_R+B_R gives Tr B_R=eta. Relative to
tau_P tensor rho_R, the two diagonal differences contribute at most eta
to trace distance. The off-diagonal block contributes at most
||Pi rho Q||_1 <= sqrt(eta(1-eta)). Thus

    D <= eta + sqrt(eta(1-eta)) <= E + sqrt(E),

also capped by 1. The inequality is valid with arbitrary quantum R.
Every subsequent complete instrument inherits this bound by contraction.

The square-root scaling cannot generally be replaced by a linear infidelity
bound. The pure state

    sqrt(1-epsilon)|b,0> + sqrt(epsilon)|b_perp,1>

has source infidelity epsilon, while its distance to tau tensor its own R
marginal is exactly

    [epsilon + sqrt(4 epsilon - 3 epsilon^2)] / 2.

The verifier evaluates this distance through a real symmetric trace-norm
calculation, as well as other correlated pure and mixed examples.

### When a channel-level claim is legitimate

An arbitrary input-dependent family of correlated states need not be a linear
channel. Do not assign it a diamond norm. A sufficient physical premise is a
CPTP initializer A: Q -> P tensor R satisfying uniform operator inequalities

    A^dagger[(I-tau_i) tensor I_R] <= epsilon_i I_Q.

These inequalities also hold against any input ancilla. Equation (2) therefore
bounds the half-diamond distance between A and tau_P tensor M, where
M=Tr_P A. To compare against an intended, undisturbed input channel M_0,
**separately add**

    delta_sys = ||M-M_0||_diamond / 2.

Source quality alone does not certify that initialization preserved the original
unknown system. The numerical witness includes a coherent CPTP initializer with
nonzero system dephasing and checks its uniform source defect operator.

## 2. Why mixed marginals and energy budgets are insufficient

Take guarded finite packets b_+ and b_- obtained by phases exp(+/- i n alpha)
from the same real packet b. Compare two pump batches:

    sigma_corr = (|b_+,b_+><b_+,b_+| + |b_-,b_-><b_-,b_-|)/2,
    sigma_ind  = [(|b_+><b_+| + |b_-><b_-|)/2] tensor itself.

They have identical complete local density matrices and identical joint energy
statistics. Nevertheless they are different joint resources. Full swaps into the
working reference followed by readouts of two fresh energy-basis Y+ probes give

    Cov_corr(d1,d2) = C1^2 sin(alpha)^2 / 4,
    Cov_ind(d1,d2) = 0.

Here C1 is the adjacent packet overlap. This is calculated using the actual
finite-ladder readout, not an assumed phenomenological phase-noise model.
For maximum ladder level 8, guard 2, alpha=0.4:

| Quantity | Correlated batch | Independent batch |
|---|---:|---:|
| Probabilities 00, 01, 10, 11 | .278434, .221566, .221566, .278434 | .25, .25, .25, .25 |
| Record covariance | .028433746 | 0 |

The distributions have total-variation distance .056867492. Each marginal's
fidelity to the intended unrotated pure packet is .828066540. Explicit density
matrices verify equality of marginals and joint energy diagonals. Thus replacing
the pure-target premise by knowledge of identical mixed marginals is invalid.

## 3. A finite-anchor test, including its backaction

Use an equal-spectrum finite ladder C as anchor for source B and a degenerate
ancilla initially |+>. Apply controlled-SWAP(B,C), then a Hadamard on the
ancilla, and retain the final Z flag +/- and both ladders. Each gate commutes
with the expanded free Hamiltonian. No energy-carrying classical drive or
infinite phase reference is introduced by these gates.

For an independent, pure anchor tau_C, tracing C only to display the source/rest
instrument gives the **unnormalized** maps

    V_+(sigma_BR) = [sigma_BR + tau_B tensor sigma_R
                    + {sigma_BR, tau_B tensor I_R}]/4,
    V_-(sigma_BR) = [sigma_BR + tau_B tensor sigma_R
                    - {sigma_BR, tau_B tensor I_R}]/4.

Hence p_+ = (1+f)/2, with f=Tr(tau sigma_B). The actual retained
instrument also contains C; the displayed marginal is not a license to discard
its energy or correlations.

This is not nondisturbing verification:

    V_+ + V_- = (sigma_BR + tau_B tensor sigma_R)/2.

The old-R marginal is unchanged only after summing both outcomes. Conditioning
on a flag can change the system or old-record state. The verifier checks both
branch formulas against the full controlled-SWAP circuit, conditional old-record
changes, the nonselective state change, and total B+C energy conservation.
Normalized pass-only maps are not automatically linear CPTP input channels.

### Imperfect and correlated anchors

If the anchor is independent but within trace distance eta_a of tau, then

    f >= 2 p_+ - 1 - eta_a.

Indeed the actual overlap Tr(sigma_B sigma_C) differs from f by at most eta_a.
If an anchor has marginal infidelity xi but can be correlated with the source
and rest, equation (2) instead gives delta_a=min(1,sqrt(xi)+xi), so

    |p_+ - (1+f)/2| <= delta_a,
    f >= 2 p_+ - 1 - 2 delta_a.

Clip inferred lower bounds at zero. These are state/model implications, not
confidence bounds from finitely many observed passes.

Without an anchor-quality premise, agreement is not a target certificate:
sigma_corr above passes the source-anchor swap test with probability 1, since
each component contains two identical packets. Its unrotated target fidelity
is still only .828066540. Unanchored energy-invariant tests cannot certify an
absolute phase. A common rotation of systems, sources and anchors is a gauge
change; rotating the sources relative to the system is an observable mismatch.

### A useful one-way rejection bound

Test each source against its corresponding anchor. The all-pass effect on the
ladders is the product of pairwise symmetric-subspace projectors. It contains
the all-target pure subspace. Therefore the any-failure effect is bounded by
I-tau_P, and

    Pr(any verification '-') <= E.                       (3)

This remains true for correlated source batches and system correlations. It
is deliberately **one-way**: a small rejection rate does not imply small E.
Also, rare negative flags do not make coherent output errors O(E); the general
complete-instrument replacement cost remains O(sqrt(E)).

## 4. Counted autonomous/gravitational implementation

For M=8 system readouts, use q=1,2,4 working/pump packets, q finite anchors,
and q degenerate test ancillas. Every ladder has maximum level N=512. The
working/pump guards are 8/q; each matching anchor targets the same packet.
The tests occur before the readouts, and all flags and anchors are retained.
Perfect target pairs pass with certainty and are unchanged by the tests.

The autonomous program has

    L = 1 + 7M + (q-1) + 2q = 59, 62, 68

bonds: emission, the seven-gate readout blocks, pump swaps, and two test gates
per pair. As before K=524288 clock sites, gamma=1/64, minimum source query
coordinate tau=16384, and the physical query window is
[1048576,2097152]. This is a finite window, not an eternal latch.

Assume each of the **2q** source/anchor marginal infidelities is at most 1e-8.
Write B for the autonomous noncompletion bound and epsilon_blk for the sum of
ideal finite-packet block errors. With independent unknown input, the complete
instrument error relative to the intended record instrument is at most

    B + (1-B) (epsilon_blk + sqrt(E)).                     (4)

The prepared clock is independent of the source/system batch, as in the base
model; its completion probability is independent of that batch.
For arbitrary initially correlated states replace sqrt(E) by delta_dec, and
compare with the actual R marginal. For uniform CPTP initialization add the
separate delta_sys if comparing with M_0. Bounds can always be capped at 1.
Verification failure and pending-clock labels are explicitly part of the
comparison; they are not postselected away.

| q | L | E | sqrt(E) | B | Complete error bound (4) |
|---:|---:|---:|---:|---:|---:|
| 1 | 59 | 2e-8 | .000141421 | .000261553 | .006685629 |
| 2 | 62 | 4e-8 | .000200000 | .000303145 | .003545759 |
| 4 | 68 | 8e-8 | .000282843 | .000399105 | .002179258 |

The state-correlated bounds add (1-B)E (or conservatively E) to the last column. The combined probability
of a pending clock or negative verification flag is at most B+(1-B)E;
this is not the same quantity as full quantum instrument error.

All anchors are gravitating matter. The enlarged single common family uses
omega_g=8192, Lambda=-4 omega_g^2/3, radial level zero, scalar band [.05,.25],
and fixed source excitation energy E_c=10985.32217170509. With omega=.1,

    H_f,min = E_c - 2 gamma - M omega,
    H_f,max = E_c + 2 gamma + 2 omega (2q) N + M omega.

Every expanded free-energy eigenvalue lies in the same radial-zero scalar band;
the common conservative margin is greater than 427.66. The verifier checks
inverse roots at both clock edges and system-energy extremes, positive flux
Jacobian, and the same Friedrichs/physical-root prescription as the prior
construction. Since every program gate commutes with this expanded H_f, the
dressed constraint is unitarily conjugate to its free form. This is the existing
homogeneous constrained model, not a new local constraint-algebra proof.

Ideal target reference-plus-anchor mean energies are 102.4, 204.8 and 409.6.
The actual imperfect-source means need not equal these: bounded ladder energies
and local trace distance give total deviations at most .02048, .04096 and
.08192 respectively. The gravitational window uses the whole spectrum, not
these target means.
Used anchors remain in the Hilbert space. The physical root-space dimension is

    K * 2^(8M+q) * (N+1)^(2q).

Large resource rows are analytic estimates, not dense simulations of these
spaces. The low-dimensional density matrices, circuits, records, and distances
are checked explicitly. This implementation costs more than omitting anchors;
it is not an optimality or free-certification claim. Initial blank flags,
controller preparation, and gate accuracy retain the earlier model assumptions;
the new infidelity theorem concerns the declared source/anchor batch.

## 5. Reproducibility and remaining direct time problem

Run:

    python verification/correlated_pump_certification.py
    python -m verification.correlated_pump_certification

The deterministic output is
[correlated_pump_certification.json](verification/correlated_pump_certification.json).
It includes decoupling witnesses, a uniform CPTP initializer, explicit correlated
pump readout distributions, a complete two-branch finite-anchor circuit, and
three expanded gravity/source budgets. Numerical checks supplement the proofs;
they are not interval certificates or experimental data.

The advance is a single complete-instrument statement robust to imperfect,
correlated finite resources. Near-pure marginal targets replace an independence
postulate, while the input-preparation and verification qualifications are made
explicit. No consciousness constitution or zero-residue derivation follows from
this conditional theorem.

Source fidelities still require a preparation model or a sampling protocol with
stated statistical assumptions; swap agreement cannot supply them unaided.
Rather than indefinitely extending the ancillary-hardware chain, the next direct
problem-of-time target is **spatial constraint consistency**: localize a reference/
record coupling and test Hamiltonian–diffeomorphism constraint closure. The
homogeneous clock's successful relational evolution cannot by itself establish
refoliation consistency or anomaly-free local quantum gravity.
