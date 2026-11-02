"""Exact finite overlap check; not QFT unification or consciousness evidence."""
from fractions import Fraction as Q
import json
from pathlib import Path


def multiply(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def diagonal(values):
    return [[Q(v) if i==j else Q(0) for j in range(len(values))]
            for i,v in enumerate(values)]


def main():
    rho=[[Q(1,2) if i in (0,3) and j in (0,3) else Q(0)
          for j in range(4)] for i in range(4)]
    za=diagonal((1,1,-1,-1))
    zb=diagonal((1,-1,1,-1))
    za_zb=multiply(za,zb)
    assert multiply(za,zb)==multiply(zb,za)
    assert multiply(rho,rho)==rho and trace(rho)==1
    reduced_a=[[sum(rho[2*i+k][2*j+k] for k in (0,1)) for j in (0,1)] for i in (0,1)]
    reduced_b=[[sum(rho[2*k+i][2*k+j] for k in (0,1)) for j in (0,1)] for i in (0,1)]
    half_identity=[[Q(1,2),Q(0)],[Q(0),Q(1,2)]]
    assert reduced_a==reduced_b==half_identity
    expectations=[trace(multiply(rho,a)) for a in (za,zb,za_zb)]
    assert expectations==[0,0,1]
    assert rho!=diagonal((Q(1,4),)*4)
    result={'scope':'Exact finite quantum-information/operator-algebra overlap only; not a relativistic QFT, full integration, empirical measurement, or phenomenal identification.',
            'expectations_ZA_ZB_ZAZB':[str(x) for x in expectations],
            'reduced_states_are_half_identity':True,
            'joint_state_not_product_of_reduced_states':True,
            'local_observables_commute':True,
            'normalized_rank_one_projector':True}
    destination=Path(__file__).with_name('integration-overlap-results.json')
    destination.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
