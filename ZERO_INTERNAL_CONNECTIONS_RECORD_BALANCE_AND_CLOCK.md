# Internal connections: record algebra, signed balance, and the relational clock

This report strengthens the links **within the existing sphere construction** rather than adding a new spectator system. It connects the [flag-incidence rule and reversible readout](ZERO_FLAG_RECORD_INCIDENCE_AND_PHYSICAL_READOUT.md), the [sphere echo](ZERO_SPHERE_LOCAL_CONSTITUTION_AND_RESERVOIR_ECHO.md), and the [one-reality constitution](ZERO_ONE_REALITY_NECESSARY_PLENITUDE_SYNTHESIS.md). Exact tests are in [the verifier](verification/zero_internal_connection_flag_access_balance_test.py).

## 1. What is now connected

**Primary-source continuation:** [Page–Wootters (1983), stationary observables, and the sphere echo](ZERO_PAGE_WOOTTERS_1983_RELATIONAL_SPHERE.md) uses the original paper to construct stationary pre/post-echo joint observables and checks their actual distribution. [The photon-clock and de Sitter analysis](ZERO_QUANTA_TIME_PHOTON_CLOCK_AND_DE_SITTER.md) connects those distinctions to the linked optical experiment and the operational meaning of cosmological horizons. [ER = EPR and the sphere access calculation](ZERO_ER_EPR_FIREWALL_AND_SPHERE_ACCESS.md) tests a separately stipulated teleportation intervention using the actual B-conditioned echo pair.

The following four facts fit into one mathematical structure:

1. The candidate incidence flag is a **conserved reference observable** in the actual 20-operation sphere echo.
2. Its compatible record algebra has a canonical coarse-graining; on that algebra, the coherent state and its flag-dephased representative give exactly the same record probabilities, including specified sequences of flag-preserving instruments.
3. The very same flag can be inferred from the existing joint echo records at one clock reading, while its inferred weight and the proposed signed quality change appropriately when records are conditioned upon.
4. A counterpart symmetry pairs positive and negative proposed signs in the whole ensemble, but an individual selected record can have a nonzero sign. Thus zero balance does not require local experiential absence or erase either local contribution.

The connection is not automatic subject selection. The actual apparatus contains **three** equally balanced conserved reference flags. The restricted midpoint interface singles out the first one operationally, but a richer interface can also read the second; this is an objective difference between interfaces, not yet a reason that a particular interface is a subject. Two flag-to-quality hypotheses can satisfy the same global balance and still make **different conditional report predictions**.

## 2. The compatible algebra is a dynamical structure, not an extra collapse

Let `P_0,P_1` be the projectors of the first physical reference flag and write

`Δ_F(A) = P_0 A P_0 + P_1 A P_1`.

The compatible algebra is `A_F = {A : [A,P_a]=0}`. The map `Δ_F` is the canonical projection of operators onto this algebra: it fixes every compatible operator, kills flag-off-diagonal blocks, is positive and trace preserving, and is the Hilbert–Schmidt orthogonal projection onto `A_F`. Equivalently, it averages `A` with `Z_F A Z_F`. These properties identify the coarse-graining **once the flag is specified**; they do not select that flag from all possible references.

For any density operator and any `E∈A_F`,

`Tr(ρ E) = Tr(Δ_F(ρ) E)`.

The two density operators differ on coherent effects, so this is equality of **restricted statistics**, not equality of physical states. In particular, the transported witness `D_t` lies outside `A_F`; the pure state gives it expectation `1`, whereas the pinched state gives `0`. No dephasing event is required to make the restricted descriptions agree.

There is also a sequential version. Suppose a sequence of record instruments has Kraus operators `K_{r_k}` satisfying `[K_{r_k},P_a]=0` and we retain their outcome labels. Its joint outcome probability has effect

`E_(r1…rn) = K†_r1 … K†_rn K_rn … K_r1 ∈ A_F`.

Consequently its probability is the same for `ρ` and `Δ_F(ρ)`, even if record effects at different stages do not commute with each other. This is not a claim about arbitrary interventions: a Kraus operation that mixes the flag sectors can reveal coherence and need not obey the equality. A specified instrument is an additional physical operation, and an interface must actually be available to the putative observer.

The existing incidence theorem now attaches directly to this operational structure. If the type is stipulated to be the flag and the positive, additive type weights have the ordinary physical marginal and sharp flag support, then every compatible record has the unique weights

