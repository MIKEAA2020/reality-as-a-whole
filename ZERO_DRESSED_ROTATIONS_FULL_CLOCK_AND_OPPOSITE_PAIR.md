# Dressed rotations through the full clock, reservoir and opposite pair

## Result and its significance

**Deeper continuation:** [the relational magnitude root cause](ZERO_META_SYMMETRY_RELATIONAL_MAGNITUDE_ROOT_CAUSE.md) distinguishes the active u-changing action here from independent changes of two internal frames with a covariant comparison link. The latter preserve the individual magnitudes as well as the zero sum, but leave an orbit-space measure question. [Relational kinetic selection](ZERO_RELATIONAL_GEOMETRY_KINETIC_MEASURE_SELECTION.md) further shows that the active action here does not generally preserve the subsequently imposed frame-gauge physical vector sector. The unitary action and pair-sector result below remain valid on their stated larger carrier; fixing the uniform history alone does not establish frame-gauge-sector preservation.

The previous [record-dressed rotation](ZERO_RECORD_DRESSED_SPHERE_ROTATION_SYMMETRY.md) related the original correlated records at the post-echo checkpoint. This pass extends the construction in two directions **at once**: through the actual 20-step echo and purified source/reservoir cycle, and into the gauge-constrained pair of opposite model charges. The resulting rotation is a clock-controlled unitary on an explicitly enlarged model; its action preserves the specified stationary history and transports the pair's constraints. The original [full quantum records](verification/zero_dressed_history_pair.py), actual reversible apparatus permutations and the finite pair encoding are used rather than replacing them with an unrelated classical model.

There is also a substantive limitation. For a nonconstant angular magnitude, the dressed rotation does **not** preserve an individual pair charge or even its square. It does preserve the pair's zero sum on the physical sector. Thus a symmetry of the correlated state and its zero total is not automatically a symmetry of every local magnitude observable or a fundamental Hamiltonian. This makes the user's proposed unification more precise: either local values transform as parts of the symmetry-related configuration, or an additional principle must explain a smaller physical symmetry. The construction does not decide which is physically correct.

The [verifier](verification/zero_dressed_history_pair_test.py) checks the original large-vector echo at every tick, the actual apparatus basis paths, the pair embedding and selected joint states. The construction and all interpretation remain conditional model work, not a claim that energy or experience has already been derived from zero.

## 1. The missing reservoir transformation is real

In the [20-step clock construction](ZERO_COHERENT_ANGULAR_RESERVOIR_CLOCK_ACCESS.md), the old system has a physical B observable. The apparatus evolves by a B-controlled sequence of seven reversible source, memory and finite-store operations, waits through the six echo operations, and reverses those seven operations. It includes coherent source references and purifiers. Write `F_t` for the full B-controlled apparatus prefix and `C_t` for the old-system/echo prefix. The latter has the actual checkpoints

```text
C_t = I, T, QT, TQT, QT, T, I  across ticks 7 through 13,
```

with composition read right to left; it is I before tick 7 and after tick 13. The separate reference clock is a spectator to these material operations. On each B block, the same apparatus prefix applies to all angular bins in that block.

At the post-echo checkpoint, the previous rotation can change a B-positive record into a B-negative one. At tick 10, however, the corresponding purified apparatus states are orthogonal: the coherent source references retain which B-controlled interface was used. The tested apparatus overlap is 1 at tick 0, **0 at tick 7 and tick 10**, and 1 again when the apparatus has completed its inverse at tick 20. Applying the old-record dressing alone at tick 10 therefore leaves the wrong apparatus record; on that conditional transfer its overlap with the correctly transported target is zero. This is a concrete negative control, not merely a warning that an apparatus might matter.

To repair it, undo the appropriate apparatus prefix in the input B block, perform the old-record transfer, and reapply the prefix in the output B block. This changes actual coherent source/reservoir records without measuring the reference or purifier labels. All 128 prepared reference/purifier combinations for each B (256 including B) and every tick are checked against the existing apparatus paths; the same permutations apply linearly to their coherent superposition. Their amplitudes and orthogonal references are retained. A B-dependent retargeting block is not a stand-alone unitary that freely overwrites B: it is part of a joint unitary which also transforms the B record.

## 2. A necessary full-space correction

