# Zero totality: can symmetry and parsimony fix the internal measure?

## Result

**Loop continuation:** [three-link consistency and measure](ZERO_TOTAL_LOOP_CONSISTENCY_AND_MEASURE.md) tests correlations invisible to each individual link, including a full-support comparison. The finite loop and measures remain specified rather than derived from the proposed whole.

**Connection follow-up:** [an internal connection for zero-total relations](ZERO_TOTAL_INTERNAL_CONNECTION_AND_MEASURE.md) makes the event invariant under independent frame changes and relates its gauge-fixed quotient to this diagonal comparison. It also constructs two invariant linked measures with identical pairwise marginals but different event weights; the link and measure remain stipulated.

In the same [finite zero-total sector](ZERO_TOTAL_RELATIONAL_EVENT_AND_RECORD.md), I tested a constructive route toward the user's proposal: impose symmetry, then use maximum entropy as an explicit parsimony/information principle to select an internal event law. It yields a **unique** law once the alternatives and measure to which the principle applies are specified. But two equally symmetry-respecting choices of alternatives give different laws. A second result pinpoints an even earlier dependency: the event itself requires a relation identifying the two snapshots across relabellings.

This is progress in locating the exact work a self-sufficient account would have to perform, not a claim that an external chooser, cosmic lottery, or separate positive foundation exists. The user is seeking an account in which whatever genuinely remains is self-subsistent, with no brute residue. The principles below are **conditional candidates** for such an account; I have not derived them from zero or shown that they are fundamental.

[Calculation](verification/zero_total_symmetry_measure.py), [tests](verification/zero_total_symmetry_measure_test.py), [receipt](verification/zero_total_symmetry_measure.json). Probabilities are checked exactly as fractions; entropy logarithms are numerical illustrations. The finite model supplies no experienced subject, actual cosmos, fundamental energy, or dynamical derivation. Neither maximum entropy nor the arbitrary measure of a representation is automatically a principle of reality.

## 1. One snapshot versus a relation

The earlier construction has six allowed charge configurations `S`, the permutations of `(1,-1,0)`, each with total charge zero. The group `G=S_3 x C_2` acts transitively, by vertex relabelling and simultaneous sign reversal. The mathematical quotient of **one** snapshot has one orbit:

```text
|S/G| = 1.
```

But the *diagonal* action of G on an ordered pair `(q,r)` has four orbits: stay, sign flip, one-charge move, and both charges moving. The respective orbit sizes are `6,6,12,12`. Hence

```text
|(S x S)/G_diagonal| = 4,
```

not one. The invariant event `F(q,r)=1` when `r=-q` is meaningful on these paired orbits. Quotienting each snapshot separately and then taking a product forgets how the two are related: `(S/G) x (S/G)` has only one element, so F cannot be recovered from that product alone. A symmetric whole can therefore have nontrivial **relative** distinctions even when no individual snapshot has a preferred label. This is a finite group-action statement, not a derivation of lived time.

### Important qualification: what is held fixed across the pair?

F is invariant under the **same** relabelling applied to q and r. It is not invariant under independent relabellings of the two snapshots. For `q=(-1,0,1)`, `r=-q=(1,0,-1)` is a flip; swapping the first and third vertices in r alone makes `r=q`, a stay. If independent `G x G` relabellings are instead treated as gauge with no cross-snapshot identification, all 36 pairs lie in one orbit and F is not an observable of that quotient.

Thus the diagonal comparison is a substantive **relational alignment/transport assumption**, even though it need not be an external coordinate frame. A candidate fundamental account must ground the relation between snapshots, or build an appropriate connection/reference variable and transform it as well. The previous record assumes such a relation; it has not derived a generally covariant clock or an actual physical transport. Whether the group is a physical symmetry or a gauge redundancy is also an interpretation to justify, not decided by the algebra.

## 2. Two precise simplicity principles, different results

For an invariant transition kernel, write the four class probabilities as `(a,b,c,d)`, ordered stay, flip, one-charge move, both-moved. All are nonnegative and sum to one; the two move successors each have `c/2`, and the two both-moved successors each have `d/2`. The single-snapshot invariant distribution is `1/6` per labelled state.

**Fine-outcome principle.** Maximize Shannon entropy of the six successors of a fixed q. Equivalently, maximize it relative to uniform counting on those six labelled successors. By `D(K_q || uniform_6)=ln 6 - H(K_q) >= 0`, the unique maximizer is uniform over the six:

```text
a=1/6, b=1/6, c=1/3, d=1/3.
Pr(F=1)=1/6;  H(six successors)=ln 6 = 1.791759... nats.
```

It also maximizes conditional entropy within the invariant family. Its joint measure on the 36 labelled ordered pairs is uniform. In this selected Markov model each next labelled state is independent of the previous one; that does not establish a physical dynamics or a derived arrow.

