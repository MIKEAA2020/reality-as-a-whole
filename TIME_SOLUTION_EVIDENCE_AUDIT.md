# Problem of time: evidence and novelty audit

## Bottom line

The repository contains a **candidate synthesis**, not a definitive solution to the problem of time. The term covers several distinct difficulties in quantum gravity; demonstrating a relational clock in a model does not by itself solve them all in a full theory. The earlier claims of complete structural closure, a proven UV completion, and a demonstrated reduction to Shlaer's model are retracted. This audit supersedes conflicting claims in the time-related closure and comparison documents and their verifier outputs.

## What has and has not been shown

- **Relational time:** Page–Wootters and other relational-clock constructions are established prior approaches. A conditional evolution in a model demonstrates a way to address frozen dynamics under its assumptions; it does not establish a globally valid clock or resolve the multiple-choice problem in general quantum gravity.
- **Modular flow:** Tomita–Takesaki theory supplies modular automorphisms for suitable algebra/state pairs. Connes' cocycle theorem relates modular flows for faithful normal states modulo inner automorphisms. Identifying that outer class with unique physical time, treating inner differences as physically irrelevant, and recovering measurable clocks require further physical arguments. The cocycle theorem itself does not provide them.
- **Temperature:** The Bisognano–Wichmann result identifies vacuum wedge modular flow with Lorentz boosts under its assumptions; the 2π normalization does not prove that every causal diamond, arbitrary state, or curved-spacetime system has the same physical temperature or geometric flow. In `verification/kms_beta_two_pi.py`, defining a boost-like operator as H/(2π) does not establish that H is the physical Lorentz-boost generator.
- **Type III₁:** A finite-dimensional oscillator calculation cannot prove an infinite-dimensional local algebra is type III₁. In particular, a single finite oscillator algebra is type I, not type IIIλ. Modular-spectrum illustrations do not establish the Connes S-invariant of the proposed physical algebra. See `verification/takesaki_dual_typeIII1.py` for the model being used; its stronger classification claims are not established by its finite calculations.
- **Bounce and arrow:** A bounce in an effective or truncated model is not proof of singularity resolution in full quantum gravity. A time-symmetric bounce alone does not derive a low-entropy condition or two thermodynamic arrows.
- **UV completion:** A spectral action, heat-kernel expansion, and polymer model do not by themselves demonstrate an interacting, unitary, UV-complete quantum gravity theory. No such demonstration is supplied here.
- **Shlaer:** `verification/shlaer_time_comparison.py` assumes several key claims as Boolean values. Its numerical example checks monotonicity of a chosen FRW volume function; it assumes rather than derives the modular/proper-time identification. Two monotonic functions being reparameterizable does not prove equality of flows, dynamical equivalence, or that one theory is an IR limit of another. Compatibility is an open question, not a demonstrated result. The asserted sign flip of Shlaer's clock momentum across a bounce is also not established by that example.
- **Conscious experience:** A proposed relationship with global workspace theory is a philosophical and empirical hypothesis, not a solution of the quantum-gravitational problem of time or a derivation of consciousness.

`verification/problem_of_time_closed.py` aggregates return codes from other scripts and labels them as resolved facets; it does not independently prove the labels' physical conclusions. Successful exit codes show that the encoded checks passed, not that the interpretations or all assumptions are correct.

## Novelty

Thermal time (Connes and Rovelli), modular theory, Bisognano–Wichmann, Page–Wootters relational clocks, and quantum-cosmological bounce models all predate this repository. Combining these ideas is a possible synthetic contribution, but neither a genuinely new theorem nor the originality of the precise combination has been established. Establishing novelty requires a targeted literature review and a precise claim, with assumptions and a derivation that does not merely restate earlier results.

## Subsequent bounded progress

[RELATIONAL_MODULAR_CLOCK.md](RELATIONAL_MODULAR_CLOCK.md) derives an exact relational/modular correspondence in a finite constrained model with a Gibbs system marginal, and gives a non-Gibbs counterexample. [FRW_MODULAR_CLOCK.md](FRW_MODULAR_CLOCK.md) extends the construction to a regulated scalar-clock FRW branch and proves an obstruction to the corresponding normal Gibbs state on the full unregulated reduced algebra. Neither resolves the general gravitational or Shlaer questions below.

## Steps toward a stronger claim

1. Specify a concrete gravitational model, algebra, state, clock observables, and constraint dynamics.
2. Prove within that model which modular flow is physically implemented and how relational observables evolve, including domains and the role of inner automorphisms.
3. Derive, rather than assume, a comparison with Shlaer: map the variables, constraints and observables, and show when their dynamics agree and when they do not.
4. Prove the algebraic classification and any bounce/UV claims in their actual infinite-dimensional or full-theory setting; distinguish model evidence from the theorem.
5. Compare the resulting precise proposition with published work and seek independent expert review.
