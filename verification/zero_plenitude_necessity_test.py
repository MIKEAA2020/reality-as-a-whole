"""Finite semantic controls, not a proof of metaphysical necessity."""
import itertools
import unittest


def all_propositions(worlds):
    for flags in itertools.product((False,True),repeat=len(worlds)):
        yield {w for w,flag in zip(worlds,flags) if flag}


def possible(accessible,proposition): return any(w in proposition for w in accessible)
def necessary(accessible,proposition): return all(w in proposition for w in accessible)


def possibility_actuality_at(world,accessible,propositions):
    return all(possible(accessible,p)==(world in p) for p in propositions)


class PlenitudeNecessityTests(unittest.TestCase):
    def test_single_totality_satisfies_strong_modal_schema(self):
        worlds=[0]; props=list(all_propositions(worlds)); accessible={0}
        self.assertTrue(possibility_actuality_at(0,accessible,props))
        for p in props:
            self.assertEqual(necessary(accessible,p),0 in p)

    def test_distinct_global_alternatives_break_schema_in_full_propositional_language(self):
        worlds=[0,1]; props=list(all_propositions(worlds)); accessible={0,1}
        self.assertFalse(possibility_actuality_at(0,accessible,props))
        self.assertTrue(possible(accessible,{1}))
        self.assertNotIn(0,{1})

    def test_restricted_language_cannot_identify_entire_totality(self):
        # Both alternatives contain experience but differ on another actual fact.
        restricted=[set(),{0,1}]
        self.assertTrue(possibility_actuality_at(0,{0,1},restricted))
        self.assertFalse(possibility_actuality_at(0,{0,1},list(all_propositions([0,1]))))

    def test_one_necessary_whole_can_contain_different_local_experiences(self):
        experiences={'pain','pleasure'}
        whole_facts={'some_pain': 'pain' in experiences,'some_pleasure': 'pleasure' in experiences,
                     'all_pain': experiences=={'pain'}}
        self.assertTrue(whole_facts['some_pain'])
        self.assertTrue(whole_facts['some_pleasure'])
        self.assertFalse(whole_facts['all_pain'])
        # Their distinct indexical contents need not be assigned to one occurrence.
        self.assertNotEqual('pain','pleasure')

    def test_deterministic_local_law_can_have_distinct_global_solutions(self):
        histories={(0,0,0),(1,1,1)}
        self.assertTrue(all(h[1]==h[0] and h[2]==h[1] for h in histories))
        self.assertEqual(len(histories),2)

    def test_unique_global_structure_does_not_force_single_successor_rule(self):
        # Illustrative fixed relational graph, not a physical quantum model.
        total_structure={('start','left'),('start','right')}
        successors={v for u,v in total_structure if u=='start'}
        self.assertEqual(len(successors),2)
        self.assertEqual(len([total_structure]),1)

    def test_negative_experience_not_erased_by_zero_total(self):
        valences=[-1,1]
        self.assertEqual(sum(valences),0)
        self.assertIn(-1,valences)
        self.assertTrue(any(v<0 for v in valences))


if __name__=='__main__': unittest.main()
