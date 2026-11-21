# Jointly controlled action versus a lived perspective

## Result

A single action can be sensitive to **both** of two inputs without the two corresponding experiences being established as jointly lived in one perspective. This remains true even when a task rules out every strategy using only one input. The task then supports a real conclusion about **information-dependent action**, not by itself a conclusion about the number of subjects.

This sharpens the earlier [split-brain task audit](SPLIT_BRAIN_DEEP_EVIDENCE_AND_TASK_AUDIT.md). It addresses Schechter's stronger notion of action unity—both experiences can contribute to the same action—rather than only noting that either side can separately trigger a response. It also gives a deliberately stronger motor-computation countermodel on the existing four-spin domain. The contribution is a separation of precise hypotheses, not a new theory of consciousness or a denial of the first-person datum.

For an XOR response, a single-input strategy succeeds at most **1/2** under balanced independently randomized inputs, but the corresponding best score is **3/4** in the existing `t=1/4` equilibrium. The difference is important: a 50% benchmark would be inappropriate if the inputs were simply drawn from that equilibrium. An independently warranted conjunction assay could still distinguish specified experiential rivals, but no such assay is supplied here. B4–B5/F2, B9/F3 and B10 remain open.

## 1. Schechter's action-unity proposal

We read the complete text of Elizabeth Schechter, [“Action unity of consciousness”](https://doi.org/10.33735/phimisci.2025.11812), *Philosophy and the Mind Sciences* **6** (2025), including its notes and reference list. The displayed caption for its reproduced Pinto figure was read; the figure image and underlying cited primary datasets were **not** independently inspected for this follow-up. The [2017 Pinto main article](SPLIT_BRAIN_FIRST_PERSON_CONSTITUTION_COMPARISON.md) was read separately in the earlier audit.

Schechter distinguishes cross-responding to one stimulus using either response modality from cross-matching two stimuli. She considers, rather than establishes, the hypothesis that direct interhemispheric visuomotor integration explains some crossed responses. She also notes alternative mechanisms, including redundant ipsilateral control and overt cueing; different patients and tasks need not use the same route. In her section 5, action unity relates experiences through their availability to contribute to the same token action or motor consumer. She explicitly distinguishes a **stronger** reading—both can contribute—from a weaker either/or reading, and says that comparing their evidential support needs more work.

Her proposal is not simply that motor unity proves a single phenomenal perspective. In section 6 she questions whether the relation is a *conscious* unity at all when downstream motor signals may be unconscious, considers possible defenses, and argues that action unity may dissociate from phenomenal or access unity. Her qualified interpretation of Lockwood leaves open one conscious being with multiple phenomenal perspectives; her own paper does not argue that actual split-brain consciousness is conclusively one or two. The 2023 study is discussed in note 5, where she questions whether deliberate processing establishes general experiential unity. Schechter's suggestion that introspection is perspective-internal is a substantive epistemic argument, not evidence that first-person testimony is worthless. Her treatment of illusionism is also not adopted here: genuine experience remains valid data.

The earlier task audit already cited action unity, and the present example is a project-specific application, not a discovery of the action/experience distinction. Nor do we claim that Schechter proposed this XOR model or that she endorsed the model's experiential assignments.

## 2. One physical response with two necessary inputs

Use the project's four-spin `t=1/4` sector. Write

```text
X = q(0,1),    Y = q(2,3),    A = X XOR Y.
```

Here `q(i,j)=1` exactly when the two spins disagree. Add an explicitly hypothetical response device that reads the two physical bits and writes `A` to a response slot; this device and its readout are **additional physical structure** held the same for all rivals. It is not part of the original autonomous four-spin dynamics and does not establish a neural mechanism. `A=0` means the mismatch values match and `A=1` means they differ; it need not report the original spins or any phenomenal content.

For every input pair, changing `X` alone changes `A`, and changing `Y` alone changes `A`. The very same response slot is jointly controlled by the two channels in this specified structural model. In a hypothetical simultaneous physical implementation, the two channel signals can both contribute to one actual action. This demonstrates a joint **physical** computation, not a direct account of Schechter's contribution from conscious experiences: that application would additionally require the signals to be appropriately related to actual conscious contents.

There is no claim that successful cross-matching cannot occur here: `A` **is** a correct binary matching response. A downstream reader could see `A`, and, if they also know one input, infer the other. Such inference, newly produced representations, and potential feedback may matter to the phenomenal theory. The narrow point is that a correct action, even one with two counterfactually necessary inputs, does not by itself show that the original two experiences were jointly present in one field during the target window. A concrete theory could impose an independently defended bridge from such integration to phenomenal unity; this model does not refute that theory by itself.

## 3. The shortcut depends on the input distribution

### Balanced controlled preparation

Hypothetically prepare `X,Y` independently and uniformly. One explicit spin preparation is

```text
(s0,s1,s2,s3) = (1, (-1)^X, 1, (-1)^Y).
```

It produces exactly the specified mismatch bits; no claim is made that these clamps can be realized in a brain or without disturbing the system. Fix the target response rule and allowed channels before seeing data.

If a response strategy receives `X` alone, then for either value of `X`, the target `X XOR Y` is an unbiased bit; its success probability is exactly `1/2` for every deterministic response map. The same is true for a strategy receiving only `Y`. Independent pre-shared randomization and mixtures of such one-input strategies cannot improve the bound. By contrast the specified joint response achieves accuracy `1`.

There is a subtle but important distinction between **marginal statistical association** and **causal dependence**. Under uniform inputs, `A` is independent of `X` alone and independent of `Y` alone: each pair `(X,A)` and `(Y,A)` is uniform. Yet `A` is fully determined by their joint values, and changing either input with the other held fixed reverses `A`. Thus a zero single-input mutual information or zero marginal correlation is not evidence that the corresponding input has no causal effect on this action. This is a familiar XOR/synergy phenomenon, not a new information-theoretic theorem.

### Uncontrolled four-spin equilibrium

The existing equilibrium is a different distribution. Its exact outer-pair mismatch probabilities are

| `(X,Y)` | probability |
|---|---:|
| `(0,0)` | `9/16` |
| `(0,1)` | `3/16` |
| `(1,0)` | `3/16` |
| `(1,1)` | `1/16` |

`X` and `Y` are independent but each is `1` only one quarter of the time. A strategy seeing only `X` can output `X`, correctly guessing `Y=0` on `3/4` of trials; symmetrically one seeing only `Y` can output `Y`. These are optimal. The balanced-input marginal-independence observation about `A` also no longer applies. Randomizing a preparation and passively sampling the equilibrium are different protocols; one must not import the former's 50% baseline into the latter's data.

The [verifier](verification/action_unity_xor_gate.py) computes the equilibrium from the existing kernel, enumerates all four Boolean response rules on either single input, checks the two exact bounds and the four controlled preparations. Its [receipt](verification/action_unity_xor_gate.json) is an arithmetic check, not evidence for experience, available interventions or a clinical mechanism.

## 4. A conditional error-tolerant control

Suppose each trial has a designated local-input-only **shadow strategy** whose choice before the current inputs may depend on past observations and shared randomness but is independent of the current unseen input. The actual response equals that shadow unless a specified leakage or violation event occurs. Conditional on the entire past, assume:

- conditional also on the shadow's pre-trial randomization and choice of accessible input, the current joint input distribution is within total variation distance `δ` of independent uniform bits;
- the probability of the violation event is at most `ℓ`;
- the target and recorded success are defined on **all** eligible trials, with missing responses treated as failures or accounted for in the violation bound.

Then the conditional success probability of any such actual strategy is at most

```text
b = min(1, 1/2 + δ + ℓ).
```

Proof: on an ideal balanced input distribution the shadow succeeds with probability `1/2`; total variation changes the probability of its success event by at most `δ`; the actual and shadow success indicators can differ only on a violation event. The union bound needs no independence between leakage, inputs, and performance. The shadow and violation assumptions must hold **conditional on each actual past**, not merely as unconditional averages. A leakage flag recorded only on easy-to-observe channels is not automatically a bound on all unobserved channels. Similarly, randomly switching which input is available can invalidate the shadow assumption if that choice depends on current input values or shared post-input signals.

For a predeclared `n`-trial protocol, suppose these conditional bounds hold for every trial, even under adaptive history. For an observed success fraction at least `b+ε`, a bounded martingale Hoeffding bound gives a null tail no larger than `exp(−2nε²)`. For illustration only, `δ=.02`, `ℓ=.05`, `n=400`, and a threshold `.70` give `b=.57`, `ε=.13`, and a bound approximately `1.35×10⁻⁶`. This is **not** a real p-value, a recommended sample size, or a guarantee that the leakage assumptions hold. The randomization, shadow coupling, operational leak controls and simultaneous validity of the budgets must be justified independently; missingness, model selection, and finite-sample uncertainty in the budgets need their own treatment.

Beating this bound challenges the specified one-input/no-leak operational model. It does not identify a particular neural pathway, prove that both inputs were conscious, establish conjoint experience, or prove two subjects. Conversely, failure to beat it need not establish absence of joint computation, because noise, access difficulty, fatigue or a flawed protocol can depress performance.

## 5. The same action under experiential rivals

Use the same preparations, four-spin dynamics where applicable, added XOR device, feedback rules and all permitted physical interventions. Compare two **stipulated, experience-respecting** descriptions:

- **L-like:** two distinct local fields are associated with the selected pairs; each has a locally experienced contrast associated with its own `q`. The device combines their physical signals. No single field is stipulated to have both original contrasts together in the target window.
- **C-like:** one whole-associated field has both corresponding contrasts conjointly in the target window. This joint-content assumption is an **additional** quality/incidence hypothesis; the original connected-component selector alone does not supply it.

These are deliberately minimal diagnostic assignments, not established metaphysically possible worlds. In both, the response device performs exactly the same XOR, both local contrast reports can be accurate under separately stipulated report links, and a physical action can depend on both bits. Thus the action's perfect accuracy, intervention sensitivity, or motor output distribution does not alone select one of these assignments. If a particular physical theory makes either field assignment impossible or imposes different response laws, that added content can break this constructed equivalence and must be assessed on its merits.

The experiential difference is real within the assumptions: C-like asserts the **conjoint** occurrence and L-like denies it for the original contrast tokens. Direct warranted experience of a particular conjunction is evidence for that occurrence; it should not be erased in favor of third-person behavior. But a laboratory report of a match can be generated by the shared motor computation without independently establishing that experiential conjunction. Assuming that report is accurate about the very disputed conjunction would add the required bridge rather than infer it from response success. New sensory feedback may itself be experienced in either model, but whether it creates a joint field, merely supplies inferred information, or changes token identity is an additional, time-sensitive question.

This comparison tests neither the original `q=1`-to-unpleasantness hypothesis nor a real individual's constitution. Representing `q` as an experienced binary contrast is a further stipulation and must not be conflated with the project's disputed valence law. The two fields and whole field are not created by the XOR device merely because we have assigned them labels.

## 6. How the alternatives could be separated

A future discriminating test must independently specify the phenomenal conjunction `J`—which contents, which local window, and which experiencing perspective—then justify how the proposed report refers to it rather than to the downstream XOR answer or a later inferred representation. It must compare C-like and L-like predictions while accounting for perceptual encoding, motor feedback, response access, timing, cueing and the possibility that probing changes the episode. The existing [split-brain first-person comparison](SPLIT_BRAIN_FIRST_PERSON_CONSTITUTION_COMPARISON.md) gives a conditional conjunction distinction; the [shared-token gate](SHARED_EXPERIENCE_VERSUS_DUPLICATED_TOKENS_GATE.md) addresses the different question of numerical identity of shared aspects.

A report with a validated, intervention-specific error bound could exclude a stipulated no-conjunction package; if the bound is assumed rather than established, so is the conclusion. A negative or missing response is not evidence of no experience without a separately defensible failure model. Actual first-person unity reports, including preserved reports after split-brain surgery, deserve evidential weight; Schechter's rival interpretation and task findings do not automatically override them. Studies, if any, must be ethical, consensual and grounded in appropriate clinical expertise; this note supplies no human data or actionable clinical protocol.

The required next step remains a noncircular principle of **phenomenal individuation and realization**, justified against action-first, field-first and neutral-ground rivals on the same evidence. Adding a motor gate or winning a response benchmark does not supply that principle, full structural and experiential intelligibility under C3, or a substantive battery pass.

## Reproduction

Run `PYTHONPATH=verification python verification/action_unity_xor_gate.py` and `PYTHONPATH=verification python -m unittest action_unity_xor_gate_test`. The statistical bound is established by the argument above; the program does not verify its assumptions or run an experiment. Other source and reading limitations are stated in section 1.