`μ_a(E)=Tr(ρ P_a E)=Tr(Δ_F(ρ) P_a E)`.

Thus the same restriction that makes the incidence rule positive also makes it insensitive to the off-diagonal flag coherence. The rule is not a claim that coherence is unreal, and a formal restricted algebra is not by itself a proof that it is a subject's self-location algebra.

## 3. The same structure is transported by the relational clock

Every gate `G_t` of the actual sphere/reservoir/echo program commutes with the reference flag. Hence

`Δ_F(G_t ρ G_t†)=G_t Δ_F(ρ) G_t†`.

The restricted description and the physical evolution therefore fit together at **every clock reading**, not just at one privileged moment. With `U_0=I`, `U_t=G_(t-1)…G_0`, the one-cycle identity `U_20=I`, and the controlled cyclic shift `W`, define

`|H⟩ = (1/√20) Σ_t |t⟩ U_t|Ψ⟩`,

`D_rel = Σ_t |t⟩⟨t| ⊗ U_t D_0 U_t†`, where `D_0=X_S X_F`.

The inverse cycle gives `W|H⟩=|H⟩` and `[W,D_rel]=0`, including across the final-to-initial clock edge. Also `[W,I_clock⊗P_a]=0`. A clock-conditioned record, the conserved flag, and the global coherence witness therefore belong to **one stationary history**: the witness is a relational observable, not evidence for an external time. The flag-compatible record algebra excludes `D_rel`, but the larger global algebra contains it.

This is an algebraic consequence of the actual program and its inverse. The verifier densely constructs an analogous smaller nontrivial cyclic clock and checks the equations; it does not claim to have densely constructed the entire sphere–reservoir history. A relational clock label is not automatically an experienced duration, and clock-gate ordering is not a preferred spacetime foliation.

## 4. Whole balance and nonzero local signs are compatible in the same model

Let `V_a` be the candidate signed observable for flag `a`, and let `C` be a genuine active counterpart involution that preserves the relevant state and flag but reverses `V_a`. For an effect `E` commuting with `P_a`, `V_a`, and `C`, the symmetry assumptions

`CρC†=ρ`, `CP_aC†=P_a`, `CE C†=E`, `CV_aC†=−V_a`

imply

`Tr(ρ P_a E V_a)=0`.

The proof is to conjugate the trace by `C`: all factors are unchanged except `V_a`. The corresponding conditional mean is zero whenever the record has nonzero probability. But if the record itself selects one side of the counterpart—so `CE C†≠E`—the inference does not apply. Positive and negative conditional contributions can be separately nonzero and cancel only on recombination. This result also requires that the counterpart be an **active pairing of distinct incidences**, not a gauge identification that would force an odd scalar to vanish on the same incidence.

In the actual sphere's commuting Born ensemble, the relevant operational statement can be checked without asserting an unproved symmetry of every full coherent density matrix: for each allowed record of `(R_0,r,x_0)` at each tick, the `s=+` and `s=−` contributions are equal and the candidate sign `h=s(b if x_0=0 else z_current)` reverses between them. The signed numerator is exactly zero in each such cell. This follows from the actual tabulated sphere amplitudes, not from assigning opposite signs to an absent experience.

Now also condition on the physical sign record `s`. At tick 10, each `(R_0,r,s)` outcome has probability `1/8`. With the proposed sign in units of `κ`, the exact conditional mean is:

| `R_0` | `r` | `E[h | R_0,r,s]` |
|---:|---:|---:|
| 0 | 0 | `s` |
| 1 | 0 | `s` |
| 0 | 1 | `0` |
| 1 | 1 | `−s` |

For example, fixing `(R_0,r)=(0,0)` gives `+1` for `s=+` and `−1` for `s=−`; both occur with equal weight. In the `(0,1)` cell the assigned flag is j and current j itself remains balanced, so even selecting s leaves its mean zero. These are actual **physical parity** predictions under a stipulated flag-to-quality rule. If they are interpreted as felt values, an additional constitutive premise must justify that interpretation. Cancellation of their weighted sum does not mean pleasure removes lived suffering. Nor is this signed sum identical to the separately maintained finite charge ledgers or to an objective whole-energy theorem.

## 5. Three existing flags: accessibility narrows but does not solve selection

