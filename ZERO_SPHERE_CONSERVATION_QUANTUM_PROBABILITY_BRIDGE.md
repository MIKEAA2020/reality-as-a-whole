# From intrinsic conservation to quantum weights and signed zero

## A new construction

The [five-ray result](ZERO_SPHERE_INTRINSIC_FIVE_RAY_CONSERVATION.md) and the [qubit sphere](ZERO_INTERNAL_SPHERE_BINARY_STRUCTURE_AND_INCIDENCE.md) were previously parallel constructions. Here they meet:

> For any generic five future null rays in effective `3+1`-dimensional Lorentz geometry, their unique positive `2+3` conservation relation determines an intrinsic center-of-momentum frame. In that frame, **each side separately is a weighted decomposition of the same maximally mixed qubit state**. Moreover, each side defines a complete qubit measurement whose Born weights in that state are exactly the intrinsic center-frame energy fractions.

This is not merely an analogy between two spheres: the same ray directions, the same coefficients fixed by four-momentum conservation, and the same local frame give both the two-outcome and three-outcome constructions. No external time or preferred cosmic foliation enters this local theorem.

There is also a signed-zero result: with respect to any intrinsic axis, each side's energy-weighted directional values separately sum to zero, although their local values need not vanish. This is a specific point at which **physical conservation, normalized quantum weights, and a differentiated signed balance coincide mathematically**.

The theorem is conditional on actual effective null rays, conservation, the spinor/qubit identification, generalized measurements and the stated state identification. It does **not** derive the physical interaction, subjective experience, experiential incidence, global energy, or the entire constitution of zero. The weight correspondence is a structural result, not a derivation of actual observed frequencies. Those qualifications are essential: the result makes a concrete bridge to investigate, rather than completing the user's no-residue programme by definition.

## 1. Set-up: a local conservation zero determines its own frame

Use signature `−+++`. Take five distinct future null vectors `k_i` such that every four are linearly independent. As proved in the earlier report, their unique relation has a `2+3` sign split. Let positive `p_i` be the appropriately scaled rays, with the two sets denoted `A` and `B`:

```text
Σ_(i∈A) p_i = Σ_(j∈B) p_j = P,      |A|=2, |B|=3.
```

The relation fixes the `p_i` up to a common positive scale. `P` is future timelike. Put

```text
M = √(−P·P),       u = P/M,
E_i = −u·p_i > 0,  q_i = E_i/M = (−P·p_i)/M².
```

`u` is the configuration's center-of-momentum four-velocity and all `q_i` are Lorentz scalars. Positive rescaling of a ray representative is absorbed by the inverse change of its conservation coefficient; common rescaling of all momenta cancels in `q_i`. There is no chosen external observer in this definition. On **each** side:

```text
Σ q_i = 1,       Σ q_i n_i = 0,
```

where `n_i` is the unit spatial direction of `p_i` in the `u` frame. This follows directly by writing `p_i=E_i(u+n_i)` and using `P=Mu`. For the pair, momentum balance forces opposite directions and `q=1/2` each. For the triple the `q` values are generally unequal. Every triple `q_i<1/2` in the generic case: the remaining two future null momenta have a timelike sum, so `(P−p_i)²<0`, yielding `M²−2ME_i>0`.

This zero is **local vector momentum balance**, not an assertion that the positive total four-momentum `P` or the whole's physical energy is zero.

## 2. The same conservation relation supplies two qubit ensembles

Use the project's previously stated identification between future null directions and rank-one `2×2` Hermitian matrices. The center frame supplies the positive inner product needed to normalize the corresponding spinors. Associate to each direction the pure-state projector

```text
Π_i = (I + n_i·σ)/2.
```

This is the standard Bloch-sphere representation of a qubit; it uses the assumed complex spinor structure. Then conservation gives, on either side,

```text
ρ_A = Σ_(i∈A) q_i Π_i = I/2,
ρ_B = Σ_(j∈B) q_j Π_j = I/2.
```

Thus the pair and triple are distinct pure-state decompositions of **one and the same density matrix**. The pair consists of antipodal states with equal weights; the triple generally has unequal weights and need not be a symmetric trine. It is their conserved common `P`, not an independently selected laboratory observer, that picks the frame in which both averages are `I/2`.

