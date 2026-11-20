#!/usr/bin/env python3
"""Fixed-plan descriptive EEG screen; source files are never emitted."""
import hashlib, json, math, pathlib, subprocess, sys
import h5py, numpy as np, scipy
from scipy import signal, stats

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / '.arena/adamos'
SOURCES = [
 ('01', 'f10793470ec456c855e9515de8529ee0523faf7e', 34381684),
 ('02', 'b96f6405c85a05442eaabeb3a5c57490562dcd71', 34406208),
 ('03', '526fba303e56f14be835e0a0385e97a133437c90', 34391694),
 ('04', '5c22299ae7db3247f91c3c6afa18f798ebe19ad1', 34333001),
]
PAIRS = [('f3','f4'),('f7','f8'),('af3','af4')]
FS = 128

def verify_blob(path, sha, size):
    if path.stat().st_size != size: raise ValueError('size mismatch')
    h = hashlib.sha1(f'blob {size}\0'.encode()); sha256 = hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda: f.read(1024*1024), b''):
            h.update(b); sha256.update(b)
    if h.hexdigest() != sha: raise ValueError('Git blob hash mismatch')
    return sha256.hexdigest()

def labels_for(f):
    refs = f['sensor_info/labels'][()].ravel()
    return [''.join(chr(int(v)) for v in f[ref][()].ravel()).strip().casefold() for ref in refs]

def validate(data, ratings, labels, fs):
    if data.shape != (10240,14,30) or ratings.shape != (30,): raise ValueError('shape mismatch')
    if fs != FS or len(labels) != 14 or len(set(labels)) != 14: raise ValueError('sampling rate or channel labels')
    if not all(ch in labels for pair in PAIRS for ch in pair): raise ValueError('required channel absent')
    if not np.all(np.isfinite(data)) or not np.all(np.isfinite(ratings)): raise ValueError('nonfinite data')
    if not all(np.count_nonzero(ratings == k) == 10 for k in (1,3,5)): raise ValueError('rating counts')

def phase_dispersion(phases):
    # channels in pair order, shape (six, 70*Fs); exactly 14 independent windows
    z = np.exp(1j*(phases[::2] - phases[1::2])).reshape(3,14,5*FS)
    return float(1 - np.abs(z.mean(axis=-1)).mean())

def features(trial, idx, common):
    x = np.asarray(trial, dtype=float).T  # sensor,time
    if common: x = x - x.mean(axis=0, keepdims=True)
    x = x[idx]
    sos = signal.butter(4, [8,13], btype='bandpass', fs=FS, output='sos')
    phase = np.angle(signal.hilbert(signal.sosfiltfilt(sos,x,axis=-1),axis=-1))[:,5*FS:-5*FS]
    dispersion = phase_dispersion(phase)
    f,p = signal.welch(x[:,5*FS:-5*FS], fs=FS, window='hann', nperseg=2*FS, noverlap=FS, detrend='constant', axis=-1)
    # uniform spectral spacing, endpoint inclusion as specified
    band = lambda lo,hi: p[:,(f>=lo)&(f<=hi)].sum(axis=-1)*(f[1]-f[0])
    tiny = np.finfo(float).tiny
    alpha = np.maximum(band(8,13), tiny)
    beta = np.maximum(band(15,30), tiny)
    return [dispersion, float(np.log(alpha[1])-np.log(alpha[0])), float(np.log(beta).mean())]

def summarize(feat, ratings):
    return [{'high_minus_low':float(v[ratings==5].mean()-v[ratings==1].mean()),
             'spearman':float(stats.spearmanr(v,ratings).statistic)} for v in feat.T]

def analyze(path, sha, size):
    digest = verify_blob(path,sha,size)
    with h5py.File(path, 'r') as f:
        data = f['EEG_Songs'][()]; ratings = f['song_ratings'][()].ravel()
        labels = labels_for(f); fs = float(f['Fs'][0,0])
    validate(data, ratings, labels, fs)
    idx = [labels.index(ch) for pair in PAIRS for ch in pair]
    results = {}
    for common in (True, False):
        feat = np.array([features(data[:,:,i], idx, common) for i in range(30)])
        if not np.all(np.isfinite(feat)): raise ValueError('nonfinite feature')
        results['common_average' if common else 'native'] = summarize(feat,ratings)
    return {'git_blob':sha,'sha256':digest,'bytes':size,'shape_hdf5':list(data.shape),
            'fs':fs,'sensor_labels':labels,'rating_counts':{str(k):int(np.count_nonzero(ratings==k)) for k in (1,3,5)},'results':results}

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    records = {}
    for sub,sha,size in SOURCES:
        path = OUT / ('s'+sub+'.mat')
        if not path.exists():
            print('Fetching subject',sub,flush=True)
            with path.open('wb') as f:
                subprocess.run(['gh','api',f'repos/AdamosDA/Music-EEG/git/blobs/{sha}','-H','Accept: application/vnd.github.raw+json'], stdout=f, check=True)
        print('Verifying and analyzing subject',sub,flush=True)
        records[sub] = analyze(path,sha,size)
        path.unlink()  # never retain a source file after successful analysis
    names = ['alpha_phase_dispersion','alpha_log_power_F4_minus_F3','mean_log_beta_power']
    means = {}
    for ref in ['common_average','native']:
        means[ref] = {name:{key:float(np.mean([records[s]['results'][ref][i][key] for s in records]))
                            for key in ['high_minus_low','spearman']} for i,name in enumerate(names)}
    receipt = {'source_commit':'26f32cb4f087326a52fbf2e0b38e00630222be63','numpy':np.__version__,'scipy':scipy.__version__,'h5py':h5py.__version__,'features':names,'subjects':records,'unweighted_subject_means':means,'category_balanced_constant_3_mae':4/3,'category_balanced_constant_3_rmse':math.sqrt(8/3)}
    (ROOT/'verification/music_appraisal_feasibility.json').write_text(json.dumps(receipt,indent=2,allow_nan=False)+'\n')
    print(json.dumps(means,indent=2))
if __name__ == '__main__': main()
