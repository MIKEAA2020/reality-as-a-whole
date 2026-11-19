#!/usr/bin/env python3
"""A finite counterexample to automatic joint probabilities from symmetry.

The symmetrized two-operator expression and decoherence condition are known;
see Halliwell arXiv:0909.2597v1, sections I and IV. This 3D toy example is
not his complex-potential class operator or an example of WKB trajectories.
"""
from fractions import Fraction as F
from pathlib import Path
import json

n=3
def mat(rows): return [[F(v) for v in row] for row in rows]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(n)] for i in range(n)]
def scale(a,A): return [[a*v for v in row] for row in A]
def sub(A,B): return add(A,scale(-1,B))
def mul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def tr(A): return sum(A[i][i] for i in range(n))
def dagger(A): return [list(row) for row in zip(*A)] # all entries real

def eq(A,B): return A==B
I=mat([[1,0,0],[0,1,0],[0,0,1]])
H=mat([[0,0,0],[0,0,0],[0,0,1]])
P=mat([[1,0,0],[0,0,0],[0,0,0]])
Q=mat([[F(1,2),F(1,2),0],[F(1,2),F(1,2),0],[0,0,0]])
rho=mat([[F(1,10),-F(3,10),0],[-F(3,10),F(9,10),0],[0,0,0]])
assert eq(mul(P,P),P) and eq(mul(Q,Q),Q)
assert eq(mul(H,P),mul(P,H)) and eq(mul(H,Q),mul(Q,H))
assert mul(P,Q)!=mul(Q,P) and eq(mul(H,rho),mat([[0,0,0]]*3))
assert tr(rho)==1 and eq(mul(rho,rho),rho)
J=scale(F(1,2),add(mul(P,Q),mul(Q,P)))
C=[J,sub(P,J),sub(Q,J),add(sub(sub(I,P),Q),J)]
assert all(eq(c,dagger(c)) and eq(mul(H,c),mul(c,H)) for c in C)
assert eq(add(add(C[0],C[1]),add(C[2],C[3])),I)
def linear(c,r=rho): return tr(mul(c,r))
def D(a,b): return tr(mul(mul(a,rho),dagger(b)))
linear_weights=[linear(c) for c in C]
diagonal=[D(c,c) for c in C]
assert linear_weights==[F(-1,10),F(1,5),F(3,10),F(3,5)]
assert diagonal==[F(1,80),F(13,80),F(17,80),F(29,80)]
assert sum(diagonal)==F(3,4)
assert sum(D(a,b) for i,a in enumerate(C) for j,b in enumerate(C) if i!=j)==F(1,4)
assert D(C[0],C[1]) == F(-3,80)
# Depolarizing within the constrained sector: q=1/5 leaves J negative.
mixed=add(scale(F(4,5),rho),scale(F(1,10),sub(I,H)))
assert tr(mixed)==1 and linear(J,mixed)==F(-3,100)
# Sequential projective measurement of P followed by Q changes Q marginal.
Pbar=sub(I,P)
after_p=add(mul(mul(P,rho),P),mul(mul(Pbar,rho),Pbar))
assert tr(mul(Q,rho))==F(1,5) and tr(mul(Q,after_p))==F(1,2)
seq11=tr(mul(mul(mul(Q,P),rho),mul(P,Q)))
assert seq11==F(1,20)
# Commuting control: Q=P produces ordinary exclusive projectors, decoherence.
Cc=[P,sub(P,P),sub(P,P),sub(I,P)]
assert all(D(a,b)==0 for i,a in enumerate(Cc) for j,b in enumerate(Cc) if i!=j)
assert sum(D(c,c) for c in Cc)==1
result={'status':'passed','scope':'finite degenerate-constraint toy; not Halliwell complex-potential replay, WKB counterexample, subject assay, or complete quantum-gravity model',
 'constraint':'H=diag(0,0,1); physical state rho supported on zero eigenspace',
 'one_region_effects':'P=|0><0|, Q=|+><+| with |+>=(|0>+|1>)/sqrt(2)',
 'joint_candidate':'J=(PQ+QP)/2', 'physical_P_Q_noncommute':True,'all_four_class_operators_commute_with_constraint':True,'class_operators_sum_to_identity':True,
 'class_order':['11','10','01','00'],
 'linear_expectations':[str(x) for x in linear_weights],
 'branch_norm_weights':[str(x) for x in diagonal],
 'sum_branch_norms':str(sum(diagonal)),'sum_off_diagonal_interference': '1/4',
 'example_cross_decoherence_functional':'D(11,10)=-3/80',
 'linear_J_with_20_percent_physical_subspace_white_noise':'-3/100',
 'unmeasured_Q_marginal':'1/5','Q_marginal_after_unread_P_measurement':'1/2','sequential_P_yes_then_Q_yes':'1/20',
 'commuting_Q_equals_P_control_decoherent_and_normalized':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
