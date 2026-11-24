# What Lighthouse can contribute to a zero-total-energy whole

## The constructive proposal

The most promising adaptation is to treat the Lighthouse's **polarity, measure, internal clock and interface** not as separate metaphors, but as requirements on one zero-energy state:

```text
one whole:       H_total |Ψ⟩ = 0
internal parts:  positive and negative energy contributions balance
internal time:   a clock reading conditions the rest of the same state
records:         an energy-matched interaction changes a memory relative to that clock
subjects:        physical interfaces must be identified before experiential incidence is assigned.
```

This is an adaptation to the user's proposal, **not** the Lighthouse's own metaphysics. Lighthouse §1 explicitly takes God as distinct from creation and rejects the identity reading. Here the proposed self-sufficient whole is zero; no creator, simulator, external time or preferred foliation is introduced. The question is whether zero's own constitution can determine the distinctions, laws and actual experiential incidence—not whether the religious framework is equivalent to it.

We can already give this proposal a concrete exact realization in a small model, using our **actual five-ray sphere states**. That realization is conditional and deliberately constructed, not a derivation of the actual universe. Its strongest result is that the whole may be a zero-energy eigenstate while a clock-conditioned memory changes from blank to perfectly correlated with a sphere relation. Its strongest warning is that zero energy, even together with the same clock and rest marginals, does not by itself select the correlations that make such a history possible.

