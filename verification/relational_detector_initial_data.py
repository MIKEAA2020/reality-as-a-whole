"""Check an action-based GR/clock/rod/detector initial-data expansion.

Exact rational polynomial arithmetic in c=cos(z). The separate analytic
implicit-function argument for exact small-amplitude initial data is in the
report; the code only verifies this numerical-parameter second-order case.
"""
from fractions import Fraction as F
from math import comb, cos, pi
import json
from pathlib import Path


def poly(*a):
    q=[F(x) for x in a]
    while q and q[-1]==0: q.pop()
    return tuple(q)
def add(*xs):
    n=max((len(x) for x in xs),default=0)
    return poly(*[sum((x[i] if i<len(x) else 0 for x in xs),F(0)) for i in range(n)])
def scale(x,v): return poly(*[a*F(v) for a in x])
def mul(x,y):
    a=[F(0)]*max(0,len(x)+len(y)-1)
    for i,p in enumerate(x):
        for j,q in enumerate(y): a[i+j]+=p*q
    return poly(*a)
def deriv(x): return poly(*[i*x[i] for i in range(1,len(x))])
def dzz(x):
    # d²/dz² P(cos z)=(1-c²)P''(c)-cP'(c).
    c=poly(0,1)
    return add(mul(poly(1,0,-1),deriv(deriv(x))),scale(mul(c,deriv(x)),-1))
def mean(x):
    return sum((v*F(comb(k,k//2),2**k) for k,v in enumerate(x) if k%2==0),F(0))

# A series pair is the coefficient at eps^0 and eps^2. No odd terms occur in
# the normalized Hamiltonian for the declared initial data.
def s_add(*xs): return (add(*[x[0] for x in xs]),add(*[x[1] for x in xs]))
def s_scale(x,v): return (scale(x[0],v),scale(x[1],v))
def s_mul(x,y): return (mul(x[0],y[0]),add(mul(x[0],y[1]),mul(x[1],y[0])))
def s_power(x,n):
    # Needed powers have constant term exactly one.
    assert x[0]==poly(1)
    return (poly(1),scale(x[1],n))

# f=1/2, tau=3/2, alpha0=1: alpha0²=f²+tau²/3.
f=F(1,2); tau=F(3,2); alpha0=F(1); p=F(1); b=F(2)
assert alpha0**2==f**2+tau**2/3
L=6*(f*f+tau*tau)
a=(3*p*p+b*b)/(12*alpha0)
c=poly(0,1); cos2=poly(-1,0,2); w=poly(1,1)
u=add(scale(c,p*p/(8+L)),scale(cos2,(p*p-b*b)/(4*(32+L))))
assert mean(u)==0
psi=(poly(1),u)
alpha=(poly(alpha0),poly(a))
pointer_source=(poly(),scale(mul(w,w),p*p/2))
signal_source=(poly(),scale(poly(1,0,-1),b*b/2))
# H/sqrt(g)= 8 psi^-5 psi'' -3 alpha²/2 +3 f² psi^-4/2
# + tau² psi^-12/2 + eps² p² w² psi^-12/2
# + eps² b² sin²z psi^-4/2 + O(eps^4) from the stabilizing potential.
Fconstraint=s_add(
    s_scale(s_mul(s_power(psi,-5),(poly(),dzz(u))),8),
    s_scale(s_mul(alpha,alpha),F(-3,2)),
    s_scale(s_power(psi,-4),3*f*f/2),
    s_scale(s_power(psi,-12),tau*tau/2),
    s_mul(pointer_source,s_power(psi,-12)),
    s_mul(signal_source,s_power(psi,-4)))
assert Fconstraint==(poly(),poly()),Fconstraint
source=add(pointer_source[1],signal_source[1])
assert mean(source)==F(7,4)
assert 3*alpha0*a==mean(source)
# Momentum constraint vanishes exactly on the declared initial slice:
# pi^ij=alpha sqrt(g) g^ij is covariantly constant as a weight-one density,
# while P_A partial_i A vanishes separately for all matter fields.
# The script verifies this algebraic form conceptually, not tensor derivatives.
# The leading interaction-induced relational acceleration coefficient is
# -lambda*epsilon*b*cos(z)*W/tau² for lapse 1, shift 0.
response=-b/tau**2
assert response==F(-8,9)
# Directly evaluate the full nonlinear constraint on the truncated ansatz,
# including kappa=1; halving epsilon should reduce the residual as eps^4.
def val(q,x): return sum(float(v)*x**i for i,v in enumerate(q))
def residual(e):
    errors=[]
    for i in range(512):
        x=cos(2*pi*i/512)
        ps=1+e*e*val(u,x)
        assert ps>0
        al=float(alpha0)+e*e*float(a)
        errors.append(abs(8*ps**-5*e*e*val(dzz(u),x)-1.5*al**2
            +1.5*float(f*f)*ps**-4+0.5*float(tau*tau)*ps**-12
            +e*e*float(p*p)/2*(1+x)**2*ps**-12
            +e*e*float(b*b)/2*(1-x*x)*ps**-4
            +e**4*float(b**4)*x**4))
    return max(errors)
r1,r2=residual(0.04),residual(0.02)
assert 14 < r1/r2 < 18,(r1,r2)
result={'status':'passed','f':str(f),'clock_momentum_tau':str(tau),'alpha0':str(alpha0),
        'pointer_momentum_amplitude_p':str(p),'signal_amplitude_b':str(b),
        'mean_matter_perturbation_energy':'7/4',
        'mean_curvature_momentum_correction_a':str(a),
        'psi_correction':'cos(z)/23 - 3 cos(2z)/188',
        'hamiltonian_coefficients_eps0_and_eps2':'0 pointwise',
        'relational_acceleration_coefficient_without_lambda_epsilon_W_cos':str(response),
        'full_constraint_residual_on_truncated_data':{'eps_0_04':r1,'eps_0_02':r2,'ratio':r1/r2,'samples':512,'kappa':1},
        'scope':'Second-order initial constraints and analytical leading response; not a quantum-record simulation.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
