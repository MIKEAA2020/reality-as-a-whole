"""Conditional sign uniqueness, and an explicit old-record counterexample.

The antiunitary below is a specified mathematical spin reversal, not a derived
physical time reversal of the lab, clock, apparatus, or experiential law.
The record-dependent sign needs a joint interface to that actual record.
"""
import math
import unittest
import numpy as np
from verification.zero_all_sector_noncommuting_sphere_test import (
    I,X,Y,Z,kron,active_base,output,relative_read
)
from verification.zero_relational_chirality_report_test import (
    initial,apply64,C,LL,SWAP,eps,SING
)
from verification.zero_relative_gauge_invariant_report_test import V,VP,VM,G
from verification.zero_internal_f_reference_transfer_test import PSI
from verification.zero_upstream_invariant_internal_history_test import factorization
from verification.zero_invariant_all_history_record_clock_test import XL,ZL
from verification.zero_conserving_sphere_handedness_report_test import j_sign,table_ij,bob_action
import verification.zero_orientation_extension_operational_boundary_test as extension
from verification.zero_nested_sphere_internal_reference_test import lift_pair
from verification.zero_all_sector_noncommuting_sphere_test import J,bob_effects,HA,HB

SIG=(X,Y,Z);BF=(-X,-Y,Z);eye=np.eye(16)
a=[kron(x,I,I,I) for x in SIG]
b=[kron(I,x,I,I) for x in BF]
d=[kron(I,I,x,I) for x in SIG]
e=[kron(I,I,I,x) for x in SIG]
charges=[sum(z) for z in zip(a,b,d,e)]
cas=sum(x@x for x in charges)
p=(cas-8*eye)@(cas-24*eye)/192
swap=(eye+sum(x@y for x,y in zip(d,e)))/2
gab=(eye+sum(x@y for x,y in zip(a,b)))/2
g=gab@swap
v=sum(s*(a[i]-b[i])@d[j]@e[k] for i,j,k,s in eps)/(4*math.sqrt(3))
vs=p@v@p
# Antiunitary Θ = t K; Θ²=+I on four spin-1/2 factors.
t=kron(*([1j*Y]*4))


def reversal(op):return t@op.conj()@t.conj().T


def physical_old_to_canonical(op):
    f=factorization()
    return kron(f.conj().T,I,I,I)@op@kron(f,I,I,I)


def lift_with_neutral(x,n):
    # A,F,D,E,N order -> A,N,F,D,E, matching old compressed space.
    return kron(x,n).reshape((2,2,2,2,4)*2).transpose(
        0,4,1,2,3,5,9,6,7,8).reshape(64,64)


def lift_spin(x):return lift_with_neutral(x,np.eye(4))


def hermitian_basis(n):
    result=[]
    for j in range(n):
        z=np.zeros((n,n),complex);z[j,j]=1;result.append(z)
    for j in range(n):
        for k in range(j+1,n):
            z=np.zeros((n,n),complex);z[j,k]=z[k,j]=1;result.append(z)
            z=np.zeros((n,n),complex);z[j,k]=-1j;z[k,j]=1j;result.append(z)
    return result


