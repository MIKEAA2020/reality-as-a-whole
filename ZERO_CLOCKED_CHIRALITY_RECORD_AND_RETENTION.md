# A clock-localized chirality record across the original echo

## Result

**Continuation:** [three-frame gauge chirality and a noncyclic clock](ZERO_THREE_FRAME_GAUGE_CHIRALITY_AND_NONCYCLIC_CLOCK.md) lifts the record to independent local frames, exhibits an extra loop-holonomy correlation, and contrasts finite cyclic erasure with an ideal noncyclic clock's non-normalizable exact stationary histories.

The [previous pass](ZERO_CHIRALITY_ECHO_RECORD_ROTATIONAL_BACKACTION.md) coupled a third-direction chirality to the original spherical echo at one checkpoint, but did not write a record at a localized clock reading. This pass supplies an explicit coherent clock-controlled construction. It introduces a **three-state neutral memory** with distinguishable `blank`, `+` and `−` states, writes the chirality at clock step `9→10`, holds it through the remainder of the old echo and a **complete additional 20-step echo cycle**, and uncomputes it at the end of an enlarged 40-step cycle.

The extended history is stationary under its own cyclic constraint; both the enlarged common-rotation singlet and the transported old opposite-pair constraint are preserved. The original old-record statistics at fixed clock readings are unchanged for the original angular-diagonal old effects. The chirality pointer remains correlated across the original echo's return, but the finite 40-step cycle **erases the correlation at its wrap**. This is conditional retention, not a durable irreversible record.

A joint comparison at the actual post-echo checkpoint also shows that the earlier spin chirality and the new sphere-pointer sign are **not the same recorded quantity** on the tested old histories: for old sign `s=+`, the spin outcomes have weights `3/4,1/4`, but the sphere signs have weights `1/2,1/2`, and their joint table is independent. The result reverses the spin weights for `s=−`. This is not a universal non-equivalence theorem or a categorical Satake map.

The larger clock, neutral memory, switch, third direction, purification and readout effects are specified model inputs. No real locality, autonomous physical clock, energetics, irreversible memory, subject or experience is derived. The [implementation](verification/zero_clocked_chirality_history.py) acts on the complete reduced clock basis; [eleven tests](verification/zero_clocked_chirality_history_test.py) check random vectors on that carrier, selected full old quantum vectors, pair encodings, all specified apparatus-purifier basis paths and an independent spinorial-pair control.

## 1. A blank state that is not an outcome

Let `t=m·(n×p)` and use the prior unsharpness parameter `0≤λ≤1`. Define

```text
a(t)=√[(1+λt)/2],      b(t)=√[(1−λt)/2].
```

In the ordered memory basis `(blank,+,−)`, the following explicit real unitary writes a record:

```text
             [ 0  1   0 ]
V_λ(t)   =   [ a  0  −b ],       V_λ(t)|blank⟩=a|+⟩+b|−⟩.
             [ b  0   a ]
```

The two recorded outcomes are orthogonal to blank. At λ=0 the pointer still leaves blank, but its signs carry no information about t; this distinction between a *write event* and an *informative write* is intentional. `V_λ` is unitary for every t; its multiplication-operator realization is bounded and commutes with the enlarged simultaneous proper rotations. Its inverse restores blank **and erases** the written sign correlation.

As before, the p factor is independently uniform and the original angular state is the actual four-bin spherical lift. The full-strength post-write conditional mean `E[t|±]=±2/9`, the sign-agreement probability `1/2+π/16`, and the original pair's old-only rotational non-singlet weight `2(1−ln 2)/9` are unchanged from the prior two-level calculation: the qutrit merely places the same recorded two-component state in a subspace orthogonal to blank. They apply on written slices and to the stated uniform old marginal, not automatically to arbitrary preparations.

## 2. A 40-step coherent history, with one record across an old cycle

