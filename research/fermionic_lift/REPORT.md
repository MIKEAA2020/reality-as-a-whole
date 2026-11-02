# Constructive step 15: from the scaled walk to a CAR field algebra

## Result and scope

The [scaled one-particle walk](../continuum_scaling/REPORT.md) admits a fermionic many-body lift once canonical anticommutation relations (CAR) are **imposed as additional kinematics**. Its finite ring realization preserves number, parity, and products, with graded locality rather than ordinary commutation for odd fields.

More substantially, the fixed-band continuum estimate extends by a cutoff-tail argument to every fixed square-integrable smearing. On a specified common continuum CAR algebra this gives **point-norm convergence of the dynamics**: each fixed bounded CAR observable converges in norm at fixed time. It does not give uniform convergence over its unit ball, convergence of every lattice regional algebra to a continuum regional algebra, or selection of a physical vacuum.

These are standard mathematical constructions and elementary consequences of the previous bound, not a newly verified fundamental theory. Thirty-two finite numerical tests accompany the analytic arguments below. They are not substitutes for those arguments.

## 1. Added kinematics and conventions

For a complex one-particle Hilbert space H, take CAR(H) with antilinear annihilation fields a(f):

\[
\{a(f),a(g)\}=0,\qquad
\{a(f),a(g)^*\}=\langle f,g\rangle I,
\]

where the inner product is conjugate-linear in its first slot. For finite H = C^d, represent this on fermionic Fock space

\[
\mathcal F_-(H)=\bigoplus_{r=0}^{d}\wedge^r H.
\]

The mode count d is not a subject count. At N two-component sites d = 2N and the Fock dimension is 2^(2N), unlike the previous one-particle dimension 2N and unlike the earlier CNOT spin-chain construction.

In the occupation basis, c_i removes an occupied mode with sign (-1) to the number of occupied lower-index modes. This is a Jordan–Wigner representation of CAR, not an identification of fermionic regional locality with qubit tensor locality. CAR statistics are not derived from the walk or from the existence of a two-component spinor.

## 2. Exterior powers give a genuine many-body automorphism

For unitary U on H, let

\[
\Gamma(U)=\bigoplus_r\wedge^r U.
\]

Matrix elements between equally occupied basis states S and R are det U[R,S]; the vacuum component is one. Exterior powers imply Γ(UV) = Γ(U)Γ(V), unitarity, and number/parity conservation. With Heisenberg pullback α_U(A) = Γ(U)* A Γ(U), our convention is

\[
\alpha_U(c_i)=\sum_j U_{ij}c_j,\qquad
\alpha_U(a(f))=a(U^*f).
\]

Thus products and adjoints are preserved. This is not a reduced channel or a compression. Successive Heisenberg pullbacks compose in reverse Schrödinger order.

The finite model uses a **periodic ring**, coin first, component 0 shifting right and component 1 left. Its Fourier symbol is exactly W_a(k) = exp(-ikaZ) exp(-imaX) at the ring momenta. Wraparound is explicit. The infinite-line continuum argument below instead uses the Fourier embedding from step 14; finite ring tests are not an infinite-volume proof.

## 3. Locality: graded fields and commuting even observables

Disjoint one-particle site subspaces give anticommuting odd fields: both their annihilator anticommutator and mixed anticommutator vanish. They generally do **not** commute. Even polynomials on disjoint subspaces commute, since exchanging their factors produces an even number of CAR signs. Norm closure preserves this commutation.

One walk step pulls a mode back to the two components at a neighboring site. After n steps its support lies within ring distance n. On the infinite line the same finite-range rule has the ordinary distance bound n. Consequently even observables outside the corresponding cone commute with the evolved even observable. The parity-fixed subnet is a local observable candidate; treating it as the physical observable algebra includes the usual parity/superselection choice, not a deduction of actual observability from matrix identities.

In the continuum let D_t = exp(-itH), H = -iZ∂x + mX. The finite-propagation result of step 14 implies graded field locality and even-observable locality: if the supports of g and D_t* f are disjoint, the mixed CAR anticommutator vanishes. In particular, spatial regions separated beyond |t| have this property. This is free 1+1-dimensional Dirac dynamics, not a demonstration of interacting relativistic QFT or a full spacetime net with all desired axioms.

## 4. Exact field norm transfers one-particle errors

CAR gives the exact C*-norm identity

\[
\|a(f)\|=\|f\|_H.
\]

For completeness, CAR gives a(f)^2 = 0, n_f = a(f)*a(f), and n_f^2 = ||f||² n_f. Positivity and a(f)a(f)* + n_f = ||f||² I give the upper bound. In Fock representation a(f) applied to a(f)*Ω/||f|| attains ||f|| for f ≠ 0, proving the matching lower bound and hence the universal CAR norm. This norm is the standard CAR C*-norm, not a Frobenius matrix norm.

For unitaries U,V, therefore,

\[
\|\alpha_U(a(f))-\alpha_V(a(f))\|
=\|(U^*-V^*)f\|.
\]

If the one-particle error on a common invariant band is at most δ, the error for one smeared field is at most δ||f||. A telescoping product expansion gives, for a degree-r monomial of annihilation or creation fields with band-supported smearings f_j,

\[
\|\alpha_U(A)-\alpha_V(A)\|
\le r\delta\prod_{j=1}^r\|f_j\|.
\]

Finite sums obey the sum of the monomial bounds with absolute coefficients. In particular the error for a(f)*a(f) is at most 2δ||f||². These estimates need no assertion of a many-body operator-norm bound on Γ(U)-Γ(V), which would scale with particle sector and is not the statement being used.

