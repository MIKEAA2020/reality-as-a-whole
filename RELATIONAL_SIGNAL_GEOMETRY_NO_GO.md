# A sign-information no-go and a relational detector response

## Result and status

A symmetry of the [covariant clock–rod–signal–detector model](RELATIONAL_MATTER_DETECTOR_GRAVITY.md) gives an **exact classical non-identifiability result**: two opposite signal preparations can have exactly the same full gravitational metric and reference fields throughout their common smooth evolution, even while their detector fields are opposite. Consequently, no observable constructed only from the metric, clock and rods can distinguish those preparations in this model. This holds with classical matter backreaction included, not merely on a frozen geometry.

We then calculate a finite clock-window interaction. In linear field-amplitude response on the exact homogeneous clock-and-rod cosmological background, a deliberately shaped pulse transfers the signal sign to a relational detector zero mode, with its leading post-pulse drift cancelled. A numerical calculation of the coupled linear fields confirms the expected small-coupling behaviour. This is **not yet an observed or durable quantum record**, a new physical law, or evidence that a geometric description can never distinguish information in other models. A signed detector reading requires a sign convention or a calibrated physical reference; no such readout apparatus is constructed here.

The no-go is a direct consequence of a familiar internal `Z2` symmetry, and zero-mode detector issues are established; see [Martín-Martínez and Louko](https://arxiv.org/abs/1404.5621). No claim of priority or non-incremental novelty is made. The advance here is the specific falsifiable constraint on a geometry-only bridge, with explicit backreacting initial data and a detector-response calculation.

## 1. Two preparations, same exact geometry

Use the preceding action with gravity, clock `T`, circle-valued rods `theta^i`, signal `Phi`, and detector field `chi`, with interaction and stabilizing potential

    V = lambda W(T,theta) Phi chi + kappa (Phi²+chi²)².

It has the exact global internal symmetry

    (Phi,chi) -> (-Phi,-chi),
    (g,T,theta) -> (g,T,theta).

The interaction and stress-energy are invariant, and the signal and detector equations change sign together. Start with the same reference-field data as in the preceding note but choose detector momentum zero (`p=0`) and prepare either

    Phi_+(0,z)= +epsilon cos z,     Phi_-(0,z)= -epsilon cos z,
    P_Phi=0,     chi=0,     P_chi=0.

The exact initial Hamiltonian constraint depends on the signal through its squared gradient and quartic potential. Its solution for `(psi,alpha)` is therefore identical in the two cases. The earlier implicit-function argument applies also to the negative-alpha branch, since its only requirement is `alpha0 != 0`. Here choose the expanding branch and parameters

    f=1/2,  tau=3/2,  alpha0=-1,
    psi=1 - epsilon² cos(2z)/188 + O(epsilon^4),
    alpha=-1 - epsilon²/12 + O(epsilon^4).

The exact momentum constraints vanish as in the previous note. Under standard local well-posedness and a common gauge, the two full classical solutions are symmetry transforms: **g, T and theta agree exactly; Phi and chi are opposite**. This is not a test-field claim. It applies only over their shared smooth evolution and wherever the relational frame is well defined.

Therefore a functional `A[g,T,theta]` has the same value for both solutions, including any covariantly defined curvature statistic or clock/rod comparison constructed solely from those fields. Such data cannot reconstruct the *signed* signal or signed detector response in this model. Conversely, `chi_rel` changes sign. If the internal sign symmetry is treated as a gauge redundancy rather than a global physical symmetry, those signs are not separately observable without an additional reference. Even if treated as physical, actually reading their signs needs a calibrated reference or apparatus, whose possible backreaction is not included. The result does not show that matter records are experimentally distinguishable without such resources.

## 2. A symmetry-based control: local response can disappear under coarse graining

Take a coupling independent of the rods, `W(T,theta)=F(T)`. The initial signal is odd under a half-period shift `z -> z+pi`, whereas its energy and the initial geometry are half-periodic. The action is invariant under the accompanying constant shift of the angular rod origin and simultaneous sign flip of `(Phi,chi)`. Uniqueness and the symmetry therefore imply, where the relational chart exists,

    chi_rel(T,r_z+pi) = -chi_rel(T,r_z).

Its uniform average over the rod circle is exactly zero, although local detector response need not vanish. This is a control on the choice of coarse-graining, not a general no-record theorem. The simulations below recover this cancellation.

To select the signed first Fourier component and generate a nonzero mean detector response, instead prescribe

    W(T,theta) = F(T) [1+cos(theta^3)].

This coupling is local as an action density and is defined in the physical rod field, but its profile extends over the torus, and the subsequent zero-mode readout is a **global rod-space average**. It is not a spatially localized measurement with a local memory.

## 3. Exact background and leading detector equations

At epsilon zero the signal and detector vanish. The full reference fields support a homogeneous spatially flat FLRW solution with scale factor `a`, proper coordinate time `t`, and expanding branch

    a(0)=1,   da/dt = sqrt(f²/4 + tau²/(12 a^4)),
    dT/dt = tau/a³,        theta^i=x^i mod 2pi.

Thus the clock and rods gravitate even in the zeroth-order background. For the stated f and tau, `da/dt=1/2` initially, corresponding to `alpha0=-1`. This is a local relational time along the chosen solutions, not a clock for a timeless absolute.

At first order in epsilon, geometry and reference fields have no signal/detector perturbation; their corrections begin at order epsilon². Write the unperturbed signal as `Phi=epsilon u(T) cos z` at lambda=0, with `u(0)=1`, `u'(0)=0`. Using T as the independent variable,

    u'' + (a^4/tau²) u = 0.

Let `C(T)` be the zero cosine coefficient of `chi/epsilon`. To first order in lambda, the detector equation gives

    C''(T) = -lambda a^6 F(T) u(T)/(2 tau²),   C(0)=C'(0)=0.

The factor 1/2 is the average of `(1+cos z) cos z`. Coupling back onto Phi changes it at order lambda²; the detector response therefore receives corrections beginning at order lambda³ in this linear-amplitude model. Nonlinear metric/reference corrections and the quartic scalar interaction are beyond this model's first order in epsilon.

After F is switched off, this linear model has `C''=0`, hence `C(T)=C(T1)+(T-T1)C'(T1)`. A detector displacement is therefore not automatically stationary. A generic one-signed pulse produces nonzero drift, illustrated below. The homogeneous massless zero mode is a standard free degree of freedom, not an intrinsically protected or decohered memory.

## 4. Pulse engineering and a finite-time response

Fix `T1=0.4` and define `B(s)=exp[-1/(s(1-s))]` for `0<s<1`, zero otherwise. Let `I=integral_0^1 B(s) ds`, and choose the smooth step `G(T)` with `G=0` before 0, `G=1` after T1, and

    G'(T)=B(T/T1)/(I T1)                  (0<T<T1).

On the specified background and initial signal, `u` is positive throughout the window; then define the predetermined profile

    F(T) = -2 tau² G''(T) / [a(T)^6 u(T)]  (0<T<T1),
    F(T) = 0                               otherwise.

This profile is smooth, sign-changing, and precomputed from the uncoupled positive-amplitude reference solution. It does not depend on which of the two signs is prepared. It is a highly tailored control, not a generic gravitational prediction. Positivity can be checked without relying solely on sampling: the background equation gives `a<1.2` for `0<=T<=0.4` (at a first crossing the speed is at most `1.2 sqrt(1.2^4+3)/6`, insufficient to cover 0.2 in 0.4). Hence `a^4/tau²<0.922`. Until any first zero, `u<=1` and `u(T)>=1-0.922 T²/2>0`; a first zero in the interval is impossible.

Substitution gives

    C(T) = lambda G(T) + O(lambda³)

in the linear-amplitude theory, so `C(T1)=lambda+O(lambda³)` and `C'(T1)=O(lambda³)`. Opposite preparations give opposite leading detector values. In the full nonlinear theory, additional terms occur at higher order in epsilon; no all-orders late-time stability is established.

The [standard-library Fourier/RK4 verifier](verification/relational_memory_pulse.py) solves the **coupled** linear field equations, not just the first-order-in-lambda formula. For lambda=0.01 it finds:

| clock T | balanced zero mode C | balanced C' | one-signed-pulse C | one-signed-pulse C' |
|---:|---:|---:|---:|---:|
| 0.4 | 0.0099998646 | 1.2344e-7 | -0.00025805 | -0.00133038 |
| 0.5 | 0.0099998770 | 1.2344e-7 | -0.00039109 | -0.00133038 |
| 0.6 | 0.0099998893 | 1.2344e-7 | -0.00052413 | -0.00133038 |

The positive-pulse control uses `F=B(T/T1)/I`; it is not strength-matched to the engineered pulse, so the table illustrates drift, not an efficiency comparison. Halving lambda reduces both balanced endpoint error and remaining slope by approximately a factor eight, consistent with cubic corrections. A uniform-spatial-coupling control has identically zero zero mode but nonzero local-mode response. Comparing modes 0–8/1,200 steps with modes 0–12/2,400 steps changes the T=0.6 zero mode by about `7.2e-16`; this is a numerical convergence check, not a rigorous error bound. [Full output](verification/relational_memory_pulse.json) includes the detector's nonzero first spatial mode.

The actual signed linearized field average is `+epsilon C` or `-epsilon C`. Its late-time value is nonzero and nearly stationary over the shown window for this engineered pulse, but the finite residual drift, inhomogeneous detector modes, quartic interaction, higher-order backreaction, noise and eventual readout are not accounted for as a durable memory. The clock has only a finite available range toward the far future of this expanding solution, so no infinite-clock-duration claim follows.

## 5. What this constrains

- **Geometry-only information reconstruction fails for this example** if the two sign-related configurations are treated as distinct physical states: the full coupled solutions have identical metric and reference fields yet opposite matter detector fields. A purported cross-framework map that uniquely infers this signed content from geometry and clock/rods alone is therefore non-injective. This is not a no-go for approaches that include matter observables, relational calibration or the appropriate symmetry quotient.
- **Coarse-graining is consequential:** a local detector response can cancel in an averaged channel. An operational theory must say which detector algebra and readout are accessible, not infer records from energy density or curvature alone.
- **A record needs resources:** tailored control and a detector field produce a candidate response. A sign reference, physical readout, noise, stable memory, complete outcomes and backreaction of those extra elements remain to be modeled.
- **No consciousness inference:** a failure of a particular geometry-only map to reconstruct matter sign does not identify experience, prove distinct experiences, or establish the user's desired absolute. It is a physical identifiability constraint on one candidate bridge.

## 6. Verification boundaries and next gate

Run `python verification/relational_memory_pulse.py`. The code checks the displayed second-order initial-data coefficients with exact rational arithmetic, then evolves the exact homogeneous background and finite cosine-Galerkin truncation of the linear **signal and detector** equations in clock time. It tests zero coupling, uniform-spatial coupling, two pulse profiles, two lambda values, and numerical refinement. It does not solve nonlinear Einstein evolution, construct a physical Hilbert space, measure probabilities, or verify a POVM. The exact sign-symmetry argument is analytic and concerns the full action, whereas the computed pointer magnitude is perturbative.

A next meaningful test is to include a physical sign reference and readout, evolve their backreaction, and compare complete outcome distributions for the same relational event. Quantum fields on this cosmology, zero-mode states, and a finite-resolution clock POVM must be specified before making a quantum record claim. Full discrete/refoliation tests and the wider zero-residue programme remain open.
