# Structural time, DATA, and the sphere echo: an explicit clock bridge and its limits

**Direct-DOI continuation:** [A stationary two-clock sphere comparison](ZERO_STRUCTURAL_TIME_TWO_CLOCK_STATIONARY_BRIDGE.md) constructs clock-to-clock observables without an external laboratory time and calculates the effect of reference-clock aliasing on actual echo access. [Action-flow and two continuous stationary sphere histories](ZERO_ACTION_FLOW_CONTINUOUS_STATIONARY_SPHERE.md) constructs two smooth completions that agree at the same recorded sphere ticks but differ at an intermediate clock-reference phase.

**Source:** Ekarach Chandon and Unyanee Mooksombud, [*Claim Map for TIME = THE UNIVERSE'S DATA MANAGEMENT, Book I*, v1.0](https://doi.org/10.5281/zenodo.21428534), released 18 July 2026. The linked deposit contains both the Claim Map and [*Structural Time, Measured Time, and Pre-Field DATA Order*, Technical Companion v1.0](https://zenodo.org/records/21428534/files/Technical_Companion_TIME_Book_I_v1.0.pdf?download=1). I read those two documents, **not** the underlying 326-page Book I; statements about the book below are what these source documents report. The companion is also deposited separately as [a preprint](https://doi.org/10.5281/zenodo.21436537); this report cites the copy in the linked deposit. Both describe their status as unreviewed and explicitly decline to claim an established new physical theory.

**Calculation:** [Verifier](verification/zero_structural_time_data_echo_test.py), building on the actual [20-step sphere/reservoir echo](ZERO_SPHERE_LOCAL_CONSTITUTION_AND_RESERVOIR_ECHO.md), its [stationary relational-clock construction](ZERO_PAGE_WOOTTERS_1983_RELATIONAL_SPHERE.md), and its [physical record/access analysis](ZERO_FLAG_RECORD_INCIDENCE_AND_PHYSICAL_READOUT.md). The construction and tests below are our proposed finite realization, **not a result claimed by the authors**.

## 1. What the source adds to our question

The authors propose that time is not merely a numerical reading, but a structural condition for the continuity and reconfiguration of what they call **DATA**. The technical companion describes a five-part provisional grammar: difference, structural identity, directionality, compatibility, and reconfiguration. It uses “pre-field” for a proposed ontological or explanatory priority, **not an earlier moment**, and says that DATA is not automatically Shannon information, bits, an existing physical observable, or a conserved quantity. “Management” is intended as lawful constraint and organization, not an agent, programmer, literal simulation, or cosmic administrator (companion §§2–3, 6–8).

This is strongly relevant to the zero program: if the whole has no external time, a clock number cannot simply be assumed to order its constitution. The source supplies a useful challenge sharper than “time is change”: **what are the admissible changes, which identities persist through them, which records make them accessible, and how do these become measured clock intervals?** The general distinction between relational time and fundamental time is prior art, including Page–Wootters, which the authors cite; it is not a new prediction of the source or of this project.

The authors themselves say the clock map is not derived, and state that their minimum grammar is a pre-formal scaffold, not a law (TC3–TC6, §§8–9). For comparison, I also checked [BIPM's definition of the SI second](https://www.bipm.org/en/si-base-units/second) and [Connes–Rovelli's thermal-time hypothesis](https://arxiv.org/abs/gr-qc/9406019), which proposes a state-dependent algebraic time flow under specified assumptions. Neither the SI definition nor that hypothesis establishes the authors' DATA proposal or selects our clock generator. They also propose Earth as a “First Stagnation Point,” a path-dependent second point, and cosmic balance. They label those **dependent conjectures**, not measurements. In their account, `n+x` is not yet a physical equation. No calculation below supports a uniquely cosmic status for Earth, post-life survival, or those specific endpoints. Our zero-radius whole is not Earth; the surface/world/inhabitant analogy should not be converted into an empirical identification.

## 2. A concrete realization of part of the grammar

Treat the already defined echo's lawful configurations and gates as a finite **candidate realization**, not as a derivation of the authors' purported pre-field substrate. Its input includes the old sphere sectors, source/reference qubits, physical stores, auxiliary and reservoir, and an echo register. It carries a conserved B-sector label and a specifically constructed signed-charge ledger. It does not assume that this ledger is the energy of the whole universe.

| Source's scaffold | Concrete echo analogue | What is still extra |
|---|---|---|
| Difference | Distinct supported configurations and distinct physical effects, e.g. different B or record values. | A specification of accessible effects and how distinctions become intrinsic experience. |
| Structural identity | B is conserved; the same designated stores and their registers are tracked throughout the circuit. | The tensor factors, charge, and identification through gates are stipulated in the model. |
| Directionality | A designated sequence of allowed gates and an indexed cyclic-clock relation. | The sequence orientation and physical clock interface; irreversible arrow is not automatic. |
| Compatibility | Allowed support and gate/charge constraints; actual correlated `(b,z,s)` Born weights. | Why these constraints, factors, and weights follow from zero rather than another structure. |
| Reconfiguration | The specific reversible gates, including the T–Q–T echo. | The gate laws and how they arise, not merely their labels. |

The authors define structural time as an ordered openness/closure status, **not** as this particular gate count. Accordingly this table illustrates one model; it does not identify DATA with a classical bit or prove the five conditions sufficient, necessary, or independent. The sphere construction already provides state spaces, amplitudes, operations and stationary observables that the companion asks future work to provide, but it has not thereby completed the authors' framework or derived field theory, the SI second or Lorentzian gravity.

The [real pair and teleportation analysis](ZERO_ER_EPR_FIREWALL_AND_SPHERE_ACCESS.md) supplies a further distinction: what exists in the full state, what is recorded by r, and what a confined party can use are not interchangeable. The no-residue objective asks for these relations to be generated by one self-sufficient constitution; merely naming a pre-field domain would add an unexplained structure rather than discharge that task.

## 3. A record forms, strengthens, and is erased without destroying the whole

The exact check uses the **actual correlated** `(b,z,s)` Born law, a thermal source reservoir `q=1/4`, and either the clean or thermal auxiliary. The echo register starts in its specified blank state. Here `b=0,1` encodes the conserved B sign. If an observer can read **only r** and makes the optimal guess of b, the probability of success is:

| Relational tick | 0–7 | 8–9 | 10 | 11–12 | 13–20 |
|---|---:|---:|---:|---:|---:|
| Optimal `P(guess b from r)` | 1/2 | 3/4 | 1 | 3/4 | 1/2 |

At tick 10, `r=b` exactly on the supported inputs. At tick 8, the actual law has `P(b,r)={(0,0):1/2,(1,0):1/4,(1,1):1/4}`; thus seeing `r=1` identifies `b=1`, while `r=0` remains ambiguous. At tick 13 r has returned to its blank value and is again uninformative about B, although B itself remains conserved. The result concerns the specified r-only interface; an observer with additional records can do better, and B itself is not thereby destroyed.

This adds a quantitative answer to the source's “openness and closure” question: in one exact internal construction, the **record interface** opens to B, reaches complete accessibility, and closes again. Global coherence is not necessarily lost; the full program is reversible. Calling the process “DATA management” would be an interpretation of this calculation, not an added physical law or an empirically new result.

## 4. A sharper distinction: the internal arrow needs an actual record

The original 20 operations are a ten-operation prefix followed by its exact inverse. Thus, for every input and each `t=0,…,10`, the **whole non-clock system** state satisfies `ρ_t=ρ_(20−t)`: the unitary prefix at these readings is identical. The verifier enumerates the actual full classical label paths—including apparatus, auxiliary, reservoir and echo labels—for arbitrary initial r; the coherent statement follows independently from the inverse-gate identity and the existing unitary tests, not from treating classical labels as a proof of quantum phases.

Consequently, at ticks 7 and 13, no instantaneous measurement of the non-clock system, even a global one, distinguishes which of these two readings is present if their priors are equal: optimal success is `1/2`. This does **not** say that the clock register, external records, a history of measurements, or an intervention cannot distinguish them. The two clock states are different. It says that “a transition happened” and even the full non-clock instantaneous state do not by themselves provide a persistent record of the side of the echo.

Now make a specific **additional intervention**: supply a blank neutral bit L, copy `r` into L at tick 10, and let the original inverse program run while L is retained. At tick 7, `L=0`; by tick 13, `L=b`, while the original computational-basis labels have returned to their tick-7 values. Since actual B values are equiprobable, for equally likely tick-7/tick-13 trials:

* before: `P(L=0)=1`;
* after: `P(L=0)=P(L=1)=1/2`;
* using L alone, optimal side-guessing succeeds with probability **3/4**, not 1.

This is a physical interface, not a free annotation or an inhabitant's automatically available memory. A full reversible implementation keeps L and uses an extra controlled gate; the clock or equivalent control has to make that operation occur at the midpoint. In a coherent superposition, leaving the copy in L can entangle it with B and decohere the reduced original system when L is ignored. Therefore the copied experiment is **not** the original unmodified echo, and equality of its original subsystem's *quantum state* at 7 and 13 is not asserted. The result is an L-only discrimination score, not an optimal bound over all possible joint measurements.

This is constructive for the whole-level picture: internal change and reversible recovery can coexist with a retained local record, but persistence of the record depends on where the inverse acts. “Closure” can mean return of a chosen subsystem, not necessarily erasure of every relation in the enlarged whole. It does not prove that an observer experiences an arrow or that all experience vanishes when a record is uncomputed.

## 5. A clock map needs more than admissible order

The technical companion explicitly requests a map `M_R` from structural histories to a reference clock's measurement. We can formulate a precise partial map and exhibit what it fails to fix.

The existing stationary history has a 20-state clock and a cyclic, controlled shift W, with `W²⁰=I`. For any chosen normalized system input, the 20 clock-labeled vectors `|t⟩⊗U_t|ψ⟩` are orthonormal, and W maps each to the next. On this **actual 20-dimensional history orbit**, choose the spectral integer operator K so that

`W = exp(−2πi K/20)`.

For any stipulated positive period T, define an auxiliary continuous laboratory embedding

`H_T = (2π ħ/T) K`, so `exp[−i H_T (mT/20)/ħ] = W^m`.

Every such T has the **same sampled order, states, gate relations, records, and cycle** at the 20 integer ticks. The earlier stationary history vector is the W-invariant eigenvector and need not evolve in an external fundamental time. The continuous Hamiltonian family here is an additional possible implementation of the shift, not an asserted unique generator or the actual unobserved dynamics between samples.

Add an independently prepared local reference oscillator with `H_R=ħω Z/2` and initial `|+⟩`. Prepare it together with the history-orbit input, let it run while the laboratory embedding completes one cycle, and compare it at the end. Its `+`-outcome probability is

`P_R(+ | one cycle) = cos²(ωT/2)`.

For `T₁=π/ω` this is **0**; for `T₂=2π/ω` it is **1**. The sphere clock is back at the same orbit state in both cases. Holding the reference oscillator fixed makes this a real difference in a stipulated comparison, not merely a change of units. The test checks the 20-dimensional shift and both oscillator probabilities.

The point is not that either T is physically selected, or that this finite laboratory model has already recovered relativistic clocks. It shows that the source's five-part grammar and a discrete admissible ordering alone cannot determine a numerical duration or a rate relative to another physical clock. A successful clock bridge needs at least a specified dynamical generator or equivalent physical relation **and** an actual comparison protocol. No universal preferred foliation follows from this example: its common laboratory parameter is a calculational device for this local, stipulated comparison, not a proposed global time of reality. Recovering proper time along worldlines, synchronization and gravitational/kinematic clock effects remains a separate correspondence requirement.

## 6. What it means for zero and subjectivity

This example connects several elements within one finite construction: invariant sector, actual Born-weighted record access, reversible relational dynamics, a clock comparison, and a possible retained trace. It shows why a zero total of a suitable signed quantity can coexist with nonzero local organization, but it does not show that the stipulated signed charge is physical cosmic energy or that its counterpart is negative felt experience.

For the user's stronger constitution of zero, the central demand is not simply a permitted tuple `(D,δ,ι,→,κ,ρ)` or the assertion that all possibilities occur. It is to show why the one self-sufficient whole has **this** internally differentiated relation, why its actual admissible histories and clock comparisons have their structure, and how intrinsic subjectivity, felt quality, and incidence weights arise as the inner nature of that same reality. The present calculation makes the target operationally sharper: any proposed identity between experience and records must account for cases where the same non-clock state occurs at two clock positions, where a copy changes subsystem coherence, and where record access varies from `1/2` to `1` and back. It neither equates subjectivity with data nor establishes that loss of an accessible record removes feeling.

A legitimate zero-level account may, as the user proposes, make genuine possibilities necessary and produce signed counterparts; neither that necessity nor opposite actual felt valence follows from the source's notion of balance. Zero total is not sameness, and signed cancellation would not mean that suffering is erased. Our result gives an explicit physical structure for investigating these claims, while leaving the proposed constitutive and experiential relation open rather than treating it as a brute addition.
