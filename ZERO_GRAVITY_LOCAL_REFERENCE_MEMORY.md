# A localized reference-relative memory field in the gravity candidate

## Result

The previous [physical-reference model](ZERO_GRAVITY_LOCAL_PHYSICAL_SIGN_REFERENCE.md) left a signal-dependent detector/reference contrast after switch-off, but that contrast was not a separate stored degree of freedom. This pass adds a **dynamical memory field** `M` to the same constrained gravity–matter action. A second localized, clock-controlled interaction couples it to the physical reference–detector product `σχ`; the memory is invariant under the joint sign redescription of the three original matter fields.

In a finite-mode perturbative calculation, the *difference* between two memory fields is nonzero at all five sampled clock readings from `T=0.6` to `T=1.0`, after both interaction windows have ended. A single engineered pulse makes the **local weighted memory difference's slope zero at switch-off** on the calibration grid. That is a finite-window, approximate storage result—not proof of a stable memory: the difference subsequently drifts substantially, and a point reading even changes sign by the final sample.

The same exact initial-data existence argument applies after the memory is added, because its initial value and momentum are zero and its coupling initially contributes nothing to the constraints. Its later field energy and coupling are part of the full action, although nonlinear gravitational backreaction is **not** solved numerically. The result is not an actual readout, an error-controlled instrument, a subject or experience, nor a proof that the actual universe's total energy vanishes. [Tests](verification/zero_gravity_local_memory_pulse_test.py).

## 1. Extend one physical constitution rather than attach a free bit

Use the compact, generally covariant action of the [physical-reference construction](ZERO_GRAVITY_LOCAL_PHYSICAL_SIGN_REFERENCE.md), with the original clock T, circle-valued rods θ, signal Φ, detector χ and reference σ. Add a real scalar memory M:

```text
S = ∫d⁴x √−g [ R_g − 1/2(∇T)² − f²/2 Σᵢ(∇θⁱ)²
    − 1/2(∇Φ)² − 1/2(∇χ)² − 1/2(∇σ)² − 1/2(∇M)²
    − W₁(T,θ)(λΦχ+μσχ)
    − ν W₂(T,θ) σχM
    − κ₄(Φ²+χ²+σ²+M²)² ].
```

The metric, clock, rods and **all four matter fields** gravitate. The quartic with `κ₄>0` bounds the potential below even with the bounded, prescribed cubic and bilinear interactions. `λ`, `μ`, `ν`, the smooth profiles and initial preparation are model inputs; neither the action nor its parameters are derived from the whole's self-sufficient nature.

Under the model's simultaneous transformation

```text
(Φ,χ,σ,M) → (−Φ,−χ,−σ,M),
```

the action and `σχM` are invariant. M can therefore retain a distinction relative to the physical reference without its value reversing under this particular sign redescription. This is an explicit action symmetry; it is not a claim that every internal symmetry is gauge or that the model realizes all symmetries of the actual universe.

The compact spatial Hamiltonian and momentum constraints vanish on physical initial data, and the canonical generator has no usual spatial-infinity boundary term. This zero is **not automatically an observable total cosmic energy**. Nonzero signal, reference, detector and memory energy are compatible with it, and no external force is needed to balance an already specified constraint.

## 2. Initial data and a second interaction window

Use the sign-comparison data and expanding background branch of the preceding physical-reference model, with `α₀=−1`, `f=1/2`, `τ=3/2`, and a smooth compact rod bump B:

```text
Φ_s=s ε 2 cos z,     χ=0,       σ=ε B,       M=0,
P_Φ=P_χ=P_σ=P_M=0,  s=+1 or −1.
```

The clock, rods and conformal gravitational data are those in that report. The two signs share the **same reference and memory preparation**. Since `M=P_M=0`, the additional kinetic and cubic terms vanish on the initial slice. The enlarged quartic reduces to the original potential there. Consequently the preceding full Hamiltonian constraint, exact momentum constraints and small-ε implicit-function argument are unchanged. This gives exact initial data **in the stated ansatz** for both preparations, not an explicit numerical solution of those elliptic equations or a global spacetime.

Let the first interaction `W₁=F₁(T)B(θ)` run on `0<T<0.4`, as before. Introduce a second localized interaction `W₂=F₂(T)B(θ)` on `0.4<T<0.6`. Both use the same physical clock and rods. With

```text
b(s)=exp[−1/(s(1−s))] for 0<s<1; otherwise 0,
I=∫₀¹ b(s)ds,       s=(T−0.4)/0.2,
F₂(T)= [b(s)/I] [1+c(2s−1)]  on 0.4<T<0.6, otherwise 0,
```

F₂ is smooth at the endpoints. The dimensionless c is an explicitly engineered, generally sign-changing pulse; **the same pulse is used for both preparations**. It is tuned using the calculated model response, not selected according to the unknown signal during a run. Its large magnitude in the example below is an important resource and fine-tuning limitation. A physical mechanism deriving this schedule, including its own control resources, is not supplied merely by writing it as a function of T and θ.

## 3. What is calculated

On the exact homogeneous clock-and-rod gravitating background, evolve Φ, χ and σ at **leading order in ε**, keeping the full λ and μ couplings in their linear system. At leading nonzero order the memory is `O(ε²)` and obeys

```text
M_s'' = (a⁴/τ²) ΔM_s − (a⁶/τ²) ν F₂(T) B(θ) σ_s χ_s,
M_s(0)=M_s'(0)=0.
```

