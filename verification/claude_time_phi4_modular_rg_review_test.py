"""Regulated Euclidean phi4 mode integration, and its configuration encoding.

The Euclidean configuration-encoding flow is not physical canonical field
flow; a separate test uses a finite physical canonical two-mode algebra.
"""
import unittest
import itertools
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.linalg import eigh, expm
from scipy.special import roots_hermitenorm, logsumexp

V=16
M2=.65
m2=.25
coupling=5.
slow=np.array([0.,1.2])
fast=np.array([-1.4,0.,1.4])

def S(x,y,lam=coupling):
    return .5*m2*x*x+.5*M2*y*y+lam/(24*V)*(x**4+6*x*x*y*y+y**4)

def prob(lam=coupling):
    energies=S(slow[:,None],fast[None,:],lam)
    logp=-energies-logsumexp(-energies)
    p=np.exp(logp);red=p.sum(axis=1);return energies,p,red

def matrices(p,red):
    # rho and its coarse marginal are diagonal in |x,y>.
    A=np.zeros((2,2),complex);A[1,0]=1
    full=np.kron(A,np.eye(len(fast)))
    def part(B):return np.einsum('ayby->ab',B.reshape(2,len(fast),2,len(fast)))
    sq=np.diag(np.sqrt(p.ravel()));inv=np.diag(1/np.sqrt(red))
    R=lambda B:inv@part(sq@B@sq)@inv
    def mod(p,B,s):
        U=np.diag(np.exp(1j*s*np.log(p.ravel())))
        return U@B@U.conj().T
    return A,full,R,mod

def exact_effective_coupling(lam, ys, weights):
    w=weights*np.exp(-lam*ys**4/(24*V));w/=w.sum()
    mean=np.dot(w,ys**2);var=np.dot(w,ys**4)-mean**2
    return lam-3*lam**2/(4*V)*var, var

def matrix_power_positive(rho, exponent):
    w,u=eigh(rho)
    return (u*w**exponent)@u.conj().T

def physical_quantum_model(d=4, lam=2., beta=.5):
    """Two spatial Fourier modes of a regulated 3+1 scalar Hamiltonian."""
    volume=8;omega0=.8;omega1=np.sqrt(1.64);identity=np.eye(d)
    def projected_powers(omega):
        # Extra levels before projection preserve P q^k P for k<=4.
        n=d+5;ann=np.diag(np.sqrt(np.arange(1,n)),1)
        pos=(ann+ann.T)/np.sqrt(2*omega)
        return [np.linalg.matrix_power(pos,k)[:d,:d] for k in (1,2,4)]
    x,x2,x4=projected_powers(omega0);_,y2,y4=projected_powers(omega1)
    h0=np.diag(omega0*(np.arange(d)+.5));h1=np.diag(omega1*(np.arange(d)+.5))
    H=np.kron(h0,identity)+np.kron(identity,h1)+lam/(24*volume)*(np.kron(x4,identity)+6*np.kron(x2,y2)+np.kron(identity,y4))
    w,u=eigh(H);weights=np.exp(-beta*(w-w.min()));rho=(u*(weights/weights.sum()))@u.conj().T
    part=lambda B:np.einsum('ayby->ab',B.reshape(d,d,d,d))
    red=part(rho);sq=matrix_power_positive(rho,.5);inv=matrix_power_positive(red,-.5)
    R=lambda B:inv@part(sq@B@sq)@inv
    logred=(lambda e: (e[1]*np.log(e[0]))@e[1].conj().T)(eigh(red))
    L=lambda h,B:-1j*(h@B-B@h)
    full=np.kron(x,identity)
    return H,rho,red,R,L,full,-logred,beta

