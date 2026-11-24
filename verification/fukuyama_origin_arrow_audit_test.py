"""Focused checks on Fukuyama (2025) and a separate record-arrow toy.

These check stated mathematical consequences and counterexamples, not a full
replication of the 1989 influence-functional calculation or 4D quantum gravity.
"""
import cmath
import math
import unittest
import numpy as np


def psi(N,chi,alpha,c1):
    return cmath.exp(c1*N*N/2+alpha*alpha*math.exp(2*chi)/(2*c1))


def trajectory(t,alpha=1.,A=1.,amax=1.):
    theta=alpha*t;a=amax*math.sin(theta);N=A*math.cos(theta)
    chi=math.log(a)
    sp=(chi+N)/math.sqrt(2);sm=(chi-N)/math.sqrt(2)
    dp=alpha*(1/math.tan(theta)-A*math.sin(theta))/math.sqrt(2)
    dm=alpha*(1/math.tan(theta)+A*math.sin(theta))/math.sqrt(2)
    return a,N,sp,sm,dp,dm


def gaussian_parameters(a,b):
    sigma2=1/(a+2*b);purity=math.sqrt(a/(a+2*b))
    q=(1-purity)/(1+purity)
    S=0. if q==0 else -math.log(1-q)-q/(1-q)*math.log(q)
    return sigma2,purity,q,S


def gaussian_grid(a,b,n=360,L=9.):
    dx=2*L/n;x=-L+(np.arange(n)+.5)*dx
    X=x[:,None];Y=x[None,:]
    return math.sqrt(2*a/math.pi)*np.exp(-a*(X*X+Y*Y)-b*(X-Y)**2)*dx


def binary_entropy(p):
    if p<1e-15 or p>1-1e-15:return 0.
    return -p*math.log2(p)-(1-p)*math.log2(1-p)


def qubit_state(t,g=1.,delta=0.):
    angle=g*t+delta
    return np.array([math.cos(angle),0,0,-1j*math.sin(angle)])


def reductions(v):
    A=v.reshape(2,2);return A@A.conj().T,A.conj().T@A


