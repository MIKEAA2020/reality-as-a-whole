# Step 40 — A concrete causal-exclusion candidate: successes and failure modes

## Outcome

A specified maximal-irreducibility selector performs better than the earlier “any positive connection merges systems” rule in two supplied physical fixtures. It selects the recurrent source rather than its passive monitor, and preserves two strong cores under a weak bridge. At stronger coupling it selects the whole.

However, this particular proxy also gives positive integration to a transient feedforward copy and changes its verdict when the same mechanism is sampled at a different temporal grain. Its physical coordinates, averaging distribution, time step, and exclusion rule are supplied assumptions. Its qualitative identity postulate remains unsupported.

**Therefore it is not the discovered unified account.** It is a concrete candidate component with a declared rule, derived predictions, and exposed limitations—not another unnamed appeal to integration.

This is an IIT-style research candidate only in the broad sense of intrinsic causal organization and exclusion by irreducibility. It is **not an implementation or test of IIT 4.0**, and its counterexamples must not be reported as refutations of that theory.

## 1. The proposed unifying hypothesis

The candidate has three commitments:

1. **Non-additive identity:** an episode is hypothesized to be the intrinsic qualitative occurrence of an actually realized causal organization, not an extra agent attached to its representation.
2. **Causal exclusion:** its physical incidence is provisionally selected by irreducibility exceeding that of overlapping candidate organizations.
3. **Structural content:** qualitative differentiation is hypothesized to correspond to the full realized cause/effect organization and current condition, not just to the scalar integration score.

Commitment 1 is motivated only conditionally by the earlier non-additive argument. Commitments 2 and 3 are substantive hypotheses, not consequences of that argument. Their truth cannot be established by successful causal graph calculations alone.

To test commitment 2 rather than leave it verbal, the executable version fixes finite Boolean coordinates and one update step. It computes the following proxy from transition probabilities rather than supplying a desired ranking.

## 2. Operational definition of the proxy

Let K(y|x) be a kernel on n declared physical bits. For a region S, define its effective kernel by averaging external **inputs** uniformly and marginalizing external outputs:

\[
K_S(y_S\mid x_S)=2^{-|\bar S|}
\sum_{x_{\bar S}}\sum_{y_{\bar S}}K(y\mid x).
\]

This is a specified interventional convention, not the actual state's marginal dynamics in general. Uniform external interventions are a modeling choice, not a theorem about intrinsic probability or a physical steady state.

For each nontrivial partition S=A∪B, sever cross-input dependence by averaging it out separately and form

\[
K^{A|B}_{\rm cut}(y_S\mid x_S)
=K_A(y_A\mid x_A)K_B(y_B\mid x_B).
\]

The score is

\[
\phi(S)=\min_{A|B}\frac1{2^{|S|}}\sum_{x_S}
\operatorname{TV}\bigl(K_S(\cdot\mid x_S),
K^{A|B}_{\rm cut}(\cdot\mid x_S)\bigr).
\]

Total variation has a standard finite probability meaning: it quantifies maximal event-probability difference for a fixed input. That gives the score a physical operational interpretation. It does not give it phenomenal authority. Averaging over inputs, taking the minimum cut, assigning singleton score zero, and comparing overlapping regions are additional declared choices.

The candidate selector retains S with φ(S)>0 if no overlapping region has strictly greater score. Equal overlapping maxima remain alternatives, not automatically multiple simultaneous subjects. Numerical tolerance is used only for floating-point comparisons; no positive phenomenological threshold is introduced.

Thus this rule avoids an externally tuned “coupling above ε₀” cutoff, but is not assumption-free or a completed unique Γ.

## 3. Source versus passive monitor

Use the existing source

\[
A(x,y)=(y,x\oplus y)
\]

and passive monitor

\[
F(x,y,u,v)=(A(x,y),A(x,y)).
\]

Exhaustive kernel calculation gives:

| Region | Score |
|---|---:|
| Source {x,y} | 0.75 |
| Monitor {u,v} alone | 0 |
| Whole source-plus-monitor | 0.5 |

The sole selected region is the source. These values are calculated from the stated transition law and cuts, not assigned consciousness scores.

This is a bounded success against the intended source/monitor discriminator. It does not establish that the source is conscious, nor that all passive-copy arrangements are excluded. It also does not independently justify why the source's causal organization should constitute a quality.

## 4. Weak and strong bridges between two cores

