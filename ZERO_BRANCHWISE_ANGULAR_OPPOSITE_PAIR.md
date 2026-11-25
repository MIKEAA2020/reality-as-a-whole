# A branchwise opposite pair in the coherent angular echo

## Result

**Gauge-constrained continuation:** [the angular pair as a physical gauge sector](ZERO_GAUGE_CONSTRAINED_ANGULAR_PAIR.md) gives an alternative formulation in which the opposite pair is required throughout the physical sector, without choosing a ready-pair vector. The gauge constraints and their physical–experiential interpretation remain substantive constitutive inputs, not an external preparation story.

The earlier [clock-dressed counterpart](ZERO_COHERENT_COUNTERPART_PAIRED_HISTORY.md) paired positive and negative **physical Born weights** across different sign branches. This pass constructs a stronger, different kind of pairing on the same original quantum echo: two distinct physical model carriers have equal-and-opposite nonzero signed values **together in every supported joint record branch**. Their sum vanishes as an operator on the prepared output, not merely after averaging over signs.

The carriers are two newly added value registers, each with its own angular-value register and two-level sign register. Their joint write is a reversible unitary that conserves the sum of their local signed model charges **on the whole finite pair Hilbert space**, not just on the prepared input. It is applied coherently to the actual original echo vectors. The write can be undone, allowing a closed 24-step stationary history.

This is a concrete route from nonzero local differentiation to a zero total, not a derivation of zero's ultimate constitution. In particular, the ready state already contains a prepared opposite-sign zero-charge pair; the signed Hamiltonian, controls, separate carriers and angular record are inputs. The modeled charges are not established cosmic energy, and two physical registers are not automatically two experiencing subjects. Suffering, if subsequently identified with a negative felt value, would remain real and would not be erased by its positive counterpart.

Executable construction: [verification/zero_pairwise_angular_charge.py](verification/zero_pairwise_angular_charge.py). Seven focused tests are in [verification/zero_pairwise_angular_charge_test.py](verification/zero_pairwise_angular_charge_test.py).

## 1. Why this advances the earlier pairing

The user's idea is stronger than the formal observation that an average can be zero: a zero whole may contain internally differentiated positive and negative contributions, without an external space, time, chooser or a denial of lived suffering. The previous pass established a sign-reversing physical symmetry of the coherent history, but positive and negative K signs appeared in different pointer branches. It did **not** establish that both are simultaneously present as distinct local contributions on an individual branch.

The earlier [conditional pair theorem](ZERO_CONFINED_REALM_SPHERE_RECORD_INCIDENCE_THEOREM.md) showed how oddness and equal incidence follow from a stronger pairwise balance premise, but that theorem did not itself create an angular-magnitude pair in the original echo. Here the plan is constructive: attach two actual mathematical carrier factors to the old echo, give each its own signed angular-magnitude observable, implement the write with charge-preserving gates, and check the complete quantum vectors and inverse. This adapts the user's cancellation proposal; it does not attribute this circuit to a source or assert that quantum factors are persons.

## 2. Two local quantities and a zero-ready resource

At the old echo's tick 10, the existing candidate sign observable is

```text
K = M J R,                 K²=I,
```

on the physical old-system/pointer/echo carrier. The added original angular register A has N orthogonal bin states `|i⟩`, N a positive multiple of four, and midpoint values `u_i=−1+(2i+1)/N`. We use the actual coherent old echo state from [the angular construction](ZERO_COHERENT_ANGULAR_SPHERE_ECHO_CONSTRUCTION.md); K and A commute.

Add **two distinct carriers**, each containing an N-state value record `A₁` or `A₂` and a two-level sign record `P₁` or `P₂`, with sign eigenvalues `z₁,z₂=±1`. For a specified function g on the bins define

```text
H₁(g) = κ g(A₁) Z₁,       H₂(g) = κ g(A₂) Z₂,
Q_pair(g) = H₁(g)+H₂(g).
```

