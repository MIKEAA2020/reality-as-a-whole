#!/usr/bin/env python3
"""Generate a traceability index and a content manifest, not a proof audit.

The manifest covers tracked and non-ignored untracked workspace files at the
moment of the run. It omits its own hash to avoid self-reference. File presence,
headings and checksums do not validate claims or establish completeness.
"""
from pathlib import Path
from urllib.parse import quote
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parent.parent
REGISTER = ROOT / 'FRAMEWORK_SOURCE_REGISTER.md'
MANIFEST = ROOT / 'verification/framework_inventory_manifest.json'


def paths_from_git():
    result = subprocess.run(['git','ls-files','-co','--exclude-standard','-z'],
                            cwd=ROOT, check=True, capture_output=True)
    return sorted(set(x.decode() for x in result.stdout.split(b'\0') if x))


def title(path):
    for line in path.read_text(encoding='utf-8').splitlines():
        if line.startswith('# '):
            return line[2:].strip().replace('[','(').replace(']',')')
    return '(no H1 heading)'


def link(path):
    return f'[{path}]({quote(path, safe="/")})'


def main():
    # Include the register in the manifest and documentation count, but omit
    # a recursive self-entry from its own document list.
    if not REGISTER.exists():
        REGISTER.write_text('',encoding='utf-8')
    docs=sorted(set(ROOT.glob('*.md')) | set((ROOT/'research').rglob('*.md')))
    docs=[p for p in docs if p!=REGISTER]
    root=[p for p in docs if p.parent==ROOT]
    research=[p for p in docs if p.parent!=ROOT]
    sources=sorted(p for p in (ROOT/'sources'/'uploads').rglob('*') if p.is_file())
    py=sorted(p for p in (ROOT/'verification').glob('*.py') if p.is_file())
    rows=['# Framework source register and coverage', '',
          '> **Navigation and coverage, not scientific verification.** This register inventories files mechanically; it does not certify that their contents were read line by line, correct, current, or incorporated in their entirety. Use the [current dossier](CURRENT_FRAMEWORK_BATTERY_DOSSIER.md) as the governing synthesis where historical claims conflict. Original uploads are historical sources, not independent evidence of their claims.', '',
          '## Scope', '',
          f'- {len(root)+1} root Markdown documents including this register; {len(research)} research Markdown documents.',
          f'- {len(sources)} original uploaded files, including provenance metadata; {len(py)} verification Python scripts.',
          '- The [complete machine-readable file manifest](verification/framework_inventory_manifest.json) covers tracked and non-ignored untracked files at generation time, with hashes, except the manifest itself. Runtime environments, ignored caches and untracked temporary external material are outside its scope.',
          '- [Markdown inventory and broken literal links](verification/project_inventory.json) is a separate mechanical check. Neither inventory is a semantic proof audit.', '',
          '## Authored root documents', '',
          'Alphabetical order is not an endorsement or a precedence rule. Titles may themselves contain historical overclaims.', '']
    for p in root:
        rel=p.relative_to(ROOT).as_posix()
        rows.append(f'- {link(rel)} — {title(p)}')
    rows.extend(['','## Research Markdown documents','',
                 'These reports and notes have their own domains and dependencies; their titles are not certificates.',''])
    for p in research:
        rel=p.relative_to(ROOT).as_posix()
        rows.append(f'- {link(rel)} — {title(p)}')
    rows.extend(['','## Original user-supplied sources','',
                 'The user approved inclusion of the original uploads in this public repository. These records are not automatically endorsed; where a source disagrees with later instructions, the latest explicit correction governs.',''])
    for p in sources:
        rel=p.relative_to(ROOT).as_posix()
        rows.append(f'- {link(rel)}')
    rows.extend(['','## Verification scripts','',
                 'Passing a script checks its encoded model or assertions only; historical closure aggregators and stipulated true flags are not proofs. The [selected regression battery](verification/framework_battery.py) has a narrower declared scope.',''])
    for p in py:
        rel=p.relative_to(ROOT).as_posix()
        rows.append(f'- {link(rel)}')
    rows.extend(['','## Other materials','',
                 'Research code, saved receipts, pinned external materials and other tracked files appear in the [file manifest](verification/framework_inventory_manifest.json). Inspect their provenance and the linked audit before treating them as evidence.',''])
    REGISTER.write_text('\n'.join(rows),encoding='utf-8')
    # Exclude manifest itself to avoid an impossible self-hash. Include the
    # generated register and other untracked deliverables when present.
    entries=[]
    for name in paths_from_git():
        if name=='verification/framework_inventory_manifest.json':
            continue
        path=ROOT/name
        if not path.is_file():
            continue
        data=path.read_bytes()
        entries.append({'path':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
    result={'scope':'Tracked plus non-ignored untracked files present at generation, excluding this manifest itself; no claim of semantic audit.',
            'base_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
            'file_count':len(entries),'files':entries}
    MANIFEST.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(f'{len(root)+1} root docs; {len(research)} research docs; {len(sources)} uploaded files; {len(py)} verification scripts; {len(entries)} files hashed')


if __name__=='__main__':
    main()
