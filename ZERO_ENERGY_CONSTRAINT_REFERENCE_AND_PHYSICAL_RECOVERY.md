# Zero constraint, physical reference and relational change

## Result

This pass tests the central physical question raised by the [common-constitution analysis](ZERO_FULL_INTELLIGIBILITY_COMMON_CONSTITUTION.md): can a zero in gravity be more than a number made zero by choosing a reference, while still admitting real positive energy and change?

In one specified compact FLRW model, **yes, conditionally**. Varying the lapse makes the complete Hamiltonian constraint vanish. Multiplying that constraint by a nonzero function and compensating the lapse leaves the same constraint surface and on-shell relational dynamics; this is not an arbitrary subtraction of whatever value the system happens to have. In the same model, shifting a constant between scalar potential and cosmological-constant terms leaves the *complete action* unchanged, whereas shifting the potential without compensation changes the gravitational constraint and its predictions.

The zero also does not determine all the structure. Two explicitly calculated model solutions have the same zero constraint but different positive local energy densities and different relational expansion rates. On a small sphere they have different positive Misner–Sharp energies. Thus the physical distinction between **zero as a constraint** and **nonzero internal energy and geometry** is real within the model, not an added force reconciling two separately chosen values.

This is a constructive route, not a proof that the actual universe's total energy is this constraint, that our universe has the model's topology or fields, or that its physical structure is experience. The constraint is the generator of a gauge freedom in this compact canonical description; an objective global energy and its relation to boundary charges must still be established. [Exact tests](verification/zero_constraint_reference_recovery_test.py).

## 1. One explicit physical model

Extend the earlier [zero-constraint model](ZERO_TOTALITY_FLRW_CONSTRAINT_AND_ENERGY.md) by allowing a **constant** scalar potential `V` and a cosmological constant `Λ`. The spacetime is spatially flat and homogeneous, with spatial slices compactified to a three-torus of fiducial coordinate volume 1. Set `c=1`, `κ=8πG>0`; `a>0` is the scale factor and `N` the lapse. This is a classical minisuperspace model, not an asserted description of the entire actual universe.

The lapse-dependent action can be written, with the same canonical conventions as the preceding model,

```text
L = −3a ȧ²/(κN) + a³ φ̇²/(2N) − N a³(V+Λ/κ).
```

Since `V` is constant, the scalar has no φ-dependent potential force. Its canonical variables are

```text
pₐ = −6a ȧ/(κN),       pφ = a³ φ̇/N,
H = N C,
C = −κpₐ²/(12a) + pφ²/(2a³) + a³(V+Λ/κ).
```

Varying N gives `C=0`. The zero is a consequence **within this model** of its reparametrization-invariant action. It is not imposed after measuring an arbitrary total and subtracting that total, nor is it a real force that subsequently makes the parts balance.

The local scalar-field energy density and the effective vacuum contribution in this bookkeeping are

```text
ρ_scalar = pφ²/(2a⁶) + V,
ρ_effective = ρ_scalar + Λ/κ.
```

Write `Hubble=ȧ/(Na)`. On the constraint surface,

```text
Hubble² = κ ρ_effective/3.
```

The symbol Hubble is used here for expansion, not for the canonical Hamiltonian H. These equations concern homogeneous classical fields. Neither `ρ_scalar` nor any other term is assumed to be a measure of felt experience.

## 2. A genuine reference redistribution—and an uncompensated change

A common reference shift of a nongravitating energy is sometimes physically irrelevant. In this gravity model the precise statement is more specific. For constant δ, transform the two **parameters** together:

```text
V → V+δ,                 Λ → Λ−κδ.
```

Their sum `V+Λ/κ` remains the same. The **entire displayed Lagrangian and constraint remain identical**, for all states, not merely on solutions. Their derivatives and the physical evolution are likewise unchanged. The scalar-assigned density increases by δ while the cosmological-assigned density falls by δ; the **combined effective density is unchanged**. Within this model, these are two ways of splitting the same constant term between the scalar and cosmological parts, not a physical process and not an external agent rebalancing the universe.

