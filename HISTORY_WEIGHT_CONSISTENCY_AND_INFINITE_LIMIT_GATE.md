# History weights: local checks, consistency and the infinite limit

## Result

Agreement with a one-trial quantum probability is not enough to establish agreement with probabilities for a subject's **sequence of records**. Even if every individual record bit is fair, a coherent weighting of complete histories can make successive bits correlated and predict very different long-run records.

There is a second, more subtle constraint. A normalized, positive weighting can exist at **every finite record length** and be perfectly consistent under shortening records, while nevertheless failing to be the restriction of any single integrable weight on the original infinite-history measure. The alternative infinite-history probability law itself can still exist: what fails is its representation as one ordinary density relative to that particular reference measure.

The construction below applies standard likelihood-ratio martingales, exchangeability and the strong law to the framework's unresolved experience–record–measure interface. These are established mathematical ideas; the contribution is their explicit joint application to this interface, not a claimed new theorem or new empirical result.

## 1. What is being compared

The candidate whole is timeless, with plural local perspectives and genuine possibilities actual within it. Nothing here introduces an outside creator or selects a universe in time. Consider only an idealized **ordered record within a perspective**, represented by an infinite binary string `h=(h₁,h₂,...)`. The index `n` expresses stipulated record order, not a fundamental universal clock. That such records or subjects exist is not proved by this model.

Let `P` be the standard fair independent-bit measure. It can serve as an effective description of repeated, independently prepared quantum measurements with equal Born probabilities. It is stipulated here rather than derived from plenitude. Let `Q` be a different proposed measure on the **same** set of records:

```text
Q = (1/2) Bernoulli(3/4)^⊗∞ + (1/2) Bernoulli(1/4)^⊗∞.
```

The displayed mixture is a mathematical description of weights; it need not be a temporal lottery over realities. Every finite record has positive P- and Q-weight; the toy separately stipulates that every infinite binary string is in the formal whole. This does not establish that every string is genuinely physically possible or inhabited by an experience. Actuality, positive measure and typicality are different claims.

For a specified length-n word with `k` ones,

```text
P_n(word) = 2^(−n),
Q_n(word) = 1/2 [(3/4)^k (1/4)^(n−k)
                + (1/4)^k (3/4)^(n−k)].
```

Both probability laws are normalized and consistent when the final bit is forgotten. The Q-law is invariant under finite permutations of bit positions, but exchangeability is not independence. Standard de Finetti theory provides general background for such mixtures; no general theorem is needed to verify this explicit example.

## 2. Single records hide a measurable joint difference

For every position `i`, both laws have

```text
P(h_i=1) = Q(h_i=1) = 1/2.
```

However,

```text
                         P             Q
P or Q(11)              1/4           5/16
P or Q(10)              1/4           3/16
probability h₁=h₂       1/2            5/8
probability h₂=1 | h₁=1 1/2            5/8
```

Thus Q agrees with the single-record marginal but not with the independent repeated-record law. In Q, the same latent component applies throughout a record; it is not reselected independently for each bit. If it were reselected each trial, this difference would vanish. The mixture is a model of a history law, not a demonstration of a physical hidden variable or an experiential mechanism.

**Operational bridge required.** If a candidate theory claims that Q describes the frequencies of consecutive, unconditionally recorded outcomes in a specified repeatable laboratory protocol where P is independently justified, the pair statistics are discriminating. That empirical claim requires linking the indexical/history measure to the actual sampled reports, and controlling preparation, drift, detector memory, losses, setting choices and dependence. If Q instead describes a different or postselected reference class, the raw laboratory test does not automatically apply. A purely metaphysical change of measure with no report bridge is not a detected anomaly.

As an illustrative design, partition a single record into disjoint adjacent pairs and mark whether the two outcomes agree. Under P these agreement indicators are independent Bernoulli `1/2`. Under either component of Q they are independent Bernoulli `5/8`; because **both components give the same agreement rate**, the indicators remain independent even after mixing. At the midpoint `9/16`, Hoeffding's inequality gives at most `exp(−m/128)` error for either side; `m=473` pairs (946 individual trials) make each bound below `0.025`. This assumes the ideal laws and exact protocol above; it is not experimental evidence, a real confidence interval or a feasible estimate in the presence of systematic errors. Other pair-level distributions or persistent noise can invalidate the IID bound.

