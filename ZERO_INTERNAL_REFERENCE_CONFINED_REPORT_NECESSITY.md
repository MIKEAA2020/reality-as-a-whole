# A reference from the paired state, and what a confined subject could report

## Result in the larger program

The proposal is that one self-sufficient, internally differentiated zero whole determines physical organization, genuine subjectivity, their relation and incidence, without an unexplained external selection. A meaningful next step is to stop introducing the geometrical reference, record, and observer as independent pictures and ask whether they can be extracted from the **same actual model state and dynamics**.

This calculation advances that connection in three ways:

1. In the noncommuting complement's paired-qubit sector, the reference \(N=I\) used in the sphere–Lorentz calculation is **twice the transpose of the pre-measurement reduced state of the other lab**, not a reference defined as the average of the chosen outcomes. The directional zero then follows from the same state's complete measurement and no-signalling.
2. The other lab does not automatically possess Alice's setting label. Even granting it unrestricted access to its own quantum multiplicity system, its optimal single-copy ability to infer the sign of Alice's reference-relative direction is strictly below certainty. The actual record–target readout is still less informative.
3. The simple work-sign readout \(j\), used as a candidate felt sign in the previous synthesis, is not neutral under two of the later reference's three exact orientation constraints. Its straightforward sharp, nondemolition copy to a neutral pointer leaves the common-zero sector. A more sophisticated charged or invariant relational report is a separate construction, not automatically forbidden.

These results do **not** derive a subject or what is felt. They identify how an actual physical reference can arise from the same stipulated paired state, and precisely where a proposed first-person interface must do additional work. The verifier is [`verification/zero_internal_reference_subject_report_test.py`](verification/zero_internal_reference_subject_report_test.py). It imports the physical complement instruments and clock/record circuit from [`ZERO_NONCOMMUTING_COMPLEMENT_SPHERE_HISTORY.md`](ZERO_NONCOMMUTING_COMPLEMENT_SPHERE_HISTORY.md), and the covariant and experiential candidates from [`ZERO_COVARIANT_REFERENCE_PHYSICS_EXPERIENCE_SYNTHESIS.md`](ZERO_COVARIANT_REFERENCE_PHYSICS_EXPERIENCE_SYNTHESIS.md).

## 1. The reference need not be defined from the measured directions

In the paired-qubit part of the existing complement, each equivalent-copy pair has the actual input

\[
 |\Phi_2\rangle=(|00\rangle+|11\rangle)/\sqrt2
\]

in Alice's logical basis and Bob's conjugate physical basis, with an independent paired irrep spectator. Therefore, **before** Alice's sphere measurement, Bob's logical reduced state is

\[
 \rho_B=I/2,\qquad N_B=2\rho_B^T=I.
\]

The transpose accounts for the chosen paired-state basis. It is not a claim that transpose is a physical time reversal. This reference is fixed here by the stipulated input state, independently of which complete Alice POVM is subsequently chosen.

For the original effects \(E_i=q_i(I+n_i\cdot\sigma)\), the actual unnormalized state conditioned on Alice's outcome is

\[
 \widetilde\rho_{B|i}=E_i^T/2,\qquad
 p_i=\operatorname{tr}\widetilde\rho_{B|i}=q_i,\qquad
 K_i=2\rho_{B|i}^T=I+n_i\cdot\sigma.
\]

Consequently

\[
 \sum_i q_iK_i=2\rho_B^T=N_B,
 \qquad\sum_iq_i(K_i-N_B)=0.
\]

This is no longer circularly **defining** the reference by the outcome average: the reference came from the original paired state. The equality is a physical ensemble relation because the complete Alice measurement, when its result is ignored, cannot change Bob's reduced state. The verifier calculates it directly from the earlier Kraus matrices. It also checks the reduced state after Bob's actual unselected measurement; the later record/work operations act on other factors, and the old clock references in these complement blocks begin independently of the logical multiplicity pair.

In particular, when the three prior directions are independently fixed, their linear independence and the state-derived reference uniquely determine \(q=(1/8,2/5,19/40)\). But **neither the paired input nor that choice of directions has been derived from zero**. The same \(\rho_B=I/2\) supports a different complete equilateral three-direction instrument with weights \(1/3,1/3,1/3\). The state thus gives a non-circular *reference*, not a unique measurement, ontology, or incidence measure. Its invariance under the unread measurement is a standard no-signalling identity, not evidence of subjective awareness.

