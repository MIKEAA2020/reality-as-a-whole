"""Two autonomous pointer records at different geometry windows.

Uses NumPy for band-matrix / spinor Chebyshev evolution. Install with
  python -m pip install --target .arena/python-deps numpy
  PYTHONPATH=.arena/python-deps python -m unittest verification.zero_autonomous_two_window_records_test

Finite Nyström/degree checks are not continuum spectral or irreversible-record
proofs. The continuum positive-root bounds are analytic in the companion note.
"""
import math
import unittest
import numpy as np

from verification.zero_sphere_finite_resolution_clock_instrument_test import mesh,window_kernel
from verification.zero_sphere_autonomous_detector_constraint_test import translated
from verification.zero_domain_restriction_sector_clock_code_test import environment_vectors,rho_s_ref,rho_reference
from verification.zero_spin_constitution_test import close

LAMBDA=.5
K1=.65
K2=.65
CENTERS=(-5.,0.,5.)


def make_model(n=80, k1=K1, k2=K2, centers=CENTERS, x0=-15.):
    p,f,dp=mesh(n); p=np.asarray(p);f=np.asarray(translated(f,p,x0),dtype=complex)
    delta=p[:,None]-p[None,:]
    kernel=np.array([[dp*window_kernel(float(x)) for x in row] for row in delta])
    effects=[kernel*np.exp(-1j*delta*a) for a in centers]
    lo=4-2*(LAMBDA+abs(k1)+abs(k2))
    hi=49/6+2*(LAMBDA+abs(k1)+abs(k2))
    if lo<=0:raise ValueError('this conservative bound does not ensure root positivity')
    return p,f,effects,lo,hi,k1,k2


def theta_apply(model,v,h):
    p,_,E,_,_,k1,k2=model
    out=(p*p/6-2*h)*v
    # spin order D, M1, M2, momentum; sigma_y |0>=i|1>.
    w=np.einsum('pq,ijkq->ijkp',E[0],v,optimize=True)
    out[1,:,:] += -2j*LAMBDA*w[0,:,:]
    out[0,:,:] +=  2j*LAMBDA*w[1,:,:]
    w=np.einsum('pq,jkq->jkp',E[1],v[1],optimize=True)
    out[1,1,:] += -2j*k1*w[0,:]
    out[1,0,:] +=  2j*k1*w[1,:]
    w=np.einsum('pq,jkq->jkp',E[2],v[1],optimize=True)
    out[1,:,1] += -2j*k2*w[:,0]
    out[1,:,0] +=  2j*k2*w[:,1]
    return out


def initial(model,pointer='balanced'):
    p,f,*_=model
    v=np.zeros((2,2,2,len(p)),dtype=complex)
    if pointer=='balanced':v[0,0,0]=f/math.sqrt(2);v[1,0,0]=1j*f/math.sqrt(2)
    elif pointer=='zero':v[0,0,0]=f
    elif pointer=='one':v[1,0,0]=f
    else:raise ValueError(pointer)
    return v


def evolve(model,h,t,pointer='balanced',degree=260,quad=640):
    lo,hi=model[3:5];mid=(lo+hi)/2;radius=(hi-lo)/2
    th=math.pi*(np.arange(quad)+.5)/quad
    coeff=(2/quad)*(np.cos(np.outer(np.arange(degree),th)) @
                    np.exp(1j*t*np.sqrt(mid+radius*np.cos(th))))
    def x(v):return (theta_apply(model,v,h)-mid*v)/radius
    a=initial(model,pointer);b=x(a);out=coeff[0]*a/2+coeff[1]*b
    for k in range(2,degree):
        a,b=b,2*x(b)-a
        out+=coeff[k]*b
    return out


def states(model,t,pointer='balanced',degree=260,quad=640):
    return [evolve(model,h,t,pointer,degree,quad) for h in (0,1)]


def probabilities(vs):
    return sum(np.sum(abs(v)**2,axis=3)/2 for v in vs)


def event_probs(model,vs):
    result=[]
    for E in model[2]:
        result.append(sum(np.vdot(v,np.einsum('pq,ijkq->ijkp',E,v,optimize=True)).real/2 for v in vs))
    return np.array(result)


