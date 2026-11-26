# Constitutive modes, neutral scalar and coherence on the same echo

## Result

Following the user's relativity example, this pass asks what the common echo's internal relations **themselves** determine, without an outside process making the result happen. On its two commuting sign observables, define

```text
S = (N+K)/2,        T = (N−K)/2.
```

These are not extra components or independently prepared systems: together they are a reversible change of coordinates on the same two-sign structure. Their operator identities imply that when the type-symmetric scalar S is zero, the antisymmetric mode T is necessarily nonzero. Thus the zero of that particular scalar does **not** erase the modeled distinction. This is an internal mathematical identity, not a claim that T is a felt quality.

The full original coherent echo shows a further distinction: a report of S=0 can leave coherence between two T alternatives, whereas an ideal finer T measurement destroys that coherence when its outcome is discarded. Both procedures can give the same coarse S report. The statement depends on the specified measurement instruments; a report value alone does not determine backaction.

The result does not establish an experiencer, a unique valence bridge or an actual incidence measure. It is a constructive piece of the user's proposed form of explanation, not a completed derivation of the whole. [Implementation](verification/zero_echo_constitutive_modes.py), [tests](verification/zero_echo_constitutive_modes_test.py).

## 1. Internal decomposition, not an imposed second system

At the anchor of the existing echo take `N=Q_now=MJ` and `K=Q_echo=MJR`; the commuting sign involutions satisfy `N²=K²=I` and `NK=R`. Define S and T as above. Algebraically,

```text
N = S+T,             K = S−T,
S² = (I+R)/2,        T² = (I−R)/2,
S²+T² = I,           ST = TS = 0.
```

These are operator identities for any such commuting involutions, not just expectation values or a special prepared state. `S²` and `T²` are the complementary R-sector projectors. Their values are ±1 or 0, and they commute; calling them two *modes* does not mean they are incompatible measurements or separately existing subjects.

On R=+1 the signs agree: `S=±1,T=0`. On R=−1 they disagree: `S=0,T=±1`. The transformation is invertible, so `(S,T)` preserves exactly the same joint sign information as `(N,K)`. For the previous positive model magnitude G, the full structural vector has coordinates `G(S,T)`; its opposite pair is `−G(S,T)`. These two pair values remain constrained opposite model observables, not automatically two independent experiencers.

Under the earlier active type swap, `(N,K)→(K,N)`, hence `(S,T)→(S,−T)`. Under the sign counterpart, `(N,K)→(−N,−K)`, both modes reverse. This is a transformation of specified physical/model records. It does not license treating T's two signs as gauge-identical, especially where the existing J and angular records distinguish them.

## 2. What is uniquely forced—and what is not

Suppose a real scalar depends only on the two signs for a fixed swap-compatible G, is invariant under their exchange, is odd under their simultaneous reversal, and has value G at `(+,+)`. Then it is uniquely

```text
v(N,K,G) = G S = G(N+K)/2.
```

Indeed, at `(+,-)` exchange produces `(−,+)`, which is also the simultaneous sign reversal. The assumed scalar must therefore be both unchanged and negated, hence zero. Oddness fixes the value at `(−,−)` to −G. This proof does **not** require assuming a linear scalar law. The normalization and exchange/oddness conditions are substantive premises, not consequences of the zero total alone.

The previous [joint occurrence analysis](ZERO_ECHO_OCCURRENCE_QUALITY_INCIDENCE_JOINT_CONSTRAINT.md) derived this scalar form and its obstruction; the added mode identity now makes explicit what the symmetric scalar omits and relates that omission to the original coherent record. In particular, the physical pointer alternative `GM` remains nonzero on R=− and is type-invariant because it uses an additional contextual variable not determined by `(N,K,G)` there. Neither scalar has been identified with feeling. A deeper constitution could determine which information and transformation law are intrinsic; the existing symmetry assumptions alone do not choose a phenomenal bridge.

## 3. One population, not independent modes

The earlier physical calculation gives weight `1/8` to each `(i,s)` event. The resulting **joint** mode law is

| S | T | Physical model weight |
|---:|---:|---:|
| +1 | 0 | 1/4 |
| −1 | 0 | 1/4 |
| 0 | +1 | 1/4 |
| 0 | −1 | 1/4 |

The two marginals each put weight 1/2 on zero and 1/4 on each nonzero sign, but they are **not independent**: for example, the joint probability of `S=T=+1` is zero, not `1/16`. The table is a distribution of two compatible queries on the same physical events. Turning the two columns into two independent occurrence populations would require an additional incidence rule.

Under the stipulated scalar interpretation, S=0 is a neutral *signed model value*, not nonexistence of experience or an absence of all structure. T=±1 preserves a real **model** distinction on those rows; whether it makes a phenomenal difference is open. Conversely, when S is nonzero, T vanishes; this does not erase the nonzero S distinction. The original physical–experiential question remains open in both sectors.

### Pair balance is not incidence balance

On each event the two constrained model mode vectors are `G(S,T)` and `−G(S,T)`, and sum to zero without an outside matching operation. Suppose, only as a hypothetical incidence extension, the two factors receive shares λ and `1−λ`. Their weighted vector contribution is

