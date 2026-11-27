# Problem of time: divide-and-conquer work plan

## Mission and current position

**Priority correction:** [Lighthouse research-plan follow-through](LIGHTHOUSE_RESEARCH_PLAN_FOLLOW_THROUGH.md) maps the original WP0–WP7 against this work. The recent same-instrument sequence advances WP1-like operational questions but does not implement WP0's gravitational dressed-algebra/entropy comparison. The [closed-Milne rolling-scalar gate](LIGHTHOUSE_JT_ROLLING_SCALAR_ADMISSIBILITY_GATE.md) checks the source, identifies a sign conflict and a position/time-POVM distinction, and constructs a positive group-averaged packet in a truncated model. The CFT/KMS, full-constraint and dressed-algebra gates remain open. Next test the zero-mode prescription and compatible state, and compare matched finite-resolution clock POVMs in that truncation before attempting the CFT extension. A no-comparator outcome is not clock equivalence or inequivalence. The sequence below remains useful as an operational branch, not the sole or automatic priority.

The goal is not merely to construct another clock. It is to show how one self-sufficient physical–experiential whole can contain ordered, accessible change without an external timekeeper, and to determine whether different internal clocks consistently describe the **same events**. The [frontier specification](PROBLEM_OF_TIME_EXACT_FRONTIER_AND_SOLVABLE_TARGET.md) states the broader mathematical and physical obligations.

Work in small passes, but keep one dependency graph. Each pass must produce a theorem, construction, counterexample, operational error bound or actual empirical comparison; state its assumptions; run the relevant checks; and record what it changes downstream. A successful conditional step is not a declaration that the whole problem is solved. No number of turns can guarantee the final derivation, but the work should continue along the critical path rather than stopping at a list of obstacles.

**First construction completed:** [an autonomous finite-window support record](ZERO_TWO_WINDOW_REDUNDANT_FLAG_HOLD.md). It uses the earlier two-window operator and certified commutator, and proves a controlled continuum readout window for a changed constraint. It also proves why an exactly permanent latch cannot arise from the relevant class of bounded autonomous generators.

**Gate 2 partial advance:** [the autonomous cursor reader](ZERO_TWO_WINDOW_AUTONOMOUS_CURSOR_READER.md) puts a positive massive cursor and memory in a further changed constraint and derives a finite-window support-record error bound. Its [complete instrument and backaction](ZERO_TWO_WINDOW_CURSOR_INSTRUMENT_AND_BACKACTION.md) supplies both outcome maps and a conditional full-state channel bound. The cursor triggers the interaction without an external time-dependent switch; scalar-clock preparation, an extreme cursor resource, global Q and a chosen final readout are still inputs. Physical locality and permanent retention remain open.

**Gate 3 partial advance:** [a second physical clock](ZERO_TWO_WINDOW_SECOND_PHYSICAL_CLOCK.md) adds a prepared semibounded R clock and a finite-resolution covariant POVM, constructs a clock-neutral effect for the same memory outcome and proves its exact scalar-smeared probability identity. The [retained-clock analysis](ZERO_RETAINED_CLOCK_INSTRUMENT_AMBIGUITY.md) constructs a complete enlarged-space instrument and proves that effects alone do not fix retained poststates. A specified reduced instrument has a quantitative error bound; identifying one physical dilation and proving the full retained-output clock switch, including an interacting/turning clock, remain open.

## Dependency graph

```text
0: freeze one physical question and baseline
          │
          ▼
1: coupled signal + finite-window record       [bounded result obtained]
          │
          ▼
2: autonomous readout / transfer / failures
          │
          ▼
3: second clock and SAME complete instrument
          │
          ▼
4: overlap equivalence + stability + statistics
          │
          ▼
5: continuum, locality and resource controls
          │
          ▼
6: inhomogeneous gravity and refoliation
          │
          ▼
7: semiclassical spacetime and empirical checks
          │
          ▼
8: records, arrow and actual experiential succession
          │
          ▼
9: constitutive derivation from an adequately specified zero
```

