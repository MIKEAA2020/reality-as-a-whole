"""Data/provenance audit of a pinned OKN supplementary demo.

Requires scipy (including numpy): python -m pip install scipy
Does not execute, translate, or reproduce the upstream MATLAB pipeline.
No subjective labels, neural data, or phenomenal identities are inferred.
"""
from pathlib import Path
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'sources/external/rivalry_okn'


def expanded_bad_mask(bad, radius):
    """Independent interval-union diagnostic in sample units, not a source port."""
    if type(radius) is not int or radius<0:
        raise ValueError('Nonnegative integer radius required')
    delta=[0]*(len(bad)+1)
    for i,is_bad in enumerate(bad):
        if is_bad:
            lo=max(0,i-radius)
            hi=min(len(bad),i+radius+1)
            delta[lo]+=1
            delta[hi]-=1
    active=0
    result=[]
    for d in delta[:-1]:
        active+=d
        result.append(active>0)
    return result


def intervals(mask):
    count=0
    prior=False
    for v in mask:
        if v and not prior:
            count+=1
        prior=v
    return count


def audit():
    import numpy as np
    from scipy.io import loadmat
    meta=json.loads((SOURCE/'provenance.json').read_text())
    for f in meta['files']:
        data=(SOURCE/f['path']).read_bytes()
        assert len(data)==f['bytes']
        assert hashlib.sha256(data).hexdigest()==f['sha256']
    d=loadmat(SOURCE/'demo.mat')
    keys=sorted(k for k in d if not k.startswith('__'))
    assert keys==['gx']
    gx=d['gx']
    assert gx.shape==(1,121021) and gx.dtype==np.float64
    x=gx.ravel()
    assert np.isfinite(x).all()
    bad=(x<0)|(x>1200)
    # Our own interval-union count, not a reproduction of removeOffscale.m.
    base=expanded_bad_mask(bad,0)
    expanded=expanded_bad_mask(bad,50)
    assert sum(base)==int(bad.sum())
    assert all(not b or e for b,e in zip(base,expanded))
    assert expanded_bad_mask([False,True,False,False],1)==[True,True,True,False]
    assert expanded_bad_mask([False]*4,50)==[False]*4
    try:
        expanded_bad_mask([False],-1)
    except ValueError:
        pass
    else:
        raise AssertionError('negative radius accepted')
    reversal=(SOURCE/'Functions/getReversals.m').read_text()
    spline=(SOURCE/'Functions/splineEMT.m').read_text()
    velocity=(SOURCE/'Functions/getVelocity.m').read_text()
    assert re.search(r'Percept\s*=\s*sign\(Switches\(:,2\)\+Switches\(:,3\)\)',reversal)
    assert 'randperm' in spline and "'pchip'" in spline
    assert '0.025,0.5,0.975' in velocity
    assert not re.search(r'\brng\s*\(',spline)
    return {
        'status':'passed',
        'commit':meta['commit'],
        'source_hashes_checked':len(meta['files']),
        'data_variables':keys,
        'gx_shape':list(gx.shape),
        'gx_dtype':str(gx.dtype),
        'samples':int(x.size),
        'finite_samples':int(np.isfinite(x).sum()),
        'minimum_position':float(x.min()),
        'maximum_position':float(x.max()),
        'README_sampling_rate_hz':1000,
        'timebase_in_mat_file':False,
        'nominal_first_to_last_span_seconds':(int(x.size)-1)/1000,
        'diagnostic_display_interval':[0,1200],
        'outside_interval_samples':int(bad.sum()),
        'outside_interval_runs':intervals(base),
        'independent_50_sample_expansion_union_count':sum(expanded),
        'Percept_is_algorithmic_output_not_demo_ground_truth':True,
        'source_uses_random_subsampling_pchip_and_velocity_quantiles':True,
        'local_rng_seed_found_in_spline_function':False,
        'independent_subjective_labels_in_demo':False,
        'stimulus_events_in_demo':False,
        'neural_recordings_in_demo':False,
        'MATLAB_pipeline_executed':False,
        'MATLAB_pipeline_reproduced':False,
        'source_modified':False,
        'phenomenal_identity_established':False,
        'subject_incidence_established':False,
        'scope':'source and demo-schema/data diagnostics only; not reproduction of paper findings',
    }


if __name__=='__main__':
    result=audit()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(f"PASS: {result['source_hashes_checked']} source hashes and {result['samples']} demo samples audited; no percept ground truth or identity inferred.")
