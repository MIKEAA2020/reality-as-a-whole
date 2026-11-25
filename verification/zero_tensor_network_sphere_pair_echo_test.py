"""Tensor factorization of the actual sphere-controlled Bell-source interface.

A tensor graph is a representation, not by itself an emergent geometry or a
subject. The 20-tick reduced-state calculation follows the existing exact
source/reference and apparatus labels, not an invented disconnected network.
"""
from itertools import product
from fractions import Fraction as F
import unittest
import numpy as np

from verification.zero_all_sector_noncommuting_sphere_test import I,X,Z,kron,active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_internal_reference_subject_valence_candidates_test import b_project
from verification.zero_persistent_sphere_subject_selection_test import norm2
from verification.zero_clock_finite_reservoir_reuse_test import BITS3,Q as THERMAL
from verification.zero_sphere_reuse_noisy_auxiliary_memory_test import words,distribution
from verification.zero_sphere_local_constitution_echo_test import twenty_tick_path
from verification.zero_joint_constitution_incidence_echo_test import coarse_table


def partial_trace(psi,keep,dims):
    a=np.moveaxis(psi.reshape(dims),keep,range(len(keep))).reshape(np.prod([dims[i] for i in keep]),-1)
    return a@a.conj().T


def entropy(rho):
    vals=np.linalg.eigvalsh(rho);vals=vals[vals>1e-12]
    return float(-np.sum(vals*np.log2(vals)))


def negativity(rho):
    # Partial transpose the reference qubit in S,F order.
    pt=rho.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)
    return float((sum(abs(np.linalg.eigvalsh(pt)))-1)/2)


def controlled_pair_mps():
    # Physical sites B, (S0,F0), (S1,F1), (S2,F2). The virtual index is b.
    lead=np.eye(2)/np.sqrt(2)
    middle=np.zeros((2,4,2));last=np.zeros((2,4))
    for b,s,f in product((0,1),repeat=3):
        if s==f^b:
            middle[b,2*s+f,b]=1/np.sqrt(2)
            last[b,2*s+f]=1/np.sqrt(2)
    a=np.einsum('ba,apc,cqd,dr->bpqr',lead,middle,middle,last)
    return a.reshape(128)


def actual_pair_reduced(t,qaux=F(0),zbit=None):
    # Exact partial trace for the first S,F pair in the actual 20-step
    # apparatus. x0 is the only label varied coherently: B, other reference
    # labels, old degrees, thermal purifiers, stores and echo are traced.
    # At any tick the latter records are orthogonal computational states.
    # By default use the actual correlated b,z,s Born law; fixed z with
    # balanced b is an additional counterfactual check, not that Born law.
    rho=np.zeros((4,4),dtype=complex);cols=((1,),(0,))
    sectors=([(int(b==-1),int(z==-1),p) for (b,z,s),p in coarse_table().items()]
             if zbit is None else [(0,zbit,F(1,2)),(1,zbit,F(1,2))])
    for (b,z0,p),x,f,e in product(sectors,BITS3,BITS3,words(1)):
        w=p*F(1,8)*distribution(THERMAL,f)*distribution(qaux,e)
        if not w:continue
        path=twenty_tick_path(b,x,f,e,cols,z0)
        state,z,r=path[t];xflip=(x[0]^1,x[1],x[2])
        alt,zz,rr=twenty_tick_path(b,xflip,f,e,cols,z0)[t]
        y=state[1];other=alt[1]
        index=2*y[0]+x[0];index2=2*other[0]+xflip[0]
        rho[index,index]+=float(w)
        if state[2:]==alt[2:] and y[1:]==other[1:] and (z,r)==(zz,rr):
            rho[index,index2]+=float(w)
    return rho


