#!/usr/bin/env python3
"""Exact checks of a three-path weak-record criterion and monitoring control.

This is a known three-box algebra applied to a proposed record criterion,
not an experiment or proof about conscious observers.
"""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import json

# |psi>=(1,1,1)/sqrt(3), |phi>=(1,-1,1)/sqrt(3).
signs=(1,-1,1)
amp=[F(s,3) for s in signs]
overlap=sum(amp)
assert overlap==F(1,3)
weak=[a/overlap for a in amp]
assert weak==[1,-1,1]
assert (amp[0]+amp[1])/overlap==0
assert all(x!=0 for x in weak)
# Repeat each fixed projector at a second internal record position: P_i^2=P_i.
# With no/environment-free monitoring, compare actual strong instruments.
fine_joint=[a*a for a in amp]
fine_success=sum(fine_joint)
fine_cond=[p/fine_success for p in fine_joint]
coarse_joint=[(amp[0]+amp[1])**2,amp[2]**2]
coarse_success=sum(coarse_joint)
coarse_cond=[p/coarse_success for p in coarse_joint]
assert fine_success==F(1,3) and coarse_success==F(1,9)
assert fine_cond==[F(1,3)]*3 and coarse_cond==[0,1]
assert fine_cond[0]+fine_cond[1]==F(2,3)
# Offdiagonal of the postselected history decoherence functional.
D=[[a*b for b in amp] for a in amp]
assert D[0][1]==F(-1,9)
assert D[0][0]+D[1][1]+2*D[0][1]==0

# Partially distinguishable flags: Gram e0.e1=r; e2 orthogonal to both.
# Such a Gram matrix is PSD for 0<=r<=1 and is realized by unit flags.
for i in range(101):
    r=F(i,100)
    G=[[F(1),r,F(0)],[r,F(1),F(0)],[F(0),F(0),F(1)]]
    DR=[[amp[a]*amp[b]*G[a][b] for b in range(3)] for a in range(3)]
    grouped=DR[0][0]+DR[1][1]+2*DR[0][1]
    success=grouped+DR[2][2]
    assert grouped==2*(1-r)/9
    assert success==(3-2*r)/9
    conditional=grouped/success
    assert conditional==2*(1-r)/(3-2*r)
    assert F(2,3)-conditional==2*r/(3*(3-2*r))
    assert abs(DR[0][1])==r/9

# Transport labels, projectors and states together; same numbers in all six.
for perm in permutations(range(3)):
    ap=[amp[i] for i in perm]
    j=perm.index(0); k=perm.index(1)
    assert (ap[j]+ap[k])/sum(ap)==0
    assert sorted(a/sum(ap) for a in ap)==[-1,1,1]

# Perturb final state to phi_eta proportional to (1,-1+eta,1).
# Overall normalization cancels in the weak ratio and conditional probability.
eta=F(1,1000)
assert eta/(1+eta)==F(1,1001)
assert eta**2/(eta**2+1)==F(1,1000001)
# SWAP witness. Vectors are ordered |00>,|01>,|10>,|11> (M,E).
# |+0> and |0+> omit the common sqrt(2), which cancels in weak ratio.
pre=(F(1),F(0),F(1),F(0)); post=(F(1),F(1),F(0),F(0))
def swap(v): return (v[0],v[2],v[1],v[3])
def p_m0(v): return (v[0],v[1],F(0),F(0))
def p_m1(v): return (F(0),F(0),v[2],v[3])
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
swap_weak=dot(post,p_m0(swap(p_m1(pre))))/dot(post,swap(pre))
assert swap_weak==F(1,2)
# Controlled classical inputs become |00> and |01>: M is 0 in both,
# E perfectly distinguishes the inputs. They are different preparations.
assert swap((F(1),F(0),F(0),F(0)))==(1,0,0,0)
assert swap((F(0),F(0),F(1),F(0)))==(0,1,0,0)

# In a stationary qubit, sigma_z^3=sigma_z. Using the paper's displayed
# pre |+> and post |1>, normalization cancels from both weak ratios.
psi=(F(1),F(1)); phi=(F(0),F(1))
def inner(a,b): return sum((a[i]*b[i] for i in range(len(a))),F(0))
def apply(diag,v): return tuple(diag[i]*v[i] for i in range(len(v)))
def cube(v):
    for _ in range(3): v=apply((F(1),F(-1)),v)
    return v
z3=inner(phi,cube(psi))/inner(phi,psi)
up3=inner(phi,apply((F(1),F(0)),psi))/inner(phi,psi) # projector is idempotent
assert z3==-1 and up3==0

out={'status':'passed','weak_values_fine':[str(x) for x in weak],
     'coarse_01_weak_value':'0',
     'fine_measurement_success':str(fine_success),
     'coarse_measurement_success':str(coarse_success),
     'fine_conditional_group_01':'2/3','coarse_conditional_group_01':'0',
     'postselected_history_offdiagonal_01':str(D[0][1]),
     'environment_overlap_cases':101,'transported_label_permutations':6,
     'perturbation_eta':str(eta),'perturbed_coarse_weak':'1/1001',
     'perturbed_coarse_strong_probability':'1/1000001',
     'swap_overwrite_sequential_weak':str(swap_weak),
     'swap_control_memory_discrimination_tv':'0',
     'swap_control_environment_discrimination_tv':'1',
     'stationary_down_sigma_z_cubed_weak':'-1',
     'stationary_down_all_up_projector_weak':'0',
     'scope':'finite model; no observed memories, real observers, or experiential subject inference'}
text=json.dumps(out,indent=2)+'\n'
Path(__file__).with_suffix('.json').write_text(text)
print(text)
