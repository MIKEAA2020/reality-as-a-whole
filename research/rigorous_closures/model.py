"""Exact arithmetic checks for conditional closure results.
No phenomenality, observer identities, or actual-world measure is inferred.
"""
from fractions import Fraction as F


def boost(dt,dx,beta,gamma):
    dt,dx,beta,gamma=map(F,(dt,dx,beta,gamma))
    if abs(beta)>=1 or gamma<=0 or gamma*gamma*(1-beta*beta)!=1:raise ValueError('Consistent subluminal boost required; units c=1')
    return gamma*(dt-beta*dx),gamma*(dx-beta*dt)


def rod_length(proper_length,beta,gamma):
    proper_length=F(proper_length)
    if proper_length<=0:raise ValueError('Positive proper length required')
    dt_prime,length=boost(F(beta)*proper_length,proper_length,beta,gamma)
    assert dt_prime==0
    return length


def atoms_checked(atoms):
    result=[];seen=set()
    for uid,kind,weight,likelihood in atoms:
        if uid in seen:raise ValueError('Actual token identifiers must be unique; descriptions are not extra atoms')
        seen.add(uid);weight,likelihood=F(weight),F(likelihood)
        if weight<0 or not 0<=likelihood<=1:raise ValueError('Nonnegative weights and likelihoods in [0,1] required')
        result.append((uid,kind,weight,likelihood))
    return tuple(result)


def posterior(atoms,kind):
    atoms=atoms_checked(atoms);denominator=sum(w*l for _,_,w,l in atoms)
    if denominator<=0:raise ValueError('Positive evidence mass required')
    return sum(w*l for _,k,w,l in atoms if k==kind)/denominator


def refine(atoms,uid,proportions):
    atoms=atoms_checked(atoms);proportions=tuple(map(F,proportions))
    if not proportions or any(p<0 for p in proportions) or sum(proportions)!=1 or uid not in {a[0] for a in atoms}:raise ValueError('Known atom and weight-preserving refinement required')
    result=[]
    for key,kind,w,l in atoms:
        if key==uid:result.extend(((uid,'part',j),kind,w*p,l) for j,p in enumerate(proportions))
        else:result.append((key,kind,w,l))
    return atoms_checked(result)


def factor_map(organization,qualitative_assignment):
    """Existence of chi on organization classes iff assignment is constant there.
    These finite supplied assignments are not measured consciousness data.
    """
    if organization.keys()!=qualitative_assignment.keys():raise ValueError('Same realization domain required')
    out={}
    for token,kind in organization.items():
        value=qualitative_assignment[token]
        if kind in out and out[kind]!=value:raise ValueError('Assignment does not factor through organization')
        out[kind]=value
    return out
