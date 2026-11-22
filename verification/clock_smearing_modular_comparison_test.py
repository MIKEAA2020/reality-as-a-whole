import unittest
import numpy as np

try:
    from . import clock_smearing_modular_comparison as m
except ImportError:
    import clock_smearing_modular_comparison as m


class ClockSmearingTests(unittest.TestCase):
    def test_reported_example(self):
        r = m.calculate(.25)
        self.assertAlmostEqual(r['sharp_B_yes_given_reading_zero'], 1)
        self.assertLess(r['noisy_B_yes_given_reading_zero'], 1)
        self.assertGreater(r['conditional_system_entropy_nats_noisy'], 0)
        self.assertLess(r['clock_system_holevo_nats_noisy'], r['clock_system_holevo_nats_sharp'])

    def test_all_clock_effects_and_constraint_lifts(self):
        J = m.history_isometry(); C = m.constraint()
        for e in (0, .1, .25, .5, 1):
            F = m.root_effects(e)
            self.assertTrue(np.allclose(sum(sum(row) for row in F), m.I))
            for row in F:
                for f in row:
                    self.assertGreaterEqual(np.linalg.eigvalsh(f).min(), -1e-12)
                    lift = J @ f @ m.dagger(J)
                    self.assertTrue(np.allclose(C @ lift - lift @ C, 0, atol=1e-12))
            m.calculate(e)

    def test_noisy_is_postprocessing_for_every_input(self):
        # Equality of effects establishes it for every density, not only PSI.
        a, b, e = m.root_effects(0), m.root_effects(.25), .25
        for j in range(m.N):
            for k in range(2):
                self.assertTrue(np.allclose(b[j][k], (1-e)*a[j][k]+e*a[(j-1)%m.N][k]))

    def test_invertible_but_not_stochastic_inverse(self):
        e=.25
        mixing = (1-e)*np.eye(m.N) + e*np.roll(np.eye(m.N), 1, axis=0)
        inverse = np.linalg.inv(mixing)
        self.assertTrue(np.allclose(inverse @ mixing, np.eye(m.N)))
        self.assertLess(inverse.min(), 0)
        # The three anchored B-yes effects are linearly independent on the
        # physical sector, so reproducing them for every input forces this
        # unique, non-stochastic inverse. Bare clock marginals are uniform.
        vectors=np.stack([row[0].reshape(-1) for row in m.root_effects(0)],axis=1)
        self.assertEqual(np.linalg.matrix_rank(vectors, tol=1e-12),3)
        self.assertGreater(abs(np.linalg.det(mixing)), .1)

    def test_equivalence_by_relabelling_and_operational_difference(self):
        a=m.joint(0); relabelled=np.roll(a, 1, axis=0)
        self.assertTrue(np.allclose(np.roll(relabelled, -1, axis=0), a))
        b=m.joint(.25)
        self.assertGreater(np.max(np.abs(b-a)), .01)
        # No permutation of noisy outcomes has the sharp pure conditional B=1.
        self.assertLess(np.max(b[:,0] / b.sum(axis=1)), 1-1e-5)

    def test_marginal_and_backreaction_depend_on_instrument(self):
        original=m.history_isometry() @ m.PSI
        rho=np.outer(original, original.conj())
        self.assertTrue(np.allclose(m.partial_system(rho), m.TAU))
        for e in (0, .25, 1):
            out=m.postmeasurement(e)
            self.assertTrue(np.allclose(m.partial_system(out), m.TAU))
            self.assertAlmostEqual(np.trace(m.constraint() @ out).real,
                                   4/3*(1-np.sqrt(e*(1-e))))
        # Same POVM, different instrument: measure-and-prepare clock |0>.
        # It preserves the system marginal but has a different global poststate.
        out=np.kron(m.projectors()[0],m.TAU)
        self.assertTrue(np.allclose(m.partial_system(out),m.TAU))
        self.assertFalse(np.allclose(out,m.postmeasurement(.25)))

    def test_same_povm_can_have_different_disturbance(self):
        e=.25
        # Sharp readout followed by a classical noisy label has the same
        # effects as the Lueders POVM, but fully dephases clock coherences.
        for j in range(m.N):
            k1=np.sqrt(1-e)*m.projectors()[j]
            k2=np.sqrt(e)*m.projectors()[(j-1)%m.N]
            self.assertTrue(np.allclose(m.dagger(k1)@k1 + m.dagger(k2)@k2,
                                        m.effects(e)[j]))
        self.assertFalse(np.allclose(m.postmeasurement(0),m.postmeasurement(e)))
        self.assertAlmostEqual(np.trace(m.constraint() @ m.postmeasurement(0)).real, 4/3)

    def test_bad_noise_and_density(self):
        with self.assertRaises(ValueError): m.effects(-.01)
        with self.assertRaises(ValueError): m.entropy(np.diag([1.1,-.1,0]))

if __name__ == '__main__': unittest.main()
