# Simulation, measure, and explanatory closure

## Consolidated surviving thesis

> Bostrom’s simulation argument is a conditional population-and-credence argument, not an ultimate explanation of reality. A reconstruction aimed at complete intelligibility must specify actual implementations, distinguish physical multiplicity from duplicate descriptions, justify its observer weighting, and explain both phenomenality and its global framework. Algorithmic probability supplies a useful family of description-based models and some robust asymptotic comparisons. It does not, by itself, supply a canonical physical measure, make copies irrelevant, or turn a self-referential specification into a self-explanatory world. Ancestor-simulation does not entail arbitrarily deep self-similarity. Where implementation, resources, or selection remain unspecified, the surviving conclusion is conditional or underdetermined—not that a zero-residue reconstruction has been achieved.

The strongest result is a disciplined set of constraints on reconstruction. The attachment does not establish that its final unbounded-closure proposal is uniquely intelligible, or that it constitutes a minimally changed version of Bostrom’s argument.

## 1. Preserve the distinction between a conditional argument and a theory of everything

The original argumentative pattern distinguishes:

1. Conditions under which conscious observers can be implemented in simulations.
2. Estimates of simulated and nonsimulated observer populations.
3. A principle connecting those populations to first-person credence, given the available evidence.

A schematic counting model can write

\[
f_{\mathrm{sim}}=\frac{\alpha}{1+\alpha},
\]

where \(\alpha\) is an appropriate ratio of simulated to nonsimulated observers. Expressing \(\alpha\) through survival rates, simulation activity, and simulation numbers requires assumptions about observer yields and the reference population. A raw count of simulated worlds cannot automatically substitute for an observer count.

The “+1” is a normalized baseline term. It is not itself an argument for an unexplained ontological foundation. Nor does allowing simulations within simulations force an infinite tower: a finite implementation hierarchy is possible. Whether its overall framework is explained is a further question.

The counting model may be coherent as a conditional inference even if it leaves its parameters unexplained. Under the present project’s stronger requirement, those parameters cannot remain ultimate brute facts. But an incomplete explanation is not thereby a false conditional argument.

A related precision matters: infinitely many observers do not automatically make every observer probability undefined. What fails is naive division of infinite counts without a justified measure or limiting prescription. Some infinite spaces admit well-defined probability measures; infinite uniform counting is not automatically one of them.

## 2. Faithful extension versus replacement

The least disruptive extension makes the hidden assumptions explicit:

- What concretely implements an observer?
- Which observers are relevant to the evidence?
- Are weights per episode, subject, duration, realization, or something else?
- How are genuinely distinct copies treated?
- What physical and probabilistic framework fixes the population?

A representation-independent implementation relation is useful. Intentional simulation may be generalized to unintentional implementation, but only if an account of implementation excludes arbitrary mappings from almost any physical system to almost any computation.

Removing agency does not remove the explanatory burden concerning implementation abundance. It replaces a question about motives with a question about which implementing systems occur and why.

Replacing observer-count weighting with an algorithmic prior is a more substantial change. It may be worth investigating, but it changes the inference rather than deriving the original inference from deeper principles. The reconstruction should therefore maintain two explicit branches:

- **Population branch:** retain observer multiplicity and justify the associated measure and sampling assumptions.
- **Description branch:** assign algorithmic weights to descriptions or centered models and justify their relation to physical observers.

Neither branch may borrow the other’s conclusion without an explicit connecting argument.

## 3. Algorithmic probability: what is justified

Fix an appropriate universal prefix machine \(U\). Prefix complexity \(K_U(x)\) is the length of a shortest self-delimiting description of \(x\). Algorithmic probability instead sums weights of all qualifying descriptions; in standard finite-output settings its associated universal semimeasure satisfies a coding relation of the form

\[
m_U(x)\asymp 2^{-K_U(x)}.
\]

The relation is up to multiplicative constants, not an exact definition valid for every possible formalism.

Several genuine mathematical facts are useful:

- Prefix-free code weights satisfy Kraft’s inequality.
- Suitable universal semimeasures dominate the appropriate class of lower-semicomputable semimeasures up to constants.
- Changing between optimal universal description languages changes complexity by at most an object-independent additive constant.
- Thus, if a rate \(K_U(x_d)/d\) has a limit, that limit is unchanged by such a machine change. Liminf and limsup rates can be used when no limit exists.

These results concern specified mathematical constructions. They do not derive a physical observer measure from normalizability alone. Many normalized or subnormalized weightings exist. Dominance requires an explicitly chosen effective class, not merely that hypotheses are describable.

