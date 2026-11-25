# One disturbed history, two experiential bridges

**Status: exact finite-model result, conditional on an explicit subject and access bridge.** This is a common-domain test using the *existing* internal-reference gate and all 16 relative-clock histories, not a claim to derive experience, brains, or subjects from the circuit. The central result is constructive: the same final physical history admits two gauge-compatible signed-quality assignments, both mirror-balanced under the same Born-weighted incidence assumption, which agree before the disturbance and disagree afterward on exactly one quarter of the weight. Zero plus this particular paired plenitude therefore does not select between them.

The physical construction and its limitations are in [the internal-reference report](ZERO_INTERNAL_CONTEXTUAL_REFERENCE_AND_RECORD_TRADEOFF.md). Executable checks are in [the verifier](verification/zero_internal_reference_subject_valence_candidates_test.py). The meditation case in [the Yang audit](YANG_7T_JHANA_PRIMARY_SOURCE_AND_INTERFACE_AUDIT.md) only motivates separating felt quality, self-boundary, access and later report; it is not a circuit-to-brain identification.

## 1. Common carrier and the extra premises

For each existing normalized input history |Ψℓ⟩, ℓ=0,…,15, Bob's sphere sign B and his old record Zj have eigenvalues b,z=±1 and obey **B Zj|Ψℓ⟩=|Ψℓ⟩**. A valid internal sign instrument measures Cint and writes its outcome s=±1 into a neutral pointer M. The outcome branches are (I+s Cint)|Ψℓ⟩/2. The gate preserves B but disturbs Zj. Because Cint and Zj do not commute, the pre-gate j value and post-gate j value must not be treated as one nondisturbed joint observable.

To compare putative experience on *this* domain, stipulate conditionally:

1. Each eligible history carries one fixed, persisting subject-carrier through the gate, with one incidence per joint final outcome, and no creation or deletion of carriers. A fixed carrier identity is a rule here, not a derived subject selector or proof of phenomenal continuity.
2. The sign pointer M supplies a common orientation reference. The two proposed signed qualities, for a positive scale κ, are

   **v_record = κ s z**, and **v_sphere = κ s b**.

   Thus neither the bare record z nor the bare conserved sign b is equated with valence. Without M the two are merely different physical correlations, not the mirror-odd signed quantities below. Both are additional psychophysical bridges.
3. For numerical incidence statements only, assign joint incidences the circuit's Born weights. Neither the existence of subjects nor the identification of their measure with Born weight follows from the unitary circuit.

On the input support, the operators Zj ZM and B ZM agree for **any** pointer state because B=Zj there. This is an operator-on-state equality, not a claim that the post-gate pointer was already measured before the gate. On the final history their values disagree precisely when b≠z. Hence the candidates provide a common-domain comparison without importing the earlier sphere-record subject graph.

In particular, these are **not** asserted to be the old current and mismatch bridges. The earlier [subject–experience comparison](ZERO_SUBJECT_EXPERIENCE_BRIDGE_COMMON_DOMAIN_TEST.md) has additional reference qubits, a selector Hamiltonian and different variables. No embedding or mapping from those variables has been established here.

## 2. Actual post-gate joint distribution

For every ℓ, let i=0,1,2 denote Alice's old record. Each number in the table is the **joint** Born weight P(i,b,z,s); the same row applies separately to s=+ and s=−. Entries not shown have zero weight.

| i | b | z | each s | 
|---:|---:|---:|---:|
| 0 | + | + | 3/80 |
| 1 | + | + | 1/20 |
| 2 | + | + | 13/80 |
| 0 | − | + | 1/80 |
| 1 | − | + | 1/40 |
| 2 | − | + | 3/40 |
| 0 | − | − | 1/80 |
| 1 | − | − | 1/40 |
| 2 | − | − | 3/40 |

Consequently P(b≠z)=1/4, including conditional on either s. The values of the two signed bridges are opposite on exactly that weight and equal on 3/4. Both sign outcomes and both b values have weight 1/2; post-gate P(z=+)=3/4. The old record is disturbed, while B retains the pre-gate record value in this history. This is not an assertion that a confined observer can access B.

The verifier computes the complete i,b,z,s table directly from all 16 quantum histories, rather than extrapolating from a single case. It also checks the old clock, work and diagonal G constraints on the projected components and the dressed gauge on those components.

## 3. Gauge, counterparts and persistence

The previously specified dressed gauge acts on the original registers as Gint=U B Zj and trivially on M. On the full valid matrix domain, both Zj ZM and B ZM commute with this gauge. They are distinct even after restriction to valid support: they are not identified by **this** gauge action. This does not prove the dressed choice is the ultimate gauge group; requiring bare U as an additional gauge has the known obstruction discussed in the source report.

There is a different involution, the exchange S of the internal reference spins together with a flip XM of the sign pointer. It exchanges the two sign branches of the actual extended state, leaves b and z unchanged, and negates *both* candidate qualities. The verifier checks the branch relation and the operator transformation. This is a counterpart symmetry of this modeled final state, **not** an established physical time reversal or a derivation of universal mirror plenitude. A subject-incidence rule must still say whether its symmetry-related alternatives are distinct actual incidences rather than gauge copies, and must provide their weights.

The fixed-carrier persistence rule keeps subject incidence independent of the outcome and of the selected bridge. It gives a meaningful controlled comparison but does not solve the problem of personal identity: one might instead posit branching subjects, a graph selector or a nontrivial incidence rule. These require additional compatible structure and could change the accounting. In particular, the older selector and Hamiltonian have not been shown to exist on this history.

