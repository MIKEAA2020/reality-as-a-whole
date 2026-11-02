# Constructive step 19: what causal structure does—and does not—determine

## Result and scope

The [localized scaling construction](../local_scaling/REPORT.md) makes it possible to ask a sharper inverse question: what geometry has actually been recovered, rather than supplied in the definition of the net?

This step establishes a **conditional reconstruction and non-identifiability ledger** in the explicit smooth 1+1-dimensional model class:

- Causal order is unchanged by positive conformal rescaling, including examples with genuinely different curvature.
- A calibrated measure on arbitrarily small causal diamonds determines the conformal factor in a fixed null chart, and therefore the metric within that conformal class.
- Coarse diamond volumes, even for an entire integer grid, can conceal nonzero curvature. Finite-parameter reconstruction works only under its declared parameter restriction.
- The free massive CAR net and vacuum have a precise dilation equivalence across masses. They provide dimensionless mass-relative distances, not an independently selected absolute unit.

This is not a derivation of a smooth spacetime from an unlabelled operator algebra, a finite causal set, or the earlier CNOT causal order. Those source-to-target reconstruction maps remain missing. Thirty-two finite tests accompany the elementary analytic arguments below.

## 1. Separate the inputs before reconstructing anything

| Available structure | What is justified here | What is not justified here |
|---|---|---|
| Abstract CAR algebra over an infinite separable one-particle space | Canonical anticommutation structure | Spatial dimension, metric, local regions, clock |
| CAR algebra plus an abstract pure quasifree projection state | A polarization and its representation | Localization without a supplied local net or symmetry action |
| Net already indexed by Minkowski regions | The localization properties proved in steps 17–18 | Independent recovery of the indexing geometry |
| Future order in our known smooth null-coordinate model class | Conformal causal structure; explicit ambiguities below | Metric scale, volume density, curvature |
| That conformal class plus all calibrated small-diamond volumes | Conformal factor, hence metric in the chosen chart | A derivation of the volume input or its physical units |
| Parametrized translation action and free massive spectrum | A mass-relative ruler and clock | An absolute unit without an external calibration convention |

The first distinction has a direct mathematical reason. Any two infinite-dimensional separable complex Hilbert spaces have a unitary basis correspondence, inducing a CAR isomorphism. A unitary can mix spatial modes nonlocally. Likewise two projections of infinite rank and corank are unitarily equivalent by separately matching their ranges and complements; their pure quasifree state pairs are therefore isomorphic if localization and dynamics are forgotten. This does not imply equivalence of their local dynamical nets. Finite tests show both nonlocal mode permutation and covariance conjugation explicitly.

Also, locality is an implication from spacelike separation to commutation, not an automatic inverse rule reading all causal relations from zero commutators. Conserved observables can commute at timelike separations. We do not identify an unlabelled commutation graph with spacetime order without a causal-faithfulness theorem.

## 2. Explicit order and its metric ambiguity

Put u=t+x and v=t-x. In Minkowski signature (+,-),

\[
ds^2=dt^2-dx^2=du\,dv,\qquad
d\mu_\eta=dt\,dx=\tfrac12du\,dv.
\]

Future causal precedence is the product order

\[
p\preceq q\quad\Longleftrightarrow\quad
u_p\le u_q\ \text{and}\ v_p\le v_q,
\]

Chronological precedence has both inequalities strict. Null-separated points are causally related but not chronologically related. A chronological diamond is the open rectangle (u_p,u_q) × (v_p,v_q).

Every pair of smooth increasing diffeomorphisms f,g gives an order automorphism (u,v) ↦ (f(u),g(v)). For example f(u)=u+αu³ and g(v)=v+βv³ with α,β ≥ 0 are global diffeomorphisms. They preserve all causal comparisons, but are generally not isometries of the fixed coordinate metric η. Their pullback metric is f'(u)g'(v)du dv.

A caveat matters: a metric and its diffeomorphic pullback are isometric descriptions, not automatically physically distinct geometries. To demonstrate a genuine ambiguity beyond coordinate relabelling, consider instead

\[
g_L=L(u,v)du\,dv,\qquad L>0.
\]

Positive rescaling preserves the future cones and the allowed causal curves, hence the same product order on the entire coordinate plane. It need not preserve curvature. For the global positive family

\[
L=A+Bu^2+Cv^2,\qquad A>0,\ B,C\ge0,
\]

