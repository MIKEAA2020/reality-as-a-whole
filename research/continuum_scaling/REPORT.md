# Constructive step 14: a controlled lattice-to-Dirac bridge

## Result and scope

An explicit scaled quantum walk converges to free Dirac evolution in one space dimension on every fixed bounded momentum band, at fixed physical time. An analytic operator-norm bound specifies the error.

The convergence is **not uniform over the whole lattice spectrum**. Near the momentum-zone boundary, a nonvanishing discrepancy survives and changes a spin observable. This is checked rather than hidden by testing only favorable low-frequency modes.

**32 new tests pass; all 372 tests across fourteen research folders pass.**

### A declared change of model

This is **not** a claimed continuum limit of the fixed CNOT circuit in the previous rounds. That rule did not approach identity under clock relabeling. Here a new gate family is introduced with an explicitly scaled coin angle.

There is also a different state space:

\[
\mathcal H_a=\ell^2(\mathbb Z)\otimes\mathbb C^2.
\]

It describes one walker's position and two-component internal state, not one independently occupied qubit at every site. On N sites its one-particle dimension is 2N, not 2ᴺ. Connecting it to a many-body local observable net requires further construction.

This is an existence example of a precise discrete/continuous bridge, not the uniquely selected dynamics of reality. No new empirical measurements were collected.

## 1. Fix the physical scaling

Set lattice spacing and time step both equal to a, with c=ℏ=1. The ratio of spatial and temporal scales is a declared convention of the model, not a derived numerical value of a fundamental speed.

At each step:

1. rotate the two-component internal state by

\[
C_a=\exp(-ima\sigma_x);
\]

2. shift the first component one site right and the second one site left.

The coin angle ma tends to zero as a tends to zero. Keeping an arbitrary fixed angle would be a different scaling problem.

## 2. Match real-space and momentum descriptions

With Fourier convention exp(−ikaj), the conditional shift is

\[
S_a(k)=\operatorname{diag}(e^{-ika},e^{ika})
=\exp(-ika\sigma_z).
\]

The step operator is

\[
W_a(k)=S_a(k)C_a.
\]

The real-space implementation and this Fourier symbol agree. The code checks their predictions and norm preservation, including a finite-grid Parseval check for a finitely supported state without aliasing on that grid.

The continuum comparison is not obtained merely by drawing a smooth line through site labels. It needs an identification of state spaces, given below.

## 3. Identify the candidate continuum generator

For fixed finite k and m:

\[
W_a(k)=1-ia(k\sigma_z+m\sigma_x)+O(a^2).
\]

Thus the candidate limiting generator is

\[
H(k)=k\sigma_z+m\sigma_x.
\]

Its exact evolution is

\[
D_T(k)=\cos(ET)1-i\frac{\sin(ET)}{E}H(k),
\qquad E=\sqrt{k^2+m^2},
\]

with the continuous E=0 case interpreted as identity.

A first-order expansion alone is not enough to control many steps. The next bound supplies that control.

## 4. Prove a one-step error bound

Let A=kσ_z and B=mσ_x. For Hermitian finite matrices, variation of constants and unitary norm preservation give

\[
\|e^{-iaA}e^{-iaB}-e^{-ia(A+B)}\|
\le\frac{a^2}{2}\|[A,B]\|.
\]

The commutator estimate follows by writing the change of a conjugated B as an integral involving [A,B]; its norm is at most s||[A,B]|| at intermediate time s. Integrating from 0 to a yields the stated a²/2 factor.

Since

\[
\|[k\sigma_z,m\sigma_x]\|=2|km|,
\]

we obtain

\[
\boxed{\|W_a(k)-D_a(k)\|\le a^2|km|.}
\]

This is an analytic bound, not a fit to the numerical examples.

## 5. Control the accumulated finite-time error

For unitaries W and D, telescoping their n-fold products gives

\[
\|W^n-D^n\|\le n\|W-D\|.
\]

At T=na:

\[
\boxed{\|W_a(k)^n-D_T(k)\|
\le Ta|km|.}
\]

On a fixed band |k|≤K:

\[
\boxed{\sup_{|k|\le K}\|W_a(k)^n-D_T(k)\|
\le TaK|m|\longrightarrow0.}
\]

This is a genuine uniform estimate **on the declared band**. The cutoff must remain fixed as a tends to zero.

For a physical time not exactly on the lattice grid, taking n=floor(T/a) adds a continuum time-mismatch error bounded by a√(K²+m²). The same restricted convergence follows.

## 6. Specify the state-space embedding

Use the unitary lattice Fourier transform

\[
(F_a\psi)(k)=\sqrt{\frac{a}{2\pi}}
\sum_j\psi_j e^{-ikaj},
\qquad k\in[-\pi/a,\pi/a).
\]

