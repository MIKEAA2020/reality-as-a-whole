# The interacting clock switch: scattering, bound states and a clock obstruction

**Continuation:** [domains, sectors and clock recoverability](ZERO_DOMAIN_SECTOR_CLOCK_RECOVERABILITY.md) distinguishes spectral sectors from observable restrictions and constructs an explicit quantum recovery map for the existing sphere–record state.

## Result

The [autonomous detector model](ZERO_SPHERE_AUTONOMOUS_CONSTRAINED_DETECTOR.md) changed the geometry dynamics, so its free scalar-to-geometry Jacobian could not simply be reused. This continuation derives an interacting spectral description and finds an important obstruction that the free model did not expose:

1. The detector coupling produces **normalizable bound eigenstates outside the free Θ spectral band** in both pointer-`σ_y` channels. Their existence follows analytically for every nonzero coupling of the indicated sign; it is not inferred solely from a finite matrix.
2. The interacting and free absolutely continuous sectors nevertheless have complete wave operators. This gives an exact **asymptotic scattering-clock transformation** on that sector, with an explicit extra outcome for states outside it. It is not an exact transformation to an instantaneous α clock inside the interaction region.
3. No normalized real-valued clock POVM can be covariant under scalar-parameter evolution on the **entire** interacting physical sector: a stationary normalizable eigenstate would induce an impossible translation-invariant probability distribution on the real line. Clocks can still be useful on suitable sectors or intervals.
4. A finite regulated interacting spectral transform reproduces the full pointer probability, including backaction. The transformed pointer connects the two detector-channel spectral bases through their overlap matrix; simply matching equal spectral indices produces a false result, even at the initial reading.

This is progress on both sides of the problem: an explicit interacting asymptotic clock map and a precise reason it cannot be promoted uncritically to a single global clock. It does not establish inhomogeneous refoliation invariance, a preferred foliation, a local material detector, a subjective flow of time, or an objective whole-energy zero. The [standard-library verification](verification/zero_sphere_interacting_clock_spectral_test.py) contains 10 tests; finite discretization checks and continuum proofs are identified separately below.

## 1. The operator and its physical spectrum

Retain the previous normalizable physical Hilbert space

```text
H = L²((-7,−6),dp) ⊗ span{|h=0⟩,|h=1⟩} ⊗ span{|d=+⟩,|d=−⟩},
Θ_(h,d) = p²/6 − 2h − 2λ d E,     Ω_(h,d)=√Θ_(h,d),
C̃ = (p_φ²−Θ)/2,                λ=0.4.
```

The pointer basis labels eigenvalues of `σ_y`. E is the positive Gaussian-smeared α-window effect from the preceding work. On this band `0≤E≤I` and `Θ≥3.2`, so the interacting root is bounded, strictly positive and self-adjoint. The scalar-clock physical dynamics is `U(φ)=exp(+iΩφ)`. Scalar momentum is conserved because the coupling is φ-independent.

For `λ=0`, the spectrum of `Θ_(h,d)` is the interval `[6−2h, 49/6−2h]` and is purely absolutely continuous. Multiplying by `−2h` merely shifts the same geometry operator; the pointer sectors have different perturbations. The free dispersion `p_φ=√(p²/6−2h)` does not diagonalize the interacting operator because `[p²,E]≠0`.

The kernel of E is continuous on the compact band. In fact E is **trace class**, not merely Hilbert–Schmidt: write `E=A†A` with `A=M_(√g) F V`, where V extends the band wavefunction by zero, F is the unitary Fourier transform, and g is the Gaussian-smeared window function. Then

```text
||A||²_HS = (band length)/(2π) × ∫g(α)dα = 1/(2π) × 4 = 2/π,
Tr E = 2/π.
```

Thus `Θ_(h,d)−Θ_(h,0)` is trace class. Weyl's compact-perturbation theorem preserves the **essential** spectral interval; it does not rule out isolated eigenvalues outside it. The numerical trace check alone would not prove this continuum statement; the factorization does.

## 2. Analytic proof of bound eigenstates

The surprise is not a numerical artifact. The kernel

```text
K(p,q)=exp[−(p−q)²/2] sin[2(p−q)]/[π(p−q)]
```

is strictly positive in a sufficiently small square near either band edge. Let `ε∈(0,π/2)` and choose a positive lower bound `k_ε` there; for ε=1/4 one can take `k_ε=K(ε)≈0.59164`.

At the lower edge write `p=−6−u`, `0<u<ε`, `L_h=6−2h`, and

```text
g(u)=p²/6−6=2u+u²/6,       ψ_δ(u)=1/[g(u)+δ].
```

Extend this L² trial function by zero outside the small edge interval. For the attractive pointer channel d=+1, its unnormalized Rayleigh numerator satisfies

