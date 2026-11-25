"""An alternative upstream invariant preparation of the old relative history.

The old RWT orientation qubit is *encoded directly* in an original lab
multiplicity qubit rather than prepared independently and subsequently swapped.
Only the stated orientation and lab charges/energy are modeled; the state,
encoding, controls, clock and interface remain stipulated.
"""
import math
import unittest
import numpy as np
from verification.zero_all_sector_noncommuting_sphere_test import (
    decomposition,local_charges,HA,HB,I256,PCODE,CODE,J,kron,active_base,
    output,relative_read,original_effects,bob_effects
)
from verification.zero_energy_sphere_work_incidence_test import (
    I,X,Y,Z,embed_records_and_work,target_memory,relative_effect_roots
)
from verification.zero_relational_orientation_reference_test import U8,U1,Jw,with_reference
from verification.zero_relational_chirality_report_test import (
    SING,initial,apply64,outcome_tables,C,LL,eps
)
from verification.zero_relative_gauge_invariant_report_test import (
    V,VP,VM,G,SOURCE
)
from verification.zero_internal_f_reference_transfer_test import triple_basis,lift,PSI
from verification.zero_nested_sphere_internal_reference_test import lift_pair
from verification.zero_five_ray_record_current_unification_test import q,ns,axis
from verification.zero_reciprocal_subject_exchange_test import n

P=(X,Y,Z)
BF=(-X,-Y,Z)


def factorization():
    vals,vec=np.linalg.eigh(Jw)
    plus=vec[:,vals>.5]
    minus=U8@plus
    return np.column_stack((plus,minus))


def history_vectors(T):
    # The same old RWT action, separately for the actual Bob pointer j.
    seed=np.ones((1,1,1,1,1,1,1,2),complex)
    x=target_memory(embed_records_and_work(seed),math.pi/2)
    states=np.array([x[(0,0,0,0,0,0,0,j)].reshape(8) for j in (0,1)])
    coords=np.array([(T.conj().T@v).reshape(2,4) for v in states])
    return states,math.sqrt(2)*coords[:,0,:]


def unitary_preparing(v):
    u,_=np.linalg.qr(np.column_stack((v,np.eye(len(v)))))
    u[:,0]*=np.vdot(u[:,0],v)
    return u


def decode(dstate,T):
    # dstate prefixes (...,4) include the old sphere and pointer/clock axes.
    x=np.einsum('...n,af,de->...anfde',dstate,PSI,SING)
    y=np.einsum('xp,...pfde->...xfde',T,x.reshape(x.shape[:-5]+(8,2,2,2)))
    return y.reshape(y.shape[:-4]+(2,2,2,2,2,2))


def select_clock_on_deg(deg,label):
    root=relative_effect_roots(4,4,16)[label].reshape(4,4,4,4)
    return np.einsum('uvcd,abrcsdijn->abrusvijn',root,deg,optimize=True)


class UpstreamInvariantInternalHistoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        *_,blocks,cls.u,cls.v,cls.odd,_=decomposition()
        cls.d,cls.f,cls.b=triple_basis(blocks[(1,1)])
        cls.p=cls.f@cls.f.conj().T
        cls.g=local_charges()
        cls.T=factorization()
        cls.oldstates,cls.etas=history_vectors(cls.T)
        cls.unitaries=[unitary_preparing(v) for v in cls.etas]

    def test_same_input_has_an_exact_all_sector_zero_orientation(self):
        d,f,b,p=self.d,self.f,self.b,self.p
        ds=[lift(f,d,kron(I,x,I)) for x in P]
        hs=[lift(f,d,kron(I,I,x)) for x in P]
        es=[lift(b,d,kron(I,x,I)) for x in P]
        fs=[lift(b,d,kron(I,I,x)) for x in BF]
        la=[x+y for x,y in zip(ds,hs)]
        lb=[x+y for x,y in zip(es,fs)]
        whole=(CODE@J@CODE.T+I256-PCODE).T/16
        self.assertAlmostEqual(np.linalg.norm(whole)**2,1,places=12)
        np.testing.assert_allclose(p@whole,whole@p.conj().T,atol=1e-12)
        for a,bob in zip(la,lb):
            np.testing.assert_allclose(a@whole+whole@bob.T,0,atol=1e-12)
            for x in self.g:np.testing.assert_allclose(a@x-x@a,0,atol=1e-12)
            for x in self.g:np.testing.assert_allclose(bob@x-x@bob,0,atol=1e-12)
            for h in (HA,HB):
                np.testing.assert_allclose(a@h-h@a,0,atol=1e-12)
                np.testing.assert_allclose(bob@h-h@bob,0,atol=1e-12)
        for ops,proj in ((ds,p),(hs,p),(es,p.conj()),(fs,p.conj())):
            for i,j,k in ((0,1,2),(1,2,0),(2,0,1)):
                np.testing.assert_allclose(ops[i]@ops[j]-ops[j]@ops[i],2j*ops[k],atol=1e-12)
                np.testing.assert_allclose(ops[i]@ops[i],proj,atol=1e-12)
        for first,second in ((ds,hs),(es,fs)):
            for x in first:
                for y in second:np.testing.assert_allclose(x@y-y@x,0,atol=1e-12)
        for i,j,k in ((0,1,2),(1,2,0),(2,0,1)):
            np.testing.assert_allclose(la[i]@la[j]-la[j]@la[i],2j*la[k],atol=1e-12)
            np.testing.assert_allclose(lb[i]@lb[j]-lb[j]@lb[i],2j*lb[k],atol=1e-12)
        # The chosen orientation representation is trivial outside the
        # 72-dimensional support on each lab. The original lab charge
        # generators are different and are not being redefined here.
        ka=[x/math.sqrt(np.trace(x).real) for x in original_effects()]
        kb=[J.conj().T@x@J for x in bob_effects()]
        Q=self.u@self.u.conj().T+self.v@self.v.conj().T
        a=[lift_pair(self.u,self.v,x)+math.sqrt(qi)*(I256-Q) for x,qi in zip(ka,q)]
        bb=[lift_pair(self.u,self.v,x.conj()).conj()+(I256-Q.conj())/math.sqrt(2) for x in kb]
        np.testing.assert_allclose(sum(x.conj().T@x for x in a),I256,atol=1e-12)
        np.testing.assert_allclose(sum(x.conj().T@x for x in bb),I256,atol=1e-12)
        for x in a:
            for y in la:np.testing.assert_allclose(x@y-y@x,0,atol=1e-12)
            for y in self.g:np.testing.assert_allclose(x@y-y@x,0,atol=1e-12)
            for y in (HA,HB):np.testing.assert_allclose(x@y-y@x,0,atol=1e-12)
        for x in bb:
            for y in lb:np.testing.assert_allclose(x@y-y@x,0,atol=1e-12)
            for y in self.g:np.testing.assert_allclose(x@y-y@x,0,atol=1e-12)
            for y in (HA,HB):np.testing.assert_allclose(x@y-y@x,0,atol=1e-12)
        for x in a:
            for y in bb:
                branch=x@whole@y.T
                for left,right in zip(la,lb):
                    np.testing.assert_allclose(left@branch+branch@right.T,0,atol=1e-12)
                for g in self.g:np.testing.assert_allclose(g@branch-branch@g.T,0,atol=1e-12)
                np.testing.assert_allclose(HA@branch+branch@HB.T,0,atol=1e-12)
        # Exact old 190-dimensional sphere preserved; code and scalar
        # remainder here use neutral effects, not the old code instrument.

    def test_factorization_and_conserving_neutral_record_control(self):
        T=self.T
        np.testing.assert_allclose(T.conj().T@T,np.eye(8),atol=1e-13)
        for a,x in zip((U8,U1,Jw),P):
            np.testing.assert_allclose(T.conj().T@a@T,kron(x,np.eye(4)),atol=1e-13)
        for state,eta,u in zip(self.oldstates,self.etas,self.unitaries):
            np.testing.assert_allclose(T.conj().T@state,kron(np.array([1,1])/math.sqrt(2),eta),atol=1e-13)
            np.testing.assert_allclose(u.conj().T@u,np.eye(4),atol=1e-13)
            np.testing.assert_allclose(u[:,0],eta,atol=1e-13)
        self.assertAlmostEqual(abs(np.vdot(*self.etas)),0,places=12)
        # Charge algebra acts only on the four spin factors A,F,D,E;
        # each pointer-controlled U_j acts only on neutral degeneracy.
        spin=[kron(x,I,I,I)+kron(I,y,I,I)+kron(I,I,x,I)+kron(I,I,I,x)
              for x,y in zip(P,BF)]
        ctrl=kron(np.diag([1,0]),self.unitaries[0])+kron(np.diag([0,1]),self.unitaries[1])
        np.testing.assert_allclose(ctrl.conj().T@ctrl,np.eye(8),atol=1e-13)
        for c in spin:
            u=kron(ctrl,np.eye(16)); total=kron(np.eye(8),c)
            np.testing.assert_allclose(u@total-total@u,0,atol=1e-13)
        # Previously declared active total and pair numbers are scalars,
        # so their encoded operators and the new neutral control commute.
        for inds in ((0,1,2,3),(0,1),(2,3),(0,2),(1,3)):
            old=sum(np.asarray(n[i]) for i in inds)[np.ix_([6,9],[6,9])]
            np.testing.assert_allclose(old,np.eye(2)*(2 if len(inds)==4 else 1),atol=1e-13)

    def test_old_sign_is_exactly_a_joint_operation_on_encoded_lab_spins(self):
        aa=[kron(x,I,I,I) for x in P]
        bb=[kron(I,x,I,I) for x in BF]
        dd=[kron(I,I,x,I) for x in P]
        ee=[kron(I,I,I,x) for x in P]
        va=sum(s*(aa[i]-bb[i])@dd[j]@ee[k] for i,j,k,s in eps)/(4*math.sqrt(3))
        charges=[a+b+d+e for a,b,d,e in zip(aa,bb,dd,ee)]
        for c in charges:np.testing.assert_allclose(va@c-c@va,0,atol=1e-13)
        # Change old RWT basis into [A, neutral degeneracy], then compare
        # the whole 64-dimensional operator including its multiplicity.
        old=kron(self.T.conj().T,I,I,I)@V@kron(self.T,I,I,I)
        lifted=np.kron(va,np.eye(4)).reshape(2,2,2,2,4,2,2,2,2,4)
        lifted=lifted.transpose(0,4,1,2,3,5,9,6,7,8).reshape(64,64)
        np.testing.assert_allclose(old,lifted,atol=1e-13)
        # Hence its spectral projectors and pointer gate are invariant
        # polynomials in the actual encoded lab spin operators, not an
        # abstract extra F or an unaccounted fifth spin.

    def test_complete_old_reference_history_is_reproduced_from_invariant_source(self):
        base=active_base();old=output(base)
        np.testing.assert_allclose(old,np.einsum('...ij,jrwt->...ijrwt',base,self.oldstates.reshape(2,2,2,2)),atol=1e-13)
        blank=np.array([1,0,0,0],complex)
        prepared=np.einsum('...ij,jn->...ijn',base,np.array([u@blank for u in self.unitaries]))
        actual=decode(prepared,self.T)
        np.testing.assert_allclose(actual,initial(old),atol=1e-13)
        for c in C:np.testing.assert_allclose(apply64(c,actual),0,atol=1e-13)
        np.testing.assert_allclose(apply64(LL,actual),actual,atol=1e-13)
        for label in range(16):
            old_label=relative_read(old,4,labels=(label,))[0]
            encoded=decode(select_clock_on_deg(prepared,label),self.T)
            np.testing.assert_allclose(encoded,initial(old_label),atol=1e-13)
            for c in C:np.testing.assert_allclose(apply64(c,encoded),0,atol=1e-13)
            np.testing.assert_allclose(apply64(SOURCE,encoded),encoded,atol=1e-13)
            np.testing.assert_allclose(apply64(V@V,encoded),encoded,atol=1e-13)
            branches,tab=outcome_tables(encoded);mass=np.linalg.norm(encoded)**2
            np.testing.assert_allclose(tab,np.array(q)[:,None]*mass/2*np.ones((1,2)),atol=1e-13)
            for proj,branch in zip((VP,VM),branches):
                np.testing.assert_allclose(apply64(proj,encoded),branch,atol=1e-13)
                for c in C:np.testing.assert_allclose(apply64(c,branch),0,atol=1e-13)
                np.testing.assert_allclose(apply64(G,branch),branch,atol=1e-13)
                np.testing.assert_allclose(apply64(LL,branch),branch,atol=1e-13)
            self.assertAlmostEqual(tab[(np.array(ns)@np.array(axis))<0].sum()/mass,3/5,places=12)

    def test_no_unrecorded_72_over_256_postselection(self):
        whole=(CODE@J@CODE.T+I256-PCODE).T/16
        valid=self.p@whole;other=(I256-self.p)@whole
        np.testing.assert_allclose(whole,valid+other,atol=1e-12)
        self.assertAlmostEqual(np.linalg.norm(valid)**2,9/32,places=12)
        self.assertAlmostEqual(np.linalg.norm(other)**2,23/32,places=12)
        self.assertAlmostEqual(abs(np.vdot(valid,other)),0,places=12)
        # The flag, if read, has these weights. Only flag=1 has the RWT
        # encoding and report; flag=0 is retained, orientation-trivial and
        # carries no assertion of a new ± sign.

if __name__=='__main__':unittest.main()
