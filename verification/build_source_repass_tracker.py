#!/usr/bin/env python3
"""Conservative multi-pass tracker, not a semantic audit of every file.

Index every available repository Markdown document and every preserved file in
sources/ and the PSR folder. Manual stage marks are partial, with explicit
existing evidence. Pending means unassessed in *this integration repass*, not
that previous research did not exist. It is deliberately not a proof checker.
"""
from pathlib import Path
import hashlib
import json
import subprocess

ROOT=Path(__file__).resolve().parent.parent
OUT='verification/source_repass_progress.json'
FIRST='ZERO_SOURCE_INTEGRATION_STATIONARY_BATTERY_INTERFACE.md'
SECOND='ZERO_SOURCE_INTEGRATION_STATIONARY_SUBJECT_INCIDENCE.md'
THIRD='ZERO_SOURCE_INTEGRATION_BOSTROM_SELF_LOCATION_SPHERE.md'
FOURTH='ZERO_SOURCE_INTEGRATION_CLOCK_REALM_AND_JOINT_INTERFACE.md'
FIFTH='ZERO_POINT_SPHERE_SIGNED_MAGNITUDE_ECHO_INTEGRATION.md'
SEVENTH='ZERO_COHERENT_ANGULAR_SPHERE_ECHO_CONSTRUCTION.md'
EIGHTH='ZERO_COHERENT_ANGULAR_RESERVOIR_CLOCK_ACCESS.md'
NINTH='ZERO_INTRINSIC_QUALITY_ANGULAR_RECONSTRUCTION.md'
PSR='ZERO_PSR5_SECOND_WAVE_ADJUDICATION_AND_LESSONS.md'

# Paths and stage evidence are conservative manual judgments. Add only after a
# source-specific audit/plan/implementation is actually recorded; not on the
# basis of a title, passing a script, or an automated text match.
PARTIAL={
 "sources/uploads/Bostrom's simulation hypothesis.md": {
  'audit':[THIRD], 'plan':[THIRD],
  'implemented':[THIRD,'verification/zero_stationary_refinement_self_location.py']},
 'sources/uploads/page1983.pdf': {
  'audit':['ZERO_PAGE_WOOTTERS_1983_RELATIONAL_SPHERE.md'],
  'plan':[FIRST,EIGHTH],
  'implemented':[FIRST,'verification/zero_stationary_battery_bridge.py',EIGHTH,
                 'verification/zero_clock_relational_povm_test.py']},
 'sources/uploads/kent2015.pdf': {
  'audit':['KENT_LORENTZIAN_QUANTUM_REALITY_FULL_PAPER_AUDIT.md'],
  'plan':[FOURTH], 'implemented':[]},
 'sources/uploads/bohn2018.pdf': {
  'audit':['BOHN_PLURAL_COLLECTIVE_CONSCIOUSNESS_FULL_PAPER_AUDIT.md'],
  'plan':[SECOND], 'implemented':[SECOND,'verification/zero_stationary_subject_incidence.py']},
 'sources/uploads/miller2017.pdf': {
  'audit':['MILLER_SUBJECT_PARTHOOD_AND_DECOMBINATION_AUDIT.md'],
  'plan':[SECOND], 'implemented':[SECOND,'verification/zero_stationary_subject_incidence.py']},
 'sources/uploads/DeepSeek_Experience-and-non-optimal-world_20261106-2010.txt': {
  'audit':['TWO_EXPERIENCE_AND_REALITY_TRANSCRIPTS_SYNTHESIS.md'],
  'plan':[NINTH], 'implemented':[NINTH,'verification/zero_intrinsic_angular_estimation.py']},
 'sources/uploads/DeepSeek_Russellian-experience-intrinsic-matter_20261104-2323.txt': {
  'audit':['TWO_EXPERIENCE_AND_REALITY_TRANSCRIPTS_SYNTHESIS.md'],
  'plan':[NINTH], 'implemented':[NINTH,'verification/zero_intrinsic_angular_estimation.py']},
 'sources/uploads/DeepSeek_Evaluate-universal-principles_20261125-0858.txt': {
  'audit':['UNIVERSAL_PRINCIPLES_POLARITY_RECORDS_AND_ZERO_AUDIT.md'],
  'plan':[FIFTH], 'implemented':[FIFTH,'verification/zero_sphere_angular_echo.py']},
 'sources/uploads/DeepSeek_Experience-and-non-optimal-world_20261123-0207.txt': {
  'audit':['UPDATED_EXPERIENCE_ZERO_TOTAL_AND_INTELLIGIBILITY_AUDIT.md'],
  'plan':[FIFTH], 'implemented':[FIFTH,'verification/zero_sphere_angular_echo.py']},
 'sources/uploads/DeepSeek_Experience-and-non-optimal-world_20261123-2.txt': {
  'audit':['ZERO_TOTALITY_PERFORMANCE_AND_RESIDUE_AUDIT.md'],
  'plan':[FIFTH], 'implemented':[FIFTH,'verification/zero_sphere_angular_echo.py']},
 'sources/uploads/DeepSeek_Experience-and-non-optimal-world_20261123-3.txt': {
  'audit':['UPDATED_EXPERIENCE_ENERGY_AND_TIME_CHAT_AUDIT.md'],
  'plan':[FIFTH,SEVENTH], 'implemented':[FIFTH,'verification/zero_sphere_angular_echo.py',SEVENTH,'verification/zero_quantum_angular_echo.py']},
 'sources/uploads/DeepSeek_Experience-and-non-optimal-world_20261123-4.txt': {
  'audit':['ZERO_NECESSITY_CHANCE_SPACETIME_UPDATED_CHAT_AUDIT.md'],
  'plan':[FIFTH,'ZERO_COVARIANT_ANGULAR_RECORD_AND_COUNTERPART.md'],
  'implemented':[FIFTH,'verification/zero_sphere_angular_echo.py','ZERO_COVARIANT_ANGULAR_RECORD_AND_COUNTERPART.md','verification/zero_angular_covariant_access.py']},
 'psr-5 battery/Plural_Structural_Realism_Entry_Packet_v5.md': {
  'audit':[PSR,'ZERO_PSR5_FROZEN_R0_DECODER_REVIEW.md'],
  'plan':[FIRST], 'implemented':[FIRST,'verification/zero_stationary_battery_bridge.py']},
}


