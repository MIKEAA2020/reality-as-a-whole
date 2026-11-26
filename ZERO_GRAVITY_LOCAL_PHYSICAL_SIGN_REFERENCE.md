# A physical sign reference in the localized gravity candidate

## Result

The prior [finite-window calculation](ZERO_LOCALIZED_FINITE_WINDOW_GRAVITY_RESPONSE.md) retained a local detector difference after switch-off but compared it against an externally specified **sign convention**. This pass replaces that convention with a **dynamical reference field** in the same generally covariant gravity–matter action. The new field has its own initial gradient energy, enters the gravitational constraints, propagates and interacts with the detector. A local composite `reference × detector` is unchanged when all three matter fields are simultaneously sign-relabelled.

For two opposite signal preparations with the **same physical reference**, the full initial constraints are identical and a small-amplitude implicit-function argument gives exact initial data in the extended model. A numerical leading-amplitude calculation, retaining both signal–detector and reference–detector couplings, gives distinct local reference-relative values at sampled times after the localized coupling is switched off. Unlike the previous calculation, the detector response is compared to a **field inside the model**, not just a stipulated sign label.

This is a useful physical interface, **not a completed memory or proof of experience**. The computed reference and detector both evolve; the local composite is not a constructed instrument, an error-bounded stable record or a subject. The finite-time calculation linearizes matter about a gravitating clock-and-rod background and does not evolve nonlinear Einstein backreaction. The exact Hamiltonian constraint is not shown to be the actual cosmos's total energy. [Tests](verification/zero_gravity_local_physical_reference_test.py).

## 1. A common action with a real reference

Extend the action of [the localized candidate](ZERO_LOCALIZED_RELATIONAL_SUBJECT_IDENTITY_CANDIDATE.md) by a real scalar reference field `σ`, and replace the stabilizing potential by one involving all three matter fields:

```text
S = ∫d⁴x √−g [ R_g
  − 1/2(∇T)² − f²/2 Σᵢ(∇θⁱ)²
  − 1/2(∇Φ)² − 1/2(∇χ)² − 1/2(∇σ)²
  − W(T,θ) (λ Φχ + μ σχ)
  − κ₄(Φ²+χ²+σ²)² ].
```

Use the same conventions `16πG=1`, spatial three-torus, physical scalar clock T and three circle-valued rods θ. Here `R_g` is spacetime scalar curvature, Φ is the signal, χ the detector and σ the **new physical reference field**. `κ₄>0`; λ and μ are real coupling parameters. W is the same smooth bump in a finite clock interval and three-dimensional rod patch constructed in [the previous pass](ZERO_LOCALIZED_FINITE_WINDOW_GRAVITY_RESPONSE.md). It is a chosen part of the action, not a derived autonomous control system. The quartic stabilizes the potential against the bounded, spatially/temporally varying bilinear terms; the potential need not be nonnegative pointwise.

The action is invariant under the simultaneous internal sign transformation

```text
(Φ, χ, σ) → (−Φ, −χ, −σ),
```

with the metric, T and θ unchanged. The sign of χ alone is convention-sensitive under that transformation, but `σχ` is invariant. The symmetry may be interpreted as a global symmetry or, in a different completed theory, potentially as a redundancy; this calculation does not decide which interpretation is physically correct. The observable we examine is relational under the **specified** transformation either way. It is not an experiential quantity.

## 2. The reference contributes to the same initial gravitational constraints

Take on the initial torus, in the old conformal ansatz,

```text
hᵢⱼ=ψ(x)⁴δᵢⱼ,     πⁱʲ=α√h hⁱʲ,
T=0, P_T=τ,         θⁱ=xⁱ mod 2π, P_θ=0,
Φ_s=s ε b cos z,   P_Φ=0,
χ=0,                P_χ=0,
σ=ε r B(x),         P_σ=0,        s=±1.
```

The smooth bump B is the product of the three localized rod bumps in the previous report. The comparison uses `b=2`, `r=1`, `f=1/2`, `τ=3/2` and the expanding `α₀=−1` branch. In particular, this is a **different detector preparation** from the preceding pass: detector momentum is now zero in both cases. Both signals use the *same* reference field, not opposite references.

The momentum constraints vanish exactly: the gravitational momentum density has constant α, and `P_A∂ᵢA` vanishes for each matter/reference field in these data. The normalized Hamiltonian constraint is

