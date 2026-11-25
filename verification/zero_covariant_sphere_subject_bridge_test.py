"""Covariant internal-reference sphere and actual complement record circuit.

The Lorentz transformations here are changes of mathematical representation,
not implemented spacetime boosts or evidence of an experienced subject.
"""
import math
import unittest
import numpy as np
from verification.zero_all_sector_noncommuting_sphere_test import (
    I,X,Y,Z,q,ns,axis,spin_matrices,positive_root,output,active_base,
    compressed_spin_base,relative_read,i_r_m_table,kron,U8,Q8,
    attach_memory,with_reference,evolve,apply32,decomposition,local_charges,
    HA,HB,I256
)
from verification.zero_energy_sphere_work_incidence_test import full_state

SIG=(X,Y,Z)
Q=np.array(q)
N0=np.eye(2,dtype=complex)
B0=sum(x*s for x,s in zip(axis,SIG))
K0=[I+sum(x*s for x,s in zip(n,SIG)) for n in ns]


def invroot(n):
    v,u=np.linalg.eigh(n)
    if min(v)<=0:raise ValueError('reference must be timelike positive definite')
    return (u*(v**-.5))@u.conj().T


def scal(n,x,y):
    inv=np.linalg.inv(n)
    return (np.trace(inv@x@inv@y)/2).real


def coeff(h):
    return np.array([(np.trace(h@s)/2).real for s in SIG])


def geom(a):
    n=a@a.conj().T
    k=[a@x@a.conj().T for x in K0]
    b=a@B0@a.conj().T
    w=invroot(n);u=w@a
    return n,k,b,u


def boosts():
    # Positive boost and a noncommuting rotation followed by a boost.
    t=.61;boost=np.diag([math.exp(t/2),math.exp(-t/2)])
    angle=.73;vec=np.array([1.,2.,3.])/math.sqrt(14)
    rot=math.cos(angle/2)*I-1j*math.sin(angle/2)*sum(x*s for x,s in zip(vec,SIG))
    return [np.eye(2),boost,boost@rot]


def spin_rotation(u,m):
    # Fundamental polar unitary u=exp(-i theta a.sigma/2), lifted to spin s.
    c=np.clip((np.trace(u)/2).real,-1.,1.)
    half=math.acos(c);sn=math.sin(half)
    if abs(sn)<1e-13:return np.eye(m,dtype=complex)
    aa=np.array([(1j*np.trace(s@u)/(2*sn)).real for s in SIG])
    spin=(m-1)/2
    generator=sum(x*y*spin for x,y in zip(aa,spin_matrices(m)))
    v,e=np.linalg.eigh(generator)
    return (e*np.exp(-2j*half*v))@e.conj().T


def stable_root(e):
    val,u=np.linalg.eigh(e)
    if val.min() < -1e-12:raise ValueError('not a positive effect')
    # Roundoff at an exactly zero eigenvalue otherwise causes O(sqrt(eps))
    # discontinuities between equivalent matrix square roots.
    val=np.where(val>1e-14,val,0.)
    return (u*np.sqrt(val))@u.conj().T


def spin_base(m,directions,compare):
    ll=spin_matrices(m);eye=np.eye(m)
    effects=[qi*(eye+sum(x*y for x,y in zip(n,ll))) for qi,n in zip(Q,directions)]
    bs=sum(x*y for x,y in zip(compare,ll))
    bob=[(eye-bs.T)/2,(eye+bs.T)/2]
    ka=[stable_root(e) for e in effects];kb=[stable_root(e) for e in bob]
    for root,e in zip(ka+kb,effects+bob):
        np.testing.assert_allclose(root@root,e,atol=1e-12)
    phi=eye/math.sqrt(m)
    lab=np.stack([np.stack([a@phi@b.T for b in kb],axis=-1) for a in ka],axis=-2)
    mat=lab.reshape(m*m,6);_,s,vh=np.linalg.svd(mat,full_matrices=False)
    comp=(s[:,None]*vh).reshape(-1,1,3,2)
    clock=np.einsum('ac,bd->acbd',np.eye(4)/2,np.eye(4)/2)
    return np.einsum('abij,rcsd->abrcsdij',comp,clock),mat


def later_table(v):
    return np.sum(abs(v)**2,axis=(0,1,2,3,4,5,7,9,11,12))


