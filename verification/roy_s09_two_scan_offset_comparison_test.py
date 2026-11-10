#!/usr/bin/env python3
"""Synthetic regression for the difference-of-correlations grid."""
import json
import tempfile
from pathlib import Path
from roy_s09_two_scan_offset_comparison import compare


def main():
    with tempfile.TemporaryDirectory() as t:
        a=Path(t)/'a.json'; b=Path(t)/'b.json'
        def write(p,values):
            p.write_text(json.dumps({'all_candidates':[{'first_trigger_frame':i+1,'pearson_r':x} for i,x in enumerate(values)]}))
        write(a,[-1,0]);write(b,[0,1]);x=compare(a,b)
        assert x['independent_offset_grid']=={'count':4,'min':0.,'max':2.,'negative':0,'zero':1,'positive':3}
        assert x['same_offset_sensitivity_only']=={'count':2,'min':1.,'max':1.,'negative':0,'zero':0,'positive':2}
    print('PASS: Cartesian grid, sign counts and equal-offset sensitivity')


if __name__=='__main__':main()
