# Occurrence, quality and incidence on the same echo

## Result

This pass returns to the original angular echo and its constrained opposite pair, rather than adding another apparatus. It asks what follows if physical event identity, quality content and incidence weights are required to fit together.

The strongest connections are conditional but precise:

1. The two existing quality coordinates **do not by themselves identify all eight physical events**. Adding the pointer and the previously chosen angular magnitude makes their joint physical signature distinguish all eight. Whether that physical signature is an occurrence's intrinsic content is a separate constitutive hypothesis.
2. If a single scalar depends **only** on the two quality signs and their swap-invariant magnitude, is unchanged by type exchange, and reverses under the sign counterpart, it must be zero on the disagreement sector, which has physical weight **1/2**. This does not follow for all scalar laws: the existing pointer sign supplies a nonzero, type-invariant, counterpart-odd contextual alternative.
3. Physical pairwise zero, counterpart-invariant incidence and zero global average are three different conditions. The second can hold without equal local factor weights; the third can hold without the second. A coherent pure-state constraint rules out some event-dependent weighting examples that fit only the diagonal record table.
4. The actual saved-record protocol provides a persistent **physical ledger** through the echo while its quality coordinates change. It supplies neither a subject nor a proof that a persisting subject owns the successive occurrences.

These calculations strengthen the internal interface; they do not establish that model signs are felt values, that all physical events are actual subjects, or that the whole-level zero constitution has been derived. [Implementation](verification/zero_echo_joint_identity_balance.py) and [tests](verification/zero_echo_joint_identity_balance_test.py).

## 1. One carrier, one physical event table

Use the [existing joint candidate](ZERO_JOINT_INCIDENCE_QUALITY_OPPOSITE_PAIR_ROOT.md), at the post-echo anchor. The physical event label is `(i,s)`, where `i=0,…,3` is the angular bin and `s=±1` is the sign pointer. The earlier construction obtains the physical weight `1/8` for each event from the original complex echo vectors. It is not an assertion that eight actual experiences or subjects exist.

The old commuting record signs are `J=j` and `R=r`, with

```text
Q_now = s j,       Q_echo = s j r,       Q_now Q_echo = r.
```

Use the earlier swap-compatible **model magnitude** `g=|u(u+1)|`, not a derived experiential intensity:

| i | u | j | r | g |
|---:|---:|:---:|:---:|---:|
| 0 | −3/4 | + | − | 3/16 |
| 1 | −1/4 | − | − | 3/16 |
| 2 | +1/4 | + | + | 5/16 |
| 3 | +3/4 | + | + | 21/16 |

At the anchor the constrained pair supplies opposite structural vectors

```text
V₁(i,s)=g(Q_now,Q_echo),       V₂(i,s)=−V₁(i,s).
```

The pair-factor labels here name the two encoded model observables. They do not establish independently prepared copies, two subjects, or two experiences. The exact operator pairing and its original coherent-vector checks are retained from the earlier construction.

## 2. Which physical distinctions can one occurrence preserve?

Let a proposed occurrence-content map `C` assign a definite content to each of these eight modeled physical events. **If** two labels describe one and the same occurrence with that same content, their C values must agree. The equivalence relation induced by C is

```text
x ~_C y    exactly when    C(x)=C(y).
```

This is the coarsest quotient that preserves all fields named by C: any other equivalence that preserves those fields must refine it. Event weights descend by summing distinct physical event weights in each class; duplicate names for the *same* event do not multiply its weight. The mathematical result neither proves that equal-content events are one experience nor that physically distinct events are separate subjects. Additional content can require a finer quotient, and actual access to any listed field must be justified.

For this actual table:

| Available physical fields C | Classes | Best guess of `(i,s)` from these fields |
|---|---:|---:|
| `(Q_now,Q_echo)` | 4 | 1/2 |
| `(Q_now,Q_echo,g)` | 6 | 3/4 |
| `(Q_now,Q_echo,s)` | 6 | 3/4 |
| `(Q_now,Q_echo,s,g)` | 8 | 1 |

These are optimal guesses from the **listed commuting fields and equal event weights**, not universal bounds on other quantum POVMs. For example, `(i,s)=(0,+)` and `(1,−)` both have `(Q_now,Q_echo,g)=(+,−,3/16)` but have opposite pointer records. Conversely `(2,+)` and `(3,+)` agree on both signs and the pointer but have different g.

