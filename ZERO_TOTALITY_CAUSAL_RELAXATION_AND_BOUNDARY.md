# Can causal relaxation account for zero experiential balance?

## Constructive result

The [locality and boundary analysis](ZERO_TOTALITY_LOCALITY_AND_BOUNDARY_BALANCE.md) found that a locally defined signed response integrates to zero only when a relevant net boundary term vanishes. One possible way to obtain that condition—without choosing a separately tuned final value—is **causal relaxation back to the same reference state**.

In a specified stable, damped response model, a finite positive pulse produces a positive response followed by a negative after-response whose complete time integral is zero. More generally, any bounded finite-duration input gives zero integrated response under the stated rest and relaxation assumptions, although its sign pattern need not have that simple ordering. A coupled two-site extension yields an even more relevant result: the **combined** integral is zero while the two individual site integrals can be nonzero and opposite.

These are ordinary conditional response-model results, not a discovery that pleasure and pain are high-pass signals. To apply them to the user's proposal, the modeled responses would have to be identified with actual felt contributions, the relevant histories and clock measures justified, and the damping, input and endpoint conditions included in a complete physical–experiential constitution. None of that is established by the calculation. Real suffering is not cancelled as an experience or justified by a later or distant positive contribution.

## 1. A causal response rather than a global re-minimization

For a single local system, take

```text
y''(t) + 2 gamma y'(t) + y(t) = x(t),     gamma>0,
q(t) = x(t)-y(t).
```

Here t is a declared internal clock parameter for this restricted system; x is a specified effective input, y a response, and q the signed mismatch. This is a standard type of damped linear response equation. We assume initial conditions and the retarded solution; neither the equation nor its interpretation follows from zero. No claim is made that q is a measured experience or physical energy.

The equation gives

```text
q = y'' + 2 gamma y',
integral_0^T q dt = [y' + 2 gamma y]_0^T.
```

If the system begins at rest and, after a finite-duration input, both y and y' relax back to zero, the complete integral over `0<=t<infinity` is zero. For a bounded, compactly supported input and this stable linear system, the response after the input ends decays exponentially, so the relevant integrals are absolutely convergent. A nontrivial continuous q with finite zero integral must have both positive and negative portions; an initial positive portion is not made unreal by a negative after-response.

This is stronger than simply *imposing* zero as an integral: within the assumed dynamics it follows from the retarded initial condition, finite input and relaxation. Yet those conditions are substantive. The model is an **effective driven, dissipative subsystem**, not automatically a closed account of the whole universe. The physical drive, dissipation, initial state, final relaxation and any surrounding degrees of freedom need explanation.

## 2. An exact positive-and-negative example

Set `gamma=1`, start at rest, and take a unit pulse `x=1` on `0<=t<T`, followed by `x=0`, with `T>0`. During the pulse the exact retarded solution is

```text
y(t)=1-(1+t)e^(-t),
q(t)=(1+t)e^(-t) > 0.
```

After the pulse,

```text
y(t)=(1+t-T)e^(-(t-T))-(1+t)e^(-t) > 0,
q(t)=-y(t) < 0.
```

Both y and y' decay to zero. Direct integration gives

```text
positive integral = 2 - (T+2)e^(-T),
negative integral = -[2 - (T+2)e^(-T)],
complete integral = 0.
```

This works for every finite `T>0`, not just a pulse duration tuned to one oscillation. It is a mathematical illustration of a **signed response**, not evidence that the positive part is pleasure or the after-response is pain. If the field were ever linked to actual experience, the negative part would be a real occurrence in its own right; the equality would not make it ethically harmless.

### Why the endpoint matters

If the input instead remains at `x=1` for all `t>=0`, the same initially resting model has `q(t)=(1+t)e^(-t)` and

```text
integral_0^infinity q dt = 2,
y(infinity)=1,    y'(infinity)=0.
```

A vanishing **derivative** at late times is not enough: the reference state must also return so that the full boundary expression matches. The finite-pulse cancellation depends on the actual whole history including its relaxation tail, not merely the input interval. Choosing a convenient cutoff or declaring that the universe relaxes in this way would not be a derivation.

## 3. Global zero without zero for each site

Now consider a finite connected graph with symmetric nonnegative couplings `c_ij`, and let `L` be its graph Laplacian. Use one declared clock t for this **restricted interacting toy system**:

```text
y_i'' + 2 gamma y_i' + y_i + kappa (L y)_i = x_i(t),
q_i = x_i-y_i,          gamma>0, kappa>0.
```

