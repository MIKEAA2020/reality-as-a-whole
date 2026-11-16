# External source excerpts for the consonance audit

These are small, public, aggregate chord-level tables—not individual listener records. They are retained for reproducibility of [the analysis](../../BOWLING_PAIRWISE_RELATIONAL_EMPIRICAL_GATE.md). The primary study is Bowling, Purves and Gill, *Vocal similarity predicts the relative attraction of musical chords* (2018), [DOI 10.1073/pnas.1713206115](https://doi.org/10.1073/pnas.1713206115). Attribute the primary authors and the intermediate data providers; neither data provider is an independent new participant sample.

## DCMLab consonance

- Source: [DCMLab/consonance](https://github.com/DCMLab/consonance/tree/a13bcb0a52ac41cff9647e8b6406aed32a8250c6), commit `a13bcb0a52ac41cff9647e8b6406aed32a8250c6`; authors Hall, Tamir and Rohrmeier, [2025 article](https://doi.org/10.5334/tismir.243).
- `dcmlab-consonance/bowling2018_consonance.tsv`: 5,132 bytes; SHA-256 `d2d47991ca051c05ac556d55a35969af0a9de21219a60104a6093f5e4caceacc`.
- `dcmlab-consonance/LICENSE.md` is the repository's supplied MIT license, retained unchanged, copyright Hall, Tamir and Rohrmeier. The file is a processed aggregation of the earlier Bowling study; repository licensing is not an independent provenance verification for original third-party research data.

## inconData Bowling tables

- Source: [pmcharrison/inconData](https://github.com/pmcharrison/inconData/tree/b95b4db27356a04241ed1a2e38ffc8f5e1f68bbe), commit `b95b4db27356a04241ed1a2e38ffc8f5e1f68bbe`, `data-raw/bowl18/data/`. The package metadata in `incondata-bowling2018/DESCRIPTION` states `License: CC0`; this is the provider's package declaration, not a separate legal determination concerning underlying third-party primary material.
- `dyads.csv` SHA-256 `f617e04b92feeb6a73a64a696163a9554d2cee578b81a40a190dd135708a5855`.
- `triads.csv` SHA-256 `d9210a546e06b83aae7109552a601304c647f6612ea2fba95b0219dae7462a20`.
- `tetrads.csv` SHA-256 `4e3826af63c366c69d84947bd68bf1d38598a33ed3f2357230e858092f04f103`.

The inconData documentation says these are transcriptions of the original supplementary data. DCMLab identifies inconData as a source: the two repositories are **not independent replications**. Cross-matching them catches some processing and transfer mistakes but does not independently verify the primary records, audio stimuli, participant-level data, or derivation of the supplied harmonic-similarity column. Files are unmodified and hash checked by the verifier.
