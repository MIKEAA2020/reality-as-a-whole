"""Wilson Hamiltonian regulator of the static conformal Dirac model.

This is not a Floquet logarithm. Free finite-energy UV exclusion is explicit;
state convergence uses the common-core/gap argument in REPORT.md. No stress
renormalization or interacting universality is inferred from these diagnostics.
"""
from functools import lru_cache
import cmath
import importlib.util
import math
from pathlib import Path

_spec=importlib.util.spec_from_file_location('hamiltonian_state_reference',Path(__file__).resolve().parents[1]/'hamiltonian_state_limit'/'model.py')
central=importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(central)
w,car,vac,local=central.w,central.car,central.vac,central.local
curved=central.curved


def wilson_mass(k,a,r=1.):
    w.parameters(k,r,a)
    if r<0:
        raise ValueError('Nonnegative Wilson parameter required')
    return r*(1-math.cos(k*a))/a


def symbol(k,mass,a,r=1.):
    w.parameters(k,mass,a)
    return w.add(w.scale(math.sin(k*a)/a,w.Z),w.scale(mass+wilson_mass(k,a,r),w.X))


def energy(k,mass,a,r=1.):
    w.parameters(k,mass,a)
    return math.hypot(math.sin(k*a)/a,mass+wilson_mass(k,a,r))


def negative_fibre(k,mass,a,r=1.):
    e=energy(k,mass,a,r)
    if e==0:
        raise ValueError('Gapped fibre required')
    return w.scale(.5,w.add(w.I,w.scale(-1/e,symbol(k,mass,a,r))))


def finite_energy_cutoff(cutoff,mass,a):
    """Exact r=1 free momentum bound in the Brillouin interval."""
    w.parameters(cutoff,mass,a)
    if mass<=0 or cutoff<mass:
        raise ValueError('Positive mass and energy cutoff >= mass required')
    argument=a*math.sqrt((cutoff*cutoff-mass*mass)/(1+mass*a))/2
    return math.pi/a if argument>=1 else 2*math.asin(argument)/a


def lattice_hamiltonian(amplitudes,mass,a,epsilon=.2,q=1.,r=1.):
    wilson_mass(0,a,r)
    result=central.lattice_hamiltonian(amplitudes,mass,a,epsilon,q)
    for j,f in amplitudes.items():
        xf=w.apply(w.X,f)
        result=local.add_lattice(result,{j:tuple(r*x/a for x in xf),j-1:tuple(-r*x/(2*a) for x in xf),j+1:tuple(-r*x/(2*a) for x in xf)})
    return result


def ring_hamiltonian(sites,mass=.7,epsilon=.2,q=1.,r=1.):
    base=central.ring_hamiltonian(sites,mass,epsilon,q)
    out=[list(row) for row in base]; a=2*math.pi/(q*sites)
    for i,k in enumerate(range(-(sites//2),sites//2+1)):
        value=wilson_mass(q*k,a,r)
        out[2*i][2*i+1]+=value; out[2*i+1][2*i]+=value
    return tuple(tuple(row) for row in out)


@lru_cache(None)
def spectral_data(sites):
    h=ring_hamiltonian(sites)
    eigenvalues,vectors=curved.symmetric_eigensystem(h)
    projection=curved.negative_projection(eigenvalues,vectors)
    return h,eigenvalues,vectors,projection


def circle_errors(sites,reference_sites=19):
    _,_,_,p=spectral_data(sites)
    _,_,_,pref=central.spectral_data(reference_sites,True)
    f,g=central.fixed_smear(sites),central.fixed_smear(sites,True)
    fr,gr=central.fixed_smear(reference_sites),central.fixed_smear(reference_sites,True)
    pf,prf=car.apply(p,f),car.apply(pref,fr)
    low_error=math.sqrt(sum(abs(pf[2*(k+sites//2)+r]-prf[2*(k+reference_sites//2)+r])**2 for k in (-1,0,1) for r in (0,1)))
    return low_error,abs(vac.pairing(p,f,g)-vac.pairing(pref,fr,gr)),abs(vac.density_pair(p,f,g)-vac.density_pair(pref,fr,gr))


def cross_regulator_pairing_error(sites):
    f,g=central.fixed_smear(sites),central.fixed_smear(sites,True)
    return abs(vac.pairing(spectral_data(sites)[3],f,g)-vac.pairing(central.spectral_data(sites)[3],f,g))


def high_zone_bound(a,cutoff,theta0,mass=.7,epsilon=.2):
    if not 0<theta0<=math.pi or cutoff<=0 or mass<=0:
        raise ValueError('Positive cutoff/mass and zone angle in (0,pi] required')
    w.parameters(cutoff,mass,a); curved.parameters(epsilon,1.)
    return a*(cutoff+mass*abs(epsilon))/(2*math.sqrt(1+mass*a)*math.sin(theta0/2))


def low_energy_high_zone_norm(sites,cutoff=1.5,theta0=math.pi/2):
    """Exact finite spectral norm, not just a maximum over eigenbasis vectors."""
    _,e,o,_=spectral_data(sites)
    low=[j for j,x in enumerate(e) if abs(x)<=cutoff]
    high=[2*i+r for i,k in enumerate(range(-(sites//2),sites//2+1)) if abs(2*math.pi*k/sites)>=theta0 for r in (0,1)]
    if not low or not high:
        return 0.
    gram=tuple(tuple(sum(o[i][j]*o[i][k] for i in high) for k in low) for j in low)
    if len(low)==1:
        return math.sqrt(max(0,gram[0][0]))
    values,_=curved.symmetric_eigensystem(gram)
    return math.sqrt(max(0,max(values)))


def free_site_amplitude(site,time_over_a,sites=31,a=1.,mass=0.):
    """Finite free ring diagnostic; no strict causal cone for continuous time."""
    if not isinstance(sites,int) or sites<5:
        raise ValueError('Ring with at least five sites required')
    out=[0j,0j]
    for ell in range(sites):
        theta=2*math.pi*ell/sites; k=theta/a
        u=w.dirac(math.sin(theta)/a,mass+wilson_mass(k,a),time_over_a*a)
        f=w.apply(u,(1,0)); phase=cmath.exp(1j*theta*site)/sites
        for r in (0,1):out[r]+=phase*f[r]
    return tuple(out)
