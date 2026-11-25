# From the reduced type swap to the original coherent quantum echo

## Result

The [earlier source-integration pass](ZERO_SOURCE_INTEGRATION_STATIONARY_SUBJECT_INCIDENCE.md) established an active transformation that swaps the binary candidate signs `sj` and `sjr` in a **reduced** stationary history. It explicitly left open whether this was a symmetry of the original coherent quantum construction. This pass supplies a concrete lift on that earlier physical echo, with a necessary correction: the operation must include the sign pointer M, not just flip j conditional on the echo memory.

For each of the **16 original source/clock labels**, the new [quantum verifier](verification/zero_full_echo_type_swap_test.py) checks that one gauge-compatible controlled operation preserves the complete complex state of the post-echo old-system/M/R construction, while on its actual `B R=+1` support it exchanges the two physical sign observables `M J` and `M J R`. This is stronger than matching a reduced probability table. The result is still a symmetry of a specified prepared model and restricted observable interface, not proof of an actual subject, felt sign, physical implementability at zero cost, a symmetry of every operation, or an incidence measure.

The [angular extension](ZERO_POINT_SPHERE_SIGNED_MAGNITUDE_ECHO_INTEGRATION.md) supplies a crucial compatibility condition: a genuine **full-quality** symmetry must preserve magnitudes as well as signs. A further quantum check now attaches a coherent, physical two-band record to this same echo: keeping the record fixed breaks the old state symmetry, but actively swapping it repairs the state symmetry. The two example magnitude assignments then behave differently under that repaired operation. Neither a bin record nor a magnitude operator establishes an experiential realization.

## 1. The operator

Use the actual old valid-sector projector P, conserved B observable, j observable J, and existing self-adjoint involution `Q=I−P+O`. The old code establishes

```text
Q²=I,      [Q,P]=[Q,B]=[Q,G]=0,
P Q J Q P = P B J P,
```

where G is the specified internal gauge. Add the pre-existing sign pointer M with `Z_M=±1` and the echo memory R with `Z_R=±1`; neither is assumed accessible to a j-only inhabitant. Define the operation on old system ⊗ M ⊗ R:

```text
D_full = I_old,M ⊗ P_R+  +  (Q ⊗ Z_M) ⊗ P_R−,
P_R± = (I ± Z_R)/2.
```

The two R blocks are orthogonal, and `Q` and `Z_M` are self-adjoint involutions, so `D_full` is a self-adjoint unitary involution. It preserves P, B, `Z_M`, `Z_R` and the declared internal gauge. It acts on Q's real old reference/work/B/j carrier, M and R; it is **not** a bare j-only operation.

Write `J` and `R` for the lifted commuting sign operators. In the R-positive block, D leaves J unchanged. In the R-negative block, it conjugates J to `B J` on P. Therefore on the actual post-echo support `P` with `B R=+1`,

```text
D_full† (Z_M J) D_full = Z_M J R,
D_full† (Z_M J R) D_full = Z_M J.
```

These are compressed operator equalities **on that support**. The script checks all four B/R sectors: the corresponding identity fails on the nonactual-in-this-protocol `B=+,R=−` sector, so it must not be promoted into a global all-state operator equality. The support is a result of the earlier ready-memory echo, not a blanket restriction on every mathematically permitted memory preparation.

## 2. The actual coherent state is stabilized

Let `x` be any of the 16 previously prepared old source histories. The pointer write has s-branch

```text
v_s = (x + s Qx)/2,       Q v_s = s v_s,      s=±1.
```

After the existing T–Q–T echo, the coherent R slices are, exactly as in the previous quantum verifier,

```text
R=+: Q Π_B+ v_s,          R=−: Q Π_B− v_s.
```

Each has B sign equal to its R sign and still has Q eigenvalue s. On R-positive, `D_full` acts as identity. On R-negative, `Q Z_M` acts as `s·s=1`. Thus it fixes each **complex vector slice**, including its phase, and by linearity fixes their M/R superposition. This is tested directly on all 16 actual old source histories, alongside the gauge and B/R support conditions.

The pointer factor is essential. Omitting `Z_M` makes the s-negative, R-negative component acquire a minus sign while the R-positive component is unchanged. In the checked s-negative case those R branches have equal norm, so the transformed coherent state is orthogonal to the original; the change is **not** merely a global phase. The corrected operation preserves the state and swaps the observables on the relevant support.

The old auxiliary forward operations are separately described as B-controlled and commuting with the old echo; on an extension where they act only on their added registers and are diagonal in B, they commute with this D operation as well. The new verifier itself checks the 16 original coherent source histories, **not** a densely constructed quantum state containing every source, reservoir, clock and reference degree of freedom. That larger state and any physical implementation cost remain separate checks.

