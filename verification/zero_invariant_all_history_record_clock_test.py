"""All-history complementary-zero dynamics with a relational clock and record.

The initial state lies in the previously constructed zero kernel. The clock,
reference, memory, couplings, and signs are stipulated. Finite toy only; not
an ontology, experience, objective cosmic energy, or a spacetime-local model.
"""
import math
import unittest
import numpy as np
from functools import reduce
from verification.zero_energy_sphere_work_incidence_test import X,Y,Z,I,Jactive,full_state
from verification.zero_all_sector_sphere_clock_work_test import complement_state
from verification.zero_relational_orientation_reference_test import (
    C1,C2,C3,L,S,Qori,with_reference,apply16
)
from verification.zero_balanced_reference_preparation_test import (
    balanced_seed,complement_base,clock_read
)
from verification.zero_dual_pair_sphere_energy_instrument_test import dual_output
from verification.zero_constitution_hamiltonian_phase_gate_test import J16,X16,Z16,P16
from verification.zero_reciprocal_subject_exchange_test import n


def kron(*a):return reduce(np.kron,a)

I16=np.eye(16,dtype=complex)
I32=np.eye(32,dtype=complex)
# Active encoded lab interface ordered (R,W,T,F); M is added last.
XL=kron(X,Jactive,X,I)
ZL=kron(Z,I,I,I)
OMEGA=.5
G=1.
NU=math.sqrt(OMEGA**2+G**2)
H=OMEGA*np.kron(XL,I)+G*np.kron(ZL,Y)
PPLUS=(I32+H/NU)/2
PMINUS=(I32-H/NU)/2
W=np.vstack([PPLUS,PMINUS])
CC=np.kron(I,H)-np.kron(NU*Z,I32)
HAD=np.array([[1,1],[1,-1]],complex)/math.sqrt(2)


def attach_memory(v):
    return np.stack((v,np.zeros_like(v)),axis=-1)


def apply32(op,v):
    assert v.shape[-5:]==(2,2,2,2,2)
    return np.einsum('xy,...y->...x',op,v.reshape(v.shape[:-5]+(32,)),optimize=True).reshape(v.shape)


def evolve(v,theta,omega=OMEGA,g=G):
    nu=math.sqrt(omega**2+g**2)
    hh=omega*np.kron(XL,I)+g*np.kron(ZL,Y)
    return math.cos(theta)*v-1j*math.sin(theta)/nu*apply32(hh,v)


def record_table(v):
    # R is axis 8; the final axis is the added memory M. Read M in X.
    x=np.einsum('mn,...n->...m',HAD,v,optimize=True)
    return np.sum(abs(x)**2,axis=(0,1,2,3,4,5,6,7,9,10,11))


def bob_record_table(v):
    # Bob's original pointer j stays fixed; R may subsequently change.
    return np.sum(abs(v)**2,axis=(0,1,2,3,4,5,6,9,10,11,12))


def information(tab):
    p=tab.sum(axis=1);q=tab.sum(axis=0)
    return float(sum(x*math.log2(x/(p[i]*q[j])) for (i,j),x in np.ndenumerate(tab) if x>1e-15))


class InvariantAllHistoryRecordClockTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.refstates=(with_reference(full_state(4)),with_reference(complement_state(4)))
        cls.initial=[attach_memory(x) for x in cls.refstates]

    def test_logical_paulis_preserve_all_complementary_zero_operators(self):
        np.testing.assert_allclose(XL@XL,I16,atol=1e-14)
        np.testing.assert_allclose(ZL@ZL,I16,atol=1e-14)
        np.testing.assert_allclose(XL@ZL,-ZL@XL,atol=1e-14)
        for q in (C1,C2,C3,L,S,Qori):
            for op in (XL,ZL):np.testing.assert_allclose(op@q,q@op,atol=1e-14)
            np.testing.assert_allclose(H@np.kron(q,I),np.kron(q,I)@H,atol=1e-14)
        np.testing.assert_allclose(H@H,NU**2*I32,atol=1e-14)
        # The logical X flips R and T and acts on W. R is no longer
        # necessarily equal to Bob's original copied pointer afterwards.

    def test_physical_full_work_and_record_encodings_preserve_charges(self):
        i16=np.eye(16,dtype=complex)
        XLp=kron(X,J16,X,I)
        ZLp=kron(Z,i16,I,I)
        hp=OMEGA*np.kron(XLp,I)+G*np.kron(ZLp,Y)
        p=kron(I,P16,I,I)
        qf=kron(I,J16,I,I)+kron(I,i16,I,Z)
        c1=-kron(Z,X16,X,I)-kron(I,P16,I,X)
        c2=-kron(Z,Z16,X,I)-kron(I,P16,I,Y)
        c3=kron(I,J16,I,I)+kron(I,P16,I,Z)
        ell=kron(Z,J16,Z,I)
        for op in (p,qf,c1,c2,c3,ell):
            np.testing.assert_allclose(hp@np.kron(op,I),np.kron(op,I)@hp,atol=1e-14)
        nums=np.asarray(n,complex)
        for inds in ((0,1,2,3),(0,1),(2,3),(0,2),(1,3)):
            op=kron(I,sum(nums[k] for k in inds),I,I,I)
            np.testing.assert_allclose(hp@op,op@hp,atol=1e-14)
        # R is physically encoded as |01>,|10>. Swap extends X_R while
        # preserving its pair number on all four R states.
        swap=np.eye(4,dtype=complex);swap[1,1]=swap[2,2]=0;swap[1,2]=swap[2,1]=1
        np.testing.assert_allclose(swap[np.ix_([1,2],[1,2])],X,atol=1e-14)
        np.testing.assert_allclose(swap@np.diag([0,1,1,2]),np.diag([0,1,1,2])@swap,atol=1e-14)
        # The lab/old clock factors are untouched; memory and new reference
        # clock are assigned zero old energy, not derived from gravity.

    def test_stationary_clock_isometry_preserves_the_full_zero_kernel(self):
        np.testing.assert_allclose(W.conj().T@W,I32,atol=1e-14)
        np.testing.assert_allclose(CC@W,0,atol=1e-14)
        for q in (C1,C2,C3,L,S,Qori):
            sys=np.kron(q,I)
            np.testing.assert_allclose(np.kron(I,sys)@W,W@sys,atol=1e-14)
        for theta in (0,.3,math.pi/4,math.pi/2):
            bra=np.array([np.exp(-1j*theta),np.exp(1j*theta)])/math.sqrt(2)
            relative=np.kron(bra.reshape(1,2),I32)@W
            expected=(math.cos(theta)*I32-1j*math.sin(theta)*H/NU)/math.sqrt(2)
            np.testing.assert_allclose(relative,expected,atol=1e-14)
        # Full phase θ∈[0,π) has POVM density 2|θ><θ|/π and uniform
        # outcome density 1/π in the stationary state.

    def test_every_sector_and_prior_clock_label_remains_in_zero_kernel(self):
        for state in self.initial:
            for theta in (0,math.pi/4,math.pi/2):
                v=evolve(state,theta)
                self.assertAlmostEqual(np.linalg.norm(v),1,places=12)
                for q in (C1,C2,C3,Qori):
                    self.assertLess(np.linalg.norm(apply32(np.kron(q,I),v)),1e-12)
                np.testing.assert_allclose(apply32(np.kron(L,I),v),v,atol=2e-14)
                np.testing.assert_allclose(apply32(np.kron(S,I),v),v,atol=2e-14)
        # The old clock instrument commutes with the new dynamics. Check
        # every one of its 16 retained branches for both physical sectors.
        for ref in self.refstates:
            for branch in clock_read(ref):
                v=evolve(attach_memory(branch),math.pi/4)
                self.assertLess(np.linalg.norm(apply32(np.kron(C1,I),v)),1e-12)
                self.assertLess(np.linalg.norm(apply32(np.kron(C2,I),v)),1e-12)
                self.assertLess(np.linalg.norm(apply32(np.kron(C3,I),v)),1e-12)
                np.testing.assert_allclose(apply32(np.kron(L,I),v),v,atol=2e-14)

    def test_actual_record_motion_and_pointer_information_are_nontrivial(self):
        for init in self.initial:
            v=evolve(init,math.pi/4)
            corr=G/NU
            table=np.array([[(1+corr)/4,(1-corr)/4],
                            [(1-corr)/4,(1+corr)/4]])
            np.testing.assert_allclose(record_table(v),table,atol=1e-13)
            self.assertAlmostEqual(information(table),.7018824866054363,places=12)
            jb=bob_record_table(v)
            np.testing.assert_allclose(jb,[[.45,.05],[.05,.45]],atol=1e-13)
            self.assertAlmostEqual(jb[0,1]+jb[1,0],.1,places=12)
        # Mutual information and pointer disagreement are Born predictions;
        # they neither imply actual outcomes nor subject/experience identity.

    def test_finite_clock_window_and_unconditioned_cycle(self):
        delta=math.pi/8
        contrast=(G/NU)*math.sin(2*delta)/(2*delta)
        p=(1+contrast)/2
        self.assertAlmostEqual(p,.9026336968358963,places=12)
        table=np.array([[p/2,(1-p)/2],[(1-p)/2,p/2]])
        self.assertAlmostEqual(information(table),.5394090623048701,places=12)
        self.assertAlmostEqual(2*delta/math.pi,.25,places=13)
        # Verify actual finite states, not merely the analytic formula.
        nodes,weights=np.polynomial.legendre.leggauss(24)
        for init in self.initial:
            avg=sum(w*record_table(evolve(init,math.pi/4+delta*x))/2
                    for x,w in zip(nodes,weights))
            np.testing.assert_allclose(avg,table,atol=1e-13)
            np.testing.assert_allclose(record_table(evolve(init,math.pi/2)),np.ones((2,2))/4,atol=1e-13)
            np.testing.assert_allclose(evolve(init,math.pi),-init,atol=2e-14)
            unconditioned=sum(w*record_table(evolve(init,math.pi*(x+1)/2))/2
                              for x,w in zip(nodes,weights))
            np.testing.assert_allclose(unconditioned,np.ones((2,2))/4,atol=1e-13)
        # The finite periodic clock does not guarantee a permanent record;
        # discarding its phase removes this R–M_X correlation.

    def test_matched_controls_separate_copying_from_record_flips(self):
        for init in self.initial:
            still=evolve(init,math.pi/4,omega=0,g=1)
            np.testing.assert_allclose(bob_record_table(still),np.diag([.5,.5]),atol=1e-13)
            self.assertAlmostEqual(information(record_table(still)),1,places=12)
            no_copy=evolve(init,math.pi/4,omega=.5,g=0)
            np.testing.assert_allclose(record_table(no_copy),np.ones((2,2))/4,atol=1e-13)
            self.assertGreater(bob_record_table(no_copy)[0,1],.24)

    def test_zero_preserving_dynamics_cannot_repair_a_seed_outside_kernel(self):
        for base in (dual_output(4,4),complement_base()):
            seed=balanced_seed(base) # old unentangled W–F input
            init=attach_memory(seed)
            q=np.kron(C1,I)
            self.assertAlmostEqual(np.linalg.norm(apply32(q,init))**2,2,places=12)
            for theta in (.2,math.pi/4,math.pi/2):
                x=evolve(init,theta)
                self.assertAlmostEqual(np.linalg.norm(apply32(q,x))**2,2,places=12)
        # Since [H,C1]=0, a closed U generated by H cannot turn a nonzero
        # C1 norm into zero. Starting in the kernel remains an input.

if __name__=='__main__':
    unittest.main()
