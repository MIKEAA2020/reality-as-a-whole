# A common incidence construction for overlap and the internal sphere

## The constructive result

The [previous analysis](ZERO_SUBJECT_LOCALITY_AND_OVERLAP_WEIGHTED_BALANCE.md) showed that overlapping candidate subjects can spoil a physical zero when the same local contribution is counted more than once. Here is a principled **conditional** way to remove the extra counting, and a connection back to the user's sphere:

> The local overlap-sharing rule and the earlier conservation-derived qubit POVMs are both instances of the same normalized-frame construction. In the classical case, it gives exactly the reciprocal-multiplicity rule; for the conserved `2+3` ray configurations, it gives exactly the two POVMs already obtained from the sphere.

This is a mathematical unification, not yet a physical–experiential constitution. The normalization follows without a free allocation coefficient **once** the actual supports, their weights, and the relevant local accounting principle are independently given. It does not establish those inputs, prove that quantum POVM outcomes are subjects, or turn a zero physical sum into actual experiential zero by itself.

The quantum extension reveals a further substantive limit: if subject-incidence effects and a signed physical observable do not commute, the classical sharing formula cannot automatically be read as a joint probability. A symmetric product may even have a negative expectation where a joint occurrence probability would have to be nonnegative.

## 1. Derive the classical sharing rule from explicit premises

For actual candidate subject incidences `s` with supports `S_s` and positive incidence weights `a_s`, define

```text
m_i = Σ_s a_s 1[i∈S_s].
```

Let `h_i` be the specified local signed physical contribution. At a covered site, suppose:

1. Every incidence sharing that same local contribution has the **same per-incidence local response** `v_i`.
2. The sum of its incidence-weighted responses is exactly the local contribution: `Σ_(s:i∈S_s) a_s v_i = h_i`.

Then, necessarily and uniquely under these two assumptions,

```text
v_i = h_i/m_i,
contribution of incidence s at i = a_s h_i/m_i.
```

This is not merely choosing a coefficient to make the *global* sum zero: it follows site by site from equal per-incidence response plus exact local accounting. But the local accounting identity is a **substantive physical–experiential hypothesis**. If its only justification were that it forces the desired zero, the explanation would be circular. Equal response is also substantive: physically overlapping subjects can differ in context or quality.

If the supports cover every relevant site and `Σ_i h_i=0`, then

```text
Σ_s a_s Σ_(i∈S_s) v_i = Σ_i h_i = 0.
```

This is an actual-incidence sum under the stated interpretation, not a probability distribution over merely possible outcomes. It allows nonzero positive and negative local values; a negative felt occurrence, **if** physically identified, is not erased by another value. The equation does not establish that `h_i` is felt valence, that `a_s` gives the actual incidences, or that the physical `h_i` has the relevant whole-level zero.

### The previous overlap example

For `S₁={0,1,2}`, `S₂={1,2,3}`, both `a_s=1`, we have `m=(1,2,2,1)`. With the earlier local physical rates

```text
h=(−1/2,+1/2,0,0),
```

the common per-incidence values are `v=(−1/2,+1/4,0,0)`. Their subject totals are

```text
V₁=−1/4,     V₂=+1/4,     V₁+V₂=0.
```

This contrasts with the uncorrected double-counting total `+1/2`. The result is conditional on two actual distinct incidences and the local accounting identity; the oscillator graph does not establish either.

For unequal weights `a₁=2,a₂=1` at a shared site, `m=3` and each incidence has response `h/3`; the two **weighted** contributions are `2h/3` and `h/3`. The choice of `a_s`, as well as the overall scale of felt intensity relative to physical units, remains to be physically and phenomenally justified.

### What normalization does not decide

If local responses are not equal, exact accounting alone leaves alternatives. For `a₁=2,a₂=1,h=6`, both `(v₁,v₂)=(2,2)` and `(3,0)` obey `2v₁+v₂=6`. They are formal assignments, not assertions that incompatible complete wholes are genuinely possible. Even exact physical accounting does not establish which actual subject feels what. Also, where `m_i=0`, there is no experience incidence to which the contribution can be assigned: the remainder is `Σ_(m_i=0) h_i`, which does not automatically vanish.

## 2. The same normalization as a positive-operator frame

Represent a finite family of proposed supports by positive projectors `P_s` on a Hilbert space and retain positive weights `a_s`. Define the positive frame operator

```text
S = Σ_s a_s P_s.
```

On the support of `S`, use its inverse square root and define

```text
E_s = S^(−1/2) a_s P_s S^(−1/2).
```

Then every `E_s≥0`, and

```text
Σ_s E_s = Π_support(S).
```