This density operator can equally be seen as the common positive Hermitian matrix associated with `P`, normalized by its center-frame trace. Before passing to that frame it need not be represented by `I/2`. General Lorentz transformations act on spinors by nonunitary congruences; they are not ordinary qubit unitaries with a fixed inner product. Our claim compares geometrically reconstructed center-frame objects, not fixed-inner-product qubits under an arbitrary boost. The intrinsic scalars `q_i` remain invariant.

The equality of density matrices means the two **stipulated ensembles** give the same `tr(ρE)` for any qubit effect `E`. It does not mean they are the same list of physical events or the same experiences. Their decomposition labels can distinguish how they were prepared, and no physical preparation has yet been derived.

## 3. Conservation simultaneously determines two valid measurements

Define one effect for each ray on a side by

```text
F_i = 2 q_i Π_i = q_i (I + n_i·σ).
```

Each `F_i` is positive, and, separately for `A` and `B`,

```text
Σ F_i = I.
```

They are consequently two legitimate abstract POVMs (positive-operator-valued measures): a two-effect projective measurement for the pair, and a three-effect generalized measurement for the triple. Since each individual effect is bounded by the sum `I`, its nonzero eigenvalue `2q_i` is at most one; for a generic triple it is strictly below one.

In the **specified** state `ρ=I/2`, the Born rule yields

```text
Pr(i | side, ρ=I/2) = tr(ρ F_i) = q_i = (−P·p_i)/M².
```

The geometry therefore fixes a common set of numbers which are both (i) invariant fractions of center-frame energy on the chosen side and (ii) Born probabilities for that side's constructed POVM in the conserved, maximally mixed state. This is a precise new candidate bridge between emergent causal geometry, a physical conservation relation and local quantum probability.

**State matters.** The same measurement acting on another state yields different probabilities: for the pair POVM, the first projector state gives `(1,0)`, not `(1/2,1/2)`. The identification of the actual operational state with the common normalized `P` is an additional physical claim. Neither the POVMs nor their abstract probabilities alone produce definite records, observers, empirical frequencies or an incidence measure.

## 4. Two exact examples

Using the projective representative

```text
k(x+iy) = (1+x²+y², 2x, 2y, x²+y²−1),
```

the earlier five rays `0,2,1,i,−i` give

```text
3 k(0) + k(2) = 2 k(1) + k(i) + k(−i) = (8,4,0,0),
q_pair   = (1/2, 1/2),
q_triple = (1/3, 1/3, 1/3).
```

The pair directions are opposite. The three triple directions have pairwise dot product `−1/2`, so this example is a center-frame trine. These are **two different** decompositions and measurements of `I/2`, not five equiprobable outcomes of one measurement. In particular, interpreting the five numbers together as one distribution would sum to two; the side/measurement context must be specified.

To show that the triple's equal weights are not generic, take the five rays `0,1,3,i,2i`. Their intrinsically selected pair is `{3,i}`, with `q=(1/2,1/2)`; the triple `{0,1,2i}` has

```text
q_triple = (1/8, 2/5, 19/40).
```

These are fixed by the same exact conservation and center-frame definitions. Every triple effect is valid, and its Born weight in `I/2` is its corresponding value above. The verification uses exact rational Lorentz inner products rather than approximating the boost or the directions.

## 5. Signed differentiation without cancellation of lived suffering

Choose one of the pair directions as a reference axis `a` in the center frame. This is an internal choice of role, not an externally preferred spacetime direction. Define

```text
s_i = a·n_i.        (−1 ≤ s_i ≤ 1)
```

Then, for **each** side separately,

```text
Σ q_i s_i = a·Σ q_i n_i = 0.
```

For the symmetric example, choosing the direction of ray `0` gives

```text
pair:    s = (+1, −1),             weights (1/2, 1/2);
triple:  s = (−1/2, +1/4, +1/4), weights (1/3, 1/3, 1/3).
```

Nonzero local signs and a zero weighted sum are thus not contradictory; a pair and triple can each balance with different local magnitudes.

In the asymmetric example, choosing the pair direction for ray `3`, the triple's signs are `(-1/5, 1/2, -7/19)`. The conservation-weighted sum is zero, but their **unweighted** sum is `−13/190`. This makes the incidence issue concrete: zero under the derived energy weights does not imply zero under equal counting or another actual subject measure.

