"""Conditional bridge: prior chemistry -> molecular invariant -> clock readout.

Chemistry and clock are joined by an explicitly supplied frozen-snapshot
instrument. This is NOT a chemically coupled clock, energy model, experience,
or an assertion that the actual universe is mirror paired.
"""
import unittest
import numpy as np

from verification.zero_molecular_chirality_amplification_test import (
    FISCHER_L, Params, excess, frame_chirality, material, solve, transform)
from verification.zero_intrinsic_difference_common_constitution_test import centered
from verification.zero_clocked_chirality_history import history, selected, dressing


MIRROR=np.diag([-1.,1.,1.])


def chirality_tags():
    l=frame_chirality(FISCHER_L)
    d=frame_chirality(transform(FISCHER_L,MIRROR,np.zeros(3)))
    return l,d


def probabilities_at_snapshot(y,q=1,reference_reading=2,strength=1.,reference_sign=1):
    """Mixture over species, with the actual clocked histories as instrument.

    A fresh ideal qutrit and clock history are allocated per molecule snapshot;
    reference_sign is a supplied pseudoscalar reference, +1 or -1, which flips
    under active reflection along with the molecule. No chemistry occurs during
    the measurement protocol, and this is not a model of the physical coupling.
    """
    if reference_sign not in (-1,1): raise ValueError('reference sign must be +/-1')
    if not 0<=strength<=1: raise ValueError('strength must be in [0,1]')
    L,D=y[1:3]
    if L<0 or D<0 or L+D<=0: raise ValueError('need nonnegative nonzero population')
    histories=[history(2,q,reference_sign*t,strength) for t in chirality_tags()]
    probs=np.zeros(3); refprob=0.
    for weight,psi in zip((L/(L+D),D/(L+D)),histories):
        # Sum actual squared amplitudes over all old labels and clock readings.
        slice_=psi[:,:,reference_reading,:]
        probs+=weight*np.sum(abs(slice_)**2,axis=(0,1))
        refprob+=weight*np.sum(abs(slice_)**2)
    return refprob,probs/refprob


def mirrored(y):
    z=y.copy();z[1],z[2]=y[2],y[1]
    return z


class ChiralChemistryClockBridgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.y0=np.array([1.,.505,.495,0.,500.,0.])
        cls.times=np.array([0.,5.,10.,20.,40.])
        cls.trajectory=solve(cls.y0,Params(),40.,cls.times)
        cls.mirror_run=solve(mirrored(cls.y0),Params(),40.,cls.times)

    def test_actual_geometry_tags_and_centered_population(self):
        l,d=chirality_tags()
        self.assertAlmostEqual(l,2/3); self.assertAlmostEqual(d,-l)
        for y in self.trajectory.y.T:
            c=centered((y[1],y[2]))
            self.assertAlmostEqual(c[0]+c[1],0,places=13)
            self.assertAlmostEqual(c[0],(y[1]-y[2])/2)
            geometric_mean=(y[1]*l+y[2]*d)/(y[1]+y[2])
            self.assertAlmostEqual(geometric_mean,l*excess(y))
            # Centering is a derived population contrast, not conserved energy.
        self.assertNotAlmostEqual(centered(self.y0[1:3])[0],centered(self.trajectory.y[:,-1][1:3])[0])

    def test_paired_mirror_compartments_and_ledger(self):
        # Equal volume, mirror initial conditions and separately maintained feeds
        # are assumptions; the second compartment is not required by the first.
        for a,b in zip(self.trajectory.y.T,self.mirror_run.y.T):
            np.testing.assert_allclose(b,mirrored(a),atol=1e-9,rtol=1e-9)
            self.assertAlmostEqual((a[1]-a[2])+(b[1]-b[2]),0,places=10)
            self.assertAlmostEqual(excess(a),-excess(b),places=10)
            self.assertAlmostEqual(material(a)+material(b),2*material(self.y0),places=8)
        self.assertGreater(excess(self.trajectory.y[:,-1]),.94)

    def test_actual_clock_history_matches_population_formula(self):
        t=chirality_tags()[0]
        for q,w,pref in ((1,4/5,1/4),(2,3/4,1/2)):
            for y in self.trajectory.y.T:
                p_ref,p=probabilities_at_snapshot(y,q=q)
                e=excess(y)
                expected=np.array([1-w,w*(1+t*e)/2,w*(1-t*e)/2])
                self.assertAlmostEqual(p_ref,pref,places=12)
                np.testing.assert_allclose(p,expected,atol=1e-13)
                self.assertAlmostEqual(p.sum(),1,places=13)
            self.assertEqual(sum(n>=10 for n in selected(2,q,2))/len(selected(2,q,2)),w)

    def test_relative_sign_reflection_and_reference_reversal(self):
        y=self.trajectory.y[:,-1]
        _,p=probabilities_at_snapshot(y,reference_sign=1)
        _,ref_flipped=probabilities_at_snapshot(y,reference_sign=-1)
        _,both_flipped=probabilities_at_snapshot(mirrored(y),reference_sign=-1)
        np.testing.assert_allclose(ref_flipped,p[[0,2,1]],atol=1e-13)
        np.testing.assert_allclose(both_flipped,p,atol=1e-13)
        # A racemate has no mean sign even if the instrument is correlated
        # with the individual hidden species.
        rac=y.copy();rac[1]=rac[2]=(y[1]+y[2])/2
        _,r=probabilities_at_snapshot(rac)
        self.assertAlmostEqual(r[1],r[2],places=13)

    def test_blank_zero_strength_and_reversible_erase(self):
        y=self.trajectory.y[:,-1]
        _,p=probabilities_at_snapshot(y,strength=0.)
        np.testing.assert_allclose(p,[.2,.4,.4],atol=1e-13)
        self.assertNotAlmostEqual(p[0],1.) # write does occur, but conveys no sign
        ready=np.array([1.,0.,0.])
        for t in chirality_tags():
            for tick in (0,9):
                np.testing.assert_allclose(dressing(tick,t)@ready,ready,atol=1e-14)
            written=dressing(10,t)@ready
            self.assertAlmostEqual(written[0],0.)
            np.testing.assert_allclose(dressing(20,t)@ready,written,atol=1e-14)
            np.testing.assert_allclose(dressing(39,t)@ready,written,atol=1e-14)
            np.testing.assert_allclose(dressing(39,t).T@written,ready,atol=1e-14)

    def test_readout_cannot_identify_excess_without_geometry_calibration(self):
        # A differently shaped (but still nondegenerate and positive) labeled
        # tetrahedron has t=1/3. Its pure L population gives the same pointer
        # marginal as a 75:25 L/D population with fixed |t|=2/3. This uses the
        # hypothetical same detector for both, not a molecular force model.
        pts={'H':np.zeros(3),'N':np.array([1.,0.,0.]),
             'C':np.array([0.,1.,0.]),
             'R':np.array([np.sqrt(8/9),0.,1/3])}
        t=frame_chirality(pts)
        self.assertAlmostEqual(t,1/3)
        pure=history(2,1,t)[:,:,2,:]
        pp=np.sum(abs(pure)**2,axis=(0,1));pp/=pp.sum()
        y=np.array([1.,.75,.25,0.,500.,0.])
        _,mixed=probabilities_at_snapshot(y)
        np.testing.assert_allclose(pp,mixed,atol=1e-13)

    def test_two_histories_not_a_measurement_record_dynamics(self):
        # Integration conserves material whether or not the offline readout
        # function is invoked; it does not contain readout backreaction.
        y=self.trajectory.y[:,-1].copy(); copy=y.copy()
        probabilities_at_snapshot(y)
        np.testing.assert_array_equal(y,copy)
        self.assertAlmostEqual(material(y),material(self.y0),places=8)


if __name__=='__main__': unittest.main()
