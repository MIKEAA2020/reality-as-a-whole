"""Finite CAR/Fock lift of the scaled walk, with explicit convention checks.

Sparse matrices are dicts (row,column)->complex on occupation-number bases.
Finite floating-point checks complement analytic CAR and continuum arguments.
"""
import cmath
from functools import lru_cache
import importlib.util
from itertools import permutations
import math
from pathlib import Path

_spec=importlib.util.spec_from_file_location('continuum_scaling_reference',Path(__file__).resolve().parents[1]/'continuum_scaling'/'model.py')
walk_model=importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(walk_model)


def cleaned(a):
    return {key:complex(value) for key,value in a.items() if value!=0}


def identity(dimension):
    return {(i,i):1+0j for i in range(dimension)}


def add(a,b):
    result=dict(a)
    for key,value in b.items():
        result[key]=result.get(key,0j)+value
    return cleaned(result)


def scale(value,a):
    return cleaned({key:value*x for key,x in a.items()})


def adjoint(a):
    return {(j,i):v.conjugate() for (i,j),v in a.items()}


def mul(a,b):
    rows={}
    for (i,j),v in b.items():
        rows.setdefault(i,[]).append((j,v))
    result={}
    for (i,k),v in a.items():
        for j,w in rows.get(k,()):
            result[i,j]=result.get((i,j),0j)+v*w
    return cleaned(result)


def error(a,b):
    difference=add(a,scale(-1,b))
    # Frobenius norm is an upper bound on operator norm; not a spectral estimate.
    return math.sqrt(sum(abs(v)**2 for v in difference.values()))


def trace(a):
    return sum(v for (i,j),v in a.items() if i==j)


def annihilator(modes,mode):
    if not isinstance(modes,int) or not 1<=modes<=12 or mode not in range(modes):
        raise ValueError('Small positive mode count and valid mode required')
    result={}
    bit=1<<mode
    for state in range(1<<modes):
        if state&bit:
            parity=(state&(bit-1)).bit_count()%2
            result[state^bit,state]=complex((-1)**parity)
    return result


def field(f):
    """a(f) = sum conjugate(f_i) c_i: antilinear in its smear."""
    result={}
    for i,v in enumerate(f):
        result=add(result,scale(complex(v).conjugate(),annihilator(len(f),i)))
    return result


def number(modes,mode):
    c=annihilator(modes,mode)
    return mul(adjoint(c),c)


def number_total(modes):
    result={}
    for i in range(modes):
        result=add(result,number(modes,i))
    return result


def parity(modes):
    return {(i,i):complex((-1)**i.bit_count()) for i in range(1<<modes)}


def one_particle_walk(sites,mass,spacing):
    """Periodic finite ring; indices 2*j and 2*j+1 are the two components."""
    if not isinstance(sites,int) or sites<2:
        raise ValueError('At least two ring sites required')
    c=walk_model.coin(mass,spacing)
    n=2*sites
    result=[[0j]*n for _ in range(n)]
    for site in range(sites):
        for incoming in range(2):
            result[2*((site+1)%sites)][2*site+incoming]+=c[0][incoming]
            result[2*((site-1)%sites)+1][2*site+incoming]+=c[1][incoming]
    return tuple(tuple(row) for row in result)


def dense_mul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))) for i in range(len(a)))


def dense_adjoint(a):
    return tuple(tuple(a[j][i].conjugate() for j in range(len(a))) for i in range(len(a[0])))


def apply(a,f):
    return tuple(sum(a[i][j]*f[j] for j in range(len(f))) for i in range(len(a)))


@lru_cache(None)
def signed_permutations(n):
    return tuple((p,(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n)))
                 for p in permutations(range(n)))


def minor_determinant(u,rows,columns):
    if not rows:
        return 1+0j
    return sum(sign*math.prod(u[rows[i]][columns[p[i]]] for i in range(len(rows)))
               for p,sign in signed_permutations(len(rows)))


def fock_lift(u):
    """Gamma(U) = direct sum of exterior powers; vacuum determinant is one."""
    n=len(u)
    if not 1<=n<=6 or any(len(row)!=n for row in u):
        raise ValueError('Square one-particle matrix with at most six modes required')
    occupations=[tuple(i for i in range(n) if state&(1<<i)) for state in range(1<<n)]
    result={}
    for row,occupied_out in enumerate(occupations):
        for column,occupied_in in enumerate(occupations):
            if len(occupied_out)==len(occupied_in):
                value=minor_determinant(u,occupied_out,occupied_in)
                if value!=0:
                    result[row,column]=complex(value)
    return result


def lifted_generator(u,mode):
    """Gamma(U)^dagger c_i Gamma(U) = sum_j U_ij c_j."""
    result={}
    for j,value in enumerate(u[mode]):
        result=add(result,scale(value,annihilator(len(u),j)))
    return result


def pullback(gamma,op):
    return mul(mul(adjoint(gamma),op),gamma)


def mode_support(u,output_mode):
    # Entries from this walk are exact zero or finite nonzero trig expressions.
    return frozenset(j for j,v in enumerate(u[output_mode]) if v!=0)


def norm_vector(f):
    return math.sqrt(sum(abs(v)**2 for v in f))


def vacuum_expectation(op):
    return op.get((0,0),0j)


def one_mode_density(f):
    a=field(f)
    return mul(adjoint(a),a)


def common_space_unitary(momentum,mass,spacing,steps):
    """Technical common-Hilbert-space extension: identity outside the zone.

    Other block-unitary choices on the discarded tail give the same fixed-vector
    limit. This extension is not an asserted physical UV law.
    """
    walk_model.parameters(momentum,mass,spacing)
    if not isinstance(steps,int) or steps<0:
        raise ValueError('Nonnegative integer horizon required')
    if -math.pi/spacing<=momentum<math.pi/spacing:
        return walk_model.power(walk_model.walk(momentum,mass,spacing),steps)
    return walk_model.I


def sampled_smear_error(momenta,spinors,mass,spacing,steps,cutoff):
    """Finite momentum-sample analogue of the analytic cutoff-tail estimate."""
    if len(momenta)!=len(spinors) or cutoff<0 or cutoff>=math.pi/spacing:
        raise ValueError('Matching samples and an interior nonnegative cutoff required')
    squared_error,low,tail=0,0,0
    for k,f in zip(momenta,spinors):
        lattice=walk_model.adjoint(common_space_unitary(k,mass,spacing,steps))
        continuum=walk_model.adjoint(walk_model.dirac(k,mass,spacing*steps))
        a,b=walk_model.apply(lattice,f),walk_model.apply(continuum,f)
        squared_error+=sum(abs(x-y)**2 for x,y in zip(a,b))
        if abs(k)<=cutoff:
            low+=sum(abs(x)**2 for x in f)
        else:
            tail+=sum(abs(x)**2 for x in f)
    delta=steps*spacing*spacing*cutoff*abs(mass)
    return math.sqrt(squared_error),delta*math.sqrt(low)+2*math.sqrt(tail)


def fourier_mode(sites,ell,spinor):
    return tuple(cmath.exp(2j*math.pi*ell*site/sites)*spinor[component]/math.sqrt(sites)
                 for site in range(sites) for component in range(2))
