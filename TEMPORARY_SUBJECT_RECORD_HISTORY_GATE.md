# Temporary friend records: a selector tested against quantum histories

## Result

We now test a concrete, independently specified **physical event selector** rather than merely naming subjects. The proposed event is the value of the friend's memory qubit `M` immediately after it records an input: use the two projectors `P₊=(I+Z_M)/2` and `P₋=(I−Z_M)/2`. The rule is fixed by the recording interaction, before Alice's choice, not by her eventual outcome.

This specifies a **candidate physical correlate**, not an actual subject or experience. In the ideal circuit, the standard sequential-Born probabilities for these intermediate events are compatible with Alice's later **read** experiment, but not with her later **reversal/interference** experiment: adding the two proposed history probabilities gives `1/4` for one final outcome where unitary quantum mechanics gives `9/20`.

Thus a subject theory cannot simply identify the experience with one memory value, assign the ordinary projective-history weights, and then add those weights as if this were the unchanged coherent reversal experiment. It must specify a different event/probability rule, change the physics, restrict which joint statements it makes, or otherwise address the interference. **This is a conditional gate on that particular selector and rule, not a proof that transient experiences cannot occur.**

## 1. What is known, and what is being tested here

The distinction between histories with additive probabilities and interfering histories is standard; see [Griffiths (1984)](https://doi.org/10.1007/BF01015734) and [Halliwell (1994)](https://arxiv.org/abs/gr-qc/9407040). The Wigner's-friend memory-erasure context has already been studied by [Elouard et al. (2021)](https://doi.org/10.22331/q-2021-07-08-498). We apply these known tools to the explicit local-memory selector in our [prior subject-identity](SUBJECT_IDENTITY_LOCAL_FRIENDLINESS_TEST.md) and [external-record](REVERSIBLE_FRIEND_RECORD_COMPLEMENTARITY.md) circuits. The numerical example and verifier are a scoped application, **not a claimed new histories theorem or a theory of consciousness**.

The operational event sequence uses lab time only. It does not postulate a fundamental external clock or derive temporal experience from our proposed timeless absolute.

## 2. The selector and two experiments

Use qubits `A,M,B,E`. The state after the friend-register interaction is

`|Ψ⟩=(|000⟩_AMB|e₀⟩_E + |111⟩_AMB|e₁⟩_E)/√2`,

where the record states have real overlap `r=⟨e₀|e₁⟩`, `0≤r≤1`. The ideal coherent case has `r=1`. The candidate physical event `c=+1` or `−1` is selected by the value of `Z_M` at this intermediate stage. This choice is made from the defined recording interaction; it does not rely on Alice's or Bob's later output.

- **Read (`x=1`):** Alice measures `Z_M`; outcome `a=±1`.
- **Reverse (`x=2`):** Alice applies the inverse `A→M` CNOT and then measures `X_A`; outcome `a=±1`.
- Bob measures `B₁=(3Z+4X)/5` or `B₂=(3Z−4X)/5`, getting `b=±1`.

Let `C_cab` be the chain of the proposed intermediate projector, the specified evolution, and the final Alice and Bob projectors. For a pure input state define the standard decoherence functional `D(c,c')=⟨Ψ|C_{c'ab}† C_{cab}|Ψ⟩`, with `a,b,x,y` fixed. Diagonal values are the candidate sequential-Born weights. The probability of the coarse-grained outcome, with `c` not measured or resolved, includes both diagonal and off-diagonal terms. This is a mathematical assessment of a particular family of projectors, not an interpretation-independent principle that every real event must be such a projector.

## 3. Exact failure of additivity in the reversal experiment

Take `r=1`, reverse (`x=2`), Bob setting `y=1`, and final outcomes `a=b=+1`. The verifier calculates exactly:

| Proposed history term | Value |
|---|---:|
| Diagonal weight for `c=+1` | `1/5` |
| Diagonal weight for `c=−1` | `1/20` |
| Off-diagonal term `D(+,-)` | `1/10` |
| Coarse-grained quantum probability | `1/5 + 1/20 + 2(1/10) = 9/20` |

If one instead sums only the diagonal weights, the result is `1/4`, not `9/20`. The discrepancy is interference between the two candidate histories. For the full reversal family here, off-diagonal terms between the two friend values for a given final `(a,b)` are `ab r/10` for `y=1`, and `−ab r/10` for `y=2`. Therefore, for any `r>0`, this fine-grained family fails even the real-part additivity condition. In contrast, in the **read** experiment, the final `Z_M` projectors distinguish the two intermediate values and all distinct history cross terms vanish.

The statement is not that a history *may never* be described or that some different coarse graining cannot be consistent. It is that these particular intermediate friend-value and final reversal-outcome projectors do not form an additive sequential-Born probability family when `r>0`.

## 4. The operational cost of inserting an actual measurement

The same diagonal-weight construction has a different, ordinary operational meaning: it gives the probabilities if one **physically measures `Z_M` at the intermediate stage and discards the result** before Alice's reversal. That extra intervention dephases the memory alternatives. It is not the original coherent protocol.

For the fixed settings above, the reversal outcomes then have zero `a–b` correlator; the coherent protocol has correlators `+4r/5` and `−4r/5`. Their full joint outcome distributions differ by total variation

`TV(P_coherent(a,b|x=2,y), P_intervened(a,b|x=2,y)) = 2r/5`.

At `r=1`, this is `2/5`; the coherent and intervened CHSH expressions are respectively `14/5=2.8` and `6/5=1.2`. At `r=3/5`, the difference is `6/25`; their scores are `54/25=2.16` and `6/5`.

This result **does not** show that an experience itself performs a Lüders measurement or causes collapse. It shows what follows if a proposal uses the particular projective sequential-Born rule, or if an experiment actually inserts this intervention. A hidden-variable or other completion can posit single events while preserving coherent observable statistics using a different joint law; our [previous gate](SUBJECT_IDENTITY_LOCAL_FRIENDLINESS_TEST.md) explicitly constructed such a probability extension and showed its stated Local Agency cost. A probability extension is not itself a physical completion.

## 5. What the selector must now say

1. **Standard history route.** Restrict probability assignments to suitable consistent families. The read family here is consistent; this fine-grained reversal family is not. One may retain the friend-value question within a compatible family and refrain from combining it with the incompatible final-outcome family. A concrete subject account must still say how first-person events and intersubjective comparisons relate to those descriptions. Changing description with the final experimental context is not, by itself, a demonstrated physical influence from a future choice.
2. **Single-event completion.** Retain a definite intermediate event and supply a physical joint law consistent with interference. The Local Friendliness assumptions and the exact joint-dependence bound in the previous gate then become constraints. Nonlocal, retrocausal, measurement-dependent or other responses are distinct proposals; the calculation does not choose among them.
3. **Modified dynamics.** A rule that genuinely dephases/collapses at the friend event changes the coherent predictions. It needs an independently stated physical law and empirical bounds, not the assumption that experience must collapse a quantum state.
4. **Relational or indexed events.** Define subject-indexed events without a single absolute `c`; state which comparisons and physical correlations are legitimate. Merely adding labels does not provide a probability law or a subject–physics map.

None of these routes is yet a complete solution for the user’s subject-first experiential monism. The candidate projectors concern a qubit record, not a demonstrated thinker, and cannot select or identify a phenomenal subject by themselves. Our earlier point remains: multiple irreducible subjects can avoid *assuming* combination or cosmic decombination, but we have not yet derived their individuation or unity from physics.

## 6. Verification and next dependency

[`verification/friend_history_selector_gate.py`](verification/friend_history_selector_gate.py) constructs the projectors and chain vectors exactly with rational arithmetic. It checks the full history Gram matrices for both settings at 90 rational record overlaps, the off-diagonal formula, the total-variation distance, the example above and both CHSH expressions. The formula applies analytically throughout the stated family; finite checks do not establish the result for other circuits, projectors or interpretations.

**Next necessary task:** decide what a proposed experiential ontology means by a physical correlate: a projective history with additive probabilities, a hidden/relational event governed by an explicit alternative law, or a physical collapse mechanism. A subsequent [collapse-identifiability gate](CONSCIOUSNESS_COLLAPSE_IDENTIFIABILITY_GATE.md) assesses one simple candidate collapse mechanism and shows that its reduced channel can be indistinguishable from ordinary dephasing without independent calibration; this is not a no-go for other physical models. A subject-individuation rule and empirical assessment are still required. The present calculation narrows the options; it does not decide among them or deliver a zero-residue account.