def mutual_information(joint):
    left=joint.sum(axis=1);right=joint.sum(axis=0)
    return sum(x*math.log2(x/(left[i]*right[j]))
               for (i,j),x in np.ndenumerate(joint) if x>1e-16)


class AutonomousTwoWindowRecordsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model=make_model(80)
        cls.vs={t:states(cls.model,t) for t in (0,30,40,60,100,150)}
        cls.probs={t:probabilities(v) for t,v in cls.vs.items()}

    def test_positive_root_and_smeared_window_operators(self):
        p,f,Es,lo,hi,k1,k2=self.model
        self.assertAlmostEqual(lo,.4)
        self.assertAlmostEqual(hi,49/6+3.6)
        for E in Es:
            self.assertLess(np.linalg.norm(E-E.conj().T),1e-12)
            ev=np.linalg.eigvalsh(E)
            self.assertGreater(min(ev),-1e-12)
            self.assertLess(max(ev),1+1e-12)
        # The translated windows do not generically commute after band projection.
        self.assertGreater(np.linalg.norm(Es[1]@Es[2]-Es[2]@Es[1]),.001)

    def test_shifted_window_correctly_tracks_translated_packet(self):
        n=80;p,f,Es,lo,hi,k1,k2=self.model
        _,unshifted,_=mesh(n);unshifted=np.array(unshifted)
        for a,E in zip(CENTERS,Es):
            packet=np.array(translated(unshifted,p,a))
            compare=np.vdot(unshifted,Es[1]@unshifted)
            self.assertAlmostEqual(abs(np.vdot(packet,E@packet)-compare),0,places=11)

    def test_initial_conditions_and_unitarity(self):
        P=self.probs[0]
        self.assertAlmostEqual(P[0,0,0],.5,places=11)
        self.assertAlmostEqual(P[1,0,0],.5,places=11)
        self.assertAlmostEqual(P[:,:,1].sum()+P[:,1,0].sum(),0,places=11)
        for t,vectors in self.vs.items():
            for v in vectors:self.assertAlmostEqual(np.vdot(v,v).real,1,places=10)
            self.assertAlmostEqual(self.probs[t].sum(),1,places=10)

    def test_root_propagation_convergence_not_just_norm(self):
        for h,t in ((0,100),(1,100),(0,150),(1,150)):
            a=evolve(self.model,h,t,degree=260,quad=640)
            b=evolve(self.model,h,t,degree=320,quad=800)
            self.assertLess(np.vdot(a-b,a-b).real,1e-20)
        # A lower degree at long times can pass neither norm nor vector check.
        bad=evolve(self.model,0,150,degree=150,quad=640)
        self.assertGreater(abs(np.vdot(bad,bad).real-1),.1)

    def test_record_order_and_final_record_correlation(self):
        p30=self.probs[30];p100=self.probs[100]
        m1_30=p30[:,1,:].sum();m2_30=p30[:,:,1].sum()
        m1_100=p100[:,1,:].sum();m2_100=p100[:,:,1].sum()
        self.assertAlmostEqual(m1_30,.30366196,places=7)
        self.assertAlmostEqual(m2_30,.12672955,places=7)
        self.assertGreater(m1_30-m2_30,.17)
        self.assertAlmostEqual(m1_100,.43271225,places=7)
        self.assertAlmostEqual(m2_100,.41709023,places=7)
        joint=p100.sum(axis=0)
        self.assertAlmostEqual(mutual_information(joint),.424712104696,places=9)
        self.assertAlmostEqual(joint[0,0]+joint[1,1],.86817014856,places=9)
        self.assertGreater(joint[1,1]/joint[1].sum()-joint[0,1]/joint[0].sum(),.72)

    def test_window_expectations_and_late_stability_are_finite_time(self):
        ev30=event_probs(self.model,self.vs[30]);ev100=event_probs(self.model,self.vs[100])
        self.assertGreater(ev30[1],ev30[0]);self.assertGreater(ev30[2],ev30[0])
        self.assertTrue(all(ev100<.001))
        p100=self.probs[100].sum(axis=0);p150=self.probs[150].sum(axis=0)
        self.assertLess(np.sum(abs(p100-p150)),.003)

    def test_second_memory_backreacts_on_first_record(self):
        without=probabilities(states(make_model(80,k2=0),100))
        first_without=without[:,1,:].sum();first_with=self.probs[100][:,1,:].sum()
        self.assertAlmostEqual(first_without,.42486978,places=7)
        self.assertGreater(abs(first_with-first_without),.007)
        self.assertAlmostEqual(without[:,:,1].sum(),0,places=11)

    def test_incident_and_receding_packet_control(self):
        back=probabilities(states(make_model(80,x0=15),100))
        self.assertLess(back[:,1,:].sum(),.002)
        self.assertLess(back[:,:,1].sum(),.003)
        incident=self.probs[100]
        self.assertGreater(incident[:,1,:].sum(),.4)
        self.assertGreater(incident[:,:,1].sum(),.4)

    def test_matched_incoherent_pointer_mixture_is_a_separate_control(self):
        p0=probabilities(states(self.model,100,pointer='zero'))
        p1=probabilities(states(self.model,100,pointer='one'))
        mixture=(p0+p1)/2
        joint=mixture.sum(axis=0)
        self.assertAlmostEqual(mutual_information(joint),.417798350099,places=9)
        self.assertGreater(mutual_information(joint),.4)
        # The coherent preparation changes statistics, but most of the record
        # correlation is present in a matched incoherent pointer mixture too.
        self.assertGreater(np.max(abs(joint-self.probs[100].sum(axis=0))),.004)

    def test_initial_pointer_zero_control(self):
        P=probabilities(states(self.model,100,pointer='zero'))
        self.assertGreater(P[1,:,:].sum(),.97)
        self.assertGreater(P[:,1,:].sum(),.85)
        self.assertGreater(P[:,:,1].sum(),.82)
        # Record agreement under this strongly biased preparation is not
        # evidence of strong mutual information.
        self.assertLess(mutual_information(P.sum(axis=0)),.002)

    def test_chebyshev_against_independent_dense_eigensystem(self):
        model=make_model(32);n=32;dim=8*n
        H=np.column_stack([theta_apply(model,np.eye(1,dim,j,dtype=complex).reshape(2,2,2,n),0).ravel()
                           for j in range(dim)])
        self.assertLess(np.linalg.norm(H-H.conj().T),1e-11)
        ev,V=np.linalg.eigh(H)
        self.assertGreater(ev.min()-2,0)
        for h in (0,1):
            init=initial(model).ravel()
            expected=V@(np.exp(1j*100*np.sqrt(ev-2*h))*(V.conj().T@init))
            actual=evolve(model,h,100).ravel()
            self.assertLess(np.vdot(actual-expected,actual-expected).real,1e-21)

    def test_same_results_on_grid_refinement(self):
        previous=None
        for n in (40,80,160):
            P=probabilities(states(make_model(n),100))
            if previous is not None:self.assertLess(np.max(abs(P-previous)),.0005)
            previous=P

    def test_operator_hermiticity_and_on_branch_cancellation(self):
        v=self.vs[40][1];tv=theta_apply(self.model,v,1)
        self.assertLess(abs(np.vdot(v,tv).imag),1e-11)
        p=self.model[0];norm=np.vdot(v,v).real
        grav=-np.sum(abs(v)**2*(p*p/12)).real
        scalar=np.vdot(v,tv).real/2
        interaction=np.vdot(v,(tv-(p*p/6-2)*v)).real/(-2)
        self.assertAlmostEqual(grav+scalar+norm+interaction,0,places=11)
        self.assertGreater(scalar,0)
        self.assertLess(grav,0)

    def test_actual_encoded_sphere_reduction_for_a_reference_slice(self):
        # Pick a nonzero momentum, two-memory sector and retain D as reference.
        # General decoupling follows from the established code isometry.
        i=40;m1=1;m2=1
        coeff=[[(1 if h==0 else 1j)*self.vs[100][h][d,m1,m2,i]
                for d in (0,1)] for h in (0,1)]
        size=math.sqrt(sum(abs(x)**2 for row in coeff for x in row))
        self.assertGreater(size,1e-6)
        coeff=[[x/size for x in row] for row in coeff]
        env=environment_vectors();actual=rho_s_ref(env,coeff);ref=rho_reference(coeff)
        expected=[[ref[a][b]/2 if r==rp else 0j
                   for rp in (0,1) for b in (0,1)]
                  for r in (0,1) for a in (0,1)]
        close(self,actual,expected)

if __name__=='__main__':unittest.main()
