# PSR-5 R0 review — correction after the later adjudications

## Correction and disposition

**I withdraw my earlier conclusion that PSR-5 did not pass R0.** The argument I supplied does not demonstrate a failure of the frozen R0 rules or two non-isomorphic outputs from a single fixed decoder. It also overlooked later records reporting R0–R3 execution and completion. The prior version of this review remains in Git history at commit `e9cbf34`; this corrected document supersedes its verdict.

The linked [second-wave documents](psr-5%20battery/2nd%20wave/) explicitly report an R0 pass and, in the R3.c adjudication, **completion of the restricted formal-interface battery**. The entry review itself was admission-only, but it was not the end of the chain. Completion is the documented docket outcome; it does not imply a public-truth bridge, discharge the declared instantiation/experience residual, establish consciousness or empirical QM/GR recovery, or establish zero residue. Those limitations are stated by the documents themselves, not grounds to erase their restricted pass.

I have not independently replayed the entire battery. The user has now supplied the R1 adjudication, and its SHA-256 matches the reference in R2; all six stage adjudications can therefore be inspected. The submitted R1–R3 audits themselves are not in the supplied folder. Thus I can verify the **reported completion** and inspect the adjudications, not independently verify every missing document. [The companion analysis](ZERO_PSR5_SECOND_WAVE_ADJUDICATION_AND_LESSONS.md) gives the source chain, an independently checked Ring5 calculation and implications for our own candidate.

## What my example actually showed

The frozen [packet](psr-5%20battery/Plural_Structural_Realism_Entry_Packet_v5.md), SHA-256 `b0d2a0fe6c72f19437aa1804230d0c2ba41c26a878a26deffbf50bd93d901321`, assigns macro `010` to the fixed record `S_with`. It says that record is a nonisomorphic structural candidate with one `Ag` role, no physical field and no instantiation. I questioned whether the packet text makes every field of that fixture unambiguously reconstructible, including the scope of its unlisted-fields convention. That is a **fixture clarification question**; it is not the parse-ambiguity or fixed-decoder counterexample that my prior disposition made it sound like.

The exact alias I used was:

```text
111011010100 = 1110 · N(2) · N(0)
N(2)=11010,  N(0)=100.
```

It has one parse: alias branch, fixture index `i=2`, permutation index `r=0`. It is accepted when `S_with` has one role, since `0<1!`. The two records I compared were two **hypothetical, alternative completions** of the fixture description, not two parses or two outputs of one fixed decoder:

```text
A: U={0}; τ(0)=Ag; ρ=κ=η=α=Φ=∅;
   ν(0)={instrumentalized:0}.
B: U={0}; τ(0)=Ag; ρ=κ=η=α=Φ=∅;
   ν(0)={instrumentalized:1}.
```

They are nonisomorphic under an isomorphism that preserves ν: the only carrier bijection sends `0` to `0`, where the values differ. The conditional observation is that the words “one Ag-role and no physical field” alone do not distinguish them **if** no additional fixture constraint or unlisted-field default applies. It does not establish that both are admissible under the packet as a whole, that either is the intended fixed `S_with`, or that `111011010100` has two outputs in the same PSR-5 model. My prior wording improperly promoted this interpretive concern into a decisive R0 non-pass.

For any **fixed** record `S_i`, any two carrier permutations are signature-preserving isomorphic: if `π_r(S_i)` and `π_s(S_i)` are the transported records, the bijection `π_s ∘ π_r⁻¹` preserves every transported field. A missing or implicit raw carrier-order convention would not make these two records nonisomorphic. The self-delimiting natural code and the disjoint macro/alias/trivial prefixes likewise do not support an ambiguous parse claim.

There is no demonstrated post-adjudication R0 reversal here. A request to make the full `S_with` and `S_noncand` records and default conventions explicit could help reproducibility in a **fresh** candidate or clarification; whether and how to do that is not a finding that the recorded restricted-formal R0 result is invalid. No change to the frozen packet has been made.

## Reproduce the bounded checks

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_psr5_adjudication_correction_test \
  verification.zero_psr5_global_decoder_r0_test -v
```

These tests check document hashes, the unique parse of the cited example, a finite illustration of permutation transport, the two conditional record completions, and the ten Ring5 checks. The self-delimiting property and permutation-isomorphism reasoning are general mathematical arguments; bounded enumeration alone is not a proof. The checks are not a replay of the full external battery or a substantive zero-residue result.
