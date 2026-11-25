"""Paired-state reference, confined readout and conservation constraints.

Subjecthood, truthful experience reports, the lab split, resources and
physical spacetime are not derived. Local discrimination is a quantum bound
for the stipulated m=2,3,9 complement instruments.
"""
from fractions import Fraction
import math
import unittest
import numpy as np
from verification.zero_all_sector_noncommuting_sphere_test import (
    I,X,Y,Z,q,ns,axis,spin_matrices,spin_instrument,active_base,
    compressed_spin_base,output,full_state,relative_read,i_r_m_table
)
from verification.zero_relational_orientation_reference_test import (
    with_reference,apply16,C1,C2,C3,L,Psing,I16
)

Q=np.array(q);N=np.array(ns);D=N@np.array(axis)


def ensemble(m):
    """Bob conditional states after Alice's actual spin-multiplicity POVM."""
    effects,_,roots,_=spin_instrument(m)
    phi=np.eye(m,dtype=complex)/math.sqrt(m)
    amps=[k@phi for k in roots]
    rho=[a.T@a.conj() for a in amps]
    return effects,rho


def trace_norm(h):return float(np.sum(np.abs(np.linalg.eigvalsh(h))))


def helstrom(m):
    _,states=ensemble(m)
    plus=states[1]
    minus=states[0]+states[2]
    delta=plus-minus
    val,u=np.linalg.eigh(delta)
    guess_plus=(u*(val>0))@u.conj().T
    accuracy=(np.trace(guess_plus@plus)+np.trace((np.eye(m)-guess_plus)@minus)).real
    return accuracy,delta,guess_plus,plus,minus


def zero_reference_projector():
    return (I16+L)@Psing/2


def j_operator():
    return np.kron(np.kron(np.kron(Z,I),Z),I)


def resolve_j(v,sign):
    mask=np.array([[int((1-2*r)*(1-2*t)==sign) for t in range(2)] for r in range(2)])
    return v*mask.reshape((1,1,1,1,1,1,1,1,2,1,2,1))


