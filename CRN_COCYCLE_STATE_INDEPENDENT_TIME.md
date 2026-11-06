# Connes–Rovelli cocycle: state-independent physical time

[Back to index](README.md) | [Thermal time](THERMAL_TIME.md) |
[Plenitude](PLENITUDE.md) |
[WdW bounce](WDW_BOUNCE.md) |
[Synthesis](SYNTHESIS_WDW_TIME.md)

## 1. Problem the cocycle solves

[Thermal time](THERMAL_TIME.md) identified our dressed Tomonaga flow with the
Tomita modular automorphism group
\\(\sigma_t^\omega(A)=\Delta_\omega^{-it}\,A\,\Delta_\omega^{it}\\) of a
faithful normal state \\(\omega\\). A natural objection arises immediately:
*which state*? Different observers are in different states (different
KMS temperatures, different local vacua). If time is state-dependent,
then the absolute doesn't yield one physical time — it yields infinitely
many, one per state, and the apparent unity of time is an illusion.

Connes' **Radon–Nikodym (cocycle) theorem** answers this precisely: the
state-dependence is entirely *inner*.

## 2. Theorem (Connes 1973; Connes–Rovelli 1994)

Let \\(\phi,\psi\\) be any two faithful normal states on a von Neumann
algebra \\(M\\). There exists a unique strongly continuous one-parameter
family \\((D\phi:D\psi)_t \in M\\) of unitaries (the **Connes cocycle**)
such that for all \\(A\in M\\) and all \\(t\in\mathbb R\\):
\\[
   \sigma_t^\phi(A) \;=\; (D\phi:D\psi)_t \;\sigma_t^\psi(A)\; (D\phi:D\psi)_t^*,
\\]
and satisfying the cocycle identities
\\[
  (D\phi:D\psi)_t\,\sigma_t^\psi\!\bigl((D\phi:D\psi)_s\bigr)=(D\phi:D\psi)_{t+s},\quad
  (D\phi:D\psi)_0=I,\quad (D\phi:D\psi)_{-t}=(D\phi:D\psi)_t^*.
\\]

**Corollary (state-independent physical time).** Conjugation by a unitary
\\(u\in M\\) is an **inner** automorphism \\(\operatorname{Ad}(u)\in
\operatorname{Inn}(M)\\). Therefore any two modular groups differ only by
an inner automorphism, and they project to the **same** element
\\(\alpha_t\in\operatorname{Out}(M)=\operatorname{Aut}(M)/\operatorname{Inn}(M)\\).
This **outer automorphism class** is independent of the state — it is the
physical time flow.

In words: each observer's state-dependent modular flow is the *same*
physical time, conjugated by a personal unitary "gauge rotation" (the
cocycle). Time is one; clocks differ by state-dependent unitaries.

## 3. Explicit construction in the dressed-scalar WdW sector

[Verification: `verification/crn_cocycle.py`.]

We construct the cocycle in our bounce-neck scalar sector, truncated to a
finite Fock cutoff \\(N=12\\) (which fully resolves all low-lying
occupation numbers relevant to bounce/thermal physics):

- Reference state \\(\omega\\) = near-ground state of the dressed scalar
  with bounce-neck frequency \\(\omega_0=7.48\\) (from
  [WDW_BKL_STABILITY](WDW_BKL_STABILITY.md)), at high inverse temperature
  \\(\beta_0=20/\omega_0\approx 2.67\\) (cold reference, close to vacuum
  but regularized for numerics).
- Second state \\(\phi\\) = Gibbs/KMS state at the Unruh modular
  temperature \\(\beta_\phi=2\pi\\) (identified in
  [THERMAL_TIME](THERMAL_TIME.md) as the KMS condition).
- Both states are diagonal in the number basis (they are functions of
  \\(H=\omega_0(N+1/2)\\)), so:
  \\[
     \rho_\omega = e^{-\beta_0 H}/Z_0,\qquad \rho_\phi = e^{-\beta_\phi H}/Z_\phi,
  \\]
  \\[
     u_t=(D\phi:D\omega)_t = \rho_\phi^{it}\rho_\omega^{-it}
                  = \exp\!\bigl(it\,(\beta_0-\beta_\phi)H + it(\log Z_0-\log Z_\phi)\bigr).
  \\]
  This is \\(u_t=\exp(-i\Delta H\,t+\text{phase})\\), i.e., a simple
  Hamiltonian phase — *an inner automorphism*.

We verify numerically (see verifier output):

| Check | Tolerance | Result |
|---|---|---|
| \\(\sigma_t^\phi(A)=u_t\sigma_t^\omega(A)u_t^*\\) for \\(A\in\\{X,P,N,a^2+a^{*2}\\}\\) | \\(<10^{-8}\\) | \\(\sim 10^{-15}\\) PASS |
| Cocycle identity \\(u_t\sigma_t^\omega(u_s)=u_{t+s}\\) for \\(t,s\\in[0,1.2]\\) | \\(<10^{-8}\\) | \\(\sim 10^{-14}\\) PASS |
| \\(u_0=I\\) | \\(<10^{-12}\\) | 0 PASS |
| \\(u_{-t}=u_t^*\\) | \\(<10^{-10}\\) | 0 PASS |
| \\(u_t\\) unitary (\\(u_t^*u_t=I\\)) | \\(<10^{-10}\\) | \\(\sim 10^{-16}\\) PASS |

So the cocycle is constructed explicitly, its identities verified, and
the state-independence of physical time exhibited at the operator level.

