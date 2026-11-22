#!/usr/bin/env python3
"""Exact controls for closure, conservation, symmetry and a signed score.

Finite illustrative structures only: not cosmological energy, empirical
subject data, or a proof of an ontology. See the accompanying source audit.
"""
import json
from pathlib import Path

# Three vertices, three oriented edges 0->1, 1->2, 2->0.
B = ((-1, 0, 1), (1, -1, 0), (0, 1, -1))


def divergence(edges):
    if len(edges) != 3:
        raise ValueError('three edges required')
    return tuple(sum(row[j]*edges[j] for j in range(3)) for row in B)


def transfer(q, flux):
    if len(q) != 3:
        raise ValueError('three vertex values required')
    d = divergence(flux)
    return tuple(q[i]+d[i] for i in range(3))


def inversion_swap(q):
    """T(q0,q1,q2)=(-q2,-q1,-q0), involution and Q(Tq)=-Q(q)."""
    if len(q) != 3:
        raise ValueError('three vertex values required')
    return (-q[2],-q[1],-q[0])


def run():
    q=(2,-1,2); flux=(1,-2,3); after=transfer(q,flux)
    assert after==(4,2,-3) and sum(q)==sum(after)==3
    gauss=divergence((1,2,0))
    assert gauss==(-1,-1,2) and sum(gauss)==0
    q_sym=(1,0,-1)
    assert inversion_swap(inversion_swap(q))==q
    assert sum(inversion_swap(q))==-sum(q)
    assert inversion_swap(q_sym)==q_sym and sum(q_sym)==0
    # A signed score on explicitly labelled occurrences is a toy index;
    # it does not establish experiential subjects, quantities, or cancellation.
    labelled=(('A',2),('B',-2))
    score=sum(v for _,v in labelled)
    assert score==0 and len(labelled)==2 and all(v!=0 for _,v in labelled)
    return {'status':'passed','model':'three-node closed oriented graph, exact integers',
        'nonzero_conserved_signed_charge_before':list(q),
        'nonzero_conserved_signed_charge_after':list(after),
        'conserved_total':sum(q),
        'additional_gauss_law_edge_field':[1,2,0],
        'gauss_vertex_charge':list(gauss),'gauss_total':sum(gauss),
        'symmetry_invariant_configuration':list(q_sym),'symmetry_fixed_total':sum(q_sym),
        'toy_signed_labelled_occurrences':list(labelled),'toy_net_score':score,
        'scope':'Algebraic controls only; not a derivation of energy, subject incidence, valence aggregation, or actual cosmology.'}


if __name__ == '__main__':
    result=run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