```text
⟨ψ_δ,(Θ_(h,+)−L_h)ψ_δ⟩
 ≤ ∫_0^ε du/(g(u)+δ) − 2λ k_ε [∫_0^ε du/(g(u)+δ)]².
```

The first integral grows logarithmically as `δ→0`, while the negative term grows as its square. Hence the numerator is negative for sufficiently small positive δ for **any λ>0**. The variational principle gives spectrum strictly below `L_h`; because the perturbation is compact, there is a normalizable isolated eigenstate below the essential interval. For ε=1/4, δ=`10⁻⁴`, λ=0.4, elementary upper/lower logarithmic bounds already give a negative witness; the test checks that bound.

The same construction at `p=−7+u` applies to the upper gap `g(u)=49/6−p²/6=(14u−u²)/6`. In the d=−1 channel the perturbation is `+2λE`, yielding an eigenstate **above** the upper edge. These are normalizable spectral bound states of the band-projected quantum model. They are not asserted to be astrophysical bound geometries or to have finite variance in α. For the selected square-root physical branch, require additionally the earlier positivity bound; in particular `0<λ<2` suffices for both h levels.

The finite Nyström matrices locate examples of these modes:

| Momentum samples | d=+ eigenvalue below 6, h=0 | d=− eigenvalue above 49/6, h=0 |
|---:|---:|---:|
| 40 | 5.980475 | 8.175590 |
| 80 | 5.977952 | 8.179675 |
| 160 | 5.977198 | 8.181038 |

For `h=1`, subtract 2 from these Θ eigenvalues before taking the positive root. Each finite matrix has one eigenvalue beyond the relevant edge in these runs; the variational argument guarantees at least one in each continuum channel but **does not prove there is exactly one**. Matrix discretization turns the continuum into many discrete levels, so its interior levels must not be presented as continuum bound states.

## 3. A rigorous global-clock obstruction

Let b be any normalized eigenstate of the interacting root Ω. Its physical state evolves only by a phase `e^(iω_b φ)`. Therefore every φ-independent physical effect, including the window effect E, has a φ-independent probability in b. In the N=40 eigensystem the test checks that `⟨E⟩` is positive and unchanged at several readings. This does not say that all states are stationary: it identifies a sector on which an always-advancing geometry reading cannot be assumed.

There is a more general result. Suppose a normalized POVM `T(B)` on all real readings were covariant under `U(φ)=e^(iΩφ)` for **every state in the full physical Hilbert space**. In the eigenstate b, the induced probability measure `μ(B)=⟨b|T(B)|b⟩` would obey `μ(B+t)=μ(B)` for every t. A finite translation-invariant probability measure on R cannot exist: all unit intervals would have the same mass, which must be zero, yet their countable union is R. Contradiction.

Thus no normalized, real-outcome, globally φ-covariant clock POVM exists on this entire sector. This is not a claim that no time, no local clock or no relational observables exist. It does not exclude noncovariant clocks, clocks on restricted/scattering sectors, periodic or finite-interval readings, POVMs with an additional non-clock outcome, or a clock relative to a different generator. The earlier finite-resolution α POVM remains a perfectly valid effect; it was not proved to be globally covariant under this interacting φ evolution. The obstruction concerns this particular model, not a theorem that all forms of time fail in the actual universe.

## 4. Constructive recovery on the scattering sector

