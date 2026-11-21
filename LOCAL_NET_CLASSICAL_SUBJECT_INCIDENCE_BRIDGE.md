# A local quantum instrument is not automatically a classical subject substrate

## Result

The existing [modular local net](MODULAR_LOCAL_NET.md) contains an explicit local two-outcome instrument. With that **same instrument**, two allowed local Weyl preparations have exactly the same initial binary outcome distribution, yet after the same intervening local unitary they give different probabilities for a second `+` outcome even when the first outcome is fixed to `+`. The recorded bit alone is therefore not a closed, preparation-independent classical state for this operational family.

This is a concrete failure of a **particular** coarse-graining, not a no-go theorem for all classical approximations, a refutation of IIT, or evidence of any subject. A classical effective model may add state variables, limit its preparation family, or use a specified reset protocol—but each choice needs justification and error control. The project has not supplied the relevant map from its quantum local net to the four-spin selector, IIT's discrete interventional model, or an experiential incidence rule.

The calculation below reuses an existing quantum-field construction rather than introducing a new spin simulation. The [fixed plan](LOCAL_NET_CLASSICAL_SUBJECT_BRIDGE_FIXED_PLAN.md) records what was known, including the protocol idea, before this report was written. The derivation is conditional on the existing net and CCR inputs; the model is not a brain or an experiment on a person.

## 1. Existing model and precise question

In `MODULAR_LOCAL_NET.md`, an interval algebra `A(I)` contains Weyl operators `W_f` and `W_g` built from explicit real compact smears with `σ(f,g)=1/1260`. Let `g₁=1260 g`, `U=W_f`, and `V=W_g₁`. Then, using the report's conventions,

```text
V† U V = e^(−i) U,
ω₀(U^n) = exp(−n² ||F_f||²/2) = c^(n²),   c=exp(−||F_f||²/2),  0<c<1.
```

Here `ω₀` is the vacuum state. The original local report exhibits the smears and shows that the Weyl operators and the measurement Kraus operators belong to the same interval algebra. The free-field Fock vacuum and the net are mathematical inputs of that construction; no fundamental ontology is read off from the choice of modes. The scaling of `g` is permitted by the same real linear subspace.

Use the already-specified normalized instrument

```text
K₊ = (1+U)/2,       K₋ = (1−U)/2,
E₊ = K₊†K₊ = (2+U+U†)/4,
K₊†K₊ + K₋†K₋ = 1.
```

There are fresh external record registers at the two measurements; the registers are not asserted to be subfactors of `A(I)` or to be experiencers. The probabilities are those of the full instrument, not assumptions of sharp projective measurement. Let two preparations be `|ψ_t⟩=V^t|Ω⟩` for `t=+1` and `t=−1`. After the first measurement, apply **the same** local unitary `V`, then measure the same instrument again. The observable coarse variable is the first recorded result `Y₀∈{+,−}`. Is there a single kernel for `P(Y₁ | Y₀)` valid for both preparations and this operation? That is a restricted operational closure question, not IIT's `do`-interventional transition matrix.

## 2. Exact sequential comparison

From the Weyl relation,

```text
ω_t(U^n) = c^(n²) e^(−int),
P_t(Y₀=+) = (1+c cos t)/2.
```

Thus the complete first-outcome distribution is the same for `t=+1` and `t=−1`; denote its positive `+` probability by `p=(1+c cos 1)/2`. For the second measurement after applying `V`, the pulled-back effect is

```text
E' = V† E₊ V = (2+e^(−i)U+e^(i)U†)/4.
```

`E'` and `K₊` are functions of the same unitary U, so the joint probability, with the actual first-measurement update included, is

```text
J_t = P_t(Y₀=+, Y₁=+)
    = ω_t(K₊† E' K₊)
    = ω_t(E₊ E')
    = [4 + 2 cos 1 + 4c(cos t + cos(t+1))
       + 2c⁴ cos(2t+1)] / 16.
```

Consequently

```text
P_{+1}(Y₁=+ | Y₀=+) − P_{−1}(Y₁=+ | Y₀=+)
  = [4c(cos 2−1) + 2c⁴(cos 3−cos 1)] / (16 p) < 0.
```

Angles are in radians. Both cosine differences in the numerator are strictly negative and `c,p>0`, so the inequality is strict for the actual `c` without needing its numerical value. A separate direct expansion of the Laurent polynomial for `E₊E'` was checked numerically at `c=.1,.6,.99`, agreeing with the displayed expression to floating-point precision. Those values are algebra controls, not estimates of the actual norm, data or proof of the general inequality.

The example establishes something stronger than unequal unconditional probabilities: **both branches have the same initial `+` probability, and the subsequent difference persists conditional on the same `+` record**. The postmeasurement states are nonetheless different; their unrecorded distinctions affect the later operation. The result is not caused by comparing two differently labeled detectors, and the subsequent unitary and instruments are fixed across the two preparations.

## 3. What follows—and what does not

A model whose complete effective state at this stage is just `Y₀`, and whose one-step transition kernel for the fixed `V` operation is required to be independent of which of these preparations produced it, cannot reproduce both conditional probabilities. The empirical-level record is not a sufficient statistic for the specified family. Calling the bit a unit of a physical causal network, and using one observational conditional probability as if it were a unique transition law, would hide a preparation-dependent residual.

This does **not** show that no classical stochastic model can represent these data. For example, a classical hidden variable carrying the preparation label can reproduce the finite observed family by using its corresponding conditional probabilities. That is a phenomenological completion, not evidence that the label is a physically autonomous unit or that it suffices for all future operations. A different physical coarse-graining could capture the missing degrees of freedom; a restricted ensemble could yield a valid effective kernel; a protocol that resets the full relevant state conditional on the bit could define another interventional row. Any such model must be checked on its declared domain. No claim is made that these are the only repairs.

