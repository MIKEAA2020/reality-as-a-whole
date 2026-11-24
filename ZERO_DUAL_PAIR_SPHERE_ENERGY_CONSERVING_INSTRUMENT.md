# Dual pairing, sphere probabilities and an energy-conserving relative-clock interface

## Result

The preceding [sign-pairing construction](ZERO_NECESSARY_PLENITUDE_SIGN_PAIRING.md) suggested that one zero whole might be constituted by dual contributions. Here we test that idea against a concrete physical interface rather than simply writing `+E−E=0`.

We construct a finite quantum system with:

* the **same five-ray sphere weights and singlet** used in our earlier conservation–record construction;
* two internally paired reference/clock systems, each initially in a finite identity-pair state;
* separate, explicit energy-conserving instruments for the sphere POVM and the other spin readout; and
* a third, energy-conserving **relative-clock pointer** whose outcomes can be compared with the two readouts.

The initial whole and the complete post-instrument state lie **exactly in the zero eigenspace** of the model's declared total energy operator. The internal apparatuses exchange energy while the total remains zero. For four-level references, an explicitly accessible nonzero-probability relative-clock window preserves the sphere weights `(1/8, 2/5, 19/40)` and yields a detailed joint table within total-variation distance **0.09321** of the earlier ideal table. The deviation is computed, not waved away.

The reference pair is doing real work: if its partner clock is ignored, the directional correlations disappear, even though the local sphere-outcome weights stay the same. A **joint** relative-clock measurement recovers them without invoking an external phase reference. That joint interface is an explicitly modeled operation, not automatic access for either local inhabitant.

This is a construction under specified finite-dimensional quantum assumptions. The negative energy contributions and initial identity pairs are chosen, not derived from zero; they are not shown to be gravitational energy. The model does not contain the recollapsing oscillator, the earlier four-qubit work/current register, actual subjects, or phenomenal valence. It also does not derive the Born rule or observed outcomes.

Verification: [verification/zero_dual_pair_sphere_energy_instrument_test.py](verification/zero_dual_pair_sphere_energy_instrument_test.py).

## 1. The sphere data and the two dual pairs

Use the prior five-ray construction's three weights and center-frame directions:

```text
q = (1/8, 2/5, 19/40),
n₁=(1,0,0),
n₂=(1/2,√3/2,0),
n₃=(−13/19,−8√3/19,0),
Σ qᵢ=1,          Σ qᵢ nᵢ=0.
```

The ideal Alice effects are `Fᵢ=qᵢ(I+nᵢ·σ)`. They sum to I and are rank one. The same asymmetric weights were obtained from the specified five-ray conservation configuration in [the earlier construction](ZERO_SPHERE_CONSERVATION_RECORD_CURRENT_SINGLE_SYSTEM.md). Here that ray geometry and its instrument are inputs, not consequences newly derived from zero.

Begin with the actual logical-qubit singlet

```text
|Ψ⁻⟩_AB = (|01⟩−|10⟩)/√2.
```

It is a local-unitary form of the qubit identity-pair state. Let `P=|1⟩⟨1|`, choose `H_A=P` and `H_B=P−I`. Then

```text
(H_A+H_B)|Ψ⁻⟩=0.
```

For each laboratory introduce an L-level reference R and clock C, with `N|n⟩=n|n⟩` and the identity pair

```text
|Φ_L⟩_RC = (1/√L) Σ_(n=0)^(L−1) |n⟩_R |n⟩_C,
(N_R−N_C)|Φ_L⟩=0.
```

The initial state is the product of the singlet and the two reference/clock pairs, with readout pointers blank. All pointers are chosen energy-degenerate. With unit energy spacing, the declared whole operator is

```text
H_tot = H_A + H_B
      + N_RA − N_CA + N_RB − N_CB.
```

Each pair has exact zero energy in the initial state, so `H_tot|Ω_initial⟩=0`. These are **prescribed signed terms** in a finite model, not empirical measurements of cosmological positive and negative energy. The negative spin and clock terms, energy reference, pairing and dimensions are physical assumptions of the model.

## 2. What an exact conservation law demands of the interface

An ideal sphere effect generally does not commute with `H_A=P`: it distinguishes directions transverse to the energy axis. There is a useful general restriction. If an apparatus starts in a state commuting with its energy, its pointer commutes with apparatus energy, and its interaction exactly conserves `H_A+H_apparatus`, then each induced effect on A commutes with `H_A`. This follows by applying a common energy-phase rotation, using invariance of the apparatus state and pointer, and tracing out the apparatus.

