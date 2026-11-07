# Can partial frontal recordings certify removal of distribution?

## Decision

**Not without a coverage assumption or additional measurements.** Even perfect measurements of a source and a monitored consumer feature, plus randomized assignment of the disruptive intervention, can leave the strength of the *joint* source-to-consumer channel completely unidentified. This is a conditional no-go for partial coverage, not a proof that P4 is impossible experimentally. It sharpens the [specific extrastriate–frontal candidate](SPECIFIC_VISUAL_PATHWAY_GATE_TEST.md) and the frozen [maintained-disclosure contract](MAINTAINED_DISCLOSURE_CANDIDATE.md).

This is not a newly discovered coding principle. Joint or synergistic population codes are established neuroscience: [Schneidman, Bialek and Berry (2003)](https://doi.org/10.1523/JNEUROSCI.23-37-11539.2003) distinguish population information, correlation and decoding. Randomizing a treatment does not, by itself, identify the causal effect of a mediator; see [Cashin and Lee (2021), an introduction to mediation analyses of randomized trials](https://doi.org/10.1016/j.jclinepi.2021.02.014). The contribution here is an explicit, exactly checked **P4 stress test** applying these known issues to the candidate and isolating the additional bound needed. It is not a finding that a particular brain uses this code.

## 1. Identical observations, different removal status

In a hypothetical binary model, let stimulus `X` and intervention `Z` be independently randomized and fair. Let `N` be an independent bit with probability 1/4 of 1, and define a source `C = X xor N`. Independent fair bits `K` and `W` are available to the consumer system. There is no feedback from the consumers to C in this deliberately simple model. In the control arm (`Z=0`), the consumer receives two components:

```
R = C xor K,    U = K.
```

In the intervention arm (`Z=1`), with probability `p` the same rule is used, and with probability `1-p` replace `C` in that rule by independent noise `W`. The consumer still has the pair `(R,U)`. Treat `p` as an unknown property of the physical mechanism, not as an estimated parameter from the study.

Assume, generously, that the observer measures **X, Z, C and R exactly**, with unlimited independent samples, but cannot observe U or its trial-by-trial association with R. The complete observed joint law of `(X,Z,C,R)` is **identical for every `p` from 0 to 1**. In both arms R is fair and independent of X and C. C has exactly the same equation and distribution in both arms. In this simple static model even the local source equation remains the same under interventions on X; this is not evidence for P3's full state, dynamics or counterfactual powers in a biological circuit.

Yet, in the intervention arm:

- At `p=0`, `(R,U)` is independent of C: this particular channel has been removed.
- At `p=1`, the consumer recovers `C = R xor U` exactly: the channel is fully retained, although neither component alone carries C information.
- More generally, the interventional influence

  `TV(law(R,U | do(C=0), Z=1), law(R,U | do(C=1), Z=1)) = p`.

Thus the same observed data are compatible with **every strength in [0,1]** for the full toy-consumer channel. The control arm has strength 1 for all p. Even an exact null effect on the measured R is insufficient to certify absence at the joint consumer. This stays true if a separate, hypothetical P6 assay has the same validated outcome in both models: P6 calibration does not supply the missing P4 physical coverage. We have not claimed an equivalence of the full H_M1 and H_D1 theories or assigned experiences to the toy circuit; their phenomenal predictions must still be applied separately once their shared physical premises are established.

If U is also recorded **on the same trials** and the joint code is analyzed, these two endpoints are distinguishable in this example. Measuring R and U separately without retaining their pairing still misses the XOR relation. If the declared consumer is genuinely *only R*, rather than `(R,U)`, the narrow R-channel is absent here; one cannot then automatically claim that the larger distributed organization, including U, is absent. The decisive question is which consumer system and what alternative or equivalent distribution P4 actually rules out.

## 2. The missing term in a quantitative certificate

Let `(Y,U)` be a predeclared consumer: `Y` is recorded, `U` is the unrecorded remainder. For a fixed intervention condition, write `P_c = law(Y,U | do(C=c))`. In a finite/discrete system, the standard triangle inequality yields

```
TV(P_0, P_1)
  ≤ TV(P_0^Y, P_1^Y)
    + E_{Y ~ P_0^Y}[ TV(P_0(U | Y), P_1(U | Y)) ].
```

Use arbitrary regular conditional versions on zero-probability rows; when a `P_1^Y` row is zero, for example, its conditional can be chosen as the corresponding `P_0` conditional. The bound is obtained by inserting the intermediate distribution `P_0^Y P_1(U|Y)`, then applying the triangle inequality. It is a standard TV decomposition, not a new theorem; compare the [conditional-distance chain rule](https://rishirajb.github.io/pubs/cond.pdf).

If independently justified upper bounds are `δ` on the recorded intervention effect and `γ` on the hidden conditional term, the full specified consumer effect is at most `min(1, δ+γ)`. To certify a tolerance `ε`, one needs `δ+γ ≤ ε` with simultaneous uncertainty control. This is **sufficient, not necessary**: a different direct bound on the full consumer would also do. `γ` is a counterfactual/physical coverage assumption or separately measured quantity, not something derived from a null finding on Y.

In the toy, `δ=0` for every p but `γ=p`, making the bound tight. The same conclusion applies to every choice of `p`, not just the endpoints. A consumer-side lower bound from a frozen decoder, as in the [previous note](SPECIFIC_VISUAL_PATHWAY_GATE_TEST.md), can show that *some* information survives. It cannot supply this missing upper bound on information outside the recorded features.

A direct source intervention, if feasible, identifies only the response to the particular implemented perturbation. It is not automatically equivalent to `do(C=c)` on the whole source state: stimulation may have off-target paths, incomplete control, and nonstationary or nonlinear effects. In particular, comparing two source states to measure influence may change the source during probe trials; one must justify transport of that effect to the actual P3-preserving separation condition. The formula assumes valid interventional distributions; it does not itself prove them identifiable from cTBS, fMRI, or observational association.

## 3. Apply to the visual candidate

For the proposed extrastriate-source/frontoparietal-consumer case, Y might comprise the recorded, time-resolved features of nominated IFJ/IFG regions; U includes relevant unrecorded neurons, interactions, other consumers and unmeasured temporal components **within the declared P4 scope**. The 2015 BOLD recordings do not provide a quantitative upper bound γ. The fact that the study found residual goal-relevance decoding is already evidence against complete *statistical-code erasure* in the measured IFJ regions; the present counterexample addresses the separate problem of falsely certifying absence elsewhere or in joint codes. Neither observation identifies a directed causal pathway from extrastriate cortex on its own.

**Concrete next substeps, in order:**

1. Freeze the consumer boundary and the phenotype-relevant content variable before looking at results. State whether P4 forbids any equivalent outside-C organization or only a specifically defined channel; do not silently turn a broad claim into a narrow ROI result.
2. Record candidate consumer features jointly and time-resolved on the same trials, including relevant interactions where feasible. Keep raw paired samples, not just per-ROI accuracies. Predeclare what temporal and spatial coverage is missing.
3. Predeclare either an experimentally justified upper bound for the full joint causal effect, or a separate scientifically defensible bound on γ. If neither can be bounded, **P4 is unresolved**, even with infinite trials and perfect null results on Y. Do not treat sample size as a substitute for coverage.
4. Validate source perturbation selectivity and the transport from probing to the P3-preserving condition; show that P3 and calibrated P6 remain warranted on the separating trials. Apply participant-clustered and simultaneous uncertainty treatment. Clinical intracranial coverage, stimulation risks, and BOLD/EEG measurement limits remain practical constraints, not resolved here.

**Result for the global plan:** this advances M4 by identifying a precise assumption that the real experiment lacks and a falsifiable condition under which a null monitored effect would be adequate. The [boundary-cut follow-up](DISTRIBUTION_CUT_AND_RECORD_PERSISTENCE.md) supplies a conditional whole-consumer bound and checks prior-record persistence in the existing workspace. This does not establish P4 for a human, decide a phenomenal law, or prove a universal subject. The separate L3/L4 physical-field work remains unchanged.

## 4. Executable check

Run `python verification/consumer_coverage_identifiability.py`; its [saved results](verification/consumer_coverage_identifiability.json) verify p = 0, 1/4, 1/2, 3/4, 1, the equality of all observed joint distributions, the control- and treatment-arm channel strengths, and the tight conditional bound. It also checks the generic bound for all 1,225 pairs of four-cell distributions with probabilities in quarter increments. These finite tests check the algebra of the examples, not the plausibility of any neural encoding or a clinical intervention.
