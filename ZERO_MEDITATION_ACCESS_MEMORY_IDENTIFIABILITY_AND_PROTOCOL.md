# From reported cessation to a discriminating experiment

## Constructive result

The previous [article analysis](ADVANCED_MEDITATION_SELF_CESSATION_AND_ZERO.md) separated a reported gap, access to a stimulus, memory, and experience. Here is a concrete reason the separation matters: **even with perfect statistics, a delayed recognition score alone cannot distinguish a weak functional cue signal from a strong signal that is rarely retained.** A second, suitably controlled response condition can distinguish these explanations in an explicit model. But it does so only if the conditions measure sufficiently comparable channels; the added response may itself alter the meditation.

This turns a general caution into an actionable design: measure both channels, deliberately test the disturbance caused by the interface, and separately evaluate phenomenology and felt valence. The example is hypothetical and exactly calculable; it is **not an analysis of the meditation studies or a claim about the consciousness of the model**.

Verifier: [`verification/zero_meditation_access_memory_identifiability_test.py`](verification/zero_meditation_access_memory_identifiability_test.py).

## 1. A recognition gap has multiple mechanisms

Consider a stimulus-present trial. Define a deliberately simple functional model:

- \(a\): probability that the stimulus generates a cue-specific signal available to an immediate response channel. This is an operational latent variable, **not defined as phenomenal awareness**.
- \(m\): conditional probability that this signal produces a usable later memory, given that the signal occurred.
- \(f_I,f_R\): immediate and delayed false-alarm probabilities. For simplicity, false alarms are independent of the signal and retention variables.

An immediate response is positive if either the signal or a false alarm occurs; delayed recognition is positive if either the signal is retained or a false alarm occurs. With a cue versus no cue,

\[
 H_I=f_I+(1-f_I)a,\quad F_I=f_I;\qquad
 H_R=f_R+(1-f_R)am,\quad F_R=f_R.
\]

No cue generates no signal in this toy model. False alarms can still produce responses. This simple Boolean channel is chosen for clarity, not assumed to describe real cognition. In particular, an immediate behavioral response need not be conscious; a missed response can also reflect response inhibition, motor limitations or other factors.

Let both false-alarm probabilities be 0.1. Consider two explanations:

| hypothetical channel | cue signal \(a\) | retention \(m\) | delayed hit | delayed false alarm | immediate hit |
|---|---:|---:|---:|---:|---:|
| strong signal, weak retention | 0.8 | 0.25 | 0.28 | 0.10 | 0.82 |
| weak signal, strong retention | 0.2 | 1.00 | 0.28 | 0.10 | 0.28 |

**Delayed recognition is identical in both rows, for cue and no-cue trials.** In fact there is a continuum: all \(a\in[0.2,1]\) with \(m=0.2/a\) give that same delayed distribution. Given the model, a valid immediate channel separates the example: one immediate cue trial distinguishes the two rows with optimal equal-prior success probability 0.77. That figure is an analytic property of this invented toy problem, **not an expected result or power estimate for a real study**.

If both channels share the same \(a\), with known or separately estimated false-alarm rates and \(f_I,f_R<1\), then

\[
 a={H_I-F_I\over1-F_I},\qquad
 m={H_R-F_R\over(1-F_R)a}\quad(a>0).
\]

This is conditional identifiability, not direct perception of an internal mechanism. When \(a=0\), \(m\) cannot be recovered at all; near zero it is unstable. Finite samples add uncertainty, unequal response and recognition biases, missed stimuli, timing errors, and potentially invalid values under model misspecification. Confidence or posterior intervals must propagate uncertainty in all four rates; a ratio of point estimates is not enough.

## 2. The interface can change the process it measures

The response and recognition channels may have to be measured in different trials: asking someone to make a prompt response could disrupt the state or alter later encoding. It is therefore **not legitimate to assume** the same \(a\) in both arms merely because the stimuli look alike.

The verifier gives an exact counterexample. In a response arm with \(a=0.8,m=0.5\), the immediate hit rate is 0.82. In a no-immediate-response arm with \(a=0.2,m=1\), the delayed hit rate is 0.28. Feeding those rates into the shared-channel equations yields \(m=0.25\), which is neither arm's actual retention parameter. The same observed rates can thus look like a successful decomposition while its crucial assumption is false.

The practical implication is to **measure intervention effects, not declare the response non-invasive**: randomize response demands and include no-cue shams, compare EEG, physiology, reported state and event frequency across arms, and perform sensitivity analyses allowing arm-specific signal probabilities. Similar observed reports and EEG can increase confidence in comparability but cannot prove that all relevant latent channels are invariant.

## 3. A separate phenomenal question

For the *same* functional model, the verifier attaches two illustrative unobserved labels: one says a hypothetical experience is present throughout; another says it is present only when the cue signal is present. Every probability of immediate and delayed response remains identical after that label is ignored. This mathematical construction does **not** establish that either label corresponds to an actual subject or is genuinely possible under the correct experiential law. It establishes the narrower point: **the response-channel equations, by themselves, do not contain a rule selecting a phenomenal interpretation**.

