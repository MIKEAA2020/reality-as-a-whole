"""Independent rotations dressed by the actual coherent echo record."""
from itertools import product
import unittest
import numpy as np

from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read,I,kron
from verification.zero_relational_chirality_report_test import initial,apply64
from verification.zero_contextual_sign_symmetry_and_dressed_report_test import valid
from verification.zero_upstream_invariant_internal_history_test import factorization
from verification.zero_internal_contextual_reference_test import gauge_history,B
from verification.zero_conserving_sphere_handedness_report_test import bob_action
from verification.zero_persistent_sphere_subject_selection_test import norm2
from verification.zero_quantum_angular_echo import embed
from verification.zero_spherical_invariant_echo import symmetric_density,rodrigues,angle
from verification.zero_dressed_sphere_rotations import (
    build_frames,swap_frames,v_sector,transport,old_exchange,dressed_pullback,sector,
)


def pair_norm(pair):return sum(norm2(x) for x in pair)
def pair_diff(a,b):return sum(norm2(x-y) for x,y in zip(a,b))
def from_bin(rows,i):return rows[0][i],rows[1][i]


class DressedSphereRotationsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.shape,cls.frames,cls.info=build_frames()
        cls.root=output(active_base())

    @classmethod
    def tearDownClass(cls):
        del cls.frames,cls.root

    def test_common_gram_matrix_and_orthonormal_record_frames(self):
        info=self.info
        self.assertEqual(info['rank'],7)
        self.assertLess(max(info['gram_errors']),1e-12)
        self.assertLess(info['cross_error'],1e-12)
        np.testing.assert_allclose(info['eigenvalues'][-7:],
            [1/4,1/4,7/6,7/6,37/12,37/12,7],atol=1e-11)
        for frame in self.frames:
            np.testing.assert_allclose(frame.conj().T@frame,np.eye(7),atol=1e-12)
        np.testing.assert_allclose(self.frames[1].conj().T@self.frames[2],0,atol=1e-12)
        # Frame 0 is R+; frames 1 and 2 are R-, J+ and R-, J-.

    def test_frame_maps_preserve_original_gauge_and_valid_sector(self):
        # valid is expressed in the canonical spin basis, whereas apply64
        # acts on the original physical axes. Undo the basis conversion.
        t=kron(factorization(),I,I,I);physical_valid=t@valid@t.conj().T
        for frame in self.frames:
            for i in range(frame.shape[1]):
                v=frame[:,i].reshape(self.shape)
                # The negative-pointer swap uses S-conjugated frames.
                for w in (v,old_exchange((v,v))[0]):
                    scale=norm2(w)
                    self.assertLess(norm2(gauge_history(w)-w)/scale,1e-22)
                    self.assertLess(norm2(apply64(physical_valid,w)-w)/scale,1e-22)
        # A unitary swapping frames inside the gauge+ and valid subspaces,
        # and acting as identity on their orthogonal complement, commutes
        # with those involutions/projectors on the full old carrier.

    def test_all_16_source_vectors_transport_as_one_family(self):
        for label in range(16):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            _,v,rows=embed(x,1,4);total=norm2(v)
            positive=from_bin(rows,2)
            for target,i in ((-.75,0),(-.25,1)):
                mapped=transport(positive,self.frames,self.shape,.25,target,1)
                self.assertLess(pair_diff(mapped,from_bin(rows,i))/total,1e-22)
        # The same source-span map works for arbitrary coherent linear
        # combinations of these source vectors, not only individual labels.

    def test_negative_pointer_uses_same_map_by_internal_counterpart(self):
        for label in range(16):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            _,vp,p=embed(x,1,4);_,vm,m=embed(x,-1,4);total=norm2(vm)
            for i in (0,1,2):
                self.assertLess(pair_diff(old_exchange(from_bin(p,i)),from_bin(m,i))/total,1e-24)
            for target,i in ((-.75,0),(-.25,1)):
                mapped=transport(from_bin(m,2),self.frames,self.shape,.25,target,-1)
                self.assertLess(pair_diff(mapped,from_bin(m,i))/total,1e-22)
                # S V+ S ensures compatibility with sign counterpart.
                other=old_exchange(transport(from_bin(p,2),self.frames,self.shape,.25,target,1))
                self.assertLess(pair_diff(mapped,other)/total,1e-22)

    def test_record_transports_are_unitary_and_obey_cocycle(self):
        rng=np.random.default_rng(141)
        x=rng.normal(size=self.shape)+1j*rng.normal(size=self.shape)
        y=rng.normal(size=self.shape)+1j*rng.normal(size=self.shape)
        pair=(x,y);total=pair_norm(pair)
        for s in (1,-1):
            for band in (1,2):
                once=v_sector(pair,self.frames,self.shape,band,s)
                twice=v_sector(once,self.frames,self.shape,band,s)
                self.assertAlmostEqual(pair_norm(once)/total,1.,places=12)
                self.assertLess(pair_diff(pair,twice)/total,1e-22)
            direct=transport(pair,self.frames,self.shape,.2,-.7,s)
            via=transport(transport(pair,self.frames,self.shape,.2,-.2,s),
                          self.frames,self.shape,-.2,-.7,s)
            self.assertLess(pair_diff(direct,via)/total,1e-22)

    def test_dressed_rotation_moves_real_records_not_just_labels(self):
        x=initial(relative_read(self.root,4,labels=(0,))[0])
        _,v,rows=embed(x,1,4);total=norm2(v)
        source=from_bin(rows,2);target=transport(source,self.frames,self.shape,.25,-.75,1)
        self.assertAlmostEqual(norm2(source[0])/total,.25,places=12)
        self.assertAlmostEqual(norm2(target[1])/total,.25,places=12)
        self.assertLess(norm2(bob_action(B,source[0])-source[0])/total,1e-24)
        self.assertLess(norm2(bob_action(B,target[1])+target[1])/total,1e-22)
        # SO(3) rotation of n at fixed m takes an old positive-u point to a
        # negative-u point, while the controlled unitary changes B and R.
        m=np.array([0.,0.,1.]);up=.25;down=-.75
        n1=np.array([np.sqrt(1-up*up),0.,up])
        rot=rodrigues((0,1,0),np.arccos(down)-np.arccos(up))
        self.assertAlmostEqual(angle(m,rot@n1),down,places=12)
        # B and R are real physical records in the model: this active map is
        # not automatically a gauge redundancy or an available local gate.

    def test_full_pullback_group_law_and_common_rotations(self):
        x=initial(relative_read(self.root,4,labels=(7,))[0])
        _,v,rows=embed(x,1,4);total=norm2(v)
        m=np.array([0.,0.,1.]);n=np.array([np.sqrt(1-.21**2),0.,.21])
        a=rodrigues((1,2,3),.73);b=rodrigues((2,-1,1),-.92)
        c=rodrigues((3,1,-1),.52);d=rodrigues((1,3,2),-.61)
        # Non-invariant complex scalar distinguishes group law from merely
        # checking the fixed echo; same state space for both pointer signs.
        source=from_bin(rows,2)
        def wave(p,q):
            z=1+.3j*p[0]-.2*q[2]
            return tuple(z*t for t in source)
        for s in (1,-1):
            def first(p,q):
                return dressed_pullback(wave,p,q,c,d,self.frames,self.shape,s)
            composed=dressed_pullback(first,m,n,a,b,self.frames,self.shape,s)
            direct=dressed_pullback(wave,m,n,a@c,b@d,self.frames,self.shape,s)
            self.assertLess(pair_diff(composed,direct)/total,1e-22)
            common=dressed_pullback(wave,m,n,a,a,self.frames,self.shape,s)
            ordinary=wave(a.T@m,a.T@n)
            self.assertLess(pair_diff(common,ordinary)/total,1e-22)
            def exchanged(p,q):return old_exchange(wave(p,q))
            negative=dressed_pullback(exchanged,m,n,a,b,self.frames,self.shape,-s)
            positive=old_exchange(dressed_pullback(wave,m,n,a,b,self.frames,self.shape,s))
            self.assertLess(pair_diff(negative,positive)/total,1e-22)

    def test_post_echo_source_family_fixed_by_dressed_pullback(self):
        m=np.array([0.,0.,1.]);n=np.array([np.sqrt(1-.21**2),0.,.21])
        a=rodrigues((1,2,3),.73);b=rodrigues((2,-1,1),-.92)
        for label in range(16):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            for s in (1,-1):
                _,v,rows=embed(x,s,4);total=norm2(v)
                def wave(p,q):
                    return from_bin(rows,{0:2,1:0,2:1}[sector(angle(p,q))])
                out=dressed_pullback(wave,m,n,a,b,self.frames,self.shape,s)
                self.assertLess(pair_diff(out,wave(m,n))/total,1e-22)

    def test_stronger_symmetry_selects_uniform_amplitude_in_this_family(self):
        x=initial(relative_read(self.root,4,labels=(0,))[0])
        _,v,rows=embed(x,1,4);total=norm2(v)
        u1,u2=.13,-.68;source=from_bin(rows,2);target=from_bin(rows,0)
        mapped=transport(source,self.frames,self.shape,u1,u2,1)
        self.assertLess(pair_diff(mapped,target)/total,1e-22)
        eps=.5
        weighted_source=tuple(np.sqrt(symmetric_density(u1,eps))*z for z in source)
        weighted_target=tuple(np.sqrt(symmetric_density(u2,eps))*z for z in target)
        mapped_weighted=transport(weighted_source,self.frames,self.shape,u1,u2,1)
        self.assertGreater(pair_diff(mapped_weighted,weighted_target)/total,1e-4)
        # The independent-rotation group is transitive on m,n, so a
        # nonconstant scalar amplitude cannot be invariant under all of it.
        # This is a state-symmetry selection under the chosen record dressing.

if __name__=='__main__':unittest.main()