The last signature is therefore a concrete *physical* one-event interface on this finite table. If one hypothesizes that all four fields are intrinsic content of the same occurrence, content-preserving identity separates all eight events. If only the two quality coordinates are relevant, four content classes remain. Neither choice proves how many subjects there are, how many experiences are actual, or whether two physical events are phenomenally identical. A confined subject is not entitled to read the pointer, angular magnitude or comparison memory merely because the global model contains them.

The existing type operation exchanges the two Q coordinates and preserves s and g; the sign counterpart reverses both Q coordinates and s while preserving g. Each induces a bijection on the signature classes. These are **active physical/model transformations**, not a declaration that different signs or suffering and pleasure are gauge-equivalent. The full clock counterpart still needs its previously established phase dressing.

## 3. Can the two coordinates become one scalar?

Suppose a proposed structural scalar is a function of the two binary coordinates alone, `v(n,e)`. Require it to reverse under their joint sign reversal:

```text
v(−n,−e)=−v(n,e).
```

Writing `a=v(+,+)` and `b=v(+,-)`, **every** such scalar has the exact form

```text
v(n,e) = a(n+e)/2 + b(n−e)/2.
```

If the physical type exchange is further required to leave this scalar unchanged, `v(e,n)=v(n,e)`, then `b=0`. Hence

```text
v = a(Q_now+Q_echo)/2,
```

and v is zero whenever the coordinates disagree. Those events have physical weight 1/2. Allowing the earlier g as an additional argument does not remove the obstruction: on the disagreement sector, exchanging the coordinates and reversing both produce the same `(n,e,g)` signature, so a scalar both invariant under the former and odd under the latter must equal its own negative.

This exposes an exact choice, not an argument that real experience vanishes. One can retain the two-coordinate structure; allow the scalar to transform rather than remain invariant under type exchange; or include physically and constitutively relevant content beyond `(n,e,g)`. In particular, the existing pointer rule

```text
v(i,s)=s
```

is nonzero on every modeled event, invariant under the specified type operation and odd under the sign counterpart. It is **not** a function of `(Q_now,Q_echo,g)` alone: the two example events above have the same Q/g signature but opposite s. It is therefore a genuine contextual alternative on the same carrier, not a new model chosen to evade the result. The physical pointer may be inaccessible, and its sign is not thereby positive or negative feeling. Which content a genuine experience includes is the substantive unresolved question.

Even for the restricted `a>0` scalar, the global mean is zero while the positive and negative parts each have mean magnitude `a/4`; half the event weight carries nonzero scalar values. A vanishing signed sum never makes a negative contribution unreal. These are model values and physical weights, not an experiential measurement.

## 4. Physical pair, actual incidence and three levels of balance

To expose the difference between a pair identity and an incidence rule, **hypothesize** a normalized factor-labeled incidence extension. Give factor 1 a conditional share `λ_(i,s)∈[0,1]` and factor 2 the remainder:

```text
μ(i,s,1)=λ_(i,s)/8,       μ(i,s,2)=[1−λ_(i,s)]/8.
```

The untyped physical event weight remains `1/8`. This is a supplemental accounting candidate, not a claim that factors are actual separate subjects. If occurrences overlap, are not normalized in this way, or are represented by a different physical–experiential algebra, another analysis is needed.

Three non-equivalent statements now have exact meanings:

1. **Branchwise factor balance.** The two model vectors cancel algebraically for every event. Their *weighted incidence* contributions cancel event by event iff `λ_(i,s)=1/2` for all eight events, since g is nonzero. Equivalently, this normalized extension is invariant under the **abstract factor-label swap** at each event. That swap is not assumed to be a physical gauge transformation.
2. **Counterpart-invariant incidence.** For the active map `(i,s,k)→(i,−s,k)`, the extension is invariant exactly when `λ_(i,+)=λ_(i,−)` for each i. Then the unnormalized vector total is zero on **every physical event set closed under s reversal**. Equal factor shares are not required. Conversely, because every bin's vector is nonzero, zero on every such closed set forces those four equalities.
3. **One global zero.** The total over all events can vanish even when the incidence extension is not counterpart-invariant, because different bins can cancel one another. A global sum alone does not certify either of the stronger relations.

