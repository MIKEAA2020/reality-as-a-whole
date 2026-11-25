# One coherent angular echo, purified reservoir and relational clock

## Result

This pass joins three previously separate levels of the shared candidate: the original quantum echo, its new angular record, and the 20-step source/reservoir clock with a second reference clock. It uses the **actual original echo vectors and gates**, the **actual reversible reservoir permutations and their purifiers**, and the existing conditional angular preparation. The result is a single, explicitly factorized coherent history—not an independently sampled classical trajectory for each tick. The [large-vector and reservoir tests](verification/zero_coherent_clock_angular_history_test.py) and [independent full reduced-basis stationary-POVM test](verification/zero_clock_relational_povm_test.py) check complementary parts of the construction.

The result also gives a sharper access constraint. Within either example angular band, two different magnitudes can correspond to **identical conditional states of the complete old system, echo memory, purified source/reservoir and clocks**, when the added angular record is inaccessible. A boundary restricted to those older factors cannot distinguish the two cases, even by an optimal measurement. If it additionally reads the new angular register, the bin states are orthogonal and can be distinguished. This is a physical-model statement, not a claim that either boundary is a subject.

The construction still assumes the angular preparation, old gates, purifications, clocks and operator laws. It does not identify the conserved model charges with cosmic energy, derive a subject or establish felt valence. Those inputs remain obligations for the user's stronger no-unexplained-residue objective, not accepted brute stopping points.

## 1. Source-to-candidate connection

- The user's relational-time and confined-realm instructions require distinguishing what exists in the whole from what a particular carrier can access. The [earlier locality test](ZERO_SPHERE_LOCAL_CONSTITUTION_AND_RESERVOIR_ECHO.md) compared explicitly specified carriers; no fact about a richer realm automatically becomes a subject's record.
- Page–Wootters motivates a stationary joint history and relational effects, not a preferred external time. [The two-clock construction](ZERO_STRUCTURAL_TIME_TWO_CLOCK_STATIONARY_BRIDGE.md) stipulated two distinct reference-clock preparations, `q=1,2`; they are not merely different names for the same clock.
- The [previous continuous-angle echo](ZERO_COHERENT_ANGULAR_SPHERE_ECHO_CONSTRUCTION.md) ran the actual `T–Q–T` gates and their inverse on an added quantum angular register but did not itself simulate the full purified reservoir history. The earlier [clock/quality interface](ZERO_SOURCE_INTEGRATION_CLOCK_REALM_AND_JOINT_INTERFACE.md) used an exact **reduced** probability ledger rather than the enlarged coherent vector.

**Plan:** factor the full coherent state by the original system's conserved B sectors; explicitly retain the source references and thermal purifiers as orthogonal quantum factors; compose their real forward/inverse gates with the angular echo; construct stationary two-clock effects; then test both full-state coherence and what an access-restricted carrier can tell about the new magnitude.

## 2. One coherent 20-step carrier

Fix one original source history x and one registered pointer sign s. The earlier verifier prepares the sector-correlated angular state `|ψ_s⟩` with echo memory ready. Let the independent apparatus state be the coherent purification

```text
|Φ⟩ = Σ_(x,f,e) √[ (1/8) p_Q(f) p_aux(e) ]
          |x⟩_source-reference |f⟩_purifier |e⟩_aux-purifier
          |apparatus initially prepared from x,f,e⟩.
```

Here x in the sum is a **three-bit source reference**, not the original source-history label named in the first sentence; f is the three-bit thermal purifier, and e the auxiliary purifier. The primary reservoir has `Q=1/4`; the tests use one auxiliary bit and columns `((1),(0))`, with thermal or clean auxiliary settings where stated. The spectator reference and purifier factors make distinct `(x,f,e)` components orthogonal. They are retained in the state; enumerating them in the program is not an assertion that they were measured.

The original observable B has orthogonal projectors `Π_+`, `Π_-`. The apparatus gates use B as their physical control and leave it unchanged. Thus the exact vector at tick t can be written without a fictitious B-copy register as

```text
|Ψ_t⟩ = Σ_(b=±) ( U_echo,t Π_b |ψ_s⟩ ) ⊗ ( F_t^(b) |Φ⟩ ),
```

