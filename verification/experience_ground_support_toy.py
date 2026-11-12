#!/usr/bin/env python3
"""Content-sensitive Boolean support toy. Formal completions are not real possibilities."""
import itertools
import json
from pathlib import Path


def supports(predicate, actual):
    """Minimal subsets of the actual literals forcing a true predicate in all completions."""
    n=len(actual)
    if not predicate(actual):raise ValueError('Predicate is not true at this assignment')
    out=[]
    for size in range(n+1):
        for subset in itertools.combinations(range(n),size):
            if any(set(smaller).issubset(subset) for smaller in out):continue
            completions=(v for v in itertools.product((0,1),repeat=n)
                         if all(v[i]==actual[i] for i in subset))
            if all(predicate(v) for v in completions):out.append(subset)
    return out


def show(ss,actual):
    return [[f'{i}={actual[i]}' for i in subset] for subset in ss]


def main():
    conj=lambda v: bool(v[0] and v[1])
    disj=lambda v: bool(v[0] or v[1])
    equal=lambda v: v[0]==v[1]
    taut=lambda v: v[0] or not v[0]
    neg=lambda v: not v[0]
    actual=(1,1)
    a=supports(conj,actual);o=supports(disj,actual);e=supports(equal,actual);t=supports(taut,actual)
    assert a==[(0,1)] and o==[(0,),(1,)] and e==[(0,1)] and t==[()]
    assert supports(disj,(0,1))==[(1,)]
    assert supports(neg,(0,1))==[(0,)]
    try:supports(conj,(0,1))
    except ValueError:pass
    else:raise AssertionError('False predicate must not get a support')
    # Exhaust both-variable states and verify permutation invariance for AND,
    # OR and equality; labels and assignments are transported together.
    for v in itertools.product((0,1),repeat=2):
        for fn in (conj,disj,equal):
            if not fn(v):continue
            s={frozenset(x) for x in supports(fn,v)}
            swapped=(v[1],v[0])
            ss={frozenset(1-i for i in x) for x in supports(fn,swapped)}
            assert s==ss
    # All 16 Boolean functions and four assignments, including asymmetric
    # predicates: transport the function, assignment, and support together.
    checked=0
    for table in itertools.product((0,1),repeat=4):
        f=lambda v: bool(table[2*v[0]+v[1]])
        swapped_f=lambda v: f((v[1],v[0]))
        for v in itertools.product((0,1),repeat=2):
            if not f(v):continue
            checked+=1
            s={frozenset(x) for x in supports(f,v)}
            transported={frozenset(1-i for i in x) for x in supports(swapped_f,(v[1],v[0]))}
            assert s==transported
    assert checked==32
    receipt={'scope':'logical support only, not a physical or experiential ground',
             'true_boolean_function_assignment_cases_checked':checked,
             'actual_assignment':list(actual),
             'minimal_literal_supports':{'and':show(a,actual),'or':show(o,actual),
                 'equality':show(e,actual),'tautology':show(t,actual)},
             'swapped_inputs_equivariant':True,
             'caveat':'Completions are formal valuations; existential, phenomenal and grounding interpretation are not supplied.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print('PASS: content-sensitive support, tie, tautology and permutation controls')

if __name__=='__main__':main()
