"""Compact-cell lattice embedding and region-preserving scaling diagnostics.

The comparison embedding is piecewise constant, NOT the earlier Fourier/sinc
embedding. Exact polynomial cell integrals avoid sampling tails. Analytic
continuum, vacuum and local-algebra arguments are in REPORT.md.
"""
from fractions import Fraction
import importlib.util
import math
from pathlib import Path

_spec=importlib.util.spec_from_file_location('spacetime_reference',Path(__file__).resolve().parents[1]/'spacetime_net'/'model.py')
net=importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(net)
w,car,vac=net.w,net.car,net.vac


def spacing(a):
    if not math.isfinite(a) or a<=0:
        raise ValueError('Positive finite cell width required')


def cell(j,a):
    spacing(a)
    if not isinstance(j,int):
        raise ValueError('Integer site required')
    return a*(j-.5),a*(j+.5)


def blob(x,radius=1.):
    if not math.isfinite(radius) or radius<=0:
        raise ValueError('Positive finite radius required')
    return (1-(x/radius)**2)**3 if abs(x)<radius else 0.


def blob_primitive(x,radius=1.):
    blob(0,radius)
    x=max(-radius,min(radius,x))
    return x-x**3/radius**2+3*x**5/(5*radius**4)-x**7/(7*radius**6)


def blob_integral(left,right,radius=1.):
    return blob_primitive(right,radius)-blob_primitive(left,radius)


def blob_norm_squared(radius=1.):
    blob(0,radius)
    return radius*float(sum(((-1)**r)*math.comb(6,r)*Fraction(2,2*r+1) for r in range(7)))


def blob_derivative_norm_squared(radius=1.):
    blob(0,radius)
    return 36/radius*float(sum(((-1)**r)*math.comb(4,r)*Fraction(2,2*r+3) for r in range(5)))


def cell_average_blob(a,radius=1.,spinor=(1,0),center=0.):
    """S_a f = a^(-1/2) integral over each cell, for f=b(x-center)*spinor."""
    spacing(a); blob(0,radius)
    if len(spinor)!=2:
        raise ValueError('Two spinor components required')
    out={}
    first=math.floor((center-radius)/a-.5)
    last=math.ceil((center+radius)/a+.5)
    for j in range(first,last+1):
        left,right=cell(j,a)
        if right<=center-radius or left>=center+radius:
            continue
        value=blob_integral(left-center,right-center,radius)/math.sqrt(a)
        if value!=0:
            out[j]=tuple(value*x for x in spinor)
    return out


def add_lattice(a,b):
    out=dict(a)
    for j,f in b.items():
        old=out.get(j,(0j,0j))
        out[j]=tuple(x+y for x,y in zip(old,f))
    return {j:f for j,f in out.items() if any(x!=0 for x in f)}


def scale_lattice(value,a):
    return {j:tuple(value*x for x in f) for j,f in a.items() if any(value*x!=0 for x in f)}


def evolve(a,mass,width,steps):
    if not isinstance(steps,int):
        raise ValueError('Integer time horizon required')
    if steps>=0:
        return w.real_evolve(a,mass,width,steps)
    return net.inverse_walk(a,mass,width,-steps)


def piecewise_inner(a,width_a,b,width_b):
    """Exact cell-intersection L2 inner product of J_a a and J_b b."""
    spacing(width_a); spacing(width_b)
    aa,bb=sorted(a),sorted(b)
    i=j=0; out=0j
    while i<len(aa) and j<len(bb):
        al,ar=cell(aa[i],width_a); bl,br=cell(bb[j],width_b)
        overlap=max(0,min(ar,br)-max(al,bl))
        out+=overlap/math.sqrt(width_a*width_b)*vac.inner(a[aa[i]],b[bb[j]])
        if ar<=br:
            i+=1
        else:
            j+=1
    return out


def piecewise_distance(a,width_a,b,width_b):
    return math.sqrt(max(0,w.norm_squared(a)+w.norm_squared(b)-2*piecewise_inner(a,width_a,b,width_b).real))


