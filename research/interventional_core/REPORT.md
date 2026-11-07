# Constructive step 7: an interventionally closed core versus a copied representation

## Main result

A passive monitor can copy every ordinary state and transition of a source without implementing the source's independently perturbable causal organization. This round constructs and exhaustively tests that distinction.

The positive result is a **physical structural discriminator**: a source supports a closed, irreducible transition system across the stipulated intervention domain; its passive monitor does not. The same observational state geometry therefore need not entail the same constitutive credentials.

The corresponding phenomenal claim remains a **candidate identity restriction**, not a theorem: an episode might be constituted by an actual interventionally organized process rather than by an arbitrary representation of its states. Neither recurrence nor irreducibility is established here as necessary or sufficient for experience.

**24 new tests pass. All 174 tests across the seven constructive rounds pass.**

## 1. The constructive advance over annotation-only models

The previous round held the physical model fixed while varying its phenomenal annotation. Unsurprisingly, physical observations alone could not discriminate annotation-only differences.

This round does something different: it tests whether two proposed physical realizers actually share the same causal structure. If they do not, identifying either one with a target episode has different intervention consequences once the phenomenal bridge is specified.

The independently justified requirement is limited but substantial:

> A proposed model of a process's causal organization must preserve the dependencies across its claimed intervention domain—not merely fit a restricted set of synchronized trajectories.

This is a requirement for an accurate causal abstraction. It does not already assert which causal organization is phenomenal.

## 2. Source and monitor

Define a two-bit source A:

\[
A(x,y)=(y,x\oplus y).
\]

Add two monitor bits u and v, updated as copies of the source's next values:

\[
F(x,y,u,v)=(y,x\oplus y,y,x\oplus y).
\]

The input domain contains all 16 four-bit states. A surgical intervention changes one coordinate while holding the others fixed before the next update.

On the synchronous domain

\[
D=\{(x,y,u,v):u=x,\ v=y\},
\]

the source and monitor have exactly the same states and transition histories. Every initial state enters D after one update.

A researcher using only ordinary synchronized observations can therefore reconstruct the same apparent four-state transition geometry from either pair.

But that observational agreement does not survive independent monitor perturbations.

## 3. Closure under projection

Let \(q_S\) project onto (x,y), and \(q_M\) onto (u,v).

For the source:

\[
q_S\circ F=A\circ q_S
\]

on the entire 16-state domain. Its next state is determined by its own current state.

For the monitor:

\[
q_M\circ F=A\circ q_M
\]

holds only on D. It fails at all 12 nonsynchronous states.

This is not merely failure to match one proposed monitor transition rule. There is **no deterministic autonomous monitor transition rule on the full domain**: the same current (u,v) can have different next (u,v), depending on the unrepresented source state.

Thus the monitor's projected state is not sufficient to describe its own future under the admitted interventions.

The monitor still realizes a physical copying process. What it does not realize by itself is the autonomous source dynamics it represents.

## 4. Intervention consequences

A monitor-bit override:

- changes its current physical state;
- does not change the source's future;
- is completely overwritten at the next update.

A source-bit override:

- changes the source's next state;
- changes the monitor's next state;
- propagates through the source dynamics.

These facts hold across every state in the finite domain, not merely selected examples.

This strengthens the source/monitor distinction beyond an observational isomorphism. It does not, by itself, imply that overriding the monitor leaves experience unchanged: that latter prediction still depends on the phenomenal identification.

## 5. Reciprocal dependence and autonomous supports

With coordinates numbered x=0, y=1, u=2, v=3, the one-step influence edges are:

\[
x\to y,v;\qquad y\to x,y,u,v.
\]

The strongly connected components are:

\[
\{x,y\},\quad\{u\},\quad\{v\}.
\]

The nonempty autonomous coordinate sets are exactly:

\[
\{x,y\},\quad\{x,y,u\},\quad\{x,y,v\},\quad\{x,y,u,v\}.
\]

The source pair is therefore the unique inclusion-minimal autonomous coordinate support in this circuit. Neither source bit alone closes dynamically. The monitor pair does not close at all.