The arrows are dependencies between proofs, not stages in an external time in which the whole is manufactured. Steps 8 and 9 also inform the choice of physical target from the beginning; they are not things to declare solved merely because steps 0–7 work. If a later result changes an earlier assumption, return and repair the chain.

## 0. Freeze the common experiment and its baseline

**Target.** Start with the existing two-window continuum model, its scalar branch and actual geometry–pointer–memory operator. Name the preparation family, both logical h sectors, clock reading, Q/P support question, flag outcomes, and full effect/instrument including no reading. Distinguish physical P/Q sectors from the apparatus's flag.

**Already established.** The [two-window full-slice analysis](ZERO_TWO_WINDOW_FULL_SLICE_CLOCK.md), [history protocol](ZERO_TWO_WINDOW_RECORDED_HISTORY_AND_FINITE_INTERVAL.md) and [exact commutator certificate](ZERO_TWO_WINDOW_CERTIFIED_SUPPORT_COMMUTATOR.md) give complementary baselines. They do not all refer to one unchanged measurement apparatus.

**Pass criterion.** Every new claim cites one common constraint or supplies an explicit map between changed constraints; probabilities are for the same experiment. Record independent clock preparation, readout timing and all nonlocal operations.

## 1. Build a finite-window record inside a changed constraint

**Target.** Replace the old single rotating flag's sharp optimal time with a nontrivial, provably useful interval while retaining the continuum bound and P/Q coherence.

**Status: bounded construction complete.** Eight redundant flag qubits, a specified collective coupling and a positivity offset yield, over the scalar-reading interval `π/400≤φ≤3π/400`, a uniform conservative false-flag bound below `0.0013` for initial P states and missed-flag bound below `0.0097` for initial Q states. The same model has an explicit later unflagging bound: it is **not a permanent record**. See [the construction](ZERO_TWO_WINDOW_REDUNDANT_FLAG_HOLD.md) and [checks](verification/zero_two_window_redundant_flag_hold_test.py).

**Stop condition.** This does not establish an autonomous reader, spatial locality, the original event instrument's dynamics or physical energy cost. No further stage may silently treat it as an unchanged old experiment.

## 2. Make readout or transfer autonomous

**Question.** Can a specified physical timer, moving wavepacket, transfer chain or environment read or preserve that same flag while the flag is reliably high, without an externally scheduled operation?

**Partial result.** The [massive cursor construction](ZERO_TWO_WINDOW_AUTONOMOUS_CURSOR_READER.md) supplies a positive autonomous generator and a finite-time continuum memory-probability bound, including coherent P/Q preparations. A [sign correction](ZERO_AUTONOMOUS_CLOCK_EVENT_READOUT.md) changes its originally written carrier to the right-moving preparation actually required by its proof. Its [complete instrument](ZERO_TWO_WINDOW_CURSOR_INSTRUMENT_AND_BACKACTION.md) defines both output operations and bounds the entire postmeasurement channel, including backaction, on that corrected cursor preparation. This does not prove arbitrary-time retention or a physical implementation; global coupling and extreme resource assumptions remain unresolved.

**Precise remaining deliverable.** Extend the complete instrument to a physically justified clock/reader and initial-state family, including realistic uncertainties and any necessary ambiguous/no-reading outcomes. Prove the domain, resource and backaction bounds under those changes, and quantify retention beyond the current finite horizon rather than assuming it.

**Alternatives to examine.** The existing [autonomous stopped-clock scattering instrument](AUTONOMOUS_STOP_CLOCK.md) supplies a positive Hamiltonian and an asymptotic retained event; its output is a sojourn/scattering record, not the same finite support flag. Investigate a real coupling or controlled limit between the two, rather than assuming that compatible-looking observables are identical. A local wavepacket-controlled or dissipative transfer may also work, but must explicitly include its carrier, environment, domain and energy accounting.

