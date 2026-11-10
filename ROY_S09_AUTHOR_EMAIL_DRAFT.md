# Draft email: S09 EEG–fMRI timing

**To:** bhe1@andrew.cmu.edu  
**Subject:** Question about EEG–fMRI timing in the Roy et al. binocular rivalry dataset

Dear Professor He,

I am working with the public EEG–fMRI dataset accompanying Roy et al. (2017), “Deactivation in the posterior mid-cingulate cortex reflects perceptual transitions during binocular rivalry” (doi:10.1016/j.neuroimage.2017.02.041). Thank you for making the data available.

For participant S09, I found 141 preprocessed fMRI image pairs in scans 1 and 2, and 129 in scans 3–9. The corresponding EEG files contain between 124 and 127 `latency_tr` markers. The README describes 129 volumes per scan and recommends skipping five; the paper describes a typical model of 121 volumes per run. These may reflect different stages or recording intervals, and I do not want to assume a mapping from the counts alone.

Would you or a colleague be able to clarify:

1. How can the first stored EEG `latency_tr` marker be mapped to a particular preprocessed fMRI volume for S09? Is there a per-run volume timing or preprocessing record that specifies which volumes were included or discarded?
2. Are the publicly shared S09 motion-regressor rows in the same order as the corresponding preprocessed fMRI image pairs, including the 141-volume runs?
3. Are the original SPM design/included-volume lists or the trial-level stimulus and replay-source records available, or is there a documented procedure for reconstructing them?

A brief description, a reference to existing documentation, or a pointer to the right person would be very helpful. I am not requesting identifiable participant information or new image files.

Thank you for your time and for the public dataset.

Best regards,  
[Your name]

---

The recipient is the original corresponding author; the current Carnegie Mellon [directory](https://www.cnbc.cmu.edu/cnbc-directory/name/bin-he/) lists this address. The 2017 README has an older University of Minnesota address. This is a draft only; no email has been sent. If documentation is unavailable, report-aligned EEG analysis can continue with explicit limitations, but an EEG-informed fMRI contrast should not choose its timing anchor by optimizing the observed data.
