# Joint quality, unity reports and incidence symmetry

## Result

The preceding [typed-process construction](ZERO_TYPED_ECHO_PROCESS_CLOCK_ACCESS_AND_SUBJECT.md) gave two jointly accessible physical signs, `N=Q_now` and `K=Q_echo`, and restricted operations that can flip either sign independently. This pass tests a **unity bridge** on that same carrier rather than treating joint accessibility as a subject by definition.

The central result is an exact operational ambiguity. On the prepared echo sector, `N K=B`. A reversible device that writes the product by successively using N and K has **exactly the same final quantum channel on the code** as a device that simply reads B. This equivalence holds for coherent inputs and entanglement with a reference. It is also checked against the original complex echo vectors and the constrained opposite pair. A successful product report therefore does not by itself establish that a subject has experienced N and K together—or even that the report apparatus combined their values along the physical path.

A stronger, explicitly conditional symmetry argument narrows but does not close the unity question. If independent single-sign flips are genuine symmetries of an actual subject-incidence law, a unity predicate depending only on `(N,K)` must be constant on the four sign cells. But **both** “one joint subject” and “separate subjects” remain possible constant assignments. Even with symmetry-invariant normalized incidence weights and an optional type swap, the weight assigned to joint versus separated incidence remains undetermined.

The concrete constructions and controls are in [verification/zero_joint_unity_bridge.py](verification/zero_joint_unity_bridge.py) and [its tests](verification/zero_joint_unity_bridge_test.py). They do not establish conscious experience, the true ownership rule, or actual subject weights.

## 1. Two explicit bridge candidates

At the anchor of the existing echo, with the added saved-J memory L retained, the physical sign observables are

```text
N = M J,       K = M L = M J R,       N K = J L = B = R
```

on the stated ready support. The last equalities are not identities on arbitrary unready states. Both signs are jointly measurable on this commuting physical interface. For the specified original state, their four joint cells have physical weight `1/4` each.

Consider two **different hypothetical bridges**, keeping the same physical state, gates and possible reports:

* **Joint bridge U:** for a relevant joint physical event, N and K are two coordinates of one subject occurrence.
* **Separated bridge S:** for that event, N belongs to one subject occurrence and K to another, with distinct owners.

These are not exhaustive: one persisting subject might have two occurrences; subjects might overlap or nest; the whole might also have its own perspective. Nor is either bridge established merely by a label. U and S are included to identify what an experiential identity law must decide while retaining the user's possibility of genuinely plural subjects.

Both can use the same physical apparatus. If their report law is also held fixed and the bridge labels have no physical effect, no physical outcome from that unchanged state and report distinguishes them. This is an underdetermination result for the stated extensions, not proof that subjecthood is nonphysical or that two complete metaphysical worlds exist. A successful theory could make a further, independently testable ownership or first-person report commitment.

## 2. A joint-looking report has a shortcut

Write signs as bits with `+→0`, `−→1`. Let a fresh report bit P initially be 0. Consider the two explicitly different circuits:

```text
Joint accumulation:   P ⊕= M;  P ⊕= J;  P ⊕= M;  P ⊕= L.
                       first pair writes N, second pair adds K.

Bypass:                P ⊕= B.
```

The first writes the XOR/product of N and K; the two M-controlled flips cancel in the **final** circuit. The second uses the existing B relation directly. On the code `B=J⊕L` they agree exactly for **every** initial P and every logical basis state. Let V encode `(M,J,L,P)` into `(M,J,L,B,P)` with `B=J⊕L`; the executable matrix check proves

```text
V†V=I,       U_joint V = U_bypass V.
```

Because these are equal isometries, not merely equal probability tables, the final full reduced code state is identical for any coherent logical input and for any input entangled with an arbitrary reference. Tensoring a disconnected spectator does not change the identity. A final measurement on the retained code and report therefore cannot distinguish the two circuits under these premises.

The identity is also checked using actual complex original echo vectors, including both pointer signs, saved L, and the original gauge-constrained pair. On every supported recorded component, the direct B projection and the `(N,K)` grouping agree, and the pair retains `Z₁=K`, `Z₂=−K`. The reduced five-bit code is a specified operational interface; the full old sphere, clock and reservoir have not been replaced by five fundamental qubits, and no assertion is made that the bypass gate is local or physically free.

### What would distinguish the histories?

The two implementations have different **internal gates**, even though their final actions agree on this code:

* An intervention that changes J while holding B and L independently fixed can make their final P outputs differ. That intervention is **off the prepared code** `B=J⊕L`; whether the complete physical theory permits it is not established.
* An intermediate readout of P after the joint circuit has written N can differ from a bypass already reading B. That comparison needs a clocked intervention and changes or records the process; it is not available from final data alone.
* Separate records of N and K reveal both signs rather than only their product. They are additional physical interactions, not a free interpretation of the parity report.

A circuit with causal inputs N and K and a circuit with a shortcut through B can thus have the same permitted final statistics. Conversely, if a subject rule depends on the *actual causal path*, more than a final input–output channel must be specified. Neither matching outputs nor differing gate decompositions alone chooses U or S.

## 3. Product access is weaker than access to both signs

With the specified equal four-cell physical distribution, P reports `N K=B` perfectly. But each of the four `(N,K)` pairs has weight `1/4`, so within either product outcome N is equally likely to be positive or negative; the same holds for K. An observer with **only** the product report has optimal success `1/2` for either individual sign. This is a restricted classical-sign statement; it is not a bound on an observer who can also access M, J, L, R, B or other quantum degrees of freedom.

There is also a coherent distinction between the instruments. On the original pure joint M/L/old state, retaining a product-only report and tracing it out dephases two B sectors, with fidelity

```text
F_product = (1/2)²+(1/2)² = 1/2.
```

Writing separate N and K reports and tracing both out dephases four joint sectors, giving

```text
F_both = 4(1/4)² = 1/4.
```

The tests compute these sector weights from actual complex source vectors and check that the constrained opposite signs are preserved. They are fidelities for this input and these report protocols, not general thermodynamic costs or a claim that awareness is a quantum measurement. Coherent uncomputation is possible but removes the durable report.

The product is even under the physical sign counterpart `(N,K)→(−N,−K)`. Hence it is a poor witness for the individual signs: an invariant P distribution can coexist with distinct positive and negative modeled contributions. No inference about actual felt valence follows, and any genuinely negative experience would not be removed by a positive counterpart.

## 4. What the symmetries do select—conditionally

The prior full quantum construction has a physical sign counterpart, and the active type operation exchanges N and K. At the level of the four sign labels, their actions are

```text
counterpart: (N,K) → (−N,−K),       type: (N,K) → (K,N).
```

A Boolean unity predicate `u(N,K)` invariant under both can still distinguish the two orbits

```text
{(+,+),(−,−)}       and       {(+,-),(−,+)}.
```

There are four such predicates, including a unity rule that depends on whether `N=K`—equivalently on B. Thus these symmetries alone do not exclude the earlier B-dependent ownership candidates.

Now impose the stronger condition that unity is also invariant under **independently flipping either coordinate**. These operations act transitively on the four labels. Therefore `u` must be constant: the only two binary predicates are “joint everywhere” and “separate everywhere.” This is an exact finite theorem, checked exhaustively over all 16 Boolean predicates.

The previous pass supplies concrete state-family-adapted operations that flip N alone or K alone **on the selected `z=+` two-bin sector** of the actual quantum history. They are active operations on the larger carrier, not established symmetries of the complete physical–experiential laws, unrestricted local interventions, or proved gauge-sector-preserving transformations. Moreover, the previously defined type swap need not preserve that selected sector. Combining all these label permutations as symmetries of one common actual-incidence domain is an additional assumption. Consequently the theorem says what would follow **if** the complete unity law had the stipulated symmetry; it does not prove those operations are fundamental symmetries or select one of the two constant bridges.

The predicate restriction matters too: a real identity rule might depend on the process, accessible algebra, history or other intrinsic structure, not only the two sign values. The result rules out value-dependent predicates under the stated group, not every possible physical constitution.

## 5. A normalized incidence countermodel

To see what even the stronger symmetry leaves open, suppose the relevant sampling domain has three stipulated incidence types:

* `J`: a joint incidence carrying both coordinates;
* `N`: an incidence carrying the N coordinate;
* `K`: an incidence carrying the K coordinate.

Define the normalized proposed weights

```text
μ(n,k,J) = α/4,
μ(n,k,N) = (1−α) β/4,
μ(n,k,K) = (1−α)(1−β)/4,        0≤α,β≤1.
```

For every α and β, summing the types gives the same physical four-cell marginal `1/4`. Each type's weight is invariant under either single-sign flip. In a specified vector bookkeeping convention—joint incidences contribute `(n,k)`, N incidences `(n,0)` and K incidences `(0,k)`—the signed sum is `(0,0)` for every α and β. This is a formal structural sum, not a derivation that physical signs are feelings.

