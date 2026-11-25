# Audit → adapt → implement: a stationary sphere-battery interface

## The process and the implemented result

The user clarified the intended sequence: **audit the supplied inputs for errors; plan what to incorporate, as-is or corrected/adapted; then actually implement it in our work.** The point is not to abandon critical checking. It is to make the checking serve a constructive integration, rather than stopping at a verdict or a plan.

This is one concrete application to the existing [sphere–echo battery candidate](ZERO_SPHERE_BATTERY_INTEGRATED_BRIDGE_CANDIDATE.md). It combines Page–Wootters' stationary joint-observable method with the PSR battery's scoped actual-bearer/control discipline and the TIME/DATA emphasis on tracking identity and reconfiguration. The new [executable interface](verification/zero_stationary_battery_bridge.py) constructs **one stationary-history effect** for each of the candidate's readiness, truth/error and quality-comparison questions. Its [tests](verification/zero_stationary_battery_bridge_test.py) compare those stationary effects against the pre-existing sphere/reservoir ledger at every original tick.

The result is not a full foundation or a battery pass. It does close a specific integration gap: **the sphere candidate's model-level claim/error controls and its competing quality signs can be expressed as compatible relational observables in one stationary history, with the exact same previously calculated physical probabilities**. Neither an external time nor a presumed access path for a confined subject is introduced.

## 1. Audit: what survives, and what must be adapted

| Input | Audited useful content | Limitation / required correction before use |
|---|---|---|
| [PSR-5 battery and R1–R3 adjudications](ZERO_PSR5_SECOND_WAVE_ADJUDICATION_AND_LESSONS.md) | Explicit domains, actual-bearer checks, fixed target, positive/negative controls, class-level identity, and staged execution make a finite interface inspectable. | Its R0–R3 completion is **restricted-formal**, with declared instantiation and experience primitives. Do not transfer its pass to our different candidate, or call those primitives no-residue explanations. My earlier R0 non-pass has been withdrawn. |
| [Page–Wootters original and prior sphere connection](ZERO_PAGE_WOOTTERS_1983_RELATIONAL_SPHERE.md) | Joint clock–system observables can be invariant under global evolution while encoding different relational readings. | A stationary global observable need not be measurable by a confined inhabitant. A chosen clock and unitary history are model inputs, not physical time or subjectivity derived from zero. |
| [TIME/DATA structural grammar](ZERO_DATA_STRUCTURAL_TIME_AND_SPHERE_ECHO.md) | Track difference, identity, compatibility and reconfiguration as related features of one history, not just an ordered list. | The source's grammar does not itself derive our gate law, clock, identity, consciousness or the specific sphere model. Here it guides the representation; no source theorem is falsely attributed to it. |
| [Our claim/quality/measure bridge](ZERO_SPHERE_BATTERY_INTEGRATED_BRIDGE_CANDIDATE.md) | A B-sector target, echo-memory claim, ready-state control and competing `sj`/`sjr` physical sign rules are already defined on one history. | Its tick-indexed analysis did not itself supply one stationary observable joining those predicates. The signs and weights are not thereby actual felt qualities or subject-incidence measures. |

**Implementation plan:** retain the existing gate sequence and physical Born ledger; represent the reduced commuting `(b,j,r,s)` interface explicitly; construct the cyclic stationary history and a transported effect for each named predicate; test closure, target/claim controls and equality to the pre-existing full-ledger probabilities. Retain the original physical and experiential limits.

## 2. The same history, not a new physical system

The reduced interface has four binary signs:

- `b`: conserved B-sector target;
- `j`: current j sign;
- `r`: current echo-memory sign, initially ready `+` in the main case;
- `s`: the M sign, retained as the proposed quality-counterpart label.

There are 16 reduced basis labels. The actual pre-existing model's positive `(b,z)` weights, with pre-echo `j=z`, are `(+, +):1/2`, `(−, +):1/4`, `(−, −):1/4`; each has `s=±` with equal weights. Tick `0…19` is the existing internal cyclic clock. The reduced gate action has `T: r↦jr` at transitions 7, 9, 10 and 12, and `Q: j↦bj` at transitions 8 and 11; B and s are unchanged. The other existing source/reservoir operations act trivially on these **particular reduced labels**, but not on the full system.

The new code checks all 16 reduced inputs, including non-ready ones, and obtains the identity after 20 transitions. It does not claim that the source, reservoir or their charges do not exist: it is a coarse-grained representation of these particular diagonal observables. The full quantum echo and charge-preserving operations remain in the already checked source program.

## 3. Implementation: readiness, assertion and quality as stationary effects

Let `U_n` be the reduced prefix through tick n and W the controlled clock shift, so that

```text
W |n,x⟩ = |n+1 mod 20, G_n x⟩,   W²⁰=I.
```

For a Boolean physical predicate `P` anchored at tick `t`, define

