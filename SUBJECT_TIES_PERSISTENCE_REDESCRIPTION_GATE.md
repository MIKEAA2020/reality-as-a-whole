# Subject constitution: ties, persistence and redescriptions

**Status:** conditional finite results and a constructive diagnostic; not a theory of actual subjects or a completed account of reality. This follows the [causal-influence constitution gate](CAUSAL_INFLUENCE_SUBJECT_CONSTITUTION_GATE.md). Its subject rule is an illustrative pairwise minimum-cut rule, **not** integrated information theory (IIT).

The question is whether a proposed constitution rule can identify a subject without an arbitrary label, explain that subject's persistence, and give consistent answers under equivalent physical descriptions. The analysis below separates those three requirements. It retains the user's one self-sufficient experiential whole, possibility = actuality, and plural-subject target; mathematical model comparisons are not an external mechanism for actualization.

## 1. Prior art: IIT already addresses ties

We should not imply that ties are an unaddressed issue in the literature. In [IIT 4.0, supplementary text S1](https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1011465.s001&type=supplementary), Albantakis et al. discuss tied overlapping candidate substrates. The stated procedure first compares structure integrated information `Φ`; if tied candidates remain tied in `Φ`, they do not qualify as complexes under the stated exclusion principle, and the next-best unique system is considered. The authors regard ties as unlikely in realistic systems. This is an explicit **theory-dependent resolution**, not a proof that our toy score has a unique subject or that IIT's phenomenal postulates are true. We do not compute IIT's `φ_s` or `Φ` here and do not claim this toy is a counterexample to IIT.

