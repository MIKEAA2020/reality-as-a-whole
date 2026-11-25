# Necessary plenitude as sign pairing: an exact construction

**Physical-interface continuation:** [dual pairing and energy-conserving sphere readouts](ZERO_DUAL_PAIR_SPHERE_ENERGY_CONSERVING_INSTRUMENT.md) constructs the five-ray measurement, two finite reference pairs and a relative-clock pointer in an exact zero-energy finite system.

**Incidence continuation:** [the actual source identity pair and incidence flag](ZERO_IDENTITY_PAIR_PHYSICAL_FLAG_AND_INCIDENCE.md) recovers a conditional equal physical reference from the sphere-coupled reservoir model and tests whether a sharp flag can consistently supply type weights for all effects of the same pure physical state.

**Directional continuation:** [zero as origin, jet and paired constraint](KAMLAPURE_ZERO_ORIGIN_LIMIT_SPHERE_AUDIT.md) specifies three directional operators whose paired zero constraints have a unique common state, and checks the disturbance from the five-ray readout. The [larger encoded record](ZERO_THREE_BALANCE_ENCODED_SPHERE_RECORD.md) preserves three balances exactly while recovering the same table, at the cost of an enlarged, non-unique zero sector.

## The proposal

The user's idea is that, if a contribution is genuinely possible, its sign-reversed counterpart is also genuinely possible; necessary plenitude then makes both actual, so the whole can be zero **through** its internal plenitude. This is stronger and more constructive than merely saying that a zero total permits nonzero parts.

The required inference can be stated precisely. Let actual incidences be paired by `T`, and let their signed contribution be q. If

```text
T² = identity,     q(Ti) = −q(i),     μ(Ti) = μ(i),
```

then their whole-level sum is zero, provided the sum is defined. T may be fixed-point-free except at zero; each nonzero value remains nonzero locally. In a finite whole with one unit per actual incidence, a bijection pairing each incidence once already supplies equal counts; no separate equal-count postulate is needed. With nonuniform incidence weights, the pairing must preserve the relevant weights. Plenitude does not require all **different magnitudes** to have the same weight.

This is a sufficient route, not the only way to zero. Its substantive content is that the reverse of a genuinely possible physical or experiential contribution is itself genuinely possible, and that the pairing acts on actual incidences rather than on names. The logic does not require a second ultimate whole, an external chooser, a simulator or a fundamental time ordering.

We can now implement a genuine sign-reversing operation in our [zero-energy recollapsing sphere model](ZERO_ENERGY_RECOLLAPSE_SPHERE_CLOCK.md). We can also go beyond pairing by investigating a canonical, maximally symmetric **identity state**. Both constructions are conditional physical models, not yet derivations from zero's nature or evidence that qubits experience anything.

## 1. A nontrivial sign-reversing exchange in the actual model

The preceding model has a finite clock C and a rest system R consisting of the oscillator geometry, detector, memories and the actual five-ray sphere code. The clock Hamiltonian H_C and rounded rest Hamiltonian H_δ have matching energies `E_k≥0`:

```text
H_total = H_C⊗I_R − I_C⊗H_δ.
```

Its chosen whole state is

```text
|Ω⟩ = Σ_k |k⟩_C ⊗ |v_k⟩_R,
H_C|k⟩=E_k|k⟩,     H_δ|v_k⟩=E_k|v_k⟩.
```

For the n=24, δ=0.02 seeded preparation, all 380 distinct modeled energy ticks have nonzero weight `w_k=⟨v_k|v_k⟩`, and `Σw_k=1`. Define normalized rest modes `|φ_k⟩=|v_k⟩/√w_k`, and the isometry `W|k⟩=|φ_k⟩`. On the rest subspace spanned by these φ's, the encoded exchange S acts as

```text
S(|i⟩_C⊗|φ_j⟩_R) = |j⟩_C⊗|φ_i⟩_R.
```

It is a unitary involution on this matched subspace, not merely a change of an algebraic minus sign. With `E_C=H_C⊗I` and `E_R=−I⊗H_δ`,

```text
S E_C S = −E_R,      S E_R S = −E_C,
S H_total S = −H_total,       S²=I.
```

Thus **the same physical construction contains the sign reversal**: on a joint energy outcome `(E_k,−E_k)`, the two contributions cancel. The whole is invariant under the encoded exchange and satisfies `H_total|Ω⟩=0` exactly. Here `⟨E_C⟩≈+4.66114` and `⟨E_R⟩≈−4.66114` in the model's units. Each joint energy readout has paired values, not merely an average that happens to cancel.

