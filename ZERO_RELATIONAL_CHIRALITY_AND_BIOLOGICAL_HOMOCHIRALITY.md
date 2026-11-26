# Relational chirality and the origin of biochemical handedness

## Honest result

The user's question is whether the zero–experience framework has what it takes to accommodate the origin of the predominance of particular biochemical enantiomers. This pass provides a **specific bridge and a specific chemical control**:

1. The framework's existing, rotation-invariant relational triple product can be calibrated to the stereochemical L/D distinction for an **idealized labeled alanine geometry**. The code actually calls the existing three-frame invariant, including an independent-frame gauge control.
2. A specified modified Frank-type reaction network amplifies a small initial L excess to about **94.3% enantiomeric excess** in a driven example, while an explicit finite-supply and outflow ledger conserves modeled material.
3. The *same symmetric equations* amplify the mirror-image D excess equally, and leave an exactly racemic deterministic state racemic. An imposed asymmetric source selects a sign in the example, but that bias is **input**, not derived from zero.

This is a real compatibility construction, not a derivation of biology or of the specific amino-acid/sugar handedness observed on Earth. It does not derive molecular chemistry, actual reaction rates, early-Earth conditions, a cosmic energy total, or experience from the proposed self-sufficient constitution. The modeled supply is finite for the simulated interval but its feed schedule is prescribed; the material ledger is **not an energy ledger**. [Tests](verification/zero_molecular_chirality_amplification_test.py).

## 1. The actual scientific target