For the higher-spin complement, the physical reduced state is \(I/m\), not a qubit. The conditional mean of its normalized spin operators is \(\eta_s n_i\), where \(\eta_s=(s+1)/(3s)<1\) for \(s=1,4\). An associated two-level moment representation is mixed; the inferred unit direction is obtained by dividing by \(\eta_s\), not by pretending the actual higher-spin conditional state is a pure null qubit. The test checks this distinction.

The previous Lorentz-cone construction can now use \(N_B\) as its rest-frame input. But its congruence transformation is still a mathematical covariance statement: a nonunitary boost of that matrix is not automatically the physical action of a Lorentz boost on Bob's finite lab or a derivation of spacetime.

## 2. What the confined side can actually infer

In the fixed geometric example,

\[
 d=(-1/5,\;1/2,\;-7/19),\qquad
 P(d>0)=2/5,\quad P(d<0)=3/5.
\]

The preceding experiential candidates were \(v_1=j\) and \(v_2=\operatorname{sgn}(d_i)j\), where \(j=rt\) is the joint record–target sign. They are formal assignments on joint labels. For a proposed subject confined to Bob's side, \(i\) is an Alice pointer label, not automatically a local record.

How much can Bob infer **without receiving that label**? For the actual spin-multiplicity instruments, the two unnormalized conditional states for positive and negative \(d\) have difference

\[
 \Delta=p_+\rho_+ -p_-\rho_-
       =\frac{1}{m}\left[-\frac15 I+\frac45\,n_2\cdot L^T\right].
\]

Here \(L\) is the normalized spin operator, \(m=2s+1\), and the positive case is the middle direction. The quantum minimum-error discrimination formula gives \(P_{\rm correct}^{\max}=(1+\|\Delta\|_1)/2\):

| Existing complement instrument | Full local multiplicity optimum | Actual \((r,t)\) records alone |
|---|---:|---:|
| exact qubit, \(m=2\) | 9/10 | 7/10 |
| unsharp spin 1, \(m=3\) | 4/5 | 19/30 |
| unsharp spin 4, \(m=9\) | 11/15 | 3/5 |

The first column permits the best possible quantum measurement on Bob's *entire* logical multiplicity state, not just the selected Bob pointer. Independent local ancillas and later local channels cannot improve that optimum. The second column is computed from the actual record–target distribution, for both the old three-label clock window and all 16 labels; it assumes those two registers are available to the proposed local interface. These conditional bounds apply to the specified complement blocks and input ensemble, not automatically to the original finite-reference code, other preparations, many-copy protocols, or communication from Alice. The old relative-clock selection in these complement blocks operates on clock references initially independent of the logical pair; it is not a channel conveying \(i\).

This is **not** a claim that Bob has no information about Alice's label: correlations permit partial inference. Nor does imperfect quantum distinguishability prove that two experiences cannot differ. It says that, if a theory additionally requires a **perfect local physical report** of \(v_2\) together with a perfect local readout of \(j\), multiplying the two reports would reveal \(\operatorname{sgn}(d_i)\), contrary to the applicable bound. The joint report would require a genuinely available interface, additional information/resource, or a revised assumption. A subject can have an experience it cannot perfectly report; that remains an open possibility, not something the information bound excludes.

## 3. A second constraint: reading \(j\) can disturb the orientation zero

The earlier reference extension adds qubit F and imposes three orientation constraints \(C_1,C_2,C_3\). With its old balance \(L=+1\), the common zero sector has projector \(P\) of rank two. On the active record–work–target–reference factors let

\[
 J=Z_R Z_T,\qquad P_\pm=(I\pm J)/2.
\]

The executable check finds the following **operator identities** on that same finite model:

\[
 PJP=0,\quad [J,C_1]\ne0,\quad [J,C_2]\ne0,\quad [J,C_3]=0,
\]

\[
 \frac14 PJC_1^2JP=P,\qquad \frac14 PJC_2^2JP=P.
\]

For every normalized state initially in \(P\), each sharp j outcome has probability \(1/2\); its unnormalized post-measurement branch has \(\|C_1P_\pm\psi\|^2=\|C_2P_\pm\psi\|^2=1\). Equivalently, each normalized branch has squared constraint norm 2. The test also checks this explicitly for the original code and the qubit, spin-1 and spin-4 complement states after an old-clock readout.

