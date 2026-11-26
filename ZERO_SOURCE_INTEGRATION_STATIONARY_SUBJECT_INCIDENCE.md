# Source integration, second pass: subject incidence on the stationary sphere

## The constructive question

**Balance follow-up:** [the echo incidence-balance diagnosis](ZERO_ECHO_INCIDENCE_BALANCE_ROOT_CAUSE.md) distinguishes equal type weights from sign-reversing balance and shows why a diagonal-only type assignment is not automatically compatible with the earlier pure all-effect marginal.

**Full-quantum continuation:** [the coherent echo type symmetry](ZERO_FULL_QUANTUM_ECHO_TYPE_SYMMETRY.md) constructs a controlled `Q Z_M` operation that exchanges the two binary quality observables on the actual post-echo support and stabilizes all 16 original source states. It does not prove the symmetry of actual experiential incidence, every degree of freedom, or a magnitude-bearing extension. [The point–sphere magnitude integration](ZERO_POINT_SPHERE_SIGNED_MAGNITUDE_ECHO_INTEGRATION.md) shows why the latter matters.

The user asks for repeated passes over the **whole available chat record**: audit inputs, plan what survives with any needed repair, and implement the resulting ideas in our framework. The [first stationary integration](ZERO_SOURCE_INTEGRATION_STATIONARY_BATTERY_INTERFACE.md) brought PSR's target/control discipline and Page–Wootters' stationary observables together on the existing sphere echo. This second pass brings the subject and self-location issues into that **same stationary history**, using Bohn, Lewtas, Miller and the user's pairing proposal.

**Result:** in the reduced model at the existing echo's tick 10, there is a nontrivial *active* transformation of the physical record that exchanges the two earlier candidate quality signs `sj` and `sjr`, preserves the specified reduced state, and leaves the tick-10 B/claim correctness and tick-7 ready preflight intact. Its transported global version commutes with the cyclic clock shift. If two separate incidence types are postulated, their physical marginal is the same pure reduced state, and the incidence measure is required to be invariant under this **combined physical-and-type swap**, the two types must have equal total weight. This is a real model-level selection conditional on a concrete extra invariance, not selection by merely renaming the types.

Crucially, this symmetry belongs only to the specified reduced history, state and effects. It does not preserve every physical observable or primitive gate, and it has not been established for the original full sphere/reservoir construction or actual experience. It is not yet an argument that nature enforces the needed incidence symmetry.

Executable definition: [verification/zero_stationary_subject_incidence.py](verification/zero_stationary_subject_incidence.py). Checks: [verification/zero_stationary_subject_incidence_test.py](verification/zero_stationary_subject_incidence_test.py).

## 1. Audit and adaptation, before implementation

