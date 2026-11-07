# OPH unification: source-chain and falsifiability audit

**Scope.** The live [unification overview](https://learn.floatingpragma.io/unification) and selected chapters of its two books, compared with the author's public repository at commit [`3cf3c14810671a16e61b7915f69079a1773a12a2`](https://github.com/FloatingPragma/observer-patch-holography/tree/3cf3c14810671a16e61b7915f69079a1773a12a2). The live textbook is not itself pinned to that commit; numerical or textual discrepancies need a version/branch crosswalk, not an assumption that every displayed row has identical ancestry. Accessed 7 November 2026. Not a full audit of the entire construction or Lean development.

## Bottom line

The overview is valuable as an unusually explicit attempt to connect a timeless observer/record architecture to physics. But **its unconditional presentation of unique physical closure, recovered Standard Model plus gravity, and zero adjustable physics is stronger than the status established by the pinned research program**. Its own ledger lists five same-construction requirements as unmet: physical clocks, interacting 3+1-dimensional Standard Model QFT, particle identification and spectrum, realization of the gravity premises, and empirical validation. See the [executable hypothesis, EMH-1–5](https://github.com/FloatingPragma/observer-patch-holography/blob/3cf3c14810671a16e61b7915f69079a1773a12a2/docs/OPH_EXECUTABLE_HYPOTHESIS.md).

This does **not** prove the program impossible, invalidate every mathematical component, or demonstrate hidden fitting in every numerical lane. The useful question is whether the **same** source process supplies all these objects with a target-independent ancestry and tested readouts.

## 1. A precise check: positivity does not force Koide

The overview says positivity of a face circulant confines the three masses to a chamber where their Koide combination is exactly 2/3. The [pinned technical Koide paper](https://github.com/FloatingPragma/observer-patch-holography/blob/3cf3c14810671a16e61b7915f69079a1773a12a2/extra/koide_identity_from_positive_c3_face_circulants.tex) is more precise: for a Hermitian cyclic matrix with diagonal `a`, complex off-diagonal `b`, and positive eigenvalues interpreted as square-root masses,

```
Q = (m1+m2+m3)/(√m1+√m2+√m3)²
  = 1/3 + (2/3)(|b|/a)².
```

Thus **Q = 2/3 exactly when |b|/a = 1/√2**. Positivity by itself does not force that ratio. For example

```
C = [[2,1,1], [1,2,1], [1,1,2]]
eigenvalues = (4,1,1) > 0
Q = (16+1+1)/(4+1+1)² = 1/2.
```

Even distinct positive eigenvalues do not rescue the implication: the Hermitian cyclic matrix with first row `(3, 1+i, 1−i)` has eigenvalues `5, 2−√3, 2+√3`, all positive and distinct, and `Q=13/27`. [Our exact-arithmetic check](verification/oph_unification_koide_gate.py) also verifies 675 strictly positive integer real-circulant examples. Its [receipt](verification/oph_unification_koide_gate.json) records the scope.

**What this does and does not show.** The technical source itself isolates a separate equal-block/balance condition and a separate physical attachment of eigenvalues to the charged leptons; its abstract explicitly calls the balance target-informed, chosen from the measured charged-lepton triple. It is not making the simplistic algebraic mistake attributed here to the overview's wording. The examples need not satisfy those extra assumptions. They refute **positivity plus cyclic symmetry alone ⇒ Koide**, not the stronger conditional source theorem or OPH as a whole. The identity is the authors' stated result, not a claimed novel discovery here. The [empirical/postdiction ledger](https://github.com/FloatingPragma/observer-patch-holography/blob/3cf3c14810671a16e61b7915f69079a1773a12a2/docs/POSTDICTION_LEDGER.md) describes the tau window as conditional and retrospective, using the measured electron and muon masses—not an independent prediction of all three absolute masses.

**Decisive next gate:** derive the equal-block balance from the same actual observer process, without importing the lepton answer; then independently show that its three response eigenvalues are the three appropriately defined physical lepton square-root masses, including the pole/running and uncertainty bridge. Check all three masses and other charged-sector properties on that same object. A finite balance theorem alone is not this gate.

## 2. The horizon number: a named but unfinished selector

[Machine chapter 14](https://learn.floatingpragma.io/book/machine/chapter/14) correctly observes that a fixed-point equation does not by itself pick a unique capacity: the identity and erasure maps behave differently. It nevertheless claims a unique, stable physical slack zero and a horizon-record identity. That is a **stronger claim** than generic self-reference and requires the specified source-family theorems and physical attachment.

At the pinned commit the authors' [direct-N verdict](https://github.com/FloatingPragma/observer-patch-holography/blob/3cf3c14810671a16e61b7915f69079a1773a12a2/code/capacity_readback/runtime/direct_n_closure_verdict.json) explicitly says direct `N` is *not evaluable*, with no direct numeric N or cosmological comparison permitted. Its finite-rung controls include reversible and erasure examples, but it explicitly does **not** claim a complete-source nonidentifiability theorem: universal source-contract membership and the executable-to-Lean bridge are open. The [named-law verdict](https://github.com/FloatingPragma/observer-patch-holography/blob/3cf3c14810671a16e61b7915f69079a1773a12a2/code/capacity_readback/runtime/named_law_n_closure_verdict.json) similarly reports `NOT_EVALUABLE_NO_GLOBAL_CAPACITY_ATTACHMENT`; the associated [branch certificate](https://github.com/FloatingPragma/observer-patch-holography/blob/3cf3c14810671a16e61b7915f69079a1773a12a2/code/capacity_readback/manifests/n_closure_branch_certificate.json) retains finite-presence and Poisson/projective-limit branches as unselected, retrospective conditional arithmetic. The latter has a number near the overview's `3.3001×10^122`, but it uses its own declared inputs; numerical similarity does not establish that the live page consumes precisely that pinned branch.

The concrete bridge needed is a versioned proof that the relevant page's selector, all-rung admissible source family, global capacity action, physical horizon entropy, and the selected numerical branch are the same objects and that the live page's additional claims are discharged. The published source explicitly leaves these joins open. Nor does the existence of a finite fixed-point certificate, if valid, establish that the physical universe is that fixed point.

## 3. The cesium-to-SI bridge: source ancestry matters

The overview presents the cesium tick as a unit definition, not a fitted parameter. The fuller [Machine chapter 14](https://learn.floatingpragma.io/book/machine/chapter/14) claims to derive the required *dimensionless* native-to-cesium transition ratio without an experimental gravity input. This is a substantive claim: defining the SI second by the cesium frequency does **not by itself** determine a native fundamental length. One additionally needs a justified prediction of the ratio

```
γ = ℓnative νCs / c.
```

If γ is derived independently, `ℓnative = γ c/νCs`, and a separate justified identification of `ℓnative² = ħG/c³` would give `G = γ² c⁵/(ħ νCs²)`. (The author's certificate uses `εCs=2πγ`, hence its equivalent `1/(4π²)` form.) The exact SI conventions do not alone supply either physical derivation.

There is a particularly direct source-chain match: the pinned [no-G DAG certificate](https://github.com/FloatingPragma/observer-patch-holography/blob/3cf3c14810671a16e61b7915f69079a1773a12a2/code/particles/hierarchy/certificates/R_gamma_noG_DAG_certificate.json) lists `γ*=4.9559743365484…×10⁻³⁴`, the same candidate scale as the textbook's unit bridge. It labels its status `skeleton_passes_forbidden_gravity_path_check_but_missing_component_certificates`: the electroweak hierarchy component is partial, while the alpha, absolute electron scale, cesium-133 nuclear/QCD and cesium atomic components are **not supplied**. Its forbidden-input list is meaningful, but a graph skeleton excluding G is not the missing atomic and nuclear derivation. The live textbook's claimed completion would need to identify later/different certificates and establish the remaining links on the same branch.

Accordingly, the evidence does **not** justify saying this bridge is necessarily fitted to G. Nor does this pinned certificate establish a completed independent prediction of G from a cesium definition. The discrepancy is a concrete, traceable proof obligation.

## 4. Quantum fields, gravity, and Λ

The overview describes Lorentzian fields, spin/statistics, the Standard Model and gravity as readings of one process. Its components deserve individual credit, but the pinned [common executable hypothesis](https://github.com/FloatingPragma/observer-patch-holography/blob/3cf3c14810671a16e61b7915f69079a1773a12a2/docs/OPH_EXECUTABLE_HYPOTHESIS.md) says the interacting chiral 3+1 QFT, physical excitation/particle and clock identification, and same-source Einstein premises remain unestablished. Supplying a radial product, reference, action, state, or matter stress tensor is not the same as showing the native process selects them. This is exactly the common-object bottleneck in our earlier [repository and cutoff audit](OPH_REPOSITORY_AND_CUTOFF_BRIDGE.md).

The entropy/null-balance implication, conservation and Einstein tensor completion are conditional mathematics; obtaining their premises in one physical refining geometry is the central missing gravity bridge. In particular, null contractions miss any `Λg_ab` term. That mathematical point is correct; it does **not** imply all local curvature is insensitive to Λ. In a four-dimensional *vacuum Einstein solution* `R_ab=Λg_ab`, all null contractions `R_ab k^a k^b` vanish, yet the scalar curvature is `R=4Λ`. Our verifier checks this algebra on sample exact null vectors; it does not derive Einstein's equations. [Outputs chapter 17](https://learn.floatingpragma.io/book/outputs/chapter/17) itself acknowledges that local de Sitter curvature can be detected, while elsewhere in the same chapter saying no local measurement or calculation can ever fix Λ. Those statements need that qualification. Locally distinguishing a bare Λ from a separately unknown vacuum stress is a further identification problem; this is not a solution to the cosmological-constant problem.

The overview's displayed inverse fine-structure value, approximately `137.035660`, also differs by about 2.47 parts per million from the 2022 CODATA value, 137.035999177(21) [1](https://physics.nist.gov/cuu/pdf/wallet_2022.pdf). A physical test must specify the same low-energy observable, renormalization/transport corrections and an independently justified theory uncertainty. This numerical mismatch alone does not reject an incompletely specified full theory.

## 5. Relevance to the requested zero-residue account

- **Timelessness and local time:** A fixed global structure can contain ordered, changing subsystem histories. A native clock model is useful, but deriving a laboratory duration and compatible local proper times still requires the common-clock bridge; no external universal clock is necessary.
- **Self-reference and actuality:** A consistent or unique solution of a *specified* mathematical map does not alone establish the physical existence of that map, necessity of the supplied axioms, or the experience of its subsystems. This is not a request for a mechanism that turns genuinely possible worlds into actual worlds.
- **Subject and experience:** Operational observers, records, and overlap agreement are not automatically phenomenal subjects. The additional incidence, subject-boundary, unity and qualitative-character gates remain, including for the proposed alignment/discomfort identity. See [the deeper book audit](OPH_BOOK_DEEPER_READING_AND_QUANTUM_GATES.md) and [subject-pluralist synthesis](SUBJECT_PLURALIST_EXPERIENTIAL_SYNTHESIS.md).
- **Non-optimality:** Self-consistency does not entail perfection or the best world. Under the user's adopted conditional `perfect whole ⇒ best world` and premise that this world is not best, the whole is non-perfect. OPH's timeless whole does not by itself remove that tension or establish a universal conscious agent.
- **Parsimony:** Zero continuously fitted parameters would be notable *if established*; it is not the same as zero assumptions. The twelve-port carrier, allowed observer operations, coherence/consensus, continuum limits, physical identification and any selection laws each need their own justification.

## Prioritized next steps

1. **Ask for exact provenance/version crosswalks** from the live course to the pinned gamma component certificates and N selector. Accept the strongest completed certificates, not a forced binary verdict.
2. **Prioritize the common-process gate:** one source and refinement family furnishing calibrated clocks, physical preparations/instruments, an interacting matter field and stress response, plus the gravity premises, with explicit error bounds.
3. **Freeze a genuinely prospective distinguishing observable** before collecting/comparing the decisive data, with competing predictions, experimental confounders, uncertainty and rejection criteria. The conditional Koide tau calculation and retrospective horizon matches do not provide this by themselves. The earlier [C/E calibration gate](OPH_BOOK_DEEPER_READING_AND_QUANTUM_GATES.md) illustrates why apparatus coherence must be controlled.
4. **Keep phenomenal identity separate:** a physics/record success is necessary input, not a proof that a repair process is experienced or that a particular mismatch is discomfort.

## Verification and source limits

Run `python verification/oph_unification_koide_gate.py`. The positivity controls and the vacuum null-contraction control are elementary exact checks (the displayed radical ordering uses floating-point `sqrt` as a sanity check; positivity also follows exactly from leading principal minors `3,7,5`). The script is not an independent proof of OPH's whole source chain or its Lean certificates. In addition to the live course and pinned repository links above, compare the author's [observer-consensus technical overview](https://floatingpragma.io/oph/papers/from-observer-consensus-to-standard-physics/) and [prior deeper-reading assessment](OPH_BOOK_DEEPER_READING_AND_QUANTUM_GATES.md). CODATA citation: [1](https://physics.nist.gov/cuu/pdf/wallet_2022.pdf).
