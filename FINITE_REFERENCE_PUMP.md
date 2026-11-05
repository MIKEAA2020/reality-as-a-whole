# A finite reference pump that transports, rather than erases, old correlations

## 1. Constructive result and its cost

The [shared-reference model](REUSED_REFERENCE_CLOCK.md) retained the reservoir's state updates, depletion and correlated records. Here replenishment is an **explicit finite unitary operation** inside the same gravitationally constrained program. A finite precharged pump supplies energy and phase coherence; after the operation its full state and old-record correlations remain in the model.

A complete exchange restores the working reference to its prepared state and decouples it from the old records **exactly**. The used state and its correlations move into the pump. A partial exchange generally does neither: it can restore part of the mean energy while introducing a phase bias and leaving quantum memory.

One source-driven finite clock executes readout blocks and pump gates without an external switching schedule. All pumps enter the free-energy conservation law, the finite apparatus spectrum and the gravitational constraint. This is not a cyclic generator of coherence, a free replacement channel, or a pump prepared from nothing.

The construction uses a finite supply of already-coherent pump packets. It is a baseline with explicit state transport and resource costs, not an optimal energy-only replenishment protocol. Initial pump preparation, regeneration, external extraction/reset and inhomogeneous gravity remain open.

## 2. The pump and the exact unitary

Keep H_Sj=omega X_Sj with omega=0.1 and the finite working reference

    H_B=2omega N_B, n_B=0,...,N.

Add an identical finite pump C,

    H_C=2omega N_C, n_C=0,...,N,
    tau_C=|b><b|.

The pump starts in the sine packet with the guard required for the next readout block. Its mean energy is omega N and maximum energy 2omega N. Its finite phase coherence and initial alignment are resources, not derived from the clock source excitation.

Let S_BC exchange the entire two ladder states. Then

    S_BC^2=I, [S_BC,H_B+H_C]=0,
    U_theta=cos(theta)I-i sin(theta)S_BC.

The operation is unitary and exactly energy conserving for every angle. A full exchange theta=pi/2 is SWAP up to a global phase. It will be a **fixed program-bond unitary**, not a pulse externally switched at a sharp epoch.

The identical gaps are a resonance assumption. An unknown initial pump phase offset changes the future measurement orientation; no absolute phase alignment is obtained for free. Because both ladders freely rotate with the same Hamiltonian, the programmed exchange is covariant: it restores the pump's freely evolved reference packet in the common interaction-picture comparison, without an omega T correction.

## 3. Full correlations retained: exact partial-pump formula

Let R denote all other systems, including old S outputs, records, untouched references and not-yet-measured systems. The used working reference can be arbitrarily correlated with them:

    sigma_BR, rho_R=Tr_B sigma_BR.

Initially C is independent in tau_C. With c=cos(theta), s=sin(theta), direct expansion and a partial trace over C give

    sigma'_BR = c^2 sigma_BR + s^2 tau_B tensor rho_R
                +i c s [sigma_BR,tau_B tensor I_R].

The commutator term is essential. A partial pump is not generally a classical mixture of 'leave used reference' and 'install fresh reference'. The old R marginal is unchanged for every theta because the physical unitary acts only on B,C. Conditioning on a later pump observation can of course change inferred conditional states; that is not unconditional erasure or signalling.

For a full exchange,

    sigma'_BCR=tau_B tensor sigma_CR,
    sigma'_BR=tau_B tensor rho_R.

The original B state has been relabelled C, including **all** correlations with R. Consequently

    I(B:R)_after=0,
    I(C:R)_after=I(B:R)_before,
    S(C)_after=S(B)_before.

These follow from the exact state identity, not from dropping the pump. Old record marginals and their conditional S-output instrument are preserved; their correlations with the used reference now reside in C.

The decoupling statement concerns B and the remaining systems after tracing C. The complete closed state is not claimed close to one with both B and C fresh. Reusing C later would bring back its stored state and correlations and requires a new analysis.

## 4. Partial replenishment can change the reference phase

