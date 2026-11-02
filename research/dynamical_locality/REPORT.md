# Constructive step 12: dynamical locality across regions and times

## The concrete advance

The previous construction connected a finite quantum channel, a final-slice observable net, a causal fork, and a contextual presheaf. This round extends the common model to **three time slices with explicit local dynamics and interventions**.

The result is a finite circuit analogue of dynamical locality:

\[
\alpha_{s,t}(\mathcal A_t(R))
\subseteq \mathcal A_s(J^-_{s,t}(R)),
\]

where α transports an observable backward through the specified evolution and J⁻ is its circuit past cone.

This inclusion is checked on a complete Pauli basis and therefore extends by linearity to the corresponding finite algebras. Causally disconnected wire-time observables also commute. Input and output descriptions are not treated as additional independent simultaneous qubits.

**32 new tests pass; all 308 tests across twelve research folders pass.**

This is a verified finite mathematical construction. It is not relativistic QFT, a continuum limit, a fundamental spacetime theory, or a phenomenal identity. No physical or phenomenological experiment was conducted.

## 1. Declare the system and clock

Use three qubits, labeled L, M, and R, with

\[
\mathcal H=(\mathbb C^2)^{\otimes3}.
\]

There are three slices t=0,1,2. Two nearest-neighbor gates act in sequence:

\[
G_0=\mathrm{CNOT}_{L\to M},
\qquad
G_1=\mathrm{CNOT}_{M\to R}.
\]

Thus:

\[
U_{0,1}=G_0,\qquad U_{1,2}=G_1,
\qquad U_{0,2}=G_1G_0.
\]

The lattice sites, update schedule, initial states, and operational clock are supplied. None is claimed to have been derived from complete intelligibility or identified with a fundamental spacetime structure.

The full Hilbert space has dimension eight at every slice. Nine wire-time labels do not imply nine independent simultaneous qubits or a 512-dimensional history Hilbert space in this model.

## 2. Define consistent state and observable evolution

States evolve forward:

\[
\rho_t=U_{s,t}\rho_sU_{s,t}^\dagger.
\]

Observables pull back:

\[
\alpha_{s,t}(a)=U_{s,t}^\dagger aU_{s,t}.
\]

The predictions agree:

\[
\operatorname{Tr}(\rho_ta)
=\operatorname{Tr}(\rho_s\alpha_{s,t}(a)).
\]

Composition is covariant on the state side and contravariant on the observable side:

\[
U_{0,2}=U_{1,2}U_{0,1},
\qquad
\alpha_{0,2}=\alpha_{0,1}\circ\alpha_{1,2}.
\]

The code checks the state relation for the selected states and the observable relation on all 64 Pauli basis elements. The identities themselves follow from the specified unitaries and trace cyclicity.

## 3. Distinguish a closed-system isomorphism from a reduced-channel map

Because U is unitary, this whole-slice pullback preserves identity, adjoints, and multiplication:

\[
\alpha(ab)=\alpha(a)\alpha(b).
\]

It is a *-isomorphism between the whole-slice algebras.

The previous round's map V†aV was a compression associated with an input qubit and a fixed ancilla. It was unital completely positive but not multiplicative.

There is no contradiction between those results. The difference is the scope:

- closed evolution includes the declared degrees of freedom;
- the reduced input description fixes or omits degrees of freedom and uses a different map.

**Integration lesson:** apparent disagreements between mathematical presentations can disappear once their system scope and map type are stated correctly. Calling all bridges “isomorphisms” would conceal this distinction.

## 4. Build the local net on each slice

For a subset R of the three sites, define the algebra of operators acting nontrivially only on those sites:

\[
\mathcal A_t(R)
=\bigotimes_{i\in R}M_2(\mathbb C)
\otimes\bigotimes_{i\notin R}\mathbb C1.
\]

Its vector-space dimension is 4 raised to the number of sites in R. Region inclusion gives algebra inclusion.

The time label identifies the slice on which the observable is operationally specified. It does not add a new tensor factor.

At a fixed slice, observables on disjoint site sets commute. When transported to a common reference slice by the same unitary, their commutation relations remain unchanged.

## 5. Construct the past cones from the gate schedule

To compute a past cone, move backward through the layers. Whenever an observed region intersects a gate, include both of that gate's input sites.

For final single-site regions:

\[
J^-_{0,2}(L)=\{L,M\},
\]

\[
J^-_{0,2}(M)=J^-_{0,2}(R)=\{L,M,R\}.
\]

A cone describes possible dependence of the entire local algebra. The support of one particular observable can be smaller.

The code verifies both:

