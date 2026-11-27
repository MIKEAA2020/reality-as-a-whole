# Cursor domain and instrument recheck

## Result and scope

This pass checks selected domain and error steps in the [autonomous cursor reader](ZERO_TWO_WINDOW_AUTONOMOUS_CURSOR_READER.md), the [full recorded instrument](ZERO_TWO_WINDOW_CURSOR_INSTRUMENT_AND_BACKACTION.md), and the [second-clock comparison](ZERO_TWO_WINDOW_SECOND_PHYSICAL_CLOCK.md). It uses the **corrected** right-moving carrier, the specified band model, and the previously [independently recomputed commutator certificate](ZERO_TWO_WINDOW_INDEPENDENT_CERTIFICATE_AND_CURSOR_BOUND.md).

For the stated fixed cursor/ancilla preparation, the checks yield three improvements:

* On the cursor model's finite readout interval, the complete recorded instrument has **half-diamond distance `<0.06513`** from its specified ideal support instrument, improving the earlier `<0.0662`. Its full diamond distance is `<0.13026`. This is a full joint classical-record/system-output bound, not the much smaller record-probability bound.
* A general conditional-branch inequality improves the earlier factor `2δ/q` to **`δ/q`**, where `q` is the ideal branch probability and δ bounds the half-diamond distance of the complete recorded channels. The factor is sharp, and conditional outputs remain undefined if the actual branch has probability zero.
* With the second-clock report's specified clock packet, tail estimate, product preparation and reduced-output convention, its clock-smeared half-diamond comparison improves **conditionally** from `<0.0394` to `<0.0388`. This is a different comparison and does not replace the uniform cursor bound.

The cursor is an explicitly stipulated effective model with an auxiliary scalar clock and a global support projector. The current framework treats space and time as non-fundamental constructs and experience as intrinsic. This calculation neither assumes fundamental spacetime nor derives physical spacetime, the physical whole's zero energy, subjects or the character of experience. The apparatus, preparation and measurements remain assumptions, not experimental evidence.

## 1. The correct domain for the massive/chiral comparison

Use the [corrected preparation and sign](ZERO_AUTONOMOUS_CLOCK_EVENT_READOUT.md): `p=−i∂x`, state `e^(−imvx) ψ_a(x+vt₀)`, and evolution `e^(+iHT)`. Conjugating the cursor kinetic operator by the carrier gives `p²/(2m)−vp+mv²/2`; the common constant is irrelevant to channel outputs. The comparison generator has `−vp`, whose evolution translates the envelope to the **right**.

Let K include the full old band system, flag, memory and an arbitrary untouched reference. On `L²(R;K)` the old band root and all spin/projector factors are bounded. The boosted massive and chiral generators have the form

```text
H_m = p²/(2m) − vp + A + f_b(x) C,
H_ch = −vp + A + f_b(x) C,
```

with A and C bounded self-adjoint operators on K. `p²/(2m)−vp` is self-adjoint on `H²(R;K)`; adding the bounded potential preserves that domain. `−vp` is self-adjoint on `H¹(R;K)`, and the bounded potential preserves that domain. The comparison operator is not claimed to be bounded below: the **massive** Hamiltonian, after the stated positive offset, is the physical positive branch of this conditional model.

The profile and envelope are compactly supported polynomials whose values **and first derivatives** vanish at their endpoints. Therefore their zero extensions have no delta contribution in the weak second derivative. In particular

```text
f_b ∈ W²,∞(R),      ψ_a ∈ H²(R),
||ψ_a'||₂ = √3/a,   ||ψ_a''||₂ = √(63/2)/a²,
||f_b'||₁ = 15/(8b),   ||f_b''||₁ = 10/(√3 b²).
```

The profile's weak second derivative can jump at endpoints and still be bounded; no unjustified C² endpoint matching is required. The [tests](verification/zero_cursor_domain_instrument_review_test.py) integrate the squared envelope polynomials exactly and check the endpoint conditions. The two profile L¹ expressions follow by integration over the polynomial pieces and splitting `f_b''` at `x=±b/√3`.

For the chiral solution, follow each translated cursor coordinate z and write its internal time-ordered propagator as `U_z(s)`. Its z-dependence is entirely through `f_b(z−vt₀+vs)`. Duhamel differentiation gives, in operator norm (the second derivative is understood weakly/a.e.),

```text
||∂_z U_z|| ≤ A₁ = κ||f_b'||₁,
||∂²_z U_z|| ≤ A₂ = κ||f_b''||₁ + A₁²,
||p² Ψ_ch(s)|| ≤ K₂
  = √(63/2)/a² + 2(√3/a)A₁ + A₂.
```

Here `v>0` cancels after changing variables along the trajectory. The second estimate includes the double insertion of `∂_z f_b` as well as the single insertion of `∂²_z f_b`. Product differentiation of `U_z ψ_a(z)` is valid in the Bochner-valued Sobolev space; these operator-norm estimates are uniform on K, including arbitrary references.

Thus each chiral state lies in the massive `H²` domain. Applying Duhamel on that common state domain—not treating the unbounded operator `p²/(2m)` as having a global norm—gives

```text
||e^(iH_m T) Ψ₀ − e^(iH_ch T) Ψ₀||
    ≤ ∫₀ᵀ ||p² Ψ_ch(s)||/(2m) ds ≤ T K₂/(2m).
```

This is a uniform **system-input** estimate only for the fixed cursor packet; it is not an operator-norm estimate over all cursor states. The Hamiltonians here are time independent, so the comparison may be justified by differentiating the interpolating product on the above common domain and integrating; the bounded f-derivative estimates ensure the requisite H² regularity. These arguments apply to the declared band system with bounded Ω. Extensions with unbounded additional old-system generators require their own domain/strong-commutation analysis.

