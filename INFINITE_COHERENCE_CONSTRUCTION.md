# An explicit infinite coherence construction

## 1. The mathematical object being constructed

We now construct, rather than merely describe, a noncommutative whole with a fixed local law, uniquely selected finite-ring ground states, a unique periodic thermodynamic limit, compatible finite restrictions, and exact correlation functions.

This is the standard spin-1 AKLT / finitely correlated state construction in a Cartesian basis. It is used here as an explicit mathematical building block for the common-constitution programme, not presented as a new physical discovery or the essence of the absolute. The all-size arguments are given below; [the executable check](verification/infinite_coherence.py) and [its output](verification/infinite_coherence.json) independently check finite instances in exact arithmetic.

The presentation has no external production time: the index N labels finite mathematical systems, not stages in the absolute's becoming. A spatial adjacency is supplied, however: the integer chain is an assumption, not derived spacetime.

**Concrete output:**

    local coherence law h
       -> unique periodic ground ray for every N >= 4
       -> unique local thermodynamic limit omega
       -> a state on the infinite quasi-local C*-algebra
       -> a cyclic representation unique up to unitary equivalence.

This determines a global state from a stated local coherence law and periodic closure, rather than inserting an independent table of global states. It does not identify finite restrictions with experiencing owners.

## 2. Minimal algebraic data

Take three Hermitian Pauli matrices sigma_x, sigma_y, sigma_z on C^2:

    sigma_a sigma_b + sigma_b sigma_a = 2 delta_ab I_2.

The physical site is C^3 with basis x,y,z. The auxiliary C^2 is a mathematical contraction space, not an extra conscious entity. Put K_a = sigma_a / sqrt(3). Then

    sum_a K_a^* K_a = I_2,
    sum_a K_a K_a^* = I_2.

For a site observable X and an auxiliary matrix B define

    E_X(B) = (1/3) sum_ab X_ab sigma_a B sigma_b.

For X = I_3 this is a unital completely positive map T. Writing B = b_0 I + sum_a b_a sigma_a gives

    T(B) = b_0 I - (1/3) sum_a b_a sigma_a,
    T^r(B) = Tr(B) I/2 + (-1/3)^r [B - Tr(B) I/2].

Thus the invariant auxiliary density matrix is uniquely I_2/2. The transfer eigenvalues are exactly 1,-1/3,-1/3,-1/3. Neither the stationary matrix nor the decay factor needs to be fitted once these data have been fixed.

## 3. The local law, before the global state

On two sites let F exchange the factors and let u = |xx> + |yy> + |zz>. Define

    h = (I + F)/2 - |u><u|/3.

The symmetric subspace has dimension six; u spans its scalar direction. Consequently h is the orthogonal projector onto the five-dimensional symmetric traceless subspace:

    h = h^*,   h^2 = h,   h >= 0,   rank(h) = 5.

The local coherence law is zero amplitude in that subspace. In coefficient form, for fixed surrounding indices,

    psi_...ab... + psi_...ba... = 0       if a != b,
    psi_...aa... = psi_...bb...           for all a,b.

On an open interval put H_N = sum_{j=1}^{N-1} h_(j,j+1). On a ring add h_(N,1). All summands are positive, so zero energy is equivalent to satisfying every local constraint. This is an exact constraint, not a tolerance or optimized numerical score.

In conventional spin-1 notation this same local projector is

    h = [(S_1 dot S_2)^2 + 3(S_1 dot S_2) + 2 I]/6.

Its vanishing sectors have total spin zero and one; total spin two has energy one. No claim about actual matter or a physical energy scale is made by choosing this law.

## 4. All-size solution of the local constraints

### Open intervals: exactly four dimensions for N >= 2

The coefficient constraints are dual to the homogeneous word relations

    ab = -ba for a != b,
    x^2 = y^2 = z^2 = q.

The degree-two element q is central: moving a generator across the square of another introduces two minus signs. Reordering words and replacing repeated letters by q leaves, at fixed degree N:

- for even N >= 2: q^(N/2) and the three q^((N-2)/2) ab with a < b;
- for odd N >= 3: the three q^((N-1)/2) a and q^((N-3)/2) xyz.

Hence the degree-N quotient has dimension at most four. Sending the generators to the Pauli matrices and q to I maps these four normal forms to a basis of M_2(C): I and three Pauli directions, with possible factors of i. They are independent. The quotient therefore has dimension exactly four, as does the space of zero-energy coefficient arrays.

Explicitly, every open-chain zero-energy vector, and no other one, has coefficients

    psi_B(s_1,...,s_N) = Tr[B sigma_(s_N) ... sigma_(s_1)],
    B in M_2(C).

The correspondence is injective for N >= 2 because products of N Pauli generators span M_2(C). This proves the dimension statement for all N, not just the sizes checked in software.

### Rings: a unique ray for every N >= 4

Any ring ground vector is first an open-chain vector psi_B. Fix the N-2 middle indices and write their matrix product as Q. The diagonal part of the closing constraint requires

    Tr(B sigma_x Q sigma_x)
      = Tr(B sigma_y Q sigma_y)
      = Tr(B sigma_z Q sigma_z).

