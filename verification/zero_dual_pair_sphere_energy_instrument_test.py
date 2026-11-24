"""Five-ray POVM via an exact energy-conserving relational reference.

Finite clock/reference dimensions, explicit charge-preserving POVM isometry,
and prescribed signed sector energies. No gravity or experience assertion.
"""
import math
import unittest
import numpy as np
from verification.zero_five_ray_record_current_unification_test import q,ns,axis

I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.diag([1.,-1.]).astype(complex)
P=np.diag([0.,1.]).astype(complex)
HB=-np.diag([1.,0.]).astype(complex)
SIGMA=(X,Y,Z)
SINGLET=np.array([[0.,1.],[-1.,0.]],complex)/math.sqrt(2)


def original_effects():
    return np.array([qi*(I+sum(nj*sj for nj,sj in zip(n,SIGMA))) for qi,n in zip(q,ns)])


def conserved_effects(L,F=None):
    if L<2:raise ValueError('reference dimension must be at least two')
    if F is None:F=original_effects()
    M=np.zeros((len(F),2*L,2*L),complex)
    for i in range(len(F)):
        M[i,0,0]=F[i,0,0]
        M[i,2*L-1,2*L-1]=F[i,1,1]
        for m in range(1,L):
            inds=[m,L+m-1]
            M[i][np.ix_(inds,inds)]=F[i]
    return M


def roots(L,F=None):
    # Preserve energy sectors exactly. Each supplied F_i is rank one with
    # nonzero eigenvalue trace(F_i); edge blocks need their own square roots.
    if F is None:F=original_effects()
    out=np.zeros((len(F),2*L,2*L),complex)
    for i in range(len(F)):
        out[i,0,0]=math.sqrt(F[i,0,0].real)
        out[i,-1,-1]=math.sqrt(F[i,1,1].real)
        for m in range(1,L):
            inds=[m,L+m-1]
            out[i][np.ix_(inds,inds)]=F[i]/math.sqrt(np.trace(F[i]).real)
    return out


def sector_unitaries(L,F=None):
    """Explicitly complete each readout isometry to an energy-block unitary."""
    K=roots(L,F);nout=len(K);blocks=[]
    for m in range(L+1):
        inds=[0] if m==0 else ([2*L-1] if m==L else [m,L+m-1])
        size=len(inds);dim=size*nout
        U=np.zeros((dim,dim),complex);cols=[]
        input_cols=[j*nout for j in range(size)]
        for j,col in enumerate(input_cols):
            v=np.zeros(dim,complex)
            for i in range(nout):v[i::nout]=K[i][inds,inds[j]]
            U[:,col]=v;cols.append(v)
        remaining=[j for j in range(dim) if j not in input_cols]
        for k in range(dim):
            v=np.eye(dim,dtype=complex)[:,k]
            for _ in range(2):
                for c in cols:v-=c*np.vdot(c,v)
            norm=np.linalg.norm(v)
            if norm>1e-10:
                v/=norm;U[:,remaining.pop(0)]=v;cols.append(v)
                if not remaining:break
        if remaining:raise RuntimeError('unitary completion failed')
        blocks.append((inds,U))
    return blocks


def effective(M,L,ref):
    # E_i[a,a'] = Σ_rs ref*_r M_i[a,r;a',s] ref_s.
    return np.einsum('r,iarbs,s->iab',ref.conj(),M.reshape(3,2,L,2,L),ref)


def refstate(L,t=0):return np.exp(1j*np.arange(L)*t)/math.sqrt(L)


def whole_initial(L):
    # axes A,B,R,C; A+B energy=0, R−C=0.
    return np.einsum('ab,rc->abrc',SINGLET,np.eye(L)/math.sqrt(L))


def whole_after(L,F=None):
    # Isometry Σ_i sqrt(M_i)⊗|i>_pointer on A,R; output A,B,R,C,i.
    K0=roots(L,F);K=K0.reshape(len(K0),2,L,2,L)
    return np.einsum('iuvax,abxc->ubvci',K,whole_initial(L))