where `F_t^(b)` is the **actual** source, reservoir and auxiliary gate prefix in the specified B sector. `U_echo,t` is identity through tick 7, follows the actual `T,Q,T,T,Q,T` gates at steps 7–13, and returns to identity thereafter. The apparatus is unchanged during those six echo steps, after which its seven gates are reversed. The factorization uses the established fact that T and Q commute with B and act on separate apparatus factors; it preserves coherence between B sectors in the full system. It is a computational representation of the same tensor state, not a new independent label or an assumption that intermediate B, j or R values have been measured.

The verifier enumerates **all** `2×8×8×2` prepared B/reference/purifier combinations for this one-bit auxiliary setting, verifies both previously specified signed model charges at every step and checks complete return. It applies the actual original quantum pulses to their complex angular/echo vectors, verifies each checkpoint and the inverse, and checks B-sector commutation on the supported state. Prior work tested the original echo and inverse for all 16 source histories and both pointer signs; this pass tests the clock-conditioned quantum predictions on source labels `0,7,15` and both signs, not an expanded full-tensor simulation of all 16. No dense state vector of every apparatus degree of freedom is constructed; the factorization and orthogonal purification retain its coherences exactly under the stated gates.

## 3. Stationarity without treating a bare clock reading as invariant

Let W be the controlled 20-step cyclic shift that advances the original clock and applies the corresponding physical gate. The gate sequence returns on the prepared carrier; since the stipulated gates have inverses, its cyclic controlled shift is well defined. Add an independent four-state reference, shift V, and choose

```text
D_q = W ⊗ V^q,
|Ω_q⟩ = (1/√20) Σ_(t=0)^19 |t⟩_C |Ψ_t⟩ |qt mod 4⟩_R,
q∈{1,2}.
```

The wrap is consistent and `D_q|Ω_q⟩=|Ω_q⟩`. These are distinct prepared clock correlations; a randomization or readout protocol is an additional resource. The clock is an internal relation in this finite model, not an established proper-time observable or a derived foliation.

A bare projector onto `R=2` is generally **not** invariant under `D_q`. To specify the clock-conditioned calculation as a stationary protocol, choose an anchor t uniformly and twirl the anchor event around the cycle:

```text
Q_(t,r,A) = Σ_(k=0)^19 D_q^k ( |t⟩⟨t|_C ⊗ A ⊗ |r⟩⟨r|_R ) D_q^(−k),
E_(r,A)   = (1/20) Σ_(t=0)^19 Q_(t,r,A).
```

For a projector A, each twirl is a projector: its terms occupy distinct original-clock blocks. Each commutes with `D_q`; the averaged effects are positive and at most identity. For `A=I`, the four reference effects form a POVM. For `A=P_D`, its joint effect is bounded above by the corresponding reference effect. Operationally, the uniform anchor choice is part of the stated comparison protocol; no claim is made that an inhabitant automatically has its control or outcome.

On the prepared history,

```text
⟨Ω_q|E_(r,A)|Ω_q⟩
  = (1/20) Σ_(t : qt=r mod 4) ⟨Ψ_t|A|Ψ_t⟩.
```

The [separate reduced-basis verifier](verification/zero_clock_relational_povm_test.py) builds the cyclic permutation and these effects on **every** reduced B/j/echo/s/angular/reference basis state, not just the history orbit. It checks the whole-basis commutators by exact permutation, POVM normalization, the prepared coherent reduced history, the reference-conditioned disagreement, and the negative control that a bare reference projector is not stationary. The full original-system implementation follows the same gate-twirl algebra; the program does not materialize its huge dense matrix or an operational apparatus for the twirl.

## 4. The original quantum vectors reproduce the clock comparison

Let `C=(B=r_echo)` and `D=(r_echo=−1)`. D is the disagreement of the two earlier candidate sign rules `sj` and `sjr`, not an already felt experience. With the actual angular quantum vectors at **N=4** and the purified apparatus composed as above, the uniform-anchor protocol gives:

| Reference | P(reference event) | P(C) | P(D) | E[|u| 1_D] | E[|u(u+1)| 1_D] |
|---|---:|---:|---:|---:|---:|
| q=1, r=2 | 1/4 | 3/5 | 1/10 | 1/20 | 3/160 |
| q=2, r=2 | 1/2 | 11/20 | 1/20 | 3/80 | 3/320 |

The four quantities after the event probability are conditional on that reference event. Every D case is also C in this model. For q=2, r=1 and r=3 have zero probability, so conditioning on them is undefined.

