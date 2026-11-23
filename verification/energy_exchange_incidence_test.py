import math
import unittest
import numpy as np
from verification import energy_exchange_incidence as energy
from verification import two_fluid_incidence_dynamics as fluid


class EnergyExchangeIncidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.forward=[energy.integrate(n,1.) for n in (64,128,256)]
        cls.backward=energy.integrate(128,-1.)

    def test_energy_transfer_boundary_identity(self):
        for r in self.forward:
            self.assertAlmostEqual(r['signed_work_integral'],r['field_energy_change'],places=9)
            self.assertLess(r['field_energy_change'],-.003)
            self.assertGreater(r['final_field_energy'],0)

    def test_work_error_decreases_at_fourth_order(self):
        errors=[abs(r['work_identity_error']) for r in self.forward]
        self.assertGreater(errors[0]/errors[1],12)
        self.assertGreater(errors[1]/errors[2],12)

    def test_time_symmetric_interval_and_direction(self):
        future=self.forward[1]; past=self.backward
        self.assertAlmostEqual(future['final_field_energy'],past['final_field_energy'],places=13)
        # The backwards run integrates 0 -> -1; reversing it gives the
        # contribution over -1 -> 0 with the opposite sign.
        self.assertAlmostEqual(future['signed_work_integral']-past['signed_work_integral'],0,places=13)
        self.assertLess(future['negative_incidence_fraction'],1)
        self.assertGreater(future['negative_incidence_fraction'],.9)
        self.assertLess(past['negative_incidence_fraction'],.1)
        mean=(future['negative_incidence_fraction']+past['negative_incidence_fraction'])/2
        self.assertAlmostEqual(mean,.5,delta=.003)

    def test_charge_conjugation_is_even_for_work_odd_for_charge(self):
        y=fluid.evolve(128,end=1)['final']; dx=2*math.pi/128
        z=y[[1,0,3,2,4]].copy(); z[4]*=-1
        h=-(y[0]*y[2]-y[1]*y[3])*y[4]
        hz=-(z[0]*z[2]-z[1]*z[3])*z[4]
        np.testing.assert_allclose(h,hz,atol=1e-15)
        np.testing.assert_allclose(y[0]-y[1],-(z[0]-z[1]),atol=1e-15)
        self.assertAlmostEqual(energy.rate(y,dx),energy.rate(z,dx),places=14)

    def test_unchanged_initial_energy_is_not_zero_total_energy(self):
        r=self.forward[-1]
        self.assertGreater(r['initial_field_energy'],.003)
        self.assertGreater(r['total_incidence'],0)
        self.assertAlmostEqual(r['total_incidence'],4*math.pi,places=11)

    def test_invalid_duration(self):
        with self.assertRaises(ValueError): energy.integrate(64,0)
        with self.assertRaises(ValueError): energy.integrate(64,1,cfl=0)


if __name__=='__main__': unittest.main()
