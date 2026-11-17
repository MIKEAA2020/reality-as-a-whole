#!/usr/bin/env python3
"""Pitch-derived pair-phase model: symmetry and empirical input diagnostics.

Not a neural model fit or a test for experience. Sampling below verifies encoded
energy identities, while the accompanying report provides the general argument.
"""
from pathlib import Path
from collections import defaultdict
import csv
import hashlib
import itertools
import json
import math
import random
import statistics

ROOT=Path(__file__).resolve().parent.parent
SRC=ROOT/'sources/external/incondata-bowling2018'
FILES={2:('dyads.csv','f617e04b92feeb6a73a64a696163a9554d2cee578b81a40a190dd135708a5855'),
       3:('triads.csv','d9210a546e06b83aae7109552a601304c647f6612ea2fba95b0219dae7462a20'),
       4:('tetrads.csv','4e3826af63c366c69d84947bd68bf1d38598a33ed3f2357230e858092f04f103')}

def check_file(size):
    name,sha=FILES[size]; path=SRC/name
    assert hashlib.sha256(path.read_bytes()).hexdigest()==sha
    with path.open(encoding='utf-8-sig',newline='') as f:
        return list(csv.DictReader(f))

def key(row,n):
    return tuple(int(row[f'pc_{i}']) for i in range(1,n+1))

def frequencies(row,n):
    return [float(row[f'f_{i}']) for i in range(1,n+1)]

def mirror(k):
    return tuple(sorted(k[-1]-x for x in k))

def max_reflection_error_cents(f,g):
    # Correspond original node i to reversed node n-1-i of mirror chord.
    # This is stronger than matching the sorted multiset of distances.
    n=len(f)
    return max(abs(1200*math.log2((f[j]/f[i])/(g[n-1-i]/g[n-1-j])))
               for i,j in itertools.combinations(range(n),2))

def interval_multiset(k):
    return tuple(sorted(b-a for a,b in itertools.combinations(k,2)))

dyads=check_file(2)
assert len(dyads)==12
minor_second=next(float(r['rating_mean']) for r in dyads if key(r,2)==(0,1))
octave=next(float(r['rating_mean']) for r in dyads if key(r,2)==(0,12))
assert abs(octave-minor_second-2.576)<1e-12
results={}
for n in (3,4):
    rows=check_file(n); D={key(r,n):r for r in rows}
    assert len(D)==len(rows)=={3:66,4:220}[n]
    pairs=[]; self_count=0
    for k,row in D.items():
        mk=mirror(k)
        assert mk in D and mirror(mk)==k
        assert interval_multiset(k)==interval_multiset(mk)
        if k==mk:
            self_count+=1
        elif k<mk:
            other=D[mk]
            y1=float(row['rating_mean']); y2=float(other['rating_mean'])
            pairs.append({'first_pitches_relative':k,'second_pitches_relative':mk,
                          'first_rating':y1,'second_rating':y2,'absolute_rating_gap':abs(y1-y2),
                          'first_frequencies_hz':frequencies(row,n),
                          'second_frequencies_hz':frequencies(other,n),
                          'maximum_node_matched_interval_mismatch_cents':max_reflection_error_cents(frequencies(row,n),frequencies(other,n)),
                          'first_published_harmonic_similarity':float(row['bowling_harm_sim']),
                          'second_published_harmonic_similarity':float(other['bowling_harm_sim'])})
    assert len(pairs)*2+self_count==len(rows)
    # This equality is empirical to the finite table, not a general statement
    # that interval multisets always determine sets up to reflection.
    by_intervals=defaultdict(set)
    for k in D: by_intervals[interval_multiset(k)].add(k)
    assert all(v=={k,mirror(k)} for v in by_intervals.values() for k in v)
    y=[float(r['rating_mean']) for r in rows]
    sse=sum(p['absolute_rating_gap']**2/2 for p in pairs)
    sst=sum((v-statistics.mean(y))**2 for v in y)
    near=[p for p in pairs if p['maximum_node_matched_interval_mismatch_cents']<1]
    near.sort(key=lambda p:(-p['absolute_rating_gap'],p['first_pitches_relative']))
    pairs.sort(key=lambda p:(-p['absolute_rating_gap'],p['first_pitches_relative']))
    results[str(n)]={'chords':len(rows), 'distinct_mirror_pairs':len(pairs),
                     'self_mirror_chords':self_count,
                     'mean_absolute_gap_across_mirror_pairs':statistics.mean(p['absolute_rating_gap'] for p in pairs),
                     'in_sample_oracle_mirror_invariant_rmse':math.sqrt(sse/len(rows)),
                     'in_sample_oracle_mirror_invariant_residual_sse_fraction':sse/sst,
                     'pairs_with_node_matched_interval_mismatch_below_1_cent':len(near),
                     'largest_near_matched_gap_example':near[0],
                     'largest_gap_example':pairs[0]}