This equivalence is limited to the declared action and constant shift. It does not prove that matter, vacuum and gravity can be freely redefined in every theory, or that all observables and couplings of a richer theory are unchanged. It also does not mean that the separately named terms have separately measured energies independent of the split.

By contrast, keep Λ fixed and change only `V→V+δ`. Then at the same canonical state

```text
C_new − C_old = a³δ,
ρ_effective,new − ρ_effective,old = δ.
```

An old on-shell state is generally no longer on the new constraint surface, and the corresponding gravitational solutions have different expansion. This is a **different physical model**, not merely a new common zero of energy. Thus the physical common mode cannot be discarded automatically just because it can be eliminated in a difference-only mathematical representation. A self-sufficient account can still derive its value intrinsically; this control says which value the derivation must address.

## 3. The lapse freedom preserves the zero without selecting a state

Let `f(a,pₐ,φ,pφ)` be a smooth, nonzero function on the relevant domain. Replace the constraint by `C'=fC` and use lapse `N'=N/f`. The multiplier terms agree when the lapses are related, and `C'=0` and `C=0` specify the same constraint surface. In a canonical computation at fixed multipliers,

```text
{F, N'fC} = N'{F,f} C + N'f{F,C}.
```

On `C=0` the first term vanishes; with `N'f=N`, the same on-shell rate of F results. This remains true for relational ratios of rates when the denominator is nonzero. The [tests](verification/zero_constraint_reference_recovery_test.py) check `f=a³` on exact rational states and explicitly retain the off-shell extra term.

The significance is **not** that the constraint is meaningless. Its zero restricts the admissible physical states; its on-shell gauge flow and relational observables are part of the theory. The significance is that its numerical normalization and decomposition are not independently absolute in the way an ordinary measured local energy density might be. A proposed identification of C with the user's total energy must explain this behavior and how the relevant observables are recovered.

This is distinct from the compensated `V,Λ` redistribution: the former rescales a constraint and its lapse on shell; the latter leaves the displayed action identical even off shell. Neither operation establishes that an actual felt quality is identical to a physical observable.

## 4. Zero and positive energy in the *same* physical construction

Use rational model units `κ=6`, a unit coordinate-volume torus, and compare two mathematical solutions at the local clock reading where `a=1` and `pφ=1`. Choose the expanding branch `pₐ<0`. For simplicity put `Λ=0`, so `U=V+Λ/κ=V`.

| Model solution | `U` | `pₐ` | Constraint terms: gravity, kinetic, U | Total `C` | `ρ_effective` | `Hubble²` | `da/dφ` |
|---|---:|---:|---|---:|---:|---:|---:|
| A | `0` | `−1` | `−1/2`, `1/2`, `0` | `0` | `1/2` | `1` | `1` |
| B | `3/2` | `−2` | `−2`, `1/2`, `3/2` | `0` | `2` | `4` | `2` |

The scalar is a valid **local** clock here because `pφ=1` and `φ̇=Npφ/a³` is nonzero for a nonzero lapse. Hamilton's equations give

```text
da/dφ = −κ pₐ a²/(6 pφ).
```

The two solutions have a zero constraint and positive effective local density, but their expansions relative to the scalar differ. They are different model solutions/theories under the stated parameter change, not evidence that two different ultimate worlds are genuinely possible. Neither value of U has been derived from full intelligibility; neither is a measurement of our universe. The point is structural: the condition `C=0` is compatible with and does not erase relational physical differences.

The negative term in C is a canonical gravitational contribution in this chosen representation, **not** an independently localized negative gravitational energy density. The zero is an exact classical constraint equation on phase space, not a quantum-operator claim or merely a zero expectation formed by averaging positive and negative states.

## 5. A nonzero quasi-local energy is not a contradiction

On a local round sphere of areal radius R in a spatially flat FLRW region, the geometric Misner–Sharp energy is

```text
E_MS = Hubble² R³/(2G) = (4π/3) R³ ρ_effective.
```

