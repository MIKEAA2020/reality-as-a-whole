# Confined succession without an interaction

## Starting with the user's correction

A game does not need an interaction to keep its move number unchanged while a player thinks. The number changes **when a half-move occurs**; thinking in the player's realm is not a half-move. Likewise, under the user's surface rule, the confined position is A during the room journey and becomes B on return. There is no need to invent a force that holds A fixed or turns the intermediate room points into hidden surface points.

This corrects the emphasis of the prior [held-position and interface report](ZERO_CONFINED_REALMS_HELD_POSITION_AND_INTERFACE.md). Its quantum interaction circuits are optional examples of additional physical assumptions; they are **not necessary to express confinement**, nor does confinement require a physical register, an accessible message, an external observer, an extra clock or a causal interface.

Here is a direct mathematical construction of the distinction. It has three results:

1. A confined succession `A→B` can coexist with arbitrarily many richer internal distinctions, without a holding interaction or a fundamental clock. Different richer structures can have the **same number** of distinctions and the same confined succession yet different internal relations.
2. This works with a partial order, so the richer structure need not have a single global sequence. The rule that A persists is a definition relative to the confined realm and the specified order, not dynamics.
3. A signed relational zero can be imposed on this very structure. **If** a parallel internal structure is symmetric and locally balanced, its equal split follows mathematically. But zero alone does not select the internal structure or the split. This shows both a constructive role for symmetry and the precise remaining demand on zero's constitution.

The constructions are internal mathematical models, not a claim that reality has an external room, a literal player or a hidden preferred time. The distinction between genuinely real structure and mere representation is a substantive part of the theory, not settled by drawing the model.

## 1. The confined realm has its own succession

Let a confined realm have a set of events `S` with its own order `≺_S`. A change count or half-move number is defined **only from events of S**. As a minimal example:

```text
S = {A,B},       A ≺_S B.
```

There is no S-event strictly between A and B. Thus B follows A directly in the confined succession. In chess, A and B may be successive *game positions* separated by one half-move. In the sphere analogy they may be the successive surface positions specified by the user's rule. These interpretations are analogies, not an assertion that a chess state and a point in space are the same kind of thing.

We say the confined state is A until the event B; it changes to B at B. **No interaction is introduced to achieve this**: no other event qualifies by definition as an event that advances this confined succession. The player/traveler is the richer-domain actor, not the piece or surface inhabitant. Nor does this claim that an inhabitant observes the traveler or experiences a jump.

The confined order is not itself an elapsed-duration scale. In chess the half-move count gives order and a discrete count; the player's elapsed time is additional to that description. In the geometric example the room-route parameter is additional to the surface succession. Neither additional parameter is assumed to be external time for the real whole.

## 2. A richer structure without a universal time

For one transparent class of comparisons, take a finite partially ordered set `H` containing the confined events, and define the confined order by restriction:

```text
A ≺_S B  iff  A ≺_H B,   for A,B in S.
```

The intermediate elements of `H` are **not elements of S**. They do not count as surface positions or half-moves merely because they can be compared to A and B in the larger relation. Restriction is a definition of domains and their orders, not a coupling or an observer's operation.

A simple comparison is

```text
chain:       A ≺ p ≺ q ≺ B

diamond:         x
               ↗   ↘
             A       B
               ↘   ↗
                 y
```

In the diamond, `A≺x≺B` and `A≺y≺B`, but `x` and `y` are incomparable. Both have exactly four elements, both restrict to `A≺_S B`, and both give **A, then B** in the confined succession. Yet they are not isomorphic: in the chain `p,q` are ordered; in the diamond `x,y` are not. The diamond has two linear extensions, `A,x,y,B` and `A,y,x,B`; neither extension is specified as the whole's privileged time or foliation. This is a finite partial-order model, not yet a relativistic spacetime or a proof of Lorentz covariance.

The order `A≺_H x≺_H B` is an additional premise of this **particular comparison**: it lets us express an internal distinction as lying between the two confined events. It is abstract order, not automatically causal influence, physical travel or an experienced interval. Different realms could instead have no such cross-domain order. Confinement alone does not determine which kind of relation obtains, and we do not infer an interface merely from the diagram.

