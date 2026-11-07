# Thoughtful Local Friendliness and subject-first reality

## The supplied paper

The attached `q-2023-09-14-1112.pdf` is Howard M. Wiseman, Eric G. Cavalcanti and Eleanor G. Rieffel, [“A ‘thoughtful’ Local Friendliness no-go theorem: a prospective experiment with new assumptions to suit”](https://doi.org/10.22331/q-2023-09-14-1112), *Quantum* **7**, 1112 (2023); [arXiv:2209.08491v4](https://arxiv.org/abs/2209.08491). This audit is based on the supplied 44-page paper, including its definitions and experimental proposal. It is not a claim that the proposed experiment has been performed.

**Why it matters here:** the paper makes explicit a challenge our subject-first account must face. Taking several experiences to be real does not, by itself, tell us which definite thought-events exist during a reversible quantum measurement or how different subjects' records fit into a single account. The paper supplies a conditional theorem and experimental roadmap for part of that issue; it does not prove that subjects combine, decombine, or arise from quantum computation.

## 1. What the theorem actually assumes

The authors' *thoughtful Local Friendliness* (`LFϑ`) uses the following four **joint** metaphysical assumptions, stated informally here; their precise wording is on pp. 13–15:

1. **Local Agency:** appropriate randomized interventions are uncorrelated with relevant physical events outside their future light cones. This combines a substantive intervention-independence condition with a relativistic causal condition; it is not merely “no faster-than-light signalling,” nor is it the same as Bell's Local Causality.
2. **Physical Supervenience:** each thought depends on physical events in an appropriate bounded spacetime region. This assumption neither identifies a thought with its physical correlate nor establishes its absolute reality.
3. **Ego Absolutism:** *my communicable thoughts* are absolutely real, not only facts relative to another observer or a particular world. This is stronger than simply acknowledging that one's experience is real.
4. **Friendliness:** if a system displays independent cognitive ability at least on par with mine, it has comparable cognition and its communicated thoughts are as real as my own. The authors deliberately say **thought**, not necessarily conscious thought, qualitative experience or sensation. Friendliness on its own does not assert absolute reality; together with Ego Absolutism it does so for the relevant communicated thoughts.

The paper also posits two technological capabilities: practically implementable human-level artificial intelligence and sufficiently capable universal quantum computing. Together, the stated four metaphysical and two technological assumptions lead to the contradiction formulated in the paper (Theorem 1, p. 5), subject to its experimental and methodological framework. The authors emphasize that the **universal validity of quantum theory is not one of those assumptions**; the universal quantum computing premise is a claim about attainable operations and correlations, not a separate statement that every physical process obeys quantum theory.

A mathematical inequality can be derived from the metaphysical assumptions under the stipulated spacetime and record conditions without assuming quantum theory. Quantum predictions or the quantum-computing premise then supply correlations that violate it. This distinguishes the derivation of the bound from the feasibility and physical realization of its violation. The paper's conclusion is that the six claims cannot **all** be held as formulated; it does not identify a single necessarily false assumption.

## 2. The proposed friend, and the importance of undoing a record

The authors envision an artificial agent called **Quall-E**, with human-level cognitive performance, running reversibly on a quantum computer. An entangled qubit pair is shared between Quall-E and Bob. Quall-E registers one qubit and encodes a message. Alice randomly either:

- **reads:** reads the message and uses it as her outcome; or
- **reverses:** coherently returns the unread message and reverses the relevant computation, then measures in another basis.

Bob independently chooses a measurement on his qubit. The relevant operational probabilities concern Alice and Bob's settings and results. The friend's postulated earlier outcome is not generally available as a surviving record in the reversal condition. The authors stress that *logical* reversibility, not perfect physical reversibility of every control or error-correction mechanism, is required; a noisy realization can suffice if it yields a statistically meaningful violation.

This deepens, but does not overturn, our [record-persistence audit](DISTRIBUTION_CUT_AND_RECORD_PERSISTENCE.md): absence of a later record is not by itself evidence that no earlier event or experience occurred. Conversely, treating a past event as absolutely definite in every run is an assumption with operational consequences under the full LF setup, not something established merely because a computational register was once correlated.

## 3. The exact implication for the subject-first account

Separate four claims that must not be conflated:

- **Reality of experience:** there is a subject's experienced episode. This is the datum we are trying to retain.
- **Plurality:** multiple subjects can be real, without their combining into a larger subject or splitting from a universal one.
- **Absolute single-event assignment:** in each relevant run there is one definite value of the named friend's thought, also usable in the joint probability model across Alice and Bob's settings.
- **Record survival:** a later system still contains a readable record of that thought.

The first two do **not automatically imply** the third or fourth. Equally, denying record survival does not automatically deny the earlier episode. The paper's formal argument turns on a stronger joint structure: its assumptions give a single-valued friend variable `c`, common joint probabilities and Local Agency restrictions, as well as agreement `a=c` when the record is read. For its two-setting/one-friend case the resulting inequalities have the same mathematical form as CHSH; in more general scenarios Local Friendliness can be strictly weaker than standard Bell assumptions. A violation does not establish that physics is local, that thoughts are unreal, or that quantum mechanics alone has decided how many subjects exist.

Our previous statement that subject-first plurality avoids the classic subject-summing and cosmic-subject-splitting problems **remains a conditional architectural advantage**. It did not supply a rule for subject identity, number or incidence through preparation, copying, superposition and reversal. This paper makes that unresolved issue sharper, not a solved problem. Nor does it imply that an artificial system is conscious because it performs a sophisticated task. The authors intentionally formulated their thought assumption without taking a position on qualia.

### A directly relevant published challenge

[Adrian Kent, *Friendly thoughts on thoughtful friendliness* (2023)](https://arxiv.org/abs/2302.12707) argues that the original assumptions need clarification or strengthening to exclude changing numbers of thoughtful agents at different stages, and questions the motivational substitution of human-level cognitive ability for conscious thought. This is a **published objection**, not an established refutation of the final theorem. It is especially relevant to our subject-first proposal: to infer a single `c` one needs to specify which individual is Charlie and how identification works if physically allowed descriptions include copies or mergers. Whether a particular interpretation satisfies the authors' four assumptions remains a matter of explicit modeling, not a free escape obtained merely by saying “plural subjects.”

A subsequent [subject-identity gate](SUBJECT_IDENTITY_LOCAL_FRIENDLINESS_TEST.md) checks a single-friend extension in an exact quantum circuit and makes the limitations of a plural-event bookkeeping alternative explicit. It finds a sharp hidden-joint-dependence bound under stated assumptions; it does not provide a physical selector or a completed observer-relative model.

## 4. What experiments actually show

The earlier Local Friendliness proof-of-principle used the path degree of freedom of a photon as the “friend,” not a human or established conscious observer. The attached paper calls the proposed Quall-E experiment future work. Its resource numbers are **conditional estimates**, not fixed technology forecasts: with selected assumptions for a very large human-level algorithm, reversible compilation and error correction, its illustrative estimate for one second of human-scale activity is roughly `1.89 × 10^10` seconds (almost 600 years) on the modeled machine. Different HLAI algorithms, architectures and assumptions change this result.

There is a more recent intermediate result: [Laux and Cavalcanti (2026), arXiv preprint](https://arxiv.org/abs/2609.12527), report quantum-computer implementations with rudimentary reversible agent-like circuits. The agents have small memories and simple conditional actions, not human-level intelligence or demonstrated experience. In the authors' one-friend two-setting setup, the mathematical inequality has CHSH form; the paper says the test is not loophole-free. For the betting circuit, it reports a shifted LF value of `0.306 ± 0.012` and an estimated readout mismatch of `0.0171 ± 0.0019`. Its relaxed test uses `S_LF ≤ 4ε` and quotes an admissible threshold of `0.0673`; its independent calibration is **an estimate, not a rigorous upper bound** on ε in the relevant experimental run. Internal setting generation, lack of spacelike separation and the gap between a toy circuit and a thoughtful friend limit the interpretation. This is a reported research milestone, not a demonstration that Local Friendliness fails for conscious observers or that a consciousness theory is true. We have not reanalyzed the experiment's raw data.

## 5. The live choices—not a forced verdict

If a future experiment genuinely met the technological, identification, record and spacetime conditions and violated the relevant inequality, then the stated joint assumptions could not all stand. Candidate responses include, among others:

- revise a suitable locality/agency assumption;
- revise the assumption that all relevant communicable thoughts have absolute single values in the required joint account;
- reject or refine the behavioral criterion for attributing the same kind of thoughts, without inferring that other human experiences are unreal;
- revise bounded physical supervenience;
- challenge whether the hypothesized reversible operation or human-level cognitive capability is physically attainable.

These options are not equivalent and cannot be declared equally plausible by the theorem. In a *completed observed violation* with every experimental condition and mathematical assumption sufficiently established, merely questioning the two technological assumptions would not explain that observed result; here the decisive experiment remains prospective. A proposed multiple-subject or relative-event alternative must work through the actual probability constraints, not simply replace a verbal label.

Our timeless absolute and emergent spacetime are not automatically inconsistent with the paper: Local Agency is formulated using light cones in the operational experimental regime, not as a proof that spacetime or an external clock is fundamental. But our project has not derived that regime or a relativistic event structure from the timeless absolute. Likewise, **real first-person acquaintance is not identical to the paper's Ego Absolutism**: preserving the former does not automatically entail its global single-event condition. The user's strong `possibility = actuality` does not itself settle whether the relevant event model is single-valued or subject-indexed; the experiment's settings are operational interventions, not a mechanism for actualizing unreal possibilities.

## 6. Research decision

The attachment identifies a new load-bearing task for a subject-first framework: specify a duality-consistent mapping from physical processes to **which subject has which thought/experience and which records can be jointly compared**, then test it against this no-go theorem's explicit premises. This connects directly to the project's subject-boundary, record and causal-identifiability work; it is not evidence that the subject-first view has been refuted or confirmed, nor a solution of the experiential character or problem of time.
