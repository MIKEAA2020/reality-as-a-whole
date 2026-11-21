#!/usr/bin/env python3
"""Exact scalar-versus-facet factorization for the existing E-L spin sector."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
from coupled_subject_boundary_gate import stationary


def bits(s):
    return tuple((1-s[a]*s[b])//2 for a,b in ((0,1),(1,2),(2,3)))


def distribution():
    out=defaultdict(F)
    for s,p in stationary(F(1,4),(None,)*4).items():out[bits(s)]+=p
    return dict(out)


def binary(x):return int(any(x))
def graded_code(x):
    l,m,r=x
    return (l+r,m)  # distinct exact D values by prime factorization


def oracle(dist,code,facet):
    bins=defaultdict(lambda:[F(0),F(0)])
    for x,p in dist.items():bins[code(x)][x[facet]]+=p
    return sum((min(v) for v in bins.values()),F(0))


def factor(dist,code,target):
    fibers=defaultdict(set)
    for x in dist:fibers[code(x)].add(target(x))
    return all(len(x)==1 for x in fibers.values())


def main():
    dist=distribution()
    assert len(dist)==8 and sum(dist.values())==1
    for l,m,r in product((0,1),repeat=3):
        expected=(F(1,4) if l else F(3,4))*(F(3,8) if m else F(5,8))*(F(1,4) if r else F(3,4))
        assert dist[l,m,r]==expected
        assert dist[l,m,r]==dist[r,m,l]
        assert binary((l,m,r))==binary((r,m,l))
        assert graded_code((l,m,r))==graded_code((r,m,l))
    results={}
    for name,code in [('binary',binary),('graded',graded_code)]:
        structured=lambda x:(code(x),x[0],x[2])
        scalar_values=len({code(x) for x in dist})
        structured_values=len({structured(x) for x in dist})
        minbits=(structured_values-1).bit_length()
        errors=[oracle(dist,code,i) for i in (0,2)]
        assert not factor(dist,code,lambda x:x[0])
        assert not factor(dist,code,lambda x:x[2])
        assert factor(dist,structured,lambda x:x[0]) and factor(dist,structured,lambda x:x[2])
        assert factor(dist,structured,code)
        assert errors[0]==errors[1]
        results[name]={'scalar_classes':scalar_values,'facet_from_scalar':False,
            'left_and_right_oracle_error':str(errors[0]),
            'structured_classes':structured_values,'minimal_fixed_length_binary_digits':minbits,
            'scalar_and_both_facets_factor_through_structured_code':True}
    assert results['binary']['left_and_right_oracle_error']=='1/4'
    assert results['graded']['left_and_right_oracle_error']=='3/16'
    assert results['binary']['structured_classes']==5
    assert results['graded']['structured_classes']==8
    # Fixed witnesses: identical scalar, different left target; no spin label leaks.
    binary_witness=((0,0,1),(1,0,1))
    graded_witness=((0,0,1),(1,0,0))
    for (a,b),f in ((binary_witness,binary),(graded_witness,graded_code)):
        assert f(a)==f(b) and a[0]!=b[0] and dist[a]>0 and dist[b]>0
    receipt={'model':'existing equilibrium four-spin t=1/4, q-left/middle/right',
             'edge_mismatch_probabilities':{'%d%d%d'%x:str(dist[x]) for x in sorted(dist)},
             'results':results,
             'witnesses':{'binary':binary_witness,'graded':graded_witness},
             'reflection_states_checked':8,
             'scope':'conditional same-field facet-transport hypothesis; idealized physical model, no demonstrated phenomenology or subject identity'}
    text=json.dumps(receipt,indent=2)+'\n';Path(__file__).with_suffix('.json').write_text(text);print(text)
if __name__=='__main__':main()
