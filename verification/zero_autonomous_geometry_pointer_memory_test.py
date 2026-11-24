"""Closed constrained geometry, sphere logical clock, pointer and memory.

The φ-independent interaction is inside the chosen branch constraint. Memory
is a reversible qubit, not an irreversible local device or a subject. Numerical
spectral propagation is checked against an independent Chebyshev calculation.
"""
import cmath
import math
import unittest
from verification.zero_sphere_interacting_clock_spectral_test import jacobi,transform,untransform
from verification.zero_sphere_finite_resolution_clock_instrument_test import mesh,effects,apply,dot
from verification.zero_sphere_autonomous_detector_constraint_test import translated
from verification.zero_domain_restriction_sector_clock_code_test import environment_vectors,rho_s_ref,rho_reference
from verification.zero_spin_constitution_test import close

LAMBDA=.4
KAPPA=1.


def build(n,kappa=KAPPA):
    p,f,dp=mesh(n);E=effects(p,dp)[0][0]
    gap=math.sqrt(kappa*kappa+4*LAMBDA*LAMBDA)
    sectors={}
    for m in (1,-1):
        for sign in (1,-1):
            s=(kappa*m+sign*gap)/2
            matrix=[[(p[i]**2/6 if i==j else 0)-2*s*E[i][j]
                    for j in range(n)] for i in range(n)]
            vals,V=jacobi(matrix)
            sectors[m,sign]=(s,matrix,vals,V)
    return p,translated(f,p),E,gap,sectors


def propagate(V,values,v,h,t):
    a=transform(V,v)
    return untransform(V,[z*cmath.exp(1j*math.sqrt(e-2*h)*t) for z,e in zip(a,values)])


def channels(f,gap,sectors,t):
    out={}
    for h in (0,1):
        for m in (1,-1):
            sp,_,ep,Vp=sectors[m,1]
            sm,_,em,Vm=sectors[m,-1]
            up=propagate(Vp,ep,f,h,t);um=propagate(Vm,em,f,h,t)
            out[h,m,0]=[(-sm*a+sp*b)/gap for a,b in zip(up,um)]
            out[h,m,1]=[1j*LAMBDA*(a-b)/gap for a,b in zip(up,um)]
    return out


def evolve_general(ch,gap,sectors,t):
    """Evolve arbitrary pointer amplitudes in each logical/memory-y sector."""
    out={}
    for h in (0,1):
        for m in (1,-1):
            sp,_,ep,Vp=sectors[m,1]; sm,_,em,Vm=sectors[m,-1]
            a,b=ch[h,m,0],ch[h,m,1]
            p0=[(-sm*x-1j*LAMBDA*y)/gap for x,y in zip(a,b)]
            p1=[(1j*LAMBDA*x+sp*y)/gap for x,y in zip(a,b)]
            q0=[(sp*x+1j*LAMBDA*y)/gap for x,y in zip(a,b)]
            q1=[(-1j*LAMBDA*x-sm*y)/gap for x,y in zip(a,b)]
            p0=propagate(Vp,ep,p0,h,t);p1=propagate(Vp,ep,p1,h,t)
            q0=propagate(Vm,em,q0,h,t);q1=propagate(Vm,em,q1,h,t)
            out[h,m,0]=[x+y for x,y in zip(p0,q0)]
            out[h,m,1]=[x+y for x,y in zip(p1,q1)]
    return out


def sequential_probe(f,gap,S,t1=40,t2=100):
    """Optional ideal pointer projection at t1, memory z measurement at t2."""
    before=channels(f,gap,S,t1);results={}
    for d in (0,1):
        after={key:(list(v) if key[2]==d else [0j]*len(v)) for key,v in before.items()}
        later=evolve_general(after,gap,S,t2-t1)
        table=joint_probs(later)
        for m in (0,1):results[d,m]=sum(table[dd,m] for dd in (0,1))
    return results


def joint_probs(ch):
    out={}
    for d in (0,1):
        for m in (0,1):
            total=0.
            for h in (0,1):
                v=[(a+(-1 if m else 1)*b)/2 for a,b in zip(ch[h,1,d],ch[h,-1,d])]
                total+=dot(v,v).real/2
            out[d,m]=total
    return out


def window_occupation(ch,E):
    # Logical and memory-y weights are each 1/2. Pointer amplitudes are explicit.
    return sum(dot(v,apply(E,v)).real/4 for v in ch.values())


def mutual_information(pr):
    dprob={d:sum(pr[d,m] for m in (0,1)) for d in (0,1)}
    mprob={m:sum(pr[d,m] for d in (0,1)) for m in (0,1)}
    return sum(x*math.log2(x/(dprob[d]*mprob[m]))
               for (d,m),x in pr.items() if x>1e-16)


