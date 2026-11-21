# How selective must a physical mismatch intervention be?

## Result and limits

The [previous four-spin measurement gate](FOUR_SPIN_PHYSICAL_MISMATCH_MEASUREMENT_GATE.md) showed that passive observations can identify a **net** pair preference in its restricted model while failing to identify a particular hidden channel's preference. It gave an ideal intervention that distinguished two stipulated channel decompositions. This gate allows that intervention to be imperfect.

In a specified conditional equilibrium model, let `Δ` be the change in the dimensionless net pair coupling between baseline and treatment, `λ>0` the fraction of a target channel attenuated, and `b` an independently justified upper bound on the absolute change of all residual pair couplings. Then the target channel's sign is identifiable whenever **`|Δ|>b`**. If measurement supplies only a simultaneous interval `[L,U]` for Δ, the corresponding sufficient conditions are `L>b` for a positive channel or `U<−b` for a negative channel. A lower bound on λ is not needed for the sign, but is needed for a finite upper bound on its magnitude.

We apply this to the same four-spin A/B models and calculate hypothetical, finite-sample uncertainty intervals. We also construct two opposite-sign target channels with **identical** baseline and intervention observations when residual drift can be as large as the observed contrast. These are model calculations, not a real selective intervention or an empirical measurement of q, discomfort, or a subject. The mathematical facts about Ising odds ratios, partial identification and concentration are standard; their use here is a conditional construction for this project's particular interface.

## 1. Two models, two interventions, one definition of selectivity

Condition on independently fixed external spin values `(s₂,s₃)`. In each gate condition suppose the joint distribution of `s₀,s₁∈{−1,+1}` has the conditional form

```text
P_g(s₀,s₁ | s₂,s₃) ∝ exp[ J_g s₀s₁ + h_{0,g} s₀ + h_{1,g} s₁ ],
```

where `g=0` means baseline and `g=1` means intervention. Fields may change across conditions and depend on the fixed external context; the binary pair interaction is entirely in `J_g`. The coefficients are dimensionless relative to the stipulated equilibrium scale. A shared reference convention for spins must be fixed; re-encoding one spin reverses both the sign and the interpreted preference.

Define the conditional cross-product odds ratio

```text
O_g = P_g(++ ) P_g(-- ) / [P_g(+- ) P_g(-+ )],
J_g = (1/4) log O_g,             Δ = J₀ − J₁.        (1)
```

The normalizer and the single-spin fields cancel. Equation (1) is algebraic under the stated distribution and known assignments of the four states. Hidden inputs that generate higher-order or condition-specific effective pair interactions are *not* eliminated by this cancellation. Changing a physical energy scale, preparation, context, state labeling, temperature or sensor across arms may also invalidate the interpretation of Δ as an intervention on one stable channel.

Decompose the baseline pair coupling into the **designated target** `J` and residual `R₀`; after intervention, assume

```text
J₀ = J + R₀,       J₁ = (1−λ)J + R₁,
Δ = λJ + δ,        δ = R₀ − R₁,       |δ| ≤ b.       (2)
```

`0<λ≤1` is attenuation of that *same target component*; `b` bounds all intervention-induced residual effective-coupling changes in the same coefficient units. Changes of one-body fields are already handled by the conditional odds, but unmodeled pair interactions, hidden-state responses, interaction misspecification and systematic instrument shifts need explicit bounds. The bound is not obtained by assuming away cross-talk or by naming the manipulation selective. This algebra is also not a claim that residual pair components are independently real; identifying the designated channel is itself a physical obligation.

## 2. Exact sign and magnitude implications

From (2), if `|Δ|>b`, the sign of `λJ=Δ−δ` must equal the sign of Δ; since `λ>0`, this is the sign of J. With a valid interval `[L,U]` for Δ, use `L>b` or `U<−b`; otherwise return unresolved unless further constraints exclude alternatives. Positive J prefers `s₀s₁=+1`; negative J prefers `−1`, within this target-channel cost convention. If J is zero there is no unique preferred sign.

If `0<λ_lo≤λ≤λ_hi≤1`, the admissible target-coefficient interval is