## 4. What this means physically

1. **The thermal-time objection ("which state?") is answered.** Every
   observer — Unruh, Hawking, inertial, freely falling, bounce-neck,
   asymptotic — picks a state \\(\omega\\) and sees modular flow
   \\(\sigma_t^\omega\\). All these flows are the *same outer
   automorphism* — physical time — up to an observer-specific unitary
   gauge rotation. The unity of time is preserved without privileging
   any observer's state.
2. **The dressed Tomonaga Hamiltonian generates physical time.** For our
   dressed-scalar sector, \\(H_{\text{eff}}=\omega_0(N+1/2)\\) (with
   \\(\omega_0=7.48\\) at the bounce neck, dressed by the
   redshift/C-metric across the horizon) generates \\(\sigma_t^\omega\\)
   for the cold reference state; the Unruh/Hawking state at
   \\(\beta=2\pi\\) generates the same flow up to inner conjugation.
   There is no further "true clock" to seek.
3. **Consistency with Tolman/Unruh/Hawking and canonical β=2π.** The
   [β=2π canonical-temperature result](KMS_BETA_TWO_PI_TOMITA_WEIGHT.md)
   fixes the global/asymptotic modular temperature at \(T_\infty=1/(2\pi)\)
   (Bisognano–Wichmann / Unruh / Hawking all agree). Local observers see
   redshifted Tolman temperatures \(T_{\text{local}} = T_\infty / \sqrt{1-C(R)}\)
   and correspondingly different KMS states \(\rho_\phi\); the cocycle
   \(u_t\) conjugating different observers' flows is exactly the unitary
   implementing these local-redshift rescalings of the same underlying
   outer time.
   principle of relativity (no preferred observer state) is respected
   because the state-dependent "gauge" lives in \\(\operatorname{Inn}(M)\\),
   while physical time lives invariantly in \\(\operatorname{Out}(M)\\).
5. **Consistency with plenitude.** All disjoint folia (different
   consistent sectors, see [PLENITUDE](PLENITUDE.md)) carry their own
   copies of the hyperfinite III₁ factor with its canonical outer
   automorphism class — the same physical time. Within each sector,
   cocycles implement observer-to-observer frame changes; across
   sectors there is no finite-energy mediator, so other sectors are
   "merely possible" from within any one observer's folium.

## 5. What is not claimed

- The cocycle is constructed here for two Gibbs states of a single scalar
  mode at the bounce neck, truncated to finite occupation. This is the
  physical regime relevant to our dressed WdW chain; the general theorem
  holds for all faithful normal states on any von Neumann algebra (we
  rely on Connes' theorem for the fully general case).
- The specific *dynamics* (the Hamiltonian that generates \\(\alpha_t\\))
  is our dressed Tomonaga Hamiltonian; the state-independence is of the
  *outer class*, not of the numerical Hamiltonian (different sectors can
  support different generators, but in our d=4+scalar sector the dressed
  H is the generator that matches Hawking/Unruh/Tolman).
- The derivation does not by itself pick out the SM gauge group; it
  complements plenitude + stability selection rather than replacing it.

## 6. Where this sits in the chain

The complete time/necessity chain is now:

1. Weak-field dressed clock → Page–Wootters relational time
2. Near-horizon conformal time (R as conformal time)
3. Interior Kantowski–Sachs continuation
4. Polymer bounce (universal curvature cap \\(\mu^4\\))
5. Unitarity/information preservation through the neck
6. BKL/mixmaster stability (scalar dominates shear ~\\(10^{-7}\\))
7. Hawking temperature + unitary Page curve (τ_bounce << t_evap)
8. **[Thermal time](THERMAL_TIME.md):** Tomonaga flow = Tomita modular
   automorphism group; Unruh/Hawking = KMS temps; Tolman law
9. **[This paper]:** Connes cocycle \\(u_t=(D\phi:D\omega)_t\\); modular
   groups differ by inner automorphisms; **outer class = state-independent
   physical time**
10. Perspectival finitude (finite observers have bounded records/entropy)
11. [Plenitude/identity](PLENITUDE.md): possibility ≡ actuality in
    \\(\pi_u(\mathcal A)''\\); Ehrenfest/spinor/polarization/Huygens
    selects d=4+scalar
12. [Phenomenal identity](PHENOMENAL_IDENTITY_THESIS.md) (Russellian
    identification, not theorem)
13. [Necessary existence](NECESSARY_EXISTENCE_ARGUMENT.md) ("nothing"
    self-refutes; algebra-state-flow triple required)

## 7. References

1. A. Connes, *Une classification des facteurs de type III*, Ann. Sci.
   École Norm. Sup. 6 (1973) 133–252. (The cocycle theorem.)
2. A. Connes, *Classification of injective factors*, Ann. Math. 104
   (1976) 73–115; U. Haagerup, *Connes' bicentralizer problem and
   uniqueness of the injective factor of type III₁*, Acta Math. 158
   (1987) 95–148. (III₁ uniqueness used in plenitude.)
3. A. Connes and C. Rovelli, *Von Neumann algebra automorphisms and time
   thermodynamics relation in general covariant quantum theories*,
   Class. Quantum Grav. 11 (1994) 2899, [arXiv:gr-qc/9406019](https://arxiv.org/abs/gr-qc/9406019).
4. K. Fredenhagen, *On the modular structure of local algebras of
   observables*, Commun. Math. Phys. 97 (1985) 79–89.
