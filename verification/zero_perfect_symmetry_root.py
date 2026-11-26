"""Conditional rotation-charge normalization on the sphere–echo candidate.

Exact algebra tests; physical energy, experiential quality and applicability
of the group/representation are not derived by these functions.
"""
import sympy as sp

I2=sp.eye(2)
SIGMA=(sp.Matrix([[0,1],[1,0]]),
       sp.Matrix([[0,-sp.I],[sp.I,0]]),
       sp.Matrix([[1,0],[0,-1]]))


def total_generators(n):
    """n spin-half generators for the honest SU(2) tensor representation."""
    if n<=0:raise ValueError('need at least one factor')
    result=[]
    for sigma in SIGMA:
        out=sp.zeros(2**n)
        for i in range(n):
            term=sp.Matrix([[1]])
            for j in range(n):term=sp.kronecker_product(term,sigma/2 if i==j else I2)
            out+=term
        result.append(out)
    return tuple(result)


def commutator(a,b):return a*b-b*a


def shifted_defects(generators,shifts):
    """Failure of exact Lie algebra under scalar changes of generators."""
    if len(generators)!=3 or len(shifts)!=3:raise ValueError('need triples')
    d=generators[0].rows
    shifted=tuple(g+c*sp.eye(d) for g,c in zip(generators,shifts))
    return tuple(sp.simplify(commutator(shifted[i],shifted[(i+1)%3])
                             -sp.I*shifted[(i+2)%3]) for i in range(3))


def local_generators_of_dot():
    """Common/individual rotations of the smooth u=m·n on R³×R³.

    These differential operators restrict to the two unit spheres.
    """
    m=sp.Matrix(sp.symbols('m_x m_y m_z',real=True))
    n=sp.Matrix(sp.symbols('n_x n_y n_z',real=True))
    u=(m.T*n)[0]
    l_m=-sp.I*m.cross(sp.Matrix([sp.diff(u,x) for x in m]))
    l_n=-sp.I*n.cross(sp.Matrix([sp.diff(u,x) for x in n]))
    return m,n,u,l_m,l_n


def state_projector(v):
    if not v or (v.conjugate().T*v)[0]==0:raise ValueError('need nonzero vector')
    return v*v.conjugate().T/(v.conjugate().T*v)[0]
