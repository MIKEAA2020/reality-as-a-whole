# Domains, sectors and clocks: an explicit recoverability construction

## Why your distinction matters

You asked whether clock applicability might be **domain-dependent**, rather than merely “sector-dependent.” The answer is yes as a constructive possibility, but the words refer to different mathematical operations:

- A **sector** specifies a class of physical states or a spectral component *within a model*. The bound and scattering components of the recent detector cosmology are examples. They can be superposed and need not be separate realms.
- A **domain restriction** specifies which observables or degrees of freedom a description can access. Two different full states—including states in different sectors—can have the same restriction to one domain while being distinguishable by a richer description.
- A **clock/frame change** can instead be a change of representation of the *same physical questions*. Properly transformed observables and probabilities agree; changing the physical clock or the question need not give the same numerical reading.

The three distinctions are related but are not interchangeable. They are also not identical to an ontology of genuinely distinct experiential realms: the latter still needs its own constitution and evidence.

## Main new result

The previous five-ray sphere–record state contains a two-dimensional logical code with a stronger property than merely having an unchanged marginal along a few tested histories:

> **The entire confined candidate subsystem is blind to every logical state in the code—even when that logical state is entangled with an arbitrary external reference. Yet the logical quantum state and its reference correlations can be recovered from the complementary environment.**

This is an explicit recoverability result for the existing sphere–record state, not a new general quantum error-correction theorem. It gives a rigorous model of the difference between what one restricted description can see and what a richer description can recover. The detector cosmology supplies an example: the confined state is unchanged while the detector pointer changes with the internal scalar reading.

There is also a counter-control. An **optional**, generally nonlocal unitary coupling to the confined subsystem can make the hidden logical bit visible there. Thus the restriction is a property of the declared code and allowed operations, not a universal proof that interfaces or interactions are impossible. This optional unitary has not been shown to respect the cosmological constraint or to occur physically; no interface is assumed in the user's analogy.

