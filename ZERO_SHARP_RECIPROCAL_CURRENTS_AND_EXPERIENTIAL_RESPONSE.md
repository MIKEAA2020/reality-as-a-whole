# Sharp reciprocal currents and the experiential-response condition

## The advance

The [reciprocal sphere–record construction](ZERO_RECIPROCAL_SUBJECT_EXCHANGE_AND_INCIDENCE.md) gave opposite memory currents as conditional expectations. There is a stronger exact fact: at one point in that same evolution, the two opposed currents are **simultaneously sharp**, nonzero and exactly correlated with the prior sphere record. This corrects the earlier report's overbroad suggestion that the displayed conditional currents are never sharp.

The same construction gives a precise condition on a proposed physical–experiential bridge. If the two candidate subjects have a common signed response `q` to the two current values, their contributions sum to zero in every active event **if and only if**

```text
q(+1) + q(−1) = 0.
```

This does not require setting either individual value to zero. But it is a substantive relation between opposite *experiences*, not a consequence of energy conservation, equal Born weights, or exchange symmetry. A common response can instead assign a negative value to both physical directions, giving a negative total. That is a mathematical counterexample, not an observation that the qubits suffer.

A further test strengthens the distinction between physical and experiential organization. A local phase operation reverses the joint current while leaving all relevant individual memory, memory–battery pair, and two-memory reduced states unchanged. Hence the current sign cannot be recovered from any rule using only those instantaneous reduced states. The interface current is a four-block joint observable, so this does **not** establish a local feeling or a relativistic signal.

The user's stronger project asks why zero's own constitution determines physical differentiation *and* real subjectivity. These results make its experiential demand specific: establish a subject-incidence and signed-quality relation whose opposite response is justified, rather than simply identifying a physical sign with a feeling. They do not treat a missing derivation as an acceptable unexplained residue or as a refutation of the thesis.

## 1. Exact current eigenvalues in the existing model

Use the previous encoded sphere state and four work qubits `(M₁,W₁,M₂,W₂)`. Write

```text
|a⟩=|0110⟩,    |b⟩=|1001⟩,
P=|a⟩⟨a|+|b⟩⟨b|,    G=|b⟩⟨a|+|a⟩⟨b|,
J₁=i[G,N_M₁],    J₂=i[G,N_M₂].
```

Here `J₂=−J₁`, `J₁²=P`, and `J₁` is Hermitian. Its active-sector eigenvalues are `+1,−1`; zero occurs outside that sector. In the exchange units chosen previously,

```text
J₁ |a⟩=−i|b⟩,       J₁ |b⟩=i|a⟩.
```

The record-controlled preparation puts `|a⟩` on `R_A R_B=01` and `|b⟩` on `10`. With `U(t)=exp(−itG)`, at `t=π/4` the two normalized work states are

```text
record 01: (|a⟩−i|b⟩)/√2,    J₁=+1, J₂=−1;
record 10: (|b⟩−i|a⟩)/√2,    J₁=−1, J₂=+1.
```

The two currents commute because they are negatives of one another, and they commute with the record projectors and the reference-controlled spin observable `T_dir` because these act on different factors. Thus in **each** record-conditioned state these are sharp joint eigenvalues. The coherent whole satisfies the state equation

```text
T_dir J₁ |Ξ(π/4)⟩ = |Ξ(π/4)⟩,
(J₁+J₂)|Ξ(π/4)⟩ = 0.
```

For each of the four tetrahedral labels, each record/current pair has Born weight `1/8`. This is a sharper physical connection than the previously quoted mean `⟨T_dir J₁⟩=1`: it is an eigenstate relation, not merely cancellation in an average.

At a general interaction parameter `t`, the mismatch between the commuting sign observables `T_dir` and `J₁` has probability

```text
p_mismatch = (1−sin(2t))/2
```

in the specified state, since it lies wholly in `P` and `⟨T_dir J₁⟩=sin(2t)`. At `t=0` and `t=π/2`, the **conditional mean** of `J₁` vanishes but `⟨J₁²⟩=1`: its two nonzero eigenvalues have equal conditional probabilities. A zero mean is not an eigenvalue zero, and a nonzero current expectation is not generally a sharp current. The current is a joint four-block interface observable; a current measurement is an added operation, not evidence of an actual experience or of an independently accessible local memory measurement.

These statements refer to the standalone `G` interaction used in the previous report. Its four-state autonomous clock does **not** automatically place this intermediate state at one of its labels. The following new clock does, while making the distinction between the probe `J₁` and the clock's own current explicit.

### An autonomous clock that includes the sharp stage

Use all five singlet states of the existing six-spin clock, so the system still contains 44 physical spins. Let `A` be a five-state weighted path with edge weights

```text
A_(k,k+1) = √((k+1)(4−k)),     k=0,1,2,3.
```

Let `V₀=I`, `V₁=V_prep`, `V₂=U(α)V_prep`, `V₃=U(π/2)V_prep`, `V₄=I`, and put `K=Σ_k|k⟩⟨k|⊗V_k`. Introduce a *single*, time-independent Hamiltonian

