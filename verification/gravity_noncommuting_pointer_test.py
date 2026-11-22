import unittest
import numpy as np

try:
    from . import gravity_noncommuting_pointer as p
    from .gravitating_clock_probe import scatter
except ImportError:
    import gravity_noncommuting_pointer as p
    from gravitating_clock_probe import scatter


class NoncommutingPointerTests(unittest.TestCase):
    def test_packet_complete_and_matched_control(self):
        report=p.run()
        outcome=report['complete_ground_channel_packet_outcomes']
        self.assertGreater(outcome['up'],.25)
        self.assertLess(outcome['up'],.30)
        self.assertAlmostEqual(outcome['up']+outcome['down'],1,places=9)
        self.assertLess(report['matched_reference_pointer_flip'],1e-20)
        self.assertLess(report['zero_gap_pointer_flip'],1e-20)

    def test_exact_reference_and_flux(self):
        for k in (2.,2.01):
            S=p.reflection(k,amplitude=0)
            ref=np.diag([scatter(k,.6),scatter(k,.2)])
            self.assertLess(np.max(abs(S-ref)),1e-8)
            coupled=p.reflection(k)
            self.assertLess(np.max(abs(coupled.conj().T@coupled-p.I)),1e-9)

    def test_zero_energy_gap_and_sign_control(self):
        k=2.005
        deg=p.reflection(k,epsilon=0)
        self.assertLess(np.max(abs(deg-scatter(k,.2)*p.I)),1e-8)
        pos=p.reflection(k)
        neg=p.reflection(k,amplitude=-p.AMP)
        self.assertLess(np.max(abs(neg-p.Z@pos@p.Z)),1e-10)
        self.assertAlmostEqual(abs(pos[0,1])**2,abs(neg[0,1])**2,places=12)

    def test_jost_wronskian_and_parameter_rejection(self):
        j,dj=p.jost(2,.6,-1)
        self.assertAlmostEqual(abs(j*dj.conjugate()-dj*j.conjugate()+4j),0,places=11)
        with self.assertRaises(ValueError):p.reflection(0)
        with self.assertRaises(ValueError):p.reflection(2,right=1)
        with self.assertRaises(ValueError):p.reflection(2,epsilon=-1)
        with self.assertRaises(ValueError):p.packet(panels=3)

    def test_backreaction_channel_changes_output(self):
        ground=p.flip(2.005,energy=.3)
        excited=p.flip(2.005,energy=.9)
        self.assertGreater(excited-ground,.06)
        # This compares two model preparations, not an empirical signal.

if __name__=='__main__': unittest.main()
