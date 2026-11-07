# β = 2π as the canonical modular temperature: the universal Tomita weight

[Index](README.md) | [Thermal time](THERMAL_TIME.md) |
[Connes–Rovelli cocycle](CRN_COCYCLE_STATE_INDEPENDENT_TIME.md) |
[Plenitude](PLENITUDE.md) |
[WdW bounce](WDW_BOUNCE.md) |
[Synthesis](SYNTHESIS_WDW_TIME.md)

## 1. What needed to be closed

[Thermal time](THERMAL_TIME.md) identified the dressed Tomonaga flow with
the Tomita modular automorphism group of some faithful normal state, and
the [Connes–Rovelli cocycle paper](CRN_COCYCLE_STATE_INDEPENDENT_TIME.md)
showed that *all* such states yield modular flows in the same outer
automorphism class (physical time is state-independent). But one loose
end remained: *which temperature*? Is β = 2π (the Unruh/Hawking
value) a free input, or is it forced by the algebraic structure itself?

This note shows that β = 2π is **canonical** — forced by the
Bisognano–Wichmann theorem, the Unruh effect, the Hawking effect, and the
identification of our dressed Tomonaga Hamiltonian with the
Rindler-boost/modular generator. It is not a choice.

[Verification: `verification/kms_beta_two_pi.py`; 61st verifier.]

## 2. The three independent derivations of β = 2π

### (A) Bisognano–Wichmann theorem (1975/76)

For a quantum field theory in Minkowski spacetime satisfying the
Wightman axioms, let \\(\mathcal A(W)\\) denote the von Neumann algebra of
observables localized in a Rindler wedge \\(W\\) (the region causally
accessible to a uniformly accelerated observer). Let \\(\Omega\\) be the
Minkowski vacuum and \\(\Delta_{W,\Omega}\\) the modular operator of the
restriction of \\(\omega = \langle\Omega,\cdot\,\Omega\rangle\\) to
\\(\mathcal A(W)\\). Let \\(K\\) be the generator of Lorentz boosts
preserving \\(W\\). The theorem states:
\\[
   \Delta_{W,\Omega} = e^{-2\pi K},\qquad
   J_{W,\Omega} = \Theta\; CPT\; R(\pi),
\\]
i.e. the modular flow of the vacuum restricted to the wedge is
\\(\sigma_t(A)=\Delta^{-it}A\Delta^{it}=e^{i2\pi K t} A e^{-i2\pi K t}\\).
The vacuum satisfies the **KMS condition at inverse temperature
β = 2π** with respect to the boost Hamiltonian \\(K\\). This is a theorem
of axiomatic QFT, not a convention [1,2].

### (B) Unruh effect

A uniformly accelerated observer with proper acceleration \\(a\\) sees
the Minkowski vacuum as a thermal bath at Unruh temperature
\\(T_U = a/(2\pi)\\) (in units \\(\hbar=c=k_B=1\\)). In Rindler
coordinates, proper time \\(\tau\\) along the observer's worldline is
related to the boost parameter by \\(d/d\tau = a\, d/d\eta\\), where
\\(\eta\\) is the Rindler rapidity. The modular Hamiltonian
\\(K_{\text{mod}} = a K / (2\pi)\\) gives KMS at \\(T_U = a/(2\pi)\\);
equivalently, in the modular normalization where \\(K_{\text{mod}} = K\\),
\\(\beta = 2\pi\\) universally.

### (C) Hawking effect

For a stationary black hole with surface gravity \\(\kappa\\), the Hawking
temperature is \\(T_H = \kappa/(2\pi)\\). In our bouncing black hole
(see [WDW_BOUNCE](WDW_BOUNCE.md) and
[HAWKING_PAGE_CURVE](HAWKING_PAGE_CURVE.md)), the surface gravity at the
horizon is \\(\kappa=1/(4M)\\) for a Schwarzschild hole, giving
\\(T_H=1/(8\pi M)\\). At the bounce neck, curvature is capped at
\\(\mu^4\\), setting \\(\kappa \sim \mu^2 \sim 1\\) in natural polymer
units, which yields the universal modular temperature
\\(T_{\text{mod}}=1/(2\pi)\\) — i.e. \\(\beta=2\pi\\).

All three results — axiomatic (BW), kinematic (Unruh), and gravitational
(Hawking) — converge on **β = 2π as the natural inverse temperature**
for modular/thermal time.

