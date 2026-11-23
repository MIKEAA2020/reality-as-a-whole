"""Sharp reciprocal currents and exact response conditions in the sphere model.

The operator results do not establish actual subjects or phenomenal identities.
"""
import cmath
import math
import unittest
from verification.zero_spin_constitution_test import add,close,eye,kron,mm,mv,scale,inner
from verification.finite_tetrahedral_zero_reference_test import maxabs,comm
from verification.zero_relational_stabilizer_constitution_test import apply_base,tetra_control,pointwise_close
from verification.zero_reciprocal_subject_exchange_test import (
    J,proj,id16,n,state,apply_work,cond,bit,mat_sum,sub,g,
    prep,exchange,embed
)
from verification.finite_tetrahedral_zero_reference_test import recorded_whole
from verification.zero_invariant_sphere_instrument_test import adj


def current_response(qp,qm,q0=0):
    # Functional calculus for the spectrum +1,−1,0 of J[0].
    return mat_sum(scale(q0,sub(id16,proj)),scale((qp+qm)/2,proj),scale((qp-qm)/2,J[0]))


def sign_conjugate_response(qp,qm,q0=0): return current_response(qm,qp,q0)


def reduced_work(v,sites,ra=None):
    # Conditional on record RA if requested, trace reference, AB, records,
    # and all work factors not named in sites.
    d=2**len(sites); out=[[0j]*d for _ in range(d)]; total=0
    other=[j for j in range(4) if j not in sites]
    for base in range(64):
        if ra is not None and ((base>>1)&1)!=ra: continue
        for x in range(16):
            ax=v[16*base+x]; total+=abs(ax)**2
            ix=sum(bit(x,k)<<(len(sites)-1-j) for j,k in enumerate(sites))
            for y in range(16):
                if any(bit(x,k)!=bit(y,k) for k in other): continue
                iy=sum(bit(y,k)<<(len(sites)-1-j) for j,k in enumerate(sites))
                out[ix][iy]+=ax*v[16*base+y].conjugate()
    return scale(1/total,out)


def phase_flip(v):
    # Local Z on memory M1, with G kept fixed.
    return [x*(1-2*bit(i%16,0)) for i,x in enumerate(v)]


def history_v(k,v,inverse=False,mid_angle=math.pi/4):
    if k in (0,4): return list(v)
    if k==1: return prep(v)
    u=exchange(mid_angle if k==2 else math.pi/2)
    if inverse: return prep(apply_work(adj(u),v))
    return apply_work(u,prep(v))


def clock_amplitude(k,t):
    return math.sqrt(math.comb(4,k))*(-1j)**k * math.sin(t)**k * math.cos(t)**(4-k)


def clock_derivative(k,t):
    s,c=math.sin(t),math.cos(t)
    first=k*s**(k-1)*c**(5-k) if k else 0
    second=(4-k)*s**(k+1)*c**(3-k) if k<4 else 0
    return math.sqrt(math.comb(4,k))*(-1j)**k*(first-second)


def history_state(t):
    phi=embed(recorded_whole(),6)
    return [[clock_amplitude(k,t)*x for x in history_v(k,phi)] for k in range(5)]


def history_h(blocks,mid_angle=math.pi/4):
    # K A K†, A a weighted five-site path, edge c_k=√((k+1)(4-k)).
    unwound=[history_v(k,blocks[k],True,mid_angle) for k in range(5)]
    out=[]
    for k in range(5):
        col=[0j]*1024
        if k>0:
            fac=math.sqrt(k*(5-k))
            col=[x+fac*y for x,y in zip(col,unwound[k-1])]
        if k<4:
            fac=math.sqrt((k+1)*(4-k))
            col=[x+fac*y for x,y in zip(col,unwound[k+1])]
        out.append(history_v(k,col,mid_angle=mid_angle))
    return out


def clock_expm(lam,t):
    # Entire 5×5 exponential applied to |0>, convergent Taylor series.
    h=[[0j]*5 for _ in range(5)]
    for k in range(4): h[k][k+1]=h[k+1][k]=math.sqrt((k+1)*(4-k))
    h[2][2]=lam
    term=[1+0j]+[0j]*4; out=term[:]
    for step in range(1,100):
        term=[(-1j*t/step)*sum(h[i][j]*term[j] for j in range(5)) for i in range(5)]
        out=[x+y for x,y in zip(out,term)]
        if max(map(abs,term))<1e-17: break
    return out


def coupled_clock_state(t,angle):
    # K exp[-it(A⊗I+|2><2|⊗G)] (|0>⊗|Ω,a>).
    phi=embed(recorded_whole(),6)
    gphi=apply_work(g,phi)
    pp=[(x+y)/2 for x,y in zip(phi,gphi)]
    pm=[(x-y)/2 for x,y in zip(phi,gphi)]
    cplus=clock_expm(1,t); cminus=clock_expm(-1,t)
    return [history_v(k,[cplus[k]*x+cminus[k]*y for x,y in zip(pp,pm)],mid_angle=angle)
            for k in range(5)]


def coupled_clock_h(blocks,angle):
    out=history_h(blocks,angle)
    out[2]=[x+y for x,y in zip(out[2],apply_work(g,blocks[2]))]
    return out


