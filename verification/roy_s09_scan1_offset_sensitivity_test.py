#!/usr/bin/env python3
"""Synthetic numerical checks for the illustrative offset sensitivity."""
import numpy as np
from roy_s09_scan1_offset_sensitivity import block_regressor, correlation


def main():
    t=np.arange(141)*2.2
    onsets=np.array([1.132,55.116,109.128,163.14,217.156])
    x=block_regressor(t,onsets)
    shifted=block_regressor(t,onsets+2.2)
    assert abs(correlation(x,x)-1)<1e-12
    assert correlation(x,shifted)<1
    try:
        correlation(x,np.ones_like(x))
    except ValueError:
        pass
    else:
        raise AssertionError('Constant regressors must fail')
    print('PASS: known-signal correlation, shift sensitivity, constant-series stop')


if __name__=='__main__':
    main()
