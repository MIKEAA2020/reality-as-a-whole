"""Static curved Dirac Hamiltonian regulator: not the variable Floquet walk.

Central differences have ultraviolet doubling and continuous-time tails. The
infinite-line strong-resolvent/state proof is in REPORT.md; finite periodic
spectra here are diagnostics, not a replacement for that proof.
"""
from functools import lru_cache
import importlib.util
import math
from pathlib import Path

_spec=importlib.util.spec_from_file_location('curved_dirac_reference',Path(__file__).resolve().parents[1]/'curved_dirac'/'model.py')
curved=importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(curved)
w,car,vac,local=curved.w,curved.car,curved.vac,curved.local


def free_symbol(k,mass,a):
    w.parameters(k,mass,a)
    return w.add(w.scale(math.sin(k*a)/a,w.Z),w.scale(mass,w.X))


def lattice_hamiltonian(amplitudes,mass,a,epsilon=.2,q=1.):
    local.spacing(a); curved.parameters(epsilon,q)
    out={}
    for j,f in amplitudes.items():
        on=w.apply(w.scale(mass*curved.omega(j*a,epsilon,q),w.X),f)
        out=local.add_lattice(out,{j:on})
        z=w.apply(w.Z,f)
        out=local.add_lattice(out,{j-1:tuple(x/(2j*a) for x in z),j+1:tuple(-x/(2j*a) for x in z)})
    return out


def derivative_consistency(a,radius=.5,spinor=(1,.3j)):
    f=local.cell_average_blob(a,radius,spinor)
    actual=lattice_hamiltonian(f,0,a)
    expected={}
    for j in range(min(f)-1,max(f)+2):
        left,right=local.cell(j,a)
        integral=local.blob(right,radius)-local.blob(left,radius)
        expected[j]=tuple(-1j*integral*x/math.sqrt(a) for x in w.apply(w.Z,spinor))
    return math.sqrt(sum(abs(x-y)**2 for j in actual.keys()|expected.keys()
                         for x,y in zip(actual.get(j,(0,0)),expected.get(j,(0,0)))))


def ring_hamiltonian(sites,mass=.7,epsilon=.2,q=1.):
    curved.parameters(epsilon,q)
    if not isinstance(sites,int) or not 3<=sites<=25 or sites%2!=1 or mass<=0 or not math.isfinite(mass):
        raise ValueError('Odd diagnostic ring size 3..25 and positive finite mass required')
    modes=tuple(range(-(sites//2),sites//2+1)); a=2*math.pi/(q*sites)
    h=[[0.]* (2*sites) for _ in range(2*sites)]
    for i,k in enumerate(modes):
        p=math.sin(2*math.pi*k/sites)/a
        h[2*i][2*i]=p; h[2*i+1][2*i+1]=-p
        for j,l in enumerate(modes):
            value=mass if k==l else mass*epsilon/2 if (k-l)%sites in (1,sites-1) else 0.
            h[2*i][2*j+1]=value; h[2*i+1][2*j]=value
    return tuple(tuple(row) for row in h)


def circle_galerkin(cutoff,mass=.7,epsilon=.2,q=1.):
    curved.parameters(epsilon,q)
    if not isinstance(cutoff,int) or not 1<=cutoff<=12:
        raise ValueError('Diagnostic cutoff 1..12 required')
    sites=2*cutoff+1; modes=range(-cutoff,cutoff+1)
    h=[[0.]*(2*sites) for _ in range(2*sites)]
    for i,k in enumerate(modes):
        h[2*i][2*i]=q*k; h[2*i+1][2*i+1]=-q*k
        for j,l in enumerate(modes):
            value=mass if k==l else mass*epsilon/2 if abs(k-l)==1 else 0.
            h[2*i][2*j+1]=value; h[2*i+1][2*j]=value
    return tuple(tuple(row) for row in h)


@lru_cache(None)
def spectral_data(sites,reference=False):
    h=circle_galerkin((sites-1)//2) if reference else ring_hamiltonian(sites)
    eigenvalues,vectors=curved.symmetric_eigensystem(h)
    p=curved.negative_projection(eigenvalues,vectors)
    return h,eigenvalues,vectors,p


def fixed_smear(sites,second=False):
    # Fixed coefficients supported in the same three low Fourier modes at every cut.
    cutoff=sites//2; out=[0j]*(2*sites)
    coefficients={-1:(.1j,.2),0:(1,.3j),1:(.2,-.1j)} if not second else {-1:(.3,.1j),0:(.4j,.5),1:(-.2j,.1)}
    for k,f in coefficients.items():
        out[2*(k+cutoff):2*(k+cutoff)+2]=f
    return tuple(out)


def circle_errors(sites,reference_sites=19):
    _,_,_,p=spectral_data(sites)
    _,_,_,pr=spectral_data(reference_sites,True)
    f,g=fixed_smear(sites),fixed_smear(sites,True)
    fr,gr=fixed_smear(reference_sites),fixed_smear(reference_sites,True)
    # Compare the fixed low-mode projection of C f, not two unequal global matrices.
    pf,prf=car.apply(p,f),car.apply(pr,fr)
    low_error=math.sqrt(sum(abs(pf[2*(k+sites//2)+r]-prf[2*(k+reference_sites//2)+r])**2 for k in (-1,0,1) for r in (0,1)))
    return low_error,abs(vac.pairing(p,f,g)-vac.pairing(pr,fr,gr)),abs(vac.density_pair(p,f,g)-vac.density_pair(pr,fr,gr))


def bessel_j(order,z,terms=60):
    if not isinstance(order,int) or order<0 or not math.isfinite(z):
        raise ValueError('Nonnegative order and finite argument required')
    return sum((-1)**k*(z/2)**(2*k+order)/(math.factorial(k)*math.factorial(k+order)) for k in range(terms))


def sign_integral_scalar(value,steps=400):
    if value==0 or steps<1:
        raise ValueError('Nonzero eigenvalue and positive quadrature count required')
    h=math.pi/(2*steps)
    # s=tan(theta): lambda/(lambda^2+s^2) ds.
    integral=sum(value/(value*value*math.cos((j+.5)*h)**2+math.sin((j+.5)*h)**2)*h for j in range(steps))
    return .5-integral/math.pi
