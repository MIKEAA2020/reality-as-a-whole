# Constructive step 1: constitutive contrast covariance

## Result in brief

This round tests a specific bridge rather than proposing another name for the whole:

> **A change in phenomenal organization must be accounted for by a difference in the constitution of the occurrence. A change confined to reporting or passive representation is not, by that fact alone, a change in the experienced organization.**

Two parts require different evidential statuses:

1. **Explanatory contrast principle:** a complete account cannot explain distinct outcomes through a constitution it treats as identical in every explanatorily relevant respect. This is a necessary constraint on explanatory sufficiency, independently motivated by the zero-residue requirement.
2. **Local constitutive hypothesis:** in a specified episode, a particular content-transition organization—not its downstream report channel—accounts for particular phenomenal contrasts. This is a substantive, falsifiable psychophysical proposal. It is not proved by the first principle.

A finite model makes the proposal precise, derives relational and reporting consequences, and survives a bounded realization-token test suite. **Thirty tests pass.** It does not derive consciousness, actual occurrence anchors, or the local hypothesis from first principles.

The advance is a constrained, two-sided bridge with an explicit failure criterion. It is not the independently sufficient ultimate principle the larger programme still seeks.

---

## 1. What can be independently justified

Let a theory attribute phenomenal organization \(E\) to a concrete constitution \(C\). If it claims to explain why two cases have different \(E\), its explanatory account must distinguish those cases somewhere relevant. If all its explanatory inputs remain identical while the explained difference varies freely, the theory has not fully explained that difference.

Schematically, a sufficiently specified deterministic constitutive account must supply

\[
C\mapsto E
\]

rather than merely a set of freely selectable \(E\)'s. A probabilistic account may explain an outcome distribution instead, but it must identify that weaker target and justify the probability structure. It must not silently claim an explanation of a particular qualitative contrast that it does not determine.

This argument does **not** establish physicalism. The complete constitution could include phenomenal or neutral intrinsic features. It does not show that everything physical is phenomenally relevant, that all phenomenal facts are relational, or that one neuroscience model is sufficient.

It does rule out calling a proposed account complete while leaving its phenomenal assignment independently adjustable and unexplained.

The independently defensible principle is therefore a **constraint on constitutive explanation**. The missing substantive question is what concrete nature satisfies it.

## 2. The candidate substantive bridge

For one already delimited candidate episode, specify:

- a physical content-state set \(Q\);
- independently defined interventions \(G\) on those states;
- a phenomenal distinction set \(\mathcal E\), characterized separately;
- a proposed correspondence \(f:Q\to\mathcal E\).

The bridge hypothesis is:

> The relations among these experienced distinctions correspond to the relations among the relevant concrete content states, and appropriately calibrated changes of the process transform those relations covariantly.

In an action-based formulation, where both sides' actions have independent meaning,

\[
f(gq)=\widehat g\,f(q).
\]

The implementation below tests a weaker, precisely delimited form: preservation of adjacency and nonadjacency in independently supplied contrast graphs. It does not assume a phenomenal action \(\widehat g\) exists for every physical intervention.

Crucially, this is not the claim that any internally represented distinction is felt. It is a proposal about the relational constitution of a candidate episode. The occurrence's phenomenality, its boundary, and the relevance of this state description require further justification.

## 3. A bounded model with two separately specified sides

### Physical side

A four-state content process has states \(Q=\{0,1,2,3\}\) and primitive reversible changes

\[
q\mapsto q+1\pmod4,\qquad q\mapsto q-1\pmod4.
\]

These changes define the cycle graph \(C_4\). Its shortest-path distances are zero for identity, one for neighbors, and two for opposite states.

The distance counts primitive changes. It is not an independently derived physical duration or experienced distance. Changing which interventions count as elementary changes the model and must be recorded.

### Phenomenal side

A separate synthetic target contains four distinguishable appearances \(A,B,C,D\), with adjacency judgments forming another cycle. These constraints stand in for a possible independently obtained phenomenological dataset.

They are **not actual human measurements**. They are not obtained by defining \(A\) as physical state zero, nor by replacing experience with report equivalence. Conversely, providing a separate graph does not establish that such a phenomenal organization is actually instantiated.

### Bridge test

Enumerate bijections preserving both adjacency and nonadjacency. There are eight.

This shows two things at once:

- The bridge is restrictive: a nonisomorphic phenomenal graph can refute it.
- Structural matching alone does not choose an absolute qualitative labeling.

The precise symmetry results are:

| Calibration data | Remaining maps |
|---|---:|
| None | 8 |
| \(0\leftrightarrow A\) | 2 |
| \(0\leftrightarrow A,1\leftrightarrow B\) | 1 |
| \(0\leftrightarrow A,2\leftrightarrow C\) | 2 |
| Physical neighbors mapped to phenomenal opposites | 0 |

Two adjacent calibrations can fix the remaining map. Their explanatory cost is explicit: they are cross-domain bridge data, not conclusions from bare physical structure.

