# Page–Wootters (1983), stationary observables, and the sphere echo

**Source:** Don N. Page and William K. Wootters, “Evolution without evolution: Dynamics described by stationary observables,” *Physical Review D* **27**, 2885–2892 (1983), [doi:10.1103/PhysRevD.27.2885](https://doi.org/10.1103/PhysRevD.27.2885). The user's [original eight-page PDF](sources/uploads/page1983.pdf) is preserved unchanged: SHA-256 `320bca34918426b2d0e736baadba25e06999cf7feeb3138d5b94597b97b7df62`. Page numbers below refer to the journal pagination. The calculations in this report are checked by [the verifier](verification/zero_page_wootters_original_sphere_connection_test.py).

## Bottom line

This is the original Page–Wootters paper, not a new discovery that time can be relational. Its important contribution to our present work is more specific: **a dynamical correlation can itself be represented by an observable commuting with the whole's evolution**. Applying that idea to the existing 20-step sphere echo gives a pair of stationary joint observables for the pre- and post-echo sphere signs. They commute, yet their exact joint distribution records a genuine change in half the ensemble.

That result makes the connection between our coherent whole, internal change and the actual sphere program mathematically sharper. It does not require an external time or an unrecorded collapse. It also does not make an inaccessible joint observable available to a confined inhabitant, establish felt duration, derive the program from zero, or show that a constructed clock constraint is objective cosmic energy.

The paper's own examples also show why a stationary whole is not the same as an empty or uncorrelated whole: averaging the **joint** clock–system observable retains correlations that are lost if each factor is averaged separately. We reproduce that effect and the authors' finite-spin result below.

## 1. What Page and Wootters actually argue

On pp. 2885–2886 the authors propose that an external translation of the coordinate time of an entire isolated system cannot be observed from inside it. They discuss the possibility of an energy superselection rule, including an analogy with long-range gravitational fields. They explicitly acknowledge that a rigorous gravity-based demonstration is lacking. Treat the restriction to stationary observables as a **scope and physical proposal**, not a general theorem that every isolated quantum system must be stationary or that all conceivable measurements commute with a chosen Hamiltonian.

Their constructive question is: if a closed system is stationary, how can one describe observable change? Their answer is by **correlations between an internal clock and other variables**, expressed with stationary operators. In the spin example on pp. 2886–2888, the clock is one precessing spin and the system is another. They time-average joint projection operators, calculate conditional probabilities, and note that repeated measurements of the same clock need not be nondisturbing.

On pp. 2889–2890 they give the general conditional expectation, with an averaged numerator and denominator, and analyze an idealized noninteracting clock/rest decomposition. Under a stationary joint state and their specified clock states, conditional expectations of the rest have the familiar clock-time dependence. They explicitly recognize that realistic clocks interact with what reads them; the simple noninteracting analysis need not apply without modification. On pp. 2890–2891 they distinguish an entropy arrow defined relative to clock variables from an external coordinate-time assertion. They do **not** derive a universally irreversible arrow or a theory of conscious experience.

The authors also note that an observer in a closed system cannot read a clock outside that system (p. 2886). This is directly relevant to our standing realm distinction: a global correlation is not, by itself, a confined subject's access to it.

## 2. Why averaging the joint observable matters

Take two spin-`1/2` systems, each initially in `|+x⟩`, with equal precession and `H∝Z_1+Z_2`. Let `P_1` and `P_2` be their respective `+x` projectors, and `Ω` be averaging over the common time translation. Then

`Ω(P_1) = I/2`, `Ω(P_2) = I/2`, but `Ω(P_1P_2) ≠ Ω(P_1)Ω(P_2)`.

The averaged **joint** observable retains coherence within the degenerate total-energy sector. In the initial product state,

`⟨Ω(P_1)⟩=1/2`, `⟨Ω(P_1P_2)⟩=3/8`,

so the conditional probability of `+x` on the second spin given `+x` on the first is `3/4`. Multiplying the two separately averaged projectors would incorrectly give `1/2`. This is a concrete reason that global stationarity or vanishing one-spin time averages do **not** imply absence of relational information.

The verifier also checks the paper's exact spin-`j` formula (its Eq. 15) for `j=1/2,1,3/2,2,3,4`:

`P(J_2x=j | J_1x=j) = ∏[l=1..2j] (1 − 1/(4l−2)²)`.

For example, this is `3/4` at `j=1/2` and `35/48` at `j=1`. Its large-`j` limit is `1/√2`, **not 1**. The authors' conditional mean, by contrast, is `E(J_2x | J_1x=j)=2j²/(2j+1)`, so its fraction of `j` tends to one. These are different statements: a macroscopic relative orientation becomes sharply aligned in relative terms even though the probability of the *exact maximum eigenvalue* need not approach one. The model is a periodic spin clock, not an ideal unlimited clock or a consciousness model.

## 3. A precise stationary observable for the existing sphere clock

The [actual sphere program](ZERO_SPHERE_LOCAL_CONSTITUTION_AND_RESERVOIR_ECHO.md) has 20 operations `G_0,…,G_19`, prefixes `U_t`, and `U_20=I`. The coherent history state and controlled cyclic shift are

`|H⟩ = (1/√20) Σ[t=0..19] |t⟩ U_t|ψ⟩`,

`W (|t⟩|φ⟩) = |t+1 mod 20⟩ G_t|φ⟩`.

Then `W²⁰=I` and `W|H⟩=|H⟩`. This program already existed; the following is a new way to extract its relational content, not a new fundamental foliation. Let `Π_t=|t⟩⟨t|` and define the cyclic average

`Ω_W(X) = (1/20) Σ[k=0..19] W^k X W^(−k)`.

For a system effect `A` anchored at reading `t`, define

`R_t(A) = 20 Ω_W(Π_t ⊗ A)`

`= Σ[n=0..19] |n⟩⟨n| ⊗ U_n U_t† A U_t U_n†`.

It obeys `[R_t(A),W]=0`, and for the normalized stationary history,

`⟨H|R_t(A)|H⟩ = ⟨ψ|U_t† A U_t|ψ⟩`.

Thus the expectation normally described as “effect A at clock reading t” is the expectation of one **stationary relational observable**. If one introduces the constructed constraint `H_clock=I−(W+W†)/2`, the same observable commutes with it and the history has eigenvalue zero. That constructed constraint is not automatically the universe's objective total energy.

There is a useful caution in the same calculation:

`Ω_W(Π_t⊗I) = I/20`.

Averaging the bare absolute clock projector loses its label: it is not a physical measurement that the universe has an externally selected tick `t`. `R_t(A)` retains a **specified clock–system relation**, with the clock origin, factorization, gate sequence and meaning of `t` supplied by the model. Implementing this generally joint, clock-conditioned observable is a separate physical question. The derivation does not establish that a confined subject can access it, that `t` is a lived present, or that the sequence has been generated by zero's constitution.

### The flag and stationary reductions fit together

The existing reference flag `P_a` commutes with every `G_t` and therefore with `W`. Its pinching map `Δ_F` consequently commutes with `Ω_W`. The Page–Wootters translation average and our [flag-compatible incidence reduction](ZERO_FLAG_RECORD_INCIDENCE_AND_PHYSICAL_READOUT.md) are **different** operations, but in this program they can be applied in either order. The first implements the chosen global cyclic invariance; the second restricts to the chosen sharp-flag algebra. Neither identifies the type with a subject, and neither licenses replacing a joint correlation by a product of separately averaged factors.

## 4. Pre- and post-echo change as one stationary joint distribution

Let `J=Z_j` be the existing sphere sign, let `B=±1` be the conserved old sphere sector, and let `E=TQT` be the actual echo operation on the valid sector. The previously verified operator identity is

`E† J E = B J`.

The forward reservoir operations commute with the old `J` and `B`. Thus the pulled-back observables for `J` at tick 7 and tick 10 are respectively `J` and `BJ`. They commute on the valid sector, so the corresponding stationary relational observables `R_7(J)` and `R_10(J)` have a joint projector there. The actual old-history quantum amplitudes, checked for all 16 original clock labels, yield:

| Pre-echo `J_7` | Post-echo `J_10` | Born weight |
|---:|---:|---:|
| +1 | +1 | 1/2 |
| +1 | −1 | 1/4 |
| −1 | +1 | 1/4 |
| −1 | −1 | 0 |

Hence `P(J_7≠J_10)=1/2`, while `⟨R_7(J)R_10(J)⟩=⟨B⟩=0`. The global history remains stationary. This is not a claim that the same value changes *at the same clock relation*; the two signs are relational values at distinct specified readings. Nor does it postulate an unobserved classical trajectory: these two transported operators commute, and their joint effects are mathematically well-defined. A real joint readout or first-person report would require an actual suitable interface and may alter the subsequent evolution.

The verifier checks the genuine old sphere quantum histories and the exact `TQT` operator relation. Separately, it builds a dense 20-clock **reduced B–j–echo label model**, checks the group-average formula and the table there, and verifies stationarity. That reduced model is not represented as a dense reconstruction of all original source, reservoir, purifier and old-sphere amplitudes; the full-program conclusion uses the algebraic prefix identities and the independently verified actual sphere dynamics.

## 5. What “zero-energy whole” does and does not follow

On p. 2889 Page and Wootters explicitly construct a larger pure **zero-energy eigenstate** in which a subsystem's energy is anticorrelated with another subsystem's energy. We independently checked a finite spin-`1/2` analogue: the two-spin energy sectors `+1,0,−1` are paired with reference energies `−1,0,+1`, respectively. The total state has zero constructed energy, while the reduced two-spin state is the energy-dephased mixture and retains the clock–system correlation above. The opposite spectrum and joint state are part of this model's input.

This is a concrete example of a zero **sum** containing nonzero subsystem contributions, with a pure correlated whole and a mixed restriction. It is not a derivation that the actual universe has this Hamiltonian, an asymptotically defined energy of zero, an opposite-energy partner for every system, or that physical energy equals a signed experiential quantity. The paper assumes an asymptotically flat setting for one discussion and explicitly presents it as a consistent model rather than an established cosmology.

The paper also discusses describing observations using an energy eigenstate. A stationary mixture and a pure eigenstate of the **same** Hamiltonian are not generally identical on all stationary observables: for example, an energy projector distinguishes their probabilities if they have different energy weights. The paper's finite-observer discussion and its construction of a larger pure eigenstate are narrower claims. In the enlarged construction, the state, reference system and accessible algebra have changed; one should not replace every mixed stationary state by a pure zero-energy state without specifying this extension.

## 6. What the paper strengthens in the one-reality program

* **One whole and internal differentiation:** a single pure stationary state can encode nontrivial relational correlations; whole-level stationarity does not make local relations nonexistent. It does not show why a bare zero or point must possess the particular sphere and state.
* **Relational time:** the sphere echo's pre/post relation can be expressed by commuting-with-constraint observables. This sharpens, rather than newly invents, the familiar relational-time idea.
* **Incidence and balance:** the conserved flag and the stationary averaging are compatible in this model, while the prior conditional signed-balance results continue to apply. Page and Wootters supply neither the flag-to-subject identity nor felt valence, nor an independent subject-counting rule.
* **Reality of local suffering:** if a signed candidate were genuinely felt, a whole-level zero or counterpart balance would not make its local negative contribution absent. The physical calculation does not establish that identification or that positive feeling literally erases suffering.
* **Access and arrows:** a stationary joint observable can exist without being accessible inside a given realm; clock readout, memory, finite resources, thermodynamic direction and experience remain distinguishable questions.

The strongest new consequence here is the explicit **stationary pre/post sphere-echo joint distribution**. The decisive no-residue task is still to connect the physical relation, the actual subject and its intrinsic quality by the constitution of the one whole, not to relabel a formal clock constraint as the answer.
