"""Charge-preserving preparation of the internal reference before work mixing.

The seed pair, pulse and couplings are stipulated finite-model inputs. They
are not derived from zero, objective cosmic energy, actual subjects or time.
"""
import math
import unittest
import numpy as np
from verification.zero_energy_sphere_work_incidence_test import X,Y,Z,I,Jactive,full_state
from verification.zero_dual_pair_sphere_energy_instrument_test import dual_output, relative_effect_roots
from verification.zero_all_sector_sphere_clock_work_test import (
    complement_state,FWEIGHTS,FA,FB
)
from verification.zero_relational_orientation_reference_test import (
    Qori, L, S, C1, C2, C3, with_reference, apply16, original_table
)
from verification.zero_constitution_hamiltonian_phase_gate_test import J16, X16, P16
from verification.zero_reciprocal_subject_exchange_test import n

LENGTH=4
I4=np.eye(4,dtype=complex)
I16=np.eye(16,dtype=complex)
I32=np.eye(32,dtype=complex)


def wf_embed(op,d=2):
    """(W,F) matrix -> (W,T,F) matrix, with T untouched."""
    return np.einsum('afbg,cd->acfbdg',op.reshape(d,2,d,2),I).reshape(d*4,d*4)


# Active two-level apparatus, with axes (R,W,T,F).
p0=(I4-np.kron(Jactive,Z))/2
k=p0@np.kron(X,X)@p0
def pair_gate(beta):
    wf=I4+(math.cos(beta)-1)*p0+1j*math.sin(beta)*k
    return np.kron(I,wf_embed(wf))


Ewf=I4+(math.cos(math.pi/4)-1)*p0+1j*math.sin(math.pi/4)*k
E=pair_gate(math.pi/4)
pjplus=(I+Jactive)/2
pjminus=(I-Jactive)/2
D=np.kron(np.kron(np.kron(I,pjplus),I),I)+1j*np.kron(np.kron(np.kron(Z,pjminus),I),I)
h=(I4-np.kron(Z,Jactive))/2
T=np.kron(np.kron(I4-h,I),I)+np.kron(np.kron(h,-1j*Y),I)


def physical_operators():
    """128D extensions on actual R, 16-state W, T, F."""
    p=np.kron(P16,I)
    jwf=np.kron(J16,Z)
    pz=(p-jwf)/2
    exchange=pz@np.kron(X16,X)@pz
    ef=I32+(math.cos(math.pi/4)-1)*pz+1j*math.sin(math.pi/4)*exchange
    Ef=np.kron(I,wf_embed(ef,16))
    plus=(P16+J16)/2
    minus=(P16-J16)/2
    outside=I16-P16
    Df=(np.kron(np.kron(np.kron(I,outside+plus),I),I)
        +1j*np.kron(np.kron(np.kron(Z,minus),I),I))
    hrw=(np.kron(I,P16)-np.kron(Z,J16))/2
    Tf=np.eye(128,dtype=complex)+np.kron(np.kron(hrw,-1j*Y-I),I)
    Qf=np.kron(np.kron(np.kron(I,J16),I),I)+np.kron(np.kron(np.kron(I,I16),I),Z)
    return Ef,Df,Tf,Qf,exchange


def complement_base():
    base=np.zeros((2,2,4,4,4,4,3,2),complex)
    ref=np.eye(4)/2
    clocks=np.einsum('ac,bd->acbd',ref,ref)
    for s in (0,1):
        for i in range(3):
            for j in range(2):
                base[s,s,:,:,:,:,i,j]=math.sqrt(FWEIGHTS[s]*FA[s,i]*FB[s,j])*clocks
    return base


def balanced_seed(base):
    """Copy existing Bob pointer to R; W is j+, F is z−, target ready."""
    v=np.zeros(base.shape+(2,2,2,2),complex)
    jp=np.array([1,-1j],complex)/math.sqrt(2)
    for j in (0,1):
        v[...,j,j,:,0,1]=base[...,j,None]*jp
    return v


