# Finite clock readings, physical instruments and a change of clock

## Result

The preceding [normalizable sphere–cosmology construction](ZERO_SPHERE_NORMALIZABLE_QUANTUM_COSMOLOGY_CLOCK.md) compared two idealized clock descriptions of the same constrained quantum state. Here we replace the ideal clock coordinate by a **finite-resolution POVM**, and give an explicit two-outcome quantum instrument whose outputs remain in that same physical Hilbert space. We then transport both the instrument and the subsequent sphere-clock observable through the previously constructed change of clock.

For the chosen packet, a Gaussian resolution of width `σ=1` and a reading window `[-2,2]`:

- The natural geometry-reading effect at scalar reading zero has probability approximately **0.47585**; the natural scalar-reading effect at geometry reading zero has probability approximately **0.23095**. These are different physical questions, not a failure of frame equivalence.
- For a separately specified instrument with yes effect **E²**, the geometry and scalar yes probabilities are approximately **0.25524** and **0.06347**, respectively. E and E² must not be confused.
- A selected geometry instrument changes a later logical-clock expectation from approximately **−0.32340** to **−0.26189** when its readout is ignored. Its mathematical outputs remain in the selected constrained physical sector; no claim is made that a realistic local detector or its energy cost has been derived.
- Transporting the *same* effect, instrument, state and later observable yields the same sequential statistics in the other representation. This follows from a unitary identity; the test checks the nontrivial transformed kernels and one sequential probability numerically.

The sphere–record confined density and its five-ray probabilities remain unchanged for every encoded logical state in this model, including both outcomes of these instruments. Pair and triple contexts also retain the same specified receiver density for arbitrary encoded logical polarizations. This strengthens the domain example without making a record into an experiencing subject.

The model uses the standard library: [verification/zero_sphere_finite_resolution_clock_instrument_test.py](verification/zero_sphere_finite_resolution_clock_instrument_test.py), 11 tests. Continuous formulas define the model; reported numerical figures use a midpoint discretization checked at increasing resolution. The code does not simulate a local gravitational measurement interaction or a closed detector.

## 1. One physical system, two natural reading POVMs

Use exactly the earlier positive-`p_φ`, negative-`p_α` FLRW branch and physical Hilbert space

```text
H_phys = L²((-7,−6), dp) ⊗ C²,
ω_h(p)=√(p²/6−2h),       h=0,1,
χ_h(p)=c_h f(p),           (c_0,c_1)=(1,i)/√2,
f(p)=√30(p+7)(−6−p) on the band, zero outside.
```

The encoded levels are the two sphere–record logical states. The chosen gravitational, scalar and rotor terms satisfy the quadratic constraint on this sector. The physical inner product, branch and rotor action are those specified in the preceding report. In particular this is not a Hilbert space of normalizable histories uniformly distributed over all clock values.

Let `F` be the unitary Fourier transform from a real spectral variable k to its conjugate reading x. Let `V` extend a band-limited wavefunction by zero into `L²(R,dk)` and then Fourier-transform it. `V` is an isometry, so for a Borel set B the Gaussian-smeared reading effect is

```text
g_B(x) = ∫_B dr exp[−(r−x)²/(2σ²)]/(√(2π)σ),
E_B = V† M_(g_B) V.
```

Here `M_(g_B)` multiplies by `g_B`. Because `0≤g_B≤1`, `0≤E_B≤I`; the effects are countably additive and `E_R=I`. Thus this is a normalized POVM even though the band-limited conjugate coordinate need not define a self-adjoint clock operator or an orthogonal sharp-reading PVM. The Gaussian width is an assumed readout resolution, not an ontologically fundamental time unit. At `σ=0` the same construction gives the band-compressed ideal-coordinate POVM, still generally not a PVM.

There are **two distinct** natural choices, each relative to a specified internal clock surface:

1. `E^α_B`: geometry reading α at `φ=0`, using k=`p_α=p` and the same Fourier isometry on both logical sectors.
2. `E^φ_B`: scalar reading φ at `α=0`, using k=`s=p_φ=ω_h(p)` in the geometry-clock representation. Different h sectors have different s bands.

The second effect becomes a well-defined physical operator in the first representation using the unitary map `W` derived in the previous report. These are relational observables in the chosen deparametrized quantization. No experimental detector, independent physical preparation of the scalar clock, or new source of φ-time probabilities is being smuggled into the model: each POVM is an additional specified physical measurement. Neither reading is an external clock.

For the symmetric window `B=[−a,a]`, its band-space kernel is

```text
K_B(k,k') = exp[−σ²(k−k')²/2] sin[a(k−k')]/[π(k−k')],
K_B(k,k)  = a/π.
```

