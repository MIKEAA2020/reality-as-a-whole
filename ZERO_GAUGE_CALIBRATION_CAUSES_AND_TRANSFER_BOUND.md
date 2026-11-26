# Why trust calibration? Selection, shared causes and a conditional transfer bound

## Result

The [previous why-chain](ZERO_GAUGE_CLOCK_CAUSAL_CHAIN_AND_CALIBRATION_ROOT.md) showed that a source–detector correlation can be mimicked by a contextual sign error. This pass follows that issue deeper rather than assuming better calibration automatically solves it:

- A **shared cause** can produce that contextual error without a direct signal from the C detector to the B detector. Locality or no direct cross-talk alone does not establish source–apparatus independence.
- A **sign-dependent clock selection** can create the same accepted correlation even with independent sign errors and an uncorrelated source. In an explicit example, its rejected records differ sharply from the intended model, making rejected-record readout a useful control when that readout itself is trustworthy.
- A four-context calibration gives an explicit finite-shot interval for the **preselection** true-sign correlation, tolerating arbitrary correlated sign readout, bounded reference contamination, source–reference mismatch, clock-selection bias, blank response and uncertainty in the written fraction. It is a conditional theorem, not a demonstration that those bounds hold in a real apparatus.
- Even perfect calibration of all four labels cannot establish source–reference transfer if a hidden apparatus mode differs systematically between calibration and source runs. More calibration shots cannot repair an untested transfer assumption.

These are specified statistical models of the commuting recorded-sign outcomes, not data or an implemented sensor. Code: [causal controls and bound](verification/zero_gauge_calibration_causal_controls.py); [focused tests](verification/zero_gauge_calibration_causal_controls_test.py).

## 1. Why might the contextual error arise?

The earlier rival has fair independent true signs `b,c`, independent C flips of probability `p_C`, and `P(B flips | b,c)=p_B+a bc`. Its B error depends on the joint context, but that is a conditional distribution, not by itself a causal explanation.

One explicit causal realization is a common-past variable `Λ=(u,v)` consisting of independent fair signs. The source produces `b=u,c=v`. The B-side apparatus also receives `v` from Λ and flips B with probability `p_B+a b v`; C uses its independent flip coin. Then `b,c` are uncorrelated as observed source signs, yet the B apparatus has information correlated with c. There is no direct C-to-B signal in this stipulated causal graph. The output law is exactly the prior rival's law. The shared variable is an **assumption of the counterexample**, not evidence of an actual hidden cause.

Direct cross-talk is another possible causal route; a common power/control environment, preparation history, memory, or conditional selection could also correlate errors and source. Preventing communication between readout locations can exclude some pathways but not a common past or common control. Conversely, randomized, independently selected reference signs and interleaved calibration can test some such correlations—provided the randomization is actually independent of relevant device/environment variables and the source runs are represented by the calibration conditions. Randomization is a physical protocol with dependencies, not a magic proof of independence.

## 2. Why check the clock selection separately?

Even with independent fixed sign-flip channels, conditioning on a clock outcome can induce correlation. Consider written true signs initially independent and fair, and replace the clock response by the alternative instrument

```text
P(Y=late | b,c,written) = r(1+s bc),
```

with valid probabilities. Its average late rate is r and its late rate conditional on **either one** of b or c alone is also r. Yet

```text
E[bc | late,written]  = s,
E[bc | early,written] = −r s/(1−r).
```

With independent flip gains `g=(1−2p_B)(1−2p_C)`, the observed product means are these expressions times g. Take `r=.9`, `s=2(.8)/81`, `p_B=.05`, `p_C=.1`. Then the two joint-context late rates are `.91777778` and `.88222222`; the observed written product means are

```text
late:  +0.01422222       early: −0.12800000.
```

The accepted written two-sign table exactly matches the prior correlated-source example, and the average clock rate remains `.9`. If the prewrite clock and blank behavior are unchanged, the accepted table including blanks also matches. This is a **different** clock instrument from the prior sign-independent `K_late`; it introduces a sign-dependent selection path. It can be realized as a classical response to pre-existing jointly recorded signs, or as a corresponding diagonal effect, but no spatially local realization is supplied.

In the original source model, clock acceptance is sign-independent, so the written early and late product means both equal `+0.01422222`; they differ in the alternative. Measuring rejected as well as accepted written records would therefore distinguish these *two* specified mechanisms if the comparison uses valid, comparably calibrated readout. Other contextual errors could also alter rejected records, and reading them may itself require a different instrument. Averaged acceptance and single-sign checks miss this particular bias; a joint-sign, clock-outcome test is needed. Postselection cannot be silently equated to an unbiased sample of the source.

## 3. Four-context robust bound

