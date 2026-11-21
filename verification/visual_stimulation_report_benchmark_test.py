import csv,io,json,unittest
from pathlib import Path
from fractions import Fraction
import visual_stimulation_report_benchmark as v

class VisualMetadataTests(unittest.TestCase):
    def row(self,label,current='n/a',static='0'):
        d={'label':label,'onset':'8','duration':'0','stim_contacts':'n/a','stim_intensity':current}
        d.update({k:'0' for k in v.TARGETS});d['sym_static']=static
        return d
    def data(self,rows):
        f=io.StringIO();w=csv.DictWriter(f,fieldnames=rows[0],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);return f.getvalue().encode()
    def test_git_blob(self):
        self.assertEqual(v.git_blob(b'hello\n'),'ce013625030ba8dba906f756967f9e9ca394464a')
    def test_strict_and_amended(self):
        rows=[self.row('prestim'),self.row('effect','1','1'),self.row('poststim'),self.row('extra')]
        with self.assertRaisesRegex(ValueError,'event structure'):v.parse_events(self.data(rows))
        self.assertEqual(v.parse_events(self.data(rows),strict=False)['flags']['sym_static'],1)
    def test_nonbinary_rejected(self):
        rows=[self.row('prestim'),self.row('effect','1','n/a'),self.row('poststim')]
        with self.assertRaisesRegex(ValueError,'nonbinary'):v.parse_events(self.data(rows),strict=False)
    def test_nonunique_current_rejected(self):
        rows=[self.row('prestim'),self.row('effect','1'),self.row('extra','1')]
        with self.assertRaisesRegex(ValueError,'non-unique'):v.parse_events(self.data(rows),strict=False)
    def test_oracle_grouped_by_patient_not_just_dose(self):
        def r(p,y):return {'person':p,'current':Fraction(1),'flags':{k:y for k in v.TARGETS}}
        result=v.score([r('a',0),r('a',1),r('a',1),r('b',0)])['sym_static']
        self.assertEqual(result['oracle_in_sample_mistakes'],1)
        self.assertEqual(result['same_patient_current_mixed_groups'],1)
        self.assertEqual(result['oracle_in_sample_mistake_fraction'],0.25)
    def test_receipt_has_no_benchmark(self):
        rec=json.loads(Path('verification/visual_stimulation_report_benchmark.json').read_text())
        self.assertEqual(rec['strict_plan_eligible'],7)
        self.assertEqual(rec['amended_events'],112)
        self.assertNotIn('evaluation',rec)
        self.assertEqual(rec['git_blobs_verified'],224)
if __name__=='__main__':unittest.main()
