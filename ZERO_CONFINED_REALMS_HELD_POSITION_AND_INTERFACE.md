# Confined realms: held position, richer activity and an optional interface

## What this builds

The user's correction is the starting rule, not something to be argued away: **in the surface-restricted description, the traveler remains at A during the room journey and changes to B upon return.** In the room description, the traveler follows the intermediate points of the chord. These are descriptions in different domains, not a claim that the traveler is physically at A in the room throughout the journey.

Likewise, while a chess player thinks, the game remains at its current position and half-move count; the thinking occurs in the player's domain, not as additional game moves. The traveler is analogous to the player, **not** to a piece or a surface inhabitant.

This report constructs and tests that retention rule, then adds two different interface rules to the existing [five-ray sphere–record–current system](ZERO_SPHERE_CONSERVATION_RECORD_CURRENT_SINGLE_SYSTEM.md). The same physically defined confined-side register remains at A while an extra sector changes. In one circuit the extra sector is inaccessible to it even after the update; in the other, a specified interaction allows a later record to depend on the extra sector. **Confinement alone does not choose between those circuits.**

A useful new result is that holding A cannot generally be defined as a function of the traveler's instantaneous room position alone: two oppositely directed journeys meet at the same room point while retaining different surface positions. The confined position is a **history-dependent state**, not an automatic geometric projection. This is compatible with the user's rule; it makes its structure explicit.

These are deliberately bounded models, not a derivation of spacetime, extra physical dimensions, a quantum tunneling mechanism, actual experiencing subjects or the zero whole. They give the idea a concrete place to succeed or fail without pretending the analogy itself proves those conclusions.

## 1. The geometry, stated with the held-position rule

Take a unit sphere in an auxiliary room and choose antipodal surface points

```text
A=(1,0,0),        B=(−1,0,0).
x(u)=(1−2u,0,0),  0≤u≤1.
```

The room route is the chord: `x(0)=A`, `x(1)=B`, and `|x(u)|<1` for `0<u<1`. Its length is 2, while a shortest surface great-circle arc between these antipodes has length π. Antipodes have many shortest surface arcs; a chord and a surface arc are shortest under **different admissible-path rules**. Neither is a shortcut available to an inhabitant confined to surface paths unless an additional route or interaction is supplied.

Define the surface-restricted position for this excursion by the user's rule:

```text
R_surface(u) = A     for 0≤u<1,
R_surface(1) = B.
```

It remains A during the room journey. A and B are consecutive in its **change sequence**; repeated occurrences of A do not introduce additional surface moves. This definition does not assert that a surface inhabitant actually measures a traveler, or can access the parameter `u`. The rule specifies the surface-domain state; the room-domain point `x(u)` is a different object. The auxiliary parameter only orders this toy route; it is not a fundamental clock for the whole.

The same confined sequence results for a different real room route, for example

```text
x_alt(u)=(1−2u, 2u(1−u), 0).
```

It has the same surface intersections and lies strictly inside the sphere for `0<u<1`, but differs from the chord at every intermediate point. The surface-level change sequence `A→B` by itself does not determine the intermediate route. Nor does it determine how much room-time the route takes.

### Why the retained A is not ordinary projection

Consider one excursion from A to B and another from B to A. Both pass through the same room center. At that shared room point, the first retains surface position A, whereas the second retains B. Therefore **no single-valued function of instantaneous room position alone** produces the user's rule in both cases. It needs the previous boundary state, or equivalent relational history, as part of the description.

For a declared route with isolated successive boundary encounters, a general version is: hold the most recently encountered surface point until the next encounter, then update. This is a well-defined retention convention with a specified history. It is not radial projection: radial projection can change continuously away from the surface and is undefined at the center. Nor is retention an automatic mathematical consequence of the sphere alone. We adopt it here because it is the user's intended rule; to apply it physically, the corresponding persistent state and update relation must be identified. For arbitrary paths with boundary accumulation or no first crossing, additional rules would be needed.

Under a rigid rotation, transport the room path, surface and retained points together. The relation is unchanged. This is a representation-covariance check, not a claim that a general quantum/spacetime frame change has been solved.

## 2. Chess time is a different parameter, not an invisible string of moves

Let game states be `G₀,G₁,…,Gₙ` and half-move count `m=0,1,…,n`. If a player's sequence is described using an auxiliary increasing parameter `τ`, write the times of the half-moves as `τ₁<⋯<τₙ`. Then

```text
m(τ) = number of half-moves completed by τ.
```

