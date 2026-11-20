#!/usr/bin/env python3
"""Arithmetic checks of printed Bakas et al. statistics and Eq. 6, not a replay."""
from fractions import Fraction
from math import sqrt
import json, pathlib

def eye(n):return [[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
def mul(a,b):
 return [[sum((a[i][k]*b[k][j] for k in range(len(b))),Fraction()) for j in range(len(b[0]))] for i in range(len(a))]
def add_scaled(a,b,c):return [[a[i][j]+c*b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
def star():
 a=[[Fraction(0) for _ in range(14)] for _ in range(14)]
 # 6 lower rhythms at sensor 1 and 4 at sensor 2 -> gamma at sensor 2
 for i in [0,1,2,3,4,5,7,8,9,10]:a[i][13]=Fraction(1)
 return a

def run():
 a=star(); I=eye(14); zero=mul(a,a); assert all(not x for row in zero for x in row)
 direct=mul(add_scaled(I,a,Fraction(-1,10)),add_scaled(I,a,Fraction(-1,10)))
 # For A² = 0 the per-time inverse is exactly I + alpha*A.
 inverse=mul(add_scaled(I,a,Fraction(1,10)),add_scaled(I,a,Fraction(1,10)))
 receive=lambda p: sum((p[i][13] for i in range(14)),Fraction())
 return {'nodes':14,'edges_per_frame':10,'alpha':0.1,'frames':2,'A_squared_zero':True,
         'literal_product_target_receive_before_positive_normalization':float(receive(direct)),
         'directed_resolvent_target_receive_before_positive_normalization':float(receive(inverse)),
         'within_sensor_expected_residual_df':20*30*294-3,
         'across_sensor_expected_residual_df':20*30*4116-3,
         'combined_feature_counts_times_trials':20*30*(294+4116),
         'conventional_f_from_reported_within_F_df':sqrt(3.38*2/176397),
         'conventional_f_from_reported_cross_F_df':sqrt(10.04*2/2469597),
         'paired_dz_if_N_is_number_of_pairs':6.19/sqrt(2646000)}
if __name__=='__main__':
 r=run();p=pathlib.Path(__file__).with_suffix('.json');p.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