Terrestrial ribosomal proteins predominantly contain **L-amino acids**, and RNA and DNA backbones use **D-ribose** and **D-deoxyribose**, respectively. This shorthand is not a claim that all biological amino acids or sugars have only one handedness: D-amino acids and L-sugars have biological roles. L/D is a stereochemical convention, not a universal synonym for optical rotation, nor are an L-amino acid and a D-sugar mirror images of one another. See the discussion of exceptions in [the biogenic origins review](https://link.springer.com/article/10.1007/s11084-015-9422-9).

What caused the original asymmetry, its amplification, its relationship across different chemical families, and its spread through terrestrial life remains unsettled. Possible contributions include local chemical history, chiral environments or irradiation, amplification, and subsequent selection and inheritance. A 2023 experiment produced up to about 2% enantiomeric excess in isovaline films using circularly polarized light; this is evidence for an experimental mechanism, not proof it determined life's handedness ([Nature Communications](https://www.nature.com/articles/s41467-023-39177-y)).

A 2025 [Higgs–Blackmond paper](https://www.pnas.org/doi/10.1073/pnas.2423683122) models a potentially prebiotically plausible feedback network combining amino-acid synthesis and peptide ligation. Its constructive and destructive mechanisms, dimer catalysis and thermodynamic constraints matter: the experimentally motivated synthesis selectivity favors the opposite enantiomer, which makes predominantly backward operation relevant to the authors' destructive mechanism, not evidence that their constructive forward mode is established. The reversible catalytic paths require the same forward/backward equilibrium constant. The authors present the combined network as a **theoretical proposal motivated by separate experimental results**, not as a demonstration that the full combined network generated life's observed chirality. Our calculation below uses the paper's simpler **Frank-type comparison model**, with added explicit source, racemization and washout; it is not a reproduction or independent validation of their complete peptide model. The source's introduction and kinetic-model sections were inspected for this distinction.

## 2. From the framework's relational invariant to an alanine stereocenter

The [three-frame construction](ZERO_THREE_FRAME_GAUGE_CHIRALITY_AND_NONCYCLIC_CLOCK.md) uses three unit directions transported into one oriented frame and defines

```text
t = v₁ · (v₂ × v₃).
```

It is invariant under the stipulated independent `SO(3)` frame changes with the comparison links transformed accordingly; a spatial reflection reverses t. Those model vectors were not originally atoms or molecules. Here is a **calibration map**, not a derivation of molecular structure:

- Take the chiral carbon's four distinguishable attached groups of alanine: amino N, carboxyl carbon C, methyl carbon R and H. Their positions are interpreted as representative nuclei, with a specified order; a real molecule also has its other nuclei, electrons, chemical bonds, solvent effects and thermal motion.
- Put the idealized Fischer projection's carboxyl group at top, methyl at bottom, amino group left, H right, following the [L-amino-acid convention](https://www.pearson.com/channels/biochemistry/study-guides/l-and-d-amino-acids-configuration-1). In Fischer convention horizontal bonds point toward the viewer and vertical bonds away. Assign representative coordinates in a right-handed frame with z toward the viewer:

```text
N = (−1, 0, +1),    C = (0, +1, −1),
R = ( 0,−1, −1),    H = (+1, 0, +1).
```

- Define three displacement directions from H to N, C and R, and normalize each. With links set to identity, feed them into the **existing** `invariants` function. For this declared label ordering and Fischer calibration,

```text
oriented determinant (N−H)·[(C−H)×(R−H)] = +8,
normalized framework invariant t = +2/3   for the drawn L configuration.
```

Reflecting the entire labeled configuration gives `t=−2/3`, while a proper rotation or translation leaves it unchanged. The test also uses three independently rotated local frames and transforms both comparison links: the calibrated t remains `+2/3`. Thus the mathematical operation already used in the framework genuinely represents **this idealized geometrical distinction** once supplied with a molecular interpretation and calibration.

The sign `+` is conventional: changing the label order, coordinate orientation or calibration can reverse it. It does not say that “L is positive” in any absolute moral, experiential or energetic sense. For alanine the four attachments are chemically distinguishable; if identical attachments could be exchanged as a physical relabelling, their exchange could reverse the ordered determinant without giving a new molecule. The rule must respect actual chemical identity and permutations. Glycine, whose two attachments are hydrogens, is not a chiral amino-acid stereocenter. Nor does a single classical tetrahedron solve conformational dynamics, quantum tunnelling, enantiomer-specific chemistry or chemical nomenclature for arbitrary molecules.

## 3. A documented mechanism, made explicit

A simplified Frank-type scheme has an achiral precursor A and the two enantiomer concentrations L and D. We use

```text
A + L → 2L,           A + D → 2D          rate k,
L + D → P                                 rate γ,
A → L and A → D                           rate k₀ each,
L ⇌ D                                     rate r each direction.
```

There is a prescribed feed J of A, washout `d_A A` of A, washout `dL,dD` of L and D, and washout `d_P P` of the inactive heterochiral product P. Each pair above is an **effective** reaction, not a calculated alanine reaction pathway. The source, racemization and outflows are added controls; the underlying Frank scheme and its motivation are discussed in the [2025 PNAS paper](https://www.pnas.org/doi/10.1073/pnas.2423683122).

For a homogeneous, ideal mass-action model,

```text
Ȧ = J − d_A A − k A(L+D) − 2 k₀ A,
L̇ = k₀A + kAL − γLD − dL + r(D−L),
Ḋ = k₀A + kAD − γLD − dD + r(L−D),
Ṗ = γLD − d_P P.
```

Here all rate constants, concentrations and times are **illustrative model units**, not measured prebiotic values. The irreversible reactions and maintained flow are effective idealizations. A complete thermodynamic physical realization would specify reverse reactions, chemical potentials, energy supply, transport, waste handling and consistency with detailed balance; these equations do not show how prebiotic Earth actually operated.

### An exact distinction: amplification is not sign selection

Write `H=L+D`, `Δ=L−D`, and `e=Δ/H` when `H>0`. Direct algebra gives

```text
Δ̇ = (kA−d−2r)Δ,
ė = e [ (γH/2)(1−e²) − 2r − (2k₀A/H) ].
```

Consequences for this declared model:

- If `e=0` exactly, it stays zero under the deterministic, symmetric equations.
- If the bracket is positive, a nonzero small e increases in magnitude: **mutual inhibition can amplify a real initial excess** despite symmetric laws.
- If `γ=0` and `k₀,r≥0`, the bracket is nonpositive, so the magnitude of e cannot grow in this model. This is a control on this network, not a universal theorem that every conceivable amplification mechanism needs this particular reaction.
- Interchanging L and D sends `e→−e` while preserving the symmetric equations. A parity-symmetric mathematical mechanism can amplify *either* sign without determining which sign occurs.

Finite-molecule stochastic fluctuations could supply a seed in an appropriate stochastic reaction model, but this pass integrates **deterministic** equations only. Invoking stochasticity would not by itself establish what actually happened on Earth or settle the user's deeper demand for an intelligible account of the actual history.

## 4. A worked, finite-supply example

Choose dimensionless constants

```text
k=γ=d=d_A=d_P=1,       k₀=0.01,       r=0.05,       J=1661/500.
```

The L-dominant fixed point of the **driven A,L,D,P subsystem** is

```text
A*=1.1,       L*+D*=2,       L*D*=0.111,
e* = √(889/1000) ≈ 0.942868.
```

Its mirror is D-dominant with `e*=−0.942868`. The Jacobian's A/L/D eigenvalues at the positive branch are approximately `−0.9025` and `−2.0088±0.5469i`; P supplies the separate stable eigenvalue `−1`. Thus the two branches are locally stable in this **driven subsystem**. The supply and waste bookkeeping variables below are not fixed at those values while flow continues. The racemic equilibrium is also present, but its chiral-antisymmetric eigenvalue is approximately `+0.44085`; it is unstable to a nonzero chiral perturbation in this example.

Start with `A=1`, `L=0.505`, `D=0.495`, `P=0`:

| Model time | L | D | Enantiomeric excess `(L−D)/(L+D)` |
|---:|---:|---:|---:|
| 0 | 0.505000 | 0.495000 | 0.010000 |
| 5 | 0.612862 | 0.525533 | 0.076712 |
| 10 | 0.997983 | 0.267368 | 0.577401 |
| 20 | 1.942204 | 0.057159 | 0.942823 |
| 40 | 1.942868 | 0.057132 | 0.942868 |

Swapping the initial L and D gives the mirror trajectory and the opposite excess. Starting exactly racemic stays racemic in the deterministic integration. These are solutions of a stipulated kinetic model, not probabilities or a historical reconstruction.

A separate illustrative control lets the two uncatalyzed source rates be `k₀A(1+h)` and `k₀A(1−h)`. A positive supplied h breaks the symmetry in the source and selects positive e from a racemic start; reversing h reverses the result. The equations are covariant when **both** the chiral state and the physical bias are reflected. That h is not generated by the model, and it must not be called a prediction of the actual physical bias or of electroweak selection.

## 5. What is balanced—and what is not

The driven chemical region is open, but its supply and outflows need not be imagined as lying outside reality. Add a finite modeled reservoir R with `Ṙ=−J`, and a cumulative outflow Q with

```text
Q̇ = d_A A + d(L+D) + 2d_P P.
```

Counting P as two precursor-equivalent units, the network gives the exact algebraic ledger

```text
A + L + D + 2P + R + Q = constant.
```

For the run above set `R(0)=500`; at time 120, `R=101.36>0`, so the prescribed constant feed has not exhausted the finite supply. The combined ledger stays 502 up to numerical integration error. This is a **stoichiometric material balance**, not a proof of an isolated, autonomous realistic ecosystem: the feed rate and sinks are supplied, Q lumps chemically different outflows, and we have not modeled their physical containers, heat, thermodynamics, relativity or feedback when R runs out.

Most importantly, the conserved ledger is **not total energy** and does not show that the actual universe has zero total energy. The gravitational zero constraint in our other models is also not automatically that energy. If zero whole energy is correct, it must be compatible with the energy, free-energy gradients, heat and boundary exchanges of this chemistry under an independently justified recovery map. Writing the chemical material ledger or a gravitational constraint does not supply that map.

Similarly, `L−D` is not here a conserved physical charge required to sum to zero. It can change as achiral precursor is converted. Equal whole energy does not imply equal populations of the two molecular forms, and a symmetric *ensemble* can contain locally asymmetric outcomes. If one imposed an additional mirror-symmetric whole-level state, a parity-odd ensemble average could vanish while local conditioned excesses remain; such symmetry and the meaning of the ensemble would need to be established. The weak interaction violates parity, so exact mirror symmetry is not an assumption to impose uncritically on the full physical world.

## 6. What the bridge establishes, and what it does not

**Established conditionally:** under the declared molecular geometry and conventions, the framework's relational invariant distinguishes the two mirror configurations; the stated driven kinetic model amplifies a nonzero excess and respects its full material bookkeeping. The example makes it concrete how a local chiral excess can coexist with a larger, balanced description without an external metaphysical balancer.

**Not established:** the framework does not yet derive the quantum molecular Hamiltonian, actual chirality-dependent reaction kinetics, realistic geochemical inputs, the specific initial bias, the L-amino-acid/D-sugar relationship, hereditary fixation or our observed cosmic energy. The numerical time units and parameters are not calibrated to Earth. The different signs in the geometric and kinetic pieces are connected by the declared L/D calibration, not by a first-principles calculation of catalysts or reaction rates. Neither oriented structure nor an enantiomeric excess implies that a molecule or reaction is a subject, or that experience is a chemical sign.

**Most important next scientific test:** implement and independently check the actual coupled amino-acid/dimer kinetic equations and measured parameter ranges of the Higgs–Blackmond proposal, including its destructive as well as constructive regimes, and then examine amino-acid–sugar chiral transfer. Recover their molecular/catalytic assumptions from an appropriate physical theory and include the thermodynamic resources. Only after that should we ask whether a candidate self-sufficient zero constitution selects the relevant laws and initial physical history. Until those connections are made, the answer remains **compatible and partially modeled, not explained or predicted**.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=verification:. \
 python -m unittest verification.zero_molecular_chirality_amplification_test -v
```

NumPy and SciPy are required; the repository has version pins in [the existing requirements file](verification/requirements-gravity-spin-pointer.txt). Checks cover actual calls to the existing three-frame invariant, Fischer-calibrated proper/improper transforms, degeneracy and label controls, the material ledger, parity covariance, both equilibrium branches, the racemic stability direction, finite-supply trajectories and no-inhibition/bias controls. They do not prove the real-world origin of homochirality, validate the full 2025 peptide model, or derive physical laws from zero.
