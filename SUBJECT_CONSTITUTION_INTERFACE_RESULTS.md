# A subject-constitution and record interface: bounded results

## Decision

The [fixed protocol and executable specification](SUBJECT_CONSTITUTION_INTERFACE_PROTOCOL.md) were committed and pushed as `5ee21b6` **before** running the comparison. This was a precommitted *mathematical exercise*, not a preregistered human study or an analysis of new data. It joins the existing four-spin subject-boundary rules to the experiential-versus-neutral grounding comparison.

The result separates two questions:

1. Under an explicitly postulated, target-valid report channel, two subject-rule **packages** make very different predictions. But the physically defined comparator already in the spin model is nowhere near the assumed report accuracy, so it cannot serve as that channel.
2. Two interpretations that use the **same** subject rule and exactly the same complete joint distribution of physical records and phenomenal labels remain indistinguishable in this interface, even if the labels were given to an ideal observer. Thus a test of subject boundaries is not automatically a test of which metaphysical base grounds them.

Both results depend on the stipulated model. They do not establish actual subjects, validate an experiential foundation, or pass the substantive formal battery.

## 1. One interface and three packages

The input is the same four-spin chain and interventional influence graph used in the [competing-rule audit](COMPETING_SUBJECT_CONSTITUTION_AND_LOCALITY_GATE.md). We compare the connected-component rule C with the overlapping-local-maxima diagnostic L. Each selected subset is **stipulated** to be one subject; the endpoint contrast `Z=1` means that endpoints 0 and 3 belong to one selected episode.

- **XC:** experiential-base interpretation with C.
- **XL:** experiential-base interpretation with L.
- **NL:** neutral-base interpretation with L, and the same stipulated actual experiences as XL.

The toy maps physical structure by projection from an input that already contains the spin and graph description. Consequently it does **not derive physics from experience**; identifying that input as fundamentally experiential is an additional postulate. Neither the spin values nor subject labels establish real feelings. The neutral bridge is also stipulated, not independently justified. The candidates are formal comparisons, not a claim that incompatible unrealized total realities are genuinely possible.

| Coupling | C-selected subsets | L-selected subsets | `Z_C`, `Z_L` |
|---|---|---|---|
| `t=0` source | `{0,1}`, `{2,3}` | `{0,1}`, `{2,3}` | `0, 0` |
| `t=1/4` target | `{0,1,2,3}` | `{0,1}`, `{2,3}` | `1, 0` |
| `t=1/2` control | `{0,1,2,3}` | six tied candidates, unresolved | `1, unresolved` |

The last row is a critical negative control: L's empty strict-winner set is **not** interpreted as no experience or a negative Z. The script transports the graph, selected sets, unresolved ties and endpoint target under all 24 vertex relabelings at each setting and checks 144 rule-by-relabeling cases. This checks permutation covariance on the supplied factorization; it does not establish invariance under different subsystem decompositions, coarse-grainings or physical representations.

## 2. The original physical comparator fails the assumed assay standard

Under the common target spin law the physically defined comparator `Q=1` if the endpoint spins agree has

`P(Q=1)=17/32 ≈ 0.53125`.

The candidates assign `Z_C=1`, `Z_L=0`, giving:

| Candidate | Error of `Q` relative to stipulated Z |
|---|---:|
| C | `15/32 ≈ 46.875%` |
| L | `17/32 ≈ 53.125%` |

At the source where C and L both assign `Z=0`, the comparator error is `1/2`. Therefore a claim that **this** comparator has at most 10% error in the specified target condition is incompatible with **both** candidate packages and their shared spin law. It would not distinguish them; it would show that at least one component of each package—the physical model, subject label or assay claim—is wrong. The number is calculated from the idealized law, not measured in a person. In particular, endpoint spin agreement is not an independently anchored measure of one joint experience.

This is a useful gate on the construction: correlation or common physical readout does not become a phenomenal-unity assay by being attached to a subject rule. Other readouts could be better; this result does not prove that all conceivable assays fail.