class Phi4ModularRGTests(unittest.TestCase):
    def test_four_dimensional_lattice_action_and_mode_truncation(self):
        sites=np.array(np.meshgrid(*([np.arange(2)]*4),indexing='ij')).reshape(4,-1).T
        parity=(-1.)**sites[:,0];x,y=1.2,-.8
        phi=(x+y*parity)/np.sqrt(V)
        kinetic=sum(np.sum((phi-np.roll(phi.reshape((2,)*4),-1,axis=ax).ravel())**2) for ax in range(4))*.1/2
        direct=kinetic+.5*m2*np.dot(phi,phi)+coupling/24*np.sum(phi**4)
        self.assertAlmostEqual(direct,S(x,y),places=13)
        self.assertEqual(len(sites),V)

    def test_exact_shell_and_probability_marginal(self):
        E,p,red=prob();self.assertAlmostEqual(p.sum(),1.)
        effective=-logsumexp(-E,axis=1)
        np.testing.assert_allclose(red,np.exp(-effective-logsumexp(-effective)),atol=1e-14)
        E0,p0,r0=prob(0.); np.testing.assert_allclose(p0,np.outer(r0,p0.sum(axis=0)),atol=1e-14)

    def test_exact_shell_quartic_from_variance(self):
        # Differentiate the exact finite sum symbolically in an independent tiny grid.
        x,L=sp.symbols('x L',real=True);v=sp.Integer(16)
        ys=[sp.Integer(-1),sp.Integer(0),sp.Integer(1)]
        z=sum(sp.exp(-sp.Rational(1,2)*y*y-L*(x**4+6*x*x*y*y+y**4)/(24*v)) for y in ys)
        fourth=sp.diff(-sp.log(z),x,4).subs(x,0)
        weights=np.exp(-.5*np.array(ys,dtype=float)**2)
        for lam in (.1,1.,3.):
            expected,_=exact_effective_coupling(lam,np.array(ys,dtype=float),weights)
            self.assertAlmostEqual(float((v*fourth).subs(L,lam)),expected,places=12)

    def test_gaussian_limit_and_perturbative_coefficient(self):
        t,w=roots_hermitenorm(80);ys=t/np.sqrt(M2);w=w/np.sqrt(2*np.pi)
        _,variance=exact_effective_coupling(0,ys,w)
        self.assertAlmostEqual(variance,2/M2**2,places=12)
        target=3/(2*V*M2**2)
        errs=[]
        for lam in (.01,.005,.0025):
            effective,_=exact_effective_coupling(lam,ys,w.copy())
            errs.append(abs((lam-effective)/lam**2-target))
        self.assertLess(errs[-1],errs[-2]);self.assertLess(errs[-2],errs[-3]);self.assertLess(errs[-1],.003)

    def test_four_dimensional_shell_integral_and_sign(self):
        def integral(hi,lo,m):
            return quad(lambda p:p**3/(p*p+m*m)**2,lo,hi,epsabs=1e-12)[0]/(8*np.pi**2)
        for m in (0.,.2,1.):
            hi=3.;lo=1.3
            analytical=(np.log((hi**2+m*m)/(lo**2+m*m))+m*m/(hi**2+m*m)-m*m/(lo**2+m*m))/(16*np.pi**2)
            self.assertAlmostEqual(integral(hi,lo,m),analytical,places=13)
            if m==0:self.assertAlmostEqual(integral(hi,lo,m),np.log(hi/lo)/(8*np.pi**2),places=13)
        # In IR blocking l=log b the sign is the reverse of UV beta.
        lam=.3;dl=1e-5;shift=-1.5*lam**2*integral(1.,np.exp(-dl),0.)
        self.assertAlmostEqual(shift/dl,-3*lam**2/(16*np.pi**2),places=11)

    def test_configuration_embedding_and_cp_map(self):
        E,p,red=prob();A,full,R,mod=matrices(p,red)
        np.testing.assert_allclose(R(np.eye(6)),np.eye(2),atol=1e-14)
        rng=np.random.default_rng(85)
        for _ in range(5):
            B=rng.normal(size=(6,6))+1j*rng.normal(size=(6,6))
            self.assertAlmostEqual(np.trace(np.diag(p.ravel())@B),np.trace(np.diag(red)@R(B)),places=13)
            self.assertGreaterEqual(np.linalg.eigvalsh(R(B@B.conj().T)).min(),-1e-12)
        c=np.sqrt((p[1]/red[1])*(p[0]/red[0]));np.testing.assert_allclose(R(full),c.sum()*A,atol=1e-14)
        for s in (.3,2.,5.):
            result=R(mod(p,full,s))-mod(red,R(full),s)
            delta=E[1]-E[0];eff=-np.log(red[1])+np.log(red[0])
            coef=np.dot(c,np.exp(-1j*s*delta))-c.sum()*np.exp(-1j*s*eff)
            np.testing.assert_allclose(result,coef*A,atol=1e-13)
            self.assertAlmostEqual(np.linalg.norm(result,2),abs(coef),places=13)

    def test_no_exact_linear_reparameterization_or_natural_embedding(self):
        E,p,red=prob();delta=E[1]-E[0]
        self.assertAlmostEqual(delta[-1]-delta[1],coupling*slow[1]**2*fast[-1]**2/(4*V),places=13)
        c=np.sqrt((p[1]/red[1])*(p[0]/red[0]));c/=c.sum()
        mean=np.dot(c,delta);variance=np.dot(c,(delta-mean)**2)
        self.assertGreater(variance,0.) # Can't equal any single frequency for all s.
        A,full,R,mod=matrices(p,red)
        eff=-np.log(red[1])+np.log(red[0]);q=mean/eff
        for s in (1.,2.):
            self.assertGreater(np.linalg.norm(R(mod(p,full,s))-mod(red,R(full),q*s),2),1e-5)
            self.assertGreater(np.linalg.norm(mod(p,full,s)-np.kron(mod(red,A,q*s),np.eye(len(fast))),2),1e-4)

    def test_physical_canonical_scalar_coarse_map(self):
        # This uses the physical two-mode oscillator algebra, unlike the
        # Euclidean configuration encoding above. No continuum convergence claim.
        for d in (4,5):
            for lam in (0.,2.):
                H,rho,red,R,L,A,he,beta=physical_quantum_model(d,lam)
                np.testing.assert_allclose(R(np.eye(d*d)),np.eye(d),atol=1e-12)
                np.testing.assert_allclose(np.trace(red@R(A)),np.trace(rho@A),atol=1e-12)
                p=R(L(beta*H,A));q=L(he,R(A));defect=p-q
                qbest=np.vdot(q,p).real/np.vdot(q,q).real
                residual=np.linalg.norm(p-qbest*q)
                if lam==0.:
                    self.assertLess(np.linalg.norm(defect,2),1e-12)
                else:
                    self.assertGreater(np.linalg.norm(defect,2),1e-4)
                    self.assertGreater(residual,1e-4)
                if d==4 and lam==2.:
                    self.assertAlmostEqual(np.linalg.norm(defect,2),.0002060321797933,places=12)
                    # Direct finite modular flow derivative converges to the commutator.
                    def sigma(h,B,s):
                        U=expm(-1j*s*h);return U@B@U.conj().T
                    s=1e-4
                    finite=((R(sigma(beta*H,A,s))-sigma(he,R(A),s))
                            -(R(sigma(beta*H,A,-s))-sigma(he,R(A),-s)))/(2*s)
                    np.testing.assert_allclose(finite,defect,atol=1e-9)

    def test_shared_canonical_imaginary_time_boundary_channel(self):
        # Exact finite-d transfer kernel, no positivity/continuum assumption.
        d=2;n=3
        H,rho,red,_,_,_,_,beta=physical_quantum_model(d,2.)
        T=expm(-beta*H/n)
        boundary=np.zeros((d,d),complex)
        for x0,xn in itertools.product(range(d),repeat=2):
            for interior in itertools.product(range(d),repeat=n-1):
                xs=(x0,)+interior+(xn,)
                for ys in itertools.product(range(d),repeat=n):
                    loop=ys+(ys[0],)
                    term=1.+0j
                    for j in range(n):
                        term*=T[d*xs[j+1]+loop[j+1],d*xs[j]+loop[j]]
                    boundary[xn,x0]+=term
        unnorm=expm(-beta*H)
        expected=np.einsum('ayby->ab',unnorm.reshape(d,d,d,d))
        np.testing.assert_allclose(boundary,expected,atol=1e-14)
        np.testing.assert_allclose(boundary/np.trace(boundary),red,atol=1e-14)
        np.testing.assert_allclose(np.trace(unnorm),np.trace(boundary),atol=1e-14)

    def test_bounded_physical_observable_cutoff_diagnostic(self):
        values=[]
        for d in (4,6,8):
            H,rho,red,R,L,_,he,beta=physical_quantum_model(d,2.)
            x=np.zeros((d,d));x[0,1]=x[1,0]=1.
            self.assertAlmostEqual(np.linalg.norm(x,2),1.)
            A=np.kron(x,np.eye(d))
            defect=R(L(beta*H,A))-L(he,R(A))
            values.append(np.linalg.norm(defect,2))
        np.testing.assert_allclose(values,[.000290392827107,.000698592851743,.000718285345107],rtol=1e-8)
        # Three values provide a reproducible cutoff diagnostic, not a limit.

    def test_free_limit_exact(self):
        _,p,red=prob(0.);A,full,R,mod=matrices(p,red)
        for s in (.1,1.,10.):
            np.testing.assert_allclose(R(mod(p,full,s)),mod(red,R(full),s),atol=1e-14)
            np.testing.assert_allclose(mod(p,full,s),np.kron(mod(red,A,s),np.eye(len(fast))),atol=1e-14)

if __name__=='__main__':unittest.main()
