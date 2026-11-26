# Can a local reporter justify the pure-state incidence rule?

## The issue and result

The preceding [incidence-balance investigation](ZERO_ECHO_INCIDENCE_BALANCE_ROOT_CAUSE.md) found that event-dependent type weights are impossible if positive type blocks must sum to the **same globally pure physical state** for every physical effect. But its diagonal-only counterexample used a weaker physical constraint. The diagnostic question is: does granting a reporter *all* effects on the part it can access restore the strong conclusion?

**Not in general.** In the existing echo with the separately added saved-J memory, that memory's actual reduced state is mixed even though the specified memory-plus-old-carrier state is pure. Two positive type blocks can sum to the **same reduced density matrix**, and therefore agree on every untyped qubit effect on that memory, while assigning different conditional type weights. They cannot also sum to the same globally pure state. A joint coherence-sensitive physical effect can distinguish the different global extensions, if the required joint access is available.

This is a scope correction, not a refutation of global purity. If the full pure marginal and positive global type blocks are independently justified, their proportionality follows regardless of an observer's access. Conversely, a locally mixed marginal does not by itself prove that the actual global state is mixed, or that the formal type labels represent real subjects or experiences.

## 1. The actual saved record supplies a concrete mixed subsystem

Use the earlier [saved-J memory protocol](ZERO_ECHO_SUBJECT_PERSISTENCE_RECORD_AND_ACCESS.md), **not** the unmodified echo alone. A new ready two-state memory L is coherently coupled to the pre-echo J sign, then the actual T–Q–T sequence acts on the original carrier. The old calculation checks source labels 0, 7 and 15 and both pointer signs, and finds in each normalized sign slice

```text
P(L=+) = 3/4,       P(L=−) = 1/4.
```

The new [verification](verification/zero_echo_accessible_marginal_root_test.py) additionally checks that the two actual old-carrier record vectors are orthogonal after the echo. Therefore, in a Schmidt basis adapted to those **actual** vectors, the specified pure recorded state and its memory marginal are

```text
|Ψ⟩ = (√3/2)|+⟩_L |e₊⟩ + (1/2)|−⟩_L |e₋⟩,
⟨e₊|e₋⟩ = 0,       ρ_L = diag(3/4,1/4).
```

The four-dimensional Schmidt-coordinate model below represents this one sign slice and the added record. It is not a claim that the entire old system, clock, apparatus or universe is four-dimensional. The memory and its coupling are added physical resources. The earlier code also found fidelity `5/8` between the original unrecorded pure old-carrier state and the old-carrier state after L is traced out. That is a comparison on the **old carrier**, not the global comparison made in section 3.

## 2. Every effect on L can agree while type assignments differ

Suppose, as a formal hypothesis, that two positive type blocks must reproduce all *untyped* effects on L:

```text
A_N + A_E = ρ_L.
```

One possibility is the product pair `A_N=A_E=ρ_L/2`. Another is

```text
A_N = diag(7/16, 1/16),     A_E = diag(5/16, 3/16).
```

Both pairs are positive, each type has total weight 1/2, and **every** qubit effect E on L has the same untyped expectation `Tr(Eρ_L)` in the two proposals. Yet for the second pair

```text
P(N|L=+) = 7/12,       P(N|L=−) = 1/4,
```

rather than 1/2 in both cases. Thus moving from diagonal event queries to the *entire local qubit effect algebra* does not make local type blocks proportional when the local density is mixed.

The freedom is larger than this diagonal example. For a Hermitian block `A_N=[[a,c],[c*,b]]`, both blocks are positive exactly when the diagonal entries of both are nonnegative and

```text
|c|² ≤ ab,           |c|² ≤ (3/4−a)(1/4−b).
```

For example, `A_N=ρ_L/2 + X/8` and `A_E=ρ_L/2 − X/8` are positive. Their untyped X expectation is zero, while their **type-conditioned** unnormalized X expectations are +1/4 and −1/4. Type-conditioned queries require access to the type as well as to L; the agreement claim concerns untyped effects only.

These are formal decompositions of a local physical density, not a derivation of an incidence law. If actual subject–quality relations are not represented by positive type blocks in this way, the calculation does not settle them.

## 3. What is hidden from L is not necessarily hidden globally

On the Schmidt-coordinate carrier, a positive global extension of the correlated local blocks is

```text
Σ_N = (7/16)|+e₊⟩⟨+e₊| + (1/16)|−e₋⟩⟨−e₋|,
Σ_E = (5/16)|+e₊⟩⟨+e₊| + (3/16)|−e₋⟩⟨−e₋|.
```

