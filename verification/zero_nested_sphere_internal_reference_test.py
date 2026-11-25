"""Nest the internal reference in the *existing* 190-dimensional POVM.

The old sphere instrument is untouched; a later joint sign report is valid
only on a separately flagged sector. All operations and interfaces remain
finite-model inputs, not a derivation from zero.
"""
import math
import unittest
import numpy as np
from verification.zero_all_sector_noncommuting_sphere_test import (
    decomposition,local_charges,HA,HB,I256,PCODE,CODE,J,I,kron,
    original_effects,bob_effects,spin_instrument,active_base,output,
    compressed_spin_base,remainder_base,full_state,relative_read,i_r_m_table
)
from verification.zero_internal_pair_sphere_report_test import physical_operators
from verification.zero_relational_chirality_report_test import (
    SING,initial,apply64,outcome_tables,C,LL
)
from verification.zero_relative_gauge_invariant_report_test import G,VP,VM,V,SOURCE
from verification.zero_five_ray_record_current_unification_test import q,ns,axis


def aligned_sector(paths,max_groups=None):
    """[sphere, reference, group, irrep], preserving old adjacent pairs."""
    d=paths[0].shape[1]; k=len(paths)//4
    if max_groups is not None:k=min(k,max_groups)
    t=k*d
    F=np.column_stack([paths[4*g+2*r+s]
                       for s in range(2) for r in range(2) for g in range(k)])
    bob=F.conj()@kron(I,J.T,np.eye(t))
    return t,F,bob


def lift_pair(u,v,a):
    return (a[0,0]*u@u.conj().T+a[0,1]*u@v.conj().T+
            a[1,0]*v@u.conj().T+a[1,1]*v@v.conj().T)


def commutant_dimension(ops):
    n=ops[0].shape[0]; eye=np.eye(n)
    matrix=np.vstack([np.kron(eye,a)-np.kron(a.T,eye) for a in ops])
    sv=np.linalg.svd(matrix,compute_uv=False)
    return n*n-np.count_nonzero(sv>1e-10)


class NestedSphereInternalReferenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        *_,cls.blocks,cls.u,cls.v,cls.odd,cls.counts=decomposition()
        cls.g=local_charges()
        cls.items=[aligned_sector(cls.blocks[k]) for k in ((0,1),(1,0),(1,1))]
        cls.ps=[F@F.conj().T for _,F,_ in cls.items]
        cls.p=sum(cls.ps)
        cls.Q=cls.u@cls.u.conj().T+cls.v@cls.v.conj().T
        cls.R=cls.odd@cls.odd.conj().T
        cls.ka=[x/math.sqrt(np.trace(x).real) for x in original_effects()]
        cls.kb=[J.conj().T@x@J for x in bob_effects()]
        cls.a=[lift_pair(cls.u,cls.v,x) for x in cls.ka]
        cls.b=[lift_pair(cls.u,cls.v,x.conj()).conj() for x in cls.kb]

    def test_unchanged_physical_qubit_instruments_and_internal_factors(self):
        np.testing.assert_allclose(self.Q@self.p,self.p,atol=1e-12)
        self.assertAlmostEqual(np.trace(self.p).real,96,places=10)
        self.assertAlmostEqual(np.trace(self.Q-self.p).real,94,places=10)
        np.testing.assert_allclose(PCODE+self.Q+self.R,I256,atol=1e-12)
        self.assertAlmostEqual(np.trace(self.R).real,64,places=10)
        for t,F,bob in self.items:
            p=F@F.conj().T
            ka,kb,alice,bobops,ds,es=physical_operators(F,bob,t)
            # Same actual physical Kraus operators as the old 190 instrument,
            # not only equal outcome probabilities or a unitary equivalent POVM.
            for old,new in zip(self.a,alice):np.testing.assert_allclose(old@p,new,atol=1e-12)
            for old,new in zip(self.b,bobops):np.testing.assert_allclose(old@p.conj(),new,atol=1e-12)
            coord=F.conj().T@(p/16)@bob.conj()
            np.testing.assert_allclose(coord,kron(I,J.T,np.eye(t))/16,atol=1e-12)
            np.testing.assert_allclose(coord,math.sqrt(4*t/256)*kron(I/math.sqrt(2),SING,np.eye(t)/math.sqrt(t)),atol=1e-12)
            for op in self.a+self.b+ds+es:
                for g in self.g:np.testing.assert_allclose(op@g-g@op,0,atol=1e-12)
                for h in (HA,HB):np.testing.assert_allclose(op@h-h@op,0,atol=1e-12)
            for k in self.a:
                for d in ds:np.testing.assert_allclose(k@d-d@k,0,atol=1e-12)
            for k in self.b:
                for e in es:np.testing.assert_allclose(k@e-e@k,0,atol=1e-12)
        # Flag can be written before or after the sphere operation.
        for a in self.a:np.testing.assert_allclose(a@self.p,self.p@a,atol=1e-12)
        for b in self.b:np.testing.assert_allclose(b@self.p.conj(),self.p.conj()@b,atol=1e-12)

    def test_same_original_instrument_on_the_coherent_whole_complement(self):
        M=(CODE@J@CODE.T+I256-PCODE).T/16
        p=self.p; other=self.Q-p
        np.testing.assert_allclose(p@M,p/16,atol=1e-12)
        np.testing.assert_allclose(other@M,other/16,atol=1e-12)
        np.testing.assert_allclose(self.R@M,self.R/16,atol=1e-12)
        for a in self.a:
            for b in self.b:
                whole=a@M@b.T
                valid=a@(p@M)@b.T
                invalid=a@(other@M)@b.T
                np.testing.assert_allclose(whole,valid+invalid,atol=1e-12)
                self.assertAlmostEqual(np.vdot(valid,invalid).real,0,places=12)
                self.assertAlmostEqual(np.vdot(valid,invalid).imag,0,places=12)
                self.assertAlmostEqual(np.linalg.norm(valid)**2/np.linalg.norm(whole)**2,96/190,places=12)
        # Flagging does not change the old joint outcome probabilities, but
        # tracing out the flag can decohere cross-sector lab coherences.
        self.assertGreater(np.linalg.norm(p@M)*np.linalg.norm((I256-p)@M),0.1)

    def test_report_and_old_clock_on_valid_sector(self):
        state=output(active_base())
        for label in range(16):
            v=initial(relative_read(state,4,labels=(label,))[0]);mass=np.linalg.norm(v)**2
            np.testing.assert_allclose(apply64(SOURCE,v),v,atol=1e-13)
            np.testing.assert_allclose(apply64(V@V,v),v,atol=1e-13)
            branches,table=outcome_tables(v)
            np.testing.assert_allclose(table,np.array(q)[:,None]*mass/2*np.ones((1,2)),atol=1e-13)
            for sign,branch in zip((VP,VM),branches):
                np.testing.assert_allclose(apply64(sign,v),branch,atol=1e-13)
                np.testing.assert_allclose(apply64(G,branch),branch,atol=1e-13)
                np.testing.assert_allclose(apply64(LL,branch),branch,atol=1e-13)
                for c in C:np.testing.assert_allclose(apply64(c,branch),0,atol=1e-12)
        states=[full_state(4),state,output(remainder_base())]
        for labels in (tuple(range(16)),(15,0,1)):
            p=len(labels)/16
            tables=[i_r_m_table(relative_read(s,4,labels=labels)) for s in states]
            aggregate=(2*tables[0]+190*tables[1]+64*tables[2])/256
            np.testing.assert_allclose(aggregate.sum(axis=(1,2)),p*np.array(q),atol=1e-12)
            self.assertAlmostEqual(96*tables[1].sum()/256,p*3/8,places=12)
            self.assertAlmostEqual(96*tables[1].sum()/512,p*3/16,places=12)

    def test_original_spin4_instrument_has_no_compatible_internal_flag(self):
        # Any noncollinear two effects generate the full irreducible spin-s
        # matrix algebra. Verify commutant dimensions on multiplicities 3,9.
        for m in (3,9):
            effects,_,_,_=spin_instrument(m)
            self.assertEqual(commutant_dimension(effects[:2]),1)
        paths=self.blocks[(1,1)];d=paths[0].shape[1]
        flat=np.column_stack(paths);p=self.ps[2]
        effects,_,ka,_=spin_instrument(9)
        def lift(x):return flat@np.kron(x,np.eye(d))@flat.conj().T
        # Direct conflict with the old unsharp 81-dimensional block:
        # preserving its actual POVM precludes a nontrivial 72-of-81 flag.
        self.assertGreater(np.linalg.norm(lift(effects[0])@p-p@lift(effects[0])),0.01)
        self.assertGreater(np.linalg.norm(lift(ka[0])@p-p@lift(ka[0])),0.01)

    def test_wider_compatible_sphere_scheme_220_dimensions(self):
        # Retain exact 96 internal-reference subspace, exact remaining pairs
        # (34 dims), old m=3 unsharp blocks (90), and scalar remainder (34).
        # Code is 2. The old m=9 spin-4 instrument is replaced, not preserved.
        paired_remainder=self.Q-self.p
        h3=sum(np.column_stack(self.blocks[k])@np.column_stack(self.blocks[k]).conj().T
               for k in ((1,2),(2,1)))
        # Two m=3 blocks overlap paired_remainder; remove them there.
        high_pair=0
        for k in ((1,2),(2,1)):
            f=np.column_stack(self.blocks[k][:2]);high_pair=high_pair+f@f.conj().T
        exact_rem=paired_remainder-high_pair
        scalar=I256-PCODE-self.p-exact_rem-h3
        self.assertAlmostEqual(np.trace(exact_rem).real,34,places=10)
        self.assertAlmostEqual(np.trace(h3).real,90,places=10)
        self.assertAlmostEqual(np.trace(scalar).real,34,places=10)
        for p in (self.p,exact_rem,h3,scalar):
            np.testing.assert_allclose(p@p,p,atol=1e-12)
            for g in self.g:np.testing.assert_allclose(g@p-p@g,0,atol=1e-12)
        np.testing.assert_allclose(PCODE+self.p+exact_rem+h3+scalar,I256,atol=1e-12)
        for key in ((1,2),(2,1)):
            paths=self.blocks[key];flat=np.column_stack(paths);d=paths[0].shape[1]
            effects,_,ka,_=spin_instrument(3)
            a,b=[flat@np.kron(x,np.eye(d))@flat.conj().T for x in effects[:2]]
            self.assertGreater(np.linalg.norm(a@b-b@a),.01)
            for x in ka:
                op=flat@np.kron(x,np.eye(d))@flat.conj().T
                for g in self.g:np.testing.assert_allclose(op@g-g@op,0,atol=1e-12)
                for h in (HA,HB):np.testing.assert_allclose(op@h-h@op,0,atol=1e-12)
        states=[full_state(4),output(active_base()),output(compressed_spin_base(3)),output(remainder_base())]
        for labels in (tuple(range(16)),(15,0,1)):
            tabs=[i_r_m_table(relative_read(s,4,labels=labels)) for s in states]
            p=len(labels)/16
            total=sum(w*t for w,t in zip((2,130,90,34),tabs))/256
            old=(2*tabs[0]+190*tabs[1]+64*tabs[3])/256
            np.testing.assert_allclose(total,old,atol=1e-12)
            np.testing.assert_allclose(total.sum(axis=(1,2)),p*np.array(q),atol=1e-12)
            self.assertAlmostEqual(total[:,0,1].sum(),p/4,places=12)
            self.assertAlmostEqual(96*tabs[1].sum()/256,p*3/8,places=12)
        # 220 = 130 exact + 90 unsharp; plus the original 2D code.

    def test_full_229_coverage_with_reduced_reference_sector(self):
        # Use only one 4-copy group inside m=9, leaving a 5-copy spin-2
        # multiplicity for a genuinely noncommuting *unsharp* instrument.
        items=[aligned_sector(self.blocks[k],1) for k in ((0,1),(1,0),(1,1))]
        valid=sum(F@F.conj().T for _,F,_ in items)
        self.assertAlmostEqual(np.trace(valid).real,60,places=10)
        for t,F,bob in items:
            p=F@F.conj().T
            ka,kb,aa,bb,ds,es=physical_operators(F,bob,t)
            for old,new in zip(self.a,aa):np.testing.assert_allclose(old@p,new,atol=1e-12)
            for old,new in zip(self.b,bb):np.testing.assert_allclose(old@p.conj(),new,atol=1e-12)
            coords=F.conj().T@(p/16)@bob.conj()
            np.testing.assert_allclose(coords,kron(I,J.T,np.eye(t))/16,atol=1e-12)
            for i,a in enumerate(aa):
                for j,b in enumerate(bb):
                    branch=a@(p/16)@b.T
                    expected=kron(ka[i],I,np.eye(t))@kron(I,J.T,np.eye(t))@kron(kb[j].T,I,np.eye(t))/16
                    np.testing.assert_allclose(F.conj().T@branch@bob.conj(),expected,atol=1e-12)
                    for x,y in zip(ds,es):np.testing.assert_allclose(x@branch+branch@y.T,0,atol=1e-12)
        # Exact remainder: 34 dimensions after removing the two m=3
        # paired pieces and the four still-unused paths in m=9.
        old_m3=0
        for key in ((1,2),(2,1)):
            f=np.column_stack(self.blocks[key][:2]);old_m3=old_m3+f@f.conj().T
        f=np.column_stack(self.blocks[(1,1)][4:8]);old_m9=f@f.conj().T
        exact_rem=self.Q-valid-old_m3-old_m9
        self.assertAlmostEqual(np.trace(exact_rem).real,34,places=10)
        spin_blocks=[((1,1),self.blocks[(1,1)][4:]),
                     ((1,2),self.blocks[(1,2)]),((2,1),self.blocks[(2,1)])]
        high=[]
        for key,paths in spin_blocks:
            m=len(paths);d=paths[0].shape[1];flat=np.column_stack(paths)
            proj=flat@flat.conj().T;high.append(proj)
            effects,_,aa,bb=spin_instrument(m)
            def lift(x):return flat@np.kron(x,np.eye(d))@flat.conj().T
            Alice=[lift(x) for x in aa];Bob=[lift(x.conj()).conj() for x in bb]
            e0,e1=[lift(x) for x in effects[:2]]
            self.assertGreater(np.linalg.norm(e0@e1-e1@e0),.01)
            for x in Alice+Bob:
                for g in self.g:np.testing.assert_allclose(x@g-g@x,0,atol=1e-12)
                for h in (HA,HB):np.testing.assert_allclose(x@h-h@x,0,atol=1e-12)
            physical=np.stack([a@(proj/16)@b.T for a in Alice for b in Bob],axis=-1).reshape(-1,6)
            compressed=compressed_spin_base(m).reshape(-1,6)
            np.testing.assert_allclose(physical.conj().T@physical,
                                       m*d/256*(compressed.conj().T@compressed),atol=2e-12)
        self.assertAlmostEqual(sum(np.trace(p).real for p in high),135,places=10)
        scalar=I256-PCODE-valid-exact_rem-sum(high)
        self.assertAlmostEqual(np.trace(scalar).real,25,places=10)
        for p in (valid,exact_rem,*high,scalar):
            np.testing.assert_allclose(p@p,p,atol=1e-12)
            for g in self.g:np.testing.assert_allclose(p@g-g@p,0,atol=1e-12)
        np.testing.assert_allclose(PCODE+valid+exact_rem+sum(high)+scalar,I256,atol=1e-12)
        states=[full_state(4),output(active_base()),output(compressed_spin_base(5)),
                output(compressed_spin_base(3)),output(remainder_base())]
        for labels in (tuple(range(16)),(15,0,1)):
            tabs=[i_r_m_table(relative_read(s,4,labels=labels)) for s in states]
            window=len(labels)/16
            total=sum(w*t for w,t in zip((2,94,45,90,25),tabs))/256
            np.testing.assert_allclose(total.sum(axis=(1,2)),window*np.array(q),atol=1e-12)
            self.assertAlmostEqual(total[:,0,1].sum(),window/4,places=12)
            self.assertAlmostEqual(60*tabs[1].sum()/256,window*15/64,places=12)
            d=np.array(ns)@np.array(axis)
            value=np.einsum('i,irt,r->',d,total,[1,-1])/window
            expected=(-56833/486400 if len(labels)==16 else -0.117551124397824)
            self.assertAlmostEqual(value,expected,places=12)
        # 229 = 94 exact qubit + 45 spin-2 + 90 spin-1.
        # This changes the old m=9 POVM; it preserves its coverage, not it.

if __name__=='__main__':unittest.main()
