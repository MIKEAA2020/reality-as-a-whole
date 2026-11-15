#!/usr/bin/env python3
"""Exact rational instance of the established two-time Wigner-friend gate.

Physical memory is not an established subject or experience. This checks two
single-time effects; it does not construct a joint process or a cosmology.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def mul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(col) for col in zip(*a)]


def plus(a,b):
    return [[x+y for x,y in zip(ra,rb)] for ra,rb in zip(a,b)]


def minus(a,b):
    return [[x-y for x,y in zip(ra,rb)] for ra,rb in zip(a,b)]


def outer(v):
    return [[x*y for y in v] for x in v]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def main():
    z=F(0); o=F(1)
    # Isometry: input |0> -> |00>, |1> -> |11>, order S,F.
    v=[[o,z],[z,z],[z,z],[z,o]]
    memory_up=[[o,z,z,z],[z,z,z,z],[z,z,o,z],[z,z,z,z]]
    e1=mul(mul(transpose(v),memory_up),v)
    a,b=F(3,5),F(4,5)
    p1=outer([a,z,z,b]); p2=outer([b,z,z,-a])
    assert mul(p1,p1)==p1 and mul(p2,p2)==p2
    assert mul(p1,p2)==[[z]*4 for _ in range(4)]
    assert plus(p1,p2)==mul(v,transpose(v))
    # Nonselective Wigner projective measurement in rotated encoded subspace.
    e2=mul(mul(transpose(v),plus(mul(mul(p1,memory_up),p1),
                                 mul(mul(p2,memory_up),p2))),v)
    assert e1 == [[o,z],[z,z]]
    assert e2 == [[F(337,625),F(-84,625)],[F(-84,625),F(288,625)]]
    comm=minus(mul(e1,e2),mul(e2,e1))
    assert comm == [[z,F(-84,625)],[F(84,625),z]]
    rho_plus=[[F(1,2),F(1,2)],[F(1,2),F(1,2)]]
    rho_dephased=[[F(1,2),z],[z,F(1,2)]]
    p=trace(mul(e2,rho_plus)); pd=trace(mul(e2,rho_dephased))
    assert p==F(457,1250) and pd==F(1,2) and pd-p==F(84,625)
    # For this single state, an independent coupling of the two marginals
    # is a normalized, nonnegative joint table. It has no claimed dynamics.
    qplus = p/2
    assert qplus == F(457,2500)
    joint = [[qplus, F(1,2)-qplus], [qplus, F(1,2)-qplus]]
    assert sum(map(sum,joint)) == 1 and all(x >= 0 for row in joint for x in row)
    assert sum(row[0] for row in joint) == p
    # The same product coupling imposed independently for all input states
    # violates preparation affinity, since the quantum state is incomplete
    # for this artificial rule. This is not a claim of physical nonlinearity.
    product_for_mixed = F(1,4)
    mixture_of_z_preparations = F(337,1250)
    assert mixture_of_z_preparations-product_for_mixed == F(49,2500)
    result={
        'status':'passed',
        'scope':'Exact quantum memory effects in one ideal two-time circuit; no phenomenal subjects, universal agent, actual measurement or full interpretation established.',
        'basis_coefficients':['3/5','4/5'],
        'early_effect':[[str(x) for x in row] for row in e1],
        'late_effect':[[str(x) for x in row] for row in e2],
        'commutator':[[str(x) for x in row] for row in comm],
        'unitary_late_memory_up_probability_input_plus':str(p),
        'late_memory_up_probability_with_intermediate_dephasing':str(pd),
        'difference':str(pd-p),
        'fixed_plus_independent_coupling':[[str(x) for x in row] for row in joint],
        'product_rule_for_mixed_state':str(product_for_mixed),
        'mixture_of_z_product_couplings':str(mixture_of_z_preparations),
        'affinity_gap':str(mixture_of_z_preparations-product_for_mixed),
        'limitations':'The no-joint-affine rule holds for all allowed input density matrices under the specified effects; a fixed input alone has couplings. The independent coupling is an unjustified bookkeeping example, not a physical law. Qubit memory is not evidence of consciousness.'
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
