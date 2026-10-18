# Nonlinear Quantum-Well Optics and Intersubband (ISB) Devices, 2018 to Oct 2026: Open Threads for a Solo Theorist

Scope note: These notes go beyond the threads the first survey already flagged: waveguide saturation bounds, programmable-QPM THz DFG, inverse design of bias-switchable stacks, RPA/TDHF chi(2), Ge/SiGe symmetric wells, mid-IR photon pairs, and ISB saturable absorbers for QCL mode-locking. When a new item overlaps one of these, the overlap is stated. Evidence levels used below:
- "Verified (abstract)" or "verified (full text)": I read the page this session.
- "Title-level": only a search-result title or snippet was seen.
- Tool/process note: the arXiv abstract page for 2505.23632 could not be read (proxy HTTP 429 rate limit), so its content is unknown.

---

## 1. ISB chi(2) and chi(3) processes (SHG, DFG/THz, OPO, rectification, THG/HHG, Kerr, saturable absorption, polaritonic metasurfaces): what is unresolved?

### Takeaway
Polaritonic ISB metasurfaces are the most active experimental front:
- Results so far: SHG above 0.1% efficiency, THG, and continuous-wave THz DFG, with full electrical amplitude and phase control of SHG (2025).
- Limits: performance is set by saturation, the depolarization-limited Rabi frequency, and the linewidth ratio γ2/Ω, and the community still models these with simple two-level Maxwell–Bloch models.
- Gaps for theory: there is no rigorous theory of the efficiency and contrast bounds, of time-modulated (nonreciprocal) operation, or of non-perturbative/high-harmonic ISB response.

### Cited Findings
**Review baseline (Krakofsky, Sarma, Brener, Alù, Lee, Belkin, Nanophotonics 14(23), 3709–3721, 2025; verified full text):**
- ISB dipoles are about 100 D across λ ≈ 3–30 µm. MQW chi(2) and chi(3) are 3–5 orders of magnitude above natural crystals — [Krakofsky et al. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12617711)
- SHG state of the art cited in the review — [Krakofsky et al. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12617711):
  - Lee et al., Nature 2014: χ(2)_eff ≈ 55 nm/V from a 400-nm InGaAs/AlInAs MQW at 8 µm pump.
  - Wolf et al. 2015: about 2.5 mW/W², and 0.14% power efficiency at 1–10 W pump.
  - Lee et al.: 0.075% efficiency at about 100 mW and about 15 kW/cm² (10 µm pump).
  - All-dielectric Ge grating (Sarma): about 1.1 mW/W², tunable over 8.5–11 µm.
  - Mie metasurface: 0.5 mW/W² at 7.65 µm.
  - Abstract headline: conversion above 0.1% in deeply subwavelength films at 10–100 kW/cm².
- III-nitride ISB SHG at 1.6 µm reaches a largest χ(2)_eff element of 1.3 nm/V (Wolf et al.) — [Krakofsky et al. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12617711)
- Kerr and saturable-absorption metasurfaces — [Krakofsky et al. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12617711):
  - χ(3) above 10⁻¹³ m²/V², with response times below 2 ps.
  - Reflection falls from about 0.64 at about 100 kW/cm² to below 0.1 at about 10 MW/cm² (ΔR ≈ 0.54 at 38.36 THz).
  - Saturation is non-negligible already at about 50 kW/cm².
- Theoretical limits stated in the review — [Krakofsky et al. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12617711):
  - Power-limiter contrast is bounded by ΔR ≤ 1/(1 + 2γ_aγ_2/Ω²)².
  - The maximum Rabi frequency is Ω_max ≈ 0.26 ω_q, versus 0.13 ω_q used to date.
  - Raising Ω further is "not feasible" without broadening, because thinner barriers broaden the line.
  - γ2 is more than 10× γ1.
- Open items the review states explicitly — [Krakofsky et al. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12617711):
  - Shorter wavelengths need GaN/AlN, GaN/AlGaN, TiN/Al2O3, or interband transitions.
  - Most devices are reflective (ground plane), so transmissive designs are wanted.
  - All-dielectric designs are wanted for lower loss.
  - Saturation limits total generated power, so pump, material, and photonics must be co-optimized.
  - Nonreciprocal routers have been proposed but not demonstrated.
  - THz DFG is "only theoretical" (their ref 18).
  - The review itself uses a simplified two-level Maxwell–Bloch model with a higher-subband loss term, and does not discuss quantum-optical effects.
