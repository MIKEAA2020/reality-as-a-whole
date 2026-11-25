# Sphere memory, subject access and a discriminating report

## Main result

The new auxiliary memory improves recovery of *source labels*, but **it does not by itself give access to the sphere sign or choose an experiential bridge**. On the actual sphere-coupled clock history:

1. At every intermediate tick, if all source qubits and all their reference qubits are excluded, the old system and **the entire added apparatus** factorize after the source interface has dephased the old sphere sectors. This holds for arbitrary initial old states and arbitrary auxiliary coding of the stated form—not just the specific input or Born probabilities. The apparatus alone therefore supplies no extra information about any old observable to a reader who already has their chosen part of the dephased old system.
2. A particular *additional interface* changes the answer. With the old j record and sign pointer M, plus reservoir R and one source reference F₁, the best probability of reading the physical sphere parity `s b` rises from `3/4` to `13/16`. One clean auxiliary bit carrying reset noise makes it **1**; two thermal auxiliary bits using a specified redundant code give `113/128`. These are optimum measurement probabilities for the explicitly stated accessible systems and prepared state, not predictions about an actual brain or subject.
3. Once both physical parities are available, a separately assumed reliable first-person report can distinguish the two candidate experience laws on the `1/4` of the original Born weight where they disagree. But **a physical parity readout is not automatically a report of what was felt**. With the physical model and symmetric Born-weighted incidence premise fixed, both candidates still balance; improved access does not select either one.

This is an integrated access-and-report test using the prior apparatus, rather than an assertion that an observer can use every system in the global state. It does **not** derive a subject, subjective valence, the incidence measure, or the ultimate constitution from zero. The [executable verifier](verification/zero_sphere_reuse_experiential_access_test.py) checks eight finite-model claims; the previous [auxiliary-memory report](ZERO_SPHERE_REUSE_AUXILIARY_RECORD_RELIABILITY.md) defines the gates and resource bookkeeping.

## 1. The two candidate bridges and their actual common domain

Use the existing actual post-sign-gate old state, separately at each of its 16 relative-clock histories. The old conserved sphere observable B and disturbed record Zj have simultaneous signs `b,z=±1`; M stores the sign `s=±1`. On the *same stipulated persistent subject incidence*, the competing intrinsic signed-quality candidates are

```text
v_B = κ s b,       v_j = κ s z,      κ>0.
```

This is a controlled comparison, not a claim that either operator is actually felt. A carrier and its persistence, the identification of a signed physical parity with valence, and the interpretation of Born weights as subject-incidence weights are extra premises. The source references or other factors are not automatically available to that carrier.

The old quantum calculation gives, after summing over the unused Alice record and either value of s,

| b | z | Born weight |
|---:|---:|---:|
| +1 | +1 | 1/2 |
| −1 | +1 | 1/4 |
| −1 | −1 | 1/4 |

For each b,z the two s signs have equal weight. Hence the candidates agree on `3/4` and are opposite on `1/4`. The verifier recomputes the old projected quantum states for all 16 histories, checks this table, and checks that the conditional j density matrices needed for the subsequent access calculation are diagonal. These are jointly readable commuting final observables; they are not a supposed unobserved trajectory through an earlier noncommuting gate.

The prior [persistence test](ZERO_PERSISTENT_CARRIER_AND_SIGN_SELECTION.md) already established that persistence alone fails to choose between these bridges, and that adding quality stability selects only within a restricted class. The [memory echo](ZERO_DYNAMIC_SUBJECT_BOUNDARY_AND_MEMORY_ECHO.md) already showed that another memory-dependent quality candidate survives that restricted selection. The present result does not claim to overturn either result.

## 2. A no-reference factorization theorem

The actual source interface prepares three independent source–reference Bell pairs and, conditional on the old B sign `b_bit∈{0,1}`, flips each source bit. In source computational labels,

```text
y = x XOR b_bit 111,
```

where x labels the three reference qubits. From the interface through the intermediate clock readings, all subsequent memory/energy operations use y as a control and do not change y. They act on the added apparatus A, which here includes **the working bit, reservoir, auxiliary bits, both stores and all their purifiers**. Initially A and the source pairs are independently prepared from the old state. The source-control law and the chosen initial states are stipulated; no reference to an external physical master time is required by the algebra.

For a clock reading `t=1,…,13`, write `V_y(t)` for the actual conditional unitary on A, with its appropriate forward or reverse gates. After tracing all source qubits and their three references, the exact old–apparatus state is

```text
ρ_old,A(t) = [Σ_b Π_b ρ_old Π_b] ⊗ σ_A(t),
σ_A(t) = (1/8) Σ_y V_y(t) ρ_A V_y(t)†.
```

