# Zero-energy universe: a deep research review

**Research date:** 31 October 2026. This review distinguishes published results, direct calculations, observational constraints and proposals relevant to the zero-totality programme. It does not reconsider the user's settled case against infinity.

## Executive finding

The zero-energy-universe idea is **substantive, mathematically realizable in important cosmological formulations, and not established as an observational fact about the actual whole**. Its strongest concrete support is not merely a popular analogy: in compact general relativity the Hamiltonian is a sum of constraints, and in certain explicitly specified energy prescriptions and cosmologies the total evaluates to zero. In an FLRW model the gravitational and matter terms of the Hamiltonian constraint cancel exactly while matter and geometry evolve.

But there is a crucial distinction: **the Newtonian mechanical energy of an expanding shell, the ADM Hamiltonian constraint, a quasi-local energy, the energy in matter and the vacuum energy density are different quantities.** They can have different values without contradiction. In particular, a flat FLRW spacetime can have zero gravitational-plus-matter Hamiltonian constraint and simultaneously have **positive Misner–Sharp energy inside a sphere**. Flat spatial geometry is compatible with a compact 3-torus and does not prove global compactness or noncompactness.

For our programme this is encouraging but not a completed foundation. It establishes a promising *structural realization*: a zero constraint can coexist with genuine physical differentiation, positive local matter energy and relational change. It does **not** yet identify that constraint with the user's objective whole-level physical energy, experiential valence, or a self-subsistent constitution. The central research task is to construct and justify those identifications, not replace them with a slogan about a universe popping into existence.

## 1. Historical proposal and what it actually said

