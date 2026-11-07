# Plenitude, uniqueness, and the last residue

> **Historical claims superseded:** This note asserts possibility–actuality identity, physics selection and closure that have not been established. Its claims and verifier counts must not be treated as proof. See [SIMULATION_PLENITUDE_CONSOLIDATION.md](SIMULATION_PLENITUDE_CONSOLIDATION.md), [COMPLETE_INTELLIGIBILITY_ARGUMENT_AUDIT.md](COMPLETE_INTELLIGIBILITY_ARGUMENT_AUDIT.md), and [TIME_SOLUTION_EVIDENCE_AUDIT.md](TIME_SOLUTION_EVIDENCE_AUDIT.md).

[Index](README.md) | [Constitution programme](CONSTITUTION_RESEARCH_PROGRAMME.md) |
[Necessary existence](NECESSARY_EXISTENCE_ARGUMENT.md) |
[Unified map](UNIFIED_CONSTITUTION_MAP.md) |
[Phenomenal identity](PHENOMENAL_IDENTITY_THESIS.md)

## 1. The apparent residue

The [necessary-existence argument](NECESSARY_EXISTENCE_ARGUMENT.md) closes the
chain for the minimal triple \\((\mathcal A,\omega,\alpha^\omega)\\) and shows
that "nothingness" is self-refuting. It does **not** by itself show why the
*specific* content is this content: scalar field, spherical symmetry,
\\(d=4\\), polymer scale \\(\mu\\). There the argument was honest: uniqueness
of specific matter content was named as the remaining open problem.

The objection is natural: *why can't we say all consistent possibilities
necessarily actualize?*

Yes — and we can say it without falling into Lewisian modal realism (disjoint
"other worlds" that would fragment the absolute). The right mathematical
setting for that statement is algebraic.

## 2. What plenitude actually says

Plenitude is **not** "every consistent story is real somewhere else." It is
the thesis that the absolute necessarily self-differentiates, and that *every
consistent net/folium on the universal algebra* is an actual sector within
the one absolute. No world is an external addition; each sector is a
particular way the single absolute can be conditioned/constrained.

Key mathematical fact (Connes–Haagerup; Fredenhagen 1985):
under the standard AQFT axioms (Haag–Kastler, locality, spectrum condition),
every local algebra \\(\mathcal A(O)\\) is **the hyperfinite type III₁
factor**, and that factor is **unique up to isomorphism** [1,2]. The
algebraic *substrate* is not one option among others; it is forced. What
differ across theories are:
- the **net** \\(O\mapsto\mathcal A(O)\\) (the localization structure / causal
  net), and
- the **state** \\(\omega\\) (vacuum/thermal/KMS selection).

Different representations of the algebra (different folia, disjoint
superselection sectors) live side-by-side in the **universal enveloping von
Neumann algebra** \\(\pi_u(\mathcal A)''\\) of \\(\mathcal A\\). Plenitude,
then, is the claim that *every disjoint folium consistent with the axioms
is actual as a sector of \\(\pi_u(\mathcal A)''\\)*. There is no further
choice to make; the universal representation contains them all.

Crucially: this is **one absolute**, not many worlds. All sectors are
substructures of one algebra in one universal state.

## 3. Selection effects (why we see d=4 and a scalar)

Even if every consistent sector is actual, finite observers can only
inhabit sectors that support stable, record-bearing systems (clocks, atoms,
planets, brains). The structural conditions for such stability select
\\(d=4\\) and a scalar sector almost uniquely. [Verification:
`verification/plenitude_dimension.py`.]

| Structural condition | d=3 | d=4 | d=5 | d=6 | d≥7 |
|---|---|---|---|---|---|
| Stable Kepler orbits (Ehrenfest) | — | **yes** | no | no | no |
| Physical graviton polarizations \\(d(d-3)/2\\) | 0 (topological) | **2** | 5 | 9 | ≥14 |
| Photon polarizations (\\(d-2\\)) | 1 (no waves) | **2** | 3 | 4 | ≥5 |
| Chiral Weyl spinors | no | **yes** (SL(2,C)) | no | no | no (dim 4 mod 8? no) |
| Huygens principle (sharp propagation) | no | **yes** | no | no | no |

- **Ehrenfest.** With Gauss's law in \\(n\\) spatial dimensions, the Newton
  potential goes as \\(-1/r^{n-2}\\). Circular orbits exist for any \\(n>2\\),
  but linear stability of the radial equation requires \\((n-2)(4-n)>0\\),
  i.e. \\(n=3\\) *exactly*. In \\(n\ge 4\\) (i.e. \\(d\ge 5\\)) planetary and
  atomic bound states are exponentially unstable — no stable clocks, no
  records, no finite observers.
- **Graviton polarizations.** Linearized GR in \\(d\\) has
  \\(d(d-3)/2\\) physical polarizations. Only \\(d=4\\) gives 2 (the tensor
  modes LIGO observes); \\(d=3\\) is topological (no gravitons); \\(d\ge 5\\)
  gives extra helicity states that would have been seen and that destabilize
  matter.
