import math
import unittest
import numpy as np

try:
    from . import dust_orientation_record as d
except ImportError:
    import dust_orientation_record as d


class DustOrientationRecordTests(unittest.TestCase):
    def test_continuous_packet_and_resource_bound(self):
        result=d.run()
        self.assertLess(result['analytic_bounds']['cantelli_wrong_sign_upper'],.078)
        self.assertGreater(result['analytic_bounds']['relational_dust_energy_lower'],2.8)
        self.assertGreater(result['uniform_p_packet']['p_expanding'],.99999)
        self.assertGreater(result['uniform_p_packet']['delta_mean_A'],0)

    def test_signed_states_same_volume_and_opposite_slope(self):
        p=.06
        e=d.target_state(True);c=d.target_state(False)
        self.assertAlmostEqual(abs(np.vdot(e,c)),0,places=12)
        for r in (.2,1.,2.,3.,5.):
            a=d.radial_wave(p,r,True);b=d.radial_wave(p,r,False)
            self.assertAlmostEqual(abs(a)**2,abs(b)**2,places=13)
        x=d.full_dilation_moments(p,True)[0]
        y=d.full_dilation_moments(p,False)[0]
        self.assertLess(x,0);self.assertGreater(y,0)
        self.assertAlmostEqual(x,-y,places=12)

    def test_projector_completeness_and_noncommutation(self):
        exp,con,ev=d.projectors(.05)
        ident=np.eye(d.N)
        self.assertLess(np.max(abs(exp+con-ident)),1e-12)
        self.assertLess(np.max(abs(exp@con)),1e-12)
        self.assertLess(np.max(abs(exp@exp-exp)),1e-12)
        self.assertGreater(min(abs(ev)),2.9)
        A=np.diag(d.grav_energies(.05))
        self.assertGreater(np.max(abs(A@exp-exp@A)),.1)

    def test_actual_dilation_recurrence(self):
        alpha=d.nu(.05); n=7; h=1e-5
        for r in (.5,1.,2.,3.):
            f=d.radial_mode(n,alpha,r)
            derivative=(d.radial_mode(n,alpha,r+h)-d.radial_mode(n,alpha,r-h))/(2*h)
            lhs=-1j*(r*derivative+f/2)
            lower=math.sqrt(n*(n+alpha))*d.radial_mode(n-1,alpha,r)
            upper=math.sqrt((n+1)*(n+1+alpha))*d.radial_mode(n+1,alpha,r)
            rhs=1j*(lower-upper)
            self.assertLess(abs(lhs-rhs),1e-7)

    def test_controlled_record_retains_qutrit_outcomes(self):
        actual=d.pulse_control(.06)
        self.assertLess(actual['max_state_error'],1e-8)
        self.assertAlmostEqual(sum(actual['qutrit_probabilities']),1,places=8)
        self.assertGreater(actual['qutrit_probabilities'][1],.99999)
        with self.assertRaises(ValueError): d.nu(.11)

if __name__=='__main__': unittest.main()