Edward Tryon's 1973 paper, *Is the Universe a Vacuum Fluctuation?*, proposed a Big Bang model in which the universe is a quantum-vacuum fluctuation. Its published abstract describes predictions of homogeneity, isotropy, closure and equal matter and antimatter; the latter is not what we observe in our accessible region today. I accessed the **abstract only**, not the paywalled full paper, so the review does not pretend to reconstruct all of Tryon's arguments from the original. [1](https://www.nature.com/articles/246396a0)

The modern popular version says positive matter energy is offset by negative gravitational energy, leaving no net energy to create. This is a useful motivation, but it combines two separate claims:

1. A particular, properly specified **whole energy or Hamiltonian** is zero.
2. A zero value **explains existence**, implies spontaneous creation, or entails no further explanatory conditions.

The first requires a definition and applicable boundary conditions; the second is a further proposal. A quantum-field vacuum is normally a structured physical state, not automatically literal nonexistence. Later tunnelling and no-boundary proposals are distinct from Tryon's fixed-background vacuum fluctuation: see section 8.

The visible universe has a pronounced baryonic matter–antimatter asymmetry. LHCb's 2025 observation of CP violation in baryon decays is relevant to this broader puzzle but does **not** by itself explain the cosmic asymmetry. A zero *electric charge* permits unequal amounts of matter and antimatter, because ordinary matter itself includes both positive and negative charges; equal charge is not equal matter and antimatter. [1](https://sciencemediacentre.es/en/cerns-lhcb-observes-matter-antimatter-asymmetry-baryons-first-time)

## 2. The Newtonian sphere: a real cancellation, but which energy?

Take an ideal homogeneous Newtonian sphere of mass `M`, radius `R`, density `ρ`, expansion velocity `v(r)=Hr`, and use a zero potential at infinity for this isolated-sphere approximation. Direct integration gives

```text
U = -3 G M²/(5 R),                 K = 3 M H² R²/10,
M = 4πρ R³/3,                     ρcrit = 3 H²/(8πG),
Ω = ρ/ρcrit.
```

Hence

```text
U/K = -Ω,                         K+U = K(1-Ω).
```

At `Ω=1`, the **Newtonian expansion kinetic energy cancels Newtonian gravitational binding energy**. This is not the same equation as `Mc²+U=0`. At the additionally chosen radius `R=c/H`,

```text
K/(Mc²) = 3/10,                  U/(Mc²) = -3Ω/10.
```

Thus for `Ω=1`, `K+U=0`, but `Mc²+K+U=Mc²` in this formal bookkeeping. This specifically explains what Valev's 30% calculation establishes and what it does not. [6](https://arxiv.org/html/0909.2726)

**Limits:** Hubble recession speeds near this chosen radius reach c; an isolated Newtonian sphere is not an exact relativistic cosmology; the chosen sphere's boundary and reference matter; treating vacuum energy as ordinary gravitating dust is not justified; and `c/H` is the Hubble radius, **not generally the particle horizon**. The algebra is valuable as an analogy and check, not a measurement of the total energy of the entire universe.

The common Newtonian **shell** argument says for dust `ε=(1/2)H²R²-GM/R=(1/2)H²R²(1-Ω)`; the zero for critical density is again kinetic-plus-potential energy per unit mass, not the rest energy of all space. General relativity supplies the full Friedmann equation and pressure contributions. A cosmology review presents the Newtonian derivation and its domain. [8](https://arxiv.org/html/2509.09954v1)

## 3. General relativity: a concrete zero with local evolution

Take a spatially flat FLRW geometry, compactified to a comoving three-torus of coordinate volume `V₀`. Set `c=1`, `κ=8πG`, lapse `N=1`, and include homogeneous matter energy density `ρ_m` and a cosmological constant `Λ`. The first Friedmann equation is

```text
3 H² = κ ρ_m + Λ,                  H = a_dot/a.
```

In this specific minisuperspace representation the **integrated Hamiltonian constraint** can be written

```text
C = V₀ a³ [ -3H²/κ + ρ_m + Λ/κ ] = 0.
```

The negative geometric expansion term and the matter plus cosmological-constant terms cancel exactly **on solutions**. This includes a positive cosmological constant; it is not necessary to set `Λ=0`. In standard ADM language the full Hamiltonian is schematically

```text
H_ADM[N,N^i] = ∫Σ (N ℋ + N^i ℋ_i) d³x + boundary term,
ℋ = 0,                             ℋ_i = 0.
```

For compact boundaryless `Σ` the usual spatial boundary term is absent, and the canonical generator vanishes on the constraint surface. This is an exact statement for the formulation and its assumptions, and it holds even with nonzero local fields. It does not assume a static universe or a fundamental preferred time. The general formulation and boundary discussion are reviewed in [2](https://arxiv.org/pdf/gr-qc/0703035); the distinction between coordinate evolution and relational descriptions is explored in [2](https://ar5iv.labs.arxiv.org/html/2312.10272).

### Explicit evolving example

Let `V₀=κ=1`, `ρ_m=1/a³` (dust) and `Λ=0.7`. The model has positive matter and positive vacuum density, with

```text
C_m = 1,                C_Λ = 0.7 a³,
C_grav = -(1 + 0.7 a³),  C_total = 0.
```

| Scale factor a | Dust term | Λ term | Gravitational term | Sum |
|---:|---:|---:|---:|---:|
| 0.5 | 1 | 0.0875 | -1.0875 | 0 |
| 1 | 1 | 0.7 | -1.7 | 0 |
| 2 | 1 | 5.6 | -6.6 | 0 |

The negative term changes as positive vacuum contribution grows. This is **not** evidence that a uniquely localizable fluid of negative gravitational energy exists; it is a mathematically explicit cancellation in this chosen Hamiltonian representation. The exact result follows from the constraint and the stated solution, not from fitting the table to observation. The small verification script listed below checks the algebra and compares the quasi-local result.

### Why the zero is meaningful but not the end of the argument

The Hamiltonian constraint is not an empty statement: it is an Einstein equation relating geometry to matter and restricts physically allowed initial data. Our [coupled nonlinear evolution](ZERO_TOTALITY_NONLINEAR_GRAVITY_CLOCK_EVOLUTION.md) shows nontrivial data evolving while the constraints converge numerically.

At the same time, the canonical Hamiltonian generates changes of coordinate description in a generally covariant theory; a relational clock can yield nontrivial physical evolution. Its zero does not, **without an additional argument**, show that a unique observer-independent scalar energy of the whole has been measured, that `Λ` is zero, or that every energy definition must also vanish. Calling it a real structural cancellation is warranted; automatically identifying it with the foundational quantity is not.

## 4. A decisive comparison: positive energy in the same cosmology

In a spherically symmetric region, the Misner–Sharp–Hernandez energy is a geometrically defined quasi-local quantity. For an FLRW sphere of areal radius `R`, with total `ρ` including vacuum energy and `c=1`,

```text
E_MS(R) = R/(2G) [1 - ∇ᵃR ∇ₐR]
        = 4π R³ ρ/3.
```

When `ρ>0` and `R>0`, `E_MS>0`. For flat FLRW this also equals `H²R³/(2G)`. Faraoni derives the FLRW expression and discusses horizons and the areal volume; it applies to a **sphere within** the geometry, not automatically to all of a 3-torus. [3](https://arxiv.org/html/1106.4427)

Thus the constraint zero and positive quasi-local energy coexist in the **same** spacetime, and they answer different questions. There is no need either to dismiss the zero as meaningless or to claim all physical energies vanish. The boundary of a selected region carries information absent from a boundaryless whole; the observer, reference and boundary conditions in other quasi-local prescriptions also matter.

Similarly, ordinary matter energy measured by comoving observers in a chosen volume is not zero merely because the gravitational constraint vanishes. This is precisely the structure needed to distinguish a proposed whole-level zero from literal absence of local physical reality.

## 5. Research literature: real agreements and disagreements

- **Closed FLRW, teleparallel prescription.** Sousa, Moura and Pereira calculate the matter-plus-gravity energy of spatially spherical FLRW using a Hamiltonian prescription in the teleparallel equivalent of GR, obtaining zero for their closed case and comparing with earlier pseudotensor results. This is an actual technical result within a prescription, not a generic empirical proof of the claim. [4](https://arxiv.org/html/gr-qc/0702109)
- **Beyond FLRW and alternative boundary prescription.** Nester, So and Vargas compute an energy for homogeneous Bianchi cosmologies using specified homogeneous boundary conditions. It vanishes for every region of class A models and is nonzero for class B models in their prescription. They discuss how alternative quasi-local energy notions can differ. This is evidence for a substantive zero construction, while showing why a prescription cannot be silently identified with every possible energy. [1](https://arxiv.org/html/0803.0181v2)
- **Asymptotically flat isolated systems are different.** Under the assumptions of the positive-mass theorem, zero ADM mass for complete asymptotically flat initial data satisfying the dominant energy condition implies embedding in Minkowski spacetime. It would therefore be wrong to claim an ordinary nontrivial isolated gravitating system can always have exactly zero ADM mass. This theorem does not apply automatically to a compact cosmology with no asymptotic end. [10](https://arxiv.org/abs/1906.11352)
- **Pseudotensors are not all useless, nor are their local components automatically invariant.** Their component values depend on coordinates; some are connected to Hamiltonian boundary choices. Agreement between calculations is interesting only once geometry, frame, boundary and reference are specified. [1](https://arxiv.org/html/0803.0181v2)

These results do not say that every author agrees on what the physically best total energy is. They make the research question sharper: **which zero is selected by the proposed self-subsistent constitution, and why that one?**

## 6. What cosmological observation says

**Curvature.** In one-parameter extensions of ΛCDM, Tristram and collaborators' Planck PR4 temperature/polarization plus lensing and BAO analysis finds `Ω_K=0.0000 ± 0.0016` (68%); that analysis is consistent with spatial flatness. A separate ACT DR6 plus Planck, lensing and DESI Year-1 BAO analysis reports `Ω_K=0.0019 ± 0.0015` (68%). The numbers are model- and dataset-dependent, not independent repeated measurements of the same data. [4](https://www.aanda.org/articles/aa/pdf/2024/02/aa48015-23.pdf) [2](https://scholarlypublications.universiteitleiden.nl/access/item:4294763/download)

A 2026 extended-model preprint using a different CMB+DESI combination reports `Ω_K=0.0024 ± 0.0011` in one analysis, a roughly two-standard-deviation shift from zero, not a definitive detection. This illustrates why the model and chosen data must accompany a number. [1](https://arxiv.org/html/2607.01226)

This is evidence for **nearly flat spatial geometry within the fitted model**, not a measurement that whole-energy equals exactly zero. Exact zero cannot be established by a finite-error interval. Nor does near-flatness establish global topology: a flat 3-torus is compact, whereas other flat spatial models are not. COMPACT's analysis emphasizes that many possible topologies remain insufficiently explored and that lack of selected matching circles does not rule out every compact topology. [5](https://www.osti.gov/biblio/2341333)

**Cosmic ingredients.** In the Planck 2018 baseline ΛCDM analysis, `Ω_m=0.315±0.007` and `H₀=67.4±0.5 km s⁻¹ Mpc⁻¹` are inferred under that model, with the remainder dominated by the modeled cosmological constant in a nearly flat universe. These percentages describe energy-density parameters in the Friedmann equation, **not** shares of a known signed global total. They do not say that the remaining 70% is negative gravitational energy. [1](https://www.aanda.org/articles/aa/full_html/2020/09/aa33910-18/aa33910-18.html)

**Dark energy is an active empirical question.** DESI DR2 combined with CMB and different supernova data sets reported a preference for a particular evolving-dark-energy parameterization over ΛCDM at `2.8–4.2σ`, depending on the supernova sample. This is not a discovery or a direct test of whole-energy zero; assumptions and systematic errors remain important. An independent analysis questions the robustness of the combined-data inference while also considering evolving dark energy plausible. [3](https://arxiv.org/html/2503.14738v3) [7](https://link.springer.com/article/10.1140/epjc/s10052-025-15076-y)

**Present assessment:** cosmological data constrain the geometry, expansion and source terms an explicit zero-totality model must reproduce. They do not directly observe the total energy of the entire universe, and a generic boundaryless Hamiltonian zero by itself is too universal within its setting to distinguish between most cosmological histories.

## 7. Vacuum energy is not total energy

If dark energy is a cosmological constant, its effective local energy density is positive in the standard fit, and its pressure is negative. A closed-universe Hamiltonian constraint can still vanish, as the example above demonstrates. Therefore

```text
vacuum energy density = 0   ≠   whole Hamiltonian constraint = 0.
```

The local conservation equation also makes the distinction concrete. For a homogeneous fluid with pressure `p` and energy density `ρ`, `ρ_dot+3H(ρ+p)=0`, equivalently `d(ρa³)=-p d(a³)` for a comoving volume (in units `c=1`). For dust, its matter energy in that volume stays constant; for radiation it scales as `1/a`; for a cosmological constant it scales as `a³`. These are local-continuity consequences, not a contradiction of the separate Hamiltonian constraint. [8](https://arxiv.org/html/2509.09954v1)

The cosmological-constant problem concerns why the **effective gravitational vacuum term** is so small compared with contributions expected from known field physics and why its value is stable under corrections. The oft-repeated `120 orders of magnitude` depends on a particular high-energy cutoff and bookkeeping; it should not be presented as a unique, regulator-independent experimental prediction of ordinary quantum field theory. A technical review discusses renormalization, phase transitions, cutoff dependence and the continuing physical puzzle. [9](https://arxiv.org/html/1205.3365v1)

For the programme this is an opportunity: an intrinsic zero principle would need to explain not only a formal constraint but **why the observed effective vacuum term has the value or dynamics it does**, without deleting observed cosmic acceleration. The zero of the total constraint alone does not select `Λ` or solve the fine-tuning problem.

## 8. Quantum creation: possibilities, not automatic consequences

A zero net energy is at most a compatibility condition for a proposed creation mechanism; it does not by itself calculate a transition amplitude, provide a state, specify a clock, or explain why a given history is actual. In ordinary quantum mechanics an energy eigenstate can have nonzero fluctuations of other observables while remaining stationary. The energy–time uncertainty relation does not give a general license for energy to be borrowed and conserved only later; nor does it prove a universe can appear from literal nothing.

The proposals differ:

- **Tryon:** a model involving a quantum-field vacuum, per the original abstract. [1](https://www.nature.com/articles/246396a0)
- **Vilenkin-type tunnelling:** a quantum-cosmological proposal involving a state with no classical geometry and a tunnelling boundary condition, not simply the ordinary laboratory vacuum.
- **Hartle–Hawking no-boundary:** a proposal for a wave function using a sum over geometries without an initial boundary, not simply Tryon's fluctuation.

These proposals involve assumed quantum rules, actions and boundary or contour choices. In a 2025 model calculation, Chou and Nishimura find that different boundary-condition parameters can select different Hartle–Hawking or Vilenkin saddle points. That is a concrete illustration that the zero constraint alone does not select a unique quantum state. It is not a general resolution of quantum gravity. [2](https://arxiv.org/html/2407.17724)

The user's proposal need not be recast as a temporal event in a pre-existing vacuum. It could instead seek a timeless or relational self-constituting whole. Whether that can be made precise and self-subsistent remains a constructive question, not something settled by these quantum-cosmology proposals.

## 9. How this advances the integrated zero-totality framework

There are **three non-interchangeable balances** already present in the programme:

1. **Gravitational constraint:** a local geometry–matter equation with a zero canonical generator on compact slices.
2. **Gauge charge:** in our compact boundaryless Maxwell model, Gauss's law forces the integrated signed gauge charge to zero, even with nonzero local charge.
3. **Experiential history:** the proposed sum or other total over actual positive and negative experiences, with subject incidence, relational duration and an intrinsically shared scale still to be established.

The first two are distinct exact structures under their own assumptions. Neither automatically gives the third. Gauge charge is not energy; negative gravitational contribution is not automatically suffering; a positive local energy density is not automatically positive experience. An analogy of signed accounting preserves room for genuine pain rather than canceling its occurrence, but it does not establish a common experiential measure or demonstrate compensation.

The present gauge–clock simulation [already shows](ZERO_TOTALITY_NONLINEAR_GRAVITY_CLOCK_EVOLUTION.md) nonzero evolving local densities, a numerically neutral gauge total, and evolving geometry. It does not derive the chosen action, topology, constants, actual subjects or a valence bridge. Moreover, the charge density relative to a normal frame depends on the chosen congruence; a genuinely relational experiential law would need an intrinsic physical observer or congruence, or a covariant alternative.

### Best constructive route suggested by the search

1. **Define a candidate whole quantity** from the covariant theory, including its topology, boundaries, gravitational and matter terms, and clock choices; establish whether it is a constraint, a boundary charge, a relational observable or a new invariant. Do not equate them by notation.
2. **Solve the positive-local/zero-whole consistency problem** explicitly across homogeneous and inhomogeneous cosmologies. The minisuperspace and quasi-local comparison above supplies the first benchmark; generalize our existing nonlinear evolution, including a physically justified dark-energy sector and realistic observations.
3. **Derive—not merely postulate—the experiential bridge:** identify actual subjects and their positive/negative felt contributions, a common intrinsic scale, the relevant relational measure, and a law connecting those to the proposed physical organization. Test candidate bridges against pain/relief and independent energy measurements. Whole cancellation must not imply that particular suffering never happened.
4. **Constrain the cosmological model against data:** expansion `H(z)`, CMB perturbations, baryon asymmetry, local gravity and topology signatures. Only a model with consequences beyond the generic constraint can be observationally distinguished.
5. **Address self-subsistence directly:** show whether the same principle determines not only a zero value but the allowed action, quantum state, constants and actual experiential organization. A formal zero with arbitrary laws and boundary conditions is a candidate implementation, not yet the fully self-subsistent result the user seeks.

## 10. Source and verification notes

**Primary or technical sources used:** Tryon 1973, abstract only; Valev 2010 Newtonian estimate; Nester–So–Vargas 2008 Hamiltonian boundary-energy analysis; Sousa–Moura–Pereira 2007/2009 teleparallel FLRW; Faraoni 2011 quasi-local FLRW; Bryden–Khuri–Sormani positive-mass rigidity; Planck 2018 and Tristram et al. 2024; DESI DR2 2025 and a critical reanalysis; COMPACT 2024; Martin's cosmological-constant review; Chou–Nishimura 2025. Links appear beside the claims above. Searches are broad but not exhaustive; not every paper was read in full, and reported empirical numbers are the named analyses, not a claim that no newer analysis exists.

The exact calculations in sections 2–4 can be checked with:

```text
python -m unittest verification.zero_energy_research_test -v
```

The tests verify algebra in the declared examples, not the empirical whole-energy thesis or experiential identity. Related files: [prior FLRW analysis](ZERO_TOTALITY_FLRW_CONSTRAINT_AND_ENERGY.md), [covariant framework](ZERO_TOTALITY_COVARIANT_GAUGE_CLOCK_FRAMEWORK.md), [clock evolution](ZERO_TOTALITY_NONLINEAR_GRAVITY_CLOCK_EVOLUTION.md), [experiential total](RELATIONAL_TIME_AND_EXPERIENTIAL_TOTAL.md).
