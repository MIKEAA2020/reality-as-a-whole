# From clock dynamics to readable classical ticks

## Result and scope

Wadhia et al., **“Entropic Costs of Extracting Classical Ticks from a Quantum Clock,” Physical Review Letters 135, 200407 (2025)**, directly concerns a missing layer of our clock programme: extracting a usable event record, rather than only producing a microscopic clock–pointer correlation.

- [Published paper](https://journals.aps.org/prl/pdf/10.1103/5rtj-djfk)
- [Supplement](https://journals.aps.org/prl/supplemental/10.1103/5rtj-djfk/SM_%281%29.pdf)
- [Authors' public code/data](https://github.com/aspects-quantum/equilibrium-clock-public), inspected at `3738ca280fff50a8e3a1d02cea26d3e143f234a7` (2025-03-08).

The entire main paper and supplement were read. The bounded source check below is **not** a reproduction of the raw-data processing, uncertainty analysis or RF/DC dissipation figures. The pinned public-code version predates publication; source-level questions about it must not automatically be attributed to the final published analysis.

**Constructive addition here:** an exactly unbiased finite-time departure-event estimator, its exact variance law, an equilibrium example with an integer record accumulator, an ideal missed-event calculation, and a readout-error composition bound for our earlier quantum instruments. The underlying counting-process mathematics is standard; this is an explicit bridge in this programme, not a claim of priority or a new fundamental law.

This stays within the operational clock/record part of **M0**. It neither solves gravitational refoliation nor derives the parameter of a Markov semigroup from a timeless constraint. It does not establish a physical–phenomenal identity or the complete constitution of reality.

## 1. What the experiment establishes

The clockwork is a Ge/SiGe double quantum dot at approximately 180 mK. A small effective state space, `0, L, R`, describes the resolved charge transitions. In the measured regime coherence decays faster than the readout resolves it, so the time estimator uses a **classical Markov description of a quantum device**, not long-lived coherent clock oscillations. Charge sensing and RF reflectometry supply two readout methods.

Two distinct things can be counted:

1. A signed transport current: forward charge-transfer cycles minus reverse cycles.
2. The ordered state-jump record, including activity that persists at detailed balance.

At equilibrium, the first has no mean drift and cannot be normalized into a clock by dividing by that drift. The second can still estimate elapsed time. The paper's asymptotic precision is

    S = lim[t -> infinity] E[Theta(t)]^2 / (t Var[Theta(t)]),

with units inverse seconds. For the state-sequence estimator,

    S_opt = 1 / sum_i (pi_i / Gamma_i),

where pi is the stationary distribution and Gamma_i is the total escape rate from state i. This remains positive at detailed balance although the **clockwork's stationary entropy production is zero**.

There is no contradiction with the usual steady-current thermodynamic uncertainty relation,

    S_net <= dot(Sigma_clockwork) / (2 k_B).

An activity/full-record estimator is not the antisymmetric current to which that relation applies. Replacing clockwork entropy by total apparatus entropy does not, by itself, prove a new universal uncertainty relation for arbitrary estimators or quantum clocks. The supplement explicitly leaves the general quantum optimal estimator open.

The experiment finds that extracting the ticks dominates the microscopic clockwork's cost by many orders of magnitude. Figure 1 gives illustrative sensor costs of order 10^9–10^11 k_B per tick, against a largest microscopic charge-cycle cost of order 60 k_B; the authors report a nine-order separation in their comparison. **These are apparatus/operating-point results, not a universal minimum cost per tick.** A charge cycle, an individual resolved jump and a weighted estimator increment are not interchangeable tick definitions.

Important accounting qualifications:

- Supplement A uses a **baseline-subtracted DC signal**, proportional to `V_cs |I_cs - <I_cs>|`. This is not the complete electrical power `V_cs I_cs` of an operating sensor, let alone the wall-plug energy of its laboratory.
- The RF budget concerns the device-level incoming/reflected signal, with wiring-loss corrections. Amplification, refrigeration, processing and memory are not thereby given a complete thermodynamic budget.
- RF readout has a lower reported cost than DC readout; a single universal reduction factor is not inferred here.
- Finite bandwidth, classification and dwell-time filters affect which jumps become records. The supplement discusses missed-transition biases, rate variation/drift and limitations of white-noise error estimates.
- At low signal-to-noise ratio, counted readout noise can turn the purported device clock into a clock supplied by the analyser's sampling process. A plausible-looking tick sequence alone is not enough.

## 2. Finite-time event clock: exact martingale identity

Let X_t be a finite-state continuous-time Markov chain. Use a **column generator** Q: q_ji >= 0 is the rate i -> j, and

    Gamma_i = sum_{j != i} q_ji = -q_ii > 0.

Assume the actual departures and their source states are observed, and all rates are calibrated and fixed. Define

    Theta_dep(t) = sum_{jumps tau <= t} 1 / Gamma_[X_(tau-)].

This needs the ordered state events and calibrated rates, **not a timestamp attached to every tick**. The reference t is used to specify and assess the model; it has not been independently derived or eliminated.

Conditional on X_t=i, the event rate is Gamma_i and the increment is 1/Gamma_i. Therefore the predictable drift is exactly one:

    M_t = Theta_dep(t) - t is a square-integrable martingale,
    E[Theta_dep(t)] = t,
    Var[Theta_dep(t)] = E[integral_0^t ds / Gamma_[X_s]].

The last identity follows from the predictable quadratic variation of M, not from assuming independent successive waiting times with identical distributions. It is valid for any initial state distribution. In particular, if the chain starts in pi,

    Var[Theta_dep(t)] = t sum_i pi_i / Gamma_i,
    E[Theta_dep(t)]^2 / (t Var[Theta_dep(t)])
        = 1 / sum_i pi_i / Gamma_i

for **every t>0**, not merely asymptotically. Chebyshev's inequality gives the explicit stationary finite-time relative-error budget

    Pr(|Theta_dep(t)/t - 1| >= r) <= min(1, 1 / (S_activity r^2 t)).

This is a conservative statistical bound, separate from instrument/readout errors. For an arbitrary initial distribution,

    t / Gamma_max <= Var[Theta_dep(t)] <= t / Gamma_min.

The paper's visited-state convention includes the initial and final visit:

    Theta_vis(t) = sum_{k=0}^{m(t)} 1 / Gamma_[s_k]
                = Theta_dep(t) + 1 / Gamma_[X_t].

Thus the two differ by a bounded endpoint term, and have the same long-time precision in an irreducible finite chain. Theta_vis is not exactly unbiased at finite time: its endpoint contribution is positive. This is an endpoint convention, not a failure of the paper's asymptotic result. The departure convention supplies a useful exact finite-time version.

Nothing here proves unrestricted finite-time or quantum optimality. The agreement with the paper's S_opt is within its calibrated classical state-sequence setting.

## 3. Explicit equilibrium clock and bounded record register

Choose escape rates `(2,3,6)` per second and equal probabilities of jumping from each state to either other state. Then

    Q = [ -2,    3/2,   3 ]
        [  1,     -3,   3 ]
        [  1,    3/2,  -6 ],

    pi = (1/2, 1/3, 1/6).

Every stationary edge flux equals its reverse flux; detailed balance holds exactly. Consequently the stationary clockwork path entropy production and signed transport drift are both zero. Nevertheless,

    E[Theta_dep(t)] = t,
    Var[Theta_dep(t)] = (7/18 seconds) t,
    S_activity = 18/7 per second > 0.

An integer register A represents this estimator in units delta=1/6 second. On a departure from states `0,1,2`, respectively, increment A by `3,2,1`. Then Theta_dep=A/6 seconds. Computing this estimator does **not** require keeping the whole event history: current source-state information and the weighted accumulator suffice.

For a run with at most N departures, `0 <= A <= 3N`, so `ceil(log2(3N+1))` register bits suffice. The increment controlled by a retained state label can be implemented as a permutation of a cyclic register of capacity `3N+1`, with inverse subtraction; no allowed path of at most N events wraps. This links to our [reversible path accumulator](OPERATIONAL_PATH_ACCUMULATOR.md).

This is an **event-count-bounded** register claim, not a hard capacity guarantee at fixed duration: a continuous-time jump process has an unbounded possible number of events in any nonzero interval. A fixed-duration implementation needs an overflow probability budget or expandable storage. Uniformization supplies one: the actual event count is stochastically dominated by a Poisson variable of mean mu=Gamma_max*t. If K=N+1>mu, then

    Pr(register exceeds the N-event provision by time t)
        <= Pr(Poisson(mu) >= K)
        <= exp[-mu + K (1 + log(mu/K))].

For this illustrative clock, t=10 seconds and N=99 give a register capacity of 298 values (nine bits suffice) and an overflow upper bound about 1.54e-5. This is a supplied finite-horizon probabilistic capacity guarantee, not permanent storage or a bound valid for indefinitely repeated runs.

Also, reversible arithmetic does not by itself supply state detection, a permanent classical record, prepared blank memory, readout amplification, reset or a physical engine for the stochastic transitions.

The script checks all **1,533 admissible state paths with zero through eight jumps**, the endpoint identity, exact detailed balance and register arithmetic. This example is illustrative and is not fitted to the double-dot device.

## 4. What missed events do—and do not—permit us to claim

As an ideal observation model, suppose every physical jump is independently retained with known efficiency eta, and a retained event carries its **correct source-state label**. Then

    Theta_eta(t) = sum_{retained jumps} 1 / (eta Gamma_source),
    E[Theta_eta(t)] = t,
    Var[Theta_eta(t)] = E[integral_0^t ds / (eta Gamma_[X_s])].

In stationarity, `S_eta = eta S_activity`. Without the efficiency correction, the estimated mean is eta*t, not t.

This result follows from marked point-process thinning. It does **not** describe general finite-bandwidth missed transitions: if unobserved transitions also make the inferred source state wrong, the required labels are unavailable. A real classification/filtering pipeline needs its own observation model. Independent spurious clicks also cannot simply be counted as physical clock activity; they alter the drift and may import the detector's own reference clock.

## 5. Bounded check against the authors' processed matrices

The lossless, small archive [processed_sample.json](verification/sources/wadhia_2025/processed_sample.json) contains the supplied MIT license, measurement metadata, and central rate/error matrices for `B-V-K3` and `PCA--K3` in folder `data/+0.005 bias/5187/`. Each payload has its original Git blob SHA-1, SHA-256 and byte length. The verifier checks both hashes and uses a strict non-pickle decoder for the small float arrays. It never executes the external code.

Only off-diagonal central rates are used to define the working generator; each diagonal is rebuilt as minus their sum. The largest corrections are 6e-16 and 2e-15 per second, respectively. Stationarity and the event-clock identities are then checked with exact rational arithmetic on the archived decimal float values.

| Processed fit | Activity precision S_opt (s^-1) | Signed current precision (s^-1) |
|---|---:|---:|
| `B-V-K3` | 9.122877524 | 0.0003764647794 |
| `PCA--K3` | 9.574197869 | 0.001867019750 |

The current variance is obtained independently from the Poisson equation for the tilted generator. For tilt Q(z), let B1=Q'(0), B2=Q''(0), nu=1^T B1 pi, and solve

    Q h = nu pi - B1 pi,    1^T h=0.
    D = 1^T B2 pi + 2 1^T B1 h,
    S_net = nu^2 / D.

Here current counts `2 -> 0` positively and `0 -> 2` negatively. The central fits have small **nonzero** currents, of opposite signs; neither is asserted to be an exact equilibrium generator. Their differing inferred rates also are not an uncertainty-controlled proof that one sensor changes the underlying clockwork. The error matrices are archived but **not propagated**. These are fitted-generator calculations, not independently measured precision values or a new experimental validation.

For a further internal consistency check the script computes

    sigma_fit/k_B = sum_{i<j} (pi_i q_ji - pi_j q_ij)
                           log[(pi_i q_ji)/(pi_j q_ij)]

and checks the current TUR. This is the stationary path-time-reversal entropy of the specified fitted Markov model. It must not be substituted for a measured reservoir heat budget or sensor dissipation.

### Public-code energy-accounting questions: not resolved reproduction

Relevant sections of the pinned `data_converter.py`, `reflecto_pwr.py` and `visualizations.py` were inspected. DC signal entropy is time-integrated in preprocessing and divided by trace duration in plotting; RF values enter plotting as rates. **The saved DC and RF `sensor_entropy.npy` scalars therefore must not be compared directly as if they had identical units.**

Two source-level RF questions remain before claiming reproduction of the published energy budget:

- `reflecto_pwr.py` uses `20*np.log(amplitude_ratio)` in its dBm conversion, rather than the conventional `20*log10(amplitude_ratio)`.
- Its function returns a variable named output power; the inspected caller divides that value by k_B*T, without an explicit incoming-minus-reflected-power subtraction at that point. This needs reconciliation with the supplement's net-power description and the calibrated signal interpretation.

These observations flag an implementation/version/calibration audit to perform, not proof that the reported experimental conclusion is false. The March public snapshot may not encode the final published analysis. No raw RF signal reconstruction, corrected numerical cost or quantitative reassessment of the paper is claimed here.

## 6. Composition with our energy-exchanging quantum clock

Our [coupled-channel clock](ENERGY_EXCHANGE_CLOCK.md) bounds a quantum instrument relative to its ideal instrument, including reference entanglement and the full outgoing state. It does **not** supply the thermodynamics of extracting a macroscopic record.

A useful explicit intermediate step is a nondemolition classical label-readout channel R(r|d). If the actual flagged instrument is I and the downstream operation only relabels its outcome d, define

    J_R(r) = sum_d R(r|d) I_d,
    epsilon_readout = max_d [1 - R(d|d)].

For every input including any reference system, positivity of the I_d outputs gives

    (1/2) || (R tensor id)(I) - I ||_diamond <= epsilon_readout.

Indeed each d contributes at most
`(1/2) sum_r |R(r|d)-delta_rd| Tr(I_d(rho))`, and these traces sum to one. If the earlier ideal-instrument error is delta_quantum, contraction and the triangle inequality yield

    delta_record <= min(1, delta_quantum + epsilon_readout).

Thus our dimensionless example with the uniform full-instrument bound `0.00922832935` would have record error at most that bound **plus a separately established readout error**. It cannot be advertised as a complete hardware record bound without the latter. The nondemolition label-channel assumption does not cover additional system disturbance, record decay, bandwidth loss or false event production; those need additional channels and bounds.

For sequential uses, uniform conditional instrument bounds can be telescoped, including adaptive control and references, to a sum of per-use errors. This requires each step's bound actually to hold on its current input and resource state. It does **not** establish that one reused, degraded clock enjoys the fresh-preparation bound at every step.

## 7. A correct thermodynamic ledger

Keep separate:

1. Clockwork dynamics and calibrated event statistics.
2. State discrimination and pointer readout, with errors and bandwidth.
3. Storage capacity, retention time and usable record redundancy.
4. Preparation, reset, amplification, refrigeration and sustained reuse.

A non-double-counted thermodynamic description is

    Sigma_total = Delta S_joint + sum_b Q_to_bath_b / T_b >= 0,

under the appropriate initially thermal, initially uncorrelated working-system/reservoir and weak-coupling assumptions. Correlations belong in S_joint; blindly adding subsystem entropy productions can miss mutual-information terms. Finite strong-coupling or nonthermal-reservoir versions require their own accounting. A unitary correlation-generating operation preserves joint von Neumann entropy, but this does not provide free blank memory or a complete cyclic readout device.

For a degenerate classical memory reset at temperature T with accessible classical side information Y, the ideal reversible-limit Landauer bound is

    Q_reset >= k_B T H(M|Y),

with H in nats and the stipulated reset cycle accounted for. It is not automatically k_B*T*ln(2) per jump: the memory's actual information, compression and accessible side information matter. The register above illustrates why estimating time need not require retaining every raw event. Conversely, throwing away raw data is a physical operation, not a resource-free mathematical omission in a cyclic apparatus.

The supplement's ideal permanently append-only record has no allowed reverse record operation and hence an infinite irreversibility in its path-reversal idealization. **Finite measured sensor cost does not prove exact, eternal record permanence.** Finite retention and finite error are the implementable targets. A reversible controlled increment with an available inverse is a different model, not a counterexample to that stipulated idealization.

## 8. Consequence for the problem of time and the unified account

The paper does not derive fundamental time from entropy. It shows that **an equilibrium clockwork can carry elapsed-time information, while extraction into readable records has a substantial apparatus cost**. Clock activity, entropy production and accessible recorded time are distinct quantities.

This sharpens rather than replaces our direct problem-of-time work:

- Constraint/clock-choice constructions address compatible relational descriptions.
- The energy-exchange construction addresses physical clock preparation, recoil and measurement accuracy.
- This event-clock bridge supplies exact finite-time statistical calibration in a stipulated open Markov model, plus explicit record/readout qualifications.
- A unified autonomous Hamiltonian for clockwork, detector, bath and finite memory, with controlled reductions and sustained-use error/entropy bounds, is **not yet supplied**. Neither is the gravitational constraint/refoliation problem solved by this paper.

For the whole-account objective, operational records do not constitute phenomenal awareness merely by being classical or dissipative. Necessary atemporal articulation remains compatible with these effective temporal descriptions, but this experiment does not establish that metaphysical constitution. The concrete gain is an explicit, testable distinction between microscopic change, calibrated event time, readable labels and durable records—not a replacement of the zero-residue objective by an entropy slogan.

## Verification

Run `python verification/tick_readout.py` or `python -m verification.tick_readout`. Deterministic output is saved in [tick_readout.json](verification/tick_readout.json). Exact identities certify the specified mathematical models; source checks certify the small archived files and arithmetic, not the experimental modelling assumptions or unresolved RF energy pipeline.
