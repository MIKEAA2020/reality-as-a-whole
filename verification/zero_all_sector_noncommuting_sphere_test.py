"""Charge-preserving qubit factors on the actual four-site complement.

The representation, energy, input state and selected pairings are the earlier
finite model's stipulated structures; a pointer is not an actual subject.
"""
import math
import unittest
import numpy as np
from verification.zero_three_balance_encoded_sphere_record_test import (
    X as GLOCAL, I4, I256, CODE, PCODE, local_charges, kron_all
)
from verification.zero_encoded_sphere_clock_work_bridge_test import HA,HB
from verification.zero_dual_pair_sphere_energy_instrument_test import (
    I, X,Y,Z, original_effects,bob_effects
)
from verification.zero_five_ray_record_current_unification_test import q,ns,axis
from verification.zero_energy_sphere_work_incidence_test import (
    full_state,embed_records_and_work,target_memory,relative_read,
    i_r_m_table,h_memory_table,project_h
)
from verification.zero_invariant_all_history_record_clock_test import (
    attach_memory,evolve,apply32,kron,H,W,PPLUS,PMINUS
)
from verification.zero_relational_orientation_reference_test import with_reference,C1,C2,C3
from verification.zero_all_sector_branchwise_balance_test import U8,Q8

PAULIS=(X,Y,Z)
J=np.array([[0.,-1.],[1.,0.]],complex)


def spinor_site():
    """Explicit onsite SO(4)=(SU(2)xSU(2))/Z2 representation."""
    x=GLOCAL
    r=[-1j*(x[1]@x[2]-x[2]@x[1]),
       -1j*(x[2]@x[0]-x[0]@x[2]),
       -1j*(x[0]@x[1]-x[1]@x[0])]
    a=[(r[i]+x[i])/2 for i in range(3)]
    b=[(r[i]-x[i])/2 for i in range(3)]
    values,u=np.linalg.eigh(2*a[2]+b[2]);top=u[:,-1]
    am=a[0]-1j*a[1];bm=b[0]-1j*b[1]
    trans=np.column_stack((top,bm@top,am@top,am@bm@top))
    return a,b,trans


def coupled_four():
    """Four spin-half irreps: matrices indexed by path then m=j,...,-j."""
    up=np.array([1,0],complex);down=np.array([0,1],complex)
    tp=np.kron(up,up);tm=np.kron(down,down)
    tz=(np.kron(up,down)+np.kron(down,up))/math.sqrt(2)
    sing=(np.kron(up,down)-np.kron(down,up))/math.sqrt(2)
    high={0:[np.kron(sing,sing),
             (np.kron(tp,tm)-np.kron(tz,tz)+np.kron(tm,tp))/math.sqrt(3)],
          1:[np.kron(sing,tp),np.kron(tp,sing),
             (np.kron(tp,tz)-np.kron(tz,tp))/math.sqrt(2)],
          2:[np.kron(tp,tp)]}
    lower=sum(kron_all([(X-1j*Y)/2 if k==i else I for k in range(4)])
              for i in range(4))
    out={}
    for j,paths in high.items():
        out[j]=[]
        for v in paths:
            states=[v]
            for n in range(2*j):
                m=j-n
                states.append(lower@states[-1]/math.sqrt((j+m)*(j-m+1)))
            out[j].append(np.column_stack(states))
    return out


def decomposition():
    a,b,site=spinor_site();sp=coupled_four();transform=kron_all([site]*4)
    def pair_vector(u,v):
        # u is four A-spins, v four B-spins. Physical sites interleave A/B.
        raw=np.outer(u,v).reshape((2,)*8).transpose(0,4,1,5,2,6,3,7).reshape(256)
        return transform@raw
    blocks={}
    for ja in range(3):
        for jb in range(3):
            paths=[]
            for pa in sp[ja]:
                for pb in sp[jb]:
                    cols=[pair_vector(pa[:,ma],pb[:,mb])
                          for ma in range(2*ja+1) for mb in range(2*jb+1)]
                    paths.append(np.column_stack(cols))
            blocks[(ja,jb)]=paths
    # Local singlet multiplicity is four; replace its basis by the original
    # two code vectors and an explicit orthogonal pair on the complement.
    k0=np.column_stack([p[:,0] for p in blocks[(0,0)]])
    residual=(k0@k0.conj().T-PCODE)
    vals,vec=np.linalg.eigh(residual)
    extra=vec[:,vals>.5]
    blocks[(0,0)]=[CODE[:,i:i+1] for i in range(2)]+[extra[:,i:i+1] for i in range(2)]
    left=[];right=[];odd=[];counts={}
    for key,paths in blocks.items():
        start=2 if key==(0,0) else 0
        p=paths[start:]
        counts[key]=len(p)
        for k in range(0,len(p)-1,2):
            left.append(p[k]);right.append(p[k+1])
        if len(p)%2:odd.append(p[-1])
    return a,b,site,blocks,np.column_stack(left),np.column_stack(right),np.column_stack(odd),counts


