"""Gauge-quotient diffusion and record-dressed quantum kinetic operator.

Round geometry, a free kinetic operator and finite angular bins are model
inputs. The operator is not identified with the universe's physical energy.
"""
import numpy as np
from verification.zero_dressed_sphere_rotations import transport
from verification.zero_dressed_history_pair import to_anchor,from_anchor,encode_pair,decode_pair


def generator(n):
    """Finite-volume d/du[(1-u²)d/du] on n equal midpoint bins."""
    if n<2:raise ValueError('need at least two bins')
    h=2/n;edges=np.linspace(-1,1,n+1)
    q=np.zeros((n,n))
    for i in range(n-1):
        rate=(1-edges[i+1]**2)/h**2
        q[i,i]-=rate;q[i+1,i+1]-=rate
        q[i,i+1]+=rate;q[i+1,i]+=rate
    return q


def type_reflection(n):
    """Negative-half band reflection, identity on the positive half."""
    if n<4 or n%4:raise ValueError('requires a multiple of four')
    indices=list(range(n//2-1,-1,-1))+list(range(n//2,n))
    return np.eye(n)[indices]


def type_symmetric_generator(n):
    """Average free Q with its reflected conjugate; generally nonlocal."""
    q=generator(n);r=type_reflection(n)
    return (q+r@q@r.T)/2


def weighted_ground_operator(q,amplitude):
    """Positive -q + diag(q f/f), with prescribed positive ground f."""
    f=np.asarray(amplitude,dtype=float)
    if f.shape!=(len(q),) or np.any(f<=0):raise ValueError('positive amplitude required')
    return -q+np.diag((q@f)/f)


def bins4():return (-.75,-.25,.25,.75)


def move_pair_state(encoded,i,j,t,s,frames,shape):
    """W_j V_j V_i† W_i†, conjugated by actual old/R echo prefixes."""
    anchor={key:to_anchor(pair,t) for key,pair in encoded.items()}
    template=next(iter(anchor.values()))[0]
    source=decode_pair(anchor,i,s,template)
    angles=bins4()
    target=transport(source,frames,shape,angles[i],angles[j],s)
    return {key:from_anchor(pair,t) for key,pair in encode_pair(target,j,s).items()}


def dressed_operator(bins,t,s,frames,shape,operator=None):
    """Apply angular matrix to four constrained, encoded physical fibers.

    The full construction also tensors/conjugates by purified apparatus
    prefixes; this function acts on the explicit original old/R and pair
    vectors. Operator defaults to the positive free kinetic -Q_4.
    """
    if len(bins)!=4:raise ValueError('this implementation uses four bins')
    if operator is None:operator=-generator(4)
    if operator.shape!=(4,4):raise ValueError('expected 4 by 4 matrix')
    output=[]
    for i in range(4):
        acc={}
        for j in range(4):
            c=operator[i,j]
            if abs(c)<1e-15:continue
            transported=move_pair_state(bins[j],j,i,t,s,frames,shape)
            for key,pair in transported.items():
                if key not in acc:acc[key]=[0*pair[0],0*pair[1]]
                acc[key][0]+=c*pair[0];acc[key][1]+=c*pair[1]
        output.append({key:tuple(pair) for key,pair in acc.items()})
    return output
