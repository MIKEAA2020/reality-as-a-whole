# Can intrinsic symmetry select the zero level?

## A positive conditional answer

The [previous relational-gauge argument](ZERO_TOTALITY_GAUGE_RELATIONAL_PRINCIPLE.md) left a specific question: why should the physical constraint have zero level, when the same local frame transformations also allow shifted levels? There is a direct, non-temporal candidate answer:

> **If the whole's intrinsic laws reverse the sign of the relevant quantity, and there is exactly one admissible constraint level on which that sign reversal acts, then that level is zero.**

The reasoning is straightforward: sign reversal must take the unique admissible level into itself; a real number equal to its own negative is zero. This is not a claim that the state of the whole must be featureless, that its local contributions vanish, or that a creator selects the level. A single zero-level sector can contain many actual internal differences and dynamics.

It is nevertheless a **conditional derivation**, not yet the demanded foundation. One must justify the sign reversal, the physical normalization of the quantity, its applicability to the whole, and the uniqueness or fixedness of the level. Symmetry of the laws *without* uniqueness does not suffice. The mechanism also does not derive experience or show that its quantity is energy or awareness.

## 1. An exact derivation in the existing relational setting

Retain the previous two-region canonical system with variables `(theta_1,p_1)`, `(theta_2,p_2)` and `(A,E)`, and define

```text
z  = theta_2 - theta_1 - A,
C1 = p_1 - E,    C2 = p_2 + E,
Q  = p_1 + p_2 = C1 + C2.
```

For a fixed constraint level `s=(s_1,s_2)`, the admissible sector is `C1=s_1`, `C2=s_2`, so `Q=s_1+s_2`. The invariant Hamiltonian previously considered is `H=(p_1^2+p_2^2+E^2+k z^2)/2`, with positive k.

Define the following sign reversal on the variables, with the region labels held fixed:

```text
T(theta_1,theta_2,A,p_1,p_2,E)
  = (-theta_1,-theta_2,-A,-p_1,-p_2,-E).
```

It preserves the canonical Poisson brackets, sends `z`, `C1`, `C2`, and `Q` to their negatives, and leaves H unchanged. It is compatible with the local-frame transformations, conjugating a frame shift by alpha into a shift by minus alpha. Consequently T maps sector `s` to sector `-s`.

Now assume, beyond the equations above:

1. T is a symmetry of the **full admissible theory**, not merely of an auxiliary Hamiltonian.
2. The full theory admits exactly one constraint level `s`, and T must preserve the set of admissible sectors.
3. The displayed zero and signs of the `C_i` are objectively defined for this application, rather than arbitrary offsets.

Then the unique allowed sector must satisfy `s=-s`, so `s_1=s_2=0` and `Q=0`. This follows without imposing zero as a separate *numerical value*; it follows from the stated symmetry and uniqueness conditions. Both conditions, however, are substantive and their applicability has not been derived from self-subsistence. The normalization condition is essential because reflection about a different center would have a different fixed level.

Within that zero sector, `p=(1,-1)`, `E=1` is allowed, and the previous Hamiltonian has nontrivial invariant relational dynamics. Thus **a unique level is not a unique state**: demanding one globally admissible level does not require erasing all internal distinctions. Whether its formal degrees of freedom are real or experiential remains a separate question.

## 2. What exactly makes the argument non-circular?

The proposed explanatory move is to replace “Q is zero because the fundamental law says Q is zero” with two potentially independent principles:

- **Sign neutrality:** the full laws do not favor either sign of the physically defined quantity.
- **Level uniqueness:** the whole admits one level of the relevant constraint, with no unexplained choice among levels.

If these principles can be motivated by the intrinsic constitution of the whole without assuming their conclusion, their conjunction genuinely explains the zero level in this setting. Sign neutrality is a candidate expression of the thought that no externally preferred orientation or positive addition is needed; uniqueness is a candidate expression of the demand to avoid an unexplained selection. Neither follows by definition from those aspirations.

In particular, level uniqueness is not guaranteed by the absence of an external selector. Several levels might be intrinsic sectors of one whole, subject to a coherent composition principle; or one level might be fixed by a different self-sufficient law. Those proposals also need explanation. One cannot simply assume that a multiplicity of formal sectors is concretely actual, but neither may one reject every nonzero level as brute without argument. Similarly, sign reversal must be a real symmetry of the *full* theory, including whatever relates it to ordinary energy and experience; it is not forced merely because signed numbers can be negated.

The assumption of uniqueness becomes question-begging if its only justification is that zero is the level one wants to obtain. To advance the user's no-residue programme, a proposed intrinsic principle should explain **why there is only that level**, why the sign operation exists, and why the relevant zero is invariantly meaningful. An explanation of these ingredients must not smuggle in an independent ground. If they can be shown to be aspects of one self-subsistent constitution, they need not be separate external causes; the identity still has to be warranted.

## 3. Why symmetry of the laws alone is not enough

Suppose instead the admissible set of levels is

```text
S = { (1,0), (-1,0) }.
```

