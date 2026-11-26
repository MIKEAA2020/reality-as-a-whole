"""Gauge-tree/loop and noncyclic clock calculations with old-echo controls."""
import math
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np
from scipy.integrate import quad

from verification.zero_spherical_invariant_echo import unit,rodrigues,bin_index
from verification.zero_three_frame_chirality import (gauge_tree,tree_vectors,invariants,
    tree_gauge_fix,gauge_loop,holonomy,loop_observables,correlated_density)
from verification.zero_noncyclic_chirality_clock import (forward_blocks,local_step,residual,
    sine_envelope,window_history)
from verification.zero_clocked_chirality_history import record_gate,history as cyclic_history
from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_coherent_clock_angular_history import quantum_echo_checkpoints
from verification.zero_dressed_history_pair import encode_pair
from verification.zero_persistent_sphere_subject_selection_test import norm2
from verification.zero_sphere_satake_symmetry_test import average,chirality,mul


def rotation(rng):return rodrigues(rng.normal(size=3),rng.uniform(-math.pi,math.pi))


class ThreeFrameGaugeTests(unittest.TestCase):
    def test_independent_frame_gauge_and_tree_fixing(self):
        rng=np.random.default_rng(930)
        for _ in range(70):
            ns=tuple(unit(rng.normal(size=3)) for _ in range(3));l,k=rotation(rng),rotation(rng)
            rs=tuple(rotation(rng) for _ in range(3));initial=invariants(ns,l,k)
            out=gauge_tree(ns,l,k,rs)
            np.testing.assert_allclose(invariants(*out),initial,atol=2e-14)
            ds,a,b=tree_gauge_fix(ns,l,k)
            np.testing.assert_allclose(a,np.eye(3),atol=1e-14)
            np.testing.assert_allclose(b,np.eye(3),atol=1e-14)
            for x,y in zip(ds,tree_vectors(ns,l,k)):np.testing.assert_allclose(x,y,atol=1e-14)
        # Keeping links fixed while rotating only one frame is NOT the gauge action.
        ns=(np.array([1.,0,0]),np.array([0,1.,0]),np.array([0,0,1.]))
        bad=(ns[0],rodrigues((0,0,1),.4)@ns[1],ns[2])
        self.assertGreater(abs(invariants(ns,np.eye(3),np.eye(3))[0]-invariants(bad,np.eye(3),np.eye(3))[0]),.1)

    def test_induced_action_group_law_and_covariant_vectors(self):
        rng=np.random.default_rng(931)
        for _ in range(30):
            ns=tuple(unit(rng.normal(size=3)) for _ in range(3));l,k=rotation(rng),rotation(rng)
            a=tuple(rotation(rng) for _ in range(3));b=tuple(rotation(rng) for _ in range(3))
            first=gauge_tree(ns,l,k,b);second=gauge_tree(*first,a)
            direct=gauge_tree(ns,l,k,tuple(x@y for x,y in zip(a,b)))
            for got,want in zip((*second[0],second[1],second[2]),(*direct[0],direct[1],direct[2])):
                np.testing.assert_allclose(got,want,atol=2e-14)
            for x,y in zip(tree_vectors(*second),tree_vectors(ns,l,k)):
                np.testing.assert_allclose(x,a[0]@b[0]@y,atol=2e-14)

    def test_loop_holonomy_changes_without_changing_tree_observables(self):
        ds=(np.array([1.,0,0]),np.array([0,1.,0]),np.array([0,0,1.]))
        eye=np.eye(3);loop=rodrigues((0,0,1),math.pi/2)
        np.testing.assert_allclose(invariants(ds,eye,eye),[0,0,0,1],atol=1e-15)
        self.assertAlmostEqual(np.trace(holonomy(eye,eye,eye)),3.)
        self.assertAlmostEqual(np.trace(holonomy(eye,eye,loop)),1.)
        rng=np.random.default_rng(932)
        for _ in range(30):
            rs=tuple(rotation(rng) for _ in range(3));state=gauge_loop(ds,eye,eye,loop,rs)
            np.testing.assert_allclose(invariants(*state[:3]),invariants(ds,eye,eye),atol=2e-14)
            np.testing.assert_allclose(loop_observables(*state),loop_observables(ds,eye,eye,loop),atol=2e-14)
            np.testing.assert_allclose(holonomy(*state[1:]),rs[0]@loop@rs[0].T,atol=2e-14)

    def test_exact_holonomy_moments_and_hidden_correlation(self):
        # SO(3) Haar class angle: (2/pi) sin²(theta/2), 0≤theta≤pi.
        weight=lambda x:2/math.pi*math.sin(x/2)**2
        character=lambda x:1+2*math.cos(x)
        for power,target in ((0,1),(1,0),(2,1)):
            val=quad(lambda x:weight(x)*character(x)**power,0,math.pi,epsabs=1e-13)[0]
            self.assertAlmostEqual(val,target,places=13)
        t=chirality();self.assertEqual(average(mul(t,t)),F(2,9))
        # Density 1+eps*t*chi/3: marginals remain unchanged; E[t*chi]=2eps/27.
        for eps in (-.9,0,.8):
            for tvalue,ch in product((-1.,0.,1.),(-1.,0.,3.)):
                self.assertGreater(correlated_density(tvalue,ch,eps),0)
            self.assertAlmostEqual(eps/3*float(average(mul(t,t))),2*eps/27,places=14)
        with self.assertRaises(ValueError):correlated_density(0,0,1)

    def test_loop_correlation_reaches_the_written_pointer(self):
        # Independent sphere/holonomy quadrature checks the mixed observable,
        # including unchanged one-variable marginals and full-strength POVM.
        nodes,weights=np.polynomial.legendre.leggauss(36)
        u=nodes[:,None,None];v=nodes[None,:,None]
        theta=(nodes[None,None,:]+1)*math.pi/2
        t=np.sqrt(1-u*u)*v;ch=1+2*np.cos(theta)
        measure=(weights[:,None,None]/2)*(weights[None,:,None]/2)*(weights[None,None,:]*np.sin(theta/2)**2)
        eps=.6;rho=1+eps*t*ch/3
        self.assertAlmostEqual(float(np.sum(measure*rho)),1.,places=13)
        self.assertAlmostEqual(float(np.sum(measure*t*rho)),0.,places=13)
        self.assertAlmostEqual(float(np.sum(measure*ch*rho)),0.,places=13)
        cross=float(np.sum(measure*t*ch*rho))
        self.assertAlmostEqual(cross,2*eps/27,places=13)
        for strength in (.25,1.):
            pplus=(1+strength*t)/2;pminus=(1-strength*t)/2
            self.assertAlmostEqual(float(np.sum(measure*pplus*rho)),.5,places=13)
            observed=float(np.sum(measure*ch*(pplus-pminus)*rho))
            self.assertAlmostEqual(observed,2*strength*eps/27,places=13)

    def test_actual_old_echo_pair_and_memory_are_frame_invariant(self):
        root=output(active_base());rng=np.random.default_rng(933)
        for label,s,u in ((0,1,-.75),(15,-1,.25)):
            x=initial(relative_read(root,4,labels=(label,))[0]);_,total,check=quantum_echo_checkpoints(x,s,4)
            n1=np.array([0.,0.,1.]);v=np.array([math.sqrt(1-u*u),0.,u]);p=unit([.2,1,.5]);l,k=rotation(rng),rotation(rng)
            ns=(n1,l.T@v,k.T@p);r=tuple(rotation(rng) for _ in range(3))
            out=gauge_tree(ns,l,k,r);inv=invariants(ns,l,k);inv2=invariants(*out)
            i,j=bin_index(inv[0],4),bin_index(inv2[0],4);self.assertEqual(i,j)
            np.testing.assert_allclose(record_gate(inv[3]),record_gate(inv2[3]),atol=1e-14)
            np.testing.assert_allclose(cyclic_history(2,1,inv[3]),cyclic_history(2,1,inv2[3]),atol=1e-14)
            pair=tuple(row[i] for row in check[3]);e=encode_pair(pair,i,s)
            same=encode_pair(tuple(row[j] for row in check[3]),j,s)
            self.assertEqual(set(e),set(same))
            self.assertLess(sum(sum(norm2(a-b) for a,b in zip(e[key],same[key])) for key in e)/total,1e-24)
            self.assertTrue(all(key[2]+key[3]==0 for key in e))