```text
[min S, max S],   S = { (d−r)/l : d∈{L,U}, r∈{−b,b}, l∈{λ_lo,λ_hi} }.  (3)
```

The formula follows because the numerator ranges from `L−b` to `U+b` and the denominator is positive; its extrema occur at endpoints, including when the interval crosses zero. It is sharp **given only** these independent interval restrictions and no additional joint constraints. If calibration imposes correlations between λ and δ, or physical models constrain the parameters, a joint admissible set can narrow it. If λ may approach zero and no independent upper bound on `|J|` exists, a finite magnitude interval generally cannot be inferred, even when its sign is fixed. For example, with exact `Δ=1` and `δ=0`, choices `λ=1/n`, `J=n` have identical Δ for all n.

As in the [continuous-phase gate](SELECTIVE_CHANNEL_CERTIFICATE_AND_HARMONIC_ALIAS.md), statistical confidence and systematic/model uncertainty are separate. A high-precision Δ alone does not bound b, λ, hidden inputs or the adequacy of the target decomposition. No calculated mismatch is thereby an experience.

## 3. Apply the imperfect gate to the existing physical rivals

In the original four-spin model the passive outer-edge factor is `1+x/2` for `x=s₀s₁`. Since `atanh(1/2)=log(3)/2`, its effective baseline coupling is `J₀=log(3)/2`, and its conditional odds are `O₀=9`.

For the ideal channel-removal operations specified in the preceding audit:

| Model | Designated target J | Net coupling after gate J₁ | `O₁` | Exact `Δ=J₀−J₁` |
|---|---:|---:|---:|---:|
| A: alignment target, no parallel residual | `log(3)/2` | 0 | 1 | `log(3)/2` |
| B: antialignment target, parallel alignment residual | `−log(3)/2` | `log(3)` | 81 | `−log(3)/2` |

The two passive laws and kernels coincide, but *if their specified target is selectively removed and the remaining channel is unchanged*, the gated conditional odds are different. These ideal gated systems are mathematical controls; they are not claimed to be attainable neural manipulations. Even a perfectly measured nonzero intervention effect does not prove that the target alone changed.

### Hypothetical sampling and imperfect gate

Suppose, separately for each of the A and B comparisons, an experimenter obtains `n=7,360` independent, identically distributed observations **per arm within the fixed external-spin stratum**, with correctly measured pair states. Pretend the observed four-cell frequencies `(++,--,+-,-+)` happen to equal the following exact model probabilities:

| Arm | Four frequencies |
|---|---|
| baseline | `15/32, 9/32, 3/32, 5/32` |
| A gated | `5/16, 3/16, 3/16, 5/16` |
| B gated | `9/16, 27/80, 3/80, 1/16` |

These are **invented observations**, not a dataset; n is chosen so all displayed frequencies correspond to integer counts. A and B are alternative analyses, not three empirical arms on the same physical system. With simultaneous per-cell error `ε=0.02`, Hoeffding's inequality and a union bound over the eight arm/cell indicators give failure probability at most

```text
16 exp(−2nε²) ≈ 0.04436.
```

Indicators of different cells in an arm are dependent; the union bound does not require their independence. Independence and stationarity **within each arm**, prespecified stratum, complete state classification and correct conditional sampling are essential. No independence between arms is needed for that particular union bound. The stated confidence coverage concerns the two-arm experiment under these assumptions; it is not a posterior probability for the parameter, and it does not cover uncertain model correctness or systematic error. Real gate assignments can alter stratum membership; conditional comparisons then require a valid sampling/selection argument and are not automatically randomized causal effects.

For each arm, a conservative odds interval comes from putting `p̂−ε` in both numerator terms and `p̂+ε` in both denominator terms for the lower endpoint, and vice versa for the upper; all bounds are positive in this example. Combining both arms and applying (1), suppose **additional independent physical justification** supplies `|δ|≤0.1` and `0.8≤λ≤1`. The resulting illustrative sets are:

