# Full roof-duality papers and a robust selector check

## Sources and exact coverage

The two files supplied by the user resolve the previously disclosed PDF access failures:

- Vladimir Kolmogorov and Martin Wainwright, [*On the Optimality of Tree-Reweighted Max-Product Message-Passing*](sources/uploads/1207.1395v1.pdf), [arXiv record](https://arxiv.org/abs/1207.1395). Eight PDF pages, SHA-256 `22e3f74c70f186a447f416e5646b2acf8746f3926ccef5ca1dd2f1e4efa3a42f`; extracted text of all pages was read. Pages 4, 6 and 7 were rendered to check the statements of Theorem 2, Corollary 1, Theorems 3–4 and the weak-persistency discussion.
- Carsten Rother, Vladimir Kolmogorov, Victor Lempitsky and Martin Szummer, [*Optimizing Binary MRFs via Extended Roof Duality*](sources/uploads/RKLS-TR07.pdf), [original link](https://pub.ista.ac.at/~vnk/papers/RKLS-TR07.pdf). Fifteen PDF pages, SHA-256 `80d9eee9b2de5e3ea460f5d6fa7de469b8b5292195c5abc70e8fb2623e9e9da9`; extracted text of all pages was read. Pages 3, 4 and 6 were rendered to check the weak/strong statements, probing, and the three-bit energy.

Reading extracted text and selected images is not an independent line-by-line proof audit. Neither study's implementation, figures in full, experiments, or data have been replayed. The older Hammer–Hansen–Simeone original paper is cited by both but remains unread in full. The separate Wainwright–Jordan monograph has now been fully text-read across turns, but not fully proof- or figure-audited: see [its coverage register](EFT_AND_GRAPHICAL_MODELS_READING_PROGRESS.md).

## What the actual papers establish, with qualifications

1. **Tree agreement and partial assignments.** Kolmogorov–Wainwright Theorem 2 assumes a binary pairwise model, a suitable tree reparameterization and a weak-tree-agreement fixed point. It says there exists an optimum agreeing *simultaneously* with all variables uniquely specified by the consistent tree family. This is a weak-persistency guarantee, not a claim that every optimum agrees. Their Theorem 4 gives optimality of the corresponding relaxation under their stated binary/WTA assumptions, not a general guarantee that an arbitrary iteration converges to an exact complete solution. Their discussion explicitly characterizes the related Rhys result as weak persistency.
2. **A route to strong information.** Their Corollary 1 gives a lower bound on the difference of opposite-label min-marginals for a fixed node; if the stated bound is strictly positive, all global optima have that label. The corollary's proof is omitted in the supplied paper, and we have not independently proved it in general. Strong tree agreement can certify an optimal complete configuration, but by itself does not make that configuration unique.
3. **Which cut matters.** Rother et al. §2.2 distinguish weak persistency for a QPBO partial labeling from strong persistency for the special `x_min` labeling. They describe `x_min` using the minimal minimum cut and note that the larger `x_max` labeling can depend on the chosen cut. Their stated strong-persistency result is not that every fractional LP optimum has the strong property. Their Appendix A refers elsewhere for the full proof of the strong property; we did not independently verify that external proof.
4. **Probing and improvement differ.** Their QPBOP uses strongly persistent labels after fixing a variable to each alternative; shared consequences can fix or contract nodes while retaining a mapping of global minimizers, under their assumptions and sufficient hard-constraint capacities. QPBOI is an energy-improvement method; it need not find the global optimum in general. They give a three-variable nonoptimal stable example and a complexity result about testing their stronger QPBO stability. A *single-spin local minimum* is a weaker notion than QPBO stability and is not evidence that an implementation is QPBO-stable. Their benchmarking results concern specified vision instances and are not reproduced here.

These sources sharpen, rather than cancel, the [earlier exact counterexample](GRAPHICAL_RELAXATION_PERSISTENCY_AND_SUBJECT_LIMITS.md) to the monograph's literal blanket strong-persistency wording. They also show that strong certificates are available with extra conditions. None of the established algorithms or derivations is claimed as a project invention.

## A finite margin test under explicit uncertainty

The published three-variable example is

```text
E(x,y,z) = 3|x−y| + 3|y−z| + 2xy + (1−x)(1−y).
```

[`verification/roof_duality_robust_boundary_gate.py`](verification/roof_duality_robust_boundary_gate.py) and its [receipt](verification/roof_duality_robust_boundary_gate.json) enumerate all eight binary configurations with exact rational arithmetic. At the nominal coefficients, `000` is the unique global minimum with energy `1`; `111` has energy `2` and all its single-bit neighbors have larger energies (`3`, `6`, `5`). The source additionally states that `111` is QPBO-stable, but our script does **not** implement or test QPBOI.

As a project-specific stress test of the objective—not a claim from the paper—let the four coefficients vary independently within `±1/4` of their nominal values. For a fixed reference `x*` and a rival `y`, with energy `Eθ(x)=θ·φ(x)`, the smallest possible energy difference over this box is exactly

```text
Eθ₀(y) − Eθ₀(x*) − Σk δk |φk(y) − φk(x*)|.
```

The script checks this elementary linear-box calculation for every rival and checks all 16 box corners. The smallest worst-case gap is `1/2`, so `000` is the unique minimizer throughout this **stipulated** box. At one allowed perturbation of radius `1/2`, coefficients become `(3,3,3/2,3/2)` and `000` and `111` tie; at a particular radius `3/4` perturbation `(3,3,5/4,7/4)`, `111` becomes the unique minimum. The radius is a sensitivity parameter, not an estimated error bar. These results establish neither a real neural boundary nor a new general optimization theorem.

## How to use this in the framework

A candidate boundary can be considered **robustly fixed within a declared model class** only when alternative assignments are excluded across all allowed parameters and context, not merely when one run returns a label. In a finite linear model, the rival-specific margin above gives one exact sufficient test for a chosen complete reference; for larger systems, properly qualified min-marginal or relaxation bounds may help. An optimizer whose bound is positive must still be checked against the *correct* admissible set: hidden interactions, dynamic states, gauge transformations, and the observation/intervention model may change that set. If error bounds are unsupported, robustness remains conditional.

This is a practical improvement to the framework's bookkeeping of uncertainty and ties. It does not justify the objective function, establish phenomenal identity, determine subject boundaries in nature, prove self-existence or plenitude, or solve the problem of time. Multiple local subjects remain possible without introducing a universal subject or an external agent.
