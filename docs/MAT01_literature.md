# MAT-01 literature scoping: intersubband optics of BaSnO3 quantum structures
Compiled 12 Oct 2026. Sources marked [OPENED] were opened with WebFetch. [NOT OPENED] means the page was paywalled, blocked, or the fetch permission timed out, so the number is second-hand. Numbers marked "derived" are my own arithmetic.

## 1. Go/no-go: prior art

| # | Paper | What it computes or measures | Status |
|---|---|---|---|
| P1 | W. Li, A. K. Hamze, A. A. Demkov, "Tunable giant nonlinear optical susceptibility in BaSnO3 quantum wells", *Phys. Rev. B* 104, 235419 (2021), doi:10.1103/PhysRevB.104.235419. The APS March 2022 G71.8 talk is the conference version. | La:BSO/BaO asymmetric double QW (4+7 u.c.; also 3+6 u.c.) and triple QW (3/4/6 u.c.) with 1-u.c. BaO barriers. Methods: DFT plus Wannier tight-binding to validate effective-mass theory, Poisson–Schrödinger with La doping (1e19 and 5e18 cm^-3), and density-matrix χ(2)zzz and χ(3)zzzz with phenomenological γ = 10 meV. Results: χ(2) up to 200 nm/V (bias −100 kV/cm) and χ(3) up to 8000 nm²/V², spanning THz to about 1.2 eV. Parameters: m* = 0.17 (DFT) vs 0.19 (exp), parabolic. CBO BSO/BaO ≈ 1.74 eV; BSO/Al2O3 ≈ 3.5 eV (unpublished). The text does not mention nonparabolicity, depolarization, LO phonons or a lifetime model. | [OPENED] accepted manuscript |
| P2 | N. Stanojević, N. Vuković, J. Radovanović, "Calculation of intersubband absorption in n-doped BaSnO3 quantum wells", *Opt. Quantum Electron.* 55, 383 (2023), doi:10.1007/s11082-023-04656-5. This is the journal version of NUSOD 2022 pp. 149–150 (doi:10.1109/NUSOD54938.2022.9894844). | La:BSO/BaO symmetric double and triple QWs. Self-consistent Schrödinger–Poisson with exchange-correlation; ISB absorption vs well width, doping and bias. The abstract gives no parameters. Nonparabolicity, depolarization and linewidth model are unknown (paywalled). | Abstract [OPENED], full text [NOT OPENED] |
| P3 | S. Jang, M.A. thesis, "Near infrared to visible intersubband transitions in all-oxide quantum wells using BaSnO3", UT Austin (Dec 2023). Conference versions: APS MAR22 G71.9 (Al2O3/BSO design) and APS MAR23 YY07.4 (MgO barrier). | MBE Al2O3/SrTiO3(5 u.c.)/BSO/Al2O3 structures. XPS offsets: BSO/Al2O3 CBO ≈ 3.5 eV, BSO/STO CBO 0.49 eV. Poisson–Schrödinger with m* 0.19, ε = 20 for BSO, parabolic and no depolarization; it predicts 4/6/9 levels for 3/6/10 u.c. **ISB absorption was not measured.** Only an ellipsometric Tauc-gap blue shift was seen (3.69 → 3.87 eV). The thesis lists no journal paper. | [OPENED] (core.ac.uk PDF) |
| P4 | "Small effective mass deep all-oxide quantum wells based on [BaSnO3?]", *Phys. Rev. B*, doi:10.1103/8z9v-d6s9. A TOC hit suggests vol. 113 (2026). | Probably the journal version of P3 (Demkov group, MgO or Al2O3 barriers). **Authors, abstract and whether ISB absorption was measured are UNKNOWN.** | [NOT OPENED]: APS blocked and doi.org permission timed out. **Must read before submission.** |

