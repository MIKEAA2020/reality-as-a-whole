"""Run named unittest modules separately with timeouts; this is not a proof audit.

Example:
  OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:verification:. python \
    verification/run_formalization_regression_batch.py --pattern 'zero_*test.py' \
    --start 0 --count 20 --timeout 15 --output .arena/example.json
The .arena output is disposable until intentionally saved as review evidence.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[1]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pattern',required=True)
    parser.add_argument('--start',type=int,default=0)
    parser.add_argument('--count',type=int,required=True)
    parser.add_argument('--timeout',type=float,default=15.)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    if args.start < 0 or args.count <= 0 or args.timeout <= 0:
        parser.error('start must be nonnegative; count and timeout must be positive')
    files=sorted((ROOT/'verification').glob(args.pattern))
    if any(not f.is_file() or f.suffix != '.py' or not f.stem.isidentifier() for f in files):
        parser.error('pattern must identify Python modules in verification')
    chosen=files[args.start:args.start+args.count]
    if not chosen:
        parser.error('empty batch')
    output=Path(args.output)
    if not output.is_absolute(): output=ROOT/output
    output.parent.mkdir(parents=True,exist_ok=True)
    data={'pattern':args.pattern,'start':args.start,'count_requested':args.count,
          'available_at_start':len(files),
          'available_files_at_start':[str(f.relative_to(ROOT)) for f in files],
          'timeout_seconds_per_module':args.timeout,
          'python':sys.version,'results':[],
          'scope':'Unittest executions for selected files only; no semantic proof audit.'}
    for f in chosen:
        module='verification.'+f.stem
        cmd=[sys.executable,'-m','unittest',module,'-q']
        t=time.monotonic()
        try:
            run=subprocess.run(cmd,cwd=ROOT,env=os.environ.copy(),capture_output=True,
                               text=True,timeout=args.timeout)
            text=run.stdout+'\n'+run.stderr
            found=re.search(r'Ran (\d+) tests? in ',text)
            num=int(found.group(1)) if found else None
            status='passed' if run.returncode==0 and num and num>0 else (
                'empty' if run.returncode==0 and num==0 else 'failed')
            record={'file':str(f.relative_to(ROOT)),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),
                    'status':status,'tests_run':num,'exit_code':run.returncode,
                    'seconds':round(time.monotonic()-t,3),'output_tail':text[-3000:]}
        except subprocess.TimeoutExpired as exc:
            def decode(v): return (v or b'').decode('utf-8','replace') if isinstance(v,bytes) else (v or '')
            record={'file':str(f.relative_to(ROOT)),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),
                    'status':'timeout','tests_run':None,'exit_code':None,
                    'seconds':round(time.monotonic()-t,3),
                    'output_tail':(decode(exc.stdout)+'\n'+decode(exc.stderr))[-3000:]}
        data['results'].append(record)
        # Checkpoint after each module; replace prevents partially written JSON.
        tmp=output.with_suffix(output.suffix+'.tmp')
        tmp.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
        os.replace(tmp,output)
        print(f"{len(data['results'])}/{len(chosen)} {module}: {record['status']} "
              f"({record['tests_run']} tests, {record['seconds']}s)",flush=True)
    return 0 if all(r['status']=='passed' for r in data['results']) else 1


if __name__=='__main__':
    raise SystemExit(main())
