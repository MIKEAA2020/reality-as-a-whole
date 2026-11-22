# When fusion and persistent private subjects make the same reports

## Result

The [Lewtas audit](LEWTAS_2016_MENTAL_CHEMISTRY_AND_FRAMEWORK_AUDIT.md) left a concrete question: what would distinguish transformation in which selected subjects cease from an account in which those subjects persist while a distinct, type-corresponding field appears?

I constructed a small **stipulated** comparison. In both cases the total represented experiential amount and its per-type amounts are conserved, subjects go from four to three, and the same physical/report channel produces the same results. Yet one case terminates two designated original subjects and the other preserves them alongside a new field. This makes the missing **subject-identity and observation rule** explicit: neither conservation, total subject count, nor the chosen common report channel decides which histories are represented.

This is a mathematical illustration, not evidence that either history is metaphysically or physically possible, that actual subjects are sets, or that the two descriptions must be empirically indistinguishable in a real brain. The example concerns selected inputs only. Lewtas explicitly permits *unselected* experiences or subjects on a constituent to persist; it would be wrong to portray his paper as excluding every lower-level subject.

## 1. The two completed toy cases

There are four already-stipulated elementary ingredient tokens `a, b, c, d`, each with unit weight. Tokens `a,c` carry the same abstract content-type label `red`; `b,d` carry the same label `blue`. The labels are bookkeeping devices, not demonstrated visual qualities. Each subject in the toy is stipulated to own one support, and at each step the supports form an exclusive partition of the tokens. Their weights sum to **4**, with **2 red-type and 2 blue-type units**, in every state. No physical conservation law or actual phenomenal measure is inferred.

`u=0` and `u=1` are two formal configurations in a local order, not evidence of a clinical procedure:

| Configuration | Selected-input fusion F | Private-copy coexistence P |
|---|---|---|
| `u=0` | `{a}`, `{b}`, `{c}`, `{d}` | `{a}`, `{b}`, `{c}`, `{d}` |
| `u=1` | `{a,b}`, `{c}`, `{d}` | `{a}`, `{b}`, `{c,d}` |

In F, the designated original `{a}` and `{b}` subjects cease when their selected supports fuse; the `c` and `d` subjects remain. In P, the designated original `{a}` and `{b}` subjects persist, while **distinct tokens** `c,d` form a field containing both content types. P also involves fusion of `c,d`: this is not a proof that Lewtas must reject P, or a complete version of the project's physically nested-subject model. The example isolates *which* designated subjects persist and which inputs transform; it does not model their anatomical locations or demonstrate that one physical support nests another.

Subject identity over time is an explicit convention: an unchanged support retains its label through consecutive states; a newly appearing support receives a new identity. In F, if `u` later returns to 0, the new `{a}` and `{b}` subjects are **not silently identified** with the originals. In P, those two supports persist through 0→1→0. Real subject persistence need not obey set equality, and this stipulated convention does not justify that it does.

Both models have four subjects at `u=0` and three at `u=1`. Both conserve the same total and per-type token quantities. Both have an integrated subject with both content-type labels at `u=1`. Their designated local subjects nevertheless have different fates. Counting subjects alone does not distinguish these two cases, and the conservation result does not resolve identity.

## 2. A common observation channel

Let `x,y∈{0,1}` be two external input bits. For both cases, stipulate the same public record:

```text
R(u,x,y) = (u, x, y, x XOR y)  if u=1
         = (u, x, y, no joint output)  if u=0.
```

This is a deliberately simplified **physical/report mapping**, not an experience oracle. Even the joint bit does not, by itself, prove that anyone experienced its ingredients together. The particular XOR rule is not inferred from Lewtas or from a split-brain study.

For any fixed sequence of inputs, the output at each step is identical in F and P by construction. The [executable check](verification/lewtas_fusion_nested_observation_gate.py) enumerates all **4,680** sequences of lengths one through four: 8, 64, 512 and 4,096 respectively. This exhaustive check verifies the implementation on those finite sequences. The general argument is simpler: the output function depends on `u,x,y`, not the hidden allocation, so the two records coincide at every step. A common adaptive policy using the same observed past and the same random seed also chooses the same next inputs by induction. That conditional result holds for this observation model, not necessarily for real reports or all imaginable measurements.

The construction is stronger than a mere conserved-*inventory* example because supports do not overlap: even summing per-subject token weights and conserving the two token types gives identical totals in F and P. It remains a toy. In particular, type-level matching does not establish identity of the underlying experiential tokens or explain how one felt quality is produced by another.

