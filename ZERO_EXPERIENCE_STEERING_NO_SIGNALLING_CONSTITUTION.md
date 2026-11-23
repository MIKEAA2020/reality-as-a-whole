# A constraint on identifying experience with the steered sphere

**Unified asymmetric example:** [the single-system synthesis](ZERO_SPHERE_CONSERVATION_RECORD_CURRENT_SINGLE_SYSTEM.md) combines the unequal conservation-derived triple weights, definite opposite record/current labels and equality of the full receiver density operator. Its explicit conditional means illustrate why locally treating them as definite values would signal.

**Sharp relational-current continuation:** [the response analysis](ZERO_SHARP_RECIPROCAL_CURRENTS_AND_EXPERIENTIAL_RESPONSE.md) gives an explicit model where equal reduced subsystem states coexist with opposite sharp joint currents, and tests which response rules would yield signed zero. Its four-body interaction is not relativistically local, and no accessible feeling or signalling claim follows.

**Constructive continuation:** [the local recording and experience-constitution analysis](ZERO_LOCAL_RECORD_EXPERIENCE_CONSTITUTION.md) supplies an explicit nondemolition pointer Hamiltonian, derives the full no-signalling record distributions, and shows that even an identical signed first-moment operator can correspond to different outcome distributions. The local response, subject and phenomenal identity are not thereby derived.

## Result: zero mean is not enough

The [last construction](ZERO_SPHERE_STEERING_BELL_NECESSARY_RECORDS.md) showed how the conserved pair and triple of rays, under an assumed singlet, generate two ensembles of remote qubit states. Both ensembles have a weighted signed directional mean of zero.

There is an important further result:

> For any **generic** conserved five-ray configuration, if a local subject's definite experiential quality is a function only of the remotely steered pure state, and if that quality is locally accessible with the conservation-derived Born weights, then no-signalling between the pair and triple measurement choices requires the quality to be **the same on all five steered states**.

If that same quality is also supposed to have the derived zero weighted mean, it must be zero on all five. Thus this particular attempt cannot simultaneously provide nonzero local experiential differentiation, the constructed balance, and experiential no-signalling.

This is not a no-go theorem for zero totality, necessitarianism or physical–experiential identity. It rules out a **specific, tempting identification**: treating a steered conditional state, all by itself, as the complete determinant of an accessible local experience. A construction in which physical outcomes and subjects depend on a fuller physical organization is not ruled out. Below I give an explicit definite-outcome alternative for the same two settings, rather than merely identifying a problem.

## 1. The five-state setting

The established conditional mathematics is

```text
Σ_(i∈pair) p_i = Σ_(i∈triple) p_i = P,
q_i = (−P·p_i)/(−P·P),
σ_B|i = q_i Π_(−n_i).
```

The first line is the unique positive conservation relation for five generic future null rays; the second defines center-frame energy fractions; the third holds when an **additional two-qubit singlet and the constructed ray POVM** are assumed. `Π_(−n_i)` is Bob's normalized conditional state, given Alice's outcome `i`. It is not automatically an unconditional local state or an ontic description of an individual Bob. The singlet's unconditional Bob state is `I/2` for either Alice measurement.