Each H acts on its own `Aᵢ⊗Pᵢ` carrier. Their sum is a well-defined Hermitian **model charge**, or a Hamiltonian if the stipulated physical realization assigns it that meaning. The two separate factors do not imply separate subjects. The sign-symmetric local spectra and their zero offsets are chosen; a negative value relative to that chosen reference is not automatically negative gravitational energy or a measurement of valence.

Prepare the two value registers in `|0,0⟩` and the sign pair in `|+,−⟩`. Before any write,

```text
H₁ = +κg(u₀),    H₂ = −κg(u₀),    Q_pair = 0.
```

For either previous positive midpoint magnitude this ready pair already has **two nonzero, opposite** contributions. This matters: the construction does not make differentiated energy or experience appear from an undifferentiated bare zero; it assumes a structured zero-charge resource. Zero is not treated as an automatically sufficient origin merely because the sum is zero.

## 3. Explicit unitary writes conserve the charge globally

Let a,b be the two value-register indices. For each old angular bin i define a permutation Cᵢ on the **complete** pair basis:

```text
if a=b and z₁=−z₂:    (a,b,z₁,z₂) ↦ (a+i,b+i,z₁,z₂) mod N;
otherwise:             leave the basis state fixed.
```

The active and inactive subspaces are disjoint and invariant; the inverse replaces i by −i. On the active subspace `Q_pair(g)=0` for **any** g, before and after the shift. Outside it the operation is the identity. Therefore Cᵢ is a unitary permutation and

```text
[Cᵢ,Q_pair(g)] = 0
```

on the **entire pair space**, not only on the ready state. The coherent controlled copy is `C=Σ_i |i⟩⟨i|_A⊗Cᵢ`. From the ready pair it makes `A₁=A₂=i` without measuring A.

Next define F to flip both sign bits **only** on the same matched-value, opposite-sign subspace, and otherwise act as identity. F is an involutive unitary and likewise commutes with `Q_pair(g)` globally. Use the old observable K as a physical control:

```text
U_K = Π_(K=+) ⊗ I + Π_(K=−) ⊗ F.
```

K acts on the old carrier; F acts on the new pair, so `U_K` is unitary and conserves the new pair charge. Applied after C on the ready pair, it gives, for every old angular-bin/K component,

```text
|i,k⟩_old |0,0,+,−⟩_pair
       ↦ |i,k⟩_old |i,i,k,−k⟩_pair.
```

Consequently

```text
H₁(g) = κ k g(u_i),       H₂(g) = −κ k g(u_i),
Q_pair(g) = 0
```

on **every supported joint branch**. The test exhaustively enumerates all finite pair basis states for N=4,8 and the two earlier g functions, checks the gate inverses and exact charge equality, and independently checks examples of arbitrary diagonal value functions. The general proof is the zero-subspace argument above. The gates use a joint control across the two new carriers; their locality, control Hamiltonian and implementation cost are not derived.

## 4. The pair is actually coupled to the old quantum echo

At tick 10 the original old state may be a complex superposition of u bins and of both sign-pointer sectors; no intermediate measurement is inserted. The circuit above is a **linear isometry** on that state. In each old `s,r,j,i` component, `k=s r j`. The verifier applies the actual old `J` projectors to the original quantum vectors for source labels `0,7,15`, s=± and N=4,8. It checks directly that the first carrier's charge is the lifted old candidate

```text
H₁(g) |Ψ_recorded⟩ = κ M J R g(A) |Ψ_recorded⟩,
[H₁(g)+H₂(g)] |Ψ_recorded⟩ = 0.
```

The equality is on the specified prepared output; H₁ and the old candidate are not asserted to be the same operator on every possible unprepared state. On a fixed nonzero-g joint record, one carrier has positive and the other negative value regardless of k. Across the full coherent state their local signs can be entangled with the old pointer; there is no claim that both alternatives have definite values before the specified joint readout. The **sum**, however, annihilates the full coherent output without such a readout.

