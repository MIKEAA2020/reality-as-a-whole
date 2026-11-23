import math
import unittest
from verification import organization_energy_gate as gate
from verification import energy_exchange_incidence as energy


class OrganizationEnergyGateTests(unittest.TestCase):
    def test_advected_marker_and_positive_support(self):
        for t in (.2,2.1,7.4):
            for x in (.4,2.2,5.1):
                u,chi,_,dtchi,dxchi=gate.fields(t,x)
                self.assertGreater(u,0)
                self.assertGreater(chi,0)
                self.assertAlmostEqual(dtchi+.5*dxchi,0,places=14)
                self.assertGreater(abs(dtchi)+abs(dxchi),0)

    def test_analytic_weighted_history_and_correction(self):
        out=gate.numerical_integrals()
        self.assertAlmostEqual(out['unweighted'],0,places=12)
        self.assertAlmostEqual(out['weighted'],.12*math.pi**2,places=11)
        self.assertAlmostEqual(out['weighted'],out['correction'],places=11)

    def test_identical_endpoints_for_u_and_chi(self):
        for x in (.2,1.4,4.6):
            a=gate.fields(0,x); b=gate.fields(4*math.pi,x)
            self.assertAlmostEqual(a[0],b[0],places=14)
            self.assertAlmostEqual(a[1],b[1],places=14)

    def test_actual_two_fluid_symmetric_slab_loses_balance(self):
        forward=energy.integrate(128,1)
        backward=energy.integrate(128,-1)
        self.assertAlmostEqual(forward['signed_work_integral']-backward['signed_work_integral'],0,places=12)
        weighted=forward['response_weighted_work_integral']-backward['response_weighted_work_integral']
        self.assertGreater(weighted,.0018)
        self.assertLess(weighted,.0019)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError): gate.fields(0,0,a=1)
        with self.assertRaises(ValueError): gate.fields(0,0,b=1)
        with self.assertRaises(ValueError): gate.numerical_integrals(points=2)


if __name__=='__main__': unittest.main()
