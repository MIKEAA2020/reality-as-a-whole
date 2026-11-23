# A zero-total relational event and its record

## Result and scope

**Independent-frame continuation:** [the internal connection and measure](ZERO_TOTAL_INTERNAL_CONNECTION_AND_MEASURE.md) transforms a formal link along with both snapshots, makes the event gauge-invariant under separate relabellings, and clarifies which measure assumptions survive. It does not supply a physical detector or derive the link.

**Continuation:** [symmetry, measure and relational identification](ZERO_TOTAL_SYMMETRY_MEASURE_AND_RELATIONAL_IDENTIFICATION.md) tests two explicit maximum-entropy principles, shows they give different invariant laws, and identifies the shared cross-snapshot structure needed for the record event.

A small, explicit zero-total model can contain internal distinctions and a relational event. Within its chosen six-state sector, relabelling symmetry **uniquely fixes an invariant normalized distribution**, but leaves a family of different event laws. An invariant, reversible record operation distinguishes two of those laws exactly, while preserving the declared zero charge.

This advances the constructive test proposed in [the performance-and-residue audit](ZERO_TOTALITY_PERFORMANCE_AND_RESIDUE_AUDIT.md): a net-zero constraint does not force a static or indistinguishable description. It also exposes what must still be explained. The sector, symmetry, admissible laws, probability interpretation, two-snapshot access and blank register are **stipulated**. Their existence and actuality are not derived from zero. There are no actual subjects, experiences, cosmological energy, local gravitational detector, or fundamental time in this construction. It is not an account without residue and does not pass the formal battery.

Everything below is finite and exact. [Code](verification/zero_total_relational_record.py), [tests](verification/zero_total_relational_record_test.py), and [receipt](verification/zero_total_relational_record.json) use integer and rational arithmetic. The setup is an illustrative application of standard symmetry, graph and reversible-register ideas; no priority claim is made.

## 1. A closed neutral sector with nonzero local values

Use three labelled vertices and three oriented edges in a cycle. Let the incidence matrix and an integer edge field be

```text
B = [ -1  0  1 ]
    [  1 -1  0 ],       e in {+e_0,-e_0,+e_1,-e_1,+e_2,-e_2}.
    [  0  1 -1 ]
q = B e,                Q(q)=q_0+q_1+q_2=0.
```

The unit edge fields `e_i` are a **chosen restriction**, not selected by the zero condition. The six resulting `q` are exactly the permutations of `(1,-1,0)`; each is locally nontrivial and globally neutral. The vanishing follows from `1^T B=0`, a Gauss-type identity together with the additional assumption `q=B e`. These are formal charges; we have not identified them with energy or awareness. The fully zero configuration is a different zero-total state that our sector excludes by assumption.

Call the six configurations `S`. A one-configuration input and a two-configuration pair `(q,r)` are mathematical internal variables. A transition `q -> r` is a relation between them; its presentation does not require asserting an external cosmic clock. But the abstract ordered pair and transition rule do not by themselves establish a physical process or experienced passage.

## 2. What symmetry does—and does not—fix

Let `G=S_3 x C_2` act by permutation of vertex labels and simultaneous reversal of every charge sign. This symmetry preserves `S` and `Q=0` and acts transitively on the six states. Therefore any **normalized probability distribution on S invariant under G** must assign each state `1/6`. This is a uniqueness result *within the chosen sector and invariant-distribution requirement*. It does not derive a real probability measure, determine an actual self-location, select this sector over the zero configuration or larger sectors, or establish that either the model or the symmetry is actual.

For a given state `q`, the stabilizer of `q` divides its six possible successors into four classes:

| Relation of `r` to `q` | Number of successors | Total conditional probability |
|---|---:|---:|
| stay: `r=q` | 1 | `a` |
| flip both signs: `r=-q` | 1 | `b` |
| move one charge to the empty vertex | 2 | `c` |
| both charges change vertex, without being `-q` | 2 | `d` |

`a,b,c,d >= 0` and `a+b+c+d=1`. The 36 ordered pairs form exactly these four orbits under `G`; the verifier checks the full orbit equality. Consequently **every** `G`-invariant one-step stochastic kernel on this sector has the form

```text
K(q,r) = a, b, c/2, d/2 respectively for the four classes.
```

Conversely every such kernel is normalized and invariant. It is also symmetric, `K(q,r)=K(r,q)`, so the uniform distribution is stationary and its two-time statistics obey detailed balance. A stationary state and a reversible kernel therefore supply **no time arrow in this model**; an arrow requires extra ingredients. This conclusion applies to these kernels and stationary distribution, not all imaginable zero-total systems.