Thus the natural nondemolition isometry that copies \(j\) into a **charge-neutral** pointer does not preserve those exact orientation-zero constraints branch by branch. Reading a noncommuting quantity as an event is mathematically possible, but treating that readout as a closed, neutral, constraint-preserving subject report would be inconsistent with this particular implementation. It would also be wrong to call the formal `r,t` table automatically accessible to a confined subject.

This is not a blanket impossibility theorem for reports or experience. One may investigate a properly charged reference/report apparatus, an invariant relational observable, a different conserved total including the apparatus, or a different subject boundary. Their preparation, accessibility and energy/charge accounting must be demonstrated. Nor should the earlier unselected zero-history claim be confused with an assertion that every arbitrary sharp postselection stays in its kernel.

## 4. Relativistic reference: a necessary enlargement, not an external clock

The previous synthesis used \(SL(2,\mathbb C)\) congruence on Hermitian matrices. It did not implement the full noncompact Lorentz group as unitary gates on the finite lab. There is a general reason this cannot be done nontrivially with an exact, continuous, finite-dimensional **unitary representation**.

Let anti-Hermitian rotation and boost generators satisfy the real Lorentz algebra, and use the positive invariant inner product \(\langle A,B\rangle=-\operatorname{tr}(AB)\). From

\[
 [K_1,K_2]=-J_3,\qquad [K_2,J_3]=K_1,
\]

invariance gives

\[
 -\|J_3\|^2=\|K_1\|^2.
\]

Both therefore vanish; cyclic permutations eliminate all generators. The test separately checks how the familiar two-dimensional spinor representation avoids this: its boost generators are Hermitian, not anti-Hermitian. This is not an obstruction to finite approximate reference frames, channels, postselected transformations or covariant descriptions; it is a warning against claiming an exact nontrivial finite-dimensional unitary Lorentz action.

A concrete mathematical enlargement is the unit future hyperboloid \(H^3\), the positive Hermitian \(N\) with \(\det N=1\). Its invariant measure is proportional to \(\sinh^2\chi\,d\chi\,d\Omega\). The pullback action \((U(A)f)(N)=f(A^{-1}N(A^{-1})^\dagger)\) is unitary on \(L^2(H^3,d\mu)\). But its invariant volume diverges:

\[
 \operatorname{Vol}(\chi\le R)=\pi\sinh(2R)-2\pi R\longrightarrow\infty.
\]

So a constant invariant wavefunction is not normalizable in this reference space. Normalizable wave packets exist, but their centre and width then need an internal relational preparation or explanation; calling one an external preferred frame would not solve the problem. This Hilbert-space construction does not supply gravity, an observer, or a unique whole state. It identifies a mathematical resource and the issue any physical use of it must solve.

## 5. What this means for the broad thesis

The emerging picture is not that a numerical zero mysteriously creates a world. It is that a single internally related whole might admit:

- **an internal reference** from an actual state, rather than an outside standpoint;
- **differentiation and geometry** through relations to that reference;
- **records and time** through changes inside the closed organization;
- **subjects and felt qualities** as aspects of appropriate internal organizations; and
- **global cancellation** if the relevant actual contributions and measure possess a genuinely justified opposite-pairing structure.

The first three have acquired a more concrete connection in the specified model, though the state, observables, clock, and dynamics are still stipulated. The last two remain substantive tasks. The calculation neither equates negative energy with negative feeling nor treats negative feeling as absence. If a future bridge justifies opposite felt contributions, their global sum could vanish while suffering remains real at the local incidence.

A constructive continuation should build and test a **reference-carrying, constraint-compatible report interface**, rather than treating a joint table as a subject's access. It should determine whether a more complete internal dynamics can select the paired input, reference and directions together, and whether a physical–experiential identity gives a unique locally realized sign. Necessary plenitude would also need a justified incidence rule: quantum support, a POVM label or an available formal assignment is not automatically an actual subject, and the user's actuality–genuine-possibility thesis cannot be settled by declaring alternative descriptions impossible. Finally, the reference-relative matrix balance here is not a proof that objective total cosmic energy or total felt valence equals zero.

## Verification

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps \
  python -m unittest verification.zero_internal_reference_subject_report_test -v
```

The finite calculations use NumPy; reported rational discrimination values are checked against exact fractions. The Lorentz no-go and the infinite-dimensional pullback representation are algebraic arguments, with executable checks of the spinor commutators and invariant-volume integral. The tests do not establish actual subjects, truthful reports, objective cosmic energy, or the self-sufficient selection of the model.