```text
H₅ = H₀ + K(A⊗I)K† + |2⟩⟨2|⊗G.
```

The added on-clock exchange is essential: without it, conditioning the clock on one label would not make `J₁=i[G,N_M₁]` the clock Hamiltonian's actual memory-current operator. All `V_k`, `G`, and hence `H₅` commute with the previously stated memory-pair, battery-pair, and total bare charges. The clock work operations preserve the encoded spin-zero factors and continuous logical symmetry. Their many-body structure is stipulated, not derived as spatially local physics.

Set `t₀=π/4`, `z=⟨2|exp[−it₀(A+|2⟩⟨2|)]|0⟩`, `φ=arg(−z)`, and `α=π/4+φ`. This is a deliberate calibration of the link, not a claim that zero independently selects α. The path parity operator `R|k⟩=(−1)^k|k⟩` gives `R(A−|2⟩⟨2|)R=−(A+|2⟩⟨2|)`. Because the endpoints 0 and 2 have even parity, the corresponding transition amplitude for `A−|2⟩⟨2|` is `z*`. In the `G=±1` sectors this makes the clock-2 work amplitude proportional to `U(−φ)`; the calibrated `V₂` therefore gives

```text
(⟨2|⊗I) exp(−it₀H₅) (|0⟩⊗|Ω⟩⊗|a⟩)
    = −|z| e^(−2it₀) |Ξ(π/4)⟩.
```

Numerically `|z|²≈0.35973924` and `α≈0.54105080`. Conditioning on clock 2 yields the *same* sharp, sphere-correlated `J₁,J₂` state above; each reference/record outcome has conditional weight `1/8`, and joint clock/reference/record weight about `0.0449674`. No clock measurement is claimed to happen by itself.

Let `J₁^(5)=i[H₅,N_M₁]` and `P₂=|2⟩⟨2|⊗I`. The off-diagonal clock-link terms imply the exact compression

```text
P₂ J₁^(5) P₂ = P₂ J₁ P₂.
```

Consequently, after a clock-2 projection and record conditioning, a subsequent measurement of the **full** clock-Hamiltonian current has conditional mean `+1` or `−1`; the two memories' actual clock currents remain opposite as an operator identity. However, `J₁^(5)` also has off-diagonal clock components: the clock-2 state is **not** generally an eigenstate of the full current. The sharpness claim is for `J₁`, the compressed/probe observable, not a joint sharp measurement of clock and the full `J₁^(5)`. Measuring clock and then current is a sequential, potentially disturbing protocol. This distinction is necessary to avoid turning a history-state label into a fictitious simultaneous trajectory.

Both the interaction parameter and this finite clock are model structures, not a fundamental spacetime foliation. The autonomous construction is coherent and calibrated; it is not an irreversible memory, an established biological system or a selection of an actually experienced record.

## 2. The exact signed-response theorem

Consider a hypothesis, not an established physical law: each memory candidate has an actual signed experiential contribution determined by the eigenvalue `x` of its associated current through a **common** response `q(x)`. If actual incidences have separate positive weights, `q` can be their product with the signed per-incidence value. The other candidate's current is `−J₁`.

Because both currents commute, their response operators can be evaluated simultaneously. For arbitrary real `q(+1)`, `q(−1)`, and `q(0)`, the spectral calculus gives the exact operator identity

```text
q(J₁) + q(J₂)
  = [q(+1)+q(−1)] P + 2q(0)(I−P).
```

Therefore, on **any state supported in the active sector**, the sum is zero exactly when `q(+1)+q(−1)=0`. This is a per-eigenvalue result: every joint current outcome in that sector has the same sum, not merely a zero state average. It applies to the sharp sphere-correlated events at `π/4` and to a joint current measurement at other times. The assumption of an actual event and subjects is additional to the quantum calculation.

This is an exact necessity-and-sufficiency result **within the stated common-response, two-subject and active-sector model**. It does not say that all possible experiential theories must use a current eigenvalue, that distinct subjects must have the same response, or that the whole contains no compensating contributions elsewhere. The outside-sector term also shows why an assumption about inactive incidences cannot be hidden; setting `q(0)=0` means zero *signed contribution* in this response model, not necessarily absence of an experience.

### Incidence and quality are separate obligations

If, more narrowly, per-incidence signed quality is stipulated as `v(x)=κx` with `κ>0`, and a positive common response weight is `w(x)`, then `q(x)=κx w(x)`. The active pair balances exactly if and only if

```text
w(+1)=w(−1).
```

This derives the required **sign-even incidence** condition from the model; it does not derive that condition from zero or imply equal incidence in nature. For example the positive, exchange-covariant choice `w(x)=1+ηx`, `0<η<1`, yields

```text
w(J₁)κJ₁ + w(J₂)κJ₂ = 2κη P.
```

The two responses are jointly measurable in the formal model because each weight is a function of its current; its spectrum is positive. The result is `2κη` in every active current event, including both sharp recorded branches. This current-weight example is distinct from the previous report's two-time endpoint-change weights. It shows that physical opposition, common response form, positivity and exchange covariance do not fix experiential incidence.

