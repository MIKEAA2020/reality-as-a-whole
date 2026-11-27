"""Focused checks of the conditional Maxwell energy-frame deformation review."""
import unittest
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp


class EnergyFrameReview(unittest.TestCase):
    def test_maxwell_poynting_and_frame_eigenvector(self):
        t, x = sp.symbols('t x', real=True)
        q = sp.Function('q')(t)
        E = 1 + sp.diff(q, t)*sp.cos(2*x)/2
        B = q*sp.sin(2*x)
        j = -(sp.diff(q, t, 2)/2 + 2*q)*sp.cos(2*x)
        self.assertEqual(sp.simplify(sp.diff(B,t)+sp.diff(E,x)), 0)
        self.assertEqual(sp.simplify(sp.diff(E,t)+j+sp.diff(B,x)), 0)
        U, S = (E**2+B**2)/2, E*B
        self.assertEqual(sp.simplify(sp.diff(U,t)+sp.diff(S,x)+j*E), 0)
        v=B/E
        self.assertEqual(sp.simplify(S-v*U-v*(U-v*S)), 0)
        self.assertEqual(sp.simplify(U-v*S-(E**2-B**2)/2), 0)
        self.assertEqual(sp.simplify(S/U-v-B*(E**2-B**2)/(2*E*U)), 0)

    def test_covariant_deformation_sign(self):
        E, B, Et, Ex, Bt, Bx, j = sp.symbols('E B Et Ex Bt Bx j', real=True)
        R=sp.sqrt(E**2-B**2); U=(E**2+B**2)/2; S=E*B
        def derivative(expr, de, db):
            return sp.diff(expr,E)*de+sp.diff(expr,B)*db
        div=derivative(E*R/2,Et,Bt)+derivative(B*R/2,Ex,Bx)
        # u_lower=(-E/R,B/R), so T^{mu nu} partial_mu u_nu.
        deform=(U*derivative(-E/R,Et,Bt)+S*derivative(B/R,Et,Bt)
                +S*derivative(-E/R,Ex,Bx)+U*derivative(B/R,Ex,Bx))
        residual=sp.simplify((-j*R-div-deform).subs({Bt:-Ex, Et:-Bx-j}))
        self.assertEqual(residual,0)

    def test_quartic_coefficient_and_remainder_bound(self):
        t, a, d = sp.symbols('t a d', real=True)
        q = -2*a*sp.cos(t)+d*sp.sin(3*t)
        e = sp.diff(q,t)/2
        j = -(sp.diff(q,t,2)/2+2*q)
        integral = sp.integrate(sp.expand_trig(j*e*q**2),(t,0,2*sp.pi))
        self.assertEqual(sp.simplify(integral-4*sp.pi*a**3*d), 0)
        # For a=d=s<=1/100, |e|<=2.5s and |q|<=3s.
        # Exact rational upper bound on the coefficient of s^4 in the
        # square-root remainder, with sqrt((1+e)^2-B^2)>0.974.
        F=sp.Rational
        bound=9*F(25,4)/(2*F(39,40))+81/(8*F(487,500)**3)
        self.assertLess(bound,41)
        # Integrated remainder <= 4pi² * 5.5 * 41 * s^5.
        self.assertLess(F(902,4000),F(1,2))

    def test_periodic_perturbation_integral_and_frame_dependence(self):
        def integral(n, a, d):
            t=np.arange(n)*2*np.pi/n; x=t.copy(); T=t[:,None]
            C=np.cos(2*x)[None,:]; S=np.sin(2*x)[None,:]
            q=-2*a*np.cos(T)+d*np.sin(3*T)
            qp=2*a*np.sin(T)+3*d*np.cos(3*T)
            qpp=2*a*np.cos(T)-9*d*np.sin(3*T)
            E=1+qp*C/2; B=q*S; j=-(qpp/2+2*q)*C
            self.assertGreater(np.min(E-np.abs(B)),0.7)
            return -np.mean(j*np.sqrt(E**2-B**2))*(2*np.pi)**2
        self.assertAlmostEqual(integral(128,.1,0),0,places=13)
        self.assertAlmostEqual(integral(128,.1,.04),-0.00019927956903697,places=13)
        self.assertAlmostEqual(integral(64,.1,.04),integral(256,.1,.04),places=13)

    def test_original_field_transported_marker_and_boundary(self):
        n=64; x0=2*np.pi*np.arange(n)/n; dx=2*np.pi/n
        chi=1+.4*np.cos(2*x0)
        def fields(t,x):
            E=1+.1*np.sin(t)*np.cos(2*x); B=-.2*np.cos(t)*np.sin(2*x)
            Et=.1*np.cos(t)*np.cos(2*x); Ex=-.2*np.sin(t)*np.sin(2*x)
            Bt=.2*np.sin(t)*np.sin(2*x); Bx=-.4*np.cos(t)*np.cos(2*x)
            R=np.sqrt(E*E-B*B); Rt=(E*Et-B*Bt)/R; Rx=(E*Ex-B*Bx)/R
            h=-.3*np.cos(t)*np.cos(2*x)*R
            return E,B,R,B/E,(Bx*E-B*Ex)/(E*E),h,h-(Et*R+E*Rt+Bx*R+B*Rx)/2
        def evolve(end):
            def rhs(t,z):
                x=z[:n]; J=np.exp(z[n:2*n]); *_,v,vx,h,defm=fields(t,x)
                return np.r_[v,vx,np.sum(chi*J*h)*dx,np.sum(chi*J*defm)*dx]
            z0=np.r_[x0,np.zeros(n+2)]
            z=solve_ivp(rhs,(0,end),z0,rtol=1e-10,atol=2e-11).y[:,-1]
            x=z[:n]; J=np.exp(z[n:2*n]); E,B,R,*_=fields(end,x); E0,B0,R0,*_=fields(0,x0)
            delta=np.sum(chi*(J*E*R-E0*R0))*dx/2
            return z[-2],z[-1],delta,np.max(abs(x-x0)),np.max(abs(J-1))
        exchange,deform,delta,_,_=evolve(1.1)
        self.assertAlmostEqual(exchange,-.36832475,places=7)
        self.assertAlmostEqual(deform,-.29423336,places=7)
        self.assertAlmostEqual(exchange-deform,delta,places=9)
        exchange,deform,delta,displace,jac=evolve(2*np.pi)
        self.assertLess(max(abs(exchange),abs(deform),abs(delta),displace,jac),1e-8)


if __name__=='__main__': unittest.main()
