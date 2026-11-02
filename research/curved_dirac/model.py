"""Conformal curved-background Dirac diagnostics; no empirical gravity claim.

A global smooth static example is Omega(x)=1+epsilon*cos(q*x). Finite Fourier
Galerkin checks are NOT local nets or proofs of vacuum-cutoff convergence.
"""
import cmath
import importlib.util
import math
from pathlib import Path

_spec=importlib.util.spec_from_file_location('local_scaling_reference',Path(__file__).resolve().parents[1]/'local_scaling'/'model.py')
local=importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(local)
w,car,vac=local.w,local.car,local.vac


def parameters(epsilon,q):
    if not math.isfinite(epsilon) or abs(epsilon)>=1 or not math.isfinite(q) or q<=0:
        raise ValueError('Require |epsilon|<1 and positive finite frequency')


def omega(x,epsilon=.2,q=1.):
    parameters(epsilon,q)
    return 1+epsilon*math.cos(q*x)


def omega_x(x,epsilon=.2,q=1.):
    parameters(epsilon,q)
    return -epsilon*q*math.sin(q*x)


def curvature(x,epsilon=.2,q=1.):
    om=omega(x,epsilon,q); first=omega_x(x,epsilon,q)
    second=-epsilon*q*q*math.cos(q*x)
    return 2*(om*second-first*first)/om**4


def sinc(x):
    return math.sin(x)/x if x else 1.


def volume(u0,u1,v0,v1,epsilon=.2,q=1.):
    parameters(epsilon,q)
    if not u0<u1 or not v0<v1:
        raise ValueError('Nonempty null rectangle required')
    du,dv=u1-u0,v1-v0
    center=(u0+u1-v0-v1)/2
    def average(c):
        return math.cos(c*center)*sinc(c*du/2)*sinc(c*dv/2)
    return .5*du*dv*(1+epsilon**2/2+2*epsilon*average(q/2)+epsilon**2/2*average(q))


def physical_rhs(psi,psi_x,mass,om,sigma_x,sigma_t=0.):
    """i partial_t psi, using the contracted conformal spin connection."""
    derivative=w.apply(w.Z,psi_x)
    zpsi=w.apply(w.Z,psi); xpsi=w.apply(w.X,psi)
    return tuple(-1j*derivative[i]-.5j*sigma_x*zpsi[i]-.5j*sigma_t*psi[i]+mass*om*xpsi[i] for i in range(2))


def rescaled_rhs(chi,chi_x,mass,om):
    derivative=w.apply(w.Z,chi_x); xchi=w.apply(w.X,chi)
    return tuple(-1j*derivative[i]+mass*om*xchi[i] for i in range(2))


def variable_step(amplitudes,mass,a,epsilon=.2,q=1.,inverse=False):
    parameters(epsilon,q); local.spacing(a)
    if inverse:
        shifted={}
        for j,f in amplitudes.items():
            for target,r in ((j-1,0),(j+1,1)):
                shifted.setdefault(target,[0j,0j])[r]+=f[r]
        result={j:w.apply(w.adjoint(w.coin(mass*omega(j*a,epsilon,q),a)),f) for j,f in shifted.items()}
    else:
        result={}
        for j,f in amplitudes.items():
            rotated=w.apply(w.coin(mass*omega(j*a,epsilon,q),a),f)
            for target,r in ((j+1,0),(j-1,1)):
                result.setdefault(target,[0j,0j])[r]+=rotated[r]
        result={j:tuple(f) for j,f in result.items()}
    return {j:tuple(f) for j,f in result.items() if any(x!=0 for x in f)}


def evolve(amplitudes,mass,a,steps,epsilon=.2,q=1.):
    if not isinstance(steps,int):
        raise ValueError('Integer step count required')
    result=amplitudes
    for _ in range(abs(steps)):
        result=variable_step(result,mass,a,epsilon,q,inverse=steps<0)
    return result


def galerkin(cutoff,mass=.7,epsilon=.2,q=1.):
    """Periodic circle, momenta k=q*ell; hard Galerkin cutoff, no wrap coupling."""
    parameters(epsilon,q)
    if not isinstance(cutoff,int) or not 0<=cutoff<=5 or not math.isfinite(mass) or mass<=0:
        raise ValueError('Small nonnegative cutoff and positive finite mass required')
    modes=tuple(range(-cutoff,cutoff+1)); d=2*len(modes)
    h=[[0.]*d for _ in range(d)]
    for i,k in enumerate(modes):
        h[2*i][2*i]=q*k; h[2*i+1][2*i+1]=-q*k
        for j,l in enumerate(modes):
            value=mass if k==l else mass*epsilon/2 if abs(k-l)==1 else 0.
            h[2*i][2*j+1]=value; h[2*i+1][2*j]=value
    return tuple(tuple(row) for row in h)


def symmetric_eigensystem(matrix,tolerance=1e-13):
    """Small real symmetric Jacobi solver, with residual checked independently."""
    n=len(matrix)
    if n<2 or any(len(row)!=n for row in matrix) or any(abs(matrix[i][j]-matrix[j][i])>tolerance for i in range(n) for j in range(n)):
        raise ValueError('Real symmetric square matrix required')
    a=[list(map(float,row)) for row in matrix]
    vectors=[[float(i==j) for j in range(n)] for i in range(n)]
    for _ in range(100*n*n):
        p,q=max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda pair:abs(a[pair[0]][pair[1]]))
        if abs(a[p][q])<tolerance:
            break
        tau=(a[q][q]-a[p][p])/(2*a[p][q])
        t=(1 if tau>=0 else -1)/(abs(tau)+math.sqrt(1+tau*tau))
        cs=1/math.sqrt(1+t*t); sn=t*cs; off=a[p][q]
        a[p][p]-=t*off; a[q][q]+=t*off; a[p][q]=a[q][p]=0.
        for r in range(n):
            if r not in (p,q):
                x,y=a[r][p],a[r][q]
                a[r][p]=a[p][r]=cs*x-sn*y
                a[r][q]=a[q][r]=sn*x+cs*y
            x,y=vectors[r][p],vectors[r][q]
            vectors[r][p]=cs*x-sn*y; vectors[r][q]=sn*x+cs*y
    else:
        raise ArithmeticError('Jacobi solver did not converge')
    order=sorted(range(n),key=lambda i:a[i][i])
    return tuple(a[i][i] for i in order),tuple(tuple(vectors[r][i] for i in order) for r in range(n))


def negative_projection(eigenvalues,vectors):
    return tuple(tuple(sum(vectors[i][k]*vectors[j][k] for k,e in enumerate(eigenvalues) if e<0) for j in range(len(eigenvalues))) for i in range(len(eigenvalues)))


def spectral_propagator(eigenvalues,vectors,time):
    return tuple(tuple(sum(vectors[i][k]*cmath.exp(-1j*time*e)*vectors[j][k] for k,e in enumerate(eigenvalues)) for j in range(len(eigenvalues))) for i in range(len(eigenvalues)))


def frobenius_distance(a,b):
    return math.sqrt(sum(abs(x-y)**2 for ra,rb in zip(a,b) for x,y in zip(ra,rb)))
