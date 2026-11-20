#!/usr/bin/env python3
"""Synthetic tests for the metadata-only audit. No trial information used."""
from daly_affective_music_event_alignment import audit_events

ok=[(0.,786),(3.,788),(3.,321)]
for i in range(8): ok += [(20.+i,800+i),(20.+i,901+i)]
a=audit_events(ok)
assert a['music_start_rows']==1 and a['starts_exact_documented_music_identity_1']==1
assert a['strict_questionnaire_intervals']==1 and a['intervals_missing_question_code']==0
assert a['starts_without_fixation_in_previous_4s']==0
b=audit_events(ok+[(20.,800),(22.5,901)])
assert b['duplicate_identical_events']==1
assert b['strict_questionnaire_intervals']==0 and b['intervals_answer_without_question_same_time']==1
c=audit_events(ok+[(20.2,800)])
assert c['intervals_repeated_question_timestamp']==1 and c['strict_questionnaire_intervals']==0
missing=audit_events([e for e in ok if e[1] not in (807,908)])
assert missing['intervals_missing_question_code']==1 and missing['strict_questionnaire_intervals']==0
near=audit_events([(0.,786),(3.,788),(3.05,310),(3.05,362),(3.2,499)])
assert near['starts_exact_documented_music_identity_0']==1
assert near['starts_near_documented_music_identity_1']==1 and near['starts_near_361_399']==1
assert near['starts_near_401_499']==0
print('Synthetic metadata parser checks passed.')
