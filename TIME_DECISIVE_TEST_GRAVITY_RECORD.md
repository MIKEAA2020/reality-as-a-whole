# Problem of time: a decisive test on a gravitating clock, and the remaining gap

**Verdict:** this does **not** solve the general problem of time. It applies established quantum-information complementarity to an existing, explicitly constrained gravitational clock model in this repository and obtains a quantitative, finite-wavepacket benchmark. It answers one narrow question: how much information can the outgoing clock retain about two distinct gravitational spectral alternatives, and how does discarding it affect a specified interference experiment? This is not a discovery of complementarity, a prediction for our universe, or a proof that the model is the correct quantum-gravity theory. Literature novelty of this particular application has not been established.

**Target:** a self-contained physical account of internal change, records and emergent spacetime without an external clock for the timeless whole. Conscious experience and the metaphysical actuality of that whole remain separate explanatory obligations, not consequences of any operator identity here. No assumption that a particular clock must be globally valid is made.

## 1. Select the best existing bridge, not a new toy by default

The repository already contains a nontrivial benchmark: [GRAVITATING_PROPER_TIME_CLOCK.md](GRAVITATING_PROPER_TIME_CLOCK.md). It augments a flat FLRW Einstein–massless-scalar model with negative cosmological constant and a **specified homogeneous, smeared comoving oscillator**. Its energy enters the gravitational constraint. In a declared ordering, the two oscillator-energy channels scatter off different Morse potentials. The source describes the physical continuum, the frequency sector, and why negative auxiliary bound modes are excluded by its real-momentum constraint. The source's action and spectral construction are premises of the present calculation; their full derivations have not been independently re-audited here.

That construction does not provide localized hardware, a covariant matter theory in full inhomogeneous GR, a finite-duration measurement engine, boundary preparation and phase-reference dynamics, singularity resolution or a full quantum-gravity solution. A related [dust extension](DUST_CLOCK_RECORD.md) makes different additional assumptions; it does not eliminate these issues.

The new calculation below uses the *same* backreacting scattering amplitudes, not the earlier ideal counter or an external clock attached afterward. Its preparation, phase calibration and measurement are assumed boundary operations. The scalar is a relational clock in a selected sector, not time for the absolute.

## 2. Prior art and why this calculation is narrower

