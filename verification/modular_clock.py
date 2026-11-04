"""Exact algebraic checks for MODULAR_CLOCK_SELECTION.md.

The infinite Hardy-space and Fock-algebra arguments are analytic in the report.
This script verifies generator identities on exponential-polynomial functions,
finite modular cocycles, AKLT spectra and Weyl phases without floating point.
"""
from fractions import Fraction as F
from math import factorial
import json
from pathlib import Path
if __package__:
    from .infinite_coherence import gadd, gmul
    from .relational_records import mm
    from .relational_constraint import eye, transpose
else:
    from infinite_coherence import gadd, gmul
    from relational_records import mm
    from relational_constraint import eye, transpose


Z0 = (F(0), F(0))
ZI = (F(0), F(1))


def zreal(x):
    return F(x), F(0)


def zscale(x, z):
    return x*z[0], x*z[1]


def zconj(z):
    return z[0], -z[1]


def function(rate, polynomial):
    return rate, {k: z for k, z in polynomial.items() if z != Z0}


def linear(*terms):
    rate = terms[0][1][0]
    out = {}
    for c, f in terms:
        assert f[0] == rate
        for k, z in f[1].items():
            out[k] = gadd(out.get(k, Z0), gmul(c, z))
    return function(rate, out)


def translate(f, a):
    # exp(i a p) changes exp(-z p) to exp(-(z-i a)p).
    rate, poly = f
    return function((rate[0], rate[1]-a), poly)


def dilate(f, r):
    assert r > 0
    return function(zscale(r, f[0]), {k: zscale(r**k, z) for k, z in f[1].items()})


def momentum(f):
    return function(f[0], {k+1: z for k, z in f[1].items()})


def boost(f):
    # B=-i p d/dp on H=L2(R+,dp/p).
    rate, poly = f
    out = {}
    for k, z in poly.items():
        out[k] = gadd(out.get(k, Z0), gmul((F(0), F(-k)), z))
        out[k+1] = gadd(out.get(k+1, Z0), gmul(gmul(ZI, rate), z))
    return function(rate, out)


def kM(f):
    # log Delta_M/(2 pi) = -B.
    return linear((zreal(-1), boost(f)))


def kN(f, a):
    return translate(kM(translate(f, -a)), a)


def moment(f, power=0):
    # <f,p^power f> for f(p)=sum c_k p^k exp(-z p), measure dp/p.
    decay = 2*f[0][0]
    assert decay > 0
    out = Z0
    for j, cj in f[1].items():
        for k, ck in f[1].items():
            degree = j+k+power
            assert degree >= 1
            integral = F(factorial(degree-1), 1)/decay**degree
            out = gadd(out, zscale(integral, gmul(zconj(cj), ck)))
    assert out[1] == 0
    return out[0]


def weyl_multiply(left, right, sigma):
    phase, (a, b) = left
    other, (c, d) = right
    return phase+other-(a*d-b*c)*sigma/2, (a+c, b+d)


def weyl_word(letters, sigma):
    out = (F(0), (F(0), F(0)))
    for letter in letters:
        out = weyl_multiply(out, letter, sigma)
    return out


