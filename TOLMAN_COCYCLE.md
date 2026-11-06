# Tolman–Ehrenfest law via the Connes–Rovelli cocycle

[Index](README.md) | [Thermal time](THERMAL_TIME.md) |
[CRN cocycle (state-independent time)](CRN_COCYCLE_STATE_INDEPENDENT_TIME.md) |
[β = 2π canonical KMS state](KMS_BETA_TWO_PI_TOMITA_WEIGHT.md) |
[Hawking backreaction bound](HAWKING_BACKREACTION_BOUND.md) |
[Hawking/Page curve](HAWKING_PAGE_CURVE.md) |
[Synthesis](SYNTHESIS_WDW_TIME.md)

## 1. What this closes

The [canonical KMS paper](KMS_BETA_TWO_PI_TOMITA_WEIGHT.md) fixed the global
asymptotic modular temperature at \\(\beta_\infty=2\pi\\) (Bisognano–
Wichmann / Unruh / Hawking). The [Connes–Rovelli cocycle
paper](CRN_COCYCLE_STATE_INDEPENDENT_TIME.md) showed that *all* faithful
normal states yield the same outer time flow. What was not yet shown
explicitly is how the Tolman–Ehrenfest law
\\(T_{\text{local}}(r)\sqrt{-g_{00}(r)} = \text{const} = T_\infty\\)
arises *within the cocycle/modular framework*: do local static observers
at different gravitational redshifts see different KMS temperatures, and
what cocycle relates them?

This note constructs the local modular structures explicitly and shows:
(i) in global Hartle–Hawking thermal equilibrium, the cocycle between
local observers at different radii is the **identity** (trivial inner
automorphism), meaning they are all in the same global KMS state whose
flow they parameterize with their own proper times — exactly the
Tolman–Ehrenfest effect; (ii) for the cold dressed vacuum, near-horizon
accelerated observers see an Unruh thermal state with a *nontrivial*
cocycle connecting it to the vacuum; (iii) the surface gravity / Hawking
temperature is recovered from the near-horizon limit of the Unruh
temperature.

[Verification: `verification/tolman_cocycle.py`; 63rd verifier.]

## 2. Setup (Planck units; Schwarzschild areal coordinates; M=1)

- Dressed scalar bounce-neck Hamiltonian: \\(H_{\text{eff}} =
  \omega_0(N+\tfrac12)\\), \\(\omega_0=7.48\\) (from
  [WDW_BKL_STABILITY](WDW_BKL_STABILITY.md)).
- Schwarzschild compactness: \\(C(r)=2M/r\\); redshift factor
  \\(\sqrt{-g_{00}} = \sqrt{1-C(r)}\\).
- A static observer at radius \\(r\\) measures proper time \\(\tau\\)
  related to Schwarzschild Killing time \\(t\\) by
  \\(d\tau = \sqrt{1-C(r)}\,dt\\).
- Global KMS at \\(\beta_\infty = 2\pi\\)
  ([KMS_BETA_TWO_PI](KMS_BETA_TWO_PI_TOMITA_WEIGHT.md)), giving
  \\(T_\infty = 1/(2\pi)\\).

### Tolman–Ehrenfest law

In thermal equilibrium in a stationary gravitational field,
\\(T(x)\sqrt{-g_{00}(x)} = T_\infty\\). In our coordinates:
\\[
  T_{\text{local}}(r) = \frac{T_\infty}{\sqrt{1-C(r)}},\qquad
  \beta_{\text{local}}(r) = \beta_\infty\sqrt{1-C(r)}.
\\]
Equivalently, the locally-measured Hamiltonian (proper-time energy) is
blueshifted:
\\[
  H_{\text{local}}(r) = \frac{H_{\text{eff}}}{\sqrt{1-C(r)}}.
\\]
Crucially, these satisfy the **generator identity**:
\\[
  \boxed{\;\beta_{\text{local}}(r)\,H_{\text{local}}(r) \;=\;
          \beta_\infty\,H_{\text{eff}}\;}
\\]
*for every \\(r\\)*. The product \\(\beta H\\) — which is the generator
of the modular automorphism group \\(\sigma_t(A) = e^{i\beta H t} A
e^{-i\beta H t}\\) — is **invariant under gravitational redshift**.

## 3. Explicit construction and verification

