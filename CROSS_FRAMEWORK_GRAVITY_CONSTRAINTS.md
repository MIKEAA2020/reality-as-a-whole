# Constraining emergent gravity across frameworks

**Answer:** yes. The earlier unifying programme can constrain a candidate much more sharply than a stand-alone toy clock does. The method is to demand *compatible representations and limits of the same physical structure*, then eliminate candidates that violate the combined requirements. This note implements one concrete classical consistency test and specifies the missing quantum/continuum bridge. It does **not** construct a complete theory, derive unique quantum gravity, or solve the general problem of time.

The absolute in the stated programme remains timeless, with no fundamental spacetime or fundamental external clock. A mathematical time parameter, causal order, circuit layer, net index or spacetime chart used below belongs to a **model or emergent regime**; the treatment does not posit that the absolute is in time. Whether spacetime and order emerge from a more primitive substrate is a real question, not settled by writing a poset.

## 1. The relevant earlier work is already in this repository

- [The unified constitution map](UNIFIED_CONSTITUTION_MAP.md) identifies the need for one concrete constitution and distinguishes physical, contextual, causal and experiential presentations. It does **not** exhibit that constitution.
- [One process, four presentations](research/framework_overlap/REPORT.md) explicitly connects a finite quantum channel, local observable algebras, a causal diagram and contextual presheaf information. This is a good starting *interface*, but its three-event diagram is neither quantum gravity nor an emergent manifold.
- [Spacetime net](research/spacetime_net/REPORT.md) and [dynamical locality](research/dynamical_locality/REPORT.md) develop field-theoretic localization and propagation in a specified setting. Their spacetime/localization inputs must not be advertised as outputs.
- [Causal geometry](research/causal_geometry/REPORT.md), [order reconstruction](research/order_reconstruction/REPORT.md) and [refinement completion](research/refinement_completion/REPORT.md) give precise inverse and regularity conditions in restricted examples. Order can leave the conformal scale and curvature undetermined; an appropriate measure and stronger continuum conditions add information but have to be obtained from the candidate.
- [Multiple-clock constraint closure](MULTI_CLOCK_CONSTRAINT_CLOSURE.md) tests a noncommuting constrained model, including a nonconstant structure function and averaging measure. Its structure is deliberately engineered; it is not the local gravitational hypersurface-deformation algebra.
- [The gravitating clock](GRAVITATING_PROPER_TIME_CLOCK.md) treats detector backreaction in minisuperspace, but homogeneity removes local refoliation questions.

The challenge is to make these *one sequence of maps with shared states, operations, observables, scales and approximations*, not just to list five analogies. A causal-event poset, a region-inclusion poset, and a poset of compatible observable contexts have different elements and arrows. They should not be identified because all three are posets.

## 2. A common candidate: typed consistency requirements

These are **proposed selection tests** for a candidate that claims a conventional low-energy GR/QFT regime. They are not asserted to characterize every conceivable theory or to hold as fundamental laws at all scales.

