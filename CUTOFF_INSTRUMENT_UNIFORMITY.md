# A necessary intermediate step: what can converge uniformly?

**Subsequent restricted advance:** [the common-Fock-space continuum comparison](CONTINUUM_COMPLETE_INSTRUMENT_CONVERGENCE.md) establishes bounds for each complete ordered instrument under a different normal-ordered oscillator-energy constraint and zero-mode regulator. It does not establish the original kinetic-only continuum claim or a physical probe; this note retains its original fixed-cutoff scope.

This note advances L3 of the [dependency register](DEPENDENCY_DRIVEN_RESEARCH_PLAN.md). It includes an energy-constrained bound on the complete ordered instruments at each fixed cutoff, **not** a cutoff-to-continuum instrument convergence proof. It reuses the fixed equal-slice 1D cosine-cutoff smears and the source/readout from the [earlier test](CROSS_FRAMEWORK_CAUSALITY_RECORD_TEST.md). The mathematical warning about infinite-dimensional diamond norm is established prior art, not a claimed discovery: see [Shirokov, energy-constrained diamond norms](https://arxiv.org/abs/1706.00361), especially its hypotheses on the energy operator. The specific application below spells out a gap in our proposed test.

## 1. Common finite-cutoff experiment

At cutoff N, let the canonical coordinates satisfy `[q_j,p_k]=i delta_jk`, and write the fixed readout as `Q_h=sum_j h_j q_j`, with `B_N=sum_j h_j²`. Let `Pi_f` be the corresponding smeared momentum source, with `[Q_h,Pi_f]=i kappa_N`. Apply `U=exp(-i g Pi_f)` either immediately before or immediately after a threshold measurement of `Q_h` at zero. The former shifts the readout mean by `g kappa_N`; the latter cannot change the already-recorded result. Retain both threshold-record bits and, for the full channel, the field output. The previous Gaussian preparation is only one admissible input.

The same normalized triangular smears of width parameter `d=.4` have

    B_N = [1 + 2 sum_{n=1}^N w_n² cos²(n pi/2)]/(2 pi) >= 1/(2 pi),
    kappa_N = [1 + 2 sum_{n=1}^N w_n² cos(n pi/2)]/(2 pi),
    |kappa_N| <= 16/(3 pi d^4 N^3).

Here `w_n=sinc²(nd/2)`. The lower bound uses the zero-mode contribution and assumes the same normalized cosine-mode coordinates and free kinetic Hamiltonian as the test. The continuum supports are disjoint, but truncated smears have global tails. This is not a comparison of two gravitational slicings.

## 2. Counterexample: fixed-state agreement is not uniform

Suppose `g kappa_N != 0`. Prepare the collective coordinate `Q_h` as a Gaussian with mean `-g kappa_N/2` and variance `sigma²`; a normalized finite-mode Gaussian state with these properties exists. The before/after source ordering gives sign probabilities `Phi(±g kappa_N/(2 sigma))`, where `Phi` is the standard normal CDF. With ideal two-bit records, the total variation distance is

    TV_order = erf(|g kappa_N|/(2 sqrt(2) sigma)).

For any nonzero overlap, taking `sigma -> 0` makes TV approach 1. Because classical record readout is a postprocessing of the complete instrument output, the (unconstrained, unhalved) diamond distance between these two finite-N instrument channels is **2**, its maximal value. This statement concerns those two ordered channels for each N with nonzero overlap; it does not assert that every N has nonzero overlap. With the original independent bit flips `q=.1`, the corresponding two-bit TV is multiplied by `1-2q=.8`, so the same construction yields an unconstrained diamond-distance lower bound approaching `1.6` even with the specified noisy records. That is only a lower bound, not the exact full-channel distance.

Why does this not contradict the previous convergence? The adversarial input changes with N and has unbounded kinetic energy. Define `P_h=sum_j h_j p_j/B_N`, so `[Q_h,P_h]=i`. For `H_kin=(1/2) sum_j p_j²`, uncertainty and Cauchy–Schwarz imply

    <H_kin> >= B_N <P_h²>/2 >= B_N/(8 sigma²).

Choosing `sigma=|g kappa_N|/8` gives ideal-record TV `erf(2 sqrt(2)) = 0.9999366575` while this energy lower bound diverges as `kappa_N -> 0` (since `B_N >= 1/(2 pi)`). At N=4 the computed lower bound is about 834; at N=16 it is about `2.92e10`, in the model's dimensionless units. The [verifier](verification/cutoff_instrument_uniformity.py) and [output](verification/cutoff_instrument_uniformity.json) calculate a small sequence. These are analytic Gaussian formulas evaluated in floating point, not a test of physical implementability.

## 3. A genuinely stronger, but still partial, bound

Keep the original two independent bit flips with probability `q`, and allow **any Gaussian input state of the retained field modes** whose total retained kinetic energy obeys `<H_kin> <= E`. Means, squeezing, and inter-mode correlations may vary with N. The readout marginal is Gaussian. From the energy inequality above, `sigma² >= B_N/(8E)`. For any mean and threshold, the difference between the two threshold probabilities is at most the total variation between the two translated Gaussian distributions. Thus

    TV_order <= (1-2q) erf(|g kappa_N| sqrt(E/B_N))
             <= (1-2q) 2 sqrt(2E) |g| 16/(3 pi d^4 N^3),

for `E>0` and `0<=q<=1/2`. The first inequality concerns the **classical two-bit marginal**; it does not bound a retained quantum field, an ancilla, or arbitrary non-Gaussian inputs. It is not an energy-constrained diamond estimate.

For illustration, fixing `E=100`, `g=1`, `q=.1`, and target `TV<=1e-4` in the same units, the second inequality gives sufficient `N=247` (bound `9.958e-5`). Combining this *different and stronger state-class probability contract* with the previous **source energy error** tolerance `.1` still permits `N=995`, since the independent conservative source-energy cutoff is 995. The input energy and source-energy tail are distinct quantities and must not be added or interpreted as a full backreaction budget. This is not a minimum physical cutoff.

## 4. Complete finite-cutoff instruments: an all-state energy bound

There is a stronger result than the Gaussian record bound, while still stopping short of continuum convergence. Use an **ideal Lüders sign measurement**, followed by two classical memory bits independently flipped with probability `q`. Let `P_0=1_{Q_h>=0}`, `P_1=1-P_0`, and let `r_{ab|i}` be the probability for bits `a,b` given ideal result `i`. For an arbitrary input density operator, including correlations with a reference ancilla on which the operations act trivially, the four subnormalized field output maps are

    before: I^before_ab(rho) = sum_i r_ab|i P_i U rho U† P_i,
    after:  I^after_ab(rho)  = sum_i r_ab|i U P_i rho P_i U†,
    r_ab|0 = (1-q)^(2-a-b) q^(a+b),
    r_ab|1 = q^(2-a-b) (1-q)^(a+b).

Here `before` means the source comes before measurement. The sum over ab is trace preserving. Recording the pair gives a classical-quantum channel with the field retained. Define its unhalved energy-constrained diamond distance as the supremum of the output trace norm difference over all field-plus-ancilla states with field `<H_kin> <= E`; there is **no** restriction on the dimension of the reference ancilla. This is a fixed-N, two-ordered-channel comparison, not an invocation of a theorem about the continuum field's energy operator.

Conjugate both outputs by `U†` and ignore bit noise temporarily. The two ideal instruments are then defined by the two complementary projections `P_i` and `P'_i=U† P_i U`. Since `U† Q_h U=Q_h+g kappa_N`, their differences are `P_0-P'_0=±Pi_I` and `P_1-P'_1=∓Pi_I`, where `Pi_I` is the spectral projection of `Q_h` onto the interval between the two thresholds, of length `|g kappa_N|`.

For any purification `|psi>` including the reference, define isometries `V=sum_i |i> P_i` and `V'=sum_i |i> P'_i`. The trace distance between their outputs is at most `2 ||(V-V') psi|| = 2 sqrt(2 <Pi_I>)`. Dephasing the outcome register and then applying the two noisy bit channels cannot increase trace distance. For `P_h=sum h_j p_j/B_N`, the vector-valued one-dimensional Sobolev estimate for the probability density of `Q_h` gives

    <Pi_I> <= 2 |g kappa_N| sqrt(<P_h²>)
           <= 2 |g kappa_N| sqrt(2 E/B_N).

The first inequality follows by integrating the derivative of the squared Hilbert-space norm of the wavefunction in the `Q_h` coordinate, then applying Cauchy–Schwarz; the other modes and ancilla are carried as a vector-valued wavefunction. Finite kinetic energy gives the required weak derivative. The second inequality follows from `H_kin >= B_N P_h²/2`. Therefore, for all field inputs including arbitrary non-Gaussians and arbitrary reference entanglement,

    ||I^before_N - I^after_N||_{diamond,E}
      <= min{2, 4 sqrt(|g kappa_N| sqrt(2 E/B_N))}
      <= min{2, 4 sqrt(|g| [16/(3 pi d^4 N^3)] sqrt(4 pi E))}.

The norm includes both record bits and the **complete retained field output**, including subnormalized selective outputs. Each outcome's subnormalized difference and the nonselective output difference are separately bounded by this same quantity by postprocessing. A normalized conditional state is not controlled without a positive lower bound on its outcome probability. The estimate is deliberately conservative, scales as `N^(-3/2)`, and is a specialized application of standard analysis and channel estimates; no literature novelty is claimed.

**Illustration:** E=100 and unhalved diamond tolerance `.01` yield sufficient N=722 from the analytic tail. At N=995, the bound is `.00618`, while the independently specified source-energy tail is `.09998`, within `.1`. These tolerances are illustrative, not empirical standards. The [arithmetic/control verifier](verification/energy_constrained_instrument_bound.py) and [output](verification/energy_constrained_instrument_bound.json) check the bounds against sample Gaussian record distances, zero-difference controls in the companion verifier, and the cutoff arithmetic; the all-state proof is the argument above, not those numerical samples. The bound includes an ideal externally implemented threshold measurement and does not budget apparatus or switching energy.

## 5. Remaining micro-steps before L3 is closed

1. Embed the finite-mode field and both instruments into one explicitly defined continuum input/output setting. Relate the **same physical energy constraint** at different cutoffs; the present bound compares two orders at each N but does not compare either instrument with the continuum instrument.
2. Control the approximation of the smeared source unitary and the threshold effects, including tails, ancillas and post-states; examine the zero-mode and operator domains. Check applicability of cited energy-constrained theorems instead of assuming it from the name of the norm.
3. Establish a continuum bound for the four selective maps and their nonselective sum. Distinguish small subnormalized error from a normalized post-state bound, which may require a lower bound on outcome probability.
4. Verify exactly commuting and zero-coupling controls in the common setting; compare assumptions and rate with published channel and field-measurement results. Only then decide whether L3 has passed or must be reformulated.

Until these steps are complete, L4 remains blocked: this fixed-N comparison does not supply a local spacetime probe, a 3+1 result, a dynamical-gravity test, or a theory of experience.

The [OPH repository and cutoff bridge](OPH_REPOSITORY_AND_CUTOFF_BRIDGE.md) identifies a relevant finite complete-instrument calibration theorem and a conditional energy-truncation transfer. It also shows why the finite-rank energy-truncation premise fails for the kinetic-energy-only input class used here; it does not close L3.
