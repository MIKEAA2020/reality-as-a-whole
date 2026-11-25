"""Continuous angular extension of the existing reduced sphere echo.

This is a new stipulated probability/record coupling, not a derivation of
an actual sphere or full quantum-state equivalence. On each internal sphere,
u=n·m has uniform density 1/2 on [-1,1]. An independent direction supplies a
symmetric sign s. The 20-tick action is the existing reduced echo action.
"""
from collections import defaultdict
from fractions import Fraction as F
from verification.zero_stationary_battery_bridge import PREFIX, SIGNS, TICKS

# Positive measure open bands; endpoints are measure-zero and deliberately
# excluded from sample-based operations. m, n, k are additional structure.
BANDS=((F(-1),F(-1,2),-1,-1),
       (F(-1,2),F(0),-1,1),
       (F(0),F(1),1,1))


def initial(u,s):
    if not (-1<u<1) or u in (F(-1,2),F(0)) or s not in SIGNS:
        raise ValueError('u must be an interior point away from boundaries; s a sign')
    b=1 if u>0 else -1
    z=1 if u>F(-1,2) else -1
    return b,z,1,s


def state(t,u,s):
    if not 0<=t<=TICKS:raise ValueError('invalid tick')
    return PREFIX[t][initial(u,s)]


def angular_swap(u):
    """Equal-area reflection of the negative hemisphere; fixed positive side."""
    if not (-1<u<1) or u in (F(-1,2),F(0)):
        raise ValueError('u on excluded measure-zero boundary')
    return -1-u if u<0 else u


def magnitude(u,kind):
    if not -1<=u<=1:raise ValueError('u outside sphere')
    if kind=='absolute':return abs(u)
    if kind=='swap_invariant':return abs(u*(u+1))
    raise ValueError('unknown magnitude')


def quality(t,u,s,kind,port):
    b,j,r,s=state(t,u,s)
    if port=='now':return s*j*magnitude(u,kind)
    if port=='echo':return s*j*r*magnitude(u,kind)
    raise ValueError('unknown port')


def band_mass(a,b):return (b-a)/2


def band_magnitude_integral(a,b,kind):
    """Exact integral (1/2) int_a^b g(u)du, band cannot cross zero."""
    if not -1<=a<b<=1 or a<0<b:raise ValueError('invalid band')
    if kind=='absolute':
        ant=lambda x:x*x/2
    elif kind=='swap_invariant':
        ant=lambda x:x*x*x/3+x*x/2
    else:raise ValueError('unknown magnitude')
    return (ant(b)-ant(a))*(1 if a>=0 else -1)/2


def coarse_tick(t):
    """Exact probability over old reduced signs at one relational tick."""
    if not 0<=t<=TICKS:raise ValueError('invalid tick')
    out=defaultdict(F)
    for a,c,b,z in BANDS:
        for s in SIGNS:out[PREFIX[t][b,z,1,s]]+=band_mass(a,c)/2
    return dict(out)


def magnitude_moments(kind):
    return {(b,z):(band_mass(a,c),band_magnitude_integral(a,c,kind))
            for a,c,b,z in BANDS}


def reference_disagreement(q,ref,kind):
    """Exact P(D|R), and E[g(u) 1_D | R], under old clock protocol."""
    if q not in (1,2) or ref not in range(4):raise ValueError('invalid clock')
    ticks=[t for t in range(TICKS) if q*t%4==ref]
    if not ticks:raise ValueError('zero-probability reference event')
    mass=F(0);moment=F(0)
    for t in ticks:
        for a,c,b,z in BANDS:
            for s in SIGNS:
                _,j,r,_=PREFIX[t][b,z,1,s]
                if r==-1:
                    mass+=band_mass(a,c)/(2*len(ticks))
                    moment+=band_magnitude_integral(a,c,kind)/(2*len(ticks))
    return mass,moment