Extend this momentum function by zero outside the Brillouin zone and apply the ordinary continuum inverse Fourier transform. This defines an isometric embedding into continuum L² spinors.

Conversely, a continuum spinor with Fourier support in [−K,K] can be compared with the lattice description once K<π/a.

The modewise uniform estimate then lifts directly to the wavepacket norm:

\[
\|W_a^n f-D_Tf\|_{L^2}
\le TaK|m|\|f\|_{L^2}
\]

under this identification and support condition.

This is a state-space comparison, not a claim that two different Hilbert-space descriptions are literally the same numerical occurrence.

## 7. Keep localization qualifications visible

The Fourier embedding is a bandlimited interpolation. A sharply localized lattice vector maps to a sinc-type continuum function with tails, not a compactly supported continuum point state.

Therefore exact lattice support statements cannot simply be transferred into compact continuum support statements through this embedding.

There are two separate locality results:

- the lattice walk has exact finite site propagation;
- the limiting Dirac PDE has its own domain-of-dependence property.

Their relationship requires the stated embedding and convergence regime. It is not established by equating a lattice site with an exact continuum point.

## 8. Recover the continuum equation

Replacing momentum by −i∂_x yields

\[
i\partial_t\psi
=(-i\sigma_z\partial_x+m\sigma_x)\psi.
\]

Choose

\[
\gamma^0=\sigma_x,
\qquad\gamma^1=-i\sigma_y.
\]

They satisfy the 1+1-dimensional Clifford relations for signature (+,−). The equation becomes

\[
(i\gamma^\mu\partial_\mu-m)\psi=0.
\]

Also:

\[
H(k)^2=(k^2+m^2)1,
\]

giving the positive and negative energy branches ±√(k²+m²).

The tests check these matrix identities and the mass-shell relation. This is a free two-component equation, not a quantized field theory, a vacuum construction, or a derivation of particles and antiparticles from an actual many-body substrate.

## 9. Check Lorentz-compatible structure without attributing it to the lattice

For a boost of rapidity η, use

\[
S(\eta)=\exp(-\eta\sigma_z/2).
\]

Its similarity action gives

\[
S^{-1}\gamma^0S
=\cosh\eta\,\gamma^0-\sinh\eta\,\gamma^1,
\]

\[
S^{-1}\gamma^1S
=-\sinh\eta\,\gamma^0+\cosh\eta\,\gamma^1.
\]

These are the corresponding spinor covariance relations. The boosted energy and momentum preserve E²−k²=m².

The limiting equation therefore has the expected relativistic form. The finite lattice itself does not have exact continuous boost symmetry. The spinor boost matrix also need not be unitary in the fixed-slice Euclidean spinor norm; its role is covariance, not an ordinary internal unitary rotation.

No gravitational dynamics, preferred-lattice elimination at all scales, or physical choice of spatial dimension has been derived.

## 10. State what locality the limiting equation supplies

For suitable solutions, define density and current:

\[
\rho=\psi^\dagger\psi,
\qquad j=\psi^\dagger\sigma_z\psi.
\]

The Dirac equation gives

\[
\partial_t\rho+\partial_xj=0,
\qquad |j|\le\rho.
\]

The characteristic velocities are ±1. The usual local energy/domain-of-dependence argument yields finite propagation for appropriate compactly supported initial data of the continuum PDE.

Separately, a lattice state initially supported at site 0 remains within |j|≤n after n steps, hence |x|≤T under x=aj and T=na.

The tests check the discrete support and the algebraic current bound. They do not simulate a proof for every continuum solution or bypass the embedding caveat in step 7.

## 11. Recover the relativistic dispersion only in its regime

The exact lattice eigenphases obey

\[
\cos\omega_a(k)=\cos(ka)\cos(ma).
\]

On the low-momentum branch:

\[
\frac{\omega_a(k)}a\longrightarrow\sqrt{k^2+m^2}.
\]

The code uses a stable atan2 expression for the principal phase rather than a cancellation-prone acos near zero. The chosen numerical examples show second-order convergence of this quasienergy and first-order convergence of the finite-time propagator.

The two orders concern different quantities. They should not be confused or generalized to all states and momenta from a short numerical sequence.

## 12. Exhibit the failure of global spectral convergence

Take T=1, a=1/n, m=1, and a zone-edge representative k_a=π/a. The two lattice zone edges represent the same periodic momentum point; the corresponding one-sided limit can equally be taken from inside the zone.

At the edge:

\[
W_a(k_a)=-e^{-ia\sigma_x},
\]

and hence

\[
W_a(k_a)^n=(-1)^n e^{-i\sigma_x}.
\]

The continuum comparison at this growing momentum approaches (−1)ⁿ1. The difference therefore tends to

\[
\|e^{-i\sigma_x}-1\|=2|\sin(1/2)|\approx0.95885,
\]

not zero.

