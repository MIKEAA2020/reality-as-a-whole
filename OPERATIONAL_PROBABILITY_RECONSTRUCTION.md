# Positive reconstruction: probability, observable algebras, and actual updating

## 1. What is derived

This construction replaces a statement of compatibility with a derivation:

> **Once physical alternatives have the effect structure of a unital C*-algebra, every normalized, noncontextual probability assignment respecting finite coarse-graining is the restriction of a unique positive normalized linear functional. In finite complex quantum mechanics it necessarily has the Born form. Restriction to subalgebras and physical channels then carries probabilities consistently between descriptions.**

The result covers qubits when probabilities are assigned to **all effects**, not only sharp projectors. No continuity assumption is needed for the first extension theorem: positivity and finite additivity supply it. The general result does not require local density matrices or a trace in a type-III AQFT algebra.

A second result establishes a strict limit: **even probabilities for every preparation and every first readout do not specify the instrument's actual conditional dynamics**. Two explicitly constructed instruments have identical first-readout effects for every input state but give different sequential probabilities. This is a positive calculation of physical underdetermination, not an assignment of experiences to an illustrative process.

These are standard mathematical results and constructions, not claims of mathematical novelty. The project gain is an explicit reconstruction and working connection among probability, state, effect, channel, subalgebra, and sequential intervention. It is **not** a derivation of quantum mechanics or the perfect absolute from pure intelligibility. No phenomenal identity is claimed. The requested zero-residue breakthrough has not thereby been obtained.

## 2. Independent premises, stated before the derivation

Let A be a complex unital C*-algebra. Its effects are

\[
\operatorname{Eff}(A)=\{E\in A:0\leq E\leq I\}.
\]

For a fixed preparation, suppose an outcome's probability is m(E). Require:

1. **Bounded probability:** m(E) lies in [0,1].
2. **Normalization:** m(I)=1.
3. **Finite coarse-graining:** if E,F are positive and E+F≤I, then m(E+F)=m(E)+m(F).
4. **Effect noncontextuality:** the same physical effect has the same probability when included in different allowed measurement decompositions.

The fourth condition is built into using a single-valued m on effects. It is not deterministic hidden-variable noncontextuality, nor a denial of quantum contextuality in all its meanings. Different implementations may have the same first-readout effect while different subsequent effects reveal their different dynamics.

A measurement is a finite family of positive effects summing to I. All effects of the claimed algebra must be in the domain of m; data on a restricted accessible subset do not automatically determine an extension to every effect.

**What is assumed, rather than derived:** the complex operator algebra and its physical interpretation. If effects are defined merely as equivalence classes of already supplied probability tables, parts of the construction may be representational rather than an independent physical explanation. We do not infer the quantum event structure from the existence of experience, the absence of brute facts, or an analogy with unity.

## 3. Derivation on the positive cone

First, m(0)=0 follows from additivity. If E≤F≤I, then F−E is an effect and

\[
m(F)=m(E)+m(F-E)\geq m(E).
\]

Thus m is monotone. Repeated subdivision gives

\[
m(E/n)=m(E)/n,
\]

and rational homogeneity whenever the relevant scaled effects lie in the domain.

For any positive a in A choose a positive integer n≥||a|| and define

\[
\omega_+(a)=n\,m(a/n).
\]

### Independence of the chosen bound

If n and k both bound ||a||, subdivide a/n into k copies of a/(nk), and a/k into n copies of that same effect. All intermediate partial sums stay below I. Hence

\[
n\,m(a/n)=nk\,m(a/(nk))=k\,m(a/k).
\]

The definition is independent of the selected integer. This integer is a proof device, not a physical cutoff or probability parameter.

### Additivity

For positive a,b choose an integer n≥||a||+||b||. Then a/n+b/n≤I, so

\[
\omega_+(a+b)
=n\,m((a+b)/n)
=n\,m(a/n)+n\,m(b/n)
=\omega_+(a)+\omega_+(b).
\]

Positive-cone additivity gives rational homogeneity and order monotonicity. For real t≥0, bound t between rational sequences r approaching from below and s from above. Then

\[
r\omega_+(a)\leq\omega_+(ta)\leq s\omega_+(a).
\]

Taking the scalar limits proves real homogeneity. **No continuity of m was assumed.** The real-valued bounds establish the needed continuity consequence.

## 4. Extension to the whole algebra

Every self-adjoint x is a difference a−b of positive elements. Define

\[
\omega_{\mathrm{sa}}(x)=\omega_+(a)-\omega_+(b).
\]

If also x=c−d, then a+d=c+b; positive additivity makes the two values equal. The extension is well-defined and real-linear. Extend complex-linearly by

\[
\omega(x+iy)=\omega_{\mathrm{sa}}(x)+i\omega_{\mathrm{sa}}(y)
\]