```text
0 = 8ψ⁻⁵ Δψ − (3/2)α²
    + (3/2)f²ψ⁻⁴ + (1/2)τ²ψ⁻¹²
    + (ε²/2)[b² sin²z + r²|∇B|²]ψ⁻⁴
    + κ₄ ε⁴[b² cos²z + r²B²]².
```

The explicit positive gradient term `ε²r²|∇B|²ψ⁻⁴/2` is the reference's initial local energy contribution; its quartic contribution and the signal–reference cross term are also retained. The bilinear couplings contribute zero initially because χ=0 (and W also vanishes at the switching endpoint). Flipping s changes neither the displayed constraint nor its zero, while holding σ fixed. The reference is not assumed energy-free.

### Why small exact initial solutions exist in the ansatz

Normalize the conformal factor to spatial mean `<ψ>=1`. At ε=0, `ψ=1` and `α₀²=f²+τ²/3=1`. Linearization in the mean-zero perturbation v and change A in α is

```text
(v,A) ↦ 8Δv − L v − 3α₀ A,       L=6(f²+τ²)=15.
```

The zero Fourier mode fixes A because `α₀≠0`; every nonzero torus mode has eigenvalue `−8|k|²−15`, never zero. The operator is an isomorphism between the appropriate mean-zero periodic Hölder spaces, with the constant mode supplied by A. For the smooth bump and sufficiently small ε, the implicit-function theorem and elliptic regularity therefore give a nearby positive smooth ψ and α solving the **full displayed initial constraint**, on the stated branch. This extends the earlier one-dimensional ansatz to three spatial dimensions. It gives no numerical ε radius, global evolution or quantum solution. The algebraic [tests](verification/zero_gravity_local_physical_reference_test.py) check sign invariance, the extra reference term and the Fourier eigenvalues; they do not compute the exact nonlinear ψ.

The compact model's full canonical Hamiltonian is a lapse-and-shift combination of constraints and vanishes on shell, absent a spatial-infinity boundary term. That is not automatically a measurable whole-universe energy or a proof about the actual cosmos. Reference, signal, detector and geometry are all retained in the same theory; the gravitational and matter terms are not independently localized observable energies merely because they balance in a constraint.

## 3. A relational composite, not an external sign label

In a patch where `X=(T,θ¹,θ²,θ³)` is invertible, define the physical clock/rod-relative fields

```text
χ_rel(t,r)=χ(X⁻¹(t,r)),     σ_rel(t,r)=σ(X⁻¹(t,r)),
Q(t)= [∫ d³r B(r) σ_rel(t,r)χ_rel(t,r)] / [∫ d³r B(r)].
```

The integrations are in the specified rod-value coordinates over their torus, with B selecting a localized patch. Under a spacetime diffeomorphism acting on all fields, the value at the corresponding reference-field event is unchanged; under the simultaneous internal sign transformation, the product is unchanged. This is a physical *candidate observable* within the model. It does not require a separate consciousness or an external reference frame.

The averaging functional and coupling profile are still selected analytically. No apparatus that autonomously computes, stores or reports Q is built. Using σ as a physical reference is progress over declaring an orientation by fiat, but its particular state, coupling, clock/rod patch and interpretation have not been derived from the whole's self-sufficient nature.

The two preparations `(Φ,σ,χ)=(+εb cos z,+εB,0)` and `(−εb cos z,+εB,0)` are **not** related by the simultaneous sign transformation: that transformation also reverses σ. In the calculation, the common reference makes their relative signs distinct. By contrast, transforming *all* matter fields changes no Q and is not to be counted as a new detector outcome merely by relabelling.

## 4. Coupled finite-window calculation

Linearize the three matter fields to first order in ε about the exact homogeneous **gravitating** clock/rod background, retaining the full λ and μ coupling within that linear system. The quartic field force and the response of geometry and reference-field coordinates to the inhomogeneous matter appear at higher order in ε and are not computed. For each field component the free part obeys

```text
Y'' = (a⁴/τ²) ΔY,
```

and the localized interaction adds

```text
Φ'':  −(a⁶/τ²) W λχ,
χ'':  −(a⁶/τ²) W (λΦ+μσ),
σ'':  −(a⁶/τ²) W μχ.
```

Primes are T derivatives on the homogeneous reference background. The code evolves the actual coupled linear equations using periodic pseudospectral spatial derivatives and RK4. Linearity allows an exact **within-the-linearized-model** decomposition into a common-reference component and a signal component; their sum and difference are the two preparations. The nonlinear composite Q is evaluated from the resulting fields, not imposed as a bit.

