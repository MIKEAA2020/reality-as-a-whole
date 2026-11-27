"""Build an auditable exchange index; indexing is not claim verification."""
from pathlib import Path
import hashlib
import re

source = Path('sources/uploads/DeepSeek-Claude time reconciliation critique.txt')
output = Path('CLAUDE_TIME_71_EXCHANGE_AUDIT_INDEX.md')
raw = source.read_bytes()
expected = 'a6d47ada9edda469b430419dd8700c4c1775c1c544a9ab266d9debd169d1492c'
actual = hashlib.sha256(raw).hexdigest()
if actual != expected:
    raise ValueError('Source changed; review and update the expected hash before indexing')
s = raw.decode('utf-8')
marks = list(re.finditer(r'(?m)^(User|Assistant):\s*$', s))
if len(marks) != 142 or any(m.group(1) != ('User' if i % 2 == 0 else 'Assistant') for i, m in enumerate(marks)):
    raise ValueError('Unexpected transcript role structure; do not silently guess boundaries')
# Selected source claims, not exhaustive message audits.
focused = set(range(1, 6)) | {9, 10} | set(range(13, 18)) | {28} | set(range(30, 43)) | set(range(58, 65)) | {71}
head = [
    '# Claude-time original: 71-exchange coverage index', '',
    f'Source SHA-256 `{actual}`. This mechanical index covers all 71 user/assistant exchanges by line range; **it is not a complete audit**. The source contains both assistant thinking sections and responses; summaries below are only excerpts of the user prompt, not reliable summaries of the assistant. Ranges point to the [preserved original](sources/uploads/DeepSeek-Claude%20time%20reconciliation%20critique.txt).', '',
    'Status **selected claims** means at least some claims in the exchange have been reviewed in [source correction](LIGHTHOUSE_CLAUDE_TIME_CHAT_SOURCE_CORRECTION.md), [analytical crosswalk](CLAUDE_TIME_CRITIQUE_ANALYTICAL_TARGET_CROSSWALK.md), [article audit](CLAUDE_TIME_ARTICLE_PROVENANCE_AUDIT.md) or [selection audit](CLAUDE_TIME_MODULAR_SELECTION_AUDIT.md); it does not mean every paragraph, citation, or inference in that exchange has been verified. **Index only** means no specific focused primary-source audit has been recorded for the exchange in these notes; prior work may still exist. Update the manual evidence set as work proceeds, rather than equating a line range with completion.', '',
    '| Exchange | Original lines | User prompt excerpt | Status |', '|---:|---:|---|---|'
]
for i in range(0, len(marks), 2):
    user, assistant = marks[i], marks[i+1]
    text = s[user.end():assistant.start()]
    text = re.sub(r'^\s*\d\d/\d\d/\d{4}[^\n]*\n', '', text).strip()
    excerpt = ' '.join(text.split())
    if len(excerpt) > 180:
        excerpt = excerpt[:177] + '…'
    excerpt = excerpt.replace('|', '\\|').replace('`', "'")
    first = s.count('\n', 0, user.start()) + 1
    last = s.count('\n', 0, marks[i+2].start()) if i+2 < len(marks) else len(s.splitlines())
    number = i//2+1
    status = 'selected claims' if number in focused else 'index only'
    head.append(f'| {number} | {first}–{last} | {excerpt} | {status} |')
output.write_text('\n'.join(head)+'\n', encoding='utf-8')
print(f'{output}: {len(marks)//2} exchanges indexed; {len(focused)} with selected-claim review, none marked fully audited')
