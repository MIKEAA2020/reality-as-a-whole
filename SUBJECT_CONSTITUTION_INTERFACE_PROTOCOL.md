# Frozen finite constitution-and-record comparison: protocol

## Purpose and status

This is a **precommitted mathematical test**, not a registered human experiment and not a genuine preparation of subjects. The definitions below are fixed before running the new comparison script. They integrate the existing four-spin subject rules and the experiential-versus-neutral grounding rival; they do not replace the frozen framework dossier or its admission criteria.

The aim is to separate three questions that are often conflated:

1. Does a physical model determine a proposed phenomenal contrast?
2. If an added report channel is assumed accurate, do two subject-rule packages give different record distributions?
3. Can even a perfect observation of that contrast distinguish an experiential *base* from a neutral base when they deliberately share the same incidence rule and all operational predictions?

## Fixed physical interface

Use the existing four-spin chain and exact equilibrium law in [the competing-rule audit](COMPETING_SUBJECT_CONSTITUTION_AND_LOCALITY_GATE.md), including its kinetic-model-inspired interventional edge graph and assumptions. Vertices are `V={0,1,2,3}`, all eligible. Nearest-neighbor couplings in the equilibrium weight are `1/2,t,1/2`, with two settings only: source `t=0`, target `t=1/4`. A trial consists of one fresh equilibrium draw of all four spins. The physical record `Q` is `1` exactly when endpoint spins agree. No empirical application or real access to spin-level phenomenal content is claimed.

Compare the existing connected-component incidence rule **C** and the existing overlapping-local-maxima incidence diagnostic **L**, defined in `verification/competing_subject_constitution_rules.py`. A selected subset is **stipulated** to be one local subject with the tuple of its vertices' spin labels as its content. `Z=1` if some selected subject contains both designated endpoints 0 and 3; otherwise `Z=0`, provided the diagnostic resolves its selection. An unresolved tie is a third status, not `Z=0`. This is a subject-incidence postulate; spin labels are not actual qualitative feelings.

The graph, spins, permitted operations, selected subsets, contents and endpoint target must be transported together under vertex relabelings. At the two settings, the code will check all 24 relabelings. It will also inspect the additional uniform-coupling tie `t=1/2` as a **negative control**, not choose a tie-break after seeing the output.

## Three distinct packages

All three packages use exactly the physical spin preparation above and the same hypothetical phenomenal label definition. They are finite formal encodings with additional philosophical postulates; they are not demonstrations that either kind of ground exists.

- **XC:** experiential-base interpretation plus C. Its elementary input consists of the complete encoded graph and spin tuple, stipulated to describe an experiential constitution. The `F` map projects those inputs to the corresponding graph and physical spin tuple; `S` applies C. This projection does not derive the graph or dynamics: the relevant physical content is already in the input.
- **XL:** the same experiential-base interpretation and `F`, but `S` applies L.
- **NL:** neutral-base interpretation with the same encoded graph and spin tuple; a stipulated phenomenality bridge assigns the *same* episodes as XL, and `F` projects to the same physical tuple. The neutral root and bridge are not established; this is not a theory of how non-experience creates experience.

The single `S` rule in each package yields both episode labels and the endpoint contrast. The status of these labels as *actual subjects and feelings*, the validity of F and the necessary existence of either ground are assumptions or open questions. The input types do not, by themselves, establish distinct metaphysical possibilities or an external time or simulator.

## Report bridge and two distinct tests

1. **Unmodified physical comparator.** In each setting let `R=Q`, so this record is specified purely by physical endpoints. Its distribution is fixed by the common spin law, independent of the proposed subject label. Calculate `P(R≠Z)` separately for the rules at the source and target. This directly checks whether the additional claim “this physical comparator is a highly accurate target assay” is compatible with each package. No inference from `Q` to phenomenal identity is allowed without that separately assessed bridge.
2. **Hypothetical target-valid assay.** In a separate, explicitly modified output model, append a new binary physical record `R*` such that `P(R*=Z)=9/10` in both source and target, with independent errors across independently prepared trials. `R*` is generated conditionally on the stipulated Z and is not the existing comparator Q. The spin distribution is unchanged, and XC, XL and NL use the *same declared channel*. This is a new psychophysical/readout assumption with no empirical calibration. It may equivalently be implemented by a physical device programmed to evaluate the chosen graph rule and add an independent bit flip; such implementation would not prove that its output accesses a subject's experience.

For the target assay test, prepare `n=21` independent target-condition trials; choose XC if at least 11 records say yes, otherwise choose the L packages. Calculate exact binomial probabilities under the stipulated channel. There is no nonresponse in this fictional protocol; a real application must preregister nonresponse, dependence, target-condition calibration, selection bias and first-person access separately. A rejectable package includes both the constitution rule **and** the assay and preparation assumptions; its failure does not identify which one was false.

For the experiential-versus-neutral test, hold L and the entire spin, label and report law fixed while changing only the asserted grounding from XL to NL. Verify that their full finite joint `(spin,Z,R*)` distributions coincide at each specified setting, and that even an ideal observer given Z cannot distinguish their grounding direction from these data. This is equality by construction, not a proof that all experiential and neutral theories are empirically equivalent.

## Reproducibility and limits

The companion script `verification/subject_constitution_interface.py` imports the earlier rules and exact equilibrium calculations, checks output probabilities and transported relabelings, and writes `verification/subject_constitution_interface.json`. The script fixes all settings, candidate rules, outcomes, noise, sample size and majority threshold before execution. The script's exact arithmetic and finite assertions check this constructed interface only; their result is not an empirical subject assay, proof of intrinsic experiential nature, a measure for self-location, recovery of fundamental physics, or a pass of the formal battery. No actual data are being held out, and no synthetic fit is being presented as preregistered experimental validation.
