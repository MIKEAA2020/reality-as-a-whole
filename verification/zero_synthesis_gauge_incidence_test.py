"""Test sign pairing against incidence gauge in the actual chirality circuit.

Gauge identification, actual subjects, incidence measure and felt values are
not derived by these operator calculations.
"""
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np
from verification.zero_relational_chirality_report_test import (
    I,I16,I64,X,Z,L,CHI,GATE,MIRROR,SING,initial,outcome_tables,
    full_state,active_base,compressed_spin_base,output,relative_read,kron
)
from verification.zero_relational_orientation_reference_test import Psing


class SynthesisGaugeIncidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        old=(I16+L)@Psing/2
        de=np.outer(SING.reshape(4),SING.reshape(4).conj())
        ready=np.array([[1.,0.],[0.,0.]])
        rho=kron(old/2,de,ready)
        cls.rho=GATE@rho@GATE.conj().T
        cls.record=kron(I64,Z)
        cls.chi=kron(CHI,I)
        cls.relative=kron(CHI,Z)
        cls.pplus=(np.eye(128)+cls.record)/2
        cls.pminus=(np.eye(128)-cls.record)/2
        cls.plus=cls.pplus@cls.rho@cls.pplus
        cls.minus=cls.pminus@cls.rho@cls.pminus

    def test_actual_branches_are_distinct_but_exchanged_by_symmetry(self):
        np.testing.assert_allclose(MIRROR@self.rho@MIRROR,self.rho,atol=1e-13)
        np.testing.assert_allclose(MIRROR@self.plus@MIRROR,self.minus,atol=1e-13)
        self.assertAlmostEqual(np.trace(self.plus).real,.5,places=13)
        self.assertAlmostEqual(np.trace(self.minus).real,.5,places=13)
        self.assertAlmostEqual(np.trace(self.pplus@self.minus).real,0,places=13)
        # They are different pointer outcomes if the record is admissible;
        # the symmetry alone does not settle whether it is a gauge redundancy.

    def test_odd_and_relational_even_observables_are_not_the_same(self):
        np.testing.assert_allclose(MIRROR@self.chi@MIRROR,-self.chi,atol=1e-13)
        np.testing.assert_allclose(MIRROR@self.record@MIRROR,-self.record,atol=1e-13)
        np.testing.assert_allclose(MIRROR@self.relative@MIRROR,self.relative,atol=1e-13)
        for state,sign in ((self.plus,1),(self.minus,-1)):
            self.assertAlmostEqual((np.trace(self.record@state)/np.trace(state)).real,sign,places=13)
            self.assertAlmostEqual((np.trace(self.chi@state)/np.trace(state)).real,sign,places=13)
            self.assertAlmostEqual((np.trace(self.relative@state)/np.trace(state)).real,1,places=13)
        # Agreement is an invariant relation but has the same sign in both
        # branches; it is not an opposite-valued cancellation.

    def test_gauge_twirling_removes_the_absolute_sign_but_not_agreement(self):
        e=(self.pplus+MIRROR@self.pplus@MIRROR)/2
        np.testing.assert_allclose(e,np.eye(128)/2,atol=1e-13)
        gauge_even=(self.relative+MIRROR@self.relative@MIRROR)/2
        np.testing.assert_allclose(gauge_even,self.relative,atol=1e-13)
        for state in (self.plus,self.minus):
            self.assertAlmostEqual((np.trace(e@state)/np.trace(state)).real,.5,places=13)
            self.assertAlmostEqual((np.trace(gauge_even@state)/np.trace(state)).real,1,places=13)
        # This twirl models a proposed gauge restriction; it does not prove
        # the concrete D/E swap and pointer flip are gauge in reality.

    def test_if_mirror_is_incidence_gauge_odd_valence_must_vanish(self):
        # Three actual model pointer settings are held fixed. If ± name the
        # SAME incidence, scalar well-definedness requires v(i,+)=v(i,-).
        # Mirror oddness says the opposite. Neither hypothesis follows merely
        # from a symmetry of the unselected physical state.
        for vals in product((-1,0,1),repeat=6):
            gauge=all(vals[2*i]==vals[2*i+1] for i in range(3))
            odd=all(vals[2*i]==-vals[2*i+1] for i in range(3))
            if gauge and odd:self.assertEqual(vals,(0,)*6)
        weights=[F(1,8),F(2,5),F(19,40)]
        paired=[(w/2,w/2) for w in weights]
        self.assertEqual(sum(a-b for a,b in paired),0)
        self.assertEqual(sum(a+b for a,b in paired),1)
        # Identifying the pair is an additional ontological choice; if the
        # partners are distinct incidences, odd nonzero valence is compatible.

    def test_pairing_and_direction_marginal_in_actual_clock_branches(self):
        q=np.array([1/8,2/5,19/40])
        states=[full_state(4),output(active_base()),output(compressed_spin_base(9))]
        for state in states:
            old=relative_read(state,4,labels=(0,))[0]
            branches,tab=outcome_tables(initial(old))
            np.testing.assert_allclose(tab,q[:,None]*np.ones((1,2))/32,atol=1e-13)
            self.assertAlmostEqual(sum(np.linalg.norm(x)**2 for x in branches),1/16,places=12)
        # In this whole circuit, q is an operational Born weight; equating it
        # with actual incidence weight is the separate bridge under study.

if __name__=='__main__':unittest.main()