The kernel is the Fourier transform of `g_B`. Finite resolution changes its off-diagonal structure, hence event probabilities. For `a=2`, `σ=1`, the chosen physical state gives, in continuum numerical integration,

```text
Pr(E^α_B) ≈ 0.47585,
Pr(E^φ_B) ≈ 0.23095.
```

The two coordinates and their numerical windows are stipulated in the model's chosen units; an equal numerical width does not mean the clocks are calibrated to the same physical resolution. The effect does not by itself determine a state update.

## 2. The exact clock transformation and what must be transported

Write `s=ω_h(p)`, `p_h(s)=−√(6s²+12h)`, `J_h(s)=|dp_h/ds|`, and

```text
(Wψ)_h(s) = √J_h(s) ψ_h(p_h(s)).
```

This is a unitary change of physical representation onto the corresponding h-dependent s bands. Therefore, for any state ρ, physical effect E, Kraus operator K and later effect B,

```text
ρ' = WρW†,   E' = WEW†,   K' = WKW†,   B' = WBW†,
Tr(KρK† B) = Tr(K'ρ'K'† B').
```

This identity preserves *joint sequential probabilities*, not just single expectation values. It holds for any physical input, provided all operators and instruments are transformed, not merely renamed.

For example, transporting the geometry-reading kernel to s-coordinates yields, within h,

```text
E^α_h(s,s') = √[J_h(s)J_h(s')] K_B(p_h(s),p_h(s')).
```

It is **not** the natural scalar effect `K_B(s,s')`. Likewise the transported logical observable connects `s_0(p)` to `s_1(p)`, which are generally different. The test checks these kernels, the Jacobians, physical-instrument outputs and one joint probability with a subsequent transported logical readout. Changing the clock need not change physical predictions; changing the measured relational question can.

The fact that these operators act on the physical solution space means that their output states can be mapped back to solutions of the same selected branch constraint. Equivalently, a bounded physical operation has a transported relational representative along the chosen branch. This is **not** a construction of a strongly constraint-commuting local detector Hamiltonian on the full kinematical Hilbert space, nor a proof that the operation commutes off-shell with every local GR constraint.

## 3. An actual, specified two-outcome instrument

For either of the effects E above, the exact Lüders instrument for the original window is abstractly

```text
L_yes=√E,      L_no=√(I−E).
```

It exists by the spectral theorem and transports under W. Its outcome probabilities are `Tr(ρE)` and `1−Tr(ρE)`. This report does **not** numerically compute its state update.

To calculate backaction without introducing an unverified numerical matrix square root, we separately define a different legitimate physical instrument:

```text
K_yes=E,       K_no=√(I−E²),
K_yes†K_yes+K_no†K_no=I.
```

Its yes effect is E², **not E**. It is a deliberately chosen filtered reading, not the only instrument for the underlying Gaussian window. Positivity of E ensures the square root exists. The tests apply the convergent binomial expansion of `√(I−E²)` to the wavepacket and independent complex test vectors, and check trace preservation. Its action on the selected physical sector is completely positive, and every conditional output belongs to that sector after normalization. The numerical implementation discretizes the continuum kernel; the continuum instrument itself is defined by functional calculus.

With midpoint discretization N=320, window half-width 2 and `σ=1`, the approximate results are:

| Selected instrument | `Pr(yes)` for E² | `⟨Y at φ=0 | yes⟩` | `⟨Y at φ=100⟩`, readout ignored |
|---|---:|---:|---:|
| Geometry-reading instrument | 0.25524 | 1.00000 | −0.26189 |
| Scalar-reading instrument | 0.06347 | 0.98754 | −0.30567 |
| No instrument | — | — | −0.32340 |

For the geometry instrument the joint probability of `yes` followed by the `+1` result of the logical Y readout at `φ=100` is approximately **0.13202**. The 80-point test gives 0.13204789; 160 and 320 points show convergence. The clock-switched calculation gives the same joint probability for the **transported** instrument and Y effect, rather than for the natural scalar instrument.

The nonselective measurement changes the geometry-momentum distribution; in the model this is backaction, not evidence that a preferred temporal frame was disturbed. All outcomes remain on the branch constraint. For example, in the numerical model the geometry instrument changes `⟨p_α²⟩` from about `42.28571` to `42.29260`, with corresponding changes in the on-shell scalar term. This is not a calculated detector energy cost: an actual apparatus, storage register, interaction, locality and closed-system accounting have not been supplied. An operation on the reduced physical state is not automatically a fully autonomous measurement process within the whole.

## 4. The same effects need not mean the same physical disturbance