class InternalReferenceSubjectReportTests(unittest.TestCase):
    def test_reference_is_the_existing_paired_marginal_before_any_readout(self):
        for m in (2,3,9):
            effects,unnormalized=ensemble(m)
            rho0=np.eye(m)/m
            np.testing.assert_allclose(sum(unnormalized),rho0,atol=1e-13)
            _,_,ka,kb=spin_instrument(m)
            phi=np.eye(m)/math.sqrt(m)
            after=np.zeros((m,m),complex)
            for a in ka:
                for b in kb:
                    branch=a@phi@b.T
                    after+=branch.T@branch.conj()
            np.testing.assert_allclose(after,rho0,atol=1e-13)
            for i,e in enumerate(effects):
                np.testing.assert_allclose(unnormalized[i],e.T/m,atol=1e-13)
                self.assertAlmostEqual(np.trace(unnormalized[i]).real,Q[i],places=12)
            ll=spin_matrices(m);s=(m-1)/2;eta=(s+1)/(3*s)
            for i,rho in enumerate(unnormalized):
                rho=rho/Q[i]
                moment=np.array([np.trace(rho@x.T).real for x in ll])
                np.testing.assert_allclose(moment,eta*N[i],atol=1e-12)
            if m==2:
                reference=2*rho0.T
                directions=[2*(r/Q[i]).T for i,r in enumerate(unnormalized)]
                np.testing.assert_allclose(reference,I,atol=1e-13)
                np.testing.assert_allclose(sum(w*k for w,k in zip(Q,directions)),reference,atol=1e-13)
                for k in directions:self.assertAlmostEqual(np.linalg.det(k).real,0,places=12)
            else:
                # The two-level moment proxy is mixed, not a physical null
                # conditional state: its directional radius is eta<1.
                self.assertLess(eta,1)
                self.assertGreater(1-eta**2,0)
        # The reference is 2 rho_B^T from the input state; it is NOT defined
        # as an average over the chosen three effects. No-signalling then
        # implies the ensemble sum. Both state and instrument are inputs.

    def test_given_state_and_directions_weights_are_unique_but_directions_are_not(self):
        # 1 and x,y coordinates suffice for these coplanar rays.
        M=np.vstack((np.ones(3),N[:,:2].T))
        self.assertGreater(abs(np.linalg.det(M)),.1)
        np.testing.assert_allclose(np.linalg.solve(M,[1,0,0]),Q,atol=1e-13)
        eq=np.array([[1,0,0],[-.5,math.sqrt(3)/2,0],[-.5,-math.sqrt(3)/2,0]])
        np.testing.assert_allclose(eq.mean(axis=0),0,atol=1e-14)
        self.assertFalse(np.allclose(Q,[1/3]*3))
        # Same input marginal also admits another complete rank-one POVM.
        alt=[(I+sum(n*s for n,s in zip(v,(X,Y,Z))))/3 for v in eq]
        np.testing.assert_allclose(sum(alt),I,atol=1e-14)
        np.testing.assert_allclose(sum(a.T/2 for a in alt),I/2,atol=1e-14)

    def test_confined_observer_cannot_perfectly_infer_the_other_setting_sign(self):
        self.assertEqual([Fraction(str(v)).limit_denominator(1000) for v in D],
                         [Fraction(-1,5),Fraction(1,2),Fraction(-7,19)])
        expected={2:Fraction(9,10),3:Fraction(4,5),9:Fraction(11,15)}
        for m in (2,3,9):
            accuracy,delta,effect,pos,neg=helstrom(m)
            self.assertAlmostEqual(accuracy,float(expected[m]),places=12)
            self.assertAlmostEqual(accuracy,(1+trace_norm(delta))/2,places=12)
            self.assertAlmostEqual(np.trace(pos).real,2/5,places=12)
            self.assertAlmostEqual(np.trace(neg).real,3/5,places=12)
            s=(m-1)/2
            l=sum(z*x.T for z,x in zip(N[1],spin_matrices(m)))
            np.testing.assert_allclose(delta,(-np.eye(m)/5+4*l/5)/m,atol=1e-13)
            np.testing.assert_allclose(effect@effect,effect,atol=1e-13)
            # Optimal unrestricted POVM on Bob's entire multiplicity system;
            # no independent local ancilla or subsequent local quantum channel
            # improves the single-copy bound. No Alice-setting message.

    def test_actual_record_table_does_not_sneak_in_alice_access(self):
        for m in (2,3,9):
            state=output(active_base() if m==2 else compressed_spin_base(m))
            eta=(m+1)/(3*(m-1))
            for labels in ((15,0,1),tuple(range(16))):
                tab=i_r_m_table(relative_read(state,4,labels=labels))
                p=len(labels)/16
                ir=tab.sum(axis=2)/p
                expected=np.array([[Q[i]*(1-(1-2*r)*eta*D[i])/2 for r in range(2)] for i in range(3)])
                np.testing.assert_allclose(ir,expected,atol=1e-12)
                np.testing.assert_allclose(ir.sum(axis=0),[.5,.5],atol=1e-12)
                np.testing.assert_allclose(ir.sum(axis=1),Q,atol=1e-12)
                # Conditional on either r, both signs of d remain possible.
                for r in (0,1):
                    self.assertGreater(ir[1,r],0)
                    self.assertGreater(ir[0,r]+ir[2,r],0)
                # Optimal classical guess using the actual r,t joint cells.
                actual=tab/p
                success=np.maximum(actual[1],actual[0]+actual[2]).sum()
                expected_accuracy={2:7/10,3:19/30,9:3/5}[m]
                self.assertAlmostEqual(success,expected_accuracy,places=12)
            # Old clock effects act on independent references in these
            # complement blocks. This does not cover the finite-reference code.

    def test_j_report_is_not_neutral_under_the_later_reference_constraints(self):
        p=zero_reference_projector();j=j_operator()
        np.testing.assert_allclose(p@p,p,atol=1e-14)
        self.assertAlmostEqual(np.trace(p).real,2,places=13)
        np.testing.assert_allclose(p@j@p,0,atol=1e-14)
        for c in (C1,C2):
            self.assertGreater(np.linalg.norm(j@c-c@j),1)
            # For every normalized state in the rank-two kernel, each sharp
            # j branch has unnormalized squared charge norm exactly one.
            np.testing.assert_allclose(p@j@c@c@j@p/4,p,atol=1e-14)
        np.testing.assert_allclose(j@C3-C3@j,0,atol=1e-14)
        states=[full_state(4),output(active_base()),output(compressed_spin_base(3)),
                output(compressed_spin_base(9))]
        for state in states:
            for old in relative_read(state,4,labels=(0,)):
                v=with_reference(old);norm=np.linalg.norm(v)**2
                for c in (C1,C2,C3):self.assertLess(np.linalg.norm(apply16(c,v)),1e-12)
                for sign in (1,-1):
                    part=resolve_j(v,sign)
                    self.assertAlmostEqual(np.linalg.norm(part)**2,norm/2,places=12)
                    for c in (C1,C2):
                        self.assertAlmostEqual(np.linalg.norm(apply16(c,part))**2,norm,places=12)
                    self.assertLess(np.linalg.norm(apply16(C3,part)),1e-12)
        # A separate charged apparatus or a different invariant relational
        # report may change the problem; neither is assumed here.

    def test_spinor_boosts_are_not_finite_dimensional_unitary_lab_gates(self):
        # Real Lorentz algebra represented by 2x2 matrices: rotations are
        # anti-Hermitian, boosts Hermitian. Multiplying boosts by i makes
        # them anti-Hermitian but reverses the boost-boost commutator.
        sig=(X,Y,Z);rot=[-1j*x/2 for x in sig];boost=[x/2 for x in sig]
        def comm(a,b):return a@b-b@a
        for i,j,k in ((0,1,2),(1,2,0),(2,0,1)):
            np.testing.assert_allclose(comm(rot[i],rot[j]),rot[k],atol=1e-14)
            np.testing.assert_allclose(comm(rot[i],boost[j]),boost[k],atol=1e-14)
            np.testing.assert_allclose(comm(boost[i],boost[j]),-rot[k],atol=1e-14)
            np.testing.assert_allclose(comm(1j*boost[i],1j*boost[j]),rot[k],atol=1e-14)
        # This matrix example illustrates but does not alone prove the
        # general no-finite-unitary-representation theorem in the report.

    def test_noncompact_reference_has_infinite_invariant_volume(self):
        # Unit future hyperboloid: dμ=sinh²χ dχ dΩ. Its ball volume
        # π sinh(2R)-2πR diverges; constants cannot be normalized.
        def volume(r):return math.pi*(math.sinh(2*r)-2*r)
        self.assertGreater(volume(4)/volume(3),7)
        for r in (1.,2.,4.):
            x=np.linspace(0,r,20001)
            numerical=4*math.pi*np.trapezoid(np.sinh(x)**2,x)
            self.assertAlmostEqual(numerical/volume(r),1,places=7)
        # Nonconstant, normalizable packet exp(-a coshχ) is allowed but
        # singles out a centre relative to its correlated preparation.
        x=np.linspace(0,15,40001);density=4*math.pi*np.sinh(x)**2*np.exp(-2*np.cosh(x))
        integral=np.trapezoid(density,x)
        self.assertTrue(np.isfinite(integral));self.assertGreater(integral,0)

if __name__=='__main__':unittest.main()
