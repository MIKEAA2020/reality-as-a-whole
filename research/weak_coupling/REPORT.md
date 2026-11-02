# Constructive step 9: weak coupling, finite exposure, and the exact-core discontinuity

## Verdict

The exact-core-to-unity conjecture is not ready to serve as an independently justified constitutive principle. This round identifies a precise reason: **arbitrarily weak effective coupling changes its discrete boundary verdict while finite-horizon physical predictions approach the uncoupled case continuously**.

This is not an empirical refutation of phenomenal discontinuities. A theory may posit such a discontinuity. But the causal graph does not independently justify it, and an arbitrary coupling threshold does not repair the missing bridge.

The positive result is an exact separation of:

- structural interaction;
- interaction detectable over a specified exposure;
- actual interaction events;
- and the still-unjustified phenomenal unity verdict.

**24 new tests pass; all 222 tests across the nine constructive rounds pass.** No phenomenological measurements were collected.

## 1. An exact weak-effective-coupling family

Use the previous two-bit source:

\[
A(x,y)=(y,x\oplus y).
\]

Define a Markov transition kernel:

\[
K_\varepsilon=(1-\varepsilon)I+\varepsilon A,
\qquad 0\le\varepsilon\le1.
\]

At each tick, the system remains unchanged with probability 1−ε or applies A with probability ε. This model specifies independent update choices across ticks.

**Scope:** small ε means rare full-strength coupled updates, not small-amplitude continuous interaction. The results apply exactly to this effective stochastic family. They do not establish a universal quantitative law for weak neural, electromagnetic, or mechanical coupling. The model also does not establish that the stochastic description is ontologically fundamental rather than a coarse description of a fuller realization.

At ε=0 there are two independent persistent bits. At ε=1 the previous deterministic source is recovered.

All intermediate kernels preserve the uniform state distribution, so instantaneous statistical independence again fails to reveal the causal organization.

## 2. A core boundary changes at every positive coupling

Measure one-step causal influence from coordinate i to j by the maximum total-variation change in the next j distribution after surgically flipping current i while holding the other coordinate fixed.

The two cross-influences are exactly:

\[
\operatorname{Influence}(x\to y)=\varepsilon,
\qquad
\operatorname{Influence}(y\to x)=\varepsilon.
\]

Thus:

- at ε=0 the coordinate graph has two separate components;
- at every ε>0 it has one reciprocal component.

This is a change in the exact support of the intervention law. It does not depend on whether a coupling event happens during a particular observed trajectory.

A separate four-vertex graph demonstrates the same boundary issue for two pre-existing cores: any positive reciprocal bridge merges them when every positive influence is admitted. This is an illustrative graph construction, not a measured brain network or an application of the full stochastic factorization test to that four-vertex graph.

## 3. Nonfactorization is not merely an arrow artifact

For the two-bit stochastic family, test all 24 static encodings of its four states. For each encoding, ask whether the transition kernel factors into two independent binary Markov kernels with locally determined marginals.

At ε=0, all 24 encodings factor because the transition is identity.

At every positive ε, no encoding factors.

### Argument for the entire positive interval

The state 00 is absorbing. The other three states form a communicating class: they cycle under A, with optional waiting when ε<1.

Suppose a static encoding turns the kernel into a product of two binary kernels. The encoded absorbing state (a,b) forces a to be absorbing in the first component and b in the second. A state (a,1−b) then cannot reach any state whose first component is 1−a.

But the other three encoded states must communicate with each other, including such a state. Contradiction. ∎

The tests enumerate representative rational values, including very small ε. The proof, rather than a finite parameter grid, establishes the full interval claim.

So the candidate's discontinuity survives the stronger static factorization criterion used in the previous rounds. It is not fixed merely by replacing graph connectivity with this exact nonfactorization test.

## 4. Yet the kernels approach the product continuously

The worst-case one-step total-variation distance from the uncoupled kernel is:

\[
\max_s\operatorname{TV}(K_\varepsilon(s,\cdot),K_0(s,\cdot))
=\varepsilon.
\]

The equality is attained at any nonfixed source state. At 00 the kernels agree for all ε.