Searches for LaInO3/BaSnO3, SrSnO3/BaSnO3, (Ba,Sr)SnO3, MgO/BSO and Al2O3/BSO combined with intersubband, SHG, χ(2), depolarization or LO-phonon lifetime returned nothing beyond P1–P4. I found **no infrared, THz or ISB optical measurement of any BaSnO3 2DEG**: not LaInO3/BSO, LaScO3/BSO, SrNbO3/BSO, delta-doped BSO, or EDL-gated BSO. THz work on bulk La:BSO films (Arezoomandan et al., *Sci. Rep.* 8, 3577 (2018), doi:10.1038/s41598-018-22038-w [OPENED]) reports σ_THz ≈ σ_DC and no Drude τ.

**Verdict: GO, provided P4 is checked.** All prior theory (P1–P3) treats doped, symmetric or biased BaO- or Al2O3-barrier wells with parabolic bands and a phenomenological linewidth. None covers:
- the polar LaInO3/BSO interface-polarization 2DEG;
- EDL-gated density dependence;
- the depolarization or exciton shift;
- the three-mode Fröhlich LO-phonon ISB lifetime;
- nonparabolicity, which is large in BSO.

One risk remains: P4 may report measured ISB transitions in BSO wells. Cite and position against it.

## 2. Material parameters

### 2a. BaSnO3