write L=exp(2σ). With the curvature convention R=-8exp(-2σ)∂u∂vσ,

\[
R_L(u,v)=\frac{16BCuv}{L(u,v)^3}.
\]

For B,C>0 this is not identically zero, while Minkowski curvature is identically zero. These order-equivalent metrics are not related by an isometry to flat Minkowski space. Causal order alone therefore does not fix curvature, much less a length unit.

These are explicit proofs within a supplied smooth two-dimensional conformal model class. They are not an appeal to a higher-dimensional causal reconstruction theorem, nor a proof that a finite order determines a continuum manifold or dimension.

## 3. What a calibrated volume measure adds

For g_L the invariant volume is

\[
d\mu_L=\tfrac12L(u,v)du\,dv.
\]

For the diamond centered at (u₀,v₀) with null half-widths h_u,h_v, continuity of L gives

\[
L(u_0,v_0)=\lim_{h_u,h_v\to0}
\frac{\mu_L\big((u_0-h_u,u_0+h_u)\times(v_0-h_v,v_0+h_v)\big)}{2h_uh_v}.
\]

Thus **all sufficiently fine calibrated diamond measures determine L** in a fixed null chart. Coordinate changes transform the density as usual, so the geometric conclusion is metric determination up to the coordinate identification, not a preferred chart selected by measure.

For L=A+Bu²+Cv² the averaged expression is exactly

\[
\frac{\mu_L(D_h)}{2h_uh_v}
=A+B(u_0^2+h_u^2/3)+C(v_0^2+h_v^2/3).
\]

Its local-density error is Bh_u²/3+Ch_v²/3. Within this declared three-parameter family, three equal-width diamonds centered at (0,0),(d,0),(0,d) suffice. Denote their averaged densities by M₀,Mᵤ,Mᵥ, with h_u=h_v=h. Then

\[
B=(M_u-M_0)/d^2,\quad C=(M_v-M_0)/d^2,\quad
A=M_0-(B+C)h^2/3.
\]

The tests recover these coefficients and check perturbation stability. If each averaged density has error at most η, the coefficient errors obey |ΔB|,|ΔC| ≤ 2η/d². A fixed raw volume error ε corresponds to η=ε/(2h²), which grows as diamonds shrink. Arbitrarily fine exact-data identification is not a claim of noise-free operational recovery.

For a constant conformal factor L=ℓ²,

\[
\mu_L(I(p,q))=\tfrac12\ell^2\Delta u\Delta v,
\qquad \tau(p,q)^2=2\mu_L(I(p,q))
\]

for timelike-related points. The last identity is exact in this constant flat case; it is not asserted for arbitrary curved diamonds. Absolute calibrated volumes fix ℓ relative to the chart convention, while volume ratios alone leave the common scaling ℓ ↦ λℓ unresolved.

## 4. Coarse volume information can miss curvature

Consider another globally positive metric factor,

\[
L_\epsilon(u,v)=1+\epsilon\sin(2\pi u)\sin(2\pi v),\qquad |\epsilon|<1.
\]

Every diamond whose null endpoints are integers has exactly the same volume as in Minkowski space: the sine terms integrate to zero over integer intervals. All these diamonds also have the same causal order as before. Yet

\[
R_{L_\epsilon}(0,0)=-16\pi^2\epsilon,
\]

which is nonzero when ε≠0. Smaller diamonds can reveal the difference; for example the factor at (1/4,1/4) is 1+ε.

Therefore even an infinite coarse integer grid of exact diamond volumes does not determine the smooth metric. The finite quadratic inverse succeeded because its model family excluded such invisible variations. We must retain that restriction rather than promote a successful fit into unrestricted geometric uniqueness.

## 5. The precise causal-set overlap and its extra assumption

A finite partial order can encode precedence without carrying lengths. If one **adds** a Poisson sampling law with density ρ per calibrated spacetime volume, then for a region of volume V,

\[
\Pr(N=n)=e^{-\rho V}(\rho V)^n/n!,\qquad
\mathbb E N=\rho V.
\]

This is a concrete order/volume/counting overlap, but its sampling law and density are extra inputs. Under constant metric rescaling g ↦ λ²g in two dimensions, V ↦ λ²V and ρ ↦ ρ/λ² leave the intensity measure, hence the Poisson count law, unchanged. Counts identify ρV, not an absolute metric scale without a specified density calibration. Finite counts also fluctuate and do not equal their expectation deterministically.