So a noncommuting directional effect needs a suitable **physical reference or a changed assumption**; writing down the desired POVM is not yet its energy-conserving implementation. Our paired reference supplies relational coherence: the whole is energy-stationary, but a reference conditioned on its partner's phase can be coherent in energy. There is no contradiction with the restriction, because the clock-conditioned reference is not an energy-diagonal standalone state.

### The joint effects

For the Alice reference ladder `n=0,…,L−1`, the total `H_A+N_R` has sectors `m=0,…,L`. For `1≤m≤L−1`, use the two-dimensional basis

```text
|0,m⟩, |1,m−1⟩.
```

Define joint effects `Mᵢ` to be the 2×2 matrix Fᵢ on every such interior sector. On the one-dimensional edge sectors use the corresponding diagonal entry of Fᵢ. Then

```text
Mᵢ≥0,       ΣᵢMᵢ=I,       [Mᵢ,H_A+N_R]=0.
```

The reference's phase-conditioned vector is

```text
|r(t)⟩ = L^(−1/2) Σ_n e^(int)|n⟩.
```

It arises by applying the normalized phase POVM of the paired clock, not by assuming an external t. At t=0 the induced A effects have the **same diagonal entries** as Fᵢ, and their off-diagonal entries are reduced by

```text
η_L = (L−1)/L.
```

For the present equatorial directions this is simply

```text
Fᵢ^(L)(0)=qᵢ(I+η_L nᵢ·σ).
```

At general phase t the transverse direction is rotated by t. The effect of the two edge sectors is included exactly. For finite L the effects are unsharp; `η_L→1` is a mathematical refinement of this particular family, not a claim that a physical apparatus of infinite size exists or that this family achieves a universal optimal bound.

Apply `√Mᵢ` coherently and write its label in a degenerate pointer. The roots commute with the same total energy, and the isometry can be completed to a unitary **within each energy sector**. The tests explicitly construct such unitary completions. The second laboratory uses the same procedure for its `±` spin effects. Thus these are energy-conserving interactions, not an externally stipulated sequence of nonconserving projections.

## 3. Exact zero survives a nontrivial interaction

After both readout isometries, the full state—including both reference systems, both clocks and both pointer registers—still obeys

```text
H_tot |Ω_after⟩ = 0.
```

This is exact at the specified finite dimensions. **The original pairs need not remain individually at zero:** the interactions can transfer energy between the spin pair and reference pairs. Define

```text
D_spin = H_A+H_B,
D_refs = (N_RA−N_CA)+(N_RB−N_CB).
```

In the full output `D_spin+D_refs=0` component by component. For L=4, the probabilities for `D_spin=−1,0,+1` are respectively

```text
0.211875,   0.576250,   0.211875.
```

On each component the total reference mismatch is the exact opposite. This is a genuinely dynamical example of **reallocated internal balance** rather than two static numbers cancelling. These are quantum energy-readout probabilities; they do not by themselves assert that all outcomes are separately actual experiences.

## 4. The joint record table, and a clock that is itself an internal interface

Bob's original measurement axis is

```text
b=(−1/5, 2√3/5, 2√3/5).
```

The ideal table from the prior sphere construction is

| sphere outcome | Bob + | Bob − |
|---|---:|---:|
| 1 | 0.075000 | 0.050000 |
| 2 | 0.100000 | 0.300000 |
| 3 | 0.325000 | 0.150000 |

For L=4 in **both** laboratories and zero relative phase, both instruments have visibility 3/4. The effective correlation visibility is `(3/4)²=9/16`, giving

| sphere outcome | Bob + | Bob − |
|---|---:|---:|
| 1 | 0.069531 | 0.055469 |
| 2 | 0.143750 | 0.256250 |
| 3 | 0.286719 | 0.188281 |

The row sums remain exactly `(1/8,2/5,19/40)` and the Bob marginal remains `(1/2,1/2)`. The total-variation distance from the ideal table is `0.0875`. For equally sized L-level references it is exactly

```text
TV = (1/5)[1−(1−1/L)²].
```

For example it is 0.15 at L=2 and 0.046875 at L=8. These are errors for this specified protocol and table, not universal accuracy limits. The ideal table does not itself establish a selected outcome, actual subject or experiential frequency.

### Comparing clocks without a third external clock

Two separate sharp clock-phase readings would themselves require an implementation and could introduce an external phase reference. Instead, we use a **joint relative phase POVM** of the two clocks. Average their two phase effects over the common phase. Its density has nonzero matrix elements only when

```text
n_A+n_B=m_A+m_B,
```

so it commutes with `N_CA+N_CB`, and hence with the clock contribution to H_tot. It measures the relative phase, not an absolute phase. Its effects can be square-rooted within fixed total-clock-energy sectors, and written into a degenerate pointer by an isometry which preserves H_tot. The tests apply this third isometry to the complete post-readout state and verify exact zero energy again. A finite unitary completion exists sector by sector. This is an explicitly **joint clock interface**; no claim is made that a confined observer has access to it.

