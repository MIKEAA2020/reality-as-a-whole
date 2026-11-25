# Structural time and two internal clocks: a stationary sphere comparison

**Constitutive continuation:** [Intrinsic quality and incidence through the same echo](ZERO_ECHO_INTRINSIC_QUALITY_AND_INCIDENCE.md) applies one fixed boundary rule to the actual physical echo and calculates its disagreement with a rival under these clock-reference conditions.

**Source:** Ekarach Chandon and Unyanee Mooksombud, [*Structural Time, Measured Time, and Pre-Field DATA Order*, v1.0](https://doi.org/10.5281/zenodo.21436537), standalone preprint released 19 July 2026. This is the directly deposited companion to the [claim map](https://doi.org/10.5281/zenodo.21428534). I read the standalone DOI version: its central proposals and limits correspond to the companion copy analyzed in [the preceding report](ZERO_DATA_STRUCTURAL_TIME_AND_SPHERE_ECHO.md). The deposited PDFs are not byte-identical—the standalone version includes its own DOI and release date—so they are cited separately rather than described as the same file. Neither document supplies the underlying 326-page Book I, which I have not read.

**New calculation:** [verifier](verification/zero_structural_time_stationary_two_clock_test.py). This is an explicit extension of our existing [20-step sphere and stationary clock](ZERO_PAGE_WOOTTERS_1983_RELATIONAL_SPHERE.md), **not a calculation made by the preprint's authors**.

## Result

The companion's §9 calls for a map from structural history to a physical clock, and asks that it not impose a preferred universal time. Previously we compared the sphere cycle with a reference oscillator using a chosen laboratory parameter. Here is a more internal construction: add a four-state reference clock, correlate it with the **actual sphere-history orbit**, and define comparison effects that commute with the joint cyclic constraint. No external laboratory parameter is needed to state their statistics.

Two equally stationary constructions give different clock comparisons:

* If the reference advances one of its four positions per sphere tick, its reading at sphere tick 10 is **2**.
* If it advances two positions per sphere tick, its reading at tick 10 is **0**.
* Conditioning only on reference reading 2, the optimal guess of the actual B sector from the original echo bit is **3/5** in the first construction and **11/20** in the second. If the original sphere tick 10 is itself available, its echo bit gives B perfectly in either construction.

The second clock is more aliased: it visits only reference positions 0 and 2 at these sampled sphere ticks. The difference is not a mere relabeling of the same clock event. But the reference clock, phase relation and step rule are additional stipulated structure; this is **not a derivation** of their values from zero, the preprint, or the original unmodified echo. Neither construction has established proper time, field dynamics, or a physical subject.

## 1. Source and precise point of contact

The source distinguishes a proposed pre-field **DATA** order from Shannon information or already measurable bits, and structural time from clock readings, entropy and subjective duration. “Pre-field” indicates proposed explanatory priority, not an earlier moment. The paper's five-part grammar—difference, identity, directionality, compatibility and reconfiguration—remains a pre-formal scaffold; its `M_R` clock map and field-emergence map are explicitly research obligations (§§3, 6–9). It says that no new empirical prediction is derived. Its Earth/SP1, SP2 and cosmic-balance proposals are marked as dependent conjectures (§§10–11); nothing below establishes them.

The constructive question for us is narrower: **can two specified clock systems compare their readings through stationary observables while retaining the actual echo statistics?** The answer is yes under the following explicit assumptions. The further question—why one such relation is determined by a self-sufficient zero whole rather than simply selected—is not answered by writing down this example.

## 2. The sphere orbit and the additional reference

Let `U_t` be the actual sphere/record/echo prefix, `U_0=U_20=I`, and let `|ψ⟩` be a normalized initial whole-system vector, including any thermal purifiers. The 20 vectors

`|h_t⟩ = |t⟩_C ⊗ U_t|ψ⟩`, `t=0,…,19`,

are orthonormal because their sphere-clock labels are orthogonal. The original controlled cyclic shift W maps `|h_t⟩` to `|h_(t+1 mod 20)⟩`. This is the real program's **20-dimensional history orbit**, not a claim that all physical degrees of freedom have dimension 20. The 20-step return makes the closing edge valid. For the existing sphere construction and full-system stationary observable definitions, see [Page–Wootters and the sphere](ZERO_PAGE_WOOTTERS_1983_RELATIONAL_SPHERE.md).

Now stipulate an extra reference R with four orthonormal states `|r⟩`, `r∈Z₄`, and shift `V|r⟩=|r+1 mod 4⟩`. For `q=1` or `q=2`, define

`D_q = W ⊗ V^q`,

`|Ω_q⟩ = (1/√20) Σ_(t=0)^19 |h_t⟩ ⊗ |q t mod 4⟩`.

Because `4` divides `20q`, the wrap is consistent and `D_q²⁰=I` on the relevant full clock/system/reference space. Index relabeling proves

`D_q|Ω_q⟩ = |Ω_q⟩`.

Thus the joined state is stationary with respect to this finite cyclic constraint. The extra correlation is a prepared resource and the comparison requires access to R and C; neither is a preexisting privilege of an inhabitant. The construction does not assert a continuous physical rate from `q`: only the specified increment in the **sampled four-state clock**. For example, `V²=V⁻²`, so the sampled half-turn cannot determine its own orientation or how many revolutions happened between samples. To interpret q as a frequency requires a further dynamical/phase-unwrapping prescription.

## 3. Stationary comparison effects

On the history orbit, define the projector for an unaveraged clock pair

`P_(t,r)=|h_t⟩⟨h_t|⊗|r⟩⟨r|`,

and its twirled relational effect

`Q_(t,r) = Σ_(s=0)^19 D_q^s P_(t,r) D_q^(−s)`.

Because each term has a different sphere-clock label, `Q_(t,r)` is a projector, and for fixed t the four `Q_(t,r)` sum to the identity **on this orbit times R**. Also `[Q_(t,r),D_q]=0`. The group average therefore supplies an explicit stationary observable for “what reference reading corresponds to sphere-clock reading t” relative to the chosen phase relation. On the full sphere Hilbert space, extend the event using the controlled shift W and a projector `|t⟩⟨t|_C⊗I_system⊗|r⟩⟨r|`; the same 20-term twirl commutes with `D_q` and gives orthogonal clock-block effects.

The exact result is

`⟨Ω_q|Q_(t,r)|Ω_q⟩ = δ_(r, q t mod 4)`.

Thus `(t,r)=(10,2)` is certain for q=1, while `(10,0)` is certain for q=2. These are relational correlations in two **different specified joint states/constraints**. Changing q changes the actual clock-to-clock relation; simply renaming a coordinate would not change any properly transformed relation. The chosen initial alignment `r=0` at sphere tick 0 is also an input: a shifted phase produces correspondingly shifted readings.

For any sphere-system effect A, the same construction gives a stationary joint effect by twirling `|t⟩⟨t|_C⊗A⊗|r⟩⟨r|` with `D_q`. On `|Ω_q⟩` its expectation is

`δ_(r,qt mod 4) ⟨ψ|U_t† A U_t|ψ⟩`.

This is the finite bridge from the added clock relationship to an actual internal observable. It is an application of the existing stationary-history technique, not a new theorem of physics, and it does not by itself implement the measurement within a confined realm.

## 4. Coarse clock access changes the actual echo prediction

Call the four-state reference reading R, and the original one-bit echo register `r_e`; they are different physical systems. The old `(b,z,s)` probabilities and the thermal reservoir are the actual ones used in the prior reports, not an independently balanced toy ensemble. The verifier uses the exact B–`r_e` laws at all 20 ticks. The reference is deterministic given the sphere tick in `|Ω_q⟩`, and the uniform clock weights determine the following conditional mixtures.

At `R=2`:

* q=1 selects sphere ticks `{2,6,10,14,18}`. Only tick 10 gives perfect echo access to B among these five; the other four give chance-level access. Averaging their **joint** B–echo probabilities and then optimizing the guess gives `3/5`.
* q=2 selects `{1,3,5,7,9,11,13,15,17,19}`. At ticks 9 and 11 the optimal echo-only B guess is `3/4`; at the other eight it is `1/2`. Averaging the joint laws and optimizing gives `11/20`.

These are proper conditional Born probabilities for the stipulated reference readout. For q=2, reference readings 1 and 3 have zero probability, so conditioning on them is undefined, not a zero-probability numerical estimate. The calculation is unchanged for clean and thermal (`q_aux=1/4`) auxiliary preparations. Direct access to the **original clock tick 10** eliminates this particular alias and gives `P_guess(B|r_e,t=10)=1` in both models.

A key nuance is that copying/entangling a new reference to clock histories changes the unconditioned state. Tracing out R dephases some off-diagonal clock-history coherences: in the history-orbit basis, entry `(t,u)` survives exactly when `q(t−u)=0 mod 4`. It is not legitimate to assert that the unconditioned original coherent history remains unchanged. Conditional on a specified original clock tick, the sphere-system state is still `U_t|ψ⟩`. Our aggregate law uses the stated reference and original clock projectors; it is not a hidden off-surface experience or an assertion that a confined observer automatically sees global records.

## 5. Why this matters for zero's constitution

The comparison strengthens the constructive side of the earlier clock analysis: records and measured relations can be exhibited as stationary, relational effects **inside** a larger constrained whole. It also pinpoints the remaining selection question. With the same original sphere prefix and actual signed/record structure, both q values are mathematically compatible; zero has not yet been shown to select either, nor a unique corresponding unit or physical clock.

A no-residue account must therefore do more than assert that “time manages DATA”: its constitution must explain which histories and reference relations exist, how physical clock rates and access are fixed, and how intrinsic experience and its measure belong to these relations. It may be that a stronger, self-sufficient zero constitution does so; this finite example neither rules that out nor derives it. Its gauge-style stationary constraint is not automatically cosmic energy, and the echo B sign is not established as felt valence. Any signed experiential balance must concern actual felt contributions, not erase suffering by changing a record or calling its absence negative.

The work remains compatible with no externally preferred foliation. It also does not claim that four-state clocks recover the metric, proper-time dilation, quantum field theory, or the authors' specifically Earth-centered conjecture. Those require additional constructive correspondences and independent evidence.