This bound concerns a well-defined pre-readout pair of commuting recorded-sign labels `b,c∈{±1}` on written records. For a general quantum device, the existence of a suitable instrument and its reduction to this classical conditional-response description must be justified; it is not automatic for arbitrary coherent errors. Let `z=E[bc | written before clock selection]`, `w=P(written | late)`, and let `X` be the actually reported product in the late ensemble. Assume

1. The accepted data are iid, with `X∈[−1,1]`; `M` accepted shots give `X_bar`.
2. In each of the four intended written reference contexts `(b,c)`, gather `m_bc` accepted iid records and measure the sample product mean `h_hat_bc`. Let `h_ref_bc` be the corresponding ideal **correct-label subpopulation** response. At most an independently justified fraction `e` of accepted reference records have an incorrect intended label, and the correctly labeled subpopulation has response `h_ref_bc`. This last condition rules out unmodeled selection of unusually responsive correct references.
3. For each context, the accepted-written source response `h_src_bc` may have arbitrary correlated B/C errors but differs from `h_ref_bc` in mean by at most `τ`. This includes relevant environment and selection differences **only if** the asserted bound covers them. It is not established by the four calibration means themselves.
4. The total-variation distance between the preselection and late-selected **written true-sign distributions** is at most `σ`. An independent bound supplies `w∈[w_L,w_U]`. On a late-selected blank, the absolute mean of X is at most `b_0`. In the old instrument, perfectly recognized blank gives `b_0=0`; here nonzero blank response is allowed.

Choose a positive comparison gain `g≤1` in advance. It can be the prior nominal `(1−2p_B)(1−2p_C)`, but need not equal the actual detector gain; deviations are included in the four measured responses. Define

```text
γ_hat = max_bc |h_hat_bc − g bc|,
R_cal = sqrt[2 log(8/δ_cal) / min_bc m_bc],
D = min[2, γ_hat + R_cal + 2e + τ],
R_data = sqrt[2 log(2/δ_data) / M],
B = (1−w_L)b_0.
```

The four-way union bound for bounded `[-1,1]` outcomes gives `|h_src_bc−g bc|≤D` simultaneously with probability at least `1−δ_cal`, given the contamination and transfer premises. The factor `2e` is the maximum mean change from an e fraction of arbitrary `[-1,1]` contaminants. Separately, `|X_bar−E[X|late]|≤R_data` with failure probability at most `δ_data`. The two events need not be independent for their union bound.

Let `A_−=X_bar−R_data−B`, `A_+=X_bar+R_data+B`. If `w_L>0`, on the joint event,

```text
z_lower = max{−1, [min(A_−/w_L,A_−/w_U) − D]/g − 2σ},
z_upper = min{+1, [max(A_+/w_L,A_+/w_U) + D]/g + 2σ}.
```

If `w_L=0`, return the trivial interval `[−1,1]`. An empty interval is an incompatibility warning for the assumptions and the confidence event, not an estimate. The reason for the endpoint minimum/maximum is that the unknown w lies in the interval and the sign of A need not be known. The selection term follows from `|E_P[bc]−E_Q[bc]|≤2 TV(P,Q)`. The guarantee has failure probability at most `δ_data+δ_cal`, **conditional** on the external bounds e, τ, σ, w and `b_0`. If any are themselves inferred statistically, their failure probabilities must also be added; if they are unjustified, the nominal coverage is not established.

This estimates a recorded-sign correlation, not the full angular–holonomy state. For the original `ρ_ε` family, independent sign instruments and sign-independent preselection, `z=λκ 2ε/81`. A sign conclusion for ε additionally requires that family, the correct preselection definition and positive `λκ`; an interval for ε needs their calibration uncertainty propagated. A positive z by itself need not have that source-family interpretation.

### Numerical illustration, not an experiment

Reuse the prior **simulated** `X_bar=.01769` from 100,000 accepted records. Separately suppose four **hypothetical** calibration batches each contain 1,000,000 accepted records. Let the positive-product counts be 860,000 when `bc=+1`, and 140,000 when `bc=−1`, giving exactly `h_hat_bc=.72 bc`. Set

```text
g=.72, δ_data=δ_cal=.025, w∈[.993,.995],
e=.0005, τ=.001, σ=.0002, b_0=.005.
```

Then `R_data≈.00936165`, `R_cal≈.00339656`, `D≈.00539656`, `B=.000035`, and

```text
z ∈ [0.003681, 0.045781]     (conditional 95% joint event).
```

This illustrative interval is positive, but needs four million **accepted reference** records and separately justified systematic limits at or below the stated levels. The calibration counts and bounds are not actual observations, and the data example was not obtained from a single end-to-end simulation incorporating all these imperfections. When the transfer bound is unavailable, use the trivial `τ=2`; for these same counts the interval becomes `[−1,1]`. More shots do not remove a fixed unknown transfer discrepancy.

