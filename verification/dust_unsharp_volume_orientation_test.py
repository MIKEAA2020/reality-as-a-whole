import math
import unittest
import numpy as np
from scipy.special import erf, eval_genlaguerre, gammaln

try:
    from . import dust_unsharp_volume_orientation as d
except ImportError:
    import dust_unsharp_volume_orientation as d


class DustUnsharpVolumeOrientationTests(unittest.TestCase):
    def test_normalizable_packet_and_outside(self):
        r=d.run()
        a=r['uniform_scalar_packet_outcomes']['expanding']
        b=r['uniform_scalar_packet_outcomes']['contracting']
        self.assertGreater(a['expanding_label'],.89)
        self.assertLess(a['contracting_label'],.001)
        self.assertGreater(a['outside_window'],.09)
        self.assertAlmostEqual(a['expanding_label'],b['contracting_label'],places=11)
        self.assertAlmostEqual(a['contracting_label'],b['expanding_label'],places=11)
        self.assertAlmostEqual(sum(a[k] for k in ('expanding_label','contracting_label','outside_window')),1,places=10)
        self.assertGreater(r['relational_dust_energy_lower_bound'],2.8)

    def test_effect_positivity_and_noncommuting(self):
        e,c=d.effects(.05)
        no=d.I-e-c
        for op in (e,c,no):
            self.assertGreater(np.linalg.eigvalsh(op).min(),-1e-9)
        self.assertGreater(np.linalg.norm(e@c-c@e,2),.05)
        self.assertGreater(np.linalg.norm(np.diag(d.grav_energies(.05))@e-e@np.diag(d.grav_energies(.05)),2),1)

    def test_position_marginal_against_direct_gaussian_integral(self):
        p=.05;e,c=d.effects(p,points=4096,panels=64)
        y=np.linspace(-12,4,16385)
        z=d.BETA*np.exp(2*y);alpha=d.nu(p)
        fields=[]
        for j in range(d.N):
            n=d.N0+j
            L=.5*(math.log(2)+(alpha+1)*math.log(d.BETA)+gammaln(n+1)-gammaln(n+alpha+1))
            fields.append(np.exp(L+(alpha+1)*y-z/2)*eval_genlaguerre(n,alpha,z))
        F=np.array(fields)
        window=(erf((d.QHI-y)/d.S)-erf((d.QLO-y)/d.S))/2
        reference=(F*window)@F.T*(y[1]-y[0])
        self.assertLess(np.max(abs(reference-e-c)),1e-6)

    def test_complete_householder_and_pulse(self):
        e,c=d.effects(0)
        Ks,J,V,P,s=d.dilation(e,c)
        self.assertGreater(s,.1)
        self.assertLess(np.max(abs(P@P-P)),1e-12)
        self.assertLess(np.max(abs((np.eye(3*d.N)-2*P)@J-V)),1e-12)
        self.assertLess(np.max(abs(sum(K.conj().T@K for K in Ks)-d.I)),1e-12)
        check=d.pulse_check(0,e,c)
        self.assertLess(check['state_max_error'],1e-8)

    def test_calibration_and_bad_arguments(self):
        self.assertAlmostEqual(.5*math.erfc(d.S*8),.0023388674905236327)
        self.assertAlmostEqual(.5*math.erfc(.5/d.S),.0023388674905236327)
        with self.assertRaises(ValueError):d.effects(0,panels=3)
        with self.assertRaises(ValueError):d.effects(.11)

if __name__=='__main__':unittest.main()