**Reason.** In the trace, a source-reference basis pair fixes both x and y. Since `y=x XOR b_bit 111`, it fixes b as well, removing cross-sector terms. For each fixed b, x is uniform, hence y is uniform; the resulting apparatus state `σ_A` is the same for either b. This argument applies to any old density operator, including coherent and entangled old states, and allows all auxiliary purifiers and stores to remain within A. It does not rely on treating f, e, x or y as actual hidden trajectories.

At tick 0 the interface has not yet acted, so the old state is not dephased. At tick 14 the entire circuit, including the inverse sphere interface, has been undone, and the original old state and preparations are restored. A coherent finite-state calculation checks factorization at all ticks for an old state entangled across B and a second old qubit; exact probability checks use the actual apparatus with several clean and thermal codes. The proof above gives the general statement.

**Operational consequence.** Given any accessible part L of the dephased old system, adding any or all of A cannot improve an optimal POVM on L for an old target: the added system is in the same product state for every target value. This does not say the interface has no back-action—it has dephased the old B sectors. Nor does it cover access to source qubits or references, an initially correlated apparatus, a different interface, or a later operation that changes the old system. It is a result for the stipulated interface, not a universal law about records or observers.

## 3. What changes when a source reference is accessible

Take the forward midpoint after all three swaps. The actual memory correlations are

```text
R₀ = y₀,
R₁ = y₁ XOR f₀,
R₂ = y₂ XOR f₁,
yᵢ = xᵢ XOR b_bit.
```

The table below gives optimal recovery of `h_B=s b`, assuming M is registered and the reader has j, M, all three R bits, all indicated auxiliary C bits, and precisely the stated reference. Other source references, all source qubits, A, batteries and purifiers are inaccessible. The added memories are initially Gibbs at `q=1/4` unless called clean. The earlier model's signed charges remain conserved; the clean blank is an additional prepared resource.

| Reference and auxiliary | Best `P(guess h_B)` |
|---|---:|
| No source reference; any tested C code | `3/4` |
| F₀, no C | `1` |
| F₁, no C | `13/16` |
| F₁, one thermal C copying f₀ | `55/64` |
| F₁, one **clean** C copying f₀ | `1` |
| F₁, two thermal C bits both copying f₀ | `113/128` |
| F₁, two thermal C bits copying f₀ and f₁ separately | `55/64` |

For example `R₁ XOR x₁ = b_bit XOR f₀`. With clean `C=f₀`, the accessible relation

```text
b_bit = R₁ XOR x₁ XOR C
```

is exact. F₀ needs no correction because `R₀=y₀` exactly. The no-reference `3/4` is already attained by using z as the guess for b; without j, M plus the added apparatus alone gives `1/2`. A subject accessing F₁ is an explicitly different boundary/interface hypothesis from one confined to j, M and the added reservoir.

The `13/16` can also be seen directly: z=− occurs with weight `1/4` and already fixes b=−; at z=+, which has weight `3/4`, the F₁/R₁ channel has error `1/4` and improves the guess of b to success `3/4`. Thus `1/4+(3/4)(3/4)=13/16`.

For the noisy auxiliary family, exhaustively searching all binary **linear** codes into k thermal bits with F₁ available yields optima `13/16`, `55/64`, `113/128`, and `931/1024` for `k=0,1,2,3`. The optimal two-bit code redundantly copies f₀ twice. This is not an optimum over arbitrary nonlinear or coherent protocols and preparations. Once a code is fixed, the displayed decoder **is** optimal among POVMs on the stated accessible quantum registers: tracing the source and excluded references and purifiers leaves a classical block in R, C and F₁, and the actual old b,s-conditional j blocks are diagonal for all 16 histories. The analytic factorization in §2 is stronger than this particular classical search.

Note that an earlier perfect full-triple recording and a perfect sphere-sign reading are not interchangeable. Source labels alone do not reveal b. The matched reference is essential, even with perfect source-label memory.

## 4. Physical parities versus felt sign

Under the clean-C/F₁ access hypothesis, `h_B=s b` and `h_j=s z` are both computable from commuting accessible registers. To see that these are **physical readouts** rather than abstract labels, prepare two degenerate neutral pointer bits and XOR into them:

```text
h_B sign bit:  M XOR R₁ XOR F₁ XOR C,
h_j sign bit:  M XOR j.
```

The signs `+1,−1` correspond to bits `0,1`. Controlled XORs leave their control registers unchanged, are unitary, and preserve the modeled signed charges: R₁ and C are used as occupation controls, F₁ and the new pointers are degenerate, and j and M are compatible neutral controls for the stated gauge/old constraints. The verifier checks the relevant old commutators and the clean-C identity. This does not include a proposed physical implementation cost for the neutral pointers, nor does it identify those pointers with a subject. Tracing them can dephase the measured coherences; the claim is about the specified joint-readout experiment.

