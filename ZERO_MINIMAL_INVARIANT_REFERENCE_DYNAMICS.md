# Minimal invariant reference and a constrained Hamiltonian

## Result

The previous [permutation-covariant history](ZERO_COVARIANT_PLENITUDE_REFERENCE_HISTORY.md) used a 24-state group reference and stipulated a controlled exchange. This round makes the construction substantially smaller and derives the interaction from explicit structural requirements:

1. The four-spin zero sector is a two-dimensional irreducible representation V of the permutation group. For a **changing invariant state** in that sector, a reference of dimension at least **four** is necessary under the stated assumptions; a four-state reference suffices.
2. On a specified parity-reference × spin-zero factor, permutation invariance, parity flipping, Hermiticity and a specified real structure determine the Hamiltonian **up to one real scale**:

   ```text
   H = λ Y_P Y_V.
   ```

3. This H gives a unique stationary zero-eigenstate under specified invariant constraints. Its relational record changes while the whole stays permutation-invariant and the prior complementary zeros remain satisfied. At one clock reading, a reference bit and a reference–spin correlation share **one bit** of mutual information. Their perfect correlation also survives when the clock is ignored.

The assumptions do significant work: in particular, parity-flipping excludes a frozen Hamiltonian, and the real structure is supplied rather than derived from zero. This is a conditional derivation and minimality theorem, **not** a completed derivation of physics or experience from zero.

Verifier: [verification/zero_minimal_symmetry_reference_record_test.py](verification/zero_minimal_symmetry_reference_record_test.py). It builds directly on the [full embedding and group tests](verification/zero_covariant_pairing_reference_history_test.py).

## 1. Why four reference states are minimal here

The total-spin-zero subspace V of four spin halves has dimension two. Permutations act on it as the real irreducible `S₄` representation of type `[2,2]`; call this action D. The tests verify its irreducibility by calculating its commutant. It is the same V that was embedded in the earlier `C₁=C₂=C₃=0`, `L=S=+1` logical sector.

For a finite-dimensional unitary reference representation A,

```text
(A ⊗ V)^G ≅ Hom_G(V*, A).
```

Its dimension is the multiplicity of V* in A. A symmetry-preserving unitary can change a pure invariant state by more than an overall phase only if this invariant subspace has dimension at least two. Since `dim V*=2`, that requires

```text
multiplicity(V* in A) ≥ 2,       dim A ≥ 4.
```

This is a **lower bound within the fixed spin-zero sector and simultaneous-permutation invariance**, not a claim about all theories or all reference architectures. If a clock or another system also carries the group representation, its degrees of freedom must be included in A for the bound. An unobserved changing state need not be an operationally accessible record.

The bound is attained by

```text
A = R ⊗ P,        dim R = dim P = 2,
D_A(g) = D(g)* ⊗ X_P^parity(g).
```

Here `X_P^0=I` for even permutations and `X_P^1=X_P` for odd ones. Equivalently, P contains a trivial and a sign representation. Because `D⊗sign` is equivalent to D for this representation, A contains two copies of V*. The joint invariant space `(A⊗V)^G` has dimension **two**. This replaces the prior 24-dimensional regular reference with four states, though the new clock remains an additional two-state system.

## 2. A symmetry-constrained interaction

Fix a real orthonormal basis for V, so all D(g) are real orthogonal. Let `X_V,Y_V,Z_V` be Pauli matrices in that basis. For the parity factor use `X_P,Y_P,Z_P`. Odd permutations conjugate X_P into itself and reverse Y_P and Z_P; on V, `Y_V` also reverses sign under an odd permutation. Consequently

```text
H = λ Y_P Y_V
```

is invariant under the simultaneous group action. It is Hermitian, real in the stated basis, anticommutes with X_P, and acts only on P and V—not on R. For `λ≠0`, choose units in which `|λ|=1`; the sign and physical scale are not determined by these conditions.

More is true than the existence of this example. The verifier expands a **general Hermitian 4×4 operator on P⊗V** in the 16 Pauli products and imposes:

1. Invariance under all simultaneous permutation actions on P⊗V.
2. Anticommutation with `X_P`—the interaction flips the parity-reference observable.
3. Reality under the chosen conjugation K, `K H K⁻¹=H`.

The real solution space is **one-dimensional**, spanned by `Y_P Y_V`. Without condition 3 it is two-dimensional, additionally allowing `Z_P Y_V`. This is a conditional uniqueness result, not uniqueness under symmetry alone. It is basis-independent only when the antiunitary K is transformed together with the representation; imposing that physical real structure is an extra assumption. Nor have we derived the restriction that H act on P⊗V without coupling to R or other factors. The zero Hamiltonian obeys the homogeneous constraints, and the requirement of a nonzero coupling remains additional.

The control `H_frozen=X_P` is real and invariant but does **not** anticommute with X_P; it leaves the initial state below unchanged up to phase. Hence symmetry and reality by themselves do not choose a changing history. The parity-flipping requirement is the explicit point where the demand for this form of change enters.