Take the geometry instrument above and apply a logical phase flip only after `yes`. The yes/no effects and their probabilities are unchanged because the extra operation is unitary. Yet the yes-conditioned initial logical value changes from `⟨Y⟩=+1` to `−1`. Thus even the complete two-outcome effect distribution does not specify the postmeasurement state. A physical account of time must identify the apparatus or instrument when it makes claims about disturbance, memory, and subsequent records.

This is not an experimentally observed effect or a prediction distinct from ordinary quantum theory. It is an exact consequence of the chosen instrument, useful as a control against mistaking a POVM for a unique physical dynamics. The postselection probability and measurement disturbance refer to the declared physical Hilbert space, not to actual subjects or automatically realized outcomes.

## 5. Why the confined description can remain unchanged

Let `|0⟩,|1⟩` denote the two active sphere–record logical states. The tests check the complete confined density and the sphere/record table for the four polarizations `|0⟩`, `|1⟩`, `|0⟩+|1⟩`, and `|0⟩+i|1⟩`. These determine the two diagonal and two cross terms of the reduced logical operator. In the encoded model they show, up to numerical tolerance, that **every normalized logical density operator** has the same confined density and the same triple-context table:

| Sphere label | Record 01 | Record 10 |
|---|---:|---:|
| 0 | 3/40 | 1/20 |
| 1 | 1/10 | 3/10 |
| 2 | 13/40 | 3/20 |

Consequently, changing or conditioning the logical state with the above geometry/clock instruments can change richer correlations while leaving the entire declared confined state unchanged. This is stronger than checking only one phase orbit. Four-polarization tests likewise show equality of the specified receiver reductions for the pair and triple contexts for arbitrary logical states and hence for the conditional outputs of these same encoded instruments. This is a result for those states, access restrictions and the same instrument; it is not a theorem of relativistic locality or evidence of a hidden interface.

The chess and sphere analogies remain precise: the player is not a chess piece; the traveler is not a surface inhabitant. In the surface-restricted description the traveler's position stays A during the room chord and changes to B upon return; no interaction is required merely to hold the description at A. The quantum model realizes a mathematical restriction with unchanged reduced density; it does not show that the traveler, player or their activity is physically visible to confined inhabitants.

## 6. Relevance to the problem of time and to the whole

The construction now distinguishes four things that a simple statement that 'time is relational' can miss:

1. A clock reading is an effect, generally with finite resolution, not simply an ideal numerical parameter.
2. Different clock systems and different surfaces can define different operational events even in the same physical state.
3. When the *same* event and instrument are transformed, their joint probabilities agree across the two selected representations.
4. Physical state changes depend on the chosen instrument; preservation of the constrained physical sector does not by itself explain a local detector or its resources.

The point–sphere framework motivates an externally timeless whole with internal differentiation. The Lorentz-cone construction supplies a conditional kinematic link, but these finite-band POVMs, the action, the Gaussian resolution and the prepared state are further inputs. The zero here remains the rescaled constraint, not an independently defined objective total energy. No fundamental preferred foliation is introduced; nevertheless the model is homogeneous and the two branch choices are not proof of local refoliation invariance.

The unchanged confined record and the evolving logical correlation do not establish felt passage, actual subjects, or an incidence measure. They also do not establish experiential cancellation. An actual local negative experience would not be erased by a different positive one merely because a proposed signed global quantity vanishes. The thesis that all genuine possibilities are necessary and actual remains a substantive proposal; neither this instrument nor its probabilities derives it.

## 7. Next decisive work

1. Construct an **autonomous** clock–detector–record coupling that generates these effects or a physically motivated alternative while satisfying the full relevant constraints. Include the detector as part of the system, quantify postselection and energy/entropy resources, and compare the resulting instrument with this abstract CP map.
2. Extend the model beyond a homogeneous single constraint to inhomogeneous relational observables and check constraint closure and consistency under changes of slicing. No ad hoc preferred foliation should be introduced.
3. Derive or independently justify the sphere encoding, action, state and metric scale from the proposed constitution, and define the objective whole-level quantity rather than calling the constraint energy by fiat.
4. Test competing subject-incidence and experiential-valence laws against local interventions and calibrated evidence; demonstrate whether a meaningful signed experiential balance follows without denying suffering.

These are not minor wording qualifications: they are where the no-residue thesis must do new explanatory work. The current result supplies a reproducible operational target against which such a derivation can be compared.

## Reproduce

```sh
python -m unittest verification.zero_sphere_finite_resolution_clock_instrument_test -v
```

Passing confirms the encoded continuum identities and discretized numerical checks to their declared tolerances; it does not certify full quantum gravity or the metaphysical account.
