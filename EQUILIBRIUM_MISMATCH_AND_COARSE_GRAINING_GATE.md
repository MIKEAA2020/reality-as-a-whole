# Can equilibrium statistics reveal experiential mismatch?

## Result

There is a second conditional route to the state-excess candidate, complementary to the [net-response route](NET_RESPONSE_STATE_MISMATCH_WORK_GATE.md): if the **complete microstates** of a fixed system really follow a canonical Gibbs distribution with a known energy scale, then their relative stationary probabilities determine the excess above the minimum. This could avoid measuring every interaction or integrating a force path.

But the strongest obstruction is not merely measurement noise. We construct two finite equilibrium systems with the **same visible probabilities, the same visible dynamics and the same response to an entire family of visible-coordinate interventions**, while their microscopic excesses differ. The visible distribution determines the same **coarse-grained free energy** in both, not the same microscopic excess. An independently justified choice of which level the experiential hypothesis concerns is therefore essential.

This is a model result, not a discovery of a new statistical-mechanics law, observation in a brain, or evidence that either kind of excess is uncomfortable. Gibbs weighting and the role of multiplicity are standard: see the [MIT Boltzmann-distribution notes](https://ocw.mit.edu/courses/res-8-010-introduction-to-statistical-physics-summer-2018/mitres_8_010su18_lec6.pdf). Coarse-graining and hidden entropy production are well-established concerns; see the [2024 single-molecule analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC11331124/). The contribution here is to apply them to the project's particular **state-excess and experiential-identity** problem, with an explicit controlled observational equivalence.

## 1. The conditional positive result

Let a finite declared microstate space have costs `E_i`, minimum `E_min`, and positive canonical probabilities

```text
π_i = exp(−E_i/θ) / Σ_j exp(−E_j/θ),      θ > 0.
```

`θ` is a known energy scale (for a thermal system it may be `k_B T`), not an independently assumed cosmic temperature. Define the candidate state excess `D_i=E_i−E_min`. Then the standard Gibbs relation gives

```text
D_i = θ log(π_max / π_i),       π_max = max_j π_j.       (1)
```

This identifies **the excess of the cost appearing in the canonical law** from exact microstate probabilities and θ, without measuring channels or finding a separate global force path. It assumes the full declared state space, a correct reference measure with one equally weighted count per microstate, stationarity and the canonical model. If θ is unknown, only `D_i/θ` is fixed: jointly rescaling E and θ leaves the distribution unchanged. For continuous variables a density is defined relative to a reference measure; densities and their modes transform with coordinates, so a bare `−log density` is not a coordinate-free microscopic energy.

Most importantly, an experimentally estimated stationary distribution can always be written *formally* as a Gibbs-like expression by defining a surrogate `−θ log π`. That algebra alone does **not** establish a physical energy, equilibrium, or identity with the proposed mismatch. Nor does equation (1) establish any subject, feeling or self-sufficient experiential ground.

### Conditional finite uncertainty bound

Suppose all true microstate probabilities satisfy a **jointly valid** set of positive bounds `0<l_i≤π_i≤u_i`, and `0<θ_lo≤θ≤θ_hi` in matching units. Then a conservative interval for each excess is

```text
D_i ≥ θ_lo max{0, log[(max_j l_j)/u_i]},
D_i ≤ θ_hi log[(max_j u_j)/l_i].                   (2)
```

This is just monotonicity and the fact that `π_max≥π_i`. The marginal bounds need not be independent, but their coverage must be joint; they must actually be compatible with a normalized distribution. Bounds including zero give no finite logarithmic upper bound. If the maximum is taken only over observed states, an unobserved, higher-probability microstate can alter the result; a complete-support or missing-mass argument is a separate requirement.

For a **hypothetical** true distribution `(1/2,1/3,1/6)`, `θ=1`, and simultaneous absolute probability bounds of `0.01` for each state, formula (2) gives `D_2∈[1.02014,1.18029]`, containing the exact `log 3≈1.09861`. The interval is only as valid as the probability, full-state-space and Gibbs assumptions. Estimating probabilities under correlated observations, drift, rare states and adaptive selection needs an appropriate statistical procedure; none is supplied here.

## 2. Exact hidden-state counterexample

Let the observable state `x` be 0, 1 or 2 and define `g=(3,2,1)`. Use energy units `θ=1`. Compare two fixed physical models:

| Model | Microstates over visible x | Baseline microstate cost | Visible probability | Baseline microscopic `D` |
|---|---|---|---|---|
| A | one per x | `E_A(x)=log(3/g_x)` | `(1/2,1/3,1/6)` | `(0, log(3/2), log 3)` |
| B | `g_x` distinct microstates per x | `E_B(x,h)=0` for all six | `(1/2,1/3,1/6)` | `(0,0,0)` |

Both models are canonical at the same θ. The microstates in B are stipulated distinct physical states hidden by the observable map, **not just renamed copies of one state**. Model B's visible probabilities differ because there are different numbers of hidden states in each visible class. Model A's probabilities differ because its visible states have different costs. Neither is asserted to be a neural model.

Both yield the same visible potential of mean force or coarse free-energy differences, `log(3/g_x)`, relative to x=0. Thus the common observable excess derived from (1) is Model A's microscopic excess but Model B's **coarse free-energy excess**, not Model B's microscopic excess. This makes precise the [previous report's](NET_RESPONSE_STATE_MISMATCH_WORK_GATE.md) warning: a measured effective potential is not automatically the microscopic mismatch postulated by an identity theory.