class CovariantSphereSubjectBridgeTests(unittest.TestCase):
    def test_zero_contrast_is_covariant_and_relative_to_nonzero_reference(self):
        np.testing.assert_allclose(sum(q*k for q,k in zip(Q,K0)),N0,atol=1e-14)
        self.assertEqual(np.linalg.matrix_rank(np.stack([k.reshape(-1) for k in K0],axis=1)),3)
        for a in boosts():
            self.assertAlmostEqual(np.linalg.det(a).real,1,places=13)
            n,k,b,u=geom(a)
            np.testing.assert_allclose(sum(q*x for q,x in zip(Q,k)),n,atol=1e-13)
            np.testing.assert_allclose(sum(q*(x-n) for q,x in zip(Q,k)),0,atol=1e-13)
            self.assertGreater(np.linalg.det(n).real,.999999999999)
            self.assertAlmostEqual(np.trace(np.linalg.inv(n)@b).real,0,places=12)
            self.assertAlmostEqual(scal(n,b,b),1,places=12)
            np.testing.assert_allclose(u.conj().T@u,I,atol=1e-13)
            for j,x in enumerate(k):
                self.assertAlmostEqual(np.linalg.det(x).real,0,places=12)
                self.assertGreater(np.trace(x).real,0)
                self.assertAlmostEqual(np.trace(np.linalg.inv(n)@x).real,2,places=12)
                self.assertAlmostEqual(scal(n,x-n,b),np.dot(ns[j],axis),places=12)
        # q is fixed by these rays and an independently specified N, but
        # q does not follow if N is merely defined as their weighted mean.

    def test_reference_closure_alone_does_not_select_a_sphere_measure(self):
        equilateral=np.array([[1,0,0],[-.5,math.sqrt(3)/2,0],[-.5,-math.sqrt(3)/2,0]])
        other=[I+sum(x*s for x,s in zip(n,SIG)) for n in equilateral]
        np.testing.assert_allclose(sum(other)/3,I,atol=1e-14)
        np.testing.assert_allclose(sum(q*k for q,k in zip(Q,K0)),I,atol=1e-14)
        self.assertEqual(np.linalg.matrix_rank(np.stack([k.reshape(-1) for k in other],axis=1)),3)
        np.testing.assert_allclose(equilateral@equilateral.T-np.eye(3),
                                   -.5*(np.ones((3,3))-np.eye(3)),atol=1e-14)
        self.assertFalse(np.allclose(np.sort((np.array(ns)@np.array(ns).T)[np.triu_indices(3,1)]),
                                     [-.5,-.5,-.5]))
        # These are mathematical models, not declared independently actual.

    def test_naive_lab_zero_is_frame_dependent(self):
        a=boosts()[1];n,k,_,_=geom(a)
        ray_directions=np.array([coeff(x)/((np.trace(x)/2).real) for x in k])
        mean=Q@ray_directions
        np.testing.assert_allclose(mean,[0,0,math.tanh(.61)],atol=1e-13)
        self.assertGreater(np.linalg.norm(mean),.5)
        # All three rays originally lie in the xy plane, so each acquires
        # the same trace scaling cosh(.61), and the normalized weights stay q.
        np.testing.assert_allclose([np.trace(x).real/2 for x in k],math.cosh(.61),atol=1e-13)
        np.testing.assert_allclose(n,np.diag([math.exp(.61),math.exp(-.61)]),atol=1e-13)
        # Whitening by the transformed N, rather than by a fixed external
        # I, recovers the relative directions and their balanced sum.
        w=invroot(n)
        np.testing.assert_allclose(sum(q*coeff(w@x@w-I) for q,x in zip(Q,k)),0,atol=1e-13)

    def test_geometry_and_qubit_effects_share_the_same_reference(self):
        for a in boosts():
            n,k,b,u=geom(a);w=invroot(n)
            effects=[qi*w@x@w for qi,x in zip(Q,k)]
            compare=w@b@w
            np.testing.assert_allclose(sum(effects),I,atol=1e-13)
            for effect,old in zip(effects,K0):
                np.testing.assert_allclose(effect/np.trace(effect).real,u@old@u.conj().T/2,atol=1e-13)
                self.assertAlmostEqual(np.linalg.det(effect).real,0,places=12)
            np.testing.assert_allclose(compare,u@B0@u.conj().T,atol=1e-13)
            for i,e in enumerate(effects):
                d=np.trace((e/Q[i]-I)@compare).real/2
                self.assertAlmostEqual(d,np.dot(ns[i],axis),places=12)

    def test_reexpressed_directions_preserve_the_real_complement_instruments(self):
        # m=2 is an actual 58- or 190-dimensional paired-qubit sector;
        # m=3 and 9 are the actual odd-multiplicity complement blocks.
        for m in (2,3,9):
            base0,amp0=spin_base(m,ns,axis)
            gram0=amp0.conj().T@amp0
            prior=compressed_spin_base(m).reshape(-1,6)
            # Earlier root routine retains tiny positive roundoff eigenvalues;
            # the difference is at most O(sqrt(machine epsilon)).
            np.testing.assert_allclose(gram0,prior.conj().T@prior,atol=1e-8)
            if m==2:
                actual=active_base().reshape(-1,6)
                np.testing.assert_allclose(gram0,actual.conj().T@actual,atol=1e-12)
            ll=spin_matrices(m)
            for a in boosts():
                n,k,b,u=geom(a);w=invroot(n)
                rays=[coeff(w@x@w-I) for x in k]
                comp=coeff(w@b@w)
                rot=spin_rotation(u,m)
                np.testing.assert_allclose(rot.conj().T@rot,np.eye(m),atol=1e-13)
                for old,new in zip(ns,rays):
                    np.testing.assert_allclose(rot@sum(x*y for x,y in zip(old,ll))@rot.conj().T,
                                               sum(x*y for x,y in zip(new,ll)),atol=2e-12)
                base,amp=spin_base(m,rays,comp)
                np.testing.assert_allclose(amp.conj().T@amp,gram0,atol=1e-12)
                s0=output(base0);s1=output(base)
                for labels in ((15,0,1),tuple(range(16))):
                    v0=relative_read(s0,4,labels=labels);v1=relative_read(s1,4,labels=labels)
                    np.testing.assert_allclose(i_r_m_table(v0),i_r_m_table(v1),atol=1e-12)
                # Joint record/target response continues through the later
                # reference/memory dynamics, not merely the initial POVM.
                for x,y in zip(relative_read(s0,4,labels=(0,)),relative_read(s1,4,labels=(0,))):
                    for t in (0,math.pi/4,math.pi/2):
                        p=later_table(evolve(attach_memory(with_reference(x)),t))
                        z=later_table(evolve(attach_memory(with_reference(y)),t))
                        np.testing.assert_allclose(p,z,atol=1e-12)
        # This is covariance of a representation and its block readouts,
        # not an active nonunitary relativistic transformation of the lab.

    def test_relative_rotations_are_charge_and_energy_preserving_on_physical_labs(self):
        _,_,_,blocks,left,right,_,_=decomposition()
        u=geom(boosts()[2])[3];charges=local_charges()
        for m,flat in ((2,np.column_stack((left,right))),
                       (9,np.column_stack(blocks[(1,1)])),
                       (3,np.column_stack(blocks[(1,2)])),
                       (3,np.column_stack(blocks[(2,1)]))):
            irrep=flat.shape[1]//m
            p=flat@flat.conj().T
            op=I256-p+flat@np.kron(spin_rotation(u,m),np.eye(irrep))@flat.conj().T
            np.testing.assert_allclose(op.conj().T@op,I256,atol=2e-12)
            for g in charges:np.testing.assert_allclose(g@op-op@g,0,atol=2e-12)
            for h in (HA,HB):np.testing.assert_allclose(h@op-op@h,0,atol=2e-12)
        # The compact rotation is realizable as an allowed lab unitary in
        # these blocks. The preceding nonunitary boost is still not a lab gate.

    def test_both_frame_scalar_mirror_odd_signs_remain_indeterminate(self):
        d=np.array(ns)@np.array(axis)
        self.assertTrue(np.all(d!=0))
        sign=np.sign(d)
        self.assertAlmostEqual(Q[sign<0].sum(),3/5,places=13)
        states=[full_state(4),output(active_base()),output(compressed_spin_base(3)),
                output(compressed_spin_base(9))]
        b=kron(kron(U8,X),I);charge=kron(Q8,I,I)
        for state in states:
            for old in relative_read(state,4,labels=(15,0,1)):
                ref=attach_memory(with_reference(old))
                for t in (0,math.pi/4,math.pi/2):
                    v=evolve(ref,t);p=later_table(v);mass=p.sum()
                    j=np.array([1.,-1.])[:,None]*np.array([1.,-1.])[None,:]
                    self.assertAlmostEqual(np.einsum('irt,rt->',p,j)/mass,0,places=12)
                    self.assertAlmostEqual(np.einsum('irt,i,rt->',p,sign,j)/mass,0,places=12)
                    self.assertAlmostEqual(p[sign<0].sum()/mass,3/5,places=12)
                    # j and sign(d)*j have opposite signs exactly on those
                    # cells; both are mirror odd, normalized, and scalar.
                    for f in (np.ones(3),sign):
                        fv=f.reshape((1,1,1,1,1,1,3,1,1,1,1,1,1))*v
                        np.testing.assert_allclose(apply32(b,fv),fv,atol=1e-13)
                        self.assertLess(np.linalg.norm(apply32(charge,fv)),1e-12)
        # These are candidate maps on labels, not proven experienced values.

if __name__=='__main__':unittest.main()
