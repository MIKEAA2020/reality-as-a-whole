"""Energy-balanced sphere instrument with actual record–work relation K.

Finite-dimensional coherent circuit using the earlier energy-conserving
sphere and relative-clock instruments. Records are not assumed to be subjects.
"""
import math
import unittest
import numpy as np
from verification.zero_dual_pair_sphere_energy_instrument_test import (
    dual_output, relative_effect_roots, original_effects, bob_effects, axis, I, SIGMA
)
from verification.zero_reciprocal_subject_exchange_test import J,g,n,proj,swap,exchange
from verification.zero_autonomous_two_window_records_test import mutual_information

X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.diag([1.,-1.]).astype(complex)
# Encoded work |a>=|0110>, |b>=|1001>; both have two unit-energy excitations.
wa=np.array([1.,0.],complex);wb=np.array([0.,1.],complex)
Jactive=-Y
WORK=np.array([(wa-1j*wb)/math.sqrt(2),(wb-1j*wa)/math.sqrt(2)])


def embed_records_and_work(base,angle=math.pi/4):
    # base axes A,B,RA,CA,RB,CB,i,j. Copy Bob pointer j to R pair
    # r=0→01, r=1→10, then prepare and exchange work within its 2-energy sector.
    shape=base.shape+(2,2,2)  # r,work in {a,b},target memory
    v=np.zeros(shape,complex)
    phase=np.diag([np.exp(1j*angle),np.exp(-1j*angle)])
    for j in range(2):
        v[...,j,j,:,0]=base[...,j,None]*(phase@WORK[j])
    return v


def project_h(v,h):
    out=np.zeros_like(v)
    for r in (0,1):
        K=(1-2*r)*Jactive
        P=(np.eye(2)+(1-2*h)*K)/2
        out[...,r,:,:]=np.einsum('uv,...vm->...um',P,v[...,r,:,:])
    return out


def target_memory(v,tau):
    one=project_h(v,1);zero=project_h(v,0)
    U=math.cos(tau)*I-1j*math.sin(tau)*Y
    return zero+np.einsum('ab,...wb->...wa',U,one)


def full_state(L=4,tau=math.pi/2,FA=None):
    return target_memory(embed_records_and_work(dual_output(L,L,FA)),tau)


def relative_read(v,L,labels=(15,0,1),N=16):
    # Return unnormalized states for each observed relative-clock pointer label.
    ks=relative_effect_roots(L,L,N)
    return [np.einsum('uvcd,abrcsdijxwm->abrusvijxwm',ks[j].reshape(L,L,L,L),v)
            for j in labels]


def h_memory_table(vs):
    result=np.zeros((2,2))
    for v in vs:
        for h in (0,1):
            w=project_h(v,h)
            result[h]+=np.sum(abs(w)**2,axis=tuple(range(w.ndim-1)))
    return result


def i_r_m_table(vs):
    return sum(np.sum(abs(v)**2,axis=(0,1,2,3,4,5,7,9)) for v in vs)


def reduced_record(vs):
    out=np.zeros((2,2),complex)
    for v in vs:
        a=v.transpose(8,0,1,2,3,4,5,6,7,9,10).reshape(2,-1)
        out+=a@a.conj().T
    return out


def reduced_work(vs):
    out=np.zeros((2,2),complex)
    for v in vs:
        a=v.transpose(9,0,1,2,3,4,5,6,7,8,10).reshape(2,-1)
        out+=a@a.conj().T
    return out


def record_work(vs):
    out=np.zeros((4,4),complex)
    for v in vs:
        a=v.transpose(8,9,0,1,2,3,4,5,6,7,10).reshape(4,-1)
        out+=a@a.conj().T
    return out


def record_memory(vs):
    out=np.zeros((4,4),complex)
    for v in vs:
        a=v.transpose(8,10,0,1,2,3,4,5,6,7,9).reshape(4,-1)
        out+=a@a.conj().T
    return out


def lab_vector(v):
    # Environment A,RA,i is traced. Retain all of B,CA,RB,CB,j,R,W,M.
    return v.transpose(1,3,4,5,7,8,9,10,0,2,6).reshape(-1,v.shape[0]*v.shape[2]*v.shape[6])


def density_frobenius_sq(a,b):
    return max(0.,float((np.linalg.norm(a.conj().T@a,'fro')**2
                   +np.linalg.norm(b.conj().T@b,'fro')**2
                   -2*np.linalg.norm(a.conj().T@b,'fro')**2).real))


class EnergySphereWorkIncidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.L=4;cls.v=full_state(cls.L);cls.clock=relative_read(cls.v,cls.L)

    def test_actual_work_operator_and_non_degenerate_local_energies(self):
        g16=np.asarray(g);j1=np.asarray(J[0]);j2=np.asarray(J[2]);pp=np.asarray(proj)
        nums=np.array(n);total=np.sum(nums,axis=0)
        def comm(A,B):return A@B-B@A
        self.assertLess(np.linalg.norm(comm(g16,total)),1e-14)
        self.assertLess(np.linalg.norm(comm(j1,total)),1e-14)
        self.assertLess(np.linalg.norm(j1+j2),1e-14)
        self.assertLess(np.linalg.norm(j1@j1-pp),1e-14)
        np.testing.assert_allclose(g16[np.ix_([6,9],[6,9])],X,atol=1e-14)
        np.testing.assert_allclose(j1[np.ix_([6,9],[6,9])],Jactive,atol=1e-14)
        self.assertEqual(total[6,6],2);self.assertEqual(total[9,9],2)
        self.assertLess(np.linalg.norm(comm(np.asarray(swap),total)),1e-14)
        initial=np.eye(16,dtype=complex)[:,6];pulse=np.asarray(exchange(math.pi/4))
        for r in (0,1):
            prepared=(np.asarray(swap)@initial) if r else initial
            out=pulse@prepared
            expected=np.zeros(16,complex);expected[[6,9]]=WORK[r]
            np.testing.assert_allclose(out,expected,atol=1e-14)
        # Each physical local occupation has energies 0 and 1, while the
        # exchange preserves the energy of each memory/battery pair and
        # aggregate memory/battery sectors.
        for ix in ((0,1),(2,3),(0,2),(1,3)):
            self.assertLess(np.linalg.norm(comm(g16,nums[ix[0]]+nums[ix[1]])),1e-14)

    def test_code_and_target_unitary_commute_with_work_energy(self):
        # h=(P_act−Z_R J1)/2; compressed active h is a projector.
        for r in (0,1):
            h=(I-(1-2*r)*Jactive)/2
            np.testing.assert_allclose(h@h,h,atol=1e-14)
            np.testing.assert_allclose(h.conj().T,h,atol=1e-14)
            self.assertLess(np.linalg.norm(h@(2*I)-(2*I)@h),1e-14)
            np.testing.assert_allclose(Jactive@WORK[r],(1-2*r)*WORK[r],atol=1e-14)
        base=dual_output(4,4)
        zero=embed_records_and_work(base,angle=0)
        self.assertLess(np.linalg.norm(project_h(zero,1)),1e-13)
        phased=embed_records_and_work(base)
        self.assertAlmostEqual(np.linalg.norm(project_h(phased,0))**2,.5,places=12)
        self.assertAlmostEqual(np.linalg.norm(project_h(phased,1))**2,.5,places=12)
        for t in (0,math.pi/4,math.pi/2):
            v=target_memory(phased,t)
            self.assertAlmostEqual(np.linalg.norm(v),1,places=12)
            for h in (0,1):self.assertAlmostEqual(np.linalg.norm(project_h(v,h))**2,.5,places=12)

    def test_target_gate_has_its_own_physical_current(self):
        # On the active work code: n_M1=(I-Z)/2, J=-Y. The h-controlled
        # memory generator has a separate work-current contribution.
        nM=np.diag([0.,1.]);K=np.kron(Z,Jactive)
        h=(np.eye(4)-K)/2
        Hgate=np.kron(h,Y)
        N=np.kron(np.eye(2),np.kron(nM,I))
        current=1j*(Hgate@N-N@Hgate)
        np.testing.assert_allclose(current,.5*np.kron(np.kron(Z,X),Y),atol=1e-14)
        self.assertGreater(np.linalg.norm(current),1)
        # Jactive was defined from the standalone exchange generator;
        # it is not the full current of this target operation.

    def test_exact_total_energy_before_and_after_relative_pointer(self):
        L=self.L;eA=np.array([0.,1.]);eB=np.array([-1.,0.])
        # Physical CA_B energies are n+2, compensating initial work energy 2.
        e=(eA[:,None,None,None,None,None]+eB[None,:,None,None,None,None]
           +np.arange(L)[None,None,:,None,None,None]-np.arange(L)[None,None,None,:,None,None]
           +np.arange(L)[None,None,None,None,:,None]-(np.arange(L)+2)[None,None,None,None,None,:]+2)
        seed=embed_records_and_work(dual_output(L,L),angle=0)
        phased=embed_records_and_work(dual_output(L,L),angle=math.pi/4)
        for v in [seed,phased,target_memory(phased,math.pi/4),self.v]+self.clock:
            self.assertLess(np.linalg.norm(v*e[:,:,:,:,:,:,None,None,None,None,None]),1e-12)
        self.assertAlmostEqual(np.linalg.norm(self.v),1,places=12)
        self.assertAlmostEqual(sum(np.vdot(x,x).real for x in self.clock),3/16,places=12)

    def test_target_memory_perfectly_records_h_and_rival_event(self):
        hm=h_memory_table(self.clock)/(3/16)
        np.testing.assert_allclose(hm,[[.5,0],[0,.5]],atol=1e-12)
        self.assertAlmostEqual(mutual_information(hm),1,places=12)
        irm=i_r_m_table(self.clock)/(3/16)
        target=np.array([[.06917444,.05582556],[.14660452,.25339548],[.28422105,.19077895]])
        np.testing.assert_allclose(irm.sum(axis=2),target,atol=6e-9)
        np.testing.assert_allclose(irm[:,:,0],irm[:,:,1],atol=1e-12)
        self.assertAlmostEqual(irm[:,0,1].sum(),.25,places=12)
        # On the event r=+, m=1, h=1, so J1=-1. Formal R and J
        # experiential candidates have opposite signs; no subjects assumed.
        self.assertAlmostEqual(sum(np.vdot(x,x).real for x in self.clock)*irm[:,0,1].sum(),3/64,places=12)

    def test_confined_record_density_is_independent_of_h_and_target(self):
        norm=3/16
        full=reduced_record(self.clock)/norm
        np.testing.assert_allclose(full,np.eye(2)/2,atol=1e-12)
        for h in (0,1):
            branch=[project_h(v,h) for v in self.clock]
            rho=reduced_record(branch);p=np.trace(rho).real
            self.assertAlmostEqual(p,norm/2,places=12)
            np.testing.assert_allclose(rho/p,np.eye(2)/2,atol=1e-12)
        # Stronger: entire encoded record pair and external memory factor.
        rm=record_memory(self.clock)/norm
        np.testing.assert_allclose(rm,np.eye(4)/4,atol=1e-12)

    def test_relation_is_in_joint_record_work_not_either_marginal(self):
        nrm=3/16;K=np.kron(Z,Jactive);branches=[]
        for h in (0,1):
            bv=[project_h(v,h) for v in self.clock]
            p=nrm/2
            np.testing.assert_allclose(reduced_record(bv)/p,I/2,atol=1e-12)
            np.testing.assert_allclose(reduced_work(bv)/p,I/2,atol=1e-12)
            rho=record_work(bv)/p
            np.testing.assert_allclose(rho,(np.eye(4)+(1-2*h)*K)/4,atol=1e-12)
            branches.append(rho)
        dist=np.sum(abs(np.linalg.eigvalsh(branches[0]-branches[1])))/2
        self.assertAlmostEqual(dist,1,places=12)

    def test_conditioning_on_alice_outcome_changes_work_only_distinguishability(self):
        # An extra Alice-outcome register is a richer interface, not available
        # to W when i is traced. For i=0, the conditional record bias makes
        # the two work-only h states distinguishable.
        states=[]
        for h in (0,1):
            branch=[]
            for v in self.clock:
                a=project_h(v,h);filtered=np.zeros_like(a)
                filtered[:,:,:,:,:,:,0]=a[:,:,:,:,:,:,0]
                branch.append(filtered)
            rho=reduced_work(branch);states.append(rho/np.trace(rho).real)
        d=np.sum(abs(np.linalg.eigvalsh(states[0]-states[1])))/2
        self.assertAlmostEqual(d,.1067909649383468,places=12)
        # This postselection does not give a work observer Alice's result.

    def test_partial_target_angle_is_predictive_without_outcome_assumption(self):
        v=full_state(4,tau=math.pi/4);vs=relative_read(v,4)
        hm=h_memory_table(vs)/(3/16)
        np.testing.assert_allclose(hm,[[.5,0],[.25,.25]],atol=1e-12)
        self.assertAlmostEqual(mutual_information(hm),.3112781244591328,places=12)

    def test_full_bob_lab_and_both_clocks_no_setting_signal(self):
        a=sum(x*s for x,s in zip(axis,SIGMA))
        pair=np.array([(I+a)/2,(I-a)/2])
        x=lab_vector(self.v);y=lab_vector(full_state(4,FA=pair))
        self.assertAlmostEqual(np.linalg.norm(x),1,places=12)
        self.assertAlmostEqual(np.linalg.norm(y),1,places=12)
        self.assertLess(density_frobenius_sq(x,y),1e-12)
        # Apply and condition on the same actual three-label joint-clock
        # window, retaining the full lab and both clocks, then sum labels.
        other=relative_read(full_state(4,FA=pair),4)
        xc=np.concatenate([lab_vector(v) for v in self.clock],axis=1)
        yc=np.concatenate([lab_vector(v) for v in other],axis=1)
        self.assertAlmostEqual(np.linalg.norm(xc)**2,3/16,places=12)
        self.assertAlmostEqual(np.linalg.norm(yc)**2,3/16,places=12)
        self.assertLess(density_frobenius_sq(xc,yc),1e-12)

    def test_finite_reference_refinement_and_window_probability(self):
        for L in (2,4,8):
            vs=relative_read(full_state(L),L)
            irm=i_r_m_table(vs)/(3/16)
            np.testing.assert_allclose(irm.sum(axis=(0,1)),[.5,.5],atol=1e-12)
            self.assertAlmostEqual(sum(np.vdot(x,x).real for x in vs),3/16,places=12)
            visibility=(1+2*math.cos(math.pi/8))/3
            ideal=np.array([[3/40,1/20],[1/10,3/10],[13/40,3/20]])
            self.assertAlmostEqual(np.sum(abs(irm.sum(axis=2)-ideal))/2,
                                   .2*(1-(1-1/L)**2*visibility),places=12)

if __name__=='__main__':unittest.main()