For example, take `λ=3/4` at every event. Factor 1 is weighted three times factor 2, so branchwise weighted cancellation fails; nevertheless the incidence measure is counterpart-invariant, and every counterpart-closed event set has zero vector total. A sign-selective query is not counterpart-closed: for `s=+` its unnormalized vector total is `(13/128,13/128)` and its conditional mean is `(13/64,13/64)`.

Conversely, set `λ_(0,+)=λ_(1,+)=3/4`, `λ_(0,−)=λ_(1,−)=1/4`, and all other shares to `1/2`. The complete vector total is zero, but the counterpart-closed pair of events in bin 0 alone has total `(3/128,−3/128)`. Thus global cancellation hides a local asymmetry. These examples preserve the coarse event table only; they do not show that either incidence law describes actual subjects or actual physical–experiential states.

### Coherence limits the weighting alternatives

The distinction between a coarse table and the *same full physical state* matters. If positive factor blocks are required to satisfy `Σ₁+Σ₂=|Ψ⟩⟨Ψ|` for the same global pure state, positivity forces `Σ₁=α|Ψ⟩⟨Ψ|` and `Σ₂=(1−α)|Ψ⟩⟨Ψ|`. Event-dependent λ cannot meet that strong all-effect condition. A constant unequal `α`, such as `3/4`, can meet it; purity alone does not prove equal factor incidence or subject identity.

For a fixed pointer-sign slice of the actual coherent echo, the four angular branch projectors have weight `1/4`. Their normalized branch vectors define an isometric four-dimensional representation in which the pure state is `(1,1,1,1)/2`, with phases absorbed into the basis. Diagonal event-dependent positive blocks can sum to `I/4`, reproducing every bin weight, but the coherent-state projector has expectation `1/4` there and 1 in the original pure state; the trace distance is `3/4`. This is a logical representation of the **actual four orthogonal branches**, not a claim that the full carrier is four-dimensional or that the coherence-sensitive effect is accessible. The previous [accessible-marginal analysis](ZERO_ECHO_ACCESSIBLE_MARGINAL_INCIDENCE_ROOT_CAUSE.md) shows why all effects on a mixed local record still need not select the full pure-state rule.

Therefore the event-dependent example demonstrates a distinction under a weaker table-only premise; it must not be treated as an alternative decomposition of the same globally pure state. Conversely, full-state consistency itself does not establish that its factor blocks are actual subjects or experiential incidence measures.

## 5. Persistence: same physical ledger, different occurrences

The earlier [saved-record protocol](ZERO_ECHO_SUBJECT_PERSISTENCE_RECORD_AND_ACCESS.md) coherently writes the initial J sign `z` to an added memory L before T–Q–T. With the physical pointer s, conserved B sign b, saved z and model magnitude g, define the branch ledger

```text
ℓ=(s,b,z,g),       b=R[i],       z=R[i]J[i].
```

In this finite supported table, ℓ distinguishes all eight `(i,s)` event labels and is unchanged through the four echo checkpoints. The tests explicitly propagate the saved memory with the **actual complex echo vectors** for three source histories and both sign slices, checking the relevant J and R projections at all four checkpoints. This is a physical branch/record result, not a claim that L is automatically accessible to a confined subject.

A candidate may assign all four time-labeled slots on that ledger to one persisting owner, while treating them as four successive occurrence slots. For example, the same ledger for `(i,s)=(0,+)` has quality coordinates

```text
before T: (−,−) → after T: (−,+) → after Q: (+,−) → after T: (+,−).
```

A persisting owner need not have an unchanging quality. But the same physical ledger is also compatible with momentary or other ownership rules; clock covariance and memory transport alone do not pick one. A finite cyclic clock additionally needs a winding record if distinct repeated laps are to be identified separately.

The memory is not a free observation. On the specified normalized sign slice, tracing it out changes the old carrier's pure-state fidelity to `5/8`; uncomputing it after the inverse echo restores coherence but erases that record. Retaining a durable, accessible comparison, with physical controls and resources, is a further requirement. The model also does not establish that any occurrence slot is a feeling or that a physical identity report accurately reports ownership.

