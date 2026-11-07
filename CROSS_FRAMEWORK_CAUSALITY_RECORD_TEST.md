# A cross-framework test: a cutoff can fabricate a causal record

## Finding

The preceding detector calculations used a small cosine-mode cutoff. That cutoff can destroy spatial locality even when the intended continuum fields are local. In an explicit test using the **same kind of `n=0,...,4` cosine regulator**, two nominally disjoint spatial regions give different recorded probabilities depending on the order of a source operation and a readout. The discrepancy is a regulator artifact, not physical superluminal signalling.

For the specified preparation, source and noisy two-bit record, the total-variation distance between the two orderings is **0.04960**. The effect shrinks as the cutoff is refined and vanishes in the local continuum limit. A sine-inclusive control also shows the artifact, so it is not explained solely by omitting sine modes. The measured source energy changes with the cutoff and is included below.

This result links our quantum instruments, operational causal relations, field-theory locality and regulator refinement in one example. The cutoff/locality problem is established prior work, not a discovery here: see [Martín-Martínez on causality and UV cutoffs](https://arxiv.org/abs/1509.07864) and [the nonperturbative cavity-detector study](https://arxiv.org/abs/1212.1973). We have applied that issue to this repository's chosen regulator and records; research priority is not claimed. It does **not** calculate the error of the earlier 71.67% detector, because that was a different, globally averaged readout and a different experiment. Nor does it test nonlinear gravitational refoliation. Its consequence is sharper: **we cannot claim local causal or foliation consistency from the earlier mode/time-step convergence alone.**

## 1. Use existing bridges without identifying unlike objects

The [framework-overlap construction](research/framework_overlap/REPORT.md) distinguishes channels, local algebras, causal events and compatible observable contexts; its CP pullback is not generally multiplicative. [Dynamical locality](research/dynamical_locality/REPORT.md) checks causal transport in a specified finite circuit. [Causal record lineage](CAUSAL_RECORD_LINEAGE.md) defines causal transport through intervention-dependent output distinguishability. The [cross-framework gravity note](CROSS_FRAMEWORK_GRAVITY_CONSTRAINTS.md) adds the separate requirement of a gravitational deformation algebra. The [energy tradeoff](FIELD_READOUT_ENERGY_TRADEOFF.md) gives a complete regulated quantum readout but not a local continuum net or controlled gravity.

These do not become the same object just because they can be drawn as ordered structures:

- an intervention channel and its outcome instrument are operations;
- a local net assigns algebras to regions;
- an operational causal edge records a change in accessible outcome statistics under an intervention;
- a compatible context consists of commuting observables;
- gravitational deformations act on physical states and relational events, with a constraint algebra and possible gauge identification.

The test below asks whether **one declared pair of operations** has compatible answers under the first four descriptions. The fifth—full gravity—remains a separate gate.

## 2. The necessary locality-to-record condition

In a local quantum field theory on a supplied spacetime, let A and B be spacelike separated. Let a nonselective A-instrument have local Kraus operators `K_a` satisfying `sum_a K_a^* K_a=I`, and let `E_B` be any B effect commuting with them. Then

    sum_a K_a^* E_B K_a = E_B,

so the unconditioned B statistics are independent of whether the A instrument is applied. The same conclusion holds for a local unitary source. In an algebraic setting one must use the relevant normal maps, domains and locality assumptions; this finite-Kraus identity is not a construction of arbitrary physical local instruments.

Thus a candidate claiming a local QFT limit cannot consistently report all of the following at once: A and B are spacelike, A and B are genuinely local, the source operation is nonselective, and B's unconditioned statistics change. If a finite regulator gives such a change, it must be shown to vanish with refinement or be accounted for in the intended notion of locality. [Fewster and Verch](https://arxiv.org/abs/1810.06512) provide an established covariant field/probe measurement framework on specified spacetimes; we do not rederive their full results here.

This is no-signalling, not a claim that conditioning on an A outcome cannot update B's statistics. Nor does equality for disjoint operations prove a gravitational hypersurface-deformation algebra.

## 3. A concrete test of the actual cutoff strategy

Take the normalized one-dimensional transverse collective sector of the preceding mode regulator on a circle `0<=z<2pi`, at the chosen slice `a=1`. It is a reduction of the three-dimensional model, not a full 3+1 local field net. Use real canonical modes

    phi_N(z) = (1/sqrt(2pi)) [q_0 + sqrt(2) sum_(n=1)^N q_n cos(nz)],
    pi_N(z)  = (1/sqrt(2pi)) [p_0 + sqrt(2) sum_(n=1)^N p_n cos(nz)],
    [q_n,p_m]=i delta_nm.

The source interval is centered at 0 and the readout interval at `y=pi/2`. Let f and h be normalized triangular functions of half-width `d=0.4`, with supports `[-d,d]` and `[y-d,y+d]` modulo `2pi`:

    f(z) = (d-|z|)/d² on |z|<=d, zero otherwise,
    h(z) = f(z-y).

The supports are disjoint, with positive separation; their transverse sheet extensions are spacelike separated on the same supplied slice. Triangular smears are H1/L2 rather than smooth test functions. They can be approximated by smooth compactly supported functions inside slightly enlarged, still-disjoint intervals; the Fourier/Hilbert-space calculation below is for the declared triangular functions.

Define `P_f=integral f pi_N`, `Q_h=integral h phi_N`. The source chooses `s=±1` with equal prior and applies

    U_s = exp(-i s g P_f),     g=1.

Take the same kind of Gaussian mode preparation used previously: zero-mode `Var(q_0)=1, Var(p_0)=1/4` and nonzero-mode `Var(q_n)=1/(2n), Var(p_n)=n/2`, with no q–p covariances. This is a prescribed state, including a normalizable Gaussian zero mode, not a selected vacuum of full quantum gravity.

Let

    w_n = sinc²(n d/2),
    kappa_N = [1+2 sum_(n=1)^N w_n² cos(n y)]/(2pi),
    V_N = [1+sum_(n=1)^N w_n² cos²(n y)/n]/(2pi).

Then `[Q_h,P_f]=i kappa_N` and the source shifts the readout mean by `s g kappa_N`, with variance `V_N`. At N=4:

    kappa_4 = 0.07900678,       V_4 = 0.25636414.

The finite-mode operators are **not genuinely localized** in the nominal intervals: projection onto finitely many cosine modes produces spatial tails. Thus noncommutation does not violate causality; it falsifies the proposed localization of those projected operators.

## 4. Complete recorded-outcome comparison

Read the sign of Q_h, write the result to two ideal neutral memory bits, then independently flip each bit with probability 0.1, as in [the prior complete instrument](RELATIONAL_CALIBRATION_AND_READOUT.md). The memory gate and noise are stipulated; no claim is made that they have local gravitating hardware.

For the plus source, compare source-then-readout with readout-then-source. The latter readout has the original centered Gaussian statistics. The four recorded probabilities are:

| order | 00 | 01 | 10 | 11 |
|---|---:|---:|---:|---:|
| source, then readout | 0.45959938 | 0.09 | 0.09 | 0.36040062 |
| readout, then source | 0.41 | 0.09 | 0.09 | 0.41 |

Their total-variation distance is `0.04959938`. If one instead asks which of `s=±1` was chosen, the two records have total-variation distance `0.09919876` and equal-prior guessing success `0.54959938` in this regulated model. This is an operational transport witness of a **cutoff-induced** dependency; it is not evidence for an actual causal link between the intended disjoint continuum regions.

Adding sine modes `sin(nz)` at the same cutoff makes the canonical truncated space less restricted. For this symmetric source the commutator overlap remains the same, while the readout variance changes; the corresponding two-bit ordering discrepancy is still `0.03738093`. Therefore the effect is not merely caused by discarding sine modes. Neither variant implements exact localization at finite N.

## 5. Refinement and energy: both must be tracked

The same source shifts the retained field's q coefficients. Relative to the unshifted Gaussian, its free-field energy increase at `a=1` is

    Delta E_N = g²/(2pi) sum_(n=1)^N n² w_n².

These are energy units of the normalized one-dimensional sector; they must not be compared directly to the earlier 3+1 background total without a normalization map. Instantaneous source/control and memory-preparation costs are additional and unmodeled. The source's continuum field-energy increment is finite, `g²/d³=15.625`.

| N | `kappa_N` | two-record ordering TV | `Delta E_N` |
|---:|---:|---:|---:|
| 4 | 0.07900678 | 0.04959938 | 3.49663 |
| 8 | 0.01165340 | 0.00716970 | 11.04268 |
| 16 | -0.00001510 | 0.00000928 | 13.37043 |
| 32 | -0.00000106 | 0.00000065 | 14.45518 |
| 256 | 0.000000016 | 0.0000000098 | 15.47768 |
| continuum | 0 | 0 | 15.625 |

For the even cosine sector the continuum equal-time kernel is the identity on even functions; the even extension of h has support around `±y`, still disjoint from f. Thus the limiting overlap is zero. In the full sine-plus-cosine sector it is simply the ordinary disjoint-support pairing. Using `|w_n| <= 4/(n² d²)` gives the explicit but conservative tail bounds

    |kappa_N| <= 16/(3 pi d^4 N^3),
    |Delta E_infinity-Delta E_N| <= 8 g²/(pi d^4 N).

They are deliberately loose for small N. The residual is not monotone: accidental cancellation at one cutoff does not itself certify convergence. More importantly, refining the cutoff changes the prepared source's energy and spatial resolution. A convergence comparison must hold the *physical smear and operation* fixed and track its stress-energy, rather than silently holding a few mode coefficients fixed.

## 6. What the combined constraints actually say

1. **Operational channel / causality:** at N=4 the declared procedure gives a nonzero intervention-to-record distinguishability. The causal relation is derived from the instrument, not from a drawn graph. Because the projected source has nonlocal tails, this does not make the continuum regions causally connected.
2. **Local algebra:** the intended disjoint continuum Weyl operations commute; the finite projected source and readout do not. The continuum no-signalling conclusion assumes actual local operations and complete nonselective outcomes.
3. **Contexts:** source and readout operators cannot be placed in a single commuting context at N=4 as though they were local disjoint observables. In the disjoint-support continuum limit the relevant Weyl algebras commute. A context poset is still not the causal-event poset.
4. **Energy/backreaction:** the source field energy approaches a finite value, but the reference, source switching and record energy remain unpriced. No fixed-background energy ratio is by itself a GR error bound. Previous successful instrument probabilities do not imply a self-consistent geometry.
5. **Refoliation and clocks:** comparing these two operational orderings is a useful *necessary locality control*, not a comparison of two solutions of the gravitational constraint algebra. A relational clock, physical localization and endpoint matching must be supplied for that stronger test; a fixed lattice or circuit order is not time for the absolute.
6. **Geometry reconstruction:** causal dependence must be separated from regulator leakage before using an event graph to infer order or geometry. Order alone still lacks volume and metric information; this example does not derive spacetime from a causal set.
7. **Experience and actuality:** neither causal records nor their consistency with geometry identify an experiencer, show why experience exists, or prove the user's desired necessary, timeless absolute. Those are separate obligations; this mathematical test does not settle them.

## 7. Reproduce and next gate

Run [verification/cross_framework_causal_cutoff.py](verification/cross_framework_causal_cutoff.py). [The output](verification/cross_framework_causal_cutoff.json) evaluates the finite sums, both cosine-only and sine-inclusive controls, all recorded outcome probabilities, and the analytic tail bounds. Its finite floating-point checks are not a proof of full QFT locality; the disjoint-support and tail arguments provide the continuum statement.

The next test must build a **local** probe instrument with physically specified smearing and stress-energy, demonstrate convergence of its complete probabilities and causal leakage under refinement, and then couple the *same* clock, rods and probe to a gravitational constraint system. Only after relational events and boundary data are matched can two gravitational deformation paths be compared. This is a concrete joint test, not an assertion that the entire programme is solved.