for self-adjoint x,y. The result is positive and normalized, since it is nonnegative on positive elements and takes I to 1.

For self-adjoint x, the order bounds −||x||I≤x≤||x||I imply |ω(x)|≤||x||. Positivity also gives the Cauchy–Schwarz inequality

\[
|\omega(a^*b)|^2\leq\omega(a^*a)\omega(b^*b),
\]

by applying ω to (aλ+b)*(aλ+b) and minimizing over complex λ (with the zero-diagonal case handled by positivity). Taking a=I gives

\[
|\omega(b)|^2\leq\omega(b^*b)\leq\|b\|^2.
\]

Thus ω is bounded, with ||ω||=ω(I)=1: **it is a C*-algebra state**.

Any positive linear extension must take positive a to n m(a/n), so it agrees on the positive cone and hence on all of A. Conversely, every state restricts to an assignment satisfying the premises. Therefore normalized effect assignments and states correspond exactly.

The uniqueness is **for a supplied m**, not a proof that the physical preparation or actual state is unique. The theorem fixes the representation and admissible form of the probabilities, not their numerical values without preparation evidence.

## 5. Classical and quantum probability emerge as the appropriate cases

### Finite classical algebra

For A=C(X) with finite X, let δ_x be its indicator effects. Put μ_x=ω(δ_x). Positivity and normalization imply μ_x≥0 and Σμ_x=1, and linearity yields

\[
\omega(f)=\sum_{x\in X}\mu_x f(x).
\]

This recovers the state/expectation formulas used in the existing finite workspace constructions. An additional arbitrary rule for the probabilities of coarse-grained events is not needed once μ is fixed.

### Finite complex quantum algebra

For A=M_d(C), use matrix units E_ij and define ρ_ij=ω(E_ji). Linearity gives

\[
\omega(A)=\operatorname{Tr}(\rho A).
\]

For any vector v,

\[
v^*\rho v=\omega(vv^*)\geq0,
\]

and Trρ=ω(I)=1. Thus ρ is a density matrix, uniquely determined by ω. Conversely any density matrix gives such a state. An effect E therefore has

\[
p(E)=\operatorname{Tr}(\rho E).
\]

This is the Born form, including **dimension two**, because the premises constrain all effects. It is a Gleason-type effect-algebra reconstruction, not a claim that the usual sharp-projector theorem applies unchanged to qubits.

### General observable algebras and AQFT

The extension theorem works without finite dimension. For a local AQFT algebra, probabilities are ω(E); an intrinsic local trace-class density matrix is not required. If a von Neumann **normal** state is needed, normality is an additional physical/mathematical requirement—for example, appropriate order continuity on increasing bounded nets. Finite additivity alone does not establish it. Not every algebraic state is normal.

No realistic brain field model, local subject, or actual state has been derived by this observation. It removes an invalid dependence on finite density matrices from the probability interface; it does not identify AQFT regions with experiencing subjects.

## 6. An exact qubit test of the load-bearing premise

For any rank-one qubit projector P_n with unit Bloch vector n, consider

\[
f(P_n)=\frac{1+n_z^3}{2}.
\]

It lies in [0,1] and satisfies f(P_n)+f(I−P_n)=1. Consequently it satisfies every binary sharp-projector normalization test. This does **not** make it a quantum state probability assignment.

Take P_z=|0><0|, P_x=(I+σ_x)/2, and P_n with n=(4/5,0,3/5). The following two sums specify the **same effect**:

\[
E=\tfrac12 P_n+\tfrac1{10}I
 =\tfrac25 P_x+\tfrac3{10}P_z
 =\begin{pmatrix}1/2&1/5\\1/5&1/5\end{pmatrix}.
\]

All summands and their coarse-grained sums lie between 0 and I. Rational homogeneity and additive refinement would require the same m(E) from either decomposition. But f gives

\[
\tfrac12 f(P_n)+\tfrac1{10}=\frac{101}{250},
\qquad
\tfrac25 f(P_x)+\tfrac3{10} f(P_z)=\frac12.
\]

The assignment cannot extend consistently to all effects. Every Born assignment gives equal values for these identical effects.

This calculation demonstrates **why** the effect/refinement premise matters, rather than hiding it in a named theorem. It does not show from metaphysics alone that every imaginable event structure must satisfy that premise.

## 7. Actual updating is not fixed by the readout probability

In Heisenberg form, an instrument consists of completely positive maps Φ_i with ΣΦ_i(I)=I. The outcome effect is E_i=Φ_i(I); for input state ω,

\[
p_i=\omega(E_i),\qquad
\omega_i(B)=\frac{\omega(\Phi_i(B))}{p_i}\quad(p_i>0).
\]