### The held state, stated without a mechanism

For an event `h∈H`, when there is a unique latest confined event at or before h, define

```text
last_S(h) = the unique maximal s∈S with s≤_H h.
```

For the diamond this gives `last_S(A)=last_S(x)=last_S(y)=A` and `last_S(B)=B`. It expresses the user's held-position convention: intermediate richer distinctions are not surface changes. It does not assert that A is the traveler's actual room position, that x or y is accessible to the surface, or that anything physically stores A. A physical realization of the convention could require further structure, but the mathematical distinction does not require one.

The general rule is **not automatically defined on every partial order**. If h has two incomparable maximal prior S-events, there is no unique latest one; the model must supply a suitable realm-specific criterion or leave this cross-domain label unspecified. That is not a reason to add a universal clock. It marks where this particular convenience rule's domain ends.

### How much does the confined succession determine?

For each integer `n≥0`, the richer chain

```text
A ≺ h₁ ≺ ⋯ ≺ hₙ ≺ B
```

has the same two-event confined order. Its richer structures have different sizes and hence are not isomorphic. The four-element chain/diamond example is stronger: even fixing the number of internal distinctions does not fix their relations. These are mathematical nonuniqueness results about the **specified input** `A≺_S B`, not a proof that all such structures are genuinely possible, separately actual, or equally weighted. The user's actuality–possibility thesis remains the substantive proposal that would need to tell us which distinctions are genuine and how they belong to the one whole.

## 3. Relation to the zero point and internal sphere

The earlier [point–sphere construction](ZERO_POINT_INTERNAL_SPHERE_CONSTITUTION.md) uses a structured blow-up: distinct internal directions map to the same zero point under the external projection. The present example can be organized in the same *formal pattern*:

```text
confined events S  ──inclusion──▶  richer structure H
       │                              │
       └──────────▶  one point ◀──────┘
```

Both down-arrows are constant maps to the single point representing the whole without external extension. The internally defined structures are retained **before** this forgetting map; the image point alone cannot recover them. The diagram is a map between stipulated structures, not a spatial room outside reality or a process that creates the whole.

This is compatible with the user's proposal that the richer structure and confined realm are both within one self-sufficient whole. It does **not** prove that an ordinary bare singleton mathematically entails a sphere, this order, experience or the real universe. The finite `S` here is not the full projective direction sphere, and the single point in the diagram is not an energy measurement. A derivation must explain the structured fiber and its relations from the zero whole's own constitution rather than select them independently.

## 4. An exact, conditional zero on the same realm model

We can put a signed relational accounting structure on the diamond, without pretending it is already physical energy or felt valence. Let `F_uv` be an oriented rational amount assigned to each drawn relation. Define the signed contribution at a node by

```text
b(v) = sum of F on outgoing edges − sum of F on incoming edges.
```

For every finite directed network, each edge is counted once positively and once negatively. Consequently

```text
Σ_v b(v) = 0.
```

This mathematical identity allows nonzero local contributions. For example, take total `T≠0`, require `b(A)=T`, `b(B)=−T` and require `b(x)=b(y)=0`. Then all of the following are balanced:

```text
F_Ax = F_xB = αT,
F_Ay = F_yB = (1−α)T.
```

Here `α` may be any rational value between 0 and 1. In particular, both a symmetric `1/2,1/2` split and an asymmetric `1/4,3/4` split give precisely the same local boundary contributions `(+T,−T)` and the same total zero. No physical exchange or interaction is being inferred from this diagram: the edge assignments are a **specified mathematical accounting law**. Their identification with actual currents, conserved energy, conscious qualities or probabilities would be additional claims.

Now add a substantive symmetry requirement: exchanging `x` and `y` leaves the edge-assignment **itself** invariant. This is stronger than merely redrawing or relabeling the network. It requires `F_Ax=F_Ay`; the boundary equation then forces

```text
F_Ax = F_xB = F_Ay = F_yB = T/2.
```

