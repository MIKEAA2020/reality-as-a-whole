"""Exact conditional identity, scalar and balance results on the echo."""
from fractions import Fraction as F
from itertools import product, combinations
import unittest
import numpy as np

from verification.zero_echo_joint_identity_balance import (
    EVENTS,signature,content_classes,optimal_event_guess,physical_ledger,
    moment,candidate_slot,scalar_value,expanded_weight,expanded_total,invariant_measure,
    factor_swap_invariant)
from verification.zero_joint_quality_incidence_root import (
    J,R,quality,weight,swap,counterpart)
from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_coherent_clock_angular_history import quantum_echo_checkpoints
from verification.zero_internal_reference_subject_valence_candidates_test import j_project
from verification.zero_persistent_sphere_subject_selection_test import norm2
from verification.zero_echo_subject_persistence import copy_initial_j,evolve_record


def partitions(seq):
    """Enumerate unlabeled partitions; Bell(8)=4140."""
    if not seq:
        yield []
        return
    first,*rest=seq
    for p in partitions(rest):
        yield [[first]]+[block[:] for block in p]
        for k in range(len(p)):
            out=[block[:] for block in p]
            out[k].append(first)
            yield out


class EchoJointIdentityBalanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.root=output(active_base())

    def test_content_quotients_and_physical_event_discrimination(self):
        cases=[(('now','echo'),4,F(1,2)),
               (('now','echo','magnitude'),6,F(3,4)),
               (('now','echo','pointer'),6,F(3,4)),
               (('now','echo','pointer','magnitude'),8,F(1))]
        for fields,count,p in cases:
            self.assertEqual(len(content_classes(fields)),count)
            self.assertEqual(optimal_event_guess(fields),p)
            self.assertEqual(sum(sum(weight(*x) for x in cell)
                                 for cell in content_classes(fields).values()),1)
        qg=('now','echo','magnitude')
        self.assertEqual(signature(0,1,qg),signature(1,-1,qg))
        self.assertNotEqual(signature(0,1,('pointer',)),signature(1,-1,('pointer',)))
        # Scores apply to the specific commuting record fields and eight equal
        # weighted events; they are not bounds on arbitrary quantum POVMs.

    def test_kernel_is_coarsest_content_preserving_equivalence(self):
        fields=('now','echo','magnitude');count=valid=0
        for blocks in partitions(list(EVENTS)):
            count+=1
            if not all(len({signature(*e,fields) for e in block})==1 for block in blocks):
                continue
            valid+=1
            for block in blocks:
                kernel=content_classes(fields)[signature(*block[0],fields)]
                self.assertTrue(set(block)<=set(kernel))
        self.assertEqual(count,4140)
        self.assertEqual(valid,4) # two two-element cells may each be split

    def test_content_kernel_respects_two_physical_transformations(self):
        for x in EVENTS:
            q=signature(*x,('now','echo','pointer','magnitude'))
            sw=signature(*swap(*x),('now','echo','pointer','magnitude'))
            cp=signature(*counterpart(*x),('now','echo','pointer','magnitude'))
            self.assertEqual(sw,(q[1],q[0],q[2],q[3]))
            self.assertEqual(cp,(-q[0],-q[1],-q[2],q[3]))
            # Sign and type are active maps, not declared gauge equivalences.

    def test_scalar_classification_and_contextual_loophole(self):
        # Exhaust all functions on the four sign pairs with values -1,0,1.
        cells=((1,1),(1,-1),(-1,1),(-1,-1))
        survivors=0
        for vals in product((-1,0,1),repeat=4):
            f=dict(zip(cells,vals))
            if not all(f[-a,-b]==-f[a,b] and f[b,a]==f[a,b] for a,b in cells):
                continue
            survivors+=1
            for i,s in EVENTS:
                self.assertEqual(f[quality(i,s)],scalar_value(i,s,f[1,1],0))
                if R[i]==-1:self.assertEqual(f[quality(i,s)],0)
        self.assertEqual(survivors,3)
        # For an odd scalar depending on Q only, a,b are independent until
        # swap invariance forces b=0; dropping invariance allows nonzero both.
        for i,s in EVENTS:
            self.assertEqual(scalar_value(*counterpart(i,s),2,3),-scalar_value(i,s,2,3))
            self.assertEqual(scalar_value(*swap(i,s),2,0),scalar_value(i,s,2,0))
            self.assertNotEqual(scalar_value(i,s,1,1),0)
        # Full physical pointer s is odd under counterpart and invariant under
        # type exchange, but is not a function of Q plus magnitude alone.
        self.assertEqual(signature(0,1,('now','echo','magnitude')),
                         signature(1,-1,('now','echo','magnitude')))
        self.assertEqual(swap(0,1),(1,1))
        for i,s in EVENTS:
            self.assertEqual(swap(i,s)[1],s)
            self.assertEqual(counterpart(i,s)[1],-s)

    def test_saved_ledger_allows_persistent_owner_with_changing_quality(self):
        self.assertEqual(len({physical_ledger(*x) for x in EVENTS}),8)
        for i,s in EVENTS:
            moments=[moment(i,s,t) for t in range(4)]
            self.assertEqual(len({m['ledger'] for m in moments}),1)
            self.assertEqual(len({m['occurrence_slot'] for m in moments}),4)
        self.assertEqual([moment(0,1,t)['quality'] for t in range(4)],
                         [(-1,-1),(-1,1),(1,-1),(1,-1)])
        # Associating this ledger with a persistent owner is a hypothesis;
        # equality of its labels is not a measured subject-identity fact.

    def test_single_joint_slot_candidate_and_owner_measure(self):
        pi=(F(1,10),F(2,10),F(3,10),F(4,10))
        slots=[candidate_slot(i,s,t,pi) for i,s in EVENTS for t in range(4)]
        self.assertEqual(len(slots),32)
        self.assertEqual(sum(x['weight'] for x in slots),1)
        for t in range(4):
            current=[x for x in slots if x['slot'][2]==t]
            self.assertEqual(sum(x['weight'] for x in current),pi[t])
            self.assertEqual(len({x['content'] for x in current}),8)
        for i,s in EVENTS:
            rows=[x for x in slots if x['slot'][:2]==(i,s)]
            self.assertEqual(len({x['owner'] for x in rows}),1)
            self.assertEqual(sum(x['weight'] for x in rows),F(1,8))
            for x in rows:
                a,b=x['pair']
                self.assertEqual(tuple(v+w for v,w in zip(a,b)),(0,0))
        with self.assertRaises(ValueError):candidate_slot(0,1,0,(1,1,1,1))
        # This construction proposes the link; it cannot establish actual
        # occurrence, an experiencing owner, or the clock sampling law.

    def test_saved_ledger_matches_actual_coherent_checkpoints(self):
        for label,s in product((0,7,15),(1,-1)):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            _,total,states=quantum_echo_checkpoints(x,s,4)
            record=copy_initial_j(states[0])
            for t in range(4):
                for i in range(4):
                    z_expected=R[i]*J[i]
                    info=moment(i,s,t);j,r=info['j'],info['r']
                    for z in (1,-1):
                        rows=record[z]
                        parts=(rows[0][i],rows[1][i])
                        cell=sum(norm2(v) for v in parts)/total
                        if z!=z_expected:
                            self.assertLess(cell,1e-23)
                            continue
                        self.assertAlmostEqual(cell,F(1,4),places=12)
                        correct_index=0 if r==1 else 1
                        self.assertLess(norm2(parts[1-correct_index])/total,1e-23)
                        v=parts[correct_index]
                        self.assertLess(norm2(j_project(v,j)-v)/total,1e-23)
                        self.assertEqual(info['quality'],(s*j,s*j*r))
                if t<3:record=evolve_record(record,(('T','Q','T')[t],))

    def test_balances_form_a_strict_hierarchy(self):
        equal={x:F(1,2) for x in EVENTS}
        biased={x:F(3,4) for x in EVENTS}
        for model in (equal,biased):
            self.assertEqual(sum(expanded_weight(*x,k,model) for x in EVENTS for k in (1,2)),1)
            for x in EVENTS:
                self.assertEqual(sum(expanded_weight(*x,k,model) for k in (1,2)),weight(*x))
            self.assertTrue(invariant_measure(model))
            # Every counterpart-invariant event E is a union of full sign pairs.
            for subset in product((False,True),repeat=4):
                E=[(i,s) for i in range(4) if subset[i] for s in (1,-1)]
                self.assertEqual(expanded_total(model,E),(0,0))
        self.assertTrue(factor_swap_invariant(equal))
        self.assertFalse(factor_swap_invariant(biased))
        # A sign-selective query is not invariant under the counterpart.
        self.assertEqual(expanded_total(biased,[(i,1) for i in range(4)]),
                         (F(13,128),F(13,128)))
        # Non-invariant incidence can nevertheless have zero global sum.
        hidden=dict(equal)
        for i in (0,1):hidden[i,1]=F(3,4);hidden[i,-1]=F(1,4)
        self.assertFalse(invariant_measure(hidden))
        self.assertEqual(expanded_total(hidden),(0,0))
        self.assertEqual(expanded_total(hidden,[(0,1),(0,-1)]),
                         (F(3,128),F(-3,128)))

    def test_event_dependent_weights_lose_global_pure_coherence(self):
        # Isometric branch representation of one fixed-sign coherent echo:
        # the four angular projectors are orthogonal and each has weight 1/4.
        ket=np.ones(4)/2
        rho=np.outer(ket,ket)
        lambdas=np.array([.75,.75,.5,.5])
        block1=np.diag(lambdas/4)
        block2=np.diag((1-lambdas)/4)
        mixed=block1+block2
        self.assertTrue(np.allclose(np.diag(mixed),np.diag(rho)))
        self.assertAlmostEqual(np.trace(rho@mixed),.25)
        self.assertAlmostEqual(np.sum(abs(np.linalg.eigvalsh(rho-mixed)))/2,.75)
        self.assertTrue(np.all(np.linalg.eigvalsh(block1)>=0))
        self.assertTrue(np.all(np.linalg.eigvalsh(block2)>=0))
        # The pure-state alternative has a constant factor share, here 3/4,
        # while preserving every effect of the coherent pure state.
        full1=.75*rho;full2=.25*rho
        self.assertTrue(np.allclose(full1+full2,rho))
        self.assertTrue(np.allclose(np.diag(full1)/np.diag(rho),.75))
        self.assertFalse(np.allclose(np.diag(block1)/np.diag(rho),.75))

    def test_counterpart_invariance_is_necessary_for_each_bin_pair(self):
        for plus,minus in product((F(0),F(1,4),F(1,2),F(3,4),F(1)),repeat=2):
            model={x:F(1,2) for x in EVENTS}
            model[2,1]=plus;model[2,-1]=minus
            zero=expanded_total(model,[(2,1),(2,-1)])==(0,0)
            self.assertEqual(zero,plus==minus)

if __name__=='__main__':unittest.main()
