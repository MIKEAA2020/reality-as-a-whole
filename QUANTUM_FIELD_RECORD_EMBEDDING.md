# Quantum field readout: an explicit but gravity-limited embedding

## Main result

The previous note had a classical field response and a separate qubit instrument. Here a **finite-mode quantum field Hamiltonian** connects them: the same two clock-switched quadratic field couplings transfer a coherent signal into a detector readout, and a quantum two-level sign reference controls the second coupling. The resulting readout probabilities and a complete two-memory instrument can be computed from its symplectic evolution.

For the chosen weak couplings and ordinary Gaussian preparation, however, the output is almost uninformative: with equal priors, reference polarization `r=0.6`, and 10% noise on each memory bit, the optimal success from the two recorded bits is **0.5000262**. The prior qubit example's 0.74 success was an engineered ideal measurement; it was not a prediction for this field coupling.

This is a real **partial embedding**, not a quantization of the complete classical gravity–matter model. The expanding clock-and-rod background is a classical solution; its metric and clock are held fixed during the quantum calculation. The classical scalar sign-reference is replaced by an ideal quantum qubit. Fourier truncation, state preparation, pointer readout and bit noise are specified. The stabilized quartic field interaction is dropped: this defines a quadratic replacement, and no bound shows that its omission is accurate for the stated quantum fluctuations. The gravitational constraints, quantum reference stress-energy, finite clock resolution and nonlinear field self-interaction are not quantized or solved. No claim of a new physical law, novel priority, durable apparatus or problem-of-time solution is made.

