# Vedral's quantum-wave article: sources, conservation and perspective

## Sources and scope

The supplied [*Everything in the universe is a quantum wave*](https://www.vlatkovedral.com/everything-in-the-universe-is-a-quantum-wave/) is Vedral's popular exposition, reproduced there from [the Institute of Art and Ideas](https://iai.tv/articles/everything-in-the-universe-is-a-quantum-wave-auid-3446). All three retrieved web chunks were read, including the end of the article; its illustrations and any external comments were not analyzed. The user-supplied [`everything-is-a-wave.txt`](sources/uploads/everything-is-a-wave.txt) is LaTeX source for Vedral's *The Everything-is-a-Quantum-Wave Interpretation of Quantum Physics*, SHA-256 `ac4eb842cf6231c3a884e6f27305476b62eec2950429333c435c587b0d817fd0`. All 161 lines, including bibliography and LaTeX preamble, were read. Its substantive text and displayed equation (3) closely match the [arXiv 2303.00831v1 HTML](https://arxiv.org/html/2303.00831v1), all three chunks of which were read. No byte-for-byte comparison with the original arXiv source archive was performed; do not assert its exact provenance or date from the filename or `\date{\today}`.

The supplied LaTeX is **not** simply the text of the web article. Nor is it byte-identical to the separately supplied [Quanta PDF](sources/uploads/The_Everything-is-a-Quantum-Wave_Interpretation_of.pdf), [DOI 10.12743/quanta.96](https://doi.org/10.12743/quanta.96), previously text-read in full, with selected pages visually checked. The earlier [assessment](VEDRAL_QUANTUM_WAVE_INTERPRETATION_AND_EXPERIENCE.md) concerns that Quanta version. Here the particularly important version distinction is explicit: the LaTeX/arXiv equation (3) uses `=`, whereas the Quanta PDF's page 2 uses `≥`. The [2023 Quantum Reports page](https://doi.org/10.3390/quantum5020031) was checked for equation (3) via a retrieved excerpt, not systematically compared in full.

## Vedral's proposal and the earlier comment

Vedral proposes an objective, universally quantum ontology of interacting operator-valued “q-waves.” Rather than fundamental classical trajectories or a special observer outside quantum mechanics, he describes measurement as quantum interaction and correlations. In the supplied LaTeX he distinguishes fully separated, approximately orthogonal records from more general overlapping coherent states; the web article calls his proposal one quantum world and criticizes taking classically separated worlds as fundamental. He regards his view as Everett-adjacent, but his precise emphasis is his own.

Neither quantum interference nor a coherent records model on its own proves a specific metaphysical account of experience or uniquely selects this interpretation over empirical rivals. Vedral's claim that the proposal resolves the measurement problem remains contested: no-collapse dynamics still requires an account of definite experienced outcomes and their probabilities.

## The displayed equation differs across versions

The supplied LaTeX and arXiv v1 write, in effect,

```text
Δx(t) = ℏ t / [m Δx(0)].
```

If both Δ symbols mean ordinary position standard deviations of a free particle in the same state, this equality is not generally true. In particular, at `t=0` its right-hand side vanishes although a normalizable wavepacket can have positive initial width. The PDF changes `=` to `≥`, but the printed lower bound is still twice the standard Robertson bound under that reading. With `[x,p]=iℏ` and `[A,B]=AB−BA`, one obtains

```text
[x(t),x(0)] = −iℏt/m,
Δx(t) Δx(0) ≥ ℏ |t|/(2m).
```

The Quanta PDF and supplied source instead write the opposite commutator sign; a consistently reversed commutator convention would reverse both signs and does not affect the uncertainty magnitude. If the author intended Δ to mean something other than the standard deviation at each time, that definition and derivation would need to be stated. The [previous exact Gaussian checks](verification/vedral_free_spread_gate.py) test the printed inequality and show possible initial contraction; they do not refute Mott's cloud-chamber result or any interpretation as a whole.

## Conservation: conditioning is not automatically a physical violation

The web article suggests Copenhagen conserves energy and momentum only on average, and expresses suspicion that hidden-variable and QBist interpretations have the same problem. This is not established by the article. The accounting depends on the model of the system, apparatus, driving and measurement update; interpretations differ on the status of collapse, and concrete objective-collapse dynamics may make different, testable predictions.

The following deliberately simple counterexample addresses the **blanket inference** that a different conditional energy implies a violation. Let a system qubit have `H_S=|1><1|` in energy units and let a pointer have degenerate free energy `H_M=0`. Prepare `|+>_S|0>_M` and use controlled-NOT with S as control. The unitary commutes exactly with `H_total=H_S+H_M`; it maps the input to `(|00>+|11>)/sqrt(2)`. Both before and after, the total-energy distribution is half at 0 and half at 1, with expectation `1/2`. Conditioning on pointer 0 or 1 gives energy 0 or 1 respectively. The different conditional means are not evidence of a physical creation or loss of energy: they condition on different sectors of a distribution already present in the initial state. A projection can represent such conditioning; treating it as a complete physical dynamics is a separate assumption.

The [exact rational checker](verification/vedral_energy_and_locality_gate.py) and [receipt](verification/vedral_energy_and_locality_gate.json) verify the unitary, commutator, pre/post distributions and conditional energies. This does not establish that arbitrary measurements are exactly energy-conserving without accounting for their apparatus. The Wigner–Araki–Yanase constraints matter for measurements of observables that do not commute with an additive conserved quantity, under their stated measurement and pointer assumptions. Rogers and Jordan, [*Post-selection and quantum energetics*](https://doi.org/10.1103/PhysRevA.106.052214), analyze more involved apparatus models; their abstract and selected search-retrieved passages were inspected, not the complete paper or experiment. We do not claim the simple illustration as new.

The example also should not be generalized to conservation of a unique total energy in every curved, time-dependent or cosmological spacetime: an appropriate symmetry and definition of energy are additional requirements.

## Locality, correlations and what q-waves do not establish

Local operations on one member of an entangled pair do not enable superluminal signalling to the other merely by changing the local operation. The two-qubit checker illustrates the distinction: applying a phase flip to one qubit of the entangled output leaves both reduced states unchanged but changes the joint `X⊗X` correlation from +1 to −1. This is a finite nonrelativistic illustration, **not** a demonstration of QFT microcausality or a resolution of Bell's theorem. Local interactions, no-signalling and Bell-local factorization are not identical assumptions. A local-QFT formalism can agree with Bell-violating correlations; what explains individual outcomes depends on the interpretation and its assumptions.

The web article's portrayal of QBism as simply everything happening in observers' heads is also too narrow. Fuchs, [*QBism, Where Next?*](https://arxiv.org/html/2303.01446v1), explicitly treats a measurement as an agent's action on an external world while taking quantum-state assignments as personal judgments. The abstract and selected retrieved passages were inspected, not the full 28 chunks. This clarification does not endorse QBism or claim its account of subjecthood is complete.

## Relevance to an experiential, timeless relational whole

- **Useful:** the quantum record picture treats apparatus and measured systems as physical participants, and gives a no-fundamental-collapse candidate compatible with distinct local observers. It does not require an agent or conscious observer outside physics.
- **Not established:** a physical interaction or an atom's capacity to become correlated does not by itself establish that it experiences anything. The article's speculation about quantum mechanics and consciousness is not a criterion for subjecthood, quality or persistence. Our target remains plural subjects, not a universal subject.
- **No necessary existence from persistence:** “q-numbers are always around” and never created or destroyed is an interpretive assertion, not a proof that the physical whole necessarily or self-sufficiently exists. Unitary evolution preserves a norm under a given dynamics; it does not establish why that dynamics, state, or reality exists. In quantum field theory excitations can be created or annihilated; that is different from asserting a mathematical field operator ceases to exist.
- **Not fundamental timelessness:** Vedral's fields are described at spacetime locations and times. They might form an effective account within a timeless relational whole, but neither the article nor the supplied LaTeX derives spacetime, local time or experienced succession. No external universal clock is introduced by our requirement.
- **No automatic plenitude or measure:** nonzero quantum amplitudes and possible decompositions do not prove every genuinely possible experiential occurrence is actual or yield a subject-location measure. The [contextual record gate](CONTEXTUAL_PLENITUDE_AND_RECORD_IDENTITY_GATE.md) and [observation-selection gate](SUBJECT_MEASURE_AND_QUANTUM_OBSERVATION_GATE.md) identify separate consistency and weighting problems.

The most productive reading is therefore to preserve Vedral's **physical proposal as a candidate effective layer**, not adopt its ontological claims as proofs of our whole-account. The governing research gaps remain necessary self-sufficiency, the possibility–actuality criterion, experiential subject constitution, quantum and spacetime emergence, and an empirically justified measure.
