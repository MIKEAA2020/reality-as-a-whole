#!/usr/bin/env python3
"""Finite partition illustration, not a model that produces consciousness."""
from itertools import permutations
from pathlib import Path
import json


def partitions(items):
    """Each unordered set partition once, as frozensets of frozensets."""
    items = tuple(items)
    if not items:
        yield frozenset()
        return
    first, *rest = items
    for p in partitions(rest):
        yield p | frozenset([frozenset([first])])
        for block in p:
            yield (p - frozenset([block])) | frozenset([block | {first}])


def valid_time_partition(partition):
    return all(len({t for _, t in block}) == len(block) for block in partition)


def edge_supported(partition):
    return all(len(block) == 1 or (len(block) == 2 and len({x for x, _ in block}) == 1)
               for block in partition)


def relabel(partition, permutation):
    return frozenset(frozenset((permutation[x], t) for x, t in block) for block in partition)


def partition_from_mask(n, mask):
    blocks = []
    for i in range(n):
        if mask & (1 << i):
            blocks.append(frozenset(((i, 0), (i, 1))))
        else:
            blocks.extend((frozenset(((i, 0),)), frozenset(((i, 1),))))
    return frozenset(blocks)


def run():
    events = tuple((i, t) for i in range(2) for t in (0, 1))
    ps = list(partitions(events))
    assert len(ps) == len(set(ps)) == 15
    time_ok = [p for p in ps if valid_time_partition(p)]
    supported = [p for p in time_ok if edge_supported(p)]
    swap = (1, 0)
    invariant = [p for p in supported if relabel(p, swap) == p]
    assert (len(time_ok), len(supported), len(invariant)) == (7, 4, 2)
    general = []
    for n in range(1, 5):
        candidates = [partition_from_mask(n, mask) for mask in range(1 << n)]
        stable = [p for p in candidates if all(relabel(p, perm) == p
                                                 for perm in permutations(range(n)))]
        assert len(stable) == 2
        general.append({'parallel_paths': n, 'edge_supported_groupings': len(candidates),
                        'permutation_invariant_groupings': len(stable)})
    return {'scope': 'partition semantics for four stipulated event tokens; not evidence of subjects',
            'all_four_event_partitions': len(ps),
            'at_most_one_per_time': len(time_ok),
            'and_edge_supported': len(supported),
            'and_exchange_invariant': len(invariant),
            'general_parallel_examples': general,
            'two_exchange_invariant_extremes': ['no temporal links', 'all temporal links']}


if __name__ == '__main__':
    report = run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))