The same accessible record is compatible with either hypothetical experiential law. Seeing both parities tells us *where they disagree*, but it cannot itself tell us which one, if either, is felt. This is not merely a matter of uncertainty: a calculator can write either parity into a physical bit, but neither operation establishes the intended phenomenal meaning.

The role of a boundary rule is therefore sharply constrained. A strict subject boundary excluding F₁ cannot infer `h_B` perfectly from j, M and the added apparatus in this setup; a boundary that includes the specified F₁ interface and clean C can. **Access does not by itself prove that an accessible property is experienced**, or that an inaccessible global description has no intrinsic counterpart. Both are additional claims about how the one reality's intrinsic and extrinsic aspects relate. The richer-domain analogy likewise does not justify inserting the F₁ interface without an actual interaction path.

## 5. A conditional discriminating experiment

Suppose, as a **separate** hypothesis, that the candidate carrier is a subject and can produce an independently obtained binary report `r=±1` of its actual felt valence. Compare the two complete physical–experiential/report models:

- `H_B`: felt sign is `h_B`, and the report has error probability ε relative to it.
- `H_j`: felt sign is `h_j`, and the report has the same error probability ε relative to it.

For the displayed numerical comparison, assume the same independent error rate conditional on each relevant joint state and on whether `b=z`. Then

| Statistic | `H_B` | `H_j` |
|---|---:|---:|
| `P(r=h_B)` over all trials | `1−ε` | `3/4−ε/2` |
| `P(r=h_B | b≠z)` | `1−ε` | `ε` |

For ε<1/2 the conditional predictions differ. A weaker and more robust version needs no independent-error model: if, **on the mismatch trials**, each hypothesis guarantees report accuracy at least `1−ε`, then `H_B` predicts alignment with h_B at least `1−ε`, whereas `H_j` predicts it at most ε. Merely assuming an overall average accuracy does not automatically imply the same conditional bound. The experiment requires access to the mismatch flag, the qualified subject, calibration, independence or a justified error model, and an actual implementation of the relevant physical observables.

These are rival *completed report models*, not two different readings of one guaranteed fixed report. If the felt sign makes a different truthful report, the full physical–experiential histories may differ. A physical XOR detector of h_B or h_j cannot be used as the supposedly independent first-person report without assuming precisely the bridge being tested. A laboratory or biological translation would need an independently specified realization, operational markers and an ethical, preregistered protocol; this finite circuit alone gives no such translation and no prediction for human valence.

## 6. Zero, counterparts and what is actually selected

The original stipulated counterpart operation changes s while retaining b and z. The newly added operations depend on b and source/noise registers, not s, so the counterpart still pairs opposite physical values of both h_B and h_j at fixed b,z and apparatus outputs. Under the **extra premise** that the relevant actual subject incidences carry the symmetric Born measure, both signed sums are zero, even within either b sector. They differ on the mismatch weight nevertheless. The added signed-energy constraint also stays zero, but it is a separately constructed charge: it neither proves objective global energy zero nor yields an experiential sum.

If the true whole has an additive signed experiential quantity, cancellation must include the appropriate actual positive counterpart to negative felt valence, with justified weights and convergence. This calculation does not identify those counterparts, imply that a person does not suffer, or establish that pleasure erases suffering. Mirror closure, the distinction between physical counterparts and gauge copies, actual incidence and its measure still require a constitutive account. Necessitated weights would not automatically be irreducible objective chance.

**What this round selects:** with this prepared interface, no-reference apparatus is irrelevant to old-system inference; F₁ plus clean noise memory is sufficient to read h_B; and the explicit report hypotheses are distinguishable. **What it does not select:** the subject boundary, which physical relation is intrinsically felt, or the incidence measure. That limitation is not a proof that the user's no-residue demand is impossible. It identifies where a proposed constitution must do more than provide symmetrical records.

A stronger next construction would start from one explicit candidate constitution of the accessible algebra and intrinsic quality, then check it against *both* this no-reference factorization and the established memory-echo intervention, rather than defining a boundary by whichever bridge one wants. It must explain why the relevant interface and subject lineage follow from that constitution and produce a measurable difference from a rival; simply renaming an accessible parity as experience is circular.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps \
 python -m unittest verification.zero_sphere_reuse_experiential_access_test -v
```

Eight tests cover the actual old quantum states at all 16 histories; exact no-reference independence at every tick; coherent old–apparatus factorization and restoration in a finite test; optimal no-reference and reference-assisted scores; exhaustive linear noisy-code searches through k=3; gauge-compatible physical parity reporting; and the conditional report-model and Born-weighted balance arithmetic. The general factorization is proved above. The previous two verifiers independently test the physical source interface, the 14-tick clock, zero-charge conservation and full reversal.
