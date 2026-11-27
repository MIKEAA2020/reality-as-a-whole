"""Independent rational-polynomial recomputation of the two-window Gram matrix.

No functions or data from the original certificate are used to COMPUTE the
matrix. Polynomials have ordinary complex rational coefficients, rather than
the original certificate's special i^k representation. This checks the same
truncated model, not its analytic remainder or physical interpretation.
"""
from fractions import Fraction as F
from math import factorial, comb

ZERO = (F(0), F(0))
ONE = (F(1), F(0))


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def mul(a, b):
    return a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0]


def scale(a, x):
    return a[0]*x, a[1]*x


def poly_product(a, b):
    out = [ZERO for _ in range(len(a)+len(b)-1)]
    for j,x in enumerate(a):
        if x != ZERO:
            for k,y in enumerate(b):
                if y != ZERO:
                    out[j+k] = add(out[j+k],mul(x,y))
    return out


def ipower(n):
    return (ONE, (F(0),F(1)), (F(-1),F(0)), (F(0),F(-1)))[n % 4]


def pi_enclosure():
    # Reconstruct the Machin alternating-series bounds without original code.
    def ends(q, count):
        s = sum((F((-1)**j, (2*j+1)*q**(2*j+1))
                 for j in range(count)),F(0))
        next_term = F((-1)**count, (2*count+1)*q**(2*count+1))
        return min(s,s+next_term), max(s,s+next_term)
    al,ah = ends(5,24)
    bl,bh = ends(239,8)
    return 16*al-4*bh, 16*ah-4*bl


def pi_reciprocal_midpoint():
    lo,hi = pi_enclosure()
    return 2/(lo+hi)


def independent_remainder_bound():
    """New telescoping order for exact residual error, no original helpers."""
    lo,hi = pi_enclosure()
    if not F(3) < lo < hi < F(22,7):
        raise ArithmeticError('independent pi interval')
    # Packet and real-phase exponential integral Taylor remainders.
    ef = F(15,2)**41/factorial(41)
    ep = F(5**33,factorial(33))
    # Gaussian and sinc first omitted alternating terms on |d| <= 1.
    eg = F(1,2**13*factorial(13))
    es = F(2**27,factorial(27))
    # Different telescoping from the prior implementation: first change phase,
    # then Gaussian, then sinc; use |G|<=1, |S|<=2 and |P|<=1+error.
    reciprocal_error = 1/lo - 1/hi
    kernel_error = (2*ep + 2*(1+ep)*eg + (1+ep)*(1+eg)*es)/3
    kernel_error += reciprocal_error*(1+ep)*(1+eg)*(2+es)
    return 4*ef + F(18,5)*kernel_error*(1+ef)


def independent_overlap_bound():
    """Bound overlap via 15 = 5*pi - y, with 0<y<1 (not Taylor at 15)."""
    lo,hi = pi_enclosure()
    ylo,yhi = 5*lo-15,5*hi-15
    if not 0 < ylo < yhi < 1:
        raise ArithmeticError('argument reduction interval')
    # On [0,1], sin and cos Taylor terms alternate and decrease; 4 terms
    # provide lower bounds, 5 terms upper bounds. Both sin(y) and -cos(y)
    # increase there.  sin(15)=sin(y), cos(15)=-cos(y).
    def sin_partial(y,n):
        return sum(((-1)**j*y**(2*j+1)/factorial(2*j+1)
                    for j in range(n)),F(0))
    def cos_partial(y,n):
        return sum(((-1)**j*y**(2*j)/factorial(2*j)
                    for j in range(n)),F(0))
    lower = 888*sin_partial(ylo,4)-180*cos_partial(ylo,5)
    upper = 888*sin_partial(yhi,5)-180*cos_partial(yhi,4)
    if not 0 < lower <= upper:
        raise ArithmeticError('overlap sign interval')
    return F(120,30**5)*upper


def packet(phase):
    exponential = [scale(ipower(j),F((phase*15)**j,factorial(j)))
                   for j in range(41)]
    return poly_product([(F(1,4),F(0)), ZERO, (F(-1),F(0))],exponential)


def kernel(center, reciprocal_pi):
    # exp(-i a d), exp(-d^2/2), and sin(2d)/d, ordinary monomial basis.
    phase = [scale(ipower(j),F((-center)**j,factorial(j))) for j in range(33)]
    gauss = [ZERO for _ in range(25)]
    sinc = [ZERO for _ in range(25)]
    for j in range(13):
        gauss[2*j] = (F((-1)**j, 2**j*factorial(j)), F(0))
        sinc[2*j] = (F((-1)**j*2**(2*j+1), factorial(2*j+1)),F(0))
    return [scale(z,reciprocal_pi) for z in poly_product(poly_product(phase,gauss),sinc)]


def integral_monomial(n):
    if n % 2: return F(0)
    return F(1,(n+1)*2**n)