If one **adds** the rule “exactly one charge moves to the empty vertex,” then `a=b=d=0,c=1`. A symmetry fixing `q` exchanges the two allowed successors, so both probabilities are exactly `1/2`. This removes an otherwise arbitrary preference *conditional on the move-only rule*. It does not derive that rule, the normalized distribution, or a physical time scale from the zero constraint.

## 3. Two symmetric laws and one invariant event

Compare on the same `S`, with the same uniform marginal at both ends:

- **Move law:** `a=b=d=0,c=1`; the two possible single-charge moves each have probability `1/2`.
- **Flip law:** `b=1,a=c=d=0`; the unique successor is `-q`.

Both are normalized, reversible, `G`-invariant and zero-total. Their single-snapshot distributions are identical. Define the relational event

```text
F(q,r) = 1 if r=-q; otherwise 0.
```

`F` is invariant under every vertex permutation and simultaneous sign reversal. With either a fixed initial state or the stated uniform ensemble,

```text
Pr(F=1 | move law) = 0,
Pr(F=1 | flip law) = 1.
```

For the general four-weight kernel, the corresponding value is `b`; for example `(a,b,c,d)=(1/5,2/5,3/10,1/10)` gives `2/5`. Thus, **if** an observer has the specified two-snapshot access and the chosen stochastic model applies, a single perfect record of F distinguishes these two extreme model laws. This is a mathematical discrimination between stipulated laws, not an experimental result, cosmological prediction or empirical accuracy claim. Relabelling cannot erase the difference because F itself is invariant.

This is a precise positive and negative result: symmetry fixes the within-sector weights; it does **not** select a unique law from the four-parameter simplex. The two laws also show that zero total and symmetry alone do not determine all conditional records. Nor does their existence prove that a fully intelligible theory could not select one by an additional internally grounded principle.

## 4. A reversible internal record, with its resources exposed

Add a two-valued register `m`, declared neutral for Q, and consider the ideal controlled map on the **two accessible snapshots and register**:

```text
R(q,r,m) = (q,r,m XOR F(q,r)).
```

This is a bijection and `R²=I` for all `6 x 6 x 2 = 72` inputs. It is `G`-equivariant if the register is invariant. The charges of q and r are unchanged and the register contributes zero, so the declared total of these two slots plus the register stays zero. With a **supplied blank** `m=0`, its output is precisely `F(q,r)`. Applying R again resets the register *provided the same q and r remain accessible*. The full trajectory of recording/reset is still distinguishable from doing nothing if that history is retained; final-state equality does not erase a history by itself.

This is a complete ideal classical logic operation, **not** a constructed autonomous or local instrument. Having q and r simultaneously available may itself require a history register or two physical copies; their preparation, capacity, locality, dynamics and costs are not supplied. The blank is an initial resource, not derived or free. Reversible logic does not establish zero thermodynamic cost, zero entropy production in a physical implementation, or persistent records in an environment. An actual constrained coupling and an energy accounting are distinct tasks; compare [the previously engineered autonomous model](AUTONOMOUS_RECORD_INSTRUMENT.md), which is not an implementation of this finite sector.

## 5. What remains for full intelligibility

The zero here is a signed sum of stipulated local formal variables; it is **not** shown to be literal absence of existence, the whole's fundamental energy, or a signed experiential quantity. No identification of a finite register with phenomenal experience is licensed. In particular, a zero net is compatible with nonzero local entries, but that arithmetic does not explain why local experience occurs, who experiences it, why it has its character, or why suffering is real. Neither a mathematical probability nor the binary record determines a subject or their qualitative content.

To take the candidate toward the user's stronger demand, a further argument would have to derive or internally ground:

1. Why this kind of charge, the Gauss relation and an invariant sector apply to the whole; why an admissible nontrivial configuration is actual; and how the proposed global quantity relates to physical energy or a different fundamental invariant.
2. Why a particular event law and any measure are necessary rather than extra inputs. The four-class family is an explicit test bed for this, not evidence that symmetry is useless or that a richer principle cannot select a law.
3. How an actual record is embodied by a constrained, appropriately local physical interaction without an external time or a gratuitously supplied duplicate, blank or controller.
4. How the same constitution gives both structural intelligibility and genuinely experienced, differentiated local occurrences; the bookkeeping event and record are not that bridge.

The user's no-brute-remainder standard remains intact. These calculations show what specified assumptions buy, and expose what still needs to be justified; they do not show that those assumptions must forever be brute, or that the zero-totality programme is impossible.