Conversely, a constant or otherwise sign-even weight with `q(x)=κx w(x)` produces `(+κw,−κw)` at the sharp point. Those would be **two nonzero contributions** if the subject and feeling hypotheses were true. A negative contribution would remain a real local negative experience, not be erased by a positive one. There is no assumption that the positive counterpart is pleasure or that an aggregate zero justifies suffering.

As an independent counterexample, `q(x)=−|x|` gives `q(+1)=q(−1)=−1` and an active-pair total of `−2`: both directions would be negative if that were the true experiential response. This is not an empirical claim about pain, nor proof of nonzero whole-level experience. It demonstrates why opposite physical energy directions alone do not determine opposite phenomenal signs. The same issue remains if the selected history is necessary rather than irreducibly chancy.

## 3. Why the sign is genuinely relational

At `t=π/4`, conditional on either record, both individual memory reduced states are `I/2`. More strongly, each record gives the **same** reduced state for each specified subsystem listed here:

```text
M₁,    M₂,    M₁W₁,    M₂W₂,    M₁M₂.
```

The two individual memory–battery pair states are also equal to one another in a given branch. Yet their associated joint currents are sharp and opposite, and the `J₁` sign reverses between record branches. Thus a rule that determines a candidate's signed quality solely from its present reduced state of one such subsystem—without record, relational history or other data—cannot reproduce these signs. This conclusion applies even if the two subjects are assigned different fixed functions: each candidate's reduced state is unchanged across the two branches.

There is a more direct controlled comparison. Apply the logical phase flip `Z_M₁` at `t=π/4`, keeping the original Hamiltonian and factor interpretation fixed. It is an operation on one encoded memory block, preserves all four work occupation observables and hence their conserved totals, and satisfies

```text
Z_M₁ J₁ Z_M₁ = −J₁.
```

After the pulse, the current correlation with the unchanged sphere observable is `⟨T_dir J₁⟩=−1` instead of `+1`; the reduced states of all five subsystems above remain identical to their pre-pulse values, including when conditioned on either original record. This is an actual unitary intervention in the model, not merely relabeling coordinates. A joint current measurement can distinguish the two global states, while those subsystem density matrices alone cannot.

The intervention acts in a model with an explicitly **four-body, potentially nonlocal** interaction. The current is not an observable of the first memory alone or of either memory–battery pair alone. The reduced-state result is not proof that two real biological subjects have the same whole local physical state, that experience is nonlocal, or that a spacelike signal is possible. Adding a local phase-control apparatus or a subject's history supplies extra information not included in the minimal reduced density matrices. The result rejects only a tightly specified present-reduced-state-only rule, not relational or history-sensitive alternatives.

## 4. What a non-decorative experiential bridge must do

The construction now supports the following explicit test rather than an association of words:

1. **Subject incidence:** identify two actual, persistent subjects in a physical realization, rather than selecting memories solely because they cancel.
2. **Signed quality:** identify what the two values feel like and why reversal of the physical relation changes that quality. The physical sign alone permits both an odd response and the two-negative response above.
3. **Actual measure:** justify why the relevant signed response is odd, or provide a different whole-level accounting that balances actual experiences. Merely imposing equal weights for this pair would assume the result.
4. **Operational and quantum consistency:** specify actual record incidence and measurement/context dependence without turning a remote conditional state into a locally accessible signal; see the earlier [steering/no-signalling analysis](ZERO_EXPERIENCE_STEERING_NO_SIGNALLING_CONSTITUTION.md).
5. **Physical domain:** derive a suitable interaction and locality from the whole rather than treating this engineered four-block gate, chosen Hilbert space or time parameter as fundamental.

An empirical implementation would require independently established subject candidates, controlled physical interventions, blinded reports or other independently validated experiential indicators, and comparison of the odd-response and two-negative alternatives. The spin-zero qubit toy is **not** an empirical protocol for identifying conscious systems; its measurement predictions only show what a suitable implementation of the stipulated operators would do.

The positive result is a genuine mathematical connection: the same internally selected spherical relation, a jointly sharp physical opposition and a necessary-and-sufficient signed-response condition now meet in one construction. The stronger claim that zero's constitution determines real subjects, felt qualities and their actual global counterterms remains the target; this model neither assumes those as brute acceptable facts nor establishes them.

## Verification

```text
python -m unittest verification.zero_sharp_opposition_and_experiential_response_test -v
```

Twelve standard-library tests verify the current spectrum and sharp branch correlations, mismatch probability, reduced states, phase-flip control, exact general response identity, positive sign-sensitive incidence counterexample, nonzero opposite and two-negative response alternatives, endpoint mean/variance distinction, and two five-state clock constructions. The calibrated clock calculation checks the matrix-exponential amplitudes, conditional branch weights, finite-difference Schrödinger equation and current compression; its exact calibration identity follows from path parity. The general response theorem is an algebraic spectral identity for all states; numerical examples are checks, not its proof. The tests do not establish actual subjecthood, phenomenal quality, measured incidence, spatial locality, emergent spacetime or a global cosmological energy zero.