### Interventions and visible dynamics

To make the comparison stronger than matching a single histogram, impose a visible-state energy perturbation `V_x` that affects every hidden microstate in class x equally, and define `w_x=exp(−V_x)>0`. At each fixed intervention, the visible equilibrium distribution is in **both** models

```text
π_x(V) = g_x w_x / Σ_y g_y w_y.                   (3)
```

Choose an explicit idealized reset kernel: at each discrete step, the system samples its next microstate from the equilibrium distribution associated with the selected V, regardless of its previous microstate. Each fixed-control microscopic chain obeys detailed balance and has visible transition probabilities `P(x→y|V)=π_y(V)` in both models. Under an adaptive control rule chosen from previous **visible** observations, their next-visible-state distributions therefore remain equal. With the same initial visible distribution, induction gives identical distributions for any finite visible history under these stipulated reset kernels and this class of controls. The controlled experiments are mathematical model operations, not assertions about achievable biological interventions. Arbitrary feedback or time-varying control need not itself be an equilibrium process.

The [verifier](verification/equilibrium_mismatch_coarse_graining.py) checks all 27 weight vectors from `{1/2,1,2}³`, detailed balance at each fixed control, and all 2,187 four-state visible histories for 27 policies selecting among three fixed controls based on the previous visible state. The general arbitrary-history claim follows from equality of the specified kernels, not from that finite enumeration.

**Scope:** these models need not have the same full physical state, and hidden-sensitive probes can distinguish them. This is not an assertion of equivalence under every possible intervention. A reliable, independently anchored subjective/report measurement might also favor one concrete experiential bridge over another; neither model by itself supplies such a measurement or predicts its result. The example instead shows that the declared visible physical records and controls do not fix the chosen microscopic D.

## 3. Stationarity is not detailed balance

A stationary histogram alone is weaker than equilibrium. In a separate three-state Markov example use the same π=`(1/2,1/3,1/6)` and define stationary probability flows `F_ij=π_i P_ij`:

```text
reversible:                  circulating:
[5/12   1/24   1/24]        [5/12   1/16   1/48]
[1/24   1/4    1/24]        [1/48   1/4    1/16]
[1/24   1/24   1/12]        [1/16   1/48   1/12]
```

In both matrices every row and column sums to π, so the normalized transition matrix has the same stationary distribution. The first is symmetric and detailed-balanced; the second has a net cycle flow. Its standard stationary **information-theoretic** time-reversal asymmetry is `log(3)/8≈0.13733` nats per step. An actual physical entropy-production interpretation requires additional assumptions about the state variables, time reversal and dynamics. This established distinction between steady states and detailed balance is discussed, for example, in the [Markov/spike-train review](https://www.mdpi.com/1099-4300/21/9/884).

Full transition data distinguish **these two** chains, whereas the histogram does not. Conversely, visible detailed balance need not prove hidden microscopic reversibility. A nonequilibrium process can also have a stationary distribution with the numerical form of a Gibbs law, so a detected current rejects an equilibrium-dynamics claim but does not by itself show that no useful potential can be defined. Sparse samples, noisy state identification, time-reversal parity, coarse-graining, hidden variables and nonstationarity all complicate real tests.

## 4. What this means for substrate independence and the whole

The proposal seeks an experiential ground and local plural subjects, not a universal agent. If it says **microscopic** D determines unpleasantness, it must say what physical organization counts as a microstate and why its cost, rather than an observationally matching coarse free energy, is the relevant intrinsic structure. If instead it says **coarse free-energy** excess determines unpleasantness, it owes an independently justified coarse-graining, reference measure, thermal or effective scale and domain. These are different hypotheses with different commitments. Treating every description or arbitrary binning as a new real microstate would make either measure representation-dependent; actual physical equivalence must be justified rather than assumed.

The strong actuality thesis says all genuinely possible local realities are actual within the whole; it does **not** by itself determine either the Gibbs probabilities above or a subject-location measure. The model's stationary distributions are stipulated local statistical laws, not measures derived by counting actual possibilities, and the local step index is not an external clock for a timeless whole. The prior [plenitude/measure gate](RELATIONAL_PLENITUDE_HISTORY_AND_MEASURE.md) addresses this independent issue.

A next empirical decision must therefore identify:

1. The local physical state space and experimentally invariant reference measure; whether hidden states are relevant and how missing-state uncertainty is bounded.
2. A physically justified equilibrium or nonequilibrium model and independent calibration of the scale θ. Matching a histogram, or merely checking one zero current, is insufficient.
3. Whether the intended quantity is microscopic excess, coarse free-energy excess, structural frustration or another invariant, and whether measuring it requires interventions that alter the state under study.
4. Independently measured unpleasantness and nonpain controls, plus prespecified held-out comparisons against stimulus/context and established predictors. Neither an apparently successful state-cost predictor nor an equilibrium model establishes a phenomenal identity.

If these conditions cannot be supported, the correct result is **unidentified**. The framework's justification of self-subsistence, experiential ground, subject constitution, physical law and local time remains open. There is no implication that an already self-sufficient whole needs an external cause.

## Reproduction

Run `python verification/equilibrium_mismatch_coarse_graining.py`; the [receipt](verification/equilibrium_mismatch_coarse_graining.json) gives the exact flow matrices, model excesses, control/path counts, conditional numerical interval, and **15,000 seeded interval-containment checks**. The general identity and equivalence follow from the stated algebra and kernels, not the random tests. No external dataset was downloaded and no real experiences were measured.