The construction and 10 tests are in [verification/zero_domain_restriction_sector_clock_code_test.py](verification/zero_domain_restriction_sector_clock_code_test.py). Standard quantum-error-correction and decoupling results are prior work; for background see [Preskill's notes](https://www.preskill.caltech.edu/ph229/notes/chap7.pdf). The particular extraction and recovery below are specific to this project's state.

## 1. The actual confined and complementary subsystems

Use the triple-context five-ray state `|+⟩` from the existing [sphere–record construction](ZERO_SPHERE_CONSERVATION_RECORD_CURRENT_SINGLE_SYSTEM.md), and its orthogonal partner

```text
|−⟩ = Z_M₁ |+⟩.
```

These are the two logical basis states `|h=0⟩_L` and `|h=1⟩_L`. The specified confined subsystem is `S={H₁,R₁,R₂,H₂}`. Its two occupied record configurations are

```text
|s_1⟩=|0,0,1,0⟩,      |s_2⟩=|0,1,0,0⟩.
```

The complementary environment E contains the other degrees of freedom of the original finite construction: the spin systems, the five-ray pointer and the four work bits. The symbols S and E specify a tensor-factor choice in this model. Calling E “richer” here does not prove it is a distinct literal room, subject or extra spatial dimension.

Extract environmental vectors directly from the actual five-ray amplitudes:

```text
e_(r,h) = √2 (⟨s_r|⊗I_E) |h⟩_L,       r=1,2; h=0,1.
```

They obey the four-vector Gram identity

```text
⟨e_(r,h)|e_(r',h')⟩ = δ_(rr') δ_(hh'),
|h⟩_L = [ |s_1⟩|e_(1,h)⟩ + |s_2⟩|e_(2,h)⟩ ]/√2.
```

The test extracts the full 320-component vectors and verifies all inner products to numerical tolerance. The orthogonality also follows from the declared construction: the two record signs correlate with orthogonal Bob-spin eigenstates; their probabilities are `1/2` because Bob's marginal is maximally mixed and the alternative Alice instrument is complete. In each record branch the work state is an equal superposition of `|0110⟩` and `|1001⟩`, so `Z_M₁` makes its two logical versions orthogonal. The test checks this spin/work factorization separately. These statements use the model's specified state, instrument and tensor factors.

## 2. A domain restriction that hides a quantum state

For every logical state ρ_L, including coherent superpositions,

```text
Tr_E[V ρ_L V†] = ρ_S
ρ_S = (|s_1⟩⟨s_1| + |s_2⟩⟨s_2|)/2,
```

where V maps the abstract logical basis to the two sphere–record states. More strongly, let A be any *additional external reference factor* and let `ρ_LA` be arbitrary, including entangled states. Then

```text
Tr_E[(V⊗I_A) ρ_LA (V†⊗I_A)] = ρ_S ⊗ ρ_A.
```

The identity follows directly from the four-vector Gram matrix: the trace over E eliminates off-diagonal logical and confined-record terms while retaining `ρ_A`. Equivalently, for every confined observable X,

```text
V† (X_S⊗I_E) V = Tr(ρ_S X_S) I_L.
```

So no measurement available **only on S** reveals which logical state was encoded, and S is uncorrelated with the extra reference A in this encoding. This includes mixtures, coherent superpositions and logical/reference entanglement—not just a handful of phase choices. Tests contract the actual environmental amplitudes for a Bell state and an asymmetric complex state.

The scope is crucial. **E itself is not independent of S.** In fact the environmental label r is perfectly correlated with the confined record r: for either r, `Pr(S=r and E has r)=1/2`, not `1/4`. Thus this result does not claim that the whole complementary domain is causally or statistically disconnected from S. A in the product formula is an additional reference, not a relabeling of all of E. Moreover, code-preserving dynamics is assumed; arbitrary physical interventions can leave the code.

The confined state is a 50–50 mixed record state, not a definite surface position A or a selected subjective outcome. It is a mathematical analogue of an unchanged restriction, **not** an implementation of the user's held-A position rule.

## 3. The missing information is recoverable, not nonexistent

Because the four `e_(r,h)` are orthonormal, define an isometry on their span by

```text
R_E |e_(r,h)⟩ = |h⟩_L ⊗ |r⟩_gauge.
```

Extend it to a physical channel on the rest of E by specifying a failure/auxiliary output. After applying this recovery to E and discarding the gauge and S, the result is exactly `ρ_LA`, including its correlations with A. The tests perform the decoding using the extracted finite vectors and recover both a logical–reference Bell state and an asymmetric complex state.

This is not cloning: S contains no logical-state information in the code. E can simultaneously retain the separate classical record label r and recover the logical qubit. Nor is this an assertion that the recovery is local, energetically free, available to an inhabitant, or performed by an actual subject. It is an explicit **mathematical recovery map**, not a proposed microscopic apparatus.

The sphere/record table is another joint observable involving E, not something determined by `ρ_S` alone. In this state family it remains the previously derived table; that separate fact is tested in the earlier [finite-instrument report](ZERO_SPHERE_QUANTUM_COSMOLOGY_FINITE_CLOCK_INSTRUMENTS.md). Pair and triple contexts share the same confined code density but have different environmental vectors; they are alternative settings, not simultaneous incidences.

## 4. One constrained model: a hidden clock and a visible pointer

Apply the encoding to the same [autonomous detector cosmology](ZERO_SPHERE_AUTONOMOUS_CONSTRAINED_DETECTOR.md). The evolving logical state becomes entangled with geometry and the detector D, but the interaction preserves the logical code. Treat geometry and D as the additional reference A in the theorem. At every scalar-clock reading in this specified model,

```text
ρ_SD(φ) = ρ_S ⊗ ρ_D(φ).
```

The tests contract the actual encoded environment with the detector wavefunctions at scalar readings 0, 40 and 100. This is stronger than merely finding a fixed mean: the *complete* S–D state factorizes, while D itself changes. Numerically, for the chosen N=40 incident packet,

```text
Pr(D=1 | φ=0)   ≈ 0,
Pr(D=1 | φ=100) ≈ 0.958898.
```

If the two readings are supplied with equal prior probability, a measurement restricted to S has optimal discrimination probability `1/2`: the reduced states are identical. The simple rule “guess 100 when D=1, otherwise guess 0” succeeds with probability approximately `0.979449` when the detector pointer is available. This is an operational comparison of two conditioned preparations and a specified measurement; it is not a literal observer outside the whole or proof of subjective time. Nor does one binary pointer identify every scalar reading or constitute a universal clock.

The spectral sector and the domain restriction are demonstrably different distinctions. In the same regulated interacting model, choose (i) a normalizable bound eigenstate in the `h=0,d=+` channel, or (ii) the earlier incident packet. The first is stationary up to phase and has `Pr(D_z=1)=1/2`; the second exhibits the changing detector probabilities above. Both restrict to the same `ρ_S`. The incident preparation need not lie purely in the scattering sector—it has small bound components—so this comparison does not mislabel finite interior eigenvectors as continuum scattering states. The continuum existence of bound states was proved in the [spectral analysis](ZERO_SPHERE_INTERACTING_CLOCK_SPECTRUM_AND_BOUND_STATES.md).

Thus **different sectors can share a confined domain description**, and **different domains can have different access to one physical state**. Neither statement alone establishes distinct metaphysical worlds.

## 5. No automatic interface—but one can be specified

The decoupling property is not automatic for every unitary on the combined system. Define the confined swap X that exchanges `|s_1⟩` and `|s_2⟩`, and on the four-dimensional environmental span choose the controlled operation

```text
U_leak = Σ_(r,h) X_S^[(r−1) XOR h] ⊗ |e_(r,h)⟩⟨e_(r,h)|,
```

extended as the identity on the orthogonal environmental complement. It is unitary: it applies either a swap or the identity on mutually orthogonal environmental sectors. On the two encoded states it yields

```text
U_leak |h⟩_L = |s_(h+1)⟩ ⊗ [|e_(1,h)⟩+|e_(2,h)⟩]/√2.
```

The confined record can now distinguish h=0 from h=1 perfectly. The test constructs the output from the actual environmental amplitudes and verifies normalization and both confined record distributions.

This is a **counterfactual finite-kinematical control**. It is generally nonlocal, takes states outside the original protected code, and has not been shown to commute with the cosmological constraint or be realizable by a local interaction. It does not imply that confined inhabitants register the richer activity. Its value is to separate the two issues: the current code and allowed evolution yield no logical information in S; an independently specified admissible interface would need to be justified and analyzed, not assumed or ruled out by analogy.

## 6. Relation to the surface, chess and relativity

In your surface analogy the traveler is not a confined surface inhabitant. In the **surface-restricted description**, the traveler's position stays A throughout the room journey and changes to B on return; its room position actually traverses the chord. In chess the player is not a piece: thinking is not a game move, so the position and half-move count remain fixed during thought. No interaction is needed merely to hold either restricted description fixed, and no inhabitant is presumed to observe the richer activity.

The mathematical code captures a related but narrower fact: many richer logical states and pointer histories induce the same S restriction. It does not reproduce a single definite A followed by B; that would require a further specified record/event construction. The quantum state of S is mixed, and no outcome or experience is selected by this calculation.

Relativity supplies a useful comparison: physical clocks follow particular paths and need not agree about elapsed proper time; coordinate choices may work only in a region. A domain restriction adds a different issue—**which observables are available at all**. Two representations of the same physical question must still agree after proper transformation; different clocks or domains can ask different questions. No preferred fundamental foliation is implied.

## 7. What this advances and what must be derived

This result converts the conceptual distinction into a structural test: a restricted domain can be completely blind to a logical degree of freedom, including its entanglement with a clock or pointer, while another mathematically specified subsystem can recover that degree of freedom. It also shows that an explicit coupling can invalidate that blindness. That is a sharper target than simply calling time “sector-dependent.”

However, the selected tensor factors, code state, constrained interaction and physical measure remain inputs. Neither quantum recoverability nor the point–sphere picture by itself establishes real subjects, experienced passage, or which domains are actual. A zero constraint is not yet the proposed objective whole-energy zero; a signed global experiential sum, if derived, would not erase suffering locally. The thesis that all genuine possibilities are actual and necessary remains to be connected to the physical state and incidence measure rather than inferred from the code.

The next discriminating step is to investigate whether a **constraint-compatible, spatially local** interaction can realize a controlled interface or a durable internal record without imposing a preferred foliation, and to derive or independently test which physical restrictions correspond to enduring subjects and actual experience. In parallel, the interacting geometry-clock map through the interaction region remains open; the prior asymptotic scattering map is not its substitute.

## Reproduce

```sh
python -m unittest verification.zero_domain_restriction_sector_clock_code_test -v
```

The algebraic decoupling/recovery implications follow from the Gram identity and linearity. Tests verify the Gram vectors, their physical factorization, explicit recovery, two logical/reference states, the optional leakage unitary, the pointer history and the bound/incident comparison. Numerical pointer results use the earlier finite cosmology discretization. None is an empirical observation or proof of the proposed ultimate ontology.
