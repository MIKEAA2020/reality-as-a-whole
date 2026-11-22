# Finite-range calibration of the existing gravitating clock

**Verdict.** Under explicit boundary preparation, spectral-band, independence and phase-reference assumptions, the existing backreacting FLRW clock admits a finite-range estimator for its **energy-averaged quantum proper-time response**, with a 95% error bound below `0.049` in the model's units. This is an analytic, conditional bound on an operational estimator, not an observation, a uniquely defined classical elapsed time, a locally constructed clock, or a B7 pass. In particular, the finite-gap quantity averages responses of *different backreacted geometries*. This is a targeted completion of part of the open operational test in [TIME_DECISIVE_TEST_GRAVITY_RECORD.md](TIME_DECISIVE_TEST_GRAVITY_RECORD.md), not a solution of the problem of time.

The parent [gravitating clock](GRAVITATING_PROPER_TIME_CLOCK.md) action, ordering, physical continuum, incoming representation and scattering solution are **assumed**, not independently rederived here. It describes a homogeneous comoving oscillator smeared across the FLRW slice, not a local detector. The calibration below is model-specific, and its numerical examples are not measurements or predictions for our universe. Related clock-neutral reductions and changes of quantum clocks already exist, e.g. [Höhn and Vanrietvelde](https://arxiv.org/abs/1810.04153) and [Höhn, Smith and Lock](https://arxiv.org/abs/2007.00580). Clock-dependent boundary conditions and quantizations can be inequivalent, as discussed by [Gielen and Menéndez-Pidal](https://arxiv.org/abs/2109.02660); this note does not resolve that issue or assert novelty against the literature.

## 1. The target and assumptions

Use the parent's `mu=1`, oscillator gap `Omega=0.6`, and energy-channel parameters `kappa_0=0.2`, `kappa_1=0.6`. For conserved scalar spectral parameter `k`, put

    z(k) = S_1(k) S_0(k)* = exp(i phi(k)),
    tau(k) = phi(k)/Omega
           = (1/0.4) integral_[0.2,0.6] [4/3 Im psi(1/2-kappa+ik)] d kappa.

The phase `phi` is the **continuous energy-integral branch** starting at zero gap, with the incoming/outgoing phases and oscillator reference fixed as in the parent. This identity uses the parent's energy-response derivation, `kappa=2E/3` and `E_1-E_0=Omega`. It is not a choice of phase after seeing outcomes. The classical lifetime associated with one fixed branch is a different quantity, `4/3 [pi/2+atan(kappa/k)]`. The parent connects them asymptotically; no rigorous finite-`k` quantum-to-classical conversion bound is proved here.

Assume each run prepares the same normalized incoming joint state: oscillator `(|0>+|1>)/sqrt(2)` in the parent's incoming-channel representation, and a scalar spectral wavepacket supported in **some unknown interval** `I` of width at most `w=0.01` contained in `[2,8]`. Its center and shape need not be known to the estimator. This band restriction is substantial prior calibration; it must not be confused with a broad unknown cosmological state. A coherent wavepacket has no assumed actual hidden `k`; `tau(k*)` for any selected `k*` in its support is a comparison to the calibration function, not a claim that the packet has a single classical trajectory. The result applies to every such `k*` simultaneously.

Assume `N` independent repetitions of the same preparation, a fixed, accurately calibrated relative phase reference, the parent's complete asymptotic Ramsey-X measurement and no unmodelled loss or selection. These preparations, the reference, repetition/reset, and detection are **supplied boundary operations**, not derived physical apparatus. The scalar representation makes the integrated measurement probability diagonal in `k`, so an arbitrary coherent packet with this support gives

    p = (1 + integral_I |a(k)|² cos phi(k) dk)/2.

No independence of spectral components is assumed; independence concerns measurement repetitions. We do not assert that repeated cosmological universes can physically be prepared, or that the phase-reference operations are free.

## 2. Certified phase branch and spectral variation

We establish conservative uniform bounds analytically, not by maximizing sampled values. Set `a=1/2-kappa`, `b=a+1=3/2-kappa`. On the declared domain `b in [0.9,1.3]` and `k>=2`. The digamma recurrence and the positive-real-part series give

    Im psi(a+ik) = sum_(n>=0) k/((n+b)²+k²) + k/(a²+k²).

For the positive decreasing summand, the sum lies between its integral and the integral plus its initial value; the integral is `pi/2-atan(b/k)`. Hence uniformly

    pi/2-atan(1.3/2) <= Im psi(a+ik) <= pi/2+2/2.

Consequently the energy integral fixes the entire relative phase in the **unaliased** interval

    0.79553688496 <= phi(k) <= 2.05663706144 < pi.

One calibrated X quadrature is sufficient *on this proved interval*: cosine is strictly decreasing there. This does not give a globally unwrapped two-level clock; outside the promise, phases separated by `2pi` give identical outcomes.

For the uniform derivative, termwise differentiation is justified locally by uniform convergence. Each differentiated summand has absolute value at most `1/(n+b)²`, whose sum is at most `b^-2+b^-1`; the recurrence term's derivative has absolute value at most `k^-2`. Thus

    |d tau/dk| <= D = (4/3)(0.9^-2 + 0.9^-1 + 2^-2)
                    = 3.4609053498.

For any two points in `I`, their responses differ by at most `D w = 0.0346090535`. The analytic bound is deliberately conservative; it is not a fitted or sampled uncertainty.

## 3. Estimator and confidence statement

Record the fraction `f` of `+` outcomes. Let `L,U` denote the phase bounds above and clip `f` to the probability interval `[(1+cos U)/2,(1+cos L)/2]`. Define

    tau_hat = arccos(2 clip(f)-1)/Omega.

Let `s = min(sin L, sin U) = 0.7142394744`. Because the mean cosine for any supported packet is between the extrema of the monotone cosine on its band, it equals `cos phi(k0)` for some `k0` in the band. Its ideal inferred response is `tau(k0)`; it differs from every `tau(k*)` in that band by at most `D w`. By Hoeffding's inequality for independent Bernoulli trials, `|f-p| <= epsilon = sqrt(log(2/alpha)/(2N))` with probability at least `1-alpha`. Clipping cannot enlarge the difference from the true probability, and the inverse-cosine slope on the certified range is at most `2/(Omega s)`. Therefore, **uniformly for every admissible packet and every `k*` in its band**,

    Pr[ |tau_hat - tau(k*)| <= D w + 2 epsilon/(Omega s) ] >= 1-alpha.

With `N=200,000`, `alpha=0.05`, the terms are respectively `0.0346091` and `0.0141727`, totaling **`0.0487818`**. This is a coverage guarantee under the declared model, not a 95% posterior probability that the model is true. With only `N=100`, the same bound exceeds `0.6`: statistical resources cannot be silently ignored. The duration unit is the parent's model unit (`mu=1`), not a calibrated SI second.

If the actual success probability differs from the ideal by at most a known `beta` in each independent run, the same derivation adds `2 beta/(Omega s)` to the error bound. A bounded relative phase-reference offset `|delta|<=rho` can be included as `beta<=rho/2` (in radians); real offsets, readout bias, dependence, drift and postselection are **not measured or bounded here**. If they are unknown the stated guarantee does not apply. The confidence statement also fails if the band, phase branch, reference convention, scattering law or independent repetition assumptions fail.

## 4. Reproducible numerical controls and limits

The [calculator](verification/gravity_clock_duration_calibration.py) and [receipt](verification/gravity_clock_duration_calibration.json) check the parent exact reflection phase against an independently integrated parent digamma response at 61 `k` points, sample the analytic phase and slope bounds, and use Simpson quadrature to check five finite-band means. These are floating-point cross-checks of the implementation, not proofs of continuum bounds, action, phase reference or measurement realizability. The [tests](verification/gravity_clock_duration_calibration_test.py) additionally check clipping, invalid domains, the statistical worst-case endpoints, weak sample size, phase aliasing and an uncalibrated-reference failure. They do not validate the physical premises or manufacture data.

For illustration, uniform packets on `[2,2.01]` and `[7.99,8]` give mean Ramsey-plus probabilities approximately `0.576607` and `0.635352`, respectively. Their midpoint response values are `2.361627` and `2.161121`. These examples use the same model and are not a statistical experiment; a real test would need separate uncertainty for all calibration and preparation errors. They do show why a single unconstrained phase cannot by itself be treated as a global time label.

## 5. Connection to the formal battery and next decisive step

- **Internal B7 remains open.** There is no derivation here of local Hamiltonian/diffeomorphism constraints or their anomaly-free refoliation algebra, local apparatus, spacetime emergence, a real clock-switching instrument on common events, or singularity resolution. Nor does the estimator explain experienced succession (B6/B8 interfaces).
- **The external foundation battery is not replayable from the repository:** its reported preregistration, program, JSON and freeze materials were not supplied. Its previous entry-incomplete verdict remains; these calculations do not establish F0–F5 passes. The selected 45-script suite is a regression check, not the research battery.
- **Next focused gate:** extend the already established [finite clock-switching construction](CLOCK_CHOICE_EQUIVALENCE.md) and [turning-point atlas](TURNING_CLOCK_ATLAS.md) to this *same backreacting gravity model*, rather than repeating their separate constrained examples. Construct a second relational clock and explicit joint-event instruments on a common physical Hilbert space, transporting an identifiable record and its uncertainty across overlapping clock charts, including the volume turning point. State the domains and boundary conditions before comparing. A demonstration fails this gate if the purported switch drops a branch, changes the physical event or preparation, assumes a globally monotone volume, or relies on inequivalent quantizations without a common observable map. If this cannot be done with the current homogeneous action, that is a concrete limitation, not a reason to declare B7 passed. Local-field constraints and emergence remain further independent obligations.
