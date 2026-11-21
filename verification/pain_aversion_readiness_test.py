import io,json,tarfile,tempfile,unittest
from pathlib import Path
from pain_aversion_readiness import COMMIT,ROOT_TREE,EXPECTED,blob_id,inspect_event,mean_floor,run

def events():
 lines=['onset\tduration\tsample\ttrial_type\tvalue']
 lines += [f'{i}.0\t0\t{i*1000}\t{e}\t{i+1}' for i,e in enumerate(EXPECTED)]
 return ('\n'.join(lines)+'\n').encode()

class TestReadiness(unittest.TestCase):
 def test_event_sequence_and_clock(self):
  r=inspect_event(events());self.assertTrue(r['sequence_ok']);self.assertTrue(r['time_valid']);self.assertEqual(r['row_count'],10);self.assertEqual(r['max_sample_onset_difference'],0)
  self.assertFalse(inspect_event(events().replace(b't02/p150',b't02/p100'))['sequence_ok'])
  self.assertFalse(inspect_event(events().replace(b'1.0\t0\t1000',b'0.0\t0\t1000'))['time_valid'])
 def test_event_schema_and_nonfinite(self):
  self.assertFalse(inspect_event(b'onset\ttype\n1\ta\n')['schema_ok'])
  self.assertFalse(inspect_event(events().replace(b'1.0\t0\t1000',b'nan\t0\t1000'))['time_valid'])
 def test_oracle_mean_bound(self):
  r=mean_floor();self.assertEqual(r['auditory_minus_thermal'],['2.51','21.32','46.99'])
  self.assertAlmostEqual(r['equal_output_oracle_rmse_over_six_published_means'],14.913368164167341)
 def test_bounded_archive_and_blob_checks(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d);path='sub-002/eeg/sub-002_task-audioactive_events.tsv';b=events()
   tree={'sha':ROOT_TREE,'truncated':False,'tree':[{'path':path,'sha':blob_id(b),'mode':'100644'}]}
   (p/'tree').write_text(json.dumps(tree))
   def archive(content):
    with tarfile.open(p/'archive','w:gz') as tf:
     i=tarfile.TarInfo(f'ds008349-{COMMIT}/{path}');i.size=len(content);tf.addfile(i,io.BytesIO(content))
   archive(b);r=run(p/'tree',p/'archive');self.assertEqual(r['checked_git_blobs'],1);self.assertEqual(r['tasks']['audioactive']['event_checks']['sequence_ok'],1)
   archive(b+b'bad');
   with self.assertRaises(ValueError):run(p/'tree',p/'archive')
   tree['truncated']=True;(p/'tree').write_text(json.dumps(tree))
   with self.assertRaises(ValueError):run(p/'tree',p/'archive')
 def test_blob_hash_known(self):
  self.assertEqual(blob_id(b'hello\n'),'ce013625030ba8dba906f756967f9e9ca394464a')
if __name__=='__main__':unittest.main()
