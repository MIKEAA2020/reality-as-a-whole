#!/usr/bin/env python3
"""Arithmetic for a preparation-dephasing control on OPH's C/E plus marginal.

Uses the pinned repository's published ideal probability formula. It does
not simulate the native instruments or compare their complete joint outputs.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def p_c(kappa, cos_theta):
    return F(3,8)+kappa*cos_theta/4


def p_e():
    return F(3,8)


def main():
    checks=0
    for i in range(101):
        k=F(i,100)
        p0=p_c(k,F(1))
        ppi=p_c(k,F(-1))
        p90=p_c(k,F(0))
        assert p0-ppi==k/2
        assert p90==p_e()
        assert F(0)<=ppi<=p0<=1
        checks+=1
    assert (p_c(F(1),F(1)),p_c(F(1),F(-1))) == (F(5,8),F(1,8))
    assert all(p_c(F(0),c)==p_e() for c in (F(-1),F(0),F(1)))
    out={'status':'passed','rational_retention_values_checked':checks,
         'ideal_C_phase_0':str(p_c(F(1),F(1))),
         'ideal_C_phase_pi':str(p_c(F(1),F(-1))),
         'E_all_phases':'3/8',
         'C_complete_preparation_dephasing_all_phases':'3/8',
         'phase_reversal_contrast':'kappa/2',
         'scope':'Plus marginal only, under the specified dephased preparation, ideal coherent projector and published ideal single-event C/E formulas. The complete joint tape/readout statistics, other probes and physical implementation are not checked.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
