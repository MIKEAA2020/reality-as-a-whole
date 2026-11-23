# A relational history with a fixed confined record

## Result

The prior [four-connection model](ZERO_FOUR_CONNECTIONS_CONFINEMENT_COHERENCE_EXPERIENCE.md) gave a family of richer quantum states but did not put them into one ordered history. This continuation constructs **one stationary, finite relational history** over the same asymmetric sphere–record system. The clock is a subsystem of the model, not a clock outside the whole.

Conditioned on its five ordered clock labels, the entire confined candidate-subsystem state remains the same, while a richer record–current correlation follows the exact sequence

```text
1,  1/√2,  0,  −1/√2,  −1.
```

There is no extra confined move while those richer correlations differ. As the user stressed, no interaction is needed to hold a game’s move count fixed: thinking is not a game move. Here the mathematical history simply has a fixed confined state at each specified label; its clock construction is **not** proposed as the mechanism that makes confinement possible.

The comparison produces two further results:

- The **same positive zero-constraint and the same confined records** admit two orthogonal histories with opposite richer correlations. The constraint does not by itself select the experiential or physical history.
- Two distinct, perfectly synchronized clock factors give exactly the same conditional states. A lower-resolution readout averages the correlation in a calculable way. A complementary Fourier readout yields zero conditional mean for every outcome, but is **not** shown to be an ordered clock. These are different measurements, not evidence that relabeling time changes reality.

The two experiential hypotheses from the previous report can be evaluated on the ordered history and make different predictions. Actual experiencing subjects, temporal passage, selected outcomes, relativity and a derivation from zero remain substantive requirements, not consequences of the clock mathematics.

## 1. One whole-history state, no external time assumed

Let `|Ψ₊⟩` be the existing five-ray state, with the two reference blocks understood as initialized as before. Put

```text
Z = Z_M₁,             U = exp(iπZ/8),
|ψ_k⟩ = U^k |Ψ₊⟩,     k=0,1,2,3,4.
```

Add a five-level **internal** clock C, with orthonormal states `|k⟩`, and define the single joint state

```text
|Hist₊⟩ = (1/√5) Σ_(k=0)^4 |k⟩_C |ψ_k⟩.
```

The existing encoding accommodates the clock's five labels in a six-physical-spin singlet sector. With the 46-spin sphere–record/reference extension this is **52 physical spins** before any additional apparatus. The encoding, the clock factorization, its orthogonal states and the relation U are specified inputs, not selected by a previously assumed outside time.

Define link operators and a positive open-path constraint

```text
D_k = ⟨k+1|⊗I − ⟨k|⊗U,       k=0,1,2,3,
C_prop = (1/2) Σ_k D_k†D_k.
```

Each link residual `D_k|Hist₊⟩` vanishes, so

```text
C_prop |Hist₊⟩ = 0.
```

This is the standard finite history-state mechanism, not a new general theorem. `C_prop` can be used as a time-independent Hamiltonian for which the displayed state is stationary. Its zero is a deliberately constructed **constraint eigenvalue**; it is not a demonstration that the objective total energy or total experience of the whole is zero. In the preceding physical realization the bare work occupation energy is 2, not zero. The link operator acts on the clock and the work factor, not on the confined record/reference blocks. This fact checks the specified model; it is not a necessary holding mechanism for the user's analogy.

If the clock is read sharply and yields k, ordinary quantum conditioning gives the normalized system state `|ψ_k⟩` with probability `1/5`. Uniformity is a property of this chosen normalized history, not a derived measure over actual lives, clock times, universes or all possibilities. The five labels and U give a proposed ordered relational description. A conditional state is not yet a selected outcome, an irreversible record or a proof that a subject experiences passage.

## 2. Same confined state, richer ordered distinctions

The confined subsystem is the same `S={H₁,R₁,R₂,H₂}` used in the preceding comparison. Since each `U^k` acts outside S,

```text
ρ_S(k) = ρ_S(0)    for every k.
```

