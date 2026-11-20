#!/usr/bin/env python3
"""Check bounded spinor/geometry and one-way classical-control examples.

These checks do not derive spacetime, experience, or a fundamental hybrid theory.
"""
from fractions import Fraction as F
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def mm(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def transpose(a):
    return [list(x) for x in zip(*a)]


def main():
    # psi=(1,1), B=diag(2,1/2), both treated as unnormalized real spinors.
    k = [F(2), F(2), F(0), F(0)]
    boosted = [F(17, 4), F(2), F(0), F(15, 4)]
    assert k[0]**2 - sum(x*x for x in k[1:]) == 0
    assert boosted[0]**2 - sum(x*x for x in boosted[1:]) == 0
    assert boosted[0] == F(17, 8)*k[0] + F(15, 8)*k[3]
    assert boosted[3] == F(15, 8)*k[0] + F(17, 8)*k[3]
    assert F(17, 8)**2 - F(15, 8)**2 == 1
    rho0 = [[F(1), F(0)], [F(0), F(0)]]
    plus = [[F(1, 2), F(1, 2)], [F(1, 2), F(1, 2)]]
    boost = [[F(2), F(0)], [F(0), F(1, 2)]]
    unnorm = mm(mm(boost, plus), boost)
    transformed = [[v / tr(unnorm) for v in row] for row in unnorm]
    assert tr(mm(rho0, plus)) == F(1, 2)
    assert tr(mm(rho0, transformed)) == F(16, 17)

    # C is classical: allowed density matrices are block diagonal in C.
    # Controlled-X is block diagonal and acts as its own inverse.
    eye4 = [[F(int(i == j)) for j in range(4)] for i in range(4)]
    U = [[F(1),0,0,0], [0,F(1),0,0], [0,0,0,F(1)], [0,0,F(1),0]]
    assert mm(U, U) == eye4 == mm(U, transpose(U))
    # Input C is fair; Q starts at |0>.  Output C and Q are correlated.
    rho = [[F(0) for _ in range(4)] for _ in range(4)]
    rho[0][0] = rho[2][2] = F(1, 2)
    out = mm(mm(U, rho), transpose(U))
    assert [out[i][i] for i in range(4)] == [F(1,2), 0, 0, F(1,2)]
    assert mm(mm(U, out), transpose(U)) == rho
    # For any two arbitrary 2x2 real block matrices, conjugation retains C-block diagonality.
    a = [[F(1),F(2)],[F(2),F(3)]]
    b = [[F(4),F(5)],[F(5),F(6)]]
    generic = [[F(0) for _ in range(4)] for _ in range(4)]
    for i in range(2):
        for j in range(2):
            generic[i][j], generic[i+2][j+2] = a[i][j], b[i][j]
    g = mm(mm(U, generic), transpose(U))
    assert all(g[i][j] == 0 for i in range(2) for j in range(2,4))
    assert all(g[i][j] == 0 for i in range(2,4) for j in range(2))
    result = {
        'scope': 'Illustrative finite calculations, not a derivation of spacetime, quantum gravity, experience, or two-way fundamental classical-quantum coupling.',
        'spinor_null_before': [str(x) for x in k],
        'spinor_null_after': [str(x) for x in boosted],
        'standard_qubit_fidelity_before': '1/2',
        'standard_qubit_fidelity_after_naive_normalized_boost': '16/17',
        'classical_control_output_diagonal': [str(out[i][i]) for i in range(4)],
        'global_input_and_output_von_neumann_entropy_bits': 1,
        'output_mutual_information_bits': 1,
        'classical_control_only_not_quantum_to_classical_measurement': True,
    }
    (ROOT / 'verification/ur_spinor_classical_control_gate.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
