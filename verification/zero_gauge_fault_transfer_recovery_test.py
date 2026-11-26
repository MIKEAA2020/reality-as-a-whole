"""Finite unitary transfer-rival, feedback and clock-disturbance tests."""
import math
import unittest
import numpy as np

from verification.zero_gauge_fault_transfer_recovery import (
    apparatus,prepare_reference,raw_output,reported_output,mixture_output,
    t_transfer_bound,written_ready_bias_bound,recovered_sensor_residual,
    analytic_recovered_residual,CONTEXTS,I2,I3,P1,X,kron)
from scipy.linalg import expm
from verification.zero_gauge_clock_joint_instrument import clock_residuals
from verification.zero_gauge_clock_meta_root import target_output


class FaultTransferRecoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.theta=math.asin(.2)
        cls.pb=.03125;cls.pc=.1;cls.eps=.8
        cls.g=(1-2*cls.pb)*(1-2*cls.pc)
        cls.z=2*cls.eps/81
        cls.reference_gain=.72
        cls.t1=-cls.reference_gain*cls.z/(2*cls.g*.04)

    def test_unitary_feedback_and_explicit_reference_preparations(self):
        u,w=apparatus(self.theta)
        self.assertTrue(np.allclose(u.conj().T@u,np.eye(24),atol=1e-14))
        self.assertTrue(np.allclose(w.conj().T@w,np.eye(24),atol=1e-14))
        # The stipulated pointer and apparatus are neutral spectators to a
        # separate frame-gauge action; this is not a locality derivation.
        gauge=np.array([[0,1],[-1,0]],complex)
        frame=kron(gauge,np.eye(24))
        for gate in (u,w):
            lifted=kron(I2,gate)
            self.assertTrue(np.allclose(frame@lifted,lifted@frame,atol=1e-14))
        for b,c in CONTEXTS:
            ref=prepare_reference(b,c,.5)
            self.assertAlmostEqual(np.trace(ref).real,1.)
            self.assertGreaterEqual(np.linalg.eigvalsh(ref).min(),-1e-14)
            out=reported_output(self.theta,b,c,.5,self.pb,self.pc)
            # Calibration looks exactly like independent 5% and 10% flips.
            for bp,cp in CONTEXTS:
                expected=(.95 if bp==b else .05)*(.9 if cp==c else .1)
                self.assertAlmostEqual(out[bp,cp],expected,places=14)
            self.assertEqual(out[0,1]+out[0,-1],0.)

    def test_two_source_mechanisms_same_table_and_same_environment_marginal(self):
        target_p=target_output(self.z)
        null_p={ctx:.25 for ctx in CONTEXTS}
        ref_t={ctx:.5 for ctx in CONTEXTS}
        source_t={ctx:.5+self.t1*ctx[0]*ctx[1] for ctx in CONTEXTS}
        target=mixture_output(self.theta,target_p,ref_t,self.pb,self.pc)
        rival=mixture_output(self.theta,null_p,source_t,self.pb,self.pc)
        expected=target_output(self.reference_gain*self.z)
        self.assertAlmostEqual(sum(null_p[k]*source_t[k] for k in CONTEXTS),.5)
        for b in (1,-1):
            self.assertAlmostEqual(sum(source_t[b,c]/2 for c in (1,-1)),.5)
        for c in (1,-1):
            self.assertAlmostEqual(sum(source_t[b,c]/2 for b in (1,-1)),.5)
        for b,c in CONTEXTS:
            self.assertAlmostEqual(target[b,c],rival[b,c],places=14)
            self.assertAlmostEqual(target[b,c],expected[b,c],places=14)
        self.assertAlmostEqual(self.t1,-.23703703703703702,places=14)
        # No direct B↔C coupling exists in U. A shared cause of E and c is
        # allowed; equal one-system marginals do not establish independence.

    def test_explicit_saturated_transfer_bound(self):
        tau=t_transfer_bound(self.theta,self.pb,self.pc,abs(self.t1))
        self.assertAlmostEqual(tau,.01422222222222222,places=14)
        for b,c in CONTEXTS:
            ref=reported_output(self.theta,b,c,.5,self.pb,self.pc)
            src=reported_output(self.theta,b,c,.5+self.t1*b*c,self.pb,self.pc)
            mu=lambda tab:sum(x*y*tab[x,y] for x,y in CONTEXTS)
            self.assertAlmostEqual(abs(mu(ref)-mu(src)),tau,places=14)
        self.assertEqual(t_transfer_bound(0.,self.pb,self.pc,1.),0.)
        self.assertGreater(t_transfer_bound(self.theta,self.pb,self.pc,0.,.001),0.)
        with self.assertRaises(ValueError):t_transfer_bound(self.theta,self.pb,self.pc,2.)

    def test_recovery_removes_false_signal_and_keeps_true_signal(self):
        target_p=target_output(self.z);null_p={ctx:.25 for ctx in CONTEXTS}
        ref_t={ctx:.5 for ctx in CONTEXTS}
        source_t={ctx:.5+self.t1*ctx[0]*ctx[1] for ctx in CONTEXTS}
        target=mixture_output(self.theta,target_p,ref_t,self.pb,self.pc,True)
        null=mixture_output(self.theta,null_p,source_t,self.pb,self.pc,True)
        for b,c in CONTEXTS:
            self.assertAlmostEqual(null[b,c],.25,places=14)
            self.assertAlmostEqual(target[b,c],(1+b*c*self.g*self.z)/4,places=14)
        self.assertNotEqual(self.g,self.reference_gain) # recalibration required

    def test_recovery_preserves_any_written_entangled_quantum_state(self):
        rng=np.random.default_rng(420)
        u,w=apparatus(self.theta)
        for _ in range(15):
            psi=rng.normal(size=(2,2,2))+1j*rng.normal(size=(2,2,2))
            psi/=np.linalg.norm(psi)
            initial=np.zeros((3,2,2,2),complex);initial[1:,:,:,0]=psi
            after=(w@u@initial.reshape(-1)).reshape(3,2,2,2)[1:]
            before_bc=np.einsum('bce,dfe->bcdf',psi,psi.conj())
            after_bc=np.einsum('bcea,dfea->bcdf',after,after.conj())
            self.assertTrue(np.allclose(before_bc,after_bc,atol=1e-14))

    def test_feedback_requires_ready_fault_qubit(self):
        u,w=apparatus(self.theta)
        # An unreset |1> fault qubit is mistaken for a fault. With E=0 the
        # interaction makes no error, but W nevertheless flips the record.
        v=np.zeros((3,2,2,2),complex);v[1,0,0,1]=1.
        result=(w@u@v.reshape(-1)).reshape(3,2,2,2)
        self.assertAlmostEqual(abs(result[2,0,0,1])**2,1.)
        # For E=1 both coherent branches also end with B flipped: the fault
        # marker and feedback have opposite meaning when A starts in |1>.
        v.fill(0);v[1,0,1,1]=1.
        result=(w@u@v.reshape(-1)).reshape(3,2,2,2)
        self.assertAlmostEqual(np.sum(abs(result[2])**2),1.)

    def test_imperfect_ready_error_factorization_and_trace_bound(self):
        u,w=apparatus(self.theta)
        env_rotation=expm(-1j*self.theta*kron(I3,I2,P1,X))
        written=kron(np.diag([0,1,1]),I2,I2,I2)
        self.assertTrue(np.allclose((w@u-env_rotation@w)@written,0.,atol=1e-14))
        rng=np.random.default_rng(721);err=.03
        for _ in range(12):
            psi=rng.normal(size=(2,2,2,2))+1j*rng.normal(size=(2,2,2,2))
            psi[:,:,:,0]*=math.sqrt((1-err)/np.sum(abs(psi[:,:,:,0])**2))
            psi[:,:,:,1]*=math.sqrt(err/np.sum(abs(psi[:,:,:,1])**2))
            v=np.zeros((3,2,2,2),complex);v[1:]=psi
            out=(w@u@v.reshape(-1)).reshape(3,2,2,2)[1:]
            original=np.einsum('bcea,dfea->bcdf',psi,psi.conj()).reshape(4,4)
            recovered=np.einsum('bcea,dfea->bcdf',out,out.conj()).reshape(4,4)
            distance=np.sum(abs(np.linalg.eigvalsh(recovered-original)))/2
            self.assertLessEqual(distance,err+1e-14)
        self.assertAlmostEqual(written_ready_bias_bound(self.pb,self.pc,.001),.0015)
        with self.assertRaises(ValueError):written_ready_bias_bound(self.pb,self.pc,2.)

    def test_blank_written_coherence_is_not_recovered(self):
        u,w=apparatus(self.theta)
        v=np.zeros((3,2,2,2),complex)
        v[0,0,1,0]=1/math.sqrt(2);v[1,0,1,0]=1/math.sqrt(2)
        final=(w@u@v.reshape(-1)).reshape(3,2,2,2)
        reduced=np.einsum('bcea,dcea->bd',final,final.conj())
        self.assertAlmostEqual(reduced[0,1].real,math.cos(self.theta)/2,places=14)
        self.assertGreater(abs(reduced[0,1]-.5),0.)

    def test_actual_coherent_sensor_history_residual_with_fault_record(self):
        for n,alpha,beta,q,h in ((40,.05,.1,1,.43),(40,.05,.1,2,-.7),
                                 (20,.1,.2,1,.2)):
            direct=recovered_sensor_residual(n,h,q,alpha,beta,self.theta)
            formula=analytic_recovered_residual(n,alpha,beta,self.theta)
            self.assertAlmostEqual(direct,formula,places=13)
            self.assertGreater(direct,clock_residuals(n,alpha,beta)['coherent'])
        self.assertAlmostEqual(recovered_sensor_residual(40,.43,1,.05,.1,self.theta),
                               .17499810964746812,places=13)

if __name__=='__main__':unittest.main()
