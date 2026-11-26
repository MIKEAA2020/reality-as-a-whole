# Connecting molecular chirality, zero balance and the clocked record

## Result and scope

This pass joins three **existing** constructions rather than merely placing them side by side:

1. the labeled alanine geometry and evolving Frank-type concentrations in [the molecular chirality model](ZERO_RELATIONAL_CHIRALITY_AND_BIOLOGICAL_HOMOCHIRALITY.md);
2. the reference-free centering map in [the common-constitution analysis](ZERO_FULL_INTELLIGIBILITY_COMMON_CONSTITUTION.md); and
3. the actual finite-clock qutrit histories in [the clocked chirality record](ZERO_CLOCKED_CHIRALITY_RECORD_AND_RETENTION.md).

The resulting interface turns the **computed molecular concentration excess** into a definite prediction for an **existing idealized relational record**, conditional on the explicitly chosen geometry, calibration, reference and measurement protocol. In the example, the record's conditional `+`/`−` probabilities at the specified reference-clock reading change from `0.402667/0.397333` at the initial chemistry snapshot to `0.651431/0.148569` at time 40; the remaining probability `0.2` is a blank record. Tests instantiate the actual earlier qutrit history, not a replacement gate.

This is a **snapshot interface**: chemistry is solved first, then its concentrations prepare an idealized species mixture supplied to the quantum clock instrument. Chemical time and the abstract clock's 40 ticks are not identified or jointly evolved. Neither the coupling, a molecular Hamiltonian, physical readout resources nor a record in the gravitating memory model is derived. The zero balance below is algebraic, not physical total energy or a claim that chemistry has experience. [Implementation and checks](verification/zero_chiral_chemistry_clock_internal_bridge_test.py).

## 1. Geometry → population → common zero-centered contrast

Use the earlier idealized labeled L alanine tetrahedron. With the earlier ordering, the **actual three-frame invariant** assigns the two mirror species

```text
t_L = +2/3,       t_D = −2/3.
```

They represent supplied, fixed stereochemical configurations; the coordinates and labeling are inputs and the magnitudes are not universal constants for all molecular conformations. The invariant respects the prior independently rotated local frames when the links are transformed consistently. The sign is defined relative to the stated orientation and label convention, not intrinsic cosmic preference.

Let the earlier chemistry state be `y=(A,L,D,P,R,Q)` and `H=L+D>0`, `Δ=L−D`, `e=Δ/H`. Sampling one molecule from the L/D population gives

```text
P(L)=L/H,  P(D)=D/H,
E[t] = (L t_L + D t_D)/H = (2/3)e.
```

Thus the relation between geometry and the evolving population is no longer just an English analogy: the previous **computed invariant** becomes the response variable of a specified population map. Normalization is conditional on picking a monomer, not on picking A, P, reservoir or waste. If H vanishes this conditional observable is undefined.

Now call the earlier common-constitution `centered` map on `(L,D)`:

```text
centered(L,D) = (Δ/2, −Δ/2),
centered_L + centered_D = 0,
E[t] = (4/3) centered_L/H.
```

Both sides of the equation refer to the **same trajectory**. A growing local stereochemical difference and an exact zero of the centered pair therefore coexist by the same algebraic constitution, with no compensating force added. This is the restricted structural sense relevant to the user's SR analogy: **given** the map and the molecular assumptions, the relation is a mathematical identity, not a separately caused balancing process.

The limits are as important as the identity. The centering subtracts the instantaneous mean and discards `H/2` as a common component; H is physically meaningful concentration and is kept separately in the chemistry. `Δ/2` can change with time and is neither a conserved charge nor identified physical energy. An arbitrary physically relevant concentration cannot be declared gauge merely because it is removed by centering. The identity does not select why this molecular geometry, these kinetic laws or this trajectory is actual, and has no experiential interpretation by itself.

## 2. A physical distinction: relative handedness needs a reference

Suppose a **supplied** oriented reference has sign `s_ref=±1`. It is an ideal pseudoscalar reference label, not yet a modeled object with a Hamiltonian or preparation cost. Let the detector's effective input be

