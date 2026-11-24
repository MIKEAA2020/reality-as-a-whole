# The full paired state: clock and work records without discarding a sector

## Result

The previous [encoded clock/work bridge](ZERO_ENCODED_SPHERE_CLOCK_WORK_DIRECTIONAL_BRIDGE.md) put the full sphere–clock–work circuit on a `1/128` code branch and retained, but did not develop, the rest. Here the **entire specified paired state** gets a finite clock, three-outcome local record, two-outcome partner record, work exchange and relation-target memory. The earlier code branch keeps its original finite-reference quantum sphere instrument; an explicit symmetry-preserving instrument acts on the other `127/128` of the state.

The completed finite circuit has the following properties:

* no sector is projected away: the flags and their coherent sectors are retained;
* every pointer branch preserves all three **global** directional balances and the declared zero energy charge;
* on both sectors the clock-window probability is `3/16`, and the same work relation h is perfectly correlated with the target memory at the specified pulse;
* the record/work event previously available only on the small code branch now has total Born weight `3/64` across the full state; and
* on the specified h-conditioned subensembles, neither record alone nor work alone reveals h, while their joint relation does.

There is a crucial qualification: the complement uses a **fixed-setting commuting instrument**, not the earlier noncommuting five-ray sphere POVM. It gives the same row weights and partner marginal and nontrivial correlations, but its detailed table differs and admits an explicit classical hidden-sector description for this setting. The construction therefore achieves an all-sector **record–clock–work extension**, not a proof that the original quantum sphere instrument operates unchanged everywhere.

Everything remains a finite, explicitly stipulated model. The input paired state, energy assignment, control schedule, reference, pointer and target interactions are not derived from zero itself. No claim is made that Born weights entail irreducible chance, that a branch is selected, that quantum registers are actual subjects, or that the declared charge is the universe's objective energy.

Verifier: [verification/zero_all_sector_sphere_clock_work_test.py](verification/zero_all_sector_sphere_clock_work_test.py).

## 1. Decompose the whole, not only the preferred code

Each lab has four four-level constituents. Let `G_i=Σ_k X_i^(k)` be the three noncommuting directional generators, E the earlier two-dimensional local code, and

```text
P = EE†,      D = I−P.
```

The specified initial physical paired state is

```text
|Ω> = (I⊗V)|Φ₂₅₆>,        |Φ₂₅₆> = (1/16) Σ_a |a>_A|a>_B,
V = E R E† + D,            R = [[0,−1],[1,0]].
```

It obeys `(G_i^A−G_i^B)|Ω>=0` and the previous lab-energy balance. Neutral local flags can record P versus D without changing those balances. They are retained as quantum registers; no definite flag selection is presumed. The joint code weight is `1/128` and complement weight `127/128`.

On the complement, swap the first two constituents and define

```text
S₁₂ = swap(1,2),        T = D S₁₂ D.
```

T is real, self-adjoint, commutes with all G_i, and commutes with the declared local lab energy, which is zero on D. Its verified spectrum is

```text
−1 (95 times),  −1/5 (once),  0 (twice, on P),  +1 (158 times).
```

Define the orthogonal projectors

```text
P_+ = T(T+I)(5T+I)/12,       P_− = D−P_+.
rank(P_+)=158,                rank(P_−)=96.
```

They commute with G_i and the lab energy. This produces actual nontrivial local alternatives in the formerly undeveloped sector. For the normalized physical states `|Φ_P±> = vec(P_±)/√rank(P_±)`, global directional balance is exact, while the individual lab generators do not vanish: for example, `<Σ_i G_i²>` is `528/79` in the plus sector and 5 in the minus sector. This is a paired cancellation of nonzero quantum contributions, not an assertion of simultaneous sharp values of the noncommuting G_i.

The complement is not intrinsically classical: `D S₁₂ D` and `D S₂₃ D` both commute with all the G_i but have a nonzero commutator. What is classical is the **particular single-setting instrument** selected below.

## 2. An explicit instrument over every sector

On P, use exactly the earlier lifted finite-reference sphere unitaries and their existing pointers. On D, assign local pointer operations controlled by `P_+` and `P_−`; those operations do not touch the local reference. The same three-outcome Alice pointer and two-outcome Bob pointer are used in both sectors.

Write `q=(1/8,2/5,19/40)`, `d_i=n_i·axis`, and

```text
w_+ = 158/254 = 79/127,       w_− = 96/254 = 48/127.
```

For complement sector s, choose Alice and Bob response probabilities

```text
f_i^+ = q_i (1−w_− d_i),      f_i^− = q_i (1+w_+ d_i),
b_0^+ = 1/2+w_−/2,            b_0^− = 1/2−w_+/2,
b_1^s = 1−b_0^s.
```

They are positive and normalized for the specified five rays and axis. They obey `Σ_s w_s f_i^s=q_i` and `Σ_s w_s b_0^s=1/2`. For each probability vector, a finite Householder unitary maps its neutral pointer's ready state to the corresponding vector of square-root amplitudes. The full local operation is block diagonal:

```text
U_A = encoded finite-reference U_A on P
      + P_+⊗I_reference⊗O(√f^+)
      + P_−⊗I_reference⊗O(√f^−),
```

and similarly for Bob with `b^±`. Since P, P_+, P_− are orthogonal and complete, this is a unitary on the whole lab–reference–pointer space. The complement blocks commute with each G_i and with reference energy; the code block has the earlier exact commutators. Thus the complete instrument conserves the declared charges, not only its average effect. The verifier constructs these blocks and tests the actual full-lab action on vectors containing both code and complement.

These probabilities are deliberately specified, not derived. In particular they use the chosen axis in the construction of Alice's response. They must **not** be interpreted as a demonstrated independent-setting, Bell-violating or geometrically faithful quantum sphere instrument.

