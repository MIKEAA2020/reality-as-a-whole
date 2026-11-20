# Entanglement swapping, heralding and perspective selection

## Result in brief

The prize-winning experiments motivate a precise new application to the framework: **a shared experimental record can define a conditional relational state, but neither the existence of that conditional state nor a setting-independent selection rate establishes an independent, unbiased selection rule.** We need the joint distribution of settings, source variables, local outcomes and selection records.

Three bounded checks make this concrete:

1. In an ideal Bell-measurement model with two noisy entangled links, each local herald has probability `1/4`, the conditional outer state has visibility equal to the **product** of the input visibilities, and ignoring the herald leaves the outer pair maximally mixed.
2. For the worked visibility `16/25`, that conditional state is entangled but does not violate CHSH. A separable state gives **exactly the same entire set of probabilities** if one side uses only one measurement basis, while it differs in a complementary basis.
3. A deliberately engineered *late central selector* can choose half the data at every setting and leave balanced selected marginals, yet produce `S=4` in the selected data. This is a classical selection/collider example, not a quantum state, a legitimate independent event-ready herald, or a model of the Nobel experiments.

These are applications of known quantum and selection principles, not new derivations of the Nobel physics. The specific side-by-side finite checks connect those principles to the framework's unfinished measure and subject questions. Neither entanglement nor conditioning establishes experience, subject boundaries or a universal consciousness.

## 1. Sources and scope