Start from the earlier 20-step old system, echo, B-controlled purified apparatus, constrained pair and a four-state reference clock. Their old step at reading `n` is denoted `U_n`, repeated with period 20. The echo pulses and apparatus forward/inverse permutations are those already used in [the old coherent clock history](ZERO_COHERENT_ANGULAR_RESERVOIR_CLOCK_ACCESS.md). In the supported carrier the old cycle returns, and the full specified reversible gate sequence also closes when its full-space gate extensions and corresponding inverses are used.

Add an **explicit** 40-state cyclic clock, not merely a relabeling of the old 20-state clock. Its old-gate control uses `n mod 20`. Let

```text
D_n = I                 for 0≤n≤9,
D_n = V_λ(T)            for 10≤n≤39.
```

For the step from n to `n+1 mod 40`, set

```text
U'_n = (D_(n+1) D_n†) U_(n mod 20).
```

The new pointer gate commutes with each old step because the stipulated old gates act pointwise without changing the directional coordinates and act trivially on p and the new memory. Therefore the only nonidentity new factors are `V_λ` on `9→10` and `V_λ†` on `39→0`. At n=20 the old 20-step cycle has returned, but the new memory is **still written**. The old gates then run through a second cycle while it is retained. The new clock coordinate is the resource that distinguishes the first old cycle from the second; this is not a claim that the original 20-state clock alone stores an unbounded counter.

Let W₀ be the old controlled cyclic shift lifted to 40 positions, including reference-clock shift `q=1` or `q=2`, and define

```text
D = Σ_n |n⟩⟨n| ⊗ D_n,        W' = D W₀ D†.
```

`W'` is unitary and closes after 40 steps on the declared carrier. If `|Ω_q⟩` is the old repeated history with memory blank and reference reading `qn mod 4`, then `|Ω'_q⟩=D|Ω_q⟩` obeys `W'|Ω'_q⟩=|Ω'_q⟩`. The record is relationally clock-localized within the stationary state; this does not claim that a bare clock projector commutes with the constraint or that a laboratory switch has been built.

The same construction works for a supplied `20k`-state cyclic clock, `k≥1`: write at `9→10`, retain through tick `20k−1`, and erase on the wrap. The written interval has `20k−10` clock readings, so a larger clock supplies proportionally longer finite retention. At each finite k the record is eventually erased. Whether a noncyclic, dissipative, fault-tolerant or infinite-dimensional memory can do better while respecting the desired constraints is a different question.

### A necessary control: do not silently omit the erase

If we keep the same closed clock and old cycle but apply `V_λ` at `9→10` **without** a compensating operation, the one-cycle monodromy sends `|blank⟩` into the orthogonal recorded subspace. The ready state therefore cannot return to itself after one clock circuit. The verifier checks unit norm, zero overlap with the input and distance `√2` on the reduced full-basis model. A uniform history constructed from that initial state does not close under that proposed shift.

This is a sharp obstruction for this **specified single-write cyclic protocol**, not a theorem that every stationary model must erase records. A larger clock, another memory, nontrivial boundary condition or altered dynamics may change the conclusion; any such alternative must explicitly account for its state and resources.

## 3. Constraints, old records and the actual quantum carrier

The new gate acts on the old/record/pair fibers as the identity and does not change `u=m·n`. The original pair's angular-bin and sign matching projectors are pointwise in these fibers, and the gate commutes with them. At another clock reading the old pair constraints are the actual transported anchor projectors; the same pointwise commutation persists because the new gate commutes with the old steps. Consequently both signs remain distinct and their **old model-charge sum is zero in each new memory branch**.

The enlarged directional group rotates m,n,p together, leaving t and hence `V_λ(T)` invariant. The complete state and each recorded branch remain in that enlarged singlet sector. This does **not** preserve an independently imposed old-only m,n singlet: the known `6.82%` full-strength old-pair singlet leakage applies while the record is present. The three-direction gauge extension is still a declared construction rather than a derived new linked-frame theory.