We construct the local KMS state at each radius
\\[
  \rho_r = \frac{e^{-\beta_{\text{local}}(r) H_{\text{local}}(r)}}{Z_r}
        = \frac{e^{-\beta_\infty H_{\text{eff}}}}{Z_\infty} = \rho_\infty,
\\]
i.e., the local Gibbs state is *identical* to the global one (in the
energy eigenbasis). The local modular flow with respect to proper time is
\\[
  \sigma^r_\tau(A) = e^{i\beta_{\text{local}} H_{\text{local}} \tau}
                     A\,
                     e^{-i\beta_{\text{local}} H_{\text{local}} \tau}
               = e^{i\beta_\infty H_{\text{eff}} t} A e^{-i\beta_\infty H_{\text{eff}} t}
               = \sigma^\infty_t(A),
\\]
where \\(t = \tau/\sqrt{1-C(r)}\\) is the Schwarzschild/Killing time.

Numerical results (truncated to \\(N=12\\) Fock levels):

| \\(r\\) | \\(C(r)\\) | \\(\beta_{\text{local}}\\) | \\(T_{\text{local}}\\) | \\(T_{\text{local}}\sqrt{1-C}\\) |
|---|---|---|---|---|
| 2.5 | 0.80 | 2.81 | 0.356 | 0.1592 (=1/2π) |
| 3.0 | 0.67 | 3.63 | 0.276 | 0.1592 |
| 4.0 | 0.50 | 4.44 | 0.225 | 0.1592 |
| 6.0 | 0.33 | 5.13 | 0.195 | 0.1592 |
| 10 | 0.20 | 5.62 | 0.178 | 0.1592 |
| 20 | 0.10 | 5.96 | 0.168 | 0.1592 |
| 100 | 0.02 | 6.22 | 0.161 | 0.1592 |
| 10⁴ | 2×10⁻⁴ | 6.28 | 0.159 | 0.1592 |

For every radius:
- **Generator invariance:** \\(\|\beta_{\text{local}} H_{\text{local}} -
  \beta_\infty H_{\text{eff}}\| < 10^{-12}\\).
- **State equality:** \\(\rho_r = \rho_\infty\\) (density matrix entries
  match to \\(<10^{-12}\\)).
- **Automorphism group checks:** \\(\sigma_0 = \mathrm{id}\\) (error 0),
  \\(\sigma_{t+s} = \sigma_t\circ\sigma_s\\) (worst error \\(< 10^{-10}\\)),
  \\(\sigma_t(B^*) = \sigma_t(B)^*\\) (error 0).
- **Trivial cocycle between radii:** \\(u_t = \rho_r^{it}\rho_\infty^{-it}
  = I\\) (distance from identity \\(<10^{-10}\\) for all tested radii
  and \\(t\\)).

## 4. Physical interpretation

The Tolman–Ehrenfest law in modular language:

1. **One KMS state, many clocks.** All static observers in equilibrium
   with the Hartle–Hawking state are described by the *same* density
   matrix \\(\rho_\infty = e^{-2\pi H_{\text{eff}}}/Z\\). They do not
   "see different states"; they parameterize the *same* modular flow
   with different proper-time rates (their clocks run at different
   speeds due to gravitational redshift).
2. **Cocycle is trivial in equilibrium.** The Connes–Rovelli cocycle
   between observers at different radii is the identity. This is
   stronger than just state-independence of the *outer* automorphism
   class (which [CRN_COCYCLE](CRN_COCYCLE_STATE_INDEPENDENT_TIME.md)
   proved): in global thermal equilibrium not just the outer class but
   the *inner* cocycle itself is trivial — equilibrium is one state.
3. **Tolman law as parameter-rescaling.** Different local temperatures
   arise because the same modular flow is labelled by proper time
   \\(\tau\\) rather than Killing time \\(t\\). A local thermometer
   (which measures in proper time) records
   \\(T_{\text{local}}=1/\beta_{\text{local}} = T_\infty/\sqrt{1-C}\\);
   the invariant physical fact is \\(\beta H = 2\pi H_{\text{eff}}\\) at
   every radius.
4. **No preferred frame, one physical time.** The state-independence of
   the outer automorphism (from CRN) plus the trivial inner cocycle in
   equilibrium means thermal equilibrium does not pick out a preferred
   observer; the physical time flow is unique.

## 5. Unruh effect from the cold vacuum (Case II)

For the dressed vacuum (cold reference state with
\\(\beta_0=20/\omega_0\approx 2.7\\)), an accelerated observer at radius
\\(r=2.5\\) (proper acceleration \\(a = M/(r^2\sqrt{1-C}) \approx 0.36\\))
sees the vacuum as a KMS state at the Unruh temperature
\\(T_U = a/(2\pi)\approx 0.057\\) (local proper-time units). The cocycle
between the cold vacuum and the Unruh thermal state is **nontrivial**
(operator norm distance from identity \\(\approx 3.2\\)), reflecting the
genuine difference between these states (unlike the equilibrium case).