## 3. A coherent quantum record of the angular bands

The angular construction distinguishes two equally weighted B-negative bands with **conditional average** `g₁` magnitudes `1/4` and `3/4`; for g₂ both band averages are `1/6`. To link that refinement to the actual old quantum echo, introduce an additional neutral qubit A in a ready state and **coherently copy final J into A** after the echo. In the B=R=− sector, final `j=−z`, so this records the old two z bands with reversed signs. This is a two-bin physical analogue of the angular information, not an embedding of the entire continuous sphere or a demonstrated felt-magnitude detector.

Let `c` be the existing R-negative state at fixed source label and M sign s; define `c_±=Π_J± c`. The old state is coherent across both J components. The new controlled record makes

```text
c ⊗ |ready⟩  →  c_+ ⊗ |A+⟩ + c_- ⊗ |A−⟩.
```

Both components have equal nonzero norm in each of the 16 checked source histories and s sectors. All old **diagonal** B/J/M/R probabilities are unchanged, but tracing out A changes the conditional old-system state's purity from 1 to 1/2: the added record is not a free redescription of the complete quantum state. The overall old-system-plus-A state remains pure; nothing is erased.

Now apply the previous `D_full` **without** changing A. In the R-negative branch Q flips J while the A label stays fixed, giving zero overlap with that recorded branch. The R-positive branch is unchanged and has equal total norm, so the normalized full-state overlap is `1/2` (fidelity `1/4`), not 1. This checks that the binary symmetry cannot simply be reused after adding a record.

There is a concrete repair: accompany `D_full` with an A flip **only in the R-negative branch**. The verifier establishes `s Q c_+=c_-` and `s Q c_-=c_+`; the A flip then restores the full recorded state, complex amplitudes included. It also exchanges the two band labels. Consequently, the bin-level magnitude operator assigning g₁'s conditional means `3/4` and `1/4` is **not** invariant under this repaired physical swap; the g₂ bin operator assigning `1/6` to both is invariant within this sector. These are exact computations on the original coherent source/echo vectors plus a newly stipulated record qubit. They do not show that the continuous angular construction preserves the original full state, or that its proposed magnitudes are actually experienced.

This result links the earlier symmetry and the angular correction at the quantum level: *a new physical record may require a transformed symmetry, and preserving signs or coarse probabilities does not settle whether the full magnitude is preserved.* The choice of actual carrier, record, magnitude law and experiential interpretation still has to follow from the sought constitution.

## 4. Stationary lift, and what it would need for incidence

For any closed cyclic quantum history with unitary prefixes `U_t`, `U_20=I`, controlled clock shift W, and a fixed anchor state stabilized by `D_full`, the dressed operator

```text
D̄ = Σ_t |t⟩⟨t| ⊗ U_t U_10† D_full U_10 U_t†
```

commutes with W and stabilizes that history state. This is the same algebraic transport used in the reduced pass; the conclusion is conditional on the chosen **full** cycle and the anchor-state stabilization. The physical locality and realizability of the clock-controlled operation are not thereby established.

If one postulates two distinct actual subject-incidence types, a physical pure-marginal product extension, and invariance of the **physical–experiential incidence law** under the joint physical/type exchange, then equal type weights follow as before. This physical operator makes that proposal better grounded than a mere renaming. It still does not prove that the actual incidence law has that symmetry, that two types exist rather than two descriptions of one occurrence, or that the proposed signs are felt.

In particular, the angular example shows why real quality magnitude matters. If the magnitude-carrying part of the full physical–experiential structure transforms nontrivially, sign exchange alone cannot be used to assert the combined operation is a full-quality symmetry. Whether the quantum D_full preserves the needed actual magnitude is an open constitutive question, not automatically answered by its action on M, J and R.

This moves the existing candidate toward a coherent common interface while preserving the stronger target: zero's own constitution must still determine the actual physical and experiential facts together, not merely leave an allowed symmetry as an unexplained extra premise. Neither the full quantum check nor the conditional type-weight theorem is an external foundation or PSR battery pass.

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_full_echo_type_swap_test \
 verification.zero_dynamic_subject_memory_echo_test \
 verification.zero_echo_intrinsic_constitution_selection_test -v
```

The four new checks cover full-operator transport on actual support, preservation of all 16 source states, the phase-sensitive pointer control, and coherent two-band recording with the repaired symmetry and conditional purity. Their tensor-factor and gauge assumptions are those of the existing finite model plus the explicitly added record qubit.