For `λ=0.1`, `μ=0.08`, initial `σ/ε=B`, `Φ/ε=±2 cos z`, and initial detector and all three field velocities zero, the `20³`/400-step computation gives:

| Clock T | `Q_+/ε²` | `Q_−/ε²` | `(Q_+−Q_−)/ε²` | `(dQ_+/dT)/ε²` |
|---:|---:|---:|---:|---:|
| 0.4, switch-off | −0.003533 | +0.001874 | −0.005407 | −0.013226 |
| 0.6 | −0.004685 | +0.002516 | −0.007202 | +0.002233 |
| 0.8 | −0.002852 | +0.001583 | −0.004435 | +0.014433 |

The interaction is off after T=0.4. Both local reference-relative values remain different at these **sampled** later times, but they drift and their derivatives change sign: this is not a stable latch or indefinitely retained memory. A concrete illustration with ε=0.01 gives a leading-model difference at T=0.6 of about `−7.20×10⁻⁷` in the model's units; no nonlinear or instrumental error bound justifies treating that number as an empirical prediction.

For comparison, at T=0.6, `16³`/320 steps gives normalized difference `−0.0071381`; `20³`/400 gives `−0.0072015`; and a separate `24³`/480 run gives `−0.0071434`. At `16³`, doubling time steps changes the sampled differences by less than `10⁻⁹`. These are discretization comparisons, not rigorous convergence bounds. The reference at the patch center changes appreciably over the interval; the detector's reference is **dynamical**, not an ideal frozen sign standard.

Controls: with λ=0, the signal has no influence on the reference–detector sector and the computed preparation difference is zero; changing λ to −λ reverses the difference in this linear-amplitude model. With μ=0, the reference no longer drives the detector: the common offset `(Q_++Q_−)/2` vanishes in this specific zero-velocity preparation, whereas it is nonzero when μ=0.08. Simultaneously flipping both σ and χ leaves Q unchanged. These establish a physical contrast under the declared action and reference preparation, not independence from all possible conventions or all possible physical symmetries.

## 5. What is needed before calling it a record

A mathematical local composite is not yet a physically realized readout. The two values in the table have opposite signs in this ideal model, but there is no actual decision apparatus, quantum instrument, noise model, error bound, preparation procedure or proof of stability. A finite Fourier approximation also does not exactly maintain the source's continuum compact support, and only the coupling—not the signal or subsequent freely propagating fields—is localized.

One conditional statement follows: at one of the displayed times, **if** a physical readout separately measures the same relational Q and the total errors, including approximation and calibration, are bounded below half the predicted separation, it can distinguish the two preparations at that time. This is a conditional margin, not a demonstrated error rate. Constructing a reference-relative memory field or material readout with its own backreaction remains the next physical task.

## 6. Relation to the intrinsic-identity aim

This result improves the physical side of the common-constitution programme: a local, sign-relative distinction can be defined using dynamical matter fields whose energy participates in the same constraints as geometry and internal clocks. It does not establish that a scalar field, detector, comparator, sign or localized patch is a subject or felt quality. Experience is not inferred from “information processing” or assigned by calling one value pain.

A successful candidate would identify a sufficiently organized occurrence with its lived character **intrinsically and noncausally**, while accounting for its subject, persistence, access and physical relations. Direct acquaintance is an internal mode of access to that same occurrence, not an extra mental substance, and need not be exhaustible in language. The present calculation supplies neither a privileged subject boundary nor the required phenomenological anchor. It also does not derive the action, reference preparation or physical cosmic energy from the whole's self-sufficient nature.

The appropriate next step is a **finite-time localized readout/memory with an internal reference**, explicitly accounting for its degrees of freedom, coupling and gravitational energy, followed by a principled subject-and-quality proposal anchored in actual first-person evidence. The user's full-intelligibility requirement remains the guiding premise; unaccounted-for brute facts or unresolved regress are not being treated as alternative solutions.

## Verification

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=verification:. \
 python -m unittest verification.zero_gravity_local_physical_reference_test \
 verification.zero_localized_gravity_finite_response_test -v
```

NumPy is required; an existing pin is in [gravity requirements](verification/requirements-gravity-spin-pointer.txt). The new tests check initial sign invariance and reference gradient cost, the Fourier-mode invertibility control, sampled contrast, symmetry and zero/reversed-coupling controls, three spatial resolutions and temporal refinement. They do not verify the infinite-dimensional implicit-function theorem, solve the nonlinear constraints/evolution numerically, establish measurement accuracy, or identify experience.
