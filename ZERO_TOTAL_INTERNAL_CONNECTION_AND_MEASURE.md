# An internal connection for zero-total relations

## Result

**Three-link continuation:** [loop consistency and measure](ZERO_TOTAL_LOOP_CONSISTENCY_AND_MEASURE.md) extends this link to a triangle, constructs gauge-invariant holonomy, and compares full-support measures that agree on single-link statistics but differ on a three-link event. It does not derive gravitational curvature or the loop law.

I constructed a finite internal link that makes the prior zero-total event well-defined under **independent relabelling of each snapshot**. The link can be set to the identity by a change of description; what remains is exactly the earlier relative event, with no preferred external frame. An ideal reversible record of that event is likewise invariant.

This repairs a specific representational gap in [the previous comparison](ZERO_TOTAL_SYMMETRY_MEASURE_AND_RELATIONAL_IDENTIFICATION.md). It does **not** derive a physical connection, the model's actual existence, or an experience from zero. The link, its transformation law, allowed states and register remain declared ingredients. The aim is to investigate the user's zero-totality candidate without adding an external creator or downgrading the no-brute-remainder demand; it is not to declare the candidate impossible.

A second, sharper result: two invariant measures give *identical distributions for every pair* of the two snapshots and the link, but give different probabilities for the linked relational event. Thus uniform endpoint and link marginals—even pairwise independence—do not by themselves fix the event measure. Under a separately stated product/Haar prescription, a definite answer does follow.

[Exact calculation](verification/zero_total_internal_connection.py), [tests](verification/zero_total_internal_connection_test.py), [receipt](verification/zero_total_internal_connection.json). All finite probabilities and orbit counts use rational or integer arithmetic; one entropy value uses floating-point logarithms. This is standard finite gauge/relational bookkeeping applied to our toy sector, not a novelty claim about gauge theory.

## 1. The linked pair

Use the earlier six configurations `S`, permutations of `(1,-1,0)`. Each obeys the stipulated zero-total condition `sum_i q_i=0`. Let `G=S_3 x C_2`, of order 12, act on S by permuting vertices and simultaneously reversing signs.

Represent two internal snapshots by `q,r in S`. Add one link `h in G`, interpreted formally as an identification transporting r's labels into q's frame. Its relative configuration and event are

```text
s = h r,
F(q,r,h) = 1  iff  h r = -q; otherwise 0.
```

Change the two descriptions independently by `g,k in G`:

```text
(q,r,h)  ->  (g q, k r, g h k^(-1)).
```

Then `h r -> g h r`, while `-q -> -gq`, so F is unchanged. The same argument applies to all four earlier event classes, not only the flip bit. The neutral totals of q and r remain zero. No physical field is claimed to carry h, and no special interpretation of the sign or charges as energy or awareness is assumed.

### The link is not a preferred external frame

Choose `g=e` and `k=h`. The transformed link is the identity, and

```text
(q,r,h)  ~  (q,h r,e).
```

After this gauge fixing, the transformations preserving `h=e` have `g=k`, precisely the diagonal action used in the preceding note. Therefore the linked quotient is in bijection with the old diagonal-pair quotient. The link **does not add a new gauge-invariant degree of freedom relative to the already aligned pair**; it makes the assumed alignment transform correctly when the two labels change separately. Relative to two *unlinked* independently quotiented snapshots, the relational comparison is extra structure and must be justified.

In particular, h alone is gauge-removable on this single link; that does not mean the relational event is empty. With the labelled endpoints fixed, changing h can change F, and the resulting triples need not be gauge equivalent. The model does not show how the alignment is embodied or selected physically. A multi-link model could contain additional gauge-invariant loop data and would require a separate analysis.

## 2. Four genuine relative classes

There are `6 x 6 x 12 = 432` labelled triples, acted on by the `144` elements of `G x G`. Their four orbits are:

| Relative class of `(q,h r)` | Orbit size | Stabilizer order |
|---|---:|---:|
| stay | 72 | 2 |
| flip | 72 | 2 |
| one-charge move | 144 | 1 |
| both-moved | 144 | 1 |

The sizes and stabilizers satisfy orbit–stabilizer and sum to 432. They are the linked counterparts of the four diagonal pair classes. All orbit values concern formal configurations; none is an independently established event in nature.

