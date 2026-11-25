# A subject boundary through memory writing, use and attempted erasure

**Main result.** On the existing quantum history, a memory written from the disturbed record and later subjected to the same write operation does **not** return to blank if the intervening compatible Q operation has changed that record. Instead, it becomes an exact record of the conserved sphere sign. This is an operator identity, checked on all 16 histories without inserting a collapse. If the memory is also used to control the sign pointer, the original sign remains recoverable from a different joint observable: the information is transported, not simply lost.

A concrete interaction-support boundary test then gives incompatible answers under two existing candidate selection rules. Both describe the same stipulated gates, not two different histories. Neither selects the formerly assumed sphere-plus-pointer carrier throughout. The result makes the boundary problem operationally sharper but does not derive an experiencing subject or show that any graph rule is correct.

This continues [the persistent-carrier test](ZERO_PERSISTENT_CARRIER_AND_SIGN_SELECTION.md) and [the common-domain quality comparison](ZERO_INTERNAL_REFERENCE_SUBJECT_VALENCE_COMPARISON.md). The executable checks are in [the new verifier](verification/zero_dynamic_subject_memory_echo_test.py).

## 1. Physical episode and notation

Use the same valid projector P, conserved sphere sign B, old record Zj, internal sign observable O, dressed gauge G̃ and sign-writing gate W as before. On P, `O²=P`; O commutes with B and G̃. The original gate W writes `s=±1` to the sign pointer M. Define the previously tested later operation `Q=I−P+O`, which is unitary and preserves the stated gauge, B and old clock/work constraints.

Add a neutral memory qubit R, ready in `Z_R=+1`. Its write T is the controlled NOT with j as control and R as target. T is self-inverse, gauge compatible, and preserves B and Zj. On commuting Z labels it sends

```text
T: (b,z,s,r) → (b,z,s,z r).
```

On the valid sector Q leaves b, s and r fixed and maps `z→bz`. These are exact transformations of commuting observables, not an assumption that a measured classical path existed in the unobserved quantum state. Q is a specified physical intervention with no established implementation cost; the modeled conserved constraints are not asserted to be objective whole-energy.

## 2. Exact coherent memory echo

First run W, then T, then Q, then T again. The last T is an **attempted unwrite**. On the relevant commuting observables the transformation is

| Stage | b | j sign | M sign | memory R sign |
|---|---:|---:|---:|---:|
| after W, R ready | b | z | s | + |
| after write T | b | z | s | z |
| after Q | b | b z | s | z |
| after attempted unwrite T | b | b z | s | b |

Thus the operation that would unwrite the memory if the record had not changed instead writes **B into R**. More strongly, with `P_{B−}=P(I−B)/2` and `C_B=(I−P_{B−})⊗I_R+P_{B−}⊗X_R`, the verifier proves on the *entire* modeled operator space, including the inactive complement,

```text
T (Q⊗I_R) T = (Q⊗I_R) C_B.
```

On the valid sector C_B copies B into a ready R. On the inactive complement Q is identity and the two T gates cancel. With Q omitted, `T²=I` and the memory is genuinely restored for every state. No measurement, readout, decoherence or presumed hidden trajectory is needed for either identity.

For each actual relative-clock history, the first write gives `P(r=+)=3/4`, `P(r=−)=1/4`. After the echo, `r=b` exactly and both signs have Born weight 1/2. The final joint table is

```text
P(j=+, r=+)=1/2;  P(j=−, r=−)=1/4;  P(j=+, r=−)=1/4.
```

In a normalized pure conditional input history including the pointer and all other factors, R's final reduced state is maximally mixed, so it is entangled with the remaining system by one qubit entropy. This is an information statement, not one unit of experience. The attempted unwrite has neither returned R to its ready state nor erased the earlier information from the total closed state: the initial z can be recovered as `z=(final j)(final r)`.

The result also warns against assuming an inhabitant can access that information. R is an added apparatus; the construction does not supply a communication path to a confined subject or an intrinsic phenomenal interpretation.

## 3. Actually using the memory

As a separate, fully coherent variant, insert a CNOT from **R to M** after the first T and before Q. It uses the memory to change the sign pointer. This operation is neutral under G̃ and commutes with the pointer-flip part of the stated counterpart transformation. The exact diagonal-label transport becomes

```text
initial: (b,z,s,r=+)  →  final: (b, j'=b z, m'=s z, r'=b).
```

Consequently the original sign is recoverable as `s=m' r' j'`. The verifier constructs the coherent M,R amplitude slices for all 16 histories and checks this relation, not only a table of measured probabilities. These commuting observables can be measured jointly at the end, but physical access to all three is still an independent interface premise. The final M value **is not** the old s by itself.

This exposes a concrete link between boundary and experience candidates. Before memory use, the prior bridges are `v_B=κ s b` and `v_memory=κ s b r`. After the complete use-and-echo protocol, on the actual valid output `r'=b`, so their transported values can be expressed as

```text
v_B      = κ m' j',
v_memory = κ m' r' j' = κ s.
```

They disagree when b=−, with Born weight **1/2**. The expression in final observables is an exact transport of these *stipulated* quality rules, not a claim that the unitary makes the rules felt. Whether a putative subject can access j or R, and whether those factors are intrinsic to it, changes what it can report or retain. A stable carrier label alone does not answer either question.

## 4. A physical back-action that a classical copy misses

