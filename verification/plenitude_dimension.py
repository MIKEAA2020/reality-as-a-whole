#!/usr/bin/env python3
"""
Plenitude / uniqueness arguments: tests of structural reasons why the
spacetime dimension d = n+1 = 4 and scalar content are special, and how
'plenitude' (all consistent structures actualize within the one absolute)
collapses the apparent residue.

Checks performed:

(1) Ehrenfest stability of bound orbits in n spatial dimensions.
    Newtonian gravity potential V(r) = -k/r^{n-2} (Gauss's law in n dims).
    Effective radial potential with angular momentum L:
        V_eff(r) = -k/r^{n-2} + L^2/(2 r^2)
    Circular orbits exist at dV_eff/dr = 0:
        (n-2)k/r^{n-1} - L^2/r^3 = 0   =>   r^{n-4} = L^2/((n-2)k)
    Stability: d^2 V_eff/dr^2 > 0 at the circular orbit.
        d^2V/dr^2 = -(n-2)(n-1)k/r^{n} + 3L^2/r^4
    At circular orbit, L^2 = (n-2)k r^{4-n}, substitute:
        d^2V/dr^2 = -(n-2)(n-1)k/r^{n} + 3(n-2)k/r^{n}
                  = (n-2)k(3-(n-1))/r^n = (n-2)k(4-n)/r^n
    Stable iff (n-2)(4-n) > 0, i.e. n = 3 exactly.
    (n=2 uses logarithmic potential; not examined here.)

(2) Gravitational degrees of freedom (linearized GR) in d = n+1 dims.
    Symmetric tensor h_{μν} has d(d+1)/2 components, gauge choices remove 2d,
    leaving d(d-3)/2 physical polarizations. For d=4 that's 2 (tensor modes
    consistent with observation); for d=3 that's 0 (GR topological); for
    d=5 that's 5 (extra polarizations not observed, plus unstable orbits).

(3) Massless particle helicity states in d dims: little group is SO(n-1),
    number of transverse polarizations of massless spin-1 (photon) is n-2;
    only in d=4 (n=3) is this 2, matching our photons. Higher d gives
    extra photon polarizations (which have not been observed and which
    violate observational constraints).

(4) The hyperfinite type III_1 factor is UNIQUE (Connes-Haagerup theorem).
    All AQFT local algebras are hyperfinite III_1 under standard axioms
    (Fredenhagen 1985).  So the *local algebraic substrate* is uniquely
    fixed; matter content is the net structure/state on that unique algebra.

(5) Scalar fields as lowest-dimension (relevant) operators: in any
    dimension, the only Lorentz-invariant operator of mass dimension 0 is
    the identity, and at dimension 2 a scalar φ^2 is relevant (it
    corresponds to mass).  A scalar is therefore universally present in
    any QFT that has any massive deformation at all.

(6) Spinor representations: in d=4, Spin(3,1) ≅ SL(2,C) admits complex
    Weyl spinors (2-component), which are chiral. For d > 4, spinor
    representations are larger; Weyl spinors exist in dimensions
    congruent to 2 mod 8, but chirality plus bound stability singles
    out d=4.

These are *structural constraints*, not full proofs. Within a plenitude
principle (all consistent nets/folia on the universal algebra are
actualized), finite observers necessarily find themselves in a sector
supporting stable records (orbits, atoms, clocks), which singles out d=4
and a scalar sector essentially uniquely.

The script verifies the algebra of items (1)-(3) and records (4)-(6) as
citations.
"""
import json, math, sys

def ehrenfest_stability(n):
    """Return True iff Kepler-like bound orbits are linearly stable
    in n spatial dimensions with 1/r^{n-2} force."""
    # derived above: stable iff (n-2)(4-n) > 0
    return (n-2)*(4-n) > 0

def gr_polarizations(d):
    """Number of physical graviton polarizations in d spacetime dimensions."""
    return d*(d-3)//2

def photon_polarizations(d):
    """Transverse polarizations of a massless spin-1 particle in d dims.
    Standard result: d components minus 1 gauge minus 1 on-shell (k·eps=0
    with k^2=0) = d-2 physical."""
    return d - 2

ehrenfest = {}
for n in range(2, 8):
    d = n + 1
    pol_g = gr_polarizations(d)
    pol_ph = photon_polarizations(d)
    # For n=2, potential is logarithmic, circular orbits are stable but
    # there are no gravitational waves (pol_g=0 in d=3 as n=2,d=3):
    stable_orbits = None if n == 2 else bool(ehrenfest_stability(n))
    ehrenfest[n] = dict(d=d, pol_graviton=pol_g, pol_photon=pol_ph,
                        stable_kepler_orbits=stable_orbits)

# Check the analytic claim that only n=3 (d=4) has BOTH stable orbits AND
# two graviton polarizations.
candidates = {n: v for n,v in ehrenfest.items()
              if v['stable_kepler_orbits'] and v['pol_graviton'] == 2}

result = dict(
    ehrenfest_table=ehrenfest,
    four_d_special=(candidates == {3: ehrenfest[3]}),
    hyperfinite_III1_unique=True,  # Connes-Haagerup, cited
    scalar_relevant_operator_universal=True,  # dim-2 relevant deformation
    spinor_chiral_d4=True,
    notes=[
        "Ehrenfest: 1/r^{n-2} force yields stable Kepler orbits iff n=3.",
        "GR polarizations d(d-3)/2: d=3->0(topological), d=4->2, d>=5->>=5.",
        "Massless photons: d-2 physical polarizations; only d=4 gives 2.",
        "Hyperfinite III_1 factor is unique (Connes-Haagerup); AQFT local "
            "algebras are III_1 (Fredenhagen).",
        "Scalar phi^2 is the unique relevant Lorentz-invariant scalar "
            "operator in any d, so any massive deformation includes a scalar.",
        "Spin(3,1)=SL(2,C) admits chiral 2-component Weyl spinors; "
            "chirality + stable orbits picks d=4.",
    ],
    status="structural constraints verified; not a uniqueness theorem but "
           "a very strong selection effect under plenitude."
)
print(json.dumps(result, indent=2))
assert result['four_d_special']
assert ehrenfest[3]['pol_graviton'] == 2
assert ehrenfest[3]['pol_photon'] == 2   # photons have 2 polarizations in d=4
assert ehrenfest[4]['stable_kepler_orbits'] is False  # d=5 orbits unstable
assert ehrenfest[2]['pol_graviton'] == 0  # d=3 GR is topological
assert ehrenfest[2]['pol_photon'] == 1  # d=3 has 1 "photon" polarization (no EM waves)
print('PASS')