This distinction cuts both ways. A missed cue and failed recall do not prove a complete absence of experience; a successful response does not prove the person consciously experienced that cue. Rich, carefully elicited first-person descriptions are indispensable evidence about reportable experiences, but their absence in an interval does not by itself settle what was present there. Neural, behavioral and report measures can constrain competing proposals more strongly without becoming a direct meter of experience.

On the proposed one-reality view, an eventual law linking intrinsic experience and extrinsic organization might restrict these interpretations. That link is precisely what needs to be derived or defended, rather than inserted by relabeling an operational signal as experience. This is not a demonstration that a fully self-sufficient zero constitution cannot supply the link.

## 4. A preregistrable protocol

This is a proposed study, not an established procedure or clinical recommendation.

**Participants and practice.** Recruit multiple trained practitioners across traditions, with repeated sessions per person, and appropriate comparison participants. Investigate reproducible meditation periods and, separately, the rarer reported cessation events. Include appropriate ordinary-rest and attentional controls. Agree on safety, stopping rules, consent and qualified support; demanding meditation and altered-state research can be distressing. Do not instruct people to force cessation.

**Randomized interface.** In counterbalanced sessions randomly assign periods to (i) a minimal immediate response demand and (ii) no immediate response demand, with randomized low-intensity cue-present and cue-absent sham periods in each arm. Obtain delayed recognition, collect separate ratings of self-boundary, attention, arousal, felt valence and distress, and elicit open phenomenological descriptions. Calibrate detectability and motor responses outside the target practice. Compare response-demand and no-response arms on event rates, distributions of reports, EEG and physiology; measure false alarms and signal detection, not just hits. Because reports may themselves affect the process, their timing should be protocolized and pilot-tested.

**Primary estimand before event selection.** Compare randomized arms on outcomes defined for *all assigned periods*, including rate of reported events, state ratings, and cue-related detection/recognition, with participant-level clustering. This estimates effects of the assigned interface under the usual randomization and adherence assumptions. It does not require treating every repeated trial as a new person.

**Event-relative analysis.** Randomize cues prospectively over eligible periods, not only after a reported cessation is known. Preregister how event times are marked from physiological cues and retrospective reports, including onset uncertainty and blink artifact, and inspect pre-event and post-event windows. The 2024 cessation paper's 37 events were from one person and used an eye-blink-related marker; the associated [network study](https://researchinformation.umcutrecht.nl/en/publications/neurophenomenological-investigation-of-mindfulness-meditation-ces/) is not independent of the spectral analysis. Retrospectively selecting only events or only reported events can introduce post-treatment selection bias if the probe changes event occurrence, recognition or reporting. Thus event-conditioned contrasts are **associational/sensitivity analyses**, not automatically randomized effects of a probe within an unchanged state. Report the cue timing distribution and event counts and model uncertainty explicitly.

**Discriminating prediction.** Before testing held-out data, specify competing ranges for the immediate hit and false-alarm rates that would follow from a strong-signal/weak-retention versus weak-signal/strong-retention explanation of the same delayed recognition rate. These predictions must be fixed using independent pilot or training data; delayed data alone do not select the ranges. Score predictions on held-out immediate-response trials, and compare a shared-channel model with one allowing arm-dependent signal and retention. Preregister a meaningful effect size and uncertainty threshold. If the response demand changes event rates, relevant state measures or the cue channel enough that the common-channel model fails, do not report its inferred \(m\) as a demonstrated memory parameter. Failure of a specified model's held-out predictions counts against that model, not against one-reality metaphysics. This design does not guarantee that any difference will be present.

Use participant-level held-out evaluation for generalization to new individuals and, separately, held-out sessions for within-person stability. Plan the number of practitioners and sessions using event-rate pilots and preregistered power simulations with realistic within-person dependence. Rare cessation events may make this infeasible; report insufficient data rather than silently treating repeated events from one person as independent replications. Consider preregistered estimates with uncertainty rather than a binary significant/nonsignificant verdict.

## 5. Consequence for the wider constitution

This protocol distinguishes operationally different ways a local report can fail while the larger physical organization remains present. It is consonant with the distinction between one whole and its changing internal interfaces, and with the insight that a disappearing narrative self need not mean all differentiated experience vanishes. But it does not imply that the person has access to another realm, that a mathematical pointer is a subject, or that an individual reports the whole.

Self-boundary and valence should be tested separately. A unity report, a zero *difference* between two measurements, and a vanishing formal signed mean are not the same as absence of suffering or a globally additive experiential zero. If intrinsic experience and extrinsic matter are aspects of the one reality, a substantive future construction must explain how the relevant physical organization and its particular felt character belong together, including negative felt valence. Neither a probe nor this toy model supplies that correspondence.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps \
 python -m unittest verification.zero_meditation_access_memory_identifiability_test -v
```

The verifier uses exact rational enumeration of the invented channels. It performs no human-data analysis and does not establish which mechanism occurs in meditation.