For the real ground-input used state derived in the reuse report, mean-energy commutator contributions vanish. Then

    Delta<E_B>=sin^2(theta)[<H_C>_initial-<H_B>_initial].

This simple energy interpolation does **not** imply phase or correlation restoration. For N=12, after two ground-input readouts with their two-site guard:

    initial reference mean energy: 1.2,
    used reference mean energy:    1.0.

A half exchange theta=pi/4 raises it to 1.1, restoring half the lost energy. Its adjacent coherence is instead

    Tr(L_B rho'_B) approximately 0.95105652-0.07095107 i,

with phase bias about -0.07446 radians relative to the prepared reference. Before pumping that coherence was real. Thus an energy meter alone would miss a changed measurement orientation. The exact finite joint formula, not an energy-only reset rule, must determine future readouts.

Near full exchange, write alpha=pi/2-theta. For this real used-state example the remaining energy deficit is of order alpha^2, while the nonzero commutator produces a phase/correlation error of order alpha. An energy-only near-reset certificate can therefore miss the leading state error.

For arbitrary complex inputs individual energy changes also contain the coherent commutator contribution, while

    Delta<H_B>+Delta<H_C>=0

always holds. A hot used reference may transfer energy into the pump; 'pump depletion' is not a universal sign statement for all inputs.

### A uniform partial-pump certification

The exact formula gives, for arbitrary R,

    D(sigma'_BR,tau_B tensor rho_R)
        <=min(1,c^2+|cs|)=:delta_theta.

Use D(A,B)=||A-B||_1/2, state distance at most one, and ||[sigma,tau tensor I]||_1<=2. The same uniform bound controls the reset-channel half-diamond distance, including correlated inputs. It vanishes at full exchange and can be nontrivial close to full exchange.

After any future CPTP processing that does not recouple C, the reduced old-and-new output difference cannot increase. It is therefore valid to add delta_theta to a joint-history error budget. The bound is conservative, not an optimized partial-pump lifetime theorem. It is **not** an error bound for a full output in which the pump is falsely required to remain unchanged.

## 5. What an exact finite reset must spend

### Dimension and information

For a universal exact reset using a pure pump and no other changing auxiliary, the pump dimension must be at least the working-reference dimension. To see this, take R trivial and distinct orthogonal B inputs. A unitary resetting every B input to the same pure tau must send the orthogonal input information into orthogonal pump states. Thus

    dim(C)>=dim(B)=N+1.

The equal-size exchange attains this dimension requirement. This is not a universal minimum energy or heat theorem, and another changing auxiliary could share the storage cost.

Returning both B and every pump/auxiliary to fixed pure states while keeping all other outputs unchanged cannot implement a universal reset: it would map orthogonal inputs to the same output. The used information/correlations must remain somewhere, as C explicitly demonstrates here.

### Energy and coherence

For a completed block of g ground-input readouts, the working reference has lost g omega. Full exchange gives

    working reference gains g omega,
    pump loses g omega,
    pump retains the used-state correlations.

The pump is not catalytic. A second exchange without other operations merely returns the old used reference and correlations to B; it is not another independent refill. After further readouts, an already-used pump still carries a used state, not the original tau.

A universal coherent reset also cannot be obtained from energy-incoherent B and C states by a unitary commuting with H_B+H_C: global energy invariance is preserved and its reduced B state remains energy invariant, unlike tau. This is why the coherent initial pump must be counted. It does **not** prove that an energy-only pump can never help the restricted already-coherent used states; no such optimality claim is made.

For r precharged pumps, no refill and ground-input readouts whose unconditional marginal error is <=epsilon<1/2, the total reference energy budget implies

    number of readouts <= (r+1)N/(1-2epsilon).

This extends the previous mechanism-specific capacity law. It includes failures and counts all initially charged references; the source clock does not recharge their free-energy sector. It is not a capacity bound on arbitrary devices supplied with additional energy/coherence sources.

## 6. Old records preserved; future blocks genuinely fresh

Load r independent precharged pumps and use each once. Between readout blocks, apply a full exchange with the next pump and do not couple that used pump again in the completed program. The old systems/records remain unchanged; the working reference becomes tau independent of them and of all future S registers.

For blocks of g_j readouts, the completed reduced instrument is therefore exactly

    I_completed = tensor_product_j I_(g_j,tau),

where each block retains its own shared-reference correlations. This is a **factorization of channels**, not a claim of independent outcomes for entangled inputs. Input-generated quantum correlations remain. What is removed is memory of the *old reservoir state* in future blocks.

The statement follows from the actual joint exchange, not from inserting a fresh state by fiat. In the full model each used pump is still correlated with the corresponding old outputs. For a general input entangled across blocks it can also carry those inherited correlations; it is simply not recoupled to the working apparatus.

If each block has a diamond error bound epsilon_j, then

    error_completed <=min(1,sum_j epsilon_j).

With partial exchanges, add the appropriate sum of delta_theta bounds, capped at one. This follows by contractivity and telescoping of actual channels; a per-block error is not treated as an independent classical failure probability.

The verifier propagates both reservoir indices through two actual readouts and the exchange for all input matrix units. Full exchange agrees with the factorized channel to floating precision. No exchange and half exchange both show nonzero deviations and correlated wrong records. There is no reservoir trace/reset inserted in that propagation.

## 7. One autonomous finite source/clock program

Concatenate the readout blocks and explicit exchange gates in the finite source clock. For M total readouts and r pump gates,

    L=1+7M+r.

The source-emission bond is still the initial identity gate. The expanded free Hamiltonian is

    H_f=omega sum_(j=1)^M X_Sj
        +2omega(N_B+sum_(a=1)^r N_Ca).

Every lifted measurement, copy/flag gate and exchange commutes with H_f. With W_n the actual prefix products and Q=sum_n |n><n| tensor W_n,

    H=Q[(E_c I+gamma A_K) tensor I+I_clock tensor H_f]Q^dagger.

This is the actual autonomous Hamiltonian in the lapse action. Source amplitudes, exact charge conservation and the finite-chain proof remain valid; no externally timed pump pulse or ideal controller has been appended.

The final readout block's G flag certifies the entire completed program. All source/program/pump-pending branches are retained. For tau=gamma T_min, T_max=2T_min and the positive boundary cap epsilon_b,

    B_clock=[sqrt(L(L+1)(2L+1)/6)/tau+epsilon_b]^2,
    error_complete <=B_clock+(1-B_clock)error_completed.

L is recomputed with the extra pump gates. Finite-clock recurrences still forbid an eternal-latch claim. All guarantees concern a single final query after unmonitored evolution in the certified window; the pump alone preserving old records does not prevent the full finite clock from later reversing its program.

## 8. Pumps are matter in the gravitational constraint

Retain the conserved one-excitation source/clock sector, the declared radial Friedrichs ordering and scalar band [0.05,0.25]. The lapse constraint is C=H-A. The exact free charges now include **every** precharged pump:

    q=n_B+sum_a n_Ca+sum_j e_j,
    0<=q<=(r+1)N+M.

The exact apparatus energies are

    E_jq=E_c+2gamma cos[pi j/(K+1)]-M omega+2omega q.

Hence the full declared spectrum lies within

    E_c-2gamma-M omega <=H
        <=E_c+2gamma+2omega(r+1)N+M omega.

Use the same fixed gravitational window as the largest reuse example:

    omega_g=4096, Lambda=-4omega_g^2/3, radial level zero,
    E_c=E_gcenter-0.1*2048 approximately 5492.66108585,
    omega=0.1, gamma=1/64.

For M=8, N=512 and r=0,1,3, all energies fit with margin greater than 213.4 model units. E_c, gravity and all system gaps are fixed across the comparison. More pumps increase the real mean/maximal matter energy; none is subtracted as a harmless offset.

Atomic rigging again fixes scalar momenta by epsilon_0(p)=E_jq, with physical norm weighted by 1/|epsilon_0'(p)| before rescaling. The physical root dimension is

    K 2^(8M) (N+1)^(r+1).

All source/pump/reference states are normalizable in that physical norm, with gravitational correlations determined by the constraint. The full finite spectral inclusion needs no polar projection. The strong constrained-instrument lift from the finite-source report applies because the common spectral margin is positive. It is a mathematical compatibility result, not an unmodelled extraction Hamiltonian.

These are formal homogeneous resources, not observed cosmological parameters. Pump preparation, realistic stress localization and the inhomogeneous constraint algebra remain unsupplied.

## 9. Explicit replenishment budgets and a fair resource comparison

All rows use one working ladder with N=512, eight fixed-gap readouts, K=524288 source/clock positions and the same window [1048576,2097152]. Each packet is prepared once with guard equal to its planned readout-block length. The initial phase alignment is part of this resource specification.

| Precharged pumps r | Readouts per block | Initial total reference mean energy | Program length | Completed-instrument error upper | Complete-operation error upper |
|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 51.2 | 57 | 0.0062844 | 0.0065190 |
| 1 | 4 | 102.4 | 58 | 0.0030436 | 0.0032915 |
| 3 | 2 | 204.8 | 60 | 0.0014981 | 0.0017726 |

These comparisons keep the working ladder fixed and add counted coherent pumps. For all-ground inputs, every row loses total reference energy 0.8 to the eight S systems. Each used pump in the last row loses 0.2 when it restores the working reference; it also acquires the corresponding old correlations. The final working reference has undergone the last block and is itself used, not fresh.

This is not an energy-efficiency improvement theorem. At the same initial total reference mean energy 204.8, one large shared ladder N=2048 has the earlier completed-joint upper bound about 0.00037672, smaller than the four-packet scheme's bound. The exact GHZ parity witness also gives a larger error for the divided pump scheme on that particular input. Pumping buys exact block decoupling and replenishment of a fixed-size working ladder; it is not generally preferable to putting all coherence into one larger reference.

For the partial-pump example the half exchange restores half the mean energy but leaves nonzero cross-block memory. The full-exchange certificate is stronger: it restores the exact working-state packet and removes old-reference correlations from future blocks, while preserving them in the used pump.

## 10. Verification and the next direct time target

Run:

    python verification/finite_reference_pump.py
    python -m verification.finite_reference_pump

The verifier writes [finite_reference_pump.json](verification/finite_reference_pump.json). It checks the exact partial-pump formula on an entangled complex B,R state at four exchange angles (400 matrix entries), 2500 unitary column pairs and 2500 free-energy commutator entries, old-record marginals, energy conservation, double-exchange return and full correlation transport. It verifies a depleted-reference partial-refill example with an explicit phase bias. Actual two-readout propagation retaining both ladder indices checks 192 matrix-unit/outcome cases: full exchange factorization versus nonfactorizing no/partial exchange. Three large analytic budgets recompute source/program length, clock noncompletion, all pump energies and 36 gravitational inverse cases. Those large rows are bound calculations, not dense simulations or interval certificates.

**Supplied:** a finite energy-conserving pump interaction, exact correlation transport and decoupling, partial-reset bias and an error certificate, minimal pump dimension under declared universal-reset assumptions, complete multi-block records, finite-source programming and all added matter in the gravitational window. No pump is discarded from the closed model or restored by an unexplained replacement channel.

**Still open:** initial preparation and regeneration of the coherent pumps, an optimized energy-only or adaptive pump, external extraction/reset and noise, gravitational locality/domain justification, and phenomenal constitution. The construction consumes a finite supply of precharged coherence; it does not create a perpetual reference cycle.

The next direct time target is **pump-quality and correlation tolerance**: replace exact independent pump packets by finite imperfect/correlated source states, derive a complete record-instrument bound from their actual joint state, and identify what source certification is sufficient. Without that step, the exact fresh-block identity could conceal the next preparation assumption.
