"""Finite diagnostics for the spacetime CAR construction in REPORT.md.

Momentum samples are not spacetime-compact functions. Geometry tests, discrete
walk tests, quadrature tests and analytic continuum proofs are kept separate.
"""
import cmath
import importlib.util
import math
from pathlib import Path

_spec=importlib.util.spec_from_file_location('vacuum_reference',Path(__file__).resolve().parents[1]/'quasifree_vacuum'/'model.py')
vac=importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(vac)
car,w=vac.car,vac.w


def smear(k,mass,samples):
    """Finite quadrature for QF(k) = integral exp(it h(k)) F(t,k) dt."""
    w.hamiltonian(k,mass)
    out=[0j,0j]
    for time,weight,f in samples:
        evolved=w.apply(w.dirac(k,mass,-time),f)
        for i in range(2):
            out[i]+=weight*evolved[i]
    return tuple(out)


def bump(t):
    return math.exp(-1/(1-t*t)) if abs(t)<1 else 0.


def bump_derivative(t):
    return -2*t*bump(t)/(1-t*t)**2 if abs(t)<1 else 0.


def eom_samples(k,mass,f,inverse_step):
    if not isinstance(inverse_step,int) or inverse_step<1:
        raise ValueError('Positive integer inverse quadrature step required')
    h=w.apply(w.hamiltonian(k,mass),f)
    return tuple((j/inverse_step,1/inverse_step,
                  tuple(1j*bump_derivative(j/inverse_step)*f[i]-bump(j/inverse_step)*h[i] for i in range(2)))
                 for j in range(-inverse_step,inverse_step+1))


def boost_point(time,space,eta):
    if not all(math.isfinite(v) for v in (time,space,eta)):
        raise ValueError('Finite coordinates required')
    c,s=math.cosh(eta),math.sinh(eta)
    return (c*time-s*space,c*space-s*time)


def branch_boost(k,mass,sign,eta):
    vac.positive_mass(mass)
    if sign not in (-1,1):
        raise ValueError('Energy branch sign must be +/-1')
    energy=sign*math.hypot(k,mass)
    ep,kp=boost_point(energy,k,eta)
    jacobian=math.cosh(eta)-math.sinh(eta)*k/energy
    return ep,kp,jacobian


def source_boost(eta):
    # Q intertwines contragredient source transformation, not S itself.
    return w.adjoint(w.boost_spin(-eta))


def diamond_contains(time,space,center=0.,radius=1.):
    if radius<=0:
        raise ValueError('Positive diamond radius required')
    return abs(time)+abs(space-center)<radius


def shadow(center_time,center_space,time_radius,space_radius):
    if time_radius<0 or space_radius<0:
        raise ValueError('Nonnegative support radii required')
    radius=space_radius+abs(center_time)+time_radius
    return center_space-radius,center_space+radius


def spacelike_boxes(a,b):
    """Boxes (time center, space center, time radius, space radius)."""
    if any(r<0 for r in (a[2],a[3],b[2],b[3])):
        raise ValueError('Nonnegative box radii required')
    return abs(a[1]-b[1])-a[3]-b[3]>abs(a[0]-b[0])+a[2]+b[2]


def inverse_walk(amplitudes,mass,spacing,steps):
    if not isinstance(steps,int) or steps<0:
        raise ValueError('Nonnegative integer horizon required')
    coin=w.adjoint(w.coin(mass,spacing))
    result=dict(amplitudes)
    for _ in range(steps):
        shifted={}
        for site,spinor in result.items():
            for target,component in ((site-1,0),(site+1,1)):
                f=shifted.setdefault(target,[0j,0j])
                f[component]+=spinor[component]
        result={site:w.apply(coin,f) for site,f in shifted.items()}
        result={site:f for site,f in result.items() if any(v!=0 for v in f)}
    return result


def lattice_inner(a,b):
    return sum(vac.inner(f,b.get(site,(0j,0j))) for site,f in a.items())