The earlier angular routines apply `value_history` to the **valid supported sector**. It is not the full unitary Q on arbitrary vectors. In fact the raw physical chirality operator has additional spectrum away from that sector. Using it as Q on the whole carrier caused the arbitrary-vector cocycle test to fail. The full involution is instead

```text
Q = I − P + O,    O = P · value_history · P,
```

where P is the valid projector transformed from the canonical spin coordinates back to the physical axes. The two projectors are on the old carrier; on the valid sector this agrees with the actual earlier echo operation. On its orthogonal complement Q is identity. The verifier checks the involution on an arbitrary vector and includes a counterexample showing that the unprojected shortcut is not that full-space extension. This matters for the operator proof; supported-vector agreement alone would not establish a unitary group action on the entire carrier.

Set `K_t=F_t C_t C_10†`, where `C_10=TQT`. K_t maps an anchor-10 old/echo vector with the common initial purified apparatus to the actual old/echo/apparatus vector at tick t. It is unitary, does not depend on sphere coordinates, and acts trivially on the separate pair registers. The finite apparatus gates and full T/Q echo gates are reversible; at tick 20 the cycle closes. The [implementation](verification/zero_dressed_history_pair.py) evaluates the echo conjugation explicitly and evaluates the apparatus prefixes and inverse as the original permutations, not by a new assumed clock trajectory.

## 3. Extend the constrained pair without erasing polarity

Use the previous N=4 spherical step lift, and let `i(u)∈{0,1,2,3}` be the bin of the relative angle. Introduce discrete angular-copy labels `a,b∈{0,1,2,3}` and sign qubits `z₁,z₂∈{±1}`. At anchor 10 the old sign is `k=s r j`, where s is the sign pointer, r the actual echo record and j the old J sign. The [gauge-constrained pair](ZERO_GAUGE_CONSTRAINED_ANGULAR_PAIR.md) has the physical relation

```text
a=b=i(u),     z₁=k,     z₂=−k.
```

The pair signs are distinct physical values, not gauge-identified opposites. There is exactly one such pair extension for each old state and angle bin. The map W_i is an isometry, not a claim that a cosmic agent prepared a blank pair.

For a full-carrier extension, choose a mathematical reference pair basis state `(a,b,z₁,z₂)=(0,0,+,+)` and define the controlled **basis permutation** E_i by

```text
(a,b,z₁,z₂) ↦ ((a+i) mod 4, (b+i) mod 4, k z₁, −k z₂).
```

Here k is the commuting anchor operator `Z_M · R · J`; the map is controlled coherently, including superpositions of its eigenvalues. E_i is a unitary on the entire finite pair basis. Restricted to the reference fiber, it gives W_i, and `E_i P₀ E_i†` is exactly the physical projector for that bin. This reference fiber is a convenient coordinate for the isometry and its extension; it is not posited as a separately existing ready resource in the physical sector. Different full-space extensions can agree on the same physical sector.

For the continuous sphere, the added pair registers copy the **finite bin label**, not a delta-normalized copy of a continuous point. We can still define local model charges using the common base angle,

```text
H₁=κ g(u) Z₁,        H₂=κ g(u) Z₂.
```

On the physical sector their sum annihilates every state, including coherent superpositions. At the N=4 midpoints these recover the previous finite-bin values. This continuous `g(u)` is an operator on the base angle, not a claim that the discrete copies independently encode every continuous u. Away from anchor 10, the pair and its constraint are carried by K_t; the transported k need not equal the instantaneous product `s r j`.

## 4. One rotation representation for the entire stationary history

Let `V(u)` be the previous sign-controlled record unitary, and define `D(u)=E_i(u) V(u)`, with V acting trivially on the auxiliary pair. Both are pointwise unitaries. For independent rotations g of the two sphere directions, let P_g be the standard pullback. At the anchor, on the **whole** old/record/apparatus/pair Hilbert space, define

```text
U_g^(anchor) = D P_g D†.
```