This equality concerns the **entire** reduced state, not only the mean of one chosen observable. The original asymmetric sphere/record table is also unchanged at each clock label:

| Sphere label | Record `01` | Record `10` |
|---|---:|---:|
| 0 | `3/40` | `1/20` |
| 1 | `1/10` | `3/10` |
| 2 | `13/40` | `3/20` |

With `K=Z_R₁J₁`, the exact clock-conditioned probe mean is

```text
⟨K⟩_k = cos(kπ/4).
```

For `r=+1` in record `01` and `r=−1` in record `10`,

```text
E[J₁ | k,r] = r cos(kπ/4),     E[J₂ | k,r] = −r cos(kπ/4).
```

Thus a richer relation can distinguish k=0,1,2,3,4 without making those labels into changes of the confined record. The register's `01` and `10` values are alternatives within the quantum state, not successive A and B positions. A definite r must be supplied by an outcome/actuality account before speaking about an actual particular branch.

**Current caveat:** `J₁=i[G,N_M₁]` is the probe defined by the *earlier exchange Hamiltonian* G. The present propagation constraint is built from phase gates commuting with `N_M₁`; therefore

```text
i[C_prop,N_M₁] = 0,
```

whereas the probe `J₁` is nonzero. The displayed varying conditional probe is **not** the physical current of this new clock Hamiltonian. This distinction is verified and is essential. At intermediate k it is also a conditional mean, not a definite sharp eigenvalue. We have not derived realistic spatial locality, a neural signal or a relativistic implementation.

## 3. One constraint, two opposite histories

Define the orthogonal initial state `|Ψ₋⟩=Z|Ψ₊⟩`, and use **the same** U, same clock, same confined subsystem and same `C_prop`:

```text
|Hist₋⟩ = (1/√5) Σ_k |k⟩ U^k |Ψ₋⟩.
```

Then

```text
C_prop|Hist₋⟩=0,             ⟨Hist₊|Hist₋⟩=0,
ρ_S⁺(k)=ρ_S⁻(k),             P⁺(i,r | k)=P⁻(i,r | k),
⟨K⟩⁺_k=cos(kπ/4),           ⟨K⟩⁻_k=−cos(kπ/4).
```

Both histories obey the same specified physical constraint, have the same clock-label probabilities and confined record table, and retain the original operator relation `J₁+J₂=0`. Yet they are orthogonal states with opposite richer correlations. This is not merely changing coordinates: the observables and apparatus identification are fixed.

Indeed the propagation constraint is intrinsically degenerate. For **any** initial system state `|φ⟩`, the vector `Σ_k |k⟩U^k|φ⟩/√5` lies in its kernel. Since C is a sum of positive link terms, every kernel vector must have successive blocks related by U; hence the kernel has the dimension of the system Hilbert space. A boundary/selection rule or a richer constitution would be needed to select particular initial data. Adding such a rule to obtain `|Ψ₊⟩` would be an additional hypothesis, not a derivation from the bare equation `C_prop=0`.

This is a precise test of what **this** zero means: it enforces compatibility along a specified history but does not select the history, the phase orientation or an experiencer. It is not a proof that the user's full self-sufficient zero constitution cannot determine them, nor that the two mathematical states are independently actual worlds. The user's actuality–genuine possibility thesis would need to explain which structures are genuine and how their incidence relates, not simply declare inconvenient alternatives unreal.

## 4. Clock comparison: what changes and what does not

### A. Two synchronized clock factors: an exact agreement case

Add a distinct five-level clock D and use the isometry `W|k⟩_C=|k⟩_C|k⟩_D` to form

```text
|Hist̃₊⟩ = (1/√5) Σ_k |k⟩_C |k⟩_D |ψ_k⟩.
```

