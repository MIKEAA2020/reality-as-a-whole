"""Check PSR-5 adjudication provenance and narrow mathematical controls.

This is not a replay of the unavailable R1 audit or the entire battery.
"""
from hashlib import sha256
from itertools import permutations
from pathlib import Path
import unittest

from verification.zero_psr5_global_decoder_r0_test import TinyRecord, isomorphic, nat, parse_alias

ROOT=Path(__file__).resolve().parent.parent
BASE=ROOT/'psr-5 battery'
WAVE=BASE/'2nd wave'


def digest(path):return sha256(path.read_bytes()).hexdigest()


def permute(rec, perm):
    """Transport types and nu from old i to new perm[i]; other fields empty."""
    roles=[None]*len(perm);nu=[None]*len(perm)
    for i,j in enumerate(perm):
        roles[j]=rec.roles[i];nu[j]=rec.nu[i]
    return TinyRecord(tuple(roles),tuple(nu))


class PSR5AdjudicationCorrectionTests(unittest.TestCase):
    def test_source_identity_and_misnamed_copy(self):
        packet=BASE/'Plural_Structural_Realism_Entry_Packet_v5.md'
        audit=WAVE/'Point-Sphere_PSR-5_R0_Global_Model_and_Locality_Audit_v1.md'
        misnamed=WAVE/'Plural_Structural_Realism_Entry_Packet_v5.md'
        self.assertEqual(digest(packet),'b0d2a0fe6c72f19437aa1804230d0c2ba41c26a878a26deffbf50bd93d901321')
        self.assertEqual(digest(audit),'ac0bead7fee5f90ee0913af253b0e5effe43330af28af342a1cf894249e461da')
        self.assertEqual(digest(misnamed),digest(audit))
        self.assertIn('R0 Global-Model and Finite-Locality Audit',misnamed.read_text())
        self.assertNotEqual(digest(misnamed),digest(packet))

    def test_actual_adjudication_chain(self):
        sources=[('Point-Sphere_PSR-5_R0_Global_Model_and_Locality_Adjudication_v1.md',
                  '5528f8b6a924573f1411cc241d3a78bbb6010f239c7e567e9fb624331c80e36c'),
                 ('Point-Sphere_PSR-5_R1_Instantiation_and_Isomorphism_Adjudication_v1.md',
                  'e4f5e35e90ec6f8db7d68f81c269672eae3745283915d0ee6cb1e6d76a2c6462'),
                 ('Point-Sphere_PSR-5_R2_Presentation_Truth_and_Error_Adjudication_v1.md',
                  'fc67203e788c1fcbbc2c48b9b4cf13f5528bcc805606a3efae2c6126268ae3ea'),
                 ('Point-Sphere_PSR-5_R3a_Phenomenal_Interface_Adjudication_v1.md',
                  '59dd14f137f87cbeb93c987625b6655521060713d8742179bbf48aab4c821666'),
                 ('Point-Sphere_PSR-5_R3b_Normative_Interface_Adjudication_v1.md',
                  '07d0ed636c9bfa05ea955585fa729bb6f70c1700fa99446f90af9e7499e404e2'),
                 ('Point-Sphere_PSR-5_R3c_Physical_Interface_Adjudication_v1.md',
                  'e0ee906a743b9c52b71d375fe8ee94254de6fa40276b10249a54f1c281cf3d07')]
        for name,expected in sources:self.assertEqual(digest(WAVE/name),expected)
        for prior,current in zip(sources,sources[1:]):
            self.assertIn(prior[1],(WAVE/current[0]).read_text())
        r1=(WAVE/sources[1][0]).read_text()
        self.assertIn('R1-Pass',r1)
        self.assertIn('1110100100',r1)
        self.assertIn('NoSelectorResidue',r1)
        self.assertEqual('1110100100','1110'+nat(0)+nat(0))
        self.assertEqual(parse_alias('1110100100',{0:16}),(0,0))
        r2=(WAVE/sources[2][0]).read_text()
        self.assertIn('R1 passed in the PSR-5 docket',r2)
        r3c=(WAVE/sources[-1][0]).read_text()
        self.assertIn('Battery-Completed',r3c)
        self.assertIn('NoSelectorResidue',r3c)
        self.assertIn('PublicBridgePass',r3c)

    def test_exact_alias_has_one_parse_not_two(self):
        code='111011010100'
        self.assertEqual(code,'1110'+nat(2)+nat(0))
        self.assertEqual(parse_alias(code,{2:1}),(2,0))
        alternatives=[]
        for i in range(7):
            for r in range(24):
                if code=='1110'+nat(i)+nat(r):alternatives.append((i,r))
        self.assertEqual(alternatives,[(2,0)])

    def test_any_permutation_of_one_fixed_record_is_isomorphic(self):
        # Several distinct type and value fields ensure transport is real;
        # all other fields are empty. This is a finite example of the general
        # bijection proof, not an exhaustive check of all PSR records.
        rec=TinyRecord(('Ag','Si','Ag'),((('instrumentalized',0),),(),(('instrumentalized',1),)))
        variants=[permute(rec,p) for p in permutations(range(3))]
        for a in variants:
            for b in variants:self.assertTrue(isomorphic(a,b))

    def test_independent_ring5_recurrence_and_false_control(self):
        target=((1,0,0,0,0),(6,1,0,0,1),(3,5,1,1,5))
        def nextrow(row):
            return tuple((row[v]+row[(v-1)%5]-row[v]+row[(v+1)%5]-row[v])%7 for v in range(5))
        self.assertEqual(nextrow(target[0]),target[1])
        self.assertEqual(nextrow(target[1]),target[2])
        perturbed=list(target[2]);perturbed[2]=(perturbed[2]+1)%7
        self.assertNotEqual(nextrow(target[1]),tuple(perturbed))
        for t in (0,1):
            for v in range(5):self.assertEqual(nextrow(target[t])[v],target[t+1][v])

if __name__=='__main__':unittest.main()