Start with two independent A sources. After their parallel update, swap one output bit from each core with probability ε. This declares an actual stochastic transition family; it is not a general model of weak brain coupling. All regional kernels and cuts are recalculated for each ε.

| Bridge ε | Core score (each) | Whole score | Selected regions |
|---:|---:|---:|---|
| 0 | 0.75 | 0 | Two cores |
| .001 | .7495 | .001 | Two cores |
| .1 | .7 | .0975 | Two cores |
| .5 | .5 | .4375 | Two cores |
| 1 | .5 | .75 | Whole |

In the tested family the selection changes between ε=.55 and ε=.6. The switch is determined by the score comparison, not by an independently chosen positive coupling cutoff. It still depends on the choice of score and exclusion rule.

This shows concretely that an exact boundary rule need not merge systems at every positive interaction strength. It does not show that the particular score crossover corresponds to an actual change of subjects. That remains the missing phenomenal identification.

## 5. Severe checks: what the proxy does not solve

### A. Positive score without recurrent organization

For the feedforward update F(x,y)=(0,x), there is no feedback dependency loop. Yet the two-bit region scores .5 and is selected. The effect kernel changes when its single cross-link is severed; that is sufficient for a positive proxy score.

If recurrence or bidirectional intrinsic causal availability is part of the intended constitutive criterion, this proxy does not implement it. One could instead posit experience for that transient feedforward organization, but that would be an additional phenomenal claim, not a prediction supported by the fixture.

We record the result rather than modifying the score after seeing it. It is a failure of the proxy as a general recurrence discriminator, not an empirical demonstration that the selected feedforward process lacks experience.

### B. Temporal-grain dependence

The source A has period three: A³=I. Its one-step score is .75, but its three-step effective kernel scores 0. Thus the same underlying process receives different proxy verdicts when its intermediate transitions are discarded.

Three-step sampling is not an invertible re-description of the entire time-resolved process. Therefore this is not a contradiction under genuine full process equivalence. It shows that the candidate needs a physically and constitutionally justified temporal grain—or a law on the time-resolved process that does not discard constitutive operations. It cannot equate “one update in the supplied table” with intrinsic episode duration without further argument.

### C. State and qualitative identification

The score averages across all interventions and is independent of the current state. A qualitative law would need more than this number, including the appropriate realized state and full organization. Merely saying that the full organization “is” experience does not identify which quality it is or explain why it is phenomenal.

The earlier relabeling and equivalence audits still apply. Exclusion does not supply χ, and quotienting a causal description does not by itself establish qualitative identity.

### D. Physical scope

The implementation assumes a finite tensor decomposition into declared bits. It does not define the same measure for continuum local algebras, derive an intrinsic elementary time scale, recover QFT, or connect twistor or Langlands constructions to phenomenology. In continuum and quantum settings, allowed interventions, subsystem structure, cut operations, and comparison measures require their own definitions and justification.

The earlier field-theory results cannot be counted as tests of this new consciousness postulate merely because both use mathematical descriptions of processes.

## 6. What genuine progress this attempt provides

The work moves from “some composition law is needed” to a specific score and selector with computed successes and explicit counterexamples. It demonstrates a possible mechanism for avoiding the weak-link merger without an externally tuned coupling threshold.

But it also prevents an unjustified promotion: this proxy is not a defensible universal episode law at its present scope. It cannot be made one just by naming its maxima conscious. A revised theory would need independently motivated treatment of temporal grain, intrinsic cause and effect, the qualitative identity, and actual realization—not unlimited post-hoc repairs.

The candidate's survival on two fixtures is a structural consistency result. Its failures do not settle the truth of all exclusion-based consciousness theories. Neither result selects a complete unifying account.

## 7. Verification and next decision

`model.py` computes regional kernels, cut distances, scores, and overlapping maxima. Sixteen tests check normalization, exact fixture values, weak-link stability, strong-link selection, physical bit-relabeling covariance, and the feedforward and temporal-grain counterexamples. The last two tests pass by detecting the limitations; passing the software suite is not passing every theoretical requirement. `enumeration.json` records the full score tables.

The correct decision is to retain **non-additive realized-process identity** as a candidate architecture and this calculation as a bounded exclusion experiment, but not accept the proxy as Γ or claim a solved χ. We have not found the unified account. The attempt has produced a concrete candidate component, some useful behavior, and specific reasons it is insufficient.
