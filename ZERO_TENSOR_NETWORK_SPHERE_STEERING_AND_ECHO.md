# Tensor networks, the actual sphere pair, and an internal projective sphere

**Source:** Jennifer Ouellette, [“How Quantum Pairs Stitch Space-Time”](https://www.quantamagazine.org/tensor-networks-and-entanglement-20150428/), *Quanta Magazine*, 28 April 2015. I also checked [Swingle’s entanglement-renormalization proposal](https://arxiv.org/abs/0905.1317), [Ryu and Takayanagi’s holographic entropy paper](https://arxiv.org/abs/hep-th/0605073v3), and [Swingle and Van Raamsdonk’s gravity-from-entanglement paper](https://arxiv.org/abs/1405.2933). The calculations below use the **existing** sphere/source/reservoir circuit, with checks in [the verifier](verification/zero_tensor_network_sphere_pair_echo_test.py).

## Result

The article motivates a precise connection between entanglement structure and geometry. Applying a small tensor network to our *actual* B-controlled three-source interface yields a more specific result than the general slogan:

* Each source–reference pair is a Bell pair **conditional on the conserved sphere sector B**, but the unconditioned first pair is separable. It nevertheless has a sharp coherent parity `X_S X_F=+1`.
* The **pair as a whole** is entangled with the rest of the pure state. During the actual 20-step record/echo cycle, the source–reference pair's internal entanglement disappears while its entanglement with the rest can increase; the reverse program restores the original Bell pair. The relevant partition matters.
* A fixed-B Bell pair lets a source measurement prepare **every projective ray of the physical reference qubit**, mathematically a `CP¹` sphere. Without the B record, that same source-only steering is restricted to a line segment of the Bloch ball. This gives a concrete, interface-dependent connection to the earlier [point–sphere/Lorentz-cone construction](ZERO_POINT_SPHERE_TO_LORENTZ_CONE.md), not a derivation that the two spheres are physically identical.

The tensor network is an exact representation of the stated interface, not proof that its graph is physical space, that every ray is an actual subject, or that the input tensors follow uniquely from zero. The detailed results below sharpen those distinctions instead of treating the words “entanglement” and “geometry” as interchangeable.

## 1. What the article contributes

The 2015 article explains tensor networks, multiscale entanglement renormalization (MERA), holographic duality and the idea that patterns of quantum entanglement may be related to spatial geometry. It highlights that the *distribution* of correlations matters, not merely the presence of a pair of entangled systems.

A tensor network is a factorization of a many-index amplitude into local tensors joined by contracted indices. Some states admit compact, useful approximations of this form; an arbitrary many-body state need not have an efficient fixed-bond representation. A virtual edge is an index in a representation, not automatically a physical wire, accessible communication channel or piece of spacetime. A MERA is a particular multiscale architecture involving disentanglers and coarse-graining isometries, not simply any tree of paired qubits. An electron also need not interact *only* with its nearest neighbors; locality and truncation are model-dependent approximations.

Swingle's [proposal](https://arxiv.org/abs/0905.1317) relates multiscale organization of certain quantum states to a higher-dimensional discrete geometry; its critical-state example resembles a spatial slice of anti-de Sitter space. The static Ryu–Takayanagi construction relates entanglement entropy of specified boundary regions to extremal/minimal bulk areas under an AdS/CFT dictionary and stated semiclassical assumptions. Such results do not identify every tensor diagram with a gravitational geometry.

The article's broad “Einstein’s equations” description also needs a scope check. [The specific 2014 source it links](https://arxiv.org/abs/1405.2933) studies infinitesimal perturbations of a large-N holographic CFT vacuum and linearized Einstein equations about AdS, with semiclassical bulk stress-energy appearing at the relevant order. This is an important conditional result, not a derivation of the full nonlinear equations, our cosmology, or an equivalence principle from arbitrary entangled qubits. A physical boundary theory, state, region structure, dictionary and applicable approximation are part of the explanation.

## 2. A general tensor cut is an upper bound, not automatically an area law

If a finite pure-state tensor network is cut between physical regions `A` and `Ā`, and the severed virtual edges have dimensions `χ_e`, contraction expresses the state as a sum of at most `∏χ_e` product terms across that partition. Hence

`Schmidt rank(A:Ā) ≤ ∏_e χ_e`,

`S(A) ≤ Σ_e log₂ χ_e`.

The bound is exact as an inequality, but equality requires additional properties of the tensors and the chosen cut. One may even pad an existing bond with unused dimensions without changing the physical state: the verifier embeds our exact `χ=2` network into `χ=4`, with all physical amplitudes unchanged. The new cut capacity is two bits, but the actual entropy remains one bit. Thus the drawn bond count by itself is not an observable area, and even a minimal network depends on which physical factors and partitions are declared relevant.

## 3. Exact tensorization of the existing three-pair interface

The established model starts from three Bell source/reference pairs and applies the actual sphere-sector-controlled interface. Label the conserved sphere sign by `b∈{0,1}` and the pair states by

`|Φ_b⟩_SF = (|b,0⟩ + |1 XOR b,1⟩)/√2`.

`b=0` is `|Φ+⟩` and `b=1` is `|Ψ+⟩`. For the old coherent state, let its normalized B-sector components be `|χ_0⟩,|χ_1⟩`; they are orthogonal. The actual old W histories have weight `1/2` in each B sector, checked at all 16 original labels. Immediately after the source interface the full pure state can be written

`|Ψ⟩ = ( |χ_0⟩ |Φ_0⟩_0|Φ_0⟩_1|Φ_0⟩_2 + |χ_1⟩ |Φ_1⟩_0|Φ_1⟩_1|Φ_1⟩_2 )/√2`.

This is an exact rewrite of the interface, including the old-sector vectors, not a replacement of the sphere by an independent spectator. In logical B coordinates it has the tensor amplitude

`Ψ(b,s_0,f_0,s_1,f_1,s_2,f_2) = (1/4) ∏[i=0..2] δ_(s_i, f_i XOR b)`.

An explicit matrix-product network with sites `B,(S_0F_0),(S_1F_1),(S_2F_2)` and virtual dimension `χ=2` contracts to precisely this state. Across each displayed MPS cut, its Schmidt rank is 2 and entropy is 1 bit, so the one-bond bound is saturated **for this network and these cuts**. Replacing the logical `|b⟩` with the actual normalized `|χ_b⟩` is an isometric embedding and preserves the pair-versus-rest statements.

The program's conditional source relations and its two distinct finite charge ledgers remain as previously verified. The MPS graph is not an extra physical sphere or an already constructed AdS geometry.

## 4. Conditional Bell entanglement versus the actual unconditioned pair

Conditioning on an accessible B outcome gives `|Φ_b⟩`; source and reference then share one ebit. But if the old system and the other pairs are traced out, the first pair is

`ρ_SF = (|Φ+⟩⟨Φ+| + |Ψ+⟩⟨Ψ+|)/2 = (I+X_S X_F)/4`.

This state is **separable**:

`ρ_SF = (|++⟩⟨++| + |−−⟩⟨−−|)/2`.

Its two individual states are maximally mixed; `S(S)=S(F)=1`, `S(SF)=1`, and mutual information `I(S:F)=1` bit. Its entanglement negativity is zero, yet `⟨X_S X_F⟩=+1`. The same physical state therefore has definite joint parity and classical correlations without source–reference entanglement on that reduced cut.

This qualifies, rather than contradicts, the earlier [coherence-witness calculation](ZERO_IDENTITY_PAIR_PHYSICAL_FLAG_AND_INCIDENCE.md). The operator `D=X_S X_F` detects coherence **between reference-flag sectors relative to the Z-flag dephasing**; it is not by itself an entanglement witness for the unconditioned S:F pair. Conditional on B, the pair is maximally entangled. Also, because the full prepared state is pure, `S(SF)=1` means the **joint pair SF is entangled with its complement** by one bit. These are three different statements about three different partitions or conditions.

Access to B is a physical requirement. A mathematical conditioning on B is not automatically a measurement by a surface inhabitant; measuring B can disturb coherence between the two old B sectors, and the apparatus and observer must be included if that intervention is performed. The fact that a mathematical tensor edge connects B to a pair does not itself supply such an interface.

## 5. What the actual 20-step echo does to that pair

For the stipulated thermal reservoir `q=1/4`, and for both a clean auxiliary bit and the checked auxiliary thermal case `q=1/4`, the exact first-pair reduced state is:

| Clock readings | `ρ_SF` after tracing old state, records and purifiers | `⟨X_S X_F⟩` | `S(SF)` bits | S:F negativity |
|---|---|---:|---:|---:|
| 0 and 20 | `|Φ+⟩⟨Φ+|` | 1 | 0 | 1/2 |
| 1 and 19 | `(I+X_S X_F)/4` | 1 | 1 | 0 |
| 2–18 | `I/4` | 0 | 2 | 0 |

The exact reduced-state calculation follows the actual correlated `(b,z,s)` Born distribution, source/reference labels, thermal purification, finite stores and echo labels. As an additional check, it holds in two hypothetical ensembles with each j label fixed and B balanced; those ensembles are not the actual distribution conditioned on j. The old quantum T/Q echo and all 16 W histories are separately checked by the existing sphere verifiers. The table is about **clock-conditioned subsystem states** in that model, not an assertion that the stationary whole literally evolves relative to an external clock.

If the complete conditioned state is kept pure, including the thermal and auxiliary purifiers, `S(SF)` is also the entanglement entropy between **SF and all the rest**. At ticks 2–18 the two local qubits are mutually uncorrelated (`I(S:F)=0`), while the pair as a unit has two bits of entanglement with its complement. Thus losing a visible pairwise “link” is not the same thing as tearing the whole apart; correlations have been redistributed. The transported global witness remains sharp, and the inverse program returns the initial Bell pair. The diagram's virtual connectivity, reduced mutual information, entanglement across different cuts and physical accessibility cannot be conflated.

This does not show that a gravitational spacetime pinches or expands during the echo. It shows how to pose such a claim correctly: specify the physical regions and complete state, a geometry dictionary, an appropriate entropy/cut, and the observable being reconstructed.

## 6. The actual reference qubit has a projective sphere—but its access is conditional

The first reference is a real qubit in the circuit, so its pure-state ray space is `CP¹`, mathematically a two-sphere. Let `|u⟩` be any normalized source-qubit measurement direction. In a fixed B sector,

`⟨u|_S Φ_b⟩_SF = (1/√2) X^b |u*⟩_F`.

Each outcome has probability `1/2`, and varying `|u⟩` reaches every reference pure ray. This gives the earlier abstract `CP¹` construction a concrete **candidate carrier and relation** inside the actual apparatus. It does not prove the proposed whole-level point's inner sphere is this particular qubit's ray space; identifying them and establishing physical Lorentz geometry are additional claims. The ray sphere is a space of possible preparations/readouts, not automatically a census of actual subject incidences.

Without the B record, the same source measurement on the actual unconditioned pair gives

`ρ_F|u = (I + ⟨u|X|u⟩ X)/2`.

As `u` varies, this ranges only over the **X-axis segment** of the Bloch ball; only its endpoints are pure. In other words, the full `CP¹` steering relation is available only on the specified B-conditioned Bell branch, not from the unconditioned S:F state alone. At the middle of the echo the reduced pair is `I/4`, so the original pairwise steering relation is not automatically available there either. This is a concrete instance of the user's realm constraint: richer global relations do not become a confined observer's experiences without the relevant interface.

The algebraic [projective-sphere-to-cone map](ZERO_POINT_SPHERE_TO_LORENTZ_CONE.md) then remains available as a mathematical construction: a chosen `C²` lift produces a determinant light cone in Hermitian matrices. But the particular qubit, physical identification of rays, spacetime scale, observable Lorentz structure and access are not derived by the tensor factorization or by zero alone.

## 7. What this advances in the one-reality program

This is a constructive synthesis of the article with the existing model: the same sphere-controlled quantum state supports a small exact tensor representation, conditionally maximal pair entanglement, globally redistributed correlations, a reversible relational clock, and a physically instantiated `CP¹` ray space. The different descriptions are tied by equations and checked on the actual circuit.

It also makes the no-residue task sharper. The whole's proposed zero cannot be substituted for a tensor, a preferred cut, a holographic dictionary, a subject boundary or a felt-quality rule. The physical source–reference qubit is a concrete candidate for the mathematical sphere, but the identification and its subjective significance remain to be obtained from the one constitution. No tensor edge has been promoted to an experiencer; no signed charge has been identified with felt valence; no local suffering is removed by a whole-level cancellation.