## 3. A conditional discriminator and its burden

Define a particular target `N` for the transition 0→1:

> The two specifically designated original `{a}` and `{b}` subjects both continue as subjects, and a subject experiences both stipulated content types together in the post-transition window.

Under the stated toy identity rules, `N=0` in F and `N=1` in P. This target concerns **persistence of particular subjects and a conjoint field**, not just two response channels, matching content, a count of subjects, or a mere neural connection. If the initial subjects cannot be individuated, the window cannot be aligned, or continued identity cannot be assessed, the real-world target is **unknown**, not zero.

Suppose a separate binary assay `Y` is justified for this exact target and context, with false-positive probability at most `e₀` when `N=0` and false-negative probability at most `e₁` when `N=1`. Then, under the two completed hypotheses,

```text
P(Y=1 | F) ≤ e₀
P(Y=1 | P) ≥ 1 − e₁
P(Y=1 | P) − P(Y=1 | F) ≥ 1 − e₁ − e₀.
```

The bound is informative when `e₀+e₁<1`. For illustration only, `e₀=0.10` and `e₁=0.20` give a minimum **0.70** probability separation. These values are **invented**, not measured or supported by the paper, the split-brain literature, or the S02 EEG classifier. This is an inequality conditional on uniform error bounds for the relevant cases; it is not a result from a real assay, a confidence interval, or an assumption that repeated windows are independent.

This conditional result identifies what would have to be added to the common report channel. It does not supply the added assay. In practice a person can provide important first-person evidence about their own perspective, but identifying inaccessible other subjects and proving that the same subjects persist across conditions require additional noncircular access and identity premises. Two hands or two verbal outputs are not automatically two subjects; a single report or failure to report is not automatically a census of all subjects. No known calibration in this project establishes the error bounds above.

## 4. Relation to the paper and the framework

Lewtas argues that selected experiences and their fields can be transformed into a larger subject rather than merely aggregated while surviving unchanged. He also permits unselected experiences on the same basic objects, so persistence *elsewhere* is not itself a counterexample. F is only an idealized rendition of the selected-input part of his proposal. P is a distinct private-copy completion for comparison, not a clinical finding and not an attribution to Lewtas.

Both cases postulate experience and subject ownership. They **do not explain** why either ownership rule holds, why types have the character they do, why a subject exists, or how physical organization fixes the rule. They also do not solve Lewtas's qualitative blending problem: giving a field two labels is not deriving an orange experience. A rule that simply assigns a desired quality to a support remains a postulate. The result supplements, rather than resolves, the earlier [private-nested comparison](PRIVATE_NESTED_FIELDS_AND_EXPERIENTIAL_CONTENT_COMPARISON.md) and [shared-token/duplication gate](SHARED_EXPERIENCE_VERSUS_DUPLICATED_TOKENS_GATE.md).

For the framework's fundamentally timeless whole, `0→1→0` may be used as a **locally ordered representation**, not as an external universal time or a self-creation of reality. A globally represented history does not automatically establish the reality of either local subject lineage. The project continues to require genuinely plural subjects and perspectives without asserting a universal subject; this finite bookkeeping does not select or derive them.

## 5. Practical consequence

The next research task is not to repeat the weak EEG detector or request another participant simply because this toy distinguishes labels. A useful evidence programme would first specify a target, independently motivated subject-identity criterion, accessible report channels and credible errors for the exact condition; compare fusion, persistence and partial-unity rivals under the same physical constraints; and identify observations that would challenge each package. Existing split-brain observations and testimony matter, but their access and anatomical limitations must be retained. Ethical clinical work would use consenting participants and existing or approved noninvasive tasks; this gate recommends no surgery or new intervention.

If those identity and calibration conditions cannot be justified, the conclusion is **indeterminate**, not an inferred subject count. The broader incidence, quality, persistence, physical–experiential bridge, and C3 full structural and experiential intelligibility remain open. No new patient data, experiments or correspondence were used.

## 6. Checks

[Code](verification/lewtas_fusion_nested_observation_gate.py), [tests](verification/lewtas_fusion_nested_observation_gate_test.py) and [aggregate receipt](verification/lewtas_fusion_nested_observation_gate.json) check partition and type conservation, identity persistence, subject-count equality, the finite public records and probability-bound arithmetic. Run them with:

```sh
python verification/lewtas_fusion_nested_observation_gate_test.py
python verification/lewtas_fusion_nested_observation_gate.py
```

Passing tests only establishes what follows from these invented assumptions. It does not measure experience or establish either rival in nature.