Between two completed moves, `m(τ)` is constant and the game position is unchanged, even if the player has extensive activity in that interval. For the same ordered game, `τ₁=1, τ₂=3` and `τ₁=100, τ₂=100.5` are compatible illustrations: move count does not fix the player's durations. The chess pieces and a game-only reviewer do not thereby acquire access to the player's thought.

The room parameter and the player's time are real within their **examples**. We do not import either as an external time for reality. In a whole without external time, the relevant task is to specify which internal relations correspond to the restricted succession and to any richer structure; a global temporal parameter or preferred foliation is not assumed.

## 3. One quantum implementation on the existing sphere state

We now use the actual stipulated `|Ψ⟩` of the previous asymmetric five-ray construction. It has Alice's pair/triple instruments, Bob's paired records and opposite sharp work currents. We do **not** identify these records with experiencing subjects or selected outcomes merely because they appear in the state.

Add two logical qubits on Bob's side:

- `R`, a confined-domain register with `|0⟩=A`, `|1⟩=B`, initially A;
- `H`, an extra-sector qubit, initially `|0⟩`.

The full starting state is `|Ψ⟩⊗|0⟩_R⊗|0⟩_H`. Like the earlier qubits, each added qubit *can* be represented in a four-spin singlet sector with encoded operations. That would take the earlier 38-spin construction to **46 physical spins**. This is a different pair of added blocks from the two reference blocks in the [subject–mismatch model](ZERO_SUBJECT_EXPERIENCE_BRIDGE_COMMON_DOMAIN_TEST.md), not an assertion that the two extensions are identical or already unified. The constructions are compatible tensor extensions but a combined model with both pairs would use 54 spins, before adding a clock.

On `H`, apply `U_H(φ)=H P(φ) H`, with `H` the Hadamard and `P(φ)=diag(1,e^{iφ})`. This produces

```text
|χ_φ⟩ = a_φ|0⟩ + b_φ|1⟩,
a_φ=(1+e^{iφ})/2,     b_φ=(1−e^{iφ})/2.
```

During those operations on the extra sector, **R remains exactly `|A⟩`**, for every φ. This is stronger than saying its mean is unchanged. The qubit and circuit are a finite *structural realization* of a held register and separate activity; `H` is not asserted to be a spatial chord, a thinking person, an independent time, or consciousness. The discrete sequence denotes the ordering of the stipulated operations, not fundamental time. Unit quantum evolution does not by itself select a unique experienced or recorded outcome.

### Case I: confinement with no extra-sector interface

After the `H` operations, apply a fixed `X` to R, independent of H:

```text
|Ψ⟩ |A⟩ |χ_φ⟩  →  |Ψ⟩ |B⟩ |χ_φ⟩.
```

The register holds A throughout the extra-sector operations and ends at B, irrespective of φ. At `φ=0`, the final H state is `|0⟩`; at `φ=π`, it is `|1⟩`. They are distinct and orthogonal, while every R-only statistic is the same. Because H remains in a product with the entire original system and R, **any adaptive operations and readouts confined to the original system plus R** yield the same statistics for the two H preparations, provided no H-dependent coupling is introduced. This is not merely equality of one mean.

Thus the specified confined history is `A→B` in either case, while the extra-sector states differ. The fixed X is a deliberately supplied update, not a derivation that the extra sector causes B. If there is no accessible interface, the confined description cannot tell which H state obtains. The existence of indistinguishable mathematical completions is not by itself proof that both are genuinely possible or actual; nor does observational equivalence prove they are the same.

### Case II: a specified interface, not a consequence of confinement

Instead, after H's operations apply a controlled-NOT with H as control and R as target:

```text
|Ψ⟩ |A⟩ (a_φ|0⟩+b_φ|1⟩)
     → |Ψ⟩ (a_φ|A,0⟩+b_φ|B,1⟩).
```

The interface is a concrete extra interaction. The Born probabilities for a final R measurement are

```text
P(R=B)=|b_φ|²=sin²(φ/2),    P(R=A)=cos²(φ/2).
```

For `φ=0, π/2, π`, they are respectively `0, 1/2, 1`. Thus R remains A during the extra-sector circuit in **every** case, but its final record statistics can depend on that sector if the specified interface is present. At φ=π it changes A→B; at φ=0 it remains A. At intermediate φ the final state is entangled, not a single selected outcome, unless an additional outcome account is supplied.

Nothing in confinement itself says there is such an interface or that inhabitants can choose φ. The CNOT is a controlled coupling between the two qubits in the same stipulated lab; it is **not** a non-interacting or spacelike process, a measured wormhole, or faster-than-light communication. Conversely, the empirical availability of an interface would not mean the intermediate H operations become surface positions or game half-moves.

## 4. The extension preserves the earlier physics rather than replacing it

