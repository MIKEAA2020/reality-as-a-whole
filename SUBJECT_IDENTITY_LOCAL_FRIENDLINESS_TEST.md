# Subject identity under a reversible observation: a quantitative gate

## Result and scope

We work through a **specific, idealized one-friend quantum circuit** motivated by the [supplied thoughtful Local Friendliness paper](THOUGHTFUL_LOCAL_FRIENDLINESS_SUBJECT_AUDIT.md). Its observable correlations are quantum-realizable and nonsignalling. Under two explicit additional assumptions about a single friend-event, every probability extension reproducing those correlations must have a quantifiable dependence hidden in an unobserved joint distribution. An explicit extension saturates the bound.

This is a worked specialization and a check, **not a new no-go theorem or a solution of quantum measurement**. The LF/CHSH constraints and contextuality/joint-distribution issues are established work: see [Wiseman, Cavalcanti and Rieffel (2023)](https://doi.org/10.22331/q-2023-09-14-1112), [Bong et al. (2020)](https://doi.org/10.1038/s41567-020-0990-x), and [Fine (1982)](https://doi.org/10.1103/PhysRevLett.48.291). The LF argument does **not** simply assume predetermined outcomes for all unperformed measurements. [Kent (2023)](https://arxiv.org/abs/2302.12707) already discussed the relevance of changing numbers of agents. Our limited contribution is the explicit rational example, the sharp cost for this chosen family, and a subject-selection diagnostic.

## 1. A concrete reversible circuit

Let `A` and `B` start in the Bell state `(|00⟩+|11⟩)/√2`; the friend's memory `M` starts at `|0⟩`. A CNOT from `A` to `M` gives `(|000⟩+|111⟩)/√2`, in the order `A,M,B`.

- Alice chooses `x=1`: read `Z_M`, with result `a=±1`.
- Alice chooses `x=2`: apply the inverse CNOT to `A,M`, then read `X_A`, result `a=±1`.
- Bob chooses `y=1` or `2`, measuring `(3 Z_B + 4 X_B)/5` or `(3 Z_B − 4 X_B)/5`, with result `b=±1`.

These are legitimate ±1 observables. The exact quantum correlators are:

| | Bob `y=1` | Bob `y=2` |
|---|---:|---:|
| Alice read `x=1` | `3/5` | `3/5` |
| Alice reverse `x=2` | `4/5` | `−4/5` |

All local outcome means are zero. Thus the observable joint distribution for each setting is `P(a,b|x,y)=[1+ab E_xy]/4` and is operationally nonsignalling. The CHSH expression is `S=3/5+3/5+4/5−(−4/5)=14/5 > 2`.

The circuit's qubit memory is **not** a human-level AI, not evidence of thought, and not a proven subject. It is the physical analogue used to make the probability issue explicit. The circuit and correlators are checked from matrices in [`verification/subject_friend_quantum_extensions.py`](verification/subject_friend_quantum_extensions.py).

## 2. The single-friend-event gate

Now **suppose**, independently of quantum mechanics, that for each trial there is a single absolute binary friend-event `c=±1` and a joint distribution `P(a,b,c|x,y)`. Impose just these two conditions:

1. **Read agreement:** when `x=1`, `a=c` with probability one. This identifies Alice's result with the same friend-event, not with a post hoc selected member of a collection.
2. **Remote joint independence from Alice's intervention:** `P(b,c|x=1,y)=P(b,c|x=2,y)` for each `y`. This is a consequence of the paper's Local Agency arrangement, where `b` and `c` are outside the future light cone of `x`. We do not assume factorization of `a` and `b` given `c`.

The read correlators then force `E(bc|x=2,y)=3/5` for both values of `y`. At `x=2`, the elementary facts `E(ac) ≥ E(ab)+E(bc)−1` and `E(ac) ≤ 1+E(ab)−E(bc)` for ±1 variables yield:

- `E(ac|x=2,y=1) ≥ 4/5+3/5−1 = 2/5`;
- `E(ac|x=2,y=2) ≤ 1−4/5−3/5 = −2/5`.

Consequently, **every** such extension obeys

`|E(ac|2,1) − E(ac|2,2)| ≥ 4/5`,

and therefore, since `ac` takes values in `[-1,1]`,

`TV[P(a,c|2,1), P(a,c|2,2)] ≥ 2/5`.

Here `TV` is total variation distance. Full Local Agency would require the distributions on the left to be equal, because both `a` and `c` are outside the future light cone of Bob's setting `y`. Thus, with read agreement and the Alice-setting independence above, this circuit's correlations are inconsistent with **full** Local Agency. This is an illustrative consequence of the established LF argument; it does not decide whether independence, read agreement, a unique friend-event, or some other premise should be abandoned.

### Why the dependence is not an observed faster-than-light signal

`c` is an additional postulated event, not a surviving readable memory in the reversal branch. The quantum-observed marginals `P(a|x,y)` and `P(b|x,y)` are independent of the remote settings. The TV distance concerns the **unobserved joint** `(a,c)` for `x=2`. If a further physical procedure could access both `a` and `c` in that same regime without changing the relevant statistics, the resulting joint dependence would matter operationally; this construction provides no such procedure. Local Agency also combines conditions beyond no-signalling, so the result does not by itself establish a controllable signal or select a causal explanation.

## 3. A sharp extension, not just an impossibility claim

The script explicitly defines `P(a,b,c|x,y)` and checks that it is nonnegative and normalized, gives `a=c` on read runs, preserves `P(b,c|y)` across Alice's settings and reproduces every quantum `P(a,b|x,y)` above. At `x=2` it uses the following conditional table. Let `f=ab`, `g=cb`; take `b=±1` uniformly, independently of the pair `(f,g)`:

| `(f,g)` | `y=1` | `y=2` |
|---|---:|---:|
| `(+,+)` | `7/10` | `1/10` |
| `(−,+)` | `1/10` | `7/10` |
| `(+ ,−)` | `2/10` | `0` |
| `(−,−)` | `0` | `2/10` |

In the read case take `c=a=gb`, with `P(g=+)=4/5` and `P(g=−)=1/5`. This gives `E(bc)=3/5` under either `x`, and in the reversal case gives `E(ac|2,1)=2/5`, `E(ac|2,2)=−2/5`. The hidden joint TV is exactly `2/5`, saturating the bound. Both `a` and `c` individually remain unbiased and independent of `y`; their **joint** distribution is not. The table is a probabilistic extension only: it supplies no local dynamical process, physical theory of `c`, subject identity or conscious event.

### Robustness within a declared noise family

For the isotropic family with all four listed correlators multiplied by visibility `v` in `[0,1]`, while local outcome means remain zero, the same two assumptions imply

`TV[P(a,c|2,1),P(a,c|2,2)] ≥ max(0, 7v/5 − 1)`.

For this particular family the bound is **tight**, not merely a loose estimate. At `v=5/7`, a mixture of four deterministic CHSH-boundary strategies gives a Local-Agency-compatible extension with `c=a` on read; below that, mix it with independent white noise. Above `5/7`, mix it with the sharp extension just displayed. The explicit distributions attain the bound for every `v` by construction. The script checks 102 exact rational visibility values including `5/7`; the affine mixture supplies the general argument, not the finite enumeration alone.

These are model-specific numbers. They are not estimated from the supplied paper's future experiment and are not measured phenomenological quantities.

## 4. What plurality can—and cannot—change

There are three distinguishable proposals:

### A. Plurality elsewhere, one identifiable Charlie

Many irreducible subjects may exist, but if there is still one specified `c` for Charlie, read agreement and the joint independence assumptions apply exactly as above. **Adding other subjects does not remove the gate.** Their existence says nothing by itself about `P(a,c|2,y)`.

### B. Two indexed friend-events, neither selected as the one Charlie in advance

As a logical bookkeeping counterexample, imagine two persistent labels `s+` and `s−` with absolute event values `c+=+1` and `c−=−1`. On a read run let the outcome `a` point to `s_a`, so `a=c_{s_a}`. Both labels can be present without postulating a split from a universal subject; the observable `P(a,b|x,y)` can still be the quantum table. The fixed pair `(c+,c−)` has no dependence on either setting and, jointly with `a`, has no dependence on `y` in this table.

But this construction does **not** satisfy the single-friend read premise: the identity `s_a` is specified **after** the read result, not independently singled out as the one friend whose event Alice reads. It is trivial to find an agreeing label if both possible labels are declared present. Nothing here says how both indexed events arise from the circuit, who or what has the experiences, how Alice connects to one of them, or why the selection has the Born distribution. No cognition, experience, physical supervenience, or lawful dynamics has been modeled. It is a diagnostic of the missing selector, not a viable many-subject interpretation or a counterexample to the paper's theorem.

If, instead, a unique label is fixed in advance and its event is the one Alice reliably reads, put its value back into `c`: the single-event gate applies again, subject to the two stated assumptions.

### C. Observer-relative event attribution

Another possible response is to treat the relevant event assignment as relative to a subject or context, not as the single absolute `c` used above. That removes or changes the joint-event premise; it does not require saying that nobody experiences anything. But simply adding an index is insufficient: a real proposal must state the compatible event relations, which comparisons are permitted, how agreement and reversal work, and how observable probabilities emerge. Neither this audit nor the supplied paper uniquely derives such a model.

**Research lesson:** a subject-first ontology must choose and defend a subject–event map *before* attributing quantum experiments to it. It may retain individually real experiences while reconsidering a global event assignment, but it cannot infer that the Local Friendliness contradiction vanishes merely from the word “plurality.” Alternatively, it may retain one absolute event and revise a locality/agency premise. Neither option currently follows from our metaphysics or the data alone.

## 5. Dependency-driven next step

The mathematically sharp question is now: **can an independently specified physical subject/record selector reproduce read agreement and quantum correlations while meeting a precisely declared local/relational event rule?**

1. Specify the ontology and variables *before* obtaining outcomes: subjects, events, physical correlates, identity through reversal, and what constitutes a read or comparison.
2. State which variables are absolute, subject-indexed or relational; do not define a selector by the result it is meant to explain.
3. Test the selector against the ideal circuit here, including the full joint Local Agency constraints—not only each observed marginal.
4. Independently check duality/representation consistency where applicable, then connect to neuroscience or AI only with evidence for a candidate subject and its phenomenal states.

A subsequent [record-complementarity audit](REVERSIBLE_FRIEND_RECORD_COMPLEMENTARITY.md) tests a stronger candidate requirement—an independently readable external friend-outcome record—against a four-qubit extension of this circuit. It derives a model-specific record/interference tradeoff but does not establish that real experiences require such a record. This work does not yet provide a selector, derive experience from physics, demonstrate conscious AI, resolve the problem of time, or establish the user's target of a zero-residue account. It narrows a particular structural gap.
