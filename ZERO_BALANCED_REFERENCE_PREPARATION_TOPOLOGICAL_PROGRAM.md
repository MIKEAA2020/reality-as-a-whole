# A charge-balanced reference prepared upstream: a topological research order

## Result

The previous [internal-reference analysis](ZERO_RELATIONAL_ORIENTATION_AND_INTERNAL_REFERENCE.md) proved that, once the specified work register has become maximally mixed, an uncorrelated reference cannot be brought into exact `J_W+Z_F=0` by a closed unitary preserving that charge. The feasible next move is to intervene **upstream**, before that mixing occurs.

I constructed and tested such an alternative preparation in the **existing all-sector circuit**:

- Start with a **product**, not a pre-entangled, work–reference pair with opposite sharp charges `J_W=+1`, `Z_F=−1`.
- Apply three specified unitary gates. Every gate preserves the new orientation charge, the original declared work-number and pair-number charges, and the old lab directional balances. The old declared energy constraint is zero on the initial state and after each gate.
- The first gate creates the required work–reference entanglement; the later gates attach it to the existing record and target.
- The output equals the exact previously constructed reference-extended state, **as a complex state vector**, in both the encoded and complement sectors. Consequently it also holds for their coherent superposition. All 16 relative-clock outcome vectors match; no sector or clock outcome is discarded.

This does not contradict the obstruction: the new seed has a *pure, sharply charged* work state and is introduced before the old state with maximally mixed W is produced. The prior mixed-W plus uncorrelated-F input still cannot reach the target by such a closed charge-preserving unitary. Nor does this show that the seed, reference, gates or control schedule follow from zero itself. It does replace an unexplained **pre-entangled** reference with a concrete zero-balanced product input and an explicit conserving mechanism.

Verifier: [verification/zero_balanced_reference_preparation_test.py](verification/zero_balanced_reference_preparation_test.py). Prior context: [relative orientation and internal reference](ZERO_RELATIONAL_ORIENTATION_AND_INTERNAL_REFERENCE.md); [Hamiltonian and eigencondition program](ZERO_CONSTITUTION_HAMILTONIAN_EIGENCONDITION_PROGRAM.md).

**Autonomous continuation:** [balanced-reference preparation with a relational clock](ZERO_AUTONOMOUS_BALANCED_REFERENCE_RELATIONAL_CLOCK.md) implements the gate sequence with a static program Hamiltonian and a stationary finite-reference constraint, and checks both finite-resolution and unselected history.

## 1. Topological order and feasibility

The order below follows dependencies: a later claim cannot discharge an earlier missing prerequisite.

| Order | Task | Current result | Feasibility / next criterion |
|---:|---|---|---|
| 1 | **Whole input and declared charges** | An explicit lab–clock state plus a product work/reference pair is zero in the stipulated charges. | Finite algebra; directly check all sectors. **Completed for this alternative input**, not derived ontologically. |
| 2 | **Create internal reference correlation** | The three-gate construction below does so with no postselection and preserves the charges. | Finite exact construction. **Completed**, conditional on the input and gates. |
| 3 | **Select relative orientation** | Within the tested pulse family, the complementary relational zero selects the needed angle. | A precise finite criterion exists; derive the complementary zero and axes rather than impose them. |
| 4 | **Account for controls and time** | Each gate has a charge-compatible generator, but their sequence and timing are stipulated. | Higher feasibility than full gravity: embed the interactions and control in one autonomous constrained system with an internal clock and all resources retained. |
| 5 | **Constitution and physical algebra** | The algebra and initial correlated lab resource are explicit inputs. | Derive the seed, algebra and relative-orientation rule from zero's own constitution; compare physical versus gauge interpretations. |
| 6 | **Actuality and experiential bridge** | Equal modeled weights and accessible target relations are explicit; subjects and felt signs are not. | Derive actual incidences, subjects, valence and their measure consistently with locality and the no-signalling constraints. |
| 7 | **Cosmological and empirical closure** | The finite charges and Hamiltonians are not shown to be objective total cosmic energy. | Connect to a covariant or emergent-spacetime theory and observational tests. |

This is an order of **logical dependence and practical feasibility**, not permission to accept any step as unexplained residue. It does not assume an external time or a preferred foliation.

## 2. Start before the obstruction applies

Use the same code or complement lab–reference–clock state and the same Alice/Bob pointer preparation as in the preceding circuit. Bob's pointer is copied to the original neutral R register. The two global lab sectors retain their coherent `1/128` and `127/128` weights; no sector projection is performed.

Instead of appending an uncorrelated F to the *already processed*, maximally mixed work marginal, take a new input with

```text
|j+⟩_W = (|0110⟩ − i|1001⟩)/√2,      J_W|j+⟩=+|j+⟩,
|−⟩_F,                                  Z_F|−⟩=−|−⟩,
|0⟩_T.
```

