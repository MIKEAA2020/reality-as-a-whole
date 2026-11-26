"""Gauge-quotient geometry and dressed zero-pair kinetic operator."""
from itertools import permutations,product
import math
import unittest
import numpy as np
from scipy.linalg import expm
from verification.zero_spherical_invariant_echo import rodrigues
from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_coherent_clock_angular_history import quantum_echo_checkpoints
from verification.zero_quantum_angular_echo import apply_swap
from verification.zero_dressed_sphere_rotations import build_frames
from verification.zero_dressed_history_pair import encode_pair,from_anchor
from verification.zero_persistent_sphere_subject_selection_test import norm2
from verification.zero_relational_laplacian import (
    generator,weighted_ground_operator,dressed_operator,type_reflection,type_symmetric_generator,
)


def octahedral():
    out=[]
    for p in permutations(range(3)):
        for signs in product((-1.,1.),repeat=3):
            a=np.eye(3)[:,p]@np.diag(signs)
            if np.linalg.det(a)>.5:out.append(a)
    return out


def encoded_diff(a,b):
    return sum(norm2(x-y) for key in a for x,y in zip(a[key],b[key]))


def scaled(a,c):return {key:tuple(c*x for x in pair) for key,pair in a.items()}


class RelationalLaplacianTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.shape,cls.frames,cls.info=build_frames()
        cls.root=output(active_base())

    @classmethod
    def tearDownClass(cls):del cls.frames,cls.root

    def test_one_sided_rotation_fails_to_preserve_gauge_singlets(self):
        group=octahedral();self.assertEqual(len(group),24)
        r=rodrigues((1,2,3),2*math.pi/3)
        projected=sum(a.T@r@a for a in group)/len(group)
        lam=np.trace(r)/3
        np.testing.assert_allclose(projected,lam*np.eye(3),atol=1e-14)
        self.assertAlmostEqual(lam,0.,places=13)
        # On ψ=sqrt(3) m·n this equals gauge averaging after n->R n.
        # ∫|ψ|²=1; its projected part vanishes and all norm leaks from the
        # gauge-invariant vector sector. Density covariance is not enough.
        r=rodrigues((1,2,3),math.pi/2)
        projected=sum(a.T@r@a for a in group)/len(group)
        np.testing.assert_allclose(projected,np.eye(3)/3,atol=1e-14)
        self.assertAlmostEqual(1-(np.trace(r)/3)**2,8/9,places=13)

    def test_finite_spherical_laplacian_and_exact_spectrum(self):
        for n in (4,8,16,24):
            q=generator(n)
            np.testing.assert_allclose(q,q.T,atol=1e-13)
            np.testing.assert_allclose(q@np.ones(n),0,atol=1e-12)
            ev=np.linalg.eigvalsh(-q)
            np.testing.assert_allclose(ev,[l*(l+1) for l in range(n)],atol=2e-11)
            u=-1+(2*np.arange(n)+1)/n
            np.testing.assert_allclose(q@u,-2*u,atol=1e-12)
            self.assertTrue(np.all(q-np.diag(np.diag(q))>=0))
        # The exact finite spectrum follows because Q preserves polynomial
        # degree and has leading eigenvalue -l(l+1), l=0,...,n-1.

    def test_heat_selector_is_positive_unique_and_scale_free(self):
        for n in (4,8,16):
            q=generator(n);p=expm(.7*q)
            self.assertGreater(p.min(),0.)
            np.testing.assert_allclose(p.sum(axis=0),1,atol=1e-12)
            np.testing.assert_allclose(p.sum(axis=1),1,atol=1e-12)
            np.testing.assert_allclose(p@np.ones(n)/n,np.ones(n)/n,atol=1e-12)
            self.assertAlmostEqual(np.linalg.eigvalsh(-q)[1],2.,places=12)
            # Positive connected nearest-neighbor rates force the sole
            # stationary distribution, independent of an overall rate scale.
        # The heat parameter here is a mathematical selector, not external time.

    def test_different_positive_zero_ground_compatible_with_same_coarse_bins(self):
        n=8;q=generator(n);u=-1+(2*np.arange(n)+1)/n
        rho=1+.5*np.cos(2*math.pi*u);f=np.sqrt(rho)
        for i in (0,2,4,6):self.assertAlmostEqual(rho[i]+rho[i+1],2.,places=13)
        h=weighted_ground_operator(q,f)
        np.testing.assert_allclose(h,h.T,atol=1e-13)
        np.testing.assert_allclose(h@f,0,atol=1e-12)
        ev=np.linalg.eigvalsh(h)
        self.assertGreater(ev[1],0)
        self.assertGreater(ev[0],-1e-12)
        self.assertGreater(np.linalg.norm(h@np.ones(n)),.1)
        # Both -Q and H_f are positive and have zero ground; neither gauge
        # invariance nor zero alone selects the free rather than weighted law.

    def test_old_type_reflection_does_not_commute_with_free_kinetic(self):
        q=generator(4);reflection=np.eye(4)[[1,0,2,3]]
        np.testing.assert_array_equal(reflection@reflection,np.eye(4))
        np.testing.assert_allclose(reflection@np.ones(4),np.ones(4))
        self.assertGreater(np.linalg.norm(q@reflection-reflection@q),1)
        # Fixing one uniform state is weaker than a symmetry of the generator.

    def test_symmetrized_kinetic_keeps_uniform_state_and_type_swap(self):
        r=type_reflection(4);q=type_symmetric_generator(4)
        np.testing.assert_allclose(q@r,r@q,atol=1e-14)
        np.testing.assert_allclose(q@np.ones(4),0,atol=1e-14)
        np.testing.assert_allclose(np.linalg.eigvalsh(-q),
                                   [0,6-2*math.sqrt(3),8,6+2*math.sqrt(3)],atol=1e-12)
        self.assertAlmostEqual(q[0,2],2.) # New non-neighbor connection.
        self.assertAlmostEqual(q[1,2],2.)
        self.assertTrue(np.all(q-np.diag(np.diag(q))>=0))
        # Any strictly nearest-neighbor Q commuting with r must have
        # Q[1,2]=Q[0,2]=0, so its left and right halves disconnect.
        for n in (8,16):
            rr=type_reflection(n);qq=type_symmetric_generator(n)
            np.testing.assert_allclose(qq@rr,rr@qq,atol=1e-12)
            np.testing.assert_allclose(qq@np.ones(n),0,atol=1e-12)
            ev=np.linalg.eigvalsh(-qq)
            self.assertGreater(ev[1],1e-8)
            self.assertGreater(qq[0,n//2],0.)

    def test_type_swap_commutator_on_original_constrained_record_subspace(self):
        x=initial(relative_read(self.root,4,labels=(0,))[0])
        for s in (1,-1):
            _,total,states=quantum_echo_checkpoints(x,s,4);rows=states[3]
            # The actual Q/pointer type swap sends each supported bin vector
            # to the reflected bin's actual vector; the pair is lifted through
            # W_i and retains its physical signs rather than being erased.
            for j in (0,1):
                selected=tuple([v if i==j else 0*v for i,v in enumerate(part)] for part in rows)
                swapped=apply_swap(selected,s);target=1-j
                for r in (0,1):
                    self.assertLess(norm2(swapped[r][target]-rows[r][target])/total,1e-23)
            raw=[encode_pair((rows[0][i],rows[1][i]),i,s) for i in range(4)]
            zero=[scaled(raw[i],0) for i in range(4)]
            source=list(zero);source[0]=raw[0]
            reflected=list(zero);reflected[1]=raw[1]
            h_source=dressed_operator(source,10,s,self.frames,self.shape)
            h_reflected=dressed_operator(reflected,10,s,self.frames,self.shape)
            hcoef=(-generator(4))[:,0]
            self.assertLess(sum(encoded_diff(h_source[i],scaled(raw[i],hcoef[i]))
                                for i in range(4))/total,1e-21)
            # Reflecting H|0> transports each actual physical branch, not a
            # coordinate-only label. Its coefficients are permutation times
            # column 0 of -Q, evaluated on the actual encoded record vectors.
            coef=(-generator(4))[:,0][[1,0,2,3]]
            reflected_h=[scaled(raw[i],coef[i]) for i in range(4)]
            error=sum(encoded_diff(h_reflected[i],reflected_h[i]) for i in range(4))
            self.assertAlmostEqual(error/total,8.,places=11)
            self.assertTrue(all(k[2]+k[3]==0 for sector in h_reflected for k in sector))
            # Symmetrized operator yields exact compatibility on the very
            # same actual old-record and gauge-constrained pair subspace.
            sym=-type_symmetric_generator(4)
            sym_ref=dressed_operator(reflected,10,s,self.frames,self.shape,sym)
            expected=[scaled(raw[i],sym[:,0][[1,0,2,3]][i]) for i in range(4)]
            self.assertLess(sum(encoded_diff(sym_ref[i],expected[i]) for i in range(4))/total,1e-21)

    def test_original_echo_pair_has_zero_dressed_kinetic(self):
        for label,s,t in ((0,1,10),(15,-1,8)):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            _,total,states=quantum_echo_checkpoints(x,s,4)
            bins=[]
            for i in range(4):
                anchor=encode_pair((states[3][0][i],states[3][1][i]),i,s)
                bins.append({key:from_anchor(pair,t) for key,pair in anchor.items()})
            out=dressed_operator(bins,t,s,self.frames,self.shape)
            err=sum(sum(norm2(x) for pair in sector.values() for x in pair) for sector in out)
            self.assertLess(err/total,1e-21)
            self.assertTrue(all(key[2]+key[3]==0 for sector in out for key in sector))
            # A nonconstant amplitude of this same physical history is not a
            # zero mode. u itself is an exact eigenvector with eigenvalue 2.
            u=(-.75,-.25,.25,.75)
            excited=[scaled(sector,u[i]) for i,sector in enumerate(bins)]
            result=dressed_operator(excited,t,s,self.frames,self.shape)
            mismatch=sum(encoded_diff(result[i],scaled(excited[i],2)) for i in range(4))
            self.assertLess(mismatch/total,1e-21)

if __name__=='__main__':unittest.main()