This is a physical boundary result relative to the supplied variables, domain, update schedule, and surgical operations. It is not a subject-boundary theorem. Larger systems can contain several such supports; two independent source pairs produce two minimal physical cores without establishing that there are two subjects.

## 6. Stronger than reciprocal arrows: an exact factorization test

A causal graph can look reciprocal because of its coordinate choice. Accordingly, test a stronger dynamical question:

> Can any static bijective encoding of the four source states turn A into two independent binary transition maps?

There are 24 encodings and 16 pairs of unary binary maps, giving 384 comparisons. None factorizes A.

### General argument for this instance

A is bijective, fixes 00, and cycles the other three states:

\[
01\to11\to10\to01.
\]

Hence its permutation order is three.

If it were conjugate to a product of two independent binary maps, both component maps would have to be bijections. Each binary permutation has order one or two. Their product has order at most two, contradicting A's order three. ∎

This establishes irreducibility into two autonomous binary factors under **all static state encodings**, not merely a failure to split the original x and y coordinates.

It does not establish phenomenal unity. The same transition system can be described as a single four-state register: one fixed state and a three-phase cycle. A small clock can have this mathematics. The factorization result is about a specified transition system and proposed 2×2 decomposition, not an independent demonstration of multiple contents becoming one experience.

## 7. Why arbitrary coding invariance is too strong

Three controls prevent treating the physical discriminator as an absolute unity metric.

### A. Mixed-coordinate encoding

Change coordinates to source state plus monitor error:

\[
(x,y,e_u,e_v)=(x,y,u\oplus x,v\oplus y).
\]

Then the circuit becomes:

\[
(x,y,e_u,e_v)\mapsto(A(x,y),0,0).
\]

The copied-state dependency arrows disappear from the error coordinates. This is an invertible encoding of the same global dynamics.

Changing an error bit at fixed source corresponds to changing a monitor bit. But changing a source bit at fixed error also changes the corresponding original monitor bit. Thus independent single-coordinate interventions in the new encoding are not the original independent single-coordinate interventions. A causal graph must be interpreted together with its intervention algebra.

The tests establish graph covariance under ordinary coordinate renaming. They deliberately do **not** claim graph invariance under arbitrary encodings that mix physical variables.

### B. Temporal coarse-graining

\[
A^3=\mathrm{id}.
\]

Observed once every three ticks, the source appears to be two independently persistent bits. Every one of the 24 static encodings then admits a factorization into binary identity maps.

An intervention between samples reveals dependencies that endpoint observations miss. Endpoint identity does not imply absence of intermediate causal organization.

Consequently, irreducibility at a selected sampling interval cannot identify a phenomenal duration by itself. The relevant temporal grain requires independent justification.

### C. Time-dependent recoding

For a freely evolving source, define:

\[
z_t=A^{-t}s_t.
\]

Then \(z_{t+1}=z_t\). The dynamics have been made formally stationary by a clock-dependent encoding.

This does not remove the original physical interactions. It changes the meaning of the coordinates and of fixed interventions with time. Permitting arbitrary such transformations without transporting the intervention structure would trivialize many claims about dynamics.

The appropriate object is therefore not a bare state graph but **an actual process with its temporal and intervention organization**.

## 8. A sharpened constitutive candidate

The working candidate can now be stated more carefully:

> A proposed constitutive identification should match an independently characterized episode to the concrete process that implements the relevant contrast transformations across the warranted intervention and temporal domain—not merely to another variable whose ordinary states encode those transformations.

For this circuit, the source qualifies as a closed implementation of A; the monitor pair qualifies only as its driven representation.

A stronger psychophysical hypothesis would say that an actual episode is constituted by a particular interventionally closed, appropriately irreducible process. This would predict, subject to calibration:

- alterations of its constitutive contrasts when the relevant source organization is perturbed;
- no corresponding alteration from a genuinely nonfeedback monitor perturbation;
- preservation under passive coordinate renaming;
- no multiplication of the episode simply because another monitor is attached.

