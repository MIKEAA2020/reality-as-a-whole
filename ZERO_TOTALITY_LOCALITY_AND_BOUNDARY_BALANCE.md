# Can zero balance be locally realized without superluminal signalling?

## The question and the result

**Causal continuation:** [relaxation and boundary balance](ZERO_TOTALITY_CAUSAL_RELAXATION_AND_BOUNDARY.md) derives zero for a specified stable, retarded response to a finite pulse and gives a coupled example with nonzero individual but zero combined history integrals.

The [actual-history candidate](RELATIONAL_ACTUAL_HISTORY_ZERO_CONSTITUTION.md) achieved a conditional zero using whole-domain means. Does that require an action-at-a-distance, or could the balance arise from local relations instead?

A constructive alternative is possible **within a specified model**: replace the global mean coupling with local reciprocal interactions. Their internal contributions cancel when summed, leaving an exact zero under a stationarity and no-source condition. A local continuum analogue also gives zero **only if the net boundary contribution vanishes**. Neither result follows merely from saying the whole is closed, and neither identifies the resulting signed field with experience.

There is also an important causal qualification. A globally defined stationary relation can make one part's mathematical value depend on distant inputs; that is a **constraint on possible models**, not by itself an operational signal. A conflict with no-signalling follows only if the distant change can be independently controlled in the required spacetime arrangement and produces a distinguishable unconditional local record. An actual relativistic physical theory and a physical–experiential readout would have to decide this.

## 1. The whole-mean candidate has a global dependence

For the preceding model's y-minimized response,

```text
q_i = [k/(1+k)] (x_i - xbar),
xbar = sum_j w_j x_j / sum_j w_j.
```

Holding the other x values fixed, changing `x_j` by delta changes another `q_i` by

```text
Delta q_i = -[k/(1+k)] [w_j/sum_l w_l] delta,    i != j.
```

This is a dependence of the **modeled stationary solution** on its input, with fixed weights. It is not automatically a process occurring in time or a physical intervention. In particular, re-minimization changes y as well; comparing the solutions does not hold the complete local physical–experiential state fixed.

For the previous three equal-weight example with `k=1`, the two inputs below are both global minima of its stated functional, with the same parameters:

```text
x  = (2,-1,-1),   y  = (1,-1/2,-1/2), q  = (1,-1/2,-1/2);
x' = (2,-1, 2),   y' = (3/2,0,3/2),   q' = (1/2,-1,1/2).
```

Both have the required variance `R=2`, zero total q and `F=-1`. Changing only the third x entry **as a comparison of inputs** is accompanied by different y and q at the other entries. Whether both complete configurations are genuinely physically possible, whether the third input is controllable while other relevant preparations are held fixed, and whether the entries can represent spacelike-separated occurrences are additional questions. Under the user's strong possibility–actuality proposal, mathematical substitution is not automatically a genuine same-token counterfactual; suitably controlled **distinct actual contexts** are another possible basis for comparison. See [actuality and interventions](ACTUALITY_CAUSAL_INFERENCE_AND_BELL.md).

## 2. A local-interaction candidate

Let actual incidence sites `i` have fixed positive weights `w_i`, and let `c_ij=c_ji>=0` be stipulated couplings on a finite graph; absent edges have zero coupling. For fixed x, suppose the y-part of the constitution is

```text
F_y = 1/2 sum_i w_i (x_i-y_i)²
    + kappa/2 sum_(i<j) c_ij (y_i-y_j)²,      kappa>0.
```

At an independently admissible stationary variation of each y_i,

```text
w_i(y_i-x_i) + kappa sum_j c_ij(y_i-y_j) = 0.
```

Define `q_i=x_i-y_i`. Summing the equations cancels each internal edge contribution with its reverse:

```text
sum_i w_i q_i = 0.
```

This is a zero **over the stipulated actual weighted sites**, not an expectation over alternatives. It is compatible with nonzero individual q. The mathematical mechanism generalizes the earlier [intrinsic accounting principle](ZERO_TOTALITY_INTRINSIC_RELATIONAL_ACCOUNTING.md): here edge contributions follow from a specified local functional and stationary solution, rather than being fitted independently to the q list.

The graph must be given a physical interpretation before “local” has spacetime meaning. A nearest-neighbor action is not automatically a relativistically causal dynamics, and q is not a felt valence merely by definition. The stationary x profile, weights, graph, couplings, admissible variation and relevant subject incidences are still inputs. The model does not derive the functional or its no-source condition from zero's nature.

### A three-site local example

Take unit weights, unit nearest-neighbor couplings on `1—2—3`, and `x=(2,-1,-1)`. The unique stationary solution is

```text
y = (7/8,-1/4,-5/8),
q = (9/8,-3/4,-3/8),     sum q=0.
```

No equal-and-opposite pointwise pairing is required. For fixed x, the quadratic is strictly convex, so this is the unique y-minimum. It is not a claim that x is itself dynamically realized, that the sites are subjects, or that these numbers measure suffering.

Although the functional has only nearest-neighbor edges, the stationary solution has an indirect end-to-end dependence: changing `x_3` by delta changes `y_1` by `delta/8`, hence changes `q_1` by `-delta/8`, after re-solving the full stationary equations. This illustrates the difference between a **local functional** and a local *operational response*: equilibrium or a boundary-value solution can encode long-range correlations. The calculation by itself supplies no intervention, propagation time, retarded solution or signal.

