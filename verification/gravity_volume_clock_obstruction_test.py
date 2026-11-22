import cmath
import math
import unittest

try:
    from . import gravity_volume_clock_obstruction as v
    from .gravitating_clock_probe import loggamma, scatter
except ImportError:
    import gravity_volume_clock_obstruction as v
    from gravitating_clock_probe import loggamma, scatter


def inner(a,b):
    return sum(x.conjugate()*y for x,y in zip(a,b))


def incoming_phase(k,kap):
    # Unit-modulus normalized incoming coefficient of the real standing mode.
    loga=loggamma(-2j*k)-loggamma(.5-kap-1j*k)+1j*k*math.log(2)
    return cmath.exp(1j*loga.imag)


class VolumeObstructionTests(unittest.TestCase):
    def test_parent_model_checks(self):
        r=v.run()
        self.assertEqual(r['status'],'passed')
        self.assertLess(r['packet_2_49_to_2_50']['conditional_record_plus_probability'],.51)

    def test_sign_bracketing_and_normalizable_packet(self):
        root=v.bisect_root(.6,2.49,2.50)
        self.assertTrue(2.49<root<2.50)
        self.assertLess(v.mode(2.49,.6)*v.mode(2.50,.6),0)
        p=v.packet_filter(2.49,2.50)
        self.assertGreater(p['unnormalized_evaluation_weight'],0)
        self.assertLessEqual(p['conditional_record_plus_probability'],1)
        with self.assertRaises(ValueError): v.bisect_root(.6,2.8,2.9)
        with self.assertRaises(ValueError): v.packet_filter(2,2)

    def test_transport_phase_is_not_bare_reference(self):
        # Exact pointwise linear-algebra witness; packets give the actual
        # normalizable example in test_parent_model_checks.
        k=2.5
        s=[scatter(k,kap) for kap in v.KAPPAS]
        psi=[x.conjugate()/math.sqrt(2) for x in s]  # F+ eigenvector
        r=[abs(v.response(k,kap)) for kap in v.KAPPAS]
        g=[v.response(k,kap)/incoming_phase(k,kap) for kap in v.KAPPAS]
        u=[z/abs(z) for z in g]
        out=[g[i]*psi[i] for i in range(2)]
        out=[x/math.sqrt(inner(out,out).real) for x in out]
        # F+ transported by polar phase u: vector u S* |+>.
        ev=[u[i]*s[i].conjugate()/math.sqrt(2) for i in range(2)]
        correct=abs(inner(ev,out))**2
        analytic=(r[0]+r[1])**2/(2*(r[0]**2+r[1]**2))
        self.assertAlmostEqual(correct,analytic,places=12)
        self.assertLess(correct,.52)
        # Keeping the incoming numerical effect while changing frame is a
        # different event; this is NOT a clock-switch probability identity.
        wrong=abs(inner(psi,out))**2
        self.assertGreater(abs(correct-wrong),.001)

    def test_classical_distinct_turning_and_limits(self):
        self.assertLess(v.volume_max(2.01,.2),2.4)
        self.assertGreater(v.volume_max(2,.6),2.4)
        self.assertAlmostEqual(v.volume_max(2,0),2)
        with self.assertRaises(ValueError): v.mode(0,.2)
        with self.assertRaises(ValueError): v.mode(2,.2,0)

if __name__=='__main__': unittest.main()
