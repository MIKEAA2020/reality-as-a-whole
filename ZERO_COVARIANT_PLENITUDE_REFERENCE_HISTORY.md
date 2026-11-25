# A permutation-symmetric whole with a changing relational history

## Main result

The [preceding test](ZERO_ISOTROPIC_PLENITUDE_AND_RELATIONAL_DYNAMICS.md) found that a closed four-spin zero sector cannot evolve nontrivially if its Hamiltonian commutes with every permutation of the four spins. Here an **internal reference carrying the permutations** removes that particular obstruction:

- The whole state and Hamiltonian are invariant under simultaneous permutation of the spins and reference.
- All three spin pairings are present coherently; no fixed pairing is selected in an external labeling.
- The four-spin reduced state is the same maximally mixed zero-spin state at every clock reading.
- Nevertheless, a **permutation-invariant spin–reference correlation changes**. In each reference frame, an initially opposite pair transfers its correlation to a different pair.
- A positive stationary constraint has a unique zero eigenstate for this specified history.

This is an explicit, nontrivial way to combine whole-level symmetry and internal differentiation. It does **not** derive the reference, the relative pairing condition, or the interaction from zero alone. The same symmetries also permit an alternative, frozen history. Thus the earlier no-go is overcome in a larger relational model, not refuted as a theorem about the smaller closed sector.

Executable checks: [verification/zero_covariant_pairing_reference_history_test.py](verification/zero_covariant_pairing_reference_history_test.py).

**Minimal-reference continuation:** [minimal invariant reference and a constrained Hamiltonian](ZERO_MINIMAL_INVARIANT_REFERENCE_DYNAMICS.md) proves a four-state lower bound for this invariant-sector architecture, constructs a reference attaining it, and derives the interaction up to scale from explicit symmetry, flip and reality conditions.

## 1. The zero sector and the reference

Let the four abstract spin-half factors be ordered `B,L,M,N`, with L the encoded logical qubit of the previous construction. The two-dimensional spin-zero space is

```text
V = ker(σ_B+σ_L+σ_M+σ_N) in each of x, y, z.
```

The earlier complementary conditions define a two-dimensional logical kernel K. The verifier explicitly embeds the four abstract spins into `B ⊗ (R,W,T,F) ⊗ M ⊗ N`, with L inside K. Every vector under this embedding is annihilated by `C₁,C₂,C₃` and has `L=S=+1`. Therefore every spin/reference branch used below keeps the **same** prior complementary zeros. To avoid a naming collision, the capital L in `B,L,M,N` denotes the logical factor; the earlier constraint `L=+1` is the operator defined in the prior reports.

Let `G=S₄`, acting by permutation `U(g)` on the four spins. Introduce a 24-dimensional reference A (distinct from the earlier internal reference F) with orthonormal states `|g⟩_A` and left regular action

```text
L(k)|g⟩ = |kg⟩,       D(k)=L(k) ⊗ U(k).
```

The reference is an internal quantum factor, not an external observer or spatial frame. The spin permutation representation and the regular reference are **stipulated**. Full simultaneous SU(2) rotations also act, but leave all vectors in V invariant.

Start with the fiducial spin singlets

```text
|s⟩_BL |s⟩_MN = |ψ₀⟩,
|Ψ₀⟩ = (1/√24) Σ_g |g⟩_A U(g)|ψ₀⟩.
```

Although a labeling appears in the formula, the complete state obeys `D(k)|Ψ₀⟩=|Ψ₀⟩` for every k. This is a coherent vector, not a classical mixture of selected pairings. The frame labels have equal Born weights in this constructed state, but they are not automatically distinct actual worlds or subjects: the 24 labels describe only **three** physical pair matchings, each represented eight times. No incidence measure follows from their count.

The state has frame–spin Schmidt rank 2 and entropy 1 bit. Tracing out A gives

```text
ρ_spin = P₀/2,
```

where `P₀` is the projector onto V. Thus the invariant mixed state found previously occurs as the spin reduction of an explicit pure whole.

## 2. A symmetric but genuinely relational Hamiltonian

Take the fiducial exchange `h=Swap_LM` and define its covariant controlled extension:

```text
H = Σ_g |g⟩⟨g|_A ⊗ U(g) h U(g)†.
```

`H²=I`, and `H` commutes with every `D(k)` and with simultaneous spin rotations. The time parameter below is a phase of an internal clock, not external fundamental time. The conditional state is

```text
|Ψ(θ)⟩ = (cos θ I − i sin θ H)|Ψ₀⟩.
```

This remains permutation-invariant and spin-zero for every θ. Nonetheless, the joint frame–spin state changes. Define two **invariant** relational triplet projectors,

```text
Q_pair   = Σ_g |g⟩⟨g| ⊗ U(g) Q_BL U(g)†,
Q_target = Σ_g |g⟩⟨g| ⊗ U(g) Q_BM U(g)†,
Q_ab = [3I + σ_a·σ_b]/4.
```

Each asks a question about the pair designated by the internal reference. They commute with simultaneous permutations and rotations; neither needs an external absolute label. Direct calculation gives

```text
⟨Q_pair⟩_θ   = (3/4) sin² θ,
⟨Q_target⟩_θ = (3/4) cos² θ.
```

