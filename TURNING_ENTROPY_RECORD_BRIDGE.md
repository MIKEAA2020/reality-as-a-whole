# Turning clocks, entropy paths, and the need for a retained record

**Status:** an explicit connection between existing bounded constructions, not a solution of the problem of time, a direct analysis of Barontini's data, or a demonstrated novel research theorem. This is a prescribed toy trajectory. It relates the *form* of Barontini's path clock to the [periodic turning-clock atlas](TURNING_CLOCK_ATLAS.md) and the distinction between recorded and unrecorded histories in [RELATIONAL_INTERVENTIONS_AND_RECORDS.md](RELATIONAL_INTERVENTIONS_AND_RECORDS.md). The Barontini-specific constraints and observed-data limitations are in [COLD_ATOM_ENTROPIC_CLOCK_AUDIT.md](COLD_ATOM_ENTROPIC_CLOCK_AUDIT.md) and [COLD_ATOM_CLOCK_COMPARISON.md](COLD_ATOM_CLOCK_COMPARISON.md). A close prior-art audit, particularly [record-based internal time](https://arxiv.org/abs/2607.25307) and existing quantum clock switching, remains necessary before claiming novelty.

## 1. A common declared model

Use the clock atlas's periodic phase, but temporarily lift it to an ordered path with parameter θ≥0. Put

    q(θ)=cos θ,       S(θ)=S₀+a q(θ),       a>0.

Choose S₀>a if a nonnegative illustrative S is desired. S is an assigned scalar function here, **not** a reconstructed quantum or thermodynamic entropy. Following the *form* of Barontini's Eq. (3), choose units `σ/k_B=1` and define

    τ(θ) = integral from 0 to θ of (dS/dq) |dq|
         = a integral from 0 to θ |dq|.

The second equality uses this particular choice `dS/dq=a`. For the actual experiment, S, q, the coarse-graining, sampling and sign alignment must be obtained from the experimental prescription; the paper does not posit S=S₀+aq. In general the integrand need not be nonnegative solely from its definition.

In the underlying periodic constrained model of [TURNING_CLOCK_ATLAS.md](TURNING_CLOCK_ATLAS.md), θ mod 2π is a clock label, not an external universal time. The lift and its traversal order are extra path data; they are not already a quantum winding-counter instrument.

## 2. Exact chart-to-path map

For integer n≥0 and `u=θ−2πn` in `[0,2π)`, let `q=cos u`. On the decreasing and increasing legs respectively,

    0≤u≤π:      τ=4an+a(1−q),
    π≤u<2π:     τ=4an+a(3+q).

The formulas agree at the turning point, and at a full cycle the next winding value gives the same endpoint. Thus a local chart consisting of q, the leg orientation and a winding record n determines τ on this prescribed path. Direction alone handles the two legs but not repeated cycles.

For instance, `θ=π/3` and `θ=2π+π/3` have identical q=1/2 and the same leg orientation, yet

    τ(2π+π/3) − τ(π/3) = 4a.

The periodic system frames in the existing atlas also repeat at these two θ values. Therefore no single-valued deterministic function of the repeated periodic clock reading, entropy proxy and orientation alone can reproduce both τ values. It needs at least a retained winding/history distinction or else must identify these occurrences. This is an explicit instance of the fiber condition already stated in the cold-atom audit, not a claim that all relational clocks are history dependent.

The [finite-path verification](verification/turning_entropy_bridge.py) numerically checks 12,000 steps, including turning points and two cycles. At a=2, the two equal q readings have τ≈1 and τ≈9. The maximum discrepancy between the piecewise formula and this aligned discrete variation is below `7×10⁻¹⁴`. The script verifies the prescribed example, not physical implementation.

## 3. A finite record lower bound under stated assumptions

Fix q and the leg orientation at the same phase in `N+1` consecutive cycles n=0,...,N. Suppose a deterministic decoder gets only that repeated local reading and a classical memory label, and must approximate all corresponding τ values with absolute error `<2a`. The τ values are separated by at least `4a`. Two different cycles cannot share a label, since the decoder would return the same output for both and would have errors totaling at least `4a`. At least N+1 distinct labels are therefore needed; a binary memory capacity of at least `ceil(log₂(N+1))` bits suffices to distinguish the labels as a coding upper bound.

This is elementary counting conditional on these precise requirements. It does **not** prove a thermodynamic cost, an optimal autonomous quantum counter, an unlimited experiment or a universal arrow of time. A continuous-valued physical register, access to additional correlations or a restricted observational target changes the resource accounting. A countable memory alone does not show how to prepare, update, preserve, read out or reset it.

## 4. What each part lends the others

- **Turning atlas → entropic path:** regular local charts show why a recurring instantaneous reading needs orientation and why the apparent singularity at a turn need not be physical.
- **Entropic path → atlas:** an accumulated path reading supplies a concrete candidate for distinguishing repeated turns, but forces winding/history resources to be explicit.
- **Recorded instruments → path:** persistent internal records are a mathematical architecture to investigate for those resources. Existing unitary-history results assume specified interactions and fresh memories; they do not automatically implement this particular accumulator.
- **Cold-atom paper and data → benchmark:** a real coarse-grained, measured path provides an operational target. The recorded τ, laboratory timing, whole-cloud estimator, uncertainty and sampling must be carried into the comparison; this toy formula must not be fitted or claimed as a result from those data.
- **Finite-perspective project → separate question:** internal temporal order is a physical/operational relation. It does not by itself establish qualitative passage, a subject, or a relation to universal consciousness.

## 5. A classical interface to recollapsing gravity

The [Einstein–scalar recollapse model](RECOLLAPSING_GRAVITATIONAL_CLOCK.md) gives, for a specified orbit with `k>0`, `x(T)=ln(k/μ)−ln cosh(T−T*)`. Define the dimensionless normalized volume along **that orbit** as

    q_g(T)=2 exp(x(T))/(k/μ)−1 = 2 sech(T−T*)−1.

It increases from −1 toward +1 on the expanding branch, then decreases toward −1 on the contracting branch. Each interior q_g value is visited twice. If we *add as an illustrative assumption* `S=S₀+a q_g` and use the same path rule starting at the expanding asymptote, then

    expanding:    τ=a(1+q_g),
    contracting:  τ=a(3−q_g).

The two branch readings for the same q_g differ by `2a(1−q_g)`, except at the shared turn. This is a classical change-of-variables example relating three documents: neither the entropy law nor the operational clock instrument follows from Einstein–scalar dynamics. Unlike the periodic toy model, this recollapsing model has one turn and approaches its endpoints only asymptotically; it does not establish repeated cycles or a winding counter. The normalization also depends on the orbit parameter k. A quantum version needs a specified operator/POVM, spectral domains, state dependence and detector backreaction; no quantum frame equivalence is claimed here.

## 6. Next discriminating construction

**Finite continuation:** [FINITE_TURNING_COUNTER_INSTRUMENT.md](FINITE_TURNING_COUNTER_INSTRUMENT.md) now supplies a bounded history constraint, prepared cycle counter, overflow flag, noisy complete readout and backaction witness. Its 13-vertex clock already supplies unwrapped ordering and the update schedule; it is not an autonomous origin of chronology, the Barontini apparatus or a gravitational model.

Extend this finite construction to a physically justified accumulator **inside one constrained history**, with clock/accumulator states, preparation, conditional instrument, error, saturation and record backaction. Compare its joint record statistics with the ideal chart/path formula, first on a finite horizon and then against the measured clock data only where the required entropy and chronology inputs are actually available. Include alternative clocks and the same anchored events. Prove a bounded operational equivalence or produce a counterexample; compare with existing record-clock work before claiming novelty. Extending the classical interface above to the quantum recollapsing Einstein–scalar model and then inhomogeneous constraints is an additional, uncompleted step.