This is a strongly continuous unitary representation with `U_g U_h=U_(gh)`. For target x and source y=g⁻¹x its record/pair factor is `E_i(x) V(x) V(y)† E_i(y)†`. It maps the physical projector at y to that at x, hence restricts to a unitary action on the constrained direct-integral sector. Its physical restriction can equivalently be written `W_i(x) V(x)V(y)† W_i(y)†`. The full permutation E supplies an extension to unphysical pair states, so this is not a partial isometry mislabeled a unitary on the whole space. Boundary conventions affect only measure-zero sets.

For each clock block transport the action with the **actual** dynamics:

```text
U_g^(t) = K_t U_g^(anchor) K_t†,
U_g^(history) = Σ_(t=0)^19 |t⟩⟨t| ⊗ U_g^(t),
P_phys^(t,x) = K_t E_i(x) P₀ E_i(x)† K_t†.
```

The independent reference clock is left untouched. These equations give a group representation and carry physical constraints covariantly at every clock block. If `W` is the cyclic clock shift with the actual next gate, then `W U_g^(history) W†=U_g^(history)`: each next-block operation conjugates K_t into K_(t+1), including the wrap. This is the same relational stationarity mechanism as the earlier clock construction, not an additional fundamental time direction.

The post-echo source-family frame relation established previously holds for all 16 source labels and both signs. Tensor the fixed reference vectors with the common coherent initial apparatus and the pair reference fiber. E_i, V(u), and K_t then yield exactly the corresponding paired, purified clock-block history. It follows algebraically that their uniform-amplitude spherical lift, and any coherent superposition of those source labels, is fixed by the clock-controlled rotations. The previously specified q=1 or q=2 reference-clock correlation is a spectator and is included in that statement. Because the transformation is linear, the apparatus references and purifiers remain coherent; no off-surface observer or extra registration by a confined inhabitant is introduced.

The code checks actual complex old-system/R vectors for three source labels and both signs at all 20 ticks, arbitrary-vector transport and echo-step intertwining, all prepared apparatus reference/purifier paths, and explicit joint old/echo/pair/apparatus transfers for two source labels and both signs at selected ticks. The general statement additionally uses the earlier all-16 source-frame test and the algebra above; it is not a claim that a dense full reservoir-and-clock matrix was materialized. The supported-component fast path is only a restriction of the full unitary, not an implementation of its action on arbitrary invalid pair inputs.

## 5. Zero sum survives; local magnitude does not

On the constrained sector, `(H₁+H₂)=0` identically, so every physical rotation preserves its kernel and its zero value. Yet

```text
H₁²=κ² g(u)² I  on that sector.
```

A transitive independent rotation can take u from `1/4` to `−3/4`. For `g₁(u)=|u|`, the squared magnitudes are `1/16` and `9/16`; for `g₂(u)=|u(u+1)|`, they are `25/256` and `9/256`. Therefore the same rotation does **not** commute with H₁². More generally, if a transitive independent-rotation action commuted with this multiplication operator everywhere on the physical sector, `g(u)²` would have to be constant almost everywhere. The supplied nonconstant g laws do not meet that condition. The verifier checks both explicit controls.

This is not a contradiction: an active rotation that carries a real local value into a different local value need not commute with the individual-value observable. It is not, however, evidence that the chosen action is a dynamical symmetry preserving all physically relevant observables. If individual model charges are taken to be invariant physical energies under these rotations, this full independent group cannot be imposed unchanged with either g law. A smaller subgroup, different transformation law, or different constitution would have to be justified rather than silently assumed. The physically meaningful zero sum remains compatible with nonzero and unequal-angle local terms.

Within the fixed dressed family the earlier transitivity argument still selects constant scalar amplitude; the joint pair and apparatus do not remove the other invariant reference states. It does **not** uniquely select this dressing, state family, local magnitude law, physical energy or actual subject-incidence measure. The model's sign and magnitude are not established felt valence, and positive experience is not assumed to erase suffering. Nor does this result prove actual plenitude, locality, spacetime dynamics or the intrinsic/extrinsic experiential identity. The aim remains a self-sufficient whole without unexplained residue; the current explicit constructions specify rather than derive their carrier, constraints, dynamics and representation.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_dressed_history_pair_test \
  verification.zero_dressed_sphere_rotations_test -v
```

The numerical checks validate the encoded finite model and selected original full-vector cases. The continuous group law, full stationary intertwining and isometric extension follow from the stated conjugation and cyclic-prefix arguments, conditional on those model inputs.