def active_base(L=4):
    """Compressed exact output for every paired complement multiplicity.

    Physical input is Phi in an Alice basis and its conjugate Bob basis. Bob
    uses J† B_j J so the joint table equals the singlet sphere experiment.
    Spectator irrep maximally-entangled states factor out and are traced.
    """
    phi=I/math.sqrt(2)
    ka=[f/math.sqrt(np.trace(f).real) for f in original_effects()]
    kb=[J.conj().T@f@J for f in bob_effects()]
    lab=np.stack([np.stack([a@phi@b.T for b in kb],axis=-1) for a in ka],axis=-2)
    clocks=np.einsum('ac,bd->acbd',np.eye(L)/math.sqrt(L),np.eye(L)/math.sqrt(L))
    return np.einsum('abij,rcsd->abrcsdij',lab,clocks)


def remainder_base(L=4):
    # Local state-independent neutral pointer rotations on the odd remainders.
    clocks=np.einsum('ac,bd->acbd',np.eye(L)/math.sqrt(L),np.eye(L)/math.sqrt(L))
    response=np.sqrt(np.array(q)[:,None]*np.ones((1,2))/2)
    return np.einsum('rcsd,ij->rcsdij',clocks,response)[None,None,...]


def spin_matrices(m):
    s=(m-1)/2
    z=np.diag([s-i for i in range(m)]).astype(complex)
    plus=np.zeros((m,m),complex)
    for k in range(1,m):
        value=s-k
        plus[k-1,k]=math.sqrt((s-value)*(s+value+1))
    return ((plus+plus.conj().T)/(2*s),
            (plus-plus.conj().T)/(2j*s),z/s)


def positive_root(x):
    val,u=np.linalg.eigh(x)
    if np.min(val)<-1e-12:raise ValueError('effect is not positive')
    return (u*np.sqrt(np.maximum(val,0)))@u.conj().T


def spin_instrument(m):
    """POVM q_i(I+n_i.L); Bob sees the opposite transpose observable."""
    ll=spin_matrices(m);eye=np.eye(m)
    effects=[qi*(eye+sum(nj*x for nj,x in zip(n,ll))) for qi,n in zip(q,ns)]
    b=sum(z*x for z,x in zip(axis,ll))
    bob=[(eye-b.T)/2,(eye+b.T)/2]
    return effects,bob,[positive_root(e) for e in effects],[positive_root(e) for e in bob]


def compressed_spin_base(m,L=4):
    effects,bob,ka,kb=spin_instrument(m)
    phi=np.eye(m)/math.sqrt(m)
    lab=np.stack([np.stack([a@phi@b.T for b in kb],axis=-1) for a in ka],axis=-2)
    # An exact environment isometry: preserve the entire Gram matrix of all
    # six joint pointer amplitudes, not just their classical probabilities.
    mat=lab.reshape(m*m,6);_,sing,vh=np.linalg.svd(mat,full_matrices=False)
    compressed=(sing[:,None]*vh).reshape(-1,1,3,2)
    clocks=np.einsum('ac,bd->acbd',np.eye(L)/math.sqrt(L),np.eye(L)/math.sqrt(L))
    return np.einsum('abij,rcsd->abrcsdij',compressed,clocks)


def output(base):
    return target_memory(embed_records_and_work(base),math.pi/2)


def normalized_clock_data(state,labels):
    return relative_read(state,4,labels=labels)


def aggregate_table(states,labels):
    weights=(2/256,190/256,64/256)
    return sum(w*i_r_m_table(normalized_clock_data(s,labels)) for w,s in zip(weights,states))


class AllSectorNoncommutingSphereTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a,cls.b,cls.site,cls.blocks,cls.u,cls.v,cls.odd,cls.counts=decomposition()
        cls.g=local_charges()
        cls.Q=cls.u@cls.u.conj().T+cls.v@cls.v.conj().T
        cls.D=I256-PCODE
        cls.rest=cls.odd@cls.odd.conj().T
        cls.labx=cls.u@cls.v.conj().T+cls.v@cls.u.conj().T
        cls.laby=-1j*cls.u@cls.v.conj().T+1j*cls.v@cls.u.conj().T
        cls.labz=cls.u@cls.u.conj().T-cls.v@cls.v.conj().T
        cls.states=[full_state(4),output(active_base()),output(remainder_base())]

    def test_onsite_generators_form_two_commuting_spin_halves(self):
        a,b,site=self.a,self.b,self.site
        np.testing.assert_allclose(site.conj().T@site,np.eye(4),atol=1e-13)
        for j in range(3):
            np.testing.assert_allclose(a[j],site@np.kron(PAULIS[j]/2,I)@site.conj().T,atol=1e-13)
            np.testing.assert_allclose(b[j],site@np.kron(I,PAULIS[j]/2)@site.conj().T,atol=1e-13)
            np.testing.assert_allclose(GLOCAL[j],a[j]-b[j],atol=1e-13)
            for k in range(3):
                np.testing.assert_allclose(a[j]@b[k]-b[k]@a[j],0,atol=1e-13)
        # The G_i and their commutators recover both SU(2) factors.

    def test_irreducible_dimensions_exhaust_and_code_is_only_one_block(self):
        self.assertEqual(self.counts,{(0,0):2,(0,1):6,(0,2):2,(1,0):6,(1,1):9,(1,2):3,(2,0):2,(2,1):3,(2,2):1})
        allcols=np.column_stack([v for paths in self.blocks.values() for v in paths])
        np.testing.assert_allclose(allcols.conj().T@allcols,np.eye(256),atol=1e-12)
        for g in self.g:np.testing.assert_allclose(g@CODE,0,atol=1e-13)
        totals=[]
        for site_ops in (self.a,self.b):
            generators=[sum(kron_all([x if k==i else I4 for k in range(4)])
                            for i in range(4)) for x in site_ops]
            totals.append(sum(x@x for x in generators))
        for (ja,jb),paths in self.blocks.items():
            for path in paths:
                np.testing.assert_allclose(totals[0]@path,ja*(ja+1)*path,atol=1e-12)
                np.testing.assert_allclose(totals[1]@path,jb*(jb+1)*path,atol=1e-12)
        np.testing.assert_allclose(self.Q+self.rest+PCODE,I256,atol=1e-12)
        self.assertEqual(self.u.shape,(256,95));self.assertEqual(self.odd.shape,(256,64))
        # In a direct sum of irreps, commuting M_2 requires pairs of equal
        # irreps; 2 floor(m/2) copies is maximal in each multiplicity block.

    def test_real_noncommuting_operators_conserve_all_lab_charges_and_energy(self):
        u,v,Q=self.u,self.v,self.Q
        np.testing.assert_allclose(u.conj().T@v,0,atol=1e-12)
        np.testing.assert_allclose(u.conj().T@u,np.eye(95),atol=1e-12)
        for op in (Q,self.rest,self.labx,self.laby,self.labz):
            for g in self.g:
                np.testing.assert_allclose(g@op-op@g,0,atol=1e-12)
            for h in (HA,HB):
                np.testing.assert_allclose(h@op-op@h,0,atol=1e-12)
        np.testing.assert_allclose(self.labx@self.laby-self.laby@self.labx,2j*self.labz,atol=1e-12)
        self.assertGreater(np.linalg.norm(self.labx@self.laby-self.laby@self.labx),20)
        for op in (self.labx,self.laby,self.labz):
            np.testing.assert_allclose(op@op,Q,atol=1e-12)
        # G and the chosen lab energies are real, so conjugate Bob logical
        # operators also commute with the respective physical generators.
        for op in (self.labx.conj(),self.laby.conj(),self.labz.conj()):
            for g in self.g:np.testing.assert_allclose(g@op-op@g,0,atol=1e-12)
            np.testing.assert_allclose(HB@op-op@HB,0,atol=1e-12)

    def test_same_initial_state_and_actual_pointer_kraus_operators(self):
        u,v=self.u,self.v;Q=self.Q
        # Original M=(CODE J CODE^T + D)^T/16: the new active and odd
        # sectors are exactly the same D/16, not newly prepared singlets.
        V=CODE@J@CODE.T+self.D;M=V.T/16
        active=Q.T/16;rest=self.rest.T/16;code=PCODE@M
        np.testing.assert_allclose(M,code+active+rest,atol=1e-13)
        self.assertAlmostEqual(np.linalg.norm(code)**2,2/256,places=13)
        self.assertAlmostEqual(np.linalg.norm(active)**2,190/256,places=13)
        self.assertAlmostEqual(np.linalg.norm(rest)**2,64/256,places=13)
        for g in self.g:
            np.testing.assert_allclose(g@active-active@g.T,0,atol=1e-12)
            np.testing.assert_allclose(g@rest-rest@g.T,0,atol=1e-12)
        np.testing.assert_allclose(HA@active+active@HB.T,0,atol=1e-12)
        np.testing.assert_allclose(HA@rest+rest@HB.T,0,atol=1e-12)
        def lift(mat):
            return (mat[0,0]*u@u.conj().T+mat[0,1]*u@v.conj().T+
                    mat[1,0]*v@u.conj().T+mat[1,1]*v@v.conj().T)
        effects=original_effects();K=[lift(f/math.sqrt(np.trace(f).real)) for f in effects]
        # Bob uses the conjugate physical basis; retain the intended
        # logical matrix entries rather than conjugating them as well.
        bs=[lift((J.conj().T@f@J).conj()).conj() for f in bob_effects()]
        np.testing.assert_allclose(sum(k.conj().T@k for k in K),Q,atol=1e-12)
        np.testing.assert_allclose(sum(k.conj().T@k for k in bs),Q.conj(),atol=1e-12)
        for k in K+bs:
            for g in self.g:np.testing.assert_allclose(g@k-k@g,0,atol=1e-12)
            for h in (HA,HB):np.testing.assert_allclose(h@k-k@h,0,atol=1e-12)
        actuals=np.stack([a@active@b.T for a in K for b in bs],axis=-1).reshape(-1,6)
        compressed=active_base().reshape(-1,6)
        np.testing.assert_allclose(actuals.conj().T@actuals,
                                   (190/256)*(compressed.conj().T@compressed),atol=2e-12)
        # Equality of the whole six-pointer Gram matrix, not just its
        # diagonal, validates the compressed post-instrument state up to an
        # environment isometry for the downstream circuit.
        # These Kraus isometries complete to charge/energy-preserving
        # unitaries by tensoring a neutral pointer on each multiplicity block.

    def test_full_history_clock_and_record_work_observables(self):
        all_labels=tuple(range(16));window=(15,0,1)
        d=np.array(ns)@np.array(axis);qv=np.array(q)
        ideal=np.array([[3/40,1/20],[1/10,3/10],[13/40,3/20]])
        np.testing.assert_allclose(np.sum(abs(active_base())**2,axis=(0,1,2,3,4,5)),ideal,atol=1e-13)
        for state in self.states:
            self.assertAlmostEqual(np.linalg.norm(state)**2,1,places=12)
            for labels in (all_labels,window):
                vs=normalized_clock_data(state,labels);p=len(labels)/16
                self.assertAlmostEqual(sum(np.linalg.norm(x)**2 for x in vs),p,places=12)
                t=i_r_m_table(vs)
                np.testing.assert_allclose(t.sum(axis=(1,2))/p,qv,atol=1e-12)
                np.testing.assert_allclose(t[:,:,0],t[:,:,1],atol=1e-13)
                np.testing.assert_allclose(h_memory_table(vs)/p,[[.5,0],[0,.5]],atol=1e-12)
                self.assertAlmostEqual(t[:,0,1].sum(),p/4,places=12)
        for labels in (all_labels,window):
            total=aggregate_table(self.states,labels);p=len(labels)/16
            np.testing.assert_allclose(total.sum(axis=(1,2))/p,qv,atol=1e-12)
            self.assertAlmostEqual(total[:,0,1].sum(),p/4,places=12)
            self.assertAlmostEqual(np.dot(d,total.sum(axis=(1,2))),0,places=12)
            if len(labels)==16:
                self.assertAlmostEqual(np.einsum('i,irt,r->',d,total,[1,-1])/p,-161/1280,places=12)
        self.assertAlmostEqual(np.einsum('i,ir,r->',d,ideal,[1,-1]),-161/950,places=12)

    def test_higher_spin_directional_instruments_cover_odd_multiplicities(self):
        # Use all copies in m=9,3,3 rather than leave one irrep in each
        # unused by the 190-dimensional exact-qubit construction.
        for key in ((1,1),(1,2),(2,1)):
            paths=self.blocks[key];m=len(paths);d=paths[0].shape[1]
            self.assertEqual(m,9 if key==(1,1) else 3)
            flat=np.column_stack(paths);projector=flat@flat.conj().T
            effects,bob,ka,kb=spin_instrument(m)
            def lift(x):return flat@np.kron(x,np.eye(d))@flat.conj().T
            physical=[lift(x) for x in ka]+[lift(x.conj()).conj() for x in kb]
            for x in physical:
                for g in self.g:np.testing.assert_allclose(g@x-x@g,0,atol=1e-12)
                for h in (HA,HB):np.testing.assert_allclose(h@x-x@h,0,atol=1e-12)
            np.testing.assert_allclose(sum(lift(x).conj().T@lift(x) for x in ka),projector,atol=1e-12)
            np.testing.assert_allclose(sum(effects),np.eye(m),atol=1e-13)
            for e in effects+bob:self.assertGreaterEqual(np.linalg.eigvalsh(e).min(),-1e-12)
            s=(m-1)/2;eta=(s+1)/(3*s)
            phi=np.eye(m)/math.sqrt(m)
            expected=np.array([[q[i]*(1-(1-2*j)*eta*np.dot(ns[i],axis))/2
                                for j in range(2)] for i in range(3)])
            actual=np.array([[np.linalg.norm(a@phi@b.T)**2 for b in kb] for a in ka])
            np.testing.assert_allclose(actual,expected,atol=1e-12)
            self.assertGreater(np.linalg.norm(effects[0]@effects[1]-effects[1]@effects[0]),.01)
            # Validate the exact compressed output's entire six-amplitude Gram
            # matrix against physical 256x256 post-instrument lab matrices.
            # Bob's block is the conjugate projector; its transpose on the
            # maximally entangled matrix leaves Alice's projector, not P^T.
            init=projector/16
            for g in self.g:
                np.testing.assert_allclose(g@init-init@g.T,0,atol=1e-12)
            np.testing.assert_allclose(HA@init+init@HB.T,0,atol=1e-12)
            actuals=np.stack([a@init@b.T for a in physical[:3] for b in physical[3:]],axis=-1).reshape(-1,6)
            comp=compressed_spin_base(m).reshape(-1,6)
            np.testing.assert_allclose(actuals.conj().T@actuals,
                                       (m*d/256)*(comp.conj().T@comp),atol=2e-12)
        # The remaining (2,2) irrep has multiplicity one, rank 25, so by
        # Schur's lemma all its local exact-charge-preserving observables are
        # scalar. This is a model-specific obstruction, not a cosmic theorem.

    def test_higher_spin_all_history_and_full_sector_coverage(self):
        # The even-multiplicity blocks alone support exact qubit statistics.
        evenkeys=[(0,0),(0,1),(0,2),(1,0),(2,0)]
        left=[];right=[]
        for key in evenkeys:
            paths=self.blocks[key][2:] if key==(0,0) else self.blocks[key]
            for j in range(0,len(paths),2):left.append(paths[j]);right.append(paths[j+1])
        u=np.column_stack(left);v=np.column_stack(right)
        self.assertEqual(u.shape,(256,29));self.assertEqual(v.shape,(256,29))
        even=u@u.conj().T+v@v.conj().T
        high=[]
        for key in ((1,1),(1,2),(2,1)):
            flat=np.column_stack(self.blocks[key]);high.append(flat@flat.conj().T)
        flat=np.column_stack(self.blocks[(2,2)])
        last=flat@flat.conj().T
        np.testing.assert_allclose(PCODE+even+sum(high)+last,I256,atol=1e-12)
        self.assertAlmostEqual(np.trace(last).real,25,places=10)
        for g in self.g:np.testing.assert_allclose(g@last-last@g,0,atol=1e-12)
        def lift(mat):
            return (mat[0,0]*u@u.conj().T+mat[0,1]*u@v.conj().T+
                    mat[1,0]*v@u.conj().T+mat[1,1]*v@v.conj().T)
        K=[lift(f/math.sqrt(np.trace(f).real)) for f in original_effects()]
        bs=[lift((J.conj().T@f@J).conj()).conj() for f in bob_effects()]
        for x in K+bs:
            for g in self.g:np.testing.assert_allclose(g@x-x@g,0,atol=1e-12)
            for h in (HA,HB):np.testing.assert_allclose(h@x-x@h,0,atol=1e-12)
        physical=np.stack([a@(even/16)@b.T for a in K for b in bs],axis=-1).reshape(-1,6)
        compressed=active_base().reshape(-1,6)
        np.testing.assert_allclose(physical.conj().T@physical,
                                   (58/256)*(compressed.conj().T@compressed),atol=2e-12)
        general=[self.states[0],output(active_base()),output(compressed_spin_base(9)),
                 output(compressed_spin_base(3)),output(remainder_base())]
        weights=(2/256,58/256,81/256,90/256,25/256)
        for state in general:
            for labels in (tuple(range(16)),(15,0,1)):
                vs=relative_read(state,4,labels=labels);p=len(labels)/16
                self.assertAlmostEqual(sum(np.linalg.norm(x)**2 for x in vs),p,places=12)
                np.testing.assert_allclose(h_memory_table(vs)/p,[[.5,0],[0,.5]],atol=1e-12)
        for labels in (tuple(range(16)),(15,0,1)):
            total=sum(w*i_r_m_table(relative_read(v,4,labels=labels)) for w,v in zip(weights,general))
            p=len(labels)/16
            np.testing.assert_allclose(total.sum(axis=(1,2))/p,q,atol=1e-12)
            np.testing.assert_allclose(total[:,:,0],total[:,:,1],atol=1e-13)
            self.assertAlmostEqual(total[:,0,1].sum(),p/4,places=12)
            # Locally signed record and work values differ in sign exactly on
            # target-minus cells, half the physical weight in this circuit.
            self.assertAlmostEqual(total[:,:,1].sum()/p,.5,places=12)
            if len(labels)==16:
                dr=np.einsum('i,irt,r->',np.array(ns)@np.array(axis),total,[1,-1])/p
                self.assertAlmostEqual(dr,-97727/972800,places=12)
        B=kron(kron(U8,X),I);charge=kron(Q8,I,I)
        d=np.array(ns)@np.array(axis)
        Dval=d.reshape((1,1,1,1,1,1,3,1,1,1,1,1,1))
        for state in general:
            for z in relative_read(state,4,labels=tuple(range(16))):
                v=attach_memory(with_reference(z))
                for theta in (0,math.pi/4,math.pi/2):
                    y=evolve(v,theta)
                    self.assertLess(np.linalg.norm(apply32(charge,Dval*y)),1e-12)
                    np.testing.assert_allclose(apply32(B,Dval*y),Dval*y,atol=1e-13)
                    for c in (C1,C2,C3):
                        self.assertLess(np.linalg.norm(apply32(kron(c,I),y)),1e-12)
                    p=np.sum(abs(y)**2,axis=(0,1,2,3,4,5,7,9,11,12))
                    np.testing.assert_allclose(p.sum(axis=(1,2))/p.sum(),q,atol=1e-12)
                    np.testing.assert_allclose(p[:,:,0],p[:,:,1],atol=1e-13)
                for proj in (PPLUS,PMINUS):
                    y=apply32(proj,v)
                    np.testing.assert_allclose(apply32(B,Dval*y),Dval*y,atol=1e-13)

    def test_survives_old_clock_sectors_and_new_reference_history(self):
        B=kron(kron(U8,X),I);charge=kron(Q8,I,I)
        d=np.array(ns)@np.array(axis)
        Dval=d.reshape((1,1,1,1,1,1,3,1,1,1,1,1,1))
        # All old clock outcomes, all three sectors and sampled new phases.
        for state in self.states:
            for z in normalized_clock_data(state,tuple(range(16))):
                v=attach_memory(with_reference(z))
                for theta in (0,math.pi/4,math.pi/2):
                    y=evolve(v,theta)
                    self.assertLess(np.linalg.norm(apply32(charge,Dval*y)),1e-12)
                    np.testing.assert_allclose(apply32(B,Dval*y),Dval*y,atol=1e-13)
                    for c in (C1,C2,C3):
                        self.assertLess(np.linalg.norm(apply32(kron(c,I),y)),1e-12)
                    p=np.sum(abs(y)**2,axis=(0,1,2,3,4,5,7,9,11,12))
                    np.testing.assert_allclose(p.sum(axis=(1,2))/p.sum(),q,atol=1e-12)
                    np.testing.assert_allclose(p[:,:,0],p[:,:,1],atol=1e-13)
                for p in (PPLUS,PMINUS):
                    y=apply32(p,v)
                    np.testing.assert_allclose(apply32(B,Dval*y),Dval*y,atol=1e-13)

if __name__=='__main__':unittest.main()