An ideal bit register can record the invariant flip event using

```text
R(q,r,h,m) = (q,r,h, m XOR F(q,r,h)).
```

For all 864 labelled inputs this is an involution, commutes with the frame transformations when m is unchanged by them, and leaves the charges in both snapshots untouched. It records F when a blank `m=0` is supplied. This is a reversible logical operation **given simultaneous access** to q, r and h and a prepared register. It does not construct an autonomous, local, gravitational or constraint-preserving detector, guarantee a durable record, or prove thermodynamic costlessness. The input copies/history access and ready state remain resources to explain.

## 3. Two measures with the same pairwise marginals

For any earlier invariant class weights `w=(a,b,c,d)`, let `K_w(q,s)` be its transition kernel. Define a normalized measure on linked triples by

```text
mu_w(q,r,h) = K_w(q, h r)/(6 x 12).
```

It is invariant under independent frame transformations because `K_w(gq,gs)=K_w(q,s)`. Its four orbit weights are exactly `(a,b,c,d)`. Direct summation, using the transitive group action and doubly stochastic kernel, gives for **every** w in this family:

```text
mu_w(q,r) = 1/36,
mu_w(q,h) = 1/72,
mu_w(r,h) = 1/72.
```

Thus each labelled variable is uniform and every pair has the same product marginal, regardless of w. These labelled variables are representation-dependent; their marginals are a mathematical control, not separately asserted gauge-invariant observations. The following F-event *is* invariant.

Compare two fully supported measures on the same linked configurations:

| Prescription | Class weights `(a,b,c,d)` | `Pr(F=1)` |
|---|---|---:|
| Uniform labelled triples / independent uniform q, r and h | `(1/6,1/6,1/3,1/3)` | `1/6` |
| Uniform four relative orbits, then uniform within each orbit | `(1/4,1/4,1/4,1/4)` | `1/4` |

Both have **exactly the same pairwise marginals** above, but distinct three-way relative correlations. For the second, its total correlation relative to the product of the three marginals is `ln 6 - (ln 32)/2 = 0.0588915...` nats; for the first it is zero. This is a finite classical Shannon quantity, not an experiential or gravitational entropy. Both are proposed measures, not experimental estimates or evidence that reality probabilistically chooses between worlds. Genuine possibilities and their alleged actuality are not settled by a sampling prescription.

### What a Haar/groupoid prescription does fix

If one **specifies** the product of uniform q, uniform r and normalized Haar measure on this finite group G for h, each labelled triple has weight `1/432`. Pushing this measure to the quotient gives the first row. Equivalently, normalized groupoid weights proportional to `1/|Stabilizer|` are `(1/6,1/6,1/3,1/3)` for the four classes.

This is a constructive route from a declared measure principle to precise relative weights, and it removes the apparent need to choose orbit weights one by one. It is **not** a derivation from gauge symmetry alone. Uniform endpoint and Haar-link marginals do not imply their joint product: the second row has all the same pairwise marginals but a different invariant event distribution. Nor does this finite example determine the correct measure for a gravitational theory, especially where groups, stabilizers or state spaces are infinite.

## 4. Relation to the zero-residue goal

The result distinguishes an **external frame** from an internal relation. A formal relation can be described without a privileged frame, and gauge fixing need not introduce one. This helps articulate how internal distinctions can coexist with a zero-valued total. It does not equate zero with literal absence of all existence or demonstrate that the formal relation is self-subsistent.

To advance the user's proposed account, the next derivation would have to explain why the admissible internal relations, transport law and any physical measure follow from the whole rather than being free inputs. In particular:

- Derive or independently justify a link/transport structure, rather than simply declare h; show its physical content when local descriptions are changed.
- Justify the product/Haar or another measure, including correlations and the domain of actual possibilities, without silently adding a lottery or treating gauge copies as distinct experiences.
- Recover appropriate physical dynamics, local constraints and actual record formation; this one-link model has no derived time or gravitational backreaction.
- Establish how the same reality is intrinsically experiential and gives determinate finite subjects and qualities. The bit register and relative event are not themselves evidence of consciousness; cancellation does not erase local suffering.

These are open constructive obligations. They do not establish that the candidate must have a brute remainder, nor that all existing structure is automatically one. The finite model makes the assumptions and a possible relational route explicit, so a stronger derivation can be tested against them.
