"""Fixed common physical report distributions versus competing quality labels.

Finite checks of a probabilistic inequality. Experiential labels and report
error are stipulated, not observations or evidence that any spin is a subject.
"""
from fractions import Fraction as F
import unittest

from verification.constitution_challenge_decision_test import physical_history, observed_mixture
from verification.four_spin_mismatch_measurement_gate import majority_failure

CELLS=((0,0),(0,1),(1,0),(1,1))


def level(c):
    return c[1]


def onset(c):
    return int(c==(0,1))


def errors(table):
    """Common conditional joint law P(C,Y), with no assumed error independence."""
    assert sum(table.values())==1
    a=sum(p for (c,y),p in table.items() if y != level(c))
    b=sum(p for (c,y),p in table.items() if y != onset(c))
    m=sum(p for (c,_),p in table.items() if c==(1,1))
    return a,b,m


def compositions(total,n):
    if n==1:
        yield (total,)
    else:
        for v in range(total+1):
            for rest in compositions(total-v,n-1):
                yield (v,)+rest


def optimal_common_report(mixture, r):
    """Y equals both assignments on agreement cells; Y=1 with prob r on 11."""
    table={(c,y):F(0) for c in CELLS for y in (0,1)}
    for c,p in mixture.items():
        if c==(1,1):
            table[c,1]=p*r
            table[c,0]=p*(1-r)
        else:
            assert level(c)==onset(c)
            table[c,level(c)]=p
    return table


class DancingQualiaReportControlTests(unittest.TestCase):
    def test_universal_bound_without_independent_errors(self):
        keys=[(c,y) for c in CELLS for y in (0,1)]
        cases=0
        for counts in compositions(6,8):
            table={key:F(value,6) for key,value in zip(keys,counts)}
            ea,eb,m=errors(table)
            self.assertGreaterEqual(ea+eb,m)
            self.assertGreaterEqual(max(ea,eb),m/2)
            cases+=1
        self.assertEqual(cases,1716)

    def test_bound_sharp_for_arbitrary_mixture_and_tradeoff(self):
        mixture={(0,0):F(2,5),(0,1):F(1,10),
                 (1,0):F(1,5),(1,1):F(3,10)}
        for r in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
            ea,eb,m=errors(optimal_common_report(mixture,r))
            self.assertEqual(ea,m*(1-r))
            self.assertEqual(eb,m*r)
            self.assertEqual(ea+eb,m)
        ea,eb,m=errors(optimal_common_report(mixture,F(1,2)))
        self.assertEqual(ea,eb)
        self.assertEqual(ea,m/2)

    def test_persistent_mismatch_has_minimum_half_max_error(self):
        mixture={(0,0):F(0),(0,1):F(0),(1,0):F(0),(1,1):F(1)}
        for r in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
            ea,eb,m=errors(optimal_common_report(mixture,r))
            self.assertEqual((ea,eb),(1-r,r))
            self.assertGreaterEqual(max(ea,eb),F(1,2))

    def test_existing_physical_noise_posterior(self):
        _,mixture=observed_mixture(physical_history(),F(19,200),majority_failure(19))
        ea,eb,m=errors(optimal_common_report(mixture,F(1,2)))
        self.assertEqual(ea,eb)
        self.assertEqual(ea,m/2)
        self.assertAlmostEqual(float(m),.8295909999,places=9)
        self.assertAlmostEqual(float(ea),.4147955,places=6)
        self.assertGreater(ea,F(1,10))

    def test_report_link_changes_complete_physical_description(self):
        mixture={(0,0):F(0),(0,1):F(0),(1,0):F(0),(1,1):F(1)}
        report_level=optimal_common_report(mixture,F(1))
        report_onset=optimal_common_report(mixture,F(0))
        self.assertEqual(errors(report_level)[:2],(F(0),F(1)))
        self.assertEqual(errors(report_onset)[:2],(F(1),F(0)))
        self.assertNotEqual(report_level,report_onset)
        # Same C distribution, different physical Y channel: not fully
        # physically identical just because the spin kernel is identical.
        for c in CELLS:
            self.assertEqual(sum(report_level[c,y] for y in (0,1)),mixture[c])
            self.assertEqual(sum(report_onset[c,y] for y in (0,1)),mixture[c])


if __name__ == '__main__':
    unittest.main()
