# Fixed follow-up: the public PAINgen task's prompt-order assignment

## Timing and scope

After the [source-discovery plan](PAINGEN_ORIGINAL_RECORDS_SOURCE_DISCOVERY_PLAN.md), the public candidate task source was inspected. Its testing generator makes 16 alternating warning/pain sequence rows, draws a permutation of eight `[intensity, unpleasantness]` and eight `[unpleasantness, intensity]` order vectors, then assigns one vector to each row; only the eight pain rows have the two actual rating labels. The published and prior BIDS aggregate order counts are known, and the candidate source's correspondence to deployed experiment versions is not independently established. No original MAT outcomes, individual BIDS rows or additional participant data were inspected in this follow-up.

## Fixed calculation

Assume, for the mathematical control only, that the permutation is uniform over the 16 labeled vectors, all eight pain positions are retained, and labels are distinct. Exactly count the probability mass function of the number K of intensity-first orders assigned to the eight pain rows, for K=0,...,8, by exhaustive enumeration of the `C(16,8)` subsets of positions assigned intensity-first. Verify against the hypergeometric formula `C(8,k) C(8,8−k) / C(16,8)`, compute mean and variance as exact fractions, `P(K=4)`, `P(3≤K≤5)`, and `P(K=0 or 8)`. Compare it to independent fair-coin assignment via its variance and all-same probability; that comparison is an abstract design implication, not a claim of an observed order effect or an audit of the actual software's random number generator.

The program must treat painful and warning slots separately and assert both total vector counts and that pain slots receive two nonempty prompts. Test the exact count table, normalization, symmetry and moments. A missing stimulus or nonstandard executed version changes the analysis; do not infer that each run has four of each order, that trials are independent or that an individual participant's observed sequence was randomly assigned as assumed.