```text
u = s_ref t_molecule.
```

Under a simultaneous active reflection of molecule **and reference**, each factor changes sign and u is unchanged. Reflect only the molecule relative to the reference and u changes sign; reverse the reference while keeping the molecule fixed and the outcome labels interchange. This is analogous to the distinction between global sign reversal and reference-relative contrast in [the gravity physical-sign-reference model](ZERO_GRAVITY_LOCAL_PHYSICAL_SIGN_REFERENCE.md), but there is **no equation here coupling this reference to that scalar field or gravity action**.

We do not simply equate active reflection with passive coordinate redescription. In a passive orientation convention change, geometry, reference and the interpretation/calibration of outcome labels must all be transformed consistently. L and D labels are fixed by a chemical convention; the instrument's `+` label is a reference-relative pointer outcome, not the same object as L without calibration. Nothing in this construction establishes an exactly parity-symmetric actual world; the weak interaction violates parity.

## 3. The existing clocked record, populated by the actual chemistry

For each sampled species, prepare a **fresh copy** of the earlier 40-step `history(cycles=2,q,u,strength=λ)`, with `0≤λ≤1`. Use its actual old-basis amplitudes and qutrit (`blank,+,−`), and mix the two histories with weights L/H and D/H. A separate ideal orthogonal species label may purify this classical preparation; we do not assume coherent L/D superpositions or solve molecular measurement dynamics. We take the abstract pointer and its switching to be the **same stipulated mathematical resources** as in the earlier history, now controlled by `u` instead of a bare orientation sign.

The old model writes at ticks `10…39` and restores blank at wrap. For reference-clock reading 2, the actual selected anchors and weights in the earlier construction are:

```text
q=1: P(reference=2)=1/4,  written fraction w=4/5;
q=2: P(reference=2)=1/2,  written fraction w=3/4.
```

The reference reading conditions the clock history, not chemical reaction time. The abstract record obeys, for either q and either s_ref,

```text
P(blank | reference=2) = 1−w,
P(+ | reference=2) = (w/2)[1+λ s_ref (2/3)e],
P(− | reference=2) = (w/2)[1−λ s_ref (2/3)e].
```

The verifier computes these quantities by summing squared amplitudes of the **actual `history` outputs** over clock and old labels, and compares them with the formula at five snapshots. Thus a model change that altered those histories or the chemical output could falsify the claimed connection. For nonzero λ, nonzero w and a fixed known sign and geometry calibration, the ideal mean record difference recovers

```text
e = [P(+)−P(−)] / [w λ s_ref (2/3)].
```

These are ideal ensemble probabilities; experimental uncertainty, finite sampling, preparation, access and instrument errors are not provided. At λ=0 a write still occurs but the pointer is uninformative. Reversing the reference reverses the sign of the recorded difference; reflecting both species population and reference leaves the joint distribution unchanged. An exactly racemic sample yields equal pointer signs even though individual ideal species can be correlated with the pointer.

### A concrete identifiability control

The readout gives a mean of `t`, not the enantiomeric excess unconditionally. The tests construct a nondegenerate positive-oriented tetrahedron with `t=+1/3`: a pure population of those geometries has exactly the same pointer marginal as a `75% L : 25% D` mixture with the original `t=±2/3`, because both have `E[t]=1/3`. Thus a real inversion from the record to e needs independently justified geometry and response calibration. The example does not claim that the deformed tetrahedron is a dynamically stable alanine conformation.

## 4. Quantitative connection for the earlier trajectory

Take exactly the prior dimensionless parameters and starting state, including a finite precursor supply of 500, and the same `DOP853` solution. Let `λ=1`, `s_ref=+1`, `q=1` and condition on reference reading 2:

| Chemistry time | e | E[t] | centered L | P(blank) | P(+) | P(−) |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0.010000 | 0.006667 | 0.005000 | 0.200000 | 0.402667 | 0.397333 |
| 5 | 0.076712 | 0.051142 | 0.043665 | 0.200000 | 0.420457 | 0.379543 |
| 10 | 0.577401 | 0.384934 | 0.365307 | 0.200000 | 0.553974 | 0.246026 |
| 20 | 0.942823 | 0.628548 | 0.942522 | 0.200000 | 0.651419 | 0.148581 |
| 40 | 0.942868 | 0.628579 | 0.942868 | 0.200000 | 0.651431 | 0.148569 |

