# ER = EPR, the firewall, and actual access in the sphere echo

**Related continuation:** [Structural time, DATA and the sphere echo](ZERO_DATA_STRUCTURAL_TIME_AND_SPHERE_ECHO.md) calculates the B information accessible from the echo record at every tick and distinguishes a retained copy from the original unmodified reversal.

**Source:** K. C. Cole, [“Wormholes Untangle a Black Hole Paradox”](https://www.quantamagazine.org/wormhole-entanglement-and-the-firewall-paradox-20150424/), *Quanta Magazine*, 24 April 2015. I checked the original [AMPS paper](https://arxiv.org/abs/1207.3123v4), [Maldacena–Susskind ER = EPR proposal](https://arxiv.org/abs/1306.0533v2), and the later [Gao–Jafferis–Wall traversable-wormhole construction](https://arxiv.org/abs/1608.05687v3). The sphere calculation is checked by [the verifier](verification/zero_er_epr_access_teleportation_test.py).

## Result

The article connects two ideas central to our recent work: a single whole can contain nonlocal quantum correlations, but the meaning of those correlations depends on **which parts are independent and which interfaces are physically available**. It does not establish that every entangled pair is a traversable wormhole or that the firewall problem has been solved.

A concrete test on our **existing sphere/source/echo** makes the distinction quantitative. If one adds a standard qubit-teleportation intervention using the actual first source–reference pair, the usable channel depends on the clock reading and whether the conserved sphere-sector record B is actually available:

* Just after the source interface, the pair is Bell-entangled conditional on B; with B and the required classical messages, the ideal protocol transmits an unknown qubit with unit fidelity. Without B, the same protocol is only a dephasing channel.
* At the echo midpoint, the record `r` contains B, but knowing B alone does **not** restore the pair's lost coherence. The same protocol is then only a dephasing channel even with that record.
* Reversing the original full program restores the initial Bell pair. This is recovery via a specified global inverse, not communication supplied by entanglement alone.

These are predictions of an ideal intervention *if* its input, measurements, receiver, B access and message channels are supplied. The original sphere program has no teleportation device or demonstrated confined observer. Performing the intervention changes the experiment; its later evolution cannot simply be identified with the untouched echo.

## 1. What AMPS and ER = EPR actually say

The [2012 AMPS paper](https://arxiv.org/abs/1207.3123v4) argues that three assumptions cannot all be maintained in its black-hole setting: (i) unitary evaporation/pure Hawking radiation, (ii) appropriate low-energy effective field theory outside a microscopic horizon neighborhood with information emitted from there, and (iii) a smooth “no drama” horizon for an infalling observer. The common short version concerns a late outgoing mode B, early radiation R, and an interior partner A. For an old black hole, purification requirements can make the late mode strongly correlated with a suitable **subsystem or decoded degree of freedom of the early radiation**, while a smooth horizon calls for the relevant near-horizon pairing. Treating all three as independent systems leads to the monogamy tension.

The exact elementary fact is: if `ρ_AB` is a pure maximally entangled state, then any larger state with that marginal has the form `ρ_AB⊗ρ_R`. A cannot simultaneously be maximally entangled with a **second independent** R. Generic quantum states can have shared, nonmaximal entanglement; monogamy is not a prohibition on all multipartite correlations. The independence and operator-identification assumptions are central in gravity, where subsystem factorization is subtle.

[Maldacena and Susskind (2013)](https://arxiv.org/abs/1306.0533v2) relate certain entangled black holes to an Einstein–Rosen bridge and propose a broader connection between entanglement and geometry. They discuss possible resolutions of versions of the paradox. This is a research proposal, not a general experimental theorem that each EPR pair possesses an ordinary smooth, macroscopic bridge, that interior and exterior operators are always interchangeable, or that AMPS is universally resolved. The article itself records significant contemporary disagreement.

Two popular metaphors need qualification. Measuring one member of an entangled pair does not make an arbitrary controllable action happen at the other, and cannot by itself signal. Hawking radiation is derived from quantum fields in curved spacetime; the “one virtual particle falls in, one escapes” story is a heuristic, not a literal universal microscopic mechanism. Negative Killing-energy flux in an appropriate black-hole calculation is not a proof of negative cosmic energy or negative felt experience.

## 2. Entanglement is not, by itself, an open passage

The two-sided eternal black-hole bridge used in the basic ER = EPR discussion is not automatically traversable. The later [Gao–Jafferis–Wall result](https://arxiv.org/abs/1608.05687v3) makes a specified bridge traversable by introducing an interaction between its two boundaries; in their model a quantum stress tensor with negative average null energy backreacts on the geometry. Their construction does not allow causal paradoxes. [Maldacena, Stanford and Yang](https://arxiv.org/abs/1704.05333) connect certain traversable-wormhole processes to teleportation in a specific nearly-AdS₂ setting.

That is a highly structured gravitational duality, not a statement that ordinary entanglement gives a controllable channel without interaction. The standard quantum teleportation protocol uses a shared entangled resource **and** a Bell measurement, a classical message of two bits and a receiver correction. It transmits a quantum *state*, not a material body, and does not exceed the speed allowed by the actual classical channel. A hypothetical route between our subject realms has to be similarly specified rather than inferred from a formal correlation.

## 3. The actual sphere resource, before any teleportation intervention

The preceding [tensor-network analysis](ZERO_TENSOR_NETWORK_SPHERE_STEERING_AND_ECHO.md) identified the first source S and reference F in the actual B-controlled interface. Use `b=0,1` for the conserved B sector. The full old history has each B value with weight `1/2`. Immediately after the source interface,

`ρ_SF|b=0 = |Φ+⟩⟨Φ+|`,

`ρ_SF|b=1 = |Ψ+⟩⟨Ψ+|`, with `|Ψ+⟩=(I⊗X)|Φ+⟩`.

Without B, the reduced state is `(I+X_S X_F)/4`, a separable mixture, even though `⟨X_S X_F⟩=1`. A sharp coherence witness relative to the reference Z flag is therefore not itself proof of entanglement across S:F or proof of a wormhole. The *full* pure state can still have entanglement between the pair SF and its complement.

For the actual 20-step program, the new verifier computes the **B-conditioned** pair at every tick using the true correlated old `(b,z,s)` Born law and the original thermal reservoir. With the stated reference convention:

| Tick(s) | Pair if B is unavailable | Pair conditioned on `b` |
|---|---|---|
| 0, 20 | `|Φ+⟩` | `|Φ+⟩` |
| 1, 19 | `(I+XX)/4` | `|Φ_b⟩` |
| 2–18 | `I/4` | `(I+(−1)^b ZZ)/4` |

The table is unchanged for the two checked auxiliary preparations: clean and thermal `q=1/4`. At tick 10, the existing echo memory obeys `r=b` on the supported inputs. Therefore a party with a physical interface to `r` can acquire B there, but that does not make the pair Bell-entangled again. The B-conditioned middle state is already separable: information about the missing phase remains in other degrees of freedom.

The conditional pure Bell pair also illustrates the precise monogamy premise: at tick 1, after conditioning on B, the pair's pure density matrix factors from the other two source/reference pairs. It cannot at the same time be maximally entangled with a second **independent** partner. This is an exact property of the modeled state, not an AMPS black hole or a claim that our B-sector bookkeeping resolves the firewall paradox.

## 4. A specified teleportation intervention

At a selected clock reading, suppose a sender can couple a fresh unknown input qubit Q to S, perform a Bell measurement on Q,S, and transmit its two outcome bits to a receiver who can act on F. If B is supplied to the receiver when relevant, the receiver also applies `X^b` to correct the B-dependent Bell label. These are **additional operations and access assumptions**, not parts of the untouched 20-step circuit. They may alter its subsequent dynamics and charge/resource accounting.

For the standard protocol, averaged uniformly over unknown pure input qubits:

| Tick(s) | If B is not used | If B is supplied and corrected |
|---|---:|---:|
| 0, 20 | `1` | `1` (B unnecessary) |
| 1, 19 | `2/3` | `1` |
| 2–18 | `1/2` | `2/3` |

The verifier obtains the channels, not just the averages:

* At ticks 0 and 20: `ρ ↦ ρ`.
* At 1 and 19 without B: `ρ ↦ (ρ+XρX)/2`. Knowing B converts the selected Bell state to `|Φ+⟩` and gives `ρ ↦ ρ`.
* At 2–18 without B: `ρ ↦ I/2`. With B and the specified correction: `ρ ↦ (ρ+ZρZ)/2`.

The `2/3` value is the classical benchmark for transmitting a uniformly unknown pure qubit without an entangled resource under the usual deterministic measure-and-prepare assumptions; see [Horodecki et al.](https://arxiv.org/abs/quant-ph/9807091v2). The `1/2` entry is **not** a universal upper bound on every possible LOCC strategy: a party could ignore the `I/4` resource and use an ordinary measure-and-prepare strategy achieving `2/3`. It is the result of the specific standard teleportation circuit tested here. Nor are these values optimization claims over joint access to the whole reservoir, purifiers or arbitrary interventions.

At tick 10, `r=b` is an existing physical correlation, so the B-corrected `2/3` case is attainable only if the receiver or an authorized communicating party can actually read and use that echo memory. This is exactly where the realm distinction bites: a formal global observable or conserved sector does not automatically supply a confined inhabitant with the record or the sender/receiver channel.

## 5. No message without an interface

If the sender performs the Bell measurement but the two measurement bits are **not delivered**, the receiver's reduced state is `I/2` for every tested input and every B sector. More generally, a local trace-preserving operation on the sender's side cannot change the receiver's reduced state without a physical interaction or communication channel. Selecting a particular post-measurement branch is conditionalization; making its label available elsewhere is an additional physical action.

This distinguishes four things the article's wormhole metaphor can otherwise blur:

1. a joint entangled state;
2. the existence of a mathematical relation or a global witness;
3. an implemented, causally permitted information channel; and
4. a subject's actual access to that channel or experience of it.

The demonstrated B–j–memory correlations satisfy the first two in appropriate cuts, but they do not establish the latter two for a confined surface inhabitant. Our reversible inverse is a global operation with specified gate access, not an inhabitant leaving its realm or a classical signal sent through an inferred wormhole.

## 6. Connection to the one-reality and zero program

ER = EPR is congenial to the idea that distinct local descriptions can belong to one underlying reality. The concrete lesson is nevertheless **not** that every correlated part is literally the same subject, that arbitrary distinct realms exchange signals, or that an entanglement edge is automatically spatial geometry. A proposed identification must specify a dictionary and the physical observable algebra; otherwise identifying two alleged independent partners merely avoids, rather than resolves, the monogamy question.

Our sphere calculation ties that lesson to an actual record and a quantitative protocol: B access changes a usable channel, while the uncomputed environment is needed to recover coherence. It preserves the 20-step history, the difference between physical signed charges and candidate felt valence, and the requirement that genuine subjective incidence be justified rather than inferred from a Bell pair.

The black-hole sources do not derive a whole-level objective energy of zero or prove that negative physical energy is negative experience. The constructive task remains to determine how the one reality's own constitution supplies the physical differentiation, actual subject and quality, their accessible interfaces and their incidence weights—without treating a wormhole metaphor, a tensor edge or a balancing equation as a substitute for those relations.