- Pan, Bouwmeester, Weinfurter and Zeilinger, [*Experimental Entanglement Swapping: Entangling Photons That Never Interacted*](https://web.physics.ucsb.edu/~quopt/swap.pdf), [DOI](https://doi.org/10.1103/PhysRevLett.80.3891): extracted full main text read in the accompanying [Nobel audit](NOBEL_ENTANGLEMENT_BELL_TELEPORTATION_SOURCE_AUDIT.md); figure images and raw data were not independently audited. The actual experiment reports additional measurements in different bases; the one-basis ambiguity below is **not** a counterexample to its full reported evidence.
- Jin et al., [*Entanglement Swapping with Quantum-Memory-Compatible Photons*](https://arxiv.org/html/1506.03704v1): first of six HTML chunks read, plus search-retrieved selected passages, **not** its full article, figures, raw data or tomography. The authors discuss conditional visibility, tomography and the limits of a Werner-noise assumption. The paper is available; the remaining text was not read for this gate.
- Bartkiewicz et al., [*Entanglement Estimation from Bell Inequality Violation*](https://arxiv.org/html/1306.6504): first of ten HTML chunks read, **not** the full paper or proofs. Its introduction states the standard Werner-state entanglement and CHSH thresholds. The original Horodecki criterion, [*Violating Bell Inequality by Mixed Spin-1/2 States: Necessary and Sufficient Condition*](https://doi.org/10.1016/0375-9601(95)00214-N), was not fully read; its abstract-level descriptions were inspected earlier. Neither source is claimed to be inaccessible.
- For an event-ready experimental example, Rosenfeld et al., [*Event-Ready Bell Test Using Entangled Atoms Simultaneously Closing Detection and Locality Loopholes*](https://doi.org/10.1103/PhysRevLett.119.010402): search-retrieved excerpts only; full text, supplement, and raw data not read. An independent early herald still requires appropriate setting-independence, spacetime and outcome-completeness assumptions.

## 2. Noisy quantum swapping: what is selected?

Let `A,B` and `C,D` be distinct qubits, with independent pair states

```text
ρ(p)AB ⊗ ρ(q)CD,     ρ(p) = p |Φ+><Φ+| + (1−p) I₄/4,
|Φ+> = (|00>+|11>)/√2,        0 ≤ p,q ≤ 1.
```

This is a stipulated independent-input, white-noise model, not a reconstruction of the optical experiment. Perform an **ideal complete** Bell measurement on `B,C` and retain its outcome `h`. The normalized conditional state of `A,D` is

```text
ρAD|h = pq |Bell_h><Bell_h| + (1−pq) I₄/4,
P(h) = 1/4,    ρAD = Σh P(h) ρAD|h = I₄/4.
```

The Bell labels correspond to `Φ+`, `Φ−`, `Ψ+`, `Ψ−`. The identity is a standard consequence of the swapping protocol. The verifier contracts the four-qubit density matrix with the Bell projectors using exact fractions, for all four combinations of endpoint values `p,q ∈ {0,1}` and several interior examples. Because both the input and claimed output are bilinear in `p,q`, the four endpoint checks establish this polynomial identity for this model; they do not establish it for non-white noise, imperfect measurements, dependent sources, loss or arbitrary quantum states.

For `p=q=4/5`, each input link can individually violate ideal CHSH: `2√2·(4/5) ≈ 2.263`. But after ideal swapping the visibility is `16/25`, giving `Smax = 2√2·16/25 ≈ 1.810`. The output remains entangled because `16/25 > 1/3`, but it does **not** violate CHSH, since `16/25 < 1/√2`. These thresholds are known results for this two-qubit white-noise family; lack of CHSH violation does not imply the state has a local model for every Bell scenario or sequence of operations. At `p=q=9/10`, by contrast, the swapped visibility is `81/100` and the ideal optimized CHSH value exceeds 2. For equal-quality inputs, the output is entangled for `p > 1/√3` and CHSH-violating for `p > 2^(−1/4)`, with the boundary points excluded from the respective strict claims.

A herald record tells an observer **which conditional state** to use once the record is accessible. If all outcomes are ignored, no conditional correlations appear in the outer pair's unconditional state. Complete ideal outcome-dependent local corrections could instead align the four branches before discarding the record, but such corrections are physical operations requiring the outcome information; they are not included in `ρAD=I₄/4`. No controlled faster-than-light communication follows.

## 3. Why one matching fringe is not enough

Let `w=16/25`. Compare the conditional `Φ+`-Werner state with the manifestly separable state

```text
σ = w (|00><00| + |11><11|)/2 + (1−w) I₄/4.
```

If Alice measures only `Z`, Bob chooses an arbitrary qubit direction `n`, and outcomes `a,b` are ±1, **both** states give

```text
P(a,b | Z, n) = [1 + ab w n_z]/4.
```

This includes a full sinusoidal scan `n=(sinθ,0,cosθ)`: the same observed fringe visibility, including all joint outcome probabilities and balanced local marginals, has two incompatible state explanations. But if Alice instead measures `X` and Bob measures `X`, the entangled model gives `⟨XX⟩=w` and the separable model gives `⟨XX⟩=0`. A complementary measurement distinguishes this pair of models.

This does not say that every separable alternative is excluded by only those two correlators or that tomography is unnecessary. It says a **fixed single-basis scan alone** is insufficient. In particular, do not substitute this deliberately incomplete scan for Pan and colleagues' additional cross-basis measurements, or identify the toy `w` with their reported visibility. Their actual setup, measurement assumptions, backgrounds and statistics must be assessed on their own terms.

## 4. An equal-rate selector that fabricates Bell correlations

For each `(x,y)∈{0,1}²`, let local stations output independently generated, uniform bits `a,b∈{−1,+1}`, irrespective of settings. Thus the **unselected** correlations are zero and the CHSH score is zero. Now, *after acquiring both settings and outcomes*, a central rule accepts precisely when

```text
h=1  iff  a b = (−1)^(xy).
```

For every setting pair, `P(h=1 | x,y)=1/2`. Within accepted rows, each local marginal remains uniform. Nevertheless,

```text
(E00,E01,E10,E11 | h=1) = (1,1,1,−1),  so S_selected = 4.
```

Within rejected rows the correlations have the opposite sign; summing both selections recovers the original independent local data. The selected source/outcome distribution is demonstrably setting-dependent: `P(a=b | h=1, xy=0)=1`, but `P(a=b | h=1, xy=1)=0`. Thus a constant acceptance rate and balanced observed marginals do **not** establish setting independence of the selected hidden variables.

The selector has access to **both settings and both outcomes**, so its operation is a global postselection procedure. It is not a pair of local detectors operating without communication and is not an event-ready Bell test. It could only be implemented after bringing the relevant records together or by an equivalent globally informed mechanism. It does not threaten well-designed tests in which suitable heralding precedes the choices, or settings are appropriately independent of the heralded source variables, and all heralded outcomes are included. Mere chronological precedence alone does not prove the absence of common causes or establish setting independence; those assumptions and spacetime details need explicit justification.

Compare the earlier [local detector-selection witness](QUANTUM_ERASER_BELL_AND_SELECTION_MEASURE_GATE.md): there a selected `S=4` also arises with equal detection rates, but by local setting-dependent losses. The present selector is a **different causal mechanism**, directly relevant when a purported perspective or record-selection rule can depend jointly on already existing outcomes and settings.

## 5. Consequences for the larger account

A mathematical account of a timeless whole may contain complete records for each setting and herald outcome without an external universal clock. But to reproduce these experiments it must specify, at minimum:

1. **The operational event structure:** the subsystems, source preparation, measurement instruments and which record labels a trial.
2. **Joint weights:** a normalized or otherwise mathematically controlled measure over setting, source, outcome and herald records—not merely a list of actual possibilities.
3. **Selection mechanism:** whether the event-ready record is independent of later settings conditional on the relevant source variables, or instead a retrospective/global selector. In the standard Bell inference, state the appropriate conditional setting-independence and locality assumptions and justify their empirical application.
4. **Complete outcome accounting:** include losses, no-clicks, herald failures and any relevant postselection; show which probabilities are local and unconditionally accessible, and which require comparing records.
5. **Complementary controls:** show that the same candidate fits more than a chosen fringe, and check Bell-test outcomes where relevant without assuming a Werner state unless independently justified.
6. **A separate phenomenal bridge:** articulate and empirically confront what, if anything, makes certain structures subjects and identifies their experience. The above physical distinctions do not answer this.

The proposal that all genuine possibilities are actual **does not entail** a particular distribution over them, nor does a fixed totality automatically imply or refute trial-level setting independence. A perspective-weighting rule that conditions on records from both wings may be mathematically legitimate as retrospective inference, but it cannot be treated as an independent event-ready trial selector without the corresponding causal and statistical justification. That is the precise compatibility gate; it does not decide whether such a rule has experiential significance.

## 6. Reproducibility and limits

Run `python verification/swapping_herald_selection_gate.py`. It writes `verification/swapping_herald_selection_gate.json`, performs exact rational density-matrix contractions for all Bell outcomes, checks the two compared states' correlators, and exhaustively enumerates the finite central-selection example. The verifier uses no external packages. It checks this calculation, not the empirical data, the general Horodecki theorem, the validity of any phenomenal bridge, or the metaphysics of actuality.