No Poisson law, preferred density, fundamental discreteness, Lorentz-invariant sprinkling realization, or manifold approximation has been derived from the walk or the earlier circuit poset. Counting lattice cells with a declared spacing a supplies the scale through a; it does not independently justify it. Counting modes or subjects does not supply a spacetime volume either.

## 6. What the massive dynamics and vacuum contribute

A positive mass supplies a natural relative length 1/m in c=ℏ=1 units. With a calibrated time parameter, the free field's translation spectrum has rest gap m; in the parity-even vacuum sector the excitation threshold is 2m. Interpreting the latter as twice a charged one-particle mass uses the free field/sector structure, not just an abstract even algebra.

But the entire family has an exact dilation relation. Let

\[
(L_\lambda f)(x)=\lambda^{-1/2}f(x/\lambda),\qquad \lambda>0.
\]

This is unitary on H. Direct differentiation gives

\[
h_{m/\lambda}L_\lambda=\lambda^{-1}L_\lambda h_m,
\qquad
D^{m/\lambda}_{\lambda t}L_\lambda=L_\lambda D^m_t,
\qquad
C_{m/\lambda}L_\lambda=L_\lambda C_m.
\]

It therefore induces an isomorphism of the free CAR nets, sending a region O to λO and preserving the corresponding vacuum expectations when m is sent to m/λ. In spacetime-smearing language the compatible source is

\[
F_\lambda(t',x')=\lambda^{-3/2}F(t'/\lambda,x'/\lambda),
\qquad Q_{m/\lambda}F_\lambda=L_\lambda Q_mF.
\]

Both the field and even nets obey this family relation. Fixed-mass dynamics with calibrated coordinates is **not** thereby dilation invariant, and the massive theory is not claimed invariant under arbitrary local conformal rescaling. Rather, changing units and transforming the mass, lengths, times and smearings together preserves dimensionless predictions such as mt and mx. A chosen numerical m does not select an absolute unit independently of the interpretation of the clock/energy scale.

This also explains why we cannot claim that a bare state already fixes geometry: forgetting localization and parametrized dynamics discards precisely the structures used to interpret mass and distance. Conversely, an enriched net, state, and translation action may contain substantially more geometric information than causal order alone. Establishing an inverse uniqueness theorem for that enriched package requires its own source domain, equivalence relation, and proof; it is not supplied by having constructed the package from Minkowski data.

## 7. Verification and integration ledger

Run `python -m unittest -v test_model.py` in this folder, or `python research/run_checks.py` from the repository root. The 32 tests cover null-coordinate order, nonlinear order automorphisms, metric/volume ambiguity, local-density and finite-family recovery, hidden curved perturbations, scale-degenerate Poisson laws, dilation of dispersion/projectors/propagators/sources, nonlocal CAR automorphisms, covariance conjugation, and timelike accidental commutation. Curvature formulas and continuum reconstruction are analytic; finite evaluations test their declared examples, not an unrestricted geometric theorem. `enumeration.json` records representative diagnostics.

**Earned:** explicit separation of conformal causal structure, calibrated measure, relative mass scale, and absolute-unit convention; a conditional metric inverse; concrete counterexamples to stronger reconstruction claims; a limited causal-set/field-theoretic overlap with all added inputs stated.

**Not earned:** extraction of continuum causal order and dimension from an unlabelled net or discrete poset; a unique actual spacetime or law; derivation of volume calibration, sampling density, statistics or vacuum selection; causal-set/twistor/Langlands unification; phenomenal constitution or ultimate explanation. Mathematical compatibility and identifiability inside a chosen family remain distinct from physical truth and actual occurrence.

**Next bridge:** formulate a genuinely coordinate-free source structure and a testable reconstruction map—for example from an explicit causal diamond incidence system—while retaining the scale/measure equivalence classes instead of silently selecting a background. Further consequences should be earned by that map, not by relabelling a spacetime-indexed net as an emergent spacetime.

## Continuation: an anonymous-order inverse

[Step 20](../order_reconstruction/REPORT.md) supplies the finite coordinate-free source and reconstruction map: a classified distributive-lattice order reconstructs two-chain incidence, and calibrated interval values support a separate metric-compatibility test. The null-grid interpretation and continuum refinement remain explicit obligations, rather than implicit consequences of rank coordinates.