Likewise, multiplicative weights with additive costs can yield exponential form under suitable assumptions. Those assumptions do not uniquely determine what physical implementation costs, or how the exponential rate should be fixed once costs have physical meaning.

### Identity under pauses is not probability invariance

Substrate independence concerns the conditions for experience to occur. It does not automatically establish that a realization’s probability weight is independent of runtime, energy use, or duration.

Even if pausing an implementation preserves its experiential sequence, an observer-moment measure could depend on duration, and a world prior could depend on resources. Choosing between time-blind and resource-sensitive measures is therefore substantive. Neither choice follows from substrate independence alone, and “speed prior” should not be treated as a single automatically determined formula.

## 4. Machine robustness is not automatically gauge redundancy

A physical gauge transformation changes representation without changing the physical situation or predictions. Changing an algorithmic reference machine can change finite prior odds. Calling that a gauge does not make the change physically redundant.

The robust conclusion is narrower:

> Some asymptotic properties are independent of the chosen optimal universal machine; particular finite probabilities generally need not be.

For any fixed pair of machines, their translation constants are finite. There is no universal finite tolerance covering every possible machine choice. A finite comparison can be meaningful relative to a justified coding scheme or restricted family, but not thereby canonical across all universal machines.

A description-length advantage \(\Delta\) can correspond to a factor of roughly \(2^\Delta\) in an appropriate algorithmic comparison. Evidence for a whole hypothesis, however, may involve sums over many descriptions rather than only its shortest one. The attachment’s estimates of a “natural” translation constant are not established and should not be used as physical resolution limits.

Nor does representation robustness replace the zero-residue standard. A statement can be invariant yet unexplained. Algorithmic incompressibility is not the definition of metaphysical bruteness: a short law may remain unexplained, while a complicated outcome may have a probabilistic explanation whose adequacy requires separate assessment.

## 5. Copies, addresses, and what the measure counts

The attachment’s strongest local calculation is conditional. If a world has weight \(q(w)\), and addresses within it receive prefix-code weights, then

\[
\sum_i q(w)2^{-|a_i|}\leq q(w).
\]

This caps the total weight assigned through that chosen addressing construction. It does **not** establish that physical copies are irrelevant under every admissible observer measure.

The construction has already chosen to distribute a bounded world weight among addresses. Another scheme can weight worlds by observer number or use different centered sampling assumptions. Even within the bounded construction, the number and arrangement of matching observers can change how much weight is assigned to a particular experience. A ceiling is not independence from multiplicity.

The surviving distinction is:

- Repeated descriptions of one execution should not be silently counted as additional physical observers.
- Distinct executions should not be silently identified merely because their experiential descriptions match.
- Whether and how their weights add requires a specified measure.

Consequently, neither simulation abundance nor agents’ motives have been shown to disappear from every reconstruction.

## 6. Depth laws require more than compressibility

Ancestor-simulation concerns the simulated content’s relationship to a host’s past. It does not entail:

- a computable self-similar sequence of hosts;
- an implementation of the same experience at every depth;
- unlimited resources;
- a depth-independent localization cost;
- a particular prior over depths or capacities.

That correction survives strongly.

For a specified weighted implementation model, define \(W_d(x)\) as the total weight of admissible depth-\(d\) routes reproducing experience \(x\). An aggregate rate such as

\[
\Lambda(x)=\lim_{d\to\infty}-\frac{1}{d}\log_2 W_d(x)
\]

can be useful if it exists and the weights and route-counting rules are well-defined. If two constructions differ only by uniform multiplicative bounds, this rate is robust between them. But zero rate does not imply computable generation or self-explanation. Subexponential decay has many forms, and a rate may fail to exist.

Similarly, zero algorithmic complexity rate does not imply that an infinite sequence is computable. Nor can the complexities of infinitely many distinct finite prefixes remain uniformly bounded: only finitely many outputs have descriptions below a fixed length. A finite description of an infinite generator is a different object from uniformly bounded descriptions of all its finite prefixes.

A universal prior on integer depth is a model choice. Summing weights over all strings of length \(d\) does not automatically give the same weight for the restricted subset of physically feasible, experience-preserving routes. The required lower bound must be proved for that subset.

Universal integer semimeasures do have unusually slow, non-effectively controlled tails under appropriate definitions. That mathematical phenomenon does not by itself establish a physical depth distribution. The attachment’s later product

\[
P(d)\asymp m(d)\,T(b\phi^{-d})
\]

requires a justified capacity prior, a joint model for capacity and depth, and the relevant independence or conditional-weight assumptions. It remains a conjectural construction, not a surviving derived physical law.

A measure supported on finite integers assigns zero probability to infinite depth by construction. It does not establish that an additional infinite-depth possibility has zero weight in every larger model.

