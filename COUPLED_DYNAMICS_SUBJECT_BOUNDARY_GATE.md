# Subject boundaries in one coupled physical dynamics

## Result and scope

This advances the [previous symmetry gate](PLENITUDE_FOUNDATION_GAPS_AND_SYMMETRY.md): the rival subject rules are now applied to the **same explicitly specified interacting stochastic dynamics**, not merely an unchanging graph and a stipulated XOR report. In one weak-coupling regime the rules disagree on whether there is one subject or two. Their physical dynamics and operational reports are nevertheless exactly identical by construction. We then identify what an additional, testable bridge would have to do to discriminate them.

This is a finite classical **diagnostic**, not a brain, a theory of consciousness, a simulated observer, or an account of the whole. Subject incidence is hypothesized, never inferred from a spin. Local update steps are an internal ordering used to describe the toy; they do not posit an external universal clock or a process by which possibility becomes actuality.

The Ising/heat-bath dynamics are standard prior art, not a new physical theory; see [Glauber (1963), DOI 10.1063/1.1703954](https://doi.org/10.1063/1.1703954). Both connectivity-based subject rules below are intentionally simple benchmarks; neither implements integrated information theory (IIT). IIT's actual exclusion and causal-structure proposals are more demanding; see the [IIT overview](https://iep.utm.edu/integrated-information-theory-of-consciousness/) and the [critique of its exclusion principle](https://pmc.ncbi.nlm.nih.gov/articles/PMC4574706/). No literature-wide novelty is claimed for the general problem of operationally indistinguishable phenomenal assignments.

## 1. One system, two subject rules

Take four binary spins `s_i ∈ {−1,+1}` in a line, with dimensionless couplings:

```
0 — K — 1 — G — 2 — K — 3
```

The two outer pairs are the candidate local modules. Let `k=tanh K=1/2` and `t=tanh G`, with `0≤t<1`. There is no field. The standard equilibrium distribution is

```
P_t(s) = exp[K(s0 s1+s2 s3)+G s1 s2] / Z
       = 1/16 (1+k s0 s1)(1+t s1 s2)(1+k s2 s3).
```

These equalities apply to the unclamped chain. For a hard clamp, restrict to configurations matching the fixed spins and renormalize. The dynamics are local asynchronous heat-bath updates: choose an unclamped vertex uniformly and resample it from its conditional Gibbs distribution. If every vertex is clamped, no update occurs. The verifier checks detailed balance exactly, using rational arithmetic, for every allowed transition in each tested clamp condition. It does not model heating, finite settling time, backreaction or biological mechanisms.

Compare the following **stipulated, relabeling-invariant** mappings on the *unclamped* weighted interaction graph:

- **Positive-connectivity rule `C`:** one subject per connected component after retaining every edge with `tanh(coupling)>0`.
- **Threshold rule `T`:** one subject per component after retaining edges with `tanh(coupling)>3/8`.

Neither rule supplies phenomenal qualities, persistence or an independent reason for its cutoff. The `3/8` value is chosen to make the comparison transparent; it is not a physiological threshold. These rules attribute subjects to components as a hypothesis, not as a consequence of their existence. We do not silently extend the rules to subjects *during* a clamp: a hard intervention changes the effective dynamics and would require its own subject-incidence analysis.

| Cross coupling `t` | `C` subjects | `T` subjects | Endpoint correlation `E[s0 s3]` | `P(s0=s3)` |
|---:|---:|---:|---:|---:|
| `0` | 2 | 2 | `0` | `1/2` |
| `1/4` | 1 | 2 | `1/16` | `17/32` |
| `3/4` | 1 | 1 | `3/16` | `19/32` |

The correlation formula is `k²t=t/4`: on this tree, each edge transmits the spin correlation by its `tanh` coupling. With an endpoint hard-clamped to either sign and the rest allowed to equilibrate, the probability that the other endpoint matches is the same table value. Thus the toy has a clear physical response to changing coupling. That response does **not** by itself decide which component rule, if either, corresponds to phenomenal subjecthood.

## 2. Controlled observations: physical access is not yet subject unity

For each of the three couplings, the verifier exhausts all `3^4=81` hard-clamp settings (each spin unclamped, clamped `−1`, or clamped `+1`) and all allowed states. It verifies `1,536` exact detailed-balance equalities across the cases. It also computes distributions for the two endpoint reports and a joint parity bit, `R=1` exactly when the endpoint signs differ.

Both subject rules receive exactly the same physical probability distribution and the same report readout. Hence they predict identical endpoint and parity statistics for each clamp setting **by the stipulated construction**. The parity is an ideal function of the two endpoint readouts, not a separately modeled physical processor. Such a joint parity report demonstrates access to a relation between the values; it does not establish that there is one phenomenal subject rather than two subjects whose information reaches a shared processor. Conversely, the absence of such a report would not by itself prove two subjects. Our earlier [shared-versus-independent report audit](TWO_REPORTS_CONSENSUS_AND_REVERSAL.md) already addresses related common-source and consensus pitfalls.

### The general operational-equivalence point

More generally, suppose two ontological proposals share:

1. an initial physical-state distribution;
2. a physical transition kernel for every allowed intervention;
3. a report/readout kernel for every allowed intervention;
4. the same rule by which experimental interventions are selected from previous observations.

Then the joint distribution of every **finite adaptive intervention–report history** is the same under both proposals. This follows by multiplying the same initial, intervention, transition and readout conditional probabilities along each history. Thus no experiment using only these shared observables distinguishes *that pair of specified proposals*. This is not a universal impossibility theorem for subject theories: theories with different physical or report predictions can be distinguished, and independent phenomenal or constitutive premises could make the physical predictions differ.

The finite code checks stationary clamps and detailed balance; the general adaptive statement is a separate elementary induction, **not** a numerical test of all possible interventions or a claim about human experiments.

## 3. An exact sharp-boundary versus finite-evidence tension

For the unclamped finite chain, all outcome probabilities vary smoothly in `t`, but rule `C` changes its subject count from two to one as soon as `t` becomes positive. Rule `T` changes at its stipulated `3/8` cutoff. A discrete count can jump even as physical probabilities change smoothly; this is not a contradiction or evidence that either rule is false. But the framework must explain why its particular boundary and apparent discontinuity are warranted, or adopt a different account of subject identity/gradation. Simply calling every nonzero coupling “unity” would group weakly coupled systems without explaining the subjective consequence.

The diagnostic can be made quantitative. For full-state, independent equilibrium snapshots from the same toy chain,

```
TV(P_t, P_0) = t/2.
```

The Kullback–Leibler divergence is

```
D(P_t || P_0) = [(1+t) ln(1+t)+(1−t) ln(1−t)]/2.
```

For `n` independent snapshots, KL divergences add. Pinsker's inequality gives an upper bound on total variation, which gives a lower bound on the optimal equal-prior error of deciding `t=0` versus a **known** `t>0` from those snapshots. For `t=1/65536` and `n=10,000`, that error is at least approximately `0.49962`. Even perfect state readouts thus hardly distinguish those two physical conditions under this restricted protocol, though `C` assigns different subject counts.

This bound concerns a specific iid equilibrium experiment and two specified physical parameter values; it does not cover time-resolved trajectories, adaptive control, unknown nuisance parameters, or all methods of detecting coupling. It does not independently observe subject count or show that its value is unknowable in principle. The analysis is comparative mathematics, not an assertion of genuinely possible unactualized global worlds under the user's modal thesis.

## 4. How to turn disagreement into a test rather than a relabeling

The subject rules alone carry no distinct report law. For an empirical distinction, each side must propose and defend an **independent bridge** from subject constitution to observable records. A useful preregistered structure is:

1. Define subject candidates and physical partitions independently of the subject's eventual responses. Specify what counts as one simultaneous subject versus two subjects communicating, including whether overlap and persistence are allowed.
2. Randomly present independently generated stimuli to two channels; minimize direct and indirect cross-cueing and record all relevant accessible outputs. Use appropriate timing, calibrations and a prespecified common-source/communication model. The data must be able to distinguish information access from a common stimulus or delayed communication.
3. Fix a jointly specified comparison task and predictions **before** inspection. For illustration only, if one complete theory-plus-bridge predicted joint-report accuracy at most `0.60` and another at least `0.80`, a threshold of `0.70` on `185` independent comparable trials has each tail bounded by `exp(−2·185·0.1²)<0.025` by Hoeffding's inequality. These are hypothetical margins, not predictions of rules `C` or `T`, estimated effects, or a complete clinical power analysis. Real serial dependence, missing data, multiplicity, bias and uncertainty in controls need their own treatment.
4. Separately validate the inference from the operational report to joint experience. Without that additional bridge, detecting shared information processing does not identify a subject count. If plausible alternatives make identical report predictions, register that fact as underdetermination.

For empirical context, [Pinto et al. (2017)](https://doi.org/10.1093/brain/aww358) report split perception together with cross-field responses in patients and argue for undivided consciousness; subsequent [discussion](https://pmc.ncbi.nlm.nih.gov/articles/PMC6057762/) disputes the interpretation. This does not validate either toy subject rule or settle subject count from the reports. Any patient research requires ethical review and must not suggest clinical procedures for the sake of this hypothesis.

## 5. Connection back to necessary plenitude

The target remains one self-sufficient, intrinsically experiential actuality with plural subjects, not one externally simulated universe. This work does not supply its essence or make it actual. It isolates a specific obligation: **a plural-subject theory must say what constitutes a subject and why, rather than borrow subject boundaries from arbitrary graph connectivity.**

Similarly, the Gibbs probabilities above describe an ideal physical ensemble conditional on supplied dynamics. They are not a measure over genuinely possible worlds, not a probability that reality becomes actual, and not a derived indexical measure. Deriving a legitimate subject measure depends on first identifying what its subjects or subject-moments are. Physical parameter variation and hard clamps are local comparative tools; they neither require an external time nor settle which complete global descriptions are genuinely possible.

The immediate next constructive task is to replace these benchmark boundary rules with independently motivated candidate constitution rules that address unity, persistence and phenomenal content, then identify whether their physical/report bridges actually differ. The other foundational problems—necessity, intrinsic experience, non-optimality, quantum/spacetime recovery and a self-location measure—remain open; this finite model does not solve them.

## Verification

Run `python verification/coupled_subject_boundary_gate.py`. The [receipt](verification/coupled_subject_boundary_gate.json) records exact fractions, all coupling cases, the detailed-balance count and the bounded finite-snapshot calculation. The script has no nonstandard dependencies. Passing checks establish only the finite mathematics and stated implementation.