class SpinReversalSignSelectionTests(unittest.TestCase):
    def test_actual_old_spin_representation_is_the_canonical_four_spin_model(self):
        np.testing.assert_allclose(physical_old_to_canonical(V),lift_spin(v),atol=1e-13)
        np.testing.assert_allclose(physical_old_to_canonical(SWAP),lift_spin(swap),atol=1e-13)
        for old,new in zip(C,charges):
            np.testing.assert_allclose(physical_old_to_canonical(old),lift_spin(new),atol=1e-13)
        self.assertAlmostEqual(np.trace(p).real,2,places=12)
        np.testing.assert_allclose(p@p,p,atol=1e-13)
        np.testing.assert_allclose(g@p,p,atol=1e-13)
        source=kron(PSI.reshape(4),SING.reshape(4))
        np.testing.assert_allclose(p@source,source,atol=1e-13)
        np.testing.assert_allclose(swap@source,-source,atol=1e-13)
        # This validates spin-factor invariance only, not time reversal of
        # the full sphere/clock history or its chosen instruments.
        self.assertAlmostEqual(abs(np.vdot(source,t@source.conj())),1,places=12)

    def test_exchange_and_spin_reversal_select_unique_spin_only_odd_operator(self):
        np.testing.assert_allclose(t@t.conj(),eye,atol=1e-13)
        for x in charges:np.testing.assert_allclose(reversal(x),-x,atol=1e-13)
        np.testing.assert_allclose(reversal(p),p,atol=1e-13)
        np.testing.assert_allclose(reversal(swap),swap,atol=1e-13)
        np.testing.assert_allclose(reversal(vs),-vs,atol=1e-13)
        s=p@swap@p;w=1j*s@vs
        np.testing.assert_allclose(vs@vs,p,atol=1e-13)
        np.testing.assert_allclose(s@s,p,atol=1e-13)
        np.testing.assert_allclose(s@vs+vs@s,0,atol=1e-13)
        np.testing.assert_allclose(w,w.conj().T,atol=1e-13)
        for x in (p,s,vs,w):np.testing.assert_allclose(p@x@p,x,atol=1e-13)
        # Four orthogonal nonzero Hermitian matrices span all Hermitian
        # operators on the two-dimensional total-zero spin sector.
        basis=(p,s,vs,w)
        gram=np.array([[np.trace(x@y).real for y in basis] for x in basis])
        np.testing.assert_allclose(gram,2*np.eye(4),atol=1e-13)
        # Parities (exchange, spin reversal): (++), (++), (--), (-+).
        for x,exchange,time in zip(basis,(1,1,-1,-1),(1,1,-1,1)):
            np.testing.assert_allclose(swap@x@swap,exchange*x,atol=1e-13)
            np.testing.assert_allclose(reversal(x),time*x,atol=1e-13)
        # Therefore only real multiples of vs meet both odd conditions;
        # the sharp ±1 condition fixes the magnitude, not the global sign.

    def test_full_neutral_multiplicity_clock_and_work_select_one_on_L_plus(self):
        # All Hermitian operators on spin-zero (rank 2) ⊗ neutral N (dim 4):
        # real dimension 64. No spin-only assumption is made here.
        s=p@swap@p;w=1j*s@vs
        basis=[lift_with_neutral(x,n) for x in (p,s,vs,w) for n in hermitian_basis(4)]
        ss=lift_spin(swap);tt=lift_spin(t);pp=lift_spin(p)
        clocks=[physical_old_to_canonical(kron(x,I,I)) for x in (XL,ZL)]
        work=physical_old_to_canonical(LL)
        for x in (*clocks,work):np.testing.assert_allclose(pp@x-x@pp,0,atol=1e-13)
        def residual(op):
            terms=[ss@op@ss+op,tt@op.conj()@tt.conj().T+op]
            terms += [x@op-op@x for x in (*clocks,work)]
            x=np.concatenate([term.ravel() for term in terms])
            return np.r_[x.real,x.imag]
        matrix=np.column_stack([residual(x) for x in basis])
        singular=np.linalg.svd(matrix,compute_uv=False)
        self.assertEqual(np.count_nonzero(singular<1e-9),2)
        self.assertGreater(singular[-3],2)
        old=lift_spin(vs)
        # The two obvious independent solutions span the computed kernel.
        for x in (old,old@work):np.testing.assert_allclose(residual(x),0,atol=1e-13)
        self.assertEqual(np.linalg.matrix_rank(np.column_stack((old.ravel(),(old@work).ravel())),tol=1e-9),2)
        valid=pp@(np.eye(64)+work)/2
        self.assertAlmostEqual(np.trace(valid).real,4,places=12)
        np.testing.assert_allclose(old@work@valid,old@valid,atol=1e-13)
        np.testing.assert_allclose((old@valid)@(old@valid),valid,atol=1e-13)
        # Constructive proof on L=+1: the sign pair and clock pair are two
        # mutually commuting qubit algebras and their 16 products span M4.
        s=ss@valid;v=old@valid;xx,zz=[c@valid for c in clocks]
        for x in (s,v,xx,zz):np.testing.assert_allclose(x@x,valid,atol=1e-13)
        np.testing.assert_allclose(s@v+v@s,0,atol=1e-13)
        np.testing.assert_allclose(xx@zz+zz@xx,0,atol=1e-13)
        for a in (s,v):
            for b in (xx,zz):np.testing.assert_allclose(a@b-b@a,0,atol=1e-13)
        left=(valid,s,v,1j*s@v);right=(valid,xx,zz,1j*xx@zz)
        product=[a@b for a in left for b in right]
        gram=np.array([[np.trace(a@b).real for b in product] for a in product])
        np.testing.assert_allclose(gram,4*np.eye(16),atol=1e-12)
        # Commuting with both clocks leaves exactly the left M2; exchange
        # odd leaves v, iSV; spin reversal odd leaves only v. Normalizing
        # the square to valid yields ±v.

    def test_existing_bob_sphere_sign_gives_record_independent_counterexample(self):
        old=extension.OrientationExtensionAndBoundaryTests
        old.setUpClass()
        eff=J.conj().T@bob_effects()[0]@J
        bloch=np.array([np.trace(eff@x).real for x in SIG])
        B=sum(c*x for c,x in zip(bloch,SIG))
        pb=old.Q.conj()
        physical=lift_pair(old.u,old.v,B.conj()).conj()
        np.testing.assert_allclose(B@B,I,atol=1e-13)
        np.testing.assert_allclose(physical@physical,pb,atol=1e-12)
        # B is the previously measured Bob axis, unlike transverse V_s.
        # It commutes with BOTH old Bob Kraus operators, the lab charges,
        # Hamiltonians and the full sign-preserving orientation extension.
        for op in (*old.b,*old.labg,HA,HB,*[-x.conj() for x in old.ext]):
            np.testing.assert_allclose(physical@op-op@physical,0,atol=1e-12)
        for j,k in enumerate(old.b):
            np.testing.assert_allclose(physical@k,(1-2*j)*pb@k,atol=1e-12)
        # A specified antiunitary extension acting as complex conjugation in
        # a B-eigenbasis makes B even. It is not asserted to be physical T.
        _,u=np.linalg.eigh(B);tb=u@u.T
        np.testing.assert_allclose(tb@tb.conj(),I,atol=1e-13)
        np.testing.assert_allclose(tb@B.conj()@tb.conj().T,B,atol=1e-13)
        pp=lift_spin(p);work=physical_old_to_canonical(LL)
        valid=pp@(np.eye(64)+work)/2
        vv=lift_spin(vs)@valid
        ss=lift_spin(swap);tt=lift_spin(t)
        clocks=[physical_old_to_canonical(kron(x,I,I)) for x in (XL,ZL)]
        for op in (kron(vv,I),kron(vv,B)):
            np.testing.assert_allclose(op@op,kron(valid,I),atol=1e-13)
            minus=(kron(valid,I)-op)/2
            gate=kron(np.eye(128)-minus,I)+kron(minus,X)
            np.testing.assert_allclose(gate.conj().T@gate,np.eye(256),atol=1e-13)
            for charge in charges:
                c=kron(lift_spin(charge),I,I)
                np.testing.assert_allclose(c@gate-gate@c,0,atol=1e-13)
            np.testing.assert_allclose(kron(ss,I)@op@kron(ss,I),-op,atol=1e-13)
            anti=kron(tt,tb)
            np.testing.assert_allclose(anti@op.conj()@anti.conj().T,-op,atol=1e-13)
            for c in (*clocks,work):
                cc=kron(c,I);np.testing.assert_allclose(op@cc-cc@op,0,atol=1e-13)
                cgate=kron(c,I,I);np.testing.assert_allclose(gate@cgate-cgate@gate,0,atol=1e-13)
            instrument=kron(np.eye(64),B,I)
            np.testing.assert_allclose(gate@instrument-instrument@gate,0,atol=1e-13)
        # In the sector preserving the B instrument the general permitted
        # candidate is vv⊗(aI+bB). Verify its square, including cross term.
        for aa,bb in ((.2,.3),(1,0),(0,1),(1/math.sqrt(2),1/math.sqrt(2))):
            candidate=kron(vv,aa*I+bb*B)
            square=kron(valid,(aa*aa+bb*bb)*I+2*aa*bb*B)
            np.testing.assert_allclose(candidate@candidate,square,atol=1e-13)
        # On the actual post-instrument histories, B and the old j register
        # agree as actions on the state, not as global operator identities.
        state=output(active_base())
        for label in range(16):
            x=initial(relative_read(state,4,labels=(label,))[0])
            np.testing.assert_allclose(bob_action(B,x),j_sign(x),atol=1e-13)
            for q in (VP,VM):
                y=apply64(q,x)
                np.testing.assert_allclose(bob_action(B,y),j_sign(y),atol=1e-13)

    def test_record_dependent_sign_also_commutes_with_actual_clock_and_work(self):
        pp=lift_spin(p);work=physical_old_to_canonical(LL)
        valid=pp@(np.eye(64)+work)/2
        vv=lift_spin(vs)@valid
        clock=[physical_old_to_canonical(kron(x,I,I)) for x in (XL,ZL)]
        ss=lift_spin(swap);tt=lift_spin(t)
        for op in (kron(vv,I),kron(vv,Z)):
            self.assertAlmostEqual(np.trace(kron(valid,I)).real,8,places=12)
            np.testing.assert_allclose(op@op,kron(valid,I),atol=1e-13)
            np.testing.assert_allclose(kron(ss,I)@op@kron(ss,I),-op,atol=1e-13)
            anti=kron(tt,I)
            np.testing.assert_allclose(anti@op.conj()@anti.conj().T,-op,atol=1e-13)
            for x in (*clock,work):
                y=kron(x,I);np.testing.assert_allclose(y@op-op@y,0,atol=1e-13)
            minus=(kron(valid,I)-op)/2
            u=kron(np.eye(128)-minus,I)+kron(minus,X)
            for x in (*clock,work):
                y=kron(x,I,I);np.testing.assert_allclose(y@u-u@y,0,atol=1e-13)
        # Both have charge-preserving gates. j is the old record register;
        # neither gate is claimed to commute with its earlier writing unitary.

    def test_adding_even_record_produces_two_distinct_normalized_signs(self):
        P=kron(p,I);S=kron(swap,I);T=kron(t,I);ZJ=kron(eye,Z)
        first=kron(vs,I);second=kron(vs,Z)
        reverse=lambda x:T@x.conj()@T.conj().T
        for op in (first,second):
            np.testing.assert_allclose(op@op,P,atol=1e-13)
            np.testing.assert_allclose(S@op@S,-op,atol=1e-13)
            np.testing.assert_allclose(reverse(op),-op,atol=1e-13)
            np.testing.assert_allclose(kron(g,I)@op@kron(g,I),op,atol=1e-13)
            for c in charges:np.testing.assert_allclose(kron(c,I)@op-op@kron(c,I),0,atol=1e-13)
            minus=(P-op)/2
            np.testing.assert_allclose(minus@minus,minus,atol=1e-13)
            # Complete neutral pointer gate: inactive subspace acts trivially.
            unitary=kron(np.eye(32)-minus,I)+kron(minus,X)
            np.testing.assert_allclose(unitary.conj().T@unitary,np.eye(64),atol=1e-13)
            for c in charges:
                cc=kron(c,I,I)
                np.testing.assert_allclose(unitary@cc-cc@unitary,0,atol=1e-13)
        self.assertGreater(np.linalg.norm(first-second),1)
        self.assertGreater(np.linalg.norm(first+second),1)
        np.testing.assert_allclose(first@second,P@ZJ,atol=1e-13)
        # In particular the j-dependent rule is neither +V nor -V.

    def test_actual_history_all_clocks_selects_equally_balanced_counterexample(self):
        state=output(active_base())
        expected=np.array([[3/40,1/20],[1/10,3/10],[13/40,3/20]])
        for label in range(16):
            x=initial(relative_read(state,4,labels=(label,))[0])
            mass=np.linalg.norm(x)**2
            np.testing.assert_allclose(table_ij(x)/mass,expected,atol=1e-13)
            for sign,q in ((1,VP),(-1,VM)):
                old=apply64(q,x)
                # For j=0 the signs agree; j=1 they are opposite.
                same=(old+j_sign(old))/2
                flip=(old-j_sign(old))/2
                self.assertAlmostEqual(np.linalg.norm(same)**2,mass/4,places=13)
                self.assertAlmostEqual(np.linalg.norm(flip)**2,mass/4,places=13)
                for part in (same,flip):
                    for charge in C:np.testing.assert_allclose(apply64(charge,part),0,atol=1e-13)
                    np.testing.assert_allclose(apply64(LL,part),part,atol=1e-13)
                    np.testing.assert_allclose(apply64(G,part),part,atol=1e-13)
                # Signs exchange under the old D/E swap; j is unaffected.
                np.testing.assert_allclose(apply64(SWAP,old),-apply64(VM if sign==1 else VP,x),atol=1e-13)
            # Projecting by the two candidate signs leaves both old records
            # intact and each candidate is equally likely within each i,j.
            old_plus=apply64(VP,x)
            second_plus=(old_plus+j_sign(old_plus))/2
            old_minus=apply64(VM,x)
            second_plus+=(old_minus-j_sign(old_minus))/2
            np.testing.assert_allclose(table_ij(old_plus)/mass,expected/2,atol=1e-13)
            np.testing.assert_allclose(table_ij(second_plus)/mass,expected/2,atol=1e-13)
            self.assertAlmostEqual(table_ij(x)[:,1].sum()/mass,.5,places=13)

if __name__=='__main__':unittest.main()
