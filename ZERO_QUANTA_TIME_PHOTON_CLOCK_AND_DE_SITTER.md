# Quanta’s time problem: photon clocks, coherence and de Sitter

**Source:** Natalie Wolchover, [“Quantum Gravity’s Time Problem”](https://www.quantamagazine.org/quantum-gravitys-time-problem-20161201/), *Quanta Magazine*, 1 December 2016. I also checked the primary [Moreva et al. photon experiment](https://arxiv.org/html/1310.4691v1), the user's [Page–Wootters original](sources/uploads/page1983.pdf), and sources on holography and de Sitter cited below. Calculations are in [the verifier](verification/zero_quanta_time_photons_horizon_test.py).

## Main result

The article usefully connects three research strands: relational quantum clocks, the two-photon Page–Wootters experiment, and the problem of describing a dynamical spacetime holographically. It is **not** evidence that our universe has been shown to emerge from entanglement, that de Sitter holography is solved, or that experience has been derived from a quantum state.

The strongest connection to our work is operational. In the ideal photon example, the **same globally stationary entangled state** gives different conditional states when its clock photon is read in different orientations. But one set of clock–system coincidence statistics alone cannot establish global coherence: a dephased mixture gives the same statistics in that basis. A separate joint interference test can distinguish them. This is the same distinction made concretely in our [sphere flag and record construction](ZERO_FLAG_RECORD_INCIDENCE_AND_PHYSICAL_READOUT.md): internal records can be definite relative to an interface while a retained joint witness detects coherence.

The article's discussion of “the end of time” also needs care. A future conformal boundary, an observer's cosmological horizon, thermodynamic heat death, and the impossibility of any local event are not the same thing. A short de Sitter calculation below shows why.

## 1. What the 2016 article says—and what its sources support

The article contrasts an external time parameter in ordinary quantum mechanics with dynamical spacetime geometry in general relativity. That is a useful introduction to the problem, though “quantum time is absolute” is too broad as a statement about every quantum theory. The problem has several facets: constraints, observables, clock choice, quantum fluctuations of geometry, and reconciling local relativistic causality with a quantum description. Choosing a clock correlation does not by itself solve all of them.

The article links the Page–Wootters proposal to a two-photon experiment and discusses AdS holography as a route from boundary quantum structure to bulk geometry. It then contrasts AdS with de Sitter and says the corresponding emergence of time in de Sitter was not understood. This was a popular account written in 2016, not a current proof that de Sitter has a complete quantum holographic dual. A modern treatment must distinguish conditional theorems, concrete experiments, and unresolved extrapolations to cosmology.

The article cites [Moreva et al., “Time from quantum entanglement: an experimental illustration”](https://arxiv.org/html/1310.4691v1), arXiv version October 2013, published *Physical Review A* **89**, 052122 (2014). The authors use two polarization-entangled photons, one as a two-outcome clock; in separate configurations they measure clock-conditioned coincidences and global interference/tomography. Their implementation includes birefringent plates, controlled settings, optical paths and laboratory apparatus. They explicitly say their demonstration does **not** discriminate between their mechanism and other approaches to the problem of time.

The experiment is strong evidence that the relevant small quantum-system correlations can be realized and tested. It does not show that the entire universe is a two-photon system, that its total energy is zero, that spacetime or consciousness literally originates in entanglement, or that an observer exists outside the whole. “Internal” and “super-observer” are **measurement roles in a laboratory model**. The experimenter is not literally outside reality.

## 2. The photon clock, calculated

The ideal state used by Moreva et al. is the polarization singlet

`|Ψ⁻⟩ = (|H⟩_C|V⟩_S − |V⟩_C|H⟩_S)/√2`.

In the `H/V` basis, their local Hamiltonians are proportional to `−Y`; for equal polarization rotations, the total `H_C+H_S` annihilates the singlet. Let

`U(θ)=exp(iθY)`, `|c(θ)⟩=U(θ)|H⟩`.

The joint state remains unchanged under `U(θ)⊗U(θ)`, but conditioning on the clock reading produces

`|ψ_S(θ)⟩ = U(θ)|V⟩`, up to normalization and phase.

Thus an ideal measurement gives `P(V_S | c(θ))=cos²θ`: it is 1 for `θ=0` and 0 for `θ=π/2`. The system photon's **unconditioned** reduced state is `I/2` throughout. The verifier checks the state and conditional probabilities; they are ideal quantum predictions, not a re-analysis of the experiment's measured counts or uncertainties. The experiment's ordinary clock mode has two outcomes; its additional delays give a richer set of conditional settings, as described in the paper.

This is prior art, not a new result of our framework. It does, however, give an experimentally realized analogue of the mathematical distinction in [our stationary sphere-echo report](ZERO_PAGE_WOOTTERS_1983_RELATIONAL_SPHERE.md): the whole can be stationary under a specified symmetry while a subsystem has changing **conditional relations**.

## 3. The key distinction: correlation, coherent record, and access

The photon example makes it tempting to identify “conditional time” with “entanglement.” The precise statement depends on the state, clock and observables:

* In a fixed bipartition, a **pure product** global state cannot produce two different nonzero conditional system rays solely by projecting different clock states; those rays are all proportional to the same system vector. A pure-state model with genuinely different conditional rays therefore requires entanglement across that split.
* A **mixed separable** stationary state can still give different conditional system states. For example, `ρ=(|00⟩⟨00|+|11⟩⟨11|)/2` commutes with `Z_C−Z_S`; conditioning on clock `0` or `1` gives system `0` or `1`. This is not the Moreva experiment and does not show that all quantum dynamics is reproducible by classical correlations.

Most importantly, a **single fixed measurement basis** does not certify coherent history. Dephase the ideal singlet in its clock `H/V` basis:

`ρ_diag=(|HV⟩⟨HV|+|VH⟩⟨VH|)/2`.

The ideal singlet and `ρ_diag` have identical `H/V` coincidence probabilities: `HV` and `VH` each have probability `1/2`. In the `X` basis, however, the singlet gives `P(+_C,−_S)=1/2` whereas the dephased mixture gives `1/4`. Equivalently, the joint witness `−X_C X_S` has expectation `1` in the singlet and `0` in the mixture. An observer must have access to the corresponding **joint measurement** to exploit the difference. The authors' super-observer mode is an actual separate interference/erasure configuration, not merely an abstract declaration of global access.

A necessary qualification: `ρ_diag` does **not** commute with the original Moreva noninteracting total Hamiltonian. Therefore this is a comparison of states with the same single-basis statistics, **not** a claim that both are stationary under that Hamiltonian. In our sphere model, by contrast, the reference flag commutes with the stipulated clock shift, so flag pinching and cyclic averaging do commute. The two settings share a measurement-algebra lesson, not identical dynamics.

### What a physical record does

In an idealized model, copying the clock's `Z` value into a fresh memory `M=0` turns the bare witness `−X_C X_S` into the dressed witness `−X_C X_S X_M`. The latter remains sharp `+1`, and applying the inverse copy restores the original pair; tracing out the memory yields the dephased pair. This is a reversible information transfer, not an erasure of the full coherent state.

The copy gate does **not** commute with the original photon Hamiltonian: an implementation must account for the interaction and the memory. One can conjugate the Hamiltonian along with the copied state in the mathematical model, but that is not evidence of a free physical operation. Our existing 24-step sphere extension separately specifies its own reversible flag-record gates and charge assumptions. Neither the ideal memory nor a photon detector is thereby a conscious subject, and neither supplies an interface across a confined realm without an actual interaction.

## 4. The two boundaries in de Sitter are not interchangeable

In ideal flat-slicing de Sitter spacetime, take `a(t)=e^(Ht)` for constant `H>0`. Then

`η(t)=−e^(−Ht)/H`, so `η→0` only as proper cosmological time `t→∞`.

The future conformal boundary is a mathematical asymptotic boundary; reaching `η=0` is not reaching a finite proper-time instant after which a new epoch of “nothing happens” begins. A comoving observer has a future **event horizon** with comoving radius `e^(−Ht)/H` and physical radius `1/H`. The horizon concerns which distant events can ever send signals to that observer; it does not make every nearby pair of events causally disconnected.

For a simple check, the static-patch radial null travel time from `r=0` to `r=1/(2H)` is

`ΔT=atanh(1/2)/H`.

The same finite interval is available at arbitrarily late finite static-patch time in ideal de Sitter geometry. This is a **test-signal calculation**, not a promise that clocks, observers, sources of energy or signals actually persist forever. It suffices to show that the geometry and a horizon alone do not imply “no local events anywhere.” Heat death is a separate conditional thermodynamic claim about available gradients, resources and asymptotic dynamics.

Current acceleration motivates studying approximately de Sitter-like models; it does not establish that our complete universe is exactly de Sitter or that its far-future state is settled. [Anninos’s de Sitter review](https://arxiv.org/abs/1205.3855v3) explicitly distinguishes a confined static-patch observer from an idealized observer with access to future-boundary data. We should preserve that difference rather than move information across a horizon by description alone.

## 5. Holography: a productive connection, not a literal simulation

AdS/CFT provides powerful examples relating a bulk gravitational theory to a boundary quantum theory under a specified dictionary. In suitable semiclassical regimes, holographic entanglement formulas relate boundary-region entropies to bulk extremal-surface areas, with corrections and additional assumptions; see [Rangamani and Takayanagi’s review](https://arxiv.org/abs/1609.01287v2). This is not the claim that any arbitrary set of qubits, entanglement numbers, or a literal computer generates a universe. AdS boundary time and bulk time are related within particular dual models; this is not an established holographic construction of our cosmology.

A useful finite warning comes from the three-qubit states `(|000⟩±|111⟩)/√2`. Every nontrivial reduced density matrix has the same entropy in both, yet their `X⊗X⊗X` expectations are opposite. The states are related by a local unitary, so this example does **not** prove that their putative geometries differ; it simply shows that entanglement entropies alone do not specify all correlations in a fixed operational description. Boundary theory, region structure, state and reconstruction dictionary carry further information. [Jaksland’s analysis](https://arxiv.org/abs/2607.09823v1) separately examines metric, gravitational dynamics and connectivity claims and argues that their emergence bases include more than entanglement alone; this is a philosophical/technical analysis, not a settled no-go theorem.

For our point–sphere analogy, a boundary/bulk correspondence is therefore a possible **mathematical tool** for internal differentiation, not proof that the zero-point literally contains a holographic screen, external computer, or simulator. A valid bridge would have to specify what the boundary and bulk are, how their observables and constraints map, and how any relevant local subject can access records.

## 6. What this contributes to the integrated program

The experimentally illustrated correlation is compatible with the user's proposal that reality has no external time while genuine internal relations occur. Our existing sphere calculation strengthens that general compatibility by exhibiting stationary pre/post-echo observables and a concrete signed-record protocol, rather than merely repeating that “time is relational.” The new photon comparison sharpens the operational distinction among:

1. **clock-conditioned local statistics**;
2. **coherence of the complete state**;
3. **a physically implemented joint interface**; and
4. **a subject's actual experience of succession**.

The first three are mathematically and, in appropriate optical settings, experimentally addressable. The fourth does not follow just from the word “observer.” Likewise the optical zero eigenvalue and the sphere's constructed charge constraints are not objective whole-level energy results, and a correlation witness is not a felt-valence balance.

The constructive demand remains the same: show how the one reality's own constitution selects its differentiations and admissible interfaces, supplies actual intrinsic experience and its signed relation to physical organization, and explains the incidence weights. This article supplies valuable tools and a real laboratory illustration of one link; it does not select that complete constitution or contradict the no-residue aim.
