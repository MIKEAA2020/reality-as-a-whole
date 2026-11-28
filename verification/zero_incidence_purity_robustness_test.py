"""Robustness of direct-sum incidence against imperfect physical purity.

The type labels are bookkeeping hypotheses, not established experiencing
subjects.  The physical state in the witness is a controlled perturbation of
the actual stored sphere/echo vector, not the original exact pure state.
"""
import unittest
import numpy as np
import sympy as sp
from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial,apply64,LL,C
from verification.zero_relative_gauge_invariant_report_test import G
from verification.zero_internal_contextual_reference_test import value_history,gauge_history
from verification.zero_persistent_sphere_subject_selection_test import norm2


def theoretical_bound(delta,alpha):
    return min(alpha*(1-alpha), max(alpha,1-alpha)*delta + .5*np.sqrt(delta*(1-delta)))


class IncidencePurityRobustnessTests(unittest.TestCase):
    def test_angular_coarse_access_variances_independently(self):
        u=sp.symbols('u',real=True); F=sp.Rational
        bands=[(F(-1),F(-1,2)),(F(-1,2),F(0)),(F(0),F(1))]
        functions=[[-u,-u,u],[-u*(u+1),-u*(u+1),u*(u+1)]]
        outputs=[]
        for f in functions:
            w=[(b-a)/2 for a,b in bands]
            means=[sp.integrate(g,(u,a,b))/(b-a) for g,(a,b) in zip(f,bands)]
            avg=sum(wi*mi for wi,mi in zip(w,means))
            second=sum(sp.integrate(g*g,(u,a,b))/2 for g,(a,b) in zip(f,bands))
            rminus=(w[0]*means[0]+w[1]*means[1])/(w[0]+w[1])
            rplus=means[2]
            risk_r=second-(w[0]+w[1])*rminus**2-w[2]*rplus**2
            risk_full=second-sum(wi*mi*mi for wi,mi in zip(w,means))
            outputs.append((means,avg,second,second-avg**2,risk_r,risk_full))
        self.assertEqual(outputs[0],([F(3,4),F(1,4),F(1,2)],F(1,2),F(1,3),F(1,12),F(1,12),F(5,96)))
        self.assertEqual(outputs[1],([F(1,6),F(1,6),F(5,6)],F(1,2),F(8,15),F(17,60),F(31,180),F(31,180)))

    def test_actual_echo_sector_square_root_witness(self):
        root=output(active_base())
        for label in (0,7,15):
            x=initial(relative_read(root,4,labels=(label,))[0])
            psi=x/np.sqrt(norm2(x)); phi=value_history(psi)
            self.assertAlmostEqual(norm2(phi),1,places=12)
            self.assertLess(abs(np.vdot(psi,phi)),1e-12)
            np.testing.assert_allclose(value_history(phi),psi,atol=1e-12)
            for v in (psi,phi):
                np.testing.assert_allclose(gauge_history(v),v,atol=1e-12)
                np.testing.assert_allclose(apply64(LL,v),v,atol=1e-12)
                np.testing.assert_allclose(apply64(G,v),v,atol=1e-12)
                for charge in C:
                    np.testing.assert_allclose(apply64(charge,v),0,atol=1e-12)
            for delta in (0.,.0001,.01,.1):
                plus=np.sqrt(1-delta)*psi+np.sqrt(delta)*phi
                minus=np.sqrt(1-delta)*psi-np.sqrt(delta)*phi
                # E=(I+O)/2 with O=value_history on the declared valid sector.
                def eprob(v): return ((norm2(v)+np.vdot(v,value_history(v)).real)/2)
                pp,pm=eprob(plus),eprob(minus)
                self.assertAlmostEqual((pp+pm)/2,.5,places=12)
                self.assertAlmostEqual(pp,.5+np.sqrt(delta*(1-delta)),places=12)
                # Product and correlated incidence states have the exact same
                # physical marginal, and equal type totals, but different joint weights.
                joint_correlated=.5*pp; joint_independent=.25
                difference=joint_correlated-joint_independent
                self.assertAlmostEqual(difference,.5*np.sqrt(delta*(1-delta)),places=12)
                self.assertLessEqual(abs(difference),theoretical_bound(delta,.5)+1e-12)

    def test_general_positive_block_bound_and_rare_conditioning(self):
        rng=np.random.default_rng(7281)
        for delta in (.001,.02,.17,.5):
            rho=np.diag([1-delta,.6*delta,.4*delta]).astype(complex)
            sr=np.diag(np.sqrt(np.diag(rho)))
            for _ in range(80):
                U,_=np.linalg.qr(rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)))
                A=U@np.diag(rng.uniform(0,1,size=3))@U.conj().T
                B=sr@A@sr
                V,_=np.linalg.qr(rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)))
                E=V@np.diag(rng.uniform(0,1,size=3))@V.conj().T
                alpha=np.trace(B).real; pE=np.trace(rho@E).real
                discrepancy=(np.trace(B@E)-alpha*np.trace(rho@E)).real
                self.assertLessEqual(abs(discrepancy),theoretical_bound(delta,alpha)+1e-12)
                self.assertLessEqual(abs(discrepancy/pE),theoretical_bound(delta,alpha)/pE+1e-12)
        # The inequality's 1/pE factor shows why rare conditional events
        # require separate certification; it is not a claim of saturation.

    def test_rare_event_can_amplify_a_small_marginal_defect(self):
        for delta in (.0001,.01,.1):
            rho=np.diag([1-delta,delta]); E=np.diag([0.,1.])
            B=np.diag([.5-delta,delta]); J=np.diag([.5,0.])
            np.testing.assert_allclose(B+J,rho)
            self.assertAlmostEqual(np.trace(B),.5,places=13)
            pE=np.trace(rho@E); pBE=np.trace(B@E)
            self.assertAlmostEqual(pBE/pE,1,places=13)
            self.assertAlmostEqual(pBE-.5*pE,delta/2,places=13)
            # |phi><phi| is a formal physical effect; operational accessibility
            # of a global projector is an independent model assumption.

    def test_approximate_flag_coherence_tradeoff_is_sharp_for_actual_pair(self):
        # The conditional Bell pair in the original source, both b sectors.
        # F is the second factor; D=X_S X_F anticommutes with its flag Z.
        X=np.array([[0.,1.],[1.,0.]])
        z=np.diag([1.,-1.]); I=np.eye(2)
        P0=np.kron(I,(I+z)/2); P1=np.kron(I,(I-z)/2); D=np.kron(X,X)
        for bit in (0,1):
            u0=np.eye(4)[:,2*bit]
            u1=np.eye(4)[:,2*(bit^1)+1]
            psi=(u0+u1)/np.sqrt(2); ideal=np.outer(psi,psi)
            self.assertAlmostEqual(np.vdot(psi,D@psi).real,1,places=13)
            for eta in (0.,.01,.2,.4,.5):
                v0=np.sqrt(1-eta)*u0+np.sqrt(eta)*u1
                v1=np.sqrt(eta)*u0+np.sqrt(1-eta)*u1
                B=np.outer(v0,v0)/2; J=np.outer(v1,v1)/2
                rho=B+J; error=np.trace(B@P1+J@P0).real
                dist=np.sum(abs(np.linalg.eigvalsh(rho-ideal)))/2
                lower=.5-np.sqrt(eta*(1-eta))
                self.assertAlmostEqual(error,eta,places=13)
                self.assertAlmostEqual(dist,lower,places=13)
                self.assertAlmostEqual(np.trace(B).real,.5,places=13)
                self.assertAlmostEqual(np.trace(J).real,.5,places=13)
                self.assertAlmostEqual(np.trace(rho@D).real,2*np.sqrt(eta*(1-eta)),places=13)
                qx=np.kron(X,I)-np.kron(I,X)
                self.assertAlmostEqual(np.trace(rho@qx@qx).real,4*dist,places=13)
        # At distance <=0.1, the exact tradeoff gives at least 20% flag error.
        self.assertAlmostEqual((1-np.sqrt(1-4*(.5-.1)**2))/2,.2,places=13)

    def test_finite_ensemble_identity_and_scale(self):
        for delta in (0.,1e-4,.01,.1,.5):
            psi=np.array([1.,0.]);phi=np.array([0.,1.])
            plus=np.sqrt(1-delta)*psi+np.sqrt(delta)*phi
            minus=np.sqrt(1-delta)*psi-np.sqrt(delta)*phi
            B=np.outer(plus,plus)/2; J=np.outer(minus,minus)/2
            rho=np.diag([1-delta,delta]); prod=rho/2
            np.testing.assert_allclose(B+J,rho,atol=1e-14)
            self.assertAlmostEqual(np.trace(B),.5,places=13)
            self.assertAlmostEqual(np.linalg.eigvalsh(B-prod)[-1],.5*np.sqrt(delta*(1-delta)),places=13)
            # Distance of physical marginal from the specified ideal pure state.
            D=np.linalg.eigvalsh(rho-np.diag([1.,0.]))
            self.assertAlmostEqual(np.sum(abs(D))/2,delta,places=13)


if __name__=='__main__': unittest.main()