These follow by composing the state with the specified physical operation and normalizing the selected branch. The instrument is additional structure: the probability reconstruction does not derive it. Complete positivity incorporates compatibility with ancillary systems and is stronger than positivity needed merely to map individual states to states.

Here is an explicit pair of instruments with identical E_i for every preparation. Let P_0=|0><0| and P_1=|1><1|. The first has Kraus operators

\[
K_0=P_0,\qquad K_1=P_1.
\]

The second uses v=(3/5,4/5) and

\[
L_0=|v><0|,\qquad L_1=|v><1|.
\]

For each i, K_i*K_i=L_i*L_i=P_i, and both sums are I. Hence **every input state has exactly the same first-outcome probabilities** for the two instruments.

For ρ=I/2 and outcome 0, however, the first prepares P_0 while the second prepares P_v. A subsequent P_v test gives conditional probabilities 9/25 and 1. The corresponding joint probabilities are

\[
p(0,\text{then }P_v)=\frac9{50}
\quad\text{versus}\quad
\frac12.
\]

Thus even a complete family of first-readout probabilities cannot replace actual dynamics. An identical readout is not a complete physical equivalence, even before any phenomenal claim is made. The zero-probability branch is left undefined as a conditional state, not normalized illicitly.

This is directly relevant to the maintained-disclosure investigation: state/effect/readout descriptions must not silently substitute for intervention-sensitive realized organization. It establishes no experience in either instrument and no consciousness criterion based on quantum coherence.

## 8. Probabilities now commute with the demonstrated physical bridges

If ι:B→A is a unital *-homomorphism representing a subalgebra, then

\[
m_B(E)=m_A(\iota(E))
\quad\Longrightarrow\quad
\omega_B=\omega_A\circ\iota.
\]

The equality follows from uniqueness of the extension. If Φ:B→A is a unital completely positive channel, ω_A∘Φ is a state on B and gives the transported probabilities. Positive unital maps already preserve individual states; the stronger CP condition is not derived from that fact alone.

This provides the probability foundation for the [workspace/algebra/channel bridge](WORKSPACE_ALGEBRA_CHANNEL_BRIDGE.md): classical pushforward, observable pullback, algebraic state restriction, and quantum channel composition are related operations on the same state/effect structure, not separately chosen probability rules.

It also respects the bridge's explicit information loss. Two states can agree on a diagonal readout yet disagree on a later interference test. In the exact verification, |+><+| and I/2 both give probability 1/2 for P_0, but a P_x test gives 1 and 1/2. A dephasing extension is therefore not faithful arbitrary quantum re-presentation.

For the wider unified account this is a concrete mathematical connection, not a claim that every mathematical framework has now been recovered. A quantum state measure is also not a distribution over experiencing subjects: the relevant observable event, record, preparation and evidence relation must first be physically and phenomenally warranted.

## 9. Verification and deliverable

Run:

```sh
python verification/operational_probability_reconstruction.py
```

The standard-library [implementation](verification/operational_probability_reconstruction.py) uses exact rational complex arithmetic. The [retained result](verification/operational_probability_reconstruction.json) checks:

- nine rational quantum states and six projector directions, including complex off-diagonal states;
- **1,350 three-outcome POVMs and 4,050 exact outcome probabilities**, with normalization, positivity, rational scaling and coarse-graining;
- the identical-effect decomposition that obstructs the nonlinear projective assignment;
- Kraus completeness and identical effects for the two physically different instruments;
- their exact different sequential probabilities, coherent/dephased discrimination, and invalid state/effect guards.

The universal C*-algebra extension is established by the proof above, **not** by enumerating finite cases. The finite verification checks the implementation and witnesses, not the physical truth of the premises. These checks are supplemental and do not increase the historical 1,149-test core total. There are no new experimental observations or neural recordings.

## 10. What has and has not been removed from the explanation

**Removed as an independent choice, conditionally:** once the quantum/classical effect algebra, preparation assignment, and refinement premises are fixed, probabilities cannot be replaced by an arbitrary alternative rule. Their positive-linear state form, the finite Born representation, and compatibility under restriction/composition follow. The qubit calculation exhibits a concrete rival that fails precisely at the physical refinement requirement.

**Not removed:** why the actual physical event structure is this algebra; why this state and these instruments are actual; why the complete constitution has those determinations; which actual occurrences are experiences and what their incidence is; or why reality is the perfect complete absolute. A no-brute-facts demand is not substituted for those missing derivations. Deriving the representation of a supplied assignment is not deriving every value of that assignment.

The constructive change is that a previously adopted probability interface is now explicitly reconstructed across finite classical, finite quantum, and general observable-algebra domains, and its strict separation from realized updating is demonstrated. This is a positive bridge in the unified programme, not the complete account and not a pretext to claim that another renamed gap is a breakthrough.
