"""Time-independent support coupling in an altered positive-frequency constraint.

A stipulated global mode-coupling, not a local detector or durable record.
Includes a continuum analytic norm bound; finite spectra illustrate it.
"""
import math
import unittest
import numpy as np
from verification.zero_two_window_coherence_tomography_test import PAULI, packet_basis, root_data, make_model
from verification.zero_two_window_imperfect_support_flag_test import outside_modes

G=1.2
TAU=math.pi/(2*G)
E_BOUND=7.2/math.pi


def spectral_limits(h):
    return math.sqrt(6-2*h-E_BOUND), math.sqrt(49/6-2*h+E_BOUND)


def continuum_bound(g=G):
    a=min(spectral_limits(h)[0] for h in (0,1))
    if not 0<g<a: raise ValueError('no guaranteed positive root')
    c=max((spectral_limits(h)[1]-spectral_limits(h)[0])/2 for h in (0,1))
    tau=math.pi/(2*g)
    return tau, g*c*tau*tau/2


def propagate(H,t):
    ev,V=np.linalg.eigh(H)
    return (V*np.exp(1j*t*ev))@V.conj().T


def system(n,h,g=G):
    model=make_model(n);B=packet_basis(model);dim=B.shape[0]
    Q=np.eye(dim)-B@B.conj().T;P=np.eye(dim)-Q
    vals,V=root_data(model,h);O=(V*np.sqrt(vals))@V.conj().T
    H=np.kron(O,np.eye(2))+g*np.kron(Q,PAULI[1])
    return model,B,P,Q,O,H


def blocks(U):
    return U[0::2,0::2],U[1::2,0::2]


def q_upper(k,n,alpha=.05):
    if n<1 or not 0<=k<=n or not 0<alpha<1: raise ValueError('bad count')
    h=min(1.,k/n+math.sqrt(math.log(2/alpha)/(2*n)))
    z=-math.expm1(math.log(alpha/2)/n) if k==0 else 1.
    return min(h,z)


class AutonomousSupportDynamicsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=[system(24,h) for h in (0,1)]
        cls.U=[propagate(d[-1],TAU) for d in cls.data]

    def test_continuum_positive_root_and_universal_bound(self):
        tau,d=continuum_bound()
        self.assertAlmostEqual(tau,TAU)
        self.assertAlmostEqual(d,.8231765919039176,places=12)
        self.assertGreater(min(spectral_limits(h)[0] for h in (0,1))-G,.10)
        self.assertLess(d*d,.68)
        with self.assertRaises(ValueError):continuum_bound(1.4)
        for h,(_,B,P,Q,O,H) in enumerate(self.data):
            a,b=spectral_limits(h)
            self.assertGreaterEqual(np.linalg.eigvalsh(H)[0],a-G-1e-11)
            self.assertLess(np.linalg.norm(H-H.conj().T),1e-11)
            self.assertLess(np.linalg.norm(H@H-(H@H).conj().T),1e-11)

    def test_commutator_refinement_is_conditional_on_continuum_bound(self):
        for h,(_,B,P,Q,O,H) in enumerate(self.data):
            a,_=spectral_limits(h)
            ctheta=np.linalg.norm(Q@(O@O)@B,2)
            croot=np.linalg.norm(Q@O@B,2)
            self.assertLess(ctheta,.42)
            self.assertLessEqual(croot,ctheta/(2*a)+1e-12)
        # Finite-grid .42 is evidence, not a certified continuum inequality.
        a=min(spectral_limits(h)[0] for h in (0,1))
        conditional=math.pi**2*.42/(16*G*a)
        self.assertLess(conditional**2,.028)

    def test_finite_operator_error_and_cross_sector_coherences(self):
        _,d_global=continuum_bound()
        for h,(_,B,P,Q,O,H) in enumerate(self.data):
            U=self.U[h];M,J=blocks(U);comm=np.linalg.norm(Q@O@B,2)
            free=propagate(O,TAU)
            ideal=np.kron(free,np.eye(2))@(np.kron(P,np.eye(2))+1j*np.kron(Q,PAULI[1]))
            diff=np.linalg.norm(U-ideal,2)
            rhs=G*comm*TAU**2/2
            self.assertLessEqual(diff,rhs+1e-11)
            self.assertLessEqual(rhs,d_global+1e-12)
            self.assertLessEqual(np.linalg.norm(M@Q,2)**2,rhs**2+1e-11)
            self.assertLessEqual(np.linalg.norm(J@B,2)**2,rhs**2+1e-11)
            E=J.conj().T@J
            self.assertGreater(np.linalg.norm(B.conj().T@E@Q,2),.06)
            self.assertLess(np.linalg.norm(M.conj().T@M+E-np.eye(len(B))),1e-11)

    def test_worst_case_statistics_and_grid_refinement(self):
        for h,(_,B,P,Q,O,H) in enumerate(self.data):
            M,J=blocks(self.U[h]);miss=np.linalg.norm(M@Q,2)**2
            fp=np.linalg.norm(J@B,2)**2
            expected=((.0041686307,.0041686331),(.0058333580,.0058333648))[h]
            self.assertAlmostEqual(miss,expected[0],places=8)
            self.assertAlmostEqual(fp,expected[1],places=8)
            _,B40,P40,Q40,O40,H40=system(40,h)
            M40,J40=blocks(propagate(H40,TAU))
            self.assertLess(abs(np.linalg.norm(M40@Q40,2)**2-miss),1e-6)
            self.assertLess(abs(np.linalg.norm(J40@B40,2)**2-fp),1e-6)

    def test_flag_bound_with_coherent_leakage_and_shots(self):
        model,B,P,Q,O,H=self.data[0];x,_=outside_modes(model,B)
        psi=math.sqrt(.99)*B[:,0]+math.sqrt(.01)*x
        lam=np.linalg.norm(Q@psi)**2
        qs=[np.linalg.norm(blocks(U)[1]@psi)**2 for U in self.U]
        q=sum(qs)/2;_,d=continuum_bound()
        self.assertLessEqual(math.sqrt(lam),math.sqrt(q)+d)
        rng=np.random.default_rng(673);n=100000;k=rng.binomial(n,q)
        qu=q_upper(k,n);self.assertLessEqual(q,qu)
        lamu=min(1.,(math.sqrt(qu)+d)**2)
        self.assertGreaterEqual(lamu,lam)
        self.assertGreater(lamu,.8)  # universal certificate is not practically tight

    def test_bounded_hamiltonian_perturbation(self):
        _,B,P,Q,O,H=self.data[1];delta=.01
        pert=delta*np.kron(P,PAULI[0]); U1=propagate(H+pert,TAU)
        U0=self.U[1];self.assertLessEqual(np.linalg.norm(U1-U0,2),TAU*delta+1e-11)
        M,J=blocks(U1);comm=np.linalg.norm(Q@O@B,2)
        bound=G*comm*TAU**2/2+TAU*delta
        self.assertLessEqual(np.linalg.norm(M@Q,2)**2,bound**2+1e-11)
        self.assertLessEqual(np.linalg.norm(J@B,2)**2,bound**2+1e-11)
        self.assertGreater(np.linalg.eigvalsh(H+pert)[0],0.)

    def test_unstopped_flag_is_not_a_persistent_record(self):
        for h,(model,B,P,Q,O,H) in enumerate(self.data):
            x,_=outside_modes(model,B);J=blocks(self.U[h])[1]
            J2=blocks(propagate(H,2*TAU))[1]
            self.assertGreater(np.linalg.norm(J@x)**2,.999)
            self.assertLess(np.linalg.norm(J2@x)**2,.001)

if __name__=='__main__':unittest.main()