## 5. A stronger continuum bridge: fixed smearings, then all fixed CAR observables

Work on the **common** continuum one-particle space H = L²(R, C²), in Fourier representation. The lattice Fourier embedding E_a identifies its one-particle space with H restricted to the Brillouin interval B_a = [-π/a, π/a). Let P_a project onto that band. For T = na, define the technical unitary extension

\[
\widetilde U_a=E_a W_a^n E_a^*+(I-P_a).
\]

The identity on the discarded tail is a comparison convention, **not a proposed physical ultraviolet law**. Any unitary acting within that complementary subspace gives the same fixed-vector limit below. D_T and the embedded walk preserve every momentum band inside B_a.

Choose fixed K < π/a, put f_K = 1_{[-K,K]}f, and use the step-14 estimate δ = TaK|m|. The same estimate holds for adjoints on this band. Unitarity bounds the remaining tail by twice its norm:

\[
\|(\widetilde U_a^*-D_T^*)f\|
\le TaK|m|\,\|f_K\|+2\|f-f_K\|.
\]

For any fixed f in H, first take a → 0 through T/a integer with K fixed, then take K → infinity. The first term vanishes and the second tends to zero by L² cutoff approximation. Thus the adjoints converge strongly for **every fixed square-integrable smearing**, not just exactly bandlimited ones. The unstarred version follows by the same argument. Rounding times adds the step-14 vanishing fixed-band correction; no uniform high-energy time estimate is needed.

By the exact field norm identity, the corresponding CAR automorphisms satisfy norm convergence on each generator. Products follow by telescoping and finite sums by addition. Finally finite field polynomials are norm dense in CAR(H). Given any fixed A and polynomial P,

\[
\|\alpha_a(A)-\alpha_D(A)\|
\le 2\|A-P\|+\|\alpha_a(P)-\alpha_D(P)\|.
\]

Isometry of both automorphisms makes the first term uniformly controllable; the second vanishes. Hence **α_a(A) → α_D(A) in norm for every fixed A in CAR(H)**. This is a common-algebra point-norm limit, with the comparison extension explicitly specified. The continuum free CAR dynamics is also point-norm continuous in time by strong continuity of D_t, the same field norm identity, and density.

### Why the high-momentum obstruction remains

The step-14 zone-edge witness uses k proportional to 1/a. It changes as a changes and is not a single fixed L² smearing. Narrow normalized wavepackets near those momenta retain the discrepancy by continuity of the matrix symbols. Their annihilation fields witness failure of uniform convergence over the CAR unit ball. Point-norm convergence and failure of uniform convergence are compatible.

Nor does this argument identify lattice-local and continuum-local subalgebras exactly: E_a maps a site vector to a sinc-like function with tails. Fixed compactly supported continuum smearings are allowed in the limit argument, but exact finite-spacing regional support does not follow. Unsmeared point fields are distributions, not elements a(f) for f in L², so this theorem does not assert point-field norm convergence.

## 6. State and vacuum obligations remain separate

The empty Fock vacuum is fixed by number-preserving Γ(U), but it is not thereby the relativistic positive-energy vacuum. The limiting Dirac one-particle Hamiltonian has positive and negative branches. Empty occupation does not minimize its naive second-quantized energy.

Already on the finite ring, the empty state, fully occupied state, and maximally mixed state are all invariant, but a mode has expected occupancy 0, 1, and 1/2 respectively. Dynamics and CAR alone do not select among them. A relativistic field interpretation requires additional state/spectral conditions, charge and antiparticle interpretation, and a chosen polarization (typically involving the negative-energy subspace). Infinite-volume representations and implementability relative to that polarization require separate treatment; the existence of the abstract CAR automorphism does not settle them. No claim is made that an appropriate free vacuum cannot be selected once such conditions are imposed.

A common fixed state can evaluate the converging bounded observables. Convergence of a lattice-dependent family of states, its correlations, energy renormalization, or its GNS representations is an additional problem, not supplied by point-norm convergence of dynamics.

## 7. Reproducibility and integration ledger

Run `python -m unittest -v test_model.py` in this directory, or `python research/run_checks.py` from the repository root. The 32 checks cover CAR signs, antilinearity, smeared CAR, the norm witness/projector identity, exterior-power sectors/composition/unitarity, Heisenberg convention, grading and locality, ring cones and Fourier correspondence, invariant-state nonuniqueness, cutoff estimates, and input guards. Sparse operator `error` is a Frobenius norm, used only as an upper bound on operator error. The sampled cutoff checks are finite-vector analogues, not numerical proofs about L² integrals. `enumeration.json` records representative diagnostics.

**Earned:** a declared fermionic many-body algebra; a finite walk lift; graded/even locality; a common-algebra point-norm continuum dynamics; explicit separation of dynamics and state selection.

**Not earned:** derivation of statistics, the physical vacuum or full interacting QFT, a continuum limit of the old CNOT rule, empirical selection of the walk, causal-set/twistor/Langlands unification, phenomenal constitution, or ultimate explanation. Mathematical realization types still do not identify actual occurrence tokens or observers.

**Next substantive obligation:** specify a quasifree state/polarization and test whether its correlations, energy interpretation, and continuum convergence support the claimed free-field vacuum, without mistaking this extra state choice for a consequence of the walk alone.

## Continuation: a specified quasifree ground state

[Step 16](../quasifree_vacuum/REPORT.md) supplies the declared negative-energy polarization and proves convergence of its fixed bounded correlations. Positive particle/hole excitation energy is constructed explicitly. The principal quasienergy branch and state criterion are extra choices; the divergent absolute sea energy is not assigned a finite physical value.