| Source | Requirement on the shared candidate | What it does not supply by itself |
|---|---|---|
| Quantum information / computation | Well-defined state and observable maps, complete instruments including failure/records, and controlled composition. Where a circuit is used, distinguish its assumed gate schedule from physical relational order. Preserve full input/output correlations when comparing different descriptions. | A circuit or CPTP map does not itself select a spacetime, matter content, gravitational constraints or a preferred clock. |
| Causal sets / quantum causal histories | In a sector with an applicable definite causal structure, specify invariant order, local finiteness if assumed, covariant observables, and a quantitative order–volume-to-geometry approximation. If order is quantum-indefinite, state the different formalism rather than forcing a fixed poset. | Order alone does not fix conformal scale, action, state or gravitational dynamics; discrete label invariance is not automatically continuum refoliation invariance. |
| Algebraic QFT / local covariance | In the claimed semiclassical regime, specify local observable nets, isotony and spacelike commutation, state/representation and suitable time-slice and covariance properties. Relative Cauchy evolution can test the response to a background metric perturbation and its relation to stress energy, where the relevant hypotheses hold. | A QFT on a classical background does not quantize the metric or derive Einstein's equations. Microcausality is not itself the hypersurface-deformation algebra. |
| Contextuality / topos | Map each commutative measurement context to the actual observable algebra, with consistent restrictions and probabilities. Do not assume one noncontextual sharp-value assignment across incompatible contexts. | The context category does not by itself give the spacetime causal order, a physical state, a selected outcome or consciousness. Global probabilistic assignments from a quantum state are not forbidden by Kochen–Specker. |
| GR / canonical consistency | In a regime represented by ADM canonical GR, require the classical local hypersurface-deformation brackets and correct matter coupling; at quantum level specify regulator, domains, a meaningful anomaly test and the limit in which the algebra or an equivalent covariant content is recovered. | At finite regulator spacing exact continuum brackets may be unavailable; deformed, discrete or covariant approaches can be viable **if** they demonstrate the appropriate physical continuum limit. |
| Internal clocks / records | Construct conditional event probabilities and operational readouts from the same physical theory; compare the same events, states and instruments across clock descriptions; account for limits, turning points and apparatus. | No single globally monotonic clock, ordinary Hilbert-space factorization, or observable subregion algebra is guaranteed in gravity. |
| Phenomenal constitution | State a testable bridge from the actually realized physical process to episode incidence and qualitative character. | Neither algebraic locality nor clock correlations establish experience or a universal subject. |