The philosophical distinction between numerical identity and continuity through fission is also well established; see the [SEP discussion of personal identity](https://plato.stanford.edu/entries/identity-personal/). Causal state/intervention mappings are established in [causal abstraction work](https://proceedings.mlr.press/v213/massidda23a/massidda23a.pdf). Our contribution is the **specific combination and exact checks** below, not the invention of those general ideas.

## 2. One tie can be resolved—but the choice has consequences

In the previous four-spin model, at middle coupling `t=1/2`, the unnormalized cohesion score has six tied maximizing subsets. A simple relabeling-invariant rule is: **among the tied maxima, keep those with the most vertices**. In this example it selects the full set `{0,1,2,3}` uniquely.

Apply this same tie-break at three nearby middle couplings, retaining `k=1/2` for both outer couplings:

| `t` | Selected candidate subset(s) |
|---:|---|
| `511/1024` | `{0,1}`, `{2,3}` |
| `1/2` | `{0,1,2,3}` |
| `513/1024` | `{1,2}` |

All are computed on the **same family of specified physical dynamics**. The size preference resolves the exact tie but changes which subsets are called subjects at the boundary, and leaves the outer vertices unassigned just above it. It is an extra normative/constitutive premise, not an entailment of causal influence or of possibility = actuality.

The comparison is also operationally delicate. The total variation distance between the full equilibrium distributions at the two non-tied parameter values is exactly `1/1024`. For 100 independent, fully observed equilibrium snapshots with known competing parameter values and equal prior odds, Pinsker's inequality gives a lower bound of approximately **0.49436** on the optimal classification error. This specific data protocol barely distinguishes the parameter values despite the candidate rule assigning different subject partitions. It does not cover time-resolved or adaptive experiments, prove subject counts, or establish that a sharp boundary is wrong: a physical theory can have a sharp constitutive condition even when observations are noisy. It does show that a sharp answer is not automatically a well-supported answer.

These are comparisons of formal local models. They do not posit a cosmic lottery or an unactualized global world becoming actual.

## 3. A symmetry obstruction for a different tie rule

It is important not to mistake success in the four-spin tie for a universal resolution. Consider a **three-spin** path `0—1—2` with symmetric interventional cut weights `w_01=w_12=2/5`, `w_02=0`. Such weights arise from the previous heat-bath influence construction for a three-spin equal-coupling chain; no physical subject is assumed. For this diagnostic, use a **different** candidate score:

```
c_norm(S) = [minimum induced cut weight of S] / |S|,   |S| ≥ 2.
```

The two overlapping maximizers are `{0,1}` and `{1,2}`, each with score `1/5`. The full triple scores `2/15`, so “prefer the largest among the top scores” does not choose it. Reflection `0↔2` exchanges the two maxima.

Suppose a selection rule must simultaneously:

1. select at least one of these top-scoring candidates;
2. select no overlapping candidates;
3. be deterministic and invariant under reflection.

There is **no such selection**. Selecting either pair alone violates reflection invariance; selecting both violates non-overlap; selecting neither violates nonemptiness. This is a finite symmetry result under those four specified assumptions, not a theorem that every subject theory has an irresolvable tie.

Possible responses include relaxing overlap-exclusion, admitting indeterminacy, supplying physically meaningful asymmetry, or modifying the maximality rule. For example, if one deliberately discards the tied maxima and chooses the next-best **unique** candidate, the full triple is selected in this toy. That resembles one aspect of IIT 4.0's tie handling after its additional `Φ` comparison, but our score is not IIT and we have not applied IIT to this example. The different choices have different ontological implications; invariance alone does not justify one of them.

## 4. Persistence: symmetry and strict numerical identity

In the four-spin benchmark, imagine local descriptions before and at the tie, with a reflection-symmetric transition. The equilibrium parameter family does not by itself specify a physical process that changes the coupling; this comparison supplies only the hypothetical boundary assignments:

```
before: A={0,1}, B={2,3}     →     at tie: U={0,1,2,3}.
```

Suppose for the sake of the test that `A` and `B` really are **distinct** prior subjects, `U` is one later subject, and a proposed persistence link means strict numerical identity. Identity is one-to-one: `U` cannot be identical to both `A` and `B` while `A≠B`.

Reflection exchanges `A` and `B` while fixing `U`. The partial one-to-one identity matchings are:

- `A→U` only;
- `B→U` only;
- neither predecessor identical to `U`.

The first two are exchanged by reflection. Under the assumptions that the whole history and all relevant subject-making data are reflection-symmetric and the identity assignment is deterministic and reflection-invariant, **only the empty matching is invariant**. So the benchmark cannot derive that exactly one of the prior subjects persists without an additional symmetry-breaking fact. It can describe `U` as a new subject related to both predecessors, but that is a substantive persistence proposal, not a proof of what happens in reality.

This obstruction is conditional. Actual experiential or physical states may break the symmetry; subject identity might require features absent from the benchmark; one can reject strict one-to-one identity in favor of another account of continuation, without calling two distinct things numerically identical; or one may reject the benchmark's instantaneous subject rule. A symmetric probability distribution over the two matchings is not itself a demonstrated fact about which identity obtains, nor a mechanism by which a possibility becomes actual. The result also does not establish that humans can split or fuse.

The constructive implication is that **subject incidence and persistence must be specified separately**. As a diagnostic, a theory can output the full set of permissible predecessor–successor matchings rather than secretly choosing a label. That set is invariant in the symmetric case, but it represents theoretical underdetermination unless the theory explains what is actually true; it is not yet a complete ontology.

## 5. Equivalent descriptions require mapped interventions

A relabeling of graph vertices is only a very limited kind of redescribing physics. Consider one bit `x` and the redundant description

```
e(x) = (x,x),   x∈{0,1}.
```

Only `(0,0)` and `(1,1)` are valid encoded states. The natural encoded version of `do(x=1)` sets both coordinates to 1; setting only the first coordinate while the second remains 0 produces `(1,0)`, which lies **outside** the encoding's allowed state space.

There are many ways to extend the evolution off the diagonal while agreeing exactly on both valid states and on both joint clamps. For example:

- extension A maps an off-diagonal pair to `(0,0)`;
- extension B maps it to `(1,1)`;
- both act identically on `(0,0)` and `(1,1)`.

A proposed independent-coordinate intervention on `(1,0)` gives opposite answers in A and B, even though all valid encoded behavior and joint bit interventions agree. Thus **ordinary behavior plus a state encoding does not uniquely determine independently clamped response functions on inadmissible states**. If a real physical implementation has independently manipulable degrees of freedom, off-diagonal interventions could be meaningful and distinguish its actual mechanism; the point is not that such interventions are universally impossible. It is that they are not licensed merely by duplicating a coordinate in a description.

A defensible redescription gate therefore needs:

1. a state map and explicit admissible state spaces;
2. a map of interventions, with corresponding response distributions checked to commute;
3. a map of proposed subject substrates and persistence/experience claims;
4. a proof that the subject conclusions agree **where those mappings genuinely represent the same system**.

This is related to, not a replacement for, established causal-abstraction conditions. Not every coarse-graining is an exact equivalence, and demanding identical results under every arbitrary coarse-graining would itself be unjustified. Our pairwise influence rule randomized and clamped individual neighbors; it has **not** passed this gate for constrained or coarse-grained physical descriptions.

## 6. Where this leaves the framework

The tie examples eliminate a false shortcut: **causal cohesion plus symmetry does not automatically yield a unique subject, an identity through change, or an invariant physical basis.** The largest-subset tie-break shows that some cases can be resolved, while the three-spin obstruction identifies the cost of simultaneously requiring top-score maximality, exclusion, nonempty selection and symmetry. Existing IIT theory supplies its own more elaborate procedure; whether any such rule is metaphysically justified and matches empirical experience is a separate question.

For a constructive next step, specify an admissible physical model and state/intervention equivalence, then compare two explicit constitution-and-persistence proposals on both descriptions. Require each proposal to state: (i) how ties and overlaps are handled, (ii) how local continuity relates to numerical identity, (iii) what experience or calibrated report predictions follow, and (iv) how any subject measure is defined. If predictions are identical, record the underdetermination rather than treat either proposal as established. Necessity, intrinsic experiential nature, valence, quantum/spacetime recovery and the measure remain open.

## Verification

Run `python verification/subject_cohesion_identity_redescription.py`. The [receipt](verification/subject_cohesion_identity_redescription.json) records exact maximizers, the finite sampling bound, the symmetry enumeration of tie selections and identity matchings, and the off-diagonal redescription test. It imports the two earlier standard-library-only verifiers. These checks are not empirical evidence of subjects or a metaphysical proof.
