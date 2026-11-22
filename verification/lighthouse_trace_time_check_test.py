import math
import unittest

try:
    from . import lighthouse_trace_time_check as c
except ImportError:
    import lighthouse_trace_time_check as c


class TraceTimeTests(unittest.TestCase):
    def test_controls(self):
        r=c.run()
        self.assertTrue(r['trace_modular_flow_fixes_X'])
        self.assertAlmostEqual(r['nontracial_modular_flow_X_off_diagonal'][1],1)
        self.assertAlmostEqual(r['sample_state_entropy_before'],r['sample_state_entropy_after'])
        self.assertNotEqual(*r['distinct_commutative_states_same_trivial_flow'])

    def test_trace_flow_identity_at_several_times(self):
        a=[[.3,.7j],[-.7j,.8]]
        for t in (-8,0,math.pi,10):
            self.assertLess(c.diff(c.conj(c.traceflow(t),a),a),1e-13)

    def test_nontracial_state_produces_nontrivial_inner_flow(self):
        x=[[0,1],[1,0]]
        t=math.pi/(2*math.log(3))
        self.assertGreater(c.diff(c.conj(c.stateflow(t),x),x),1)

    def test_entropy_invariant_for_other_state(self):
        rho=[[.6,.2],[.2,.4]]
        for t in (0,.1,2,10):
            self.assertAlmostEqual(c.qubit_entropy(c.conj(c.stateflow(t),rho)),c.qubit_entropy(rho),places=13)

    def test_reject_non_density(self):
        with self.assertRaises(ValueError):c.qubit_entropy([[1.1,0],[0,-.1]])
        with self.assertRaises(ValueError):c.qubit_entropy([[1,1],[0,0]])

if __name__=='__main__':unittest.main()