The relevant established measurement setting is [Fewster and Verch's quantum-field probe framework](https://arxiv.org/abs/1810.06512), which is formulated on a supplied spacetime, and its [measurement review](https://arxiv.org/abs/2304.13356). The role of finite reference systems and twirling is standard; see [Bartlett, Rudolph and Spekkens](https://arxiv.org/abs/quant-ph/0610030). Our finite-mode calculation is not a claim to reproduce the full local-covariant framework.

## 1. What is quantized and what is not

Use the exact homogeneous expanding reference-field solution of [the previous detector calculation](RELATIONAL_SIGNAL_GEOMETRY_NO_GO.md), with `f=1/2`, `tau=3/2`, clock T, and scale factor a(T). Retain real cosine modes `n=0,...,N` of the three scalar fields `Phi, chi, D`; omit x/y dependence and sine modes. On the coordinate three-torus of volume `V0=(2pi)^3`, use

    e_0=1,   e_n=sqrt(2) cos(nz), n>=1,
    field(x)=V0^(-1/2) sum_n q_n e_n(z),
    [q_n,p_m]=i delta_nm,        hbar=1.

The restricted cosine subspace and hard cutoff are an explicit finite-dimensional *mode regulator*, not a spatially local quantum-field net. The zero modes are ordinary continuous canonical pairs, not finite-dimensional Hilbert spaces.

Introduce a **separate ideal qubit** `R` with `Z_R=±1` and vanishing free Hamiltonian. This is an explicit replacement of the previous classical scalar reference, not a derived two-level truncation of that scalar. Its sign is conserved by the idealized Hamiltonian. In a qubit-Z eigenblock `z_R=±1`, the quadratic Hamiltonian generating evolution in T is

    H_T = sum_(field,n) [p_n²/(2 tau) + a(T)^4 n² q_n²/(2 tau)]
        + a(T)^6/tau [lambda F_1(T) q_Phi^T M q_chi
                       + g z_R F_2(T) q_chi^T q_D].

`F_1`, `F_2` are the smooth tailored pulses defined in the preceding notes; `M` is multiplication by `1+cos z` projected onto the retained orthonormal modes. Its diagonal entries are 1, its 0–1 entries are `1/sqrt(2)`, and its other nearest-neighbour entries are `1/2`. Couplings are zero outside their windows. Each finite-mode Hamiltonian is a real quadratic form and defines a unitary Gaussian evolution for the finite time interval, even if the instantaneous quadratic form is not positive definite.

The diagonal sign transformation flips `Phi,chi` and the reference Z eigenvalue but not D. Thus D is invariant under **that chosen diagonal symmetry**, and the quantum analogue of the previous relative readout is meaningful. As before, invariance under a chosen diagonal subgroup is not invariance under every independently postulated sign symmetry.

## 2. Initial quantum states and exact regulated instrument

Take equal-prior signal hypotheses `s=±1` with initial signal mode `q_Phi,1` displaced by `s A` and its conjugate momentum undisplaced. All other means vanish. For each nonzero mode n, initially use a pure oscillator Gaussian with frequency n on the a=1 slice:

    Var(q_n)=1/(2n),  Var(p_n)=n/2,  Cov(q_n,p_n)=0.

For each zero mode use the normalizable pure Gaussian `Var(q_0)=1`, `Var(p_0)=1/4`, zero covariance. There is no normalizable free-particle ground state for a massless zero mode; this is an explicit state choice. Use the same product Gaussian for signal, detector and readout. Prepare the ideal reference with probabilities `(1±r)/2` in its two Z blocks, and, if no external diagonal sign orientation is available, twirl over the simultaneous sign flip. Twirling does not change the probabilities of the invariant readout below.

Let S(T) be the symplectic propagator in the `Z_R=+1` block, indexed by all initial field canonical coordinates. With `j=D,0` the final readout position,

    mu = A S[j,Phi,1],
    V = sum_k S[j,k]^2 Var(X_k initially).

The `Z_R=-1` block has the opposite mean and the same V by parity covariance. Thus a projective sign readout `b=0` for `q_D,0>=0`, `b=1` otherwise has

    P(b=0 | s) = [1+s r erf(mu/sqrt(2V))]/2.

This is an exact Gaussian result for the declared **regulated quadratic model**, apart from numerical approximation of S. It is not an exact statement about the original interacting quantum-gravity theory.

To retain outcomes, write the sign projectively to two neutral memory qubits with the controlled unitary of [the preceding instrument note](RELATIONAL_CALIBRATION_AND_READOUT.md), now controlled by the actual field spectral projectors `P_0,P_1` for the sign of `q_D,0`. Independently flip each stored bit with probability q. If `J_b` denotes the completely positive map obtained by evolving, projecting onto `P_b`, and tracing out the detector/readout fields, then the full signal-plus-reference instrument is

    I_(m1,m2) = sum_(b=0,1) t(m1|b)t(m2|b) J_b,
    t(m|b)=1-q if m=b, else q.

All four outcomes are included, and their maps sum to a trace-preserving channel. The memory-write gate, memory readiness and subsequent independent noise are still idealized inputs; no local apparatus Hamiltonian or physical stability analysis for them is supplied.

For `0<=q<=1/2`, the total-variation distance of the two two-bit outcome distributions is

    D_bits = r erf(|mu|/sqrt(2V)) (1-2q),
    P_success = (1+D_bits)/2.

The two bits share one underlying field-sign outcome. They are not two independent measurements of the original signal; the `01` and `10` results are ties in the equal-prior decision rule.

## 3. Numerical outcome and controls

Run [verification/quantum_relational_field_instrument.py](verification/quantum_relational_field_instrument.py). The code solves the symplectic ODE for the quadratic Hamiltonian with RK4, computes the Gaussian mean/variance and every recorded outcome probability, and checks preservation of the canonical symplectic form. [The JSON output](verification/quantum_relational_field_instrument.json) records all parameters and controls.

For modes `0–4`, 1,600 steps, `lambda=g=0.01`, `T=0.8`, and `A=1`, it obtains

    S[D0,Phi1] = 0.0001414190,    V = 1.0707436,
    max symplectic defect = 3.1e-14.

With `r=0.6`, `q=0.1`, the full two-bit probabilities are

| signal | 00 | 01 | 10 | 11 |
|---|---:|---:|---:|---:|
| + | 0.41002617 | 0.09 | 0.09 | 0.40997383 |
| - | 0.40997383 | 0.09 | 0.09 | 0.41002617 |

The total-variation distance is `5.234e-5`, and success is `0.50002617`. With an ideal reference and noiseless memories it is still only `0.50005452`: field readout noise, not merely calibration, dominates for this choice. An unpolarized reference or zero second coupling gives no information. Modes `0–3`/800 steps reproduce transfer and variance to better than `4e-12` in this example; this limited comparison is not a rigorous cutoff or continuum convergence theorem.

### Is the signal itself indistinguishable?

No. Before the field interaction, the two coherent signal states have squared overlap `exp(-2 A²)`. With the stated two-level reference and diagonal twirl, the trace distance of the two *signal-plus-reference* states is

    D_initial = r sqrt(1-exp(-2 A²)).

At `A=1`, `r=0.6`, this is `0.557924`, corresponding to an ideal equal-prior Helstrom success of `0.778962` before noisy memory storage. The Helstrom measurement is a mathematical benchmark; no local covariant or gravitational implementation is established. The enormous gap to `0.500026` is a limitation of the **selected coupling and pointer observable**, not evidence that the initial states lack information or that all possible detectors fail.

### Why not simply increase the amplitude?

In the fixed-background formula, reaching 70% success with the same r and q requires `A≈10,119`. On the initial `a=1` slice the added coherent signal-mode energy is `A²/2≈5.12e7`, while the chosen classical clock-plus-rod energy in the coordinate torus is approximately `372`. The bare ratio is about `1.38e5`.

This is a **consistency warning**, not a calculated backreaction error or a no-go theorem: the numbers use a finite-mode bare Hamiltonian and omit the reference, memory and renormalized vacuum stress. They nevertheless show why that large-amplitude extrapolation cannot be promoted to a self-consistent gravitational prediction without solving the constraints and evolving the coupled geometry. The subsequent [energy tradeoff test](FIELD_READOUT_ENERGY_TRADEOFF.md) evaluates squeezing and stronger coupling: the selected design reaches 71.67% under an initial energy proxy, but its later field energy is substantial and full backreaction is not controlled. Thus the large signal-only number is not a general requirement.

## 4. What would close the remaining bridge?

1. Derive a physical quantum reference and local readout from the covariant action, rather than replacing the reference scalar with a QND qubit and postulating memory gates.
2. Quantize or consistently approximate the **joint** constraints, including clock, rods, detector, reference and memory, and control renormalized stress-energy/backreaction; the product Gaussian on a supplied background is not shown to be a physical constraint state.
3. Recover causal localization and control the spatial/UV regulator; the current cosine-only, globally averaged readout is not a local field measurement.
4. Compare complete instrument probabilities at the same relational event in different gravitational slicings, including finite clock/rod resolution.
5. Establish finite-time persistence and physical readout costs rather than identifying a field quadrature with an autonomously maintained memory.

Until those gates are passed, this is a quantitative countercheck against treating an ideal abstract record as automatically realized by a gravitating field. It does not establish quantum refoliation invariance, spacetime emergence, experience, or zero-residue closure.
