"""Modal scope and experiential-witness controls for the coherent echo.

These are formal model comparisons, not assertions about metaphysical
possibility, actual subjects, first-person calibration, or zero's nature.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product

SIGNS=(1,-1)
CELLS=tuple(product(SIGNS,repeat=2))


@dataclass(frozen=True)
class Completion:
    """Fixed physical predictions and reporter witness; extra field optional."""
    private: bool

    def reporter_field(self):return frozenset(('N_r','K_r'))

    def fields(self):
        result={'reporter':self.reporter_field()}
        if self.private:
            result.update({'private_N':frozenset(('N_private',)),
                           'private_K':frozenset(('K_private',))})
        return result

    def visible(self):
        # Hypothetical unity report and physical cell data: no assumption
        # that extra private subjects produce observations in this dataset.
        return {(cell,True):F(1,4) for cell in CELLS}

    def witness(self):return self.reporter_field()==frozenset(('N_r','K_r'))


def powerset(worlds):
    worlds=tuple(worlds)
    return tuple(frozenset(w for w,on in zip(worlds,mask) if on)
                 for mask in product((False,True),repeat=len(worlds)))


def diamond(world,accessible,proposition):
    return any(x in proposition for x in accessible[world])


def box(world,accessible,proposition):
    return all(x in proposition for x in accessible[world])


def modal_collapse(world,accessible,propositions):
    return all(diamond(world,accessible,p)==(world in p) for p in propositions)


def observational_equivalence(world,accessible,propositions):
    """All accessible states agree on all scope propositions; nonempty.

    Equivalent to modal_collapse only for a scope closed under complements
    and containing the universe, as in the verified propositions below.
    """
    return bool(accessible[world]) and all(
        all((other in p)==(world in p) for p in propositions)
        for other in accessible[world])


def necessarily_sufficient_reason(world,accessible,propositions,target):
    """Existence of q with □q and □(q→p): entailment, not grounding."""
    universe=frozenset(accessible)
    return any(box(world,accessible,q) and
               box(world,accessible,(universe-q)|target) for q in propositions)