Therefore nonfactorable kernels can be arbitrarily close to a factorable kernel. Exact irreducibility is a categorical property, not a lower bound on interaction strength or an experimentally justified unity threshold.

## 5. Exact finite-horizon distinguishability

Start at a nonfixed state, such as 01, and observe the **entire path** for T ticks.

Under zero coupling, the path is constant. Under positive coupling, the path stays constant exactly when no A update occurs. The total-variation distance between the two full-path distributions is therefore:

\[
D_T(\varepsilon)=1-(1-\varepsilon)^T.
\]

Consequently:

\[
D_T(\varepsilon)\le \min(1,T\varepsilon),
\qquad
\lim_{\varepsilon\to0}D_T(\varepsilon)=0
\]

for every fixed finite T.

For 0<ε<1, the no-change path has positive probability under both hypotheses. No finite path observation supplies a universally error-free distinction between zero coupling and every positive coupling. Observing a change can reject zero coupling in this ideal noiseless family; failing to observe one cannot establish exact zero.

This is a limitation of finite evidence, not proof that the systems are physically identical.

### Example

At ε=1/1000:

- 10 ticks give D≈0.00996;
- 1000 ticks give D≈0.6323.

The exact core is merged in both protocols. Its resolvability differs substantially because the observation exposure differs.

These distances compare physical path laws. They are not degrees of consciousness or probabilities that an observer exists.

## 6. Endpoint measurements can miss the entire interaction history

Because A has order three, after N coupled updates the endpoint depends on N modulo three.

The endpoint distance from the zero-coupling endpoint is:

\[
D_T^{\mathrm{end}}(\varepsilon)
=\sum_{\substack{0\le n\le T\\n\not\equiv0\ (\mathrm{mod}\ 3)}}
\binom Tn\varepsilon^n(1-\varepsilon)^{T-n}.
\]

This is at most the full-path distance.

An extreme control is ε=1 and T=3:

- every intermediate tick changes the state;
- the endpoint returns exactly to the starting state;
- full-path distance is 1;
- endpoint distance is 0.

A stable endpoint does not establish absence of a constitutively relevant intermediate process. Conversely, a detected intermediate interaction does not establish phenomenal unity.

Starting at 00 produces no difference at all in either observation scheme. A useful protocol must include an informative state or intervention, not merely longer passive observation.

## 7. The exact-core robustness trilemma

Consider three commitments:

1. **Separation at zero:** the uncoupled pair is assigned separate episode supports.
2. **Unity from every positive exact core:** every ε>0 is assigned one support because its dynamics are nonfactorable and reciprocally coupled.
3. **Boundary stability:** sufficiently small changes in the physical law around ε=0 preserve that discrete episode assignment.

They cannot all hold. The kernels approach K₀ continuously, while commitments 1 and 2 force a different discrete verdict arbitrarily near it.

This is a conditional incompatibility, not a proof that commitment 3 is a universal metaphysical necessity. A genuine phenomenal boundary might be discontinuous. But accepting that possibility is not the same as independently explaining why this particular discontinuity should occur at exact zero coupling.

Options must therefore be stated openly:

- accept the discontinuity and justify its phenomenal significance;
- reject exact nonfactorization as a sufficient unity criterion;
- reject the proposed separation verdict for independent processes;
- or supply a different, independently motivated account of constitutive boundaries.

The present evidence supports **withholding the sufficiency claim**. It does not select a replacement psychophysical law.

## 8. Why a threshold does not solve the bridge

A graph can be thresholded: keep only influences greater than λ. In the illustrative two-core graph, a bridge of strength ε merges the components when λ<ε and is removed when λ≥ε.

This makes the verdict depend on λ. It does not derive λ.

An operational resolution criterion can be stated without pretending otherwise. If a study chooses a full-path separation target δ, then the present model requires:

\[
1-(1-\varepsilon)^T\ge\delta.
\]

Equivalently, for T>0:

\[
\varepsilon\ge1-(1-\delta)^{1/T}.
\]

Here δ is a declared experimental criterion and T is the exposure. Neither is a derived phenomenal unity threshold. Total-variation separation is also not automatically the power of a specific noisy measurement procedure; actual observations can discard information.