If the graph has disconnected components, the same proof yields zero separately in each component. This is stronger than global balance and may be inappropriate if separately experienced components are supposed to have nonzero individual totals. Adding an independently specified source term `-sum_i w_i J_i y_i` changes the result to `sum_i w_i q_i=-sum_i w_i J_i`. An internal source is not automatically an external creator; the physical account must explain whether it exists and why its net contribution vanishes.

## 3. A local spacetime analogue and its boundary term

In an illustrative Lorentzian region with metric signature `(-,+,+,+)`, let x and y be real scalar fields and assume the local action

```text
S_y = integral sqrt(|g|) [-1/2 (x-y)² - kappa/2 (nabla y)²] d⁴x.
```

Here `(nabla y)²=g^(ab) nabla_a y nabla_b y`. Vary y at fixed x. The Euler–Lagrange equation is

```text
q := x-y = -kappa box y.
```

Integrating over a suitable finite spacetime region and applying the divergence theorem gives

```text
integral q sqrt(|g|) d⁴x
   = -kappa integral_boundary n^a nabla_a y dSigma,
```

with the usual oriented boundary convention, for a sufficiently regular region with suitable non-null boundary pieces. The integral of q is zero **if the net flux on the complete boundary is zero**. A closed spatial boundary alone does not guarantee this: initial and final time boundaries may contribute. A boundaryless compact model, imposed no-flux conditions, or a limit with vanishing boundary flux could provide the condition only if separately justified and mathematically admissible; compact Lorentzian models can have causal pathologies and are not assumed to describe our universe. Infinite integrals, quantum constraints, the physical measure and clock emergence need further work.

This action is a local mathematical analogue, not an asserted effective action for consciousness, gravity or the actual universe. Holding x fixed for this variation does not explain x or make it an external creator; a complete theory must also specify its own equation or constitutive role. A stationary action need not be an energy minimum. A local classical equation does not alone establish a consistent relativistic quantum theory or an experiential identity.

### One-clock boundary control

For a one-dimensional proper-time illustration with `kappa=1` and `0<=tau<=1`, the same sign convention gives `q=y''`. Choose

```text
y(tau)=tau²(1-tau)²,
q(tau)=2-12 tau+12 tau²,
x(tau)=y(tau)+q(tau).
```

Here `y'(0)=y'(1)=0`, so `integral_0^1 q d tau=0`, while q is positive near both ends and negative near the middle. This is a specified field history, not an actual measured subject; x was constructed from y for the illustration, so it is not independent evidence for the law. With `y=tau²` and `x=y+2`, the same local equation holds but the integral is `2`, because the endpoint flux is nonzero. Thus **locality and the equation alone do not force zero**.

## 4. A scoped no-signalling gate

Standard finite-dimensional quantum theory supplies a benchmark: for a bipartite state `rho_AB` and an unconditional trace-preserving operation `Lambda_B` applied only to B,

```text
Tr_B[(I_A tensor Lambda_B)(rho_AB)] = Tr_B(rho_AB).
```

Therefore an ordinary local operation on B does not change the unconditional statistics of an A-only measurement in that isolated bipartite comparison. Conditioning on a particular B outcome can change A's conditional state, but the selection record must be available before that conditional distribution can be used; it is not automatically a signal. This does not decide a quantum-gravity theory, a metaphysical subject measure, or every kind of nonlocal correlation.

For the present candidate, a no-signalling conflict would follow **only if all** of the following are shown in a physically specified regime:

1. the relevant A and B operations and records are suitably spacelike separated and B's setting is independently controllable in the comparison;
2. the model's predicted difference in A's q corresponds to a real difference in A's experiential/physical state with an independently supported, locally available readout or report;
3. the change affects A's **unconditional** local record distribution, not only a sample selected using B's later record;
4. preparations, possible common causes, causal paths and measurement assumptions are controlled sufficiently to identify the claimed effect.

If those premises hold and the local distributions differ, the specified mapping conflicts with operational no-signalling in that regime. If they are not established, the stationary mathematical dependence is a warning and research question, not evidence that a person can signal superluminally. An actual qualitative difference may exist without a proven reliable report; conversely, a report difference is not by itself proof of the proposed phenomenology. See the existing [subject-weight and no-signalling gate](SUBJECT_WEIGHT_STEERING_AND_NO_SIGNALLING_GATE.md) for a distinct postselection comparison.

## 5. Foundational consequence

The local-interaction and boundary versions give a positive route worth investigating: global zero could express a single internal relation among actual local contributions, without an external balancer, a preferred foliation, or the erasure of suffering. Their local equations can have nonzero contributions of both signs.

What remains is decisive: derive the appropriate domain, the physical and experiential identity of q, its subject incidence and scale, the local dynamics, the required boundary condition, and their unity from the whole's own nature. A vanishing formal boundary flux is not automatically an explanation of why there is experience or why the whole is self-subsistent. The models neither prove nor disprove the user's stronger zero-totality thesis, and a failed locality proposal would not rule out a different non-additive or emergent-spacetime account.

## Verification

`python -m unittest verification.zero_locality_boundary_test -v` checks the two whole-mean minima, the nearest-neighbor stationary solution and its sensitivity, the one-clock boundary integrals, and a finite Bell-state no-signalling/postselection control. These checks validate stipulated mathematical models, not actual experience, genuine physical interventions or the universe's energy.

Related: [actual-history zero constitution](RELATIONAL_ACTUAL_HISTORY_ZERO_CONSTITUTION.md), [relational experiential total](RELATIONAL_TIME_AND_EXPERIENTIAL_TOTAL.md), and [subject-weight no-signalling](SUBJECT_WEIGHT_STEERING_AND_NO_SIGNALLING_GATE.md).
