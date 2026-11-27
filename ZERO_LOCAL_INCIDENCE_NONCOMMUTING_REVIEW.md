# Recheck: noncommuting incidence and current allocation

## Scope and result

This pass independently examines selected algebraic claims in [local incidence and a conserved quantum current](ZERO_LOCAL_INCIDENCE_QUANTUM_CURRENT_CONSTRUCTION.md). That document supplies a sufficient commuting construction and a counterexample to a sharp, mutually exclusive support split; it does **not** claim noncommuting incidence always makes allocation impossible. We strengthen both sides: an exact operator-norm distance for the exclusive case, and a necessary-and-sufficient solvability condition for arbitrary finite-dimensional overlapping projections, with an explicit noncommuting allocation that succeeds.

The current research framework treats space and time as non-fundamental constructs and experience as intrinsic. The finite operators below are an effective mathematical test: neither a local projection nor a current is thereby a subject, experience, or the physical energy of the whole. Locality means membership in a **declared** effective local algebra, not an assumption that spacetime is fundamental. This is a bounded structural result, not a resolution of the physical–experiential constitution.

## 1. Exact obstruction and optimal approximation for exclusive supports

Let P be an orthogonal projection, Q=I−P, and J a bounded Hermitian operator on a finite Hilbert space. Two Hermitian operators `V_P=P V_P P` and `V_Q=Q V_Q Q` sum to J **iff** `[J,P]=0`: their sum is block diagonal; conversely, if J commutes with P, choose `V_P=PJP` and `V_Q=QJQ`.

More strongly,

    inf_(B=B†, [B,P]=0) ||J−B|| = ||P J Q||.

For any block-diagonal B and `U=2P−I`,

    (J−UJU)/2 = (J−B−U(J−B)U)/2,

so the norm of this off-diagonal part is at most `||J−B||`. Its block form `[[0,PJQ],[QJP,0]]` has norm `||PJQ||`. Equality is achieved by `B=PJP+QJQ`. This is an exact distance, not just a visual observation that a matrix is off-diagonal.

For the original two-site single-excitation example, `P=|0⟩⟨0|`, `Q=|1⟩⟨1|`, and `J=2Y`. Then `||PJQ||=2`; even the **best** exact support-preserving split has operator-norm error 2. For the symmetric assignment `{P,J}/2` and `{Q,J}/2`, each equals `J/2` and their sum is J, but neither is supported in its named sector. In the P-absent state `|1⟩`, the first operator has mean 0 and variance 1: zero mean does not imply a zero-valued sharp record.

This result concerns the full stated Hilbert space and operator norm; an approximate claim restricted to a smaller physically admissible sector or states may have a different error. It does not rule out unsharp or overlapping incidence models.

## 2. General finite-dimensional criterion for overlapping supports

Let `P₁,…,P_n` be arbitrary projections on a finite-dimensional Hilbert space; they need not commute or be orthogonal. Define the real vector space of admissible signed Hermitian contributions

    V_s=P_s V_s P_s,          J=Σ_s V_s.

Positive incidence weights `a_s>0` can be absorbed into the respective V_s without changing solvability. Define the linear map L taking the tuple of supported Hermitian operators to their sum. With the real Hilbert–Schmidt inner product `⟨A,B⟩=Tr(AB)`,

    L*(B)=(P₁BP₁,…,P_nBP_n).

Finite-dimensional linear algebra gives the **iff** condition

    J is a supported sum  ⇔  Tr(BJ)=0 for every Hermitian B
                              with P_s B P_s=0 for every s.

Necessity follows by cyclicity of trace. Sufficiency follows from `im L=(ker L*)⊥`; finite dimensionality ensures the image is closed. This is a practical obstruction/feasibility test even when the projections overlap or do not commute. It does not assert positive V_s, a unique decomposition, local accessibility, quantum instruments, or experiential identity. If locality is required, the entire criterion must be applied within the **specified local algebra** and its admissible supported operator spaces; a globally existing split may fail that further requirement.

## 3. A noncommuting overlap that succeeds

On one qubit set

    P=|0⟩⟨0|=(I+Z)/2,       R=|+⟩⟨+|=(I+X)/2,
    J=P−R=(Z−X)/2,          V_P=P,       V_R=−R.

Here `[P,R]≠0`, `[J,P]≠0`, and `[J,R]≠0`, yet `V_P=PV_PP`, `V_R=RV_RR`, and `V_P+V_R=J` exactly. Hence the commutation assumptions in the original local allocation theorem are sufficient for its particular inverse-based construction, **not necessary for every supported signed decomposition**. The two subspaces overlap in the sense of nonorthogonality; their range intersection is zero because both are distinct one-dimensional subspaces. Do not confuse nonorthogonal projectors with a nontrivial common vector.

This example can even represent an energy *rate* in a specified finite Hamiltonian model. With `E=(I+(X+Z)/√2)/2` and `H=Y/√2`, the standard Heisenberg expression gives

    i[H,E]=(Z−X)/2=J,        i[H,I−E]=−J.

Thus the two effective energy-rate operators sum to zero, but the example still supplies neither an actual incidence law nor an identification of its signed operators with experiential qualities. It does not prove a total physical-energy zero; it is exchange-rate conservation in a prescribed model.

## 4. Verification and limits

[Tests](verification/zero_local_incidence_noncommuting_review_test.py) verify the exact norm optimum, a basis of the finite-dimensional image/orthogonal obstruction, the supported noncommuting decomposition, and the Hamiltonian energy-rate identity. They check examples, while the iff condition and norm bound follow from the proofs above. Future work should test the **actual** proposed incidence operators and current within a common physical model, with a stated locality algebra and subject-incidence interpretation; do not infer that a formal projection or sum is felt.