These quantum checks recover the prior sign/joint ledger, but the last column **differs** from its continuous-integral values. This is the expected finite midpoint discretization, not a contradiction. For N divisible by four, the mean of `g₂=|u(u+1)|` on either negative half-band is `1/6+1/(3N²)`, giving

```text
q=1:  1/60 + 1/(30N²)  → 1/60,
q=2:  1/120 + 1/(60N²) → 1/120.
```

The `|u|` result is already exact at these midpoints. The common-L² construction in the prior report establishes the continuous multiplication-operator limit; the present direct large-vector clock check uses N=4. For each fixed original clock anchor, tracing the reference does not change that anchor's quantum system state. Averaging reference-conditioned data nevertheless gives different predictions because the two physical preparations group different anchors.

## 5. A full-carrier coherence comparison

The joint history is pure, but neither the added reservoir records nor the added reference can be assumed invisible to its reduced clock. At ticks 7–13 the actual apparatus state is unchanged, so its full purified overlap is exactly 1. For the tested source labels and pointer sign s, the actual old-system/echo/angular overlap is

```text
⟨Ψ_7|Ψ_9⟩ = ⟨Ψ_7|Ψ_10⟩ = s/2.
```

Before adding the four-state reference, these off-diagonal entries of the original clock marginal are `s/40`. Tracing the reference multiplies entry `(t,u)` by `δ_(qt,qu mod 4)`:

* `(7,9)` is erased for q=1 but retained for q=2;
* `(7,10)` is erased for both.

Thus the clock choice changes an explicitly computed **full-system** coherence, not just an abstract clock-only toy. Separately, for the specified thermal apparatus at ticks 0 and 7, the prepared apparatus overlap is `9/128` in B-positive and zero in B-negative; the actual old B-sector weights are one half each. Therefore `⟨Ψ_0|Ψ_7⟩=9/256`, showing that the source/reservoir gates themselves already alter the clock marginal before the reference is attached. The analogous values are conditional on the specified preparations and not a general law of time or decoherence. A pure global history can have these mixed reduced clocks without an external observer.

## 6. What a confined carrier cannot infer

At N=8, choose the two negative-band bins `u=−7/8` and `u=−5/8`, or the positive-band bins `u=1/8` and `u=7/8`. The bins in each pair have the same B and initial j sector but different values of both `|u|` and `|u(u+1)|`. Direct application of the actual T–Q–T gates shows that within each pair the old-system plus echo-memory vectors are identical after normalizing by the common bin weight. Their source/reservoir apparatus states also coincide, because the apparatus controls on B and not on which angular bin in that sector was prepared. A fixed anchor's original and reference clock labels are likewise the same.

Consequently, for a specified experiment that conditions on either bin and then withholds the added angular record, the two complete accessible density matrices are equal. With equal priors, **every** measurement on that old carrier plus apparatus and clocks has success probability exactly 1/2 for telling which of the two bins was prepared. If A is supplied, its orthogonal bin states give a perfect readout. This comparison assumes the particular conditional-bin preparations and allowed carrier algebra; it is not a claim about every imaginable preparation or operation that couples to A.

Under the additional *candidate* principle that a subject's instantaneous magnitude must be a single-valued function of that selected accessible reduced state, neither varying g law can be implemented at that boundary for both bins. Access to A removes this particular indistinguishability, but it does **not** prove that any actual subject experiences its value or that local-state sufficiency is the right bridge. Richer-realm activity is not automatically registered by a surface/game inhabitant; adding A explicitly changes the allowed interface.

## 7. Constitutional consequence

The new construction shows how the user's relational-time, carrier confinement and point–sphere directions can coexist in **one** quantum model, and pinpoints a substantive selection issue: different angular magnitudes can be real physical distinctions in the enlarged model yet unavailable to a narrower candidate bearer. It neither declares those distinctions to be experienced nor removes them by averaging. Positive and negative local experiences, if later derived, remain real even when a signed total vanishes.

The remaining constructive step is to derive, rather than stipulate, the physical angular carrier and measure, clock coupling, actual subject boundary and physical–experiential identity from the zero whole; then establish any relevant incidence symmetry and whole-level quantity. The finite model and its charge balance are not a proof of zero's self-subsistence, a complete foundation or external battery pass.

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_coherent_clock_angular_history_test \
 verification.zero_clock_relational_povm_test \
 verification.zero_quantum_angular_echo_test -v
```