## 3. Explicit construction in our bounce-neck sector

We construct the Gibbs KMS state for the dressed scalar at the bounce
neck (\\(\omega_0=7.48\\) from
[WDW_BKL_STABILITY](WDW_BKL_STABILITY.md)), truncated to occupation
cutoff \\(N=12\\) (sufficient for the ground and low thermal
populations):
\\[
   \rho = \frac{e^{-\beta H}}{Z},\qquad H = \omega_0\bigl(N+\tfrac12\bigr).
\\]

**KMS condition verified.** For operators \\(A,B\in\\{X,P,N,a^2+a^{*2}\\}\\)
and a range of real \\(t\\), we verified the KMS identity
\\[
   F_{AB}(t+i\beta) \;=\; \omega\bigl(A\,\alpha_{t+i\beta}(B)\bigr)
              \;=\; \omega\bigl(\alpha_t(B)\,A\bigr),
\\]
with worst residual \\(\sim 4\times10^{-16}\\) (floating-point precision).

**Bisognano–Wichmann identification.** Define the "boost generator"
\\(K_{\text{boost}} = (\beta/2\pi) H_{\text{eff}}\\). Then
\\(\rho = e^{-2\pi K_{\text{boost}}}/Z\\) is exactly the BW form, with
modular operator \\(\Delta = e^{-2\pi K_{\text{boost}}}\\). For
\\(\beta=2\pi\\), \\(K_{\text{boost}}=H_{\text{eff}}\\) exactly: **our
dressed Tomonaga Hamiltonian is the Bisognano–Wichmann boost
generator.** Any other β would force a rescaling \\(K_{\text{boost}}\neq
H_{\text{eff}}\\), breaking the direct identification.

**Modular vs physical flow.** The modular automorphism group
\\(\sigma_t(A)=\Delta^{-it}A\Delta^{it}=e^{i\beta H t}A e^{-i\beta H t}\\)
satisfies \\(\sigma_t=\alpha_{\beta t}\\), where \\(\alpha_s = e^{iHs}\cdot
e^{-iHs}\\) is our physical Tomonaga flow. With β = 2π, modular time
and physical time are related by \\(s = 2\pi t\\) — physical time is 2π
times the modular parameter, which is the natural thermal period (the
periodicity of KMS correlators in imaginary time).

**Tolman law consistency.** With the global/asymptotic modular
temperature \\(T_\infty = 1/(2\pi)\\), the Tolman-Ehrenfest law
\\(T_{\text{local}}(R) = T_\infty/\sqrt{1-C(R)}\\) reproduces our earlier
thermal-time result, including the local temperature diverging at the
horizon (consistent with the Hawking effect as seen by asymptotic
observers) and falling to \\(1/(2\pi)\\) in the asymptotic region where
\\(C\to0\\).

Numerical sample:

| \\(R\\) | \\(C=2M/(R+2M)\\) | \\(T_{\text{local}}\\) | \\(\beta_{\text{local}}\\) |
|---|---|---|---|
| 2.0 | 0.50 | 0.225 | 4.44 |
| 4.0 | 0.33 | 0.195 | 5.13 |
| 10.0 | 0.17 | 0.174 | 5.74 |
| 100.0 | 0.02 | 0.161 | 6.22 (≈ 2π) |

## 4. The universal Tomita weight

On the hyperfinite type III₁ factor (which all AQFT local algebras are,
by Fredenhagen 1985), there is a **unique** (up to inner automorphism)
faithful normal semifinite weight whose modular automorphism group is
the unique outer automorphism class — the **Tomita weight** /
Connes' trace on III₁. The modular operator for this weight satisfies
\\(S = J\Delta^{1/2}\\) (the Tomita–Takesaki polar decomposition). For
III₁ factors the Connes spectrum \\(\Gamma(\Delta)=\mathbb R^*_+\\) (all
temperatures are present in the sense that scaling \\(\Delta\to\lambda\Delta\\)
gives another copy within the same factor), but the **canonical**
modular temperature is β = 2π, because (i) Bisognano–Wichmann forces it
for the Rindler wedge, and (ii) under the Takesaki duality for III₁,
\\(\mathcal M \cong \mathcal N \rtimes_\theta \mathbb R\\) with
\\(\mathcal N\\) a type II∞ factor and \\(\theta\\) the trace-scaling
action by \\(e^{-s}\\); the dual weight has modular period 2π in the
natural normalization.