Conditioning on `Y₀=+` is a selective measurement, **not** `do(Y₀=+)`: the former has a preparation-dependent back-action and success probability, whereas a hard setting requires an independently specified physical intervention and its consequences for the rest of the system. The unitary `V` is an actual specified operation in the mathematical protocol, not a hard clamp on the recorded bit. The model involves sequential readouts and control in an idealized chiral net; no claim about typical neural coarse variables or actual intervention feasibility follows.

IIT 4.0, as reviewed in the [exclusion audit](IIT4_EXCLUSION_AND_PRIVATE_NESTED_FIELDS_AUDIT.md), begins with finite discrete units, a current state, a complete interventional transition model and conditionally independent unit updates. Its background and cut conventions operate on that supplied model. It does **not** require treating this particular detector outcome as a unit, nor does it prescribe replacing `do` by a selective measurement. The primary paper also recognizes practical causal-model incompleteness ([substrate formalism](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011465#sec012)). The present calculation challenges an *unjustified bridge* from this single local bit to an autonomous substrate, not the mathematical consistency of IIT. Quantum extensions of IIT are separate proposals and have not been analyzed here.

The project's [pairwise influence selector](CAUSAL_INFLUENCE_SUBJECT_CONSTITUTION_GATE.md) has a different score and uses specific clamps and randomized backgrounds. It is not IIT. It also cannot be applied to the net merely by relabeling `+` and `−` as spins: it needs independently defined units, joint states, update law, admissible directed interventions and background distributions. An external record of a measurement is not automatically an internal causal degree of freedom of a subject.

## 4. Positive control: translate the entire operational protocol

The existing net has recovered translations `T(a)` at one-particle level and `𝒰(a)=Γ(T(a))` on Fock space, with `𝒰(a)|Ω⟩=|Ω⟩` and `𝒰(a)A(I)𝒰(a)†=A(I+a)`. Translate **everything**:

```text
U_a=𝒰(a)U𝒰(a)†,       V_a=𝒰(a)V𝒰(a)†,
K_{±,a}=𝒰(a)K_±𝒰(a)†,  |ψ_{t,a}⟩=𝒰(a)|ψ_t⟩.
```

The identical fresh-pointer recording scheme is also transported. The Weyl phase and vacuum expectations are unchanged, so all first and joint probabilities above are unchanged, including the strict conditional difference. This is a concrete covariance check for **this family of preparations and instruments**, not an invariance proof for an arbitrary subject selector, arbitrary grain or a different representation. The interval, candidate localization, state and interventions have all been mapped.

By contrast, translating a preparation or source while **holding the detector fixed** changes their physical relation and may change its statistics. Section 7 of the local-net report calculates a nonzero change for overlapping compact smears and zero change for disjoint support in its specified setup. That is a physical protocol change, not a passive re-expression to which equality of statistics should automatically be demanded. Translation covariance likewise does not make all mode decompositions or independently defined resets equivalent.

## 5. The bridge that would actually be needed

Before using a classical incidence selector on a quantum-field or biological model, specify and justify all of the following together:

1. **Units and state:** a finite family, compatible joint state variables and update window, their operational readouts, admissible state space, and the environment retained or marginalized. A POVM outcome is not automatically a pre-existing definite system state. Multiple noncommuting field observables cannot simply be assumed jointly sharp; different effective variables or restricted regimes may nevertheless be valid.
2. **Causal intervention dictionary:** physically implementable or explicitly idealized preparations for *every* state and each needed partial clamp, including background handling, back-action, energy/resource costs, and a test of whether the same setting has stable consequences across allowed hidden states. Distinguish selective instruments and unconditional channels from independent settings. If ideal counterfactuals are not implementable, defend the model-based extrapolation and its domain.
3. **Dynamics and error:** measure or derive interventional responses, update timing, memory effects and unit-level conditional independence where required; quantify residual dependence across preparations, unsupported states, omitted modes and cutoff limits. Record approximation errors and test whether they are small enough to preserve candidate ranking, including ties. A small average fit is not automatically an error bound on all counterfactual cuts.
4. **Physical equivalence:** translate the full state, candidate supports and allowed operations under true equivalences, as above; treat distinct relative configurations and changing grains separately. Do not assume a mode basis, a QFT local algebra or detector pointer is already a complete set of IIT units. No available calculation here shows that a candidate subject verdict survives these maps.
5. **Experiential incidence and quality:** specify whether the completed physical rule predicts L-exclusive, C-full, C-layered, P or another package, and how first-person ownership and the designated content types connect to separately elicited reports. Neither a closed causal model nor an IIT `φ_s` scalar alone specifies the project's `q`-unpleasantness association, `D/G/N` targets or subject identity. Respect testimony, report uncertainty and no-response alternatives; do not infer absent experience from failure to report. Establish clinically applicable population, anatomy, timing and subject-access assumptions independently.

The output can be **unmapped or indeterminate**, not a forced score. Even a successful classical effective model and a valid `φ_s` computation would still need a defensible IIT explanatory identity and unfolded structure to make specific phenomenal claims. The competing private nested proposal likewise needs a non-circular incidence and quality account. Neither follows from this calculation, and neither has been empirically adjudicated.

## Status

This advances a narrow operational bridge by identifying an explicit insufficiency of an existing local measurement record, together with one positive translation-covariance check. It does not refute local QFT, classical modeling, IIT or P; does not calculate IIT scores; does not establish a continuum subject; and does not derive time, gravity, valence or physical necessity. C3, B4–B5/F2, B9/F3 and B10 remain open. Standard CCR machinery and the old local-net proof were not independently re-proved here.