At a fixed clock reading, tracing over uniform p gives the same old angular-diagonal density for either recorded sign after normalization and the same old-only record probabilities unconditionally. This remains true while the original gates evolve, since they do not act on p or the new memory. Off-diagonal angular observables can distinguish the recorded and unrecorded states; identical old-record tables do not imply an unchanged full state.

The tests use actual `quantum_echo_checkpoints` and `from_anchor` on selected source/sign pairs `(0,+)` and `(15,−)`, bins 0 and 2, and ticks spanning writing, return and retention. The finite pair is encoded with the actual `encode_pair` map, and the complete reduced-basis transported constraint is checked at every one of 40 steps. For the one-bit auxiliary setting, every prepared B/source-reference/purifier apparatus basis path returns after 20 steps; repeating that path while the pointer is held gives the second old cycle. This is an exact factorization argument plus finite checks, **not** a dense simulation of every old apparatus, source, direction and clock factor at once.

## 4. Stationary clock comparisons

As in the original clock work, a bare reference-reading projector need not commute with the cyclic constraint. For an anchor a, reference reading r and memory effect A, use the twirl

```text
Q_(a,r,A) = Σ_(j=0)^(40−1) (W')^j (|a,r⟩⟨a,r| ⊗ A) (W')^(−j),
E_(r,A)   = (1/40) Σ_a Q_(a,r,A).
```

The averaging over anchors is a **specified protocol resource**. The effects commute with W', are positive, and form a joint POVM when A ranges over `blank,+,−` and r over the reference states. The matrix-free verifier checks these properties and a bare-reference negative control on sampled complex vectors spanning the full **reduced** B/J/echo/sign/reference/clock/memory carrier, for sampled chirality fibers. The operator twirl and direct-integral arguments establish the identities on the declared carrier; finite samples are controls, not exhaustive checks.

For reference reading `r=2`, define `w` as the fraction of selected clock anchors at which the memory is written. In the 40-step case, for the symmetric p preparation:

| Reference preparation | P(r=2) | Written fraction w | P(blank \| r=2) | P(+ \| r=2) | P(− \| r=2) | E[sign·t \| r=2] |
|---|---:|---:|---:|---:|---:|---:|
| q=1 | 1/4 | 4/5 | 1/5 | 2/5 | 2/5 | 8λ/45 |
| q=2 | 1/2 | 3/4 | 1/4 | 3/8 | 3/8 | λ/6 |

Here `sign=0` on blank, and `±1` on the recorded outcomes. The right column follows from `E[t²]=2/9`. The q=1 anchors are `2,6,10,…,38`; q=2 selects the odd anchors, half of all readings. For a `20k` clock, the corresponding written fractions are `1−2/(5k)` and `1−1/(2k)`. For fixed t before averaging over p, `P(−|r=2)=w(1−λt)/2`; this is also checked directly with the twirled effects. These are two specified reference correlations and a uniform-anchor comparison, not evidence of inequivalent physical histories under a passive clock change.

## 5. Compare the actual spin and spherical chirality signs

The old [charge-conserving spin-chirality reporter](ZERO_CONSERVING_RELATIONAL_CHIRALITY_REPORT.md) has sharp projectors `P_spin,+`, `P_spin,−`, `P_spin,0` on its old spin/reference factors. The scalar sphere write acts on the direction and a different neutral pointer, so its unitary commutes with those projectors and with the supplied spin-readout unitary as tensor-factor operations. Applying both is an extra joint instrument; it is not already present in the unmodified echo.

At anchor 10, the actual old quantum vectors for source labels `0,7,15` and both old sign-pointer branches give the following spin distribution by spherical bin (entries are probabilities in the **normalized old sign branch**):

```text
old bins 0 and 1:  each has P(spin +)=1/8, P(spin −)=1/8;
old bins 2 and 3:  each has P(spin s)=1/4, P(spin −s)=0;
P(spin 0)=0.
```

The new sphere-memory signs, after uniform p is integrated, are each `1/2` conditional on every bin and every spin effect. Thus for `s=+`, the joint table at the written checkpoint is

