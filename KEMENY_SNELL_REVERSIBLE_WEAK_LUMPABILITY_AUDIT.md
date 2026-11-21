# Reversible weak lumpability: a stronger constraint on the integrated candidate

## Result

The supplied [*Finite Markov Chains*](sources/uploads/Kemeny_Snell_Finite_Markov_Chains.pdf) makes a stronger conclusion available for the existing E-L four-spin model. Its Theorem 6.4.8 states that **for a regular reversible chain, weak lumpability implies lumpability**. We verified both assumptions for the actual toy kernel. Consequently, its previously identified non-lumpable projections cannot become exact homogeneous first-order Markov chains merely by selecting a favorable initial distribution. The all-edge relational projection does have an exact homogeneous Markov kernel for every initialization.

This is an application of a published theorem, **not a new general theorem**. It strengthens a physical-model constraint, not a claim about a brain or a subject. Open subjects need not be dynamically closed, experience is accepted as a datum, and no identification of a selected set with a subject or its felt quality follows.

## Source and coverage

The user supplied Kemeny and Snell, [*Finite Markov Chains: With a New Appendix “Generalization of a Fundamental Matrix”*](https://link.springer.com/book/9780387901923), ISBN 978-0-387-90192-3. The 238-page scanned PDF is retained at the local link above, SHA-256 `8380bc85e6740a4baac5ad811fc0ad81db625e430511d300e856869d08350537`. We read the text of printed sections 6.3–6.4, pp. 123–140, using OCR, and visually checked printed pp. 124, 132, 134–136 and 138–140, including both pages of the proof of Theorem 6.4.8. The remaining book, other figures, exercises and external references were not systematically inspected; imperfect OCR on unverified matrix examples should not be treated as a reliable transcription. [Burke and Rosenblatt, *A Markovian Function of a Markov Chain*](https://doi.org/10.1214/aoms/1177706444), whom the book cites for part of section 6.4, was identified from bibliographic search but not read here.

The book distinguishes:

- **Lumpability** (Definition 6.3.1 and Theorem 6.3.2, p. 124): all starting distributions yield a homogeneous Markov chain with the same transition matrix. This holds exactly when all fine states in a given block have equal transition sums into each block. This is often called *strong* lumpability.
- **Weak lumpability** (p. 132): at least one initial distribution yields a Markov chain in the book's sense. For regular chains, Theorem 6.4.3 additionally relates this to equilibrium (pp. 134–135).
- **Theorem 6.4.8** (pp. 138–139): for reversible **regular** chains, weak lumpability implies lumpability. Its proof uses reversibility and a positive-semidefinite argument; we cite rather than claim it as our own. Its conclusion should not be applied to an arbitrary nonreversible chain.

We use “homogeneous first-order Markov” to make the transition-matrix convention explicit. The result is not asserted for arbitrary time-inhomogeneous models, approximate Markov models, restricted observation windows, changing interventions, memory-augmented states, or different time grains.

## Verification in the same four-spin sector

The [fixed plan](KEMENY_SNELL_REVERSIBLE_PROJECTION_FIXED_PLAN.md), exact [code](verification/kemeny_snell_reversible_projection.py), [tests](verification/kemeny_snell_reversible_projection_test.py), and [receipt](verification/kemeny_snell_reversible_projection.json) reuse the existing random-site heat-bath transition matrix at `t=1/4`. The verifier checks the exact positive stationary distribution, all 256 detailed-balance equalities, every stochastic row, and positivity of all 256 entries of `P^4`. Thus it checks regularity and reversibility instead of assuming them. A step is a local model update, not an external universal clock or a temporal actualization mechanism.

| Retained description | Max strong block-TV discrepancy | Some initial distribution gives an exact homogeneous Markov chain? |
|---|---:|---|
| complete left pair `(s0,s1)` | `1/21` | No |
| left mismatch `q01` | `1/21` | No |
| left and middle mismatch `(q01,q12)` | `5/42` | No |
| two outer mismatches `(q01,q23)` | `2/21` | No |
| any-mismatch bit | `5/24` | No |
| all three edge bits `(q01,q12,q23)` | `0` | Yes, for every initialization |

The maximum block-TV discrepancies were obtained in the earlier [relational dynamics gate](INTEGRATED_SUBJECT_CONTEXT_AND_RELATIONAL_DYNAMICS_GATE.md) and [structure audit](CHALMERS_COMBINATION_FULL_PAPER_AND_STRUCTURE_AUDIT.md); the present verifier recomputes them using those existing routines and cross-checks the five shared projections against both routines. The stationary two-step calculation is separate. The five “no” answers apply the **contrapositive** of Theorem 6.4.8 after verifying its hypotheses. This is stronger than the earlier result that no *single* projected kernel works for **all** initial distributions. The table does not say that all stochastic models or all experiential accounts using those variables are impossible.

## A directly calculated two-step consequence

For a stationary projected process, let `Q` contain its actual one-step conditional probabilities and let `R` contain its actual two-step conditional probabilities. A time-homogeneous first-order Markov process must have `R=Q²`. In this model the exact maximum entrywise gaps are:

| Projection | Maximum `|R−Q²|` |
|---|---:|
| left pair | `5/2352` |
| left mismatch | `5/2352` |
| left and middle mismatch | `25/3528` |
| two outer mismatches | `25/4704` |
| any-mismatch bit | `1651/95616` |
| all edge bits | `0` |

For instance, conditioned on stationary `q01=1`, the actual probability of `q01=1` two updates later is `201/448`, while squaring the exact one-step conditional matrix gives `4201/9408`; their difference is `5/2352`. These fractions are exact ensemble predictions of the toy model, not measured probabilities, error bars or predictions about actual consciousness. Different rows predict different outputs, so the numerical gaps are not a monotonic ranking of useful descriptions.

A positive two-step discrepancy independently disproves homogeneous Markovity **for the stationary initialization**. The no-initialization conclusion above additionally uses the cited theorem and its checked conditions. A zero two-step discrepancy alone is not generally sufficient to prove a projected process Markov: longer histories can matter.

## Why the reversible assumption matters

The book's Example 6.4.2 on p. 134 supplies a contrasting regular, nonreversible chain. Its transition matrix, in the book's state order, is

```text
      1/4   1/4   1/2
P  =   0    1/6   5/6
      7/8   1/8    0
```

For the partition `{s1}`, `{s2,s3}`, transition probabilities to the first block are `0` and `7/8` from the two states in the second block: strong lumpability fails. The verifier checks `P²` is strictly positive, the stationary distribution is `(7/16,3/16,3/8)`, and detailed balance fails. It also verifies that the two stationary conditional within-block distributions are preserved by a transition followed by conditioning on either block. Therefore, by induction over observable histories, the equilibrium projected process is a homogeneous Markov chain despite failing strong lumpability. The script checks this invariant conditional-distribution property, **not just** a two-step equality. This control illustrates a known textbook example, not an original counterexample or evidence that the E-L model is weakly lumpable.

## Consequences for the framework

If the existing pair rule is retained, the candidate cannot claim that a fortunate preparation makes either its entire local pair or its mismatch bit an exact autonomous homogeneous first-order process. It can still describe an **open** locally selected perspective interacting with context, supply inputs or memory, or use a richer state representation. The full three-edge quotient is one exact representation, but it does not decide whether there are one, two, overlapping, or no subjects in that model. Nor does its predictive success show why `q=1` would feel unpleasant.

The experiment-free result is therefore a more precise division of labor: the physical context problem has an exact constraint and a specific finite predictive repair; subject incidence, persistence, phenomenological content and their constitutive bridge remain separate. An experience-respecting connected-component rival shares the same kernel and this dynamical finding but stipulates a different subject boundary. An experience-respecting neutral-ground rival can also share the dynamics while owing its own bridge. No global subject, physical string identification or emergent-spacetime reconstruction follows.

C3 remains **full structural and experiential intelligibility**, jointly with C1–C7. B4–B5/F2, B9/F3 and B10 remain open; this theorem and the regressions do not pass the formal battery.