def run():
    operator_cases = 0
    for decay in (F(1), F(2), F(5, 3)):
        for m in (1, 2, 3):
            f = function(zreal(decay), {m: zreal(1), m+1: (F(1, 3), F(2, 5))})
            assert moment(f) > 0 and moment(f, power=1) > 0
            commutator = linear((zreal(1), boost(momentum(f))),
                                (zreal(-1), momentum(boost(f))))
            assert commutator == linear(((F(0), F(-1)), momentum(f)))
            for r in (F(1, 2), F(2), F(3)):
                assert moment(dilate(f, r)) == moment(f)
                assert moment(dilate(f, r), power=1) == moment(f, power=1)/r
                for a in (F(1), F(2, 3), F(3)):
                    assert dilate(translate(dilate(f, 1/r), a), r) == translate(f, r*a)
                    difference = linear((zreal(1), kN(f, a)), (zreal(-1), kM(f)))
                    assert difference == linear((zreal(a), momentum(f)))
                    assert moment(translate(f, a)) == moment(f)
                    operator_cases += 1
    spectra = []
    for n in range(2, 13):
        x = F(-1, 3)**n
        l0, l1 = (1+3*x)/4, (1-x)/4
        ratio = l0/l1
        assert l0 > 0 and l1 > 0 and l0+3*l1 == 1
        assert (ratio > 1) == (n % 2 == 0)
        # The analytic log bound uses 4/[(1+3x)(1-x)] <= 6 on |x|<=1/9.
        assert (1+3*x)*(1-x) >= F(2, 3)
        spectra.append({'block_sites': n, 'lambda_scalar': str(l0),
                        'lambda_other': str(l1), 'frequency': 'log('+str(ratio)+')',
                        'absolute_frequency_bound': str(6*F(1, 3)**n)})
    assert [row['frequency'] for row in spectra[:3]] == ['log(3/2)', 'log(6/7)', 'log(21/20)']
    # Finite reference-state dependence and the twisted, not ordinary, cocycle law.
    rho = [[F(2, 3), F(0)], [F(0), F(1, 3)]]
    R = [[F(3, 5), F(-4, 5)], [F(4, 5), F(3, 5)]]
    state_sigma = mm(mm(R, rho), transpose(R))
    Fop = [[F(-1), F(0)], [F(0), F(1)]]
    Gop = mm(mm(R, Fop), transpose(R))
    u = mm(Gop, Fop)
    assert mm(transpose(u), u) == eye(2)
    assert mm(u, u) != eye(2)
    assert mm(u, mm(mm(Fop, u), Fop)) == eye(2)  # u_(2t*) = I
    X = [[F(0), F(1)], [F(1), F(0)]]
    Z = [[F(1), F(0)], [F(0), F(-1)]]
    def expectation(state, A):
        q = mm(state, A)
        return q[0][0]+q[1][1]
    for A in (eye(2), X, Z, mm(X, Z)):
        evolved_rho = mm(mm(Fop, A), Fop)
        evolved_sigma = mm(mm(Gop, A), Gop)
        assert mm(mm(u, evolved_rho), transpose(u)) == evolved_sigma
        assert expectation(rho, evolved_rho) == expectation(rho, A)
        assert expectation(state_sigma, evolved_sigma) == expectation(state_sigma, A)
    assert expectation(state_sigma, X) == F(8, 25)
    assert expectation(state_sigma, mm(mm(Fop, X), Fop)) == F(-8, 25)
    # Real half-line smearing f_lambda=x exp(-lambda x), dilated g=r x exp(-lambda r x).
    phases = []
    for lam in (F(1), F(2), F(3, 2)):
        for r in (F(1, 2), F(1), F(2), F(3)):
            decay = lam*(1+r)
            integral = r*(F(factorial(1), 1)/decay**2
                          - lam*r*F(factorial(2), 1)/decay**3)
            sigma = r*(1-r)/(lam**2*(1+r)**3)
            assert integral == sigma
            assert sigma == -(1/r)*(1-1/r)/(lam**2*(1+1/r)**3)
            Wf, Wg = (F(0), (F(1), F(0))), (F(0), (F(0), F(1)))
            minus_f, minus_g = (F(0), (F(-1), F(0))), (F(0), (F(0), F(-1)))
            assert weyl_word((Wf, Wg, minus_f, minus_g), sigma) == (-sigma, (F(0), F(0)))
            phases.append({'lambda': str(lam), 'dilation_r': str(r), 'symplectic_phase': str(sigma)})
    assert next(p['symplectic_phase'] for p in phases if p['lambda']=='1' and p['dilation_r']=='2') == '-2/27'
    # Translation-smearing phase: remove the exact common exp(-lambda*a) factor.
    for lam in (F(1), F(2)):
        for a in (F(0), F(1), F(2, 3)):
            decay = 2*lam
            coefficient = (F(1)/decay**2 - 2*lam/decay**3
                           + a/decay - a*lam/decay**2)
            assert coefficient == a/(4*lam)
    return {
        'status': 'passed', 'arithmetic': 'rational and Gaussian rational; symbolic exponential functions',
        'core_generator_cases': operator_cases,
        'generator_recovery': '(log Delta_N - log Delta_M)/(2*pi*a) = positive translation P',
        'affine_covariance': 'D(s) T(a) D(-s) = T(exp(s)*a)',
        'aklt_supported_modular_frequencies': spectra,
        'finite_cocycle': {'test_time': 'pi/log(2)', 'ordinary_group_law': False,
                          'twisted_cocycle_law': True,
                          'fixed_sigma_state_X_before': '8/25',
                          'fixed_sigma_state_X_after_rho_flow': '-8/25'},
        'weyl_operational_phases': phases,
        'ramsey_record_formula': 'p_plus=(1+cos(symplectic_phase))/2',
        'analytic_not_numerical': ['standard real subspace and proper Hardy-strip inclusion',
                                   'Fock modular identification via standard CCR theorem',
                                   'half-sided modular inclusion and positive generator closure',
                                   'finite-dimensional obstruction and all-block frequency bound'],
        'not_derived': ['which state/localization pair is actual', 'unique physical clock or metric scale',
                        'complete AQFT net or gravitational time', 'phenomenal ownership or absolute necessity'],
    }


if __name__ == '__main__':
    result = run()
    target = Path(__file__).with_suffix('.json')
    target.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS: modular generators, finite cocycles, AKLT spectra and Weyl phases')
    print(target)
