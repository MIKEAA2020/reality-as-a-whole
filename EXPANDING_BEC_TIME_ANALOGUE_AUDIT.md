# Expanding BEC as a cosmological and clock analogue: source audit

## Source and scope

S. Eckel, A. Kumar, T. Jacobson, I. B. Spielman and G. K. Campbell, [“A Rapidly Expanding Bose-Einstein Condensate: An Expanding Universe in the Lab,” *Physical Review X* 8, 021021 (2018)](https://doi.org/10.1103/PhysRevX.8.021021). Inspected the journal abstract, article introduction and phonon discussion, and relevant PDF text/figure captions. This note is a source-grounded comparison, not an independent data analysis or a new experimental result. PDF-extracted figure tables are not treated as experimental data.

## What the paper actually reports

The group forced a ring-shaped Bose–Einstein condensate to expand by changing its confining potential. A representative example has initial and final radii 11.3(4) and 46.4(1.4) μm (radius ratio 4.1(3)). The authors compare the experiment to numerical simulations and a linearized mode model.

- **Redshift:** Imprinted long-wavelength azimuthal phonon modes stretch as the ring expands; approximately conserved azimuthal mode number makes this analogous to cosmological wavelength redshift. The paper plots initial/final frequency ratios. Because the azimuthal speed of sound also changes, frequency does not simply scale as 1/R in their apparatus: for the quoted confinement approximation they obtain cθ∝R^(-2/7) and ω_i/ω_f≈(R_f/R_i)^(9/7).
- **Hubble-like attenuation:** The 2018 paper describes *hints* of a term analogous to Hubble friction, with a fitted coefficient 0.55(21); it also discusses differences from the ideal thin-ring model and other possible effects. The damping contains both an independently characterized phenomenological term and the expansion-related term. It should not be described as clean proof of the idealized coefficient.
- **Preheating analogy:** Rapid expansion excites a radial mode, followed by turbulent redistribution and abundant phonon production. Simulations identify soliton and vortex dynamics. The authors state that their imaging could not resolve solitons or similarly sized structures directly. The similarity to cosmological preheating is qualitative and model-dependent.

Later work matters: Eckel and Jacobson, [“Phonon redshift and Hubble friction in an expanding BEC”](https://doi.org/10.21468/SciPostPhys.10.3.064) (2021), develops an effective dimensional-reduction analysis; Banik et al., [Phys. Rev. Lett. 128, 090401 (2022)](https://doi.org/10.1103/PhysRevLett.128.090401), report more precise attenuation/amplification measurements for expansion and contraction, phase-dependent nonadiabatic behavior, and a measured coefficient differing from recent theory. Any proposed new fit must use that subsequent literature rather than assuming the 2018 thin-ring equation is settled.

## Relation to the time programme

The apparent scale factor is an **externally driven trapping configuration**. Phonon dynamics can mimic quantum fields on an effective expanding background, but the apparatus is not governed by an Einstein Hamiltonian constraint, and the experiment uses laboratory time. A dynamical laboratory ring radius is not the FRW gravitational degree of freedom α=log a, and no correspondence to the gravitational physical inner product, internal-clock POVM, generalized modular weight, or β selection has been shown. Redshift or analogue reheating therefore does **not** verify [the FRW scalar-clock calculation](FRW_INTERNAL_POVM.md), the thermal-time hypothesis, a cosmological bounce, or a solution to quantum gravity.

The closest use is as a **testbed for operational clock comparisons**. During a strictly monotonic portion of the driven expansion, a calibrated reading log(R/R₀) can be used as an experimental proxy for an expansion label; it ceases to serve as a one-to-one clock where R stops or recurs. A phonon phase readout might supply a different clock, but its phase is periodic, may be unobservable at nodes, and requires an explicitly implemented phase-unwrapping record or additional observables. Neither proxy is automatically a gauge-invariant internal clock, and neither proves the reduced cosmological operator identity.

This experiment differs from the repository's [2026 cold-atom clock comparison](COLD_ATOM_CLOCK_COMPARISON.md): that work concerns processed data from a separate trapped-condensate experiment and tests an entropy-derived ordering recipe. No claim of shared runs, directly comparable state preparation, or independent replication is made.

## Potential research test, not an accomplished result

A useful concrete follow-up would compare radius-based and phase-based descriptions on the **same matched runs** in an expanding/contracting ring. Before asserting a result:

1. Specify the system, a physically accessible clock instrument and its uncertainty, whether phase and amplitude (or both quadratures) can be reconstructed, and whether records are available in individual runs or only across an ensemble.
2. Use measured R(t), cθ(t), mode phase and amplitude with independently calibrated timing; avoid inferring a supposedly internal clock solely by reusing the externally supplied time ordering.
3. Prespecify an interval of monotonic R, phase-wrap/turning-point handling, and held-out reconstruction of another mode observable. Compare with laboratory time and appropriate control models; include instrumental uncertainties and phase/amplitude-dependent attenuation.
4. Treat recurrent radius values as a clock-ambiguity challenge and test what additional branch or history information actually resolves it. Do not infer physical memory bits or thermodynamic entropy solely from a fitted model.
5. Investigate whether data suitable for this test are accessible, then separately check whether it has already been performed. The 2018 figures and current source review do not establish feasibility or novelty.

A successful analogue experiment could constrain **the operational performance of proposed clock constructions in that apparatus**. Testing a specifically modular-clock prediction would additionally require a reconstructed state or independently validated modular generator and a falsifiable prediction distinguishable from the ordinary driven BEC model. Nothing in the 2018 study supplies that comparison by itself.
