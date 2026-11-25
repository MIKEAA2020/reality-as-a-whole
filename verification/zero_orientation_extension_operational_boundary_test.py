"""Extend the invariant lab orientation, and compare exact report interfaces.

The maximality statements are restricted to the original lab charge
commutant, unchanged 190D sphere instrument, separate code and, where stated,
the exact old full-space relative-sign observable. Neither a pointer interface
nor its information is asserted to be a subject or a felt experience.
"""
import math
import unittest
import numpy as np
from verification.zero_all_sector_noncommuting_sphere_test import (
    decomposition,local_charges,HA,HB,I256,CODE,PCODE,J,kron,spin_matrices,
    original_effects,bob_effects,active_base,output,relative_read
)
from verification.zero_nested_sphere_internal_reference_test import lift_pair
from verification.zero_internal_f_reference_transfer_test import triple_basis,lift,PSI
from verification.zero_relational_chirality_report_test import (
    I,X,Y,Z,SING,eps,initial,outcome_tables
)
from verification.zero_five_ray_record_current_unification_test import q,ns,axis

SIG=(X,Y,Z)
BF=(-X,-Y,Z)


def pair_factor(paths):
    # Sphere is exactly the old adjacent pair, spectator counts the pairs.
    copies=len(paths)//2;d=paths[0].shape[1]
    f=np.column_stack([paths[2*r+s] for s in range(2) for r in range(copies)])
    return copies,d,f


def spin_generators(copies):
    s=(copies-1)/2
    return [2*s*x for x in spin_matrices(copies)]


def embed_spin(paths):
    m,d,f=pair_factor(paths)
    return [f@kron(I,x,np.eye(d))@f.conj().T for x in spin_generators(m)]


def v_canonical():
    # Four logical spins initially ordered A,F,D,E; turn into Alice A,D
    # and Bob F,E and use a Bob basis making the input |Phi_4>.
    aa=[kron(x,I,I,I) for x in SIG]
    bb=[kron(I,x,I,I) for x in BF]
    dd=[kron(I,I,x,I) for x in SIG]
    ee=[kron(I,I,I,x) for x in SIG]
    v=sum(s*(aa[i]-bb[i])@dd[j]@ee[k] for i,j,k,s in eps)/(4*math.sqrt(3))
    v=v.reshape((2,)*8).transpose(0,2,1,3,4,6,5,7).reshape(16,16)
    amp=np.einsum('af,de->adfe',PSI,SING).reshape(4,4)
    b=(2*amp).T
    vc=kron(np.eye(4),b.conj().T)@v@kron(np.eye(4),b)
    return vc,amp,b


def symmetry_map(v):
    cols=[]
    for i in range(4):
        for j in range(4):
            x=np.zeros((4,4),complex);x[i,j]=1
            total=kron(x,np.eye(4))-kron(np.eye(4),x.T)
            cols.append((total@v-v@total).ravel())
    return np.column_stack(cols)


def binary_entropy(p):
    return -sum(x*math.log2(x) for x in (p,1-p) if x>0)


class OrientationExtensionAndBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        *_,cls.blocks,cls.u,cls.v,cls.odd,cls.counts=decomposition()
        cls.labg=local_charges()
        d,f,b=triple_basis(cls.blocks[(1,1)])
        cls.valid=f@f.conj().T
        ds=[lift(f,d,kron(I,x,I)) for x in SIG]
        hs=[lift(f,d,kron(I,I,x)) for x in SIG]
        es=[lift(b,d,kron(I,x,I)) for x in SIG]
        fs=[lift(b,d,kron(I,I,x)) for x in BF]
        cls.old=[x+y for x,y in zip(ds,hs)]
        cls.oldbob=[x+y for x,y in zip(es,fs)]
        cls.extra=[embed_spin(cls.blocks[k]) for k in ((0,1),(1,0))]
        cls.ext=[cls.old[i]+sum(block[i] for block in cls.extra) for i in range(3)]
        cls.alt9=embed_spin(cls.blocks[(1,1)][:8])
        cls.full=[cls.alt9[i]+sum(block[i] for block in cls.extra) for i in range(3)]
        cls.Q=cls.u@cls.u.conj().T+cls.v@cls.v.conj().T
        cls.ka=[x/math.sqrt(np.trace(x).real) for x in original_effects()]
        cls.kb=[J.conj().T@x@J for x in bob_effects()]
        cls.a=[lift_pair(cls.u,cls.v,x)+math.sqrt(qi)*(I256-cls.Q) for x,qi in zip(cls.ka,q)]
        cls.b=[lift_pair(cls.u,cls.v,x.conj()).conj()+(I256-cls.Q.conj())/math.sqrt(2) for x in cls.kb]
        cls.whole=(CODE@J@CODE.T+I256-PCODE).T/16

    def check_physical_conservation(self,ops):
        bob=[-x.conj() for x in ops]
        for i,j,k in ((0,1,2),(1,2,0),(2,0,1)):
            np.testing.assert_allclose(ops[i]@ops[j]-ops[j]@ops[i],2j*ops[k],atol=1e-12)
            np.testing.assert_allclose(bob[i]@bob[j]-bob[j]@bob[i],2j*bob[k],atol=1e-12)
        for x,y in zip(ops,bob):
            np.testing.assert_allclose(x@self.whole+self.whole@y.T,0,atol=1e-12)
            for g in self.labg:
                np.testing.assert_allclose(g@x-x@g,0,atol=1e-12)
                np.testing.assert_allclose(g@y-y@g,0,atol=1e-12)
            for h in (HA,HB):
                np.testing.assert_allclose(h@x-x@h,0,atol=1e-12)
                np.testing.assert_allclose(h@y-y@h,0,atol=1e-12)
            for a in self.a:np.testing.assert_allclose(a@x-x@a,0,atol=1e-12)
            for b in self.b:np.testing.assert_allclose(b@y-y@b,0,atol=1e-12)
        for a in self.a:
            for b in self.b:
                branch=a@self.whole@b.T
                for x,y in zip(ops,bob):
                    np.testing.assert_allclose(x@branch+branch@y.T,0,atol=1e-12)

    def test_extended_charge_preserves_full_source_and_existing_sphere(self):
        for a,b in zip(self.old,self.oldbob):np.testing.assert_allclose(b,-a.conj(),atol=1e-12)
        self.check_physical_conservation(self.ext)
        # Old sign-report sector and its four spin algebras are unchanged.
        for a,old in zip(self.ext,self.old):
            np.testing.assert_allclose(a@self.valid,old,atol=1e-12)
        # SU(2) Casimir counts ACTUALLY nontrivial representation support,
        # not all 72 dimensions in a sector with a singlet component.
        cas=sum(x@x for x in self.ext);e=np.linalg.eigvalsh(cas)
        np.testing.assert_allclose(e[:166],0,atol=1e-11)
        np.testing.assert_allclose(e[166:],8,atol=1e-11)
        self.assertEqual(np.count_nonzero(e>1e-9),90)
        original=np.linalg.eigvalsh(sum(x@x for x in self.old))
        self.assertEqual(np.count_nonzero(original>1e-9),54)
        # 54 old spin-1 dimensions + 18 + 18 newly active.

    def test_highest_coverage_when_original_sign_operator_is_not_required(self):
        self.check_physical_conservation(self.full)
        eig=np.linalg.eigvalsh(sum(x@x for x in self.full))
        np.testing.assert_allclose(eig[:148],0,atol=1e-11)
        np.testing.assert_allclose(eig[148:184],8,atol=1e-11)
        np.testing.assert_allclose(eig[184:],15,atol=1e-11)
        self.assertEqual(np.count_nonzero(eig>1e-9),108)
        # Spin 3/2 on the 4-dimensional multiplicity spectator gives 72,
        # but is not compatible with the old relative sign (next test).
        expected=0
        for key,paths in self.blocks.items():
            paths=paths[2:] if key==(0,0) else paths
            r=len(paths)//2;d=paths[0].shape[1]
            if r>=2:expected+=2*r*d
        self.assertEqual(expected,108)
        # The full commuting sphere M2 has scalar commutant when r=1.
        # Unpaired one-copy blocks and the energy-split retained code likewise
        # admit only scalar charge-commuting generators under the stated class.

    def test_exact_old_sign_restricts_the_four_copy_orientation_symmetry(self):
        v,amp,b=v_canonical();np.testing.assert_allclose(amp@b.conj(),np.eye(4)/2,atol=1e-13)
        matrix=symmetry_map(v)
        singular=np.linalg.svd(matrix,compute_uv=False)
        self.assertEqual(np.count_nonzero(singular<1e-10),4)
        # The four-dimensional complex kernel is exactly span{I,A_i+D_i}.
        known=[np.eye(4)]+[kron(x,I)+kron(I,x) for x in SIG]
        self.assertEqual(np.linalg.matrix_rank(np.column_stack([x.ravel() for x in known]),tol=1e-10),4)
        for x in known:
            total=kron(x,np.eye(4))-kron(np.eye(4),x.T)
            np.testing.assert_allclose(total@v-v@total,0,atol=1e-13)
        # The old representation is 0⊕1; no choice of its su(2) basis can
        # remove the 1D local singlet. Spin-3/2 instead conflicts with V and
        # with its negative-report projector on the complete operator space.
        vm=(3/4)*(v@v)@(v@v-np.eye(16)/3)@(np.eye(16)-v)
        vp=(3/4)*(v@v)@(v@v-np.eye(16)/3)@(np.eye(16)+v)
        # Even the weaker requirement of preserving just the old pointer
        # projector forces a common 1D singlet in the local spectator.
        self.assertEqual(np.count_nonzero(np.linalg.svd(symmetry_map(vm),compute_uv=False)<1e-10),10)
        vals,vec=np.linalg.eigh(vm)
        self.assertAlmostEqual(vals[-1],1,places=12)
        self.assertEqual(np.count_nonzero(vals>1e-10),1)
        z=vec[:,-1].reshape(4,4)
        np.testing.assert_allclose(z@z.conj().T,z.conj().T@z,atol=1e-13)
        self.assertGreater(abs(np.trace(z)),1)
        # The two eigenspaces of z have multiplicities 3 and 1.
        ev=np.linalg.eigvals(z)
        multiplicities=[np.count_nonzero(abs(ev-e)<1e-10) for e in ev]
        self.assertEqual(sorted(multiplicities),[1,3,3,3])
        # For a projector symmetry [X,Z]=lambda Z; nonzero Tr Z forces
        # lambda=0, so every X preserves the 1D eigenspace. An su(2)
        # representation cannot act nontrivially in one dimension.
        phi=np.eye(4).reshape(-1)/2
        for x in spin_generators(4):
            total=kron(x,np.eye(4))-kron(np.eye(4),x.T)
            self.assertGreater(np.linalg.norm(total@v-v@total),1)
            self.assertGreater(np.linalg.norm(total@vm-vm@total),1)
            np.testing.assert_allclose(total@phi,0,atol=1e-13)
        for proj in (vp,vm):
            branch=proj@phi
            self.assertAlmostEqual(np.linalg.norm(branch)**2,.5,places=12)
            total_var=sum(np.linalg.norm((kron(x,np.eye(4))-kron(np.eye(4),x.T))@branch)**2
                          for x in spin_generators(4))
            self.assertAlmostEqual(total_var,22/3,places=12)
            # A neutral-pointer sign branch violates the 3/2 total charge
            # even on the actual source; a charged pointer is outside scope.

    def test_neutral_reader_dynamically_opens_a_limited_interface(self):
        # On the *same* recorded histories, a neutral reader initially |0>
        # is coupled by H=|1><1|_M⊗Y. M is the existing gauge-even sign
        # pointer; theta can be read relative to the previously stipulated
        # clock, but this operation/control is not derived from zero.
        proj1=np.array([[0,0],[0,1]],complex)
        h=kron(proj1,Y)
        np.testing.assert_allclose(h@kron(Z,I)-kron(Z,I)@h,0,atol=1e-13)
        ready=np.array([1.,0.],complex)
        for theta in (0,math.pi/6,math.pi/2):
            val,vec=np.linalg.eigh(h)
            u=(vec*np.exp(-1j*theta*val))@vec.conj().T
            np.testing.assert_allclose(u.conj().T@u,np.eye(4),atol=1e-13)
            p0=u@kron(np.array([1.,0.]),ready)
            p1=u@kron(np.array([0.,1.]),ready)
            np.testing.assert_allclose(p0,kron(np.array([1.,0.]),ready),atol=1e-13)
            np.testing.assert_allclose(p1,kron(np.array([0.,1.]),np.array([math.cos(theta),math.sin(theta)])),atol=1e-13)
            rho0=np.outer(ready,ready.conj())
            r1=np.array([math.cos(theta),math.sin(theta)])
            rho1=np.outer(r1,r1.conj())
            trace_distance=np.sum(abs(np.linalg.eigvalsh(rho0-rho1)))/2
            self.assertAlmostEqual(trace_distance,math.sin(theta),places=12)
            # Equal prior signs, optimal quantum readout of the reader only.
            p1_correct=(1+trace_distance)/2
            self.assertAlmostEqual(p1_correct,(1+math.sin(theta))/2,places=12)
            # Alternate formal sign flips for i of total weight 3/5.
            rplus=.4*rho0+.6*rho1;rminus=.6*rho0+.4*rho1
            alt_distance=np.sum(abs(np.linalg.eigvalsh(rplus-rminus)))/2
            self.assertAlmostEqual((1+alt_distance)/2,(1+.2*math.sin(theta))/2,places=12)
            # With i additionally present, its known sign enables the same
            # Helstrom accuracy as the first candidate. Sign/i marginals and
            # the model's orientation charge are untouched by this gate.

    def test_precise_operational_boundary_on_same_recorded_histories(self):
        # Actual old sign branches at every clock label supply the same joint
        # classical distribution p(i,s)=q_i/2. Only stated classical pointer
        # algebras are compared; no optimization over extra lab measurements.
        state=output(active_base());d=np.array(ns)@np.array(axis)
        for label in range(16):
            old=relative_read(state,4,labels=(label,))[0]
            v=initial(old);_,table=outcome_tables(v)
            table=table/np.linalg.norm(v)**2
            np.testing.assert_allclose(table,np.array(q)[:,None]/2*np.ones((1,2)),atol=1e-13)
            # h1=s and h2=sgn(d_i)*s: both unbiased, but not identical.
            agree=np.sum(table[d>0]);disagree=np.sum(table[d<0])
            self.assertAlmostEqual(agree,.4,places=12)
            self.assertAlmostEqual(disagree,.6,places=12)
            # M reads s; i is not available in the smaller interface.
            self.assertAlmostEqual(1-disagree,.4,places=12)
            self.assertAlmostEqual(max(agree,disagree),.6,places=12)
            self.assertAlmostEqual(1-binary_entropy(disagree),.02904940554533142,places=12)
            # M+i determines either candidate exactly; i alone has no sign
            # information. Labels are formal, not assumed experiences.
            np.testing.assert_allclose(table[:,0],table[:,1],atol=1e-13)

if __name__=='__main__':unittest.main()