def included(name):
    p=Path(name)
    return ((len(p.parts)==1 and p.suffix.lower()=='.md') or
            (p.parts[0]=='research' and p.suffix.lower()=='.md') or
            p.parts[0] in ('sources','psr-5 battery'))


def category(name):
    if name.startswith('sources/uploads/'):return 'preserved upload'
    if name.startswith('sources/external/'):return 'external source artifact'
    if name.startswith('psr-5 battery/'):return 'PSR supplied record'
    if name.startswith('research/'):return 'research document'
    return 'authored root document'


def collect():
    raw=subprocess.run(['git','ls-files','-co','--exclude-standard','-z'],
                       cwd=ROOT,check=True,capture_output=True).stdout
    names=sorted({x.decode('utf-8') for x in raw.split(b'\0') if x})
    return [x for x in names if included(x) and (ROOT/x).is_file()]


def build():
    names=collect()
    for path,stages in PARTIAL.items():
        if path not in names:raise ValueError('Tracked source missing: '+path)
        for refs in stages.values():
            for ref in refs:
                if not (ROOT/ref).is_file():raise ValueError('Evidence missing: '+ref)
    records=[]
    for name in names:
        evidence=PARTIAL.get(name,{})
        stages={key:{'status':'partial' if evidence.get(key) else 'unassessed_in_this_repass',
                     'evidence':evidence.get(key,[])}
                for key in ('audit','plan','implemented')}
        records.append({'path':name,'kind':category(name),
                        'sha256':hashlib.sha256((ROOT/name).read_bytes()).hexdigest(),
                        'stages':stages})
    return {'scope':'Tracked and non-ignored untracked repository Markdown, all preserved sources and PSR records; not the complete chat or ignored private caches.',
            'status_semantics':'partial = documented contribution only, not complete integration; unassessed_in_this_repass does not erase or deny prior work.',
            'records':records}


def main():
    data=build();path=ROOT/OUT
    path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    counts={}
    for r in data['records']:counts[r['kind']]=counts.get(r['kind'],0)+1
    print('Indexed',len(data['records']),'records:',counts)
    print('Manually marked partial:',len(PARTIAL),'source records; all other stage fields unassessed in this repass')
    print(OUT)

if __name__=='__main__':main()
