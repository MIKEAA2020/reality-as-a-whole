# Cold-atom entropic time: source audit and connection to our time work

## 1. Source and coverage

Giovanni Barontini, **“Testing the problem of time with cold atoms,” Physical Review Research 8, L022047 (11 June 2026)**, DOI [10.1103/1h9j-df4k](https://doi.org/10.1103/1h9j-df4k).

Inspected:

- complete extracted [main PDF](https://journals.aps.org/prresearch/pdf/10.1103/1h9j-df4k), including equations and references;
- complete [supplement](https://journals.aps.org/prresearch/supplemental/10.1103/1h9j-df4k/Entropic_time_SM.pdf);
- [dataset v1, DOI 10.5281/zenodo.19651064](https://zenodo.org/records/19651064), and its [API metadata](https://zenodo.org/api/records/19651064), which specifies CC BY 4.0;
- the complete text of two released traces, [V0](https://zenodo.org/records/19651064/files/Fig2Fig3V0.dat?download=1) and [V1](https://zenodo.org/records/19651064/files/Fig2Fig3V1.dat?download=1).

The other three experimental traces, the numerical width trace and the large numerical density file have **not** been analyzed here. No raw absorption images, atom-number sequence, macropixel calibration, covariance model or entropy reconstruction code was inspected. This is not a replication of the experiment or its numerical evolution.

Reproducible check: [cold_atom_clock.py](verification/cold_atom_clock.py), [results](verification/cold_atom_clock.json). Its [attributed source subset](verification/sources/barontini_2026_clock_subset.json) is a manual decimal-preserving transcription of the two t/tau columns plus selected tied readouts, **not an original-byte download**. Listed original MD5 values are source metadata, not independently verified file hashes. The script hashes our transcription separately. Figure-like tables synthesized by PDF extraction were not treated as experimental data.

## 2. What the experiment contributes

The reported platform is an approximately isolated 87Rb condensate oscillating in a conservative trap, partitioned by an optical barrier into bright and dark sectors. The bright sector expands and recollapses while exchanging atoms with the dark sector. The main text follows 120 ms of evolution with absorption images at nominal 2 ms sampling, then constructs an internal ordering parameter from measured quantities. It reports broadly laboratory-compatible ordering across cycles and reproduces a measured width trace using an effective equation with an experimentally inferred entropy-dependent coefficient.

This is substantially more physically grounded than another isolated clock toy model. It supplies an experimentally implemented system, a declared operational clock recipe and published processed traces against which clock admissibility can be tested.

It does **not** establish that a stationary Wheeler-DeWitt universe has been realized. A time-independent laboratory Hamiltonian does not imply a stationary quantum state or a gravitational constraint H Psi=0. The paper itself presents an analog testbed, not an experimental solution of canonical quantum gravity.

## 3. What the entropy estimator actually is

The supplement defines macropixel probabilities from the **whole-cloud** density image,

    p_i=N_i/sum_j N_j,
    s=-k_B sum_i p_i log(p_i).

It explicitly calls this the Shannon entropy per particle of the measured single-particle position distribution. The main text uses S=N_bright*s for the bright-sector entropy proxy.

Thus this is not a measured von Neumann entanglement entropy, nor by itself a complete thermodynamic entropy measurement. A globally pure state can have positive position-measurement Shannon entropy. The clock is tied to an explicitly chosen coarse-graining and estimator.

There is an additional locality distinction: s uses both sectors' pixels. The recipe is internal to the full atomic system, but is not established as a clock measurable from bright-sector data alone. “Dark” means unobserved in the reduced model, not absent from the experimental entropy calculation.

For a partition with bright probability b, the Shannon chain rule is

    H(whole)=h_2(b)+b H(bright|bright)+(1-b)H(dark|dark).

Multiplying H(whole) by N_bright is not generally the entropy of the conditional bright distribution. It can vary when the dark distribution changes while the bright distribution and population stay fixed. This identifies a property of the proxy; it does not prove that such a change occurred in these data.

A resolution test is also necessary: uniformly splitting every pixel into m equal subpixels adds k_B log(m) to s. Since N_bright varies, S changes by k_B N_bright log(m), not merely a constant. The induced clock need not change by a single global rescaling. A practical benchmark should quantify this dependence rather than assume every entropy estimator defines the same clock.

## 4. The entropic clock is a path clock

Equation (3), using the article's tau notation, is

    tau[lambda]=(sigma/k_B) integral_lambda (dS/dphi) |dphi|.

Here sigma is an arbitrary time unit and phi is the bright center-of-mass coordinate. On a differentiable branch with phi_dot nonzero,

    tau_dot=(sigma/k_B)*S_dot*sign(phi_dot).

It is nonnegative when S_dot and phi_dot have the same sign. This is a condition to test, not a generic theorem that entropy or its derivative always supplies a global arrow. At a turn, the ratio must be handled branchwise or by a justified limiting/discrete prescription.

The construction can accumulate while entropy decreases during recollapse. It is therefore not simply tau proportional to the instantaneous entropy or to irreversible entropy production. When sign alignment holds it is the accumulated variation of S along the path.

### A direct connection to our turning-clock problem

Take a closed trajectory with S=S_0+a phi, a>0, and phi traversing 0,1,0,-1,0. In units sigma/k_B=1, the state (phi,S) returns exactly to its initial value, but the integral increases by 4a. The script checks a=2, giving increment 8.

Consequently no single-valued instantaneous function T(phi,S) can equal this accumulated clock on that orbit. This does **not** invalidate a history-dependent clock. It identifies the resource: a path/order record or accumulator is needed to distinguish recurrence. The paper supplies an ordered sequence of images for calculating tau; an autonomous internal realization of that accumulator is an additional task.

This is precisely the global issue left open in our [turning-clock atlas](TURNING_CLOCK_ATLAS.md), now with an experimentally motivated candidate for a cumulative reading. Its relation to an actual winding/entropy register should be constructed, not inferred from plotting a path integral.

## 5. A clock-descent test and two released traces

For a retained observable trajectory z(t) and proposed clock tau(t), a single-valued reduced trajectory z_tilde(tau) exists **if and only if**

    tau(t_1)=tau(t_2) implies z(t_1)=z(t_2).

Necessity is immediate; sufficiency defines z_tilde on each clock fiber. Monotonicity alone, if non-strict, is insufficient. A plateau cannot parametrize changing retained observables without an additional branch/record label or an explicit loss of those distinctions.

The released files inspected here are sorted by tau, not by laboratory t. We sorted by t before testing the ordering. Exact decimal-central-value results are:

| Trace | Rows | Adjacent tau decreases in chronological order | Equal-tau adjacent pairs | Largest relative adjacent decrease |
|---|---:|---:|---:|---:|
| V0 | 56 | 3 | 4 | about 0.3004% |
| V1 | 53 | 7 | 4 | about 1.4192% |

These are not statistically established clock reversals. The paper reports approximate 5% relative statistical uncertainty and explicitly acknowledges small wiggles. Our subset contains no per-row uncertainty/covariance model, so no significance claim follows.

There are also exact ties in the released central tau values with distinct central phi and width values. For V0, t=20,22,24 all have tau=50126.9931907532, while phi and width change. For example phi at t=20 is 3.36248841146653e-5 m and at t=24 is 3.46178658404052e-5 m. This motivates a fiber/plateau test **with uncertainty propagation**, not a declaration that the experimental clock is disproved. Estimated ties, interpolation, clipping or finite resolution may matter; their implementation is not reconstructed from these columns.

The column named sigma in these data is the cloud width, **not** a statistical error bar and not the arbitrary time-unit sigma in Eq. (3). The code does not use it as an uncertainty estimate.

These two released traces lack S, s and N_bright. Therefore they cannot independently reproduce Eq. (3) or validate its entropy estimator. They can test ordering, ties and observable-vs-clock consistency at the processed-data level.

## 6. Equation checks required before importing the effective dynamics

These are qualifications of particular printed mathematical claims, not a denial of the measured cold-atom motion.

### 6.1 Time dependence is not nonunitarity

The displayed Eq. (6) has the form

    i*hbar*dpsi/dtau=[Phi(tau)I+Lambda(tau)H_geom]psi.

For real Phi,Lambda and fixed self-adjoint H_geom, its propagator is exactly

    exp[-i integral Phi/hbar] * exp[-i H_geom integral Lambda/hbar],

which is unitary even when dLambda/dtau is nonzero. More generally a suitable time-dependent self-adjoint Hamiltonian preserves norm. Thus the text's assertion that strictly unitary dynamics requires dLambda/dtau=0 does not follow from Eq. (6) alone.

A gain/loss term, a changing population normalization N(tau), or an explicitly reduced open-system map can introduce other behavior. Those must be distinguished from real time dependence of an energy coefficient. The article plots N(tau)|psi|^2, which makes that normalization distinction particularly relevant. Our [coupled clock-rate report](INTERACTING_CLOCK_RATE.md) makes the analogous separation between bare conditional normalization and the derived physical metric.

### 6.2 The printed square-root reduction needs clarification

Taking Eq. (4) literally,

    [-hbar^2/(2M) d_phi^2 + V(phi)]psi=0,
    V=(1/2)M omega^2 phi^2+H_geom.

Freezing coefficients, this implies p_phi^2=-2M V. But the square root displayed in Eq. (5) corresponds to +2M V. A simple constant-coefficient probe with M=1,V=1/2 and first-order momentum magnitude 1 leaves residual 1 in Eq. (4), not zero. This probe tests the printed signs; it is not a reconstruction of the full experiment.

For variable coefficients, an exact first-order equation i*hbar*psi'=h(phi)psi also gives

    p_phi^2 psi=[h(phi)^2+i*hbar*h'(phi)]psi.

A positive-frequency truncation therefore requires a treatment of the derivative/coupled-branch terms as well as the sign. An omitted energy shift, a different convention or further approximation must be specified before importing the printed derivation. This audit has not supplied an author clarification or established a corrected version of their model.

### 6.3 Signature is a real limitation of the analogy

The article acknowledges its positive kinetic form versus the indefinite Wheeler-DeWitt principal form, but says the sign is not invariant under field redefinitions. Under nonsingular real point-coordinate redefinitions the principal quadratic form changes by congruence, and its inertia is invariant (Sylvester's law). Thus an elliptic positive kinetic form does not become Lorentzian/hyperbolic merely through such a redefinition. The cold-atom clock benchmark remains useful without treating the two full constraint structures as equivalent.

## 7. What we should adopt constructively

1. **An experimental benchmark, not another unsupported universal clock claim.** Compare the entropy clock with center-of-mass/branch and record-augmented clocks on the same trials.
2. **An explicit operational clock definition.** Retain its coarse-graining, whole-cloud estimator, trajectory orientation and accumulation record as part of the model.
3. **Clock admissibility tests:** sign alignment, uncertainty-aware ordering, plateau fibers, cycle distinguishability, and behavior where entropy exchange vanishes.
4. **An independently checked dynamical equation:** derive the physical measure and branch approximation, resolve the printed sign/unitarity issues, then compare predictions across clocks with the same anchored events.
5. **Keep entropic and modular time distinct.** A coarse-grained path accumulator is not automatically the state/algebra modular flow. Their equivalence would require an explicit map and matching observable predictions; the article itself leaves a possible limiting connection for future work.
6. **Held-out validation:** an experimentally inferred pump reproducing a trace is valuable but not automatically an independent prediction. Test on withheld cycles, repeats or barrier settings with calibration fixed in advance.

This paper changes the immediate opportunity: the time programme now has a concrete experimental target. Our exact constructions supply consistency and measure tests, but are not thereby experimentally verified. The next data step is the remaining released traces and uncertainty-aware clock comparison; full entropy reconstruction needs the atom-number/entropy or image-level inputs absent from the inspected columns.

## 8. Scope

The strongest supported conclusion is a reported cold-atom laboratory benchmark for an operational relational clock, with a useful but history-dependent entropy-based reading and identifiable mathematical checks still needed. It is not proof that entropy creates time, that clocks stop all physical evolution when their entropy flow stops, or that the gravitational problem of time has been solved.

This remains direct M0/W1-W6 time work. No experimental result here establishes phenomenal passage, a constitutive Gamma/chi law or necessary actuality.
