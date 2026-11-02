"""Signed particle/hole covariance updates; not a positive-kernel assumption."""
import importlib.util
import math
import cmath
from pathlib import Path
s=importlib.util.spec_from_file_location('particle_hole_packet_reference',Path(__file__).resolve().parents[1]/'wilson_wavepacket_composite'/'model.py')
p=importlib.util.module_from_spec(s);s.loader.exec_module(p)
w=p.w


def validate(a,n,particle,hole):
    p.validate(a,particle);p.validate(a,hole);w.parameters(a,n,1.)


def packet(kind,x,t=0.,a=None,j=0,component=0):
    if kind not in ('particle','hole'):raise ValueError('Particle or hole mode required')
    if kind=='particle':return p.packet(x,t,a,j,component)
    # Mirror negative momentum, negative signed energy. Lower spinor is odd.
    return (-1 if component else 1)*p.packet(x,t,a,j,component).conjugate()


def target(x,t=0.,particle=1.,hole=1.):
    validate(.1,1,particle,hole)
    return (particle+hole)*p.target(x,t)


def terms(a,n,x,t=0.,particle=1.,hole=1.):
    validate(a,n,particle,hole);h=a*n
    vp=(packet('particle',x+h/2,t,a),packet('particle',x-h/2,t,a))
    vh=(packet('hole',x+h/2,t,a),packet('hole',x-h/2,t,a))
    linear=w.shape(n)*(particle*(vp[1].conjugate()*vp[0]).imag-hole*(vh[1].conjugate()*vh[0]).imag)/h
    signed_gram=-math.pi*particle*hole*abs(vp[0]*vh[1]-vh[0]*vp[1])**2
    return linear,signed_gram


def current(a,n,x,t=0.,particle=1.,hole=1.):return sum(terms(a,n,x,t,particle,hole))


def covariance(a,n,x,t=0.,particle=1.,hole=1.):
    validate(a,n,particle,hole);h=a*n;sites=(x+h/2,x-h/2);base=w.same_chirality_covariance(a,n)
    v=[packet('particle',z,t,a) for z in sites];u=[packet('hole',z,t,a) for z in sites]
    return tuple(tuple(base[i][j]+a*(particle*v[i]*v[j].conjugate()-hole*u[i]*u[j].conjugate()) for j in range(2)) for i in range(2))


def signed_term_bound(a,n,particle=1.,hole=1.):
    validate(a,n,particle,hole)
    return math.pi*particle*hole*(a*n)**2*(2*p.B(0)*p.B(1))**2


def error_bound(a,n,t=0.,particle=1.,hole=1.):
    validate(a,n,particle,hole)
    return (particle+hole)*p.error_bound(a,n,t)+signed_term_bound(a,n,particle,hole)


def hamiltonian_image(kind,x,t,a,component=0):
    validate(a,1,1.,1.)
    if kind not in ('particle','hole') or component not in (0,1):raise ValueError('Invalid spectral mode')
    sign=1 if kind=='particle' else -1
    def integrand(k):
        momentum=sign*k;energy=2*math.sin(a*momentum/2)/a
        spin=math.cos(a*momentum/4) if component==0 else math.sin(a*momentum/4)
        return p.amplitude(k)*spin*energy*cmath.exp(1j*(momentum*x-energy*t))
    return p.integral(integrand)/math.sqrt(2*math.pi)


def local_energy(a,x,t=0.,particle=1.,hole=1.):
    validate(a,1,particle,hole)
    return sum(weight*(packet(kind,x,t,a,component=c).conjugate()*hamiltonian_image(kind,x,t,a,c)).real
               for kind,weight in (('particle',particle),('hole',-hole)) for c in (0,1))


def total_energy(a=None,particle=1.,hole=1.):
    validate(a if a is not None else .1,1,particle,hole)
    return (particle+hole)*p.total_energy(a)


def signed_number(particle=1.,hole=1.):
    validate(.1,1,particle,hole)
    return particle-hole
