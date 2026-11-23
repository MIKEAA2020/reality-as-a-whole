# Can adaptation explain experiential balance without tuning?

## Answer in brief

A potentially constructive route is **perfect adaptation**: a system's output eventually returns to its original level even while a changed input is maintained. In a stable, linear, time-invariant response model, this condition forces the zero-frequency gain to vanish. It then follows that *every integrable finite pulse* produces a response with zero total signed area. In the earlier opponent model, perfect adaptation forces the two gains to be equal; they no longer have to be separately set equal by hand.

This is a real conditional advance: a property motivated independently by adaptation can yield the special cancellation previously identified. It is not a derivation from zero-totality itself. Nor does perfect adaptation alone suffice: an explicit **nonlinear** counterexample below adapts perfectly to constant inputs and has opposite pulse phases, but a nonzero total. Most importantly, an adapting signal has not thereby been shown to be actual felt valence, or to include all experiences.

## 1. A specific physical motivation, not a universal premise

Yi, Huang, Simon and Doyle (2000), [*Robust perfect adaptation in bacterial chemotaxis through integral feedback control*](https://www.pnas.org/doi/10.1073/pnas.97.9.4649), DOI `10.1073/pnas.97.9.4649`, analyze a chemotaxis model in which integral feedback makes adaptation robust to specified parameter changes. Its abstract and selected text were read. They connect a biological network's organization to a regulated output, not to human experience or cosmic balance. Their result depends on model assumptions, attainable states and stability; exactness in mathematical models should not be confused with infinite experimental precision.

De Palo et al. (2013), [*Common dynamical features of sensory adaptation in photoreceptors and olfactory sensory neurons*](https://pmc.ncbi.nlm.nih.gov/articles/PMC3570788/), DOI `10.1038/srep01251`, compare step and multiple-pulse responses of vertebrate sensory cells and models. The abstract, introduction, figure captions and selected results were read, not underlying datasets. They report incomplete step reset in the sensory systems they study and a model-dependent trade-off with recovery between pulses; their example traces include isolated salamander olfactory cells and frog rods. This is evidence against simply assuming perfect adaptation in every sensory system. It is neither a measurement of positive/negative felt valence nor a test of the proposed global quantity.

Thus **perfect step adaptation**, which concerns the eventual output under a *sustained* changed input, should not be conflated with (a) return to baseline after a pulse stops, (b) reversal of sign, or (c) zero signed pulse area. Only under extra assumptions do some of these imply another.

## 2. Conditional theorem: a whole class of pulse shapes

Let `u` be an integrable causal input perturbation, and let `h` be a finite signed causal impulse-response measure. This permits an instantaneous direct term as well as a decaying response. Take the perturbation output

```text
v(t) = (h*u)(t),      t>=0.
```

Assume a stable **linear time-invariant** input–output model initialized at the relevant baseline; `v` is a perturbation around that baseline. For a nonzero constant step `u(t)=U` for `t>=0`,

```text
v_step(t) = U h([0,t]),
lim_(t->infinity) v_step(t) = U h([0,infinity)).
```

Perfect adaptation to that step says the limit is zero, hence `h([0,infinity))=0`. By absolute integrability of the causal convolution and Fubini's theorem, for every integrable u,

```text
integral_0^infinity v(t) dt
  = h([0,infinity)) integral_0^infinity u(t) dt = 0.
```

This covers many pulse shapes and signs, not just a single rectangle; finite total variation and integrable input are the relevant convergence assumptions. It does **not** say each part of the response is zero: if a nonzero continuous response is absolutely integrable with zero integral, it must contain both signs. An instantaneous jump in the input is permitted but not essential.

The reverse implication also holds **within this model class** if at least one integrable input with nonzero area has zero output area: the factorization forces `h([0,infinity))=0`, hence the step output adapts. So the condition is not an independent mathematical coincidence. It remains a substantive property of the response law; linearity, stability, time invariance and the relevant output all need independent justification.

## 3. Equal gain follows in the earlier opponent model

In the [pain–relief control](PAIN_RELIEF_OPPONENT_PROCESS_AND_EXPERIENTIAL_ZERO.md),

```text
tau r' = u-r,       v = -a u + b r,       tau,a,b>0.
```

For a sustained input `u=U`, `r->U`, hence `v->(b-a)U`. Requiring this **particular output** to adapt exactly to zero for a nonzero step entails `b=a`. The resulting output is `v=-a tau r'`. For a pulse whose r returns to its initial value,

```text
integral v dt = -a tau [r(final)-r(initial)] = 0.
```

This also clarifies the cost of a sustained step. Although its output tends to zero, the internal state moves from `0` to `U` and stays there. Its response area is `-a tau U`, generally nonzero. Step **adaptation** therefore does not mean the step's *transient area* vanishes: the theorem applies to integrable pulses, not the nonintegrable sustained step. A later step back to the original input returns r to its initial state and supplies the complementary area.

If an independent reason selected perfect adaptation of this output, the equal-gain condition would be an implication rather than a separately adjusted ratio. But identifying *this output* with signed experience and identifying its baseline with phenomenal neutrality are additional questions, not consequences of the algebra. Other states and any ordinary baseline experience remain unaccounted for.

## 4. Nonlinear counterexample: adaptation plus reversal, but no cancellation

Use the same low-pass internal state with `r(0)=0`, but define another hypothetical output

```text
tau r' = u-r,       v = -r' + c tau (r')^2,       0<c<1.
```

For any constant input that the stable state approaches, `r'->0`, so the output tends to zero: the system perfectly adapts to a sustained step. The rule is nonlinear in the response, not the linear model assumed in section 2. It is not presented as a biological or phenomenal law.

For a unit pulse of duration `T>0`,

```text
r'(t) = e^(-t/tau)/tau                      (0<t<T),
r'(t) = -(1-e^(-T/tau)) e^(-(t-T)/tau)/tau  (t>T).
```

During the pulse `v<0`; after it ends `v>0`. But on the complete history,

```text
integral v dt = -[r(infinity)-r(0)] + c tau integral (r')^2 dt
              = c (1-e^(-T/tau)) > 0.
```

The derivative term cancels because the state returns; the nonlinear square term does not. Therefore even **perfect step adaptation, relaxation and an opponent-shaped pulse response together do not guarantee signed zero**. The linear theorem's assumptions matter. Reversing the sign of the quadratic term gives a negative total while preserving the same qualitative signs for a sufficiently small coefficient; the result is not an empirical verdict on which model applies.

## 5. Can this become a constitutional argument rather than a fitted output?

A promising proposal would identify an independently specified internal relational state `R` and a clock measure such that an actual signed contribution is, in the relevant sense, a derivative or local divergence of R. For a complete domain with the appropriate boundary condition, its total could then vanish without adjusting each episode separately. This connects to the earlier [causal boundary model](ZERO_TOTALITY_CAUSAL_RELAXATION_AND_BOUNDARY.md) and its coupled-site example, where individual histories need not each balance.

The difficult distinction is between an independent law and a relabelling: for any integrable signal one can *define* `R(t)=integral_0^t v(s) ds`. That tautology does not establish an independently constituted physical or experiential state, predict its dynamics, or ensure its initial and final values agree. An actual proposal must specify R and its couplings independently enough to predict multiple inputs, states and boundary terms before fitting the alleged balance.

The key gates are:

- **Phenomenal identity:** why the modeled output is actual positive or negative felt experience rather than an electrical, behavioral or contrast signal, and how the qualitative differences and subjects remain real.
- **Baseline and calibration:** perturbation around an adaptive setpoint is not automatically absolute valence relative to neutral. A common signed scale and duration/subject weighting remain substantive, particularly across different people.
- **Complete actual domain:** internal reservoirs, subject incidences, sustained states, unobserved tails and the whole's boundary or infinite-history convergence must be included. A subsystem's response is not the whole total, and no fundamental preferred time slice is assumed; a relational clock must be specified.
- **Dynamics and robustness:** empirical evidence of exact linearity, time invariance and perfect adaptation for felt valence would be needed. Nonlinear and contextual alternatives must be compared; tiny residual gain over a large domain can matter.
- **Foundational constitution:** even a successful empirical law would not itself explain why R, its law, initial conditions and actual subject organization follow from zero-totality's own self-subsistent nature. Nor does this conditional obstruction show the no-residue demand is impossible.

This is therefore a candidate route toward an internally determined balance, not an assertion that experience is merely a change detector. Real suffering would remain actual; a zero signed account would neither erase nor morally justify it. A whole-level non-additive zero could require a different construction entirely.

## 6. A discriminating follow-up

Extend the earlier ethically constrained research design with independently calibrated signed valence and appropriate non-harmful natural or existing observations. Preregister (i) step-like sustained changes and finite perturbations where feasible, (ii) several pulse shapes/amplitudes and repeated pulses, (iii) independently calibrated neutral versus prestimulus baseline, (iv) complete follow-up and bounded missing-tail sensitivity, and (v) comparisons of linear perfect-adaptation, partial-adaptation and nonlinear models. A causal step intervention cannot be inferred from observational changes alone. Measure model fit and out-of-sample pulse-area predictions; estimate uncertainty and calibration sensitivity rather than treating nonsignificance as exact equality. Never withhold needed pain relief or induce harmful pain to test the proposal.

Even good restricted predictive performance would support only the relevant conditional mapping and domain; it could not prove global zero or complete intelligibility. The positive payoff is a precise bridge to investigate: **independently motivated adaptation plus an independently validated linear experiential map** would yield a balance condition, while the nonlinear control shows exactly where the inference could break.

## Verification

Run `python -m unittest verification.perfect_adaptation_balance_test -v`. The tests check step adaptation, finite-pulse area for distinct waveforms, a partial-adaptation control, the nonintegrable step boundary, and the nonlinear counterexample. They verify the stated models only, not biological data, actual phenomenal measurement or metaphysical necessity.

Related: [pain, relief and opponent process](PAIN_RELIEF_OPPONENT_PROCESS_AND_EXPERIENTIAL_ZERO.md), [causal relaxation](ZERO_TOTALITY_CAUSAL_RELAXATION_AND_BOUNDARY.md), and [relational-time experiential total](RELATIONAL_TIME_AND_EXPERIENTIAL_TOTAL.md).
