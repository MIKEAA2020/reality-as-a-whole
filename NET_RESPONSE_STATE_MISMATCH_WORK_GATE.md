# Can total response identify state mismatch without resolving every channel?

## Main result

**Conditionally, yes for a difference between two states—but not for every quantity called frustration.** If the proposed total mismatch cost is a fixed scalar potential and a calibrated total response is its gradient, then integrating that response along a path gives the difference in state mismatch. The individual channels need not be separated and the unknown minimum cancels. This bypasses the separate-channel remainder bound in the [previous gate](STATE_MISMATCH_CONTRAST_AND_FALSIFICATION_GATE.md), **but replaces it with demanding whole-system response and potential-identification assumptions**.

This distinction matters for the user's idea. Hidden opposing channels can leave channel-defined *minimum frustration* unidentified even under complete net-force observations, as shown in the [hidden-channel audit](FRUSTRATION_CYCLE_IDENTIFIABILITY_GATE.md). Yet under the assumptions above, the same net response can identify **differences in state excess**. Neither quantity is automatically discomfort. No experimental brain channel or experiential bridge has been established here.

The work–potential relation and line-integral theorem are standard, not invented here; see [OpenStax, University Physics, chapter 8](https://charma.uprm.edu/~mendez/Lectures/OpenStax_v1/v1_ed0_openstax_08.pdf) and the discussion of conservative fields in [Edinburgh lecture 17](https://www2.ph.ed.ac.uk/~mevans/mp2h/VTF/lecture17.pdf). The contribution here is their **specific application and error/identification gates** for the project's previously defined state-mismatch candidate, including concrete counterexamples.

## 1. Exact identification, given a correct potential

Take one fixed admissible state space Ω, with a continuously differentiable single-valued cost `E` and finite infimum `F = inf_Ω E`. Set `D(z)=E(z)−F`. Let a feasible, sufficiently smooth path `γ:[0,1]→Ω` go from `A` to `B`. Suppose an independently calibrated total response gives the signed path derivative

```text
q(s) = ∇E(γ(s)) · γ′(s).
```

Then standard potential theory gives

```text
D(A) − D(B) = E(A) − E(B) = −∫₀¹ q(s) ds.        (1)
```

A force convention may instead report `−∇E`; the measured sign must be fixed independently. Equation (1) holds without decomposing E into channels and without knowing F, provided **the response is the derivative of the entire mismatch cost that the hypothesis actually uses**. It also applies when A and B lie in the same path-connected component, even if the global infimum lies in a different component. If the two states are in different components and no meaningful calibrated path exists, (1) cannot be used to compare them.

### Why this is narrower than it sounds

An observed total physical force is not automatically the gradient of the proposed mismatch cost. Suppose it instead equals the gradient of `E+R`, where R includes conservative but non-mismatch contributions. Then integrating it identifies `(E+R)(A)−(E+R)(B)`, not `D(A)−D(B)`. One must separate R or independently bound `|R(A)−R(B)|≤b_R`, enlarging the contrast interval by `b_R`. If no bound exists, the intended quantity is unidentified. This is **not** resolved by declaring every physical force a mismatch force. Similarly, a measured phase drift `−M∇E` is not the gradient itself unless the mobility/response operator M and other drives are independently known or corrected.

The path must describe the relevant **unchanged** landscape: changing coupling, subject/system boundary, environment or admissible space while moving or probing may change E and F. A calibration sweep can change the very experience or state it is intended to explain; one would have to show that its inferred landscape applies to the separately observed A and B episodes, not assume this or equate the sweep itself with those experiences. Work performed by an apparatus, nonequilibrium dissipation, inertia, path-dependent interventions and direct sensory effects must not be silently identified with the gradient. Holding only a subset of variables fixed while hidden variables respond may access a different effective potential, discussed below. Path feasibility and interventions are substantive physical questions, not consequences of the formula.

## 2. A finite, error-bounded measurement gate

Let `s_j=(j+1/2)/n`, `j=0,…,n−1`, and suppose:

- the **true** q along the specified path is L-Lipschitz on `[0,1]`, with L independently justified;
- all `n` observed `q̂_j` simultaneously satisfy `|q̂_j−q(s_j)|≤ε`, including measurement, model, path-setting and calibration errors to the extent validly bounded;
- the cost landscape and response law are stable and equation (1) holds.

Define `M = n⁻¹ Σ_j q̂_j`. The midpoint quadrature error follows from integrating `L|s−s_j|` over each cell. With `r=ε+L/(4n)`,

```text
D(A) − D(B) ∈ [−M−r, −M+r].                      (2)
```

If an independently justified residual-potential bound `b_R` is needed, replace r by `r+b_R`. No statistical independence of cell errors is needed for this deterministic implication. Statistical confidence regions require simultaneous coverage, with systematics, model selection and multiple paths accounted for; repeated observations do not eliminate unbounded bias. If γ itself is measured with error, its effect on `∇E·γ′` must actually be included in ε or treated separately. `L` is a regularity bound on **q as a function of the declared path parameter**, not a claim that neural activity is globally Lipschitz.

### Hypothetical control from the previous reversal

The previously examined models have phase `x=πs` and costs

```text
E_K(x) = 1 + cos x + K(1 − cos x),       K ∈ {0, 2}.
```

They share the same selected antiphase channel, but their total response along the path is `q_K(s)=π(K−1) sin(πs)`. For `n=32`, `ε=.1`, and a genuinely justified `L=π²`, equation (2) gives radius `r≈0.17711`:

| Model | Exact `D(A)−D(B)` | Midpoint estimate | Bound |
|---|---:|---:|---:|
| K=0 | +2 | +2.00080 | [1.82370, 2.17791] |
| K=2 | −2 | −2.00080 | [−2.17791, −1.82370] |

These values are ideal calculations in model units, **not measurements**. With sufficiently controlled total response the models' opposite rankings can be distinguished; selected-channel contrast plus endpoint forces alone could not. This does not imply that any feasible clinical method can control or read out the required phase path.

## 3. Why finite response samples alone are not enough

For any `n≥1` and amplitude `C>0`, compare a zero response with

```text
q_alias(s) = C sin(πs) cos²(nπs),       0≤s≤1.
```

Both are zero at the n midpoint samples and at the two endpoints, but

```text
∫₀¹ q_alias(s) ds = (C/π) [1 + 1/(1−4n²)] > 0.
```

The integral can be arbitrarily large as C increases. `q_alias` extends to a smooth period-2 phase response whose integral over a complete period vanishes, so it is the derivative of a smooth periodic scalar potential, not merely a nonconservative artifact. Its potential can be shifted to be nonnegative without changing q. For n=32 and C=100 the true integral is about **31.8232**, despite zero ideal sampled values. This example violates the illustrative `L=π²` bound; it demonstrates why a valid, independently established regularity/error bound is essential. Finite additional samples only move the alias problem unless the allowed function class is constrained. The proof is constructive; the numerical check is not an exhaustive functional analysis.

## 4. The distinction between total excess and channel frustration

If Ω is path-connected, two continuously differentiable potentials have the same gradient everywhere on Ω exactly when they differ by a constant (within the usual connected smooth setting). Their infima shift by that same constant, so they have the **same D at every state**, even if their channel decompositions and channel-based F differ. If only pathwise response on a connected subset is known, equation (1) identifies only differences **within that subset**; it does not establish the minimum outside it or absolute D there.

Disconnected domains expose the limitation. Suppose Ω has components C₀ and C₁. Two potentials may have zero force everywhere but take constants `(0,0)` and `(1,0)` on `(C₀,C₁)`. For a state on C₀, their global excesses are respectively 0 and 1. There is no path between components to measure the relative offset. Thus local force observations do not determine absolute D across disconnected components. Even when Ω is connected, no finite practical force sample determines all-state D without adequate coverage and regularity.

Returning to the earlier hidden-channel example: equal opposing channels can have positive channel-baselined F while producing a constant total E and zero D; an alternative with no interaction plus a constant background has the same total potential and D, but a different channel-defined F. Net response may identify the **total-potential equivalence class** while failing to identify the channel decomposition. It does not resolve whether the selected experiential quality should depend on F, D, or something else, or whether such a potential is physically meaningful.

## 5. Path dependence and hidden degrees of freedom

**Loop test.** A gradient of a single-valued potential has zero integral around every closed path. Thus a reproducibly nonzero circulation whose full uncertainty interval excludes zero rejects the exact-gradient assumption on that domain. Conversely, a few zero loops do **not** prove it. Topology matters: on a phase circle a constant torque `τ` is locally curl-free, yet integration around the full circle gives `2πτ`, not zero. For `τ=.7` the two paths from 0 to π and 0 to −π give `+2.1991` and `−2.1991`, a loop discrepancy of **4.3982**. This is an explicit model, not an experiment. A nonzero loop could also reveal instrument drift, changing states or omitted work rather than a uniquely identified physical mechanism.

**Effective free energy is not automatically microscopic mismatch.** In a simple equilibrium toy, let hidden `h∈{0,1}`, microscopic costs `E(x,0)=0` and `E(x,1)=1−cos x`, with inverse temperature 1. If h equilibrates at fixed x, its free-energy profile is

```text
A(x) = −log[1 + exp(−(1−cos x))].
A(π) − A(0) = log[2/(1+e^(−2))] ≈ 0.56622,
E(π,0) − E(0,0) = 0.
```

A mean-force integration can therefore identify an **ensemble effective free-energy contrast**, which differs from the microscopic cost of a particular hidden state. Entropic, constraint-geometry and sampling terms depend on the coordinate and ensemble; the molecular-literature discussion of [constrained mean-force/free-energy relations](https://arxiv.org/html/1105.2733) and [coordinate-dependent corrections](https://theory.rutgers.edu/resources/pdfs/Wong_JChemTheoryComput_2012_v8_p3998.pdf) is relevant precedent. It does not establish an equilibrium assumption in brains. For real neural systems, oscillations, nonstationarity, common drive, hidden variables and nonequilibrium dynamics make the potential assumption particularly demanding; phase-only and fMRI observables do not directly provide a calibrated conjugate force.

## 6. What to do with the two routes

- **Channel route:** useful if a specific decomposition is independently real, selectively controllable and calibrated; needs a bound on the change in omitted terms. It can in principle address channel-defined F but is vulnerable to hidden channels and functional aliasing.
- **Net-response route:** potentially avoids individual channel resolution for `D(A)−D(B)`, if the entire relevant mismatch potential is measurable through a stable, integrable total response. It does not identify channel-defined F, the absolute minimum, or a mismatch component embedded among unrelated forces without further information.
- **Both routes fail closed:** when the potential, response scale, hidden-state relaxation, regularity or error coverage is not justified, label the physical contrast **unidentified**. More repetitions are not a substitute for these assumptions.

If a validated future experiment did certify a positive contrast, it could feed the explicitly narrow report-falsification rule in [the previous gate](STATE_MISMATCH_CONTRAST_AND_FALSIFICATION_GATE.md), with independent subjective calibration and a prespecified positive slope. A successful prediction remains evidence about a model, not an identity proof or a demonstration that the self-sufficient whole is intrinsically experiential. No universal subject, creator, external time or literal simulation is assumed.

## Reproduction and scope

Run `python verification/net_work_mismatch_gate.py`; its [receipt](verification/net_work_mismatch_gate.json) records the two model bounds, smooth unsampled alias, nonzero loop, hidden-state example and **15,000 seeded Fourier-family numerical containment checks**. These tests validate implementations on the stated cases, not the physical assumptions, a human study, or the full framework. Existing work on work integrals and free energy is cited rather than presented as a new derivation.