Both circuits act only on the newly appended `R,H` factors. Therefore the complete reduced state of the **original** five-ray system is unchanged, including its asymmetric joint probabilities

```text
(triple i, original record 01/10):
(3/40,1/20), (1/10,3/10), (13/40,3/20),
```

and its sharp opposite original work currents in each original record branch. They are correlations in the stipulated vector, not proof of a selected outcome or a felt quality. The added register is not one of those two earlier record bits. The new ancillas may carry their own physical energy under an explicit implementation; we have **not** derived a zero total energy for the enlarged system.

The original pair and triple alternatives give the same full Bob-side density matrix. With identical product ancilla preparation and the same Bob-local ancilla circuit, the complete Bob-plus-ancilla state remains equal between Alice's two instrument choices. Therefore neither case lets Bob signal which instrument Alice selected. This is an operational quantum no-signalling statement for the specified factorization and operations, not a proof of spacetime-local implementation, physical subject locality, or no-signalling for arbitrary experiential access and incidence rules.

A phase set on H can be read through the Case II coupling, but that is a different task from Alice's choice. No conflict exists: interacting local subsystems can influence one another; a remote trace-preserving choice cannot be inferred from an unchanged local reduced state.

## 5. What this says about zero and necessary actuality

The previous system's opposite currents still add to zero in every specified original record branch. Both `φ=0` and `φ=π` preserve that cancellation, the five-ray record table and the initial confined register; in Case II they lead to different final R statistics. Thus **the current-zero constraint alone does not select the extra-sector relation or the interface**. Nor does the current sum establish a global zero of energy or experience.

This does not refute the stronger thesis that zero's *full constitution* necessarily determines the richer relations. It identifies the precise extra work: show why the complete zero constitution requires a particular interface, or why all genuinely possible relations and their incidences necessarily obtain, rather than supplying a phase and gate as independent choices. Declaring either possibility unreal merely because it is inconvenient would not answer that demand. Equally, these alternative circuit specifications do not by themselves prove metaphysical possibility, that every mathematical phase is actual, or how simultaneous actualities are weighted. An all-actuality account must say what counts as an actual branch/subject, how incompatible settings relate, and how the physical and experiential measures arise.

A useful mathematical challenge is therefore to replace the **free H preparation, phase, retention/update rule and gate** with relations that follow from a single internally differentiated zero constitution. The comparison above remains a control: any proposed derivation must explain which features are physically distinct and which are transported representations. Merely changing coordinates while transforming the state, observables and gate together does not create a new physical alternative; applying a phase operation while holding the rest of the apparatus fixed is a different, stipulated physical protocol.

## 6. Further connections and limits

- **Point–sphere:** The [blow-up construction](ZERO_POINT_INTERNAL_SPHERE_CONSTITUTION.md) already represents one external zero projection together with internal directional differentiation. The present held-register rule adds a different structure: a restricted history and a possible richer-sector interface. The blow-up does not automatically supply the history, and a geometric sphere is not identical to a quantum register.
- **Experience:** A person's experiential unity and duration need not simply be defined as the succession of accessible physical records. But the circuit does not establish a thinking subject, extra experience, unequal experienced durations or a bridge from H to feeling. Any such proposal needs its own subject, quality, incidence and empirical/report criteria, as in the [common-domain candidate](ZERO_SUBJECT_EXPERIENCE_BRIDGE_COMMON_DOMAIN_TEST.md). No literal external player is posited.
- **Wormholes and tunneling:** A wormhole tunnel is ordinarily part of the spacetime geometry described, not automatically an extra realm external to it. Standard tunneling has an amplitude in the barrier; neither phenomenon demonstrates an unobserved higher-domain journey or instantaneous transfer. The chord and circuit motivate well-defined comparisons, not an established mechanism.
- **Arrow and relativity:** A held register uses a directed update history, not a proof of the thermodynamic arrow. Our finite circuit assumes an ordered set of operations; it has not been embedded in relativistic field theory or shown independent of spacetime foliation. Nothing here licenses superluminal signalling or a preferred universal present.

## Verification

Run:

```text
python -m unittest verification.zero_confined_realms_interface_test -v
```

Ten standard-library tests cover the exact rational chord and alternative route, the history-dependent A/B retention rule, rotations, different chess dwell schedules, the inaccessible and coupled quantum cases, preservation of the original five-ray table and branchwise opposite currents, and pair/triple receiver equality. Quantum amplitudes are checked to numerical precision; the geometric calculations use exact fractions. The tests verify the declared models, not the actual existence of a richer physical plane, experiential incidence, or zero's self-sufficiency.