Even a real deviation would not identify its cause: an ordinary classical mixture of device biases yields the same Q record distribution. Distinguishing such an apparatus model from an experience-weighting model requires independent device calibration and further falsifiable differences; correlations by themselves do not reveal subject constitution.

## 3. Finite-horizon weights can be consistent without one global density

At each finite `n`, define the nonnegative relative weight

```text
L_n(word) = Q_n(word)/P_n(word)
          = 1/2 [(3/2)^k (1/2)^(n−k)
                + (1/2)^k (3/2)^(n−k)].
```

The exact finite checks establish, and the formula immediately gives,

```text
E_P L_n = 1,
L_n(word) = [L_(n+1)(word·0) + L_(n+1)(word·1)]/2.
```

The second line is the martingale condition `E_P[L_(n+1) | first n bits]=L_n`. It expresses consistency of the proposed Q weights on nested record events. It is *not* a claim about a subject's personal identity through time or a rule that one subject must conserve mass through physical branching.

A useful closed check is

```text
E_P[L_n²] = (1/2)[(5/4)^n + (3/4)^n],
```

which grows without bound. This growth alone is not a general proof of non-uniform integrability; here the following stronger argument establishes it.

By the strong law, under P the fraction `k/n` tends to `1/2`. Along P-almost every history, both terms in L_n tend exponentially to zero, with asymptotic nth root `√3/2`. Consequently

```text
L_n → 0  P-almost surely,     but     E_P L_n = 1 for every finite n.
```

Therefore the weights are not uniformly integrable and do not converge to their limit in `L¹(P)`. It would be wrong to substitute the pointwise limit `L∞=0` into the weighting formula and conclude that Q is the zero measure. Finite normalizations survive by concentrating weight on increasingly rare P-histories.

## 4. Why no single integrable P-density can represent this Q

Define the measurable events

```text
A = {limiting fraction of ones = 1/2},
B = {limiting fraction of ones = 1/4 or 3/4}.
```

The strong law yields `P(A)=1`, `Q(A)=0`, `P(B)=0`, and `Q(B)=1`. Hence P and Q are **mutually singular**, even though they give positive probability to every finite cylinder and are mutually absolutely continuous at each finite horizon.

Suppose there were a nonnegative P-integrable global occurrence density `W` with `E_P W=1` and `Q(E)=E_P[W 1_E]` for all measurable history events E. Then `P(B)=0` would force `Q(B)=0`, contradicting `Q(B)=1`. No such W exists. This is a conditional restriction on a proposed way of building the subject measure; it is not a proof that Q is incoherent or that an infinite measure must be a density on P.

The converse design route is available: an **explicitly chosen** global nonnegative integrable W defines a measure by that formula. Its finite prefix weights are `E_P[W | first n bits]`, a uniformly integrable martingale; they consistently recover the same global measure. For a concrete control, put

```text
W = 1 + (1/4)(2h₁−1)(2h₂−1),       3/4 ≤ W ≤ 5/4.
```

Its mean under P is one. Its resulting law agrees with Q's entire first-two-bit table, including `5/8` pair agreement, but every later bit remains fair and independent of that pair; the second pair has agreement `1/2`, not Q's `5/8`. Since W is bounded, this law retains every P-almost-sure event, including limiting frequency `1/2`. Thus an early correlation alone does not establish a singular infinite limit, and requiring an integrable global density does **not** force every finite record law to be independent.

Alternatively, Q may be specified directly as an independent probability measure, as in this example, without a P-density. A theory must say which route it takes and why; either is an additional measure choice. Uniform integrability here concerns densities with respect to a normalized reference probability, not a universal solution to all unbounded or infinite cosmological measures.

## 5. Implications for the research programme

