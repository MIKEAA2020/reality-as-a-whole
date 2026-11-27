"""Current-weight compatibility on the actual encoded autonomous history."""
import math
import unittest
import numpy as np
from scipy.integrate import quad
from verification.zero_autonomous_clock_record_subject_test import clock_state
from verification.zero_sector_record_energy_exchange_test import E, H0, records_state, unitary

I=np.eye(4,dtype=complex)
A=np.array([[int((j-i)%4 in (1,3)) for j in range(4)] for i in range(4)],complex)
P=np.diag([0,1,1,0]).astype(complex)
D=1j*(A@P-P@A)
LAMBDA=.5


def anti(a,b):return a@b+b@a


def weights(x):return (I+x)/2,(I-x)/2


def expect(v,op):return np.vdot(v,op@v).real


class CycleIncidencePartitionReview(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Actual 48-dimensional encoded pointer/memory/battery writer,
        # tensored with the two logical AB qubits of the prepared state.
        u=np.kron(np.eye(4),np.asarray(unitary(math.pi/2),complex))
        h0=np.kron(np.eye(4),np.asarray(H0,complex))
        cls.energies=[np.kron(np.eye(4),np.asarray(e,complex)) for e in E]
        cls.vs=[np.eye(192),u,u,np.eye(192)]
        cls.h0=h0
        phi=np.zeros(192,complex)
        for (a,b,r,m1,w1,m2,w2),amp in records_state(0).items():
            phi[(2*a+b)*48+r*16+m1*8+w1*4+m2*2+w2]=amp
        np.testing.assert_allclose(np.linalg.norm(phi),1,atol=1e-12)
        basis=np.zeros((4*192,4),complex)
        for t in range(4):basis[t*192:(t+1)*192,t]=cls.vs[t]@phi
        cls.basis=basis

    @classmethod
    def k(cls,v,dagger=False):
        a=v.reshape(4,192)
        return np.stack([(cls.vs[t].conj().T if dagger else cls.vs[t])@a[t]
                         for t in range(4)]).reshape(-1)

    @classmethod
    def h(cls,v):
        a=cls.k(v,True).reshape(4,192)
        return cls.k((A@a).reshape(-1))+np.stack([cls.h0@x for x in v.reshape(4,192)]).reshape(-1)

    @classmethod
    def energy(cls,v,j):
        return np.stack([cls.energies[j]@x for x in v.reshape(4,192)]).reshape(-1)

    @classmethod
    def current(cls,v,j):
        return 1j*(cls.h(cls.energy(v,j))-cls.energy(cls.h(v),j))

    @classmethod
    def weighted(cls,v,w):
        return cls.k((w@cls.k(v,True).reshape(4,192)).reshape(-1))

    def test_normalized_positive_complementary_effects_leave_nonzero_current(self):
        np.testing.assert_allclose(D@D,I,atol=1e-14)
        wm,wb=weights(LAMBDA*D)
        for w in (wm,wb):
            self.assertGreater(np.linalg.eigvalsh(w).min(),0)
            self.assertLess(np.linalg.eigvalsh(w).max(),1)
            np.testing.assert_allclose(w@D,D@w,atol=1e-14)
        np.testing.assert_allclose(wm+wb,I,atol=1e-14)
        for p in (3/5,7/8):
            jm=p*D;jb=-jm
            total=(anti(wm,jm)+anti(wb,jb))/2
            np.testing.assert_allclose(total,p*LAMBDA*I,atol=1e-14)
            for t in (0,.3,1.2,math.pi):
                self.assertAlmostEqual(expect(np.array(clock_state(t)),total),p*LAMBDA)

    def test_joint_povm_realizes_the_compressed_weighted_current(self):
        wm,wb=weights(LAMBDA*D)
        for p in (3/5,7/8):
            for t in (0,.2,.9,math.pi/2,math.pi):
                psi=np.array(clock_state(t));mean=0.
                for d in (-1,1):
                    proj=(I+d*D)/2
                    for sign,w in ((1,wm),(-1,wb)):
                        joint=proj@w
                        self.assertGreaterEqual(np.linalg.eigvalsh(joint).min(),-1e-14)
                        mean+=sign*p*d*expect(psi,joint)
                self.assertAlmostEqual(mean,LAMBDA*p,places=12)

    def test_weighted_product_rule_and_whole_cycle(self):
        wm,wb=weights(LAMBDA*D);p=3/5
        em=p*P;eb=I-em;jm=p*D;jb=-jm
        weighted_energy=(anti(wm,em)+anti(wb,eb))/2
        dwm=1j*(A@wm-wm@A);dwb=-dwm
        correction=(anti(dwm,em)+anti(dwb,eb))/2
        weighted_current=(anti(wm,jm)+anti(wb,jb))/2
        np.testing.assert_allclose(1j*(A@weighted_energy-weighted_energy@A),
                                   weighted_current+correction,atol=1e-13)
        integ=quad(lambda t:expect(np.array(clock_state(t)),correction),0,math.pi)[0]
        self.assertAlmostEqual(integ,-math.pi*LAMBDA*p,places=12)
        self.assertAlmostEqual(quad(lambda t:expect(np.array(clock_state(t)),weighted_current),
                                    0,math.pi)[0],math.pi*LAMBDA*p,places=12)
        self.assertAlmostEqual(expect(np.array(clock_state(0)),weighted_energy),
                               expect(np.array(clock_state(math.pi)),weighted_energy),places=12)

    def test_anticommutation_is_iff_for_normalized_pair(self):
        p=3/5
        # Different weights can cancel even without commuting with the current.
        x=.8*(2*P-I);wm,wb=weights(x);jm=p*D
        self.assertGreater(np.linalg.norm(wm@D-D@wm),.1)
        np.testing.assert_allclose(anti(x,jm),0,atol=1e-14)
        np.testing.assert_allclose((anti(wm,jm)+anti(wb,-jm))/2,0,atol=1e-14)
        # A sharp D measurement and this effect cannot be joint: its off-block
        # matrix is nonzero, so W is not block diagonal in D eigenspaces.
        plus,minus=weights(D)
        self.assertGreater(np.linalg.norm(plus@wm@minus),.1)

    def test_original_encoded_model_and_global_partition_compress_correctly(self):
        wm,wb=weights(LAMBDA*D);B=self.basis
        for j,p in ((0,3/5),(2,7/8)):
            cols=[];jmcols=[];jbcols=[]
            for k in range(4):
                v=B[:,k];jmv=self.current(v,j);jbv=self.current(v,j+1)
                jmcols.append(B.conj().T@jmv);jbcols.append(B.conj().T@jbv)
                contribution=(self.weighted(jmv,wm)+self.current(self.weighted(v,wm),j)
                              +self.weighted(jbv,wb)+self.current(self.weighted(v,wb),j+1))/2
                cols.append(B.conj().T@contribution)
            np.testing.assert_allclose(np.column_stack(jmcols),p*D,atol=2e-13)
            np.testing.assert_allclose(np.column_stack(jbcols),-p*D,atol=2e-13)
            np.testing.assert_allclose(np.column_stack(cols),p*LAMBDA*I,atol=2e-13)
        # The K-conjugated global effects are complementary on the full space.
        v=np.arange(4*192,dtype=float)+1j*np.arange(4*192,dtype=float)[::-1]
        np.testing.assert_allclose(self.weighted(v,wm)+self.weighted(v,wb),v,atol=1e-11)
        np.testing.assert_allclose(self.current(v,0)+self.current(v,1),0,atol=1e-10)

    def test_full_current_factorization_and_commuting_tags(self):
        rng=np.random.default_rng(13)
        v=rng.normal(size=768)+1j*rng.normal(size=768)
        v/=np.linalg.norm(v)
        wm,wb=weights(LAMBDA*D)
        for j in (0,2):
            u=self.vs[1];energy=self.energies[j]
            delta=u.conj().T@energy@u-energy
            # K† J_M K = D ⊗ (U† E_M U−E_M) on all encoded states.
            transformed=self.k(v,True).reshape(4,192)
            expected=self.k((D@transformed@delta.T).reshape(-1))
            np.testing.assert_allclose(self.current(v,j),expected,atol=2e-13)
            np.testing.assert_allclose(self.weighted(self.current(v,j),wm),
                                       self.current(self.weighted(v,wm),j),atol=2e-13)
            jv=self.current(v,j);jbv=self.current(v,j+1)
            total=(self.weighted(jv,wm)+self.current(self.weighted(v,wm),j)
                   +self.weighted(jbv,wb)+self.current(self.weighted(v,wb),j+1))/2
            expected_total=LAMBDA*self.k((transformed@delta.T).reshape(-1))
            np.testing.assert_allclose(total,expected_total,atol=2e-13)
        # Unequal clock-phase effects anticommute with D, so they give exact
        # global cancellation even though they do not commute with current.
        phase_m,phase_b=weights(.8*(2*P-I))
        jv=self.current(v,0);jbv=self.current(v,1)
        total=(self.weighted(jv,phase_m)+self.current(self.weighted(v,phase_m),0)
               +self.weighted(jbv,phase_b)+self.current(self.weighted(v,phase_b),1))/2
        np.testing.assert_allclose(total,0,atol=2e-13)
        self.assertGreater(np.linalg.norm(self.weighted(jv,phase_m)-
                                           self.current(self.weighted(v,phase_m),0)),.01)

if __name__=='__main__':unittest.main()