Conditioning on `C=k` and tracing D gives exactly the same system state `|ψ_k⟩` as conditioning on `D=k` and tracing C. Both give label probability `1/5`, the same full confined state and the same `⟨K⟩_k`. This is an explicit comparison of two clock **subsystems** on one state, not just renaming one clock. Their readings are perfectly synchronized by construction, so they are not independent clocks with realistic error, relative motion or backreaction; the copying is of specified orthogonal states, not cloning arbitrary unknown quantum states.

It can use the positive constraint

```text
C_two = (W⊗I) C_prop (W†⊗I) + (I−WW†)⊗I.
```

Both terms are positive and `C_two|Hist̃₊⟩=0`. The orthogonal history obtained by embedding `Hist₋` also satisfies the same constraint, so adding this agreeing clock does not uniquely select a history. A second six-spin encoded clock would bring the stated physical-spin count to **58**. The encoding and synchronization are specified, not derived; this construction does not show that arbitrary clocks agree or that two laboratories are spacelike separated.

### B. A monotone, lower-resolution clock readout

In the original one-clock history, keep the same clock but read only whether `k∈{0,1}` or `k∈{2,3,4}`. This is a valid ordered **coarse readout of the same clock**, not a second independent physical reference frame. The probability and conditional K mean are

| Clock bin | Probability | Conditional `⟨K⟩` |
|---|---:|---:|
| `{0,1}` | `2/5` | `(2+√2)/4` |
| `{2,3,4}` | `3/5` | `−(2+√2)/6` |

These numbers are weighted averages of the sharp-clock conditional statistics. They demonstrate ordinary loss of resolution without inserting extra confined events. They do not themselves establish the duration of an experience or a preferred scale.

### C. A complementary clock measurement

On the **same history state**, use the Fourier basis

```text
|f_m⟩ = (1/√5) Σ_k exp(2πimk/5)|k⟩,    m=0,…,4.
```

The five outcome probabilities are approximately

```text
(0.7265764, 0.1045279, 0.0321839, 0.0321839, 0.1045279),
```

and, remarkably for this chosen family,

```text
E[K | f_m] = 0     for every m.
```

This follows analytically as well as numerically. Let `a_m=Σ_k cos(kπ/8)e^(−2πimk/5)` and `b_m=Σ_k sin(kπ/8)e^(−2πimk/5)`. Because `sin(kπ/8)=cos((4−k)π/8)`, `b_m=e^(−8πim/5) conjugate(a_m)`. Their magnitudes are equal, so the two K-eigencomponents have equal conditional weights. For this family the full conditioned S state is also unchanged.

The Fourier basis is **not shown to be a suitable ordered clock**: its outcomes do not supply the previous ordered k record, and its measurement is incompatible with a sharp k measurement. Conditioning on it produces different postselected states. Comparing those states with the k-conditioned states is not a coordinate change on the same event, and does not establish observer-dependent reality or failure of covariance. By contrast, a mere relabeling of k while transporting the state, observable and ordering leaves the physical conditional facts unchanged. The tests check that distinction.

The synchronized C/D example is a definite equivalence case; the coarse and Fourier examples are controlled, limited readout comparisons. A comparison of **independently calibrated, imperfect clocks or quantum reference frames**, including clock backreaction and common observable transport, remains an additional task. None is a solution of the general problem of time.

## 5. Experience and persistence: explicit assumptions, distinct predictions

Continue the previous pair of experiential hypotheses for **richer-domain experiencers** `P₁,P₂`; these are analogous to the player/traveler, not the chess pieces or surface inhabitants. Suppose, without claiming to have derived it, that:

1. `P₁,P₂` are actual subject incidences with equal weights;
2. each has a persistence relation across the relevant k-conditioned events;
3. a definite record r and the relevant clock-conditioned branch are actual in the proposed account;
4. a common unit `κ>0` and a physical–experiential relation are meaningful.

On `Hist₊`, the two prior proposed laws give

```text
P:  (v₁,v₂) = ( κ r cos(kπ/4), −κ r cos(kπ/4) ),
Q:  (v₁,v₂) = ( κ r,             −κ r ).
```