The bound states do not destroy the whole clock programme. For each h,d let `Ω₀,h=√(p²/6−2h)` and `Ω_h,d=√Θ_h,d`. Since the squared-root perturbation is trace class and both roots are uniformly positive, the resolvent integral for the square-root difference implies `Ω_h,d−Ω₀,h` is trace class too. The [Kato–Rosenblum theorem](https://arxiv.org/html/1211.6694) then gives complete wave operators

```text
W_±,h,d = s-lim_(t→±∞) exp(+i Ω_h,d t) exp(−i Ω₀,h t),
W†W=I on the free band,       WW†=P_ac(Ω_h,d),
Ω_h,d W = W Ω₀,h.
```

Here `t` is the parameter in a mathematical strong limit, not an extra fundamental clock. The free band has purely absolutely continuous spectrum. These are exact **existence and intertwining statements** on the selected band; they do not explicitly evaluate the wave operators or eliminate possible singular-continuous spectrum in the complement.

Let `J_h` denote the earlier unitary free change from p to `s=√(p²/6−2h)`, including `√|dp/ds|`. For the interacting absolutely continuous subspace,

```text
χ_(h,d)(p)  →  (J_h W_±,h,d† χ_(h,d))(s)
```

is a norm-preserving spectral/scattering representation. It returns the **incoming or outgoing free asymptotic geometry-clock data** with the detector channel retained. For a free asymptotic geometry-reading effect `E_free^α(B)`, the corresponding physical scattering-sector effect is

```text
E_asym^α(B) = W_± E_free^α(B) W_±†,
E_asym^α(⊥) = I − P_ac(Ω).
```

Together the real-reading effects and the extra outcome ⊥ form a normalized POVM on the complete interacting sector. The ⊥ outcome includes bound and any other non-absolutely-continuous parts; it is not automatically an observed detector failure. On the scattering part, the former p-to-s Jacobian is now used **after** removing the interaction through the appropriate wave operator, not applied directly to the interacting p wavefunction. A separate Fourier POVM conjugate to s gives a φ-covariant real-valued reading on the absolutely continuous sector, again with ⊥ on its complement.

This is an interacting **asymptotic** map. It does not establish a finite-α, instantaneous local clock switch through the detector region: the band-projected interaction is nonlocal in α, and a geometry-clock flux and operational instrument there still require construction. The wave operators are analytically known to exist by the stated theorem but are not numerically evaluated in the present tests. The ⊥ sector must not be discarded or silently renormalized if comparing unconditional probabilities.

For the earlier incident packet, the finite N=80 bound-mode weights are approximately `0.001074` in d=+ and `0.000726` in d=−; with the initial equal pointer-channel amplitudes, their average is about `0.000900`. At N=160 the average is about `0.000855`. These are **finite-resolution approximations** to the selected bound overlaps, not a proof that the full scattering weight is exactly their complement; other non-absolutely-continuous spectrum has not been excluded. Their smallness is specific to this packet and does not justify dropping the sector for arbitrary states.

## 5. Transforming the pointer: an explicit finite check

As an independent operational check, diagonalize each interacting N=40 channel:

```text
Θ_(0,d) V_d = V_d diag(θ_(d,j)),
Ω_(h,d) → diag(√(θ_(d,j)−2h)),
S = V_+† V_−.
```

The eigenvector transforms are unitary and the detector `σ_z` is **off-diagonal in d**. Its off-diagonal spectral block is S, not the identity: the two pointer channels have different interacting geometry eigenfunctions. Calculating the coupled pointer probability with this S exactly matches the earlier Chebyshev time evolution at the tested readings:

| φ | Full interacting spectral representation | Direct coupled evolution |
|---:|---:|---:|
| 0 | 0 | 0 |
| 40 | 0.779528 | 0.779528 |
| 80 | 0.958855 | 0.958855 |
| 100 | 0.958898 | 0.958898 |

If one replaces S by the identity without justification, the same numerical convention gives about `0.324` at φ=0 even though the pointer was prepared in `|0_z⟩`. This is a deliberately **incorrect** control, and its numerical value depends on arbitrary eigenvector phases; the physical result does not. The test flips an eigenvector sign to demonstrate that the transported probability is invariant while the naive result changes.

The two N=80 edge-bound eigenvectors have an overlap of only about `0.051`. Thus a pointer operation that exchanges the d channels can carry a state supported on one channel's bound eigenvector mostly into the orthogonal complement of the other channel's particular bound vector. That complement may contain scattering and other sectors. A calculation confined to scattering states must therefore track pointer-induced leakage and postselection; transporting states alone and discarding bound components does not transport the instrument.

The finite spectral transform is a full **unitary change of representation of the regulator**, including its edge modes. A finite matrix has no actual continuous spectrum or mathematical scattering limit; it is not a numerical construction of the continuum wave operators above. The analytical asymptotic result and the numerical pointer-equivalence check are complementary, not identical claims.

## 6. Interpretation and next step

The point–sphere proposal permits a whole with no external time but differentiated internal correlations. The new calculation makes this more precise: the same zero-constrained system has useful asymptotic internal clock descriptions and normalizable states that do not support one globally covariant real-valued clock. The obstruction is not a reason to adopt a fundamental preferred foliation; it calls for patchwise, sector-sensitive relational descriptions and correctly transported observables.

Nor does the mathematical stationary bound mode establish an experienced timeless state or deny experienced passage. The detector remains an idealized pointer; actual subject persistence, incidence and valence are separate bridges. A zero constraint still is not a demonstrated objective energy of the whole, and a putative global signed experiential balance must not erase local suffering. The action, coupling, band, state and encoding have not been derived from zero's own constitution.

The next decisive work is to **construct the finite-interaction-region geometry-clock instrument and compare it with the scalar-clock detector including bound/scattering transitions**, or establish precisely why no adequate local flux exists in the band-projected model. A more physical continuation should remove the artificial momentum band, implement a spatially local detector and record, account for resources, and move to inhomogeneous constraints without imposing a preferred foliation. Separately, competing subject-incidence laws must be tested rather than inferred from the pointer record.

## Reproduce

```sh
python -m unittest verification.zero_sphere_interacting_clock_spectral_test -v
```

The proof of bound-state existence, trace-class scattering, and the no-global-covariant-clock result are analytic. The tests verify finite variational bounds, matrix spectra, numerical unitarity, pointer transport, selected bound overlaps and eigenstate stationarity. They do not prove absence of other continuum spectral components, calculate the continuum wave operators, or certify full quantum gravity.