For L=4, use 16 equally spaced relative-phase pointer labels. The discrete POVM is normalized and each label has probability 1/16. A label is an outcome of an unsharp POVM, **not** a perfectly sharp phase. Grouping the three labels around zero gives an operational finite window with probability `3/16`; its conditional table is

| sphere outcome | Bob + | Bob − |
|---|---:|---:|
| 1 | 0.069174 | 0.055826 |
| 2 | 0.146605 | 0.253395 |
| 3 | 0.284221 | 0.190779 |

Its distance from the ideal table is approximately `0.093209`. The additional visibility factor is `(1+2cos(π/8))/3≈0.949253`. This finite-window result requires no selection of a measure-zero clock value and includes the relative-clock pointer in the zero-energy accounting.

When the clock information is ignored altogether, the two output pointers have joint probabilities `qᵢ/2` for each Bob sign. Their separate weights persist, but the directional correlation vanishes. This difference is a conditional correlation, not a signal that one setting controls Bob's local distribution. The relative phase depends only on the difference of the clocks' readings; a common phase shift changes neither table. This is a finite relational construction, not a derivation of relativistic spacetime or a preferred universal foliation.

## 5. No-signalling, access and experience

For the one-reference construction, we explicitly compare the full density matrix of Bob plus Alice's partner clock after Alice uses either the pair or the triple instrument. It is exactly `I/(2L)` in both cases. In the two-reference construction we also retain **Bob, both clocks, Bob's reference and Bob's pointer**, while discarding Alice, her reference and her pointer: the complete retained density matrix is identical for the pair and triple settings. This follows from the local nonselective operation, and the tests check full marginals, not just average spins. Thus no measurement on those retained factors can distinguish Alice's choice in this specified tensor model without Alice's result.

The **joint** two-clock comparison used above is a richer interface. It need not be locally available to either putative subject, and there is no spacelike embedding or faster-than-light claim here. Conditional tables must not be mistaken for independent local access to the other party's setting. The earlier [subject-boundary and report-causality result](ZERO_SUBJECT_BOUNDARY_REPORT_CAUSALITY.md) remains a constraint on any proposed experiential reporting law.

The construction does not create or prove a subject. It makes a specific connection between a zero-energy paired whole, an internally relational reference, and the physics of a sphere-record interface. It does not show why a given registered difference is **felt**, which differences are pleasure or suffering, or how actual experiential incidences are paired. A negative felt quality, if present, remains locally real; a balanced whole cannot be used to erase it.

## 6. What this contributes to the zero–plenitude proposal

The constructive gain is that **the sign-paired state can fund an actual conservation-respecting interface**. Local direction-sensitive readouts do not have to violate the model's zero energy or use a literal external clock. Their accuracy and their dependence on the relative interface can be calculated. The internal imbalance after interaction is itself exactly balanced by the reference mismatch.

It is not yet a derivation from zero alone:

* The two identity pairs, the qubit singlet, the energy spectrum and signs, the sphere geometry and its POVM, the finite dimensions and the unitary interactions are specified.
* The Born rule is used to calculate effects and tables. Equal identity-pair weights or geometric POVM coefficients do not, by themselves, derive actual incidence, unique outcomes or the Born rule from necessary plenitude.
* The negative clock/spin terms and the zero reference are not derived gravitational energies. The exact finite operator zero is a mathematical feature of this model, not a theorem about our universe's global energy.
* The physical measurement of a relative phase uses a joint clock interface. Its accessibility, stability and a relativistic realization would need to be established, without assuming a preferred foliation or that realm inhabitants register inaccessible activity.
* The present construction retains the earlier sphere **input** and geometric weights, but does not include its original work/current registers or the later recollapsing geometry. Their coupling to this energy-conserving instrument is a further model, not a result claimed here.

The next consequential step is to put the **actual record–work K relation and its memory** behind this conservation-respecting interface, then determine which record/sign relations remain accessible with a finite reference. That would let the proposed experiential pair be tested against energy balance, internal time and full-coupling report causality in the same system. A successful zero constitution would still have to determine the paired state, interface and real incidence rather than leave them as separate unexplained inputs.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_dual_pair_sphere_energy_instrument_test -v
```

The tests verify the actual five-ray qubit effects and singlet, positive energy-block POVMs, explicit unitary completions, exact global zero before and after both local instruments and the relative-clock pointer, the analytic visibility/table error, the finite clock window, relative rather than common-phase dependence, and the no-signalling marginal. The results assume ordinary quantum mechanics and the declared finite model; they do not establish cosmological global energy, subjectivity, irreversible records or a continuum quantum-gravity limit.