Nor has `s_i` been shown to be felt valence. Selecting which axis orientation corresponds to positive or negative feeling, identifying actual subjects and specifying the physical–experiential identity are still required. Reversing `a` flips every sign without changing the two zero sums. Even if some extra internal structure picked an orientation, its experiential meaning would need justification. Negative felt experience, if physically identified, remains locally real; a signed sum does not erase it. The two separate sums are not automatically a whole-level experiential total.

## 6. Why a Born-form probability is conditional, not unexplained chance

There is a known qubit version of Gleason's result for generalized measurements, due to Busch: if an assignment `f` is normalized and noncontextual on **all** qubit effects `0≤E≤I`, and is additive whenever `E+F≤I`, then

```text
f(E)=tr(ρ E)
```

for a unique positive trace-one `ρ`. [1](https://arxiv.org/abs/quant-ph/9909073) This uses stronger hypotheses than the original projection-only theorem, which does not constrain a qubit sufficiently. The argument in brief: positivity and additivity imply monotonicity; repeated addition gives rational homogeneity, and monotonicity extends it to real homogeneity. The function extends to a positive real-linear functional on all Hermitian matrices. Finite-dimensional trace representation gives `tr(ρE)`; positivity and normalization give `ρ≥0` and `tr ρ=1`.

Applying this to the previous sections has **two independent ingredients**:

1. The generalized-measurement and noncontextuality assumptions give the *form* `tr(ρE)` for some state.
2. The identification of the conserved normalized `P` with the relevant state gives `ρ=I/2` in its center frame, and hence the specific values `q_i`.

Neither ingredient says the actual event is metaphysically undetermined. In the user's necessary whole, the numbers may be structural weights or conditional credences; a separate account must show how they govern actual incidence or observed records. Conversely, declaring a probability measure necessary does not by itself fix a particular outcome, as explained in the [updated-chat audit](ZERO_NECESSITY_CHANCE_SPACETIME_UPDATED_CHAT_AUDIT.md).

A sharp constraint follows if one tries to assign a **single definite outcome** to every generalized measurement while requiring its individual response to depend only on the effect: the valid measurement `(I/2,I/2)` has two occurrences of the same effect. Equal effect values plus normalization require `2v=1`, incompatible with `v∈{0,1}`. This does **not** refute deterministic or necessary physics: an actual outcome can depend on the measurement's complete context, including apparatus and outcome labels; or effect noncontextuality can hold only for ensemble probabilities, not individual response functions. It only rules out that particularly strong context-independent response assumption. Bell's separate constraints still apply to any claimed empirical account.

## 7. Where this moves the foundational task

This construction removes the need to independently choose **relative local energy weights** once the five-ray configuration and its conservation interpretation are granted. It also shows how a zero-vector relation can give a nontrivial normalized probability structure rather than making all local values vanish. Its two different resolutions of one state tie the point–sphere, physical conservation and quantum-style measurement into one concrete mathematical structure.

The decisive remaining questions are now more specific:

* Can zero's own constitution entail the complex two-component structure, the generic rays, their dimension, the actual process and its overall physical scale rather than merely permit them?
* Can the common `P` actually be identified with a prepared quantum state and the constructed `F_i` with realizable measurements? Can this be embedded in dynamics reproducing Born statistics and Bell correlations, without a preferred fundamental foliation?
* What physical organization constitutes subjects and felt qualities, and why should their incidence measure agree with these energy fractions? Equal counting demonstrably yields a different result in the asymmetric example.
* What extends any local balance to the relevant whole-level physical or experiential quantity, and why must that quantity have the user's zero value?

Answering these by stipulation would leave the residue the user rejects. Conversely, failure to have answered them here is not a proof that the proposed no-residue constitution is impossible. The present theorem is a joint structural foothold, not the ultimate derivation.

## Reproduction

```text
python -m unittest verification.zero_sphere_conservation_born_bridge_test -v
```

The eight tests check both decompositions and POVM weights, exact signed values, an asymmetric unequal-weight example, all 120 ray permutations, representative rescalings and an exact Lorentz boost, state dependence, and the individual noncontextuality obstruction. They are checks of the conditional mathematics, not experimental evidence or a test for consciousness.