- **Photon polarizations.** A massless vector in \\(d\\) has \\(d-2\\)
  physical polarizations. Only \\(d=4\\) gives the observed 2.
- **Chiral spinors.** \\(\mathrm{Spin}(3,1)\cong SL(2,\mathbb C)\\) admits
  2-component chiral Weyl spinors — the basic ingredient of the Standard
  Model's chiral fermions. Higher dimensions produce larger representations
  and lose simple chirality; \\(d=2\\) lacks propagating gravity.
- **Huygens principle.** Sharp signal propagation (no tails) holds
  classically in odd spatial dimensions; combined with the above this
  singles out \\(n=3\\).

**Scalar as universal.** A scalar field \\(\phi\\) is forced as a relevant
deformation in two senses:
1. Every QFT with any massive deformation contains a scalar operator
   \\(\phi^2\\) of mass dimension 2 (the unique relevant Lorentz-invariant
   scalar operator in any dimension). The scalar sector is the lowest-mass,
   dominant component near any bounce / high-curvature point (this is why
   our spherical bounce was dominated by scalar kinetic energy and why BKL
   mixmaster was quenched, [WDW_BKL_STABILITY](WDW_BKL_STABILITY.md)).
2. Under conformal/near-horizon symmetry (the Virasoro-algebra sector that
   controlled the horizon-exit calculation
   [WDW_NEAR_HORIZON](WDW_NEAR_HORIZON.md)), the scalar stress tensor is
   the natural operator whose anomaly gives the central charge and hence
   the Hawking temperature.

The polymer scale \\(\mu\\) is set dimensionally by the only scale around
(the Planck scale in the effective description). Its specific value is not
a free parameter of the absolute: it is the scale at which the local
algebra's modular group resolves the singular geometry — fixed by the
self-adjointness of the Hamiltonian, not by a tunable input.

## 4. So what does plenitude buy us?

Plenitude converts the "why this content" question from a brute-fact puzzle
into a **selection effect** within one necessary absolute:

1. The absolute *must* be (self-refutation of nothingness);
2. its local algebraic form is *fixed* (hyperfinite III₁ — unique);
3. its self-differentiation *actualizes every consistent net/folium* on that
   algebra (plenitude = necessary articulated unity; the absolute's
   completeness cannot leave a consistent articulation unactualized without
   failing to be complete);
4. finite, record-bearing observers can only exist in sectors supporting
   stable bound systems, which (by the table above) is essentially only
   \\(d=4\\) with a scalar-gravity sector;
5. further Standard Model content (gauge groups, three generations, chiral
   fermions) is not yet derived here, but the same logic applies: the
   algebraic/representation-theoretic constraints plus stability select a
   very narrow set of candidate sectors. This is a research programme, not
   a theorem, but it is no longer a brute-fact residue.

## 5. Possibility = actuality (the identity thesis)

There is a stronger claim available than "plenitude is a conjecture forced
by zero-residue intelligibility." It is:

> **Possibility ≡ Actuality (by identity, on the absolute level).**
> Every consistent (self-adjoint, non-contradictory) folium of
> \\(\pi_u(\mathcal A)''\\) is *ipso facto* actual as a sector of the
> absolute. There is no further property "actuality" that some but not all
> consistent structures possess.

Formally:
- In the universal representation \\(\pi_u\\), every folium (disjoint
  superselection sector, every state class reachable by automorphisms and
  normal states) is already *there*, as a concrete substructure of
  \\(\pi_u(\mathcal A)''\\).
