"""Coherent recovery and access limits on the existing clocked echo pointer.

Checks reduced stationary record histories and conditional pointer operations.
No subjective observer, full apparatus, locality or phenomenal identity is
established. Run with OPENBLAS_NUM_THREADS=1 and PYTHONPATH=.arena/python-deps:.
"""
import math
import unittest
import numpy as np

from verification.zero_echo_mode_clock_transport import clock_shift, anchored_history_projector
from verification.zero_sr_echo_intrinsic_access_test import (
    clock_pair, stationary_write, pointer_density, trace_distance, optimal_effect, success)


def eraser_basis(r):
    """Output-plane orthonormal basis; at r=1 the second outcome has zero weight."""
    if not 0 <= r <= 1:
        raise ValueError('overlap must be in [0,1]')
    a, b = math.sqrt((1+r)/2), math.sqrt((1-r)/2)
    return np.array([0.,a,b]), np.array([0.,b,-a])


def written(coefficients, r):
    """Record-history x pointer amplitudes after the actual reduced write."""
    plus, minus = clock_pair()
    state = coefficients[0]*plus + coefficients[1]*minus
    ready = np.array([1.,0.,0.])
    return (stationary_write(r)@np.kron(state,ready)).reshape(160,3)


def compressed(out):
    plus, minus = clock_pair()
    return np.column_stack((plus, minus)).conj().T @ out


def conditional_amplitude(out, pointer_vector):
    return out@pointer_vector.conj()


def copied_environment_state(sign, r):
    """2-branch x pointer x extra binary record, after ideal extra T copy.

    This is an added interaction on the already selected record qubit, not a
    claim about an actual environment. sign=+1/-1 encodes the phase input.
    """
    mp = np.array([0.,1.,0.])
    mm = np.array([0.,r,math.sqrt(1-r*r)])
    state = np.zeros((2,3,2), dtype=complex)
    state[0,:,0] = mp/math.sqrt(2)
    state[1,:,1] = sign*mm/math.sqrt(2)
    return state


