# When a pitch-to-frustration explanation cannot work

## Result

The proposed connection between misalignment and discomfort needs a defensible map from physical relations to a subject's experience. A tempting shortcut is to turn musical pitch separations directly into preferred phase offsets and then calculate a network's minimum frustration `F`. This report tests that shortcut. It gives three restrictions on a precisely defined family, not a general refutation of relational experience:

1. A single pairwise edge has **zero minimum frustration**, whatever its preferred phase difference. Therefore a bare `rating = h(F)` model with one oscillator per note cannot reproduce differing dyad ratings.
2. If the preferred phase difference is additive in the notes' log frequencies, **every graph is unfrustrated**, even for chords with three or more notes. A nonzero prediction requires non-additive edge preferences or a different architecture.
3. Even with arbitrarily nonlinear pairwise preferences, an important reciprocal, pitch-difference-only family is **invariant under pitch reflection**. It must predict identical `F` for exact mirror chords. A near-matched example in the existing data shows why this matters—but differences in spectral content and measurement noise remain alternative explanations.

This identifies where the hypothesis must become more specific: what interactions exist, how they acquire incompatible preferences, and why their organization belongs to an experiencing subject. It does not assume that musical notes are the oscillators of a brain or that consonance equals pain.

## 1. What is known, and the model under test