The source/reference preparation already contains independent balanced bits `x_0,x_1,x_2`; all three reference qubits are left untouched by the program. Any one could be assigned as a sharp two-sector flag. At tick 10, the exact optimal flag-guess probabilities are:

| Flag | `R_0,r` only | `R_0,R_1,R_2,C,r`, clean C | Same, C thermal `q=1/4` |
|---|---:|---:|---:|
| `x_0` | 1 | 1 | 1 |
| `x_1` | 1/2 | 1 | 3/4 |
| `x_2` | 1/2 | 3/4 | 3/4 |

Here `C` is the existing one-bit auxiliary register, not a new abstract side channel. The source/reference and finite-battery assumptions are those of the earlier program, and the thermal original reservoir has `q=1/4`. With clean `C`, the actual midpoint identities are

`x_0=R_0 XOR r`,

`x_1=R_1 XOR C XOR r`.

The first identity needs only the smaller interface; the second uses the extra physically prepared auxiliary bit. The remaining thermal error leaves `x_2` at `3/4` for this specified interface. The verifier computes the optimal classical guess for the displayed record ensembles, not a universal optimum over all quantum operations or possible apparatus.

This builds a genuine bridge from physical organization to candidate incidence: **relative to the smaller accessible record interface**, `x_0` is recoverable while `x_1` and `x_2` are not. But the bridge is conditional on that interface, not on calling a reference “first.” Giving an observer the larger interface changes the answer; confinement does not automatically provide either interface. Conserved equal flag weight, source-pair relations, and zero signed balance alone cannot select the intended subject-type flag.

This matters physically–experientially. Compare two hypotheses using the *same* state and dynamics: `A` assigns type B for `x_0=0`, j for `x_0=1`; `B` uses `x_1` instead. They assign different types with probability `1/2`. At tick 10, `h_B` and `h_j` disagree with weight `1/4`, independently of the reference bits; hence the proposed signs differ with weight **`1/8`**. Both hypotheses have equal type priors and zero signed mean. Equal balance is therefore not enough to make their intrinsic-content proposals equivalent.

## 6. A discriminating prediction if an actual report interface exists

Consider the tick-10 cases where the simultaneous physical candidate signs `h_B=sb` and `h_j=s z_current` disagree. Their Born weight is `1/4`. Suppose, additionally:

* there is one persistent eligible subject whose actual felt binary sign is the candidate selected by the relevant flag;
* it can independently report that sign with the same calibrated bit-flip error `ε<1/2` in both hypotheses; and
* a real joint interface can establish `R_0`, `r`, `s`, current `j`, and the report without invalidating the stated measurement protocol.

Use the `x_0` rule and `x_0=R_0 XOR r` to predict which of the two physical signs the subject reports. Then

`P(report matches x_0 prediction | mismatch, A) = 1−ε`,

`P(report matches x_0 prediction | mismatch, B) = 1/2`.

Under hypothesis B, `x_1` remains independent and balanced even after the specified mismatch and record conditioning, so either sign is equally likely. This contrast survives the same symmetric report error in both cases. It is a conditional discriminator between **complete bridge hypotheses**, not evidence that either physical flag is a subject or that the required interface and report exist. A report interaction may alter subsequent echo evolution; it must be specified and implemented at the claimed reading. The confined inhabitant is not assumed to access the room, a reservoir, or the player's activity merely because the joint measurement is mathematically definable.

## 7. Relation to the zero/no-residue program

The point–sphere proposal treats internal differentiation as a feature of one whole rather than a second substance in an outside space. The present construction shows a concrete **compatibility pattern** for that ambition: one coherent whole admits a conserved internal record algebra, weighted alternatives, relational succession, and signed counterpart balance without requiring its local contributions to vanish. It also distinguishes a physically accessible interface from a merely global mathematical observable.

It does **not** derive the sphere, the first reference, the initial state, the exact dynamics, an actual experience, or objective zero total energy from bare numerical zero. Calling their joint occurrence one structure does not explain why that structure rather than another is necessary. The stronger constitutive target is to establish together why a particular organized interface is an actual subject, why its admissible self-location effects are those of that interface, and why its internal quality corresponds to a signed physical relation. The two-flag discriminator above turns that issue into a precise difference between candidate joint constitutions, rather than treating a matching global zero as a substitute for the link.
