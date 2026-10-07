# DOSnpSupplement — band gaps of the GW1500 materials by ecalj

Databases of band gaps, band structures and DOS of about 1500 nonmagnetic materials of the Materials Project, computed with
[ecalj](https://github.com/tkotani/ecalj) (QSGW, LDA, MLO models). Each database has its own cover page with the conditions,
the version of ecalj of every value, and the checks. The newest is in the tree; an earlier version is kept as a git tag, with
a file of what the newer one changed.

| database | made | content | files |
| --- | --- | --- | --- |
| [QSGW80_20261007](QSGW80_20261007/README.md) | 2026-10-07 19:21 | QSGW80 (scaledsigma 0.8) iterated to convergence, LDA, MLO model (MLO: PASS 1537, FAIR 4, SKIPPED 2, OK 2, FAIL 1) | tables, figures, history, inputs (ctrlg), band data |
| [QSGW80_2026](https://github.com/tkotani/DOSnpSupplement/tree/QSGW80_20261003/QSGW80_2026) (git tag `QSGW80_20261003`) | 2026-10-03 | the earlier version; [what QSGW80_20261007 changed](QSGW80_20261007/changes_from_20261003.md) (a past log) | in the tag only; the DOS panel of its figures is shifted by E_F |
| [DOSnp2025](DOSnp2025.md) | 2025 | 1shot and 2ndshot QSGW and LDA of 1516 materials, the supplement of arXiv:2507.19189 | tables, band plots (GW/, LDA/) |

The crystal structures are those of the Materials Project (`ecalj_auto/INPUT/gw1500/POSCARALL` in ecalj).