- every transported Pauli observable stays within its declared cone;
- the union of supports of a site's transported X, Y, and Z observables fills its declared cone in this circuit.

Thus the cones are not merely oversized labels for this example. They capture the actual algebraic support when all local contrast directions are considered.

## 6. Recover a cross-time commutation condition

Represent a wire-time event by (t,i). A later event is causally reachable from an earlier one when the earlier site lies in its circuit past cone.

For distinct events with neither direction of reachability, the local observables commute after transport to the common reference slice:

\[
[a(t,i),b(s,j)]=0
\]

for this causally disconnected case.

The tests check all such event pairs and all local X, Y, Z combinations. Together with identity and linearity, that establishes the statement for each pair's full local matrix algebras in the finite model.

This is a **circuit-relative analogue** of a microcausal condition. It does not establish Lorentz invariance, a physical light speed, a continuum metric, or the axioms of a full AQFT.

## 7. Do not confuse different times with different independent systems

Some timelike observables fail to commute. For example, X on L at t=0 fails to commute with Z on M at t=2 after the latter is pulled back.

Even observables on the same wire at different times need not commute.

If the model had treated each wire-time label as an independent tensor factor, those independent-factor observables would commute automatically. That would erase the actual sequential relations.

The construction instead represents different-time observables within one fixed system algebra through explicit evolution. A separate history formalism could use additional spaces, but would need its own consistency and probability interpretation; it cannot be inferred simply by multiplying time labels.

## 8. Check interventions outside the cone

Suppose an observable's backward transport is supported on S. A trace-preserving local channel acting on a disjoint input region cannot change its expectation: in the dual description, that channel leaves the transported observable unchanged.

The tests verify this with:

- local X and Z unitary perturbations;
- nonunitary trace-preserving resets;
- selected pure and coherent initial states;
- the available time intervals and output sites.

The underlying general finite-system argument uses locality and Kraus completeness, not the absence of correlations. Correlated initial states do not by themselves permit unconditional signaling through a trace-preserving operation on a disjoint subsystem.

The checks establish the stipulated circuit behavior. They do not show that a real experimental intervention has exactly the assumed locality or selectivity.

## 9. Demonstrate propagation along the allowed chain

Start from |000>. Apply X to L before the first gate.

After the first gate, R is unchanged. After the second gate, the perturbation has reached R:

\[
|000\rangle\longrightarrow|000\rangle,
\]

whereas the perturbed preparation evolves as:

\[
|100\rangle\longrightarrow|110\rangle\longrightarrow|111\rangle.
\]

The final Z_R expectation changes from +1 to −1, but its expectation at the intermediate slice does not.

This is an explicit causal-path prediction. Its finite propagation speed comes from the declared local gate architecture and schedule, not a derived fundamental relativity principle.

## 10. Include all quantum contrast directions when defining influence

A CNOT's computational-basis arrow is not the complete direction of quantum causal influence.

Prepare L and M in |+>, with R in |0>. Before the first gate, apply Z to M. This changes M from |+> to |−>. After the gate, the X_L expectation changes from +1 to −1.

Thus the nominal target can influence the nominal control through phase-sensitive behavior. A causal diagram inferred only from classical bit changes would miss that dependence.

This is why the circuit cones include both input wires of a gate, rather than treating the CNOT notation as a universal one-way causal arrow.

**Integration lesson:** the relevant intervention and observable algebra matters. A restricted interface can hide causal powers visible in the fuller description.

## 11. Do not assume reduced dynamics closes

At the intermediate slice, consider two global states with the same R reduced state |0><0| but different M values.

The second gate gives different future R states. Therefore R's present reduced state alone does not determine its future across that domain.

A closed reduced transition law requires further assumptions about the neighbor/environment or a larger state description. One cannot automatically assign a self-contained Markov dynamics to every local algebra simply because the whole system evolves unitarily.

This preserves the earlier monitor lesson: a local state can be an accurate instantaneous restriction while being insufficient for autonomous dynamics.

## 12. Preserve intervention timing

An M reset before the first gate and an M reset between the two gates need not have the same effect.

For input |100>:

- resetting M at t=0 leaves the later propagation to R intact;
- resetting M at t=1 interrupts that propagation before the second gate.

The final Z_R expectations differ.

Collapsing the interventions into an untimed statement “M was reset” would lose the explanatory distinction. Temporal provenance belongs to the operational model, not merely its narrative.

## 13. Recover the previous finite construction as an overlap

For input |+00>, the first gate prepares a Bell state on L,M with an untouched R ancilla. This is exactly the previous two-qubit construction embedded in the three-qubit system.

