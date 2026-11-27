"""Conservative file-level review queue. A receipt never certifies a whole file."""
from pathlib import Path
from collections import Counter
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]
RECEIPTS = ROOT / 'verification/formalization_review_receipts.json'
OUTPUT = ROOT / 'verification/formalization_review_progress.json'
# Overinclusive: includes sources, tests and prose that may contain no proof.
SUFFIXES = {'.md', '.py', '.m', '.txt', '.pdf'}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def build(root, filenames, receipts):
    root = Path(root)
    records = []
    for name in sorted(set(filenames)):
        path = root / name
        if not path.is_file() or path.suffix.lower() not in SUFFIXES:
            continue
        sha = digest(path.read_bytes())
        receipt = receipts.get(name)
        status = 'not_rechecked_in_this_sweep'
        detail = None
        if receipt:
            if any(not (root / evidence).is_file() for evidence in receipt['evidence']):
                raise ValueError(f'missing evidence for {name}')
            evidence_hashes = receipt['evidence_sha256']
            if set(evidence_hashes) != set(receipt['evidence']):
                raise ValueError(f'evidence hashes do not match evidence for {name}')
            if sha != receipt['reviewed_sha256']:
                status = 'review_stale_file_changed'
            elif any(digest((root / item).read_bytes()) != evidence_hashes[item]
                     for item in receipt['evidence']):
                status = 'review_stale_evidence_changed'
            else:
                status = 'selected_claims_reviewed'
            detail = {k: receipt[k] for k in ('scope', 'evidence', 'reviewed_sha256', 'evidence_sha256')}
        records.append({'path': name, 'sha256': sha, 'status': status, 'receipt': detail})
    missing = sorted(set(receipts) - {r['path'] for r in records})
    if missing:
        raise ValueError(f'receipts outside scanned candidates: {missing}')
    return {
        'scope': ('Tracked and non-ignored files with .md, .py, .m, .txt or .pdf suffixes; '
                  'an overinclusive file-level queue, not an enumeration of distinct theorems. '
                  'Other files, ignored caches and absent originals are not reviewed by this tracker.'),
        'semantics': ('not_rechecked_in_this_sweep does not erase prior audits. '
                      'selected_claims_reviewed means only the listed scope, not a complete file audit. '
                      'A reviewed-file or evidence hash change marks the receipt stale; tests are not independent proof.'),
        'counts': dict(sorted(Counter(r['status'] for r in records).items())),
        'records': records,
    }


def main():
    filenames = subprocess.check_output(
        ['git', 'ls-files', '--cached', '--others', '--exclude-standard', '-z'], cwd=ROOT
    ).decode('utf-8').split('\0')
    receipts = json.loads(RECEIPTS.read_text(encoding='utf-8'))
    result = build(ROOT, (x for x in filenames if x), receipts)
    OUTPUT.write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print(f"{len(result['records'])} candidate files: {result['counts']}")


if __name__ == '__main__':
    main()