class FukuyamaOriginArrowAuditTests(unittest.TestCase):
    def test_wdw_exact_solution_by_derivative_and_finite_difference(self):
        for N,chi,alpha,c1 in ((.6,-.4,1.,-1+.7j),(-.7,.3,.8,-.3+1.2j)):
            v=psi(N,chi,alpha,c1)
            mixed=(c1*N)*(alpha**2*math.exp(2*chi)/c1)*v
            self.assertLess(abs(mixed-alpha**2*N*math.exp(2*chi)*v),1e-13)
            e=1e-4
            fd=(psi(N+e,chi+e,alpha,c1)-psi(N+e,chi-e,alpha,c1)
                -psi(N-e,chi+e,alpha,c1)+psi(N-e,chi-e,alpha,c1))/(4*e*e)
            self.assertLess(abs(fd-mixed),1e-7)

    def test_wdw_current_conservation_for_the_exact_mode(self):
        # In (χ,N) variables, ∂−j−+∂+j+=2[∂χ(ρ S_N)+∂N(ρ S_χ)].
        for N,chi,alpha,beta,gamma in ((.2,.1,1.,.7,1.2),(-.9,-.4,.8,1.1,.6)):
            a=alpha**2*math.exp(2*chi)/(beta**2+gamma**2)
            rho=abs(psi(N,chi,alpha,complex(-beta,gamma)))**2
            SN=gamma*N;Schi=-gamma*a
            logN=-2*beta*N;logchi=-2*beta*a
            divergence=2*rho*(logchi*SN+logN*Schi)
            self.assertAlmostEqual(divergence,0,places=12)

    def test_wave_mode_is_not_square_integrable_on_flat_measure(self):
        # beta>0; rho -> exp(-beta*N^2) as chi -> -infinity.
        c1=-1+.7j;N=.2
        for chi in (-10,-20):
            self.assertAlmostEqual(abs(psi(N,chi,1.,c1))**2,math.exp(-N*N),places=8)
        # This is not a claim about the physical Klein-Gordon inner product.

    def test_printed_jt_equation_and_proposed_trajectory(self):
        # The PDF prints χ''+χ'=Λ; the stated sin trajectory satisfies
        # χ''+(χ')²=Λ instead.  Check (25) independently as printed.
        alpha=1.;t=math.pi/3;A=1.
        chidot=alpha/math.tan(alpha*t)
        chiddot=-alpha**2/(math.sin(alpha*t)**2)
        self.assertGreater(abs(chiddot+chidot+alpha**2),.2)
        self.assertAlmostEqual(chiddot+chidot**2,-alpha**2,places=12)
        N=A*math.cos(alpha*t);Nd=-A*alpha*math.sin(alpha*t);Ndd=-alpha**2*N
        self.assertAlmostEqual(Ndd+chidot*Nd+2*alpha**2*N,0,places=12)

    def test_local_clock_turn_after_maximum_not_at_maximum(self):
        for A in (.1,1.,3.):
            c=(1-math.sqrt(1+4*A*A))/(2*A);turn=math.acos(c)
            self.assertGreater(turn,math.pi/2);self.assertLess(turn,math.pi)
            self.assertAlmostEqual(trajectory(turn,A=A)[5],0,places=12)
            self.assertGreater(trajectory(math.pi/2,A=A)[5],0)
            self.assertLess(trajectory(turn-.01,A=A)[5]*trajectory(turn+.01,A=A)[5],0)
            self.assertLess(trajectory(turn,A=A)[4],0)
            for t in (.2,.8,1.2):
                a,N,sp,sm,_,_=trajectory(t,A=A)
                a2,N2,sp2,sm2,_,_=trajectory(math.pi-t,A=A)
                self.assertAlmostEqual(a,a2);self.assertAlmostEqual(N,-N2)
                self.assertAlmostEqual(sp,sm2);self.assertAlmostEqual(sm,sp2)

    def test_flat_bounce_friedmann_and_curvature(self):
        # k=0, a=cosh t, 8πG=1. NEC violation is explicit.
        for t in (-10,-2,0,2,10):
            H=math.tanh(t);dH=1/math.cosh(t)**2
            rho=3*H*H;p=-(2*dH+3*H*H)
            self.assertAlmostEqual(rho+p,-2*dH)
            self.assertLess(rho+p,0)
            R=6*(dH+2*H*H)
            kretsch=12*(1+H**4)
            self.assertGreaterEqual(R,6);self.assertLessEqual(R,12)
            self.assertGreaterEqual(kretsch,12);self.assertLessEqual(kretsch,24)
        # a>=1 implies affine-parameter bounds for causal geodesics.

    def test_open_de_sitter_slice_is_nonsingular_in_curvature(self):
        for t in (.001,.3,1,5):
            a=math.sinh(t);ad=math.cosh(t);add=a
            self.assertAlmostEqual(ad*ad-a*a,1,places=10)
            self.assertAlmostEqual(6*(add/a+(ad*ad-1)/(a*a)),12,places=8)
            self.assertAlmostEqual(12*((add/a)**2+((ad*ad-1)/(a*a))**2),24,places=8)

    def test_coherence_width_can_narrow_as_entropy_falls(self):
        results=[]
        for a in (1.,4.):
            sig,purity,q,S=gaussian_parameters(a,1.)
            r=gaussian_grid(a,1.);vals=np.linalg.eigvalsh(r)
            self.assertGreater(vals.min(),-1e-12)
            self.assertAlmostEqual(np.trace(r),1,places=11)
            self.assertAlmostEqual(np.trace(r@r),purity,places=10)
            self.assertAlmostEqual(vals[-1],1-q,places=10)
            numeric=-sum(v*math.log(v) for v in vals if v>1e-14)
            self.assertAlmostEqual(numeric,S,places=9)
            results.append((sig,purity,S))
        self.assertLess(results[1][0],results[0][0])
        self.assertGreater(results[1][1],results[0][1])
        self.assertLess(results[1][2],results[0][2])
        self.assertAlmostEqual(results[0][2],.7939454041714471,places=12)
        self.assertAlmostEqual(results[1][2],.3641011943154372,places=12)

    def test_record_history_satisfies_constraint(self):
        X=np.array([[0,1],[1,0]],complex);H=np.kron(X,X)
        for t,delta in ((.1,0.),(.5,math.pi/8),(1.2,0.)):
            e=1e-6
            d=(qubit_state(t+e,delta=delta)-qubit_state(t-e,delta=delta))/(2*e)
            self.assertLess(np.linalg.norm(-1j*d+H@qubit_state(t,delta=delta)),1e-9)

    def test_two_sided_unitary_record_arrow_and_boundary_control(self):
        T=math.pi/2
        for t in (0,T/4,T/2,3*T/4,T):
            v=qubit_state(t);rho,_=reductions(v)
            S=binary_entropy(float(rho[1,1].real))
            self.assertAlmostEqual(S,binary_entropy(math.sin(t)**2),places=12)
            self.assertAlmostEqual(S,binary_entropy(math.sin(T-t)**2),places=12)
            self.assertAlmostEqual(np.vdot(v,v).real,1)
        self.assertAlmostEqual(binary_entropy(math.sin(T/2)**2),1)
        # Same H and scale-factor profile, different initial correlations.
        shift=math.pi/8
        left=binary_entropy(math.sin(T/4+shift)**2)
        right=binary_entropy(math.sin(3*T/4+shift)**2)
        self.assertAlmostEqual(left,1)
        self.assertAlmostEqual(right,0)

    def test_directional_derivative_is_chart_invariant(self):
        # On an overlap, dW/dt = (dW/dsigma+)(dsigma+/dt),
        # whether sigma+ increases or decreases along the same direction.
        for t in (1.7,2.,2.4,2.8):
            _,_,_,_,dp,dm=trajectory(t)
            if abs(dp*dm)<1e-9:continue
            dWdt=math.cos(t)*.7
            dWdm=dWdt/dm; dWdp=dWdm*dm/dp
            self.assertAlmostEqual(dWdp*dp,dWdt)

if __name__=='__main__':unittest.main()