For N independent paths of T ticks from nonfixed starting states, the corresponding full-path distance is:

\[
1-(1-\varepsilon)^{NT}.
\]

Additional exposure can improve physical identification. It does not transform the chosen resolution criterion into an ontological boundary.

## 9. Laws, interaction events, and actual episodes

The occurrence-first distinction matters here.

For every ε>0, the **law** permits reciprocal interaction and is nonfactorable. But a particular finite trajectory can contain no coupled update at all.

These are different claims:

- the system has a disposition to interact;
- an interaction event actually occurred in the selected interval;
- a unified phenomenal presentation actually occurred.

The model establishes the first and gives probabilities for the second. It does not establish the third.

A constitutive theory may legitimately refer to counterfactual powers rather than only events realized on one path. But then it must explain why those powers constitute this actual episode, including when no coupling event occurs during its proposed duration. It cannot silently substitute a property of a probability law for the actuality of experience.

Nor may a sampled path be treated as a complete physical realization if hidden gates, clocks, or environmental conditions have been omitted from the effective kernel. A fuller realization can require a larger constitutive scope or a different autonomy analysis.

## 10. Implication for the larger programme

The exact-core criterion solved one limited problem: it distinguished a passive copied representation from implementing the source's intervention structure.

It does not yet solve unity. If promoted to a universal rule, arbitrarily weak reciprocal bridges can merge candidate cores. In sufficiently connected models that may produce boundaries far larger than the locally warranted episode. Whether this actually occurs in brains or a whole-world model is not established here.

Exact autonomy is also demanding for open systems. The correct response is not to declare irrelevant inputs absent, or to choose a threshold until the desired subject appears. The relevance and temporal scope must be independently argued.

The surviving constructive constraints are therefore:

- preserve actual-token and law/type distinctions;
- explain differentiated contents and incidence separately;
- use interventions rather than observational copies to characterize implementation;
- disclose the temporal domain and what finite data can distinguish;
- do not derive a categorical unity boundary from a continuous interaction quantity without an additional justified principle.

## 11. A better next research target

The next useful step is **boundary identifiability under uncertainty**, rather than another asserted boundary law.

Given independently calibrated physical data and a declared observation protocol:

1. determine which coupling/process models remain compatible;
2. compute which candidate constitutive boundaries are shared by all compatible models;
3. report an unresolved boundary where the compatible models disagree;
4. keep that epistemic uncertainty separate from phenomenal indeterminacy;
5. ask what independently warranted episode contrast, additional intervention, or constitutive principle would resolve it.

This will not manufacture a unity law. It would prevent the programme from claiming exact subjects from data that cannot even establish exact causal separation.

The parallel explanatory task remains open: justify why a particular concrete interaction organization constitutes co-presentation, rather than merely increasing communication, coordination, or report access.

## Reproducibility

- `model.py`: rational Markov kernels, total variation, causal influence, static stochastic factorization, exact path/endpoint formulas, propagation, and illustrative threshold graphs.
- `test_model.py`: 24 tests.
- `enumeration.json`: generated numeric summary and exact small-case checks.
- `results.log`: observed test output.

```bash
# This round
cd research/weak_coupling
python -m unittest -v test_model.py

# Entire sequence, from repository root
python research/run_checks.py
```

**Observed verification:** 24 new tests pass; 222 tests pass across the nine research rounds. Parameter-grid tests complement the stated interval proofs; they do not replace them. No experiment on actual experience was conducted.

### Final constructive verdict

Exact causal nonfactorization distinguishes implementation from passive representation but does not independently justify a robust phenomenal boundary. The weak-coupling family makes the remaining burden explicit: a unity discontinuity, a constitutive strength/temporal criterion, or another boundary principle must be justified—not hidden in graph construction, sampling, or a threshold. Until then, report a conditional candidate and a boundary-identification set rather than a derived subject.

## Subsequent boundary-identification work

[Constructive step 10](../boundary_identifiability/REPORT.md) implements compatible parameter intervals and boundary sets, explicit ideal/noisy access channels, non-amalgamating must/may links, and an audit of prior mass at exact zero coupling. It preserves uncertainty rather than treating nondetection or merged possibilities as an established boundary.