```text
G(2λ−1)(S,T).
```

Because G is positive and `S²+T²=1` on this support, this **full vector** vanishes event by event exactly when `λ=1/2`. On R=− the S component vanishes for *any* λ while the T component still detects unequal weighting. This makes the scalar-versus-vector distinction concrete; it does not prove that the factors are separate subjects, that such λ is the actual measure, or that cancellation erases negative experience. The earlier [balance analysis](ZERO_ECHO_OCCURRENCE_QUALITY_INCIDENCE_JOINT_CONSTRAINT.md) also shows how global cancellation can hide local incidence asymmetry.

## 4. The original coherent echo and the cost of learning more

Use the **unscaled** S and T observables for this measurement calculation; measuring `G S` can distinguish additional positive-sector magnitudes and has a different disturbance. For each selected pointer sign `M=s`, the actual T–Q–T echo's normalized sign slice has four angular bins with weight `1/4` each. On the supported anchor state:

- bins 0 and 1 lie in R=−, have S=0 and opposite T signs;
- bins 2 and 3 lie in R=+, have the same `S=s` and T=0.

The tests check the actual complex echo vectors for source labels 0, 7 and 15 and both pointer signs, including the appropriate J and R support. These checks concern this specified source family; they do not assert an arbitrary off-support decoder or a subject-accessible measurement.

Consider two explicit **ideal Lüders** instruments with nonselective outcomes:

1. Measure S alone, retaining coherence *within* each degenerate S eigenspace. Its two nonzero outcome probabilities in this sign slice are `1/2,1/2`.
2. Jointly measure the commuting pair `(S,T)`, or equivalently refine the S=0 outcome by T. Its three nonzero probabilities are `1/2,1/4,1/4`.

For a pure input `|ψ⟩`, the overlap `⟨ψ|ρ_out|ψ⟩` after nonselective Lüders measurement is `Σ p_outcome²`. Hence the fidelity with the original state is

```text
S alone:                  1/2,
refined joint (S,T):      3/8.
```

Both retain the same S statistics. A physical device that internally measures the finer observable and then discards T may output exactly the coarse S report yet disturb the state more than a genuine Lüders S instrument. Therefore the mathematical relation between the modes does not by itself specify an instrument, its disturbance, or its resources.

### The S=0 sector can retain phase, too

Condition the actual sign slice on S=0. The two angular branches have equal norm and are orthogonal. Absorb their existing phases into normalized branch vectors `|e₊⟩,|e₋⟩`, labeled by opposite T. Their selected pure state has the isometric representation

```text
|ψ₊⟩ = (|e₊⟩+|e₋⟩)/√2.
```

An additional stipulated phase flip yields `|ψ₋⟩=(|e₊⟩−|e₋⟩)/√2`. Both give S=0 with certainty and T=±1 with probability `1/2`, yet are orthogonal; a suitable joint coherence-sensitive effect distinguishes them. The selected-state fidelity after an ideal S=0 Lüders operation is 1, while a nonselective T measurement gives fidelity `1/2` and makes the two phase alternatives identical as density operators.

Thus even the pair `(S,T)`'s outcome distribution does not exhaust the full coherent state. The phase-flip intervention and coherence effect are **additional model operations**; neither locality nor availability to a subject is established. As in earlier coherence controls, their point is to prevent identifying a coarse report with all that exists in the underlying modeled state.

## 5. Why-chain and next step

1. **Why does neutral S retain an internal distinction?** Because the same two sign involutions imply `S²+T²=I`; if S=0 on a joint eigenstate, T=±1. No second agent has to add T afterward.
2. **Why not just call T the missing feeling?** The identity is physical/mathematical; an experiential identity must establish what is felt, by whom, with what accessible content and under what transformations. Calling a coordinate a feeling would not supply that demonstration, though a deeper constitution might genuinely identify them.
3. **Why can a report miss structure?** A coarse effect groups different states. Even a refined S/T outcome law misses relative phase, and different implementations of the same coarse report can have different backaction. Actual access and intervention belong in the theory.
4. **Why can pairwise zero coexist with unequal incidence?** The operator pair and a proposed weighting are different mathematical inputs. The full-vector calculation shows when a particular weighted pair cancels, without forcing a real subject census or allowing an opposite contribution to erase suffering.
5. **Why these signs, sector and measure?** Their algebra has a constitutive necessity conditional on the chosen echo, but the self-sufficient whole's actual carrier, intrinsic quality, subject identity and incidence remain to be derived together. The user's relativity analogy directs us to seek that deeper identity, not an external coercer. This is an active explanatory gap, not a proven ultimate bedrock.

Next, transport the full mode **effects and instruments**, not only sign values, across the echo's clock descriptions; investigate when an actual accessible joint interface can preserve or necessarily disturb the relevant coherence, and how any such interface relates to plural subject incidence.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_echo_constitutive_modes_test -v
```

The tests check the operator identities, the unique normalized scalar under its premises, the exact joint table, actual complex-vector support, ideal-instrument fidelities and phase control. They do not validate an experiential bridge, subjective access or foundational necessity.
