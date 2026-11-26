"""Record-algebra clocks and effects, with original complex-echo controls."""
from itertools import product
import unittest
import numpy as np

from verification.zero_echo_mode_clock_transport import (
    BASIS,INDEX,COARSE,FINE,PREFIXES,logical_circuit,past_labels,mode_values,
    anchor_projector,forward,clock_shift,anchored_history_projector,write_unitary,
    bare_anchor_projector,instantaneous_history_projector,uniform_history)
from verification.zero_coherent_clock_angular_history import quantum_echo_checkpoints,checkpoint_at
from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_internal_reference_subject_valence_candidates_test import j_project,b_project
from verification.zero_dressed_history_pair import to_anchor,from_anchor
from verification.zero_persistent_sphere_subject_selection_test import norm2


def anchored_zero(pair):return (0*pair[0],pair[1])


def anchored_fine_plus(pair,sign):
    return (0*pair[0],j_project(pair[1],sign))


def direct_past(pair,cp,sign,kind,outcome):
    """Independently construct retrodicted PVM using B,J,R projectors."""
    result=[]
    for r,vec in zip((1,-1),pair):
        out=0*vec
        for b,j in product((1,-1),repeat=2):
            ja,ra=past_labels(cp,b,j,r)
            S,T=mode_values(ja,ra,sign)
            keep=(S==outcome if kind=='coarse' else (S,T)==outcome)
            if keep:out=out+b_project(j_project(vec,j),b)
        result.append(out)
    return tuple(result)


def pair_norm(pair):return sum(norm2(x) for x in pair)
def pair_diff(a,b):return sum(norm2(x-y) for x,y in zip(a,b))