Primes are derivatives with respect to the model's internal clock T. On this approximation the memory's feedback into the other matter fields, quartic forces, inhomogeneous gravitational and clock/rod response, and the memory's own later backreaction are neglected. The action includes them; the **numerical calculation does not**. No bound is available on the discarded terms for a particular finite ε.

Define the local weighted two-preparation separation

```text
Δm_B(T) = [∫ B(θ)(M_+(T,θ)−M_−(T,θ)) d³θ]
           / [ε² ∫ B(θ)d³θ].
```

This is a comparator functional of physical memory fields at rod-relative locations. The two alternatives are model preparations, not two actual worlds proven to exist. A device to measure the average and its calibration is not built.

Linearity of the leading memory equation in F₂ lets us evolve the two temporal basis profiles `b(s)/I` and `(2s−1)b(s)/I` independently. On the `20³`/400-step calibration grid, choosing

```text
c = −33.27298053
```

makes the computed **weighted-average slope** `dΔm_B/dT` vanish at `T=0.6`, while Δm_B itself remains nonzero. This is a designed control, not a general theorem that localized memory is stationary. In particular it does not set the slope at every point to zero. It uses no outcome-dependent feedback, but the schedule and the calibration calculation are stipulated.

## 4. Finite sampled result and the limitation

For `λ=0.1`, `μ=0.08`, `ν=1`, the calibration grid gives:

| Internal T | weighted separation `Δm_B` | weighted slope `dΔm_B/dT` | point separation `(M_+−M_−)(T,0)/ε²` |
|---:|---:|---:|---:|
| 0.6, second pulse off | `0.00033213` | `0` by tuning | `0.00141036` |
| 0.7 | `0.00032440` | `−0.00015853` | `0.00118684` |
| 0.8 | `0.00029971` | `−0.00033820` | `0.00081093` |
| 0.9 | `0.00025646` | `−0.00052613` | `0.00034801` |
| 1.0 | `0.00019526` | `−0.00069003` | `−0.00007919` |

All entries are for **differences between preparations**, not absolute memory readings. A practical threshold would also need the common baseline, a physical reference and bounded errors. At ε=0.01 the leading-model separation at T=0.6 would be about `3.32×10⁻⁸` in model units, but no bound on approximation or measurement error is supplied.

The weighted separation retains roughly 59% of its switch-off value at the T=1 sample; the point difference has already crossed sign. Thus a claim of a robust permanent record, or of pointwise stability, would be false. The sampled nonzero values do not establish a continuous-interval lower bound. A real memory would need greater protection, a physically implemented readout and an independently specified acceptable error and duration.

### Tests and controls

- The memory difference is identically zero before the second interaction, for ν=0, and for λ=0 in the implemented perturbative model.
- Spatial grids `12³`, `16³` and `20³` are compared using **the same pulse tuned once on `20³`**, not a separately optimized pulse at each grid. At T=0.6 the weighted separations are approximately `0.00031448`, `0.00033339`, and `0.00033213`; a separate `24³`/480-step run with that same pulse gives `0.00032739`. The `24³` slope is not exactly zero (`−0.00000429`), showing that the zero-slope tuning is numerical and resolution-dependent.
- At `16³`, doubling time resolution from 320 to 640 steps changes the two basis-response values by less than `10⁻⁹` at the tested times. These are finite-resolution checks, not certified continuum or nonlinear-GR error bounds.
- The smooth compact profile is approximated by a finite pseudospectral representation; the freely propagating memory field may spread outside its interaction patch. The weighted average is not a physical confinement condition.

The [test](verification/zero_gravity_local_memory_pulse_test.py) reproduces the three primary grids, same-pulse comparison, time refinement and controls. The 24³ comparison can be reproduced by `evolve(24,480)` with the 20³ calibration coefficient.

## 5. What this means for intrinsic identity

This is a substantive improvement in the **physical interface**: the proposed localized memory is not a free abstract bit; it is a field with an invariant reference-relative coupling in the same constrained action. On the declared approximation, its state at a later clock reading depends on an earlier physical distinction.

It does **not** establish a subject, a qualitative experience, an enduring autobiography, a real report, or consciousness. The selected bump and pulse are not a subject-boundary criterion. A memory field can exist without being experienced, and reading a stored difference does not alone determine what it is like. Conversely, the user's intrinsic-identity proposal does not require experience to be an extra substance generated by a memory: a sufficiently organized physical occurrence might itself be the directly lived occurrence. This calculation supplies only a possible component of such an organization.

The right next step is to replace the tuned transient with an **error-controlled physically readable memory** or derive an alternative organization with adequate persistence, then motivate a subject boundary and a qualitative identity using first-person and physical evidence. The deeper task remains to derive the action, the physically relevant whole-level zero and the specific experience from one self-sufficient constitution. Neither brute facts nor an external creator are proposed as answers.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=verification:. \
 python -m unittest verification.zero_gravity_local_memory_pulse_test \
 verification.zero_gravity_local_physical_reference_test -v
```

NumPy is required; see [the existing requirements](verification/requirements-gravity-spin-pointer.txt). The checks exercise the two pulse bases, fixed calibration, spatial/time refinement and zero-coupling controls. They do not solve nonlinear Einstein evolution, quantify full-system errors, demonstrate a real measurement or establish any experiential identity.