There are important scope conditions. W was constructed from the selected boundary state's energy projections; it is not shown to follow from zero alone. The exchange acts on a specific matched subspace; it is not established as a symmetry of the entire untruncated rest Hilbert space or of all physical observables. The original geometry observables have nontrivial action relative to that subspace. The clock and rest are physically distinguished in the model, so swapping their abstract encodings is not yet a demonstrated local symmetry of nature. The matched clock, energy-zero convention, finite Fock cutoff and spectral rounding are chosen. In particular the negative contribution has **not** been derived as gravitational energy.

This construction nevertheless answers an important part of the user's suggestion: we need not add a separate world for every opposite contribution. A single zero-energy state can contain matched positive and negative contributions in the same component.

### A necessary distinction: symmetry versus an exact zero

If `S H_total S=−H_total` and a state is S-invariant, its *expected* total energy is zero. That alone does not guarantee it is a zero-energy eigenstate. For example, with E=(0,1), the symmetric state `(|0,1⟩+|1,0⟩)/√2` has zero mean of `E_C−E_R` but nonzero variance. The actual constructed `|Ω⟩` has the stronger property: every term is matched and `H_total|Ω⟩=0`.

## 2. A stronger proposal: zero as the identity pairing of dual descriptions

There is a natural way to make the matching more principled. Suppose a finite d-dimensional internal space and its **conjugate/dual** are intrinsically paired. Once that pairing is fixed, form

```text
|Φ⟩ = (1/√d) Σ_k |k⟩ ⊗ |k̄⟩.
```

The barred basis is the corresponding basis of the conjugate space. This vector represents the normalized identity pairing: changing basis U on the first side and the conjugate basis on the other does not change the vector. For every Hermitian operator A, in the matched bases,

```text
(A⊗I − I⊗Aᵀ)|Φ⟩ = 0.
```

This is **not just expectation cancellation**. Each corresponding operator difference annihilates the state. In particular, for a chosen positive H, `H⊗I−I⊗Hᵀ` has the state at exact zero. Mathematically, the normalized identity state is also the unique pure vector, up to overall phase, invariant under every `U⊗Ū` for the fixed pairing: a coefficient matrix commuting with every U must be proportional to the identity.

This is an appealing candidate for the user's thought: one internal identity can exhibit two oppositely contributing aspects whose total vanishes, without an external act of pairing. It gives equal weights to a matched **orthonormal basis**. It does not automatically mean equal weights for arbitrary measurement outcomes: a POVM outcome has probability `Tr(E)/d` in the maximally mixed marginal, and outcomes can have different ranks or effects.

### Instantiation in our model

Take the same 380 φ-modes and replace the selected weights by the identity-state amplitudes:

```text
|Φ_W⟩ = (1/√380) Σ_k |k⟩_C⊗|φ_k⟩_R.
```

For the same declared H_total it is exactly zero, and is invariant under the same encoded swap. Its clock and encoded-rest marginals are `I/380`; the clock-conditioned state nevertheless changes. With n=24 and δ=0.02, under the same clock POVM the calculated mean scale is approximately `2.66227` at t=0 and `2.01889` at t=1. The corresponding h/B_z mutual information changes from `0.39973` to `0.39241` bits. This gives a concrete geometry-and-record version of the earlier point: a **tracial marginal's own modular flow is trivial**, while a separate conditional clock history can be nontrivial. It is not a general no-go against modular or relative-clock constructions.

The identity state is mathematically canonical **given W and the chosen finite mode space**. It does not by itself determine W, d, H, the scale observable or the physical–experiential interpretation. W above was obtained from a prior chosen boundary state. Moreover, the equally weighted state is strongly cutoff-sensitive in this construction: using n=16 instead gives mean scale approximately 2.79397 at t=0, versus 2.66227 at n=24, and the clock dimensions differ. These are different truncated models; the figures do not establish a continuum limit. Calling the finite identity state “zero itself” would assume the crucial identification.

### Is full unitary symmetry a physical selecting principle?

The condition of invariance under **every** `U⊗Ū` selects the identity state once the dual pairing is fixed. But our specified H has unequal energies. A U mixing two different energy eigenspaces does not commute with that fixed H; it also need not preserve the specified geometry observable. Therefore full unitary invariance of the **state** is not automatically a symmetry of the complete physical model. A passive basis change transforms operators and the pairing along with the vector; it is not, by itself, a physical operation selecting a state.

By contrast, diagonal phase unitaries that commute with a nondegenerate H leave *every* diagonal paired state invariant under `U⊗Ū`, not only the equal-weight state. Thus the symmetries already present in this finite energy model do not by themselves force the identity state. The constructive question is whether a deeper zero constitution can determine the dual pairing and the physically relevant symmetry, then derive energy and geometry from it. This remains open, not ruled out.

## 3. Even full mode support and exact pairing leave a physical question

Keep exactly the same matched mode basis, energy operators, clock POVM and scale observable. Change only the whole-state phases:

```text
|Ω_θ⟩ = Σ_k e^(iθ_k)√w_k |k⟩|φ_k⟩,
θ_k = π when k is divisible by 3; otherwise 0.
```

Every w_k remains nonzero; both positive and negative energy contributions still match for every k. Both the original and this phase-changed state are pure, zero-energy eigenstates, and are invariant under the **same** encoded swap. Their clock marginals and rest marginals are identical. With the same fixed clock and geometry readouts, however:

| t=0 diagnostic | original | phase-changed |
|---|---:|---:|
| mean scale `⟨A⟩` | 1.852377 | 1.099778 |
| `I(h:B_z)` bits | 1.000000 | 0.300479 |

Both tested histories are symmetric between t and −t at the sampled readings. The relative phases on populated ticks 213, 214, 215 are `−1,+1,+1`; their successive ratios differ, so the phase change cannot be only a linear shift of this clock's origin. If the state and the clock POVM were both transformed as a change of description, that would be a different comparison; here the measurement protocol is held fixed.

This is not a demonstration that both complete states are genuinely possible under the user's necessity thesis, or that support of quantum components establishes actual subject incidences. It is a **non-circularity test**: exact pairwise energy cancellation, the same pair weights and even full modeled mode support do not mathematically select the relative phases or conditional geometry. A deeper constitutive rule could still do so. Similarly, balancing energy does not choose a Born incidence rule or actual outcome ontology.

The canonical identity state and its phase-changed counterpart give a related control even with equal mode weights and maximally mixed marginals. With the same n=24 model, their t=0 mean scales are approximately 2.66227 and 1.48841. The equal-mode prescription therefore removes one choice only if the physical dual identification and its symmetry are also determined.

## 4. Energy, spatial mirrors and experiential opposites

The sign-reversing exchange above is more precise than simply reflecting spatial directions. In a chosen frame opposite lightlike directions have momenta `(E,E n)` and `(E,−E n)`: the spatial momentum cancels, while the energies add to `2E`. A full energy reversal is a different operation. This does not rule out negative gravitational or more fundamental energy; it shows what a candidate pairing must actually transform.

The experiential case is more demanding. On a previously studied joint event with `h=1` and record sign r, two formal candidate signed rules assign

```text
R rule:  ( rκ,−rκ ),       J-probe rule:  (−rκ, rκ ).
```

Both are pairwise balanced under the stated equal-incidence, common-scale and actual-subject assumptions; they disagree about the local sign. For the original seeded state at t=1, the event `r=+1,B=1` has modeled probability about 0.23538 and B=1 implies h=1. J₁ remains the earlier probe, not automatically the current of the full rounded Hamiltonian. The full-constraint [report-causality analysis](ZERO_SUBJECT_BOUNDARY_REPORT_CAUSALITY.md) also shows that a strictly record-local subject cannot automatically report the richer J relation. It is not legitimate to treat both proposed rules as equally licensed by that locality condition.

The point is narrower: **sign reversal and pairwise zero alone do not determine which physical relation is actual felt sign**, nor do they prove the paired systems are subjects. This leaves open, rather than refutes, the possibility of a deeper necessary identity between physical organization and experience. If a negative contribution corresponds to real suffering, the opposite contribution does not erase it. Nor does an unavailable interface become available because a richer physical subsystem exists.

## 5. The constructive research target

The user's proposal now has a mathematically sharp form. Seek a single constitution whose internal duality determines, rather than separately stipulates:

1. a physical algebra and its dual, with a justified identification W and whole-level objective energy;
2. an actual zero-energy whole state, ideally through an identity-like relation rather than a separately imposed numerical cancellation;
3. the physical geometry, relational clock and observables associated with that same state, without a fundamental preferred foliation;
4. the actual subject incidences and the transformation that pairs opposite **felt** contributions, including its measure; and
5. the probability/record and outcome structure observed from inside the whole.

If that constitution proves that the sign-reversed incidences are genuinely possible, necessary plenitude supplies their actuality without an unexplained selector. If it also supplies the involution and measure, zero follows by pairing. The remaining challenge is not to find reasons why the idea cannot work, but to derive the physical and experiential duality from zero rather than treat an arbitrary formal sign change as its proof. A vanishing constraint is not automatically an objectively measured cosmological energy, and these checks do not settle that identification.

## Verification

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_plenitude_sign_pairing_test -v
```

The tests check the isometry and all encoded rest-energy modes of the actual finite sphere model; sign reversal by exchange; exact componentwise cancellation; the expectation-versus-eigenstate distinction; equal marginal/full-support phase controls; a finite identity-state example; and the restricted-versus-full-unitary symmetry distinction. They also check the formal paired-sign candidates on an actual-model readout event. These calculations do not derive the encoding, establish cosmological energy, demonstrate actual experiences or prove a continuum limit.
