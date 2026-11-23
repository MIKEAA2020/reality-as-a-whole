import math
import unittest
import numpy as np
from verification import energy_flow_locked_incidence as model


class EnergyFlowLockedIncidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full=[model.run(n) for n in (64,128,256)]
        cls.partial=[model.run(n,end=1.1) for n in (64,128,256)]

    def test_maxwell_and_poynting_in_declared_external_source(self):
        A=.1; t=.63; x=np.linspace(0,2*np.pi,256,endpoint=False)
        E=1+A*np.sin(t)*np.cos(2*x)
        B=-2*A*np.cos(t)*np.sin(2*x)
        dtE=A*np.cos(t)*np.cos(2*x)
        dxE=-2*A*np.sin(t)*np.sin(2*x)
        dtB=2*A*np.sin(t)*np.sin(2*x)
        dxB=-4*A*np.cos(t)*np.cos(2*x)
        j=3*A*np.cos(t)*np.cos(2*x)
        np.testing.assert_allclose(dtB+dxE,0,atol=1e-15)
        np.testing.assert_allclose(dtE+dxB+j,0,atol=1e-15)
        np.testing.assert_allclose(E*dtE+B*dtB+dxE*B+E*dxB,-j*E,atol=1e-15)

    def test_full_cycle_alignment_and_relative_flow_contrast(self):
        for r in self.full:
            self.assertAlmostEqual(r['aligned_weighted_exchange'],0,places=10)
            self.assertAlmostEqual(r['aligned_final_weighted_energy'],r['initial_weighted_energy'],places=10)
            self.assertAlmostEqual(r['moving_final_weighted_energy'],r['initial_weighted_energy'],places=12)
            self.assertAlmostEqual(r['moving_weighted_exchange'],-.12*math.pi**2,places=11)
            self.assertAlmostEqual(r['moving_weighted_exchange']+r['moving_marker_correction'],0,places=11)
            self.assertAlmostEqual(r['aligned_incidence_integral'],4*math.pi**2,places=9)
            self.assertGreater(r['min_N_sampled'],.4)
            self.assertGreater(r['min_chi_sampled'],.59)
            self.assertLess(r['max_energy_speed_sampled'],.4)

    def test_nontrivial_partial_interval_balance_convergence(self):
        residuals=[abs(r['aligned_balance_residual']) for r in self.partial]
        self.assertGreater(residuals[0]/residuals[1],14)
        self.assertGreater(residuals[1]/residuals[2],14)
        self.assertLess(residuals[1]/residuals[2],18)
        for r in self.partial:
            self.assertLess(r['aligned_weighted_exchange'],-.3)
            self.assertAlmostEqual(r['moving_balance_residual'],0,places=10)

    def test_incidence_current_conserves_total_count(self):
        for r in self.full+self.partial:
            self.assertAlmostEqual(r['aligned_final_number'],2*math.pi,places=11)

    def test_energy_flux_speed_and_null_edge(self):
        E=np.array([1.,0.,0.]); B=np.array([0.,1.,0.])
        u=(E@E+B@B)/2; S=np.cross(E,B)
        self.assertAlmostEqual(u*u-S@S,0)
        self.assertAlmostEqual(np.linalg.norm(S)/u,1)
        B=B/2; u=(E@E+B@B)/2; S=np.cross(E,B)
        self.assertGreater(u*u-S@S,0)
        self.assertLess(np.linalg.norm(S)/u,1)

    def test_invalid_inputs(self):
        for kw in ({'n':8},{'A':0},{'a':1},{'end':0},{'cfl':0}):
            with self.assertRaises(ValueError): model.run(**kw)


if __name__=='__main__': unittest.main()