class EchoModeClockTransportTests(unittest.TestCase):
    def test_exact_past_labels_and_complete_pvm(self):
        for cp in range(4):
            suffix=('T','Q','T')[cp:]
            for b,j,r in BASIS:
                final=logical_circuit((b,j,r),suffix)
                self.assertEqual(past_labels(cp,b,j,r),final[1:])
                for sign in (-1,1):
                    s,t=mode_values(*past_labels(cp,b,j,r),sign)
                    self.assertIn(s,COARSE);self.assertIn((s,t),FINE)
        # On R-ready input, the anchor's S=0 is B=- at the start,
        # while the instantaneous initial S=0 event is impossible.
        for b,j in product((1,-1),repeat=2):
            self.assertEqual(mode_values(*past_labels(0,b,j,1),1)[0]==0,b==-1)
            self.assertNotEqual(mode_values(j,1,1)[0],0)
        with self.assertRaises(ValueError):past_labels(4,1,1,1)

    def test_clock_invariant_kraus_projectors_and_twirl(self):
        w=clock_shift();eye=np.eye(160)
        np.testing.assert_allclose(w.T@w,eye,atol=1e-14)
        np.testing.assert_allclose(np.linalg.matrix_power(w,20),eye,atol=1e-14)
        for kind,outs in (('coarse',COARSE),('fine',FINE)):
            projectors=[anchored_history_projector(1,kind,o) for o in outs]
            np.testing.assert_allclose(sum(projectors),eye,atol=1e-14)
            for a,p in enumerate(projectors):
                np.testing.assert_allclose(p@p,p,atol=1e-14)
                np.testing.assert_allclose(w@p,p@w,atol=1e-14)
                for q in projectors[a+1:]:np.testing.assert_allclose(p@q,0,atol=1e-14)
            bare=bare_anchor_projector(1,kind,outs[-1])
            twirl=np.zeros_like(bare);term=bare.copy()
            for _ in range(20):
                twirl+=term;term=w@term@w.T
            np.testing.assert_allclose(twirl,projectors[-1],atol=1e-14)
            self.assertGreater(np.linalg.norm(w@bare-bare@w),1.)
        naive=instantaneous_history_projector(1,'coarse',0)
        self.assertAlmostEqual(np.linalg.norm(w@naive-naive@w),4.)

    def test_history_coherence_and_operational_cost_of_clock_readout(self):
        # Isometry of three orthogonal B/J record categories of the original
        # sign-positive branch; angular branches 2 and 3 share a record mode.
        psi=np.zeros(8);psi[INDEX[-1,-1,1]]=.5;psi[INDEX[-1,1,1]]=.5
        psi[INDEX[1,1,1]]=2**-.5
        h=uniform_history(psi);w=clock_shift()
        np.testing.assert_allclose(w@h,h,atol=1e-14)
        for kind,outs,expected in (('coarse',COARSE,.5),('fine',FINE,3/8)):
            projs=[anchored_history_projector(1,kind,o) for o in outs]
            probs=[float(np.vdot(h,p@h).real) for p in projs]
            self.assertAlmostEqual(sum(x*x for x in probs),expected)
            for p,q in zip(projs,probs):
                if q>1e-12:np.testing.assert_allclose(w@(p@h),p@h,atol=1e-14)
            # Separately reading the 20-state clock dephases its orthogonal
            # ticks, changing fidelity from sum(q²) to sum(q²)/20.
            clock_probs=[]
            for tick in range(20):
                for p in projs:
                    part=(p@h)[8*tick:8*(tick+1)]
                    clock_probs.append(float(np.vdot(part,part).real))
            self.assertAlmostEqual(sum(x*x for x in clock_probs),expected/20)
        # Clock-dephased history is invariant under W by conjugation but is
        # not supported entirely in the W=1 constraint eigenspace.
        constraint=sum(np.linalg.matrix_power(w,k) for k in range(20))/20
        support=0.;dephased=np.zeros((160,160),dtype=complex)
        for tick in range(20):
            localized=np.zeros_like(h)
            localized[8*tick:8*(tick+1)]=h[8*tick:8*(tick+1)]
            dephased+=np.outer(localized,localized.conj())
            support+=float(np.vdot(constraint@localized,constraint@localized).real)
        np.testing.assert_allclose(w@dephased@w.T,dephased,atol=1e-14)
        self.assertAlmostEqual(support,1/20)
        naive=instantaneous_history_projector(1,'coarse',0)
        for tick,expected in ((7,0.),(8,.25),(9,.25),(10,.5)):
            v=h[8*tick:8*(tick+1)]
            inst=naive[8*tick:8*(tick+1),8*tick:8*(tick+1)]
            conditional=float(np.vdot(v,inst@v).real/np.vdot(v,v).real)
            self.assertAlmostEqual(conditional,expected)
        # The non-invariant instantaneous query is not the same relational
        # observable as a transported anchor effect.

    def test_global_ready_pointer_write_preserves_stationary_constraint(self):
        psi=np.zeros(8);psi[INDEX[-1,-1,1]]=.5;psi[INDEX[-1,1,1]]=.5
        psi[INDEX[1,1,1]]=2**-.5
        history=uniform_history(psi);w=clock_shift()
        for kind,outs,expected in (('coarse',COARSE,.5),('fine',FINE,3/8)):
            size=len(outs)+1;u=write_unitary(1,kind)
            np.testing.assert_allclose(u.T@u,np.eye(160*size),atol=1e-14)
            ready=np.zeros(size);ready[0]=1
            written=(u@np.kron(history,ready)).reshape(160,size)
            np.testing.assert_allclose(w@written,written,atol=1e-14)
            self.assertAlmostEqual(np.linalg.norm(written[:,0]),0.)
            overlaps=[np.vdot(history,written[:,i]) for i in range(1,size)]
            self.assertAlmostEqual(sum(abs(v)**2 for v in overlaps),expected)
            for i,o in enumerate(outs,1):
                np.testing.assert_allclose(written[:,i],
                    anchored_history_projector(1,kind,o)@history,atol=1e-14)
            # Ready state is distinguishable from every outcome; this does
            # not construct autonomous switching, locality or energy control.

    def test_full_complex_echo_agrees_with_reduced_past_effects(self):
        root=output(active_base())
        for label,sign in ((0,1),(15,-1)):
            x=initial(relative_read(root,4,labels=(label,))[0])
            _,total,states=quantum_echo_checkpoints(x,sign,4)
            for tick in (7,8,9,10,11,12,13):
                cp=checkpoint_at(tick)
                # Coherent combinations of actual old-carrier branch vectors;
                # the angular labels are not being asserted to be accessible.
                pair=tuple(sum((states[cp][r][i] for i in (0,1,2))) for r in (0,1))
                self.assertAlmostEqual(pair_norm(pair)/total,.75,places=12)
                anch=to_anchor(pair,tick)
                self.assertAlmostEqual(pair_norm(anch)/total,.75,places=12)
                for kind,outcome,projector in (
                    ('coarse',0,lambda v:anchored_zero(v)),
                    ('fine',(0,1),lambda v:anchored_fine_plus(v,sign))):
                    expected=direct_past(pair,cp,sign,kind,outcome)
                    transported=from_anchor(projector(anch),tick)
                    self.assertLess(pair_diff(transported,expected)/total,1e-22)
                    # Evolved conditional vectors, not just their output
                    # probabilities, agree under ideal Lüders transport.
                    self.assertLess(pair_diff(to_anchor(expected,tick),projector(anch))/total,1e-22)
                    expected_mass=.5 if kind=='coarse' else .25
                    self.assertAlmostEqual(pair_norm(expected)/total,expected_mass,places=12)

if __name__=='__main__':unittest.main()