That is genuine non-arbitrary structure **conditional on the diamond, the local balance, a fixed T, and an actual exchange symmetry**. The same argument gives `T/n` along each of n internally identical parallel routes. No preferred intermediate route is chosen. But the total-zero identity alone does not require the diamond, the symmetry, nonzero T, the number of routes, or any interpretation of F. Symmetry is doing real work; it cannot be smuggled into zero's bare numerical value.

### A common-boundary counterexample

The chain `A≺p≺q≺B` can instead carry F=T along each edge. Its internal contributions vanish and its boundary contributions are again `(+T,−T)`. The symmetric diamond does the same with `T/2` on each branch. Both have the same confined succession and the same whole signed sum zero; their richer orders are nevertheless different. So **the confined succession plus that zero sum does not by itself determine the richer structure**. A stronger constitutive principle may do so; this finite counterexample says exactly which weaker inference is insufficient.

These internal distinctions can be taken as real within each candidate model. The counterexample is not an argument that the richer domain is imaginary, or a denial that actual reality has a necessary constitution. The user's proposed demand is to derive the full constitution—potentially including all genuine possibilities and their actual incidence—not simply to assume a tolerable residual choice.

## 5. Connecting to the preceding physical and experiential results

The earlier [five-ray construction](ZERO_SPHERE_CONSERVATION_RECORD_CURRENT_SINGLE_SYSTEM.md) provides a **physical** example of branchwise opposite sharp work currents, `J₁+J₂=0` on its specified sector. It is not derived from the abstract network above. Conversely, the two opposite records in that construction are simultaneous paired record bits in a branch, **not** the sequential A and B of this report. Substituting one for the other would erase the very distinctions under investigation.

A future unification would have to construct a justified map from a confined succession and its richer relations to the actual sphere–record operators, show which signed network quantity corresponds to a measurable physical current, and preserve local reduced-state no-signalling. No such map is assumed here. Equal network routes `T/n` are not automatically Born probabilities or subject-incidence weights; the earlier three asymmetric sphere weights, for example, cannot be replaced by `1/n` just because this special network has permutation symmetry.

For experience, local negative and positive contributions could cancel in an appropriate whole-level quantity without eliminating the negative experience. But this network has no experiencing subjects and its sign values are not felt. Even with genuine subjects, incidence matters: duplicating the positive contribution twice while counting the negative contribution once changes the sum. The previous [subject–experience comparison](ZERO_SUBJECT_EXPERIENCE_BRIDGE_COMMON_DOMAIN_TEST.md) treats that as a distinct burden. This report does not identify subjective time with extra nodes, claim experience occurs in an external time, or infer experience from zero.

## 6. Where this takes the programme

The useful distinction is now sharper than a picture of one space inside another:

- **Confinement:** what counts as a state or step is fixed within the realm; no force is needed to stop other-domain events counting as its steps.
- **Richer constitution:** a whole can be modeled with real internal distinctions not in that realm; their relationship to its events is a separate question.
- **Zero and symmetry:** signed relational balance can coexist with differentiation, and symmetry can determine a relative split when its premises hold.
- **Necessity:** neither the confined description nor a signed zero alone fixes the richer structure in this example. To meet the no-residue demand, derive the relevant relations, symmetry, physical realization and experiential incidence from the full self-sufficient constitution—not from a hand-chosen network or a hidden external player.

This is a constructive intermediate result, not a claim that the stronger derivation is impossible or complete. The next concrete mathematical task is to identify a candidate constitution whose own necessity fixes both the restriction and the richer relation, and to test whether it recovers the already derived sphere/record/current predictions without imposing their outcomes afterward.

## Verification

Run `python -m unittest verification.zero_realm_restriction_without_interaction_test -v`. Ten standard-library tests check arbitrarily many internal links, equal-cardinality chain/diamond nonisomorphism, both linear extensions without selecting one, the held-state rule, transported relabelings, ambiguous partial-order cases, exact symmetric `T/n` flow, asymmetric controls, shared chain/diamond boundary balance and incidence-count sensitivity. All flow arithmetic uses exact rational numbers. The tests do not validate an external clock, any physical interface, actual metaphysical possibilities, subjecthood or experiential zero.