def chebyshev(p,E,h,s,v,t,degree=180,quad=512):
    # Independent operator-functional propagation on a rigorous global interval.
    smax=(KAPPA+math.sqrt(KAPPA*KAPPA+4*LAMBDA*LAMBDA))/2
    lo=4-2*smax;hi=49/6+2*smax;c=(hi+lo)/2;r=(hi-lo)/2
    angles=[math.pi*(j+.5)/quad for j in range(quad)]
    vals=[cmath.exp(1j*t*math.sqrt(c+r*math.cos(x))) for x in angles]
    coeff=[2/quad*sum(y*math.cos(k*x) for x,y in zip(angles,vals)) for k in range(degree)]
    def X(z):
        Ez=apply(E,z)
        return [((p[i]**2/6-2*h-c)*z[i]-2*s*Ez[i])/r for i in range(len(p))]
    a=list(v);out=[coeff[0]*z/2 for z in a]
    b=X(a);out=[x+coeff[1]*z for x,z in zip(out,b)]
    for k in range(2,degree):
        xb=X(b);cc=[2*x-y for x,y in zip(xb,a)]
        out=[x+coeff[k]*z for x,z in zip(out,cc)];a,b=b,cc
    return out


def control_no_memory(data,t):
    # κ=0, so a single D coupling λσ_y. Direct spectral propagation.
    p,f,E,_,_=data;S={}
    for d in (1,-1):
        mat=[[(p[i]**2/6 if i==j else 0)-2*LAMBDA*d*E[i][j]
              for j in range(len(p))] for i in range(len(p))]
        ev,V=jacobi(mat);S[d]=(ev,V)
    return sum(dot([(a-b)/2 for a,b in zip(propagate(S[1][1],S[1][0],f,h,t),
                                             propagate(S[-1][1],S[-1][0],f,h,t))],
                   [(a-b)/2 for a,b in zip(propagate(S[1][1],S[1][0],f,h,t),
                                             propagate(S[-1][1],S[-1][0],f,h,t))]).real/2
               for h in (0,1))


class AutonomousGeometryPointerMemoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data={n:build(n) for n in (40,80,160)}
        p,f,E,gap,S=cls.data[80]
        cls.bytime={t:joint_probs(channels(f,gap,S,t)) for t in (0,40,60,100,150,200)}

    def test_positive_root_and_previous_spectral_bounds_apply_in_channels(self):
        smax=(KAPPA+math.sqrt(KAPPA*KAPPA+4*LAMBDA*LAMBDA))/2
        cmax=2*smax
        self.assertGreater(4-cmax,1.71)
        self.assertLess(cmax,3*math.pi*math.sqrt(3)/7)
        self.assertLess(cmax*7/(3*math.pi),2)
        for p,f,E,gap,S in self.data.values():
            for s,mat,ev,V in S.values():
                self.assertGreater(min(ev)-2,0)
                nlow=sum(x<6 for x in ev);nhigh=sum(x>49/6 for x in ev)
                if abs(s)>1:
                    self.assertEqual((nlow,nhigh),(1,0) if s>0 else (0,1))
                else:
                    # Shallow continuum modes need not be resolved at finite N.
                    self.assertEqual((nlow,nhigh),(0,0))

    def test_zero_initial_record_and_normalization_at_readings(self):
        pr=self.bytime[0]
        self.assertAlmostEqual(pr[0,0],1,places=11)
        for key in ((0,1),(1,0),(1,1)):self.assertAlmostEqual(pr[key],0,places=11)
        for pr in self.bytime.values():
            self.assertAlmostEqual(sum(pr.values()),1,places=11)
            self.assertTrue(all(x>=0 for x in pr.values()))

    def test_joint_pointer_memory_correlations(self):
        pr=self.bytime[100]
        self.assertAlmostEqual(pr[0,0],.462954440036677,places=10)
        self.assertAlmostEqual(pr[0,1],.17036172298662433,places=10)
        self.assertAlmostEqual(pr[1,0],.05126952913725878,places=10)
        self.assertAlmostEqual(pr[1,1],.3154143078394622,places=10)
        m_if_d1=pr[1,1]/(pr[1,0]+pr[1,1])
        m_if_d0=pr[0,1]/(pr[0,0]+pr[0,1])
        self.assertGreater(m_if_d1-m_if_d0,.59)
        self.assertAlmostEqual(mutual_information(pr),.25335708300738513,places=10)

    def test_readout_changes_pointer_and_is_not_nondemolition(self):
        pr=self.bytime[100];pointer=pr[1,0]+pr[1,1]
        unmonitored=control_no_memory(self.data[80],100)
        self.assertAlmostEqual(unmonitored,.958895,places=4)
        self.assertGreater(unmonitored-pointer,.55)
        # [P_D=1, λσ_y] is nonzero: λσ_y flips pointer sectors.
        self.assertNotEqual(LAMBDA,0)

    def test_intermediate_pointer_projection_and_later_memory(self):
        p,f,E,gap,S=self.data[80]
        first=channels(f,gap,S,40)
        advanced=evolve_general(first,gap,S,60)
        direct=channels(f,gap,S,100)
        for key in direct:
            self.assertLess(sum(abs(a-b)**2 for a,b in zip(advanced[key],direct[key])),1e-21)
        table=sequential_probe(f,gap,S,40,100)
        self.assertAlmostEqual(sum(table.values()),1,places=10)
        self.assertAlmostEqual(table[0,0],.519066136648028,places=10)
        self.assertAlmostEqual(table[1,1],.2683780958812817,places=10)
        self.assertAlmostEqual(mutual_information(table),.248007049067934,places=10)
        # The extra projection changes the later memory distribution.
        probed=table[0,1]+table[1,1]
        unprobed=self.bytime[100][0,1]+self.bytime[100][1,1]
        self.assertGreater(abs(unprobed-probed),.05)

    def test_receding_control_distinguishes_event(self):
        p,f,E,gap,S=self.data[80]; fback=translated(f,p,30)
        # Original f had x0=-15: translating by +30 changes x0 to +15.
        pr=joint_probs(channels(fback,gap,S,100))
        self.assertAlmostEqual(pr[1,1],.00016858056431159587,places=10)
        self.assertLess(pr[0,1]+pr[1,1],.001)
        self.assertGreater(self.bytime[100][0,1]+self.bytime[100][1,1],.48)

    def test_late_joint_statistics_and_window_activity(self):
        p,f,E,gap,S=self.data[80]
        for t in (100,150,200):
            ch=channels(f,gap,S,t)
            self.assertLess(window_occupation(ch,E),.0015)
        for t in (150,200):
            self.assertLess(sum(abs(self.bytime[t][k]-self.bytime[100][k]) for k in self.bytime[t]),.001)
        # Finite sample persistence is not irreversibility or an asymptotic theorem.

    def test_encoded_confined_reduction_stays_decoupled_from_pointer_reference(self):
        # One projected momentum/memory-y slice of the actual two-logical-
        # component output, with pointer retained as reference. The general
        # statement follows from the prior environment-code isometry.
        p,f,E,gap,S=self.data[80];ch=channels(f,gap,S,100);i=40;m=1
        coeff=[[(1 if h==0 else 1j)*ch[h,m,d][i] for d in (0,1)] for h in (0,1)]
        size=math.sqrt(sum(abs(x)**2 for row in coeff for x in row))
        coeff=[[x/size for x in row] for row in coeff]
        env=environment_vectors();actual=rho_s_ref(env,coeff);ref=rho_reference(coeff)
        expected=[[ref[a][b]/2 if r==rp else 0j
                   for rp in (0,1) for b in (0,1)]
                  for r in (0,1) for a in (0,1)]
        close(self,actual,expected)

    def test_grid_refinement(self):
        for t in (40,100,200):
            previous=None
            for n in (40,80,160):
                p,f,E,gap,S=self.data[n];pr=joint_probs(channels(f,gap,S,t))
                if previous is not None:self.assertLess(max(abs(pr[k]-previous[k]) for k in pr),.0005)
                previous=pr

    def test_spectral_propagation_against_chebyshev(self):
        p,f,E,gap,S=self.data[40]
        for h,m,sign,t in ((0,1,1,40),(1,1,1,100),(0,-1,-1,100)):
            s,mat,ev,V=S[m,sign]
            x=propagate(V,ev,f,h,t);y=chebyshev(p,E,h,s,f,t)
            self.assertLess(sum(abs(a-b)**2 for a,b in zip(x,y)),1e-22)

    def test_constraint_cancellation_with_memory_interaction(self):
        p,f,E,gap,S=self.data[80]
        for h,m,sign,t in ((0,1,1,40),(1,-1,-1,100),(1,1,-1,60)):
            s,theta,vals,V=S[m,sign]
            u=propagate(V,vals,f,h,t)
            grav=-sum(p[i]**2*abs(u[i])**2 for i in range(len(p)))/12
            scalar=dot(u,apply(theta,u)).real/2-h*dot(u,u).real
            internal=h*dot(u,u).real
            interaction=s*dot(u,apply(E,u)).real
            self.assertAlmostEqual(grav+scalar+internal+interaction,0,places=11)
            self.assertGreater(scalar,0)
            self.assertLess(grav,0)

if __name__=='__main__':unittest.main()