- [Höhn and Vanrietvelde](https://arxiv.org/abs/1810.04153) provide clock-neutral quantum reductions and changes between internal clocks; these changes need not be globally valid. [Höhn, Smith and Lock](https://arxiv.org/abs/2007.00580) develop the frequency-sector/covariant-POVM trinity in relevant relativistic settings. The calculation below is not a replacement for those results or a new general clock-switching theorem.
- The information–interference tradeoff is established quantum mechanics: Englert, *Fringe visibility and which-way information: an inequality*, Phys. Rev. Lett. 77, 2154 (1996), [DOI](https://doi.org/10.1103/PhysRevLett.77.2154). [Zych et al.](https://doi.org/10.1038/ncomms1498) already apply clock/path complementarity to gravitational proper-time interferometry. The relevant general fidelity/trace-distance bound is due to [Fuchs and van de Graaf](https://arxiv.org/abs/quant-ph/9712042). Our calculation is a model-specific application, not a new universal information–gravity law.
- [Ashtekar's LQC overview](https://arxiv.org/abs/0812.0177) already discusses scalar clocks and recollapse; [Gielen and Menéndez-Pidal](https://arxiv.org/abs/2109.02660) illustrate how clock choices, unitarity and boundary conditions can affect quantum cosmology. A single minisuperspace sector cannot settle their general multiple-choice concerns.
- [Barontini's cold-atom experiment](https://doi.org/10.1103/1h9j-df4k) is a separately significant realized internal-clock construction. It does not measure this cosmological phase or validate this model; laboratory ordering and whole-cloud entropy estimation matter. See [the experiment audit](COLD_ATOM_ENTROPIC_CLOCK_AUDIT.md).
- The [clue assessment](CLUES_CROSS_PROJECT_ASSESSMENT.md) records why monitored-circuit record statistics, bounded transduction, categorical instruments, modular flow, arithmetic and theology are useful leads with **different types and assumptions**. In particular, record entropy alone is not clock accuracy, a circuit schedule already supplies order, and an opfibration obstruction is not a universal no-clock theorem. Combining incompatible domains by analogy would not be progress.

This is a targeted collision check, not an exhaustive literature review. No novelty or experimental priority is asserted.

## 3. Define one operational experiment

Use the parent model's two-level sector with `mu=1` and oscillator gap `Omega=0.6`. Its two oscillator levels have Morse parameters `kappa_0=0.2`, `kappa_1=0.6`. For `k>0` let the source's exact continuum reflection phases be

    S_n(k) = Gamma(2ik)/Gamma(-2ik)
             * Gamma(1/2-kappa_n-ik)/Gamma(1/2-kappa_n+ik)
             * (2mu)^(-2ik),       |S_n(k)|=1.

The incoming and outgoing channel labels and their phase reference must follow the same convention. The incoming geometry-plus-oscillator product is defined in the **incoming channel representation**, not asserted to be a product of finite-volume geometries and detector states. Prepare the oscillator in `|+>=(|0>+|1>)/sqrt(2)`.

The system label to be inferred is **which of two bands of the conserved scalar spectral parameter `k`** was prepared. It is not automatically a time-of-arrival label or an experienced duration. Choose

    k_A(u)=0.3+0.2u,       k_B(u)=7.9+0.2u,       0<=u<=1,

and uniform normalized wavepackets of equal weight on these disjoint intervals. The common `u` identifies corresponding offsets within the two bands; that matching is part of this interference protocol and is not a unique physical factorization. The two discrete alternatives have equal prior probability. To discuss interference, prepare their **coherent** equal superposition; to evaluate guessing, prepare each band separately with equal prior. These are different but related preparations.

Remove the common channel-0 phase by the known geometry unitary `S_0(k)^*` as a reference calibration. This is a specified spectral operation, not shown to be a freely available device. Define

    z_j(u)=S_1(k_j(u)) S_0(k_j(u))*,
    |r_j(u)>=(|0>+z_j(u)|1>)/sqrt(2),
    |chi_j>=integral_0^1 du |u> |r_j(u)>.

The integral is a direct-integral state with unit norm, not an integral of orthogonal normalized vectors in a finite-dimensional space. In the calibrated outgoing representation the superposed state is

    (|A> |chi_A> + |B> |chi_B>)/sqrt(2),

where the two bands are identified with `C²_path tensor L²([0,1]_u)` using the declared equal-width map. This decomposition is restricted to these two intervals; the orthogonal complement is retained in the full physical Hilbert space. The clock plus the unresolved `u` are **not** assumed independent after scattering.

## 4. Exact information and coherence formulas

Set

    zbar_j=integral_0^1 z_j(u) du,
    c=integral_0^1 z_A(u)* z_B(u) du.

When `u` is not read, the two oscillator states are

    rho_j=(1/2) [[1,zbar_j*],[zbar_j,1]].

Their trace distance and the optimal equal-prior clock-only guessing probability are

    D = (1/2)||rho_A-rho_B||_1 = |zbar_A-zbar_B|/2,
    P_guess^opt=(1+D)/2.

This optimum allows **any** oscillator POVM and an assumed suitable phase reference; it is not the success probability of every readout. For the parent's fixed `|+>,|->` Ramsey readout the obtainable distinguishability and success probability are

    D_X=|Re(zbar_A-zbar_B)|/2,   P_guess^X=(1+D_X)/2.

For the coherent superposition, trace out the oscillator and `u`. The off-diagonal path entry is `<chi_B|chi_A>/2`, and the visibility of an ideal path-phase recombination measurement is

    V=|<chi_B|chi_A>|=|1+c|/2.

Thus the general trace-distance/fidelity inequality yields

    D² + V² <= 1.

Indeed the full `chi_j` are purifications of `rho_j`, so their overlap is bounded above by the fidelity, and trace distance obeys the standard fidelity bound. Equality need not hold for finite-width packets because the unresolved `u` contains additional correlations. Nothing here assumes the Ramsey-X measurement attains the optimal POVM. The inequality applies to this specified physical preparation and factorization; it does not say that information obtained by all possible quantum clocks must obey this same numerical expression without their own operational definitions.

**Important:** visibility loss is relative to the specified phase-corrected path recombination after discarding the oscillator and `u`. The full state remains pure under the joint scattering. Coherence can be redistributed into correlations, and an appropriate joint operation or quantum eraser can change the observed visibility. This is not fundamental irreversible loss, a thermodynamic arrow, or a solution of the measurement problem.

## 5. Numerical example and verification

For the declared two 0.2-wide bands and `Omega=0.6`, composite Simpson quadrature gives approximately:

| Quantity | Value |
|---|---:|
| Clock-only distinguishability `D` | 0.446428 |
| Optimal clock-only correct-guess probability | 0.723214 |
| Fixed Ramsey-X distinguishability `D_X` | 0.437140 |
| Fixed Ramsey-X correct-guess probability | 0.718570 |
| Calibrated path visibility `V` | 0.887823 |
| `D²+V²` | 0.987528 |

These are conditional model numbers, not observed cosmological probabilities. The optimum is computed with knowledge of the declared two alternatives and prior; it is not an unbiased estimate of general clock accuracy. The path interferometer, calibration, coherent preparation and oscillator measurement remain supplied operations.

[verification/gravity_clock_complementarity.py](verification/gravity_clock_complementarity.py) and [its JSON output](verification/gravity_clock_complementarity.json) compute nine combinations of spectral bandwidth and oscillator gap and verify the bound and readout ordering. Composite Simpson results at 512 and 1024 subdivisions agree within `5e-9` for the three reported discrimination/visibility quantities. Two runs produced identical JSON. Separately, the phase formula as implemented in the existing parent code was compared at 42 parameter points with 50-digit `mpmath` complex gamma evaluation; the maximum absolute discrepancy was `9.2e-14` in that test. The prior [parent verifier](verification/gravitating_clock_probe.py) also passed. These checks are numerical consistency tests, **not** rigorous quadrature error bounds or a proof of the parent continuum model.

## 6. Connection to time and decisive open tests

The oscillator's relative phase can probe a proper-time response in a controlled regime: the parent document relates its energy derivative to a classical proper lifetime at large action. At finite gap the phase compares **backreacted oscillator-energy branches**, so the divided phase is an average response, not automatically the duration of one unperturbed geometry. In this calculation the estimated quantity is a spectral-band label. To make the result a proper operational test of time, define a finite-range, calibrated, unwrapped duration target and show that readout distinguishes it with quantified errors; a periodic two-level phase alone cannot do that globally. Retain the required preparation and phase reference.

A decisive solution—not merely this benchmark—would have to establish at least:

1. **Full gravitational physical theory:** a nonperturbative or controlled quantum theory with well-defined domains, physical states, and anomaly-free local Hamiltonian/diffeomorphism constraints, or a genuinely consistent alternative that recovers their empirical content. The one homogeneous constraint here has no nontrivial refoliation algebra to test.
2. **Physical events and interventions:** clock/record instruments derived from the actual coupled theory, with preparation, backreaction, failures and finite accuracy. Boundary operations in this example are not so derived. Same physical events and conditioning must be transported, not merely the same-looking matrices.
3. **Multiple clocks and global limits:** a comparison on overlapping clock domains, including turning points, inequivalent quantizations, boundary conditions and loss of information under coarse graining. A common neutral construction can be powerful but cannot simply be presumed for all quantizations.
4. **Spacetime and empirical limit:** controlled recovery of semiclassical locality, causal structure, proper-time comparisons and general relativity; a distinguishing prediction or independent consistency result where feasible. No idealized spectral probe alone establishes this.
5. **Phenomenal and ultimate interfaces:** why internal records correspond to experienced succession and how the proposed timeless absolute is actual and experiential. Physics alone does not establish either; neither is needed to *define* the specific operational benchmark above.

These are programme-level tests, not a proof that only this approach can succeed. Different valid approaches might use different fundamental objects and need no universal clock. The construction above meets a limited part of item 2 under its explicit assumptions; the wider gates remain open. Claiming a decisive solution now would repeat the project's earlier unsupported closure claims, retracted in [TIME_SOLUTION_EVIDENCE_AUDIT.md](TIME_SOLUTION_EVIDENCE_AUDIT.md).
