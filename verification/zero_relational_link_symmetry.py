"""Frame-gauge resolution and meta-level controls for relational angle.

The link is a stipulated relative-frame transporter, not a derived physical
connection or a new propagating field. The invariant law on the orbit space is
not fixed by gauge invariance; these functions expose that distinction.
"""
import math
import numpy as np
from verification.zero_spherical_invariant_echo import unit,angle


def relational(m,n,link):
    return angle(m,np.asarray(link)@unit(n))


def gauge(m,n,link,a,b):
    """A,B independently change frame; L transports n's frame into m's."""
    return a@unit(m),b@unit(n),a@link@b.T


def triad(m,v):
    m=unit(m);v=unit(v);t=v-np.dot(m,v)*m
    if np.linalg.norm(t)<1e-12:
        basis=np.eye(3)[np.argmin(abs(m))]
        t=basis-np.dot(basis,m)*m
    t=unit(t)
    return np.column_stack((m,t,np.cross(m,t)))


def orbit_transport(x,y):
    """Find A,B taking x=(m,n,L) to y with equal relational cosine."""
    m,n,l=x;p,q,k=y
    if abs(relational(m,n,l)-relational(p,q,k))>1e-10:
        raise ValueError('different physical relational angle')
    a=triad(p,k@q)@triad(m,l@n).T
    b=k.T@a@l
    return a,b


def density(u,eps):
    if not -1<=u<=1 or not -1<eps<1:raise ValueError('invalid density')
    return 1+eps*math.cos(2*math.pi*u)


def inverse_flow(u,eps):
    """h = T^{-1}: pushes density(u) du/2 to uniform du/2."""
    density(u,eps)
    return u+eps*math.sin(2*math.pi*u)/(2*math.pi)


def forward_flow(v,eps):
    """Invert h by bisection; positive density makes h strictly increasing."""
    density(v,eps)
    lo=-1.;hi=1.
    for _ in range(60):
        mid=(lo+hi)/2
        if inverse_flow(mid,eps)<v:lo=mid
        else:hi=mid
    return (lo+hi)/2


def change_angle(m,n,target):
    """Preserve m and tangent azimuth while changing n's relative cosine."""
    m=unit(m);n=unit(n);u=angle(m,n)
    if abs(u)>=1-1e-13 or abs(target)>=1:raise ValueError('singular pole')
    return target*m+math.sqrt((1-target*target)/(1-u*u))*(n-u*m)


def conjugated_rotation(wave,m,n,a,b,eps):
    """T P_(a,b) T†, with T constant ↦ sqrt(density).

    T is a unitary induced by the radial diffeomorphism, including its
    Radon–Nikodym factor. The resulting action is not a bare rotation of n.
    """
    u=angle(m,n)
    nm=change_angle(m,n,inverse_flow(u,eps))
    p=a.T@unit(m);q=b.T@nm
    v=angle(p,q);target=forward_flow(v,eps)
    q2=change_angle(p,q,target)
    return math.sqrt(density(u,eps)/density(target,eps))*wave(p,q2)