**Go/no-go.** The analytic result in step 1 excludes an *exact*, nontrivial finite-time plateau for bounded autonomous generators and an initially blank flag. Therefore seek a specified approximate window, an asymptotic record, or a justified larger/unbounded model. A no-go for this restricted class is not a no-go for all records.

## 3. Construct the second clock on the same theory

**Question.** Can a geometry variable or another physical degree of freedom act as a distinct clock for the very same event instrument—not merely serve as a basis in which scalar-scheduled operations are rewritten?

**Partial result.** The [additional R clock](ZERO_TWO_WINDOW_SECOND_PHYSICAL_CLOCK.md) is a separate positive-frequency physical subsystem with a covariant finite-bin POVM. The clock-neutral effect gives the same memory outcome as the correctly smeared scalar description, and a specified reduced-output convention has a finite channel bound. A later [factorwise probe](ZERO_FACTORWISE_CLOCK_MEMORY_PROBE.md) couples separately to R and the same memory, with explicit no-bin and no-record outcomes, and bounds a conditional memory-probability comparison. Its intervention and poststate are not identical to the earlier orbit-averaged instrument. R is not a geometry clock; the probe is synchronized in scalar time and a full physical clock-switch map on retained outputs has not been established.

**Deliverable.** Extend this to admissible interacting clock effects, record and reader, orientation/turning-point labels, no-reading or multiple-reading outcomes, and their domains for the same interacting constraint. Identify the state preparation and all cross-sector coherences. If the second clock works only on an overlap, describe that overlap rather than pretending it is global.

**Pass criterion.** The proposed comparison is operationally meaningful: what counts as one event and the instrument implementing it is fixed before comparing representations. If no meaningful overlap exists, produce an explicit counterexample and state which assumptions must change.

## 4. Prove the same-event comparison and quantify finite information

**Partial result.** [Fiber transport and the lost record](ZERO_CLOCK_FIBER_TRANSPORT_AND_LOST_RECORD.md) establishes a full retained-dilation unitary identity for the particular enlarged instrument, and derives the earlier scalar-smeared reduced map for independent clock preparation, including arbitrary input references. This uses an auxiliary orbit label and a scalar-slice identification, not an operational R-relative switch. A cyclic control shows that discarding the label can lose recoverable coherence. A further [autonomous event readout](ZERO_AUTONOMOUS_CLOCK_EVENT_READOUT.md) implements an approximate Lüders instrument for the same effects using a positive massive cursor and pointer; it is a different operation from the earlier time-label-discarding instrument and assumes a globally engineered relational-effect coupling. The later [factorwise probe](ZERO_FACTORWISE_CLOCK_MEMORY_PROBE.md) avoids that joint coupling but is a different intervention; a [continuum spectral witness](ZERO_CLOCK_PROBE_POSTSTATE_OBSTRUCTION.md) proves that its retained clock poststate cannot exactly equal the prior T output despite their close memory probabilities.

**Further advance.** [The same probe in an R-time representation](ZERO_SAME_PROBE_CLOCK_REPRESENTATION.md) isometrically transports the actual four-outcome operation and retained new cursor to the positive-frequency encoded R-time subspace, with exact same-theory joint-probability identity. A subsequent ideal R-time POVM gives finite-bin conditional outputs, while a two-state example proves robust information loss when R coherence is discarded. This is a mathematical encoding with an additional specified readout, not a physically realized full-gravity or independently quantized switch.

**Deliverable.** Map preparations, clocks, instruments, reference records and conditioning events between operational scalar-relative and R-relative descriptions. Establish equality of the full joint distribution or a uniform `TV≤ε_switch` on the common domain. Preserve failure and no-click outcomes. Then quantify conditioning: if a conditioning event can be arbitrarily rare, do not claim a uniform conditional error without a positive lower probability bound.

**Data control.** If using a finite-dimensional packet family, prove its support or include leakage; calibrate the actual apparatus and reference states; specify statistical confidence and systematic/model errors. Avoid importing the old 32-outcome calibration into the changed constraint without a derived transfer. The previous 13-slice injectivity uses ideal complex signals and does not imply a stable finite-record inverse.