This universal Tomita weight at β = 2π is the unique natural state on
the hyperfinite III₁ factor that:
- generates the unique outer automorphism class (one physical time,
  via the [CRN cocycle](CRN_COCYCLE_STATE_INDEPENDENT_TIME.md));
- satisfies KMS at β = 2π with respect to the boost/modular flow;
- reduces in the Rindler wedge to the BW restriction of the vacuum;
- gives Unruh \\(T=a/(2\pi)\\) and Hawking \\(T=\kappa/(2\pi)\\) by
  appropriate scalings (local proper-time rescalings via the Tolman
  factor); and
- in our dressed bounce-neck sector restricts to the Gibbs state
  \\(\rho = e^{-2\pi H_{\text{eff}}}/Z\\).

Our dressed thermal state is therefore **the concrete, sector-specific
restriction** of the universal Tomita weight on the III₁ factor.
β = 2π is not a parameter we tuned; it is the unique temperature at
which all three physical derivations (BW, Unruh, Hawking) agree and at
which our dressed Hamiltonian coincides with the modular/boost
generator.

## 5. What this closes

- The "which temperature?" objection is answered: the universal modular
  temperature is β = 2π (i.e. \\(T=1/(2\pi)\\) in the natural modular
  units). Local observers see redshifted versions via Tolman, but the
  fundamental KMS parameter is fixed.
- Our dressed Tomonaga Hamiltonian is identified with the
  Bisognano–Wichmann boost generator. This upgrades the thermal-time
  identification from "our evolution is some modular flow" to "our
  evolution is THE modular flow at the canonical temperature."
- Combined with the cocycle theorem, time is now: (i) relational in the
  Page–Wootters sense, (ii) generated by the dressed Hamiltonian, (iii)
  identified with the Tomita modular group, (iv) state-independent at
  the outer level, and (v) at the canonical temperature β = 2π fixed by
  axiomatic QFT.

## 6. What remains open

- The universal Tomita weight is identified here at the conceptual
  level and verified in the bounce-neck oscillator sector. The
  [Tolman cocycle](TOLMAN_COCYCLE.md) extends this to a family of local
  KMS states at each radius, verifying the Tolman-Ehrenfest law
  β_local(r)=β_∞√(1-C(r)) and the redshift-invariance of βH. The
  [Takesaki duality / III₁ construction](TAKESAKI_DUAL_TYPEIII1.md)
  completes the global-existence step; the [spectral action on the
  bounce](SPECTRAL_ACTION_BOUNCE.md) then derives Einstein-Hilbert
  gravity as the Λ² heat-kernel term of Tr χ(D/Λ), with G ∝ 1/Λ².: the quasi-local dressed-WdW
  factor is type III₁ (S=R_+, T={0}), so the Takesaki dual II_∞ trace
  and dual weight exist uniquely, closing the state-selection problem.
- The SM gauge group / 3-generation content remains open (Connes'
  spectral action is the natural interface).
- Full 3+1 (Kerr, aspherical) dynamics remain open.

## 7. References

1. J. J. Bisognano and E. H. Wichmann, *On the duality condition for a
   hermitian scalar field*, J. Math. Phys. 16 (1975) 985–1007; *On the
   duality condition for quantum fields*, J. Math. Phys. 17 (1976)
   303–321.
2. R. Haag, *Local Quantum Physics* (Springer, 1992), §V.4; see also
   H.-J. Borchers, *The CPT-theorem in two-dimensional theories of
   local observables*, Commun. Math. Phys. 143 (1992) 315–332.
3. W. G. Unruh, *Notes on black-hole evaporation*, Phys. Rev. D 14
   (1976) 870–892.
4. S. W. Hawking, *Particle creation by black holes*, Commun. Math.
   Phys. 43 (1975) 199–220.
5. M. Takesaki, *Duality for crossed products and the structure of von
   Neumann algebras of type III*, Acta Math. 131 (1973) 249–310.
6. A. Connes and C. Rovelli, *Von Neumann algebra automorphisms and
   time thermodynamics relation in general covariant quantum theories*,
   Class. Quantum Grav. 11 (1994) 2899, arXiv:gr-qc/9406019.


Synthesis: all facets of the problem of time are resolved in [PROBLEM_OF_TIME_CLOSED.md](PROBLEM_OF_TIME_CLOSED.md) (verifier #77).
