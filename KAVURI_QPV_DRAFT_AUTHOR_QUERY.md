# Draft author query — not sent

**Subject:** Clarification of QPV localization ratios and reported timing details

Dear authors,

Thank you for making your quantum position verification work available. I am independently checking the spatial-region definitions in [arXiv:2601.16892v2](https://arxiv.org/html/2601.16892v2), especially supplement IV, and would appreciate your help understanding several details. These are questions, not conclusions about your experimental results or security analysis.

1. For the 1D comparable-classical region in supplement IV.2.3, is the quantity in Table 4 the length of the **union** of the two projected spatial regions, with their overlap counted only once? Using the rounded Table 1 verifier times `sA=1291.0`, `sB=1429.1`, `rA=2340.3`, `rB=2207.7` ns, `L=195.1 m` and `c=0.299792458 m/ns`, I obtain approximately 78.895 m for the quantum projection and 273.995 m for the classical union: a ratio of 3.473. The corresponding ideal-classical ratio is 2.473, close to your 2.47(2); Table 4 reports 4.48(2) for the comparable-classical 1D factor. Am I interpreting the sets or the 1D projection incorrectly, or is another convention or input used?
2. Would you be willing to share the geometry and uncertainty-propagation scripts, the exact input definitions and, where practical, unrounded timing and separation values or the relevant public records? In particular, how are the 1D ratios aggregated in the Monte Carlo, and are the two comparisons evaluated using the same sampled inputs? The displayed Table 3 major axis `273.1 m` for the `rA−sB` ellipsoid also appears slightly different from the `273.1709 m` obtained from the rounded times; is there an additional convention or input precision involved?
3. In v2, the main text reports a 3 ± 2 ns challenge-arrival difference; supplement III.2 says B arrives 9 ± 2 ns after A; and supplement IV Table 1 lists 1766 ± 1 ns and 1769 ± 1 ns. Do these refer to different quantities or configurations? Similarly, the main text gives a 92.8 m distance from B while Table 2 labels 92.8 m as the A-to-prover axial projection. Could you clarify the station labels and definitions?
4. A supplied ten-page manuscript bearing DOI `10.1038/s41586-026-11247-3` prints 103 passes from 102 extended-protocol instances, whereas arXiv v2 reports 102 of 103. Can you confirm the intended count and identify the relevant manuscript version or any correction? The supplied file has a 7 November 2026 creation timestamp and no filled-in publication date; I cannot independently establish its version-of-record status.

I would be grateful for any clarification or public code/data references you can provide. Thank you for your time.

Best regards,
[Name]