| Input | What we retain | What we do **not** import without a derivation |
|---|---|---|
| [Bohn's plural consciousness paper](BOHN_PLURAL_COLLECTIVE_CONSCIOUSNESS_FULL_PAPER_AUDIT.md), [uploaded original](sources/uploads/bohn2018.pdf) | Collective experiential properties need not be assembled by fusing pre-existing conscious microsubjects. Treat a physical carrier, a property type and a particular subject-incidence as distinct kinds of thing. | No blanket claim that each component is a subject, that the whole is one subject, or that Bohn's brute distribution of consciousness satisfies the user's no-residue demand. A plural carrier alone does not select a lived subject. |
| [Lewtas on mental chemistry](LEWTAS_2016_MENTAL_CHEMISTRY_AND_FRAMEWORK_AUDIT.md) | Choosing a carrier, placing aspects in a field, and explaining a blended quality are separate obligations; amount and subject count differ. | His conservation and mental-chemistry laws, individual micro-subjects and particular speculative physical mechanism are not demonstrated. The candidate signs below do not solve phenomenal blending. The source PDF is not in the tracked uploads; the historical audit reports it was read in a private cache, which is not presently established to be available. |
| [Miller's subject-relative boundary](MILLER_SUBJECT_PARTHOOD_AND_DECOMBINATION_AUDIT.md), [uploaded original](sources/uploads/miller2017.pdf) | Access and unity must be indexed to the proposed subject; different carriers can overlap without their subjects or shared experiential tokens being automatically identified. | This construction does not claim Miller's shared-token nesting or a cosmic subject; overlap of physical observables is not evidence of token sharing or a new subject. |
| [User's necessary-plenitude and opposite-pair proposal](ZERO_NECESSARY_PLENITUDE_SIGN_PAIRING.md), plus [incidence refinements](ZERO_INCIDENCE_REFINEMENT_AND_BORN_MEASURE.md) | Seek a weight-preserving, sign-reversing counterpart within one whole; transport weights rather than count arbitrary labels as new occurrences. | A formal map or nonzero Born weight does not itself prove the two mapped terms are genuinely possible, actually experienced, or equal-weight incidences. Do not treat an unpleasant occurrence as erased by an opposite one. |
| [Earlier same-echo incidence construction](ZERO_JOINT_CONSTITUTION_INCIDENCE_AND_ECHO.md) | Keep the physical marginal and incidence type distinct. Under all-effect consistency with a pure physical marginal, each positive type block is a scalar multiple of that state, but the type coefficient remains open. | Do not assume a passive type renaming forces equal weights; the earlier B/j type comparison did not establish a symmetry of the full physical–experiential package. |

**Plan:** preserve the already tested stationary echo and physical target; at its tick 10 define both quality signs on the same `M–j–E` interface; search for an explicit physical operation swapping them rather than an exchange of labels alone; lift that operation to the cyclic stationary history; then ask exactly what additional incidence principle would determine the type weights. This avoids claiming that Bohn, Lewtas or Miller themselves proposed this specific model.

## 2. A concrete physical swap, not just a type-label swap

Use the earlier reduced four-sign basis `(b,j,r,s)` with the 20-step cycle `U_n`, as defined in the [stationary interface](ZERO_SOURCE_INTEGRATION_STATIONARY_BATTERY_INTERFACE.md). At anchor tick 10, set

```text
v_now = s j,          v_echo = s j r,
D(b,j,r,s) = (b,j r,r,s).
```

D is a permutation and an involution. It acts on the physical record j, controlled by r; it fixes b, r and s. Consequently it exchanges the two candidate sign observables:

```text
v_now(Dx) = v_echo(x),    v_echo(Dx) = v_now(x).
```

This is not just relabeling two proposed incidence types: on `r=−`, D physically changes the j sign in the reduced model while leaving the B target and r claim fixed.

The original positive initial weights are `P(b,z)=(1/2,1/4,1/4)` on `(+,+),(−,+),(−,−)` and equal s counterparts, with r ready. At tick 10, `r=b`, `j=bz`. D fixes the entire `b=+` sector; in the `b=−` sector it exchanges the two equally weighted z branches. The amplitudes of our explicitly chosen **reduced coherent state** are equal and positive on those branches, so the state—not merely its diagonal distribution—is D-invariant. That phase condition is a property of this reduced realization, not a demonstrated fact about the complete original quantum state.

Lift D to all clock rows by

```text
D_n = U_n U_10⁻¹ D U_10 U_n⁻¹,
D̄ |n,x⟩ = |n,D_n x⟩.
```

Because the full reduced cycle closes, `D̄²=I` and `[D̄,W]=0`. It preserves our stationary reduced history, and swaps the two transported tick-10 quality effects. The tests verify equality on **all 320 clock/sign basis states** and state invariance, not only a few supported samples.

D̄ also preserves the transported ready predicate at tick 7 and the tick-10 B-versus-r correctness predicate. It does **not** fix every physical effect: j changes on a nonempty sector. Nor does the bare anchor D commute with the individual T gate. The dressed operation is therefore a symmetry of the reduced stationary history and the listed relational questions, **not automatically** of all local gates, accessible operations, the full reservoir, all times as physical observables, or the laws of nature. It may require a clock-controlled operation unavailable inside a confined realm.

## 3. Apply Bohn/Lewtas/Miller distinctions to incidence types

Use two **hypothetical** type labels `N` and `E` for occurrences with the quality rules `sj` and `sjr`. A label does not establish an actual subject, two subjects, a merger, or two shared phenomenal tokens. Both candidate functions concern the same proposed physical `M–j–E` carrier. Do not assume the j-only surface inhabitant can read the richer carrier.

Adopt, provisionally, the strong pure-physical-marginal and all-effect consistency premises from the earlier incidence construction. On the type bookkeeping algebra, the corresponding positive blocks must be

```text
σ_N = α |H⟩⟨H|,       σ_E = (1−α) |H⟩⟨H|,
0 ≤ α ≤ 1.
```

The diagonal physical question `E⊕E` has the same Born weight for every α. This is a proposed measure over types, not an objective random selection of a world. We have not established that every block effect is a meaningful first-person incidence question.

Now combine the physical transformation D̄ with type exchange `N↔E`. Unlike a bare type swap, the combined operation exchanges the two quality rules **and** changes the physical record on the disagreement sector. It preserves the proposed signed value after transforming both physical state and type. If the actual incidence measure is invariant under this combined transformation, then

```text
α = 1−α  ⇒  α = 1/2.
```

Conversely, in this explicitly stipulated product family, α=1/2 is invariant. The executable exact tests verify both directions for representative unequal/equal rational weights; the displayed algebra proves the general statement. At α=1/2, each type has weight 1/2, the aggregate physical distribution remains unchanged, and the probability that the two physical candidate signs disagree is 1/2. Because `s↦−s` pairs the reduced state's weights, either sign rule has equal positive and negative model weights for every α.

This is a **new sufficient route to the desired equal-type selection**, but with a significant cost: invariance of *actual incidence* under D̄ plus type exchange must be justified. Physical state invariance alone does not imply it. A passive redescription transports the measure with the labels and is consistent with any α. Further, a complete ontology could identify the two ports, reject one, assign different quality laws, have subject-relative access or additional physical observables that break the putative symmetry; these are structural alternatives to investigate, not claims that distinct complete realities are genuinely possible.

## 4. What is genuinely gained, and what remains to derive

The earlier bare type exchange failed as a justification because it did not preserve the fixed quality operator. Here the **combined physical-plus-type operation does preserve the proposed typed sign**, and is explicitly realized in the common stationary reduced model. This shows exactly what an equal-weight argument would have to mean: not “both descriptions exist, so count them equally,” but an actual symmetry of the relevant full physical–experiential incidence law.

Nor does a zero signed mean establish a zero of actual experience. Under the hypothesis that the negative sign really is felt negative valence, the negative occurrence remains real even when the total is balanced. Magnitudes, ownership, addition across distinct subjects and experiential incidence weights require their own constitution. No equation here says that pleasure removes another subject's suffering, that negative experience is absence, or that the constructed sign is cosmic energy.

A complete framework must still determine from the nature of zero whether the relevant physical space, gates, boundary, symmetry, qualities, actual subject incidences and measure hold together necessarily, and recover physical and first-person evidence. The result is a concrete conditional bridge toward that task, not a permissible unexplained residue or an established battery pass. The strong possibility–actuality proposal is not decided by finite formal alternatives.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_stationary_subject_incidence_test \
  verification.zero_stationary_battery_bridge_test \
  verification.zero_joint_constitution_incidence_echo_test -v
```

Six new tests check the involution, the stationary lift and reduced pure state, the unchanged fixed target and readiness controls, type-measure selection under its added premise, physical sign balance, and the difference from invariance under every individual gate. They do not certify that any represented system has experience.
