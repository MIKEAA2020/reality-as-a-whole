# A demonstrated bridge: maintained dynamics, observable algebras, and channels

## 1. What is connected

The implemented workspace and its maintenance-preserving replacement now have an exact common formulation through:

1. finite controlled state transitions;
2. commutative observable algebras and positive states;
3. a quantum-channel extension with explicit Kraus operators;
4. an exact reduced observable sector whose controlled dynamics intertwine with both full models.

This implements the previously proposed finite algebraic interface rather than only writing it schematically. It is a bounded mathematical bridge relevant to W3 and to the H_M1/H_D1 preservation question. It is **not** a derivation of consciousness, the absolute, realistic neural physics, continuum AQFT, or quantum gravity. It does not establish nonseparability or favor idealism over Leibniz by experimental evidence.

The source dynamics are the repository's [workspace model](research/realized_workspace/model.py) and [replacement audit](verification/workspace_intervention_audit.py). No new physical or phenomenal observations are supplied.

## 2. Specify the finite processes

Let X be the model's full state space:

    x = (workspace, consumer memory, source feedback).
    |X| = 5 * 5 * 3 = 75.

Each workspace/memory entry is empty or one of four tagged binary contents; feedback is empty, visual, or auditory. These tags are model variables, not established qualities.

Let Y be the declared maintained core:

    y = (workspace, source feedback).
    |Y| = 5 * 3 = 15.
    R: X -> Y discards consumer memory.

For a fixed control u (proposals, entry/maintenance/action/feedback switches, and workspace intervention), let T_u be the ordinary full-state update with distribution enabled. Let T'_u be the update with original distribution disabled and content-sensitive feedback replacement.

Their detailed pathways and consumer outputs can differ. The exact finite result is a common reduced map t_u satisfying

    R T_u = t_u R = R T'_u.

### Why that reduced map exists

The next workspace is selected or maintained from current workspace, feedback, and u, independently of consumer memory. In the reference, next feedback is the selected source when feedback/action are enabled, otherwise empty. The replacement supplies exactly that same feedback function. Therefore both next core states depend only on R(x) and u, and agree for every x.

This proves constancy on each fiber of R and defines t_u. It is not a numerical extrapolation. It extends to any saliences admitted by the selection rule with matched controls, although the finite executable audit samples only its declared proposal family. Induction gives matching reduced trajectories for matched initial core and any sequence of declared matched controls.

## 3. The observable-algebra bridge

Associate X with the commutative unital *-algebra C(X) of complex functions, with pointwise multiplication and conjugation. Likewise use C(Y).

The reduced-to-full observable map is

    iota: C(Y) -> C(X),
    iota(f) = f composed with R.

Because R is surjective, iota is injective. Directly:

    iota(1) = 1,
    iota(fg) = iota(f) iota(g),
    iota(conjugate(f)) = conjugate(iota(f)).

Thus iota is a unital *-embedding: the reduced observables form an exact subalgebra. It is an embedding of **observables**, not an additional universe or an experiencing subject.

For deterministic dynamics define the Heisenberg pullbacks

    beta_u(g) = g composed with T_u,
    beta'_u(g) = g composed with T'_u,
    b_u(f) = f composed with t_u.

The controlled-state intertwining becomes

    beta_u iota = iota b_u = beta'_u iota.

Hence both physical-model presentations give exactly the same evolution of every reduced observable, not merely one matching scalar or baseline signal. These deterministic pullbacks preserve multiplication; they need not be automorphisms because the transitions can be irreversible.

## 4. States and predictions agree exactly

A probability distribution mu on X defines a positive normalized state

    omega_mu(g) = sum_x mu(x) g(x).

Its reduced distribution is R_*mu, and its restriction to the reduced algebra is

    omega_mu(iota(f)) = omega_(R_*mu)(f).

State pushforward and observable pullback are dual:

    omega_(T_u*mu)(g) = omega_mu(beta_u(g)).