Every admitted graph map preserves shortest-path distance. Thus, **if the bridge is correct**, the model explains a relational constraint without assigning every pairwise relation independently.

This is conditional explanatory compression. It does not establish that experienced distance equals graph distance in general, or explain why the episode has a particular intrinsic quality.

The automated test of the remaining mapped labels is a logical consequence of the already supplied graph and anchors. It is **not an empirical held-out validation**. A real study must withhold relevant phenomenal observations before fitting or selecting the bridge.

## 4. A two-sided consequence: reporting noise need not alter phenomenal geometry

Append a downstream report channel. With probability \(\eta\), the channel replaces its output with a uniformly random report among the four labels; otherwise it reports the content state correctly:

\[
p(r\mid q,\eta)=(1-\eta)\mathbf1_{r=q}+\eta/4.
\]

This is a causal restriction, not just a naming convention: the report channel has no feedback into the content process over the modeled episode.

For distinct contents \(q,q'\), the total-variation distance between reports is

\[
\operatorname{TV}\bigl(p(\cdot\mid q,\eta),p(\cdot\mid q',\eta)\bigr)=1-\eta.
\]

With equal priors for a binary discrimination task, optimal report-based accuracy is

\[
P_{\rm correct}=\frac{1+\operatorname{TV}}2=1-\eta/2.
\]

Consequently, accuracy falls from one to chance while the content-transition graph stays fixed.

The distinction is now exact:

- **Established physical/model result:** the specified report statistics change while the content dynamics do not.
- **Phenomenal consequence of the bridge hypothesis:** the modeled relational experience remains the same, even though evidence accessible through that report channel degrades.

Thus the proposal makes a discriminating prediction: **an impairment genuinely confined to downstream reporting need not compress phenomenal contrast**.

This is not the unqualified assertion that neural noise leaves experience unchanged. A second model allows the supposed nuisance to affect content:

\[
q'=(q+u+z)\pmod4.
\]

Changing \(z\) now changes content. The invariance claim no longer applies. The test suite exhibits this failure, preventing the rule from treating all inconvenient noise effects as irrelevant.

The example also shows why report Fisher geometry or report discriminability cannot automatically be identified with phenomenal similarity. A reporting channel can change them without changing the proposed constitutive content organization.

## 5. What this explains—and what it does not

The same specified content organization now does two jobs under the bridge:

1. **Public role:** determines the content's transformations and the distributions produced by an attached report channel.
2. **Phenomenal role:** constrains a relational contrast structure and its invariance under modifications genuinely outside the proposed constitutive content.

That is the two-sided explanatory target. It is narrower than a derivation of experience from physical vocabulary.

An opponent can agree with every physical calculation and deny that the content process has experience, deny that its phenomenal geometry is the graph geometry, or propose a richer constitutive state. This work has not eliminated those alternatives.

It has, however, made their disagreement exact. The issue is no longer merely “why does processing feel?” It includes:

> Does this independently specified organization determine these independently characterized phenomenal relations, including their preservation under the specified reporting perturbation?

A mismatch cannot be repaired simply by relabeling the report output as experience. It requires rejecting or revising the bridge, its state description, or the causal scope assumption, with the added dependency recorded.

## 6. Realization-token stress tests

The candidate is evaluated locally on **supplied anchored role-segments**, not treated as an observer counter. A role certificate records concrete update-event blocks, a trajectory, storage metadata, and a descriptive layer.

Those anchors are witnesses imported from an occurrence account. The present model does not derive their actuality or adequacy.

| Case | Test result | Scope |
|---|---|---|
| Duplicate description | No new anchored role | Numerical role witness, not proof of subject identity |
| Host/emulator/target descriptions of one anchor | No extra role merely from layer labels | No claim every physical emulator is phenomenally inert |
| Separate duplicate with distinct anchors | Two supplied role occurrences retained | Does not establish that either is conscious |
| Hidden copy | Local profile can agree while total supplied list differs | Does not infer the entire population from a local interface |
| Passive event renaming | Witness transported through explicit provenance | Provenance is supplied, not inferred from identical values |
| Moving storage | A time-indexed readout follows one lane through rotating locations | A transported content lane is not automatically a subject |
| Shared control | Separate supplied roles are not merged solely by a common control | Constitutive/enabling status of control remains open |
| Split/merge | Continuation is not treated as identity equivalence | Does not decide personal survival |
| Temporal resampling | Endpoint protocol can change the candidate graph | No unearned claim of grain invariance |
| Physical reblocking of events | Different certificate unless a further justified correspondence is supplied | No silent identity across changes in contribution unit |

These tests block obvious incompatibilities with the earlier realization programme. They do **not** solve the earlier programme's unresolved inputs.

The construction respects the distinction

\[
q:\text{state alternatives}\to\text{predictive types}
\quad\ne\quad
\tau:\text{actual occurrences}\to\text{organizational types}.
\]

It also assigns no self-locating weight to occurrences. The equal priors in the binary-report calculation belong to an explicitly specified decision task, not a population-selection argument.

## 7. Independent motivation is not independent sufficiency

The crucial status distinction is:

| Claim | Status after this round |
|---|---|
| A complete account must explain a phenomenal difference through relevant distinguishing constitution | Independently motivated necessary explanatory constraint |
| Actual experience need not have the same concepts as its physical process | Compatible with the identity programme; not established identity |
| The four-state content graph matches the synthetic phenomenal graph | Exact conditional correspondence calculation |
| Downstream report noise changes discrimination without changing modeled content | Derived from explicit dynamics and channel assumptions |
| The same perturbation preserves phenomenal contrast | Testable consequence of the substantive bridge; not empirically established |
| Event provenance distinguishes descriptions from additional roles | Implemented relative to supplied witnesses |
| These witnesses identify actual phenomenal subjects | Not established |
| This local constitution explains its own actuality or necessity | Not established |

The exercise does not meet the strongest reading of “an independently justified constitutive principle” yet. It supplies an independently defensible constraint and a concrete constitutive hypothesis with consequences on both sides. The remaining sufficiency claim is exposed rather than concealed.

That is a constructive outcome, not an impossibility verdict. Nor should failure to complete the bridge be hidden behind thirty successful implementation checks.

## 8. An empirical validation design, rather than invented evidence

A suitable empirical study would require a much richer neurobiological model. Its logical design can nevertheless be specified now:

1. **Fix scope before fitting.** Define the candidate episode, content variables, allowed interventions, temporal window, and report pathway. Identify what could violate the no-feedback assumption.
2. **Characterize phenomenology independently.** Obtain contrast, similarity, and co-presence judgments without defining them as task accuracy. Record uncertainty and reliability rather than treating introspection as infallible.
3. **Fit only designated calibration data.** Keep independent phenomenal relations or perturbation conditions out of the fitting stage. Structural agreement calculated from a full supplied graph is not a new prediction.
4. **Manipulate reporting separately from candidate content.** Prefer perturbations whose location can be independently established. A late motor/report disruption is a possible methodological direction, not a guarantee of phenomenally irrelevant intervention.
5. **Compare three hypotheses.** Contrast the constitutive-content account with an account identifying phenomenal geometry with report discriminability, and with a richer account in which the intervention changes content or its constitutive context.
6. **Use convergent evidence.** Delayed calibrated judgments and retained records might help, but they introduce memory assumptions. A no-report measure cannot establish phenomenality by naming itself a phenomenal measure.
7. **Predeclare failures.** Reject the simple bridge if independently justified contrasts disagree with its graph invariants. Revise the nuisance classification if a causal route into content is demonstrated; do not retroactively relocate every mismatch without evidence.

At complete report erasure, the model's claim that experience persists cannot be directly validated through that erased channel. Lack of observed disagreement is not confirmation. Other evidence would be required, with its own assumptions stated.

No measurements have been collected in this round.

## 9. Next mathematical and constitutive obligations

The next step should strengthen exactly one missing implication:

\[
\text{independently characterized occurrence}
\overset{?}{\Longrightarrow}
\text{this content organization is phenomenally sufficient}.
\]

There are two particularly useful tests:

- **Boundary extension:** retain the same local contrast graph while varying recurrent bodily, affective, memory, or controller context. Determine which changes the candidate regards as constitutive, and why. This directly tests whether the local state is too thin.
- **Residual qualitative freedom:** preserve every justified physical and phenomenal relation used so far. Ask whether inequivalent qualitative profiles remain. Do not dismiss them as labels unless equivalence is defended. A surviving family limits what this relational bridge explains.

An improved principle must account for the experience-relevant intervention family and the local occurrence scope rather than borrow them indefinitely. It must also connect to the global actuality obligation. This model does neither by fiat.

## 10. Delivery and reproducibility

Files in this folder:

- `model.py`: standard-library-only finite model, graph correspondences, report channel, and supplied occurrence certificates.
- `test_model.py`: 30 tests, including counterexamples and expected non-identification.
- `results.log`: actual test run.
- `assumptions.csv`: explicit inputs and their limits; not a claim that a table verifies its own entries.

Run:

```bash
cd research/contrast_covariance
python -m unittest -v test_model.py
```

**Observed result:** 30 tests passed, exit code 0. The tests check finite mathematics and bookkeeping, not whether any toy system is conscious.

### Final constructive verdict

> The first candidate worth retaining is **constitutive contrast covariance**, qualified by an explicitly defended occurrence scope. It offers a way for one concrete organization to explain public transformation structure and constrain phenomenal relations while distinguishing experience from reporting. Its finite implementation respects the known realization-token limits and supplies clear refutation conditions. The independent explanatory constraint is justified; the substantive psychophysical sufficiency is not yet justified independently. The project has advanced from a unifying aspiration to a bounded bridge that can fail, not from an aspiration to a completed metaphysics.

## Subsequent boundary test

[Constructive step 2](../contextual_constitution/REPORT.md) tests the scope of this candidate. It shows why a restricted content correspondence must not be promoted to comprehensive phenomenal sufficiency without contextual and temporal contrast completeness. The original restricted result is preserved; the broader sufficiency claim remains open.