| Comparison | Simultaneous Δ interval | Target J interval under the additional gate assumptions |
|---|---:|---:|
| A baseline vs gate | `[0.3559, 0.7567]` | `[0.2559, 1.0709]` |
| B baseline vs gate | `[−0.9672, −0.2269]` | `[−1.3340, −0.1269]` |

Both intervals correctly include their respective ideal target `±log(3)/2` and exclude zero. The endpoint construction is conservative: it ignores normalization and possible dependencies between the cell probability bounds. The 95.56% simultaneous sampling guarantee holds only under its stated assumptions; if the b and λ bounds are themselves confidence statements, use their **joint** coverage as well, rather than multiplying or ignoring error probabilities. This is not a power calculation, a clinical recommendation, or evidence that a real device has `b=0.1` or `λ≥0.8`. Larger b or statistical error can erase the sign certificate.

## 4. An intervention can look decisive while the channel stays ambiguous

Consider an exact separate control with `J₀=1/2`, `J₁=1/5`, `Δ=3/10` and `λ=1`. Both decompositions below give the **same net coupling in both gate conditions**, and hence the same stipulated full equilibrium laws and same corresponding heat-bath dynamics when all other terms are held fixed:

| Model | Target J | `R₀` | `R₁` | `δ=R₀−R₁` |
|---|---:|---:|---:|---:|
| A | `1/2` | 0 | `1/5` | `−1/5` |
| B | `−1/10` | `3/5` | `1/5` | `2/5` |

Both respect `|δ|≤2/5`. Their designated target signs are opposite although the physical records under these two conditions are identical. The treatment changes the residual pair term in both; that is precisely the confound. A positive Δ means the **net** coupling falls, but with only this wide residual allowance it does not tell us whether the designated target was alignment- or antialignment-preferring. This is a constructive ambiguity in a declared model class, not an impossibility claim for all interventions. Independently bounded residual drift below `3/10`, a more selective gate, or an additional valid channel-specific measurement would exclude at least one such construction.

The two models use different hidden target/residual decompositions, but each gives the same full on/off observable distributions under the stated common remaining factors. A measurement that directly accesses the target constituents could distinguish them. Different unmeasured models, interaction changes or selected samples may remain even after this particular counterexample is ruled out.

## 5. What is required before an affect test

1. Fix the physical target, component identity, sign convention, time scale and candidate subject independently of held-out affect ratings. Decide whether the law concerns a net interaction, one physical channel, state excess, or structural frustration; they are not interchangeable.
2. Validate the measurement model and the gate: characterize attenuation, residual pair-coupling drift, hidden/common inputs, sensor leakage, non-equilibrium, state-selection and changing interactions. Separately justify simultaneous uncertainty on model inputs; a sham alone may not bound all cross-talk. If `L≤b` and `U≥−b`, stop or report an identified set rather than assign a sign.
3. For any real-person research use only ethically reviewed, safe, consensual interventions and predefined stopping rules. No specific painful or invasive procedure is recommended here. A hypothetical large n is not a feasibility estimate.
4. Only after physical identification, use the separately anchored first-person contrast and uncertainty requirements in the [assay gate](HISTORY_MISMATCH_FIRST_PERSON_ASSAY_ERROR_GATE.md), with independent calibration and held-out tests. Assignment effects do not automatically identify a causal effect of q after conditioning on its measured history.
5. Successful prediction or intervention could constrain a particular operational bridge, but does not by itself derive why any physical configuration is felt, establish subject boundaries, or choose experiential over neutral grounding. Failure of this particular certificate does not imply absence of experience or refute all mismatch theories.

## Reproduction and status

Run `PYTHONPATH=verification python verification/imperfect_channel_gate.py` and `PYTHONPATH=verification python -m unittest imperfect_channel_gate_test`. The [receipt](verification/imperfect_channel_gate.json) records exact conditional odds, the counterexample, hypothetical intervals, and 729 rational-grid containment checks of (3). The analytic bounds hold under the specified premises; these tests do not certify the premises, identify a human channel or validate the full framework. B4–B5/F2, B9/F3 and B10 remain open; C3 remains **full structural and experiential intelligibility**, jointly with C1–C7.