1. **Subject constitution:** specify which ordered records genuinely belong to a continuing subject, and which local records are eligible. Neither P nor Q solves that identification.
2. **Physical benchmark:** specify the state, preparations, instruments, record events and their multi-trial joint predictions. A one-shot Born match is insufficient; it is also not evidence of the independent-trial assumption.
3. **Measure bridge:** define an occurrence measure on the same record algebra and explain its meaning. For nested prefixes check that marginalizing future records preserves earlier weights; for a fixed P-density construction check integrability and the applicable limiting conditions. If the reference class changes with record length, projective consistency is an extra assumption, not automatic.
4. **Observation and locality:** explicitly decide whether that measure predicts unconditioned records, conditioned records, or self-locating credences. Apply the [no-signalling gate](SUBJECT_WEIGHT_STEERING_AND_NO_SIGNALLING_GATE.md) only when the operational bridge warrants it. Preserve passive redescription invariance without assuming arbitrary active swaps are symmetries.
5. **Infinite case:** justify the limiting measure or its regularization and compare different prescriptions. The present construction shows why finite agreement and finite normalizations do not decide that limit; it does not establish that the real whole has infinitely many subjects.

These requirements fit the preferred substrate-independent experiential ground, but do not derive experience, self-sufficiency, plenitude, empirical quantum law, spacetime, or a unique reference class. No universal subject is assumed.

## Sources and reading scope

- Kyle Siegrist, [*Convergence*](https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/17%3A_Martingales/17.05%3A_Convergence): chunks 0–1 of 4 read, including uniform-integrability martingale convergence and the likelihood-ratio example; remaining chunks not fully read. We use the standard results, not an original derivation.
- Steven Lalley, [*Conditional Expectation and Martingales*](https://galton.uchicago.edu/~lalley/Courses/313/Martingales.pdf): first 2 of 6 extracted chunks read (conditional expectations and martingale definition); the remaining notes were not fully read.
- Gavalakis and Kontoyiannis, [*An Information-Theoretic Proof of a Finite de Finetti Theorem*](https://arxiv.org/abs/2104.03882v2): abstract and search excerpts read; full available paper and proof were not audited. It concerns a finite approximation theorem, distinct from the elementary explicit mixture above.
- Don Page, [*Born Again*](https://arxiv.org/html/0907.4152v1): first of four HTML chunks and search excerpts read; full article not audited. His averaged-density/conditional-probability proposal is relevant context, not a derivation of this record model. Also see the earlier fully text-read [*Born's Rule Is Insufficient in a Large Universe*](https://arxiv.org/html/1003.2419v1).
- Joshua Cooperman, [*Rescuing the Born Rule for Quantum Cosmology*](https://arxiv.org/html/1010.3395v2): first of 18 HTML chunks read, not the full paper or proofs.
- The Oxford slides [*Exchangeable random variables: Theorems of de Finetti, Hewitt and Savage*](https://www.stats.ox.ac.uk/~steffen/teaching/grad/definetti.pdf) appeared in search excerpts but the PDF fetch failed; they were not read in full. The HTML fetch for Gavalakis and Kontoyiannis also failed; the linked abstract and PDF are available, but the full PDF was not read.
- The [earlier symmetry and subject-measure gate](PLENITUDE_SYMMETRY_AND_SUBJECT_MEASURE.md) already explained full support versus singular typicality and the weakness of exchangeability. The present extension shows **matching one-bit marginals, a specific multi-record test, the consistent likelihood-ratio martingale and the global-density obstruction**. The [operational-probability reconstruction](OPERATIONAL_PROBABILITY_RECONSTRUCTION.md) supplies a separate conditional quantum trace-form result.

## Reproduction

Run `python verification/history_weight_martingale_gate.py`. The [exact rational verifier](verification/history_weight_martingale_gate.py) checks all prefix counts through length 30, normalization, projective consistency, the martingale relation and the second moment; checks the agreement-block law through eight pairs; and computes the illustrative Hoeffding bound. The [receipt](verification/history_weight_martingale_gate.json) records the checks. Finite calculations do not prove the infinite strong law, uniform-integrability conclusion or any physical or phenomenal premise.
