"""Scaled two-component walk and a restricted Dirac limit.

Different model from the CNOT spin chain: one-particle Hilbert space is
l2(Z) tensor C2, not the tensor product of one qubit at every site.
Numerical checks use floating-point tolerances; analytic bounds are in REPORT.md.
Units: lattice spacing = time step a, c = hbar = 1.
"""
import cmath
import math

I=((1+0j,0j),(0j,1+0j))
X=((0j,1+0j),(1+0j,0j))
Y=((0j,-1j),(1j,0j))
Z=((1+0j,0j),(0j,-1+0j))


def add(a,b):
    return tuple(tuple(a[i][j]+b[i][j] for j in range(2)) for i in range(2))


def scale(c,a):
    return tuple(tuple(c*a[i][j] for j in range(2)) for i in range(2))


def mul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def adjoint(a):
    return tuple(tuple(a[j][i].conjugate() for j in range(2)) for i in range(2))


def apply(a,v):
    return tuple(sum(a[i][j]*v[j] for j in range(2)) for i in range(2))


def norm(a):
    # Exact formula for largest singular value of a 2x2 matrix; float evaluation.
    h=mul(adjoint(a),a)
    discriminant=(h[0][0].real-h[1][1].real)**2+4*abs(h[0][1])**2
    largest=(h[0][0].real+h[1][1].real+math.sqrt(max(0,discriminant)))/2
    return math.sqrt(max(0,largest))


def distance(a,b):
    return norm(add(a,scale(-1,b)))


def power(a,n):
    if not isinstance(n,int) or n<0:
        raise ValueError('Nonnegative integer power required')
    result=I
    while n:
        if n%2:
            result=mul(result,a)
        a=mul(a,a)
        n//=2
    return result


def parameters(k,m,a):
    if not all(math.isfinite(v) for v in (k,m,a)) or a<=0:
        raise ValueError('Finite parameters and positive step required')


def coin(m,a):
    parameters(0,m,a)
    return add(scale(math.cos(m*a),I),scale(-1j*math.sin(m*a),X))


def shift(k,a):
    parameters(k,0,a)
    return ((cmath.exp(-1j*k*a),0j),(0j,cmath.exp(1j*k*a)))


def walk(k,m,a):
    parameters(k,m,a)
    return mul(shift(k,a),coin(m,a))


def hamiltonian(k,m):
    if not all(math.isfinite(v) for v in (k,m)):
        raise ValueError('Finite momentum and mass required')
    return add(scale(k,Z),scale(m,X))


def dirac(k,m,time):
    if not all(math.isfinite(v) for v in (k,m,time)):
        raise ValueError('Finite parameters required')
    energy=math.hypot(k,m)
    if energy==0:
        return I
    return add(scale(math.cos(energy*time),I),scale(-1j*math.sin(energy*time)/energy,hamiltonian(k,m)))


def one_step_bound(k,m,a):
    parameters(k,m,a)
    return a*a*abs(k*m)


def n_step_bound(k,m,a,n):
    if not isinstance(n,int) or n<0:
        raise ValueError('Nonnegative integer horizon required')
    return n*one_step_bound(k,m,a)


def quasienergy(k,m,a):
    parameters(k,m,a)
    # atan2 avoids cancellation in acos near zero.
    ka,ma=k*a,m*a
    cosine=math.cos(ka)*math.cos(ma)
    sine_magnitude=math.sqrt(math.sin(ma)**2+math.sin(ka)**2*math.cos(ma)**2)
    return math.atan2(sine_magnitude,cosine)/a


def real_step(amplitudes,m,a):
    c=coin(m,a)
    result={}
    for site,spinor in amplitudes.items():
        if not isinstance(site,int):
            raise ValueError('Integer lattice site required')
        rotated=apply(c,spinor)
        for target,component,value in ((site+1,0,rotated[0]),(site-1,1,rotated[1])):
            current=list(result.get(target,(0j,0j)))
            current[component]+=value
            result[target]=tuple(current)
    return {site:spinor for site,spinor in result.items() if any(v!=0 for v in spinor)}


def real_evolve(amplitudes,m,a,n):
    if not isinstance(n,int) or n<0:
        raise ValueError('Nonnegative integer horizon required')
    result=amplitudes
    for _ in range(n):
        result=real_step(result,m,a)
    return result


def norm_squared(amplitudes):
    return sum(abs(v)**2 for spinor in amplitudes.values() for v in spinor)


def fourier_sample(amplitudes,k,a):
    parameters(k,0,a)
    factor=math.sqrt(a/(2*math.pi))
    return tuple(factor*sum(spinor[i]*cmath.exp(-1j*k*a*site) for site,spinor in amplitudes.items()) for i in range(2))


def spin_expectation(spinor,observable):
    out=apply(observable,spinor)
    return sum(v.conjugate()*w for v,w in zip(spinor,out)).real


GAMMA0=X
GAMMA1=scale(-1j,Y)


def boost_spin(rapidity):
    return ((complex(math.exp(-rapidity/2)),0j),(0j,complex(math.exp(rapidity/2))))


def boost_momentum(k,m,rapidity):
    energy=math.hypot(k,m)
    c,s=math.cosh(rapidity),math.sinh(rapidity)
    return c*energy-s*k,c*k-s*energy