For the two toy solutions above, choose the same `R=1/4` in units where the coordinate period is 1 and `a=1`; this is a local embedded ball smaller than half the torus period. With `κ=8πG=6`, the exact values are

```text
A: E_MS/π = 1/96,      B: E_MS/π = 1/24.
```

Both are positive and different, although `C=0` in both cases. This is not a contradiction: the quasi-local energy of a sphere and the integrated Hamiltonian constraint/gauge generator are **different defined quantities**. It is the gravitational analogue of the previous analysis's distinction between a zero balance and a nonzero relational spread—but now with a specified physical local-energy prescription, not merely an arbitrarily chosen norm.

It also does **not** establish an objective total energy for the whole torus. In compact gravity the lapse and shift constraints contribute to the canonical generator and there is no usual spatial-infinity boundary term; in asymptotically flat gravity, boundary charges such as ADM energy are different quantities and cannot be inferred by importing the compact calculation. Realistic inhomogeneity, horizons, quantum effects, boundary conditions and observational cosmology are outside this calculation.

## 6. Consequence for the user's full-intelligibility argument

The physical steelman gains a sharper form:

> One self-sufficient physical constitution could have a zero whole-level constraint by its own geometric structure, with local positive energy and change as internal relations. No external coercer must create the cancellation, and zero need not mean the absence of local reality.

The remaining identification is equally sharp. To conclude that the **actual universe's total energy must be zero**, a complete theory must show why the relevant global physical energy is represented by an appropriate zero constraint, or supply a different intrinsically zero quantity with a justified physical recovery map. It must account for how the vacuum contribution, boundary conditions and observed local physics follow within the same constitution. The field equations displayed here leave different effective U and different solutions; a further intrinsic principle could select or explain them, but has not yet been derived.

This is not a demand for something *outside* the whole. It is the demand that the whole's own nature explain its particular physical organization, rather than that a chosen formal scalar be relabelled as energy. A necessary principle may be discovered empirically or constitutively; its not being contained in this short model is not evidence that no such principle can exist.

## 7. The experiential half must be the same success, not a second slogan

The user's parallel argument says an independently existing experiential realm cannot remain an unexplained addition if reality is fully intelligible. A successful constitution might indeed make a particular lived occurrence identical with a particular physical–relational occurrence, with no external bridge or force. Nothing in the zero-constraint calculation proves or disproves that identity: `φ`, its clock role, `C`, and `E_MS` do not by themselves identify a subject, an unpleasant quality or actual experience.

Our [explicit candidate access circuit](CONSTITUTIVE_SUBJECT_QUALITY_ACCESS_CIRCUIT.md) demonstrates the complementary issue: a mathematical output can track a proposed physical distinction while its significance as a subject's lived contrast remains an additional hypothesis. A complete account must not merely conjoin the gravity example with that unrelated spin circuit and call it one constitution. It must derive or otherwise justify **one** physical–experiential organization and its qualitative, subject and incidence consequences. Neither experiential acquaintance nor a physical report must be treated as something that floats outside the whole; first-person evidence can constrain the identity internally.

The strong premises “if zero cannot meet complete intelligibility, nothing can” and “if identity cannot meet it, nothing can” remain the guiding research thesis. The present pass strengthens their constructive physical route and makes the recovery obligation definite; it does not prove those dominance premises or establish a zero-residue account.

## Reproduce

```sh
PYTHONPATH=verification:. python -m unittest \
 verification.zero_constraint_reference_recovery_test \
 verification.zero_total_flrw_constraint_test \
 verification.zero_energy_research_test -v
```

The new checks use exact rational arithmetic for the declared canonical equations, split invariance, uncompensated shift, two zero-constraint solutions, normalized quasi-local energies and on-shell lapse rescaling. They do not derive GR, measure the universe, establish a global energy, or demonstrate consciousness. The earlier model's source and reading-scope limitations remain those stated in [its report](ZERO_TOTALITY_FLRW_CONSTRAINT_AND_ENERGY.md); this note is not a new full literature audit.