The previous physical sign counterpart reverses K while keeping the angular bin fixed. At this post-echo anchor, accompanying it with a flip of both new signs exchanges the pair's positive and negative local assignments. The quantum test checks the relevant original complex branch vectors and pair records for the same three source labels and N=4,8. This is a physical pairing symmetry on the recorded support, not evidence that the two carriers are actual experiencers or that an actual-incidence measure identifies their weights.

The new records are not a free relabeling. For fixed s, the old-system/R/A vector was pure before this write. The two value registers coherently record the bin, so after tracing out **all** new pair factors the old-system/R/A purity becomes `1/N`, and an old angular off-diagonal entry that was `1/N` becomes zero. The complete enlarged state is still pure: information is entangled with the new carriers, not destroyed. This result concerns the specified preparation and trace; reversible recording alone does not imply dissipation or a Landauer cost.

## 5. Closed relational history, not an external creation story

Insert the two new gates and their inverses after the old echo and before its inverse:

```text
F ; T Q T ; C U_K ; U_K C⁻¹ ; T Q T ; F⁻¹
7     3       2          2         3        7  = 24 ticks.
```

Since `U_K²=I`, this returns the pair, the angular register and the full old carrier to their ready input. The existing original apparatus gates do not touch the new pair. The pair charge is conserved by C and `U_K` on the entire finite pair space and is untouched by the other gates. The two earlier *specified* source/reservoir charges are also unaffected by the new gates under the existing tensor-factor assignments; none is thereby established to be objective whole-universe energy. A controlled cyclic shift and its uniform history can therefore be formed for this 24-step model, without an external time or preferred foliation.

With the earlier four-state reference rule `R_ref=q t mod 4`, both q=1 and q=2 wrap consistently because 24 is divisible by four. Under the same uniform-anchor relational comparison protocol, reference reading zero includes the **designated** completed-record anchor t=12 with conditional weight `1/6` for q=1 and `1/12` for q=2. These are weights for selecting that anchor, not probabilities that a similar pair never occurs at other ticks. The reference is another prepared resource, and q is a sampled increment, not automatically a proper-time rate.

## 6. What zero, by itself, still does not select

The same copy/write gates conserve `Q_pair(g)` for **every** diagonal value function g, because their nontrivial action is confined to a zero-charge sector. The construction works for both previous candidates

```text
g₁(u)=|u|,              g₂(u)=|u(u+1)|,
```

and for many others. This is constructive non-uniqueness within the stated finite mathematical model: pairwise zero and charge-conserving recording alone do not select the magnitude law. It is not a proof that multiple complete self-sufficient realities are genuinely possible. The stronger zero constitution may determine a unique law, but that has to be shown rather than assumed by declaring the other formal functions impossible.

The branchwise identity also does not by itself settle experience. To turn the physical pair into the desired experiential pair one would have to establish, rather than label:

1. which physical organizations are actual subjects or incidences and whether the two distinct carriers support one, two or no separate subjects;
2. why their intrinsic felt values are `H₁,H₂` on a common additive scale, including genuine negative felt valence rather than absence;
3. why the relevant whole-level aggregation includes these contributions exactly once, including any overlap, other incidences and unrecorded sectors; and
4. why the initial balanced resource, angular laws and actual physical energy arise from one self-subsistent zero constitution.

Those are not accepted residues. The constructive gain is that the shared model now has an explicit **simultaneous opposite-pair mechanism with exact unitary charge conservation**, alongside the earlier cross-branch counterpart. It demonstrates that neither nonzero local contributions nor coherent quantum dynamics logically require a nonzero modeled whole. It does not yet establish that the modeled whole is the actual physical–experiential whole, or that zero by itself necessitates this particular carrier.

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_pairwise_angular_charge_test \
 verification.zero_coherent_signed_counterpart_test \
 verification.zero_quantum_angular_echo_test -v
```