def prepare(seed):
    return apply16(T,apply16(D,apply16(E,seed)))


def clock_read(v,labels=tuple(range(16))):
    roots=relative_effect_roots(4,4,16)
    return [np.einsum('uvcd,abrcsdijxwmf->abrusvijxwmf',
                      roots[j].reshape(4,4,4,4),v,optimize=True) for j in labels]


class BalancedReferencePreparationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bases=(dual_output(4,4),complement_base())
        cls.old=(full_state(4),complement_state(4))

    def test_seed_is_product_in_new_work_reference_and_exactly_charge_zero(self):
        for base in self.bases:
            v=balanced_seed(base)
            self.assertAlmostEqual(np.linalg.norm(v),1,places=12)
            self.assertLess(np.linalg.norm(apply16(Qori,v)),1e-13)
            # Fixed j+ and F−, not an existing Bell-pair resource. It is a
            # specified internally oppositely charged seed, not derived.
            # Direct seed components check that W,F are fixed independently
            # of every lab, clock and record amplitude.
            pminus=(I-Jactive)/2
            self.assertLess(np.linalg.norm(np.einsum('wu,...rutf->...rwtf',pminus,v)),1e-13)
            self.assertLess(np.linalg.norm(v[...,0]),1e-13) # F z+ absent

    def test_each_preparation_gate_is_unitary_and_preserves_orientation_charge(self):
        for gate in (E,D,T):
            np.testing.assert_allclose(gate.conj().T@gate,np.eye(16),atol=1e-13)
            np.testing.assert_allclose(gate@Qori,Qori@gate,atol=1e-13)
        for base in self.bases:
            x=balanced_seed(base)
            for gate in (E,D,T):
                x=apply16(gate,x)
                self.assertAlmostEqual(np.linalg.norm(x),1,places=12)
                self.assertLess(np.linalg.norm(apply16(Qori,x)),1e-13)

    def test_declared_original_energy_is_zero_through_each_gate(self):
        eA=np.array([0.,1.]);eB=np.array([-1.,0.]);z=np.arange(4.)
        qenv=(z[:,None,None,None]-z[None,:,None,None]
              +z[None,None,:,None]-z[None,None,None,:])
        code=(eA[:,None,None,None,None,None]+eB[None,:,None,None,None,None]
              +qenv[None,None,:,:,:,:])
        other=np.broadcast_to(qenv,(2,2,4,4,4,4))
        for base,energy in zip(self.bases,(code,other)):
            state=balanced_seed(base)
            for gate in (None,E,D,T):
                if gate is not None:state=apply16(gate,state)
                self.assertLess(np.linalg.norm(state*energy[:,:,:,:,:,:,None,None,None,None,None,None]),1e-12)
        # Work has stipulated total energy 2 and the negative clock offset 2;
        # their constant contributions cancel in this compressed expression.
        # This is not a proof of global gravitational/cosmological energy.

    def test_physical_work_extensions_preserve_work_and_reference_charge(self):
        Ef,Df,Tf,Qf,exchange=physical_operators()
        eye=np.eye(128,dtype=complex)
        for gate in (Ef,Df,Tf):
            np.testing.assert_allclose(gate.conj().T@gate,eye,atol=1e-13)
            np.testing.assert_allclose(gate@Qf,Qf@gate,atol=1e-13)
        self.assertGreater(np.linalg.norm(exchange),1)
        numbers=np.asarray(n,complex)
        for inds in ((0,1,2,3),(0,1),(2,3),(0,2),(1,3)):
            charge=np.kron(np.kron(np.kron(I,sum(numbers[k] for k in inds)),I),I)
            for gate in (Ef,Df,Tf):
                np.testing.assert_allclose(gate@charge,charge@gate,atol=1e-13)
        # Gates are identity on the lab factors, so commute with their
        # original G_i and declared energies; R,T,F are assigned neutral.

    def test_constructed_output_is_the_previously_correlated_all_sector_state(self):
        for base,old in zip(self.bases,self.old):
            output=prepare(balanced_seed(base))
            np.testing.assert_allclose(output,with_reference(old),atol=2e-14)
            for C in (C1,C2,C3):self.assertLess(np.linalg.norm(apply16(C,output)),1e-13)
            np.testing.assert_allclose(apply16(L,output),output,atol=2e-14)
            np.testing.assert_allclose(apply16(S,output),output,atol=2e-14)
        # Because the map is common and linear, this holds for the coherent
        # code/complement whole, not only for their probabilistic mixture.

    def test_all_16_relative_clock_labels_are_retained_and_match(self):
        from verification.zero_energy_sphere_work_incidence_test import relative_read
        for base,old in zip(self.bases,self.old):
            output=prepare(balanced_seed(base))
            newlabels=clock_read(output)
            oldlabels=relative_read(old,4,labels=tuple(range(16)))
            self.assertAlmostEqual(sum(np.linalg.norm(x)**2 for x in newlabels),1,places=12)
            for v,w in zip(newlabels,oldlabels):
                np.testing.assert_allclose(v,with_reference(w),atol=2e-14)
                self.assertLess(np.linalg.norm(apply16(Qori,v)),1e-13)
            self.assertAlmostEqual(sum(np.linalg.norm(newlabels[k])**2 for k in (15,0,1)),3/16,places=12)

    def test_balanced_seed_evolves_into_correlated_pair_without_postselection(self):
        # The first pulse alone maps |j+,F−> to (|j+,F−>+|j−,F+>)/√2.
        jp=np.array([1,-1j],complex)/math.sqrt(2)
        jm=np.array([1,1j],complex)/math.sqrt(2)
        fm=np.array([0,1],complex);fp=np.array([1,0],complex)
        first=Ewf@np.kron(jp,fm)
        expected=(np.kron(jp,fm)+np.kron(jm,fp))/math.sqrt(2)
        np.testing.assert_allclose(first,expected,atol=1e-14)
        coeff=first.reshape(2,2)
        np.testing.assert_allclose(np.linalg.svd(coeff,compute_uv=False),[1/math.sqrt(2)]*2,atol=1e-14)
        for s in (first,expected):
            np.testing.assert_allclose((np.kron(Jactive,I)+np.kron(I,Z))@s,0,atol=1e-14)

    def test_pairing_angle_selected_by_the_relational_zero_condition(self):
        for base in self.bases:
            seed=balanced_seed(base)
            for beta in (0,math.pi/8,math.pi/4):
                out=apply16(T,apply16(D,apply16(pair_gate(beta),seed)))
                self.assertLess(np.linalg.norm(apply16(Qori,out)),1e-13)
                self.assertAlmostEqual(np.vdot(out,apply16(S,out)).real,
                                       math.sin(2*beta),places=12)
                self.assertAlmostEqual(np.linalg.norm(apply16(C1,out))**2,
                                       2*(1-math.sin(2*beta)),places=12)
        # If relational C1=0 is independently required and this pulse family
        # applies, its first solution in [0,pi/2] is beta=pi/4. Neither the
        # target condition, pulse family nor its physical schedule is derived.

    def test_prior_obstruction_still_applies_to_uncorrelated_mixed_work(self):
        # No contradiction: original pre-existing work marginal I/2 plus an
        # uncorrelated reference has <Q²>=2, while this NEW input has a
        # definite opposite work/reference pair and <Q²>=0 from the start.
        q=np.kron(Jactive,I)+np.kron(I,Z)
        blank=np.kron(I/2,np.array([[0,0],[0,1]],complex))
        self.assertAlmostEqual(np.trace(blank@q@q).real,2,places=13)
        jp=np.array([1,-1j],complex)/math.sqrt(2)
        seed=np.kron(jp,np.array([0,1],complex))
        self.assertAlmostEqual(np.vdot(seed,q@q@seed).real,0,places=13)

if __name__=='__main__':
    unittest.main()
