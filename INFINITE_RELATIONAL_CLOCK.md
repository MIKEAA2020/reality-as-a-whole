# An infinite relational clock without a global clock distribution

## 1. Result and necessary tradeoff

The [finite relational clock](RELATIONAL_TIME_CONSTRUCTION.md) and [recorded intervention process](RELATIONAL_INTERVENTIONS_AND_RECORDS.md) now extend to clock readings n in Z. The extension preserves normalized relational experiment probabilities, coherent clock correlations on finite windows, and a normalized probability measure for countably many persistent records.

There is a precise cost: **the infinite coherent clock history is not an ordinary normalized normal joint clock-system state.** We prove that such a state cannot satisfy the stated translation constraint. The replacement is a physical Hilbert space obtained by group averaging, together with a positive functional on the finite-clock-support algebra and compatible window-conditioned states. The functional is not silently promoted to a normal weight.

What is removed is an arbitrary global distribution over clock readings. The clock group, transports, system state, and physical interpretation of the chosen clock are still supplied. This is a solution of that mathematical normalization bottleneck, not a derivation of fundamental time or of the absolute.

This uses established constrained-quantization/group-averaging and algebraic probability mathematics. The proofs, domains, and finite-core implementation are specified here; no claim of a new foundational physics discovery is made.

Code: [infinite_relational_clock.py](verification/infinite_relational_clock.py). Output: [infinite_relational_clock.json](verification/infinite_relational_clock.json).

## 2. The infinite constraint and the obstruction

Let A be a unital C*-algebra, omega a state, and (H_omega,pi,Omega) its GNS representation. Choose unitaries P_n in A with P_0=I. The kinematic Hilbert space is

    H_kin = l2(Z) tensor H_omega.

Define the transported bilateral shift and positive diagnostic constraint by

    (S f)_n = pi(P_n P_(n-1)^*) f_(n-1),
    C = (I-S)^*(I-S) = 2I-S-S^*.

The diagonal unitary Q with blocks pi(P_n) conjugates S to the ordinary bilateral shift and C to its Laplacian. Thus spectrum(C)=[0,4]. However, zero is not an eigenvalue: S f=f requires f_n=pi(P_n)h, whose norm is constant at all n. Such a sequence is square summable only if h=0.

Therefore ker(C)={0} in this kinematic Hilbert space. An infinite uniform normalizable history vector does not exist.

There is a stronger probabilistic obstruction. If a normalized normal joint state were invariant under conjugation by S, the probabilities of all single-clock projectors p_n=|n><n| tensor I would be equal, say c. Normality and sum_n p_n=I imply sum_n c=1, impossible for c>=0. Hence no normalized normal translation-invariant clock-system state exists, even when entanglement and mixed system states are allowed.

This does not rule out every singular state on a larger algebra, every nonuniform clock state, or every other kind of clock. It rules out this particular package of normality, normalization, and translation invariance.

## 3. Positive group averaging and the physical Hilbert space

Take the test space Phi of finite-support H_omega-valued sequences and define

    eta(f) = sum_n pi(P_n)^* f_n.

Every sum here is finite. Then

    eta(S f)=eta(f),   eta(C f)=0,
    sum_(k in Z) <f,S^k g> = <eta(f),eta(g)>.

The group average is finite for compact clock supports: only differences of support indices can contribute. The last identity follows by setting n=m+k and grouping the two finite sums. It supplies a positive semidefinite inner product.

Quotient Phi by ker(eta) and complete. Since eta is onto H_omega (use support at n=0),

    H_phys is unitarily isomorphic to H_omega.

The test space uses the locally convex finite-support direct-sum topology. Eta is continuous there because each finite-support restriction is bounded. No bounded or closed extension of eta to all of H_kin in its l2 norm is asserted. The quotient uses the new positive physical inner product, not an ordinary l2 limit.

This is a normalized physical carrier, not an l2-uniform clock vector. The vector h in H_phys corresponds to the generalized parallel history with components pi(P_n)h. The GNS vector Omega supplies the physical state. No clock probability density is inserted.

The fundamental condition retained here is **S invariance**, namely the original edge propagation equations. It is not merely the formal distributional equation C psi=0. The second-order equation alone admits extra affine histories pi(P_n)(a+n b). They solve the second difference equation but generally fail S invariance. The executable checks this distinction. Positivity arguments for ordinary Hilbert vectors cannot automatically be transferred to arbitrary distributional solutions.

## 4. Constraint-compatible observables survive

For a in A and a clock label v define the bounded diagonal multiplier

    D_v(a)_n = P_n P_v^* a P_v P_n^*.

