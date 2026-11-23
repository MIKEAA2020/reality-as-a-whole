import math
import unittest
from fractions import Fraction as F
from verification.sphere_closed_plasma_incidence import organization, rhs, run, state


class ClosedPlasmaSphereTests(unittest.TestCase):
    def test_two_fluid_equations_and_total_energy(self):
        e,j=F(2,5),F(1,10)
        vplus=j/2; vminus=-j/2
        vplus_dot=e/2; vminus_dot=-e/2
        self.assertEqual(vplus-vminus,j)
        self.assertEqual(vplus_dot-vminus_dot,e)
        e_dot=-j
        field_dot=e*e_dot
        kinetic_dot=2*vplus*vplus_dot+2*vminus*vminus_dot
        self.assertEqual(field_dot+kinetic_dot,0)
        self.assertEqual(field_dot,-e*j)
        self.assertGreater(e*e/2+j*j/2,0)

    def test_dynamic_weights_remain_positive_and_charge_even(self):
        for k in range(24):
            e,j=state(2*math.pi*k/24)
            for mode in ('flow','energy'):
                w=organization(e,j,.5,mode)
                self.assertGreaterEqual(w,.5-1e-14)
                self.assertLessEqual(w,1.5+1e-14)
                self.assertAlmostEqual(w,organization(-e,-j,.5,mode))
        with self.assertRaises(ValueError): organization(0,0,.5,'flow')
        with self.assertRaises(ValueError): organization(1,1,1,'flow')

    def test_bloch_coordinates_and_flow(self):
        for t in [0,.37,1.2,2.8]:
            e,j=state(t)
            nx,ny,nz=e/.1,j/.1,0
            self.assertAlmostEqual(nx*nx+ny*ny+nz*nz,1)
            self.assertAlmostEqual(2*nx*ny,math.sin(2*t))
            self.assertAlmostEqual(rhs([e,j,0,0,0],.5)[2],-.01*math.sin(2*t)/2)

    def test_rk4_cycle_endpoints_and_signed_zero_controls(self):
        r=run(steps=1024,amplitude=.1,b=.5)
        self.assertAlmostEqual(r['endpoint_E'],.1,places=10)
        self.assertAlmostEqual(r['endpoint_j'],0,places=10)
        self.assertAlmostEqual(r['unweighted_exchange'],0,places=11)
        self.assertAlmostEqual(r['flow_weighted_exchange'],-math.pi/400,places=10)
        self.assertAlmostEqual(r['energy_weighted_exchange'],0,places=11)
        self.assertLess(r['max_energy_drift'],1e-11)
        opposite=run(steps=1024,amplitude=.1,b=-.5)
        self.assertAlmostEqual(opposite['flow_weighted_exchange'],math.pi/400,places=10)
        plain=run(steps=1024,amplitude=.1,b=0)
        self.assertAlmostEqual(plain['flow_weighted_exchange'],0,places=11)

    def test_rk4_error_decreases(self):
        coarse=abs(run(64)['flow_error'])
        fine=abs(run(128)['flow_error'])
        self.assertGreater(coarse,fine*8)


if __name__=='__main__': unittest.main()