For N >= 4, these middle products span M_2(C). Nondegeneracy of the trace pairing and cyclicity give

    sigma_x B sigma_x = sigma_y B sigma_y = sigma_z B sigma_z.

Expanding B in the Pauli basis forces all three traceless coefficients to vanish. Thus B is scalar. Conversely scalar B also satisfies the off-diagonal closing constraints, by cyclicity of trace and Pauli anticommutation. The trace vector is nonzero: even-length words can multiply to I, and odd-length words of length at least three can multiply to iI.

Therefore the periodic Hamiltonian has a **one-dimensional ground space for every N >= 4**. Global phase is the only vector freedom. This is the first determination result: a fixed local law plus periodic closure selects the finite state without an independent state selector.

## 5. The limit is explicit, not assumed

Let q_0 = -1/3. For the unnormalized periodic vector with coefficients

    3^(-N/2) Tr[sigma_(s_N) ... sigma_(s_1)],

the squared norm is the superoperator trace of T^N:

    Z_N = 1 + 3 q_0^N.

For a word s of length n put P_s = sigma_(s_n) ... sigma_(s_1). Define

    (rho_n)_st = Tr(P_t^* P_s) / (2 * 3^n).

Let rho_(n,0) be its Gram sector consisting of words whose Pauli product is scalar. The other sectors have products proportional to x,y,z. Orthogonality in the Hilbert-Schmidt inner product makes these four sectors mutually orthogonal.

For N >= max(n,4), the reduced state of n consecutive sites in the normalized periodic ground state is exactly

    rho_n^(N)
      = [rho_n + q_0^(N-n) (4 rho_(n,0) - rho_n)] / Z_N.

To derive the formula, write the block contraction as the linear map B -> P_t^* B P_s / 3^n. Its superoperator trace is Tr(P_t^*)Tr(P_s)/3^n = (4 rho_(n,0))_st; its trace against the rank-one stationary transfer projection is (rho_n)_st. Now use T^(N-n) = P_stationary + q_0^(N-n)(I-P_stationary).

The limit is therefore rho_n. A uniform sufficient bound is

    ||rho_n^(N) - rho_n||_1 <= 6 * 3^(-(N-n)).

Indeed ||4 rho_(n,0)-rho_n||_1 <= 3, Tr(rho_n)=1, Z_N >= 2/3 for N >= 2, and 3|q_0|^N <= |q_0|^(N-n) for n >= 1. This supplies a controlled infinite limit, not just a finite extrapolation.

## 6. Positivity, compatibility, and the single infinite state

For every n, rho_n is a Gram matrix divided by a positive constant, so rho_n >= 0. Each word product is unitary, giving Tr(rho_n)=1. Tracing the last site uses sum K_a^* K_a=I; tracing the first uses sum K_a (I/2) K_a^*=I/2. Thus

    Tr_first(rho_(n+1)) = rho_n = Tr_last(rho_(n+1)).

These end restrictions define consistent states on all intervals of the integer chain. Arbitrary finite subsets are handled by restriction from an encompassing interval; consistency makes the choice of that interval irrelevant.

Let A_I = tensor_(j in I) M_3(C), embedded by tensoring identities, and define

    A = norm closure of the union of all A_I.

Set omega(a) = Tr(rho_I a) for local a. Compatibility makes this well-defined. Positivity holds locally, and |omega(a)| <= ||a||; hence omega extends continuously to a normalized positive functional on A. The local union is norm dense, so the extension is unique.

This is an infinite noncommutative state space, not a single finite global density matrix. Disjoint site algebras commute, but each site algebra is noncommutative. It is a spin-chain quasi-local C*-algebra, **not** a relativistic AQFT net and not a derivation of type-III local factors.

The second determination result is therefore:

> The periodic local law determines a unique local thermodynamic limit; its compatible finite states determine exactly one state on the specified quasi-local algebra.

## 7. A minimal global carrier without a second state choice

Construct N_omega = {a : omega(a^*a)=0}. Complete A/N_omega with inner product <[a],[b]> = omega(a^*b), and define

    pi_omega(a)[b] = [ab],
    Omega_omega = [I].

This is the cyclic GNS representation. If another cyclic representation has the same state, the assignment pi(a)Omega -> pi'(a)Omega' preserves inner products and extends to a surjective unitary. Thus the cyclic carrier is fixed up to unitary equivalence.

This is mathematical uniqueness of presentation, not numerical identity between distinct concrete occurrences. It does not establish actual existence, experiential acquaintance, or an ontological priority of Hilbert space.

## 8. Derived local structure, entanglement, and bounded block entropy

The one-site state is

    rho_1 = I_3/3.

The two-site state is

    rho_2 = [|u><u| + I - F]/9.

Its nonzero eigenvalues are 1/3,2/9,2/9,2/9. Its support is precisely the kernel of h. The state is not a product of its one-site restrictions. More strongly,

    <u/sqrt(3) | rho_2^(partial transpose) | u/sqrt(3)> = -1/9.

Every separable state has a positive partial transpose; thus this negative witness establishes entanglement without a numerical eigensolver.

