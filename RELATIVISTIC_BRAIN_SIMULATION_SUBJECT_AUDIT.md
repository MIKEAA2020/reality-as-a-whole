# Cicurel and Nicolelis: brains, simulation and subject plurality

## What this attachment changes

The supplied book is **Ronald Cicurel and Miguel Nicolelis, *The Relativistic Brain: How It Works and Why It Cannot Be Simulated by a Turing Machine* (2015)**. It is directly relevant to the preceding question, but it challenges a more basic premise than whether there is one subject or many:

> Would a sufficiently detailed **digital simulation** of a human brain actually have experiences?

Bostrom assumes a suitable form of substrate independence for his argument. Cicurel and Nicolelis explicitly reject the relevant digital-simulation conclusion, proposing that biological brains have causally important continuous electromagnetic dynamics and arguing that their higher functions cannot be reproduced by a Turing machine. Their challenge is substantive. **Their book does not, however, establish that digital minds are impossible**, nor does it establish one universal consciousness or a subject-counting law.

This modifies the confidence and scope of my preceding answer: **plurality remains the more natural reading of Bostrom's simulated-people scenario, conditional on there being simulated experiencers.** The book makes that condition a central open question rather than something to assume. A theory with many biological subjects does not automatically imply there could be many conscious digital subjects.

## 1. Source and reading scope

The supplied PDF contains 108 PDF pages; the book's printed page number is generally PDF page minus two. Its SHA-256 is `b141852afc188d25d70bd1d9c8f5fa3b55a17001186810494947f3ce1807f957`. Text was OCR-extracted and searched throughout, with close reading of the preface, the theory, the mathematical/computational and information arguments, conclusions and predictions. This is a targeted audit, not a claim of a complete independent examination of every referenced experiment. OCR can misread symbols; page references below identify the PDF page as well as the printed page. The copyrighted PDF itself is not copied into the repository.

## 2. What the authors actually propose

The book calls its proposal the **relativistic brain theory** (RBT). “Relativistic” here concerns a brain's own context-dependent point of view and a proposed neuronal space–time continuum. It is not a demonstrated derivation of Einstein's relativity, or a solution to the physical problem of time. See PDF pp. 27–31 / printed pp. 25–29 and PDF p. 86 / printed p. 84.

Its proposed hybrid digital–analog computational engine has two interacting components:

1. Distributed neuronal firing, described as the “digital” component.
2. Time-varying neuronal electromagnetic fields, especially those hypothesized to arise from distributed white-matter pathways, constituting an “analog” component.

The authors propose reciprocal feedback: neuronal activity generates fields, which affect subsequent activity. The resulting “mental space” is claimed to contribute to binding, body image, pain, memory, sense of self and consciousness. They recognize analog membrane and synaptic potentials as well; they are specifically interested in field activity they think can integrate widely distributed functions (PDF pp. 29–33 / printed pp. 27–31).

Their Appendix I makes concrete empirical claims, including detectable deep white-matter-associated fields, field-induced distributed synchronization, and altered perceptual, motor or cognitive function when relevant fields are disrupted (PDF pp. 102–105 / printed pp. 100–103). These are **proposals and predictions**, not results established merely by listing them. Claims about autism and potential treatment in the appendix are speculative and are not clinical recommendations.

The authors explicitly characterize their position as **monist and materialist/physicalist**, while arguing that outside measurements and inside felt information differ (PDF pp. 91–92 / printed pp. 89–90). They do not rule out higher functions being reproduced by artificial means in general; they say such reproduction would not occur through a Turing machine (PDF pp. 92–93 / printed pp. 90–91). Their monism is not a demonstration that the whole universe is one conscious agent. Their examples normally concern an individual brain's perspective, shaped by history and interacting with other brains. Such a picture is congenial to local subject plurality, but an individual brain's apparent functional unity does not itself settle how many phenomenal subjects exist.

## 3. What is established—and what is not