T maps the two sectors into one another, so the **set** of allowed sectors is sign-symmetric. Each sector has nonzero Q, respectively `+1` and `-1`. The zero sector is not in S. This is a formal counterexample to the inference from symmetry of the allowed set *alone* to zero in an admissible sector; it is not a proof that these sectors describe genuine possible worlds or the actual whole. It also does not require a lottery choosing one sector.

Even including the zero level alongside the pair would not show that only zero is realized. A rule assigning equal weights to the two nonzero signs gives mean Q equal to zero, but a zero mean is different from Q being zero in each member. A weight is an additional assumption and need not represent an external selection process.

Another route is to require **the actual classical state** to be fixed by sign reversal. Then, because `Q(Tx)=-Q(x)`, a fixed state satisfies `Q(x)=0`, even without unique sectors. That is a legitimate alternative conditional, but it is a stronger statement than invariance of the laws. In the present simple model T fixes every listed sign-odd variable only at zero, so this particular fixed-state requirement also eliminates its local signed contributions. Other symmetries can include a region exchange and preserve nonzero local differences; which transformation represents an intrinsic symmetry matters. Neither fixed-state nor unique-level invariance follows merely from the absence of an external frame.

## 4. A quantum distinction: symmetric state versus zero charge

In a quantum example, sign symmetry requires extra care. Let the normalized states `|+>` and `|->` have Q eigenvalues `+1` and `-1`, and let a **physical** sign-reversal symmetry R exchange them. The state

```text
|psi> = (|+> + |->)/sqrt(2)
```

is invariant under R, and its expectation of Q is zero. But

```text
Q|psi> = (|+> - |->)/sqrt(2) != 0,
<psi|Q^2|psi> = 1.
```

So even an invariant quantum state need not satisfy the stronger constraint `Q|psi>=0`. The example describes the state and observable mathematically, without interpreting it as a cosmic lottery or making any claim about the actual universe. If sign reversal is instead declared a **gauge redundancy**, Q is sign-odd and cannot itself be an ordinary gauge-invariant observable; the example must then be reformulated in terms of permitted invariant quantities such as Q squared or a relationally defined orientation. One must not identify gauge-equivalent descriptions and at the same time treat the sign-dependent Q as a directly invariant observation.

A continuous constraint can enforce the stronger condition: if `U(t)=exp(-itQ)` acts trivially on the **state vector** for all real t, differentiation gives `Q|psi>=0`, assuming the required operator domain. But physical states are often rays, and a ray can be unchanged while its vector acquires a phase: a Q-eigenvector of nonzero eigenvalue has this property. Thus triviality on rays alone does not fix the zero eigenvalue. Different quantum constraint prescriptions and physically meaningful charge normalization require justification; the vector condition must not be silently substituted for ray invariance.

## 5. The connection to the user's proposal

This symmetry route offers a concrete version of the user's idea that zero is uniquely self-sufficient: zero can be the **unique fixed level**, rather than just a number assigned after local contributions are chosen. It strengthens the positive case provided the uniqueness, sign reversal and normalization can themselves be explained by the nature of the whole. The inference does not require that fundamental reality *is* a quantity; it concerns a proposed global quantity applying to it.

There remain three distinct bridges:

1. **Physical:** identify the appropriate global quantity and establish, rather than assume, its sign-reversal symmetry and unique level. A gauge charge in this illustration is not automatically total energy, and a gravitational constraint is not automatically an observable total energy. An emergent spacetime theory may provide different resources, but must specify them.
2. **Constitutive:** show why the relevant principles and the actual internal organization are self-subsistent. A unique constraint level can contain many states; zero and uniqueness of the level do not themselves fix the actual relations, laws, measures or local subject boundaries. Nor is a determinate relation automatically an unexplained residue if it can be internally grounded.
3. **Experiential:** establish why the concrete organization is locally experienced with its particular qualities and subject incidences. Actual acquaintance is genuine evidence, not an extra spectator; a symmetry calculation alone neither derives it nor makes suffering disappear. No cosmic subject or perfect world is assumed.

Finally, the claim “if zero cannot meet the demand, no account can,” and the claim that structural and experiential intelligibility must be jointly satisfiable, remain substantive proposals requiring arguments beyond this conditional symmetry result. This report neither demonstrates a zero-residue account nor proves such an account impossible.

## 6. The next question

The sharpest next step is to ask whether **unique admissible level** can be obtained from a defensible self-subsistence principle rather than imposed. That requires comparing (i) one sign-neutral unique level, (ii) a sign-symmetric set of levels, and (iii) a self-subsistent principle that fixes a nonzero level, without treating merely formal descriptions as actual alternatives. The comparison should address how the whole contains real differentiated experience, and whether any required law or identity is genuinely explained rather than counted as free by stipulation.

Related: [relational symmetry and accounting](ZERO_TOTALITY_GAUGE_RELATIONAL_PRINCIPLE.md), [intrinsic relational accounting](ZERO_TOTALITY_INTRINSIC_RELATIONAL_ACCOUNTING.md), and [actual experience and constitution](ZERO_TOTALITY_EXPERIENCE_TO_CONSTITUTION.md).