The second gate extends it to:

\[
|\mathrm{GHZ}\rangle
=(|000\rangle+|111\rangle)/\sqrt2.
\]

The code verifies the selected density matrices, normalization, and projector identities.

This is a real overlap relation between rounds: the new model contains the previous preparation under a stated embedding and time restriction. It is not just another unrelated example with similar vocabulary.

It also does not mean that the GHZ state is a unified phenomenal subject. Multipartite quantum correlation and phenomenal unity remain distinct targets.

## 14. Transport contextual structure through time

Embed the previous Mermin–Peres square on L,M, with identity on R. Pull every observable back through the same evolution.

Since the pullback preserves products and commutation:

- each commuting measurement context remains a commuting context;
- the five +1 context products remain +1;
- the remaining −1 product remains −1.

The no-global-noncontextual-valuation parity obstruction therefore survives the change of reference slice.

This is an explicit bridge between dynamics and the previous contextual description. The physical support of a transported measurement can become nonlocal, however. An abstract equivalence of contexts is not a claim that the same local apparatus or implementation cost suffices at every time.

Nor does the obstruction exclude a global quantum state. It excludes the specified global deterministic value assignment, exactly as before.

## 15. What has been integrated, and what remains supplied

| Component | Earned in this construction | Still not earned |
|---|---|---|
| Local observable net | Slice isotony and disjoint-region commutation | A relativistic continuum field net |
| Dynamics | Unitary composition and observable duality | The actual laws or their necessity |
| Causal structure | Circuit cones and cross-time commutation | Fundamental spacetime geometry or Lorentz symmetry |
| Local interventions | Conditional propagation and no influence outside the cone | Empirical selectivity of real interventions |
| Contexts | Product/commutation-preserving temporal transport | A general identification of contextuality with experience |
| Whole-slice reconstruction | A basis-bijective algebra map | Ultimate explanation of actual occurrence |
| Previous model | Exact embedded Bell-preparation overlap | Integration of causal-set gravity, twistors, or Langlands |

The initial states, gates, subsystem variables, clock, quantum probability interpretation, and implementation assumptions remain inputs.

The construction does not choose an actual measurement outcome, derive Born weighting, count observers, or establish phenomenal identity. An executing classical model is not evidence that the modeled quantum experiment physically took place.

## 16. The next substantive extension

The natural algebraic extension is from this finite local circuit to a **consistent family of finite-region algebras**, then to a quasi-local limit with finite propagation.

That would test whether the finite translations remain coherent when system boundaries move and the number of modeled degrees of freedom grows. A local circuit architecture can motivate such a construction, but boundary conventions and the actual infinite update rule must be specified rather than assumed from this three-site example.

Even a successful lattice/quasi-local construction would not derive continuum QFT or spacetime. It would earn a more substantial algebraic dynamics bridge and clarify what additional continuum, symmetry, state, and physical interpretation conditions remain.

The phenomenal line remains parallel: independently warranted episode contrasts must constrain the proposed identity. Neither causal cones nor contextuality are to be promoted into a unity law by definition.

## Reproducibility

- `model.py`: three-qubit slice nets, gate dynamics, causal cones and event order, local interventions, partial traces, and contextual transport. Matrix primitives are reused from `research/framework_overlap/model.py` under a separate import namespace.
- `test_model.py`: 32 tests.
- `enumeration.json`: generated support, causal, and propagation summaries.
- `results.log`: actual execution output.

All supplied matrix operations use small exactly representable dyadic Gaussian entries. No tolerance-based comparison or numerical eigenvalue routine is used. This exactness statement concerns the chosen examples, not arbitrary continuous parameters.

```bash
# This round
cd research/dynamical_locality
python -m unittest -v test_model.py

# All research folders, from repository root
python research/run_checks.py
```

**Observed verification:** 32 new tests pass; 308 tests pass across twelve research folders.

### Consolidated verdict

The common finite model now has consistent region-and-time structure, rather than only a final-state correspondence. Locality, dynamics, and contextual constraints fit through explicit maps while earlier and later descriptions remain descriptions of the same evolving degrees of freedom—not extra copies. This earns a finite dynamical integration. It does not yet earn relativistic spacetime, a completed multi-framework theory, or the physical/phenomenal constitutive bridge.

## Subsequent finite-region/quasi-local construction

[Constructive step 13](../quasilocal_limit/REPORT.md) proves that buffered finite windows stabilize on each local observable and finite time horizon, constructs the quasi-local completion and extended automorphism, and identifies the obstruction to obtaining continuous time by simply shrinking the clock label.
