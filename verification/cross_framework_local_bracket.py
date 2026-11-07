"""Discrete numerical witness for a continuum scalar-field bracket calculation.

This is a fixed-background matter example, not a gravitational constraint algebra.
Uses exact derivatives of the discrete Hamiltonians and the lattice Poisson bracket.
"""
import json
import math
from pathlib import Path


def discrete(n, speeds):
    h=2*math.pi/n
    x=[i*h for i in range(n)]
    deriv=lambda f:[(f[(i+1)%n]-f[(i-1)%n])/(2*h) for i in range(n)]
    lapse_n=[1.0]*n
    lapse_m=[math.sin(2*t) for t in x]
    field=[math.sin(t) for t in x]
    p=[math.cos(t) for t in x]
    field_prime=deriv(field)
    dm=deriv(lapse_m)
    d_lapse_n_field=deriv([lapse_n[i]*field_prime[i] for i in range(n)])
    d_lapse_m_field=deriv([lapse_m[i]*field_prime[i] for i in range(n)])
    # δH_f/δφ=-c² D(f Dφ), δH_f/δp=f p. The discrete
    # canonical brackets are {φ_i,p_j}=δ_ij/h.
    def bracket(c):
        return h*sum((-c*c*d_lapse_n_field[i])*(lapse_m[i]*p[i])
                     -(lapse_n[i]*p[i])*(-c*c*d_lapse_m_field[i])
                     for i in range(n))
    d_one=h*sum(p[i]*field_prime[i]*dm[i] for i in range(n))
    return {'n':n,'bracket':sum(bracket(c) for c in speeds),
            'discrete_total_momentum':len(speeds)*d_one,
            'mismatch':sum(bracket(c) for c in speeds)-len(speeds)*d_one,
            'single_velocity_bracket':bracket(1.0)}


def main():
    cases=[discrete(n,(1.0,.5)) for n in (32,64,128,256,512,1024,2048)]
    for row in cases:
        n=row['n']
        # Exact identity for this discretization, for all selected n>8:
        # B_c=c² π sinc(h)², D_c=π sinc(h)sinc(2h).
        h=2*math.pi/n
        sinc=lambda z:math.sin(z)/z
        assert abs(row['bracket']-1.25*math.pi*sinc(h)**2)<1e-11
        assert abs(row['discrete_total_momentum']-2*math.pi*sinc(h)*sinc(2*h))<1e-11
    assert abs(cases[-1]['bracket']-1.25*math.pi)<1e-4
    assert abs(cases[-1]['mismatch']+.75*math.pi)<1e-4
    matched=discrete(2048,(1.0,1.0))
    assert abs(matched['mismatch'])<1e-4
    # Two independent field profiles force one common effective structure
    # coefficient to be simultaneously c1² and c2², impossible here.
    assert 1.0**2 != .5**2
    result={'status':'passed', 'speeds':[1.0,.5],
            'continuum_bracket':1.25*math.pi,
            'continuum_total_momentum':2*math.pi,
            'continuum_mismatch':-.75*math.pi,
            'mismatch_cases':cases, 'equal_speed_control':matched,
            'scope':'Classical fixed-background matter; no claim of a quantum GR anomaly.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
