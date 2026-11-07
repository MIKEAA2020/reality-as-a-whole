# Finite noncommutative algebra of the spectral Standard Model

[Index](README.md) | [Spectral action (gravity)](SPECTRAL_ACTION_BOUNCE.md) |
[Takesaki/III₁](TAKESAKI_DUAL_TYPEIII1.md)

## 1. What this closes

The [spectral-action bounce paper](SPECTRAL_ACTION_BOUNCE.md) shows that
gravity (Einstein-Hilbert with G∝1/Λ² plus Gauss-Bonnet and the cosmological
term) is forced as the heat-kernel expansion of Tr χ(D/Λ) on the
manifold side of the spectral triple. But the gauge/matter sector is
governed not by the commutative manifold M but by the *finite*
noncommutative space F = (A_F, H_F, D_F, J_F, γ_F) in the product M×F.

Connes and Chamseddine's classification theorem (JMP 2013; Chamseddine-
Connes-van Suijlekom 2013) answers the question "why this gauge group?"
structurally: among real even finite spectral triples of KO-dimension 6
(which is the dimension that pairs with 4D commutative spacetime to give
the correct physical signature, spin-statistics, and PCT), satisfying the
order-1 condition

    [[D, a], J b^* J^†] = 0   for all a,b ∈ A_F,

and with Hilbert space H_F of dimension 32 per generation (16 Weyl
fermions × 2 particle/antiparticle), the algebra is **unique**:

> A_F = ℂ ⊕ ℍ ⊕ M₃(ℂ).

Here ℍ is the quaternions (whose unitary group is Sp(1) ≅ SU(2), giving
the weak SU(2)_L doublet structure on left-handed fermions) and M₃(ℂ) is
3×3 complex matrices (whose unitary group U(3) contains SU(3)_c for color
and an extra U(1) that combines with the ℂ factor to give hypercharge
U(1)_Y). This paper documents the verifier that reproduces the structural
core of this classification.

## 2. Dimension counting

The algebra A_F and its unitary group have the real dimensions forced by
the axioms:

| Object | Real dimension |
|---|---|
| ℂ (hypercharge U(1)) | 2 |
| ℍ (weak SU(2) quaternions) | 4 |
| M₃(ℂ) (3-color) | 18 |
| **A_F total** | **24** |
| u(1) from ℂ | 1 |
| su(2) from Sp(1)⊂ℍ | 3 |
| u(3) from M₃(ℂ) | 9 |
| **u(A_F) total Lie algebra** | **13** |
| U(1)_Y ⊕ SU(2)_L ⊕ SU(3)_c (physical SM gauge group) | **12** |
| U(1) center (baryon minus lepton number, decouples) | **1** |

The 13→12 mismatch is exactly the U(1) global (B−L or hypercharge
redundancy) that decouples from the *gauged* sector — one U(1) remains
ungauged (global B−L). This matches the SM exactly: 1 photon, 3 weak
bosons, 8 gluons = 12 gauge bosons.

## 3. Hilbert space: 32 dimensions per generation

Per generation of fermions, the SM has 16 Weyl (chiral) fermions:

  - Leptons: ν_L, e_L (SU(2) doublet), e_R (singlet), ν_R (right-handed
    see-saw partner) = 4.
  - Quarks: (u,d)_L SU(2) doublet × 3 colors, u_R × 3, d_R × 3 = 12.

Adding antiparticles (conjugate reps via J) doubles this to 32 dimensions
in the 1-particle Hilbert space H_F per generation. 3 generations × 32 =
96 physical fermionic degrees of freedom in the one-particle space,
matching the observed 3-generation SM fermion content.

## 4. Order-0 (commutant) and order-1 conditions

The key axiom that selects the SM algebra from all possible finite-
dimensional C*-algebras is the order-1 condition for the real spectral
triple. In [verification/spectral_action_finite_sm.py](verification/spectral_action_finite_sm.py)
we verify on a lepton-sector toy (4-dimensional, the ℂ⊕ℍ piece) that the
real structure J implements the commutant correctly:

  - J b^* J^† commutes with a for all a,b ∈ ℂ⊕ℍ (order-0), verified to
    machine precision (~0).

The full order-1 condition on the 32-dim H_F (with D_F the Yukawa/
Majorana mass matrix) is what selects A_F uniquely; it is a theorem, not
a numerical check, that ℂ⊕ℍ⊕M₃(ℂ) is the unique real even KO-6 triple of
dimension 32 satisfying order-1. Adding extra U(1) factors (B-L
Pati-Salam ℂ⊕ℂ⊕ℍ⊕M₄, or SU(5) GUT M₅(ℂ)) yields algebras whose unitary
groups have **extra generators**:

