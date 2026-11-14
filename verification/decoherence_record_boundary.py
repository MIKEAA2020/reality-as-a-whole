#!/usr/bin/env python3
"""Finite analytical controls, not real-world subject or collapse evidence."""
from fractions import Fraction as F
from math import atan, cos, pi
from pathlib import Path
import json


def main():
    # Equal branch weights; each discarded fragment has overlap 1/2.
    # Two orthonormal retained branch vectors yield the 2x2 coherence block.
    branches = []
    for m in (0,1,2,4,10,20):
        r = F(1,2)**m
        distance = r/2  # trace distance of coherent and dephased states
        success = (1+distance)/2
        assert F(1,2) <= success <= F(3,4)
        branches.append({'discarded_fragments':m,'remaining_overlap':str(r),
                         'trace_distance':str(distance),'equal_prior_optimal_success':str(success),
                         'equal_prior_optimal_success_decimal':float(success)})
    assert branches[0]['equal_prior_optimal_success']=='3/4'
    assert branches[-2]['equal_prior_optimal_success']=='2049/4096'

    # rho± = I/2 ± epsilon X. Their top eigenvectors |±> are orthogonal;
    # trace distance of the full input matrices is 2 epsilon.
    selector=[]
    for eps in (F(1,10),F(1,100),F(1,10000)):
        assert 0 < eps < F(1,2)
        selector.append({'epsilon':str(eps), 'input_trace_distance':str(2*eps),
                         'top_eigenprojector_trace_distance':'1'})
    # Nondegenerate diagonals: delta=epsilon²; eigenvector angle in (0,π/4).
    e=0.01; delta=e*e; angle=0.5*atan(e/delta)
    pointer_overlap=cos(angle)**2
    assert abs(pointer_overlap-0.5049997500187484)<1e-12
    assert 0<angle<pi/4
    result={'scope':'Exact binary-fragment and density-matrix toy controls, not new data, a collapse model or a subject test.',
            'bounded_access':{'branch_weights':'1/2,1/2','fragment_overlap':'1/2',
               'rows':branches,'note':'S and apparatus retained, and all other listed discarded fragments identical; ideal Helstrom measurement on all retained systems.'},
            'selector_instability':selector,
            'nondegenerate_pointer_example':{'epsilon':e,'delta':delta,'angle_radians':angle,
                   'dominant_eigenvector_pointer_overlap_squared':pointer_overlap,
                   'diagonalizing_basis_is_not_a_stability_criterion':True}}
    text=json.dumps(result,indent=2)+'\n'
    Path(__file__).with_suffix('.json').write_text(text,encoding='utf-8'); print(text)

if __name__=='__main__': main()
