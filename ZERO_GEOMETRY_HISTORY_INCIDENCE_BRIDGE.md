# From sphere balance to all-history records and incidence: an explicit join

> **Subsequent construction:** [Noncommuting sphere readouts on the actual complement](ZERO_NONCOMMUTING_COMPLEMENT_SPHERE_HISTORY.md) replaces much of the surrogate discussed here with explicit charge-preserving directional POVMs, while keeping the limitations and alternative joint tables distinct.

## The connection

The earlier results can be joined more tightly than their separate presentations suggest. In the **same specified finite model**, one can start with a three-direction zero vector on the internal sphere, follow its unequal weights through the full code-plus-complement record/clock history, and ask which signed readout correlations the same symmetry actually cancels. The result is constructive but conditional: sphere balance, the Hamiltonian history, its conserved charges and an incidence rule are not automatically identical notions of zero.

The accompanying executable check is [`verification/zero_geometry_all_history_incidence_bridge_test.py`](verification/zero_geometry_all_history_incidence_bridge_test.py). The construction imports the existing matrices and states rather than building a separate unrelated model. It extends the checks in [`ZERO_SPHERE_CONSERVATION_QUANTUM_PROBABILITY_BRIDGE.md`](ZERO_SPHERE_CONSERVATION_QUANTUM_PROBABILITY_BRIDGE.md), [`ZERO_ALL_SECTOR_SPHERE_CLOCK_WORK_RECORD.md`](ZERO_ALL_SECTOR_SPHERE_CLOCK_WORK_RECORD.md), and [`ZERO_ALL_HISTORY_COMPLEMENTARY_BALANCE_RECORD_CLOCK.md`](ZERO_ALL_HISTORY_COMPLEMENTARY_BALANCE_RECORD_CLOCK.md).

## 1. A geometric zero actually fixes unequal weights—under a specific bridge condition

For the earlier exactly specified five-ray example, the relevant three directions can be written

\[
 n_1=(1,0,0),\qquad n_2=(1/2,\sqrt3/2,0),\qquad
 n_3=(-13/19,-8\sqrt3/19,0).
\]

They are unit vectors. Solving **both** normalization and the full vector equation

\[
 \sum_i w_i=1,\qquad \sum_i w_i n_i=0
\]

gives the unique solution

\[
 (w_1,w_2,w_3)=(1/8,\;2/5,\;19/40)=q.
\]

Each weight is positive. Taking the existing comparison ray \(b=(-1/5,2\sqrt3/5,2\sqrt3/5)\) gives

\[
 d_i=b\!\cdot\!n_i=(-1/5,\;1/2,\;-7/19),\quad
 \sum_iq_i d_i=0,\quad \sum_iq_i|d_i|=2/5,\quad
 \sum_iq_i d_i^2=161/950.
\]

Thus the zero is compatible with **nonzero signed local contributions** and, in this configuration, determines unequal relative weights if those weights are the coefficients of the normalized vector balance. Equal counting instead gives \(\sum_i d_i/3=-13/570\), not zero. The test derives these fractions by exact rational elimination and checks them against the original five-ray calculation.

This is a sharper candidate bridge to incidence than assuming an arbitrary uniform count: **if** physical/experiential incidence coefficients really enter that vector balance, they are fixed to \(q\) in this configuration. But it is precisely that identification which still needs derivation. A geometrically weighted effect, Born weight, number of subjects, and signed experiential contribution are distinct objects. In particular, the single scalar condition \(\sum_i w_i d_i=0\) plus normalization does *not* uniquely determine three weights; the complete vector condition matters. The ray configuration, Hilbert space, and normalization are also supplied, not derived uniquely from zero's constitution.

## 2. The same weights survive the existing whole history

The actual all-sector state combines the encoded two-dimensional code with the 254-dimensional complement, with weights \(1/128\) and \(127/128\). The code carries the genuine noncommuting encoded sphere instrument. **The complement does not:** it has the prior commuting fixed-setting surrogate, in which the same \(q_i\) and \(d_i\) were deliberately inserted. This calculation does not claim to have derived that surrogate from a genuinely directional complement measurement. The noncommuting compressed swaps there remain a concrete path for further construction.

Nevertheless the new check uses **both actual sector states**, the entire 16-label old relative clock, the reference and the new record-memory evolution. For every old clock label and for both sectors it checks that the normalized three-setting marginal remains \(q\) at relative phases \(0,\pi/4,\pi/2\); it also checks the unselected new-clock state. The Hamiltonian and memory interaction do not act on the direction label, so preservation of its marginal is an operator-level consequence for all phases, not an inference from the samples alone. The weights are therefore consistently transported through this full-history construction, but in the large complement they remain an input to the instrument, not a new derivation.

The zero kernel of each of the three reference-orientation constraints is checked after the new relational evolution. These are declared finite-model charges, not a demonstration of objective total cosmic energy zero; the control and interaction-energy bookkeeping remains as qualified in the earlier reports. The stationary whole and its reference, seed, Hamiltonian, clock, measurement and preparation are stipulated in the prior construction, not selected by the sphere-vector equation.

## 3. An exact pairing survives the Hamiltonian and record interaction

Let \(R\) be the old signed record, \(T\) the target qubit, \(F\) the reference qubit, and \(M\) the added memory. Let \(U_0\) be the earlier all-sector record involution on \(RWT\), and put

\[
 B=U_0 X_F\otimes I_M.
\]