For any block size n the nonzero sector eigenvalues are

    lambda_0(n) = [1 + 3(-1/3)^n]/4,
    lambda_1(n) = lambda_2(n) = lambda_3(n) = [1 - (-1/3)^n]/4.

Proof: squared amplitudes within each Pauli sector are equal. The sector labels execute the four-state walk that moves to each of the other labels with probability 1/3. Its eigenvalues are 1,-1/3,-1/3,-1/3. Each Gram sector has rank one, so its total probability is its sole eigenvalue.

At n=1 the scalar eigenvalue vanishes; for every n>=2 all four are positive. The block entropy follows explicitly:

    S_n = -lambda_0 log(lambda_0) - 3 lambda_1 log(lambda_1),
    lim_(n->infinity) S_n = log(4).

The local mixedness, finite-block entanglement spectrum, and entropy saturation are consequences of the law. They are not separately assigned experience labels.

There is also a derived effective boundary space. Equip M_2(C) with its Hilbert-Schmidt inner product. The injective map W_n: M_2(C) -> (C^3)^(tensor n), B -> psi_B, has image exactly ker(H_n) for n>=2. Its polar normalization V_n = W_n (W_n^* W_n)^(-1/2) is an isometry from a four-dimensional space onto that support. Thus a block's supported state can be represented on a four-dimensional carrier for every n>=2; the dimension is derived from the local law, not chosen as an independent truncation. The choice of interval remains supplied, and these effective edges are not identified with boundaries of conscious subjects.

## 9. Derived correlations and an infinite Fourier sum

In the Cartesian basis take

    L_z = [[0,-i,0],[i,0,0],[0,0,0]].

Direct contraction gives

    E_(L_z)(I) = (2/3) sigma_z,
    E_(L_z)(sigma_z) = -(2/3) I.

Consequently, for site separation d >= 1,

    omega(L_z(j)) = 0,
    omega(L_z(j)^2) = 2/3,
    C(d) = omega(L_z(j) L_z(j+d)) = (4/3)(-1/3)^d.

Thus nearest-neighbor correlation is -4/9, next-neighbor correlation 4/27, and the correlation length is 1/log(3) in lattice units. There is no arbitrary correlation fit.

For arbitrary local blocks A and B separated by r identity sites, the connected correlation has the exact form c_(A,B)(-1/3)^r, by the transfer decomposition in section 2. This states clustering for all block observables, not just L_z.

Summing both directions gives the static structure factor

    S(k) = sum_(d in Z) exp(i k d) C(d)
         = 2(1-cos(k)) / (5+3 cos(k)).

Here C(0)=2/3 and C(-d)=C(d). The series is absolutely convergent. Cutting at |d|<=R leaves absolute error at most 4*3^(-(R+1)). In particular S(0)=0, S(pi/2)=2/5, and S(pi)=2. These are quantitative consequences of this mathematical model, not new experimental predictions about brains or fundamental physics.

## 10. What has and has not been constructed

**Relational-dynamics continuation:** [The clock-constraint construction](RELATIONAL_TIME_CONSTRUCTION.md) now uses this state as the input to a single stationary history with changing conditional correlations. It proves a constraint-commuting observable embedding for general C*-algebras, classifies path consistency by holonomy, and separates state preparation from the gauge constraint. It does not infer time from the static AKLT state alone.

**Constructed:** a fixed positive local law, its all-size ground-space solution, periodic uniqueness, a controlled infinite limit, compatible noncommutative restrictions, a unique global state extension and cyclic carrier, explicit entanglement, block spectra, and correlation functions. Finite exact computations check the formulas and rank statements; they do not replace the proofs.

**Supplied choices:** the integer adjacency, three-dimensional site space, Pauli auxiliary algebra, zero-energy coherence law, and periodic finite approximants. The construction does not establish why these are the actual or necessary choices. Other Hamiltonians can share ground states. No universality or complete physical foundation is claimed.

**Experiential status:** a restriction of omega is not thereby a conscious perspective. Neither Gamma nor chi is defined by this construction. The achievement is a mathematically determined common physical presentation on which a constitutive law could act; identifying owned qualitative acquaintance still requires positive warrant. The mathematics also supplies no axiology or reconciliation of every local privation with absolute perfection.

This is a worked infinite building block for [necessary articulated unity](NECESSARY_ARTICULATED_UNITY.md) and the [algebra/channel bridge](WORKSPACE_ALGEBRA_CHANNEL_BRIDGE.md). It replaces open-ended coherence vocabulary with a stated law and an explicit, generative solution. It does not claim the requested zero-residue account is complete.

### Mathematical lineage

I. Affleck, T. Kennedy, E. H. Lieb, H. Tasaki, *Rigorous results on valence-bond ground states in antiferromagnets*, Physical Review Letters 59 (1987), 799-802. M. Fannes, B. Nachtergaele, R. F. Werner, *Finitely correlated states on quantum spin chains*, Communications in Mathematical Physics 144 (1992), 443-490. These identify the established construction being used; the proofs and conventions needed here are specified above, rather than claiming a new review of those papers.
