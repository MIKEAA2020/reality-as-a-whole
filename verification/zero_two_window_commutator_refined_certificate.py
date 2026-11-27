"""Exact-rational refinement of the two-window continuum certificate.

The rational Gram entries and uniform residual error are *reused* from the
original verifier, not independently recomputed. The overlap bound is new.
The analytic connection to the model is in the companion review.
"""
from fractions import Fraction as F
from math import factorial
from verification.zero_two_window_commutator_certificate import verify


def trig_enclosures_at_15():
    """Enclose sin(15), cos(15) using real Taylor's integral remainder."""
    x = 15
    sine = sum((F((-1)**k * x**(2*k+1), factorial(2*k+1))
                for k in range(40)), F(0))  # degree 79
    cosine = sum((F((-1)**k * x**(2*k), factorial(2*k))
                  for k in range(41)), F(0))  # degree 80
    # Derivatives of sin and cos have absolute value at most one on R.
    sine_err = F(x**80, factorial(80))
    cosine_err = F(x**81, factorial(81))
    return (sine, sine_err), (cosine, cosine_err)


def check():
    base = verify()
    (s, es), (c, ec) = trig_enclosures_at_15()
    # Integral 30*x^2*(1-x)^2 exp(30 i (x-1/2)) on [0,1].
    prefactor = F(120, 30**5)
    overlap_center = -prefactor * (888*s + 180*c)
    overlap_error = prefactor * (888*es + 180*ec)
    overlap_upper = abs(overlap_center) + overlap_error
    if not overlap_upper < F(11,5000):
        raise ArithmeticError('overlap bound')

    # The original bounds are strict; Euclidean norm beats |Re|+|Im|.
    re, im = F(834,10**6), F(671,10**6)
    cross = F(1071,10**6)
    if not re*re + im*im < cross*cross:
        raise ArithmeticError('Gram cross bound')
    eta = base['eta']
    residual_upper = F(168294,10**6) + cross + 4*eta + 2*eta**2
    comm_squared_upper = residual_upper / (1-F(11,5000))
    comm_upper = F(412,1000)
    if not comm_squared_upper < comm_upper**2:
        raise ArithmeticError('refined continuum commutator bound')

    amplitude = F(22,7)**2 * comm_upper / (16*F(6,5)*F(13,10))
    if not amplitude == F(12463,76440):
        raise ArithmeticError('amplitude arithmetic')
    if not amplitude**2 < F(266,10000):
        raise ArithmeticError('flag probability bound')
    return {'overlap_upper':overlap_upper, 'eta':eta,
            'comm_squared_upper':comm_squared_upper, 'comm_upper':comm_upper,
            'amplitude_upper':amplitude, 'probability_upper':amplitude**2}


if __name__ == '__main__':
    result = check()
    for key, value in result.items():
        print(f'{key}: {float(value):.15g}')
    print('REFINED: exact rational comparisons passed; inherited bounds remain conditional on the original verifier and its analytic proof.')
