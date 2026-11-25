"""Transfer an internally paired reference onto the old orientation qubit.

Conditional on a 72-dimensional charge-commuting lab sector, the original
paired state supplies the sphere pair, DE, and F's entangled partner H.
The explicit swap conserves the *enlarged* orientation charge; H retains
its nonzero spin. No global-zero, autonomous-control, or experience claim.
"""
import math
import unittest
import numpy as np
from verification.zero_all_sector_noncommuting_sphere_test import (
    decomposition,local_charges,HA,HB,I256,PCODE,CODE,J,kron,
    original_effects,bob_effects,active_base,output,relative_read
)
from verification.zero_energy_sphere_work_incidence_test import I,X,Y,Z
from verification.zero_relational_orientation_reference_test import (
    U8,U1,Jw,with_reference,C1,C2,C3
)
from verification.zero_relational_chirality_report_test import (
    SING,initial,apply64,outcome_tables,C,LL
)
from verification.zero_relative_gauge_invariant_report_test import (
    V,VP,VM,G as GAUGE,SOURCE
)
from verification.zero_nested_sphere_internal_reference_test import lift_pair
from verification.zero_five_ray_record_current_unification_test import q,ns,axis
from verification.zero_constitution_hamiltonian_phase_gate_test import X16,Z16,J16,P16
from verification.zero_reciprocal_subject_exchange_test import n

P=(X,Y,Z)
AA=(U8,U1,Jw)
BF=(-X,-Y,Z)
PLUS=np.array([1.,1.],complex)/math.sqrt(2)
PSI=np.array([[0,1],[1,0]],complex)/math.sqrt(2) # F,H
I8=np.eye(8,dtype=complex)
SWAP=(np.eye(32)+sum(kron(a,I,x) for a,x in zip(AA,P)))/2 # RWT F H
K=[kron(a,I,I)+kron(I8,b,I)+kron(I8,I,x) for a,b,x in zip(AA,BF,P)]
COLD=[kron(c,I) for c in (C1,C2,C3)]


def apply32(op,v):
    assert v.shape[-5:]==(2,2,2,2,2)
    return np.einsum('xy,...y->...x',op,v.reshape(v.shape[:-5]+(32,)),optimize=True).reshape(v.shape)


def triple_basis(paths):
    # Existing old sphere pairs 0/1,2/3,4/5,6/7 remain adjacent.
    # Alice order sphere S, reference D, partner H, irrep; Bob S,E,F.
    d=paths[0].shape[1]
    f=np.column_stack([paths[4*h+2*r+s] for s in range(2)
                       for r in range(2) for h in range(2)])
    b=f.conj()@kron(I,J.T,X,np.eye(d))
    return d,f,b


def lift(f,d,a):return f@kron(a,np.eye(d))@f.conj().T


class InternalFReferenceTransferTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        *_,cls.blocks,cls.u,cls.v,cls.odd,cls.counts=decomposition()
        cls.d,cls.f,cls.b=triple_basis(cls.blocks[(1,1)])
        cls.p=cls.f@cls.f.conj().T
        cls.g=local_charges()
        cls.ka=[f/math.sqrt(np.trace(f).real) for f in original_effects()]
        cls.kb=[J.conj().T@x@J for x in bob_effects()]
        cls.a=[lift_pair(cls.u,cls.v,x) for x in cls.ka]
        cls.bb=[lift_pair(cls.u,cls.v,x.conj()).conj() for x in cls.kb]

    def test_actual_source_contains_three_pairs_and_old_sphere_instrument(self):
        d,f,b,p=self.d,self.f,self.b,self.p
        self.assertEqual(d,9)
        np.testing.assert_allclose(f.conj().T@f,np.eye(72),atol=1e-12)
        np.testing.assert_allclose(b@b.conj().T,p.conj(),atol=1e-12)
        np.testing.assert_allclose(p@PCODE,0,atol=1e-12)
        self.assertAlmostEqual(np.trace(p).real,72,places=10)
        coord=f.conj().T@(p/16)@b.conj()
        np.testing.assert_allclose(coord,kron(I,J.T,X,np.eye(d))/16,atol=1e-12)
        normalized=kron(I/math.sqrt(2),SING,PSI,np.eye(d)/math.sqrt(d))
        np.testing.assert_allclose(coord,math.sqrt(72/256)*normalized,atol=1e-12)
        # PSI is symmetric, hence its F,H order equals H,F in the matrix.
        for a,x in zip(self.a,self.ka):
            np.testing.assert_allclose(a@p,lift(f,d,kron(x,I,I)),atol=1e-12)
        for a,x in zip(self.bb,self.kb):
            np.testing.assert_allclose(a@p.conj(),lift(b,d,kron(x,I,I)),atol=1e-12)
        ds=[lift(f,d,kron(I,x,I)) for x in P]
        es=[lift(b,d,kron(I,x,I)) for x in P]
        hs=[lift(f,d,kron(I,I,x)) for x in P]
        fs=[lift(b,d,kron(I,I,x)) for x in BF]
        for op in ds+es+hs+fs:
            for g in self.g:np.testing.assert_allclose(op@g-g@op,0,atol=1e-12)
            for energy in (HA,HB):np.testing.assert_allclose(op@energy-energy@op,0,atol=1e-12)
        for op in self.a:
            for x in ds+hs:np.testing.assert_allclose(op@x-x@op,0,atol=1e-12)
        for op in self.bb:
            for x in es+fs:np.testing.assert_allclose(op@x-x@op,0,atol=1e-12)
        for i,a in enumerate(self.a):
            for j,bb in enumerate(self.bb):
                branch=a@(p/16)@bb.T
                expected=kron(self.ka[i],I,I,np.eye(d))@kron(I,J.T,X,np.eye(d))@kron(self.kb[j].T,I,I,np.eye(d))/16
                np.testing.assert_allclose(f.conj().T@branch@b.conj(),expected,atol=1e-12)
                for de,ee in zip(ds,es):np.testing.assert_allclose(de@branch+branch@ee.T,0,atol=1e-12)
                for h,ff in zip(hs,fs):np.testing.assert_allclose(h@branch+branch@ff.T,0,atol=1e-12)
        # H/F are F/G in PSI; the local reference pair is not reset.

    def test_swap_is_a_conserving_unitary_only_for_enlarged_orientation(self):
        np.testing.assert_allclose(SWAP,SWAP.conj().T,atol=1e-13)
        np.testing.assert_allclose(SWAP@SWAP,np.eye(32),atol=1e-13)
        for a,x in zip(AA,P):
            np.testing.assert_allclose(SWAP@kron(a,I,I)@SWAP,kron(I8,I,x),atol=1e-13)
        for total in K:np.testing.assert_allclose(SWAP@total-total@SWAP,0,atol=1e-13)
        self.assertGreater(np.linalg.norm(SWAP@COLD[0]-COLD[0]@SWAP),1)
        # A pure singlet AF cannot be produced while conserving AF charge
        # alone from the mixed-F late input; H receives the missing charge.
        # SWAP is generated by pi/2*(I-SWAP), an invariant Hamiltonian.
        h=math.pi/2*(np.eye(32)-SWAP)
        vals,u=np.linalg.eigh(h)
        np.testing.assert_allclose((u*np.exp(-1j*vals))@u.conj().T,SWAP,atol=1e-13)
        for total in K:np.testing.assert_allclose(h@total-total@h,0,atol=1e-13)
        # The full old work-space generators commute with the declared work
        # number and pair-number operators. The inactive support projector
        # permits an identity extension of the controlled swap.
        physical_a=(-kron(Z,X16,X),-kron(Z,Z16,X),kron(I,J16,I))
        support=kron(I,P16,I)
        for inds in ((0,1,2,3),(0,1),(2,3),(0,2),(1,3)):
            number=kron(I,sum(np.asarray(n[i]) for i in inds),I)
            for x in (*physical_a,support):
                np.testing.assert_allclose(x@number-number@x,0,atol=1e-13)

    def test_transfer_matches_full_old_source_for_all_clock_labels(self):
        state=output(active_base())
        for label in range(16):
            v=relative_read(state,4,labels=(label,))[0]
            source=np.einsum('...rwt,fh->...rwtfh',v,PSI)
            result=apply32(SWAP,source)
            desired=np.einsum('...rwtf,h->...rwtfh',with_reference(v),PLUS)
            np.testing.assert_allclose(result,desired,atol=1e-13)
            # Conserve K_i while *transferring* orientation to H.
            for total in K:
                initial_value=apply32(total,source)
                final_value=apply32(total,result)
                np.testing.assert_allclose(final_value,apply32(SWAP,initial_value),atol=1e-13)
            for c in COLD:np.testing.assert_allclose(apply32(c,result),0,atol=1e-13)
            mass=np.linalg.norm(v)**2
            # Original A is exactly pure +X; after the reference transfer it
            # is maximally mixed. This exposes the actual state change made
            # by the earlier with_reference isometry, not just its statistics.
            av=np.einsum('xy,...y->...x',U8,v.reshape(v.shape[:-3]+(8,))).reshape(v.shape)
            np.testing.assert_allclose(av,v,atol=1e-13)
            extended=with_reference(v)
            previous=extended.reshape(-1,2)
            overlaps=np.einsum('i,if->f',v.reshape(-1).conj(),previous)
            self.assertAlmostEqual(np.sum(abs(overlaps)**2)/mass**2,.5,places=12)
            plus=(previous[:,0]+previous[:,1])/math.sqrt(2)
            minus=(previous[:,0]-previous[:,1])/math.sqrt(2)
            np.testing.assert_allclose(plus,v.reshape(-1)/math.sqrt(2),atol=1e-13)
            self.assertAlmostEqual(np.linalg.norm(minus)**2,mass/2,places=12)
            self.assertAlmostEqual(abs(np.vdot(v.reshape(-1),minus)),0,places=12)
            for a in AA:
                op=kron(a,I)
                acted=np.einsum('xy,...y->...x',op,extended.reshape(extended.shape[:-4]+(16,))).reshape(extended.shape)
                self.assertAlmostEqual(np.vdot(extended,acted).real,0,places=12)
            self.assertAlmostEqual(sum(np.linalg.norm(apply32(c,source))**2 for c in COLD),6*mass,places=12)
            self.assertAlmostEqual(np.linalg.norm(apply32(COLD[2],source))**2,2*mass,places=12)
            self.assertAlmostEqual(sum(np.linalg.norm(apply32(k,source))**2 for k in K),3*mass,places=12)
            self.assertAlmostEqual(sum(np.linalg.norm(apply32(k,result))**2 for k in K),3*mass,places=12)
            self.assertAlmostEqual(np.vdot(result,apply32(K[0],result)).real,mass,places=12)
            # This is exact in phase and all environment amplitudes.

    def test_relative_sign_report_and_actual_charge_carrier(self):
        state=output(active_base())
        d=np.array(ns)@np.array(axis)
        for label in range(16):
            v=relative_read(state,4,labels=(label,))[0]
            source=np.einsum('...rwt,fh->...rwtfh',v,PSI)
            swapped=apply32(SWAP,source)
            # Move H to the environment prefix, before compressed RWT F D E.
            joint=np.einsum('...rwtfh,de->...hrwtfde',swapped,SING)
            target=np.einsum('...rwtfde,h->...hrwtfde',initial(v),PLUS)
            np.testing.assert_allclose(joint,target,atol=1e-13)
            np.testing.assert_allclose(apply64(SOURCE,joint),joint,atol=1e-13)
            np.testing.assert_allclose(apply64(V@V,joint),joint,atol=1e-13)
            original=initial(v); branches,table=outcome_tables(original)
            mass=np.linalg.norm(v)**2
            np.testing.assert_allclose(table,np.array(q)[:,None]*mass/2*np.ones((1,2)),atol=1e-13)
            for proj,old in zip((VP,VM),branches):
                new=apply64(proj,joint)
                expected=np.einsum('...rwtfde,h->...hrwtfde',old,PLUS)
                np.testing.assert_allclose(new,expected,atol=1e-13)
                for c in C:np.testing.assert_allclose(apply64(c,new),0,atol=1e-13)
                np.testing.assert_allclose(apply64(LL,new),new,atol=1e-13)
                np.testing.assert_allclose(apply64(GAUGE,new),new,atol=1e-13)
                # Total C+H acts as H on each branch, hence its Casimir is 3.
                np.testing.assert_allclose(np.einsum('hk,...krwtfde->...hrwtfde',X,new),new,atol=1e-13)
                self.assertAlmostEqual(sum(np.linalg.norm(np.einsum('hk,...krwtfde->...hrwtfde',x,new))**2 for x in P),3*np.linalg.norm(new)**2,places=12)
            # Two existing formal valence candidates still disagree at 3/5;
            # a physical sign or a zero mean does not select experience.
            self.assertAlmostEqual(table[d<0].sum()/mass,3/5,places=12)
            self.assertAlmostEqual(np.einsum('is,s->',table,[1,-1]),0,places=13)
            self.assertAlmostEqual(np.einsum('is,i,s->',table,np.sign(d),[1,-1]),0,places=13)

    def test_whole_state_and_no_global_singlet_in_five_spin_algebra(self):
        p=self.p
        whole=(CODE@J@CODE.T+I256-PCODE).T/16
        active=p@whole;inactive=(I256-p)@whole
        np.testing.assert_allclose(active,p/16,atol=1e-12)
        np.testing.assert_allclose(active+inactive,whole,atol=1e-12)
        self.assertAlmostEqual(np.linalg.norm(active)**2,72/256,places=12)
        self.assertAlmostEqual(np.linalg.norm(inactive)**2,184/256,places=12)
        # Five spin-half representations: A,F,H,D,E. An odd number of
        # spin halves has no SU(2)-invariant vector, independent of state.
        pauli=[kron(*[x if j==i else I for j in range(5)])
               for i in range(5) for x in P]
        total=[sum(pauli[3*i+k] for i in range(5)) for k in range(3)]
        cas=sum(x@x for x in total)
        eig=np.linalg.eigvalsh(cas)
        np.testing.assert_allclose(eig[:10],3,atol=1e-12)
        self.assertGreater(eig.min(),2.999999999)
        # The chosen Pauli orientations are related by local unitaries to
        # those in this model; zero multiplicity is basis independent.

if __name__=='__main__':unittest.main()