The cycle-holonomy compatibility criterion is existing mathematics and oscillator-network theory, not our discovery; see, for example, the [cycle-holonomy paper](https://arxiv.org/html/2604.19682v2), and our earlier [phase-frustration](VIBRATIONAL_DISSONANCE_EXPERIENCE_TEST.md) and [cycle-identifiability](FRUSTRATION_CYCLE_IDENTIFIABILITY_GATE.md) audits. We apply it here to a specific proposal for converting pitch differences into preferred phase offsets and compare its symmetry with a published dataset. Pitch-set reflection is also familiar music theory; see [Gettysburg's account of transposition and inversion](https://theory-iv.musictheory.sites.gettysburg.edu/lessons/week-07/inversion-transposition.html). Reflection here means `x → c−x`, not merely changing which chord tone is lowest.

Let `x_i = 1200 log₂(f_i/f_ref)` be a note's fundamental frequency in cents relative to an arbitrary reference, and let `φ_i` be a modeled phase. For a fixed undirected graph `G` and one independent reciprocal channel per edge, take

```text
E(x,φ) = Σ_(ij in G) k(x_i−x_j) [1−cos(φ_i−φ_j−g(x_i−x_j))],
F(x)   = min over all φ of E(x,φ).
```

Here `k(d)≥0` is even, `g(d)` is odd modulo `2π`, and both functions are the same on each edge. Edges use an arbitrary but fixed orientation; reversing it changes both phase difference and preferred offset sign. A possible predictive rule for **consonance** is a single-valued `rating = h(F)` shared across the stimuli considered; it need not be monotonic for the no-go arguments. For graph comparison, graphs must correspond under node reflection; complete graphs are an example. These are strong modeling choices. They are **not** asserted properties of real auditory or neural systems. In particular, independent parallel channels, register-dependent weights, other environmental nodes, external forcing, an evolving state, and context-dependent `h` are excluded from this narrow model.

## 2. First obstruction: the dyad

For a graph of two nodes joined by one nonnegative edge, choose `φ₁−φ₂ = g(x₁−x₂)`. The only cost vanishes. Thus `F=0` **for every dyad**, regardless of pitch interval, k or g. More generally, any finite tree with one such cost per edge can be satisfied by assigning phases along its edges. A common `h(F)` consequently assigns all these dyads the same rating.

The [Bowling et al. 2018](https://doi.org/10.1073/pnas.1713206115) aggregate table instead gives a minor second `1.317` and octave `3.893`, a difference of `2.576` on its four-point scale. A constant prediction has absolute error at least `1.288` for one of these two **observed means**, by the triangle inequality. This is a deterministic fit statement about this table, not a significance test or proof of the population difference.

The direct one-note/one-node single-edge **F-only explanation** is therefore incompatible with reproducing these observed means. The broader proposal is not: for example, a brain network might have many additional channels even for a dyad; state-dependent mismatch `E−F`, a baseline acoustic contribution, or context might matter. Each addition requires independent specification and testing, not a post-hoc label. [Marjieh et al.](https://doi.org/10.1038/s41467-024-45812-z) show why timbre and established psychoacoustics matter to such comparisons.

## 3. Second obstruction: additive pitch preferences

Suppose `g(d)=αd (mod 2π)` for a common fixed α, with α measured in radians per cent. Assign `φ_i=αx_i`. Then every edge mismatch is zero, simultaneously, so `F=0` for **every graph and chord**, including those with cycles, regardless of the positive weights. The same conclusion holds for any additive map into the phase circle, since `g(x_i−x_j)=g(x_i)−g(x_j)`.

This is a special case of the known fact that a pure node-gradient connection has zero cycle holonomy. It is a useful design gate: simply converting frequency or log-frequency differences to preferred phase differences does not create intrinsic frustration. It also illustrates why large frequency separations or small raw synchrony do not, by themselves, measure frustration.

Nonadditivity can create it. For a triangle with coordinates `(0,a,a+b)`, the oriented sum of preferred offsets is, up to orientation,

```text
g(a) + g(b) − g(a+b)   (mod 2π).
```

In the stipulated one-channel cosine model, a nonzero sum with strictly positive weights makes `F>0`; a zero sum makes it possible to satisfy all three edges. As an illustrative mathematical example only, in arbitrary pitch units take `(x₀,x₁,x₂)=(0,1,2)`, `g(d)=(π/2)sin(πd/2)` and unit weights. The sum has magnitude π, and the known frustrated-triangle minimum is `F=3/2`, reached at phases `(0,π/6,π/3)`. There is no claim that such a `g` describes musical hearing or brains. Even a nonzero `F` does not establish an experience.

## 4. Third obstruction: reflection symmetry even for nonlinear preferences

Fix any graph whose edge set is transported with its nodes, any allowed even k and odd g, and any number of vertices. Reflect coordinates `x'_i=c−x_i` and phases `φ'_i=−φ_i`. For every edge, both the coordinate difference and phase difference reverse. Consequently the phase mismatch changes sign, while cosine and k are even:

```text
E(x', −φ) = E(x, φ) for every phase assignment φ.
```

Negation bijects the phase-configuration spaces. Therefore their minima are equal:

```text
F(c−x) = F(x).                                          (1)
```

This holds for arbitrarily nonlinear g, for any fixed weights from the stated common even function, and even if the same model is fitted to all data: fitting cannot remove its symmetry. A common `h(F)` also makes equal predictions. The result does **not** extend automatically to frequency-register-dependent or timbre-dependent couplings, edge functions that are not transported under reflection, nonreciprocal forces, multiple unobserved channels, state-dependent readouts, or a neural graph that changes across chords. Such models can break (1), but must state and justify how.

### Why this is not already a neural result

Pitch reflection preserves the multiset of pairwise log-frequency distances, but not the actual frequency spectrum. The map sends `f_i → constant/f_i`, not each sound's harmonic partials into an equivalent set of partials; loudness, absolute frequencies and familiarity can change. [Bowling et al.](https://doi.org/10.1073/pnas.1713206115) already analyze vocal-spectral similarity; [Hall et al.](https://doi.org/10.5334/tismir.243) already study interval-based models. A failure of the narrow model cannot be attributed uniquely to a new psychological or neural mechanism.

## 5. A closer empirical pair and an error bound

The earlier [chord audit](BOWLING_PAIRWISE_RELATIONAL_EMPIRICAL_GATE.md) found symbolic mirror chords with different ratings but substantially different just-tuned pairwise intervals. A stronger **exploratory, post-selected** comparison from the same transcribed source is:

| Relative integer pitches | Reported frequencies, Hz | Rating mean | Supplied harmonic-similarity score |
|---|---|---:|---:|
| 0, 1, 8, 12 | 184.68, 196.99, 295.49, 369.36 | 2.367 | 0.142 |
| 0, 4, 11, 12 | 170.86, 213.58, 320.36, 341.72 | 3.333 | 0.233 |

The integer pitch sets are exact reflections. Pair original node 1 with second node 4, original 2 with second 3, and so on. Among all six corresponding intervals calculated from the **reported rounded fundamental frequencies**, the largest discrepancy is approximately `0.08334` cent. The observed group-mean gap is `0.966` scale points. This is much closer to an acoustic interval mirror than the previous triad example, but it does **not** make the recordings identical or establish a statistically significant effect: register, spectra, timbre, perceptual context, participant variation, rounding and possible transcription errors remain. The supplied harmonic-similarity scores differ; they are not independently recomputed here.

### Conditional robustness to near-mirroring

Equation (1) is exact. For near-reflection, let each corresponding pairwise pitch difference differ from its reflected counterpart by at most `δ` cents. Assume over the relevant interval range that k is even and `L_k`-Lipschitz, g is odd and `L_g`-Lipschitz as a circle-valued offset (radians per cent), `0≤k≤K`, and the graphs have corresponding m edges. Then

```text
|F(x) − F(x')| ≤ m δ (2 L_k + K L_g).                   (2)
```

To see this, compare E at φ for the first graph to E at −φ for the second. Each weight change contributes at most `2 L_k δ`, since `0≤1−cos≤2`; each offset change contributes at most `K L_g δ`, since cosine is 1-Lipschitz in angle. The bound is uniform in φ. Minimizing both sides in turn preserves the same bound. If `h` is `L_h`-Lipschitz in F, its predicted rating gap is at most

```text
B = L_h m δ (2 L_k + K L_g).                            (3)
```

For this tetrad m=6 and the tabulated fundamental-frequency comparison gives `δ≈0.08334` cent, **conditional on the reported values representing the relevant inputs**. If two model predictions are compared to two observed means separated by `0.966`, at least one absolute residual is at least `max(0,0.966−B)/2`. This is a finite-table triangle inequality, not a confidence bound. Without independent bounds on `L_k`, `L_g`, `K`, `L_h`, model mismatch, measurement precision and sampling error, B could be too large to constrain anything. The estimate does not imply that the full sound spectra or the unknown neural interactions are close.

The full table contains 30 distinct symbolic reflection pairs among 66 triads and 95 among 220 tetrads; 6 and 30 chords respectively are self-reflecting. Even an in-sample oracle allowed to assign its own best constant to each reflection pair cannot reduce RMSE below `0.185` for the observed triad means or `0.153` for tetrads. This is the same representation floor noted in the preceding audit for these particular chord sizes: all relevant multiset collisions happen to be reflection pairs in this dataset. It includes measurement noise and is **not** independently predictive, noise-corrected, or a bound on population performance. All examples and counts were selected or calculated after seeing the source table; there is no preregistration.

## 6. A decision-ready test rather than flexible storytelling

A defensible future study would:

1. **Declare the model before held-out data:** graph, nodes, edge identification, `g`, `k`, F versus state mismatch, frequency and timbre dependence, and a fixed readout. Estimate the Lipschitz constants or another independently justified uncertainty bound. A symbolic note model and a neural-network model must not be conflated.
2. **Use a factorial stimulus design:** exact or tightly calibrated pitch reflections at several registers, timbres, levels and small detunings. Obtain calibrated recordings, spectra and participant-level repeated reports, rather than assuming fundamentals alone control the sound. Independent timbre and reflection manipulations help disentangle an interval-only rule from spectral and learned-context alternatives, but do not automatically isolate neural causality.
3. **Compare meaningful rivals:** acoustic roughness, harmonicity, familiarity and established interval-based models, all fitted and evaluated using a prespecified held-out listener/stimulus/timbre design. Predict mirror contrasts as well as absolute ratings; report uncertainty and failures, and treat shared listeners hierarchically rather than as independent chord rows. No single observed discrepancy warrants a model discovery claim.
4. **Separate neural identification:** independently measure the relevant nodes and interactions; challenge the reciprocal phase model and use the [selective-channel identification gate](SELECTIVE_CHANNEL_CERTIFICATE_AND_HARMONIC_ALIAS.md) or another validated method. Accurate behavioral prediction alone does not identify the interaction graph or prove phenomenal identity.

We have not executed or preregistered this study, established usable neural channels, or established sample size. Future human studies require consent, ethics review, safe listening levels and voluntary withdrawal. Findings would address bounded perceptual predictions, not the necessity of experiential ground or all genuine possibilities being actual.

## 7. Reproduction and integration

Run `python verification/pitch_frustration_inversion_gate.py`. It verifies the pinned input hashes, enumerates reflected chord sets, matches the *corresponding physical pair intervals* from reported frequencies, checks dyad data, exercises the invariance on 10,000 seeded phase/graph examples and the pointwise near-reflection energy bound on 5,000 more, checks 1,000 additive assignments, and evaluates the nonadditive triangle witness. The [JSON receipt](verification/pitch_frustration_inversion_gate.json) contains the numbers. The sample checks do not prove the theorem; the transformation and uniform-minimum arguments above do. [Source and license provenance](sources/external/README.md) is shared with the prior audit.

The larger framework still aims at a self-sufficient experiential ground with genuinely plural subjects, substrate independence and actuality of all genuinely possible local realities, without assuming a universal subject or an external creator. None of those commitments supplies the missing node/edge selection, empirical readout, qualitative identity, probability measure or emergent physics. Here “phase” is a local model variable, not an external universal time.
