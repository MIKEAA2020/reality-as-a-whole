"""Actual phase-averaged sea rotation versus quasifree state of its covariance."""
import importlib.util
import math
from pathlib import Path
s=importlib.util.spec_from_file_location('nonquasifree_coherence_reference',Path(__file__).resolve().parents[1]/'wilson_coherent_rotation'/'model.py')
c=importlib.util.module_from_spec(s);s.loader.exec_module(c)
p,w=c.p,c.w


def validate(a,n,theta):c.parameters(a,n,theta,0.)


def probability(theta=math.pi/4):
    validate(.1,1,theta)
    return math.sin(theta)**2


def covariance(a,n,x,t=0.,theta=math.pi/4):
    validate(a,n,theta);q=probability(theta);base=w.same_chirality_covariance(a,n);swap=c.covariance(a,n,x,t,math.pi/2,0)
    return tuple(tuple((1-q)*base[i][j]+q*swap[i][j] for j in (0,1)) for i in (0,1))


def density(a,n,x,t=0.,theta=math.pi/4):
    """Actual reduced mixed density: mixture of states, not Wick of mean C."""
    validate(a,n,theta);q=probability(theta);base=p.density_matrix(w.same_chirality_covariance(a,n));swap=p.density_matrix(c.covariance(a,n,x,t,math.pi/2,0))
    return w.car.add(w.car.scale(1-q,base),w.car.scale(q,swap))


def quasifree_density(a,n,x,t=0.,theta=math.pi/4):return p.density_matrix(covariance(a,n,x,t,theta))


def current(a,n,x,t=0.,theta=math.pi/4):
    validate(a,n,theta)
    return probability(theta)*c.current(a,n,x,t,math.pi/2,0)


def quasifree_current(a,n,x,t=0.,theta=math.pi/4):
    validate(a,n,theta);q=probability(theta);linear,det=c.terms(a,n,x,t,math.pi/2,0)
    return q*linear+q*q*det


def connected_current(a,n,x,t=0.,theta=math.pi/4):
    validate(a,n,theta);q=probability(theta)
    return q*(1-q)*c.terms(a,n,x,t,math.pi/2,0)[1]


def connected_bound(a,n,theta=math.pi/4):
    validate(a,n,theta);q=probability(theta)
    return math.pi*q*(1-q)*(a*n)**2*(c.B(0,0)*c.B(1,1)+c.B(1,0)*c.B(0,1))**2


def target(x,t=0.,theta=math.pi/4):return probability(theta)*c.target(x,t,math.pi/2,0)


def error_bound(a,n,t=0.,theta=math.pi/4):
    validate(a,n,theta)
    return probability(theta)*c.error_bound(a,n,t,math.pi/2,0)


def local_energy(a,x,t=0.,theta=math.pi/4):return probability(theta)*c.local_energy(a,x,t,math.pi/2,0)


def mode_density(theta=math.pi/4,quasifree=False):
    """Packet sector basis: vacuum, p occupied, h occupied, both occupied."""
    q=probability(theta)
    if not quasifree:return {(1,1):complex(q),(2,2):complex(1-q)}
    return p.density_matrix(((complex(q),0j),(0j,complex(1-q))))
