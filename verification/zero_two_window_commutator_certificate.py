"""Exact-rational certificate for the continuum support commutator.

No numerical quadrature, floating-point arithmetic, NumPy, or external
packages enter verify().  See the companion report for the operator proof,
series remainder inequalities, and the scope of the certificate.
"""
from fractions import Fraction as F
import math

Z=F(0); ONE=F(1)


def sign(k):
    return -1 if k % 2 else 1


def atan_interval(inverse, n):
    """Exact alternating bounds for arctan(1/inverse), inverse > 1."""
    partial=sum((F(sign(k),(2*k+1)*inverse**(2*k+1)) for k in range(n)),Z)
    following=F(sign(n),(2*n+1)*inverse**(2*n+1))
    return min(partial,partial+following), max(partial,partial+following)


def pi_interval():
    # Machin: pi=16 atan(1/5)-4 atan(1/239).
    a,b=atan_interval(5,24); c,d=atan_interval(239,8)
    return 16*a-4*d,16*b-4*c


def multiply(a,b):
    out=[Z]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:out[i+j]+=x*y
    return out


def packet(sign_of_phase):
    """Polynomial coefficients a_k in g(t) exp(±15it) = sum i^k a_k t^k.

    g(t)=1/4-t²; sqrt(30) normalization is applied to inner products.
    """
    expansion=[ONE]
    for k in range(1,41): expansion.append(expansion[-1]*sign_of_phase*15/k)
    out=[Z]*43
    for k,x in enumerate(expansion):
        out[k]+=x/4
        out[k+2]+=x  # -t² changes i^(k+2) by a minus sign
    return out


def kernel(center, inverse_pi):
    """Rational coefficients of the truncated kernel as sum i^k a_k d^k."""
    phase=[ONE]
    for k in range(1,33): phase.append(phase[-1]*(-center)/k)
    gaussian=[Z]*25; sinc=[Z]*25
    for j in range(13):
        gaussian[2*j]=F(1,2**j*math.factorial(j))
        sinc[2*j]=F(2**(2*j+1),math.factorial(2*j+1))
    return [x*inverse_pi for x in multiply(multiply(phase,gaussian),sinc)]


def integrated_power(k):
    return F(1,(k+1)*2**k) if k%2==0 else Z


def moments(f,n):
    """Return m_j for integral s^j f(s) ds = i^j m_j."""
    result=[]
    for j in range(n):
        val=Z
        for k,x in enumerate(f):
            if (k+j)%2==0: val+=x*sign((k-j)//2)*integrated_power(k+j)
        result.append(val)
    return result


def apply_kernel(coeff,f):
    """Analytically integrate the polynomial kernel over [-1/2,1/2]."""
    moment=moments(f,len(coeff));out=[Z]*len(coeff)
    for n,a in enumerate(coeff):
        if a:
            for j in range(n+1):
                if moment[j]:out[n-j]+=a*math.comb(n,j)*moment[j]
    return out


def residual(f,e):
    """(p²/6 - 7.046) f - E_-5 f as real/imag coefficients of i^k t^k."""
    size=max(len(f)+2,len(e));real=[Z]*size;imag=[Z]*size
    t0=F(169,24)-F(7046,1000);t1=F(-13,6);t2=F(1,6)
    for j,x in enumerate(f):
        real[j]+=t0*x
        imag[j+1]-=t1*x
        real[j+2]-=t2*x
    for j,x in enumerate(e):real[j]-=x
    return real,imag


def inner(a,b):
    """Exact integral of conjugate(a)*b; a and b are rational coefficient pairs."""
    ar,ai=a;br,bi=b;real=Z;imag=Z
    for i,(u,v) in enumerate(zip(ar,ai)):
        for j,(x,y) in enumerate(zip(br,bi)):
            if (i+j)%2==0:
                f=integrated_power(i+j)*sign((j-i)//2)
                real+=(u*x+v*y)*f
                imag+=(u*y-v*x)*f
    return real,imag


def as_real(a):return a,[Z]*len(a)
def scale(a,s):return a[0]*s,a[1]*s
def add(a,b):return a[0]+b[0],a[1]+b[1]


def verify():
    """Return exact bounds, or raise ArithmeticError if a certificate check fails."""
    lo,hi=pi_interval()
    if not F(314,100)<lo<hi<F(22,7):raise ArithmeticError('pi enclosure')
    if not 4-F(36,5)/lo>F(169,100):raise ArithmeticError('positive root bound')
    inverse_pi=1/((lo+hi)/2)
    inverse_pi_error=1/lo-1/hi
    ps=[packet(1),packet(-1)]
    kernels={a:kernel(a,inverse_pi) for a in (-5,0,5)}
    acted={a:[apply_kernel(k,f) for f in ps] for a,k in kernels.items()}
    res=[residual(ps[j],acted[-5][j]) for j in (0,1)]

    def gram(i,j):
        z=inner(res[i],res[j])
        for a in (0,5):
            z=add(z,scale(inner(as_real(acted[a][i]),as_real(acted[a][j])),F(169,200)))
        return scale(z,30)

    d0=gram(0,0);d1=gram(1,1);cross=gram(0,1)
    if not (d0[1]==d1[1]==0 and 0<=d0[0]<F(168294,10**6)
            and 0<=d1[0]<F(168294,10**6)
            and abs(cross[0])<F(834,10**6) and abs(cross[1])<F(671,10**6)):
        raise ArithmeticError('rational residual Gram bounds')

    # Alternating / real-phase Taylor remainders, uniform on the full band.
    ef=F(15,2)**41/math.factorial(41)
    eg=F(1,2**13*math.factorial(13))
    es=F(2**27,math.factorial(27))
    ep=F(5**33,math.factorial(33))
    ek=(2*eg+(1+eg)*es+(1+eg)*(2+es)*ep)/3
    ek+=inverse_pi_error*(1+eg)*(2+es)*(1+ep)
    # ||Theta-7.046||<4 and the three interaction coefficients sum to 3.6.
    eta=4*ef+F(18,5)*ek*(1+ef)
    if not eta<F(1,10**11):raise ArithmeticError('uniform series remainder')

    # Integration by parts twice and Cauchy--Schwarz give overlap <=sqrt(720)/900 < .03.
    if not F(720)<(900*F(3,100))**2:raise ArithmeticError('packet overlap threshold')
    diag=F(168294,10**6);re=F(834,10**6);im=F(671,10**6)
    squared=(diag+re+im+4*eta+2*eta**2)/F(97,100)
    comm=F(419,1000)
    if not squared<comm**2:raise ArithmeticError('commutator threshold')

    # a_1=sqrt(4-7.2/pi)>13/10, pi<22/7, and g=6/5.
    amplitude=(F(22,7)**2*comm)/(16*F(6,5)*F(13,10))
    if not amplitude**2<F(28,1000):raise ArithmeticError('uniform error threshold')
    return {'pi_lo':lo,'pi_hi':hi,'diag0':d0[0],'diag1':d1[0],
            'cross_re':cross[0],'cross_im':cross[1],'eta':eta,
            'commutator_squared_upper':squared,'commutator_upper':comm,
            'flag_amplitude_upper':amplitude,'flag_error_upper':amplitude**2}


if __name__=='__main__':
    c=verify()
    for name in ('diag0','diag1','cross_re','cross_im','eta',
                 'commutator_squared_upper','commutator_upper',
                 'flag_amplitude_upper','flag_error_upper'):
        print(f'{name}: {float(c[name]):.15g}')
    print('CERTIFIED: exact rational checks completed; see companion proof.')