They agree at k=0 but differ at k=4, while the entire confined state remains unchanged. Thus the history provides the missing **ordered mathematical setting** for the earlier experience–time question. The positive/negative labels are intended as genuinely felt under the hypotheses, not one person's suffering being erased by another's positive value.

Crucially, the physics has not established those hypotheses. P treats a conditional mean of a four-block probe as a designated felt contribution; it is not a sharp result at intermediate k, and it cannot be derived from a single confined pair's reduced state. Q is another experience-respecting law on the same physics. The earlier L rule does not identify these richer experiencers; subject boundaries, possible overlap, persistence and weighting require independent justification. Conditional clock states are not automatically a sequence actually lived by either subject.

Under equal incidence both P and Q have pairwise signed total zero at each k. Their common zero does **not** select which experiential law is true. If incidence is unequal, P's pair total is `κr cos(kπ/4)(μ₁−μ₂)`, which is generically nonzero; a whole-level zero does not automatically require that this pair alone balance. The previous [incidence theorem](ZERO_CONFINED_REALM_SPHERE_RECORD_INCIDENCE_THEOREM.md) states precisely the stronger assumptions under which equal weights and odd response would follow.

## 6. No-signalling and empirical status

For both `Hist₊` and `Hist₋`, the earlier pair/triple Alice choices give the same full initial Bob density operator. The same clock preparation and controlled U define a Bob-side isometry, so the **entire Bob-plus-clock** density operator is equal across Alice choices. No measurement of the clock, confined subsystem, work blocks or their joint observables can reveal which Alice instrument was used. Tests compare complete unnormalized Bob states for each sharp-clock and Fourier-clock outcome, not merely their means.

This is operational no-signalling for the specified lab partition, not a relativistic-locality derivation or proof that every conceivable experiential access, conditional ensemble, incidence rule or report model is safe. P and Q must not use Alice's inaccessible conditioning information as locally available experience. The Feynman–Kitaev link, clock and state are mathematical inputs; no universal physical present or preferred spacetime foliation is asserted.

The earlier [pain–relief readiness gate](ZERO_FOUR_CONNECTIONS_CONFINEMENT_COHERENCE_EXPERIENCE.md) remains relevant: current and experience must be independently identified, report reliability and valence scales calibrated, subject persistence justified, and outcomes tested on held-out human data with stimulus/history/expectation controls. Existing data do not measure this quantum probe, its proposed subject incidences or the experiential law. No new experiment or empirical confirmation is claimed here.

## 7. What follows for zero's constitution

This is genuine progress over a loose succession analogy: **one static state** contains a specified relational history; its confined state is unchanged at every clock value; the richer correlation has an exact sequence; an alternative readout and an orthogonal same-constraint history are calculated; and two experiential laws make distinct conditional predictions.

But a constructed constraint is not the user's sought self-subsistent zero. `C_prop=0` leaves a full kernel of histories; the choice of clock, gates, initial state, subject and physical–phenomenal bridge is not derived from that equation. The challenge is not to accept these as brute: it is to show whether the full constitution of zero necessarily determines the relevant relations, actualities and experiential incidence—possibly through all genuine possibilities—while recovering spacetime and physics without a preferred foliation. This calculation identifies a specific selection/constitution problem that such a derivation must solve; it neither establishes nor refutes the stronger thesis.

## Verification

Run `python -m unittest verification.zero_relational_history_experiential_clock_test -v`. Thirteen standard-library tests check the normalized zero-constraint histories and positivity, the full confined state and five-ray table at every label, both orthogonal histories, synchronized clock factors and their positive constraint, coarse and Fourier clock readouts, transported clock relabeling, full Bob-side no-signalling, the distinction between probe and constraint current, and the two stipulated quality laws. Quantum amplitudes and Fourier values use numerical precision; the stated irrational expressions and kernel result have the analytic proofs above. The tests do not establish actual subjective passage, a real subject, unique clock, physical higher plane, realistic locality or whole-level experiential zero.
