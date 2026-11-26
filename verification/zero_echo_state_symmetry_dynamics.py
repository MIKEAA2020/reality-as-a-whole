"""Distinguish symmetry of one echo state from symmetry of its dynamics.

Finite relational-bin Hamiltonians are candidate operators, not established
physical time evolution, energy, subject incidence or lived experience.
"""
import sympy as sp


def free_q():
    return sp.Matrix([[-3,3,0,0],[3,-7,4,0],[0,4,-7,3],[0,0,3,-3]])


def swap():
    return sp.Matrix([[0,1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]])


def projector_plus():
    return (sp.eye(4)+swap())/2


def invariant_history_constraints():
    """First three constraints suffice for the full R-even Q-cyclic space."""
    q=free_q();r=swap()
    return sp.Matrix.vstack(*[(r-sp.eye(4))*q**k for k in range(3)])


def spectral_projector(q,lam,eigenvalues):
    p=sp.eye(q.rows)
    for mu in eigenvalues:
        if mu!=lam:p=p*(q-mu*sp.eye(q.rows))/(lam-mu)
    return p


def odd_transition_amplitude(t):
    """Amplitude <w|exp(-i(-Q)t)|v> for normalized even v and odd w."""
    q=free_q();v=sp.Matrix([1,1,0,0])/sp.sqrt(2)
    w=sp.Matrix([1,-1,0,0])/sp.sqrt(2)
    eigenvalues=(0,-2,-6,-12)
    return sp.simplify(sum((w.T*spectral_projector(q,lam,eigenvalues)*v)[0]
                           *sp.exp(sp.I*lam*t) for lam in eigenvalues))


def stationary_invariant_density(p):
    """All scalar-bin densities commuting with both Q and R, 0 <= p <= 1."""
    u=sp.ones(4,1)/2;ground=u*u.T
    return p*ground+(1-p)*(sp.eye(4)-ground)/3