As an abstract algebra map, D_v is a faithful unital *-homomorphism. It commutes with S and C. On the test space,

    eta(D_v(a) f) = pi(P_v^* a P_v) eta(f).

Thus it descends to the physical observable represented by pi(P_v^*aP_v). If pi is not faithful, that physical representation can have its usual representation kernel; the abstract multiplier embedding remains faithful.

Its normalized physical prediction is

    omega_v(a) = omega(P_v^* a P_v).

The full noncommutative observable structure is preserved, not replaced by a deterministic valuation or a distribution over clock indices. The original clock projectors do not thereby become physical Dirac observables.

## 5. A coherent functional on finite clock supports

Let F_alg consist of matrices x=(x_nm), x_nm in A, with only finitely many nonzero entries. It is a *-algebra norm dense in K(l2(Z)) tensor A. Define

    W(x) = sum_nm omega(P_n^* x_nm P_m).

This is a well-defined positive linear functional on F_alg. For x^*x,

    W(x^*x) = sum_k omega(B_k^* B_k) >= 0,
    B_k = sum_m x_km P_m.

It has coherent off-diagonal entries, not just diagonal counting terms. It satisfies exact Ward identities

    W(Sx)=W(x)=W(xS)

and the corresponding inverse-shift identities. Consequently W(Cx)=W(xC)=0 whenever x has finite clock support. S and C themselves are multipliers, not generally in F_alg; W(C) is not asserted to be a finite, defined value.

W is uniquely determined by these left/right shift identities and its root corner W(|0><0| tensor a)=omega(a). To see this, conjugate by Q. Any matrix unit becomes a left and right shift of the root matrix unit, so its value is forced to omega(a). Transforming back yields the displayed formula.

Rescaling all of W by a positive constant changes no normalized conditional prediction. The root-corner normalization fixes this scale, not a probability distribution on the entire clock.

## 6. Compatible window states and finite experiments

For every nonempty finite clock window F let p_F=sum_(n in F)p_n. Then

    W(p_F)=|F|,
    omega_F(x)=W(p_F x p_F)/|F|.

This is a normalized state on the finite corner M_(|F|)(A). For E subset F, conditioning omega_F on p_E gives exactly omega_E. Thus these are a coherent family of conditional local normalizations, not a projective family of globally normalized clock distributions.

For each relational observable,

    W(p_F D_v(a) p_F) / W(p_F) = omega(P_v^* a P_v),

independently of F. The arbitrary choice of finite normalization window therefore drops out of relational experiment predictions.

Evaluating a back-evolved event observable at an earlier mathematical window is not access to a future pointer record. D_v(a) need not equal the raw local pointer observable before its write interaction. The persistence theorem's physical conditions remain necessary.

A window cut is also not asserted to preserve the closed infinite constraint. The next section computes its precise boundary effect.

## 7. The cutoff error is a boundary term, not a hidden exact solution

For a normalized root vector h and finite F, put

    Psi_F = |F|^(-1/2) sum_(n in F) |n> tensor pi(P_n)h.

Then

    <Psi_F,C Psi_F> = |F symmetric_difference (F+1)|/|F|.

This follows because <Psi_F,S Psi_F>=|F intersect (F+1)|/|F|. For an interval of length L,

    <C>_F = 2/L,
    ||C Psi_F||^2 = 4/L for L>=2.

For L=1 the squared residual is six. Hence interval histories, or more general Folner windows with vanishing boundary-to-volume ratio, are controlled approximate infinite-constraint vectors.

The earlier finite path Laplacian has endpoint degrees one. Compressing the infinite constraint to that interval instead adds its two boundary projectors; this is why the finite zero mode does not remain an exact zero mode of the infinite problem.

As expanding intervals grow, Psi_F converges weakly to zero in H_kin, not to a normalized zero-constraint vector. Every fixed finite clock-support expectation tends to zero. Weak-* cluster states may be considered on a larger multiplier algebra, but finite clock projectors have zero probability in them: ordinary conditioning there would be 0/0. No uniqueness of such global cluster states is invoked. The window construction and the physical quotient avoid relying on one.

## 8. Why an ordinary normal weight is not a substitute

The diagonal counting functional

    W_diag(x)=sum_n omega(P_n^* x_nn P_n)

does not contain the coherent off-diagonal data. For the transported off-diagonal matrix unit |n><m| tensor P_n P_m^* with n!=m, W=1 but W_diag=0. Also W(C p_F)=0 whereas W_diag(C p_F)=2|F|. The usual counting weight cannot simply replace the coherent history functional while retaining the constraint identities.