The tests also show a persistent discrepancy at interior momenta k_a=π/a−0.1. This is not only an isolated endpoint artifact. Continuity supplies neighborhoods with nonzero error, so the low-band theorem cannot be promoted to an all-spectrum operator-norm theorem.

For a spinor initially in a σ_z eigenstate, the walk's final σ_z expectation is cos(2), while the high-momentum Dirac comparison approaches +1. Thus the discrepancy is not merely an unobservable overall phase.

These are mode calculations and analytic consequences, not an empirical experiment with an exact plane wave.

## 13. Numerical examples of the bound's regime

For k=1.2, m=0.7, T=1:

| n | a=1/n | Propagator error |
|---:|---:|---:|
| 20 | 0.05 | approximately 0.02975 |
| 40 | 0.025 | approximately 0.01487 |
| 80 | 0.0125 | approximately 0.007434 |
| 160 | 0.00625 | approximately 0.003717 |

The errors decrease consistently with the analytic first-order bound.

At the zone edge for m=T=1, the same refinements instead produce errors approaching 0.95885. Testing both regimes exposes the scope rather than manufacturing a global convergence claim from favorable points.

## 14. Explain what had to change

The previous fixed CNOT automorphism made a finite norm change on some local observables regardless of a clock label. This family instead scales the coin angle and, for fixed physical momentum, the shift phase with a.

It also introduces:

- a one-particle position/internal-state structure;
- a mass parameter;
- a spatial/time scaling relation;
- a Fourier embedding;
- and a restricted convergence topology and momentum regime.

Those choices do explanatory work and remain assumptions. The Dirac equation is recovered **from them**, not derived from complete intelligibility alone or shown to be the unavoidable limit of every local quantum system.

Opposite finite coin/shift ordering differs at nonzero a but has the same bounded-momentum limiting generator and a corresponding error bound. This is one explicit example of different microscopic descriptions sharing a controlled effective equation; it is not a theorem of phenomenal equivalence.

## 15. What the larger integration has gained

We now have an explicit example of a bridge that the integrated-account architecture previously only requested:

\[
\text{scaled local discrete dynamics}
\longrightarrow
\text{controlled continuum spinor equation}.
\]

The bridge includes a map between state descriptions, a quantitative estimate, causal qualifications, a relativistic limiting structure, and a failure regime.

It does not yet establish:

- a continuum limit of the prior CNOT algebra;
- a quantized Dirac field or a local observable field net;
- an arbitrary causal-set continuum limit;
- twistor or Langlands correspondences for this model;
- a cosmological state or physical constants;
- actual occurrence or phenomenal identity.

The original Born probability interpretation is used, not derived. No observer measure or unity criterion follows from the limiting equation.

## 16. The next necessary bridge

To connect this one-particle result to local algebraic field structure, the next task is a **many-body/CAR lift**:

1. specify fermionic mode generators and their canonical anticommutation relations;
2. lift the one-particle unitary to the corresponding algebraic transformation;
3. verify locality with the correct grading—odd fermionic fields anticommute on disjoint supports, while appropriate even observables commute;
4. state the state/vacuum assumptions rather than deriving them from notation;
5. determine which form of continuum convergence is justified for the field and observable algebra, not only its one-particle propagator.

This could connect the scaling bridge to the observable-net programme. It would not automatically produce the full Standard Model, gravity, or a constitutive account of consciousness.

## Reproducibility and verification scope

- `model.py`: walk symbol, real-space propagation, Fourier samples, Dirac propagator, error bounds, quasienergies, and boost matrices.
- `test_model.py`: 32 tests.
- `enumeration.json`: generated convergence and failure-regime data.
- `results.log`: actual run output.

Unlike the preceding symbolic-Pauli implementation, these checks use floating-point trigonometric functions and declared tolerances. The exact analytic inequalities and limiting arguments are supplied in this report; finite parameter grids do not prove them by themselves.

```bash
# This round
cd research/continuum_scaling
python -m unittest -v test_model.py

# All research folders, from repository root
python research/run_checks.py
```

**Observed verification:** 32 new tests pass; all 372 tests across fourteen research folders pass. No new empirical data were collected, and no claim of a novel general quantum-walk theorem is made.

### Consolidated verdict

A controlled lattice/continuum connection is now explicit rather than metaphorical. It succeeds on its stated state-space identification and fixed momentum bands, and it fails outside that regime in an observable way. This is a real conditional integration step—not a continuum limit of the earlier CNOT rule, a complete field theory, or the completed account of actuality and experience.

## Continuation: CAR lift

[Step 15](../fermionic_lift/REPORT.md) adds fermionic kinematics explicitly and lifts the walk to exterior-power Fock dynamics. Its cutoff-tail argument strengthens the fixed-band result to convergence for each fixed L² smearing and hence point-norm convergence on a specified common CAR algebra. This does not remove the changing-high-momentum obstruction or select a vacuum.
