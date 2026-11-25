"""State-family-adapted record dressings for independent sphere rotations.

The source-span isometries are numerically constructed from the actual 16
model vectors, not claimed to be fundamental spacetime or experiential
symmetries. They act on the original old carrier and echo R, with M control.
"""
import numpy as np
from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial,apply64
from verification.zero_internal_contextual_reference_test import ss
from verification.zero_persistent_sphere_subject_selection_test import norm2
from verification.zero_quantum_angular_echo import embed
from verification.zero_spherical_invariant_echo import angle

# Frame 0 = positive u / R+; 1 = lower negative band / R-, J+;
# 2 = upper negative band / R-, J-. Their physical sectors are orthogonal.


def build_frames():
    """Common orthonormal source-span frames for all 16 s=+ histories.

    The construction is conditional on equal Gram matrices. The old sources
    and the chosen span are inputs, not an external actuator or a universal
    symmetry on all possible physics. Returns numerical diagnostics as well.
    """
    root=output(active_base())
    first=initial(relative_read(root,4,labels=(0,))[0])
    shape=first.shape;d=first.size
    cols=[np.empty((d,16),dtype=complex) for _ in range(3)]
    for label in range(16):
        x=initial(relative_read(root,4,labels=(label,))[0])
        _,v,rows=embed(x,1,4)
        for matrix,vec in zip(cols,(rows[0][2],rows[1][0],rows[1][1])):
            n=norm2(vec)
            if n<=0:raise ValueError('zero source branch')
            matrix[:,label]=vec.reshape(-1)/np.sqrt(n)
    grams=[a.conj().T@a for a in cols]
    errors=[float(np.max(np.abs(g-grams[0]))) for g in grams]
    cross=float(np.max(np.abs(cols[1].conj().T@cols[2])))
    if max(errors)>1e-10 or cross>1e-10:
        raise ValueError('source-family Gram condition failed')
    eigenvalues,u=np.linalg.eigh(grams[0]);keep=eigenvalues>1e-10
    coeff=u[:,keep]/np.sqrt(eigenvalues[keep])
    frames=[matrix@coeff for matrix in cols]
    return shape,frames,{'gram_errors':errors,'cross_error':cross,
                         'eigenvalues':eigenvalues,'rank':int(sum(keep))}


def swap_frames(pair,frames,shape,band):
    """Swap the common frame between sector 0 and band 1 or 2, identity else."""
    if band not in (1,2):raise ValueError('invalid sector')
    left,right=pair
    e0,ej=frames[0],frames[band]
    c0=e0.conj().T@left.reshape(-1)
    cj=ej.conj().T@right.reshape(-1)
    dl=(e0@(cj-c0)).reshape(shape)
    dr=(ej@(c0-cj)).reshape(shape)
    return left+dl,right+dr


def sector(u):
    if not -1<u<1 or u in (-.5,0):raise ValueError('measure-zero boundary')
    return 1 if u<-.5 else 2 if u<0 else 0


def old_exchange(pair):return tuple(apply64(ss,x) for x in pair)


def v_sector(pair,frames,shape,band,s):
    """V_band^s; negative sign is the physical S-conjugate of positive."""
    if s not in (1,-1) or band not in (0,1,2):raise ValueError('invalid input')
    if band==0:return pair
    if s==1:return swap_frames(pair,frames,shape,band)
    return old_exchange(swap_frames(old_exchange(pair),frames,shape,band))


def transport(pair,frames,shape,u_from,u_to,s):
    """V(u_to)V(u_from)† on original complex old/R vectors."""
    pair=v_sector(pair,frames,shape,sector(u_from),s)
    return v_sector(pair,frames,shape,sector(u_to),s)


def dressed_pullback(wave,m,n,rm,rn,frames,shape,s):
    """Evaluate U_(rm,rn) wave at (m,n) for SO(3) matrices rm,rn.

    Pointwise representative only: sector boundaries and their rotated
    preimages are omitted, as appropriate for the L2 representation. Matrices
    must be rotations; the proof of unitarity uses area preservation.
    """
    m0=rm.T@m;n0=rn.T@n
    return transport(wave(m0,n0),frames,shape,angle(m0,n0),angle(m,n),s)