The companion check verifies on the complete finite matrices that \(B^2=I\), \([B,H]=0\), and the memory isometry \(W\) intertwines it: \((I_{M'}\otimes B)W=WB\). It commutes with the relevant old sign condition \(L\) and swap \(S\); conjugation fixes \(C_1\) and reverses \(C_2,C_3\), so their common zero kernel is preserved. The new clock projectors also commute with \(B\).

For each old-clock sector, both sector states satisfy \(B|\psi\rangle=|\psi\rangle\), even after multiplying the state by the diagonal geometric-value operator \(D=\operatorname{diag}(d_i)\), because \(B\) does not act on the label \(i\). The old complementary-balance operator \(Q_0\) is odd under \(B\). Consequently, for all relative phases and either new-clock eigencomponent, the \(D\)-weighted state remains paired and remains in the \(Q_0=0\) kernel. This is a state-and-operator statement, not just cancellation of a sampled mean. The explicit tests cover all 16 old labels, both sectors, the indicated phases, and the unselected new clock.

On the checked support \(L=+1\), if \(r=\pm1\) is the old record and \(t=\pm1\) the old target, the earlier work/record witness is \(j=rt\). The verified joint distribution obeys

\[
 p(i,r,t=+1)=p(i,r,t=-1),\qquad
 \langle d\rangle=0,\quad\langle d j\rangle=0.
\]

The first equality is stronger than just the last mean: the symmetry pairs opposite \(j\) at fixed \(i,r\). It is a property of this specified state and interaction, not of all states or of arbitrary readouts. Access to these joint quantities by a confined observer still requires an interface; the external joint calculation does not supply one.

## 4. The decisive distinction: zero geometry is not automatically zero experience

Consider two *candidate*, dimensionless signed assignments on the same joint cells:

\[
 v_{\rm record}=d_i r,\qquad v_{\rm work}=d_i j=d_i rt.
\]

The first is **even** and the second **odd** under the specified pairing \(B\). After tracing the old clock and before adding the new memory, the actual all-sector Born table gives

\[
 \langle v_{\rm record}\rangle=-38157/965200\simeq-0.039533,
 \qquad \langle v_{\rm work}\rangle=0.
\]

For the unselected additional stationary clock, the corresponding values are

\[
 \langle v_{\rm record}\rangle=-38157/1206500\simeq-0.031626,
 \qquad \langle v_{\rm work}\rangle=0.
\]

The nonzero record correlation does not contradict \(\langle d\rangle=\langle r\rangle=0\): those are separate marginals, while \(d\) and \(r\) are correlated. The squared-direction moment \(161/950\) is one contribution to its exact value in the supplied complement surrogate. The new Hamiltonian changes this record correlation while leaving the paired work correlation zero. Its stated \(\omega=1/2,g=1\) produce a sign-flip probability \((1/5)\sin^2\theta\), and the test verifies the resulting correlation factors \(1,4/5,3/5\) at the three phases.

Both candidate values are locally nonzero, and they have **opposite signs on half of the weighted joint cells** at every tested old-clock label and relative phase, because all \(d_i\ne0\) and the target signs are balanced. Thus there is a concrete, model-internal distinction between coupling the geometric sign to a record and coupling it to its paired work witness. A purported experiential bridge must specify which structural variable, if either, is felt and why. The calculation does not establish that either candidate is an actual experience or that a negative value is suffering. If a justified mapping identifies a negative local contribution with suffering, the global cancellation of an odd value would not erase that local suffering.

The particular nonzero record number depends substantially on the **surrogate complement**, which accounts for 127/128 of the state. It should not be presented as a prediction of a completed all-sector noncommuting sphere theory.

## 5. What the geometry fixes—and what remains to connect

The joint Born table and a separate independent table \(p(i,r,t)=q_i/4\) share the same \(q\) marginal, the same balanced \(r\) and \(t\) marginals, and the same within-cell \(t\)-pairing. Yet their \(\langle d r\rangle\) differ. Hence even **imposing the unique full-vector-balanced geometric marginal and the work-pair symmetry** does not by itself fix the incidence coupling between geometric direction and record. The second table is a mathematical alternative incidence rule, not a claim that a second physical state or additional subjects actually exist. To rule it in or out one must establish which state/effect weights govern actual incidences and which identities survive refinement; compare [`ZERO_INCIDENCE_REFINEMENT_AND_BORN_MEASURE.md`](ZERO_INCIDENCE_REFINEMENT_AND_BORN_MEASURE.md).

This provides a concrete target for the next integration: derive a genuine charge-preserving noncommuting instrument on the complement and its compatible correlated preparation; then show whether its joint direction/record/work table transports through the existing clock and reference construction. Separately, derive a subject-individuation and felt-valence law strong enough to make the relevant geometrical coefficients actual incidence weights and the physically paired sign an experiential sign. Without those bridges, neither the formal geometric balance nor its transported record symmetry establishes subjecthood, realized phenomenology, or objective whole-energy cancellation. Necessary plenitude and determinism are not settled by the finite calculation.

## Verification

Run from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest verification.zero_geometry_all_history_incidence_bridge_test -v
```

NumPy is required; `.arena/python-deps` is a local transient dependency location, not part of the theory. Exact rational identities are checked with `fractions.Fraction`; finite operator/state comparisons use NumPy with explicit tolerances. All-phase statements above follow from the tested matrix commutators, the diagonal direction control, and the specified Hamiltonian/memory construction; the test samples representative phases rather than exhaustively numerically sampling a continuum.