## 3. An added accurate assay discriminates *packages*, conditionally

Now add the protocol's **different** hypothetical record `R*`, with a 10% symmetric error relative to the proposed Z and independent errors on independently prepared trials. This accuracy is **assumed**, not measured or derived from Q. At the target:

`P(R*=1 | XC)=0.9`, while `P(R*=1 | XL)=P(R*=1 | NL)=0.1`.

For 21 independent target trials and the fixed majority threshold of 11 yes responses, the exact probability of a wrong majority under either package is about **1.353×10⁻⁶**. The source gives the same predicted yes probability `0.1` in all three packages; it cannot by itself select their target subject rule. The number assumes the exact stipulated channel, independent preparations and errors, no nonresponse, and correct candidate outputs. It is **not** a real-world sample-size recommendation or measured reliability.

Crucially, the differing `R*` predictions are supplied by the additional package-dependent readout kernel. The model did not derive a physical feedback channel from phenomenal consciousness. An ordinary physical device programmed to evaluate C would report C's graph calculation regardless of which incidence rule actually constitutes experience; a device programmed to evaluate L would similarly report L's calculation. Those are different programs, not evidence that one joint episode exists. A real proposal needs the same fixed apparatus, a justified physical/phenomenal mapping and independent calibration in the target condition. Without those, selecting one of the two output kernels simply assumes the disputed bridge.

The existing [assay identifiability audit](EXPERIENCE_ASSAY_LATENT_IDENTIFIABILITY.md) documents why several agreeing indicators can still share a non-phenomenal common source. The previous [Roy S08 transfer](ROY_S08_FIXED_TRANSFER_RESULTS.md) did not independently calibrate this particular target or demonstrate an experience assay; no Roy data were reused here.

## 4. A post-protocol dependence stress test

The independence condition is material. A separate [follow-up control](verification/subject_assay_dependence_control.py), added **after** the frozen protocol was run, preserves a 10% error rate for each individual trial but compares different dependencies across a 21-trial block:

| Error model | Wrong-majority probability |
|---|---:|
| Independent trial errors | `0.0000013531` |
| One common error bit shared by all 21 trials | `0.10` |
| 1% mixture of common-error blocks, otherwise independent | `0.00100134` |

The last two are hypothetical countermodels, not measured rates. Even a small common-error component increases the nominal majority error by a factor of roughly 740 in this example. Repeating the same source-correlated report does not automatically create independent phenomenal evidence. More complex dependency structures, nonresponse and actual calibration uncertainty would require their own model; a real study cannot take the table as its error budget.

## 5. What does this do to the foundation question?

XL and NL are constructed to agree on the exact joint distribution of the spin tuple, Z, and `R*` at both defined settings. Their only difference is the stipulated direction of grounding. This remains true even under an idealized, not-realistically-available oracle for Z. The equality is **by construction**: it does not rule out developing other experiential and neutral accounts that make different testable predictions. But for these candidates, a successful boundary assay would distinguish the rule C from L **given its bridge assumptions**, not whether the L episodes are fundamental or neutrally grounded.

This is why the next B1–B2 work cannot simply equate a successful subject test with a proof that the whole is intrinsically experiential or necessarily actual. To close the gap, a candidate needs a non-circular account of its intrinsic nature and why its constitution and actuality hold, plus physics recovery rather than projection of preloaded inputs. To close B4–B5 it needs a justified incidence and quality rule that handles factorization, ties and real target-domain evidence. The physical instrument, gravity, measure and rival-comparison gates remain independent obligations. Nothing here requires an external creator, a literal simulator, a temporal actualization mechanism, or a fundamental spacetime.

## Reproduction

Run `python verification/subject_constitution_interface.py` for the precommitted exercise and `python verification/subject_assay_dependence_control.py` for the post-protocol stress test. The respective receipts are [interface](verification/subject_constitution_interface.json) and [dependence](verification/subject_assay_dependence_control.json). Both use exact rational arithmetic for the relevant probabilities; neither contains empirical data. A full framework battery pass is not claimed.