class SREchoQuantumEraserTests(unittest.TestCase):
    def test_phase_distinguishability_across_three_interfaces(self):
        for r in (0., .6, 1.):
            outp = written((1/math.sqrt(2), 1/math.sqrt(2)), r)
            outm = written((1/math.sqrt(2), -1/math.sqrt(2)), r)
            self.assertAlmostEqual(abs(np.vdot(outp, outm)), 0.)  # full joint D=1
            ap, am = compressed(outp), compressed(outm)
            self.assertAlmostEqual(trace_distance(ap@ap.conj().T, am@am.conj().T), r)
            self.assertAlmostEqual(trace_distance(outp.T@outp.conj(), outm.T@outm.conj()), 0.)
            # Basis T and pointer marginals both have no information about phase.
            np.testing.assert_allclose(np.diag(ap@ap.conj().T), [.5,.5], atol=1e-14)
            np.testing.assert_allclose(np.diag(am@am.conj().T), [.5,.5], atol=1e-14)

    def test_eraser_outcomes_store_no_T_bit(self):
        for r in (0., .6, 1.):
            u, v = eraser_basis(r)
            self.assertAlmostEqual(np.vdot(u,u).real, 1.)
            self.assertAlmostEqual(np.vdot(v,v).real, 1.)
            self.assertAlmostEqual(abs(np.vdot(u,v)), 0.)
            for vec, probability in ((u,(1+r)/2),(v,(1-r)/2)):
                for minus in (False,True):
                    rho = pointer_density(r,minus)
                    self.assertAlmostEqual(np.vdot(vec,rho@vec).real, probability)

    def test_eraser_kraus_and_corrected_identity_for_all_inputs(self):
        plus, minus = clock_pair()
        basis = np.column_stack((plus,minus))
        z2 = np.diag([1.,-1.])
        w = clock_shift()
        pminus = anchored_history_projector(1,'fine',(0,-1))
        zglobal = np.eye(160)-2*pminus
        np.testing.assert_allclose(w@zglobal, zglobal@w, atol=1e-14)
        for r in (0., .6, 1.):
            u, v = eraser_basis(r)
            first = written((1.,0.),r)
            second = written((0.,1.),r)
            ku = basis.conj().T @ np.column_stack((conditional_amplitude(first,u),
                                                   conditional_amplitude(second,u)))
            kv = basis.conj().T @ np.column_stack((conditional_amplitude(first,v),
                                                   conditional_amplitude(second,v)))
            np.testing.assert_allclose(ku, math.sqrt((1+r)/2)*np.eye(2), atol=1e-14)
            np.testing.assert_allclose(kv, math.sqrt((1-r)/2)*z2, atol=1e-14)
            np.testing.assert_allclose(ku.conj().T@ku + kv.conj().T@kv, np.eye(2), atol=1e-14)
            for rho in (np.array([[1,0],[0,0]],complex),
                        np.array([[.5,.5j],[-.5j,.5]],complex),
                        np.array([[.3,.1],[.1,.7]],complex)):
                restored = ku@rho@ku.conj().T + z2@kv@rho@kv.conj().T@z2
                np.testing.assert_allclose(restored, rho, atol=1e-14)
            # Check physical clock-history vectors, not only the logical map.
            for state in ((1/math.sqrt(2),1j/math.sqrt(2)), (1,0), (0,1)):
                out = written(state,r)
                for vec, correction, prob in ((u,np.eye(160),(1+r)/2),
                                              (v,zglobal,(1-r)/2)):
                    branch = correction@conditional_amplitude(out,vec)
                    np.testing.assert_allclose(w@branch, branch, atol=1e-14)
                    target = math.sqrt(prob)*(state[0]*plus+state[1]*minus)
                    np.testing.assert_allclose(branch,target,atol=1e-14)
        with self.assertRaises(ValueError): eraser_basis(-.1)

    def test_eraser_phase_pair_can_be_recovered_but_not_T_from_outcome(self):
        r=.6
        u,v=eraser_basis(r)
        plus,minus=clock_pair()
        zglobal=np.eye(160)-2*anchored_history_projector(1,'fine',(0,-1))
        for phase in (1,-1):
            target=(plus+phase*minus)/math.sqrt(2)
            out=written((1/math.sqrt(2),phase/math.sqrt(2)),r)
            for pointer, correction, prob in ((u,np.eye(160),.8),(v,zglobal,.2)):
                branch=correction@conditional_amplitude(out,pointer)
                self.assertAlmostEqual(np.vdot(branch,branch).real,prob)
                np.testing.assert_allclose(branch,math.sqrt(prob)*target,atol=1e-14)
        # After correction, the two system states remain orthogonal: perfect
        # phase discrimination, but eraser outcomes alone have no T evidence.
        self.assertAlmostEqual(abs(np.vdot((plus+minus)/math.sqrt(2),
                                          (plus-minus)/math.sqrt(2))),0.)

    def test_T_optimal_pointer_measurement_retains_only_r_phase_distance(self):
        for r in (0.,.6,.9):
            a=pointer_density(r,False)[1:,1:]
            b=pointer_density(r,True)[1:,1:]
            self.assertAlmostEqual(success(a,b,optimal_effect(a,b)),
                                   (1+math.sqrt(1-r*r))/2)
            _, vecs=np.linalg.eigh(a-b)
            outp=compressed(written((1/math.sqrt(2),1/math.sqrt(2)),r))
            outm=compressed(written((1/math.sqrt(2),-1/math.sqrt(2)),r))
            total_phase_distance=0.
            for j in (0,1):
                pointer=np.r_[0.,vecs[:,j]]
                vp=outp@pointer.conj(); vm=outm@pointer.conj()
                unnormalized_diff=np.outer(vp,vp.conj())-np.outer(vm,vm.conj())
                total_phase_distance+=np.abs(np.linalg.eigvalsh(unnormalized_diff)).sum()/2
            self.assertAlmostEqual(total_phase_distance,r)

    def test_extra_copy_is_a_clock_invariant_record_operation(self):
        plus, minus = clock_pair()
        basis = np.column_stack((plus,minus))
        w = clock_shift()
        pm = anchored_history_projector(1,'fine',(0,-1))
        np.testing.assert_allclose(w@pm,pm@w,atol=1e-14)
        for phase in (1,-1):
            out = written((1/math.sqrt(2),phase/math.sqrt(2)),.6)
            # A controlled X writes an initially zero extra T bit: T+ leaves
            # it zero and T- flips it to one. Output indexed system,pointer,E.
            copied = np.stack(((np.eye(160)-pm)@out,pm@out),axis=-1)
            for p in range(3):
                for e in range(2):
                    np.testing.assert_allclose(w@copied[:,p,e],copied[:,p,e],atol=1e-14)
            compressed_copy = np.einsum('is,ipe->spe',basis.conj(),copied)
            np.testing.assert_allclose(compressed_copy,copied_environment_state(phase,.6),atol=1e-14)

    def test_environment_copy_blocks_local_eraser_without_environment_access(self):
        r=.6
        plus=copied_environment_state(1,r)
        minus=copied_environment_state(-1,r)
        # Trace out extra record: the joint original system+pointer states for
        # both phases are equal, so no such local operation can distinguish them.
        a=plus.reshape(6,2); b=minus.reshape(6,2)
        np.testing.assert_allclose(a@a.conj().T,b@b.conj().T,atol=1e-14)
        self.assertAlmostEqual(abs(np.vdot(plus,minus)),0.)  # global D still 1
        z=np.diag([1.,-1.]); restored=np.zeros((2,2),complex)
        for vec, correction in ((eraser_basis(r)[0],np.eye(2)),
                                (eraser_basis(r)[1],z)):
            amp=np.einsum('spe,p->se',plus,vec.conj())
            corrected=correction@amp
            restored += corrected@corrected.conj().T
        np.testing.assert_allclose(restored,np.eye(2)/2,atol=1e-14)
        # Extra environment is an explicitly added perfect T copy. Access to
        # and reversal of that record would be a different, global protocol.


if __name__ == '__main__':
    unittest.main()
