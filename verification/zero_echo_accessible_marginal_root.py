"""Local versus global physical marginal in the saved-J echo instrument.

The two incidence types and any type-sensitive reporter are hypotheses.
The four-dimensional matrices are Schmidt-coordinate representatives of
one recorded sign slice, not the full old-system/clock Hilbert space.
"""
import sympy as sp


def saved_memory_density():
    return sp.diag(sp.Rational(3,4),sp.Rational(1,4))


def local_blocks():
    """Equal total type weights, but different conditional saved-J weights."""
    return (sp.diag(sp.Rational(7,16),sp.Rational(1,16)),
            sp.diag(sp.Rational(5,16),sp.Rational(3,16)))


def product_local_blocks():
    rho=saved_memory_density()
    return rho/2,rho/2


def recorded_pure():
    v=sp.Matrix([sp.sqrt(3)/2,0,0,sp.Rational(1,2)])
    return v*v.T


def global_correlated_blocks():
    return (sp.diag(sp.Rational(7,16),0,0,sp.Rational(1,16)),
            sp.diag(sp.Rational(5,16),0,0,sp.Rational(3,16)))


def partial_trace_environment(rho):
    if rho.shape!=(4,4):raise ValueError('expected two qubit Schmidt coordinates')
    return sp.Matrix(2,2,lambda i,j:sum(rho[2*i+k,2*j+k] for k in (0,1)))


def cq_tagged(local_blocks):
    return sp.diag(*local_blocks)


def coherent_witness():
    c=sp.zeros(4);c[0,3]=c[3,0]=1
    return c