def projection_error(a,radius=1.,spinor=(1,0),center=0.):
    f=cell_average_blob(a,radius,spinor,center)
    norm2=blob_norm_squared(radius)*sum(abs(x)**2 for x in spinor)
    return math.sqrt(max(0,norm2-w.norm_squared(f)))


def massless_reference_error(amplitudes,a,time,radius,spinor):
    norm2=blob_norm_squared(radius)*sum(abs(x)**2 for x in spinor)
    inner=0j
    for j,f in amplitudes.items():
        left,right=cell(j,a)
        for r in range(2):
            shift=time if r==0 else -time
            inner+=complex(f[r]).conjugate()*spinor[r]*blob_integral(left-shift,right-shift,radius)/math.sqrt(a)
    return math.sqrt(max(0,w.norm_squared(amplitudes)+norm2-2*inner.real))


def local_spacetime_blob(a,mass,time_radius,space_radius,spinor=(1,0)):
    """a sum W^(-n) S_a F(na), F=b_time(t)*b_space(x)*spinor."""
    spacing(a); blob(0,time_radius)
    initial=cell_average_blob(a,space_radius,spinor)
    out={}; source_labels=[]
    for n in range(-math.ceil(time_radius/a),math.ceil(time_radius/a)+1):
        weight=a*blob(n*a,time_radius)
        if weight==0:
            continue
        source_labels.extend((n,j) for j in initial)
        out=add_lattice(out,scale_lattice(weight,evolve(initial,mass,a,-n)))
    return out,source_labels


def cell_in_diamond(n,j,a,radius,center=0.):
    left,right=cell(j,a)
    if radius<=0:
        raise ValueError('Positive diamond radius required')
    return abs(n*a)+max(abs(left-center),abs(right-center))<radius


def full_cells(a,left,right):
    spacing(a)
    if not left<right:
        raise ValueError('Nonempty interval required')
    return tuple(j for j in range(math.floor(left/a)-1,math.ceil(right/a)+2)
                 if left<cell(j,a)[0] and cell(j,a)[1]<right)


def periodic_embed(values,refinement):
    """Finite-circle analogue of the cell isometry; odd refinement aligns centers."""
    if not isinstance(refinement,int) or refinement<1 or refinement%2!=1:
        raise ValueError('Positive odd refinement required')
    n=len(values); out=[(0j,0j)]*(n*refinement)
    for j,f in enumerate(values):
        for d in range(-(refinement//2),refinement//2+1):
            out[(refinement*j+d)%len(out)]=tuple(x/math.sqrt(refinement) for x in f)
    return tuple(out)


def periodic_compress(values,refinement):
    if not isinstance(refinement,int) or refinement<1 or refinement%2!=1 or len(values)%refinement:
        raise ValueError('Compatible positive odd refinement required')
    return tuple(tuple(sum(values[(refinement*j+d)%len(values)][r] for d in range(-(refinement//2),refinement//2+1))/math.sqrt(refinement)
                       for r in range(2)) for j in range(len(values)//refinement))


def periodic_covariance_apply(values,mass,cell_width,walk_spacing):
    """Finite DFT check of the periodic-symbol covariance, not infinite volume."""
    import cmath
    spacing(cell_width); spacing(walk_spacing)
    n=len(values); transformed=[]
    for ell in range(n):
        f=tuple(sum(cmath.exp(-2j*math.pi*ell*j/n)*values[j][r] for j in range(n))/math.sqrt(n) for r in range(2))
        transformed.append(w.apply(vac.walk_covariance(2*math.pi*ell/(n*cell_width),mass,walk_spacing),f))
    return tuple(tuple(sum(cmath.exp(2j*math.pi*ell*j/n)*transformed[ell][r] for ell in range(n))/math.sqrt(n) for r in range(2)) for j in range(n))


def localize_to_interval(amplitudes,a,left,right):
    allowed=set(full_cells(a,left,right))
    return {j:f for j,f in amplitudes.items() if j in allowed}