def clock_conditional(v,t):
    L=v.shape[3];clock=np.exp(-1j*np.arange(L)*t)/math.sqrt(L)
    return math.sqrt(L)*np.einsum('c,abrcp->abrp',clock.conj(),v)


def table(conditioned):
    # Alice, Bob, reference, i. Project Bob along the specified axis.
    a=sum(ni*s for ni,s in zip(axis,SIGMA))
    out=np.zeros((3,2))
    for i in range(3):
        v=conditioned[:,:,:,i]
        rb=np.einsum('abr,acr->bc',v,v.conj())
        for j,sgn in enumerate((1,-1)):
            out[i,j]=np.trace(rb@(I+sgn*a)/2).real
    return out


def table_average_over_clock(v):
    # Trace the clock; all labels are actual quantum registers, not subjects.
    return sum(table(v[:,:,:,c,:]) for c in range(v.shape[3]))


def bob_effects():
    a=sum(ni*s for ni,s in zip(axis,SIGMA))
    return np.array([(I+a)/2,(I-a)/2])


def dual_output(LA,LB,FA=None):
    # Independent relational reference–clock pairs for the two laboratories.
    initial=np.einsum('ab,rc,sd->abrcsd',SINGLET,np.eye(LA)/math.sqrt(LA),np.eye(LB)/math.sqrt(LB))
    ka0=roots(LA,FA);ka=ka0.reshape(len(ka0),2,LA,2,LA)
    kb=roots(LB,bob_effects()).reshape(2,2,LB,2,LB)
    mid=np.einsum('iuvax,abxcsd->ubvcsdi',ka,initial)
    return np.einsum('jyzbw,ubvcwdi->uyvczdij',kb,mid)


def dual_conditional(out,tA,tB):
    LA=out.shape[3];LB=out.shape[5]
    ca=np.exp(-1j*np.arange(LA)*tA)/math.sqrt(LA)
    cb=np.exp(-1j*np.arange(LB)*tB)/math.sqrt(LB)
    return math.sqrt(LA*LB)*np.einsum('c,d,abrcsdij->abrsij',ca.conj(),cb.conj(),out)


def dual_table(v):
    return np.sum(abs(v)**2,axis=(0,1,2,3))


def relative_phase_density(LA,LB,delta):
    # Average the product of local phase POVMs over the common phase.
    # The resulting density commutes with N_CA+N_CB, integrates to I.
    d=LA*LB;M=np.zeros((d,d),complex)
    for n in range(LA):
        for u in range(LB):
            for m in range(LA):
                for v in range(LB):
                    if n+u==m+v:
                        M[n*LB+u,m*LB+v]=np.exp(1j*(u-v)*delta)/(2*math.pi)
    return M


def relative_table(out,delta):
    LA,LB=out.shape[3],out.shape[5]
    M=relative_phase_density(LA,LB,delta)
    # Conditional joint pointer distribution from the actual clock POVM.
    x=out.transpose(3,5,6,7,0,1,2,4).reshape(LA*LB,6,-1)
    p=np.empty(6)
    for j in range(6):
        r=x[:,j,:]@x[:,j,:].conj().T
        p[j]=(2*math.pi*np.trace(M@r)).real
    return p.reshape(3,2)


def relative_effect_roots(LA,LB,N):
    if N<max(LA,LB):raise ValueError('phase quadrature too short')
    result=[];tot=(np.arange(LA)[:,None]+np.arange(LB)[None,:]).ravel()
    for delta in 2*math.pi*np.arange(N)/N:
        E=(2*math.pi/N)*relative_phase_density(LA,LB,delta)
        root=np.zeros_like(E)
        # Preserve the exact total-clock-energy blocks despite degeneracies.
        for k in np.unique(tot):
            ix=np.where(tot==k)[0];vals,U=np.linalg.eigh(E[np.ix_(ix,ix)])
            if min(vals)<-1e-12:raise ValueError('relative phase effect is not positive')
            vals=np.where(vals>1e-14,vals,0)
            root[np.ix_(ix,ix)]=(U*np.sqrt(vals))@U.conj().T
        result.append(root)
    return np.array(result)