## 3. Clock, work and target on both sectors

Use the same finite reference/clock pairs, work states `|0110>`, `|1001>`, work-current probe `J₁`, record pair R and target T as in the earlier circuit. Copy Bob's pointer to R and apply the same work preparation, phase pulse and target interaction

```text
h = (P_act−Z_R J₁)/2,       U_T = exp(−i(π/2)hY_T).
```

These operations act on the designated record/work/target registers and commute with the lab directional generators. The relative-clock instrument remains the earlier actual 16-outcome joint POVM; its three-label window has probability `3/16` **in each sector**. In D, the local sphere surrogate leaves the references untouched; in P the original reference-coupled instrument is used.

In either sector, conditional on the window,

```text
              T=0     T=1
h=0           1/2       0
h=1             0     1/2.
```

The same relation distinguishes the two h subensembles in their joint record–work state,

```text
ρ_RW^(h) = [I₄+(1−2h)Z_R J₁]/4,
```

while each separate R and W reduction is `I₂/2`. This survives the flag-unselected mixture because the stated marginals hold in both sectors. The target has an explicit joint interaction; it does not grant a strictly R-local system automatic access to h. Additional supplied registers or different preparations can change the locality comparison.

The construction's compressed numerical tensor uses two abstract labels for the two orthogonal physical paired states `|Φ_P+>` and `|Φ_P−>`. This is a **global compression of the correlated two-lab subspace**, not a claim that either 256-dimensional lab is actually a qubit. The verifier separately constructs the actual projectors and physical paired matrices, checks the directional and energy balances for each complement pointer pair, and uses the exact orthogonal-sector isometry to calculate the record/clock/work reductions.

## 4. The unselected table and the event

The three-label-window table in the complement is

| Alice i | r=+ | r=− |
|---|---:|---:|
| 1 | 0.06543881 | 0.05956119 |
| 2 | 0.17648955 | 0.22351045 |
| 3 | 0.25807164 | 0.21692836 |

It has the form `q_i(1∓η d_i)/2` with `η=3792/16129`. It is explicitly generated by the two hidden sector labels and the local response probabilities above. The original code sector has the earlier, different finite-reference table. Keeping both flags and tracing them only for the displayed statistics gives

| Alice i | r=+ | r=− |
|---|---:|---:|
| 1 | 0.06546799 | 0.05953201 |
| 2 | 0.17625608 | 0.22374392 |
| 3 | 0.25827593 | 0.21672407 |

The full table retains Alice marginal q and Bob marginal `(1/2,1/2)`. Its total-variation distance from the earlier **ideal** five-ray table is approximately `0.152512`; equal marginals do not make the instruments equivalent.

On the full paired state the clock window, `r=+`, `T=1` event has Born weight

```text
(3/16) × (1/2) × (1/2) = 3/64.
```

Its contributions are `3/8192` from the old code sector and `381/8192` from the complement. In the specified active work support, T=1 entails h=1, and on r=+ this gives `J₁=−1`. These are conditional relations within a coherent quantum model; they do not assert that the event uniquely occurs or specify actual experiencers. Born weights are used as standard operational statistics, without assuming irreducible objective chance.

## 5. Conservation and locality, carefully scoped

For the paired sector vectors, the physical operator identity is `(G_i^A−G_i^B)|Ψ>=0`; the individual lab G_i generally **do not** annihilate complement states. The verifier checks this identity after each complement Alice/Bob pointer pair. All pointer and work/clock effects preserve it. The earlier encoded sector satisfies the stronger local conditions.

For Q, on the complement the lab energies are zero, the reference/clock identity pairs give their prescribed balanced contribution, and work energy 2 cancels the explicitly supplied clock offset −2. The relative-clock effects preserve the total clock number. The verifier checks the full compressed complement state and every selected clock pointer against the actual energy labels; the earlier isometric argument covers P. Thus the full circuit is in `ker Q` as an operator statement. This is still the **declared** Q: interaction/control/switching energies and an autonomous clock mechanism are not fully accounted for, and the zero offset and paired input are assumptions.

The complement Alice instrument and an alternative `q_i I` instrument are both complete. Nonselectively tracing Alice's lab and pointer leaves Bob's reduced state unchanged; the complementary reference/clock pairs are untouched by those local instruments. The previous complete-retained-lab no-signalling check applies on P, including the same joint clock-window conditioning. Retaining Bob's sector flag yields a blockwise equality, so the full model has the corresponding fixed-operation no-signalling property. This is not a demonstrated spacelike experiment, and the joint clock window is not automatically available to a confined subject.

## 6. Consequence for the larger proposal

This moves beyond the earlier postselected construction: **both parts of the specified whole now contain a finite operational record, work relation and clock interface**, and local nonzero directional structure is balanced across the paired labs in every branch. Yet their detailed sphere measurements are not the same. Matching the first table's weights and marginals does not supply the noncommuting angular structure of the original instrument in the complement.

A direct next construction is to use the noncommuting invariant compressed swaps to analyze the complement's representation multiplicities and build genuine charge-preserving directional measurements there. One should keep the complete sector state and evaluate the actual clock/work instrument, rather than impose a desired table by hand. In parallel, the paired initial resource and physical Hamiltonian still need explanation, and the R/−R valence ambiguity still needs a subject–incidence rule. Opposite mathematical signs do not by themselves constitute opposite experiences or erase locally felt suffering.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_all_sector_sphere_clock_work_test -v
```

The tests check the invariant projectors and their dimensions, the paired physical states and pointer branches, block-unitary charge conservation, clock/work/target correlations in both sectors, the whole table and event weight, and the stated no-signalling controls. Spectral multiplicities are checked numerically; the model's physical and experiential interpretation is not established by those tests.