**Relational-class principle.** Instead maximize Shannon entropy of the four diagonal-G event classes. The unique maximizer is uniform over classes:

```text
a=b=c=d=1/4.
Pr(F=1)=1/4;  H(four classes)=ln 4 = 1.386294... nats.
```

Lift this measure to labelled pairs uniformly *within* each orbit; equivalently, give each q probability `1/6` and each successor probability `a`, `b`, `c/2` or `d/2`. This is symmetry-invariant and has the same fully supported set of labelled pairs as the first measure. Its fine-successor entropy is `(ln 32)/2 = 1.732868...` nats, less than `ln 6`. Conversely the fine-outcome principle's class entropy is `1.329661...` nats, less than `ln 4`.

Both are exact consequences of **different explicit optimization problems**. They do not show that one equally deserves to describe physical actuality, or that entropy is the correct ultimate principle. They show why the maxim “no distinctions without a reason” needs a precise account of what is distinct and which weights are intrinsic. If relabellings are gauge, uniform counting of labelled pairs can weight orbits by multiplicity; uniform orbit weighting is a different convention. Neither convention follows merely from declaring the symmetry. Gauge measures can require stabilizer or other factors; this finite example does not settle their correct treatment in a physical theory.

The two proposals can also be regarded as **different weights on the same stipulated full-support relational structure**, rather than alternative total worlds or a procedure selecting which possibility becomes actual. Which measure, if any, governs self-location or observed statistics remains an independent question. This respects the user's possibility–actuality project without assuming that counting labels automatically supplies a probability of experience.

## 3. A stronger conditional selection—and its limitation

Suppose an independent condition fixes the flip-event probability `b=p`, with `0<=p<=1`. Among invariant kernels with this fixed p, maximize entropy of the six successors. The unique solution is

```text
a=(1-p)/5,  b=p,  c=2(1-p)/5,  d=2(1-p)/5.
```

Reason: the flip is one outcome of weight p; write the normalized probabilities of the other five as `v`. The entropy is

```text
H(K_q) = h_2(p) + (1-p) H(v) <= h_2(p) + (1-p) ln 5,
```

with equality exactly when those five are equally weighted (the `p=1` case is the unique flip kernel). The formula reduces to the fine-outcome maximizer at `p=1/6`. At `p=1/2` it gives

```text
(a,b,c,d)=(1/10, 1/2, 1/5, 1/5).
```

This is a real derivation from declared conditions, not an assertion that `p=1/2` or entropy maximization has been established for reality. The fixed p is an input; a self-sufficient theory would still need to explain why that input, the admissible outcome space and the entropy/reference rule apply.

Even the **entire flip-bit history** need not determine the other event relations. Consider a second, fully supported invariant kernel with

```text
(a,b,c,d)=(2/5, 1/2, 1/20, 1/20).
```

For both kernels, from **every** current state the probability of a flip is exactly `1/2`. Therefore, in the Markov model, every finite binary word of flip/non-flip outcomes has probability `2^(-n)` for its length n, regardless of the initial state. This analytic statement follows by conditioning on the history at each step; the script also exhaustively checks words through length five from the uniform initial distribution. Yet the invariant stay-event probabilities are `1/10` and `2/5`, respectively. Both kernels give positive weight to all four event classes.

So even complete agreement on this selected record process, together with the same zero constraint, symmetry and support, does not identify the full transition law. An independently accessible stay-versus-change record would distinguish these particular models. This is a mathematical identifiability result; the ideal two-snapshot register is still a stipulated instrument, not a demonstration of an experiential report or laboratory experiment.

## 4. What this contributes to the zero-residue programme

The constructive lesson is not that simplicity is irrelevant. It is that a simplicity principle becomes powerful when stated precisely enough to do work: here it supplies a unique law for a specified outcome algebra and constraints. To turn it into part of the proposed self-sufficient totality, the programme would need to show, without assuming an external selector:

1. Why the relevant internal distinctions and their cross-stage relation have this form, and whether relabellings are genuine gauge or physically meaningful symmetries.
2. Why one reference measure and one entropy functional, or a stronger non-statistical selection principle, is necessary rather than an unexplained choice. Fine labels, orbits and possible stabilizer factors are not interchangeable.
3. Why the admissible sector and whatever constraints replace p are necessary/actual; including every admissible local alternative does not alone provide their weights.
4. How the structural relation and its law are the same actual reality as concrete experiential occurrences, including subject incidence, qualitative character and real suffering. A record bit or Shannon entropy is not already acquaintance, awareness, or a subject.
5. How a physical clock, invariant record coupling and energy/gravity limit arise, without importing an external time or an unaccounted ready-made apparatus.

None of these open obligations proves that the user's candidate cannot meet the demand. They identify a precise next place to try to derive rather than stipulate: the **relation and measure on genuinely distinct internal events**. The formal battery and the problem of time remain open.