For `a=b=10⁻⁶`, `m=10¹⁶`, `κ=π/2` and `T≤π/100`, rational upper bounds on π and the radicals give

```text
K₂ < 3.356×10¹³,        T K₂/(2m) < 0.0000528.
```

These are analytical bounds for the specified packet, not a simulation of the full massive cursor. The rational test also checks the existing π enclosure.

## 2. A sharper complete-instrument comparison

The previous derivation compares the recorded channel against the ideal initial-support Lüders instrument followed by `U₀(T)=e^(iΩT)`. Under the same prescribed ready states, pulse, positivity and comparator assumptions, the vector error includes

```text
δ(T) = 400 c_* T² + 2κgNb/v + T K₂/(2m) + √2 η,
N=8, g=100, c_*=0.412/(2×1.3), η<10^−31.
```

The first term continues **through the full final time**: `||Q(s)−Q||≤s||[Ω,Q]||` and Duhamel bound the difference by `Ng c_*T²/2`. Stopping that term at the end of the pulse is justified only for the earlier memory-probability comparison, not the full output state. The last term replaces the small blank Q component of the comparator's environmental state by an orthogonal recorded component; its norm is at most `√2η`.

For `T≤π/100`, exact rational upper bounds yield

```text
δ(T) < 0.06513,
(1/2)||C_actual−C_ideal||_diamond < 0.06513,
||C_actual−C_ideal||_diamond < 0.13026.
```

The diamond input includes arbitrary old-system states and untouched references, while the cursor and ancillas are fixed. The vector-isometry error is converted to trace distance and then to the recorded channel using contractivity under memory readout and discarded apparatus. It does not cover arbitrary cursor preparation or implementation mismatch. On an equal coherent P/Q input, the ideal nonselective instrument has trace distance exactly 1/2 from the no-measurement comparator, so the actual reduced-system disturbance obeys

```text
D_trace(actual, no-support-measurement comparator) > 0.43487.
```

This is model-specific measurement backaction, not an entropy arrow or general physical lower bound on heat.

## 3. Sharper normalized branch guarantee

This section is a general instrument statement, independent of the cursor's details. For normalized recorded channels with a classical outcome register, assume their joint output trace distance on the input, including any retained reference, is at most δ. For one outcome m let the actual and ideal subnormalized branch states be A and B, with traces `p` and `q`.

The event probability difference obeys `|p−q|≤δ`. If `q>δ`, then `p>0`, and

```text
D_trace(A/p, B/q)
 ≤ (||A−B||₁ + |p−q|)/(2q)
 ≤ δ/q.
```

For the second inequality, all other outcome blocks together have trace difference `q−p`, so their total trace norm is at least `|p−q|`. Adding their norms to `||A−B||₁` gives at most twice the joint trace distance. Consequently, if `q≥κ>δ`, the normalized branch distance is bounded by `min(1,δ/κ)`. This strengthens the earlier conservative `min(1,2δ/κ)` without dropping rare or zero-probability branches.

The factor 1 is sharp: ideal and actual branches `(1/4,0)` and `(1/5,1/20)` with identical complementary branch have joint distance `δ=1/20`, ideal branch probability `q=1/4` and normalized distance `δ/q=1/5`. If `q=δ`, an actual branch can have p=0, so a normalized conditional output cannot be guaranteed. [The test](verification/zero_cursor_domain_instrument_review_test.py) checks both controls exactly.

## 4. Existing second clock: a conditional propagation

A distinct semibounded R clock and a specified smeared reduced instrument were **already constructed** in [the second-clock report](ZERO_TWO_WINDOW_SECOND_PHYSICAL_CLOCK.md). Its normalized clock-neutral memory effect and finite-resolution comparison are meaningful progress, but retaining R/φ/cursor poststates and proving a general clock switch are not settled; later [retained-clock](ZERO_RETAINED_CLOCK_INSTRUMENT_AMBIGUITY.md) and [fiber transport](ZERO_CLOCK_FIBER_TRANSPORT_AND_LOST_RECORD.md) analyses further qualify the identification.

For that report's fixed packet, bin and product preparation, retain its stated two-tail bound `τ_B<0.0000177` and reduced-output convention. Substituting the new c_* and the K₂ bound into its clock-smearing inequality, using

```text
σ_B < 0.000316,   ||Ω|| < 3.251,
π < 3.1416,       T_end=π/200+2×10^−6,
r=(T_end+π/100)/2,
```

gives by rational upper arithmetic

```text
(1/2)||C_J−C_L(r)||_diamond < 0.0388.
```

The variance formula implies the σ bound; the Ω bound follows from the spectral interval and π>3. The original τ_B integral bound and the clock-neutral effect/partial-trace construction are **inherited**, not independently rederived here. This conditional result does not include clock-preparation drift, unmodeled implementation error, retained-clock state equivalence or a physical realization of the global Q coupling.

## 5. Verification and remaining work

The rational tests check packet norms/weak endpoint matching, radicals, δ arithmetic, the inherited-tail clock substitution, and sharp classical branch examples. They test the calculations, not the functional-analytic proof by themselves. Existing reader and instrument checks use finite-grid/chiral controls; they do not numerically simulate or establish the full massive-cursor continuum dynamics.

Next: independently audit the R-clock POVM normalization, bin-tail envelope and retained-poststate transport; examine the effects of cursor/preparation perturbations and physical-locality constraints; and connect the clock/readout and subject-incidence constructions on a justified common carrier. None of the bounds proves actual experience, a physical energy zero, or completion of the problem of time.
