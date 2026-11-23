# Conserved sphere, quantum steering and definite Bell records

## Main result

The [conservation–quantum bridge](ZERO_SPHERE_CONSERVATION_QUANTUM_PROBABILITY_BRIDGE.md) produced two decompositions of the same local state `I/2`: one from the conserved pair of rays, and one from the conserved triple. Here is the next connection:

> If that state is the reduced state of an assumed two-qubit singlet, **both conserved-ray decompositions also arise as remote conditional states**, with exactly the same conservation-derived energy fractions. The remote reduced state remains `I/2` regardless of which decomposition is measured.

This is a mathematical steering identity valid for **every generic five-ray configuration**, not only the symmetric example. It connects a local four-momentum conservation zero, the earlier signed directional zero, local quantum weights and quantum no-signalling in one construction. It also tells us what that connection requires: two actual subsystems and a singlet are additional physical assumptions, not consequences of five rays alone.

I then use the same sphere to specify a Bell experiment. Its singlet correlations give `|S|=14/5>2`. A concrete finite block of definite records reproduces those correlations **exactly**, respects the same marginal no-signalling and a setting-independent trial distribution, and approximately matches the additional three-outcome statistics. Its individual responses are explicitly contextual. It is a consistency construction for a definite record, **not a derivation of necessity, a relativistic mechanism, a complete reproduction of quantum theory, or an empirical experiment**.

## 1. From conservation to a singlet: what is assumed

For five generic future null rays, let the positive conserved momenta and intrinsic center frame be as in the previous report:

```text
Σ_(i∈pair) p_i = Σ_(i∈triple) p_i = P,
q_i = (−P·p_i)/(−P·P),   Π_i = (I+n_i·σ)/2.
```

On each side separately, `Σq_i=1`, `Σq_i n_i=0`, and `Σq_i Π_i=I/2`. The corresponding POVM elements are `F_i=2q_i Π_i` and sum to `I` on either side.

**Additional assumption:** there are two qubit subsystems, labelled `A` and `B`, prepared in the spin singlet

```text
|Ψ⁻⟩ = (|01⟩−|10⟩)/√2,
ρ_AB = |Ψ⁻⟩⟨Ψ⁻| = (I⊗I − Σ_(r=x,y,z) σ_r⊗σ_r)/4.
```

Both reduced states are `I/2`. The spinor pair obtained from the antipodal pair rays can be antisymmetrized to form the same mathematical singlet; but treating those spinors as **two physical subsystems** and postulating their joint preparation is a new input. A maximally mixed local state alone does not entail a singlet: for example, `I/4` has the same local reductions but no singlet correlations. The assumptions do not yet give actual subjects or show how quantum systems emerge from zero.

The center frame is determined relationally by the selected conservation configuration, not a universal preferred foliation. Relativistic localization, transport of spin frames, and the actual dynamics of two separated instruments would still have to be supplied in a physical theory.

## 2. The steering identity

Measure either conserved-ray POVM on `A`. For outcome `i`, the **unnormalized** conditional state on `B` is

```text
σ_B|i = tr_A[(F_i⊗I) ρ_AB]
       = q_i (I−n_i·σ)/2
       = q_i Π_(−n_i).
```

Its trace is `q_i`. The normalized remote conditional state is `Π_(−n_i)`. Summing outcomes,

```text
Σ_i σ_B|i = (I−(Σ_i q_i n_i)·σ)/2 = I/2.
```

Both the pair measurement and the triple measurement produce the **same** unconditional state on `B` but different decompositions into conditional states. No remote observer learns which measurement was chosen by looking at their local marginal alone. This is the usual quantum steering/no-signalling structure instantiated by the conservation-derived weights; the decomposition labels and conditional correlations are meaningful when records are compared.

The earlier signed zero now has a precise operational form. For a unit direction `a` and the remote Pauli observable `a·σ`,

```text
⟨a·σ⟩_(B | i) = −a·n_i,
Σ_i q_i ⟨a·σ⟩_(B | i) = 0.
```

Individual conditional values can be positive or negative while their **actual Born-weighted average in this stipulated singlet model** is zero. This is a measurement expectation, not a phenomenal valence. If conditional outcomes were to be identified with experience, their real subject-incidence and that physical–experiential identity would need independent justification. The sum does not remove a negative experience, and it is not a global experiential total.

The identity works for the asymmetric triple `q=(1/8,2/5,19/40)` too. Its unequal weights are essential to the weighted state and directional cancellation. Neither equal counting of rays nor the mere presence of both signs suffices.

## 3. A Bell test from the same intrinsic sphere

For the exact symmetric rays `0,2,1,i,−i`, the triple directions `n₀,n₁,n₂` form a trine: `n_i·n_j=−1/2` for `i≠j`. Choose a role within the trine and define two perpendicular center-frame directions

```text
a₀ = n₀,
a₁ = (n₁−n₂)/√3,
b₀ = (3a₀+4a₁)/5,
b₁ = (3a₀−4a₁)/5,
b₂ = a₀.
```

These are legitimate measurement settings derived relative to the trine. Choosing the role and the `3:4` measurement angle is part of the test arrangement; it is **not** derived as the unique necessary arrangement. The sphere is the center-frame state sphere of the stipulated qubit, not an externally imposed physical spherical universe.

For singlet outcomes `x,y∈{−1,+1}` along directions `a,b`,

```text
P(x,y|a,b) = (1−xy a·b)/4,   E(a,b)=−a·b.
```

Consequently the four correlations for `a₀,a₁` and `b₀,b₁` are