More strongly, the coherent W has no normal-weight extension in the regular clock representation that agrees on this finite core. It suffices to examine its scalar root-frame restriction. For a finite-support scalar vector f,

    q(f)=W(|f><f|)=|sum_n f_n|^2.

Set f_L=(1/L)sum_(n=1)^L |n>. Then

    ||f_L||^2=1/L -> 0,
    q(f_L)=1,
    q(f_L-f_K)=0.

This form is not closable. Normal weights on B(l2(Z)) are represented by positive operators and their closed extended quadratic forms; a finite restriction of such a form must be closable. Thus no such normal weight extends q. The same obstruction occurs in the transported scalar clock subalgebra for arbitrary A.

We therefore use exactly what has been constructed: a positive functional on an algebraic core, a physical quotient, and normalized finite-corner predictions. We do not label W a faithful normal semifinite weight or feed it into modular theory as if those hypotheses held.

## 9. Countably many interventions and a normalized record measure

The absence of a global clock distribution does **not** prevent a normalized distribution for records.

Adjoin countably many finite pointer algebras to A by an inductive limit. Their initial blank product states and omega define compatible finite states and hence one normalized state eta_0 on the quasi-local system-pointer algebra B. No finite-dimensional global density matrix is required.

At step j use the previous explicit finite-inner recording interaction with its fresh pointer. Feedback may depend on the finite earlier prefix. Each P_n is a finite product of bounded unitary couplings in B; take P_n=I before the first step. No infinite product unitary P_infinity is assumed to exist.

Suppose later interactions preserve each already-written coarse record projector Q_j(a). For any t after its writing define

    E_j(a)=P_t^* Q_j(a) P_t.

Persistence makes this independent of t. Include blank/invalid labels when necessary to make each pointer family complete. Any finite family of E_j can be evaluated at a common late clock, so the E_j commute with one another. Its cylinder probabilities are

    p(a_1,...,a_n)=eta_0(E_1(a_1)...E_n(a_n)).

They equal the sequential instrument probabilities. They are nonnegative, normalized, and consistent under summing the last label. The cylinder functions on the product of finite record alphabets are uniformly dense in the continuous functions of that compact product. The positive normalized functional therefore extends uniquely, and the Riesz/Kolmogorov theorem gives a normalized probability measure mu on the infinite record strings.

Each pointer's blank outcome has zero post-write probability in eta_0. Countable additivity makes the set with any such blank record a null set. Restricting to the written-outcome strings consequently retains total probability one.

This is a probability measure over a specified compatible record process, not a clock-time distribution, a self-location measure, a selection of one actual outcome, or a joint valuation of every incompatible quantum experiment. Erasing old records can violate the persistence assumption; mutually incompatible readout protocols are not assigned one universal classical measure.

For any finite cylinder event its Dirac record representative has the same probability under every finite-window normalization in section 6. Thus the previous intervention, back-action, feedback and record-refinement results survive without a global clock prior.

## 10. Exact executable instances

The script uses a nontrivial rational rotation P_n=R^n at positive and negative clock readings. It checks group averaging, Dirac intertwining, Ward identities, positivity on finite cores, conditional corner consistency, and interval and disconnected-window boundary formulas.

It also checks the nonclosability witness and the affine second-order warning. These finite instances support the displayed constructions but do not substitute for the analytic nonexistence and infinite-extension proofs.

For records it continues the previous correlated two-event qubit experiment, then appends scalar Kraus writes K_0=(3/5)I, K_1=(4/5)I into fresh pointers. The latter are normalized instruments giving tail probabilities 9/25 and 16/25. Every checked finite prefix normalizes and marginalizes correctly; the theorem supplies the unique infinite extension. All four probabilities of the original two-event experiment remain unchanged under the tested finite-window relational evaluations.

## 11. Position reached

**Removed:** the need for an arbitrary normalized global distribution over integer clock readings in order to obtain finite relational experiment probabilities. Countably many compatible persistent records have their own unique normalized measure from the specified process.

**Price made explicit:** there is no regular normal stationary joint clock state. The coherent history is generalized, its finite-core functional is not a normal weight, and the first-order propagation condition must be retained rather than replaced by an underdetermined distributional second-order equation.

**Still supplied:** A, omega, the clock group Z, the transports and instruments, blank resources, and the interpretation of this clock. Clock selection, a continuum metric, an entropy arrow, arbitrary-clock equivalence, gravitational constraints, actual outcome selection, qualitative ownership, and the necessary actuality and perfection of the whole remain open. The unboundedness of the clock is not a proof that it is fundamental.

This is a constructive infinite-clock extension and an obstruction theorem within M0/W1-W6, not a completed zero-residue account or a new independent programme.
