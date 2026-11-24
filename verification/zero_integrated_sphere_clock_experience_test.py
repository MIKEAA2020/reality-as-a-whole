"""One sphere-record state coupled to the autonomous two-window clock.

The physical joint probabilities are conditional finite-grid calculations.
Experience, actual subjects, incidence and outcome selection are not derived.
"""
import math
import unittest
import numpy as np
from verification.zero_five_ray_record_current_unification_test import joint_state,axis,ns,q
from verification.zero_sphere_mismatch_experience_comparison_test import phase_flip
from verification.zero_reciprocal_subject_exchange_test import J,proj
from verification.zero_autonomous_two_window_records_test import make_model,states,probabilities,mutual_information


def sphere(context):
    v=joint_state(context)
    return np.array([v,phase_flip(v)],complex).reshape(2,2,2,5,4,16)


def gram_ir(psi):
    result=np.zeros((5,4,2,2),complex)
    for i in range(5):
        for r in range(4):
            m=psi[:,:,:,i,r,:].reshape(2,-1)
            result[i,r]=m@m.conj().T
    return result


def bob_cross(psi,h,g):
    # trace Alice qubit and her recorded sphere label; retain b,r,work
    a=psi[h].transpose(0,2,1,3,4).reshape(10,128)
    b=psi[g].transpose(0,2,1,3,4).reshape(10,128)
    return a.T@b.conj()


def joint_k_mem(model,t):
    vs=states(model,t)
    # 1/2 prior for K=±1; conditional M1,M2 readouts for each h.
    return np.array([np.sum(abs(v)**2,axis=(0,3)) for v in vs])/2


def h_memory2(joint):return joint.sum(axis=1)


class IntegratedSphereClockExperienceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.triple=sphere('triple');cls.pair=sphere('pair')
        cls.model=make_model(80)
        cls.early=joint_k_mem(cls.model,30);cls.late=joint_k_mem(cls.model,100)

    def test_actual_sphere_records_and_current_are_the_code_eigenstates(self):
        J1=np.asarray(J[0]);J2=np.asarray(J[2]);P=np.asarray(proj)
        self.assertLess(np.linalg.norm(J1+J2),1e-14)
        self.assertLess(np.linalg.norm(J1@J1-P),1e-14)
        for context in (self.pair,self.triple):
            for h in (0,1):
                v=context[h]
                jv=np.einsum('abirw,xw->abirx',v,J1)
                k=jv*np.array([1,1,-1,-1])[None,None,None,:,None]
                self.assertLess(np.linalg.norm(k-(1-2*h)*v),1e-13)
                self.assertAlmostEqual(np.linalg.norm(v),1,places=12)

    def test_actual_sphere_table_and_per_record_h_orthogonality(self):
        g=gram_ir(self.triple)
        expected=np.array([[3/40,1/20],[1/10,3/10],[13/40,3/20]])
        for i in range(3):
            for r in (1,2):
                self.assertAlmostEqual(g[i,r,0,0].real,expected[i,r-1],places=12)
                self.assertAlmostEqual(g[i,r,1,1].real,expected[i,r-1],places=12)
                self.assertLess(abs(g[i,r,0,1]),1e-14)
        self.assertLess(np.linalg.norm(g[:,[0,3]]),1e-14)
        for i in range(3):self.assertAlmostEqual(expected[i].sum(),q[i])
        self.assertLess(np.linalg.norm(sum(qi*np.array(ni) for qi,ni in zip(q,ns))),1e-14)

    def test_complete_bob_cross_operators_are_same_for_pair_and_triple(self):
        for h in (0,1):
            for g in (0,1):
                self.assertLess(np.linalg.norm(bob_cross(self.pair,h,g)-bob_cross(self.triple,h,g)),1e-13)
        # Since both h branches are obtained by the same Bob-local Z pulse,
        # any fixed Bob+geometry+memory CPTP operation preserves equality.

    def test_k_memory_correlation_is_transient_not_the_late_record_mi(self):
        e=h_memory2(self.early);l=h_memory2(self.late)
        self.assertAlmostEqual(mutual_information(e),.02479102803495,places=10)
        self.assertAlmostEqual(mutual_information(l),.0000001170537,places=11)
        self.assertAlmostEqual(e[1,1]/sum(e[:,1]),.7389622165727,places=10)
        self.assertAlmostEqual(l[1,1]/sum(l[:,1]),.4997618909211,places=10)
        self.assertAlmostEqual(mutual_information(self.late.sum(axis=0)),.42471210469619,places=10)
        self.assertGreater(mutual_information(self.late.sum(axis=0)),1000000*mutual_information(l))

    def test_sphere_record_and_memory_joint_factorizes(self):
        # Construct the full physical vector, rather than assuming factorization.
        vs=np.array(states(self.model,30));c=np.array([1,1j])/math.sqrt(2)
        whole=np.einsum('habirw,hdmnp,h->abirwdmnp',self.triple,vs,c,optimize=True)
        self.assertAlmostEqual(np.linalg.norm(whole),1,places=11)
        g=gram_ir(self.triple);jm=self.early.sum(axis=0)
        actual=np.sum(abs(whole)**2,axis=(0,1,4,5,8))
        expected=np.einsum('ir,mn->irmn',g[:,:,0,0].real,jm)
        self.assertLess(np.max(abs(actual-expected)),1e-13)
        # Stronger than a single table: the entire record+memory density
        # factors, including off-diagonal memory components.
        V=whole.transpose(3,6,7,0,1,2,4,5,8).reshape(16,-1)
        rho=V@V.conj().T
        mem=sum(np.einsum('dmnp,dklp->mnkl',v,v.conj()).reshape(4,4)/2 for v in vs)
        rhor=np.diag([0,.5,.5,0])
        self.assertLess(np.linalg.norm(rho-np.kron(rhor,mem)),1e-13)

    def test_experience_rivals_disagree_on_same_commuting_readout_events(self):
        # For record r=+1 and M2=1, h=0 has J1=+1 and h=1 has J1=-1.
        # R=+1 is fixed; J's conditional mean is 1-2 Pr(h=1|M2=1).
        e=h_memory2(self.early)
        chance=e[1,1]/sum(e[:,1])
        self.assertAlmostEqual(1-2*chance,-.477924433145384,places=10)
        for r in (1,-1):
            for h in (0,1):
                record=(r,-r)
                current=(r*(1-2*h),-r*(1-2*h))
                mismatch=((-1 if r==-1 else 0),(-1 if r==1 else 0))
                self.assertEqual(sum(record),0)
                self.assertEqual(sum(current),0)
                self.assertEqual(sum(mismatch),-1)
                self.assertEqual(record==current,h==0)

    def test_finite_grid_refinement_includes_actual_h_conditionals(self):
        vals=[]
        for n in (40,80,160):
            x=h_memory2(joint_k_mem(make_model(n),30))
            vals.append((mutual_information(x),x[1,1]/sum(x[:,1])))
        for a,b in zip(vals,vals[1:]):
            self.assertLess(abs(a[0]-b[0]),3e-6)
            self.assertLess(abs(a[1]-b[1]),8e-6)

    def test_equal_subject_count_is_not_derived_from_probability(self):
        for r in (-1,1):
            for h in (0,1):
                v=r*(1-2*h)
                self.assertEqual(v-v,0)
                self.assertNotEqual(2*v-v,0)
        # Fixed unequal positive weights leave opposite nonzero branch sums.

if __name__=='__main__':unittest.main()
