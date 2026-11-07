"""Gaussian readout energy bound, optimized preparation, coupling test.

Finite modes on a fixed reference cosmology. The budget counts the coherent
signal energy and the readout zero-mode kinetic energy, not the energy of all
other fields, reference, memory, switching, vacuum renormalization or gravity.
It is an explicitly incomplete backreaction proxy, not a GR constraint.
"""
from math import erf, sqrt, pi
from pathlib import Path
import json
from quantum_relational_field_instrument import coupled

R=.6; Q=.1
BACKGROUND=1.5*(2*pi)**3


def evaluate(data,B):
    t=data['transfer']; a=data['readout_q_coefficient']; b=data['readout_p_coefficient']
    v=data['other_mode_variance']; c=a*a/8
    assert abs(a)>1e-6 and B>0
    ub=(1+R*(1-2*Q)*erf(sqrt(2)*abs(t)*B/abs(a)))/2
    # Exact optimizer within the stated product-Gaussian family.
    Ed=B/(1+sqrt(1+v*B/c)); Es=B-Ed; P=2*Ed
    cov=-b*P/a
    Qv=b*b*P/(a*a)+1/(4*P)
    assert abs(Qv*P-cov*cov-.25)<1e-8
    variance=v+a*a/(4*P)
    success=(1+R*(1-2*Q)*erf(abs(t)*sqrt(Es/variance)))/2
    assert success<=ub+1e-14
    return {'budget':B,'gaussian_upper':ub,'signal_energy':Es,
            'readout_kinetic_energy':Ed,'signal_displacement':sqrt(2*Es),
            'readout_q_variance':Qv,'readout_p_variance':P,
            'readout_qp_covariance':cov,'readout_final_variance':variance,
            'success':success}


def field_energy(data, opt, t0=False):
    """Bare free-field energy at a pulse-free endpoint for the chosen input.

    Includes retained-mode vacuum contributions, not gravity or reference qubit.
    The n=0 readout has the contractive covariance used in evaluate().
    """
    n=data['nmax']; m=n+1; fields=3*m; dim=2*fields
    S=data['matrix']
    if t0: S=[[float(i==j) for j in range(dim)] for i in range(dim)]
    a=1. if t0 else data['scale']
    variances=[]
    for _ in range(3):
        for k in range(m): variances.append(1. if k==0 else 1/(2*k))
    for _ in range(3):
        for k in range(m): variances.append(.25 if k==0 else k/2)
    iq=2*m; ip=fields+iq
    variances[iq]=opt['readout_q_variance']
    variances[ip]=opt['readout_p_variance']
    cov=opt['readout_qp_covariance']; amp=opt['signal_displacement']
    def second(row):
        return (sum(x*x*v for x,v in zip(row,variances))
                +2*row[iq]*row[ip]*cov+(row[1]*amp)**2)
    total=0.
    for k in range(fields):
        mode=k%m
        total+=second(S[fields+k])/(2*a**3) +a*mode**2*second(S[k])/2
    return total


def main():
    weak=coupled(4,1600,.01,.01)
    bg=BACKGROUND
    rows=[]
    for frac in (.01,.1,1.,10.):
        rows.append({'budget_over_reference_energy':frac, **evaluate(weak,bg*frac)})
    def needed(method):
        lo=0.; hi=bg
        while method(hi)<.7:hi*=2
        for _ in range(80):
            m=(lo+hi)/2
            if method(m)<.7:lo=m
            else:hi=m
        return hi
    necessary=needed(lambda B:evaluate(weak,B)['gaussian_upper'])
    family=needed(lambda B:evaluate(weak,B)['success'])
    strong=coupled(4,1600,.2,.2,include_matrix=True)
    coarse=coupled(3,800,.2,.2)
    check=coupled(6,1600,.2,.2)
    budget=.1*bg
    candidate=evaluate(strong,budget)
    assert candidate['success']>.7
    assert abs(candidate['success']-evaluate(coarse,budget)['success'])<1e-8
    assert abs(candidate['success']-evaluate(check,budget)['success'])<1e-8
    initial=field_energy(strong,candidate,True)
    final=field_energy(strong,candidate)
    scale=strong['scale']
    final_background=(2*pi)**3*(3*.5**2*scale/2+1.5**2/(2*scale**3))
    # H_free initial = budget + other retained-mode Gaussian energy.
    assert abs(initial-(budget+15.25))<1e-9
    result={'status':'passed','scope':'finite-mode quadratic Gaussian field model, fixed cosmology; initial energy budget proxy, not GR backreaction',
            'reference_background_classical_energy':bg,'reference_polarization':R,
            'memory_bit_flip_probability':Q,'weak_coupling':{'lambda':.01,'g':.01,
                'transfer':weak['transfer'],'readout_q_coefficient':weak['readout_q_coefficient'],
                'other_mode_variance':weak['other_mode_variance'],'budgets':rows,
                'necessary_for_70_percent':necessary,'family_optimal_for_70_percent':family,
                'necessary_over_reference':necessary/bg,'family_optimal_over_reference':family/bg},
            'strong_candidate':{'lambda':.2,'g':.2,'modes':'0 through 4','steps':1600,
                'transfer':strong['transfer'],'readout_q_coefficient':strong['readout_q_coefficient'],
                'other_mode_variance':strong['other_mode_variance'],
                'symplectic_defect':strong['symplectic_defect'],'budget_over_reference':.1,
                'preparation':candidate,'initial_bare_total_retained_field_energy':initial,
                'initial_bare_total_over_reference_energy':initial/bg,
                'final_bare_free_field_energy':final,
                'final_clock_rod_energy_on_fixed_background':final_background,
                'final_bare_fields_over_clock_rods':final/final_background,
                'coarse_success':evaluate(coarse,budget)['success'],
                'six_mode_cutoff_success':evaluate(check,budget)['success']},
            'limitations':'Fixed reference cosmology; QND sign qubit; field interactions quadratic; initial energy proxy excludes reference and memory, switching costs, discarded modes, renormalization and nonlinear gravitational response.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
