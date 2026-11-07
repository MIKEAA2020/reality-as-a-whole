"""Declared negative-energy polarization of the free walk/Dirac CAR system.

Finite diagnostics only; common-space and infinite-volume proofs in REPORT.md.
No absolute vacuum energy is inferred from a quasienergy branch.
"""
import importlib.util
import math
from pathlib import Path

_spec=importlib.util.spec_from_file_location('fermionic_reference',Path(__file__).resolve().parents[1]/'fermionic_lift'/'model.py')
car=importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(car)
w=car.walk_model


def positive_mass(mass):
    if not math.isfinite(mass) or mass<=0:
        raise ValueError('Strictly positive finite mass required in this gapped construction')


def dirac_covariance(k,mass):
    positive_mass(mass)
    h=w.hamiltonian(k,mass)
    return w.scale(.5,w.add(w.I,w.scale(-1/math.hypot(k,mass),h)))


def walk_vector(k,mass,a):
    positive_mass(mass)
    w.parameters(k,mass,a)
    if not 0<mass*a<math.pi/2:
        raise ValueError('Require 0 < mass*spacing < pi/2 for the chosen branch')
    return (math.cos(k*a)*math.sin(mass*a),math.sin(k*a)*math.sin(mass*a),math.sin(k*a)*math.cos(mass*a))


def pauli_vector(v):
    return w.add(w.add(w.scale(v[0],w.X),w.scale(v[1],w.Y)),w.scale(v[2],w.Z))


def walk_covariance(k,mass,a):
    v=walk_vector(k,mass,a)
    length=math.sqrt(sum(x*x for x in v))
    return w.scale(.5,w.add(w.I,w.scale(-1/length,pauli_vector(v))))


def effective_hamiltonian(k,mass,a):
    v=walk_vector(k,mass,a)
    length=math.sqrt(sum(x*x for x in v))
    return w.scale(w.quasienergy(k,mass,a)/length,pauli_vector(v))


def common_covariance(k,mass,a):
    # Empty outside the embedded lattice zone: a comparison-state convention.
    walk_vector(k,mass,a)
    return walk_covariance(k,mass,a) if -math.pi/a<=k<math.pi/a else w.scale(0,w.I)


def projector_bound(cutoff,mass,a):
    positive_mass(mass)
    w.parameters(cutoff,mass,a)
    if cutoff<0 or cutoff>=math.pi/a or mass*a>=math.pi/2:
        raise ValueError('Interior cutoff and gapped branch required')
    k=cutoff
    b=a*k*mass+a*a*(mass*k*k/2+mass**3/6+k*mass*mass/2+k**3/6)
    return min(1,b/mass)


def inner(f,g):
    return sum(complex(x).conjugate()*y for x,y in zip(f,g))


def pairing(c,f,g):
    """omega(a^dagger(f) a(g)) = <g, C f>."""
    return inner(g,car.apply(c,f))


def normal_expectation(c,creations,annihilations):
    """Creations f1..fr followed by annihilations gr..g1 (Wick determinant)."""
    if len(creations)!=len(annihilations):
        return 0j
    n=len(creations)
    matrix=tuple(tuple(pairing(c,f,g) for f in creations) for g in annihilations)
    return car.minor_determinant(matrix,tuple(range(n)),tuple(range(n)))


def occupied_spinor(c):
    j=max(range(2),key=lambda i:c[i][i].real)
    return tuple(c[i][j]/math.sqrt(c[j][j].real) for i in range(2))


def slater_state(c):
    v=occupied_spinor(c)
    return (0j,v[0],v[1],0j)


def expectation(op,state):
    return sum(state[i].conjugate()*value*state[j] for (i,j),value in op.items())


def second_quantized(h):
    n=len(h)
    result={}
    for i in range(n):
        for j in range(n):
            result=car.add(result,car.scale(h[i][j],car.mul(car.adjoint(car.annihilator(n,i)),car.annihilator(n,j))))
    return result


def renormalized_generator(k,mass):
    positive_mass(mass)
    energy=math.hypot(k,mass)
    return car.add(second_quantized(w.hamiltonian(k,mass)),car.scale(energy,car.identity(4)))


def density_pair(c,f,g):
    return pairing(c,f,f)*pairing(c,g,g)+pairing(c,f,g)*(inner(f,g)-pairing(c,g,f))


def cutoff_energy_density(cutoff,mass):
    """Continuum filled-sea energy per length before subtraction, symmetric cutoff."""
    positive_mass(mass)
    if not math.isfinite(cutoff) or cutoff<0:
        raise ValueError('Nonnegative finite momentum cutoff required')
    return -(cutoff*math.hypot(cutoff,mass)+mass*mass*math.asinh(cutoff/mass))/(2*math.pi)