### One explicit joint candidate

The preceding pieces can be assembled, without asserting them as metaphysical facts, into one testable **conditional candidate** on this same carrier:

```text
occurrence slot:   o=(i,s,t),                 t=0,1,2,3,
structural content C(o)=(Q_now(t),Q_echo(t),s,g),
proposed owner:    owner(o)=ℓ=(s,b,z,g),
slot weight:       μ(o)=π_t/8,                π_t≥0, Σ_t π_t=1.
```

Here `π` is an expressly supplied clock-selection/sampling law; it is not derived as the actual frequency of experience. For each chosen t, the conditional physical distribution of `(i,s)` is the existing `1/8` table, and the code verifies that C distinguishes all eight supported events at **every** checkpoint. Summing over t gives each ledger owner weight `1/8` under this particular sampling convention. The two opposite pair vectors are features of the same slot in this candidate, not automatically two separate incidences. The candidate also keeps different t slots distinct while assigning them the same proposed owner. A distinct-factor or momentary-owner ontology is a different candidate, not disproved by this bookkeeping.

This makes explicit what a single constitution would have to establish: that these slots actually occur, that C is their intrinsic quality rather than merely physical data, that ℓ identifies their subject, and that the chosen measure is appropriate to their incidence. The mathematical coherence of the four assignments does not supply those identity claims. In particular, changing the clock-selection protocol π should not silently be taken to create or erase subjects.

## Continuation: access and ownership witnesses

The [next pass](ZERO_ECHO_JOINT_CANDIDATE_ACCESS_AND_IDENTITY_WITNESS.md) computes minimal record sets for this particular candidate at the actual echo checkpoints, distinguishes classical record redundancy from quantum coherence, and gives a conditional test of persistent versus momentary ownership. The candidate's physical ledger remains distinct from an established subject identity.

## 6. Why these connections remain conditional

Following the dependencies rather than stopping at the equations:

1. **Why can one use these weights?** They are the Born weights of specified commuting physical effects. Treating them as actual experiential incidence weights requires a justified event-to-occurrence map, eligible reference class and coarse-graining rule. Equal algebraic labels do not settle subject identity.
2. **Why should the proposed content be complete?** `(Q_now,Q_echo,g)` excludes a physically available pointer distinction; adding s removes the finite collision. But even the enlarged physical signature need not exhaust intrinsic character or be accessible to a subject. A physical record and its phenomenal interpretation cannot be identified just by naming them.
3. **Why choose a scalar and its transformations?** The zero-on-disagreement result follows from quality-only dependence plus type invariance and counterpart oddness. The pointer counterexample shows why removing or adding a relation changes the conclusion. Whether either rule is a genuine phenomenal law must be argued or discriminated, not selected for numerical balance.
4. **Why count the pair or preserve its counterpart?** The pair constraint is a physical operator identity; a factor census, overlap rule and measure-preserving map of actual occurrences are separate hypotheses. Global zero can arise through cancellation that does not preserve a proposed local pairing.
5. **Why this carrier, measure and actuality?** The angular register, echo, clock, pair encoding and their state were constructed with supplied inputs. Internal consistency demonstrates a possible joint structural interface; it does not yet derive them, their subject–quality identity, or the genuine incidence rule from a self-sufficient zero. The open constitutive task is to show what the whole's own nature necessitates and how it excludes or identifies alternatives without encoding the desired answer in a definition. This is the current explanatory boundary, not proof of a brute ultimate bedrock or an external temporal cause.

A constructive next test is to specify a **single candidate** physical–experiential incidence map that says which content is intrinsic, what identifies its owner over the actual record history, and how its measure transforms under the dressed physical symmetries. Then test it against the pointer/context alternative, the restricted-versus-global state distinction, unequal factor census and independently calibrated report controls. A candidate that simply labels all four fields “experience” or all balanced events “subjects” has not yet supplied the missing relation.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_echo_joint_identity_balance_test -v
```

The tests check the finite quotient and exact weights, all 4,140 event partitions, symmetry and scalar controls, the original coherent saved-record checkpoints, three levels of balance and the pure-versus-dephased comparator. They do not prove actual subjecthood, felt valence, physical locality, full source survival or foundational necessity.
