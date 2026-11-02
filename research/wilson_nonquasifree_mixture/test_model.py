import math
import unittest
import model as m
class NonquasifreeTests(unittest.TestCase):
    def test_01_mode_density_normalized(self):self.assertAlmostEqual(m.w.car.trace(m.mode_density()).real,1)
    def test_02_mode_density_positive(self):self.assertTrue(all(v.real>=0 for v in m.mode_density().values()))
    def test_03_same_mode_covariance(self):
        car=m.w.car;a,b=m.mode_density(),m.mode_density(quasifree=True)
        for i in (0,1):
            for j in (0,1):
                op=car.mul(car.adjoint(car.annihilator(2,j)),car.annihilator(2,i))
                self.assertAlmostEqual(m.w.cell.expectation(op,a),m.w.cell.expectation(op,b))
    def test_04_mode_four_point_differs(self):
        car=m.w.car;op=car.mul(car.number(2,0),car.number(2,1));e=m.w.cell.expectation
        self.assertAlmostEqual(e(op,m.mode_density()),0);self.assertAlmostEqual(e(op,m.mode_density(quasifree=True)),.25)
    def test_05_fixed_packet_number(self):
        car=m.w.car;N=car.add(car.number(2,0),car.number(2,1));Nminus=car.add(N,car.scale(-1,car.identity(4)));var=car.mul(Nminus,Nminus)
        self.assertAlmostEqual(m.w.cell.expectation(var,m.mode_density()),0);self.assertGreater(m.w.cell.expectation(var,m.mode_density(quasifree=True)).real,0)
    def test_06_phase_average_local_density(self):
        a,n,x,t=.02,2,.4,.3;car=m.w.car
        rho=car.scale(.5,car.add(m.p.density_matrix(m.c.covariance(a,n,x,t,phase=0)),m.p.density_matrix(m.c.covariance(a,n,x,t,phase=math.pi))))
        self.assertLess(car.error(rho,m.density(a,n,x,t)),1e-12)
    def test_07_same_local_covariance(self):
        cov=m.covariance(.02,2,.4,.3);rho=m.density(.02,2,.4,.3);car=m.w.car
        for i in (0,1):
            for j in (0,1):self.assertAlmostEqual(m.w.cell.expectation(car.mul(car.adjoint(car.annihilator(2,j)),car.annihilator(2,i)),rho),cov[i][j])
    def test_08_local_density_not_wick_density(self):self.assertGreater(m.w.car.error(m.density(.02,4,.4,.3),m.quasifree_density(.02,4,.4,.3)),1e-9)
    def test_09_actual_current(self):
        a,n,x,t=.02,2,.4,.3;e=m.w.cell.expectation;op=m.w.cell.current_product(a);ref=m.p.density_matrix(m.w.same_chirality_covariance(a,n))
        self.assertAlmostEqual((e(op,m.density(a,n,x,t))-e(op,ref)).real,m.current(a,n,x,t),places=9)
    def test_10_quasifree_current(self):
        a,n,x,t=.02,2,.4,.3;e=m.w.cell.expectation;op=m.w.cell.current_product(a);ref=m.p.density_matrix(m.w.same_chirality_covariance(a,n))
        self.assertAlmostEqual((e(op,m.quasifree_density(a,n,x,t))-e(op,ref)).real,m.quasifree_current(a,n,x,t),places=9)
    def test_11_connected_identity(self):self.assertAlmostEqual(m.current(.02,4,.4,.3)-m.quasifree_current(.02,4,.4,.3),m.connected_current(.02,4,.4,.3))
    def test_12_connected_nonzero(self):self.assertLess(m.connected_current(.02,4,.4,.3),0)
    def test_13_connected_bound(self):
        for n in (8,16,32):self.assertLessEqual(abs(m.connected_current(1/n**2,n,.7,.3)),m.connected_bound(1/n**2,n))
    def test_14_connected_quadratic_decay(self):self.assertLess(abs(m.connected_current(1/32**2,32,.7,.3)),abs(m.connected_current(1/8**2,8,.7,.3))/12)
    def test_15_full_bound(self):
        for n in (8,16,32):self.assertLessEqual(abs(m.current(1/n**2,n,.7,.3)-m.target(.7,.3)),m.error_bound(1/n**2,n,.3))
    def test_16_limit(self):self.assertLess(abs(m.current(1/128**2,128,.7,.3)-m.target(.7,.3)),.001)
    def test_17_quasifree_same_limit(self):self.assertLess(abs(m.quasifree_current(1/128**2,128,.7,.3)-m.target(.7,.3)),.001)
    def test_18_local_energy(self):self.assertAlmostEqual(m.local_energy(.0001,.7,.3),m.target(.7,.3),places=6)
    def test_19_mixed_not_pure(self):
        rho=m.mode_density();self.assertLess(m.w.car.trace(m.w.car.mul(rho,rho)).real,1)
    def test_20_vacuum_endpoint(self):self.assertEqual(m.current(.02,4,.4,.3,theta=0),0)
    def test_21_swap_endpoint_quasifree(self):self.assertAlmostEqual(m.current(.02,4,.4,.3,theta=math.pi/2),m.quasifree_current(.02,4,.4,.3,theta=math.pi/2))
    def test_22_transport(self):self.assertAlmostEqual(m.target(.7,.3),m.target(.4,0))
    def test_23_phase_averaged_current(self):self.assertAlmostEqual(m.current(.02,4,.4,.3),.5*(m.c.current(.02,4,.4,.3,phase=0)+m.c.current(.02,4,.4,.3,phase=math.pi)))
    def test_24_validation(self):
        for call in (lambda:m.current(.1,0,0),lambda:m.current(.8,2,0),lambda:m.probability(-1),lambda:m.probability(float('nan'))):
            with self.assertRaises(ValueError):call()
if __name__=='__main__':unittest.main()