**Field effects deserve serious attention.** [10](https://www.nature.com/articles/nrn3241) reviews how extracellular fields can affect neuronal excitability; [4](https://www.proquest.com/scholarly-journals/ephaptic-coupling-cortical-neurons/docview/847452923/se-2) describes Anastassiou and colleagues' rat cortical-slice experiments with weak applied fields and spike timing. Later [1](https://www.sciencedirect.com/science/article/abs/pii/S0014488618305235) reports evidence for field-mediated propagation in an *in vitro* hippocampal preparation under epileptiform conditions.

These findings support studying **ephaptic coupling**; they do not show that the book's particular white-matter-coil mechanism is the necessary or sufficient substrate of normal human consciousness. Field measurement, field-to-neuron effects, brain-wide binding, causal necessity for a particular experience, and phenomenal identity are distinct claims. A field perturbation may act through neurons, synapses, blood flow, sensory stimulation or other pathways; selective causal identification needs controls. A brain–machine interface showing learning or correlated firing also does not uniquely identify the proposed field mechanism.

The authors' emphasis on **first-person reports and internally felt experience** is useful and consistent with treating experience as data. But naming that information “Type II” or “Gödelian” does not establish a theorem that all such reports are noncomputable or that an external observer can never learn anything about their physical correlates. In our [experience-assay gate](EXPERIENCE_ASSAY_LATENT_IDENTIFIABILITY.md), first-person evidence and its physical communication are distinguished without declaring either intrinsically infallible.

## 4. Audit of the anti-simulation argument

The strongest issue raised is that a finite digital description or numerical model is not automatically the **actual physical process** or the **experience** it purports to model. Bostrom needs an additional psychophysical claim about implementation; behavioral similarity or successful computation alone does not settle it. This is a genuine live philosophical and empirical problem.

The book's wider no-go claim requires additional steps that have not been established:

| Argument in the book | What follows, and what does not |
|---|---|
| **Continuous electromagnetic fields contain uncountably many points** (PDF p. 29 / printed p. 27, footnote). | A finite machine does not list arbitrary exact real values at every point. It does not follow that a specified computable field evolution cannot be approximated to relevant finite precision over a finite region and time. Some mathematical field/PDE problems do have noncomputability pathologies; the mere use of continuous variables does not show that a particular brain exploits one. |
| **Chaos, non-integrability and changing conditions** (PDF pp. 65–66 / printed pp. 63–64). | Exact long-term trajectory prediction can be very difficult or practically unavailable. Non-integrability does not mean no numerical solutions, and sensitivity does not by itself rule out short-time approximations, statistical predictions or reproducing a functional organization. Whether those are adequate for experience is a separate question. |
| **Undecidable problems and Gödel** (PDF pp. 61–64, 71–72 / printed pp. 59–62, 69–70). | General algorithmic undecidability is real. It does not by itself establish that a human can reliably solve a specified undecidable problem, or that the brain is a physical oracle. The Lucas–Penrose inference depends on contested premises about human mathematical insight and soundness; see [1](https://iep.utm.edu/lp-argue/). |
| **Evolution and open-system plasticity** (PDF pp. 73–75 / printed pp. 71–73). | History, embodiment, environmental exchange and plasticity may be important and difficult to model. Their importance does not prove that a model must literally rerun the entire historical evolutionary process or that it cannot reproduce some relevant interactions by other means. |
| **Protein-folding search** (PDF pp. 67–68 / printed pp. 65–66). | An exhaustive search through a huge configuration space can be infeasible; it does not follow that all useful algorithms must exhaustively search it, or that a protein solves a general NP-hard optimization problem. [1](https://www.nature.com/articles/s41586-024-07487-w) reports major computational advances on structural prediction while also explicitly describing limitations, including dynamics and incorrect conformations. That result is not a simulation of a whole brain or proof of conscious AI. |

Nor does a finite-speed computer necessarily need to run at the original brain's wall-clock speed for every question: an entirely simulated environment might evolve on the same slower simulated clock. In a **real-time interaction with an unmodified external environment**, speed mismatch can indeed be an important constraint; whether experienced time itself is preserved in a slowed implementation is an additional unresolved psychophysical question.

### A limited mathematical check

The book links continuous, feedback-coupled processing to noncomputability. The established theory of [1](https://ar5iv.labs.arxiv.org/html/1310.8278) gives computability results for specified Lipschitz ODE solution functions under its stated assumptions. As a small explicit check, [`verification/continuous_feedback_digital_approximation.py`](verification/continuous_feedback_digital_approximation.py) approximates

```
x′ = y,    y′ = −x,    x(0)=1, y(0)=0
```

using only rational Euler updates over `0≤t≤1`. The analytic solution is `(cos t, −sin t)`, and a standard error estimate gives

```
error at t=1 ≤ [(1+1/n)^n−1]/(2n) ≤ (e−1)/(2n).
```

At 1,024 steps the computed error is about `0.0004884`, below the bound `0.0008384`. This is a **two-variable dimensionless counterexample to the general inference** “continuous reciprocal feedback ⇒ impossible to digitally approximate.” It is not a neuronal model, an argument that every physical field is computable, a real-brain resource estimate, or evidence that a numerical simulation would feel anything.

## 5. Implications for Bostrom, without overstating either side

[Bostrom's original argument](https://simulation-argument.com/simulation/) assumes that a suitably detailed computational implementation can have conscious experience; it does not purport to prove this premise. It considers many simulated human-like minds, not merely realistic-looking output. Its trilemma also depends on empirical and self-location assumptions and does not independently determine which disjunct holds.

| Candidate bridge from implementation to experience | Consequence for the literal digital ancestor-simulation scenario |
|---|---|
| Suitable computation is sufficient | Many simulated subjects or perspectives are possible in principle; population weighting still needs justification. This is the conditional route Bostrom adopts. |
| Particular causal electromagnetic/biological properties are required | A software description **alone** is not enough unless the host implementation also realizes the relevant properties. Whether artificial or analog realizations could do so depends on the actual criterion. |
| The book's strong claim: no Turing-machine implementation can realize the relevant higher brain functions | If, in addition, the specific inaccessible functions or properties are necessary for the simulated agents' conscious experiences, digital simulations on the excluded substrates do not supply the assumed conscious observers. The premise of Bostrom's standard argument then fails for that class. Neither necessity nor the claimed general no-go has **been demonstrated**. |

One must distinguish a simulated field represented in software from a field physically instantiated in the host hardware, and also distinguish either from phenomenal experience. Which physical features would suffice is the disputed bridge. A simulation need not have the *same* microscopic substrate if substrate independence is true; if it is false, the necessary physical properties must be specified rather than assumed.

In a restricted example with `B>0` base-level human-like experiencers and `S` relevant digitally simulated experiencers, if an independently justified theory makes `S=0`, the simulated fraction `S/(B+S)` is zero for **that class**. It says nothing by itself about other kinds of artificial implementation, non-digital simulations, different host physics, or the actual reference class. And if Bostrom's substrate premise fails, it is invalid simply to invoke his original trilemma and infer that one of the other disjuncts must therefore hold; its premises must be reconsidered.

## 6. Plurality versus a universal subject

The comparison becomes two separate questions:

1. **Are there multiple conscious people, whether biological or simulated?** The book's focus on individual brains makes local plurality a natural working reading; it does not prove metaphysically irreducible subjects or show that brain-to-brain communication joins or separates subjectivity.
2. **Can a digital simulation instantiate any of those people as experiencers?** Bostrom assumes a positive answer under conditions; the book argues strongly against it, but does not establish the claimed no-go.

A universal-consciousness interpretation could describe individual brains as limited perspectives of one universal subject, but that is **not what the book derives**. Nor should a non-agentive common physical field be relabeled as the agentive universal consciousness the user had in mind. Conversely, a pluralist can accept one shared physical/experiential ground without claiming that the whole is one subject.

Under the user's adopted premises `perfect whole ⇒ best universe` and `our universe not best`, the whole is not perfect. Neither this book nor the simulation argument proves plurality from that conclusion; a non-perfect universal subject is a separate possibility. Nor does either prove `possibility = actuality`, a timeless fundamental reality, or the emergence of local spacetime.

## 7. The next actual test

For the book's most constructive contribution, formulate a pre-registered **field-causality bridge**, not an immediate consciousness verdict:

1. Specify the neuronal/white-matter-derived field component, its spatial extent, source model, strength and time window; quantify measurement uncertainty and compare alternative neural sources.
2. Identify an intervention or natural contrast that changes the candidate field component while measuring and bounding concomitant changes in neuronal, synaptic and sensory inputs. Show whether selective manipulation is physically feasible; do not assume TMS or tES selectively targets endogenous fields.
3. Predict a quantitative difference between a field-feedback model and a matched neural-only or common-input model on held-out data. Compare spike timing, behavior and available first-person reports with appropriate controls.
4. Separately specify why the measured mechanism would constitute an experience rather than merely influence its physical correlates; use independently justified report/error bounds. The [random-audit proposal](RIVALRY_RANDOM_AUDIT_EXPERIENCE_BRIDGE.md) illustrates the remaining assay problem but does not solve it.

A positive field effect would support a causal physiological role, not alone hypercomputation, digital impossibility, consciousness identity or subject plurality. A negative or small effect within one measurement window would not rule out all field theories. At present, the complete bridge and required experiment remain open.

## Verification

Run `python verification/continuous_feedback_digital_approximation.py` for the restricted numerical check and see its [receipt](verification/continuous_feedback_digital_approximation.json). The quantitative bound is a standard Euler-error calculation; the finite checks are not a proof about actual brains. This audit is an evaluation of selected arguments and evidence, not an independent validation or refutation of the whole book.
