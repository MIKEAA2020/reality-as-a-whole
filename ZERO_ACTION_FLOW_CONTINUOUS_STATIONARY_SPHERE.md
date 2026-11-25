# Action-flow, a timeless whole, and two continuous sphere histories

**Source.** Sanjay Soni, [*Time in the Universe — A Conceptual Model Based on Action-Flow Theory*](https://doi.org/10.5281/zenodo.23770244), Zenodo software release `SSR`, published 29 October 2026. The deposit describes an archive whose preview contains one `README.md`; I read its source at the pinned GitHub commit [`1d4ead007186c278440f5dbd7c8a0e0d2df2a6e0`](https://github.com/sonisanjay93570-eng/A-Conceptual-Model-Based-on-Action-Flow-Theory/blob/1d4ead007186c278440f5dbd7c8a0e0d2df2a6e0/README.md). GitHub reports the tree contains that single file. The retrieved README's SHA-256 is `4a3fa6bf918016960b2c9ebd124903f349235033deeab5e73e2e3aad8f0ad65c`. The linked deposit identifies this as an independent **conceptual hypothesis**, open to review, not an established physical theory.

**New calculation.** [Verifier](verification/zero_action_flow_continuous_stationary_echo_test.py), applying the proposal's question about continuity to our actual [20-step sphere echo and candidate intrinsic qualities](ZERO_ECHO_INTRINSIC_QUALITY_AND_INCIDENCE.md). The 40-state reference clock and the two flow generators below are **our extra stipulated constructions**, not results in the source or an experiment performed by the author.

## Result

Soni asks whether observable changes might share a continuous underlying flow, while distinguishing physical processes, clock measurements and subjective duration. This connects to our question without requiring the whole to exist **in** an external time. A whole can be stationary under a joint constraint while its internal reference clock conditions continuously varying relations.

The actual sphere program supplies a sharp test of what that idea adds. I constructed **two different continuous, internally conditioned completions** of its 20-step history. They:

* reproduce the same actual sphere state at every one of the original 20 clock readings;
* preserve the sphere model's stipulated zero charges and satisfy an exact stationary **joint clock constraint**;
* nevertheless give different observable intermediate-record predictions at a specified reference-clock phase.

At the halfway phase between the first two sphere readings, the probability of the existing echo bit being negative is approximately **0.00394** for one completion and **0.01937** for the other. This is a physical probability in the stipulated extended model, not an observed phenomenon or an experiential measure. The difference also gives the physical disagreement probability between the prior `s j` and `s j r` candidate signs at that phase.

Thus a continuous flow can be made compatible with the timeless-whole picture, but the existing discrete record history, charge cancellation and stationarity do **not by themselves** select a unique flow. This is a conditional mathematical comparison of two constructed completions, not a claim that both are genuinely self-sufficient possibilities or a disproof of the user's stronger zero constitution.

## 1. What the linked model says—and what it does not

The source proposes exploring

`hypothetical fundamental flow → interactions → transformations → observable states`.

It asks what the flow is, what remains invariant, how a physical process is related to a measurement of duration, and what could distinguish the proposal empirically (README §§2, 6, 11–13). It explicitly says that ordinary examples of transformation do **not** establish a single universal flow. It distinguishes physical time, measured time and subjective perception, and acknowledges the measured dependence of clock intervals on motion and gravitation. It does not argue that clocks create natural change or that physical time is merely a human invention.

The source provides no specified universal-flow state space, equation of motion, physical clock map or quantitative discriminating prediction. Its schematic arrows are a research proposal, not a derived dynamics. It does not establish that continuous flow is a fundamental global time, a preferred foliation, energy, or experience. Nor does the author's cautious statement “Experience is an idea, not a claim” justify denying the reality of felt experience. In our program, experience is taken seriously as the proposed intrinsic nature of reality; its specific relation to a physical process must be justified.

The broad idea that processes, records and clocks may be relational is prior art, not a new discovery of either project. The constructive issue here is more specific: **can a particular continuous relational interpolation be recovered from the actual finite zero-charge echo, and what would it change at an accessible interface?**

## 2. The original sphere history is the common input

Write `U_t` for the actual sphere–reservoir–echo prefix at integer tick `t=0,…,19`, with `U_20=I`. For any one specified normalized initial state `|ψ⟩`, including thermal purifiers, define the clock-labeled vectors

`|h_t⟩ = |t⟩_C ⊗ U_t|ψ⟩`.

They are orthonormal because their original sphere-clock states are orthogonal. The existing controlled cyclic shift W satisfies `W|h_t⟩=|h_(t+1 mod 20)⟩`. These vectors span a **20-dimensional orbit of the actual program**, not the whole physical Hilbert space. The physical zero-charge properties of the original input and every `U_t` carry over to this orbit; the added reference below is stipulated neutral under those charges.

Let

`|u_k⟩ = 20^(-1/2) Σ_t exp(2π i k t/20) |h_t⟩`, `k=0,…,19`.

Then `W|u_k⟩=exp(−2π i k/20)|u_k⟩`. The original stationary history on this orbit is `|u_0⟩`. Nothing here requires a literal universe inside a computer; the clock labels represent modeled relational degrees of freedom.

## 3. Two continuous generators, the same recorded steps

On that orbit define two self-adjoint, nonnegative spectral generators

`K₀ = Σ_(k=0)^19 k |u_k⟩⟨u_k|`,

`K₁ = K₀ + 20 |u_10⟩⟨u_10|`.

Set `V_a(θ)=exp(−i θ K_a)` for `a=0,1`. Both are continuous unitary families in the mathematical parameter θ, and

`V₀(2π/20)=V₁(2π/20)=W`, `K₀|u_0⟩=K₁|u_0⟩=0`.

Consequently `V₀(2π t/20)|h_0⟩ = V₁(2π t/20)|h_0⟩ = |h_t⟩` at **every** integer sphere tick. Both also leave the unaugmented uniform history `|u_0⟩` stationary for all θ. Their difference is a spectral branch—adding 20 to a particular eigenvalue is invisible at those step phases, but not in between. On this orbit the generators act within the original prepared zero-charge sector. Extending them by zero on its orthogonal complement gives self-adjoint extensions preserving the stipulated charge sector; this does not establish locality, a physical apparatus implementation or objective whole-level energy.

These two interpolations are not obtained by re-labeling one known physical time curve: below they are compared against the **same fixed reference phase measurement** and give different joint probabilities. Nor has it been shown that the user's strongest constitution permits both; they are two mathematical completions of the same current finite premises. Additional physical constraints could rule one or both out.

## 4. Put the comparison inside a stationary whole

To avoid assuming a fundamental external time, add a **specified**, neutral 40-state phase reference R. Its spectral basis is `|m⟩_R`, `m=0,…,39`. Let the sphere generator's eigenvalues be

`λ_k^(0)=k`, `λ_k^(1)=k+20 δ_(k,10)`.

Both sets fit in `0,…,39` and have 20 distinct members. Prepare, respectively,

`|Ω_a⟩ = 20^(-1/2) Σ_k |u_k⟩ ⊗ |λ_k^(a)⟩_R`.

With `M_R|m⟩=m|m⟩`, each obeys the exact stationary constraint

`(K_a ⊗ I − I ⊗ M_R)|Ω_a⟩=0`.

This is a constructed relational-clock constraint, not a statement that the universe's physical energy has been identified or measured. The two joint states and their constraints differ. Tracing R out gives the **same** sphere-orbit marginal `I/20` in both; that marginal is dephased and is **not** the original unaugmented pure `|u_0⟩` history. Preparing the reference correlations is an intervention, not a free description change.

Use the orthonormal reference phase basis

`|θ_l⟩ = 40^(-1/2) Σ_(m=0)^39 exp(i m θ_l)|m⟩`, `θ_l=2π l/40`.

Every reference result has probability `1/40`. Conditioning on it yields

`|φ_a(θ_l)⟩ = 20^(-1/2) Σ_k exp(−i λ_k^(a) θ_l)|u_k⟩`.

At even reference readings `l=2t`, both conditional sphere states equal the actual `|h_t⟩`; at `l=1`, they are two different states at the halfway phase. There is no unconditioned physical requirement for a universal preferred time here. The phase basis, reference system, correlation, spectral generators and condition-to-observable map are explicit added ingredients. Continuous dependence between the sampled phase values is supplied by `V_a(θ)`; the finite reference has only 40 orthogonal phase outcomes and is not an ideal continuous clock.

## 5. A quantitative distinction at the physical interface

For the half-step event `l=1`, let `|φ₀⟩,|φ₁⟩` be the two normalized conditioned sphere-orbit states. Their overlap is

`⟨φ₀|φ₁⟩=9/10`, `|⟨φ₀|φ₁⟩|²=81/100`.

Their trace distance is `√19/10 ≈ 0.43589`; this is the optimal distinguishing advantage **if** a suitable global orbit measurement is physically accessible. It is not automatically available to an inhabitant restricted to a smaller realm.

A simpler existing-clock comparison does not require invoking that optimal measurement. The probability of the original sphere clock being in position 0, conditional on `l=1`, is

`P₀(C=0 | l=1) = [1+cot²(π/40)]/400 ≈ 0.40612`,

`P₁(C=0 | l=1) = [1+(cot(π/40)−2)²]/400 ≈ 0.28906`.

The fixed reference and clock effects thus distinguish the completions in principle, although all original even reference phases have the same sphere state. This is a conditional model calculation; it is not a prediction unique to Soni's proposal or a measurement in nature.

The result also reaches **the actual echo record**, rather than stopping at the clock. Because the original sphere clock is traced when only E is read, the orthogonal clock labels make the conditional E probability a mixture of the actual tick-conditioned probabilities. Using the exact original `(b,z,s)` Born law and the two previously checked auxiliary preparations gives

| Reference half-step `l=1` | Completion `K₀` | Completion `K₁` |
|---|---:|---:|
| `P(r_E=−1)` | **0.00394089** | **0.01936630** |

For the fixed earlier physical candidate signs `s j` and `s j r_E`, disagreement is exactly the event `r_E=−1`; their physical disagreement probabilities at this phase are therefore the same numbers. The conditioned state at this phase is a coherent superposition over **all** original sphere-clock labels, including later labels. It is not a classical trajectory in which the future echo has somehow occurred before the first gate; nor is either global spectral interpolation shown to be a local gate-by-gate implementation. Both candidate signs remain physically balanced between positive and negative within each E record cell because the s-counterparts have equal Born weights. This does not make either physical sign an actual felt valence or establish the Born weights as subject-incidence weights. An experiential comparison requires the same independently justified subject boundary, quality rule, access and measure demanded in the preceding report.

## 6. Continuity, subjectivity, and the no-residue aim

This calculation gives the “continuous flow” idea a definite internal meaning: a continuous family on an already specified orbit, correlated with a physical reference, whose conditional effects can be checked while the joint constraint is stationary. It does not derive the orbit, the two spectral generators, the reference state, a physical timescale, the finite clock spectrum, or a reference-to-subject interface from zero. In particular, smooth interpolation does not turn the selected `s j r_E` candidate into experience, nor does a zero mean remove any negative felt contribution.

It also sharpens the constructive requirement. If zero's own constitution determines physical differentiation and experienced succession, it must determine **which** continuous relations and clock comparisons are actual, not merely accommodate any interpolation of a finite record. A successful principle could select one generator, identify the two completions under a genuinely justified equivalence, or lead to a different structure. Their different fixed-reference predictions mean an equivalence cannot be asserted while keeping the same physical reference observables and preparation unchanged. Nor may we simply declare an unwanted completion not genuinely possible; the relevant criterion must follow from the self-sufficient whole.

The two constructed stationary constraints and the original model's signed charges are not the same as a demonstrated objective zero total energy of reality. Likewise, mathematically changing the direction or speed of a flow does not automatically produce an opposite experience. If actual felt valence is a globally additive quantity, its cancellation and incidence weights still need to be derived together with the physical constitution, without identifying suffering with absence or treating its local reality as erased.

**Reproduce:**

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. \
  python -m unittest verification.zero_action_flow_continuous_stationary_echo_test -v
```

The verifier checks both stationary joint states, all 20 sampled states, the half-step overlap and clock probabilities, and the actual E-record/quality-candidate statistics. Its checks are finite quantum mathematics, not evidence of a universal fundamental flow or actual subjects.
