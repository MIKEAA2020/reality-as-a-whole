"""Frozen PSR-5 R0: test determinacy of the explicitly declared code universe.

This is a countermodel to determinacy of the standalone frozen packet, not an
assertion that either completion is actual, self-sufficient, or zero-residue.
No R1--R3 battery case is executed.
"""
from dataclasses import dataclass
from hashlib import sha256
from itertools import permutations
from math import factorial
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parent.parent
PACKET=ROOT/'psr-5 battery'/'Plural_Structural_Realism_Entry_Packet_v5.md'
PACKET_HASH='b0d2a0fe6c72f19437aa1804230d0c2ba41c26a878a26deffbf50bd93d901321'


@dataclass(frozen=True)
class TinyRecord:
    # Roles and nu-values are aligned to carrier 0,...,len(roles)-1.
    # All relations, contents, temporal indices, successors, and field
    # values are empty. nu is a finite keyed map of role values.
    roles: tuple
    nu: tuple


def candidate(record):
    # The examples have only Ag/Si roles and no edges, Pr, Ph, Ac, or field.
    # All nontrivial host/typing/order clauses from SREC are then vacuous.
    return (len(record.roles)==len(record.nu)
            and all(role in ('Ag','Si') for role in record.roles))


def isomorphic(left,right):
    if len(left.roles)!=len(right.roles):return False
    n=len(left.roles)
    return any(all((left.roles[i],left.nu[i]) ==
                   (right.roles[p[i]],right.nu[p[i]]) for i in range(n))
               for p in permutations(range(n)))


def nat(n):
    if n<0:raise ValueError('natural required')
    bits=format(n,'b')
    return '1'*len(bits)+'0'+bits


def parse_nat(code,pos):
    end=pos
    while end<len(code) and code[end]=='1':end+=1
    length=end-pos
    if not length or end>=len(code) or code[end]!='0':raise ValueError('unary length')
    stop=end+1+length
    if stop>len(code):raise ValueError('truncated bits')
    n=int(code[end+1:stop],2)
    if nat(n)!=code[pos:stop]:raise ValueError('noncanonical natural')
    return n,stop


def parse_alias(code,carrier_sizes):
    # This implements just the frozen Alias branch, with an explicitly
    # supplied macro carrier-size roster. It does not supply the omitted
    # PSR-5 fixture and is not a complete candidate decoder.
    if not code.startswith('1110'):return None
    try:i,pos=parse_nat(code,4);r,pos=parse_nat(code,pos)
    except ValueError:return None
    if pos!=len(code) or i not in carrier_sizes:return None
    if r>=factorial(carrier_sizes[i]):return None
    return i,r


class PSR5GlobalDecoderR0Tests(unittest.TestCase):
    def test_frozen_source_and_specific_clauses(self):
        raw=PACKET.read_bytes()
        self.assertEqual(sha256(raw).hexdigest(),PACKET_HASH)
        text=raw.decode('utf-8')
        self.assertIn('The accepted language and decode function are total',text)
        self.assertIn('i\\in\\{0,\\ldots,6\\}',text)
        self.assertIn('r<n_i!',text)
        self.assertIn('with one \\(Ag\\)-role and no physical field',text)
        self.assertIn('preserving every }\\tau,\\rho,\\kappa,\\eta,\\alpha,\\nu,\\Phi',text)

    def test_two_nonisomorphic_records_fit_single_role_fixture_description(self):
        # Even if "one Ag-role" is read as exactly one TOTAL carrier role,
        # neither finite nu value is specified by the S_with sentence.
        a=TinyRecord(('Ag',),((('instrumentalized',0),),))
        b=TinyRecord(('Ag',),((('instrumentalized',1),),))
        self.assertTrue(candidate(a) and candidate(b))
        self.assertFalse(isomorphic(a,b))
        # One Ag role, no field, no edges; their one role cannot be mapped
        # to the 16-role semantic fixture or 5-role ring fixture.
        self.assertEqual(len(a.roles),1)
        self.assertNotEqual(len(a.roles),16)
        self.assertNotEqual(len(a.roles),5)
        # The different nu values must be preserved by PSR-5 isomorphism.

    def test_same_accepted_alias_has_two_nonisomorphic_decodes(self):
        self.assertEqual(nat(2),'11010')
        self.assertEqual(nat(0),'100')
        code='1110'+nat(2)+nat(0)
        self.assertEqual(code,'111011010100')
        self.assertEqual(parse_alias(code,{2:1}),(2,0))
        a=TinyRecord(('Ag',),((('instrumentalized',0),),))
        b=TinyRecord(('Ag',),((('instrumentalized',1),),))
        # r=0 is the identity permutation on either one-element carrier.
        self.assertFalse(isomorphic(a,b))
        # The text therefore does not determine the image of this accepted
        # code up to the candidate's own declared structural equivalence.

    def test_carrier_size_is_also_underdetermined_if_other_roles_permitted(self):
        one=TinyRecord(('Ag',),((('instrumentalized',0),),))
        two=TinyRecord(('Ag','Si'),((('instrumentalized',0),),()))
        self.assertTrue(candidate(one) and candidate(two))
        self.assertFalse(isomorphic(one,two))
        code='1110'+nat(2)+nat(1)
        self.assertEqual(code,'111011010101')
        self.assertIsNone(parse_alias(code,{2:1}))
        self.assertEqual(parse_alias(code,{2:2}),(2,1))
        # This secondary ambiguity assumes the S_with sentence permits
        # an Si role in addition to its one Ag; the primary test does not.

    def test_nat_parser_rejects_truncation_and_noncanonical_encodings(self):
        for i in range(7):
            for r in range(5):
                code='1110'+nat(i)+nat(r)
                self.assertEqual(parse_alias(code,{i:3}),(i,r))
                self.assertIsNone(parse_alias(code+'0',{i:3}))
                self.assertIsNone(parse_alias(code[:-1],{i:3}))
        self.assertIsNone(parse_alias('1110'+'11000'+nat(0),{0:1}))
        # '11000' encodes zero with a forbidden leading zero rather than N(0).

if __name__=='__main__':unittest.main()
