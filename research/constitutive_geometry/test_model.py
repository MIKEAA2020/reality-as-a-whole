from fractions import Fraction as F
import math
import unittest
from model import (Family, packet, fisher, pushforward, deterministic_channel,
                   coordinate_pullback, matmul, transpose, quadratic, difference,
                   psd_two, noisy_monitor, independent_repetitions, packet_distance)
from workspace_adapter import workspace as w, response_family

ZERO = ((F(0), F(0)), (F(0), F(0)))

class GeometryTests(unittest.TestCase):
    def setUp(self):
        self.theta = (F(1,4), F(1,3))
        self.p = packet(self.theta)
        self.g = fisher(self.p)

    def test_normalization_and_derivatives(self):
        self.assertEqual(sum(self.p.probabilities.values()), 1)
        self.assertEqual(tuple(sum(d[j] for d in self.p.derivatives.values()) for j in range(2)), (0,0))

    def test_exact_product_metric(self):
        self.assertEqual(self.g, ((F(16,3), F(0)), (F(0), F(9,2))))

    def test_formula_over_rational_grid(self):
        for x in (F(1,5), F(1,2), F(4,5)):
            for y in (F(1,7), F(2,3), F(6,7)):
                self.assertEqual(fisher(packet((x,y))), ((1/(x*(1-x)),F(0)),(F(0),1/(y*(1-y)))))

    def test_boundaries_rejected(self):
        for theta in ((0,F(1,2)),(1,F(1,2)),(F(1,2),-1)):
            with self.assertRaises(ValueError): packet(theta)

    def test_bad_normalization_rejected(self):
        with self.assertRaises(ValueError): Family({0:F(1,2)}, {0:(0,)})

    def test_bad_derivative_rejected(self):
        with self.assertRaises(ValueError): Family({0:F(1)}, {0:(1,)})

    def test_singular_support_rejected(self):
        with self.assertRaises(ValueError): Family({0:F(0),1:F(1)}, {0:(1,),1:(-1,)})

    def test_mixed_coordinate_transform(self):
        j = ((F(1,2),F(1,2)),(F(1,2),F(-1,2)))
        gnew = fisher(coordinate_pullback(self.p,j))
        self.assertEqual(gnew, ((F(59,24),F(5,24)),(F(5,24),F(59,24))))
        self.assertEqual(gnew, matmul(matmul(transpose(j),self.g),j))

    def test_line_element_invariant(self):
        j = ((F(1,2),F(1,2)),(F(1,2),F(-1,2)))
        v = (F(1,10),F(1,20))
        old = tuple(sum(row[k]*v[k] for k in range(2)) for row in j)
        self.assertEqual(quadratic(fisher(coordinate_pullback(self.p,j)),v), quadratic(self.g,old))

    def test_angular_chart_is_flat(self):
        for t in ((F(1,4),F(1,3)),(F(2,5),F(4,7))):
            g = fisher(packet(t))
            derivative = [math.sqrt(float(v*(1-v))) for v in t]
            self.assertAlmostEqual(float(g[0][0])*derivative[0]**2,1.)
            self.assertAlmostEqual(float(g[1][1])*derivative[1]**2,1.)
            self.assertEqual(g[0][1],0)

    def test_geodesic_formula(self):
        a, b = (F(1,4),F(1,4)),(F(3,4),F(3,4))
        self.assertAlmostEqual(packet_distance(a,b),math.sqrt(2)*math.pi/3)
        self.assertEqual(packet_distance(a,a),0.)
        self.assertEqual(packet_distance(a,b),packet_distance(b,a))

    def test_faithful_copy_adds_no_information(self):
        copy = deterministic_channel(self.p,lambda o:(o[0],o[1],o[0]))
        self.assertEqual(fisher(copy),self.g)

    def test_copy_interpretation_as_independent_is_wrong(self):
        p, d = {}, {}
        for (a,b), po in self.p.probabilities.items():
            for z in (0,1):
                pz = self.theta[0] if z else 1-self.theta[0]
                p[a,b,z] = po*pz
                da, db = self.p.derivatives[a,b]
                d[a,b,z] = (da*pz+po*(1 if z else -1),db*pz)
        independent = fisher(Family(p,d))
        self.assertEqual(independent[0][0],2*self.g[0][0])
        self.assertEqual(independent[1][1],self.g[1][1])

    def test_noisy_copy_joint_law_adds_no_information(self):
        for error in (F(0),F(1,5),F(1,2),F(1)):
            self.assertEqual(fisher(noisy_monitor(self.p,error)),self.g)

    def test_monitor_only_contracts(self):
        monitor = deterministic_channel(noisy_monitor(self.p,F(1,4)),lambda o:o[2])
        gm = fisher(monitor)
        self.assertEqual(gm,((F(16,15),F(0)),(F(0),F(0))))
        self.assertTrue(psd_two(difference(self.g,gm)))

    def test_fully_noisy_monitor_is_null(self):
        monitor = deterministic_channel(noisy_monitor(self.p,F(1,2)),lambda o:o[2])
        self.assertEqual(fisher(monitor),ZERO)

    def test_erasure_is_null(self):
        self.assertEqual(fisher(deterministic_channel(self.p,lambda _:None)),ZERO)

    def test_coarsegrain_one_component(self):
        ga = fisher(deterministic_channel(self.p,lambda o:o[0]))
        self.assertEqual(ga,((F(16,3),F(0)),(F(0),F(0))))

    def test_parity_channel_contracts(self):
        gp = fisher(deterministic_channel(self.p,lambda o:o[0]^o[1]))
        self.assertTrue(psd_two(difference(self.g,gp)))
        self.assertEqual(gp[0][0]*gp[1][1]-gp[0][1]**2,0)

    def test_informationally_complete_noise_not_scalar_metric(self):
        # Parameter identifiability is not physical reversibility of a channel.
        kernel = {(a,b): {(a,b): F(3,4), (1-a,b): F(1,4)}
                  for a,b in self.p.probabilities}
        measured = pushforward(self.p,kernel)
        noisy_g = fisher(measured)
        self.assertEqual(noisy_g, ((F(16,15),F(0)),(F(0),F(9,2))))
        pz = sum(p for (z,b),p in measured.probabilities.items() if z == 1)
        py = sum(p for (z,b),p in measured.probabilities.items() if b == 1)
        self.assertEqual((pz-F(1,4))/F(1,2),self.theta[0])
        self.assertEqual(py,self.theta[1])
        self.assertNotEqual(noisy_g[0][0]/self.g[0][0],noisy_g[1][1]/self.g[1][1])
        self.assertTrue(psd_two(difference(self.g,noisy_g)))

    def test_general_stochastic_kernel_contraction(self):
        for k in (2,3,5):
            kernel = {o:{0:F(1+o[0]+o[1],k+4),1:1-F(1+o[0]+o[1],k+4)}
                      for o in self.p.probabilities}
            self.assertTrue(psd_two(difference(self.g,fisher(pushforward(self.p,kernel)))))

    def test_outcome_renaming_is_invariant(self):
        self.assertEqual(fisher(deterministic_channel(self.p,lambda o:('renamed',1-o[1],1-o[0]))),self.g)

    def test_independent_trials_scale_information(self):
        for n in (1,2,3):
            gn = fisher(independent_repetitions(self.p,n))
            self.assertEqual(gn,tuple(tuple(n*v for v in row) for row in self.g))

    def test_bad_kernel_rejected(self):
        with self.assertRaises(ValueError):
            pushforward(self.p,{o:{0:F(1,2)} for o in self.p.probabilities})

    def test_reflection_symmetry_does_not_fix_quality(self):
        reflected = packet((1-self.theta[0],self.theta[1]))
        self.assertNotEqual(reflected.probabilities,self.p.probabilities)
        self.assertEqual(fisher(reflected),self.g)

    def test_singular_pullback_is_not_a_chart(self):
        j = ((F(1),F(0)),(F(0),F(0)))
        self.assertEqual(fisher(coordinate_pullback(self.p,j)),((F(16,3),F(0)),(F(0),F(0))))

class WorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.p = packet((F(1,4),F(1,3)))
        self.g = fisher(self.p)

    def test_realized_action_protocol(self):
        self.assertEqual(fisher(response_family(self.p)),self.g)

    def test_report_off_retains_action_geometry(self):
        self.assertEqual(fisher(response_family(self.p,config=w.Config(report=False))),self.g)
        self.assertEqual(fisher(response_family(self.p,'report',config=w.Config(report=False))),ZERO)

    def test_distribution_off_erases_action_not_report(self):
        cfg = w.Config(distribute=False)
        self.assertEqual(fisher(response_family(self.p,'action',cfg)),ZERO)
        self.assertEqual(fisher(response_family(self.p,'report',cfg)),self.g)

    def test_passive_monitor_override_has_no_action_effect(self):
        self.assertEqual(response_family(self.p,override_monitor=True),response_family(self.p))

    def test_passive_monitor_still_has_same_metric(self):
        self.assertEqual(fisher(response_family(self.p,'monitor')),self.g)
        self.assertEqual(fisher(response_family(self.p,'monitor',override_monitor=True)),self.g)

    def test_workspace_intervention_changes_consumers(self):
        a = w.step(w.State(),force_workspace=w.Content('visual',0))
        b = w.step(w.State(),force_workspace=w.Content('visual',1))
        self.assertNotEqual(a.state.memory,b.state.memory)
        self.assertNotEqual(a.action,b.action)
        self.assertNotEqual(a.comparison,b.comparison)

    def test_monitor_intervention_does_not_change_consumers(self):
        proposals = (w.Proposal(w.Content('visual',1)),)
        a = w.step(w.State(),proposals)
        b = w.step(w.State(),proposals,force_monitor=w.Content('visual',0))
        self.assertEqual(w.signature(a),w.signature(b))
        self.assertNotEqual(a.monitor,b.monitor)

if __name__ == '__main__':
    unittest.main()
