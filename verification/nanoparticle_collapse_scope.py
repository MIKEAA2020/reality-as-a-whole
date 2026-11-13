#!/usr/bin/env python3
"""Dimensional checks and finite-toy operator-scope controls.

Not a replay of the authors' raw data, a posterior, or a laboratory bound on
energy-driven collapse. See NANOPARTICLE_INTERFERENCE_COLLAPSE_AUDIT.md.
"""
import json
import math
from pathlib import Path
import numpy as np
from scipy.constants import h, hbar, physical_constants
from scipy.integrate import quad
from scipy.special import spherical_jn, sici

ROOT=Path(__file__).resolve().parent.parent


def f(x):
    if abs(x)<1e-3:
        return x*x/18-x**4/600+x**6/35280
    return 1-sici(x)[0]/x


def main():
    # Nature Eq. 10: monodisperse spherical cluster, ell=1, no mass/velocity average.
    mass=172000*physical_constants['atomic mass constant'][0]
    me=physical_constants['electron mass'][0]
    radius=4e-9; period=133e-9; spacing=.983; speed=160.; ell=1
    coherence_length=10e-9; tau=2.84e15
    wavelength=h/(mass*speed)
    talbot=period**2/wavelength
    alpha=radius/coherence_length
    b=ell*period/coherence_length*spacing/talbot
    def integrand(z):
        factor=3*spherical_jn(1,alpha*z)/alpha
        return math.exp(-z*z/2)*factor**2*f(b*z)
    integral,err=quad(integrand,0,np.inf,epsabs=1e-12,epsrel=1e-12)
    k=2*math.sqrt(2/math.pi)*(mass/me)**2*(spacing/speed)*integral
    tau_visibility=k/(-math.log(.78))
    assert 0 < math.exp(-k/tau) < 1
    assert abs(math.log10(tau)-15.453318340)<1e-7
    # Exactly degenerate energy doublet, versus position-like dephasing.
    # H=diag(0,0,1), X=diag(-.5,.5,0); rate gamma=1, t=1.
    energy=np.array([0.,0.,1.]); position=np.array([-.5,.5,0.])
    def retention(vals,i,j,coupling=1.,t=1.):
        return math.exp(-.5*coupling*t*(vals[i]-vals[j])**2)
    energy_degenerate=retention(energy,0,1)
    position_degenerate=retention(position,0,1)
    energy_gap=retention(energy,0,2)
    assert energy_degenerate==1 and abs(position_degenerate-math.exp(-.5))<1e-15
    assert abs(energy_gap-math.exp(-.5))<1e-15
    # A generic r>=.78 / T exercise is NOT a bound inferred from the Nature data.
    rate=-math.log(.78)/(2*spacing/speed)
    out={'scope':'Monodisperse arithmetic and abstract finite-level controls; not an experimental reanalysis.',
         'mass_Da':172000,'cluster_diameter_m':2*radius,'period_m':period,
         'velocity_m_per_s':speed,'grating_spacing_m':spacing,
         'de_broglie_wavelength_m':wavelength,'talbot_length_m':talbot,
         'spacing_over_talbot_length':spacing/talbot,'two_leg_time_s':2*spacing/speed,
         'mmm':{'model':'Nature eq. 10, ell=1; single representative mass and velocity, no averaging',
                'hbar_over_sigma_q_m':coherence_length,'published_tau_m_s':tau,
                'log10_published_tau':math.log10(tau),'quadrature_integral':integral,
                'quadrature_error_estimate':err,'coefficient_K_s':k,
                'single_particle_R1_at_published_tau':math.exp(-k/tau),
                'heuristic_tau_for_R1_0p78_s':tau_visibility,
                'heuristic_not_authors_credible_bound':True},
         'basis_counterexample':{'energy_eigenvalues':energy.tolist(),
             'position_like_eigenvalues':position.tolist(),'gamma_times_t':1,
             'energy_dephasing_retention_degenerate_pair':energy_degenerate,
             'position_dephasing_retention_same_pair':position_degenerate,
             'energy_dephasing_retention_nondegenerate_control':energy_gap},
         'illustrative_constant_rate_for_R_0p78_per_s':rate}
    (ROOT/'verification/nanoparticle_collapse_scope.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