- Conflict on THz DFG: Krakofsky, Stich, Böhm, and Belkin reported CW THz DFG from an ISB polaritonic metasurface at CLEO 2024 (conference paper; verified abstract):
  - χ(2) > 10⁵ pm/V. The exponent was garbled on the page, so treat this value with caution.
  - IR-to-THz conversion efficiency exceeded photomixers at 2.5–5 THz with commercial CW lasers.
  - So THz DFG from ISB metasurfaces is no longer purely theoretical, though only a conference report exists — [TUM portal, CLEO 2024](https://portal.fis.tum.de/en/publications/continuous-wave-terahertz-difference-frequency-generation-from-in/)
- Electrically tunable THG (Park, Yu, Boehm, Belkin, Lee, Light Sci. Appl. 13, 169, 2024; verified full text) — [Park et al. 2024](https://link.springer.com/10.1038/s41377-024-01517-y):
  - Susceptibilities: MQW |χ(3)_zzzz| = 7.15×10⁻¹⁴ m²/V² at 9 µm; metasurface |χ(3)_xxxx,eff| = 2.3×10⁻¹⁴ m²/V².
  - Efficiency: 1.38×10⁻⁴ % at 77 kW/cm².
  - Electrical control: 450% modulation depth, about 1.1π phase tuning (versus 135° in earlier SHG work), and beam steering to ±10.7°.
  - Model: a four-subband model with Poisson–Schrödinger Stark tuning.
  - Discrepancies they flag: measured spectral tuning (8.82 to 8.9 µm) fell short of simulation, which they attribute to nonuniform band bending from Schottky contacts. The RC-limited modulation cutoff is only about 3.38 MHz.
- Full complex-amplitude electrical control of SHG from ISB polaritonic metasurfaces appeared in Science Advances on 25 July 2025 (UNIST/TUM/Sandia; DOI 10.1126/sciadv.adw8852). Title and metadata only; the abstract was not retrieved. This is direct prior art for any bias-controlled chi(2) amplitude or sign scheme and should be cited in the user's manuscript — [Nature Index record](https://www.nature.com/nature-index/article/10.1126/sciadv.adw8852)
- Power limiters and switching: Mann et al., Optica 2021 ("Ultrafast optical switching and power limiting in intersubband polaritonic metasurfaces"), and arXiv 2403.15911 ("…high-contrast ultra-fast power limiting and optical switching"). Title-level — [Colorado nano-optics](https://nano-optics.colorado.edu/index.php/paper-2021-ultrafast-optical-switching-and-power-limiting-in-intersubband-polaritonic-metasurfaces); [arXiv 2403.15911](https://arxiv.org/pdf/2403.15911)
- Coherent vs incoherent nonlinearities (Cominotti, Leymann, Nespolo, Manceau, Jeannin, Colombelli, Carusotto, PRB 107, 115431, 2023; verified abstract) — [arXiv 2109.00285](https://arxiv.org/abs/2109.00285):
  - Method: time-dependent Schrödinger–Poisson (Hartree).
  - Prediction: the resonance redshifts with intensity because the dipole shrinks and the depolarization shift is suppressed. They compare this coherent nonlinearity against incoherent saturation from mid-IR to THz.
  - They call the quantum-optics (single-photon) direction "speculative."
- Optical rectification and THz emission from asymmetric ISB transitions: "Terahertz emission from AC Stark-split asymmetric intersubband transitions" (arXiv 1404.2326, 2014, before the window). Title-level; no 2018–2026 ISB-metasurface optical-rectification paper was found — [arXiv 1404.2326](https://arxiv.org/pdf/1404.2326)
- ISB high-harmonic generation in quantum wells: targeted searches returned only bulk or 2D-crystal HHG — [Andersen et al., PRA 109, 063109 (2024)](https://www.arxiv.org/abs/2404.06237v2); [Kim et al., arXiv 2503.04335, WS2](https://arxiv.org/abs/2503.04335v1). The closest QW-related hit was interband + THz high-order sideband generation (Feynman path-integral formula; title-level) — [NSF PAR 10470515](https://par.nsf.gov/biblio/10470515-explicit-formula-high-order-sideband-polarization-extreme-tailoring-feynman-path-integrals). A theoretical THz-2DCS framework (density matrix, perturbative and non-perturbative; Sept 2026) does not mention QWs in its abstract — [arXiv 2609.16623](https://arxiv.org/abs/2609.16623)
- ISB OPO/OPA: searches returned only 1990s optically pumped ISB emission work. I found no 2018–2026 ISB OPO proposal — [HUJI record](https://cris.huji.ac.il/en/publications/optically-pumped-intersub-band-emission-in-quantum-wells/)

### Inferences
- **Opportunity A: fundamental performance bounds for ISB polaritonic metasurface switches and limiters beyond the two-level model.**
  - Idea: replace the Maxwell–Bloch two-level bound with a multi-subband, nonparabolic, depolarization-shifted treatment, and ask whether InAs/AlSb, GaN, or multi-well designs beat Ω_max ≈ 0.26 ω_q at fixed γ2.
  - Toolkit fit: Schrödinger–Poisson, Ando depolarization, and multilevel saturation are all already built.
  - Experiment needed: no.
  - Done? Not found as a standalone bound paper (the review gives only the two-level formula). Partial overlap with the flagged "saturation-limited efficiency bounds," but this is about metasurface switching contrast, not waveguide conversion.
- **Opportunity B: Floquet/spatiotemporal Stark-modulated ISB metasurfaces for nonreciprocity and frequency shifting.**
  - Inputs: realistic Stark coefficients and RC limits (3.38 MHz in Park 2024 versus the 10 Gbit/s Stark modulators in section 6).
  - Experiment needed: no.
  - Done? No ISB-specific paper was found. The closest is a superconducting JoFET metasurface — [Taravati, arXiv 2409.08137](https://arxiv.org/abs/2409.08137). The review lists nonreciprocity as undemonstrated.
- **Opportunity C: non-perturbative, strong-field ISB harmonic generation (THG/5HG/HHG) in asymmetric and symmetric QWs.**
  - Method: time-dependent Schrödinger–Poisson with depolarization, extending Cominotti's TDSP to multi-subband, bias-switchable wells.
  - Experiment needed: no.
  - Done? No QW-specific 2018–2026 hit (search-level negative, so verify with a deeper arXiv full-text search).
- **Opportunity D: theory of CW THz DFG in ISB metasurfaces.**
  - Content: saturation- and heating-limited efficiency versus photomixers; design of doubly resonant three-level systems.
  - Experiment needed: no (an experiment exists).
  - Done? The theory side seems thin. It is distinct from the flagged waveguide/QPM THz DFG.
- **Opportunity E: transmissive and all-dielectric ISB nonlinear metasurface design.**
  - The user's planar TM-mode solver is not a full 3D FDTD, so this would need FDTD/RCWA. Medium fit.

### Gaps
- Exact numbers in the 2025 Sci. Adv. full-complex-amplitude SHG paper (authors, phase range, sign-reversal mechanism) were not retrieved. This must be checked against the user's sign-reversal QPM manuscript.
- The exponent of the CLEO 2024 χ(2) is uncertain.
- No reliable 2018–2026 sources were found on ISB OPO proposals or ISB optical-rectification metasurfaces. Absence is search-level only.

---

## 2. QCL frequency combs and nonlinear dynamics; ISB polaritons, ultrastrong coupling, electrically controlled coupling

### Takeaway
QCL nonlinear dynamics have moved to monolithic active-ring solitons:
- Nozaki–Bekki dark solitons (Nature 2024).
- DC-driven bright solitons, about 1 ps at 8.3 µm (Nature 2025).
- Microscopic inputs: these are the effective Kerr coefficient (Bloch gain, about 10⁻¹⁵ m²/W) and the linewidth enhancement factor (LEF, 0.1–1 from NEGF). Both are still poorly understood at a microscopic level, and density-matrix approximations can get the LEF sign wrong.
- ISB polaritons: stimulated scattering and LO-phonon scattering have now been seen, but no polariton lasing yet.

### Cited Findings
- Nozaki–Bekki solitons in ring QCLs — [Opačak et al., Nature 625, 685 (2024)](https://link.springer.com/article/10.1038/s41586-023-06915-7):
  - Free-running dark solitons form spontaneously by bias tuning, including multisoliton and soliton-crystal states (68 GHz beatnote).
  - Open: the coherence of the soliton crystal could not be characterized because 68 GHz exceeds the detector cutoff. The envelope shift is only "likely" due to a large GVD change. The authors frame the junction of laser multimode dynamics and Kerr parametric processes as "largely unexplored."
- Driven bright solitons on a mid-IR laser chip — [Kazakov et al., Nature 641, 83–89 (2025)](https://ideas.repec.org/a/nat/nature/v641y2025i8061d10.1038_s41586-025-08853-y.html):
  - Kazakov, Letsou, Piccardo, Columbo, Brambilla, Prati, …, Lugiato, Schwarz, Capasso.
  - About 1 ps pulses at 8.3 µm with GHz repetition, from a DC drive only.
  - Mechanism: fast bistability in an active nonlinear ring, with drive laser, ring, coupler, and filter monolithically integrated.
  - Runs for hours without stabilization.
- Bloch-gain-induced giant Kerr nonlinearity — [Opačak, Dal Cin, Hillbrand, Schwarz, arXiv 2102.08167 / PRL 127, 093902 (2021)](https://ar5iv.labs.arxiv.org/html/2102.08167):
  - The resonant Kerr contribution is about 10⁻¹⁵ m²/W, which they call two orders of magnitude above the highest bulk values.
  - Model: density matrix plus a single Bloch parameter b.
  - They state that "the origin of the dispersive spectral shape is not well understood." Tailoring the gain shape for ring solitons is open.
- NEGF linewidth enhancement factor — [Franckié, Bertrand, Faist, arXiv 2207.09222](https://ar5iv.labs.arxiv.org/html/2207.09222):
  - LEF ≈ 0.1–1 depending on bias and frequency.
  - A two-level RWA model gives at most about 0.04 (about 10% of NEGF). Counter-rotating terms contribute about −0.05.
  - Density-matrix approximations, even with dispersive gain, differ significantly and can give the wrong sign at the gain peak.
  - Limits: one frequency at a time, thermal effects excluded, no direct LEF measurement.
- QCL Roadmap 2026 — [Silvestri, Rakić, Indjin (eds.) et al., arXiv 2602.17042](https://arxiv.org/pdf/2602.17042):
  - The main comb challenge is emission bandwidth: FM combs above 100 cm⁻¹ at 1300 cm⁻¹, RF-driven up to 250 cm⁻¹, and above 1 THz at 3 THz.
  - For octave combs, nonlinear dispersion is the main obstacle.
  - Directions highlighted: ring soliton routing, quantum-walk combs, and mid-IR PICs for supercontinuum.
- Dissipative Kerr solitons in semiconductor ring lasers (2021; title-level) — [arXiv 2106.05078](https://arxiv.org/pdf/2106.05078)
- ISB polariton–polariton stimulated coherent scattering — [Knorr et al. (Huber, Colombelli, Carusotto), PRL 128, 247401 (2022)](https://pred.uni-regensburg.de/id/eprint/58228/):
  - GaAs/AlGaAs QWs in a dispersive microcavity, lower polariton at about 25 THz.
  - Probe reflectivity peaks at k∥ = 0.
  - Framed as a step toward bosonic lasing.
- ISB polariton–LO-phonon scattering — [Goulain, Jeannin, Pirotta, Bousseksou, Biasiol, Carusotto, Colombelli, Manceau, arXiv 2509.13843 (Opt. Mater. Express 2025)](https://arxiv.org/abs/2509.13843):
  - First observation of spontaneous polariton–LO-phonon scattering (emission one LO phonon below the pump) in non-dispersive cavities.
  - The rate is "extremely low." Stimulated gain via pump–probe is supported only numerically.
- Generalized Gross–Pitaevskii model for ISB polariton lasing (title-level) — [arXiv 1903.10213](https://arxiv.org/pdf/1903.10213)

### Inferences
- **Opportunity F: microscopic gain and Kerr spectra as design targets for ring-QCL solitons.**
  - Content: compute the complex χ(3)(ω, bias), meaning Kerr, Bloch-gain asymmetry, and LEF, with a multilevel density-matrix model that includes counter-rotating and non-resonant terms. Map which active-region designs yield the Kerr/GVD sign and magnitude needed for bright versus dark solitons (Kazakov 2025 vs Opačak 2024).
  - Experiment needed: no.
  - Done? Partially (Opačak 2021 Bloch-gain Kerr; Franckié 2022 NEGF LEF). A design-mapping paper linking heterostructure to soliton existence regions was not found.
  - Caveat: Franckié shows density-matrix models can mis-sign the LEF, so the user's toolkit (no NEGF) would need careful validation against published NEGF numbers. The TU Wien, ETH, and Harvard groups are strong incumbents.
- **Opportunity G: origin of the dispersive (Bloch) gain lineshape.**
  - Content: a k-resolved density-matrix treatment of scattering-assisted transitions with nonparabolicity, testing the "not well understood" statement.
  - Experiment needed: no.
  - Done? Opačak 2021 gives a phenomenological parameter. Some earlier first-principles treatments exist (Wacker, Willenberg; not re-verified here).
- **Opportunity H: design optimization of ISB polariton–LO-phonon stimulated scattering (polariton lasing threshold).**
  - Content: use the LO-phonon scattering code with Hopfield coefficients to find the QW and cavity designs that maximize the rate (Goulain 2025 calls it extremely low).
  - Toolkit fit: high.
  - Experiment needed: no.
  - Done? The Colombelli/Carusotto team has a custom model. A broad design-space study was not found.

### Gaps
- I did not verify a 2018–2026 paper explicitly on electrically gated ultrastrong coupling nonlinearities, beyond the metasurface papers in section 1.
- The QCL Roadmap sections on polaritons, quantum light (4.7), and modulators were not reached in the fetch, which covered about 100k characters.
- Faist-group 2023–2026 comb theory papers (for example on RF injection and quantum-walk combs) were not verified individually.

---

## 3. Quantum ISB photonics (entanglement, squeezing, single-photon nonlinearity, polariton blockade)

### Takeaway
The quantum ISB regime remains almost entirely theoretical.
- The strongest recent proposal is Oliveira and Ciuti (Oct 2025). Photon-exchange-bound "excitons" of bound-to-continuum ISB polaritons give Rydberg-like, giant mid-IR/far-IR quantum nonlinearities.
- On the experimental side, even QCL/ICL sub-shot-noise work is blocked by excess noise and detector mismatch.

### Cited Findings
- Oliveira and Ciuti, "Strong quantum interaction between excitons bound by cavity photon exchange" — [arXiv 2510.24421 (Oct 2025)](https://arxiv.org/abs/2510.24421):
  - Setup: a cavity coupled to bound-to-continuum ISB transitions in a doped QW.
  - Mechanism: polariton–polariton interactions come from Coulomb and Pauli blocking. Lowering the binding energy (tuned by the cavity frequency) enhances interactions through a larger Bohr radius along the growth direction (Rydberg analogy).
  - Prediction: "giant quantum optical nonlinearities in the mid and far infrared." Theory only.
- Cominotti et al. (2023) call single-photon mid-IR/THz ISB emission "speculative" — [arXiv 2109.00285](https://arxiv.org/abs/2109.00285)
- Electron-to-photon noise transfer in commercial QCLs and ICLs — [La Penna et al., arXiv 2512.05636 (Phys. Rev., DOI 10.1103/3t25-1gnk)](https://arxiv.org/abs/2512.05636):
  - A driver with noise up to 10 dB below shot noise was used.
  - The main obstacles to quantum light are laser excess noise and laser–detector bandwidth and power mismatch.
- Interband cascade laser quantum photonics and amplitude-squeezing models from the Grillot group (title-level) — [HAL 04559877](https://hal-imt.archives-ouvertes.fr/hal-04559877v1); [IP Paris record](https://researchportal.ip-paris.fr/en/publications/modeling-of-amplitude-squeezing-in-a-pump-noise-suppressed-interb/)
- Interband χ(2) coupled QWs are proposed for telecom entangled photons; no demonstration yet — [Ramesh et al., arXiv 2602.23246](https://arxiv.org/abs/2602.23246)

### Inferences
- **Opportunity I: materials-specific realization of the Oliveira–Ciuti mechanism.**
  - Content: use Schrödinger–Poisson with nonparabolicity and a discretized continuum to compute bound-to-continuum oscillator strengths, effective Bohr radii, and interaction constants U/γ for real InGaAs/InAlAs, GaAs/AlGaAs, and InAs/AlSb wells and cavity volumes. Then state whether the blockade criterion U > γ is reachable in patch-antenna microcavities.
  - Experiment needed: no.
  - Done? Not found (the 2025 paper is model-level). Timeliness is high; Ciuti's group may follow up itself.
- **Opportunity J: quantum-noise (squeezing) model of QCLs with sub-shot pump noise.**
  - Content: rate equations with Langevin noise, using the multilevel rate-equation code.
  - Experiment needed: no, but it should be compared with La Penna 2025 data.
  - Done? Partially for ICLs (Grillot group). A QCL-specific cascade model with realistic LO-phonon lifetimes appears less covered (not verified).
- Mid-IR photon pairs are already flagged and are not repeated here.

### Gaps
- I found no 2018–2026 experiment showing ISB polariton blockade or single-photon ISB nonlinearity.
- The QCL Roadmap section 4.7 (quantum light) was not read.

---

## 4. Materials: GaN/AlN, ScAlN, ZnO, InAs/AlSb, 2D vdW (WSe2), oxide QWs

### Takeaway
Near-IR ISB nonlinear optics has seen only modest progress:
- GaN/AlN SHG at 1.6 µm with χ(2) ≈ 1.3 nm/V, and all-optical switching with high saturation intensity.
- 2D vdW ISB transitions are now imaged and gate-tuned, but nonlinear (χ(2)/χ(3)) ISB response in gated TMD multilayers appears unexplored.
- I could not verify ScAlN, ZnO, or oxide-QW ISB nonlinear work in this session.

### Cited Findings
- III-nitride ISB SHG at 1.6 µm: largest χ(2)_eff element 1.3 nm/V (Wolf et al., via the review) — [Krakofsky et al. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12617711)
- GaN/AlN telecom ISB plus plasmonic antenna nonlinear metasurface (2021; title-level) — [arXiv 2105.09726](https://www.arxiv.org/abs/2105.09726)
- GaN/AlN ISB all-optical switching (pre-window baseline) — [Li, …, Moustakas, Paiella, Opt. Express 15, 17922 (2007)](https://www.bu.edu/paiella/files/2021/08/OE_AlGaN_ISB_PumpProbe.pdf):
  - Measured: Isat ≈ 9.6 W/µm² at 1.55 µm (theory 3.9 W/µm²), and 10 dB at 38 pJ.
  - Simulated: AlN/GaN/AlGaN coupled QWs could cut Isat by more than 30×. This was "not demonstrated experimentally."
- 2D vdW ISB:
  - Nano-imaging of ISB transitions in few-layer vdW QWs, Nat. Nanotechnol. 2018 (title-level) — [arXiv 1806.09519](https://arxiv.org/pdf/1806.09519); [DOI](https://www.doi.org/10.1038/s41565-018-0233-9)
  - Hybrid k·p tight-binding subband model for MoS2, MoSe2, WS2, WSe2 films (title-level) — [arXiv 1808.01540](https://arxiv.org/pdf/1808.01540)
  - "Electrical Control of Intersubband Transitions in Few-Layer WSe2 Multivalley Quantum Wells Probed by Electronic Raman Scattering" (title-level) — [PMC12895561](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12895561/)
  - A Sapienza project, "Infrared detection using quantum wells of van der Waals semiconductors" (title-level) — [Uniroma1](https://research.uniroma1.it/progetti-di-ricerca/103287/vista)
- InAs/AlSb near-IR ISB in delta-doped MQWs (title-level, older) — [ASU record](https://asu.elsevierpure.com/en/publications/near-infrared-intersubband-transitions-in-delta-doped-inasalsb-mu/). An InAs SWIR ISB document from C2N also exists (title-level) — [C2N pdf](https://odin.c2n.universite-paris-saclay.fr/media/filer_public/ae/79/ae794d6e-8e61-4b5f-a482-7797b61d20ea/inas_-_swir_-_15023284.pdf)
- ZnO/MgZnO triple-QW ISB absorption (title-level; appears to be a theory paper) — [REDI record](https://redi.cedia.edu.ec/document/297511)
- Purdue (Malis, Manfra) has NSF-PAR-indexed nitride ISB papers, but ScAlN ISB content was not verified (title-level author listings only) — [NSF PAR Malis](https://par.nsf.gov/search/author:%22Malis,%20Oana%22)

### Inferences
- **Opportunity K: gate-induced χ(2) (and electrically switchable χ(2) sign) in few-layer TMD ISB stacks.**
  - Idea: gating breaks inversion symmetry, which is the 2D analogue of the user's bias-polarity sign reversal.
  - Experiment needed: no.
  - Done? Not found. Requires layer-resolved k·p/TB inputs from the 1808.01540 model, which the toolkit lacks. Medium fit.
- **Opportunity L: polarization-field-engineered, bias-switchable χ(2) in GaN/AlN or AlGaN coupled wells at 1.3–2 µm.**
  - Content: includes a coupled-well Isat reduction study revisiting the 30× claim with modern nitride parameters.
  - Experiment needed: no.
  - Done? Partially (older simulations). Needs a nonparabolic nitride band model with built-in piezo/spontaneous fields, a modest extension of Schrödinger–Poisson.
- InAs/AlSb (about 2.1 eV conduction band offset) is a natural platform for near-IR versions of the user's mirror-symmetric triple-well QPM concept. The status of such work is unknown.

### Gaps
- ScAlN ISB: no usable source found.
- Oxide QWs (for example SrTiO3, β-Ga2O3/(AlGa)2O3) ISB nonlinear work: not searched successfully.
- ZnO ISB nonlinear experiments 2018–2026: not found.

---

## 5. Modeling methods: NEGF for nonlinear response, non-Lorentzian lineshapes and χ(2) phase, density matrix vs Maxwell–Bloch, ML surrogates, inverse design

### Takeaway
- NEGF is the gold standard but takes hours per simulation and treats electron–electron interactions mostly at the Hartree level. Density-matrix models can mis-sign key nonlinear quantities.
- ML for QCL design is emerging (Princeton 2024), but ML surrogates for nonlinear χ(2)/χ(3) spectra and phase appear absent.
- The Bloch (dispersive) gain lineshape and LEF show that lineshape physics directly sets nonlinear phase.

### Cited Findings
- Modeling state of the art from the QCL Roadmap 2026 — [arXiv 2602.17042](https://arxiv.org/pdf/2602.17042):
  - NEGF is "the most general, but also the most computationally expensive," "often requiring hours per simulation."
  - Electron–electron scattering is "often only treated in Hartree approximation."
  - Most transport models compute unsaturated gain, so output power and wall-plug efficiency modelling is lacking.
  - The design space for a 3-well RP design is about 10⁶ combinations.
  - Suggested tools: Bayesian optimization, ML, GPU transport, and linear-scaling density-matrix methods.
- A machine learning framework for QCL design (Princeton, 2024; title-level) — [arXiv 2406.07755](https://arxiv.org/pdf/2406.07755). See also "Inverse-quantum-engineering" (NAU, title-level) — [NAU record](https://experts.nau.edu/en/publications/inverse-quantum-engineering-a-new-methodology-for-designing-quant/)
- NEGF versus density-matrix discrepancy for the LEF (sign errors at the gain peak) — [Franckié et al., arXiv 2207.09222](https://ar5iv.labs.arxiv.org/html/2207.09222). An earlier NEGF α-factor theory exists (SPIE 9934, title-level) — [SPIE](https://astronomicaltelescopes.spiedigitallibrary.org/conference-proceedings-of-spie/9934/993408/Nonequilibrium-Greens-functions-theory-for-the-alpha-factor-of-quantum/10.1117/12.2238619.full)
- Bloch-gain dispersive lineshape is "not well understood" — [Opačak et al. 2021](https://ar5iv.labs.arxiv.org/html/2102.08167)
- A time-dependent Schrödinger–Poisson (Hartree) approach for coherent ISB nonlinearity — [Cominotti et al. 2023](https://arxiv.org/abs/2109.00285)
- The Bank/Khurgin interband χ(2) paper includes an ML co-author (Shakkottai) and reports that measured χ(2) approaches ideal-interface predictions only with growth interruptions. This means interface-profile modelling from electron microscopy is central — [Ramesh et al., arXiv 2602.23246](https://arxiv.org/abs/2602.23246)

### Inferences
- **Opportunity M: a validated ML surrogate (or differentiable solver) for complex χ(2)(ω1, ω2; V) and χ(3) spectra, including phase.**
  - Content: generate the training set with the user's density-matrix χ(2) and Schrödinger–Poisson codes. Release it as an open dataset and model, then use it for inverse design of sign-switchable and phase-programmable stacks.
  - Experiment needed: no.
  - Done? Not found for nonlinear ISB. It partly overlaps the flagged "inverse design" thread, but the dataset/surrogate as an artifact is a separate contribution (fits Opt. Express, APL Machine Learning, Nanophotonics).
- **Opportunity N: interface-roughness and interdiffusion tolerance analysis of χ(2) magnitude and sign for coupled-well designs.**
  - Content: a Monte Carlo over graded interfaces. Motivated by the Bank group's finding that interface abruptness limits χ(2).
  - Experiment needed: no.
  - Done? Not found for ISB sign-reversal designs. It would directly strengthen the user's manuscript.
- **Opportunity O: benchmark of density-matrix vs Maxwell–Bloch vs TDSP predictions of SHG saturation in metasurfaces.**
  - Content: a methods paper quantifying when the review's two-level model fails.
  - Experiment needed: no.
  - Done? Not found.

### Gaps
- I did not verify 2018–2026 NEGF calculations of χ(2) specifically (as opposed to gain or LEF). The Wacker, Jirauschek, Lindskog, and Winge lines were not individually confirmed.
- Non-Lorentzian ISB lineshape effects on χ(2) phase: only older lineshape theory hits were found (title-level) — [NAU lineshape theory](https://experts.nau.edu/en/publications/theory-of-the-lineshape-of-quantum-well-intersubband-transitions-/)

---

## 6. Interband nonlinearities in coupled QWs (Khurgin/Bank 2026), mid-IR QCSE/ISB modulators, QWIPs and QCDs as nonlinear elements

### Takeaway
2026 brought a revival of engineered interband χ(2) in asymmetric AlGaAs/GaAs coupled QWs:
- Measured: 2750 pm/V at 1550 nm (7× bulk GaAs).
- With a metasurface: about 14 nm/V effective at 1.57 µm.
- Predicted: up to about 7 nm/V for complex layer designs.

Mid-IR unipolar Stark modulators reach 10 Gbit/s at 9 µm, and two-photon QWIPs exist as quadratic detectors.

### Cited Findings
- "Enhanced Interband Optical Nonlinearities from Coupled Quantum Wells" — [arXiv 2602.23246, 26 Feb 2026](https://arxiv.org/abs/2602.23246):
  - Authors: Ramesh, Brown, Ricks, …, Brener, Pan, Alù, Wasserman, Khurgin, Bank.
  - Measured χ(2) up to 2750 pm/V for SHG 1550 → 775 nm in AlGaAs/GaAs CQWs (more than 7× GaAs). Growth interruptions improve abruptness toward ideal-interface predictions.
  - Complex designs are predicted to reach "up to 7 nm/V," with the unit ambiguous in the abstract.
  - Telecom entangled photons are proposed.
- "Quantum-Well-Metasurface to Maximize Nonlinear Polarization" — [Fathi, …, Bank, Capasso, arXiv 2604.15476, 16 Apr 2026](https://arxiv.org/abs/2604.15476):
  - Intrinsic interband tensor element of 1.6 nm/V at 1.57 µm in a band-engineered GaAs/AlGaAs stack.
  - About 14 nm/V effective with a high-Q dielectric metasurface that accesses the zzz element.
  - Proof-of-concept experiment.
- The UT Austin LASE group (Bank) bibliography lists "Engineering of the Interband Second Order Optical Nonlinearity with Asymmetric Coupled Quantum Wells" and "Interband second-order nonlinear optical susceptibility of asymmetric coupled quantum wells" (title-level; likely the theory precursors) — [LASE ref 340](https://lase.ece.utexas.edu/bibcite/reference/340); [LASE ref 339](https://lase.ece.utexas.edu/bibcite/reference/339)
- 10 Gbit/s free-space link at 9 µm with unipolar quantum optoelectronics — [Dely, …, Vasanelli, Sirtori, arXiv 2110.06572](https://arxiv.org/abs/2110.06572):
  - Uses a QCL, a Stark-type amplitude modulator that shifts an ISB absorption across the laser line, and an ISB detector.
  - The modulator bandwidth number was not in the abstract.
- Room-temperature 9 µm photodetectors and GHz heterodyne receivers (Nature 2018, Sirtori group; title-level) — [Nature 556](https://www.nature.com/articles/nature25790). Patch-antenna QCD heterodyne receivers (title-level) — [arXiv 2003.10752](https://arxiv.org/pdf/2003.10752). A 70 GHz detector paper (Hakl et al., ACS Photonics; title-level) — [C2N pdf](https://odin.c2n.universite-paris-saclay.fr/media/filer_public/3b/72/3b721c78-331a-4bd3-a8ca-dfac306808fd/hakl_-_70ghz_-_acsphotonics0c01299.pdf)
- Two-photon QWIPs as quadratic detectors and autocorrelators, including "Two-photon quantum well infrared photodetectors below 6 THz" (HZDR; title-level, year not confirmed) — [HZDR Publ-22289](https://hzdr.de/publications/Publ-22289); [HZDR Publ-12135](https://www.fzd.de/publications/Publ-12135)
- The THG metasurface modulation bandwidth is RC-limited at about 3.38 MHz — [Park et al. 2024](https://link.springer.com/10.1038/s41377-024-01517-y)

### Inferences
- **Opportunity P: bias-switchable sign of interband χ(2) in mirror-symmetric coupled QWs for electrically poled QPM at 1550 → 775 nm.**
  - Idea: the direct telecom/interband analogue of the user's ISB sign-reversal QPM manuscript.
  - Experiment needed: no.
  - Done? Not found. The Bank/Khurgin papers use fixed asymmetric designs.
  - Requires a multiband (electron + heavy/light hole) k·p extension of the toolkit, plus excitonic corrections. Competition from the Bank/Khurgin/Brener team is high, and fast publication is advised.
- **Opportunity Q: doubly resonant two-photon QWIP/QCD designed for ps autocorrelation of 8 µm ring-QCL solitons.**
  - Motivation: Opačak 2024 could not characterize 68 GHz states. Kazakov 2025 pulses are about 1 ps.
  - Experiment needed: no for the design paper.
  - Done? Two-photon QWIPs exist (HZDR). A design targeted at QCL soliton characterization was not found.
  - Toolkit fit: high (Schrödinger–Poisson, χ(3)-like two-photon rates, LO-phonon lifetimes).
- **Opportunity R: bandwidth-limit theory of ISB Stark modulators.**
  - Content: tunneling time, RC, and capacitance of patch arrays, and a Stark coefficient vs insertion-loss figure of merit, including chirp from the ISB "QCSE." The electrode Laplace solver is directly relevant.
  - Experiment needed: no.
  - Done? The Sirtori group has device papers. A general figure-of-merit/bound paper was not found.

### Gaps
- Mid-IR interband QCSE modulators (for example in type-II or Sb-based QWs) for 2018–2026 were not found in this session.
- The arXiv 2505.23632 abstract could not be read (HTTP 429), so its relevance to ISB modulators is unknown.
- A Polimi Optics Express 30(26) 46710 (2022) PDF appeared in modulator searches but was not read (title-level, topic unknown) — [Polimi](https://re.public.polimi.it/retrieve/e268f985-6cda-453f-826a-910a5bf3efc6/oe-30-26-46710.pdf)

---

## 7. Which theory-only papers are publishable now and where?

### Takeaway
The best near-term, experiment-free opportunities for this toolkit, in descending order of fit and novelty:
1. Interface-tolerance and robustness analysis of sign-reversal χ(2) designs (N). This strengthens the existing manuscript.
2. A materials-specific estimate of Oliveira–Ciuti Rydberg-like ISB polariton blockade (I).
3. A two-photon QCD/QWIP design for mid-IR soliton characterization (Q).
4. Bounds for ISB metasurface limiters and switches beyond the two-level model (A).
5. Floquet Stark-modulated ISB metasurfaces for nonreciprocity (B).
6. Polariton–LO-phonon lasing-threshold design maps (H).
7. An interband sign-switchable χ(2) QPM at 1550 nm (P; needs a k·p extension).
8. Non-perturbative ISB harmonics via TDSP (C).
9. A χ(2) surrogate/dataset (M).
10. Microscopic Kerr/LEF design maps for ring-QCL solitons (F/G; high incumbent competition).

### Cited Findings
- Precedent for theory-only ISB nonlinear papers in PRB: Cominotti et al., PRB 107, 115431 (2023) — [arXiv 2109.00285](https://arxiv.org/abs/2109.00285)
- Precedent for theory-only ISB quantum-optics preprints (Oliveira and Ciuti 2025; venue not yet known) — [arXiv 2510.24421](https://arxiv.org/abs/2510.24421)
- Precedent for theory/computation of QCL nonlinearity in PRL (Opačak et al. 2021, Bloch-gain Kerr; density-matrix plus GPU master equation) — [ar5iv 2102.08167](https://ar5iv.labs.arxiv.org/html/2102.08167)
- Precedent for an NEGF-only LEF paper, with no experimental LEF measurement — [Franckié et al. 2207.09222](https://ar5iv.labs.arxiv.org/html/2207.09222)
- Precedent for a model-plus-experiment ISB metasurface paper (Light Sci. Appl.), showing the experimental incumbents (Lee/UNIST, Belkin/TUM) — [Park et al. 2024](https://link.springer.com/10.1038/s41377-024-01517-y)
- The QCL Roadmap explicitly calls for Bayesian/ML optimization, linear-scaling density-matrix methods, and saturated-gain/output-power modelling — [arXiv 2602.17042](https://arxiv.org/pdf/2602.17042)

### Inferences
Venue mapping is my judgement, not sourced:
- PRB: I (blockade), G (Bloch lineshape), C (TDSP harmonics).
- PR Applied: A (bounds), R (modulator figure of merit), Q (two-photon detector design), H (polariton lasing threshold).
- Optics Express / JOSA B / IEEE JQE: N (tolerance), M (surrogate), F (design maps).
- Nanophotonics / ACS Photonics: B (Floquet ISB metasurfaces), K (2D vdW gated χ(2)).
- Optica / APL Photonics: P (interband electrically poled QPM), if it has a strong design-to-device story.

Other points:
- Experiment needed: none of A–R strictly requires an experiment. A/B/D/P/Q are stronger with a named experimental collaborator: Lee/UNIST, Belkin/TUM, Sarma/Brener/Sandia, Bank/UT Austin, Sirtori/ENS.
- Competition risk is highest for F/G (TU Wien, ETH, Harvard) and P (UT Austin/Johns Hopkins/Sandia). It is lowest for Q, R, H, and N.
- The user's manuscript must cite and differentiate itself from Sci. Adv. 2025 (DOI 10.1126/sciadv.adw8852) on full complex-amplitude (and likely sign) electrical control of ISB SHG. It should also cite Park et al. 2024 for electrically induced phase gratings in THG.

### Gaps
- "Done or not done" judgements for the opportunities are based on targeted web searches (about 50 tool calls), not exhaustive arXiv full-text searches. Each item marked "not found" needs a Google Scholar/arXiv citation-chain check before submission.
- Journal scope and acceptance tendencies for theory-only ISB papers were not sourced.