```text
                    sphere +    sphere −
spin +                3/8         3/8
spin −                1/8         1/8
```

For `s=−` interchange the spin rows. The two readout signs agree with probability `1/2` on either sign branch. This does not make the sphere pointer uninformative: each sign is correlated with the continuous t as calculated above. It does show that, for these actual states and this comparison, it cannot simply be relabeled as the earlier spin-chirality sign.

The verifier additionally checks that these spin projections do not leak from the encoded old pair sector on the tested source/sign/bin vectors. This supported-state check is not a proof that the spin reporter preserves the full pair sector on every possible input, nor a demonstration of its switching, access, or joint energy cost. It also does not rule out a more elaborate map between other states or observables.

## 6. A balanced spinorial lift and the Satake interface

The [previous pass](ZERO_SPHERE_REPRESENTATIONS_GAUGE_LANGLANDS.md) showed that a scalar sphere carrier cannot itself map nontrivially and equivariantly to a single fundamental `SU(2)` doublet: the center acts with opposite signs. Here is a minimal conditional extension that preserves a whole-level singlet. Add **two new** abstract doublet factors `K,K'`, distinct from both the new qutrit and the earlier spin-chirality references, and stipulate their singlet

```text
|s⟩_(KK') = (|↑↓⟩−|↓↑⟩)/√2,
J_i^(KK') = (σ_i⊗I + I⊗σ_i)/2,
J_i^(KK') |s⟩ = 0.
```

For every `U∈SU(2)`, `(U⊗U)|s⟩=|s⟩`. The isometry `Ψ↦Ψ⊗|s⟩` preserves all old inner products and old observables. If the two new factors transform under a **chosen common rotation double cover**, the enlarged three-direction-plus-spin state remains invariant, and the new chirality write, old clock gates and old pair constraints commute with the added spin factors. The tests check the singlet charges, rotations, center, and memory-gate composition. A single unmatched doublet would instead transform by −1 under the central element and cannot contain an invariant vector. This is an explicit repair of that particular center obstruction at the level of an added pair, not a derivation of a fundamental spinor from a scalar.

There is a precise, but conditional, Satake comparison. For the minuscule `PGL₂` object `F` of the prior report, geometric Satake sends `F` to the `SL₂` fundamental V and sends convolution to tensor product. Thus `F⋆F` corresponds to `V⊗V=1⊕3`, and the invariant alternating tensor defines, via the equivalence, a singlet morphism from the tensor unit to `F⋆F`. The qubit singlet above has that same algebraic type **only after choosing an identification** between its supplied spin `SU(2)` action and the compact form of the mathematical dual action. This is an application of the known Satake equivalence, not a newly proved equivalence or an intrinsic map from the old echo to perverse sheaves. Constructing the `O(1)` section carrier, compatible geometry, tensor functor and physical observable map remains open. Neither the qubit pair nor the old finite model-charge cancellation is a Yang–Mills duality.

## 7. Remaining work

1. Replace the explicitly scheduled 40-state clock and reversible wipe with a physical mechanism or an independently analyzed noncyclic memory. Determine retention and error under realistic couplings; include the energy of all new degrees of freedom and control.
2. Construct the extended frame-gauge link for p and analyze whether the memory remains accessible to a specified physical subsystem. Rotational invariance and an abstract pointer are not a local experiment.
3. Examine whether the two chirality signs admit a state-independent intertwiner or are genuinely different operational observables. The joint table is an explicit constraint on any proposed identification, not a no-go for all possible correspondences.
4. Build an actual spinorial `O(1)` or other appropriate bundle carrier and an observable-preserving Satake map. The balanced abstract doublets merely make a compatible representation-theory input explicit.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_clocked_chirality_history_test -v
```

The history verifier works with fixed chirality fibers and the exact reduced-state permutation, while the report's spherical averages use the analytical continuous sphere measure established in the previous pass. The memory, switch and long clock are stipulated, and the numerical large-vector checks have the explicit limited support described above.
