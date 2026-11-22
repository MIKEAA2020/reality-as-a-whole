#!/usr/bin/env python3
"""Finite stipulated ownership and report-channel comparison, not neuroscience.

Subjects, experiences, types, conservation and observations are mathematical
stipulations; there is no inference to real consciousness or physical possibility.
"""
import itertools
import json

TOKENS=('a','b','c','d')
TYPES={'a':'red','c':'red','b':'blue','d':'blue'}
CASES=('selected_fusion','private_copy')


def supports(case,mode):
    if case not in CASES or mode not in (0,1):raise ValueError('Invalid case or mode')
    if mode==0:return (frozenset('a'),frozenset('b'),frozenset('c'),frozenset('d'))
    if case=='selected_fusion':return (frozenset(('a','b')),frozenset('c'),frozenset('d'))
    return (frozenset('a'),frozenset('b'),frozenset(('c','d')))


def states(case,modes):
    """Exact support persists iff unchanged, stipulated; new supports get new IDs."""
    if case not in CASES:raise ValueError('Invalid case')
    previous={};next_id=0;out=[]
    for mode in modes:
        current={}
        for support in supports(case,mode):
            if support in previous:current[support]=previous[support]
            else:current[support]=next_id;next_id+=1
        out.append(current);previous=current
    return out


def quantities(partition):
    all_tokens=[token for support in partition for token in support]
    if sorted(all_tokens)!=sorted(TOKENS):raise ValueError('Not a partition')
    return {'total':len(all_tokens),
            'by_type':{k:sum(TYPES[t]==k for t in all_tokens) for k in ('red','blue')},
            'subjects':len(partition)}


def record(mode,x,y):
    """A shared, deliberately subject-blind observation model."""
    if mode not in (0,1) or x not in (0,1) or y not in (0,1):raise ValueError('Invalid input')
    return (mode,x,y,(x^y) if mode else None)


def trace(case,inputs):
    modes=[s[0] for s in inputs];latent=states(case,modes)
    return latent,tuple(record(*t) for t in inputs)


def target_initial_locals_persist_with_global(latent):
    """Defined on a 0->1 step: both designated originals persist + conjunct field."""
    if len(latent)!=2:raise ValueError('Requires a two-step transition')
    old,new=latent;a=frozenset('a');b=frozenset('b')
    if a not in old or b not in old:raise ValueError('First state must be split')
    both=(new.get(a)==old[a] and new.get(b)==old[b])
    # Content-type conjunction, not numerical identity of physical or experiential tokens.
    global_field=any({'red','blue'} <= {TYPES[t] for t in sup} for sup in new)
    return bool(both and global_field)


def lower_gap(e0,e1):
    """Known uniform FP/FN upper bounds imply P(Y=1|N=1)-P(Y=1|N=0) >= 1-e1-e0."""
    if not 0<=e0<=1 or not 0<=e1<=1:raise ValueError('Bounds must be probabilities')
    return 1-e0-e1


def main():
    alphabet=list(itertools.product((0,1),repeat=3));counts={}
    for n in range(1,5):
        matched=0
        for seq in itertools.product(alphabet,repeat=n):
            left,record_f=trace('selected_fusion',seq)
            right,record_p=trace('private_copy',seq)
            assert record_f==record_p
            for t in range(n):
                assert quantities(left[t])==quantities(right[t])
            matched+=1
        counts[str(n)]=matched
    prepost={case:target_initial_locals_persist_with_global(states(case,[0,1])) for case in CASES}
    out={'scope':'Invented finite model, not biological evidence or a subject census.',
         'scenarios':{'selected_fusion':'a and b fuse; c and d remain separate',
                      'private_copy':'a and b persist; c and d fuse into a type-corresponding field'},
         'state_quantities':{str(mode):quantities(supports('selected_fusion',mode)) for mode in (0,1)},
         'number_of_equal_record_histories_by_length':counts,
         'designated_original_locals_persist_with_global_after_0_to_1':prepost,
         'idealized_positive_assay_gap_example':{'false_positive_upper_bound':0.10,'false_negative_upper_bound':0.20,'gap_lower_bound':lower_gap(0.10,0.20)},
         'caveats':['Identical observation mapping is assumed, not an empirical discovery.',
                    'Subject identity, experience, compositional amounts, types, and quality are all stipulated.',
                    'The illustrative assay error bounds are not measured or established.']}
    print(json.dumps(out,indent=2,allow_nan=False))


if __name__=='__main__':main()