## 4. Where could those bounds come from?

A concrete sufficient route for τ makes the missing physical content visible. Suppose for each accepted written context there is a normalized environment/reference state `ρ_ref,bc` or `ρ_src,bc` and a bounded self-adjoint output-product operator `D_bc` with `||D_bc||≤1`. If the source and reference effects are `D_src,bc` and `D_ref,bc`, then

```text
|h_src,bc−h_ref,bc|
 ≤ 2 T(ρ_src,bc, ρ_ref,bc) + ||D_src,bc−D_ref,bc||,
```

where `T=½||ρ_src−ρ_ref||_1`; use at most 2 for the resulting τ. This follows by adding and subtracting `Tr(D_src ρ_ref)` and applying trace-norm duality. It is useful only if the **conditional** states and effects, including clock selection and environmental correlations, have independently justified uniform bounds. Measuring a few reference outputs does not by itself certify their trace distance from the source environment or the operator norm on untested modes. The related [support-flag analysis](ZERO_TWO_WINDOW_IMPERFECT_SUPPORT_FLAG_ROOT.md) gives an explicit hidden-direction example of that problem.

Similarly, if the true written late-acceptance probabilities satisfy `0<r_min≤r_bc≤r_max` for all four contexts in the source ensemble, then

```text
σ ≤ min[1, (r_max−r_min)/(2 r_min)].
```

This conservative inequality comes from `P_late(b,c)=P_pre(b,c)r_bc/E_pre[r]`. To use calibration to assert those source rates, its labels and acceptance must themselves be reliable and transferable. For the selection example, the joint rates differ even though every single-sign average is `.9`. Use rejected records, joint-context references, randomized settings and independent clocks as controls, but explicitly account for their own disturbances and calibration; none individually proves the source selection bound.

## 5. Why even perfect reference tables are not enough

Consider two stipulated worlds. In both, calibration runs on all four known sign contexts have exactly the same independent-flip channel. In the first, the source has the intended correlated signs and the same channel. In the second, the source signs are independent and the source-run apparatus has the prior contextual error; its output table matches the first. Give the apparatus a hidden mode `H=0` on reference runs and `H=1` on source runs. A calibration can be arbitrarily precise yet observe only `H=0`. Matching all four calibration contexts does not logically bound source-mode response at `H=1`.

Interleaving randomized calibration settings can make such a mode harder to attribute merely to time and can expose some setting-dependent responses. It does not exclude every hidden variable correlated with the physical distinction between reference and source preparations. A justified device model, protected randomization, independent environmental monitoring, a provable norm bound or an expanded observable set could constrain the issue; each must be tested or derived rather than assumed. This is an identifiability counterexample for the declared accessible records, not a theorem that calibration is impossible in every physical setting.

**Why is transfer the deeper dependence?** A probability observed under one intervention predicts another only through an invariant response law or a bound on its change. The new theorem makes that premise quantitative; it does not create it. **Why should that law hold?** It must follow from actual coupling, preparation and isolation mechanisms, whose material conditions and resources must be independently constrained. **Why those mechanisms and a source at all?** The current three-frame link, history clock and sensors remain chosen constructions; the zero constraint and covariance do not yet derive them or select the `ρ_ε` family. **Why should the underlying constitution be necessary or actual?** The present work has no non-circular derivation of this. That is the boundary reached by the current argument, not a claim that reality is ultimately brute or that a deeper self-sufficient explanation cannot exist. No external temporal cause of the whole is presumed.

## Continuation: an explicit fault interaction

The [next pass](ZERO_GAUGE_FAULT_RECORD_RECOVERY_AND_CLOCK_COST.md) realizes the transfer rival with a finite environment–fault coupling, gives a coherent correction that works on the written sector under explicit ready-state assumptions, and calculates its disturbance to the retained clock-sensor history. The gate, accessible fault record and feedback remain supplied physical inputs.

## 6. Next work

- Specify physically preparable joint-sign reference states and a common local interaction, model their environment and selection, and derive or independently bound τ, e and σ rather than simply assigning them. Include randomized source/reference interleaving and all retained early/late outcomes.
- Compare explicit clock descriptions with preparation, readout and selection transported together; constrain the transformation of their physical environments and resources. The small fixed-effect state-shift drift is not that result.
- Continue the constitutive chain from zero/whole to the admission, physical realization and selection of carriers and dynamics, separating mathematical sufficiency, empirical discrimination and metaphysical necessity.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_gauge_calibration_causal_controls_test -v
```

The tests check the two causal counterexamples, the bound's numerical example, synthetic non-independent response tables, uncertainty controls and 500 reproducible randomized response/weight cases. They do not prove real-world assumptions or comprehensive source coverage.