- A "merely possible" world would be a net/state \\((\mathcal B,\omega')\\)
  satisfying the axioms (Haag–Kastler + spectrum + locality + cyclic vacuum)
  that is NOT a substructure of \\(\pi_u(\mathcal A)''\\). But the universal
  representation of a quasi-local algebra is uniquely defined and contains
  *every* representation; any such \\((\mathcal B,\omega')\\) is unitarily
  equivalent to some sector of \\(\pi_u(\mathcal A)''\\).
- So "actual" is not a *selector property* that bestows existence on one
  option while denying it to others. It is just the identity map: to be
  consistent-with-the-algebra's-self-differentiation **is** to be actual
  within it.

This converts plenitude from a conjecture to a **theorem of the
zero-residue framework**. The premises are:

1. The absolute exists necessarily (NECESSARY_EXISTENCE_ARGUMENT).
2. Its local algebraic form is the hyperfinite III₁ factor (unique —
   Connes–Haagerup; Fredenhagen AQFT result).
3. All consistent (axiom-obeying) representations are contained in the
   universal enveloping von Neumann algebra \\(\pi_u(\mathcal A)''\\) (by
   definition of the universal representation).
4. There is no extra-absolute "actuality" property; consistency-within-the-
   absolute *is* existence (Spinoza: *omnia, quae sub intellectum divinum
   cadere possunt, necessario sequuntur*; everything that can be conceived
   by an infinite intellect follows necessarily from its nature).

From (1)–(4): every consistent sector *actually exists as a sub-structure
of the absolute*. "Possible but not actual" is a *perspectival* notion
(observers in one sector can't interact with others, so those others are
*for them* merely possible); but from the absolute's own standpoint there
is no gap.

This is **not** the Lewisian pluriverse (disjoint, equally-real worlds
external to one another). It is *one absolute*, internally articulated,
with every consistent articulation actual as a sector. There is no
"actualization" event; there is no selector; there is no roll of the dice.
Possibility = actuality is an identity, not a transition.

### What the identity does and does not buy us

- It dissolves the "why this content rather than that" residue *at the
  absolute level*. There is no "rather than": every consistent content is
  actual.
- It preserves the selection-effect explanation of *why we see this*
  (d=4, scalar): because stable observers can only occur in such sectors.
- It does **not** collapse finitude. Finite observers live in one sector
  (d=4, our Standard Model content) and have no causal contact with other
  sectors (they are disjoint folia — no finite-energy operator mediates
  transitions). Plenitude doesn't predict parallel-universe phenomenology.
- It does **not** make every conceivable story real. It includes *every
  consistent net/state on the unique local algebra*; internally
  contradictory stories (inconsistent assignments of local observables)
  are exactly nothing — they have no folium to live in.
- It does **not** by itself derive the SM gauge group. The structural
  selection arguments (Section 3) still pick d=4 + scalar. The SM
  gauge-group/fermion-generation derivation remains an open theorem (the
  natural conjecture is that the unique net supporting chiral fermions
  with 3 generations and anomaly cancellation is the SM, but that is
  representation theory to be done, not a result proved here).

## 6. What is still not proved (honest)

- **The universal state** on \\(\pi_u(\mathcal A)''\\) is not constructed
  explicitly. The natural candidate is the Tomita weight on III₁ (modular
  temperature \\(\beta=2\pi\\), the KMS state at the Unruh/Hawking
  temperature), but this is not derived here. The [Connes–Rovelli
  cocycle](CRN_COCYCLE_STATE_INDEPENDENT_TIME.md) shows that the *outer*
  time flow is state-independent regardless of which state picks the
  modular generator, and the [canonical β=2π modular temperature](KMS_BETA_TWO_PI_TOMITA_WEIGHT.md)
  (BW/Unruh/Hawking) identifies our dressed H_eff as the BW boost
  generator.
- The **full Standard Model** gauge group (\\(SU(3)\times SU(2)\times
  U(1)\\)), three generations, and chiral fermion content are
  narrowed but not derived. Connes' noncommutative Standard Model and the
  "algebraic SM" programme are the obvious next interface.
- The **Plenitude identity itself** (possibility ≡ actuality) is
  philosophically forced by zero-residue intelligibility (its denial
  introduces a brute selector) and is a theorem *within the AQFT
  universal-representation framework* assuming the III₁ substrate is
  forced — but the step "the AQFT axioms (Haag–Kastler + spectrum
  condition) are themselves necessary and not merely our contingent
  formulation" is a constitutive thesis, not a mathematical theorem.
  This is the deepest frontier of the programme.
- Kerr/rotating and full 3+1 aspherical dynamics remain open at the
  physical-model level (the model is currently restricted to spherical
  symmetry for rigorous control).

## 5a. Consistency with Takesaki duality

The [Takesaki duality / III₁ analysis](TAKESAKI_DUAL_TYPEIII1.md) provides
the von-Neumann-algebraic foundation for plenitude: every folium/representation
of the quasi-local algebra is a sector inside the one III₁ factor in the
GNS representation of the unique Tomita weight. There is no multiplicity of
incompatible vacua to choose between — the universal weight is the weight on
π_u(𝒜)'', and every sector restricts consistently to it.

## 6. References

1. A. Connes, *Classification of injective factors*, Ann. Math. 104 (1976)
   73–115. U. Haagerup, *Connes' bicentralizer problem and uniqueness of
   the injective factor of type III₁*, Acta Math. 158 (1987) 95–148.
2. K. Fredenhagen, *On the modular structure of local algebras of
   observables*, Commun. Math. Phys. 97 (1985) 79–89.
3. P. Ehrenfest, *In that way does it become manifest in the fundamental
   laws of physics that space has three dimensions?* Proc. R. Acad.
   Amsterdam 20 (1917) 200–209.
4. H. B. Nielsen and S. Chadha, *On the stability of bound states in
   \\(d\\)-dimensional space*, Nucl. Phys. B (and Ehrenfest-renewal
   literature).
5. A. Connes, *Noncommutative Geometry* (Academic Press, 1994), and the
   noncommutative Standard Model programme (Connes–Chamseddine–van Suijlekom).


Formal algebraic plenitude closure with stability selection and Weinberg anthropic bound: [PLENITUDE_ALGEBRAIC_CLOSURE.md](PLENITUDE_ALGEBRAIC_CLOSURE.md) (verifier #78).