**Important existing bridges:** Markopoulou's [quantum causal histories](https://arxiv.org/abs/gr-qc/0703097) already connects finite causal structures, operator algebras and quantum information; this connection is not ours to claim. [Brunetti, Fredenhagen and Verch](https://arxiv.org/abs/math-ph/0112041) develop local covariance and relative Cauchy evolution. [Döring and Frembs](https://arxiv.org/abs/1910.09591) explain the context-presheaf/Kochen–Specker distinction. [Hojman, Kuchař and Teitelboim](https://doi.org/10.1016/0003-4916(76)90112-3) and [Anderson's assessment](https://arxiv.org/abs/gr-qc/0511070) show how demanding a hypersurface-deformation representation constrains canonical geometrodynamics under substantial assumptions. These works are **prior art**, not a proof that the joint programme here is unique or complete.

## 3. Concrete combined test: local matter must fit the same deformation algebra

### 3.1 Why the additional test matters

For canonical GR on a spatial slice with metric `q_ab`, its inverse `q^ab`, lapse functions `N,M`, Hamiltonian constraint `H` and diffeomorphism constraint `D`, the standard classical bracket is

    {H[N],H[M]} = D[v],
    v^a=q^ab (N partial_b M - M partial_b N).

Overall signs depend on conventions; use the convention above. The inverse metric is a **phase-space-dependent structure function**, not a fixed Lie-algebra structure constant. A quantum formulation has domain, ordering, regulator and potential anomaly questions not settled by this classical formula.

Now give two scalar matter fields individually local, finite-propagation dynamics. Let their fixed-background matter Hamiltonian densities be

    h_i = (p_i² + c_i² (partial_x phi_i)²)/2,
    d_i = p_i partial_x phi_i,      i=1,2,
    H_m[N]=sum_i integral dx N h_i,    D_i[v]=integral dx v d_i.

Here `x` is a periodic spatial coordinate, `p_i` is canonically conjugate to `phi_i`, and `c_i>0`. We are **not** claiming that this 1+1-dimensional matter example is a theory of gravitational waves or an Einstein gravitational action. Periodicity removes boundary terms.

The standard Poisson bracket, using the common canonical convention, is

    {H_m[N],H_m[M]}
      = sum_i c_i² D_i[N M' - M N'].

Derivation: `δH_i[N]/δp_i=N p_i`, `δH_i[N]/δphi_i=-c_i² partial_x(N phi_i')`; integrate by parts and antisymmetrize. A local potential depending only on the fields does not add an antisymmetric derivative-of-lapse term. This elementary calculation is an application of known canonical field theory, not a new theorem.

If the candidate demands a *single standard effective metric* and the total momentum generator `D_1+D_2` in this normalization, its matter bracket must instead be

    (D_1 + D_2)[N M' - M N'].

Thus the particular ansatz passes this test only when both coefficients match the same normalized geometry: `c_1²=c_2²=1`. More generally, before normalizing the common light cone, the required shared coefficient is `c_1²=c_2²`. Independent field configurations can make `D_1` nonzero with `D_2=0` or vice versa, so a single common structure coefficient cannot match both if the speeds differ. Additional fields, constraints, nonminimal couplings, a preferred foliation or a modified deformation law define **different candidate theories**; this calculation does not rule them all out.

The two different-speed fields can each have local propagation contained in the *same broader causal cone*. They can therefore satisfy that limited microcausality/no-signalling condition and admit causal-computational descriptions, while failing the specific common-metric bracket. They do **not** furnish a fully Lorentz-covariant two-field AQFT on one metric when their characteristic speeds differ. This is exactly the point: local commutation alone is a weaker input than the combined covariance and deformation test.

### 3.2 Where gravity enters—and where it has not been constructed

The same check can be stated for an ADM matter ansatz in 3+1 dimensions:

    H_i[N] = 1/2 integral d³x N [p_i²/sqrt(q)
                  + sqrt(q) c_i² q^ab partial_a phi_i partial_b phi_i],
    D_i[v] = integral d³x v^a p_i partial_a phi_i.

On the declared canonical phase space, its matter–matter bracket is `sum_i c_i² D_i[v]`, with the `v^a` defined above. For the standard ADM gravity Hamiltonian plus this simple matter ansatz, the antisymmetrized gravity–matter cross terms cancel: the gravity momentum derivative and the matter metric derivative are local and carry the symmetric product `N M`. Consequently the off-shell total bracket has the form

    {H_total[N],H_total[M]} = D_grav[v] + sum_i c_i² D_i[v].

The standard GR target is `D_grav[v]+sum_i D_i[v]`. Unequal speeds leave a mismatch in this ansatz. This is a precise necessary test **under the stated choice of canonical variables, density, couplings, and target algebra**; it is not a proof that an arbitrary modified theory is inconsistent, nor by itself a proof that an operator anomaly survives on the full quantum constraint surface. In particular the constrained surface and the other brackets have not been analyzed for the different-speed ansatz.

This is how requirements from other fields can bite: a candidate may have a circuit, local algebras and a broad causal cone, yet its proposed long-distance matter response must also be compatible with the **same** gravitational deformation structure. Requiring the full appropriate Lorentz/local-covariance content may reject the unequal-speed candidate even before the bracket test. These constraints reinforce rather than magically derive one another.

### 3.3 Explicit numerical witness

On the circle `[0,2pi)` choose

    N=1,  M=sin(2x),  phi_1=phi_2=sin(x),  p_1=p_2=cos(x),
    c_1=1,  c_2=1/2.

For both fields `D_i[N M'-M N']=pi`. Hence the continuum matter bracket is `5pi/4`, while the standard-metric total momentum expression is `2pi`; their difference is `-3pi/4`. This compares off-shell functionals on deliberately specified classical test data, not a constrained gravitational state or an observed event.

[The verifier](verification/cross_framework_local_bracket.py) evaluates the **canonical lattice Poisson bracket of the discrete Hamiltonians**, not a discretization of the expected answer alone. Its exact discrete expressions are

    bracket_n=(5pi/4) sinc(h)^2,
    D_total,n=2pi sinc(h) sinc(2h),     h=2pi/n.

At `n=2048`, the bracket is `3.9269785` and the mismatch is `-2.3561575`, approaching `5pi/4` and `-3pi/4`. An equal-speed control converges to zero mismatch. The nonzero finite-spacing residual in that control reflects the central-difference product-rule defect; it is **not** misidentified as a physical quantum anomaly. See [output](verification/cross_framework_local_bracket.json). The continuum derivation is analytic; the finite calculations check this example and its discretization, not the infinite-dimensional proof or a quantum operator domain.

## 4. How to apply all the insights without assuming the answer

The proposed common construction can be developed in stages:

1. **Common physical object.** Choose a quantum causal-history or other operational candidate with explicit local algebras, complete instruments, a state space and transformations. Its causal relation, if supplied, is an input; do not call it emergent without an inverse map. Spell out how context restrictions are induced by actual algebra maps. General CP pullbacks need not be *-homomorphisms, so they do not automatically map context posets as if they were invertible; this was already exposed in [framework overlap](research/framework_overlap/REPORT.md).
2. **Refinement and geometry.** Give a state-dependent family of coarse-graining maps and identify relational observables from which order, calibrated volume and an effective metric are estimated. Control approximation, fluctuations, non-manifold-like sectors, discreteness errors and identification of the same regions. The existing finite inverse results are conditional ingredients, not this full limit.
3. **Matter and metric response together.** Establish a continuum observable net and a response to geometric perturbations compatible with the candidate's emergent matter propagation. Test relative Cauchy evolution/stress response when appropriate. Matching causal cones is necessary in a chosen single-metric GR limit, but not sufficient: apply the local deformation test to the effective gravitational **and matter** generators, including clocks and their stress energy.
4. **Refoliation test.** Define two local, endpoint-matched deformation paths and compare the same relational effects and recorded joint probabilities. In an ADM limit check all three hypersurface brackets, not just the scalar–scalar one; at finite resolution specify what is exact, approximate or deformed and bound discrepancies on appropriate states. A kinematic quantum circuit ordering is not automatically a physical lapse. A state-by-state numerical zero is not an anomaly-free operator identity.
5. **Dynamical clock and experiments.** Derive clock/readout couplings from the same effective theory, include failures and backreaction, and compare with the known classical GR and QFT limits. Barontini's [cold-atom experiment](COLD_ATOM_ENTROPIC_CLOCK_AUDIT.md) constrains an experimental internal-clock model, not the gravitational constraint algebra. Its laboratory time and entropy measurement must stay in the empirical model.
6. **Explanatory closure.** The preceding stages leave the absolute, actuality and phenomenal constitution open. They constrain any unified account but do not derive its metaphysical commitments. Conversely, the commitments alone do not determine the regulator, matter spectrum or correct dynamics.

This is an intersection of independently motivated constraints, not a belief that any one existing mathematical language must be fundamental. Known approaches also attempt parts of this bridge. For example, [Bonzom and Dittrich](https://doi.org/10.1088/0264-9381/30/20/205013) study discrete deformation algebras in special sectors, and [the simplicial graviton work](https://arxiv.org/abs/2305.01803) reports a classical discrete construction with explicit caveats about quantum and intercell extensions. These results must be compared at the level of hypotheses and observables before claiming a new result.

## 5. The strongest next target

A subsequent [causality and record cutoff test](CROSS_FRAMEWORK_CAUSALITY_RECORD_TEST.md) exposes a spurious operational causal dependence in a finite-mode regulator and checks its continuum suppression. It is a necessary local-QFT control, not a nonlinear gravitational deformation-algebra calculation.

Rather than write down a speculative full theory immediately, select a documented discrete gravity construction with a controlled **inhomogeneous** classical limit and ask: can its local gravitational moves be coupled to the same matter net and complete record instrument while preserving endpoint-matched event probabilities? Then derive a precise bracket defect, its scaling under refinement, and a semiclassical observable test. Compare directly with the cited discrete gravity literature. A successful model would be significant progress; it still would not settle the metaphysical and empirical questions by itself.

**Status:** cross-framework requirements constrain viable local gravitational dynamics; the scalar example shows a concrete way they exclude an ansatz. A physical quantum candidate satisfying all the requirements, and a decisive solution of the problem of time, remain to be established.