## 3. The invariant state and its relational record

Let `|0⟩,|1⟩` be any orthonormal basis of V and let R carry the conjugate basis. Set

```text
|Φ⟩_RV = (|0*⟩_R|0⟩_V + |1*⟩_R|1⟩_V)/√2,
|ψ₀⟩ = |Φ⟩_RV ⊗ |+⟩_P,       X_P|+⟩=|+⟩.
```

The canonical vector `|Φ⟩` is invariant under `D*⊗D`, and `|+⟩_P` is invariant under the parity action. The vector is therefore invariant under the full simultaneous permutation action. It is selected, up to phase, by that invariance together with the **additional** `X_P=+1` condition. Although the + state is the trivial component of P's representation, requiring that component initially is still a relative constraint; it is not derived from zero.

For normalized phase θ let

```text
|ψ(θ)⟩ = exp(−iθ H)|ψ₀⟩,       H=Y_P Y_V.
```

The entire state remains invariant. The reduced V state remains `I/2`; internal change occurs in correlations. Introduce two commuting invariant readouts:

```text
Q_P    = (I−X_P)/2,
Q_corr = I − |Φ⟩⟨Φ|_RV.
```

`Q_P` is a parity-reference bit. `Q_corr` tests whether the R–V correlation has changed from the canonical one; it is a **joint** observable, not a local observable on the four-spin system alone. Their joint Born table at phase θ is exactly

```text
                       Q_corr=0     Q_corr=1
Q_P=0                    cos²θ          0
Q_P=1                       0          sin²θ.
```

At `θ=π/4` this is a perfectly correlated unbiased bit, with **1 bit mutual information**. At θ=0 it is `00`; at θ=`π/2` it is `11`. At θ=`π` the initial vector returns up to phase, so the memory is not permanent.

These are mathematical quantum readouts. `Q_corr` requires a joint R–V interface, whose physical locality, availability to a confined observer, and material resources are not established. A correlated bit is not by itself a subject, actual incidence, or felt valence.

## 4. One stationary zero-eigenstate, including the unselected clock

For `H²=I`, define a two-level neutral clock and isometry

```text
W = |+⟩_C (I+H)/2 + |−⟩_C (I−H)/2,
𝒞 = H − Z_C,              P_G = (1/24) Σ_g D_A(g)⊗D(g),
H_whole = 𝒞²/4 + (I−P_G) + W Q_P W†.
```

`W†W=I` and `𝒞W=0`. The three terms of `H_whole` are commuting positive projectors. Their common kernel is **one-dimensional**, spanned by `W|ψ₀⟩`; the gap is 1 for the displayed unit coefficients. The full state is permutation invariant, and its spin V component embeds in the prior common-zero sector. The clock's phase POVM gives `|ψ(θ)⟩` with uniform density on `[0,π)`.

An additional result is visible without selecting a clock phase. Trace out C and measure `Q_P,Q_corr` jointly. The table is

```text
[[1/2, 0], [0, 1/2]].
```

Thus the unselected state retains **one bit of mutual information** between the two specified invariant readouts, unlike the single readout in the earlier periodic example whose full-cycle average erased its correlation. This does not mean it records the precise clock phase, nor does it imply an irreversible or permanent memory. `H_whole` is a constraint operator, not a demonstrated objective cosmological energy.

## 5. What is and is not forced by zero

The gain is a dependency reduction: the 24-state reference becomes the minimal four-state reference for this invariant-sector architecture, and the Hamiltonian is no longer arbitrary **once** the four displayed interaction requirements are granted. The permanent limitations are equally concrete:

- The representation, factorization and real structure are supplied. Minimality given a chosen symmetry is not a derivation of that symmetry from zero.
- Parity flipping is a demand for this kind of change; symmetry alone still admits frozen dynamics. The sign and scale of λ and the clock relation remain undetermined.
- The original work/reference sector is carried by an exact encoding, but the new reference and interaction have not been realized locally or shown to preserve every original laboratory charge. No subjective interface is assumed.
- Equal correlations, spin opposites and invariant states do not establish actual subjects, their measure or oppositely signed felt experience. A global signed sum would not make an individual's suffering unreal.

The next meaningful challenge is to derive, rather than stipulate, the parity-flipping and real-structure conditions—or to show that a stronger plenitude principle makes their alternatives complementary parts of a single invariant whole. Any proposed answer can now be tested against the explicit frozen control and the minimal-reference theorem.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_minimal_symmetry_reference_record_test \
  verification.zero_covariant_pairing_reference_history_test \
  verification.zero_isotropic_singlet_history_test -v
```

The six new tests check the invariant-space dimension, irreducibility, the full 16-Pauli interaction solve, unique stationary kernel, exact conditional and unselected record tables, the alternative allowed when reality is dropped, and the frozen control. NumPy is required.