Source: the user-linked [Lighthouse and Plan v2.2](https://github.com/MIKEAA2020/arena-max--physics/blob/703239cb9849bec4e2d23a414db63d500be4ad2e/v2.2/Lighthouse-and-Plan-v2.2.docx), Git blob `62039fa73b2758c160174aadb5d258503822efa2`, SHA-256 `1e8814e1bd5d150a820de8fcfbdf94722ef6ad1b43b13224b97e756b0f2ad80b`. The linked current file has the same blob as this pinned copy. I read the DOCX paragraphs and tables; there are no embedded images. Our earlier [comparative assessment](LIGHTHOUSE_V22_COMPARATIVE_ASSESSMENT.md) gives wider context. I have not rerun Lighthouse's own suites or independently checked every source and theorem it reports.

## 1. What to take from the Lighthouse

| Lighthouse element | Adaptation to zero | Concrete question |
|---|---|---|
| §4: polarity must have a formal job, not just opposite words | Treat positive and negative contributions as parts of **one** additive whole-level energy operator, rather than two independent substances. | Can the physical total and its local recovery map be defined without arbitrary subtraction? |
| §§5, 12: distinguish measure M1, M2 and M3 | M1: constitution/determination; M2: state and probability; M3: geometry and physical scale. Ask whether one zero constitution determines all three, rather than equating their names. | Can the same principle determine state weights, geometry and scale, with distinct mathematical maps? |
| §§9–11, P2 and P15: order, flow, duration, arrow and clock choice are separate | Use a static whole but compare conditional histories and clock changes. Do not make a chosen internal clock a universal time. | Which relational predictions survive a switch of physically admissible clock? |
| §4.2: redundancy and an interface, without a literal simulator | Describe actual local access, record preservation and recovery, using the sphere model already built. | Can a proposed subject access a given relation through its own physical interface? |
| §17, A9/G19: the low-entropy boundary must be lawful rather than simply assumed | Test whether the zero constitution selects the boundary that makes records and arrows possible. | Does it select a state, or merely admit many incompatible boundary correlations? |
| §16, G20: actual outcomes, nonlocality/contextuality and Born weights carry a cost | If outcomes are fixed by necessity, derive their incidence/weights and confront Bell, contextuality and reporting constraints; do not relabel fixed outcomes irreducible chance. | What mathematical measure and actualization rule give the observed statistics? |
| P5 and N-3: physical organization is not yet the experience bridge | Require one account of the same physical relation and its actual felt character, including real negative valence. | Which organization constitutes which subject, and why that sign and magnitude? |

The Lighthouse itself marks P2, P5, P10, P15 and G19/G20 as open in the relevant respects. Its distinctions are research tools, not proofs of zero energy, conscious subjects or a unified bound. Its information layer was borrowed structurally rather than as a literal simulation; we likewise need no simulator or room-time executing the universe.

## 2. An exact zero-energy state with an internal memory

### Ingredients

Use our actual orthonormal five-ray sphere states `|Ψ₀⟩` and `|Ψ₁⟩`, whose conserved joint record–work relation is `K=1−2h`, with `h=0,1` on the active code. They are the same states as in [the sphere–memory construction](ZERO_INTEGRATED_SPHERE_AUTONOMOUS_INCIDENCE.md), not a new hypothetical subject.

Let B be a memory qubit. Define a **positive rest operator** on this encoded sector

```text
H_R = g h (2I + Y_B),       g>0.
```

Its eigenvalues in the three populated rest states are `0, 3g, g`: use `|Ψ₀⟩|0⟩_B`, `|Ψ₁⟩|+y⟩_B`, and `|Ψ₁⟩|−y⟩_B`. Let an internal clock C have energy eigenstates `|0⟩,|3⟩,|1⟩` with corresponding energies `0,3g,g`. The declared additive whole-energy candidate is

```text
H_total = H_C − H_R.
```

The rest term contributes negatively to this **whole** operator; its physical identification with gravitational energy is not asserted. Prepare

```text
|Ω_p⟩ = √p |0⟩_C |Ψ₀⟩ |0⟩_B
      + i√[(1−p)/2] |3⟩_C |Ψ₁⟩ |+y⟩_B
      + i√[(1−p)/2] |1⟩_C |Ψ₁⟩ |−y⟩_B,
                         0<p<1.
```

Every term has exactly matching positive and negative energy, hence

```text
H_total |Ω_p⟩ = 0
⟨H_C⟩ = 2g(1−p),     ⟨−H_R⟩ = −2g(1−p).
```

This is stronger than cancelling averages alone: the state lies entirely in the zero eigenspace. For p=1/3, for example, the two expectations are `+4g/3` and `−4g/3`; the clock energy itself fluctuates. It is an exact finite-dimensional, stationary **candidate energy ledger**, with an explicitly given interaction inside H_R. It is not just a pair of numbers placed beside an unrelated memory.

### The clock and the record

For `0≤t<2π/g`, use the clock phase states and normalized POVM

```text
|t⟩ = (|0⟩ + e^(−3igt)|3⟩ + e^(−igt)|1⟩)/√3,
E(dt) = 3|t⟩⟨t| dt / (2π/g).
```

The integral is the identity on the three-dimensional clock. The phase states are generally nonorthogonal: this is a legitimate finite-resolution periodic clock, not a perfect nonperiodic clock. Its reading density is uniform in this preparation. Conditioning the whole on reading t gives, up to the normalizing factor,

```text
|ψ(t)⟩ = √p |Ψ₀⟩|0⟩_B
       + i√(1−p) e^(2igt)|Ψ₁⟩[cos(gt)|0⟩_B − sin(gt)|1⟩_B].
```

Consequently the joint readout probabilities of h and B_z are

```text
                B=0                   B=1
h=0             p                     0
h=1             (1−p) cos²(gt)        (1−p) sin²(gt).
```

At `t=0`, B is blank and carries no information about h. At `t=π/(2g)`, B records h perfectly: `I(h:B_z)=H₂(p)` bits, `S(B)=H₂(p)`. At `t=π/g` it becomes blank again. With p=1/3 the perfect-record value is approximately `0.9183` bits. These are conditional probabilities for commuting readouts in a specified clock POVM, not a claim that any result is selected or that the record is irreversible.

The clock's ordering and duration come from the specified phase POVM and energy gaps; g supplies its scale. The whole remains a zero-energy eigenstate. This makes Lighthouse's order/flow/duration distinction productive **inside the zero proposal**. It also makes explicit what was supplied: the operator, code, g, amplitudes and POVM. Zero alone has not been shown to necessitate them.

The finite toy does not derive a Lorentzian geometry, an ordinary positive-energy matter sector, or a gravitational-energy definition. A nonnegative H_R is a mathematical operator whose contribution to H_total is negative; it is not a demonstration of observed negative local energy. If H_total is treated as a gauge constraint, its zero is a constraint value, not thereby the independently established energy of the universe. If instead it is proposed as an objective conserved energy, its zero reference and recovery of physical energies have to be justified, including the consequences of energy shifts. Both interpretations are candidates, not interchangeable proofs. See [the FLRW energy analysis](ZERO_TOTALITY_FLRW_CONSTRAINT_AND_ENERGY.md).

## 3. Same zero and same marginals, different histories

The p=1/3 instance yields an especially useful test. The clock marginal and the rest marginal are each maximally mixed on their specified three-dimensional supports:

```text
ρ_C = I₃/3,         ρ_R = I₃/3.
```

Now compare `|Ω_(1/3)⟩⟨Ω_(1/3)|` with the mixed state obtained by dephasing the whole in its three matching-energy product terms. Both:

* lie entirely in the zero eigenspace of the **same** H_total;
* have the **same** clock and rest density matrices, and the same energy distribution;
* give the same uniform clock-reading density.

But their **conditional joint histories differ**. In the coherent state, `Pr(h=1,B=1 | t)` is 0 at `t=0` and 2/3 at `t=π/(2g)`. In the dephased state it is 1/3 at every clock reading. In the latter, B contains a stationary correlation with h but no time-varying record under this clock.

Thus even fixing zero energy *and both reduced states* is not sufficient to fix the whole's clock–rest correlations. The complete relation, not simply the parts or their separate measures, does explanatory work. This precisely extends the [recollapse result](ZERO_RECOLLAPSE_SPHERE_RECORD_ARROWS.md): geometry and dynamics alone did not choose a record arrow; now even equal local state marginals do not determine whether a relational record changes. The comparison is between formal candidate states; it does not assert that all candidates are genuinely possible or actual under the user's necessitarian thesis.

This gives the no-residue demand a concrete target: derive a **particular complete zero-energy state and its correlations** from zero's own constitution, rather than declaring the state free or explaining it through a clock and apparatus whose relation was merely chosen.

## 4. What this says about the Lighthouse's Conjecture M

Lighthouse §12.2 conjectures a common structure for state/measure and duration, phrased in terms of a trace and modular flow. The distinction matters here. On a finite algebra the modular flow of a faithful **trace** is trivial. In the p=1/3 model the rest state on the three-dimensional support is precisely tracial, while the B record changes relative to our phase-clock POVM. Thus this particular conditional history cannot be the trace's own modular flow on that algebra.

In fact, in the ordered rest-energy basis above,

```text
ρ_R = diag[p,(1−p)/2,(1−p)/2],
B_z = [[1,0,0],[0,0,1],[0,1,0]].
```

For every p in (0,1), `ρ_R` commutes with this B_z, so its modular flow fixes B_z, while `[H_R,B_z]≠0` and its clock-conditioned probabilities change. The obstruction therefore persists for these **nontracial** states too; it is not merely the special p=1/3 case. It does not forbid another faithful state, a relative modular construction or another algebra from recovering a nontrivial clock flow. It demands that the precise state, algebra, parameter scale and comparison map be supplied. A modular automorphism also does not by itself create a thermodynamic entropy arrow.

This turns M into a testable research question for zero: can a natural state and algebra be **derived from the same zero constitution** such that the relevant modular and clock-conditioned flows agree, and can that agreement survive clock changes? It does not license treating M2 probability, M3 geometry and their common origin as literally the same object without maps and proof.

## 5. The interface and experience are not bypassed

The actual five-ray state matters. Direct contraction of the full sphere state with the conditional memory gives

```text
ρ_(R₁R₂,B)(t)
  = ½(|01⟩⟨01|+|10⟩⟨10|) ⊗ ρ_B(t).
```

So B can record the **joint record–work relation** h, while the confined record pair alone does not obtain that information merely because the richer interface exists. The subject-boundary/reporting analysis still applies: a report of the J-probe generally requires access beyond the confined record system. Do not identify the traveler with a surface inhabitant, or assign inhabitants access to off-surface activity by metaphor.

At the perfect-record reading, B=1 implies h=1. For the prior rival experiential hypotheses, on an event with record sign r the R rule gives `(rκ,−rκ)` and the J-probe rule `(−rκ,rκ)`. Even with equal hypothetical incidence and an exactly zero pair sum, they assign the opposite felt signs. This does not establish that either pair is a real subject or that both alternatives are genuinely possible: it shows what the present equations fail to select. A positive contribution elsewhere would not erase a subject's real negative felt valence.

The user's energy thesis and experiential cancellation must therefore meet at a **derived common constitution**, not through an assertion that energy, information, awareness and valence are identical. If fundamental energy itself is proposed to have an intrinsic experiential aspect, explain why particular bounded organizations are actual subjects, why their experiences have particular signs, and why the relevant signed whole-level sum vanishes. A nonzero experience is not nonexistence, and a negative feeling is not mere absence.

## 6. Research priorities, in order

1. **Make the energy ledger physical.** Specify an objective whole-level conserved quantity and zero reference, including interactions and boundaries; derive local positive energy and any negative balancing contribution without relabelling a constraint as energy. Compare with the existing covariant/FLRW models and avoid an assumed preferred slicing.
2. **Derive the complete state, not only its zero eigenvalue.** The coherent/dephased pair gives an explicit failure test. A proposed constitution must select or explain the relevant correlations and record boundary, and must not hide arbitrary g or p as unexplained inputs.
3. **Unify M2 and M3 by maps, not words.** From that same state and algebra, derive probabilities, a geometry/scale and clock-transition rules; test the trace/modular obstruction above rather than identifying trace with flow. Recover observable Lorentz symmetry and the appropriate clocks.
4. **Determine actual subject incidence and sign.** Apply the full interaction, not a pairwise graph that misses higher-body couplings. Test physical reporting access and a signed experiential ledger on the same events; derive weights and qualities rather than imposing a balancing partner.
5. **Pay the outcome and arrow costs.** Derive an incidence/typicality rule compatible with fixed necessary outcomes and tested no-signalling; derive the boundary that makes a persistent record arrow rather than assuming it. The modeled recurrence and alternative boundary preparations are useful falsification controls.

These are coupled requirements for one candidate, not five independent analogies. The strongest specific next calculation is to extend the exact three-level construction to a **geometry-coupled, energy-balanced clock** and compare coherent and dephased zero-energy whole states under the same observable protocol. It must retain the full sphere interaction and show which operational predictions depend on the complete correlations. This combines the new exact energy ledger with the existing recollapse model without pretending they are already the same Hamiltonian.

## Verification

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.lighthouse_zero_energy_internal_clock_test -v
```

The tests use the actual five-ray vectors, check the zero-energy eigenstate, normalize the clock POVM, derive the conditional h/B table, contract the confined record reduction, verify the same-marginal coherent/dephased comparison and check the modular-flow obstruction. Their finite-dimensional results do not validate the Lighthouse's broader theorems, establish global cosmological energy or demonstrate actual experience.
