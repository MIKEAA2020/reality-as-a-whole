# Time from a zero whole: a sphere–record relational clock and a cosmological constraint

## The proposal and the result

The most promising way to reconcile quantum and relativistic time in this programme is **not to make a single cosmic clock fundamental**. Treat the whole as externally timeless, while its internally differentiated structures contain clocks, records and relational changes. A clock's reading is a physical correlation within the whole; proper time is a particular relational quantity recovered when an appropriate spacetime and clock limit exists. Quantum theory supplies amplitudes and conditional probabilities for such correlations; relativity constrains how different physical clocks compare.

This is compatible with the stronger thesis that the whole is a self-sufficient zero whose internal differentiation is necessary, rather than a bare empty nothing. It is not yet a derivation of that thesis. Three distinct claims must not be conflated: (1) no external space or time, (2) vanishing of a reparametrization constraint, and (3) an objectively defined total energy of the whole equal to zero. The construction below establishes a conditional example of (2) with nontrivial change, while giving a concrete way to investigate (1) and (3).

**New joint result.** In the same asymmetric five-ray sphere–record system used in the recent confined-history work, we construct a five-reading stationary quantum history whose internal logical qubit has prescribed relativistic energies. Its full confined-subsystem density matrix and sphere/record probabilities remain fixed while its richer record–current quadrature evolves. The same relational construction also accepts an explicitly specified scalar-clock FLRW constraint sector in which nonzero positive scalar and internal contributions cancel a negative gravitational constraint term. Fifteen numerical and exact-arithmetic tests pass. This brings zero constraints, clock comparison, the sphere probabilities and domain restriction into one reproducible model; it does **not** derive GR, the prescribed clock Hamiltonians, consciousness or objective whole energy.

Test: [verification/zero_sphere_relativistic_relational_time_test.py](verification/zero_sphere_relativistic_relational_time_test.py). Prior state and clock definitions: [five-ray unification](ZERO_SPHERE_CONSERVATION_RECORD_CURRENT_SINGLE_SYSTEM.md) and [confined relational history](ZERO_CONFINED_REALM_RELATIONAL_HISTORY_AND_CLOCK_TEST.md).

## 1. What needs reconciling?

Ordinary nonrelativistic quantum mechanics normally uses an external time parameter in `i d|ψ⟩/dt = H|ψ⟩` (units `ℏ=1`). GR makes geometry dynamical: different worldlines generally accumulate different proper times, and the lapse and slicing are not a fundamental universal present. Canonical quantum gravity adds constraints, so a naive global state satisfying `Ĉ|Ψ⟩=0` appears frozen. The problem has additional facets: defining observables and their algebra, the physical inner product, clock choices and their domains, global existence of clocks, and recovering local relativistic field theory. A single finite history addresses only a restricted part of that problem. See Anderson's [review](https://arxiv.org/abs/1009.2157) and the [existing evidence audit](TIME_SOLUTION_EVIDENCE_AUDIT.md).

The internal-time strategy is to ask a different question: **what is the distribution of a physical event or reading when another physical system reads a specified value?** In an ideal noninteracting model with clock T and system S, a formal constraint of the form `p_T + H_S=0` implies a Schrödinger equation for the system conditioned on T. This is not a universal clock construction: clocks can be quantum, imperfect, interacting, nonmonotonic or only locally valid. Conditional descriptions and Dirac observables must agree when the hypotheses for their equivalence hold, and physical transition probabilities require a justified physical inner product.

