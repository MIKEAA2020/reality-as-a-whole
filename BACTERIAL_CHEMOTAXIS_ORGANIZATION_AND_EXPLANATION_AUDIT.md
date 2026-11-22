# Bacterial chemotaxis: what organization explains, and what it does not

## Bottom line

A real example supports the strongest part of [Jaworski's argument](JAWORSKI_2016_BIOLOGICAL_STRUCTURE_AND_FRAMEWORK_AUDIT.md): **what components do together depends on their organized interactions, not merely on an inventory of their ingredients**. In *E. coli* chemotaxis, receptor activity, chemical modification and feedback jointly help restore signalling after a persistent attractant stimulus. A control-theoretic description explains why adaptation can be relatively insensitive to some changes, while component-level mechanisms explain how the feedback can operate and where it can fail.

The evidence does **not** establish that biology is beyond physics. The mechanistic and organizational accounts can be complementary descriptions of the same experimentally studied pathway. Nor does this subsystem constitute a complete theory of organism identity or establish bacterial experience. It provides a concrete constraint on our framework's treatment of realized organization, not a solution to phenomenal subjecthood.

The analysis is exploratory and retrospective: the [plan](CHEMOTAXIS_ADAPTATION_MECHANISM_AUDIT_PLAN.md) was written after abstracts and search results revealing both robust adaptation and its limits had been seen. No experiment or original simulation was rerun.

## 1. The system and what adaptation means

Motile *E. coli* alternate relatively straight **runs** and reorienting **tumbles**. Chemical changes influence the timing of these motions, biasing a random walk; the bacterium does not need to move directly toward a source at every instant. In the pathway described by [Neumann et al. (2014)](https://doi.org/10.1371/journal.pone.0084904) and [Yi et al. (2000)](https://doi.org/10.1073/pnas.97.9.4649):

1. Receptor complexes, including the kinase CheA and adaptor CheW, respond to attractants. An attractant increase generally reduces kinase signalling.
2. CheA-dependent phosphorylation of CheY affects flagellar motor switching; CheZ helps dephosphorylate CheY. The relationship between pathway activity and actual swimming is a further link, not an identity.
3. CheR methylates receptors, generally increasing activity; CheB demethylates them, generally reducing activity. Their activity-dependent actions form a feedback process that can counteract a sustained change in stimulation. CheB also has a deamidation function, important when interpreting the mutant below.

**Adaptation** here is the recovery of a specified signalling output toward its pre-stimulus level *while the changed stimulus remains present*. It is not necessarily genetic adaptation, complete recovery of every variable, return of the molecular system to its original state, or proof of an optimal response. Perfect adaptation is an exact mathematical ideal; real measurements have finite precision and finite observation times. The system can have a similar output at different persistent ligand levels while its receptor modification state differs.

## 2. What the primary studies report

| Source | What was done or analyzed | What it supports—and its limits |
|---|---|---|
| [Alon et al. 1999](https://doi.org/10.1038/16483), *Nature* | The available abstract reports experiments systematically varying intracellular chemotaxis-protein concentrations. Adaptation precision was reported robust across those tested changes, whereas baseline behavior and adaptation time could vary strongly. | Useful evidence for **selective** robustness, not invariance of all properties or all perturbations. Only the abstract and figure titles were accessible; I did not inspect the full methods, figures, estimates, or raw data. |
| [Yi et al. 2000](https://doi.org/10.1073/pnas.97.9.4649), *PNAS* | Analyzed the Barkai–Leibler biochemical model using control theory, deriving an integral-feedback form under stated kinetic assumptions. Their necessity argument uses a stable linearized class and extends to nonlinear systems in the sense discussed in their appendix. | A mechanistic **model analysis**, not a new direct experimental measurement of every assumption. The paper itself notes uncertainties and possible violations. It does not prove every adaptive mechanism is literally the same circuit. |
| [Neumann et al. 2014](https://doi.org/10.1371/journal.pone.0084904), *PLOS ONE* | Measured stimulus responses using a CheY-YFP/CheZ-CFP FRET reporter, compared strains and a `cheB` mutant, measured growth separately, and simulated navigation using RapidCell. | Reports a gradual loss of precision with stronger stimulation. The saturation mechanism is a supported interpretation, not uniquely proven by these data. Navigation results are simulations, not direct measurements of those simulated trajectories. |
| [Hansen et al. 2008](https://doi.org/10.1371/journal.pcbi.0040001), *PLOS Computational Biology* | A stochastic molecular **model** of interacting receptors and dynamic CheR/CheB “assistance neighborhoods,” compared with prior experimental constraints. | Shows how a candidate clustered mechanism can produce broad adaptation and how kinetic or neighborhood assumptions limit it. It is not direct evidence that every modeled detail holds in vivo. |

These sources share intellectual history and some authors or laboratories; they are **not four independent replications** of the same experiment. The 2014 paper explicitly reuses some earlier data. Below, source results are author reports, not our reanalysis.

### The 2014 experiment in more detail

The authors exposed attached cells to step-like attractant additions and removals in a flow chamber. The FRET reporter relies on phosphorylation-dependent CheY–CheZ interaction and is used as a readout of pathway kinase activity; it is not a direct measurement of every receptor's methylation or of each cell's swimming direction. Their strains included deletions of native `cheY`/`cheZ` and expression of the tagged reporter pair, so the measurement is a constructed assay, not an unmodified wild organism in its natural environment.

For the authors' definition, **imprecision** was the buffer-to-ligand-adapted YFP/CFP ratio difference, normalized to the response amplitude for a saturating 100 µM MeAsp stimulus; **precision was `1 − imprecision`**. The adaptation time was the time to recover half of the initial loss in activity. Slow photobleaching caused a baseline drift, corrected by linear interpolation between buffer measurements; the authors discuss possible interpolation error. These details matter: their precision measure is not automatically identical to the simple post/pre activity ratio used in other models. The paper says error bars represent standard errors for multiple measurements, but the inspected text does not support a precise independent sample-count or uncertainty reanalysis here.

Across the tested attractants the authors report decreasing precision as the initial stimulation becomes stronger, with ligand-specific concentration dependence. Similar dependencies were observed in two strain backgrounds. Their `cheB`-deficient comparison approximated a highly modified receptor state, because CheR action was not counterbalanced and CheB also affects deamidation. Its response at high attractant was consistent with a methylation-limit explanation, while imprecision appeared already below the concentrations that inhibited the highly modified mutant. This supports, but does not by itself uniquely identify, limited available modification sites as the cause; altered mutant properties, reporter interpretation and other model assumptions remain relevant.

The authors also measured reduced growth at high serine or cysteine in particular media and separately simulated chemotactic movement. Their suggestion that reduced adaptation might have been selected to prevent accumulation at harmful concentrations is **a hypothesis**, not a demonstrated evolutionary explanation. In their simulation, reduced precision had different effects on drift and accumulation near an attractant peak; this is a model-dependent prediction, not a directly observed behavioral effect from that figure.

## 3. The control principle and its assumptions

Yi et al. explain that, in an idealization of the Barkai–Leibler model, a variable `z` approximating total receptor methylation can obey

```text
dz/dt = r − bA,
```

where `A` is receptor-complex activity and `r,b` are effective rates. If `r` and `b` do not depend on the persistent ligand level, and the system reaches an unconstrained steady state with `b > 0`, then `dz/dt = 0` implies `A = r/b`: the adapted activity is independent of that ligand level. The integrated error changes `z`, and `z` feeds back on `A`. **Convergence and an accessible steady state are essential**; the equation alone does not prove stability, adaptation after every disturbance, or that a finite biochemical system has unlimited adjustment range.

Yi et al. list four model assumptions, including strongly activity-dependent CheB action, constraints on reaction-rate dependencies, low activity of unmethylated receptors, and ligand-independent bound CheR. They explicitly note that some experimental support was indirect or uncertain. The adapted baseline can depend on enzyme concentrations and rates: robustness of the *return to that baseline* under a ligand change is not the claim that the baseline is unchanged when those rates change. The later clustered-receptor model adds biological detail but introduces its own assumptions. These are interacting biochemical processes, not an independently observed disembodied controller.

### A checked illustration—not a fitted bacterial model

To make the logic and its limitation explicit, we constructed a separate dimensionless example:

```text
A(z,L) = (1+z)/(1+z+L),       dz/dt = k (1/2 − A),     k > 0.
```

For a fixed input `L > 1` and an unconstrained controller starting at `z=0`, the equilibrium is `z*=L−1` and `A*=1/2`. Since `A` increases with `z`, the drift points toward that equilibrium, which is asymptotically stable. Changing `k` changes the rate, not this equilibrium. At a step from `L=1,z=0` to `L=2`, activity immediately falls from `1/2` to `1/3` and then returns asymptotically to `1/2`. If `z` is frozen instead, activity remains at `1/3`.

Now impose `0 ≤ z ≤ 2`, preventing outward movement at the boundaries, and step to `L=8`. The ideal equilibrium would require `z=7`, outside the allowed range. The constrained trajectory reaches `z=2`, where `A=3/11≈0.273`, not `1/2`. At that boundary the *unconstrained* controller still demands an increase, but the projected derivative is zero. Thus one cannot conclude `A=1/2` merely from zero constrained movement. This is a simple mathematical illustration of an adjustment limit, **not a quantitative model of methylation-site saturation in the experiment**.

The [checker](verification/chemotaxis_integral_feedback_example.py) compares Runge–Kutta trajectories with a separately integrated scalar solution; [five tests](verification/chemotaxis_integral_feedback_example_test.py) check exact equilibria, boundary error, monotonicity, gain and numerical agreement. They passed, as did the five prior turnover tests and 45 selected framework regression scripts. A [receipt](verification/chemotaxis_integral_feedback_example.json) records the illustrative values. No empirical parameters were fitted, and the trajectories are not experimental data.

## 4. What does the organizational explanation add?

The feedback description identifies **a counterfactual pattern**: within specified assumptions and a stable feasible domain, an output returns to its baseline despite changes in a persistent input. It explains why certain parameter changes need not destroy adaptation and why response time, baseline, saturation and other properties can still vary. This is more informative for that question than listing proteins independently.

The molecular account explains **how** the relevant feedback may be realized: receptor binding, kinase signalling, methylation/demethylation, enzyme kinetics and receptor interactions. It also provides ways to alter or limit it. Neither level replaces the other automatically. A topological diagram without kinetics, state, boundaries and resources does not establish stable adaptation; a catalogue of molecules without interactions does not derive the functional response.

In the constructed example, the exact macro-property follows from explicitly specified lower-level equations and constraints. That demonstrates the logical possibility of explaining an organized property through a structured mechanistic model while treating it as real. It does not establish that the toy equations are fundamental physics, that this is an exhaustive molecular account, or that every biological explanation reduces to a particular micro-description.

## 5. Jaworski and the framework

A physicalist organizational realist can accept the importance and reality of the feedback network and also hold that its relations and dynamics are physically realized. A hylomorphist can agree with all measured effects but argue that the realized biological organization is not exhaustively captured by physics. **If both accounts predict the same responses, these observations alone do not decide which grounding claim is true.** A version that predicts a distinct intervention outcome could be tested only after specifying that outcome, the physical comparison model and relevant controls. No such additional predicted effect is supplied by this audit, and lack of one does not by itself refute hylomorphism.

The experimental case therefore strengthens Jaworski's challenge to a mere-parts inventory, but not his further conclusion that all possible physical descriptions must omit biological structure. Conversely, the existence of biochemical models does not by itself prove that the idealized model exhausts the organism or that strong physicalist completeness is true.

For our framework the practical upshot is that a proposed organization must specify **variables, interactions, timescales, environmental inputs, constraints, and interventions**, not just a name or graph. Biological persistence, information about prior stimulation, and response regulation can all be analyzed without declaring them conscious. The pathway is a **subsystem**, not the entire organism's self-maintenance. Nor does the fact that a bacterium adapts establish or rule out experience. A subject/episode and qualitative-character rule, with credible independent access and calibration where applicable, remains a separate unresolved obligation. No conclusion about the necessity, timelessness, or intrinsic experiential nature of the whole follows from this case.

## Source-access and verification ledger

- **Neumann et al. 2014:** read the main HTML text, Methods and figure/supplement captions. Figure images, supplemental image files, raw FRET traces, underlying data, analysis scripts and RapidCell runs were not inspected or reproduced. Some Figure 1B data are replotted from an earlier study.
- **Yi et al. 2000:** read the principal HTML text, its key ideal equations and control-theory appendix. Supplemental derivations and figure images were not independently inspected; the full biochemical model was not reconstructed.
- **Hansen et al. 2008:** inspected abstract, introduction, selected discussion and methods, including simulation procedure; not every model equation, figure image, parameter or supplemental result was independently checked. It is a modeling paper, not a fresh observational confirmation of all components.
- **Alon et al. 1999:** publisher abstract and figure titles only; full article and original data were inaccessible in this environment. Avoid asserting its individual numerical estimates or exact controls from this audit.
- **Jaworski 2016:** all pages of the user-supplied article were read in the [prior audit](JAWORSKI_2016_BIOLOGICAL_STRUCTURE_AND_FRAMEWORK_AUDIT.md). His book and the older primary works quoted in that article were not independently examined here.