Consequently,

    R_*(T_u*mu) = t_u*(R_*mu) = R_*(T'_u*mu).

This holds for every initial distribution and all reduced observables. The distributions are supplied mathematical states; this bridge does not derive an observer probability, a Born measure, or an interpretation of all physical probabilities.

## 5. Explicit completely positive quantum-channel extension

Let H_X have basis |x> for x in X. Extend a deterministic T_u to a channel on matrices by

    K_(u,x) = |T_u(x)><x|,
    E_u(rho) = sum_x K_(u,x) rho K_(u,x)^*,
    sum_x K_(u,x)^* K_(u,x) = I.

The last identity proves trace preservation. The Kraus form proves complete positivity: after adjoining any finite ancilla, every positive input is mapped to a sum of positive conjugates.

For a diagonal density matrix diag(mu),

    E_u(diag(mu)) = diag(T_u*mu).

Writing D_g = sum_x g(x)|x><x|, the dual channel satisfies

    E_u^*(D_g) = D_(beta_u(g)).

Therefore the state-machine, algebraic, and channel formulations agree exactly on the declared classical observable sector. The same construction applies to the replacement and reduced maps, giving a commuting diagram of classical states and observables inside finite quantum-channel mathematics.

### The extension is deliberately lossy

E_u measures the specified basis and prepares its image. It deletes off-diagonal coherence, even if T_u is injective. Distinct orthogonal pure states

    (|x0> + |x1>)/sqrt(2),
    (|x0> - |x1>)/sqrt(2)

therefore have the same output density matrix. The executable check supplies this witness.

This is not a faithful rewriting of arbitrary quantum physics. Classical reversibility does not make this particular channel extension unitary. Its basis, state preparation, control functions, and physical realization remain supplied. A Kraus representation is not a neural implementation or an explanation of ultimate actuality.

## 6. Concrete verification and a non-equivalence witness

Run:

    python verification/workspace_algebra_bridge.py

[The script](verification/workspace_algebra_bridge.py) checks the actual transition implementation; [the retained results](verification/workspace_algebra_bridge.json) report:

- 75 full states and 15 reduced states;
- 864 control settings: nine proposal sets, 16 switch configurations, six workspace interventions including the unforced case;
- 64,800 statewise reference/replacement intertwinings;
- exact rational state-pushforward/observable-pullback identities for declared diagnostic states and observables;
- multiplication and unit preservation on the reduced indicator basis;
- the matrix-unit Kraus completeness identity and the coherence-loss witness.

The algebraic and CP/TP statements are established by the analytic arguments above; finite checks verify their implementation in the declared family, not arbitrary continuum claims. These are supplemental comparisons, not new consciousness tests or additions to the core research-suite count.

In 644 audited settings the **full** reference and replacement state maps differ despite sharing the reduced map. One witness maps source index 0 to full index 18 in the reference and 15 in the replacement, while both reduce to core index 3. The enumeration is defined in the script, not a phenomenal numbering scheme.

Thus the bridge demonstrates both an exact preservation result and a limit: equality on the embedded reduced algebra does not establish equality of full states, detailed pathways, or all interventions on omitted consumers. A distribution lesion alone remains different from the content-sensitive replacement.

## 7. What this contributes to the constitution programme

**Earned:** the maintenance hypothesis's candidate effective organization has an exact observable-sector formulation with controlled dynamics and state correspondence. This connects a concrete systems/control model to finite algebraic and quantum-channel language without adding a second ontology.

**Still open:** whether that reduced sector is constitutively sufficient for local disclosure. The identity

    R T_u = t_u R

is dynamical factorization. Phenomenal sufficiency additionally requires the actual Gamma–chi target to factor through R on the declared domain. No consciousness assignment was supplied, so that conclusion has not been assumed or checked into existence.

The exact next physical task is to replace the stipulated finite basis with a justified material/neural observable relation, including localization, state class, relevant interventions, time regime, and error bounds. The exact next constitutive task is to warrant the target-preservation premise independently. Realistic AQFT algebras need not be finite matrix factors; that bridge cannot be supplied by calling C(X) a field theory.

**Conclusion:** one particular bridge is now demonstrated: maintained finite organization, its algebra of observables, its exact controlled reduction, and its channel presentation are mathematically connected with explicit preservation and loss. This fulfills a bounded mathematical task, not the complete account's outstanding physical, phenomenal, and foundational obligations.
