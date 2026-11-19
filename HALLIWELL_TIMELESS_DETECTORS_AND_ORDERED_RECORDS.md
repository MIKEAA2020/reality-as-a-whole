# Timeless detectors and relational order

## Source and coverage

J. J. Halliwell's [*Trajectories for the Wave Function of the Universe from a Simple Detector Model*](https://arxiv.org/html/gr-qc/0008046v2), [published-paper DOI](https://doi.org/10.1103/PhysRevD.64.044008), has now been read in full as the arXiv v2 HTML text, including its references. Its equations were read through HTML/LaTeX text, not systematically checked against rendered pages; this is not independent verification of every calculation. The published version has not been compared in full with the preprint. This supersedes the partial-reading statement in [the Vedral assessment](VEDRAL_QUANTUM_WAVE_INTERPRETATION_AND_EXPERIENCE.md).

Halliwell later developed related machinery in [*Probabilities in Quantum Cosmological Models: A Decoherent Histories Analysis Using a Complex Potential*](https://arxiv.org/abs/0909.2597), [published-paper DOI](https://doi.org/10.1103/PhysRevD.80.124032). Its arXiv v1 HTML text has since been read in full, including captions and references, but its figures were not visually inspected and its proofs were not independently audited; see [the dedicated assessment](TIMELESS_CLASS_OPERATORS_DECOHERENCE_AND_JOINT_EVENTS.md). It reports constraint-commuting class operators and approximate decoherence in specified WKB regimes; these claims are not being treated as independently established by the present check.

## What Halliwell's model supplies

The paper adapts Mott's cloud-chamber idea to a constrained system, using detector degrees of freedom **inside** the closed description. For two two-state detectors, it obtains in perturbation theory a detection amplitude proportional to `G f₂ G f₁|ψ⟩ + G f₁ G f₂|ψ⟩`, with a Green operator `G`, localized couplings `f₁,f₂`, and specified boundary conditions. The sum does not select a preferred detector ordering. Under a semiclassical stationary-phase argument, amplitudes are enhanced for detector regions lying along classical paths; this is conditional on the approximation and the state, not a general exact theorem that all solutions yield classical worlds.

The full system plus detectors satisfies its total constraint exactly. The detected subsystem amplitude is generally sourced inside the detector regions; the paper treats it as approximately satisfying the unperturbed constraint for weak coupling. A small absolute source term alone is not automatically a relative-error bound for a small detected component; an application needs a specified norm, scaling and boundary conditions. In a discrete equal-frequency oscillator model, the paper projects coherent states onto a fixed-energy subspace and describes states concentrated along entire closed orbits. It explicitly flags redundancy from multiple labels on the same orbit.

The ideal two-state detector can flip back and fails as a robust “ever entered” register beyond a suitable weak-coupling/dwell regime. Its oscillator detector improves the response but can also recur because its driving integral can cancel. The author does not claim an exhaustive derivation of emergent trajectories. These qualifications matter: a mathematical orbit label is not automatically a locally readable, durable memory of a past event.

The preprint's reference 23 lists Mott with volume/page `A124, 375`, which are instead the bibliographic coordinates given for [Darwin's collision paper](https://doi.org/10.1098/rspa.1929.0123). [Mott's *The Wave Mechanics of α-Ray Tracks*](https://doi.org/10.1098/rspa.1929.0205) is volume `A126`, pages `79–84`. This is a bibliographic mismatch in the inspected preprint, not a finding that Mott's result is wrong; the Mott and Darwin papers were identified, not fully re-read for this assessment.

## A bounded test: unordered visits versus relative order

An unordered collection of “ever visited” answers can lose a distinction required for a local chronology. This point is not a new theorem about time: conditional clocks and invariant observables are established approaches, including [Page and Wootters](https://doi.org/10.1103/PhysRevD.27.2885), and this repository already has a [stationary path accumulator](OPERATIONAL_PATH_ACCUMULATOR.md). The following explicit finite example applies those ideas to Halliwell's specific unordered-detection question. Its site-visit effects are mathematical projectors, **not a replay or physical implementation of Halliwell's detector**.

Use an internal six-position dial `c`, a six-site system `x`, and a direction bit `d=+1` or `−1`, all stipulated. Define the unitary permutation

`W|c,x,d⟩ = |c+1, x+d, d⟩` (indices modulo 6).

For each `d`, the normalized state `|Ψ_d⟩ = (1/√6) Σ_c |c,dc,d⟩` is invariant under `W`. It is therefore in the zero eigenspace of the positive finite constraint `2I−W−W†`. The dial and system are components of the same stationary state; this is not a postulated external universal clock.

Define the “ever visits site a” projector by the Boolean OR of the six commuting, diagonal, time-translated site projectors in this particular model. Each system orbit traverses every site, so the projector is the identity for **each** site. Both histories consequently answer yes to visiting sites 1 and 2, and indeed every site. Their clock-only and position-only marginals are both uniform. This restricted data loses order, even though the complete states are different and their direction bits are distinguishable.

To retain relational information, define the group-averaged effect `E(c₀,x₀)=Σ_{j=0}^5 W^j P(c₀,x₀) W^(−j)`, where `P(c₀,x₀)` projects onto that dial reading and site, leaving `d` unrestricted. The six terms are orthogonal because their dial values differ. Each effect is a projector commuting with `W`, and at a fixed dial reading the six site effects form a PVM. The verifier checks every such commutation and PVM exactly. With the chosen dial orientation and zero anchor:

| Relative event | `d=+1` | `d=−1` |
|---|---:|---:|
| Site 1 when dial is 1 | 1 | 0 |
| Site 2 when dial is 2 | 1 | 0 |
| Site 2 when dial is 4 | 0 | 1 |
| Site 1 when dial is 5 | 0 | 1 |

In this stipulated cyclic clock convention, the first history associates site 1 with an earlier dial reading than site 2; the second reverses them. The joint projector `E(1,1)E(2,2)` has probability 1 versus 0. Nothing selects the orientation, the dial's origin or an arrow of time from first principles: the comparison uses an explicitly fixed calibration. On a cycle the readings also repeat; these are relative statements within a chosen traversal, not an indefinitely monotonic global time.

The exact finite computation is in [the verifier](verification/halliwell_unordered_and_relational_records_gate.py) and [receipt](verification/halliwell_unordered_and_relational_records_gate.json). General quantum “ever” questions can involve noncommuting effects and incompatible histories; this Boolean construction is valid because the toy's site projectors commute. The physical-to-experiential map is absent, and no claim about subject count or experienced succession follows.

## Implications for the whole

- A timeless whole can coherently be *modeled* with internal relative events; it need not be imagined as acquiring possibilities in an external time. The model presupposes its constraint, tensor factors, calibration and state; it does not explain why they exist or establish that every genuine possibility is actual.
- A list of coarse orbit-wide visit labels is not, by itself, enough to infer a locally oriented sequence. The exact relative effects demonstrate one way to preserve information under this particular constraint; they do not establish that every universe has such effects, durable records or a preferred clock. Different internal clocks and imperfect physical realizations require separate comparisons.
- A simultaneous orbit label is not the same as a memory at a particular local configuration. A memory claiming “event A happened” needs a physical preparation, stable record dynamics, an accessible readout and checks against false positives, erasure and recurrence. For engineered finite resources, see [the autonomous record tape](AUTONOMOUS_RECORD_TAPE.md); it is not derived from this cyclic constraint and is not a solution to gravitational backreaction.
- Records are not subjects. Even if a sequence of relative records is physically available, a proposal must independently justify its subject boundary, phenomenal contents and persistence. Nor does any of this establish a universal experiencer. The project still needs an empirically constrained bridge from local physical organization to plural experience and a treatment of interference between histories.

**Next substantive dependency:** the later Halliwell class-operator treatment has now been [text-read and assessed](TIMELESS_CLASS_OPERATORS_DECOHERENCE_AND_JOINT_EVENTS.md), including its limits on multiple crossings, the constraint, decoherence and physical normalization. Relate a nontrivial invariant ordered-record event to an actual internal detector and accessible memory, rather than equating a formal projector with a working observer. This is a research path, not a closure claim.