At θ=0, the frame-designated B–L pair is a singlet. At θ=`π/2`, the designated B–M pair is a singlet. In contrast, `ρ_spin=P₀/2` **at all θ**. Without access to the reference, the spin-only density operator does not reveal the change; the change is in an invariant relational observable of the larger whole. This is not merely an externally described relabeling: the specified fixed joint observables have different expectation values at different clock readings. Whether those observables are physically accessible remains an additional question.

For a common-axis B–M readout in a frame, rotational invariance gives

```text
P(opposite | θ) = 1 − (2/3)⟨Q_target⟩_θ
                = [1 + sin² θ]/2.
```

At θ=`π/2` this probability is 1. With a finite window centered there and half-width `π/8`, its probability is `1/4`; the window-conditioned opposite-outcome probability is approximately `0.975079`, corresponding to `0.831757` bits of mutual information. The comparison presupposes an available common-axis readout and the stated joint reference interface. It is a reversible Born-statistical correlation, not an established actual record, subject or conscious experience.

## 3. A stationary whole with a unique zero eigenstate

Add a neutral two-level clock C, and define on the restricted spin-zero space

```text
W = |+⟩_C (I+H)/2 + |−⟩_C (I−H)/2,
𝒞 = H − Z_C,
P_G = (1/24) Σ_k D(k),
H_whole = 𝒞²/4 + (I−P_G) + W Q_pair W†.
```

`W†W=I`, `𝒞W=0`; the three terms are commuting positive projectors. `P_G` projects onto the simultaneous-permutation-invariant subspace, which has dimension **two** before imposing the relational pairing condition. The common kernel of `I−P_G` and `Q_pair` is one-dimensional. Consequently `H_whole` has one zero eigenvector, `W|Ψ₀⟩`, with gap 1 in the chosen units. The phase POVM gives the conditional histories above with a uniform phase density on `[0,π)`.

The verifier carries out the matrix calculation on the 48-dimensional reference⊗V space and its 96-dimensional clock extension. On the full four-spin space one can additionally impose `I−P₀`; the permutation, pairing and exchange operators preserve V, as separately checked. The exact complementary-zero embedding described in section 1 is likewise checked. The construction does not assert that the auxiliary clock or reference has a derived physical energy cost, or that this positive constraint is objective whole energy.

The reference eliminates an **absolute** pairing preference: all group-transformed pairings occur and the condition is invariant. It does not eliminate the **relative** condition that the frame-designated B–L pair is initially singlet. Nor is the initial clock-phase relation derived. The full invariant subspace before that condition has dimension two, so permutation symmetry and spin zero do not alone choose this particular invariant vector.

## 4. Why the original freezing result still matters

In the four-spin-only zero sector, every permutation-invariant Hamiltonian is proportional to the identity. Here the Hamiltonian is not invariant under spin permutations **alone**: its control reference transforms too. The total joint Hamiltonian is invariant under the combined action. There is no contradiction; the reference supplies a relational degree of freedom on which invariant observables can vary.

This does not by itself establish that zero fixes the dynamics. Replace the fiducial `Swap_LM` by `Swap_BL`, and apply exactly the same group-controlled construction. It has the same symmetry, the same squared Hamiltonian `I`, the same spin-zero and relational pairing condition, and a unique stationary zero eigenstate. But the fiducial singlet is an eigenstate of this second exchange, so the resulting relational pairing history is frozen. In particular, `⟨Q_target⟩` remains `3/4` rather than falling to zero. Both alternatives satisfy the displayed constraints; one cannot deduce record transfer from permutation invariance and zero alone.

Likewise, covariance does not derive the 24-state regular reference or its transformation rule. A different reference, pair condition or covariant coupling may give another admissible history. The original old-environment encoding of B is state-dependent and may be nonlocal; operations on that encoding have not been shown to preserve all the old laboratory or clock charges. No claim is made that the old all-sector history is unchanged by these new reference-controlled operations.

## 5. Significance for the zero program

The concrete progress is that **undifferentiated global symmetry and changing internal relations are compatible**, provided the reference participates in the symmetry. This makes the plenitude idea mathematically actionable: the whole can retain a coherent orbit of pairings rather than choose one absolute pairing, while a comparison internal to the whole exhibits a record transfer.

The construction still assumes the group, representations, reference, relative pair condition and exchange. It does not prove that all genuine possibilities are actual, provide their incidence weights, derive objective cosmological energy, or identify a physical opposite with an opposite felt valence. A signed global balance would not erase an individual's suffering. These are not solved by the new invariant correlations.

A substantive next step is to ask whether the reference and its relative condition can themselves arise from the same zero principle—e.g. by deriving a necessary representation or a unique relational constraint, while keeping enough invariant multiplicity for nontrivial dynamics. The frozen alternative above gives a direct benchmark for any such proposal.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_covariant_pairing_reference_history_test \
  verification.zero_isotropic_singlet_history_test \
  verification.zero_stationary_whole_unique_history_test -v
```

The nine new tests check all 24 group elements, the singlet embedding into the prior complementary-zero kernel, invariant controlled operators, the unique stationary zero, clock conditioning and finite-window correlations, the unchanged spin reduction, the frozen symmetric alternative and the eightfold reference-label redundancy. NumPy is required.