Prior work matters: Höhn, Smith and Lock relate Dirac observables, Page–Wootters conditioning and deparametrization under stated conditions, including relativistic frequency sectors ([arXiv:2007.00580](https://arxiv.org/abs/2007.00580)). Clock-neutral switching is prior art ([arXiv:1810.04153](https://arxiv.org/abs/1810.04153)). Smith and Ahmadi analyze conditional quantum clocks and relativistic time dilation on specified backgrounds, including an interference-sensitive proposed correction ([Nature Communications](https://doi.org/10.1038/s41467-020-18264-4)). The construction here is a *particular integration with this project's sphere–record and domain models*, not a discovery of relational time or relativistic time dilation.

## 2. Point, sphere, domains and the physical target

The point is a representation of the whole's absence of external spatial and temporal location; the internal sphere is a representation of differentiated directions, **not** a literal sphere sitting inside the point in ordinary external space. The blow-up `π(r,n)=rn`, with internal direction `n∈S²` retained at `r=0`, gives a mathematical model of that distinction. The special point and the complete sphere express whole and internal directional plenitude; antipodal pairs express one possible opposition structure, while great circles, chords and center-crossings are useful specific internal comparisons. No external radius or external temporal succession is implied. See [internal sphere constitution](ZERO_POINT_INTERNAL_SPHERE_CONSTITUTION.md).

The project's `CP¹`/Hermitian-matrix construction connects directional data with a Lorentz null cone: `det X=t²−x²−y²−z²` and positive rank-one matrices give future null rays. This is a substantive kinematic bridge, but its assumptions matter: a complex spinor/qubit structure and its symmetry are supplied. A cone fixes causal directions, not a metric scale. For example, `g` and `4g` have identical null cones but proper times differing by a factor two. Sphere geometry alone therefore does not determine elapsed proper time, gravitational lapse, a spacetime field equation or a physical energy scale. See [sphere to Lorentz cone](ZERO_POINT_SPHERE_TO_LORENTZ_CONE.md).

**Domains are not automatically mutually visible.** A surface-restricted description can keep the traveler's position at A during a room journey and change it to B on return, while the traveler's actual room position follows the chord. An inhabitant confined to the surface is not the traveler. Similarly, a chess position and its half-move count remain unchanged while the player thinks; the player is not a chess piece. These are restriction facts, not evidence for an interaction that holds the state still, or that a confined inhabitant detects the richer activity. A quantum equality of reduced density matrices realizes a precise analogue, not a proof that a real room or player exists. The total order of chess moves also cannot substitute for spacetime's causal partial order. See [restriction without interaction](ZERO_REALM_RESTRICTION_WITHOUT_INTERACTION.md) and [held position and interface](ZERO_CONFINED_REALMS_HELD_POSITION_AND_INTERFACE.md).

## 3. The exact finite construction

Let `|+⟩` be the existing normalized five-ray joint state in the triple context and `|−⟩=Z_M₁|+⟩`. They are orthogonal and the existing richer observable `K=Z_R₁ J₁` has eigenvalues `+1` and `−1` on them. On their active two-dimensional support, define the complementary quadrature `Y=−i K Z_M₁`. The chosen initial state is `|v⟩=exp(iπ Z_M₁/4)|+⟩`; in the test conventions, `⟨Y⟩=1` initially. The auxiliary complement of the active two-level support is assigned an energy too so the evolution is unitary on the full finite state space.

Choose energies `E₀,E₁`, let `U=exp(−iH)`, and define five system states `|v_k⟩=U^k|v⟩`. The normalized whole history is

```text
|Hist⟩ = (1/√5) Σ_{k=0}^4 |k⟩_C ⊗ |v_k⟩.
D_k = |k+1⟩⊗I − |k⟩⊗U†,      C_path = (1/2) Σ_{k=0}^3 D_k D_k†.
```

Equivalently, for a general block vector `χ=(χ₀,…,χ₄)`,

```text
⟨χ|C_path|χ⟩ = (1/2) Σ_k ||χ_{k+1} − U χ_k||² ≥ 0.
```

Thus `C_path|Hist⟩=0` by construction, with no external clock in the history. Conditioning on the clock label gives `|v_k⟩` and probability `1/5` in this chosen normalized history. This uniform weight is not a universal probability measure or a claim that each reading or subject is actually experienced.

For an operator O on the system the transported observable at reading k is

```text
R_k(O) = Σ_l |l⟩⟨l| ⊗ U^(l−k) O U^(k−l).
```

Its blocks intertwine with every propagation edge, so `[R_k(O),C_path]=0` on the finite kinematical space, and `⟨Hist|R_k(O)|Hist⟩=⟨v_k|O|v_k⟩`. Tests check commutation on the history and on one nonphysical vector; the intertwining identity gives the general proof. This supplies a genuine Dirac-style relational observable for this **one finite positive path constraint**, not the infinite family of local GR constraints or their quantum algebra. `J₁` is the earlier exchange probe; it is not asserted to be the physical current generated by the new clock Hamiltonian.

For the prescribed spectrum the logical quadratures obey

```text
⟨Y⟩_k = cos[(E₁−E₀)k],     ⟨Z_M₁⟩_k = sin[(E₁−E₀)k].
```

At every tested reading the complete density matrix of the confined candidate subsystem `S={H₁,R₁,R₂,H₂}` remains equal to its initial density, and the original triple record table is unchanged:

| Sphere label | record 01 | record 10 |
|---|---:|---:|
| 0 | 3/40 | 1/20 |
| 1 | 1/10 | 3/10 |
| 2 | 13/40 | 3/20 |

These numbers arise from the chosen asymmetric rays and state; pair and triple contexts are alternative arrangements, not simultaneous experiential incidences. The existing construction relates sphere balance to a qubit POVM after an assumed qubit identification. It does not derive the Born rule or identify a real experiencing subject. Full receiver reduced states also agree between pair and triple contexts for the tested readings and prescribed spectra. Equality supports no-signalling for the model's receiver access and tested settings; no communication channel or universal locality theorem is thereby derived.

## 4. Relativistic clock comparison in that same system

Take a positive-frequency relativistic particle model, with `c=ℏ=1`, base mass `M=3`, logical internal energies `h=0,1`, fixed momentum p, and the **assumed** spectrum

```text
E_h(p) = √[p²+(M+h)²],       ΔE(p)=E₁(p)−E₀(p).
```

At `p=0`, `ΔE=1`. At `p=4`, `ΔE=4√2−5 ≈ 0.656854`; the logical phase progresses more slowly per unit of the chosen coordinate-clock reading. These are physically different prescribed momentum sectors, not merely relabelings of one reading. For a small energy gap δ, `ΔE/δ → M/√(p²+M²)=3/5` at p=4, the usual inverse Lorentz factor. For the finite gap 1, the exact value is not exactly `3/5`. This fixed-momentum comparison alone is not the same as evaluating both components on one definite-velocity worldline.

The test makes that distinction explicit: for `v=4/5`, `γ=5/3`, mass 3 and gap `3/4`, choosing equal velocities gives `(p₀,p₁,E₀,E₁)=(4,5,5,25/4)`. Along `x=vt`, the phase-rate difference is `ΔE−vΔp=(3/4)/γ`. Omitting the spatial phase would give the wrong result. This is an on-shell phase identity for idealized momentum components, not a simulated localized clock trajectory or a proof that the sphere generates spacetime.

A second example imposes a static lapse `N` and rest spectrum `E_h=N(M+h)`. Two clocks with `N₁=1` and `N₂=1/√2` have phase-rate ratio `1/√2` relative to the common coordinate label. This reproduces the stipulated static redshift relation; **the background lapse and metric are inputs**. No Einstein equations, source, experiment or self-consistent gravitational backreaction are simulated. Classical relativistic clock-rate effects are experimentally established, e.g. optical-clock comparisons at different speeds and heights ([Chou et al.](https://doi.org/10.1126/science.1192720)); the present toy is not a new empirical test.

If orthogonal momentum alternatives p=0 and p=4 are equally weighted and their momentum is ignored, their logical coherences average. At `t*=π/(1−(4√2−5))≈9.1553`, their equal-weight phasors cancel and the reduced logical visibility is zero, while each momentum-conditioned clock remains pure. An incoherent mixture with the same diagonal momentum weights has the same reduced logical density under this momentum-diagonal evolution: **this dephasing is not itself a demonstrated interference correction**. Distinguishing one would require nonorthogonal wavepackets or an interference-sensitive recombination measurement with matched controls, as in the cited clock literature.

## 5. A second constraint: positive internal clock contributions in FLRW

To connect the sphere clock to a physical gravitational constraint rather than only a propagation constraint, consider a **specified minisuperspace extension** of the prior flat compact-FLRW/free-scalar model. Set `κ=1`, `α=ln a`, rescale the classical constraint by positive `a³`, and add a stipulated internal sector `h`. The resulting model is

```text
C̃ = −p_α²/12 + p_φ²/2 + h = 0.
```

This corresponds to adding a physical energy term `h/a³` before rescaling. Its origin and coupling to the five-ray apparatus are assumptions, not derived matter physics. For the sector `p_α=−6`, the three assigned internal eigenvalues `h=0,1,1/2` require respectively `p_φ²=6,4,5`. In each sector the contributions cancel exactly:

```text
−3 + (3, 2, 5/2) + (0, 1, 1/2) = 0.
```

The scalar contribution is positive throughout, and the internal contribution is nonnegative. This is cancellation of terms in the chosen rescaled constraint, **not** identification of the gravitational term with a unique local negative-energy density or with the objective energy of the whole. Rescaling the constraint changes its off-shell terms while preserving its zero surface when the multiplier is adjusted.

Choose the branch `p_φ>0`; φ is monotonic on the classical branch, and solving gives the reduced generator for increasing φ, `H_φ=−p_φ=−√(p_α²/6−2h)`. For fixed `p_α=−6` its internal energies are `−√6`, `−2` and `−√5`, yielding the active phase gap `√6−2≈0.44949`. The same five-label construction produces `⟨Y⟩_k=cos[(√6−2)k]`, with the same confined density and record table. The classical relational geometry satisfies `dα/dφ=−p_α/(6p_φ)=1/p_φ>0`; its rate differs between the internal-energy sectors. Energies with `h>3` lie outside the real square-root sector for this fixed momentum.

This is a finite spectral/constraint consistency test: the code inserts the reduced energies into the finite path history and checks the algebraic FLRW constraint per sector. It does **not** construct normalizable quantum states of the continuous `(α,φ)` variables, quantize the full cosmological model, derive the internal coupling, show one shared classical geometry for the superposed sectors, or solve the physical inner-product problem. Fixed momenta in the continuum are generalized states; a rigorous packet, positive square-root domain, relational observables and physical measure are required for the next step. The earlier regulated scalar-clock FRW/modular analysis has its own limitations, notably the unregulated Gibbs trace obstruction ([FRW modular clock](FRW_MODULAR_CLOCK.md)).

## 6. Clock choice, foliation and experience

A **relabeling** `s=f(t)` of the same monotonic clock changes numerical rates by the chain rule but not physical clock-to-clock correlations. A **different physical clock** is a different degree of freedom or worldline with its own readings, noise and coupling; clocks at different velocities or gravitational potentials can physically accumulate different proper times. Conversely, changing the quantum reference clock in the same constrained model is an equivalent description only when the physical state, observables, conditional measure and appropriate domains are transformed consistently. Different clocks need not be interchangeable everywhere. The existing [clock-choice test](CLOCK_CHOICE_EQUIVALENCE.md) includes nonideal and information-losing controls; the synchronized-clock comparison in the preceding history is not a proof that every clock is equivalent.

Nothing in the proposal requires a fundamental preferred foliation. The five ordered labels are a local, one-clock toy and are not relativistic simultaneity slices. A viable continuation must define local clock/record observables for overlapping spacetime regions and show consistency under changes of slicing, including the Hamiltonian and spatial-diffeomorphism constraints and their algebra or an appropriate emergent replacement. A chosen internal scalar clock or a gauge fixing is a computational perspective, not automatically an ontological preferred time.

Experience is a distinct domain question. Physical records and correlations can be related to candidate subject structures without assuming that a register is itself felt, that one candidate subject rule is uniquely right, or that the traveler/player is the confined inhabitant. In the prior two rival incidence laws, the same physical records allow different experiential assignments; hence the present clock evolution does not establish experienced passage. A signed experiential total would need actual subject selection, a non-arbitrary incidence measure and an empirically grounded valence law. Equal and opposite formal assignments do not mean pleasure eliminates another subject's suffering. Any genuinely local suffering remains morally and phenomenally real even if a justified global signed sum vanishes. See [four connections](ZERO_FOUR_CONNECTIONS_CONFINEMENT_COHERENCE_EXPERIENCE.md).

The necessitarian proposal that all genuine possibilities are actual, and thus all facts necessary, remains a substantive foundational hypothesis. Fixed conditional weights or a frozen constraint do not by themselves pick actual outcomes, identify genuine possibilities, or establish subjective incidence. If outcomes are necessitated they are not irreducibly open chance in that sense; probabilistic self-location could still describe limited internal information if an actual incidence measure were justified. No literal simulators are needed.

## 7. The decisive continuation

The construction has advanced the target by showing that a constraint-zero history can retain a sphere-derived record structure, richer clock-sensitive correlation, relativistically prescribed clock rates and, separately, an explicit gravitational constraint cancellation. To move from compatibility to the demanded self-sufficient constitution, work should proceed through these concrete gates:

1. **One coupled quantum cosmology:** promote `h` and the scalar/geometry to a single constrained quantum system with normalizable wavepackets, a defined positive-root domain and physical inner product; recover the finite result and quantify clock backreaction and dispersion. Derive the coupling instead of merely assigning `h/a³`.
2. **Local covariance and metric recovery:** construct relational local observables and verify closure/anomaly freedom and slicing-independent comparisons in an inhomogeneous model; recover the Lorentz cone *and* conformal scale, field equations and measured clock rates. If spacetime is emergent, specify the replacement structure and its recovery map.
3. **Whole energy:** define a genuinely global observable or charge with justified boundary/topology and show why it is objective, zero and nontrivial; do not infer it from `Ĉ=0`. Explain how zero's own constitution selects the permitted physical structure without an external choice or unexplained residual constants.
4. **Actual experience and probability:** derive or independently support subject persistence, local incidence, signed valence and their mapping to physical records, then test against competing laws, local interventions and no-signalling. Establish a defensible measure before applying self-location; test whether global signed cancellation follows without erasing local suffering.
5. **Clock alternatives and empirical control:** compare physical clock choices including imperfect clocks, nonorthogonal/recombined motional states and matched mixtures; recover observed relativistic predictions and identify a quantitative deviation that could distinguish the framework from existing relational quantum theory.

The zero-residue demand is not satisfied merely by labeling remaining inputs as acceptable. The new example identifies where an explicit constitution must replace them: the spinor and five-ray identification, the energy and gravitational coupling, the physical Hilbert space and measure, clock and subject selection, and the link to actual experience. Whether the proposed necessity of all genuine possibilities determines all of these is the central research question, not a result of this finite test.

## Reproduction

From the repository root:

```sh
python -m unittest verification.zero_sphere_relativistic_relational_time_test -v
```

This uses the Python standard library and existing project modules. Passing establishes only the encoded finite assertions and numerical tolerances; it is not a certification of full quantum gravity or the metaphysical thesis.
