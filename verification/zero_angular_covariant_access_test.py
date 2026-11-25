"""Lorentz and transported-counterpart tests on the same angular interface."""
from fractions import Fraction as F
import unittest
import numpy as np
from verification.zero_angular_covariant_access import (
    boost_angle,inverse_angle,transported_density,transported_counterpart,
    counterpart_abs_derivative,transported_sign,naive_sign,conditional_angle,lorentz_z,
)
from verification.zero_quantum_angular_echo import latitudes,reflect_index,embed
from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial as source_initial
from verification.zero_persistent_sphere_subject_selection_test import norm2
from verification.zero_sphere_angular_echo import initial,magnitude

class AngularCovariantAccessTests(unittest.TestCase):
    def test_old_u_and_quantum_bin_meanings_survive_passive_boost(self):
        eta=np.diag([1.,-1.,-1.,-1.]);t=np.array([1.,0,0,0]);m=np.array([0.,0,0,1.])
        for beta in (-.7,.4,.8):
            L=lorentz_z(beta)
            np.testing.assert_allclose(L.T@eta@L,eta,atol=1e-13)
            for u in latitudes(8):
                f=float(u);k=np.array([1.,np.sqrt(1-f*f),0.,f])
                result=conditional_angle(L@t,L@m,L@k)
                self.assertAlmostEqual(result,f,places=13)
                self.assertAlmostEqual(conditional_angle(L@t,L@m,3.1*(L@k)),f,places=13)
                b,z,_,_=initial(u,1)
                self.assertEqual((b,z),(1 if result>0 else -1,1 if result>-.5 else -1))
                # A chosen physical T,M transform with the ray: a passive
                # coordinate change does not change the physical question.

    def test_changed_observer_rebins_the_same_ray_distribution(self):
        beta=F(1,2)
        # For a physically changed observer, u'=(u-beta)/(1-beta*u).
        # With original du/2, u'>0 iff u>beta and u'>-1/2 iff u>0.
        b_cut=inverse_angle(F(0),beta);z_cut=inverse_angle(F(-1,2),beta)
        self.assertEqual((b_cut,z_cut),(F(1,2),F(0)))
        weights=((1-b_cut)/2,(b_cut-z_cut)/2,(z_cut+1)/2)
        self.assertEqual(weights,(F(1,4),F(1,4),F(1,2)))
        self.assertEqual(sum(weights),1)
        # These are alternative observer-dependent questions, not a passive
        # transform of the earlier fixed M,T record with its apparatus.

    def test_rebinned_questions_on_original_coherent_echo(self):
        root=output(active_base());beta=F(1,2);n=8
        for label in (0,5,15):
            x=source_initial(relative_read(root,4,labels=(label,))[0])
            for s in (1,-1):
                u,v,rows=embed(x,s,n);total=norm2(v)
                weights={(1,1):0.,(-1,1):0.,(-1,-1):0.}
                for i,u_value in enumerate(u):
                    obs=boost_angle(u_value,beta)
                    # Avoid samples exactly at the new sign thresholds.
                    self.assertNotIn(obs,(0,F(-1,2)))
                    b=1 if obs>0 else -1;z=1 if obs>F(-1,2) else -1
                    weights[b,z]+=sum(norm2(part[i]) for part in rows)/total
                for key,value in {(1,1):.25,(-1,1):.25,(-1,-1):.5}.items():
                    self.assertAlmostEqual(weights[key],value,places=12)
        # New observer bins are different questions on the same added angular
        # register, not evidence of an actual relativistic apparatus.

    def test_counterpart_and_measure_transport_not_naive_antipodes(self):
        for beta in (F(1,3),F(1,2),F(-2,3)):
            for raw in (F(-4,5),F(-1,4),F(1,5),F(3,4)):
                y=boost_angle(raw,beta);h=transported_counterpart(y,beta)
                self.assertEqual(inverse_angle(y,beta),raw)
                self.assertEqual(transported_counterpart(h,beta),y)
                self.assertEqual(transported_sign(h,beta),-transported_sign(y,beta))
                self.assertEqual(transported_density(y,beta),
                                 transported_density(h,beta)*counterpart_abs_derivative(y,beta))
                if beta and raw:self.assertNotEqual(h,-y)
        # At beta=1/2, naïvely taking sign(y) on the pushed measure makes
        # P(+)=1/4 and signed mean=-1/2; transported original sign yields
        # P(+)=1/2, mean zero. Neither is an experiential incidence theorem.
        beta=F(1,2)
        self.assertEqual((1-beta)/2,F(1,4))
        self.assertEqual(2*((1-beta)/2)-1,F(-1,2))
        self.assertEqual(inverse_angle(-beta,beta),0)
        self.assertEqual((1-F(0))/2,F(1,2))

    def test_finite_echo_reflection_transports_under_frame_change(self):
        beta=F(1,2);u=latitudes(16)
        for i,x in enumerate(u):
            y=boost_angle(x,beta);x1=inverse_angle(y,beta)
            partner=u[reflect_index(i,16)]
            # Keep original reference roles T and M: the same transformed
            # pair still obeys h(u), even though the chart is aberrated.
            yp=boost_angle(partner,beta)
            self.assertEqual(inverse_angle(yp,beta),partner)
            self.assertEqual(magnitude(x1,'swap_invariant'),magnitude(partner,'swap_invariant'))
            if x<0 and abs(x)!=abs(partner):
                self.assertNotEqual(magnitude(x1,'absolute'),magnitude(partner,'absolute'))

if __name__=='__main__':unittest.main()