Their sum is the **dephased** recorded state, not `|Ψ⟩⟨Ψ|`. Both have the same reduced `ρ_L`, so no measurement on L alone distinguishes them. However, the joint Hermitian observable

```text
C = |+e₊⟩⟨−e₋| + |−e₋⟩⟨+e₊|
```

has expectation `√3/2` in `|Ψ⟩` and 0 in the dephased state. The projector `|Ψ⟩⟨Ψ|` has expectation 1 versus `5/8`. In this Schmidt model the global trace distance is `√3/4`, giving optimal single-shot discrimination probability `(4+√3)/8` for equal priors. That optimum assumes arbitrary joint physical access to the old carrier and memory; the modeled reporter is **not** shown to possess it.

The `5/8` here is the overlap of the **global recorded pure state** with its dephased global alternative. It equals the previous old-carrier fidelity because the same Schmidt weights enter both computations; the two operational comparisons should not be conflated. The existing physical protocol also permits coherent inverse operations and uncomputation, but a coherence-sensitive global test requires the relevant phase reference, joint operations and preparation. Mathematical existence of C is not an established accessible laboratory gate or evidence of subjecthood.

If one instead insists that the positive global blocks sum to the original pure `|Ψ⟩⟨Ψ|`, positivity forces them to be `α|Ψ⟩⟨Ψ|` and `(1−α)|Ψ⟩⟨Ψ|`. Their local reductions are then also proportional to ρ_L. Limited access does not overturn this theorem; it shows why local measurements alone cannot select that stronger premise over all other global extensions.

## 4. What would a type-sensitive report add?

Compare the two local type proposals with an additional **ideal physical tag** that records the hypothesized type. The joint tag–memory table has

```text
                 L=+      L=−
N                7/16     1/16
E                5/16     3/16
```

instead of the product table `(3/8,1/8)` in each type row. Ignoring the tag yields exactly the same memory density; reading both the tag and memory distinguishes the two tables with total variation `1/8`, or best single-shot success `9/16` with equal prior probabilities.

This is an explicit **conditional instrument design**, not an existing report in the echo. A real tag requires a physically realizable interaction sensitive to the relevant type; the construction has not supplied one. In particular, labeling a block “N” or “E” does not make it a reportable subject, make an experience third-person observable, or justify an accuracy calibration. Exporting an ideal type tag may disturb the physical state or add a new carrier; these costs and the effect algebra must be specified. It is not a device for reading an unproved phenomenal property by definition.

Nor can L alone be assumed to contain the earlier quality signs. In the specified **commuting physical sign-readout table**, the best guesses of `Q_now` or `Q_echo` from saved z alone each succeed with probability 1/2. Adding the pointer sign s to z makes the echo-sign query exact in that table. These are physical model probabilities for stated readouts, not universal quantum-access bounds or first-person report accuracies.

## 5. Recursive diagnosis and remaining constitutive question

1. **Why did the local type freedom reappear?** Partial access maps a pure global state to a mixed reduced state. Mixed density matrices are not extremal and admit many positive decompositions.
2. **Why can all local effects miss it?** The untyped accessible expectation depends on the sum of the blocks. Type correlations and global coherence are not specified by that sum; an added type-sensitive query is a different effect.
3. **Why not conclude that the original pure echo has event-dependent incidence weights?** The correlated extension in section 3 changes the global physical state. Under positive all-effect consistency with the fixed globally pure state it is inadmissible. Local ignorance does not change that mathematical fact.
4. **Why not simply impose the global rule?** The program must explain which physical state is actually fixed, whether the full relevant physical–experiential incidence algebra admits such positive blocks, and why all-effect consistency applies to actual occurrences rather than only to a selected reporter or effect algebra. The prior full-clock purification and physical echo checks are evidence about specified formal states, not by themselves a derived ontology.
5. **Meta-level issue:** physical carrier, accessible report, subject identity and incidence measure must be determined together. Neither an arbitrary hidden local decomposition nor a stipulated global type tag constitutes a subject. A common constitutive principle might determine them; these examples neither derive nor rule out it.

For the next investigation, compare an explicitly defined reporter/ownership bridge with the **same** complete physical state and a stated class of accessible interventions. A difference in raw block labels is not enough; a discriminating physical or first-person report needs an independently justified connection to the proposed occurrence. Preserve genuine plurality and negative experience if that bridge is eventually established.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_echo_accessible_marginal_root_test \
  verification.zero_echo_subject_persistence_test \
  verification.zero_echo_incidence_balance_root_test -v
```

The verifier checks the stated finite matrices, effect equality, coherence distinction, tagged-table statistics and original recorded complex vectors. It does not establish actual reporters, subjects, experiential type weights, cosmic energy, or self-sufficient constitution.
