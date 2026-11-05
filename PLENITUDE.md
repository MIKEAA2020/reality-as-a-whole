# Plenitude, uniqueness, and the last residue

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

## 5. What is still not proved (honest)

- Plenitude is here stated as a **conjecture** (highly plausible, not
  derived). The strongest argument for it is that its *denial* — that
  there is one particular net/state that is actual while the others are
  not — reintroduces an external selection fact, which is exactly the
  residue the necessary-existence argument forbids. So plenitude is
  *forced by zero-residue intelligibility*; but that is a philosophical
  argument, not a theorem in AQFT.
- The full Standard Model gauge group and fermion content are **not**
  derived here; the structural results above narrow the candidates but do
  not uniquely pin them down. Connes' noncommutative Standard Model and
  the "algebraic SM" programme are the obvious next interface.
- The universal state on \\(\pi_u(\mathcal A)''\\) is not constructed
  explicitly. If it is the maximally-symmetric KMS state (Tomita weight) at
  modular temperature \\(\beta=2\pi\\), it is natural — but this is a
  conjecture.
- Kerr/rotating and full 3+1 aspherical dynamics remain open at the
  physical-model level (the model is currently restricted to spherical
  symmetry for rigorous control).

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