```text
R_t(P) = 20 Ω_W(|t⟩⟨t| ⊗ P),
Ω_W(X) = (1/20) Σ_{k=0}^{19} W^k X W^(−k).
```

For these diagonal predicates, the implementation computes the identical transported projection directly: at clock row n, it maps a current label back through `U_n⁻¹`, forward through `U_t`, and evaluates P. Thus it is a projection and commutes with W. The tests check this **on every clock/sign basis state**, not just on the selected inputs. This is the Page–Wootters-style joint relational construction, applied to our existing claim/reference protocol.

The single normalized stationary reduced history is the coherent vector

```text
|H⟩ = (1/√20) Σ_n |n⟩ U_n |ψ⟩,
|ψ⟩ = Σ_{(b,z),s} √(P(b,z)/2) |b,z,r=+,s⟩.
```

It obeys `W|H⟩=|H⟩`. The code evaluates the **exact rational diagonal weights** of this pure reduced history. These probabilities agree with the prior sphere/reservoir ledger for the tested diagonal interface, both for the clean and the thermal auxiliary. Agreement of diagonal effects does **not** establish equality of this reduced pure state to the full physical model or equality of their non-diagonal coherences.

Use the fixed propositions `c=r` and “B has sign c”; error is the opposite relation. Four target/claim joint projections `B=b and r=c` sum to the identity, are mutually exclusive, and are stationary after transport. For tick 10 their weights are

```text
(b,c)=(+,+): 1/2     (+,−): 0
      (−,+): 0       (−,−): 1/2.
```

The inversion control `c=−r` yields no correct cases at that tick. This is a model-defined binary statement about the B observable, not a public real-world truth witness or a demonstrated assertion by an experiencing subject.

## 4. Results: one stationary history, one shared interface

| Effect / control | Exact stationary-history result | Meaning |
|---|---:|---|
| Readiness at tick 7, normal preparation | 1 | The model-level preflight accepts the specified ready record. |
| Readiness at tick 7, dirty `r=−` preparation | 0 | The preflight detects the changed input. |
| Normal B-claim correct at tick 10, ready | 1 | Perfect correlation in the stipulated model. |
| Inverted B-claim correct at tick 10, ready | 0 | The same target does not automatically fit any decoder. |
| Normal B-claim correct at tick 10, dirty | 0 | Readiness is a causal input, not an after-the-fact label. |
| `s j` versus `s j r` physical sign disagreement at tick 10 | 1/2 | The same interface supports distinct candidate-quality values. |
| Positive physical weight of either candidate sign at tick 10 | 1/2 | Each sign is physically balanced under the given Born ledger; balance does not choose between them. |

The implementation and tests check **every original tick** and all seven predicates against the independent existing ledger, including both clean and thermal auxiliary preparations. In particular, the normal-claim correct weights are `1/2` at 0–7, `3/4` at 8–9, `1` at 10, `3/4` at 11–12, and `1/2` at 13–19. Tick 20 is the returned copy of tick 0 rather than a second clock label.

The tick-10 quality comparison is on the same stationary state and the same physical algebra as the claim control. This matters: the formal referenceable record can work while the physically expressible candidate signs remain different. The result does not prove either value is felt, fix the experiential subject, or fix a self-location measure. A negative value, if an experiential bridge justified it as suffering, would remain a real local occurrence rather than be erased by balance.

## 5. What this advances and what remains

This is an **implemented adaptation**, not simply a source review or a promise to import ideas later. PSR contributes how to scope the controls; Page–Wootters supplies the actual stationary-observable construction; the TIME/DATA grammar informs the tracked distinction and reconfiguration; the sphere and echo provide the common underlying model. The source proposals remain distinct from what has been implemented here.

It does not claim a PSR-5 R0–R3 pass, an external F0–F5 pass, or a complete point–sphere packet. The full original battery conditions may differ, and the submitted candidate has not been frozen or adjudicated. Nor has the reduced construction derived the original Hilbert space, gate laws, global energy, genuinely actual subjects, phenomenal character, incidence weighting or necessity from zero. A complete no-residue framework must supply those together rather than treating the disclosures as acceptable brute remainders.

The next battery construction should reuse these very effects as concrete entries in a **versioned candidate**, close its complete global model and dependency definitions, and address the shared subject/quality/measure bridge. It must maintain an honest separation between a successful restricted formal interface and the user's stronger goal of a self-sufficient, physically and experientially complete zero constitution.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_stationary_battery_bridge_test \
  verification.zero_sphere_battery_bridge_candidate_test \
  verification.zero_page_wootters_original_sphere_connection_test -v
```

The new five tests cover the reduced cyclic action, stationary projection invariance, all-tick comparison to the prior clean/thermal ledger, joint-effect completeness, and ready/dirty and quality controls. The earlier tests supply the independent full-quantum echo checks. These are mathematical/model checks, not experiential evidence or a formal external battery adjudication.