| Quantity | Value | Source |
|---|---|---|
| Band-edge mass m0* | 0.19 m0 (fit of optical mass vs n) | Niedermeier et al., arXiv:1609.05508 [OPENED]; published as PRB 95, 161202(R) (2017) [journal ref NOT OPENED] |
| Nonparabolicity | ħ²k²/2m0* = E(1+βE), **β = 0.56 eV⁻¹**; m*(n) = m0*√(1+2βħ²k²/m0*), k = (3π²n)^{1/3}. m* rises to ≈0.35–0.40 m0 at 4–7×10²⁰ cm⁻³. Data: FTIR/Drude with ellipsometry, n = 1.6e19–7.3e20 cm⁻³. | same |
| Nonparabolicity (theory) | m*Γ = 0.20 m0, α = 0.25 eV⁻¹ (HSE hyperbolic fit; 0.21–0.29 by direction) | Krishnaswamy et al., *PRB* 95, 205202 (2017), doi:10.1103/PhysRevB.95.205202 [OPENED] |
| Other masses | 0.35 m0 (IR Drude, 4% La): Seo et al., *APL* 104, 022102 (2014) [abstract OPENED]. 0.40 m0 (thermopower): Sanchela et al., arXiv:1704.03653 [OPENED; journal NOT OPENED]. ARPES 0.17 bulk, 0.12 surface state: Naamneh et al., *Commun. Phys.* 5, 317 (2022) [OPENED]. GW 0.20: Aggoune et al. 2022 [OPENED]. The Char-group Poisson–Schrödinger uses **0.42** (Kim et al. 2019, below). | — |
| Gap | Indirect 2.97±0.04 eV (EELS), 3.1 eV fundamental at RT. Direct onset 3.57±0.04 eV. Exciton binding ≈100 meV. GW@HSE at 0 K: 3.50 indirect, 3.96 direct. | Aggoune et al., *Commun. Mater.* 3, 12 (2022), doi:10.1038/s43246-022-00234-6 [OPENED] |
| Gap (older) | 2.95 indirect / 3.10 direct | H. J. Kim et al., arXiv:1207.0764 (PRB 86, 165205) [OPENED] |
| ε∞ | 3.3 above phonons, ≈4.3 at 0.75 eV (Stanislavchuk). 4.3 (Krishnaswamy). 4.2 (Aggoune, KK). 2.9–3.8 (Niedermeier fits). | — |
| ε0 (static) | **17±2** (exp, ε∞+ΣS); DFT 13.8 (Stanislavchuk). **20** is the value commonly used (Krishnaswamy, Niedermeier, Kim 2019); Prakash 2019 uses 17. | — |
| TO/LO phonons (IR ellipsometry, RT) | TO 135 / 244.5 / 628 cm⁻¹; LO 154 / 421 / 723 cm⁻¹ (= 19.1 / 52.2 / 89.6 meV, derived). Oscillator strengths S = 3.8 / 8.5 / 1.1. Raman LO2 408, LO3 724 cm⁻¹. | Stanislavchuk et al., *J. Appl. Phys.* 112, 044108 (2012), doi:10.1063/1.4748309 [OPENED via author PDF] |
| Fröhlich α | Per mode **α1 = 0.08, α2 = 0.70, α3 = 0.74** (m* = 0.19, ε∞ = 3.3, εs = 20, using LO 146 / 443 / 784 cm⁻¹, which differ from Stanislavchuk's). τ2 = 4.7×10⁻¹⁴ s. | Niedermeier, Kamiya, Moram, "Polaron coupling constants in BaSnO3", arXiv:1612.01343 [OPENED; journal NOT OPENED] |
| LO-limited mobility (theory) | 594 cm²/Vs at 300 K, n = 1e20; LO2 (51 meV) dominates | Krishnaswamy 2017 [OPENED] |
| a | 4.116 Å | Lee et al. 2024 [OPENED] |

Kane estimate: β ≈ 1/Eg ≈ 0.32 eV⁻¹ (derived). It lies between the experimental 0.56 and the theoretical 0.25 eV⁻¹, so use both as bounds.

### 2b. LaInO3

| Quantity | Value | Source |
|---|---|---|
| Gap | 5.0 eV (Char group, thin films). Bulk crystal direct optical gap 4.35/4.39 eV. G0W0 5.0 eV (Aggoune). Floating-zone crystal edge ≈4.13 eV. | Kim 2019 [OPENED]; Galazka et al., *pss(a)* 218, 2100016 (2021), doi:10.1002/pssa.202100016 [abstract OPENED]; Jang et al., *JAP* 121, 125109 (2017) [abstract OPENED] |
| ε0 | **23.7** (Jang 2017); **24.6** along [001] (Galazka 2021); 24 (Aggoune). The Char-group Poisson–Schrödinger uses **38**. | — |
| ε∞ | Not found. n(632.8 nm) = 2.07–2.13 gives ε ≈ 4.3–4.5 (derived; upper bound for ε∞). | Rose et al., arXiv:2604.15156 [OPENED] |
| LO/TO phonons | **No IR data found.** 25 IR-active modes (Pnma). Raman and DFT phonons in Rose et al. | gap: needs DFPT |
| m* | 0.46 m0 (used by Kim 2019); hole mass 0.48 (Aggoune) | — |
| Pseudocubic a | 4.117 Å (lattice-matched to BSO) | Lee 2024 |

### 2c. LaInO3/BaSnO3 interface and other barriers

| Quantity | Value | Source |
|---|---|---|
| CBO LIO/BSO | **1.6 eV** (experiment as cited; the authors note tunnelling underestimates it). The original measurement paper was not identified or opened. | Kim et al., "Interface polarization model for a 2DEG at the BaSnO3/LaInO3 interface", *Sci. Rep.* (7 Nov 2019), doi:10.1038/s41598-019-52772-8 [OPENED]; Lee 2024 [OPENED] |
| CBO (DFT) | 1.35–1.4 eV (periodic), 1.7 eV (non-periodic) | Aggoune & Draxl, *npj Comput. Mater.* 7, 174 (2021), doi:10.1038/s41524-021-00646-x [OPENED, arXiv v3] |
| Interface polarization | P = 65, 65, 25, 10 µC/cm² in the first four pseudocubic LIO cells (fit). Ideal LaO⁺/InO2⁻ value 50 µC/cm², so n2D = P/e ≈ 3.1×10¹⁴ cm⁻². Deep donors in LIO 2×10²⁰ cm⁻³; deep acceptors in BSO 4–6×10¹⁹ cm⁻³. Confinement ≈2 nm. n2D peaks at 4 u.c. LIO; no critical thickness. | Kim 2019 |
| DFT 2DEG | 0.03 e/a² at 4 pc. 2.7×10¹⁴ cm⁻² at 12 pc (periodic), 2.9×10¹⁴ cm⁻² non-periodic. tc = 2–7 pc. 2DEG extent ≈10–20 Å. 2DEG mass 0.24 m0. Experimental max quoted ≈3×10¹³ cm⁻². | Aggoune & Draxl 2021 |
| EDL gating | Ionic liquid DEME-TFSI on 5 nm LIO/110 nm MBE BSO on MgO. n2D up to ≈1×10¹⁴ cm⁻²; 6.52×10¹³ cm⁻² at 2 K, 8 V. μ ≈ 2100 cm²/Vs at 10 K, 1262 at 150 K. Ungated n2D and RT μ not reported; no SdH oscillations. | J. Lee, H. Cho, J. Park, B. Kim, D. G. Schlom, K. Char, "Observation of Mobility Above 2000 cm²/Vs in 2DEG at LaInO3/BaSnO3 Interface by EDL Gating", *Adv. Electron. Mater.* 2400811 (2024/25), doi:10.1002/aelm.202400811 [OPENED] |
| Other offsets | BaO/BSO 1.74 eV (P1). Al2O3/BSO ≈3.5 eV (P3, XPS). LaAlO3/BSO 3.7±0.1 eV, SrTiO3/BSO 0.6±0.1 eV (Chambers et al., doi:10.1063/1.4946762 [arXiv OPENED]). La:SrSnO3/BSO CBO only +0.10±0.02 eV, VBO 0.71 eV, so it is a poor barrier (Prakash et al., *Nano Lett.* 19, 8920 (2019) [OPENED]). LaScO3/BSO ≈1.2 eV (Cho et al., arXiv:2110.05738 [OPENED]). MgO gap ≈7.8 eV, CBO not found. No BaHfO3 or SrHfO3 offset found. | — |

## 3. Mobility and scattering times (linewidth input)

| System | n2D | μ | ħ/τ_tr (derived, m* = 0.2 m0) |
|---|---|---|---|
| LIO/BSO, EDL-gated, 10 K (Lee 2024) | ~0.65–1×10¹⁴ | 2100 | ≈2.8 meV |
| LIO/BSO, 150 K, gated (Lee 2024) | ~1×10¹⁴ | 1262 | ≈4.6 meV |
| LIO/BSO ungated RT (Ngabonziza review, arXiv:2408.10146 [OPENED]) | ~2×10¹⁴ | ~80 | ≈72 meV |
| LaScO3/BSO RT (Eom et al., arXiv:2110.02305 [OPENED]) | 1.7×10¹³ | 60 | ≈96 meV |
| LaScO3/BSO FET (Cho) | ~2×10¹³ | ~99 (field-effect) | ≈58 meV |
| EDL-gated BSO films RT (Wang et al., *PRMater.* 3, 075001 (2019) [OPENED]) | up to ~8×10¹³ | 12–51 | ≥110 meV |
| Bulk La:BSO crystals RT | 1e19–4e20 cm⁻³ | 200–320 | ≈18–29 meV |

Notes:
- ħ/τ_tr = ħe/(μm*), which gives 5.79 meV for μ = 1000 cm²/Vs at 0.2 m0. Scale it by 0.2/m* if a larger m* applies.
- Transport τ only bounds the ISB linewidth; it ignores interface roughness and intrasubband vs intersubband dephasing. P1 assumed γ = 10 meV.
- No quantum lifetime from SdH and no optical scattering time has been measured for any BSO 2DEG.

## Open gaps to flag in MAT-01
1. P4 is unread.
2. P2's parameters (paywalled).
3. LaInO3 IR phonons and ε∞ are unknown, so DFPT or an assumption is needed for the barrier LO/IF modes.
4. ε0 conflicts: BSO 17 vs 20; LIO 24 vs 38 (Char).
5. m* in Char-group simulations (0.42) vs 0.19 band edge.
6. The original experimental source of the 1.6 eV CBO is unidentified.
