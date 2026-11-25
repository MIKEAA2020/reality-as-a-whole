"""Coherent finite-latitude dilation of the original 16-history echo.

The angular register is an additional, sector-controlled quantum resource.
At finite N=4m its uniform midpoint latitudes approximate du/2, rather than
being an exact continuous sphere. No subject or energy interpretation is used.
"""
from fractions import Fraction as F
from math import sqrt
from verification.zero_internal_contextual_reference_test import value_history
from verification.zero_dynamic_subject_memory_echo_test import jwrite
from verification.zero_internal_reference_subject_valence_candidates_test import b_project,j_project
from verification.zero_conserving_sphere_handedness_report_test import j_sign
from verification.zero_persistent_sphere_subject_selection_test import norm2
from verification.zero_sphere_angular_echo import magnitude


def latitudes(n):
    if n<4 or n%4:raise ValueError('n must be a positive multiple of four')
    return tuple(F(-1)+F(2*i+1,n) for i in range(n))


def reflect_index(i,n):
    latitudes(n)
    if not 0<=i<n:raise ValueError('invalid index')
    return n//2-1-i if i<n//2 else i


def embed(x,s,n):
    """Post-echo coherent R slices with an added angular register.

    Ancilla bins correlate with old B,J; branches are copies of physical
    state vectors at orthogonal angular labels, not classical hidden paths.
    x is one of the original valid source vectors, s is the M pointer sign.
    """
    if s not in (1,-1):raise ValueError('invalid sign')
    u=latitudes(n)
    v=(x+s*value_history(x))/2
    a,c=jwrite(v,0*v);a,c=value_history(a),value_history(c);a,c=jwrite(a,c)
    cp,cm=j_project(c,1),j_project(c,-1)
    zero=0*x
    plus=[a/sqrt(n//2) if i>=n//2 else zero for i in range(n)]
    minus=[cp/sqrt(n//4) if i<n//4 else cm/sqrt(n//4) if i<n//2 else zero
           for i in range(n)]
    return u,v,(plus,minus)


def embed_before_echo(x,s,n):
    """Prepare the same record coherently before T-Q-T (R initially ready)."""
    u=latitudes(n)
    if s not in (1,-1):raise ValueError('invalid sign')
    v=(x+s*value_history(x))/2
    plus=[]
    for i in range(n):
        b=1 if i>=n//2 else -1
        z=-1 if i<n//4 else 1
        count=n//2 if b==1 else n//4
        plus.append(j_project(b_project(v,b),z)/sqrt(count))
    return u,v,(plus,[0*x for _ in range(n)])


def pulse(rows,operation):
    """Apply an actual coherent T or Q to every angular-register slice."""
    a,c=rows
    if operation=='T':
        pairs=[jwrite(x,y) for x,y in zip(a,c)]
        return ([x for x,y in pairs],[y for x,y in pairs])
    if operation=='Q':return ([value_history(x) for x in a],[value_history(x) for x in c])
    raise ValueError('invalid pulse')


def apply_swap(rows,s):
    """D_lift: identity in R+, and s*Q plus angular reflection in R-."""
    plus,minus=rows;n=len(plus)
    return (list(plus),[s*value_history(minus[reflect_index(i,n)]) for i in range(n)])


def apply_quality(rows,s,kind,port):
    """Diagonal physical candidate signs times angular magnitude."""
    if port not in ('now','echo'):raise ValueError('invalid port')
    n=len(rows[0]);u=latitudes(n)
    return tuple([s*(1 if port=='now' else r)*float(magnitude(u[i],kind))*j_sign(x)
                  for i,x in enumerate(part)]
                 for r,part in zip((1,-1),rows))


def mass(rows):return sum(norm2(x) for part in rows for x in part)


def difference_mass(left,right):
    return sum(norm2(a-b) for part,other in zip(left,right) for a,b in zip(part,other))