class TensorNetworkSphereTests(unittest.TestCase):
    def test_existing_b_sector_weights_all_original_histories(self):
        base=output(active_base())
        for label in range(16):
            v=initial(relative_read(base,4,labels=(label,))[0]);mass=norm2(v)
            for b in (-1,1):self.assertAlmostEqual(norm2(b_project(v,b))/mass,.5,places=12)
        # The conditional source reference states and physical controlled
        # interface are separately verified in the identity-pair tests.

    def test_exact_mps_contraction_and_bond_capacity(self):
        psi=controlled_pair_mps();self.assertAlmostEqual(np.vdot(psi,psi).real,1,places=13)
        for b,x in product((0,1),BITS3):
            # flatten B and 3 pair indices, with each pair S,F in that order
            pair=[2*(xi^b)+xi for xi in x];idx=((b*4+pair[0])*4+pair[1])*4+pair[2]
            self.assertAlmostEqual(psi[idx].real,.25,places=13)
        for cut in (1,2,3):
            dims=[2,4,4,4];matrix=psi.reshape(int(np.prod(dims[:cut])),int(np.prod(dims[cut:])))
            sv=np.linalg.svd(matrix,compute_uv=False);rank=sum(sv>1e-12)
            self.assertEqual(rank,2)
            self.assertAlmostEqual(-sum(v*v*np.log2(v*v) for v in sv if v>1e-12),1,places=13)
            # A single bond of dimension 2 upper-bounds the entropy by one
            # bit, and here its Schmidt spectrum saturates that bound.
        # Embed the same network into virtual bond dimension 4. The graph's
        # bond capacity rises, but no physical state or Schmidt value changes.
        lead=np.zeros((2,4));lead[:,:2]=np.eye(2)/np.sqrt(2)
        mid=np.zeros((4,4,4));last=np.zeros((4,4))
        for b,s,f in product((0,1),repeat=3):
            if s==f^b:
                mid[b,2*s+f,b]=1/np.sqrt(2);last[b,2*s+f]=1/np.sqrt(2)
        padded=np.einsum('ba,apc,cqd,dr->bpqr',lead,mid,mid,last).reshape(128)
        np.testing.assert_allclose(padded,psi,atol=1e-13)
        # Actual old state may have more degrees than the logical b factor:
        # its two normalized b-sector vectors are orthogonal and can replace
        # the two logical |b> vectors isometrically without changing cuts.

    def test_conditional_bell_vs_unconditional_classical_pair(self):
        psi=controlled_pair_mps();dims=(2,2,2,2,2,2,2)
        sf=partial_trace(psi,[1,2],dims);s=partial_trace(psi,[1],dims);f=partial_trace(psi,[2],dims)
        np.testing.assert_allclose(sf,(np.eye(4)+kron(X,X))/4,atol=1e-13)
        self.assertAlmostEqual(entropy(s),1,places=13);self.assertAlmostEqual(entropy(f),1,places=13)
        self.assertAlmostEqual(entropy(sf),1,places=13)
        self.assertAlmostEqual(entropy(s)+entropy(f)-entropy(sf),1,places=13)
        self.assertAlmostEqual(negativity(sf),0,places=13)
        self.assertAlmostEqual(np.trace(sf@kron(X,X)).real,1,places=13)
        plus=np.array([1,1],complex)/np.sqrt(2);minus=np.array([1,-1],complex)/np.sqrt(2)
        mix=(np.outer(np.kron(plus,plus),np.kron(plus,plus))+
             np.outer(np.kron(minus,minus),np.kron(minus,minus)))/2
        np.testing.assert_allclose(sf,mix,atol=1e-13) # explicit separable form
        for b in (0,1):
            bell=np.zeros(4,complex)
            for x in (0,1):bell[2*(x^b)+x]=1/np.sqrt(2)
            rho=np.outer(bell,bell.conj())
            self.assertAlmostEqual(negativity(rho),.5,places=13)
            self.assertAlmostEqual(entropy(partial_trace(bell,[0],(2,2))),1,places=13)
        # Every SF pair conditioned on actual B is a Bell pair; without B,
        # the same reduced S,F pair is separable though D=XsXf remains +1.
        # The full pure-pair-versus-rest cut has one ebit, distinct from S:F.
        self.assertAlmostEqual(entropy(sf),1,places=13)
        two=partial_trace(psi,[1,2,3,4],dims)
        self.assertAlmostEqual(entropy(two),1,places=13)
        self.assertAlmostEqual(2*entropy(sf)-entropy(two),1,places=13)

    def test_conditional_projective_sphere_requires_access_to_b(self):
        # The real F qubit has projective pure-state space CP1. For fixed B,
        # steering its Bell partner spans every ray, without claiming that
        # measurement settings are all actual subjects or spacetime points.
        mixed=(np.eye(4)+kron(X,X))/4
        for theta,phi in product((0.,.4,1.2,np.pi/2,np.pi),(0.,.7,1.9,3.)):
            u=np.array([np.cos(theta/2),np.exp(1j*phi)*np.sin(theta/2)])
            for b in (0,1):
                bell=np.zeros(4,complex)
                for x in (0,1):bell[2*(x^b)+x]=1/np.sqrt(2)
                part=kron(u.conj().reshape(1,2),I)@bell
                self.assertAlmostEqual(np.vdot(part,part).real,.5,places=13)
                goal=np.linalg.matrix_power(X,b)@u.conj()/np.sqrt(2)
                np.testing.assert_allclose(part,goal,atol=1e-13)
            # Ignoring B gives an entanglement-breaking S->F steering map:
            # only the X-axis interval of the Bloch sphere is accessible.
            conditional=np.einsum('i,iajb,j->ab',u.conj(),mixed.reshape(2,2,2,2),u)
            self.assertAlmostEqual(np.trace(conditional).real,.5,places=13)
            expected=(I+np.vdot(u,X@u).real*X)/2
            np.testing.assert_allclose(conditional/.5,expected,atol=1e-13)
        # The bijection uses a b-conditioned measurement interface and does
        # not identify the physical F sphere with an actual Lorentz cone.

    def test_actual_pair_state_through_twenty_tick_echo(self):
        bell=np.array([1,0,0,1],complex)/np.sqrt(2);rho_bell=np.outer(bell,bell.conj())
        mixed_pair=(np.eye(4)+kron(X,X))/4
        for q,zbit in product((F(0),THERMAL),(None,0,1)):
            for t in range(21):
                rho=actual_pair_reduced(t,q,zbit)
                target=(rho_bell if t in (0,20) else mixed_pair if t in (1,19) else np.eye(4)/4)
                np.testing.assert_allclose(rho,target,atol=1e-13,err_msg=f't={t},q={q},z={zbit}')
                self.assertAlmostEqual(negativity(rho),.5 if t in (0,20) else 0,places=13)
                self.assertAlmostEqual(np.trace(rho@kron(X,X)).real,
                                       1 if t in (0,1,19,20) else 0,places=13)
                self.assertAlmostEqual(entropy(rho),0 if t in (0,20) else 1 if t in (1,19) else 2,places=13)
        # Neither zero negativity nor zero bare witness implies that the
        # global pure history lost coherence; the dressed witness survives.

if __name__=='__main__':unittest.main()
