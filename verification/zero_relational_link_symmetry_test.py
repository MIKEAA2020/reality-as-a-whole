"""Frame-gauge orbit theorem, continuum weights and symmetry meta-controls."""
import math
import unittest
import numpy as np
from scipy.integrate import quad
from verification.zero_spherical_invariant_echo import unit,rodrigues,angle
from verification.zero_relational_link_symmetry import (
    relational,gauge,orbit_transport,density,inverse_flow,forward_flow,
    change_angle,conjugated_rotation,
)
from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_coherent_clock_angular_history import quantum_echo_checkpoints,apparatus_overlap
from verification.zero_clock_finite_reservoir_reuse_test import Q
from verification.zero_dressed_history_pair import encode_pair,from_anchor,bin_at,apparatus_prefix
from verification.zero_persistent_sphere_subject_selection_test import norm2


def pairdiff(a,b):return sum(norm2(x-y) for x,y in zip(a,b))


class RelationalLinkSymmetryTests(unittest.TestCase):
    def test_independent_frame_gauge_preserves_true_angle(self):
        rng=np.random.default_rng(160)
        for _ in range(80):
            m=unit(rng.normal(size=3));n=unit(rng.normal(size=3))
            link=rodrigues(rng.normal(size=3),rng.uniform(-3,3))
            a=rodrigues(rng.normal(size=3),rng.uniform(-3,3))
            b=rodrigues(rng.normal(size=3),rng.uniform(-3,3))
            new=gauge(m,n,link,a,b)
            self.assertAlmostEqual(relational(*new),relational(m,n,link),places=12)
            np.testing.assert_allclose(new[2].T@new[2],np.eye(3),atol=1e-12)
            self.assertAlmostEqual(np.linalg.det(new[2]),1.,places=12)
        # If link is incorrectly held fixed, the same independent frame
        # operation generally alters the physical comparison.
        m=np.array([0.,0.,1.]);n=unit([1.,0.,.25]);l=np.eye(3)
        b=rodrigues((0,1,0),.8)
        self.assertGreater(abs(relational(m,b@n,l)-relational(m,n,l)),.1)

    def test_orbits_are_exactly_labeled_by_relative_angle(self):
        rng=np.random.default_rng(161)
        for u in (-1.,-.75,-.25,0.,.45,1.):
            for _ in range(8):
                m=unit(rng.normal(size=3));n0=unit(rng.normal(size=3))
                link=rodrigues(rng.normal(size=3),rng.uniform(-3,3))
                n=link.T@change_angle(m,n0,u) if abs(u)<1 else link.T@(u*m)
                p=unit(rng.normal(size=3));q0=unit(rng.normal(size=3))
                k=rodrigues(rng.normal(size=3),rng.uniform(-3,3))
                q=k.T@change_angle(p,q0,u) if abs(u)<1 else k.T@(u*p)
                a,b=orbit_transport((m,n,link),(p,q,k))
                actual=gauge(m,n,link,a,b)
                for got,want in zip(actual,(p,q,k)):
                    np.testing.assert_allclose(got,want,atol=2e-12)
                self.assertAlmostEqual(np.linalg.det(a),1.,places=12)
                self.assertAlmostEqual(np.linalg.det(b),1.,places=12)
        with self.assertRaises(ValueError):
            orbit_transport(([0,0,1],[1,0,0],np.eye(3)),([0,0,1],[0,0,1],np.eye(3)))

    def test_full_support_gauge_invariant_weights_leave_band_masses(self):
        eps=.7
        intervals=((-1.,-.5),(-.5,0.),(0.,.5),(.5,1.))
        for a,b in intervals:
            mass=quad(lambda u:density(u,eps)/2,a,b,epsabs=1e-13)[0]
            self.assertAlmostEqual(mass,.25,places=12)
        self.assertGreater(min(density(float(u),eps) for u in np.linspace(-1,1,2001)),0)
        for u in np.linspace(-.99,-.01,50):
            self.assertAlmostEqual(density(float(u),eps),density(float(-1-u),eps),places=12)
        second=quad(lambda u:u*u*density(u,eps)/2,-1,1,epsabs=1e-13)[0]
        self.assertAlmostEqual(second,1/3+eps/(2*math.pi**2),places=12)
        self.assertNotAlmostEqual(second,1/3,places=5)
        # Same bin, old record and finite-pair weights; distinct continuum
        # magnitude-squared expectation. Both densities have full support.

    def test_actual_record_pair_clock_states_are_frame_gauge_invariant(self):
        m=unit([0.,0.,1.]);link=rodrigues((1,2,1),.9)
        a=rodrigues((2,1,3),.7);b=rodrigues((1,-1,2),-.8)
        root=output(active_base());cols=((1,),(0,))
        for label in (0,15):
            x=initial(relative_read(root,4,labels=(label,))[0])
            for s in (1,-1):
                _,total,states=quantum_echo_checkpoints(x,s,4)
                for u in (-.75,-.25,.25,.75):
                    n=link.T@np.array([math.sqrt(1-u*u),0.,u])
                    transformed=gauge(m,n,link,a,b)
                    i=bin_at(relational(m,n,link));j=bin_at(relational(*transformed))
                    self.assertEqual(i,j)
                    pair=(states[3][0][i],states[3][1][i])
                    enc=encode_pair(pair,i,s)
                    for t in (0,8,10,19):
                        physical={key:from_anchor(v,t) for key,v in enc.items()}
                        other={key:from_anchor(v,t) for key,v in encode_pair(pair,j,s).items()}
                        self.assertLess(sum(pairdiff(physical[k],other[k]) for k in physical)/total,1e-24)
                        self.assertTrue(all(key[2]+key[3]==0 for key in physical))
                    # Gauge acts on m,n,L only. The actual apparatus operator
                    # and its B control are unaltered because u is unaltered.
                    st=(0 if u>0 else 1,(1,0,1),(0,0,1,0),3,(1,),1)
                    st_gauge=(0 if relational(*transformed)>0 else 1,)+st[1:]
                    self.assertEqual(apparatus_prefix(st,10,cols),apparatus_prefix(st_gauge,10,cols))

    def test_actual_coherent_clock_cross_term_matches_for_both_weights(self):
        x=initial(relative_read(output(active_base()),4,labels=(0,))[0])
        _,total,states=quantum_echo_checkpoints(x,1,4)
        eps=.7;cols=((1,),(0,));unweighted=0j;weighted=0j
        for i,(lo,hi) in enumerate(((-1.,-.5),(-.5,0.),(0.,.5),(.5,1.))):
            pair=(states[3][0][i],states[3][1][i])
            enc=encode_pair(pair,i,1)
            old={k:from_anchor(v,0) for k,v in enc.items()}
            post={k:from_anchor(v,10) for k,v in enc.items()}
            overlap=sum(np.vdot(a,b) for k in old for a,b in zip(old[k],post[k]))
            bbit=1 if i<2 else 0
            apparatus=float(apparatus_overlap(0,10,bbit,cols,Q))
            old_cross=overlap*apparatus/total
            mass=quad(lambda u:density(u,eps)/2,lo,hi,epsabs=1e-13)[0]
            unweighted+=old_cross;weighted+=old_cross*(4*mass)
        self.assertAlmostEqual(unweighted.real,9/256,places=12)
        self.assertAlmostEqual(unweighted.imag,0.,places=12)
        self.assertAlmostEqual(abs(unweighted-weighted),0.,places=12)
        # This pre-clock-normalization overlap survives the q=2 reference
        # trace at t=0,10; it is not only a probability ledger.

    def test_nonuniform_state_can_be_invariant_under_conjugate_action(self):
        eps=.55;m=np.array([0.,0.,1.]);n=unit([.8,.3,.4])
        a=rodrigues((1,2,3),.61);b=rodrigues((2,-1,1),-.73)
        c=rodrigues((1,1,2),-.41);d=rodrigues((3,2,1),.32)
        for u in (-.9,-.5,-.1,.3,.8):
            self.assertAlmostEqual(forward_flow(inverse_flow(u,eps),eps),u,places=12)
            self.assertGreater(density(u,eps),0)
        def invariant(p,q):return math.sqrt(density(angle(p,q),eps))
        self.assertAlmostEqual(conjugated_rotation(invariant,m,n,a,b,eps),invariant(m,n),places=12)
        def wave(p,q):return (1+.4j*p[0]+.3*q[1])
        def first(p,q):return conjugated_rotation(wave,p,q,c,d,eps)
        via=conjugated_rotation(first,m,n,a,b,eps)
        direct=conjugated_rotation(wave,m,n,a@c,b@d,eps)
        self.assertAlmostEqual(abs(via-direct),0.,places=11)
        bare=invariant(a.T@m,b.T@n)
        self.assertGreater(abs(bare-invariant(m,n)),1e-3)
        # This conjugate group is not the same geometrical action on m,n;
        # the weighting cannot be selected by unspecified abstract symmetry.

    def test_radial_flow_preserves_spherical_norm_and_commutes_with_common_rotation(self):
        eps=.65
        # Change of variables h'(u)=density(u); exact L2 Jacobian identity.
        f=lambda u:1+u*u+.2*math.sin(3*u)
        left=quad(lambda u:density(u,eps)*f(inverse_flow(u,eps))/2,-1,1,epsabs=1e-12)[0]
        right=quad(lambda v:f(v)/2,-1,1,epsabs=1e-12)[0]
        self.assertAlmostEqual(left,right,places=12)
        m=unit([.2,.4,1]);n=unit([1.,-.2,.3]);r=rodrigues((1,3,2),.72)
        self.assertTrue(np.allclose(change_angle(r@m,r@n,.3),r@change_angle(m,n,.3),atol=1e-12))

if __name__=='__main__':unittest.main()