class NoncyclicClockTests(unittest.TestCase):
    def test_retains_without_wrap_and_preserves_unitarity(self):
        for q,h in product((1,2),(-.8,.2,.9)):
            arr=forward_blocks(100,q,h)
            for i in (0,9,10,19,20,30,50,99):self.assertAlmostEqual(np.linalg.norm(arr[i]),1.,places=13)
            np.testing.assert_allclose(arr[10],arr[30],atol=1e-14)
            np.testing.assert_allclose(arr[20],arr[40],atol=1e-14)
            # On every n≥10 the blank amplitude is zero, without a later erase.
            self.assertAlmostEqual(np.linalg.norm(arr[10:,:,:,0]),0.,places=14)
            self.assertAlmostEqual(np.linalg.norm(arr[:10,:,:,1:]),0.,places=14)
            # Reference shift and physical old carriers are part of every step.
            np.testing.assert_allclose(local_step(arr[9],9,q,h),arr[10],atol=1e-14)

    def test_optimal_finite_support_approximate_constraint(self):
        for n,q,h in product((20,40,80),(1,2),(-.8,.4)):
            v=window_history(n,q,h);self.assertAlmostEqual(np.linalg.norm(v),1.,places=13)
            err=residual(v,q,h)
            self.assertAlmostEqual(err*err,2-2*math.cos(math.pi/(n+1)),places=13)
            uniform=np.ones(n)/math.sqrt(n)
            delta=np.diff(np.r_[0,uniform,0])
            self.assertAlmostEqual(float(np.dot(delta,delta)),2/n,places=14)
            self.assertLessEqual(err*err,2/n+1e-14)
            # N×N Toeplitz Laplacian gives the universal support-limited optimum
            # even when old state amplitudes vary across positions by a unitary.
            m=2*np.eye(n)-np.diag(np.ones(n-1),1)-np.diag(np.ones(n-1),-1)
            self.assertAlmostEqual(np.linalg.eigvalsh(m)[0],err*err,places=13)

    def test_ready_and_record_weights_in_window(self):
        for n in (20,40,80):
            f=sine_envelope(n);v=window_history(n,1,.5)
            self.assertAlmostEqual(float(np.linalg.norm(v[:10])**2),float(sum(f[:10]**2)),places=13)
            self.assertAlmostEqual(float(np.linalg.norm(v[10:])**2),float(sum(f[10:]**2)),places=13)
            self.assertAlmostEqual(np.linalg.norm(v[:10,:,:,1:]),0.,places=14)
            self.assertAlmostEqual(np.linalg.norm(v[10:,:,:,0]),0.,places=14)
        # Normalizable history has finite clock support; there is no claimed
        # post-support conditional probability. Exact stationary bilateral
        # histories require constant slice norm and hence are not in l².

if __name__=='__main__':unittest.main()
