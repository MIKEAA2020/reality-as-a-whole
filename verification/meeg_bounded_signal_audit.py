#!/usr/bin/env python3
"""Bounded public archive prefix, exact pinned preprocessing methods, no pickle execution."""
import ast
import hashlib
import json
import math
import sys
import zlib
from pathlib import Path

import numpy as np
import scipy
from scipy import signal

PREFIX = Path('.arena/meeg/sample1-prefix.gz')
SOURCE = Path('.arena/meeg/train/prepare_data.py')
OUT = Path('verification/meeg_bounded_signal_audit.json')
PREFIX_SHA = '41746450387a6ab7e940228753b8c991c458b11ae114300f22c02618e6f40aab'
SOURCE_SHA = '805b808534184465dc79bc6b3a85e8aba039273a44731fb629752aa77eb58984'
PICKLE_HEADER_SHA = '06423fdc016f4462844027001365ed07e2feb73a9573e978eb9caf5be83fb102'
N = 59900
FS = 1000


def sha(b): return hashlib.sha256(b).hexdigest()


def tar_member_prefix(buf, target):
    pos=0
    while pos + 512 <= len(buf):
        h=buf[pos:pos+512]
        name=h[:100].split(b'\0')[0].decode('utf-8')
        size=int(h[124:136].strip(b'\0 ') or b'0',8)
        begin=pos+512
        if name==target: return size,buf[begin:min(begin+size,len(buf))]
        pos=begin+((size+511)//512)*512
    raise ValueError('target member not present in prefix')


def first_channel_from_prefix(raw):
    if sha(raw)!=PREFIX_SHA: raise ValueError('compressed prefix differs from pinned bytes')
    decomp=zlib.decompressobj(16+zlib.MAX_WBITS)
    data=decomp.decompress(raw,2_000_000)
    size,member=tar_member_prefix(data,'sample_1.dat')
    if size!=306688410 or len(member)<160+8*N: raise ValueError('unexpected member size or insufficient prefix')
    if sha(member[:160])!=PICKLE_HEADER_SHA: raise ValueError('pickle/array header differs from pinned prefix')
    if member[155]!=0x42 or int.from_bytes(member[156:160], 'little')!=20*32*N*8:
        raise ValueError('unexpected ndarray payload framing')
    b=member[160:160+8*N]
    x=np.frombuffer(b,dtype='<f8').copy()
    if len(x)!=N or not np.isfinite(x).all(): raise ValueError('nonfinite/incomplete samples')
    return x,sha(b)


def upstream_methods(source):
    if sha(source)!=SOURCE_SHA: raise ValueError('upstream source mismatch')
    tree=ast.parse(source)
    cls=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=='PrepareData')
    names={'bandpass_filter','notch_filter','notch_filter_per_channel'}
    methods=[n for n in cls.body if isinstance(n,ast.FunctionDef) and n.name in names]
    if {m.name for m in methods}!=names: raise ValueError('unexpected source schema')
    node=ast.ClassDef(name='BoundedUpstreamMethods',bases=[],keywords=[],body=methods,decorator_list=[])
    env={'signal':signal}
    exec(compile(ast.fix_missing_locations(ast.Module(body=[node],type_ignores=[])),'pinned_source','exec'),env)
    return env['BoundedUpstreamMethods']()


def local_power(x, frequency):
    f,p=signal.welch(x,fs=FS,nperseg=4000,detrend='constant')
    return float(p[np.argmin(abs(f-frequency))])


def ratio(x,y,f):
    before=local_power(x,f); after=local_power(y,f)
    return after/before if before>0 else None


def trial_split_witness():
    # Outer test: one complete trial; remaining inner folds split flattened segments.
    rows=[(trial,seg) for trial in range(4) for seg in range(4)]
    outer_train=[r for r in rows if r[0]!=3]
    outer_test=[r for r in rows if r[0]==3]
    inner_val=[r for i,r in enumerate(outer_train) if i%3==0]
    inner_train=[r for i,r in enumerate(outer_train) if i%3!=0]
    overlap=sorted({r[0] for r in inner_train}&{r[0] for r in inner_val})
    assert not ({r[0] for r in outer_train}&{r[0] for r in outer_test})
    assert overlap==[0,1,2]
    return {'outer_training_trials':3,'outer_test_trials':1,
            'outer_trial_overlap':0,'inner_trial_overlap':len(overlap),
            'note':'synthetic split witness; not the actual paper folds'}


def main():
    x, sample_sha=first_channel_from_prefix(PREFIX.read_bytes())
    upstream=upstream_methods(SOURCE.read_bytes())
    t=np.arange(10000)/FS
    synthetic=np.sin(2*np.pi*25*t)+np.sin(2*np.pi*50*t)
    def examine(x):
        input3d=x[np.newaxis,np.newaxis,:].copy()
        result=upstream.notch_filter(input3d,fs=FS,Q=50)
        standalone=upstream.notch_filter_per_channel(x.copy(),fs=FS,Q=50)
        b,a=signal.iirnotch(50,50,fs=FS)
        corrected=signal.filtfilt(b,a,x)
        return {'caller_input_unchanged':bool(np.array_equal(input3d[0,0],x)),
                'caller_output_identical':bool(np.array_equal(result[0,0],x)),
                'standalone_25hz_power_ratio':ratio(x,standalone,25),
                'standalone_50hz_power_ratio':ratio(x,standalone,50),
                'corrected_25hz_power_ratio':ratio(x,corrected,25),
                'corrected_50hz_power_ratio':ratio(x,corrected,50)}
    real_bandpassed=upstream.bandpass_filter(x,lowcut=1,highcut=50,fs=FS,order=5)
    syn=examine(synthetic); real=examine(real_bandpassed)
    assert syn['caller_output_identical'] and syn['caller_input_unchanged']
    assert syn['standalone_25hz_power_ratio']<0.01 and syn['standalone_50hz_power_ratio']>0.98
    assert syn['corrected_50hz_power_ratio']<0.01 and syn['corrected_25hz_power_ratio']>0.98
    assert real['caller_output_identical'] and real['caller_input_unchanged']
    receipt={'source_commit':'9136727e6a1d7370cf0cd8fbf057a7662efd17fc',
             'archive_git_blob':'09359f5e5466a93010d8471d2e5f04d6252912c0',
             'archive_compressed_size_bytes':96062569, 'compressed_prefix_bytes':PREFIX.stat().st_size,
             'compressed_prefix_sha256':PREFIX_SHA, 'upstream_preprocessing_source_sha256':SOURCE_SHA,
             'first_trial_first_channel':{'header_declared_array_shape':[20,32,N],
                                         'samples_decoded':len(x),'finite_samples':int(np.isfinite(x).sum()),
                                         'decoded_float64_bytes_sha256':sample_sha,
                                         'bandpassed_signal_diagnostic':real},
             'synthetic_diagnostic':syn,'called_filter_center_hz':25,'corrected_filter_center_hz':50,
             'filter_quality_factor':50,'sample_rate_hz':FS,
             'synthetic_fold_witness':trial_split_witness(),
             'environment':{'python':sys.version.split()[0],'numpy':np.__version__,'scipy':scipy.__version__},
             'scope':'one prefix/one channel, no labels, no complete-archive verification or neural-experience inference'}
    OUT.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
    print(json.dumps(receipt,indent=2,sort_keys=True))

if __name__=='__main__': main()