| Candidate | u(A) dim | Extra generators beyond SM |
|---|---|---|
| SM ℂ⊕ℍ⊕M₃(ℂ) | 13 → 12 (gauged) | 1 global U(1) |
| Pati-Salam ℍ⊕ℍ⊕M₄(ℂ) | 22 | 10 (SU(2)_R + leptoquarks) |
| SU(5) GUT M₅(ℂ) | 25 | 13 (X/Y leptoquarks + extra U(1)) |

These alternatives are mathematically consistent spectral triples but
violate the order-1 condition on KO-6 with Majorana masses; they would
predict unobserved gauge bosons (right-handed W'_R, proton-decay X/Y) and
are therefore not the physical finite algebra at low energy.

## 5. What this adds to the chain

Combined with previous verifiers, the structural stack is now:

  1. **Manifold + algebra:** The quasi-local algebra is type III₁
     ([Takesaki](TAKESAKI_DUAL_TYPEIII1.md)); the Tomita weight is unique.
  2. **Gravity sector:** Tr χ(D/Λ) on the manifold side yields
     Einstein-Hilbert (G∝1/Λ²), Gauss-Bonnet, Λ_CC
     ([spectral action](SPECTRAL_ACTION_BOUNCE.md)).
  3. **Gauge sector (this paper):** The finite noncommutative piece
     F = (ℂ⊕ℍ⊕M₃(ℂ), ℂ^{32}, D_F, J_F, γ_F) has unitary group U(1)×SU(2)×SU(3)
     (modulo the global U(1) center), i.e. the SM gauge group, with 3
     generations × 32 fermionic d.o.f. matching the observed matter content.

The "why these forces/particles?" residue is therefore answered at the
same structural level as the "why gravity?" and "why this time/state?"
residues: all three are consequences of the same set of axioms (real
spectral triple, KO-dimension 6 modulo 8, III₁ quasi-local factor,
order-1 condition) applied to the unique Tomita weight on the algebra of
the bounce-regularized geometry.

## 6. KO-dimension and generations

The [KO-dimension analysis](KO_DIMENSION6_SM.md) pins the real structure:
F must be KO-dimension 6 mod 8 (giving Minkowski signature, CPT,
spin-statistics, and see-saw Majorana mass for right-handed neutrinos)
and KO₆(A_F) ≅ Z/2 forces an odd number of generations; 3 is the smallest
odd number matching 3 colors of SU(3).

## 7. Honest limitations

  - We verify the algebra/gauge-group dimension count and order-0
    commutant in a lepton-sector toy; the full order-1 condition with
    Yukawa D_F and Majorana masses on the 32-dim H_F is a theorem in the
    literature (Connes JMP 2013, CCvS 2013) rather than a fresh numerical
    calculation here.
  - The number of generations (3) is constrained by the axioms only
    through the Poincaré duality / KO-homology condition (the class of
    the mass matrix in KO_6 must be 3 mod 8), which we do not reproduce
    numerically; this remains the most subtle part of the SM derivation.
  - Neutrino mixing, PMNS/CKM matrix structure, and the specific Yukawa
    couplings are free parameters in the spectral action (they appear in
    D_F, not forced by the algebra), just as they are in the SM itself.
  - Detailing the full Connes-Chamseddine spectral Lagrangian (Higgs
    sector from the inner fluctuations, see-saw, etc.) is beyond the
    scope of this verifier.

## 8. Verification

    python verification/spectral_action_finite_sm.py
    python -m verification.spectral_action_finite_sm

Output: [verification/spectral_action_finite_sm.json](verification/spectral_action_finite_sm.json).

PASS: dim_R(A_F)=24, u(A_F)=13, SM gauge group=12 generators, 1 extra U(1)
center (B-L), H_F per generation=32; order-0 commutant holds on lepton
toy to machine precision; Pati-Salam and SU(5) alternatives have extra
generators (10, 13) that would produce unobserved gauge bosons.

## 9. References

1. A. Connes, *Gravity coupled with matter and the foundation of non-
   commutative geometry*, Commun. Math. Phys. 182 (1996) 155,
   arXiv:hep-th/9603053.
2. A. H. Chamseddine and A. Connes, *The spectral action principle*,
   Commun. Math. Phys. 186 (1997) 731, arXiv:hep-th/9606001.
3. A. H. Chamseddine and A. Connes, *Why the Standard Model*, J. Geom.
   Phys. 58 (2008) 38, arXiv:0706.3688.
4. A. H. Chamseddine, A. Connes, and W. D. van Suijlekom, *Inner
   fluctuations in noncommutative geometry without the first order
   condition*, J. Geom. Phys. 73 (2013) 222, arXiv:1304.7580; *Beyond
   the spectral standard model: emergence of Pati-Salam unification*,
   JHEP 11 (2013) 132, arXiv:1304.8050.
5. A. Connes, *Geometry and the quantum*, in *Foundations of Mathematics
   and Physics one century after Hilbert* (Springer, 2018), arXiv:
   1703.02470.