Each row is a separate prepared snapshot and a fresh clocked readout, **not** consecutive actual measurements of one quantum history while the chemistry evolves. Both initial and final records have blank probability 0.2 because this is a uniform-anchor conditional protocol: blank means that the chosen clock anchor precedes the write, not that a molecule was unidentified. On a written anchor alone the final positive probability is approximately `0.814289`.

At time 40 the ideal readout is substantially more asymmetric than at time 0 because the earlier kinetic model amplifies the imposed initial excess. This is a prediction of the *combined stipulated model*, not observation of a real detector or a first-principles derivation of such amplification.

## 5. What whole-level zero can and cannot mean here

As a separate constructive comparison, take two equal-volume, independently supplied modeled compartments with mirror initial states and the same parity-symmetric rates. Actual integration of both trajectories shows

```text
Δ₁(T) = −Δ₂(T),       e₁(T) = −e₂(T),
Δ₁(T)+Δ₂(T)=0,
material₁(T)+material₂(T)=1004
```

at the sampled chemistry times, while local excesses grow in magnitude. The opposite compartment and equal supply are **imposed mirror-paired initial conditions**, not a consequence of local chemistry, a proof the universe contains the pair, or an external balancing agent. Exact parity-equivariance of the symmetric equations explains why the imposed pairing is preserved. The value 1004 is a conserved precursor-equivalent **material** amount, not zero and not energy. Physical time reversal, heat generation and detailed balance are not modeled by this irreversible driven network.

This also clarifies three different zero statements that must not be collapsed:

1. `centered_L + centered_D = 0` is an instantaneous identity, even for one strongly asymmetric compartment;
2. `Δ₁+Δ₂=0` follows only for this explicitly prepared mirror pair with matching dynamics and volumes;
3. a zero **physical total cosmic energy** is a different hypothesis, requiring a justified gravitational/thermodynamic definition and a physical bridge from the relevant degrees of freedom. Neither preceding zero proves it.

The stronger philosophical aim is that all three physical and experiential determinations belong to one intelligible self-sufficient constitution. This pass instead shows exactly how a conditional fragment fits together and where its inputs still enter. It does not treat brute fact or regress as worthwhile alternatives, nor does it assert the present fragment already supplies the necessary foundation. The account of actual subjecthood and experienced character needs independent first-person anchoring and physical/relational incidence; no molecular chirality or pointer outcome is, merely by its structure, a subject or a feeling.

## 6. Real connection still required

The central missing link is **dynamical**, not a further relabeling. A next model should introduce an explicit molecular/species degree of freedom into one constrained physical action or quantum open-system model, couple it to a real chiral reference and detector, and derive their energy, backreaction, finite-clock response and chemical kinetics together. It should recover this snapshot mapping in a controlled limit, test the real Higgs–Blackmond network and a reference-free negative control, and examine chiral transfer to sugars. The present finite qutrit record is uncomputed at the clock wrap and does not solve the separate drifting-gravity-memory problem. None of these steps is presumed to establish historical L/D selection or experiential identity.

## Reproduce

Install the NumPy and SciPy versions in [the existing requirements file](verification/requirements-gravity-spin-pointer.txt), then run:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=verification:. \
 python -m unittest verification.zero_chiral_chemistry_clock_internal_bridge_test \
 verification.zero_molecular_chirality_amplification_test \
 verification.zero_clocked_chirality_history_test \
 verification.zero_intrinsic_difference_common_constitution_test -v
```

The bridge tests use the same imported geometry, integration, centering and clock-history functions. They verify the mirror-pair and material ledgers, two clock rates, reference reversal, simultaneous reflection, zero-strength and erase controls, and the geometry/mixture ambiguity. They do not demonstrate an autonomous clocked chemistry, a physical energy budget, actual historical selection or experience.