The R write is not merely a one-way classical connection. Let `D=O P_{B−}`, a nonzero **joint** old-reference/sphere/record observable. It is invariant under the stipulated dressed gauge. The exact write satisfies

```text
T† (D⊗I_R) T = D⊗X_R.
```

On each actual s, b=− branch, the verifier checks that preparing R in an X eigenstate + or − makes the sharp D outcome respectively `s` or `−s`. These are alternative, controlled R preparations, not the originally ready `Z_R=+` history. They show a possible influence from R to a gauge-invariant **joint** observable. They do not show that a sphere-only inhabitant can prepare R, observe D or receive this influence.

A naive local graph based on a bare `X_j` perturbation would be misleading here: `X_j` is odd under G̃ and is not by itself an admissible gauge-invariant observable. The joint dressed D is admissible, but it is not local to j or to the proposed sphere-plus-pointer carrier. Thus deriving a dynamical boundary requires specifying the allowed intervention algebra and accessible interfaces, not just reading off a circuit drawing.

## 5. Two explicit boundary rules on the same gates

For a transparent diagnostic, group the *encoded 64-dimensional old reference/work factor* as K, and use four qubit factors B, j, M, R. K is a coarse factor, not a demonstrated subject; other registers of the whole history, including Alice's record, are not analyzed as potential subject members here. On this factorization the specified gate supports are

```text
sign W:      {K,B,j,M}        memory write T: {j,R}
memory use:  {M,R}            pulse Q:        {K,B,j}
attempted unwrite T: {j,R}.
```

These are multibody **gate-support hyperedges**. The verifier checks the decomposed O, the actual gate algebra and the memory-use unitary. A gate can have conditional or genuinely multibody action: the hyperedge is not a measurement of all-pairs causal influence.

To make the competing rules executable, give every gate occurrence one unit and expand each hyperedge into a clique, summing co-occurrences over the stated window. This is a specified coarse-graining convention, **not** a derived Hamiltonian strength, timescale, gauge-local causal graph or measure of consciousness. Compare the repository's connected-component rule C and its strict overlapping-local-minimum-cut rule L; singleton inactive nodes are omitted, ties are reported rather than arbitrarily broken.

| Window | Rule C | Rule L |
|---|---|---|
| sign W only | `{K,B,j,M}` | `{K,B,j,M}` |
| first memory write only | `{j,R}` | `{j,R}` |
| memory use only | `{M,R}` | `{M,R}` |
| Q only | `{K,B,j}` | `{K,B,j}` |
| attempted unwrite only | `{j,R}` | `{j,R}` |
| **whole five-gate episode** | `{K,B,j,M,R}` | `{K,B,j}` |

For the full episode, L's minimum-cut scores are 4 for `{K,B,j}`, 3 for `{K,B,j,M}`, and 3 for all five; its strict local winner is `{K,B,j}`. C instead connects all five. Stagewise, even the memory-use and Q selections are disjoint, despite a continuous unitary process and a physically retained memory. Therefore neither simply identifying a momentary active component with a persisting subject nor using a temporal union is justified by these calculations. Strict identity of selected sets fails between every stage; overlaps, when present, do not themselves determine lineage.

The disagreement is robust as a **rule comparison** but the precise answer depends on the coarse-graining. As a sensitivity control on the four-gate episode *without* memory use, retaining unit weights for W and Q while assigning each T occurrence diagnostic weight λ gives C all five for every λ>0 tested. L selects `{K,B,j}` at λ=1/10 and 1, reports unresolved tied candidates at λ=2, and selects `{j,R}` at λ=3. These λ values vary the graph weighting convention; no different quantum interaction strength or physical experiment is being claimed. All 120 factor relabelings preserve the corresponding rule outputs and ties. Relabeling invariance is useful but does not remove dependence on factorization, weighting, time window, state or gauge-access choices.

## 6. Whole-zero, incidence and the constructive next problem

In the echo, the actual Born ensemble remains symmetric in s at fixed b and z. If—and only if—distinct subject incidences are assigned that same measure and the counterpart map reverses the signed quality, both transported candidates still have zero signed mean within each b sector. Yet they disagree on half the weight after the echo. Thus even this more dynamic memory process does not make whole-zero or mirror balance select one subject boundary or one phenomenal bridge. A formal positive contribution also does not erase an actual negative experience.

The constructive progress is the information-routing identity: the very interaction that challenges a static boundary can coherently convert a disturbed record into a conserved-sign record, and a memory can affect an admissible joint observable while remaining inaccessible to a confined carrier. A viable subject constitution must consequently specify, from physical dynamics rather than a chosen answer:

1. the eligible factors and gauge-invariant local/interfacial intervention algebras;
2. how a carrier persists through writing, use, idle storage and reversibly attempted unwriting;
3. which stored or jointly accessible relations are intrinsic to its experience, and how its reporting interface works; and
4. how actual incidences and their signed weights arise, including counterpart pairing and any additional sectors.

The co-occurrence graph is an explicit stress test of such criteria, not the missing criterion itself. It neither proves the user's zero constitution nor establishes that the demand for one is impossible.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps \
 python -m unittest verification.zero_dynamic_subject_memory_echo_test -v
```

Eight tests verify the gauge-compatible gate algebra and coherent back-action, exact echo identity including the inactive complement, both protocols on all 16 actual histories, the output ledger and conditional balance, graph rules and their factor-relabeling/weight sensitivity. They do not establish actual subjects, subjective memory, physical time reversal, objective whole-energy or the consciousness of any modeled subsystem.