If the type swap also exchanges N and K incidence types while leaving J fixed, invariance requires `β=1/2` whenever the separated weight is nonzero. It still leaves **α arbitrary**. For example, α=1 gives the joint-only sampling extension; α=0, β=1/2 gives equal sampling weight to the two coordinate types. The exact tests include intermediate α and unequal β controls.

This does not say that these probabilities are the number of actual subjects, that every physical cell is actual, or that normalized sampling of coexisting subjects is mandatory. In particular, a claim that each separated event contains two actual subjects requires its own incidence and sampling law. The table demonstrates the limited point: symmetry of signs, a fixed physical marginal, and a zero structural sum can all hold while joint-versus-separated **incidence weight** remains free. As above, applying all the assumed symmetry maps to one real incidence domain still needs proof.

## 6. A conditional positive unity-witness protocol

The no-go above concerns *physical output alone*, not the impossibility of a genuine first-person witness. Here is a specific proposed discriminator, with the phenomenological assumption isolated rather than buried in the decoder:

1. Use the previously checked two-bin, `z=+` sector and its restricted N- and K-flipping operations to define the four physical conditions. Randomize or counterbalance their order. The apparatus must separately verify N and K, control access to B/R/H shortcuts, specify the clock interval, and retain or export its records. These are protocol requirements; the full-clock, local, freely repeatable realization of those controls has not been demonstrated.
2. Define an experiential target **Z independently of the device output**: on a trial, a single subject has a unified occurrence containing the two specified aspects. Bridge U predicts `Z=1`; the *strict* separated bridge S predicts `Z=0`. More nuanced overlapping, nested or sequential subject theories are not covered by that binary prediction. Identifying the physical N/K signs with the specified experiential aspects is itself an unproved premise.
3. Obtain a separate first-person unity report Y, and assume a separately justified error bound `P(Y≠Z)≤ε`. A perfect physical product report is not Y. Both U and S can generate the same correct N, K and B records, so those records are controls and do not by themselves validate the phenomenological report.
4. As an illustrative **conditional** design, let `ε=1/10` and suppose nine independently prepared trials with independent report errors. Decide U when at least five Y reports say unity. If U and strict S make the stated opposite Z predictions, each error probability is at most the binomial tail

```text
Σ_(k=5)^9 C(9,k) (1/10)^k (9/10)^(9−k)
    = 22273/25000000 ≈ 0.000891.
```

This is not a measured error rate, a demonstrated human assay or a recommended sample size. It illustrates the exact consequence of the premises. Physical access, independently prepared repetitions, report retention, calibration, and the identity of experiential aspects are all unresolved. The initial report and saved-memory operations also disturb or entangle the state; coherent reset removes the corresponding record, so durable repeated observations need their own resources.

The independence premise is consequential. With the **same** per-trial error probability `1/10`, a correlated control can fail the majority decision with probability `9/50=0.18`: with probability `9/50`, exactly five randomly chosen trials are wrong; otherwise all are correct. Each trial is wrong with probability `(9/50)(5/9)=1/10`. The verifier checks both exact calculations. A nominal per-trial calibration alone therefore does not justify the IID tail.

Most importantly, the latent Z and its error bound are not provided by the physical echo. If Z is defined as whatever Y says, or if the error bound is inferred only from the same report, the comparison is circular. A usable witness requires an independently justified first-person/physical correspondence and a way to assess its errors; the present construction specifies what such a bridge must deliver, not that it has been delivered.

## 7. Refinement and the next dependency

The channel comparison is also transported through the earlier coherent J₁/J₂ encoding: the test checks both physical report circuits intertwine with the old code and remain identical on the transported code. A single J-share flip is not generally a code-preserving logical intervention. This protects the conclusion against that specified implementation change without assuming that the extra physical share is phenomenally irrelevant in all possible theories.

The next task is to seek a **noncircular basis for the witness assumptions**—especially the identity of the two experiential aspects, the report/ownership error relation, admissible interventions and reproducible records—and to extend the comparison beyond strict disjoint U/S alternatives to overlapping or nested subjects. Only with a justified incidence/valence bridge can the user's signed whole be assessed rather than installing the desired zero.

Reproduce:

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_joint_unity_bridge_test \
  verification.zero_typed_echo_process_test \
  verification.zero_ownership_report_bridge_test -v
```
