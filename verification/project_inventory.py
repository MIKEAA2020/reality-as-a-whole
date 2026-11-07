#!/usr/bin/env python3
"""Deterministic text inventory, not a semantic or scientific proof audit.

Includes authored root and research Markdown; excludes supplied source transcripts,
external archives, verification assets, and this inventory's outputs. The scanner
reads all included file bytes and extracts literal Markdown links and risk phrases.
"""
from pathlib import Path
import hashlib
import json
import re
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'verification' / 'project_inventory.json'
LINK = re.compile(r'(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)')
RISK = re.compile(r'\b(?:zero[- ]residue|all (?:checks )?pass|solved|closed|proved|proves|unique(?:ly)?|forced|exact(?:ly)?)\b', re.I)


def authored_docs():
    return sorted(set(ROOT.glob('*.md')) | set((ROOT / 'research').rglob('*.md')))


def main():
    paths = authored_docs()
    docs, broken = [], []
    for path in paths:
        raw = path.read_bytes()
        text = raw.decode('utf-8')
        rel = path.relative_to(ROOT).as_posix()
        headings = [line.lstrip('#').strip() for line in text.splitlines() if re.match(r'^#{1,2}\s', line)]
        links = []
        in_fence = False
        for line in text.splitlines():
            if line.lstrip().startswith(('```', '~~~')):
                in_fence = not in_fence
                continue
            if in_fence or line.startswith(('    ', '\t')):
                continue
            for match in LINK.finditer(line):
                target = match.group(1).strip().split(' ', 1)[0]
                if not target or target.startswith(('http:', 'https:', 'mailto:', '#', 'data:')):
                    continue
                local = unquote(target.split('#', 1)[0].split('?', 1)[0])
                if not local:
                    continue
                dest = (path.parent / local).resolve()
                if not dest.is_relative_to(ROOT):
                    continue
                links.append(dest.relative_to(ROOT).as_posix())
                if not dest.exists():
                    broken.append({'source': rel, 'target': target})
        risk_lines = [i for i, line in enumerate(text.splitlines(), 1) if RISK.search(line)]
        docs.append({'path': rel, 'sha256': hashlib.sha256(raw).hexdigest(),
                     'bytes': len(raw), 'lines': len(text.splitlines()),
                     'title': headings[0] if headings else '',
                     'headings': headings[:8], 'local_links': links,
                     'risk_phrase_lines': risk_lines})
    report = {'scope': 'root and research Markdown; supplied transcripts and verification assets excluded',
              'note': 'Risk phrases flag text for review, not falsity. Literal link scan does not validate anchors.',
              'document_count': len(docs), 'bytes': sum(d['bytes'] for d in docs),
              'line_count': sum(d['lines'] for d in docs),
              'document_count_with_risk_phrases': sum(bool(d['risk_phrase_lines']) for d in docs),
              'broken_local_link_count': len(broken), 'broken_local_links': broken,
              'documents': docs}
    OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f"Inventoried {len(docs)} documents, {report['line_count']} lines, {report['bytes']} bytes")
    print(f"Literal local links with missing targets: {len(broken)}; risk phrase hits: {report['document_count_with_risk_phrases']} documents")
    print('Risk phrases and link counts are NOT correctness assessments.')
    print(OUT.relative_to(ROOT))


if __name__ == '__main__':
    main()