The graph is an invented model of reciprocal interaction, not an established network of subjects. A common parameter here does not posit a fundamental preferred cosmic foliation, but the model also does not derive relational or relativistic time. The edges need a physical interpretation; an ODE graph by itself is not proof of finite relativistic signal speed.

Assume a finite-duration input, initial rest and relaxation of all y_i and y_i' to zero. Then

```text
q_i = y_i'' + 2 gamma y_i' + kappa (L y)_i,
sum_i integral_0^infinity q_i dt = 0,
```

because the endpoint terms vanish and `sum_i (L y)_i=0`. The zero concerns the complete stipulated collection of site histories. It need not hold for each site separately. For the specified finite symmetric graph and common positive damping, stability follows by diagonalizing L: each mode has positive restoring coefficient `1+kappa lambda_L` and negative-real-part characteristic roots. The endpoint and integrability conditions still have to be appropriate to the physical system one is modelling.

Let `X_i=integral x_i dt` and `Y_i=integral y_i dt`. Under these same endpoint conditions,

```text
(I+kappa L)Y=X,       Q_i=integral q_i dt=X_i-Y_i=kappa (L Y)_i.
```

For two sites joined by one edge, `kappa=1` and an input with total `(X_1,X_2)=(1,0)`,

```text
Y=(2/3,1/3),       (Q_1,Q_2)=(1/3,-1/3),
Q_1+Q_2=0.
```

Thus the combined total can vanish while the two site histories have different nonzero totals. No subject is created by calling a site a subject; even if each site were identified with a subject-incidence history, neither person's experience would be erased or morally offset. The integrals also do not establish a universal cross-subject valence scale.

## 4. Why this is not yet the whole explanation

Several premises can fail without refuting the user's broader proposal:

- **Complete domain and endpoints.** The actual whole may not be an initially resting, finite-input, relaxing system. Infinite activity, sustained inputs, horizons or missing late-time tails can invalidate the integrals or endpoint cancellation. A whole without an outside does not by itself imply these boundary conditions.
- **Dissipation and input.** Damping in an effective model ordinarily entails an environment or other degrees of freedom, while x is an imposed drive in this calculation. Those are not automatically external to reality or a creator, but a self-subsistent whole must account for them and any contributions they carry. A complete conservative realization and its energy balance are not supplied here.
- **Subject and quality.** A signed dynamical mismatch is not itself a felt positive or negative experience. One needs an independently motivated identity linking actual subject fields, q, qualitative content and the chosen clock measure. A negative q need not be suffering.
- **Relativistic locality.** This graph is causal as an initial-value ODE in its declared clock, but that is not the same as an operational no-superluminal-signalling theorem in spacetime. The existing [no-signalling gate](ZERO_TOTALITY_LOCALITY_AND_BOUNDARY_BALANCE.md) requires a physical embedding, controllability and unconditional local readout. An eventual local account must justify those features without assuming a preferred fundamental time.
- **Energy and non-additive alternatives.** The vanishing response integral is not shown to be the global physical energy, a gravitational constraint, or the whole's ontology. A different signed quantity or non-additive zero may require a different construction.
- **No brute remainder.** Even if a physical subsystem obeyed these equations, that alone would not derive the law, subject incidence, the initial conditions or experiential character from zero's self-subsistent nature.

## Result

Causal relaxation provides a concrete *conditional* way for the relevant boundary term to vanish, and internal reciprocal coupling permits an exact zero across histories without requiring each history to have zero total. This improves the causal specificity of the candidate, while leaving the central physical, experiential and foundational identity open. It neither proves the zero-totality thesis nor shows that the no-residue demand is impossible.

## Empirical continuation

The [pain, relief and opponent-process analysis](PAIN_RELIEF_OPPONENT_PROCESS_AND_EXPERIENTIAL_ZERO.md) examines primary experimental evidence and an unequal-gain control: reversal and return to baseline can occur with negative, zero or positive integrated valence. It identifies the equal-gain and measurement assumptions required for an empirical bridge, without treating local results as a verdict on the whole.

## Verification

`python -m unittest verification.causal_relaxation_zero_test -v` checks the pulse formula and integrals, the non-returning counterexample, the two-site integrated response, and a numerical time-domain solution against its exact area identities. These are calculations in stipulated models, not measurements of felt valence or evidence of the universe's boundary conditions.

Related: [locality and boundary balance](ZERO_TOTALITY_LOCALITY_AND_BOUNDARY_BALANCE.md), [relational actual-history constitution](RELATIONAL_ACTUAL_HISTORY_ZERO_CONSTITUTION.md), and [relational-time experiential total](RELATIONAL_TIME_AND_EXPERIENTIAL_TOTAL.md).
