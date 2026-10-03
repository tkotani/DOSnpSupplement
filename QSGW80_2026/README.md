# GW1500 — QSGW80 band gaps, bands and DOS of 1546 materials (ecalj)

Made 2026-10-03 17:49 by `gw1500db_build.py` (ecalj, `ecalj_auto`). An update of the 2025 database
[tkotani/DOSnpSupplement](https://github.com/tkotani/DOSnpSupplement) (1shot/2shot QSGW of 1516 materials, the supplement of arXiv:2507.19189):
here every material is QSGW80 (scaledsigma = 0.8) iterated to convergence, the conditions of each value are written,
and results of different conditions are compared.

- [table.md](table.md): one row per material (gaps, conditions, direct/indirect, checks). Machine-readable: [gw1500db.tsv](gw1500db.tsv)
- Bands and DOS: [1 atoms](bands_1atoms.md), [2 atoms](bands_2atoms.md), [3 atoms](bands_3atoms.md), [4 atoms](bands_4atoms.md), [5 atoms](bands_5atoms.md), [6 atoms](bands_6atoms.md), [7 atoms](bands_7atoms.md), [8 atoms](bands_8atoms.md)
- Materials: Materials Project, paramagnetic, no lanthanides or actinides, PBE gap > 0, at most 8 atoms per cell
  (structures `ecalj_auto/INPUT/gw1500/POSCARALL`). The structures of MP are not always the experimental ones.

## Conditions

**Each material: check which ecalj made its value before comparing it with your own calculation.** The table gives, per
material, the version of ecalj and the conditions of the bold value (column *ecalj version*), and the letters of the other
results. Different versions and conditions can differ by 0.05–0.3 eV, M by more in some materials (see "How reliable are the
May values"); the present ecalj may differ again.

Every gap carries the letter of its conditions. **Bold** is the value adopted: N if the database run converged, else R, else M.

| | when | conditions |
| --- | --- | --- |
| **M** | 2026-04/05 | production of April-May 2026: ecalj of that time (~/bin2), input ctrl+GWinput (most) or the first TOML; GPU products all TF32 (--mp); chi0 by the T=0 tetrahedron method; Sigma levels Gaussian-smeared (esmr = 0.003 Ry); QSGW80 (scaledsigma 0.8), k 8x8x8 for lmf, 4x4x4 for GW; 5 iterations, then gwscconv until the gap of the last 3 iterations stays within 0.1 eV (at most 10) |
| **R** | 2026-09-30/10-02 | reruns from scratch: ecalj 989a18637 (2026-09-29); POSCAR -> vasp2ctrl -> ctrlgenToml.py --ssig=0.8; --prec=fp32; [gw] t_tetrakbt = +300 K (finite-T tetrahedron), t_sigmaw = 300 K; same k meshes; gwscconv: gap of the last 3 iterations within 0.1 eV twice (metals: eigenvalues within 5 eV of E_F change < 0.03 eV twice), at most 10 |
| **N** | 2026-10-02 night | database run: as R, but --prec=tf32 and t_tetrakbt = -300 K (chi0 by the T=0 tetrahedron method, Im chi0 smoothed by a Gaussian of the width of a 300 K Fermi-Dirac), t_sigmaw = 300 K; ecalj 989a18637 (kt1) or b695fa65c (2026-09-30, kr7) with the same gwscconv |

Common to all: LDA (VWN) as the starting point and for the LDA column, PMT basis (APW + MTO) made by `ctrlgenToml.py`
(M: its predecessors), no spin polarization, no spin-orbit coupling.

## How to read the QSGW80 column

`**2.96** N / M ≈` : 2.96 eV from N; M agrees within 0.05 eV. `**3.04** R / M 2.75` : M differs, its value written.
Column *check*: `differs` = some other result differs by 0.05–0.2 eV; `CHECK` = by more than 0.2 eV (to be looked at).
D/I: direct or indirect gap along the band path of the figure (the gap value itself is from the k mesh of lmf).
`· path 0.04`: the gap along the band path, written when it is smaller than the gap on the 8x8x8 k mesh in LDA too
(`path<mesh(mesh)`: the mesh misses the band extremum, so the true gap is nearer the path value; e.g. rocksalt SnS 0.79 on
the mesh, 0.04 on the path, 0.08 in 2025). `· path 0 (semimetal?)`: the bands cross E_F on the path (graphite-like carbons).

## Status (2026-10-03 17:49)

| adopted from | materials |
| --- | --- |
| N | 565 |
| R | 277 |
| M | 703 |
| none | 1 |

Database run (N) so far: 567 materials logged (CONVERGED 557, CONVERGED_METAL 8, FAIL(1) 1, TIMEOUT 1).
Order of the run: the materials with trouble in May first (SUSPECT_GOOD, MAY_WRONG, DRIFT_GOOD, UNKNOWN), then the
FAILED/NOTCONV of May (reruns R exist) alternating with a random sample of the May GOOD (by number of atoms), and the
two-atom GOOD on the second machine. The 16 materials with invalid or suspect structures were not run.

**Agreement between the condition sets** (|difference of gaps|, eV)

| pair | materials | median | mean (first − second) | > 0.05 | > 0.2 | max |
| --- | --- | --- | --- | --- | --- | --- |
| N − M | 506 | 0.024 | +0.051 | 186 | 56 | 8.69 |
| N − R | 77 | 0.000 | +0.002 | 1 | 0 | 0.11 |
| R − M | 19 | 0.253 | +0.641 | 14 | 11 | 8.69 |

## How reliable are the May values (M)?

The May production (April: the ecalj of that time with all GPU products in TF32, the old `--mp`; then continued in May)
differs from a run from scratch with the present code. For MgO (mp-1265, May 8.33 eV, now 8.18 eV) the inputs, the smearing,
`pb_lcutmx` and the precision of the present code were ruled out, and the ecalj of 2026-05-10 run from scratch on the May
inputs in double precision gives 8.18 eV, iteration by iteration as the present code. The sigm of the first May iterations,
read by that same lmf, gives gaps off by 0.05–0.26 eV already at iteration 1 (MgO, BeO, LiF, NaCl; CdS 0.01 eV), with signs
changing from material to material and from iteration to iteration: the precision of the old all-TF32 `--mp`. Materials with both M and N so far: 506; |N − M| (eV):

| | < 0.02 | 0.02–0.05 | 0.05–0.1 | 0.1–0.2 | 0.2–0.5 | > 0.5 |
| --- | --- | --- | --- | --- | --- | --- |
| suspected in May, run first (category not GOOD, or far from 2025) | 28 | 20 | 24 | 17 | 27 | 16 |
| others (random sample of the GOOD, all two-atom GOOD) | 204 | 68 | 54 | 35 | 13 | 0 |
| all | 232 | 88 | 78 | 52 | 40 | 16 |

So a May value (M) without a check by N carries an uncertainty of typically a few 10 meV, sometimes 0.2–0.5 eV, and in rare
cases more (LiGaO₂ 4.75 → 6.18 eV, RbSrCO₃F 5.33 → 7.26 eV). The database run checked the materials with trouble in May
first, then those whose May value is far from the 2025 values, then a random sample.

## Automatic checks

| check | materials | meaning |
| --- | --- | --- |
| CHECK | 56 | QSGW80 results of different conditions differ by more than 0.2 eV |
| differs | 132 | they differ by 0.05–0.2 eV |
| QSGW<LDA | 3 | the QSGW80 gap is smaller than the LDA gap by more than 0.05 eV |
| path<mesh(mesh) | 54 | the gap along the band path is smaller than the gap on the k mesh of lmf by more than 0.1 eV, and in LDA by more than 0.05 eV: the 8x8x8 mesh misses the band extremum (the true gap is nearer the path value) |
| path<mesh(noLDA) | 2 | the gap along the path is smaller than on the k mesh by more than 0.1 eV; no LDA bands to tell the mesh from Σ |
| path-metal | 5 | the bands along the path cross E_F while the k mesh of lmf gives a gap > 0.1 eV (the mesh misses the point where the gap closes, e.g. K of graphite) |
| LDA≠PBE | 6 | the LDA gap and the PBE gap of MP differ by more than 1 eV (MP uses GGA+U for oxides and fluorides of Co, Cr, Fe, Mn, Mo, Ni, V, W; or structure, basis) |
| vs2025 | 25 | the QSGW80 gap differs by more than 0.5 eV from LDA + 0.8 (QSGW100 − LDA) of the 2025 2nd shot |
| no-result | 1 | no QSGW80 result |
| N:FAIL(1) | 1 | database run did not converge (FAIL(1)) |
| N:TIMEOUT | 1 | database run did not converge (TIMEOUT) |

### CHECK (56)

| mpid | formula | LDA | QSGW80 | PBE (MP) | path gap | checks | category | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [mp-1794](bands_2atoms.md#mp-1794) | BeO | 8.19 | **11.10** N / M 11.37 | 8.17 | 11.10 | CHECK | GOOD |  |
| [mp-1009129](bands_2atoms.md#mp-1009129) | MgO | 3.04 | **5.89** N / M 6.12 | 3.05 | 5.88 | CHECK | GOOD |  |
| [mp-2064](bands_2atoms.md#mp-2064) | RbF | 6.50 | **10.48** N / M 10.28 | 5.91 | 10.48 | CHECK | GOOD |  |
| [mp-1883](bands_2atoms.md#mp-1883) | SnTe | 0.00 | **0.05** N / M 0.37 | 0.04 | 0.05 | CHECK | GOOD |  |
| [mp-1029](bands_3atoms.md#mp-1029) | BaF2 | 6.53 | **10.37** N / M 10.62 | 6.60 | 10.36 | CHECK | GOOD |  |
| [mp-1018033](bands_4atoms.md#mp-1018033) | AgRhO2 | 0.57 | **1.77** N / M 1.56 · path 1.64 | 0.49 | 1.64 | CHECK path<mesh(mesh) | DRIFT_GOOD | 5 月は収束の基準を満たしたが、最後の 3 反復が同じ向きに +0.09 eV 動いていた（履歴 1.5928, 1.3423, 1.4710, 1.5570, 1.5574）。回し直していない |
| [mp-1018096](bands_4atoms.md#mp-1018096) | Ba2NF | 0.91 | **2.36** N / M 2.11 | 1.08 | 2.36 | CHECK | GOOD |  |
| [mp-2542](bands_4atoms.md#mp-2542) | Be2O2 | 7.66 | **10.76** N / M 10.96 | 7.46 | 10.76 | CHECK | GOOD |  |
| [mp-23154](bands_4atoms.md#mp-23154) | Br4 | 1.21 | **3.51** N / M 3.72 | 1.35 | 3.50 | CHECK | GOOD |  |
| [mp-672285](bands_4atoms.md#mp-672285) | CuCSN | 2.07 | **3.60** N / M 3.29 | 2.27 | 3.60 | CHECK | GOOD |  |
| [mp-4280](bands_4atoms.md#mp-4280) | GaCuO2 | 1.01 | **2.59** N / M 2.08 | 0.78 | 2.59 | CHECK | GOOD |  |
| [mp-8188](bands_4atoms.md#mp-8188) | KScO2 | 3.52 | **6.54** N / M 6.22 | 3.62 | 6.54 | CHECK | GOOD |  |
| [mp-8409](bands_4atoms.md#mp-8409) | KYO2 | 3.89 | **6.48** N / M 6.05 | 3.97 | 6.48 | CHECK | GOOD |  |
| [mp-1006888](bands_4atoms.md#mp-1006888) | KYS2 | 2.15 | **4.02** N / M 3.42 / R ≈ | 2.32 | 4.02 | CHECK | SUSPECT_GOOD | 5 月は GOOD だが 2 反復目以降に 0.5 eV を超えて振動（履歴 2.6872, 3.9244, 3.2604, 3.3863, 3.4772, 3.4245） / 回し直し(run3): CONVERGED 5 反復、ギャップ 4.019836 eV（LDA 2.1 |
| [mp-8002](bands_4atoms.md#mp-8002) | LiGaO2 | 3.71 | **6.18** N / M 4.75 | 3.74 | 6.16 | CHECK | GOOD |  |
| [mp-24199](bands_4atoms.md#mp-24199) | LiHF2 | 8.08 | **13.03** N / M 11.96 | 8.04 | 13.03 | CHECK vs2025 | GOOD |  |
| [mp-1001786](bands_4atoms.md#mp-1001786) | LiScS2 | 1.33 | **3.04** N / M 2.75 / R ≈ | 1.48 | 3.04 | CHECK | SUSPECT_GOOD | 5 月は GOOD だが 2 反復目以降に 0.5 eV を超えて振動（履歴 2.7887, 3.1778, 2.5089, 2.7130, 2.7803, 2.7531） / 回し直し(run3): CONVERGED 5 反復、ギャップ 3.043529 eV（LDA 1.3 |
| [mp-15788](bands_4atoms.md#mp-15788) | LiYS2 | 1.75 | **3.29** N / M 2.99 | 1.92 | 3.29 | CHECK | GOOD |  |
| [mp-672233](bands_4atoms.md#mp-672233) | N4 | 6.93 | **13.50** N / M 13.72 | 6.60 | 13.47 | CHECK | GOOD |  |
| [mp-1066400](bands_4atoms.md#mp-1066400) | NaN3 | 3.99 | **7.07** N / M 6.71 | 4.15 | 7.07 | CHECK | GOOD |  |
| [mp-22003](bands_4atoms.md#mp-22003) | NaN3 | 3.91 | **7.31** N / M 5.83 / R ≈ | 4.03 | 7.31 | CHECK | SUSPECT_GOOD | 5 月は GOOD だが 2 反復目以降に 0.5 eV を超えて振動（履歴 6.9434, 5.3852, 6.2185, 5.8605, 5.9227, 5.8322） / 回し直し(run3): CONVERGED 5 反復、ギャップ 7.308540 eV（LDA 3.9 |
| [mp-7914](bands_4atoms.md#mp-7914) | NaScO2 | 3.90 | **7.09** N / M 6.53 | 3.98 | 7.09 | CHECK | GOOD |  |
| [mp-3056](bands_4atoms.md#mp-3056) | NaTlO2 | 0.64 | **1.98** N / M 1.47 / R ≈ | 0.62 | 1.98 | CHECK | SUSPECT_GOOD | 5 月は GOOD だが 2 反復目以降に 0.5 eV を超えて振動（履歴 2.0278, 0.5805, 1.4607, 1.4096, 1.4647） / 回し直し(run3): CONVERGED 6 反復、ギャップ 1.981450 eV（LDA 0.640949）、5 |
| [mp-8145](bands_4atoms.md#mp-8145) | RbScO2 | 3.19 | **5.81** N / M 5.41 | 3.30 | 5.83 | CHECK | GOOD |  |
| [mp-8176](bands_4atoms.md#mp-8176) | RbTlO2 | 0.87 | **2.17** N / M 1.80 | 0.85 | 2.17 | CHECK | GOOD |  |
| [mp-999265](bands_4atoms.md#mp-999265) | RbYS2 | 2.13 | **3.93** N / M 3.57 | 2.31 | 3.93 | CHECK | GOOD |  |
| [mp-973185](bands_4atoms.md#mp-973185) | ScAgO2 | 2.13 | **4.04** N / M 3.52 | 2.07 | 4.04 | CHECK | GOOD |  |
| [mp-10694](bands_4atoms.md#mp-10694) | ScF3 | 6.03 | **11.94** N / M 11.65 | 6.08 | 11.94 | CHECK | DRIFT_GOOD | 5 月は収束の基準を満たしたが、最後の 3 反復が同じ向きに +0.09 eV 動いていた（履歴 11.5653, 11.6507, 11.6530）。回し直していない |
| [mp-665922](bands_4atoms.md#mp-665922) | SrHgO2 | 2.18 | **4.52** N / M 3.47 | 2.20 | 4.52 | CHECK | DRIFT_GOOD | 5 月は収束の基準を満たしたが、最後の 3 反復が同じ向きに -0.08 eV 動いていた（履歴 3.5140, 3.2745, 3.5540, 3.4719, 3.4703）。回し直していない |
| [mp-1066131](bands_4atoms.md#mp-1066131) | YTlS2 | 1.37 | **2.29** N / M 2.58 / R ≈ | 1.50 | 2.29 | CHECK | SUSPECT_GOOD | 5 月は GOOD だが 2 反復目以降に 0.5 eV を超えて振動（履歴 1.8727, 2.4057, 3.0360, 2.6476, 2.5802, 2.5215, 2.5781） / 回し直し(run3): CONVERGED 5 反復、ギャップ 2.285675 eV |
| [mp-3163](bands_5atoms.md#mp-3163) | BaSnO3 | 0.51 | **2.74** N / M 2.35 | 0.37 | 2.74 | CHECK | GOOD |  |
| [mp-7986](bands_5atoms.md#mp-7986) | CaSnO3 | 1.13 | **3.59** N / M 3.92 | 1.39 | 3.59 | CHECK | GOOD |  |
| [mp-1069819](bands_5atoms.md#mp-1069819) | SnN2F2 | 1.00 | **4.12** N / M 3.61 | 0.94 | 4.12 | CHECK | GOOD |  |
| [mp-546711](bands_6atoms.md#mp-546711) | CsClO4 | 5.41 | **8.95** N / M 0.26 / R ≈ | 5.32 | 8.95 | CHECK | MAY_WRONG | 5 月は GOOD でギャップ 0.26 eV（LDA 5.41 より小さい）。回し直しで 8.95 eV。5 月の値は誤り / 回し直し(run1): CONVERGED 5 反復、ギャップ 8.953423 eV（LDA 5.412798）、5 月との差 +8.69 eV |
| [mp-1072956](bands_6atoms.md#mp-1072956) | Mg2F4 | 6.63 | **11.85** N / M 12.42 | 6.85 | 11.85 | CHECK | GOOD |  |
| [mp-552537](bands_6atoms.md#mp-552537) | Sr2CuBrO2 | 2.40 | **4.74** N / M 4.51 | 2.35 | 4.74 | CHECK | GOOD |  |
| [mp-4359](bands_6atoms.md#mp-4359) | Sr2PdO3 | 0.06 | **2.18** N / M 2.61 | 0.24 | 2.18 | CHECK | DRIFT_GOOD | 5 月は収束の基準を満たしたが、最後の 3 反復が同じ向きに -0.09 eV 動いていた（履歴 2.1326, 3.1425, 2.7010, 2.6114, 2.6101）。回し直していない |
| [mp-552120](bands_6atoms.md#mp-552120) | Y2Cl2O2 | 4.26 | **6.82** N / M 6.50 | 4.27 | 6.73 | CHECK | DRIFT_GOOD | 5 月は収束の基準を満たしたが、最後の 3 反復が同じ向きに -0.09 eV 動いていた（履歴 4.7872, 6.5909, 6.5649, 6.5010）。回し直していない |
| [mp-545756](bands_6atoms.md#mp-545756) | ZnSO4 | 4.57 | **8.54** N / M 8.77 | 4.27 | 8.54 | CHECK | GOOD |  |
| [mp-29585](bands_7atoms.md#mp-29585) | K4CdAs2 | 0.50 | **1.62** N / M 1.11 / R ≈ | 0.61 | 1.62 | CHECK | SUSPECT_GOOD | 5 月は GOOD だが 2 反復目以降に 0.5 eV を超えて振動（履歴 1.4420, 0.4743, 1.0255, 1.1139, 1.1070） / 回し直し(run3): CONVERGED 5 反復、ギャップ 1.617516 eV（LDA 0.499491）、5 |
| [mp-8753](bands_7atoms.md#mp-8753) | K4HgP2 | 0.80 | **1.93** N / M 1.64 / R ≈ | 0.94 | 1.93 | CHECK | SUSPECT_GOOD | 5 月は GOOD だが 2 反復目以降に 0.5 eV を超えて振動（履歴 1.8568, 0.7993, 1.6384, 1.6377, 1.6410） / 回し直し(run3): CONVERGED 5 反復、ギャップ 1.931914 eV（LDA 0.802632）、5 |
| [mp-863745](bands_7atoms.md#mp-863745) | RbSrCO3F | 3.85 | **7.26** N / M 5.33 | 4.13 | 7.25 | CHECK | GOOD |  |
| [mp-8560](bands_7atoms.md#mp-8560) | SF6 | 6.10 | **12.14** N / M 12.55 | 5.81 | 12.14 | CHECK | GOOD |  |
| [mp-624688](bands_7atoms.md#mp-624688) | Ta2O5 | 2.32 | **4.03** N / M 4.47 | 2.47 | 4.03 | CHECK | GOOD |  |
| [mp-8255](bands_8atoms.md#mp-8255) | CaPtF6 | 2.48 | **7.09** N / M 6.61 | 2.66 | 7.09 | CHECK | GOOD |  |
| [mp-9636](bands_8atoms.md#mp-9636) | CsSbF6 | 5.23 | **10.20** N / M 9.52 / R ≈ | 5.04 | 10.20 | CHECK | SUSPECT_GOOD | 5 月は GOOD だが 2 反復目以降に 0.5 eV を超えて振動（履歴 9.5758, 10.1857, 9.4742, 9.5269, 9.5218） / 回し直し(run3): CONVERGED 6 反復、ギャップ 10.198779 eV（LDA 5.227938） |
| [mp-27999](bands_8atoms.md#mp-27999) | K5CuSb2 | 0.64 | **1.65** N / M 1.90 / R ≈ | 0.75 | 1.65 | CHECK | SUSPECT_GOOD | 5 月は GOOD だが 2 反復目以降に 0.5 eV を超えて振動（履歴 1.6216, 2.5315, 1.9968, 1.9250, 1.8993） / 回し直し(run3): CONVERGED 5 反復、ギャップ 1.646245 eV（LDA 0.635402）、5 |
| [mp-12015](bands_8atoms.md#mp-12015) | KAg2AsO4 | 0.04 | **2.42** N / M 2.83 | 0.21 | 2.42 | CHECK | GOOD |  |
| [mp-4608](bands_8atoms.md#mp-4608) | KPF6 | 7.26 | **12.55** N / M 12.09 | 7.04 | 12.55 | CHECK | GOOD |  |
| [mp-1078799](bands_8atoms.md#mp-1078799) | LiNbF6 | 4.99 | **9.16** N / M 8.71 | 4.79 | 9.16 | CHECK | GOOD |  |
| [mp-29521](bands_8atoms.md#mp-29521) | Rb2Bi2O4 | 1.98 | **3.67** N / M 3.93 | 2.12 | 3.67 | CHECK | GOOD |  |
| [mp-27421](bands_8atoms.md#mp-27421) | RbBiF6 | 2.80 | **6.99** N / M 6.65 | 2.64 | 6.99 | CHECK | GOOD |  |
| [mp-2068](bands_8atoms.md#mp-2068) | Rh2F6 | 0.77 | **4.00** N / M 3.62 | 0.87 | 4.00 | CHECK vs2025 | GOOD |  |
| [mp-23309](bands_8atoms.md#mp-23309) | Sc2Cl6 | 3.59 | **7.02** N / M 6.30 | 3.91 | 7.03 | CHECK | DRIFT_GOOD | 5 月は収束の基準を満たしたが、最後の 3 反復が同じ向きに +0.09 eV 動いていた（履歴 5.9855, 6.6573, 6.2043, 6.2940, 6.2962）。回し直していない |
| [mp-1078195](bands_8atoms.md#mp-1078195) | Si2I6 | 2.78 | **4.94** N / M 5.16 / R ≈ | 2.99 | 4.92 | CHECK | SUSPECT_GOOD | 5 月は GOOD だが 2 反復目以降に 0.5 eV を超えて振動（履歴 4.9379, 4.1919, 5.1101, 5.0901, 5.1581） / 回し直し(run3): CONVERGED 5 反復、ギャップ 4.940172 eV（LDA 2.779810）、5 |
| [mp-2552](bands_8atoms.md#mp-2552) | Te2O6 | 1.45 | **3.62** N / M 3.17 | 1.16 | 3.62 | CHECK | GOOD |  |

### path-metal (5)

| mpid | formula | LDA | QSGW80 | PBE (MP) | path gap | checks | category | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [mp-169](bands_2atoms.md#mp-169) | C2 | 1.66 | **2.52** R · path 0 (semimetal?) | 0.20 |  | path-metal LDA≠PBE vs2025 | NOTCONV_MAY | 5 月は 10 反復で収束せず（最後の 3 反復の幅 0.1482 eV、履歴 2.3996, 3.5521, 2.9277, 2.7925, 2.9407） / 回し直し(run3): CONVERGED 4 反復、ギャップ 2.519014 eV（LDA 1.663932）、 |
| [mp-1008505](bands_4atoms.md#mp-1008505) | Ba2Pd2 | 0.12 | **0.30** N / M ≈ · path 0 (semimetal?) | 0.00 |  | path-metal | GOOD |  |
| [mp-2516584](bands_4atoms.md#mp-2516584) | C4 | 1.45 | **2.48** N / M 2.40 · path 0 (semimetal?) | 1.43 |  | differs path-metal vs2025 | GOOD |  |
| [mp-569304](bands_4atoms.md#mp-569304) | C4 | 1.85 | **3.68** R · path 0 (semimetal?) | 0.01 |  | path-metal LDA≠PBE vs2025 | INVALID_STRUCTURE | 硝酸を挿入した黒鉛（Graphite, nitrated）から N・O を除いたもの。密度 1.38（黒鉛 2.26）、層間が開いたまま / 回し直し(run3): CONVERGED 5 反復、ギャップ 3.677225 eV（LDA 1.848254）、5 月との差 -0.1 |
| [mp-569416](bands_8atoms.md#mp-569416) | C8 | 1.80 | **4.97** M · path 0 (semimetal?) | 0.11 |  | path-metal LDA≠PBE vs2025 | INVALID_STRUCTURE | 硝酸を挿入した黒鉛から N・O を除いたもの。密度 1.67（黒鉛 2.26） |

### path<mesh(noLDA) (2)

| mpid | formula | LDA | QSGW80 | PBE (MP) | path gap | checks | category | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [mp-30302](bands_6atoms.md#mp-30302) | Hf2Br2N2 | 1.85 | **3.45** R | 1.90 | 3.35 | path<mesh(noLDA) | FAILED_MAY | 5 月の失敗: PROD_NaN_lqpe / 回し直し(run1): CONVERGED 5 反復、ギャップ 3.453893 eV（LDA 1.851679） |
| [mp-691](bands_8atoms.md#mp-691) | Sn4Se4 | 0.79 | **1.24** R | 0.61 | 1.14 | path<mesh(noLDA) | FAILED_MAY | 5 月の失敗: PROD_TIMEOUT_8h / 回し直し(run1): CONVERGED 4 反復、ギャップ 1.243348 eV（LDA 0.792248）、5 月との差 +0.01 eV |

### QSGW<LDA (3)

| mpid | formula | LDA | QSGW80 | PBE (MP) | path gap | checks | category | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [mp-9379](bands_5atoms.md#mp-9379) | SrSn2As2 | 0.14 | **0.06** N / R ≈ | 0.00 | 0.02 | QSGW<LDA | UNKNOWN_MAY | 5 月: NOGAP_SMALL_GAP(LDA gap 0.14 eV; possibly semimetal)（金属・半金属。gwscconv がギャップを読めず止まった） / 回し直し(run2m): CONVERGED 4 反復、ギャップ 0.040954 eV（LDA  |
| [mp-3829](bands_8atoms.md#mp-3829) | Cd2Sn2As4 | 0.11 | **0.06** N / M ≈ / R ≈ | 0.01 | 0.06 | QSGW<LDA | SUSPECT_GOOD | 5 月は GOOD だが QSGW80 のギャップが LDA より小さい（履歴 0.0595, 0.0628, 0.0628） / 回し直し(run3): CONVERGED 4 反復、ギャップ 0.051696 eV（LDA 0.111058）、5 月との差 -0.01 eV |
| [mp-796276](bands_8atoms.md#mp-796276) | Mo2O6 | 1.14 | **0.98** N / M 1.07 / R ≈ | 0.45 | 0.98 | differs QSGW<LDA | SUSPECT_GOOD | 5 月は GOOD だが QSGW80 のギャップが LDA より小さい（履歴 1.7149, 0.7988, 1.0927, 1.0956, 1.0694） / 回し直し(run3): CONVERGED 7 反復、ギャップ 0.981008 eV（LDA 1.137048）、 |

### path<mesh(mesh) (54)

| mpid | formula | LDA | QSGW80 | PBE (MP) | path gap | checks | category | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [mp-1876](bands_2atoms.md#mp-1876) | SnS | 0.63 | **0.78** N / M ≈ · path 0.03 | 0.05 | 0.03 | path<mesh(mesh) vs2025 | GOOD |  |
| [mp-2693](bands_2atoms.md#mp-2693) | SnSe | 0.58 | **0.79** N / M ≈ · path 0.12 | 0.17 | 0.12 | path<mesh(mesh) vs2025 | GOOD |  |
| [mp-7188](bands_3atoms.md#mp-7188) | Al2Os | 0.41 | **0.98** N / M ≈ · path 0.79 | 0.29 | 0.79 | path<mesh(mesh) | GOOD |  |
| [mp-567677](bands_3atoms.md#mp-567677) | GeI2 | 2.02 | **3.09** N / M ≈ · path 2.96 | 1.96 | 2.96 | path<mesh(mesh) | GOOD |  |
| [mp-1434](bands_3atoms.md#mp-1434) | MoS2 | 1.18 | **1.76** N / M 1.71 · path 1.58 | 1.38 | 1.58 | differs path<mesh(mesh) | GOOD |  |
| [mp-14](bands_3atoms.md#mp-14) | Se3 | 1.11 | **2.14** N / M ≈ · path 2.03 | 1.01 | 2.03 | path<mesh(mesh) | GOOD |  |
| [mp-19](bands_3atoms.md#mp-19) | Te3 | 0.56 | **0.90** N / M ≈ · path 0.64 | 0.18 | 0.64 | path<mesh(mesh) | GOOD |  |
| [mp-9813](bands_3atoms.md#mp-9813) | WS2 | 1.31 | **2.00** N / R ≈ · path 1.78 | 1.56 | 1.78 | path<mesh(mesh) | NOTCONV_MAY | 5 月は 10 反復で収束せず（最後の 3 反復の幅 0.1242 eV、履歴 1.3930, 1.3211, 1.4459, 1.3523, 1.3217） / 回し直し(run3): CONVERGED 4 反復、ギャップ 1.999899 eV（LDA 1.314100）、 |
| [mp-23162](bands_3atoms.md#mp-23162) | ZrCl2 | 0.97 | **1.90** N / M ≈ · path 1.73 | 0.85 | 1.73 | path<mesh(mesh) | DRIFT_GOOD | 5 月は収束の基準を満たしたが、最後の 3 反復が同じ向きに +0.09 eV 動いていた（履歴 1.7770, 1.9192, 1.7892, 1.8618, 1.8820）。回し直していない |
| [mp-1018033](bands_4atoms.md#mp-1018033) | AgRhO2 | 0.57 | **1.77** N / M 1.56 · path 1.64 | 0.49 | 1.64 | CHECK path<mesh(mesh) | DRIFT_GOOD | 5 月は収束の基準を満たしたが、最後の 3 反復が同じ向きに +0.09 eV 動いていた（履歴 1.5928, 1.3423, 1.4710, 1.5570, 1.5574）。回し直していない |
| [mp-2793](bands_4atoms.md#mp-2793) | Au2Se2 | 0.14 | **0.64** N / M ≈ · path 0.54 | 0.26 | 0.54 | path<mesh(mesh) | GOOD |  |
| [mp-2653](bands_4atoms.md#mp-2653) | B2N2 | 5.38 | **7.50** N / M ≈ · path 7.16 | 5.20 | 7.16 | path<mesh(mesh) | GOOD |  |
| [mp-7991](bands_4atoms.md#mp-7991) | B2N2 | 3.80 | **6.53** N / M ≈ · path 6.29 | 4.27 | 6.29 | path<mesh(mesh) vs2025 | GOOD |  |
| [mp-984](bands_4atoms.md#mp-984) | B2N2 | 4.33 | **6.56** N / M ≈ · path 6.43 | 4.48 | 6.43 | path<mesh(mesh) vs2025 | GOOD |  |
| [mp-1008559](bands_4atoms.md#mp-1008559) | B2P2 | 1.13 | **1.96** N / M ≈ · path 1.75 | 1.08 | 1.75 | path<mesh(mesh) | GOOD |  |
| [mp-23301](bands_4atoms.md#mp-23301) | BiF3 | 3.99 | **6.41** N / M ≈ · path 6.30 | 3.95 | 6.30 | path<mesh(mesh) | GOOD |  |
| [mp-47](bands_4atoms.md#mp-47) | C4 | 3.58 | **5.23** N / M ≈ · path 4.84 | 3.34 | 4.84 | path<mesh(mesh) vs2025 | GOOD |  |
| [mp-29643](bands_4atoms.md#mp-29643) | CuAsSe2 | 0.66 | **0.94** N / M ≈ · path 0.52 | 0.32 | 0.52 | path<mesh(mesh) | GOOD |  |
| [mp-23177](bands_4atoms.md#mp-23177) | Hg2Br2 | 2.02 | **3.60** N / M ≈ · path 3.50 | 2.26 | 3.50 | path<mesh(mesh) | GOOD |  |
| [mp-20526](bands_4atoms.md#mp-20526) | Pb2S2 | 1.74 | **3.24** M · path 3.13 | 1.70 | 3.13 | path<mesh(mesh) | SUSPECT_STRUCTURE | PbS。a=4.22、c=11.3 Å、1 原子 50.2 Å³、配位 4。非整合層状化合物の PbS 層と同じ形 |
| [mp-727323](bands_4atoms.md#mp-727323) | Pb2S2 | 1.73 | **3.23** M · path 3.12 | 1.65 | 3.12 | path<mesh(mesh) | INVALID_STRUCTURE | Pb–Ti–S の非整合層状化合物の「Pb S-part」。a=4.22、c=11.2 Å、1 原子 49.7 Å³（岩塩型 PbS 26.7） |
| [mp-22009](bands_4atoms.md#mp-22009) | Pb2Se2 | 1.46 | **2.93** M · path 2.71 | 1.30 | 2.71 | path<mesh(mesh) | SUSPECT_STRUCTURE | PbSe。1 原子 58.5 Å³、配位 5（岩塩型 PbSe は約 29.5、配位 6）。層状化合物の副格子と見られる |
| [mp-7140](bands_4atoms.md#mp-7140) | Si2C2 | 2.44 | **3.53** M · path 3.26 | 2.30 | 3.26 | path<mesh(mesh) | GOOD |  |
| [mp-557835](bands_4atoms.md#mp-557835) | Tl2F2 | 2.96 | **4.76** N / M ≈ · path 4.61 | 2.99 | 4.61 | path<mesh(mesh) | GOOD |  |
| [mp-1017567](bands_5atoms.md#mp-1017567) | Hf2SN2 | 0.94 | **2.08** M · path 1.87 | 0.89 | 1.87 | path<mesh(mesh) | GOOD |  |
| [mp-865185](bands_5atoms.md#mp-865185) | MgBe2As2 | 0.57 | **1.38** M · path 1.16 | 0.40 | 1.16 | path<mesh(mesh) | GOOD |  |
| [mp-1017628](bands_5atoms.md#mp-1017628) | MgBe2P2 | 0.76 | **1.74** M · path 1.52 | 0.63 | 1.52 | path<mesh(mesh) | GOOD |  |
| [mp-553875](bands_5atoms.md#mp-553875) | Zr2SN2 | 0.70 | **1.72** M · path 1.52 | 0.55 | 1.52 | path<mesh(mesh) | GOOD |  |
| [mp-1205322](bands_6atoms.md#mp-1205322) | Ca2H4 | 0.41 | **2.79** M · path 2.64 | 0.65 | 2.64 | path<mesh(mesh) | GOOD |  |
| [mp-24809](bands_6atoms.md#mp-24809) | Ca2H4 | 0.39 | **2.77** M · path 2.61 | 0.65 | 2.61 | path<mesh(mesh) | GOOD |  |
| [mp-541911](bands_6atoms.md#mp-541911) | Hf2N2Cl2 | 2.21 | **3.96** M · path 3.84 | 2.23 | 3.84 | path<mesh(mesh) | GOOD |  |
| [mp-9244](bands_6atoms.md#mp-9244) | Li2B2C2 | 0.97 | **1.98** M · path 1.59 | 0.85 | 1.59 | path<mesh(mesh) | GOOD |  |
| [mp-1018809](bands_6atoms.md#mp-1018809) | Mo2S4 | 1.23 | **2.06** N / M 1.99 · path 1.86 | 1.34 | 1.86 | differs path<mesh(mesh) | DRIFT_GOOD | 5 月は収束の基準を満たしたが、最後の 3 反復が同じ向きに -0.09 eV 動いていた（履歴 2.0763, 2.0088, 1.9896）。回し直していない |
| [mp-2815](bands_6atoms.md#mp-2815) | Mo2S4 | 1.28 | **2.19** M · path 1.98 | 1.46 | 1.98 | path<mesh(mesh) | GOOD |  |
| [mp-1018807](bands_6atoms.md#mp-1018807) | Mo2Se4 | 1.18 | **1.97** M · path 1.82 | 1.25 | 1.82 | path<mesh(mesh) | GOOD |  |
| [mp-1179094](bands_6atoms.md#mp-1179094) | Sr2H4 | 1.05 | **3.28** M · path 3.15 | 1.28 | 3.15 | path<mesh(mesh) | GOOD |  |
| [mp-23759](bands_6atoms.md#mp-23759) | Sr2H4 | 1.08 | **3.34** M · path 3.20 | 1.26 | 3.20 | path<mesh(mesh) | GOOD |  |
| [mp-1019322](bands_6atoms.md#mp-1019322) | Te4W2 | 1.13 | **1.68** M · path 1.40 | 0.94 | 1.40 | path<mesh(mesh) | GOOD |  |
| [mp-224](bands_6atoms.md#mp-224) | W2S4 | 1.29 | **2.22** M · path 1.97 | 1.57 | 1.97 | path<mesh(mesh) | GOOD |  |
| [mp-1821](bands_6atoms.md#mp-1821) | W2Se4 | 1.26 | **2.04** M · path 1.90 | 1.45 | 1.90 | path<mesh(mesh) | GOOD |  |
| [mp-541912](bands_6atoms.md#mp-541912) | Zr2Br2N2 | 1.55 | **2.91** M · path 2.78 | 1.47 | 2.78 | path<mesh(mesh) | GOOD |  |
| [mp-580886](bands_6atoms.md#mp-580886) | Zr2I2N2 | 0.81 | **2.00** M · path 1.90 | 0.74 | 1.90 | path<mesh(mesh) | GOOD |  |
| [mp-542791](bands_6atoms.md#mp-542791) | Zr2N2Cl2 | 1.82 | **3.25** M · path 3.12 | 1.73 | 3.12 | path<mesh(mesh) | GOOD |  |
| [mp-14790](bands_7atoms.md#mp-14790) | GeTe4As2 | 0.60 | **0.74** N / M ≈ · path 0.43 | 0.37 | 0.43 | path<mesh(mesh) | GOOD |  |
| [mp-570002](bands_8atoms.md#mp-570002) | C8 | 3.06 | **4.59** M · path 4.44 | 3.00 | 4.44 | path<mesh(mesh) | GOOD |  |
| [mp-19178](bands_8atoms.md#mp-19178) | Co2Ag2O4 | 0.41 | **1.84** M · path 1.66 | 1.33 | 1.66 | path<mesh(mesh) vs2025 | GOOD |  |
| [mp-7936](bands_8atoms.md#mp-7936) | Li2Nb2S4 | 0.79 | **1.40** M · path 1.28 | 0.71 | 1.28 | path<mesh(mesh) | GOOD |  |
| [mp-757](bands_8atoms.md#mp-757) | Li6As2 | 0.75 | **1.72** M · path 1.55 | 0.64 | 1.55 | path<mesh(mesh) | GOOD |  |
| [mp-2341](bands_8atoms.md#mp-2341) | Li6N2 | 1.41 | **2.87** N / M 2.81 · path 2.66 | 1.22 | 2.66 | differs path<mesh(mesh) | GOOD |  |
| [mp-736](bands_8atoms.md#mp-736) | Li6P2 | 0.78 | **1.82** M · path 1.65 | 0.70 | 1.65 | path<mesh(mesh) | GOOD |  |
| [mp-7955](bands_8atoms.md#mp-7955) | Li6Sb2 | 0.62 | **1.45** M · path 1.30 | 0.48 | 1.30 | path<mesh(mesh) | GOOD |  |
| [mp-864954](bands_8atoms.md#mp-864954) | Mg2Mo2N4 | 0.95 | **1.58** M · path 1.32 | 0.74 | 1.32 | path<mesh(mesh) | GOOD |  |
| [mp-557179](bands_8atoms.md#mp-557179) | Na2Sb2S4 | 0.83 | **1.44** M · path 0.91 | 0.45 | 0.91 | path<mesh(mesh) vs2025 | GOOD |  |
| [mp-20042](bands_8atoms.md#mp-20042) | Tl2In2S4 | 0.48 | **1.17** M · path 0.94 | 0.47 | 0.94 | path<mesh(mesh) | GOOD |  |

### LDA≠PBE (6)

| mpid | formula | LDA | QSGW80 | PBE (MP) | path gap | checks | category | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [mp-169](bands_2atoms.md#mp-169) | C2 | 1.66 | **2.52** R · path 0 (semimetal?) | 0.20 |  | path-metal LDA≠PBE vs2025 | NOTCONV_MAY | 5 月は 10 反復で収束せず（最後の 3 反復の幅 0.1482 eV、履歴 2.3996, 3.5521, 2.9277, 2.7925, 2.9407） / 回し直し(run3): CONVERGED 4 反復、ギャップ 2.519014 eV（LDA 1.663932）、 |
| [mp-569304](bands_4atoms.md#mp-569304) | C4 | 1.85 | **3.68** R · path 0 (semimetal?) | 0.01 |  | path-metal LDA≠PBE vs2025 | INVALID_STRUCTURE | 硝酸を挿入した黒鉛（Graphite, nitrated）から N・O を除いたもの。密度 1.38（黒鉛 2.26）、層間が開いたまま / 回し直し(run3): CONVERGED 5 反復、ギャップ 3.677225 eV（LDA 1.848254）、5 月との差 -0.1 |
| [mp-18921](bands_4atoms.md#mp-18921) | NaCoO2 | 0.79 | **3.38** R | 2.16 | 3.54 | LDA≠PBE vs2025 | FAILED_MAY | 5 月の失敗: AC_lmf-SCF-diverged@llmf_start / 回し直し(run2m(続き)): CONVERGED 14 反復、ギャップ 3.375416 eV（LDA 0.791976）、5 月との差 +0.91 eV |
| [mp-18943](bands_8atoms.md#mp-18943) | Ba2Ni2O4 | 0.15 | **2.23** N / M ≈ | 2.32 | 2.23 | LDA≠PBE | GOOD |  |
| [mp-569416](bands_8atoms.md#mp-569416) | C8 | 1.80 | **4.97** M · path 0 (semimetal?) | 0.11 |  | path-metal LDA≠PBE vs2025 | INVALID_STRUCTURE | 硝酸を挿入した黒鉛から N・O を除いたもの。密度 1.67（黒鉛 2.26） |
| [mp-867515](bands_8atoms.md#mp-867515) | Na2Co2O4 | 0.72 | **3.68** R | 2.12 | 3.67 | LDA≠PBE | NOTCONV_MAY | 5 月は 10 反復で収束せず（最後の 3 反復の幅 0.1091 eV、履歴 2.8570, 3.4392, 3.5383, 3.6123, 3.6475） / 回し直し(run3x(続き)): CONVERGED 19 反復、ギャップ 3.678100 eV（LDA 0.72 |

### no-result (1)

| mpid | formula | LDA | QSGW80 | PBE (MP) | path gap | checks | category | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [mp-1179832](bands_8atoms.md#mp-1179832) | Rb8 |  | — | 0.59 |  | no-result | INVALID_STRUCTURE | Rb-IV（高圧相、ICSD 109016）を MP が圧力ゼロで緩和。一辺 19.9 Å の胞に Rb8 の正八角形の環（Rb–Rb 4.63 Å、隣 2 個）。1 原子 551 Å³（bcc Rb 93）、凸包から 0.45 eV/原子。ギャップは環の HOMO–LUMO。平 |

## Limits

- k mesh: the gap is that of lmf on the 8x8x8 mesh. When the band extremum is not on the mesh (layered and hexagonal
  materials, K and M points), the true gap is nearer the gap along the band path (`· path` in the table, check
  `path<mesh(mesh)`). Graphite-like carbons are semimetals although the mesh shows a gap (`path-metal`).
- GW mesh 4x4x4, QSGW80 (80 % of the QSGW self-energy, which corrects the overestimate of QSGW gaps for the average of
  materials), no spin polarization, no spin-orbit coupling, LDA starting point, structures of Materials Project.
- The DOS of the figures is that of lmf, written up to a little above E_F (the conduction-band DOS is not shown).
- Band plots interpolate the self-energy between the mesh points; a check compares the same k points met twice.

## Files and how this was made

- `gw1500db.tsv`: one row per material (all columns of the table, the other results in `others`, notes in `dbnote`)
- `fig/<mpid>.png`. The raw data behind the figures (`npz/<mpid>.<tag>.npz`, bands and DOS; tags `may_qsgw`, `may_lda`, `rr_<run>`,
  `db_qsgw`, `db_lda`) and the logs of the runs are kept by the maintainers and are not in the published copy
- Published at https://github.com/tkotani/DOSnpSupplement/tree/main/QSGW80_2026 (by `TOOLS/publish_gw1500db.sh` of ecalj)
- ecalj `ecalj_auto/`: `gw1500_rerun.sh` (the runs, `T_TETRAKBT`), `gw1500db_extract.py`, `gw1500db_build.py`,
  `gw1500_reorder.py`; the status of the earlier runs `GW1500_status.md`, `gw1500_status_20260930.tsv`, `gw1500_notes_20261001.tsv`
- Machines: kt1 (RTX 5090 x2, 64 cores, 4 workers x 16 cores), kr7 (RTX 5090, 16 cores, 2 workers x 8 cores)

## Categories (from the May production, `ecalj_auto/GW1500_status.md`)

GOOD: converged in May. DRIFT_GOOD: converged but the gap drifted over the iterations. SUSPECT_GOOD: converged, but the
iterations oscillated. NOTCONV_MAY: not converged within 10 iterations in May. FAILED_MAY: crashed in May (mostly the
all-TF32 precision of that time). UNKNOWN_MAY: no gap (metals, semimetals). MAY_WRONG: the May value was wrong.
INVALID_STRUCTURE / SUSPECT_STRUCTURE: the MP structure is a fragment cut out of another compound, or doubtful
(listed with their values, which have no physical meaning).