## 4. Access: an exact conditional limit, not a consciousness test

Assume M has been registered in its computational basis and is available alongside one other system. Trace out everything else. The verifier constructs the subnormalized conditional density matrices of the target binary parity and uses the Helstrom optimum, Pguess=(1+||ρ+−ρ−||₁)/2, for **arbitrary POVMs on the stated accessible subsystem**:

| Accessible post-gate system | Candidate directly readable | Best guess of other candidate |
|---|---|---:|
| j + M | s z | s b: **3/4** |
| B + M | s b | s z: **3/4** |
| B + j + M | both | **1** |

Both 3/4 optima occur for all 16 histories; reading the available sign and using the available record achieves them. The proof is quantum, not just a restriction to classical readout, but is conditional on the sign pointer having been registered and on the assumed subsystem boundary. It does not say that every internal subject has this access, that an outcome is consciously felt, or that subjective reports are truthful. Report noise can obscure even a genuine difference.

A useful interface consequence: if Alice's **classical i record** as well as j and M is made jointly available, the best classical table-based guess of s b improves from 3/4 to **4/5**. The required cross-realm or communication interface is not supplied by the model, and this is not a bound on arbitrary access to all of Alice's coherent degrees of freedom. Direct B access would instead give perfect discrimination of the two candidate values on mismatch events. One cannot assume off-realm access merely because the global description contains the data.

Both final parities admit a nondemolition reporting construction if a suitable additional neutral report qubit is available: for V=Zj ZM or B ZM, let P−=(Pvalid−V Pvalid)/2 and Ureport=(I−P−)⊗I+P−⊗Xreport. These projectors commute with the dressed gauge, B, Zj and the already-written M, and Ureport is unitary. Thus neither candidate is excluded by an in-principle **post-gate** gauge-compatible report operation in the enlarged mathematical system. Accessibility, the extra qubit, its preparation and a truthful phenomenal-to-report coupling remain premises; no claim is made that the earlier record-writing gate is undisturbed.

## 5. What zero and necessary plenitude do—and do not—select

Under the stipulated one-carrier/Born-incidence rule, s is balanced for each (i,b,z), so both ⟨v_record⟩ and ⟨v_sphere⟩ are exactly zero. Each has half positive and half negative incidence weight. Thus the different unreferenced means ⟨z⟩=1/2 and ⟨b⟩=0 after disturbance do **not** distinguish the signed candidates: multiplying by the shared, balanced s changes the accounting. That correction matters for the proposed cancellation argument.

A mismatch-only alternative illustrates a real selection consequence: set q=(1−s z)/2 and w=−κq, or use q=(1−s b)/2. With the same incidence measure each has mean −κ/2. If, additionally, this w is the complete additive whole-level experiential quantity, the selected incidences exhaust reality, no other contributions compensate, and that total must equal zero, it fails those combined premises. This is a deliberately chosen negative-or-zero mapping with the sign pointer as reference; it is not a derivation of the older model's mismatch q, and negative felt experience is not absence.

More importantly, whole-zero alone does not imply equal counterpart weights. The verifier constructs a strictly positive normalized incidence measure on the same support by shifting a small amount from s=− to s=+ on b=z=+ and an equal amount in the opposite signed-quality direction on b=z=−. Both candidate signed sums remain zero, but weights are unequal within those counterpart pairs. This measure is **not** the circuit's Born measure: it is a mathematical counterexample to deriving pairwise equal incidence merely from global signed cancellation. Conversely, equal Born amplitudes do not by themselves establish subject incidence or measure.

A potentially generative necessity principle would therefore need to establish, rather than stipulate: (a) why the complete subject-incidence space is closed under an appropriately physical counterpart map; (b) why the map reverses the relevant intrinsic experiential contribution; (c) why it pairs distinct actual incidences rather than gauge descriptions; (d) why their incidence measure is invariant and finite/convergent; and (e) why one particular physical relation, rather than both v_record and v_sphere, fixes felt sign. Parts (a)–(d) can yield pairwise cancellation, but this worked example demonstrates that **even all of them, as imposed here, leave (e) open**. Nor does failure of one selected subsystem to cancel establish failure of a whole-zero ontology: other incidences, weights or contributions may exist.

## Subsequent persistence and access tests

[Can subject persistence determine experiential sign?](ZERO_PERSISTENT_CARRIER_AND_SIGN_SELECTION.md) constructs conserved carrier-sector projectors on this same gate, derives a restricted stability-based selection theorem and tests an explicit memory-dependent counterexample. It also distinguishes the sequential readout experiment from the unmeasured coherent history.

[Sphere memory, subject access and a discriminating report](ZERO_SPHERE_MEMORY_EXPERIENCE_ACCESS_AND_REPORT.md) then tests these two original candidates on the sphere-coupled reservoir and auxiliary apparatus. It proves a no-reference factorization, specifies when a source-reference interface improves access to the sphere parity, and separates physical parity readout from an independently postulated report of felt sign.

## 6. Next constructive target

The sharp remaining problem is not to pick one sign by aesthetic declaration. Construct a compatible subject selector and persistence dynamics on this *same* history, and derive a reference-sensitive intrinsic bridge from their constitution. Then determine whether its allowed physical transformations force one of these two parities, admit both, or require a different quality variable. A successful derivation must distinguish an actual subject from an arbitrary carrier, identify the subject's accessible algebra and report mechanism, and justify its incidence measure without assuming that every mathematical branch is a subject. This preserves the user's zero/plenitude proposal as a substantive generative program while exposing exactly which connection is still being sought.