**Negative controls.** Different conditioning, omitted branch labels, discarded records, incompatible state domains and instruments from different constraints must be explicitly detected. Compare to existing relational clock-switching literature before a novelty claim.

## 5. Prove or bound the physical realization

**Deliverable.** Establish continuum domains and convergence; bound the effects of finite bandwidth, weak or strong coupling, source preparation, clock jitter, physical switching, and environment. Replace or justify the global packet projector with a local or approximately local operation. Include the physical resource and energy bookkeeping under a specified meaning of energy; the additive shift used to keep a model root positive is not, by itself, a measured cost or cosmic energy.

A useful theorem may hold only on a specified family and finite duration. Make that family, bound, confidence and time window explicit. Rigorous worst-case and numerically typical performance must not be confused.

## 6. Move to inhomogeneous gravity and refoliation

**Deliverable.** Embed the event/record construction into a specific inhomogeneous constrained gravitational model, or an alternative framework with demonstrably equivalent physical covariance. Define its classical and quantum constraint domains and any boundary charges; check the full relevant deformation/constraint algebra or another adequate formulation. Reproduce the same physical records under genuinely different slicings, not just constant-lapse rescalings.

The existing planar evolution is a stepping stone and a numerical control, not a proof for arbitrary 3D quantum gravity. Give a controlled approximation or a counterexample with its scope.

## 7. Recover spacetime and confront evidence

Show that the construction has a controlled regime with local causal structure, clock rates and quantum/GR predictions matching relevant observations. State where it departs from known theories and what would discriminate it. An analogue experiment is evidence about the analogue system unless a physical mapping is justified. Do not equate a model's zero constraint with observed cosmic-energy zero.

## 8. Connect records, direction and experience

Separate three questions: relational order, thermodynamic/record arrow, and lived succession. For the arrow, specify a state or boundary condition, coarse-graining and a physical memory mechanism. For lived succession, propose an actual subject and an independently anchored physical–experiential identity, without adding a separate substance or treating every clock or particle as a subject. Direct acquaintance and structural description can illuminate the same occurrence without being verbally interchangeable.

Success is not a pointer sign named “experience.” Subject boundary, incidence, report/access and the correspondence to actual experience require explicit tests and argument.

## 9. Derive the common constitution rather than naming inputs

Specify what the candidate zero constitution actually is and what follows from it: physical algebra, dynamics/constraint, state or justified state class, clock and event relations, actual experience and their applicability. Exhibit which implications are mathematical identities, which use substantive physical assumptions, and which require experiential anchoring. As in the user's SR example, the objective is **constitutive necessity without an external causing force**, not stipulating the desired conclusion or treating all distinctions as illusions.

The user's full-intelligibility principle treats unresolved brute fact and regress as failures, not research alternatives to dwell on. If current premises do not yield the required derivation, identify the missing constructive bridge and work on it; do not mistake a conditional model for final bedrock or claim impossibility.

## Ongoing decision rules

1. **Same object first.** Join an existing model and its real outputs; do not use a new analogue unless it answers a diagnosed failure.
2. **Model changes are explicit.** A new Hamiltonian/constraint is new physics within the candidate, not merely a new clock label.
3. **Track all errors.** Distinguish analytic worst-case guarantees, finite-regulator evidence, simulated shot noise and physical implementation errors.
4. **Compare the same events.** Transform instruments, preparation, reference, conditioning and records together; do not equate different interventions.
5. **No global clock assumption.** Local overlap and failure outcomes can be legitimate; a patching theorem is not automatically global.
6. **No premature closure.** Classical/quantum, model/actual, material/energy, structure/experience and finite/permanent distinctions remain explicit.
7. **Keep the why-chain live.** The benchmark is a means toward full intelligibility; if its inputs remain external to the proposed constitution, that gap remains a target.