# Algebraic invariance of the entire objective for any phases: simulate a
# family with arbitrary non-additive odd g and even positive k, plus arbitrary
# graph masks. The proof does not rely on these randomized samples.
rng=random.Random(20261031)
def g(z): return 0.7*z+0.8*math.sin(z)+0.13*math.sin(2*z)
def k(z): return 0.2+0.3*math.cos(z)**2

def energy(x,phi,edges):
    return sum(k(x[i]-x[j])*(1-math.cos(phi[i]-phi[j]-g(x[i]-x[j]))) for i,j in edges)
max_error=0.0
for _ in range(10000):
    n=rng.randint(2,8)
    x=[rng.uniform(-6,6) for _ in range(n)]
    phi=[rng.uniform(-math.pi,math.pi) for _ in range(n)]
    edges=[(i,j) for i,j in itertools.combinations(range(n),2) if rng.random()<0.6]
    c=rng.uniform(-3,3)
    reflected=[c-v for v in x]
    err=abs(energy(x,phi,edges)-energy(reflected,[-v for v in phi],edges))
    max_error=max(max_error,err)
    assert err<1e-11
# Check the stated pointwise perturbation bound; the reported mathematical
# minimum bound follows independently from the uniform pointwise bound.
# |k'| <= .3, 0 <= k <= .5 and |g'| <= .7+.8+.26 = 1.76.
max_bound_excess=-float('inf')
for _ in range(5000):
    n=rng.randint(2,8)
    x=[rng.uniform(-6,6) for _ in range(n)]
    phi=[rng.uniform(-math.pi,math.pi) for _ in range(n)]
    edges=list(itertools.combinations(range(n),2))
    c=rng.uniform(-3,3)
    xp=[c-v+rng.uniform(-.1,.1) for v in x]
    delta=max(abs((xp[i]-xp[j])+(x[i]-x[j])) for i,j in edges)
    bound=len(edges)*delta*(2*.3+.5*1.76)
    excess=abs(energy(x,phi,edges)-energy(xp,[-v for v in phi],edges))-bound
    max_bound_excess=max(max_bound_excess,excess)
    assert excess<1e-11
# An explicitly non-additive odd g produces the standard frustrated triangle.
x=[0,1,2]
ph=[0,math.pi/6,math.pi/3]
nonlinear=lambda d: math.pi/2*math.sin(math.pi*d/2)
edges=list(itertools.combinations(range(3),2))
E=sum(1-math.cos(ph[i]-ph[j]-nonlinear(x[i]-x[j])) for i,j in edges)
assert abs(E-1.5)<1e-12
# An additive assignment is exactly met by choosing phase=alpha*x.
for _ in range(1000):
    x=[rng.uniform(-10,10) for _ in range(5)]; alpha=rng.uniform(-5,5)
    ph=[alpha*t for t in x]
    assert abs(sum(1-math.cos(ph[i]-ph[j]-alpha*(x[i]-x[j])) for i,j in itertools.combinations(range(5),2)))<1e-12

out={'status':'completed', 'scope':'exploratory aggregate data, conditional symmetry math; no neural channels or participant-level inference',
     'inconData_commit':'b95b4db27356a04241ed1a2e38ffc8f5e1f68bbe',
     'source_hashes':{str(s):d[1] for s,d in FILES.items()},
     'random_seed':20261031,'energy_reflection_checks':10000,
     'maximum_numerical_energy_difference':max_error,'additive_zero_cost_checks':1000,
     'near_reflection_uniform_energy_bound_checks':5000,
     'maximum_sampled_bound_excess':max_bound_excess,
     'illustrative_nonadditive_triangle_energy_at_known_minimizer':E,
     'dyad_rating_examples':{'minor_second':minor_second,'octave':octave,
                             'observed_gap':octave-minor_second,
                             'F_single_edge_both':0},
     'observed_mirror_comparisons':results,
     'caveats':'mirror matching in symbolic space is exact; near matching in cents uses reported rounded frequencies and does not imply matched timbre, loudness, spectral partials, individual ratings, neural dynamics or statistical significance'}
path=ROOT/'verification/pitch_frustration_inversion_gate.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