def action(kernel_coefficients, f):
    # Integrate sum_n c_n(t-s)^n f(s) by independently expanding each
    # binomial and ordinary polynomial moment in complex rational arithmetic.
    moments = []
    for j in range(len(kernel_coefficients)):
        v = ZERO
        for k,b in enumerate(f):
            if (j+k)%2 == 0:
                v = add(v,scale(b,integral_monomial(j+k)))
        moments.append(v)
    out = [ZERO for _ in kernel_coefficients]
    for n,c in enumerate(kernel_coefficients):
        if c == ZERO: continue
        for j in range(n+1):
            if moments[j] != ZERO:
                out[n-j] = add(out[n-j],scale(mul(c,moments[j]),(-1)**j*comb(n,j)))
    return out


def subtract(a,b):
    out = [ZERO for _ in range(max(len(a),len(b)))]
    for j in range(len(out)):
        aa = a[j] if j<len(a) else ZERO
        bb = b[j] if j<len(b) else ZERO
        out[j] = add(aa,scale(bb,-1))
    return out


def inner(a,b):
    value = ZERO
    for j,x in enumerate(a):
        if x == ZERO: continue
        conjugate = (x[0],-x[1])
        for k,y in enumerate(b):
            if y != ZERO and (j+k)%2 == 0:
                value = add(value,scale(mul(conjugate,y),integral_monomial(j+k)))
    return value


def compute_gram():
    inv_pi = pi_reciprocal_midpoint()
    fs = [packet(1),packet(-1)]
    kernels = {a:kernel(a,inv_pi) for a in (-5,0,5)}
    acted = {a:[action(kernels[a],f) for f in fs] for a in kernels}
    # T(t)-k = (t-13/2)^2/6 - 7046/1000.
    t = [(F(169,24)-F(7046,1000),F(0)),(F(-13,6),F(0)),(F(1,6),F(0))]
    residuals = [subtract(poly_product(t,fs[j]),acted[-5][j]) for j in (0,1)]

    def entry(i,j):
        value = inner(residuals[i],residuals[j])
        for a in (0,5):
            value = add(value,scale(inner(acted[a][i],acted[a][j]),F(169,200)))
        return scale(value,30)
    return [[entry(i,j) for j in (0,1)] for i in (0,1)]


def conditional_cursor_bounds():
    """Rational propagation of the bound into the existing cursor model.

    This does not independently prove the cursor's dispersive, pulse or
    finite-horizon comparison estimates; those are assumed from its report.
    """
    _,hi = pi_enclosure()
    pi_upper = F(3927,1250)  # 3.1416
    if not hi < pi_upper:
        raise ArithmeticError('pi upper bound for cursor')
    c = F(412,1000)/(2*F(13,10))
    end = pi_upper/200 + F(1,500000)  # g=100; (a+b)/v = 2e-6
    system_error = 400*c*end**2      # N*g/2 = 400
    pulse_error = pi_upper*800*F(1,10**6)
    dispersion_error = F(528,10**7)  # inherited strict bound 0.0000528
    blank_amplitude = F(1,10**31)   # inherited strict bound
    total = system_error+pulse_error+dispersion_error+blank_amplitude
    if not (total < F(1821,100000) and total**2 < F(332,10**6)):
        raise ArithmeticError('cursor probability bounds')
    return {'system_error':system_error,'pulse_error':pulse_error,
            'total_amplitude_upper':total,'probability_upper':total**2}


def certify():
    """Independently reproduce the refined threshold from stated premises."""
    g = compute_gram()
    eta = independent_remainder_bound()
    overlap = independent_overlap_bound()
    lo,hi = pi_enclosure()
    if not (0 < eta < F(1,10**11) and overlap < F(11,5000)
            and 4-F(36,5)/lo > F(169,100) and hi < F(22,7)):
        raise ArithmeticError('analytic bounds')
    if not (g[0][0][1] == g[1][1][1] == 0
            and 0 <= g[0][0][0] < F(168294,10**6)
            and 0 <= g[1][1][0] < F(168294,10**6)
            and g[1][0] == (g[0][1][0],-g[0][1][1])
            and g[0][1][0]**2+g[0][1][1]**2 < F(1071,10**6)**2):
        raise ArithmeticError('Gram bounds')
    squared=(F(168294,10**6)+F(1071,10**6)+4*eta+2*eta**2)/F(9978,10000)
    if not squared < F(412,1000)**2:
        raise ArithmeticError('commutator bound')
    amplitude = F(22,7)**2*F(412,1000)/(16*F(6,5)*F(13,10))
    if not (amplitude == F(12463,76440) and amplitude**2 < F(266,10000)):
        raise ArithmeticError('flag bound')
    return {'gram':g,'eta':eta,'overlap_upper':overlap,
            'comm_squared_upper':squared,'amplitude':amplitude}


if __name__ == '__main__':
    result = certify()
    for row in result['gram']:
        print([(float(re),float(im)) for re,im in row])
    for key in ('eta','overlap_upper','comm_squared_upper','amplitude'):
        print(f'{key}: {float(result[key]):.15g}')
    cursor=conditional_cursor_bounds()
    print(f"conditional cursor amplitude upper: {float(cursor['total_amplitude_upper']):.15g}")
    print(f"conditional cursor probability upper: {float(cursor['probability_upper']):.15g}")
    print('Independent rational-polynomial checks complete; see analytic assumptions in companion review.')