If the supports span the space, they form a POVM; otherwise the complementary effect `I−Π_support(S)` represents an **uncovered sector in the mathematical model**, not automatically a non-conscious physical sector. This is the standard square-root normalization used in quantum measurement theory, here applied as an incidence-frame **candidate**. [1](https://arxiv.org/pdf/quant-ph/0504083)

In a common diagonal basis, `P_s(i)=1[i∈S_s]`, so `S(i)=m_i`, and the above operators have entries

```text
E_s(i) = a_s 1[i∈S_s]/m_i.
```

Thus the classical rule is the commuting instance of the same normalization. The effects are invariant under relabelling the supports and covariant under a joint unitary change of basis: transport `P_s`, `S` and the state together. That covariance does not choose the physically meaningful supports, weights, localization, or phenomenology.

A POVM is a representation of mutually exclusive measurement **outcomes**. Several subjects may coexist; it is not legitimate to infer that only one exists from an exclusive measurement, or to interpret the POVM as actual subject-incidence weights without an additional operational and ontological argument. The formula supplies a candidate accounting structure, not a subject census.

## 3. The earlier point–sphere POVMs emerge from the same frame

For either the pair or the triple in the [five-ray conservation bridge](ZERO_SPHERE_CONSERVATION_QUANTUM_PROBABILITY_BRIDGE.md), the projectors `Π_i` and intrinsic energy fractions `q_i` satisfy

```text
Σ_i q_i Π_i = I/2.
```

Set `P_i=Π_i` and `a_i=q_i`. Then the frame operator is `S=I/2` and the normalization gives

```text
E_i = (√2 I) q_i Π_i (√2 I) = 2 q_i Π_i.
```

These are exactly the conserved-sphere POVM effects obtained earlier. This is a nontrivial common mathematical structure: the same normalization that corrects the classical overlap accounting also recovers both the pair and the triple quantum measurement effects, using their already-derived energy fractions.

The interpretation differs in the two applications. Ray directions are not established subject supports; their energy fractions are not established weights of actual experiences. The fact that the formulas coincide does not demonstrate a physical–experiential identity or derive the assumed complex sphere from zero. The condition `S=I/2` comes from the stipulated conserved ray configuration, not from arbitrary overlapping subject projectors.

## 4. Noncommuting supports: normalization can change their meaning

The frame construction is positive and normalized, but is not a free solution to quantum subject incidence. If `S` and `P_s` do not commute, the transformed effect `E_s` need not have its range inside the original proposed support `P_s`.

For a qubit take

```text
P₀ = |0⟩⟨0|,       P₊ = |+⟩⟨+|,       S=P₀+P₊.
```

The normalized effects sum to `I`, but `S^(−1/2)P₀S^(−1/2)` has nonzero support along `|1⟩`; it is not simply a positive operator localized within the original `P₀` subspace. The numerical test constructs this effect explicitly. The normalization has changed the associated operator support, so whether the normalized outcome still denotes the same subject is an additional question.

In fact, requiring two effects of the form `c₀P₀` and `c₊P₊` with nonnegative coefficients to sum to `I` is impossible: the off-diagonal entry forces `c₊=0` while the lower diagonal entry would require `c₊/2=1`. This is not a general ban on nonorthogonal supported POVMs: the trine projectors `Π_i` satisfy `Σ_i (2/3)Π_i=I`. The issue is whether the **actual** supports admit the required coverage without changing their meaning.

## 5. Incidence and signed quantum values need a joint account

Even if `E_s` is a valid positive incidence effect and `V` a signed Hermitian physical observable, the product is not generally a joint observable. Replacing it by the symmetric product

```text
(E_s V + V E_s)/2
```

makes it Hermitian but does not make it positive when `V≥0`. Take `E_s=P₊` and `V=P₀`; their symmetric product is

```text
[[1/2,1/4], [1/4,0]],
```

with eigenvalues `(1±√2)/4`. The smaller is negative. Consequently its expectation cannot generally be interpreted as the probability of two positive events occurring together.

A useful exact compatibility fact is: if `P` is a **sharp** yes/no observable and `E` is an effect, a joint POVM with marginals `P` and `E` exists only if `[P,E]=0`. Indeed, its two joint effects under the `P` and `I−P` outcomes must respectively be supported in those orthogonal subspaces; their sum `E` is then block diagonal in `P`. Conversely, if they commute, the obvious products give a joint POVM.

A sequential physical instrument is another option, but it may change the signed physical observable. For example, nonselective measurement of `X`-basis projectors transforms `Z` in the Heisenberg picture to

```text
Pₓ₊ Z Pₓ₊ + Pₓ₋ Z Pₓ₋ = 0.
```

On the initial `|0⟩` state, the original `Z` expectation is `1`, but after this operation it is `0`. This is ordinary measurement disturbance, not proof that actual consciousness entails a measurement. It shows that an operational incidence procedure cannot be presumed both to supply positive joint probabilities and leave an independently defined signed current unchanged. A physical theory must specify its actual instrument or a compatible joint structure.

Nor does a global frame operator automatically respect the preceding subject-locality requirement: if its inputs include distant supports or weights, changing them can change its normalized effects. Locality, dynamics and no-signalling require their own demonstration.

## 6. What the construction contributes to the foundation

This is a constructive bridge rather than a completed explanation:

* **One mathematical mechanism** now covers both overlapping local accounting and the conserved internal-sphere POVMs.
* **Local equal-response and budget premises** determine the reciprocal-multiplicity allocation without a further numerical allocation choice. They do not derive the premises or actual subject weights from zero.
* **Quantum positivity and compatibility** give explicit conditions any physical version must satisfy; simply multiplying a subject weight by a physical signed operator is not enough.
* **Remaining constitutive demand:** derive the actual local subjects, their felt qualities, correct incidence measure and relevant physical/experiential quantity from the self-sufficient whole itself. Show why its interactions, uncovered sectors and whole-history boundary give zero without treating unexperienced environment as experience or negating real suffering.

The stronger no-residue thesis remains live and unproved; the failure of a proposed normalization to supply those premises would not prove the thesis impossible. Mathematical normalization is not an external creator, but it is also not by itself a reason that any specific concrete physical–experiential configuration exists necessarily.

## Verification

```text
python -m unittest verification.zero_subject_incidence_frame_test -v
```

Ten checks cover equal and unequal incidence weights, the overlapping example, a coverage gap, nonunique unequal responses, the conserved-sphere frame, noncommuting support normalization, the negative symmetric-product eigenvalue, sequential disturbance and the trine control. They validate the stated mathematical constructions, not subjects, felt qualities, actual weights or global zero.