```text
E₀₀=−3/5,  E₀₁=−3/5,  E₁₀=−4/5,  E₁₁=+4/5,
|S|=|E₀₀+E₀₁+E₁₀−E₁₁|=14/5 > 2.
```

These are not experimental data. They are standard singlet predictions for a concrete arrangement constructed from the previously conserved sphere. Existing Bell experiments support such violations under their stated assumptions; see the [Bell and necessity audit](ZERO_NECESSITY_CHANCE_SPACETIME_UPDATED_CHAT_AUDIT.md).

For the triple POVM `F_i=(2/3)Π_i`, the singlet also gives

```text
P(i,y | triple,b) = (1−y n_i·b)/6,
P(i | triple)=1/3,     P(y | b)=1/2.
```

The triple probabilities `1/3` are simultaneously the earlier intrinsic energy fractions, provided the assumed identification of that POVM and state is physically realized.

## 4. Definite records with the same Bell correlations

To test compatibility with definite records rather than merely assert it, construct a finite table. It is a **fixed block of records**, not a probability law that independently selects an outcome. The table has one record for each of

```text
Alice setting a ∈ {0,1,T}, Bob setting b ∈ {0,1,2}, seed s ∈ {0,…,59}.
```

There are 540 records. Here `T` is the three-outcome POVM; the other Alice settings and all Bob settings have binary results. Each seed occurs once in **every** setting pair, so the empirical distribution of the chosen seed is identical across settings in this constructed block. This setting independence does not imply that full microphysical initial conditions are independent of the ultimately fixed settings.

For binary Alice settings, set `r=s mod 20`, let Alice's result be `+1` for `r<10` and `−1` otherwise, and put `j=r mod 10`. Let `K` be the corresponding entry of

```text
       b=0  b=1  b=2
 a=0    2    2    0
 a=1    1    9    5
```

Set Bob's result equal to Alice's when `j<K`, and its opposite otherwise. In every binary context the table exactly reproduces the **full joint distribution**, not merely the correlation, of the singlet for the specified directions. In particular its `|S|=14/5`, and both one-party marginals are `1/2`.

For `a=T`, set Alice's result to `i=s mod 3`, and let `j=floor(s/3)` range from 0 to 19. Bob's outcome is `+1` exactly when `j<K_(b,i)`, using

```text
       i=0  i=1  i=2
 b=0    4    6   20
 b=1    4   20    6
 b=2    0   15   15
```

The triple marginal is exactly `1/3` for each outcome, and Bob's marginal is exactly `1/2` for every Alice setting. The three-outcome joint distribution agrees **exactly** for `b₂`; for `b₀,b₁` its largest absolute joint-probability error is about `0.001197`, because the exact singlet values involve `√3` and cannot all be realized by these 60 equal counts. The tests evaluate the singlet Born probabilities directly with `4×4` matrices and compare the records against them.

Thus one explicit finite record block can have definite outcomes, CHSH violation, exact no-signalling marginals, and a setting-independent distribution of the specified seed. It does **not** reproduce all quantum statistics exactly, show how the records are generated, explain why this block exists, or make the block necessary. A fixed block and a necessary whole are distinct claims. Equal counting here is an explicitly stipulated measure over trial records, not a derived measure over conscious subjects.

## 5. What Bell forces the definite-record account to give up

The above table does **not** evade Bell while retaining local factorization. Bob's assigned outcome depends on Alice's setting at the individual-response level. For example, the same `s=1,b=0` gives

```text
(a=0): (Alice,Bob) = (+1,+1)
(a=1): (Alice,Bob) = (+1,−1).
```

This is explicit nonlocal parameter dependence/context dependence in the table, though the aggregate marginals do not signal. That operational claim is restricted to the stipulated uniform seed distribution: if a party could access or control the seed and condition on it, Bob's local result can reveal Alice's setting in cases like this. A physical account would need to explain why such access or control is unavailable, rather than just assert no signalling. The table does not itself provide a covariant physical mechanism for its context dependence. It supplies no spacetime ordering, dynamical law, preferred foliation, or intervention theory; it is therefore **not a completed relativistic model**. Bell's theorem requires relaxing some premise, not this particular one. Here measurement independence for the specified seed is retained and local factorization is not.

The constructive lesson for the user's view is sharper than “determinism can reproduce statistics”: a necessary whole with definite records can accommodate these particular Bell correlations only if its physical account explains how the relevant Bell assumptions are handled. Necessity alone does not provide that explanation. Emergent spacetime may provide an appropriate setting for such a deeper account, but this finite table does not establish one.

## 6. Remaining constitutive step

The genuinely new link is the **generic steering identity**: the same conservation-derived fractions that balance center-frame momenta determine an entire family of conditional remote states, whose weighted signed values balance and whose unconditioned state is invariant under the pair/triple choice. The finite-record construction then demonstrates that fixed outcomes are compatible with the selected correlations and no-signalling, while exposing the exact locality trade-off.

To reach the user's no-residue goal, the account must still derive the effective ray geometry and conservation, the two-subsystem singlet and its dynamics, the actual record organization and justified incidence measure, and the identity of physical organization with felt experience. In particular, the steering balance is not a proof that the whole has zero energy or zero signed experience. No preferred fundamental foliation has been assumed here, but a physical relativistic completion without one has not been supplied either.

## Verification

```text
python -m unittest verification.zero_sphere_singlet_fixed_records_test -v
```

Nine checks verify the trine and asymmetric triple against the previous five-ray Gram matrix, singlet Born probabilities using explicit matrices, steering probabilities and no-signalling, the complete finite block, exact Bell value, equal specified-seed distribution across settings, individual contextuality and the size of the trine approximation. These tests do not establish physical realization or conscious experience.