def direct_pair_state_output(L,t):
    # A second way to compute the clock conditional result.
    ref=refstate(L,t);v=np.einsum('ab,r->abr',SINGLET,ref)
    K=roots(L).reshape(3,2,L,2,L)
    return np.einsum('iuvax,abx->ubvi',K,v)


class DualPairSphereEnergyInstrumentTests(unittest.TestCase):
    def test_original_effects_and_identity_pair_steering(self):
        F=original_effects()
        np.testing.assert_allclose(F.sum(axis=0),I,atol=1e-14)
        np.testing.assert_allclose(sum(qi*np.asarray(n) for qi,n in zip(q,ns)),0,atol=1e-14)
        for i in range(3):
            self.assertGreaterEqual(np.linalg.eigvalsh(F[i]).min(),-1e-14)
            self.assertAlmostEqual(np.trace(F[i]).real/2,q[i],places=12)
            self.assertAlmostEqual(np.linalg.det(F[i]).real,0,places=12)
        # Singlet = a local-unitary version of the canonical identity pair.
        unit=np.array([[0,1],[-1,0]],complex)
        identity=np.eye(2)/math.sqrt(2)
        np.testing.assert_allclose(identity@unit,SINGLET,atol=1e-14)

    def test_joint_povm_is_positive_normalized_and_energy_conserving(self):
        for L in (2,4,8):
            Ms=conserved_effects(L)
            np.testing.assert_allclose(sum(Ms),np.eye(2*L),atol=1e-14)
            energies=(np.arange(L)[None,:]+np.arange(2)[:,None]).ravel()
            H=np.diag(energies)
            for m,k in zip(Ms,roots(L)):
                self.assertGreaterEqual(np.linalg.eigvalsh(m).min(),-1e-13)
                self.assertLess(np.linalg.norm(H@m-m@H),1e-13)
                self.assertLess(np.linalg.norm(H@k-k@H),1e-12)
                np.testing.assert_allclose(k@k,m,atol=1e-12)

    def test_explicit_energy_block_unitary_dilation(self):
        L=4;axisop=sum(x*s for x,s in zip(axis,SIGMA))
        pair=np.array([(I+axisop)/2,(I-axisop)/2])
        for F in (None,pair):
            K=roots(L,F);nout=len(K)
            for inds,U in sector_unitaries(L,F):
                np.testing.assert_allclose(U.conj().T@U,np.eye(len(U)),atol=1e-12)
                for j in range(len(inds)):
                    for i in range(nout):
                        np.testing.assert_allclose(U[i::nout,j*nout],K[i][inds,inds[j]],atol=1e-12)
            # No cross-energy matrix element exists by construction.

    def test_exact_effect_shrinkage_and_conservation_restriction(self):
        F=original_effects()
        for L in (2,4,8,16):
            M=conserved_effects(L);eta=1-1/L
            E=effective(M,L,refstate(L))
            target=F.copy();target[:,0,1]*=eta;target[:,1,0]*=eta
            np.testing.assert_allclose(E,target,atol=1e-13)
            self.assertAlmostEqual(np.linalg.norm(E[0]@P-P@E[0]),math.sqrt(2)*q[0]*eta,places=12)
            # An energy-diagonal reference has no noncommuting local effects.
            for n in range(L):
                r=np.eye(L,dtype=complex)[:,n]
                for x in effective(M,L,r):self.assertLess(np.linalg.norm(x@P-P@x),1e-13)

    def test_global_zero_before_and_after_readout_isometry(self):
        for L in (2,4,8):
            v=whole_initial(L);out=whole_after(L)
            eA=np.array([0.,1.]);eB=np.array([-1.,0.]);eR=np.arange(L);eC=-np.arange(L)
            energies=(eA[:,None,None,None]+eB[None,:,None,None]+
                      eR[None,None,:,None]+eC[None,None,None,:])
            self.assertAlmostEqual(np.linalg.norm(v),1,places=12)
            self.assertAlmostEqual(np.linalg.norm(out),1,places=12)
            self.assertLess(np.linalg.norm(energies*v),1e-13)
            self.assertLess(np.linalg.norm(energies[:,:,:,:,None]*out),1e-12)
            # Every output pointer effect commutes with its degenerate energy.
            self.assertLess(np.linalg.norm(sum(k.conj().T@k for k in roots(L))-np.eye(2*L)),1e-12)

    def test_clock_phase_povm_is_normalized_and_conditional_states_agree(self):
        L=4;v=whole_after(L);n=32
        ts=2*math.pi*np.arange(n)/n
        povm=sum((L/n)*np.outer(refstate(L,-t),refstate(L,-t).conj()) for t in ts)
        np.testing.assert_allclose(povm,np.eye(L),atol=1e-13)
        for t in (0.,.4,math.pi/2,math.pi):
            a=clock_conditional(v,t);b=direct_pair_state_output(L,t)
            np.testing.assert_allclose(a,b,atol=1e-13)
            self.assertAlmostEqual(np.linalg.norm(a),1,places=12)
            out=table(a)
            np.testing.assert_allclose(out.sum(axis=0),[.5,.5],atol=1e-13)
            np.testing.assert_allclose(out.sum(axis=1),q,atol=1e-13)

    def test_actual_asymmetric_table_and_sharp_limit(self):
        ideal=np.array([[3/40,1/20],[1/10,3/10],[13/40,3/20]])
        for L in (2,4,8,16):
            eta=1-1/L
            a=table(clock_conditional(whole_after(L),0))
            dot=np.array([sum(x*y for x,y in zip(n,axis)) for n in ns])
            expected=np.array([[qi*(1-eta*d)/2,qi*(1+eta*d)/2] for qi,d in zip(q,dot)])
            np.testing.assert_allclose(a,expected,atol=1e-12)
            self.assertAlmostEqual(np.sum(abs(a-ideal))/2,.2/L,places=12)
        expected4=np.array([[.071875,.053125],[.125,.275],[.303125,.171875]])
        np.testing.assert_allclose(table(clock_conditional(whole_after(4),0)),expected4,atol=1e-12)

    def test_unread_clock_erases_directional_correlations_not_weights(self):
        L=4;v=whole_after(L);unconditional=table_average_over_clock(v)
        expected=np.stack([np.array(q)/2,np.array(q)/2],axis=1)
        np.testing.assert_allclose(unconditional,expected,atol=1e-12)
        conditional=table(clock_conditional(v,0))
        self.assertGreater(np.sum(abs(conditional-unconditional))/2,.14)
        np.testing.assert_allclose(unconditional.sum(axis=1),q,atol=1e-13)
        np.testing.assert_allclose(unconditional.sum(axis=0),[.5,.5],atol=1e-13)

    def test_both_labs_have_exact_energy_conserving_readout(self):
        for LA,LB in ((2,2),(4,4),(4,3)):
            out=dual_output(LA,LB)
            self.assertAlmostEqual(np.linalg.norm(out),1,places=12)
            eA=np.array([0.,1.]);eB=np.array([-1.,0.])
            E=(eA[:,None,None,None,None,None]+eB[None,:,None,None,None,None]
               +np.arange(LA)[None,None,:,None,None,None]-np.arange(LA)[None,None,None,:,None,None]
               +np.arange(LB)[None,None,None,None,:,None]-np.arange(LB)[None,None,None,None,None,:])
            self.assertLess(np.linalg.norm(E[:,:,:,:,:,:,None,None]*out),1e-12)
            # The original A/B and reference/clock pairs need not each remain
            # at zero: their two mismatch operators cancel in every component.
            if LA==LB==4:
                pop=np.sum(abs(out)**2,axis=(2,3,4,5,6,7))
                self.assertAlmostEqual(pop[0,0],.211875,places=12)
                self.assertAlmostEqual(pop[1,1],.211875,places=12)
            np.testing.assert_allclose(sum(k.conj().T@k for k in roots(LB,bob_effects())),np.eye(2*LB),atol=1e-13)
            for tA,tB in ((0.,0.),(.4,0.),(.4,.4)):
                v=dual_conditional(out,tA,tB);self.assertAlmostEqual(np.linalg.norm(v),1,places=12)
                j=dual_table(v)
                np.testing.assert_allclose(j.sum(axis=1),q,atol=1e-12)
                np.testing.assert_allclose(j.sum(axis=0),[.5,.5],atol=1e-12)
                for i,n in enumerate(ns):
                    angle=tA-tB
                    dot=(n[0]*(axis[0]*math.cos(angle)+axis[1]*math.sin(angle))
                         +n[1]*(-axis[0]*math.sin(angle)+axis[1]*math.cos(angle)))
                    factor=(1-1/LA)*(1-1/LB)
                    self.assertAlmostEqual(j[i,0],q[i]*(1-factor*dot)/2,places=12)

    def test_two_energy_conserving_pointers_have_explicit_accuracy(self):
        ideal=np.array([[3/40,1/20],[1/10,3/10],[13/40,3/20]])
        for L in (2,4,8):
            table=dual_table(dual_conditional(dual_output(L,L),0,0))
            self.assertAlmostEqual(np.sum(abs(table-ideal))/2,.2*(1-(1-1/L)**2),places=12)
        expected=np.array([[.06953125,.05546875],[.14375,.25625],[.28671875,.18828125]])
        np.testing.assert_allclose(dual_table(dual_conditional(dual_output(4,4),0,0)),expected,atol=1e-12)

    def test_clock_alignment_is_relative_and_finite_resolution(self):
        L=4;out=dual_output(L,L)
        base=dual_table(dual_conditional(out,.23,-.17))
        shifted=dual_table(dual_conditional(out,.93,.53))
        np.testing.assert_allclose(base,shifted,atol=1e-12)
        # Ignore both clocks: the relative phase is averaged and the
        # directional correlations vanish, while each local marginal remains.
        unread=np.sum(abs(out)**2,axis=(0,1,2,3,4,5))
        np.testing.assert_allclose(unread,np.stack([np.array(q)/2,np.array(q)/2],axis=1),atol=1e-12)
        # Two symmetric bins of width π/3 about zero have sinc² visibility.
        width=math.pi/3;n=64
        ts=-width/2+(np.arange(n)+.5)*width/n
        average=sum(dual_table(dual_conditional(out,a,b)) for a in ts for b in ts)/(n*n)
        eta=(1-1/L)**2*(math.sin(width/2)/(width/2))**2
        ideal=np.array([[3/40,1/20],[1/10,3/10],[13/40,3/20]])
        self.assertAlmostEqual(np.sum(abs(average-ideal))/2,.2*(1-eta),places=5)

    def test_relative_clock_pointer_is_energy_conserving(self):
        LA=LB=4;N=16;out=dual_output(LA,LB)
        rootsR=relative_effect_roots(LA,LB,N)
        np.testing.assert_allclose(sum(k.conj().T@k for k in rootsR),np.eye(LA*LB),atol=1e-12)
        clock_energy=(np.arange(LA)[:,None]+np.arange(LB)[None,:]).ravel()
        H=np.diag(clock_energy)
        for j,k in enumerate(rootsR):
            delta=2*math.pi*j/N
            effect=2*math.pi/N*relative_phase_density(LA,LB,delta)
            np.testing.assert_allclose(k@k,effect,atol=1e-12)
            self.assertLess(np.linalg.norm(H@k-k@H),1e-12)
            np.testing.assert_allclose(relative_table(out,delta),dual_table(dual_conditional(out,delta,0)),atol=1e-12)
        # Apply an actual degenerate relative-clock pointer isometry to the
        # complete postmeasurement state; no additional clock is used.
        z=np.array([np.einsum('uvcd,abrcsdij->abrusvij',k.reshape(LA,LB,LA,LB),out) for k in rootsR])
        self.assertAlmostEqual(np.linalg.norm(z),1,places=12)
        eA=np.array([0.,1.]);eB=np.array([-1.,0.])
        E=(eA[:,None,None,None,None,None]+eB[None,:,None,None,None,None]
           +np.arange(LA)[None,None,:,None,None,None]-np.arange(LA)[None,None,None,:,None,None]
           +np.arange(LB)[None,None,None,None,:,None]-np.arange(LB)[None,None,None,None,None,:])
        self.assertLess(np.linalg.norm(z*E[None,:,:,:,:,:,:,None,None]),1e-12)
        # The finite pointer is uniform and each conditional i,j table equals
        # the corresponding relative phase table, without a sharp phase claim.
        for j in range(N):
            tab=np.sum(abs(z[j])**2,axis=(0,1,2,3,4,5))
            self.assertAlmostEqual(tab.sum(),1/N,places=12)
            np.testing.assert_allclose(tab*N,relative_table(out,2*math.pi*j/N),atol=1e-12)
        # Operational nonzero-probability phase window: three pointer labels.
        labels=(N-1,0,1)
        coarse=sum(np.sum(abs(z[j])**2,axis=(0,1,2,3,4,5)) for j in labels)
        self.assertAlmostEqual(coarse.sum(),3/N,places=12)
        coarse/=coarse.sum()
        ideal=np.array([[3/40,1/20],[1/10,3/10],[13/40,3/20]])
        visibility=(1+2*math.cos(2*math.pi/N))/3
        self.assertAlmostEqual(np.sum(abs(coarse-ideal))/2,.2*(1-(3/4)**2*visibility),places=12)

    def test_bob_and_clock_full_marginal_are_setting_independent(self):
        L=4;axisop=sum(x*s for x,s in zip(axis,SIGMA))
        pair=np.array([(I+axisop)/2,(I-axisop)/2])
        np.testing.assert_allclose(conserved_effects(L,pair).sum(axis=0),np.eye(2*L),atol=1e-13)
        densities=[]
        for F in (None,pair):
            out=whole_after(L,F)
            a=out.transpose(1,3,0,2,4).reshape(2*L,-1)
            densities.append(a@a.conj().T)
        for rho in densities:np.testing.assert_allclose(rho,np.eye(2*L)/(2*L),atol=1e-12)
        np.testing.assert_allclose(densities[0],densities[1],atol=1e-13)

    def test_full_bob_apparatus_and_both_clocks_cannot_signal_setting(self):
        L=4;axisop=sum(x*s for x,s in zip(axis,SIGMA))
        pair=np.array([(I+axisop)/2,(I-axisop)/2])
        densities=[]
        for FA in (None,pair):
            v=dual_output(L,L,FA)
            # Retain B, CA, RB, CB and Bob's pointer; discard A, RA and PA.
            x=v.transpose(1,3,4,5,7,0,2,6).reshape(2*L*L*L*2,-1)
            densities.append(x@x.conj().T)
        self.assertAlmostEqual(np.trace(densities[0]).real,1,places=12)
        np.testing.assert_allclose(densities[0],densities[1],atol=1e-12)

    def test_reference_edges_are_not_hidden_outcomes(self):
        # The joint POVM includes its two boundary energy sectors explicitly.
        for L in (2,4,8):
            ms=conserved_effects(L);F=original_effects()
            np.testing.assert_allclose(ms[:,0,0],F[:,0,0],atol=1e-14)
            np.testing.assert_allclose(ms[:,-1,-1],F[:,1,1],atol=1e-14)
            # Boundary contribution leads to the explicit 1/L degradation.
            self.assertGreater(np.linalg.norm(effective(ms,L,refstate(L))[0]-F[0]),0)

if __name__=='__main__':unittest.main()
