"""Quanta article: photon clock, coherent record, and dS horizon checks.

Optical states are ideal theoretical counterparts to the published apparatus,
not reconstructed experimental data or a model of a conscious observer.
"""
import math
import unittest
import numpy as np
from verification.zero_all_sector_noncommuting_sphere_test import I,X,Y,Z,kron


def pure(v):return np.outer(v,v.conj())
def reduced(a):return np.trace(a.reshape(2,2,2,2),axis1=0,axis2=2)


class QuantaPhotonHorizonTests(unittest.TestCase):
    def test_moreva_ideal_singlet_clock_and_two_conditional_readings(self):
        singlet=np.array([0,1,-1,0],complex)/np.sqrt(2);rho=pure(singlet)
        # Moreva et al. use h=i(|H><V|-|V><H|)=-Y, up to hbar omega.
        h=-Y;total=kron(h,I)+kron(I,h)
        np.testing.assert_allclose(total@singlet,0,atol=1e-14)
        np.testing.assert_allclose(reduced(rho),I/2,atol=1e-14)
        for theta in (0.,.17,.6,math.pi/4,math.pi/2):
            u=math.cos(theta)*I+1j*math.sin(theta)*Y
            np.testing.assert_allclose(kron(u,u)@singlet,singlet,atol=1e-14)
            clock=u@np.array([1.,0.]);system=u@np.array([0.,1.])
            conditional=kron(clock.conj().reshape(1,2),I)@singlet
            np.testing.assert_allclose(pure(conditional)/np.vdot(conditional,conditional),pure(system),atol=1e-14)
            self.assertAlmostEqual(abs(system[1])**2,math.cos(theta)**2,places=13)
        # Global invariance and different conditional states refer to the
        # same two-photon singlet. External apparatus controls still exist.

    def test_single_basis_correlation_does_not_witness_coherence(self):
        singlet=np.array([0,1,-1,0],complex)/np.sqrt(2);rho=pure(singlet)
        p=[(I+Z)/2,(I-Z)/2]
        dephased=sum(kron(a,I)@rho@kron(a,I) for a in p)
        for a,b in ((0,1),(1,0)):
            effect=kron(p[a],p[b])
            self.assertAlmostEqual(np.trace(rho@effect).real,.5,places=13)
            self.assertAlmostEqual(np.trace(dephased@effect).real,.5,places=13)
        # |+x> and |-x> outcome correlation distinguishes them, but needs
        # joint access and a separate measurement setting.
        px=[(I+X)/2,(I-X)/2]
        self.assertAlmostEqual(np.trace(rho@kron(px[0],px[1])).real,.5,places=13)
        self.assertAlmostEqual(np.trace(dephased@kron(px[0],px[1])).real,.25,places=13)
        self.assertAlmostEqual(np.trace(rho@(-kron(X,X))).real,1,places=13)
        self.assertAlmostEqual(np.trace(dephased@(-kron(X,X))).real,0,places=13)
        self.assertAlmostEqual(sum(abs(np.linalg.eigvalsh(rho-dephased)))/2,.5,places=13)
        # Important: retaining identical z statistics after clock pinching is
        # NOT the claim that the dephased pair remains stationary for the
        # original noninteracting Moreva Hamiltonian.
        total=-(kron(Y,I)+kron(I,Y))
        self.assertGreater(np.linalg.norm(total@dephased-dephased@total),1)

    def test_sign_record_coherence_can_be_recovered_with_pointer(self):
        singlet=np.array([0,1,-1,0],complex)/np.sqrt(2)
        initial=np.kron(singlet,np.array([1,0]));p0=(I+Z)/2;p1=(I-Z)/2
        copy=kron(p0,I,I)+kron(p1,I,X);out=copy@initial
        bare=-kron(X,X,I);dressed=-kron(X,X,X)
        self.assertAlmostEqual(np.vdot(out,bare@out).real,0,places=13)
        self.assertAlmostEqual(np.vdot(out,dressed@out).real,1,places=13)
        np.testing.assert_allclose(copy@out,initial,atol=1e-14)
        h=-(kron(Y,I,I)+kron(I,Y,I))
        self.assertGreater(np.linalg.norm(copy@h-h@copy),1)
        # Interaction is a proposed ideal record gate, not the optical
        # experiment's whole apparatus nor an automatically free operation.
        h_after=copy@h@copy.conj().T
        np.testing.assert_allclose(h_after@out,0,atol=1e-14)

    def test_known_entangled_and_separable_stationary_correlations(self):
        # A mixed, classically correlated 2-qubit state can be globally
        # stationary and yield different conditional clock states. The
        # specified H is not the photons' noninteracting Hamiltonian.
        rho=(pure(np.array([1,0,0,0]))+pure(np.array([0,0,0,1])))/2
        h=kron(Z,I)-kron(I,Z)
        np.testing.assert_allclose(h@rho-rho@h,0,atol=1e-14)
        p0=kron((I+Z)/2,I);p1=kron((I-Z)/2,I)
        s0=reduced(p0@rho@p0)*2;s1=reduced(p1@rho@p1)*2
        np.testing.assert_allclose(s0,(I+Z)/2,atol=1e-14)
        np.testing.assert_allclose(s1,(I-Z)/2,atol=1e-14)
        # In a fixed pure product state, every nonzero clock projection is
        # proportional to one and the same system vector. This contrasts
        # with the explicitly mixed two-qubit stationary example.
        c=np.array([1,1],complex)/np.sqrt(2);s=np.array([1,1j],complex)/np.sqrt(2)
        v=np.kron(c,s)
        for a in (np.array([1,0]),np.array([0,1])):
            part=kron(a.reshape(1,2),I)@v
            np.testing.assert_allclose(pure(part)/np.vdot(part,part),pure(s),atol=1e-14)

    def test_de_sitter_future_boundary_is_not_finite_time_horizon(self):
        # Flat slicing a=e^(H t), H>0. Future conformal boundary eta=0
        # is t=infinity; physical radius of event horizon remains 1/H.
        for H in (.4,1.,3.):
            for t in (0.,1.,10.):
                scale=math.exp(H*t);eta=-math.exp(-H*t)/H
                horizon_comoving=math.exp(-H*t)/H
                self.assertAlmostEqual(eta,-horizon_comoving,places=13)
                self.assertAlmostEqual(scale*horizon_comoving,1/H,places=13)
            # Static-patch radial null ray from r=0 to r=1/(2H) needs
            # ΔT=atanh(1/2)/H, irrespective of starting static time.
            travel=math.atanh(.5)/H
            self.assertGreater(travel,0)
            self.assertAlmostEqual(math.tanh(H*travel)/H,1/(2*H),places=13)
        # A test signal is not a guarantee of eternal observers or resources.

    def test_equal_entanglement_entropy_does_not_fix_correlations(self):
        # Fixed three-qubit factorization: GHZ ± have the same spectrum for
        # every nontrivial reduction but opposite X⊗X⊗X correlations.
        plus=np.zeros(8,complex);minus=plus.copy()
        plus[0]=plus[7]=1/np.sqrt(2);minus[0]=1/np.sqrt(2);minus[7]=-1/np.sqrt(2)
        for state in (plus,minus):
            for axis in range(3):
                matrix=np.moveaxis(state.reshape(2,2,2),axis,0).reshape(2,4)
                np.testing.assert_allclose(np.linalg.eigvalsh(matrix@matrix.conj().T),[.5,.5],atol=1e-14)
        xxx=kron(X,X,X)
        self.assertAlmostEqual(np.vdot(plus,xxx@plus).real,1,places=13)
        self.assertAlmostEqual(np.vdot(minus,xxx@minus).real,-1,places=13)
        # They are related by a local unitary: this does not show that their
        # emergent metrics differ or that entanglement is irrelevant.
        np.testing.assert_allclose(kron(Z,I,I)@plus,minus,atol=1e-14)

if __name__=='__main__':unittest.main()