**These are conditional phenomenal predictions, not observed results.** Their warrant cannot come from defining experience as the source state. Independent target evidence must support the contrast mapping and intervention reliability.

Nor does this candidate establish that every experience is dynamically autonomous, recurrent, or irreducible in this sense. Inputs, attention, memory, environmental coupling, or a richer constitutive domain may be essential. Imposing autonomy as a universal necessary condition would be a substantive additional premise.

## 9. What it explains on the physical side—and what is still missing

The model explains why ordinary source/monitor trajectory agreement is compatible with sharply different perturbation responses. It derives a minimal closed support and a genuine static dynamical nonfactorization result. Those are independently checkable physical/mathematical achievements.

On the phenomenal side it supplies a more restrictive hypothesis, not an achieved explanation. It distinguishes **implementing transformations** from **representing their outcomes**, but it has not demonstrated that phenomenal unity is identical to the former.

In particular, independently variable phenomenal features need not imply dynamically independent subexperiences. Conversely, dynamically irreducible registers need not imply any experience. The correspondence between physical factorization and phenomenal separability must be argued or tested, not assumed.

The candidate therefore improves the constitutive programme's specificity without meeting its full zero-residue objective.

## 10. Realization-token and duplication limits

A copied representation is not an additional implementation of the represented autonomous dynamics merely because it matches their trajectory. That is the new limited distinction.

It does not follow that simulation cannot realize experience. A simulation that actually implements the relevant causal/counterfactual organization is different from a passive monitor under the proposed criterion. Whether that implemented organization is sufficient for experience remains open.

Likewise, two genuinely independent realizations of A would both instantiate its physical organization, unlike one source plus a passive copy. This does not derive a phenomenal occurrence count, duplicate weighting, or a self-location probability.

The tests enumerate abstract states and encodings. They do not create warranted observer tokens, establish an actual phenomenal episode, or explain why the physical laws or their occurrences exist.

## 11. Where the next decisive work lies

The key remaining question is now precise:

> Is the independently characterized organization of a unified presentation matched by implemented interventional closure and irreducibility, or can it persist through physical factorization that the candidate treats as constitutively significant?

A useful next investigation would compare two targets that the present model does not identify:

1. **phenomenal differentiation:** which contents or qualities can vary independently;
2. **phenomenal unity:** which differentiated contents occur together in one presentation.

If the same irreducibility criterion is made to explain both without respecting their difference, it will likely conflate differentiated content with divided experience. That is the next adversarial test for the candidate, rather than another assumption of unity from a connected graph.

## Reproducibility

- `model.py`: source/monitor dynamics, surgical perturbations, intervention influence graph, strongly connected components, autonomous supports, static factorization search, and coordinate transformations.
- `test_model.py`: 24 tests, including exhaustive domain checks, all 24 coordinate renamings, factorization, temporal aliasing, mixed encoding, and independent duplicate cores.
- `enumeration.json`: computed structural summary.
- `results.log`: actual test output.

```bash
# This round
cd research/interventional_core
python -m unittest -v test_model.py

# All rounds, from repository root
python research/run_checks.py
```

**Observed verification:** 24 new tests pass; 174 tests pass across the seven rounds. No empirical phenomenal observations were collected. The constitutive identity remains a hypothesis, and no test count is evidence that the model is conscious.

### Consolidated verdict

The strongest surviving advance is **intervention-sensitive implementation rather than observational representation**. It defeats a specific passive-monitor counterexample to a bare structure-matching proposal. But the discriminator is protocol-sensitive, and its phenomenal authority is unproved. The next constitutive burden is to distinguish unity from differentiation without merely declaring that physical dynamical irreducibility is experience.

## Subsequent differentiation/unity test

[Constructive step 8](../differentiation_unity/REPORT.md) demonstrates independent content preparation within nonfactorable dynamics, resolves a synthetic temporal content correspondence, and isolates the remaining incidence bridge. It states the core-to-unity claim as a substantive conjecture rather than a consequence of physical irreducibility.
