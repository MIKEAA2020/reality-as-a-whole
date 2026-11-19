#!/usr/bin/env python3
"""Exact finite cyclic constraint: unordered visitation versus relative records.

Standard stationary history/group averaging ideas are used, not derived as a
new method. See Halliwell, arXiv:gr-qc/0008046v2, and Page and Wootters,
DOI 10.1103/PhysRevD.27.2885. This is NOT Halliwell's detector dynamics.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json

N = 6
basis = {(c,x,d) for c,x,d in product(range(N), range(N), (-1,1))}
def step(s):
    c,x,d = s
    return ((c+1)%N,(x+d)%N,d)
def syst_step(s):
    x,d = s
    return ((x+d)%N,d)
def advance(s, n, fn=step):
    for _ in range(n): s=fn(s)
    return s
assert {step(s) for s in basis} == basis
assert all(advance(s,N)==s for s in basis)

# Normalized history vector has equal amplitudes 1/sqrt(N) on these N basis
# states, all positive and distinct. Their equal squared moduli are rational.
hist = {d:{(c,(d*c)%N,d) for c in range(N)} for d in (-1,1)}
assert all({step(s) for s in support}==support for support in hist.values())
assert hist[-1].isdisjoint(hist[1])

def prob(support,effect): return Fraction(len(support & effect),len(support))
def orbit_effect(c0,x0):
    seed={(c0,x0,d) for d in (-1,1)}
    return {advance(s,j) for s in seed for j in range(N)}

# Equal-position projectors along an orbit commute, so their Boolean OR is
# a well-defined projector in this toy model. Here the OR visits every site.
sys_basis=set(product(range(N),(-1,1)))
ever={a:{s for s in sys_basis if any(advance(s,k,syst_step)[0]==a for k in range(N))} for a in range(N)}
assert all(effect==sys_basis for effect in ever.values())

# Diagonal group-averaged relational effects commute with W, tested as sets.
rel={(c,x):orbit_effect(c,x) for c,x in product(range(N),range(N))}
assert all({step(s) for s in eff}==eff for eff in rel.values())
# Each fixed-clock setting yields a PVM; it is not six independent clocks.
for c in range(N):
    assert set.union(*(rel[c,x] for x in range(N))) == basis
    assert sum(len(rel[c,x]) for x in range(N)) == len(basis)

p={str(d):{f'clock_{c}_site_{x}':str(prob(hist[d],rel[c,x]))
           for c,x in ((1,1),(2,2),(4,2),(5,1))} for d in (-1,1)}
assert [prob(hist[1],rel[c,x]) for c,x in ((1,1),(2,2),(4,2),(5,1))] == [1,1,0,0]
assert [prob(hist[-1],rel[c,x]) for c,x in ((1,1),(2,2),(4,2),(5,1))] == [0,0,1,1]
assert prob(hist[1],rel[1,1] & rel[2,2])==1
assert prob(hist[-1],rel[1,1] & rel[2,2])==0

# Tracing out the other two factors gives uniform clock and position marginals.
for d in (-1,1):
    for k in range(N):
        assert sum(Fraction(1,N) for c,x,_ in hist[d] if c==k)==Fraction(1,N)
        assert sum(Fraction(1,N) for c,x,_ in hist[d] if x==k)==Fraction(1,N)
result={'status':'passed','cycle_length':N,'kinematic_basis_dimension':len(basis),
 'constraint':'W|c,x,d>=|c+1,x+d,d> modulo 6; H=2I-W-W^dagger has kernel Fix(W)',
 'stationary_histories':'|Psi_d> = sum_c |c,dc mod 6,d>/sqrt(6), d=+1 or -1',
 'unordered_single_site_ever_effects_all_identity':True,
 'all_clock_and_position_marginals_uniform':True,
 'group_averaged_relative_effects_commute_with_W':True,
 'relative_event_probabilities':p,
 'positive_history_joint_P_site1_at_1_and_site2_at_2':'1',
 'negative_history_joint_P_site1_at_1_and_site2_at_2':'0',
 'scope':'finite cyclic idealization with stipulated orientation, dial calibration, and subsystem split; ever-visit effects are not detector dynamics; no gravitational implementation, subject selector, or phenomenal time'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
