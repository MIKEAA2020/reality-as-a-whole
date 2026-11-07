"""An actual two-cell CAR composite and its relative massless stress limit.

States are compressions of specified continuum conformal covariances, not Wilson
or Floquet ground states. Analytic cell-integral limits are in REPORT.md; smooth
relative-kernel quadrature and stable subtraction are used for diagnostics.
"""
import importlib.util
import math
from pathlib import Path

_root=Path(__file__).resolve().parents[1]
_spec=importlib.util.spec_from_file_location('relative_subtraction_reference',_root/'relative_subtraction'/'model.py')
relative=importlib.util.module_from_spec(_spec); _spec.loader.exec_module(relative)
_spec_car=importlib.util.spec_from_file_location('cell_car_reference',_root/'fermionic_lift'/'model.py')
car=importlib.util.module_from_spec(_spec_car); _spec_car.loader.exec_module(car)
previous=relative.previous


def parameters(a,n):
    if not math.isfinite(a) or a<=0 or not isinstance(n,int) or n<2 or n%2:
        raise ValueError('Positive cell width and even separation count n>=2 required')


def shape(n,terms=40):
    """h times the exact flat cell-averaged 1/s kernel, h=n*a."""
    parameters(1.,n)
    r=1/n
    return sum(2*r**(2*k)/((2*k+1)*(2*k+2)) for k in range(terms))


def flat_cell_kernel(a,n):
    parameters(a,n)
    return shape(n)/(n*a)


def relative_fermion_kernel(alpha,midpoint,separation):
    """sqrt(f'_+ f'_-)/(f_+-f_-)-1/s, stable through s=0."""
    f=relative.remainder(alpha,midpoint,separation)
    radicand=1+separation*separation*f
    if radicand<=0:
        raise ValueError('Positive conformal Jacobian required')
    return separation*f/(math.sqrt(radicand)+1)


def averaged_relative_kernel(alpha,u,a,n,steps=24):
    parameters(a,n)
    if not isinstance(steps,int) or steps<2:
        raise ValueError('At least two quadrature cells per direction required')
    h=n*a; out=0.
    for i in range(steps):
        xi=a*((i+.5)/steps-.5)
        for j in range(steps):
            eta=a*((j+.5)/steps-.5)
            midpoint=u+(xi+eta)/2; separation=h+xi-eta
            out+=relative_fermion_kernel(alpha,midpoint,separation)
    return out/(steps*steps)


def covariance_pair(alpha,u,a,n,steps=24):
    """Positive contraction exactly in the cell-integral definition (quadrature here)."""
    k0=flat_cell_kernel(a,n)
    delta=averaged_relative_kernel(alpha,u,a,n,steps)
    off=-1j*a*(k0+delta)/(2*math.pi)
    return ((.5+0j,off),(off.conjugate(),.5+0j))


def relative_stress(alpha,u,a,n,steps=24,calibrated=False):
    k0=flat_cell_kernel(a,n); delta=averaged_relative_kernel(alpha,u,a,n,steps)
    # Exact algebraic difference; do not subtract two large kernel squares.
    value=-(2*k0*delta+delta*delta)/(4*math.pi)
    return value/shape(n) if calibrated else value


def density_matrix(covariance):
    """Two-mode gauge-invariant quasifree density for diagonal occupations 1/2."""
    off=covariance[0][1]
    d=.25-abs(off)**2
    if abs(covariance[0][0]-.5)>1e-12 or abs(covariance[1][1]-.5)>1e-12 or d<0:
        raise ValueError('Supported positive half-filled two-mode covariance required')
    return {(0,0):complex(d),(3,3):complex(d),(1,1):complex(.5-d),(2,2):complex(.5-d),(1,2):complex(off),(2,1):complex(off).conjugate()}


def expectation(operator,density):
    return sum(value*density.get((j,i),0j) for (i,j),value in operator.items())


def current_product(a):
    parameters(a,2)
    identity=car.identity(4)
    j0=car.scale(1/a,car.add(car.number(2,0),car.scale(-.5,identity)))
    j1=car.scale(1/a,car.add(car.number(2,1),car.scale(-.5,identity)))
    return car.scale(math.pi,car.mul(j0,j1))


def covariance_eigenvalues(covariance):
    return .5-abs(covariance[0][1]),.5+abs(covariance[0][1])