def scale_blocks(c,blocks): return [[c*x for x in b] for b in blocks]


class SharpOppositionAndResponseTests(unittest.TestCase):
    def test_autonomous_clock_with_real_exchange_current_at_sharp_probe_stage(self):
        # For z=<2|exp[-i(A+P2)π/4]|0>, choose α=π/4+arg(-z).
        # The parity identity gives c_−=c_+* for the even sites 0 and 2.
        t=math.pi/4; z=clock_expm(1,t)[2]; zm=clock_expm(-1,t)[2]
        self.assertAlmostEqual(abs(z-zm.conjugate()),0)
        self.assertGreater(abs(z),.5)
        angle=math.pi/4+cmath.phase(-z)
        blocks=coupled_clock_state(t,angle)
        self.assertAlmostEqual(inner(blocks[2],blocks[2]).real,abs(z)**2)
        pointwise_close(self,blocks[2],[-abs(z)*x for x in state(math.pi/4)])
        self.assertAlmostEqual(abs(z)**2,.3597392417856652)
        self.assertAlmostEqual(sum(inner(x,x).real for x in blocks),1)
        for label in range(4):
            for record in (1,2):
                p=sum(abs(amp)**2 for i,amp in enumerate(blocks[2])
                      if (i//16)//16==label and (i//16)%4==record)
                self.assertAlmostEqual(p,abs(z)**2/8)
        # Independent numerical Schrödinger derivative of the full blocks.
        for t0 in (.27,t,1.0):
            h=1e-5
            before=coupled_clock_state(t0-h,angle); after=coupled_clock_state(t0+h,angle)
            rhs=coupled_clock_h(coupled_clock_state(t0,angle),angle)
            for k in range(5):
                derivative=[(x-y)/(2*h) for x,y in zip(after[k],before[k])]
                for a,b in zip(derivative,[-1j*x for x in rhs[k]]):
                    self.assertLess(abs(a-b),1e-8)
        # Clock projection of actual i[H_clock,N_M1] equals the G-current,
        # but the full current has off-diagonal clock components.
        for ra,sign in ((0,1),(1,-1)):
            branch=[x if ((i//16>>1)&1)==ra else 0j for i,x in enumerate(state(math.pi/4))]
            only=[[0j]*1024 for _ in range(5)]; only[2]=branch
            hn=coupled_clock_h([apply_work(n[0],x) for x in only],angle)
            nh=[apply_work(n[0],x) for x in coupled_clock_h(only,angle)]
            actual=[[1j*(x-y) for x,y in zip(a,b)] for a,b in zip(hn,nh)]
            pointwise_close(self,actual[2],apply_work(J[0],branch))
            pointwise_close(self,actual[2],[sign*x for x in branch])
            self.assertGreater(sum(inner(actual[k],actual[k]).real for k in (0,1,3,4)),0)

    def test_five_state_autonomous_clock_contains_sharp_current_stage(self):
        phi=embed(recorded_whole(),6)
        for t in (0,.21,math.pi/4,1.11,math.pi/2,math.pi):
            blocks=history_state(t); rhs=history_h(blocks)
            self.assertAlmostEqual(sum(inner(x,x).real for x in blocks),1)
            for k in range(5):
                deriv=[clock_derivative(k,t)*x for x in history_v(k,phi)]
                pointwise_close(self,deriv,[-1j*x for x in rhs[k]])
        blocks=history_state(math.pi/4)
        probs=[inner(x,x).real for x in blocks]
        for x,y in zip(probs,(1/16,4/16,6/16,4/16,1/16)):
            self.assertAlmostEqual(x,y)
        middle=blocks[2]; v=state(math.pi/4)
        self.assertAlmostEqual(inner(middle,middle).real,3/8)
        pointwise_close(self,middle,[clock_amplitude(2,math.pi/4)*x for x in v])
        for label in range(4):
            for record in (1,2):
                p=sum(abs(amp)**2 for i,amp in enumerate(middle)
                      if (i//16)//16==label and (i//16)%4==record)
                self.assertAlmostEqual(p,3/64)
        end=history_state(math.pi/2)
        self.assertAlmostEqual(inner(end[4],end[4]).real,1)
        pointwise_close(self,end[4],phi)

    def test_nonzero_current_spectrum_and_exact_opposition(self):
        j=J[0]; close(self,mm(j,j),proj)
        close(self,add(j,J[2]),scale(0,id16))
        plus=scale(.5,add(proj,j)); minus=scale(.5,sub(proj,j))
        close(self,mm(plus,plus),plus); close(self,mm(minus,minus),minus)
        close(self,mm(plus,minus),scale(0,id16))
        self.assertGreater(maxabs(j),0)

    def test_sphere_current_match_is_sharp_at_quarter_exchange(self):
        v=state(math.pi/4)
        r=apply_base(kron(tetra_control(),eye(4)),apply_work(J[0],v))
        pointwise_close(self,r,v)
        pointwise_close(self,apply_work(add(J[0],J[2]),v),[0j]*len(v))
        for record,sgn in ((0,1),(1,-1)):
            w=[x if ((i//16>>1)&1)==record else 0j for i,x in enumerate(v)]
            pointwise_close(self,apply_work(J[0],w),[sgn*x for x in w])
            pointwise_close(self,apply_work(J[2],w),[-sgn*x for x in w])
            self.assertAlmostEqual(inner(w,w).real,.5)

    def test_mismatch_probability_exact_for_arbitrary_exchange_time(self):
        # T_dir²=I, J²=P_ab and state lies in P_ab. The mismatch
        # spectral projector is (I−T_dir J)/2 on the occupied sector.
        for t in (0,.17,math.pi/8,math.pi/4,math.pi/2,3*math.pi/4):
            v=state(t); corr=inner(v,apply_base(kron(tetra_control(),eye(4)),apply_work(J[0],v))).real
            self.assertAlmostEqual((1-corr)/2,(1-math.sin(2*t))/2)

    def test_same_branch_marginals_cannot_determine_opposite_currents(self):
        v=state(math.pi/4)
        for sites in ([0],[2],[0,1],[2,3],[0,2]):
            close(self,reduced_work(v,sites,0),reduced_work(v,sites,1))
        close(self,reduced_work(v,[0],0),scale(.5,eye(2)))
        close(self,reduced_work(v,[2],0),scale(.5,eye(2)))
        close(self,reduced_work(v,[0,1],0),reduced_work(v,[2,3],0))
        self.assertAlmostEqual(cond(v,J[0],0),1)
        self.assertAlmostEqual(cond(v,J[0],1),-1)

    def test_single_memory_phase_flip_reverses_current_with_same_marginals(self):
        v=state(math.pi/4); z=phase_flip(v)
        zmat=[[complex((1-2*bit(i,0)) if i==j else 0) for j in range(16)] for i in range(16)]
        close(self,mm(mm(zmat,J[0]),zmat),scale(-1,J[0]))
        for k in n: self.assertLess(maxabs(comm(zmat,k)),1e-10)
        for ra in (None,0,1):
            for sites in ([0],[2],[0,1],[2,3],[0,2]): close(self,reduced_work(v,sites,ra),reduced_work(z,sites,ra))
        for ra in (0,1): self.assertAlmostEqual(cond(z,J[0],ra),-cond(v,J[0],ra))
        corr=inner(z,apply_base(kron(tetra_control(),eye(4)),apply_work(J[0],z))).real
        self.assertAlmostEqual(corr,-1)
        # G and its tensor-factor interpretation stay fixed: this is a
        # physical logical phase operation, not only a coordinate relabelling.

    def test_exact_general_response_parity_condition(self):
        for qp,qm,q0 in ((2,-2,0),(2,-1,0),(-1,-1,0),(3,.5,4),(.4,-.4,.7)):
            result=add(current_response(qp,qm,q0),sign_conjugate_response(qp,qm,q0))
            expected=add(scale(qp+qm,proj),scale(2*q0,sub(id16,proj)))
            close(self,result,expected)
            active=mm(mm(proj,result),proj)
            close(self,active,scale(qp+qm,proj))
        # On nonzero active support, cancellation iff q(+1)+q(−1)=0.

    def test_positive_sign_sensitive_weights_do_not_cancel_sharp_currents(self):
        eta=.3; j=J[0]; jm=J[2]
        w1=add(id16,scale(eta,j)); w2=add(id16,scale(eta,jm))
        result=add(mm(w1,j),mm(w2,jm))
        close(self,result,scale(2*eta,proj))
        for record in (0,1):
            self.assertAlmostEqual(cond(state(math.pi/4),result,record),2*eta)
        # w has strictly positive spectrum {1,1±eta}; weights commute
        # with the current whose value they weight.
        self.assertGreater(1-eta,0)

    def test_even_incidence_response_cancels_without_forcing_zero_local_values(self):
        k=2.7; w=1.4
        qplus,qminus=k*w,-k*w
        response=current_response(qplus,qminus)
        total=add(response,sign_conjugate_response(qplus,qminus))
        close(self,total,scale(0,id16))
        v=state(math.pi/4)
        self.assertAlmostEqual(cond(v,response,0),k*w)
        self.assertAlmostEqual(cond(v,response,1),-k*w)

    def test_two_negative_experiential_values_are_an_allowed_response_counterexample(self):
        # q(x)=−|x|: both opposite active currents map to −1. This
        # demonstrates underdetermination, not actual suffering in the model.
        negative=current_response(-1,-1)
        both=add(negative,sign_conjugate_response(-1,-1))
        close(self,both,scale(-2,proj))
        for ra in (0,1): self.assertAlmostEqual(cond(state(math.pi/4),both,ra),-2)

    def test_endpoints_are_not_sharp_current(self):
        for t in (0,math.pi/2):
            v=state(t)
            self.assertAlmostEqual(cond(v,J[0],0),0)
            self.assertAlmostEqual(cond(v,mm(J[0],J[0]),0),1)
        # Thus a zero mean is not a zero current eigenvalue; active-sector
        # projective measurements at the endpoints give ±1 equiprobably.

if __name__=='__main__': unittest.main()
