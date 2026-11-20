#!/usr/bin/env python3
"""Unit tests for training-only linear and film-conditioned fits."""
from eeg_baseline_deviation_valence_gate import fit

def close(a,b): assert abs(a-b)<1e-12, (a,b)

# y = 2 + 3*x; a held-out label must not enter the predictor.
train=[{'s':0,'c':0,'y':2.,'deviation':0.}, {'s':1,'c':0,'y':5.,'deviation':1.},
       {'s':0,'c':1,'y':8.,'deviation':2.}, {'s':1,'c':1,'y':11.,'deviation':3.}]
held={'s':2,'c':0,'y':999.,'deviation':4.}
close(fit(train,'deviation',False)(held),14.)
close(fit(list(reversed(train)),'deviation',False)(held),14.)
close(fit(train,None,False)(held),6.5)
# Film means absorb different offsets; common slope is 2.
train=[{'c':0,'y':1.,'deviation':0.},{'c':0,'y':3.,'deviation':1.},
       {'c':1,'y':11.,'deviation':0.},{'c':1,'y':13.,'deviation':1.}]
close(fit(train,'deviation',True)({'c':1,'deviation':2.,'y':-999.}),15.)
close(fit(train,None,True)({'c':1,'y':-999.}),12.)
constant=[{'c':0,'y':1.,'deviation':2.},{'c':0,'y':5.,'deviation':2.}]
close(fit(constant,'deviation',False)({'deviation':100.}),3.)
close(fit(constant,'deviation',True)({'c':0,'deviation':100.}),3.)
print('Training-only OLS, film intercept and zero-variance checks passed.')