The pair is a product and obeys `Q_orient=J_W+Z_F=0` sharply. It is independent of the pre-existing lab/clock/record state. Each work basis vector has the same stipulated work energy 2, canceled by the specified clock offset, and F is neutral under the **old** energy assignment. The verifier checks the original declared energy constraint for this seed and every subsequent stage in both lab sectors. The model's new `Q_orient` is not identified with objective total cosmic energy.

This is an *alternative upstream preparation*, not a charge-preserving conversion of the exact late-stage mixed-W input ruled out previously. The two initial states are physically different. The pair's sharp ± values and the reference itself remain stipulated; neither is yet derived from zero's own constitution.

## 3. Three exact charge-preserving gates

All formulas below are on the active work subspace; the verifier also builds the full `2×16×2×2` R–W–T–F operators, including inactive work states, and checks unitarity and commutators.

### A. Make the internal pair

Let

```text
P₀ = (I−J_W Z_F)/2,
K = P₀ X_W X_F P₀,
E(β) = exp(iβK).
```

`K` commutes with `Q_orient`. At β=`π/4`, the initial product pair becomes

```text
(|j+⟩|−⟩_F + |j−⟩|+⟩_F)/√2.
```

The state has equal Schmidt coefficients and remains exactly in the zero orientation-charge sector. This is a unitary correlation-generating interaction; it does not require a pre-entangled W–F input or postselection.

### B. Relate the pair to the existing record

Let `P_±=(I±J_W)/2` and apply

```text
D = P_+ + i Z_R P_−.
```

D is unitary and commutes with `J_W+Z_F`. It attaches the appropriate relative phase to the two work components in relation to the **already copied** record R. It is an explicitly stipulated interaction between R and W, not an automatic interface between confined realms.

### C. Record the actual R–work relation in T

Use the same relation and target gate as the preceding circuit:

```text
h = (I−Z_R J_W)/2,
T_gate = (I−h) − i h Y_T.
```

This gate commutes with `Q_orient` and changes T only through h. R, T and F are neutral under the prior declared energy assignment; the work operations stay in the same two-excitation work sector. The operators act trivially on the lab directional generators and the old reference/clock factors.

The ordered output `T_gate D E(π/4)|seed⟩` is exactly the previously constructed internal-reference state `V|Ψ_old⟩` in each lab sector, with the same phases—not merely the same classical tables. The test also applies all 16 actual relative-clock roots and verifies each resulting state vector separately. The control sequence is written in parameter order for this calculation; a physical autonomous clock and switching apparatus have not been derived.

## 4. What fixes the pulse, conditionally?

Let S and `C₁=U₀−X_F` be the invariant relative-phase witness and complementary balance of the previous report. Replacing β=`π/4` by a variable β in the same gate family gives, in each normalized lab sector,

```text
Q_orient|Ψ_β⟩ = 0,
⟨S⟩_β = sin(2β),
⟨C₁²⟩_β = 2[1−sin(2β)].
```

If `C₁=0` is required, then in `0≤β≤π/2` the unique solution is β=`π/4`. This is a concrete dependency: the relative zero **selects the needed angle within this family**. It is not yet a derivation of `C₁`, the family of allowed gates, or a mechanism that implements the selected pulse. Nor does the condition by itself decide whether all other relative phases are genuine alternatives, gauge descriptions, or distinct actual incidences.

## 5. Remaining inputs and why the ordering matters

The preparation uses less than the prior construction assumed, but it is not a self-sufficient derivation:

- The original all-sector lab/reference state and the new, opposite W–F product state are inputs. The new state is balanced but still selects sharp local signs and a specific work/reference representation.
- The exchange, record-controlled phase and target couplings are constructed, not derived from zero. They connect designated factors; the model does not establish a spacetime-local realization or that a confined subsystem can access their joint relation.
- The gates preserve the **declared** old energy and the newly introduced orientation charge. This does not establish an objective global gravitational-plus-matter energy or identify either charge with experience.
- A prescribed gate sequence is not a derived autonomous history. Demonstrating conserved generators separately does not automatically pay for clock preparation, switching or a physical record of the control.
- An internal reference, pointer, qubit, or entangled state is not an actual subject. Equal weights and algebraic opposites do not determine felt orientation, or make pleasure erase suffering.

The most feasible next step is to put the three given generators into the already developed autonomous relative-clock framework and test whether the same final state and all sectors are retained with an explicit clock and control. If that can be done, the next prerequisite is a derivation of the balanced seed and interaction algebra from the zero-whole, rather than an additional construction chosen for success. Subject incidence and signed felt quantities must then be derived as part of that same constitution, not pasted onto the result.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_balanced_reference_preparation_test -v
```

Nine tests check the product zero-charge seed, all three unitary gates, full physical work-register extensions, prior declared energy and work charges at each stage, exact all-sector target state, all 16 clock labels, the pulse-selection relation, and the prior no-go control. Tests establish only these specified finite equations and probabilities, not necessity, subjecthood, physical locality, global cosmological energy or a complete autonomous clock.
