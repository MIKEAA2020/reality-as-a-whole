# Scalar-clock FRW and modular flow: a regulated calculation and an obstruction

## Result

Starting from the flat, homogeneous Einstein–massless-scalar constraint, a scalar-field clock yields a familiar deparametrized Hamiltonian proportional to the magnitude of gravitational momentum. On one momentum branch, a **finite, periodically regulated version** admits an exact clock-history state whose gravitational marginal is Gibbs; its modular and relational flows then agree after rescaling. This provides a gravity-derived *starting point*, not an unregulated quantum-gravity result.

More importantly, the natural extension encounters an obstruction: in the unregulated continuum, the Gibbs operator for the reduced Hamiltonian is **not trace-class**. Indeed no faithful normal density state on the full reduced algebra B(H) can have precisely the desired modular flow at a finite positive inverse temperature. The finite construction cannot be promoted to the continuum by simply removing its regulators. This does not rule out suitable KMS states on other observable algebras, or different choices of model or state.

These results do **not** derive a temperature, solve the problem of time, demonstrate singularity resolution, or compare Shlaer dynamically. The classical deparametrization and Gibbs modular identity are known methods; no research novelty is asserted. In particular van Neerven and Portal, [arXiv:2306.13774](https://arxiv.org/abs/2306.13774), already study the positive-momentum massless-particle operator, equivalent up to scaling to this continuum branch, using their generalized modular-time framework. See [FRW_CLOCK_WINDOW_MISMATCH.md](FRW_CLOCK_WINDOW_MISMATCH.md) for the prior-work comparison and a finite-window stress test. Run [verification/frw_modular_clock.py](verification/frw_modular_clock.py) for the finite checks and [its results](verification/frw_modular_clock.json). The continuum obstruction below is an analytic argument, not a numerical extrapolation.

## 1. Classical gravitational origin

Use a unit fiducial comoving cell, 8πG=1, a>0, no cosmological constant or potential, and lapse N. The classical minisuperspace Lagrangian is

    L = -3 a (da/dt)²/N + a³ (dφ/dt)²/(2N).

The momenta are p_a=-6a (da/dt)/N and p_φ=a³ (dφ/dt)/N, giving the constraint

    C_ADM = -p_a²/(12a) + p_φ²/(2a³) = 0.

Set α=log(a) and p_α=a p_a. Multiplication by the positive factor 12a³ gives the equivalent classical constraint for a>0

    C̃ = 6p_φ² − p_α² = 0.

This rescaling changes the lapse parameterization and is not assumed automatically equivalent after quantization. Choose the open classical branch p_α>0, p_φ=-p_α/√6. Then

    p_φ + h = 0,      h = κ p_α,      κ=1/√6.

The scalar is monotonic along each classical solution with p_φ≠0 and positive lapse, since dφ/dt=N p_φ/a³. It can therefore label the evolution on this branch. With φ as the parameter, the reduced Hamiltonian is h: the action reduces to ∫(p_α dα/dφ − h)dφ. In particular dα/dφ=κ. Neither the other sign branches nor p_φ=0 are covered by this choice.

Scalar-clock deparametrization of FRW is established prior work, not derived here for the first time; see e.g. Corichi and Montoya, [arXiv:1105.2804](https://arxiv.org/abs/1105.2804), and the repository's [RECOLLAPSING_GRAVITATIONAL_CLOCK.md](RECOLLAPSING_GRAVITATIONAL_CLOCK.md). The latter studies a different negative-Λ model and should not be identified with the present one.

## 2. Quantization and explicit regulators

For the unregulated line one may represent p_α=-i∂_α on L²(R,dα) and work on its positive-momentum spectral subspace H₊=L²(R₊,dp), excluding p=0. With the factor ordering chosen here, h=κp is self-adjoint on its standard multiplication-operator domain. The branch constraint is (p̂_φ+h)Ψ=0, formally

    i∂_φ Ψ(φ) = h Ψ(φ),     Ψ(φ)=exp(-ihφ)ψ₀.

These are generalized constraint solutions in the noncompact scalar clock; a constant-norm history over the whole real φ line is not a normalizable vector in the kinematical tensor product. A physical inner product and its relation to the quadratic constraint require a specified quantization. The finite example below sidesteps, rather than solves, those issues.

For the finite test, **compactify α to an artificial circle** of length L and retain only N positive Fourier modes p_n=2πn/L, n=1,...,N. Put E_n=κp_n, Δ=2π/L, ω=κΔ, so E_n=nω. This is an IR box and spectral truncation, not the original noncompact FRW geometry. In particular a=e^α is not a single-valued global scale factor on the α circle. The truncation is performed on the chosen rescaled and deparametrized branch; it is not a quantization of all observables or of the original unrescaled ADM constraint.

Use an additional finite, periodic clock: M=N+1 orthonormal readings |j> with

    φ_j = 2πj/(Mω),    j=0,...,M-1.

Define an M×M Fourier matrix F_jk=exp(iω k φ_j)/√M for k=0,-1,...,-N, and

    P_C = F diag(ωk) F†,   H=diag(E_1,...,E_N),
    K = P_C⊗I + I⊗H,      Q = P_C²⊗I − I⊗H².

Here Q is a finite analogue of C̃ on this branch, not the full Wheeler–DeWitt operator. The clock is periodic and finite; its readings do not constitute a globally monotonic real scalar field. Fourier aliasing and the asymmetric selected clock spectrum are part of this regulator.

For any normalized ψ₀∈C^N, define the isometric history map

    Jψ₀ = (1/√M) Σ_j |j>⊗exp(-iHφ_j)ψ₀.

Each system mode n is paired with clock Fourier mode k=-n. Consequently KJ=0 and QJ=0 exactly. The state Jψ₀ is normalized and stationary under exp(-iuK); its conditioned state at reading j is U(φ_j)|ψ₀><ψ₀|U(φ_j)†, with U(φ)=exp(-iHφ). This construction does not claim the finite clock itself is a normalizable monotonic continuum clock.

## 3. Derived correspondence, conditional on preparation

Choose a positive β and prepare

    ψ₀ = Σ_(n=1)^N sqrt(p_n)|n>,
    p_n = exp(-βE_n)/Z_N,   Z_N=Σ_(n=1)^N exp(-βE_n).

The finite Fourier average kills off-diagonal terms because 0<|n−m|<M. Thus tracing out the clock gives the actual gravitational marginal

    τ = Tr_C |Jψ₀><Jψ₀| = exp(-βH)/Z_N.

This is a selected preparation. Neither the gravitational constraint nor the scalar clock forces β or the Gibbs weights. Using σ_s^τ(A)=τ^(is)Aτ^(-is) and α_φ(A)=U(φ)†AU(φ), the identity is

    σ_s^τ(A) = α_(-βs)(A),
    Tr(ρ_j A) = <ψ₀|σ^τ_(-φ_j/β)(A)|ψ₀>.

So relational and modular predictions agree at the discrete clock readings, while the operator-group identity holds for every real φ on the finite system algebra. For any reduced observable A, a constraint-compatible representative of the reading-j expectation is

    O_j(A) = J α_(φ_j)(A) J†.

Because KJ=0 and QJ=0, it commutes with both finite constraints; its expectation in Jψ₀ equals the conditioned expectation. This representative acts on the chosen physical subspace and is extended by zero outside it. It does not solve the full gravitational observable problem.

Change the positive weights to q=(0.4,0.3,0.2,0.1). The same history then has faithful marginal diag(q), but consecutive log-probability gaps are unequal whereas the energy gaps are equal. Hence there is no single β making this marginal Gibbs for H and no such all-observable modular/relational identification. The test exhibits a mismatch after calibrating the first transition. Thus even this regulated gravitational example does **not** make agreement automatic.

## 4. Why the continuum step is nontrivial

On H₊=L²(R₊,dp), h acts by multiplication by κp. For any finite β>0 the putative Gibbs operator acts by multiplication by f(p)=exp(-βκp). It is not compact: choose an infinite sequence of normalized functions supported on disjoint subintervals of (0,1). They are orthonormal and ||fψ_n||≥exp(-βκ). A compact operator sends an orthonormal sequence to zero in norm; therefore f(h) is not compact and, a fortiori, not trace-class. There is no finite normalization Tr exp(-βh).

In fact there is no nonzero normal stationary density operator for this multiplicity-one continuous-spectrum h. A trace-class density is Hilbert–Schmidt and has an L² kernel K(p,q). Invariance under exp(-iht) for every t implies (p−q)K(p,q)=0 almost everywhere; the diagonal has two-dimensional measure zero, so K=0. This reinforces why an invariant normal system marginal cannot be obtained directly in this representation.

The obstruction is also stronger for the full algebra B(H₊): suppose a faithful normal density operator ρ had σ_s^ρ(A)=α_(-βs)(A) for every A and s. The two strongly continuous unitary implementers must differ only by a scalar character, since the commutant of B(H₊) consists of scalars. Uniqueness of the self-adjoint generators then implies logρ = -βh + cI, hence ρ=e^c exp(-βh), contradicting trace-classness. Domain considerations are covered by the self-adjoint generator identity; the positive constant e^c cannot repair noncompactness. This rules out precisely a faithful **normal density state on this full algebra** with that flow, not non-normal states or states on other algebras.

The box illustrates the obstruction but does not prove it: for the positive momentum tower with the cutoff removed at fixed L,

    Z_∞(L) = Σ_(n≥1) exp[-βκ(2π/L)n]
           = 1/(exp(βκ 2π/L)−1) ~ L/(2πβκ).

The partition function diverges as L→∞. At fixed finite N the limit is instead N; simply taking L→∞ while retaining N is not a continuum limit. Independently, a uniform clock marginal over all real φ is not a normalizable probability density. Treating generalized solutions or choosing a finite clock wavepacket requires its own physical inner product and a fresh calculation; finite-window conditioning need not give an exact Gibbs marginal.

## 5. What would genuinely advance this result

1. Specify a physically justified observable algebra and state for the unregulated scalar-clock sector; establish existence and faithfulness and calculate the modular flow without assuming the desired answer. If using a local, reduced or non-normal KMS construction, state precisely how it avoids the B(H₊) obstruction.
2. Analyze normalizable clock wavepackets and controlled limits, including what replaces the finite uniform-clock marginal.
3. Extend beyond the homogeneous sector and this ordering, and compare clock choices and singular regimes without inferring a bounce from a rescaling.
4. For Shlaer, derive the relevant homogeneous constraints and compare observables and reduced dynamics explicitly; neither monotonicity nor the present scalar clock establishes his Λ–χ model as a limit.

See also [RELATIONAL_MODULAR_CLOCK.md](RELATIONAL_MODULAR_CLOCK.md) and [TIME_SOLUTION_EVIDENCE_AUDIT.md](TIME_SOLUTION_EVIDENCE_AUDIT.md).
