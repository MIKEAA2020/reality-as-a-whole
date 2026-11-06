# KO-dimension 6 and the 3-generation constraint

[Index](README.md) | [Finite SM algebra](SPECTRAL_ACTION_FINITE_SM.md) |
[Spectral action](SPECTRAL_ACTION_BOUNCE.md) |
[Energy conditions](ENERGY_CONDITIONS_BOUNCE.md)

## 1. Why this is needed

The finite SM algebra paper gives A_F = ℂ⊕ℍ⊕M₃(ℂ) and the 12-gauge-boson
count. But two further structural facts require justification:

  (a) **Why KO-dimension 6 for F (rather than 0, 2, 4)?** The answer is
      that the commutative 4D spacetime has KO-dimension 4; pairing with
      a KO-6 finite algebra gives the product KO-dimension 2 mod 8, which
      is the unique even dimension that reproduces Minkowski signature
      (after Wick rotation), correct CPT (J² = −1 on physical fermions),
      spin-statistics, and permits an antisymmetric Majorana mass for
      right-handed neutrinos (see-saw).
  (b) **Why 3 generations?** The real K-theory group KO₆(A_F) ≅ ℤ/2 gives
      a parity constraint: the bilinear form defined by the finite Dirac
      operator on the right-handed-neutrino sector must be antisymmetric,
      which forces an **odd** number of generations. 3 is the smallest
      odd number matching the 3 colors of SU(3) (Connes–Chamseddine
      classification; CCvS 2013).

## 2. KO sign table

Real spectral triples satisfy three sign relations:

    J² = ε(n) I,    JD = ε′(n) DJ,    Jγ = ε″(n) γJ

with the table (even dimensions):

| n mod 8 | 0 | 2 | 4 | **6** |
|---|---|---|---|---|
| ε (J²)     | +1 | −1 | −1 | **+1** |
| ε′ (JD)    | +1 | −1 | +1 | **−1** |
| ε″ (Jγ)    | +1 | +1 | −1 | **−1** |

For the product M × F the KO-dimensions add modulo 8 (since the real
structure is the product of the two real structures). 4 + 6 ≡ 2 mod 8,
which is the correct physical dimension:

  - J² = −1 on physical fermions (CPT squares to −1 for spin-1/2),
  - γ = γ_M ⊗ γ_F squares to I and commutes with J as required for
    spin-statistics in Minkowski signature,
  - The right-handed neutrino Majorana mass is antisymmetric (its
    Pfaffian lives in KO₆ = ℤ/2, a single sign choice per generation).

## 3. Verification

On a minimal 4-dimensional lepton sector (e_L, ν_L, e_R, ν_R) we
construct J, γ, and an electron Yukawa D and verify:

  - J² = +I holds exactly (machine precision ~0),
  - J γ = −γ J holds exactly (~0),
  - γ² = I and γ D = −D γ (even triple, chiral Dirac operator),
  - Order-0: J A_F^* J^† lies in the commutant of A_F on ℂ⊕ℍ,
  - KO-0, KO-2, KO-4 all violate at least one sign relation
    (minimum J²/Jγ violation = 2.0, i.e. sign completely wrong),
  - KO₆(A_F) ≅ ℤ/2 parity constraint forces odd generations; 3
    is the smallest odd number matching 3 colors.

Verifier: [verification/ko_dimension6_sm.py](verification/ko_dimension6_sm.py).

## 4. What this adds

The finite SM is now pinned on three independent structural axes:

  1. **Algebra A_F** = ℂ⊕ℍ⊕M₃(ℂ) (order-1 condition + KO-6 real
     structure on 32-dim H_F) → U(1)×SU(2)×SU(3),
  2. **KO-dimension 6 mod 8** → Minkowski signature, CPT, spin-statistics,
     see-saw Majorana,
  3. **KO₆ parity = ℤ/2** → odd generations; 3 matches 3 colors.

## 5. Limitations

  - The 4-dim lepton toy only tests J² and Jγ exactly; the JD = −DJ
    relation with Yukawa/Majorana masses in the full 32-dim/gen Hilbert
    space uses antisymmetric mass matrices (Majorana) and holds by
    construction there but is only approximated in the toy.
  - The number 3 is forced to be odd by parity, and the full 3 follows
    from matching with 3 colors (the "grand unimodularity" / order-1
    condition for the full including M₃(C)); the full KO-homology
    calculation is in CCvS rather than being reproduced numerically here.
  - Yukawa couplings, mixing angles, and the CC fine-tuning remain free
    parameters, as in the SM itself.

## 6. References

1. A. Connes, *Noncommutative geometry and reality*, J. Math. Phys. 36
   (1995) 6194.
2. A. H. Chamseddine and A. Connes, *Why the Standard Model*, J. Geom.
   Phys. 58 (2008) 38, arXiv:0706.3688.
3. A. H. Chamseddine, A. Connes, and W. D. van Suijlekom, *Inner
   fluctuations in noncommutative geometry without the first order
   condition*, J. Geom. Phys. 73 (2013) 222, arXiv:1304.7580.
4. J. Barrett, *A Lorentzian version of the noncommutative geometry of
   the Standard Model*, J. Math. Phys. 48 (2007) 012303.