The two pair weights are `(1/2,1/2)`. Every triple weight is strictly between `0` and `1/2` and the three sum to `1`. These statements follow from conservation and genericity, as shown in the earlier bridge. The familiar fact that a reduced density matrix admits multiple remotely generated ensembles is part of quantum steering; it does not by itself make those decompositions distinct underlying local realities. See [1](https://arxiv.org/html/1905.03614).

For the proposed experience reading, make the following additional, strong assumptions explicit:

1. Alice can realize the pair or triple POVM in appropriately comparable preparations, with the stated quantum outcome weights.
2. Bob is a real subject in the relevant physical situation, and the steered pure state `Π_m` alone fixes a definite local quality `g(m)`, with the **same** function `g` in both contexts. No extra hidden or contextual local variable affects that quality.
3. The distribution of locally accessible/operationally distinguishable qualities is the Born-weighted distribution over the outcomes, with no selective conditioning on Alice's setting or outcome.
4. Those local quality distributions must be independent of Alice's distant measurement choice when the ordinary operational no-signalling conditions apply.

Nothing here says that such a subject actually exists or that these weights are in fact subjective incidence weights. Those are the **test hypothesis**, not an established identity. “Locally accessible” is load-bearing: if the purported difference cannot in any way affect a local observation, report, choice, or other accessible record, the operational signalling conclusion does not automatically follow. A necessary whole can still be tested against no-signalling by comparing appropriately controlled actual subensembles; this does not require metaphysically open choices.

## 2. The generic pair–triple theorem

For a measurable set `D` of distinguishable qualities, no-signalling under the above assumptions requires equality of the full pushforward distributions:

```text
Σ_(i∈pair) q_i 1[g(−n_i) ∈ D]
  = Σ_(j∈triple) q_j 1[g(−n_j) ∈ D]       for every D.
```

This is stronger than equality of their means. Write the two pair values as `x` and `y`.

* If `x≠y`, their distribution has two atoms, each of weight `1/2`. For the triple distribution to be identical, some nonempty proper subset of its three weights must sum to `1/2`. That is impossible: each single weight is strictly less than `1/2`, while each two-weight sum is strictly greater than `1/2`, since it is `1` minus the remaining weight.
* Therefore `x=y=c`. The pair distribution is the point mass at `c`. As all three triple weights are strictly positive, equality requires all three triple values also to equal `c`.

Hence `g` must be the same on the five states. If, in addition, its weighted mean is required to equal zero, the common value is `c=0`. This proof allows arbitrary distinct quality labels; it is not limited to a numerical sign function, continuous functions, or the symmetric example. The finite tests check examples; the argument is the general proof.

**Broader conditional corollary:** if the same `g` must satisfy operational no-signalling for *all* antipodal projective measurements on Alice and one fixed equal-weight trine POVM, then it is constant on the entire pure-state sphere. Every antipodal pair distribution must equal the same trine distribution; the two-versus-three argument forces both values in every pair to equal one common value. This broader statement assumes access to that whole family of measurement contexts; one fixed five-ray event alone only constrains its five states.

## 3. Why the earlier signed quantity fails the direct experience test

For the symmetric conserved configuration, take `a` to be the center-frame direction of the first pair ray, and use the prior candidate

```text
g(−n_i) = −a·n_i.
```

The two predicted **distributions of definite local values**, if one makes that direct identity, are

```text
Alice chooses pair:   −1 with weight 1/2;    +1 with weight 1/2.
Alice chooses triple: +1/2 with weight 1/3;  −1/4 with weight 2/3.
```

Both means equal zero, but the supports are disjoint. If those quantities were directly distinguishable by Bob without access to Alice's outcome, one observation would reveal which of these two settings was chosen, under the stipulated controlled-preparation assumptions. This is why **a zero weighted mean or equal reduced density matrix alone is not enough to establish no-signalling for a proposed extra experiential variable**.

The point is not that quantum mechanics signals. Standard quantum mechanics assigns `−a·n_i` as a **conditional expectation**, not as a single definite outcome of Bob's spin measurement. Nor does a remote state conditioned on Alice's result automatically represent Bob's complete local ontology. The conflict arises from adding the proposed direct identification and accessible-experience rule.

## 4. Constructive repair: distinguish conditional mean from actual outcome

Let Bob instead measure `a·σ`, with actual physical result `y∈{−1,+1}`. Under the stipulated singlet model,

```text
P(y | i) = (1−y a·n_i)/2,
E[y | i] = −a·n_i.
```

For the pair, the conditional results are definite and opposite to the corresponding pair direction. For the triple, the probabilities of `y=+1` are

```text
(3/4, 3/8, 3/8).
```

With the triple weights `(1/3,1/3,1/3)`, the overall positive probability is

```text
(1/3)(3/4 + 3/8 + 3/8) = 1/2,
```

and the negative probability is also `1/2`. The pair measurement gives the same local distribution `(1/2,1/2)`. The local result is definite in an individual record while the conditional expectation can be fractional; mixing up the two caused the apparent signalling in the direct candidate.

As a **test only**, suppose an additional independent physical–experiential identity associated the two actual local results with felt values `+1` and `−1`. The two settings would then give the same local distribution and a zero weighted mean while both signs occur. A negative local value would remain negative and real, not be erased by the positive value. This is a way to make the construction consistent with no-signalling; it does **not** establish that a spin result is a subject or a felt quality, that actual pleasure and suffering have equal probability, or that these are the weights of the whole.

## 5. An explicit block of definite records

The conditional probabilities in the repair can be represented by one fixed finite table; no irreducible draw is required as part of this mathematical example. Take 24 equally counted seed labels `s=0,…,23` for each Alice setting:

* Pair: `i=s mod 2`; Bob's `y=−1` for `i=0`, `+1` for `i=1`.
* Triple: `i=s mod 3`, `r=floor(s/3)`; Bob's `y=+1` when `r` is less than `6`, `3`, or `3` respectively for `i=0,1,2`, and `−1` otherwise.

The pair gives twelve records of each Bob outcome. The triple gives `(6,3,3)` positive and `(2,5,5)` negative Bob outcomes across its three eight-record groups. Thus it matches the conditional probabilities above **exactly**, while also giving twelve `+1` and twelve `−1` locally. Each seed appears in both settings' recorded subensembles.

This table is a consistency witness, not an explanation of why records exist or why their counting measure is the experiential measure. For the same seed, Bob's response can differ between Alice's two settings; individual response is context-dependent, and conditioning on an accessible seed would expose that dependence. Consequently the model's no-signalling statement holds only for its specified unconditioned distribution. It does not supply a relativistically covariant law, establish global necessity, or independently derive the Born rule. Its scope is the two Alice settings and one Bob setting here; the separate Bell construction addresses additional settings but does not combine all of them with a subject model.

## 6. Consequence for zero's constitution

This result tells us **which version of the proposed bridge cannot work** and gives a sharper target for one that might:

* The local structural zero arising from conservation cannot be promoted directly into a distribution of definite local felt values by identifying each conditional expectation with an experience. With the stated assumptions that would allow signalling or force the values to be trivial.
* A viable physical–experiential identity must specify actual local events/organization and subject incidence, not merely attach feelings to remotely conditioned descriptions. It must account for the **full distribution** of locally accessible experience, not only its mean.
* Distinct conditional ensembles can give the same local outcome distribution, so no-signalling does not require all real local events or experiences to vanish. It remains to show why a physical process constitutes those experiences and why the relevant whole-level measure and quantity are zero.
* The argument does not establish that the user's full no-residue demand is impossible; it exposes assumptions an eventual constitution must avoid or justify. It also does not establish a fundamental preferred foliation or interpret probability as irreducible chance.

This is a genuine constraint on the experiential side of the sphere framework, not just a formal balance: it shows how a seemingly natural identification would conflict with an operational physical requirement, and gives an exact non-signalling, definite-record alternative under clearly stated assumptions.

## Verification

```text
python -m unittest verification.zero_experience_steering_no_signalling_test -v
```

Seven standard-library checks verify the two unequal pushforward distributions despite equal means, the symmetric and asymmetric triple subset property, an exhaustive finite-label control, exact conditional and unconditional record counts, contextual seed dependence, and the persistence of negative local values. The general theorem is the proof in section 2; the tests do not establish real subjects, empirical incidence weights, or fundamental physical laws.