## 7. Finite resource bounds: retain the conditional mathematics

Under an explicit resource model, suppose that each nested level has capacity

\[
S_{d+1}\leq\phi S_d,\qquad 0<\phi<1,
\]

and that the target realization requires capacity at least \(b>0\). Then any feasible depth obeys

\[
d\leq\frac{\log(S_0/b)}{\log(1/\phi)}.
\]

This is a valid conditional bound. An additive-overhead assumption yields a different bound.

But neither overhead model follows merely from the word “simulation.” The resource accounting must specify simultaneous versus sequential execution, time-memory tradeoffs, compression, shared computation, fidelity, and what makes implementations distinct. The same numerical state-count measure must be applicable across levels.

The attachment’s cosmological capacity estimate, observer-world size, and overhead fraction are unverified model inputs. They do not establish that actual ancestor-simulations are universally limited to tens or hundreds of levels. A finite physical depth cutoff could be explained by physical resources; it need not be brute merely because an algorithmic prior also allows larger capacities.

Identifying supposedly different levels as one execution may make depth a redundant descriptive coordinate. That is an important alternative to multiplying observers by description. It does not imply that every cyclic implementation structure contains only one observer: the number of actual occurrences still requires analysis.

## 8. Fixed points are not completed explanations

A proposal such as

\[
R\cong\operatorname{Host}(R)
\]

requires a definition of the objects, host operation, and isomorphism. Universality of computation does not canonically specify that operation, establish a unique solution, or show that a mathematical solution is physically actual.

Kleene’s recursion theorem concerns computable self-reference and extensional fixed points of program transformations. It is not a theorem that every proposed physical host operation has a unique, productive, resource-feasible universe as its fixed point. A self-referential program may diverge or specify no suitable observer realization.

The finite-set fact that no finite set is bijective with a proper subset applies only after that structure has actually been established. It cannot simply be read off the informal Host equation. An infinity result within a proposed model also leaves the model’s own explanatory sufficiency to establish.

The strongest global proposal is therefore:

> Seek an internally specified, non-brute explanatory structure whose self-reference is mathematically coherent, physically interpretable, and genuinely explanatory rather than merely circular.

The attachment does not show that only such a fixed point can satisfy complete explanation, or that its proposed closure does so. A finite specification can summarize an infinite structure without explaining its actuality.

## 9. What remains mandatory for zero residue

No local success removes the following obligations:

1. **Implementation:** distinguish genuine physical realization from arbitrary computational interpretation.
2. **Phenomenality:** explain why the relevant realization is an experience and what fixes its character and subject boundaries.
3. **Measure:** justify world weights, centered weights, and any resource dependence.
4. **Global actuality:** explain why this framework obtains, not merely what follows if it does.
5. **Empirical accountability:** connect the model to evidence without assuming a privileged outside viewpoint or declaring internal evidence immune to distortion.

The lack of an external observer does not dissolve skeptical or evidential problems. Internally accessible records can still be misleading relative to the world that produces them.

## Final formulation

> The faithful starting point is Bostrom’s conditional relation between implementation assumptions, observer abundance, and centered credence. The strongest extension makes these components explicit and subjects each to the demand for explanation. Algorithmic priors provide a useful alternative modeling branch, not a derived replacement for observer counting. Machine-robust asymptotics, resource bounds, and fixed-point constructions are valuable only within their stated assumptions. None establishes phenomenal identity, canonical observer weighting, unlimited self-similar depth, or self-explanatory actuality by itself. A zero-residue reconstruction remains a research target, not a result obtained by replacing the simulator narrative with an unbounded computational closure.

**Audit verdict:** The surviving contribution is a clearer map of the implementation, multiplicity, measure, resource, and global-explanation problems. Ancestor-simulation’s failure to entail self-similarity is a substantive surviving conclusion. Universal copy irrelevance, the proposed physical depth laws, canonical measure, and the claim that unbounded closure is uniquely intelligible are not established—even though some remain asserted in the final response.

### Relation to the other audits

This analysis reinforces the later separation of physical history measure, local records, and centered selection. It also preserves the process–phenomenality audit’s requirement that experience not be inferred from computation by definition. It supplies no missing proof for an experiential ultimate or a neutral-monist self-explanatory whole. These remain competing global proposals with explanatory obligations, not conclusions established by algorithmic invariance.

---

*Source: all 175 lines of `Bostrom's simulation hypothesis.md`, read in the context of its successive qualifications. This is a consolidated reconstruction and mathematical/conceptual audit, not a chronological ledger. Named literature and numerical estimates in the attachment have not been independently verified; no independent literature review is claimed.*