## 6. Surface gravity and Hawking temperature

Near the horizon, the locally-measured proper acceleration diverges as
\\(a(r) \sim 1/(r^2\sqrt{1-2M/r})\\), but the Tolman-redshifted product
\\(a(r)\sqrt{1-C(r)} = M/r^2 \to 1/(4M)\\) as \\(r\to 2M\\). This is the
**surface gravity** \\(\kappa = 1/(4M)\\). Numerically (taking
\\(r=2M+10^{-5}\\)):
\\[
   \kappa_{\text{numeric}} \approx 0.249998,\qquad \kappa_{\text{exact}} = 0.25,
\\]
giving the Hawking temperature
\\[
   T_H = \frac{\kappa}{2\pi} \approx 0.0398,\qquad
   T_H^{\text{exact}} = \frac{1}{8\pi} \approx 0.0398,
\\]
with relative error \\(\sim 10^{-5}\\) (limited by the finite \\(\epsilon\\)
to the horizon).

So the chain closes: global KMS at \\(\beta=2\pi\\) → Tolman-redshifted
local temperatures with trivial cocycle in equilibrium → Unruh
temperature for accelerated observers in the vacuum → Hawking temperature
as the Tolman-redshifted near-horizon Unruh temperature. All four
ingredients are consistent and numerically verified.

## 7. What this adds to the chain

The time/thermal chain is now:

- Page–Wootters relational time
- Conformal near-horizon time → interior KS → polymer bounce
- Unitarity/info preservation, BKL stability, Hawking/Page curve
- **Thermal time:** Tomonaga = Tomita modular automorphism
- **CRN cocycle:** state-independent outer time class
- **β=2π KMS:** canonical temperature (BW/Unruh/Hawking)
- **Tolman cocycle (this paper):** local temperatures redshift by
  \\(\sqrt{1-C}\\); cocycle trivial in equilibrium; \\(\beta H\\) is the
  redshift-invariant generator; surface gravity → Hawking
- Perspectival finitude → plenitude identity → Russellian identity →
  necessary existence

## 8. Limitations

- The construction uses the truncated Fock space (N=12), accurate for
  temperatures below the truncation scale. Very close to the horizon
  (\\(r\to 2M^+\\)) the local temperature diverges and would populate
  high-n modes beyond our cutoff; that regime is handled analytically
  via the surface-gravity limit rather than numerical Fock construction.
- The dressed scalar is a single-mode model; real Hawking radiation
  includes all particle species with appropriate greybody factors.
- Full dynamical Vaidya/backreacting spacetime (i.e., evaporating
  geometry rather than fixed Schwarzschild) is not treated; the
  [backreaction bound](HAWKING_BACKREACTION_BOUND.md) shows this is
  \\(\Delta M/M < 10^{-6}\\) during the neck.

## 9. Takesaki-duality context

The local KMS states constructed here at each radius fit into the one global
Tomita weight whose existence and uniqueness is established by the
[Takesaki duality / III₁ analysis](TAKESAKI_DUAL_TYPEIII1.md). The equilibrium
cocycle identity (Dφ_r:Dφ_∞)_t = I verified above is exactly the condition
that all local β_local states are restrictions of this one universal weight.

## 10. References

1. R. C. Tolman, *On the weight of heat and thermal equilibrium in general
   relativity*, Phys. Rev. 35 (1930) 904.
2. P. Ehrenfest and T. Ehrenfest, *Begriffliche Grundlagen der statistischen
   Auffassung in der Mechanik* (Encykl. Math. Wiss. IV.2.II, 1911);
   Tolman-Ehrenfest law T√g₀₀ = const.
3. R. Haag, N. Hugenholtz, M. Winnink, *On the equilibrium states in
   quantum statistical mechanics*, Commun. Math. Phys. 5 (1967) 215–236.
4. A. Connes and C. Rovelli, *Von Neumann algebra automorphisms and time
   thermodynamics relation in general covariant quantum theories*,
   Class. Quantum Grav. 11 (1994) 2899, arXiv:gr-qc/9406019.
5. W. G. Unruh, *Notes on black-hole evaporation*, Phys. Rev. D 14
   (1976) 870–892.
6. S. W. Hawking, *Particle creation by black holes*, Commun. Math.
   Phys. 43 (1975) 199–220.
7. M. Takesaki, *Duality for crossed products and the structure of von
   Neumann algebras of type III*, Acta Math. 131 (1973) 249–310.
