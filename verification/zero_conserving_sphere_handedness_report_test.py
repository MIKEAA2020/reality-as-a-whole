"""Conserved sign from an existing sphere factor, not old chirality.

The new pointer reports a deliberately selected transverse Bloch direction.
The pre-existing sphere instrument is unchanged before this later readout;
the later readout disturbs its postmeasurement qubit. No felt valence,
subjecthood, autonomous control or objective global energy is assumed.
"""
import math
import unittest
import numpy as np
from verification.zero_all_sector_noncommuting_sphere_test import (
    I,X,Y,Z,J,I256,HA,HB,kron,original_effects,bob_effects,
    active_base,output,relative_read
)
import verification.zero_orientation_extension_operational_boundary_test as extension
from verification.zero_nested_sphere_internal_reference_test import lift_pair
from verification.zero_relational_chirality_report_test import (
    initial,apply64,C,LL
)
from verification.zero_relative_gauge_invariant_report_test import (
    VP,VM,G
)

SIG=(X,Y,Z)
BF=(-X,-Y,Z)


def bob_action(op,v):
    return np.einsum('uv,av...->au...',op,v,optimize=True)


def coeffs(op):return np.array([np.trace(op@x).real for x in SIG])


def table_ij(v):
    return np.sum(abs(v)**2,axis=(0,1,2,3,4,5,8,9,10,11,12,13))


def j_sign(v):
    shape=[1]*v.ndim;shape[7]=2
    return v*np.array([1,-1]).reshape(shape)


class ConservingSphereHandednessReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old=extension.OrientationExtensionAndBoundaryTests
        cls.old.setUpClass()
        old=cls.old
        # Relative transverse direction from the actual two pre-existing
        # Bloch settings in Bob's logical convention, not a new z-axis.
        kb=[J.conj().T@x@J for x in bob_effects()]
        cls.b=coeffs(kb[0]); ref=J.conj().T@original_effects()[0]@J
        cls.u=coeffs(ref)/np.trace(ref).real
        cls.c=np.cross(cls.b,cls.u);cls.c/=np.linalg.norm(cls.c)
        cls.B=sum(t*x for t,x in zip(cls.b,SIG))
        cls.V=sum(t*x for t,x in zip(cls.c,SIG))
        def boblift(x):return lift_pair(old.u,old.v,x.conj()).conj()
        cls.phys_b=boblift(cls.B);cls.phys_v=boblift(cls.V)
        cls.pb=old.Q.conj()
        cls.signp=[(cls.pb+cls.phys_v)/2,(cls.pb-cls.phys_v)/2]

    def test_geometry_and_exact_local_sphere_instrument(self):
        old=self.old
        self.assertAlmostEqual(np.linalg.norm(self.b),1,places=13)
        self.assertAlmostEqual(np.linalg.norm(self.u),1,places=13)
        self.assertAlmostEqual(np.dot(self.b,self.c),0,places=13)
        np.testing.assert_allclose(self.c,[0,1/math.sqrt(2),1/math.sqrt(2)],atol=1e-13)
        np.testing.assert_allclose(self.B@self.B,I,atol=1e-13)
        np.testing.assert_allclose(self.V@self.V,I,atol=1e-13)
        np.testing.assert_allclose(self.B@self.V+self.V@self.B,0,atol=1e-13)
        for p in self.signp:np.testing.assert_allclose(p@p,p,atol=1e-12)
        np.testing.assert_allclose(sum(self.signp),self.pb,atol=1e-12)
        np.testing.assert_allclose(self.signp[0]@self.signp[1],0,atol=1e-12)
        # Full physical controlled gate U=(I-Pminus)⊗I+Pminus⊗X,
        # including inactive sectors, is unitary because Pminus is a projector.
        p=self.signp[1]
        np.testing.assert_allclose((I256-p)@(I256-p)+p@p,I256,atol=1e-12)
        np.testing.assert_allclose((I256-p)@p+p@(I256-p),0,atol=1e-12)
        for op in (self.phys_b,self.phys_v,*self.signp):
            for g in old.labg:np.testing.assert_allclose(g@op-op@g,0,atol=1e-12)
        # Actual declared lab Hamiltonians and new maximum-coverage charges.
        for op in (self.phys_b,self.phys_v,*self.signp):
            for h in (HA,HB):np.testing.assert_allclose(h@op-op@h,0,atol=1e-12)
            for x in old.full:
                bob=-x.conj();np.testing.assert_allclose(bob@op-op@bob,0,atol=1e-12)
        # The previous Bob instrument has eigenstates of B, while the new
        # sign measures its orthogonal V: it is not a nondisturbing report.
        self.assertGreater(np.linalg.norm(self.phys_v@old.b[0]-old.b[0]@self.phys_v),1)

    def test_full_original_state_and_every_branch_retain_108_orientation_zero(self):
        old=self.old
        for a in old.a:
            for j,b in enumerate(old.b):
                prior=a@old.whole@b.T
                active=prior@self.pb.T
                np.testing.assert_allclose(active@self.phys_b.T,(1-2*j)*active,atol=1e-12)
                for p in self.signp:
                    branch=prior@p.T
                    self.assertAlmostEqual(np.linalg.norm(branch)**2,np.linalg.norm(active)**2/2,places=12)
                    for x in old.full:
                        y=-x.conj()
                        np.testing.assert_allclose(x@branch+branch@y.T,0,atol=1e-12)
                    for g in old.labg:np.testing.assert_allclose(g@branch-branch@g.T,0,atol=1e-12)
                    np.testing.assert_allclose(HA@branch+branch@HB.T,0,atol=1e-12)
        # All 190 old exact-qubit complement dimensions have a valid sign;
        # the 66-dimensional code/scalar remainder is retained without one.
        self.assertAlmostEqual(np.trace(self.pb).real,190,places=10)
        self.assertAlmostEqual(np.linalg.norm(self.pb@old.whole)**2,190/256,places=12)
        self.assertAlmostEqual(np.linalg.norm((I256-self.pb)@old.whole)**2,66/256,places=12)

    def test_neutral_pointer_gate_and_nonlocal_gauge_redundancy(self):
        # Local Bob sign gate is exact with a neutral pointer, including
        # its active/inactive branches. Its generator inherits all tested
        # lab-charge and 108-orientation commutators.
        m=(I-self.V)/2
        gate=kron(I-m,I)+kron(m,X)
        h=math.pi/2*kron(m,I-X)
        vals,vec=np.linalg.eigh(h)
        np.testing.assert_allclose((vec*np.exp(-1j*vals))@vec.conj().T,gate,atol=1e-13)
        np.testing.assert_allclose(gate.conj().T@gate,np.eye(4),atol=1e-13)
        # The old diagonal swap, expressed in the m=9 four-copy canonical
        # basis, is identity on the full 3/2 × 3/2 orientation-zero sector.
        a=[kron(x,I,I,I) for x in SIG]
        b=[kron(I,x,I,I) for x in BF]
        d=[kron(I,I,x,I) for x in SIG]
        e=[kron(I,I,I,x) for x in SIG]
        ga=(np.eye(16)+sum(x@y for x,y in zip(a,b)))/2
        gb=(np.eye(16)+sum(x@y for x,y in zip(d,e)))/2
        g=(ga@gb).reshape((2,)*8).transpose(0,2,1,3,4,6,5,7).reshape(16,16)
        _,amp,transform=extension.v_canonical()
        g=kron(np.eye(4),transform.conj().T)@g@kron(np.eye(4),transform)
        total=[kron(x,np.eye(4))-kron(np.eye(4),x.T) for x in extension.spin_generators(4)]
        cas=sum(x@x for x in total);id16=np.eye(16)
        p0=(8*id16-cas)@(24*id16-cas)@(48*id16-cas)/(8*24*48)
        self.assertAlmostEqual(np.trace(p0).real,1,places=12)
        ev=np.linalg.eigvalsh(cas)
        np.testing.assert_allclose(ev,[0]+[8]*3+[24]*5+[48]*7,atol=1e-12)
        phi=np.eye(4).reshape(16)/2
        np.testing.assert_allclose(p0@phi,phi,atol=1e-12)
        np.testing.assert_allclose(g@p0,p0,atol=1e-12)
        self.assertGreater(np.linalg.norm(g@total[0]-total[0]@g),1)
        # G is not asserted to commute with the new generators outside the
        # zero sector; on that sector it acts identically. On other blocks
        # its chosen extension is the identity. V acts on sphere instead.

    def test_all_old_clock_labels_report_new_sign_with_preserved_records(self):
        state=output(active_base());ideal=np.array([[3/40,1/20],[1/10,3/10],[13/40,3/20]])
        for label in range(16):
            old=relative_read(state,4,labels=(label,))[0]
            v=initial(old);mass=np.linalg.norm(v)**2
            np.testing.assert_allclose(bob_action(self.B,v),j_sign(v),atol=1e-13)
            np.testing.assert_allclose(apply64(G,v),v,atol=1e-13)
            signs=[(v+bob_action(self.V,v))/2,(v-bob_action(self.V,v))/2]
            for sign,branch in zip((1,-1),signs):
                np.testing.assert_allclose(bob_action(self.V,branch),sign*branch,atol=1e-13)
                np.testing.assert_allclose(apply64(G,branch),branch,atol=1e-13)
                np.testing.assert_allclose(apply64(LL,branch),branch,atol=1e-13)
                np.testing.assert_allclose(table_ij(branch),mass*ideal/2,atol=1e-13)
            # T0=Z_j B preserves the prepared source and swaps the branches;
            # appending X_M yields a counterpart symmetry of the final record.
            np.testing.assert_allclose(j_sign(bob_action(self.B,v)),v,atol=1e-13)
            np.testing.assert_allclose(j_sign(bob_action(self.B,signs[0])),signs[1],atol=1e-13)
            np.testing.assert_allclose(j_sign(bob_action(self.B,signs[1])),signs[0],atol=1e-13)
            # A repeat of Bob's old sphere measurement returns either j' with
            # equal probability conditional on original j and either new sign.
            for j in (0,1):
                shape=[1]*v.ndim;shape[7]=2;mask=np.zeros(2);mask[j]=1
                part=v*mask.reshape(shape)
                for sign in (1,-1):
                    x=(part+sign*bob_action(self.V,part))/2
                    for j2 in (0,1):
                        reread=(x+(1-2*j2)*bob_action(self.B,x))/2
                        self.assertAlmostEqual(np.linalg.norm(reread)**2,np.linalg.norm(x)**2/2,places=13)

    def test_new_and_old_signs_are_independent_in_old_conserving_72_sector(self):
        # In the 90D orientation option both observables commute with the
        # same total charge and act on different tensor factors. This checks
        # the actual old history, not a claim that the old sign is conserved
        # in the alternative 108D spin-3/2 orientation.
        state=output(active_base())
        for label in range(16):
            v=initial(relative_read(state,4,labels=(label,))[0]);mass=np.linalg.norm(v)**2
            total=0.
            for p in (VP,VM):
                oldbranch=apply64(p,v)
                for sign in (1,-1):
                    both=(oldbranch+sign*bob_action(self.V,oldbranch))/2
                    self.assertAlmostEqual(np.linalg.norm(both)**2,mass/4,places=12)
                    for c in C:np.testing.assert_allclose(apply64(c,both),0,atol=1e-13)
                    np.testing.assert_allclose(apply64(G,both),both,atol=1e-13)
                    total+=np.linalg.norm(both)**2
            self.assertAlmostEqual(total,mass,places=12)
        # The two signs agree on half the Born weight, disagree on half.
        # Both are operational labels, not derived experiential values.

if __name__=='__main__':unittest.main()
