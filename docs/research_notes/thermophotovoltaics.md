# Thermophotovoltaics (TPV) and thermal-photonic energy conversion: open threads, QW/intersubband roles, and theory-only paper opportunities (2018 to Oct 2026)

Scope note. The research ran on 2026-10-10 using about 55 search and fetch calls. Several primary pages were blocked: PMC and HAL returned bot-check pages, and some Nature pages redirected. Where a number comes only from an aggregator (patsnap, pv-magazine) or only from a title, it is labelled. Items marked "[training knowledge, not re-verified]" come from prior knowledge and were NOT confirmed in this session. The report writer should treat them as leads, not facts.

Researcher-fit note: The University of Oklahoma "Rui Yang" in TPV is most likely **Rui Q. Yang** (OU ECE). He is an interband-cascade (IC) device physicist whose group publishes IC thermophotovoltaic cells built from InAs/GaSb-type QW and superlattice structures. That is a QW-structure TPV line, not a far-field thermal-radiation line. It is distinct from Ronggui Yang, a thermal-radiation and heat-transfer researcher at other institutions. See the OU sources under Q2. This matters for fit: the researcher's Schrödinger–Poisson and QW toolkit maps directly onto IC-TPV modeling.

---

## Q1. Far-field TPV records (MIT/NREL tandem, Michigan air-bridge, NREL single-junction, Antora/Fourth Power): what limits them and what modeling questions are open?

### Takeaway
Far-field TPV is now in the 39–44% regime. MIT/NREL reached 41.1% with a 1.4/1.2 eV tandem at about 2400 °C. NREL reached 38.8% with 0.74 eV GaInAs at 1850 °C and 3.78 W/cm². Michigan reached about 44% with a 0.90 eV InGaAs air-bridge cell at 1435 °C and about 99% out-of-band reflectance. The remaining limits are out-of-band parasitic absorption (free-carrier absorption in substrates and contacts, imperfect reflectors), series resistance at high current density, view factor, and emitter durability. Two startups, Antora and Fourth Power, are commercializing with grid-storage targets. The open modeling questions are system-level: reflectance-limited efficiency, high-flux transport, and the efficiency versus power-density trade-off at lower storage temperatures.

### Cited Findings
- **MIT/NREL (LaPotin, Henry et al., Nature 604, 2022).** The 1.4/1.2 eV two-junction III–V device reached 41.1 ± 1% at 2400 °C and 2.39 W/cm², under 30.4 W/cm² irradiance. The 1.2/1.0 eV device reached 39.3 ± 1% at 2127 °C and 1.8 W/cm². The cells were designed for 1900–2400 °C emitters and use high-reflectivity back-surface reflectors to return sub-bandgap light to the emitter. — [arXiv 2108.09613](https://arxiv.org/abs/2108.09613); [Nature citation (RePEc)](https://ideas.repec.org/a/nat/nature/v604y2022i7905d10.1038_s41586-022-04473-y.html)
- **NREL single-junction (Tervo, Steiner et al., Joule 2022).** 0.74 eV GaInAs reached 38.8 ± 2.0% at 1850 °C, with 3.78 W/cm² over 0.8 cm². The authors credit an optimized architecture, spectral management, material quality and very low series resistance. They also report early two-junction 0.84 eV GaInPAs / 0.74 eV GaInAs results. — [arXiv 2207.00565](https://arxiv.org/abs/2207.00565); [UW–Madison ETC lab news](https://etclab.engr.wisc.edu/2022/10/28/new-paper-on-efficient-scalable-thermophotovoltaic-cells-published-in-joule/)
- **Michigan air-bridge (Roy-Layinde, Lenert, Forrest et al., Joule 2024).** About 44% efficiency, with 43.8% for the 0.90 eV InGaAs cell at a 1435 °C emitter. Bandgaps of 0.74, 0.90 and 1.1 eV were tested. Reflectance was nearly 99% ("nearly perfect mirror"), with a 570 nm air-bridge layer and a 1 µm membrane. The 2020 air-bridge cells reached 32% and earlier designs 37% in the same temperature range. Forrest says they are "not yet at the efficiency limit." Lenert says storage could run at 1300 °C instead of 2000 °C, giving about 2× the energy per kg of graphite. The device is not yet at kW or MW scale. — [pv magazine USA](http://pv-magazine-usa.com/2024/05/28/u-s-scientists-develop-air-bridge-thermophotovoltaic-cells-with-44-efficiency/); journal attribution confirmed by [Jeyar et al. arXiv 2412.04258](https://arxiv.org/html/2412.04258v1) ("almost 44%" single-junction, Roy-Layinde et al., Joule 2024)
- **Fourth Power (MIT spin-out, Henry).** Graphite storage at 1900–2400 °C with a liquid-tin heat-transfer loop. A full-scale unit is 25 MW / 250 MWh (10 to over 100 h). The company claims about 100 MW per acre against roughly 10 MW per acre or less for typical storage, and about 1% per day heat loss. A 1 MWh system is planned at its Bedford, MA headquarters "later this year" (article dated March 2026). The stated challenges are materials cycling, corrosion and thermal expansion. — [MIT News, Mar 2026](https://news.mit.edu/2026/turning-extreme-heat-large-scale-energy-storage-0318)
- **Antora Energy.** Claims more than 40% TPV cells and a 2 MW/yr TPV cell line in Sunnyvale (press release 24 Jan 2023), with an NREL collaboration since 2018. Carbon-block storage discharges at up to 1500 °C or higher. Cell materials are not disclosed. — [Antora TPV page](https://antoraenergy.com/tpv); [pv magazine](https://www.pv-magazine.com/?p=32370)
- **Ge TPV (Datas group, UPM Madrid, arXiv Feb 2026).** First calorimetric efficiency measurement of Ge TPV: 7.3% and 1.77 W/cm² at 1480 °C (Au rear contact), and 6.3% and 1.22 W/cm² at 1426 °C for a PERC-type cell. A validated model identifies out-of-band losses as dominant, mainly free-carrier absorption in the doped substrate. Earlier Ge projections drop to as low as 8.1% under the realistic graphite spectrum. A simulated AlN/W selective emitter could reach 22.3% at 1800 °C. InGaAs beats Ge under identical conditions. — [arXiv 2602.08761 via papers.cool](https://papers.cool/arxiv/2602.08761)
- **UPM 2023, aggregator-only.** 26.4% efficiency at view factors up to 0.98 with InGaAs cells and 4.3 W/cm². — [patsnap blog (aggregator, low confidence)](https://www.patsnap.com/resources/blog/articles/thermophotovoltaic-tech-hits-40-efficiency-in-2026/)
- **Measurement standardization (title-level only).** NREL has a paper titled "Platform for Accurate Efficiency Quantification of >35% Efficient Thermophotovoltaic Cells." — [NREL research hub](https://research-hub.nrel.gov/en/publications/platform-for-accurate-efficiency-quantification-of-gt-35-efficien-2/)
- **Zero-vacuum-gap TPV (Habibi, …, Tervo, Steiner, Longji Cui; Energy Environ. Sci., published 27 Dec 2024; CU Boulder, NREL, UW–Madison).**
  - Design: a fused-quartz spacer (n = 1.45) replaces the vacuum gap.
  - Power: about 2× the far-field power density at 700–1100 °C, and about 60% above the gap-integrated far-field blackbody limit with a graphite emitter. This is comparable to near-field TPV at a vacuum gap of about 200 nm.
  - Cell and efficiency: 0.74 eV InGaAs cell. Efficiency was below 5% with a 2 cm spacer and nearly 19% with a 10 cm spacer.
  - Modeling: up to about 30% at 1200 K, and about 17× power with an a-Si spacer (modeled only).
  - Stated limits: spacer conduction, sub-bandgap absorption in the spacer, side-wall escape, series resistance, and the need for a cell below 0.7 eV for medium temperatures.
  — [RSC EES d4ee04604h](https://pubs.rsc.org/en/content/articlehtml/2025/ee/d4ee04604h)
- **Front-contact modeling (Jeyar, …, Vaillon, Antezza, arXiv Dec 2024).** In near-field InAs cells, the shadowing approximation for front metal grids systematically overestimates efficiency. The authors recommend grating height below about 500 nm and a low filling fraction. — [arXiv 2412.04258](https://arxiv.org/html/2412.04258v1)

### Inferences
- In single-junction cells, the efficiency frontier is set mainly by **out-of-band reflectance R_oob**. Moving from about 98.5% to 99%+ is worth several absolute points because sub-bandgap power dominates at about 1300–1500 °C. Free-carrier and intervalence-band absorption in doped contact and substrate layers is the measured dominant loss in Ge and is a known limiter in InGaAs. This favours modeling papers on parasitic absorption in heavily doped layers, and the researcher's multilayer and TM-mode solver applies directly.
- The three groups chose different operating points (2400 °C tandem, 1850 °C 0.74 eV, 1435 °C 0.9 eV air-bridge). That makes a unified "efficiency × power density × storage-temperature" Pareto analysis valuable for system work. It is theory-only, but partly done in reviews; see Gaps.
- At 2–4 W/cm² and fill-factor-limited operation, lateral series resistance and contact-grid design couple to optics. The coupled optics + 2D/3D electrical modeling question is open beyond simple shadowing.

### Gaps
- Could not retrieve the full LaPotin or Roy-Layinde papers for their loss breakdowns (series resistance, R_oob values). [training knowledge, not re-verified]: Fan et al., Nature 2020, "Near-perfect photon utilization in an air-bridge thermophotovoltaic cell" reported about 98.5% out-of-band reflectance and about 32% at about 1455 K. Burger, Sempere, Roy-Layinde & Lenert, Joule 2020, "Present efficiencies and future opportunities in thermophotovoltaics" is the standard review. Neither was confirmed here.
- No verified 2025–2026 far-field efficiency record above about 44% was found. No independent technical data on Antora's or Fourth Power's cell bandgaps or module efficiency were found.
- I did not find a published TPV-specific Auger-limited efficiency map for 0.5–0.75 eV absorbers under air-bridge reflectance; see Q2.

---

## Q2. QW/MQW and low-bandgap TPV cells (InGaAs/InGaAsP, GaSb-based, InAs/GaSb and InAs/InAsSb superlattices, interband cascade): Auger and radiative limits, QW band-edge absorption

### Takeaway
QW-TPV was an active 1990s–2000s topic: Barnham-group "advantages of QW cells for TPV," and strain-compensated InGaAs/InGaAs QW cells with about a 2 µm band edge (CNR/Tyndall). Since 2018 it has been nearly dormant in the records race, which is dominated by bulk 0.74–0.9 eV InGaAs and III–V tandems. The live QW-structure threads are in **very-low-bandgap cells** for low-temperature heat. These are OU's interband cascade TPV (about 0.4 eV, 9.6% for 3-stage at 300 K; about 0.2 eV multistage) and Montpellier's InAs/InAsSb T2SL barrier cells (0.23 eV), whose efficiencies are still low because of dark current and Auger. A modern detailed-balance and Auger re-analysis of QW absorbers in the high-reflectance, thin-absorber, photon-recycling regime appears to be open.

### Cited Findings
- **Historical QW-TPV anchors (title-level only).**
  - "Advantages of quantum well solar cells for TPV." — [OSTI 577804](https://www.osti.gov/biblio/577804)
  - "Strain-compensated InGaAs/InGaAs quantum well cell with 2 micron band-edge." — [CNR](https://data.cnr.it/data/http://www.cnr.it/ontology/cnr/individuo/prodotto/ID233764)
  - "A comparative study of bulk InGaAs and InGaAs/InGaAs strain compensated [QW cells]." — [UCC](https://research.ucc.ie/en/publications/a-comparative-study-of-bulk-ingaas-and-ingaasingaas-strain-compen/)
  - US patent 6150604, "Quantum well thermophotovoltaic energy converter." — [USPTO](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6150604)
- **Interband cascade TPV (OU, Sandia, WVU; IEEE J. Photovoltaics vol. 7 no. 5, about 2017).** About 0.4 eV bandgap at 300 K. The 3-stage cell gave Voc about 800 mV and 9.6% maximum power efficiency; the 2-stage cell gave Voc about 530 mV and 6.5% (300–340 K). Each stage has a thin absorber, and the authors adapt the Suns-Voc method to extract series and shunt resistance. — [OSTI 1497660](https://www.osti.gov/biblio/1497660); [Sandia listing](https://sandia.gov/research/publications/details/narrow-bandgap-interband-cascade-thermophotovoltaic-cells-2017-09-01)
- **Multistage IC-TPV at about 0.2 eV.** Huang, Li, Massengale, R. Q. Yang, Mishima & Santos, 46th IEEE PVSC 2019 (title-level). — [OU QDL page](https://sites.create.ou.edu/qdlou/2023/05/23/multistage-interband-cascade-thermophotovoltaic-devices-with-0-2-ev-bandgap)
- **Related OU theses and SPIE work (title-level).** OU dissertation "Interband Cascade Structures for Infrared Photodetectors and Thermophotovoltaic Devices." — [SHAREOK](https://shareok.org/items/d782101e-f4db-49a6-8330-aecb24084ea2/full). SPIE 11275 "Efficiencies and limiting factors of narrow-bandgap thermophotovoltaic cells." — [SPIE](https://biomedicaloptics.spiedigitallibrary.org/conference-proceedings-of-spie/11275/1127511/Efficiencies-and-limiting-factors-of-narrow-bandgap-thermophotovoltaic-cells-Conference/10.1117/12.2542920.full). Patent US11569403B2, resonant-cavity-enhanced IC PV device. — [Google Patents](https://patents.google.com/patent/US11569403)
- **Very-low-bandgap InAs/InAsSb T2SL TPV (Vaillon et al., CNRS/Montpellier; Solar Energy Mater. Sol. Cells, reported Aug 2026).** Eg = 0.23 eV at 200 K, with a 200 nm AlAsSb barrier versus a PIN reference. The barrier cells perform more than 10× better than PIN above 150 K. At 123 K they gave Voc about 23 mV and FF about 0.2. A passivated micro-cell gave Voc about 75 mV at 273 K under an 800 °C emitter at 14 cm. Efficiency was not reported. Dark current is the main limit; sulfur passivation and a larger bandgap are proposed. — [pv magazine, 24 Aug 2026](http://www.pv-magazine.com/2026/08/24/very-low-bandgap-thermophotovoltaics-for-operation-at-higher-temperatures/)
- **Ideal-limit context for thin InAs.** Papadakis, Orenstein, Yablonovitch & Fan (2021) show analytically that near-field operation naturally enhances radiative recombination. Photon recycling allows much thinner cells, which cuts volumetric non-radiative (Auger/SRH) loss, so Voc rises as the gap shrinks. A thin-film InAs near-field TPV example exceeds 50% at a 1100 K emitter. — [arXiv 2107.10705](https://arxiv.org/abs/2107.10705)
- **Low-bandgap need.** The z-TPV paper explicitly calls for cells below 0.7 eV for 700–1100 °C sources. — [RSC EES](https://pubs.rsc.org/en/content/articlehtml/2025/ee/d4ee04604h)

### Inferences
- **QW opportunity logic.** Papadakis et al. show that thin absorbers win when photon recycling is strong. Air-bridge cells give R_oob ≈ 99%. QWs are the extreme thin-absorber limit and offer tunable band edges (0.5–0.75 eV with strain-balanced InGaAs/InGaAsP or InGaAsSb), a step-like 2D DOS with excitonic band-edge absorption, and reduced Auger volume. A QW-aware detailed-balance and Auger analysis inside an air-bridge or back-reflector cavity is therefore physically well-motivated. In my searches I found no such 2018–2026 paper (not proven absent).
- **Interband cascade cells.** These convert many-stage voltage addition into a low-current, high-voltage cell, which reduces I²R losses at high W/cm². That links directly to the series-resistance limit in Q1. Near-field IC-TPV and IC thermoradiative modeling did not appear in my searches.
- The researcher's toolkit (Schrödinger–Poisson with nonparabolicity, absorption, multilayer optics) can compute QW absorption spectra and the radiative limit. Auger in QWs needs additional k·p and overlap-integral machinery. Vurgaftman/Lumb/Meyer (Bands and Photons, 2021) is a direct reference for this.

### Gaps
- I could not verify any 2018–2026 experimental MQW InGaAs/InGaAsP TPV cell paper. The search returned only 1990s–2000s items.
- Verified efficiency values for the 0.2 eV multistage IC-TPV were not found.
- Whether Rui Q. Yang's group has recent (2022–2026) IC-TPV papers under 1000+ K emitters was not established here.

---

## Q3. Near-field TPV, thermophotonics/electroluminescent cooling, thermoradiative and negative luminescence, PETE

### Takeaway
Measured near-field TPV efficiency is still below about 15%. The best reported value is about 14% (Lucchesi et al., Nano Lett. 2021, InSb). Power-density enhancements over far-field have been demonstrated (Fiorino 2018, Inoue 2019/2021, Bhatt 2020, Mittapally 2021). Recent emphasis is on scalability: NREL's 0.28 cm² self-supported pair at a 150 nm gap, and the CU Boulder/NREL zero-vacuum-gap concept. Thermophotonics (LED + PV) is theoretically very attractive. At 600 K, GaAs could give about 63% efficiency and about 1500 kW/m² in the ideal limit. However, "functional TPX devices are yet to be demonstrated experimentally," and EQE must exceed about 90–95%. Negative-electroluminescence cooling (about 6 W/m² at 55 nm) and thermoradiative power (2.26 mW/m²) have been demonstrated at tiny power levels. Coupled fluctuational electrodynamics (FE) + drift-diffusion modeling now exists (Callahan/Tervo/Zhang, PRApplied 2021).

### Cited Findings
- **Near-field TPV efficiency is below 15%.** Experiments cited are Bhatt 2020, Inoue 2021, Lucchesi 2021 and Mittapally 2021. — [Jeyar et al. arXiv 2412.04258](https://arxiv.org/html/2412.04258v1). Lucchesi et al. title: "Near-field thermophotovoltaic conversion with high electrical power density and efficiency above 14%." — [HAL hal-03649749 (title only, page blocked)](https://hal.archives-ouvertes.fr/hal-03649749); also "Efficient near-field thermophotovoltaic conversion with InSb cells." — [HAL](https://hal.archives-ouvertes.fr/hal-03438226)
- **Michigan near-field 2021 (Mittapally et al., Nat. Commun. 2021).** About 5 kW/m² and 6.8% efficiency at a 1270 K emitter with sub-100 nm gaps. — [patsnap aggregator, low confidence](https://www.patsnap.com/resources/blog/articles/thermophotovoltaic-tech-hits-40-efficiency-in-2026/); paper: [Nat. Commun. (Springer)](https://link.springer.com/article/10.1038/s41467-021-24587-7). The primary PMC page was blocked, so the numbers are not verified from the primary source.
- **Prior near-field experiments listed (titles).** Fiorino 2018 Nat. Nanotechnol. "Nanogap near-field thermophotovoltaics"; Inoue 2019 Nano Lett. one-chip near-field TPV; Bhatt 2020 Nat. Commun. integrated near-field TPV; Inoue 2021 ACS Photonics "overcoming blackbody limit"; Song 2022 ACS Photonics far-to-near-field transition (KAIST, 250–2600 nm gaps, oscillatory photocurrent). — [RSC EES reference list](https://pubs.rsc.org/en/content/articlehtml/2025/ee/d4ee04604h); [patsnap](https://www.patsnap.com/resources/blog/articles/thermophotovoltaic-tech-hits-40-efficiency-in-2026/)
- **Large-area near-field TPV (Selvidge, France, …, Steiner, Tervo; NREL, arXiv Aug 2024).** 0.28 cm² self-supported emitter-cell pair at a 150 nm gap, giving 1.22 mW at 460 °C, about 25× far-field. — [arXiv 2408.01295](https://arxiv.org/abs/2408.01295)
- **Coupled FE + Poisson–drift-diffusion (Callahan, Feng, Z. M. Zhang, Toberer, Ferguson, Tervo; Phys. Rev. Applied 15, 054035, 2021).** An iterative coupling is needed to capture photon recycling and near-field-enhanced luminescence, applied to GaSb TPV and thermoradiative cells. — [arXiv 2101.04746](https://arxiv.org/abs/2101.04746v1). A related paper is "Spatial profiles of photon chemical potential in near-field TPV cells" (Feng/Zhang/Tervo, NREL). — [arXiv 2103.14740](https://www.arxiv.org/abs/2103.14740)
- **Thermophotonics requirements (Sadi, Radevici, Behaghel, Oksanen; SEMSC 239, 111635).**
  - Experimental status: "functional TPX devices are yet to be demonstrated experimentally."
  - Competitiveness thresholds: TPX beats the best TPV at 300–500 K once QE ≳ 90%. GaAs efficiency falls from 63% to 18% as EQE drops from 100% to 95%.
  - Loss and resistance budgets: extraction losses below about 4% (500 K) or 7% (600 K); specific resistance below about 10⁻⁴ Ω·cm².
  - Ideal-limit output: GaAs at 600 K gives about 63% and 1500 kW/m²; InGaAs about 60% and 900 kW/m².
  - Coverage: QW active regions are not discussed.
  — [Aalto PDF](https://acris.aalto.fi/ws/portalfiles/portal/80226279/Prospects_and_requirements_for_thermophotonic_waste_heat_energy_harvesting.pdf)
- **TPX-Power EU project (Aalto-coordinated, 2021–Jun 2025, €3.42M).**
  - Theory and limits: Legendre & Chapuis, "Operating conditions and thermodynamic bounds of dual radiative heat engines," PRApplied 23, 034023 (2025), and GaAs near-field TPX with 1D PN junctions (SEMSC 2025).
  - Optics and LED materials: AlGaAs PIN to overcome non-radiative losses (APL 2023); Kivisaari & Oksanen on resonance effects in intracavity devices (APL 2023); extended-perimeter LEDs for electroluminescent cooling (ACS AEM 2024); GaAs/GaInP LED doping engineering (APL 2024).
  — [CORDIS 951976](https://cordis.europa.eu/project/id/951976/results/es)
- **Negative-electroluminescence photonic cooling (Zhu, Reddy et al., Univ. Michigan, Nature 2019; theory from Stanford/Fan).** About 6 W/m² cooling at a 55 nm gap using a reverse-biased LED. The theoretical limit cited is about 1000 W/m². — [Physics World](https://physicsworld.com/a/new-cooling-mechanism-uses-normal-light-instead-of-lasers/)
- **Thermoradiative diode (Nielsen, …, Ekins-Daukes, UNSW; ACS Photonics 2022).** HgCdTe photodiodes gave 2.26 mW/m² peak at ΔT = 12.5 °C (emission about 4.7 µm), with an estimated radiative efficiency of 1.8%. — [Compound Semiconductor](https://compoundsemiconductor.net/article/114842/Australian_team_generates_electricity_from_HgCdTe_photodiodes); [ACS figshare](https://acs.figshare.com/articles/journal_contribution/Thermoradiative_Power_Conversion_from_HgCdtTe_Photodiodes_and_Their_Current_Voltage_Characteristics/19736247)
- **Hot-electron thermophotonic solar cell via thermal upconversion (Nat. Commun. 2015; anchor).** — [PMC4659835 (title-level)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4659835/)
- **Photon-enhanced thermionic emission (PETE).** Literature found was mostly pre-2018: Schwede et al. 2010 and Tel Aviv University (Kribus) PETE converters. No 2022–2026 PETE record was verified. — [TAU PETE page](https://energy.tau.ac.il/node/1856); [Nat. Commun. 2013 (title-level)](https://www.nature.com/articles/ncomms2577)

### Inferences
- **Thermophotonics is the most "theory-ahead-of-experiment" thread.** The requirements paper explicitly omits QW active regions. A QW versus double-heterostructure active-region study for TPX LEDs is open and suits the toolkit. It would weigh radiative rate enhancement against Auger (which scales roughly with n³ in thin QWs) and against reduced SRH volume and photon recycling, and would include the near-field coupling of QW emission (in-plane dipoles, TE/TM) into the PV cell.
- **The near-field "thin cell" argument favours QW absorbers.** Papadakis 2021 + Callahan 2021 together imply that a quantum-corrected (Schrödinger–Poisson + capture/escape) version of coupled FE-DD for QW cells in near-field is the natural next step. It was not found in searches.
- **Negative luminescence and thermoradiative devices.** These are a natural fit for multistage IC structures, whose voltage adds per stage. IC-based thermoradiative or negative-luminescence cooling modeling was not found in searches.

### Gaps
- Primary verification of Lucchesi (efficiency above 14%, power density) and Mittapally numbers failed because PMC and HAL were blocked.
- No source found for Harder's thermophotonics (title-level only) or a Xiao/Lipson TPV result. These names were in the brief but not verified.
- No 2023–2026 experimental net-positive thermophotonic power demonstration was found. Aalto's 2025 paper says none existed at that time.

---

## Q4. Spectral control: selective emitters, ISB-QW tunable/switchable emitters (Noda, GaN/AlGaN), ENZ, metasurfaces, inverse design

### Takeaway
The QW/ISB anchor is Noda's group (Kyoto). In Nature Materials 2014, carrier depletion modulated intersubband absorption in n-type MQWs inside a photonic-crystal slab, switching resonant emissivity from 0.74 to 0.24 about 10⁴× faster than thermal modulation. Follow-ups covered narrowband QW+PhC mid-IR emitters, including GaN/AlGaN variants (title-level in searches). Inverse design and ML for TPV emitters is crowded: Georgia Tech W gratings, PearSAN, and many others. A theory paper on the ultimate temperature limits of ISB-based selective emitters is plausible and unclaimed in what I found. It would cover subband thermal population, depolarization and plasma shift, LO-phonon-limited linewidth, and nonparabolicity at emitter temperatures of 500–1000 K.

### Cited Findings
- **Inoue, De Zoysa, Asano & Noda, "Realization of dynamic thermal emission control," Nature Materials 13, 928–931 (2014).** Emissivity is controlled by extracting carriers from n-type QWs, with ISB absorption enhanced by a PhC slab resonance. Resonant emissivity changes from 0.74 to 0.24, about four orders of magnitude faster than conventional temperature modulation (10–100 Hz). — [Nature Materials](https://www.nature.com/articles/nmat4043)
- **Related QW+PhC work (title-level).**
  - "Single-peak narrow-bandwidth mid-infrared thermal emitters based on quantum wells and photonic crystals." — [OUCI](https://ouci.dntb.gov.ua/works/27PajwY4)
  - IEICE Trans. Electron. E101-C (2018) QW thermal-emitter paper by the Noda/Asano group. — [IEICE](https://global.ieice.org/en_transactions/electronics/10.1587/transele.E101.C.545/_pdf)
  - JSPS Kiban grant on QW/PhC emitters. — [JSPS](https://www.jsps.go.jp/j-grantsinaid/12_kiban/ichiran_25/e-data/h25_e3107_noda.pdf)
  - KAKEN project 17K14665. — [KAKEN](https://kaken.nii.ac.jp/grant/KAKENHI-PROJECT-17K14665)
- **"Electrical modulation of emissivity" (IOGS, HAL; title-level).** — [HAL](https://hal-iogs.archives-ouvertes.fr/hal-00821552)
- **Reviews.** Vázquez-Lozano & Liberal, "A Review on the Scientific and Technological Breakthroughs in Thermal Emission Engineering" (arXiv Jan 2024). It covers nanophotonic and time-modulated platforms; the abstract does not mention ISB. — [arXiv 2401.10001](https://arxiv.org/abs/2401.10001). Chapuis, Lee & Rodriguez, "Thermal radiation at the nanoscale and applications," APL 123 (2023). — [CORDIS list](https://cordis.europa.eu/project/id/951976/results/es)
- **Time-modulated thermal emission for photonic refrigeration (Buddhiraju, Li, Fan; arXiv 2019).** — [arXiv 1905.12196](https://arxiv.org/pdf/1905.12196)
- **Inverse design is crowded.**
  - Georgia Tech: "Inverse Design and Optimization Methods for TPV Emitters made of Tungsten Gratings." — [GT repository](https://repository.gatech.edu/entities/publication/0b3902c2-0c66-4495-87a9-0b59460e8702)
  - PearSAN ML inverse design (arXiv 2412.19284). — [arXiv](https://arxiv.org/pdf/2412.19284)
  - Materials screening for thermochemically stable thin-film emitters (arXiv 2410.19829). — [arXiv](https://arxiv.org/pdf/2410.19829)
- **Emitter spectral engineering is the stated next lever in Ge TPV** (simulated AlN/W reaches 22.3%). — [arXiv 2602.08761](https://papers.cool/arxiv/2602.08761)

### Inferences
- ISB emitters operate in the mid-IR (about 3–15 µm, i.e. about 0.08–0.4 eV). They pair naturally with **low-temperature TPV and very-low-bandgap cells** (IC-TPV, InAs/InAsSb T2SL; Q2) and with thermoradiative and negative-luminescence devices. They do not suit the 1–1.4 eV high-temperature regime.
- **A temperature-limits paper is a candidate.** The idea: "How narrow and how switchable can an ISB/QW emitter stay at 500–1000 K?" It would combine the toolkit's density-matrix optical response with the depolarization shift, LO-phonon-limited dephasing, thermal population of excited subbands, and nonparabolicity, then embed the result in PhC or planar-cavity optics through the TM-mode solver. It needs no experiment, and I found no direct prior art in searches.
- Generic inverse design of W/metal emitters is a saturated, low-novelty entry point for a solo theorist unless it is tied to a new physics constraint, such as QW/ISB active layers or co-optimization with a QW cell.

### Gaps
- No 2019–2026 Noda-group dynamic-emission follow-up with numbers (speed, high-temperature operation) was verified.
- No GaN/AlGaN ISB thermal emitter paper was verified beyond search titles. ENZ and metasurface TPV emitters were not specifically sourced here.

---

## Q5. Up/down-conversion, hot-carrier, intermediate-band, multijunction, space (radioisotope) and grid-storage TPV

### Takeaway
Hot-carrier TPV has a recent detailed-balance treatment: Nimje, Giteau & Papadakis (ICFO, arXiv Nov 2023) claim near-Carnot efficiency near maximum power. Realistic carrier-cooling physics (LO-phonon emission, hot-phonon bottleneck in QWs) has not been layered on in what I found, and that suits the toolkit's LO-phonon scattering module. Multijunction TPV is proven (41.1% tandem; NREL 2J GaInPAs/GaInAs). Grid storage is the commercial driver (Antora, Fourth Power; Datas latent-heat TPV batteries). NASA's radioisotope program remains thermoelectric-based (Next-Gen RTG SiGe, Mod 1 by 2030), so space RTPV is not a NASA program priority in the source found.

### Cited Findings
- **Hot-carrier TPV (Nimje, Giteau, Papadakis; arXiv 2311.04795, 2023).** A detailed-balance analysis shows hot carriers relax the monochromatic-efficiency versus broadband-power trade-off, giving near-Carnot efficiency near maximum power, and supplies analytic design rules. No device realization is proposed. — [arXiv 2311.04795](https://arxiv.org/abs/2311.04795). Earlier work: "Hot carrier based near field thermophotovoltaic energy conversion" (Penn State, title-level). — [PSU](https://pure.psu.edu/en/publications/hot-carrier-based-near-field-thermophotovoltaic-energy-conversion/)
- **Multijunction TPV.** The 41.1% 1.4/1.2 eV tandem result. — [arXiv 2108.09613](https://arxiv.org/abs/2108.09613). NREL's two-junction 0.84/0.74 eV early results. — [arXiv 2207.00565](https://arxiv.org/abs/2207.00565)
- **Space radioisotope power.** NASA RPS status (IEEE 2025 draft) describes the Next Generation RTG using heritage SiGe thermoelectric unicouples, Mod 1 planned for 2030, with commercial interest in non-Pu-238 isotopes. TPV is not mentioned. — [NASA NTRS](https://ntrs.nasa.gov/api/citations/20240012942/downloads/FINAL_RPS_IEEE_Paper_2025_draft_v6_clean.pdf). Older RTPV work exists (title-level): "Emissivity Tuned Emitter for RTPV Power Sources" — [OSTI](https://www.osti.gov/biblio/1047203); General Atomics RTPV — [ORNL](https://impact.ornl.gov/en/publications/general-atomics-radioisotope-fueled-thermophotovoltaic-power-syst/). Thermoradiative cells are also proposed for space waste heat (title-level). — [1-ACT PDF](https://www.1-act.com/wp-content/uploads/2023/05/Thermo-Radiative-Cell-A-New-Waste-Heat-Recovery-Technology-for-Space-Power-Applications.pdf)
- **Grid storage.**
  - Fourth Power: 25 MW / 250 MWh at 1900–2400 °C, with a 1 MWh pilot in 2026. — [MIT News](https://news.mit.edu/2026/turning-extreme-heat-large-scale-energy-storage-0318)
  - Antora: 2 MW/yr cell line, more than 40% cells. — [Antora](https://antoraenergy.com/tpv)
  - Latent-heat TPV batteries (Datas, UPM). — [UPM OA](https://oa.upm.es/86766/)
  - TPV techno-economics talk (title-level). — [AIChE 2024](https://proceedings.aiche.org/conferences/aiche-annual-meeting/2024/proceeding/paper/431e-evaluation-thermophotovoltaics-decarbonization-and-clean-energy-storage-technology-techno)
  - Waste-heat TPV review (title-level). — [Erdogan Univ.](https://avesis.erdogan.edu.tr/yayin/75d23ee4-0bbe-4c86-b4e6-1aaf4597d932/development-of-thermophotovoltaic-technology-in-waste-heat-recovery-a-review-of-the-last-five-years)

### Inferences
- **Hot-carrier TPV with QW absorbers.** Hot-phonon bottleneck and reduced LO-phonon emission in QWs are the classic hot-carrier enablers. The toolkit's LO-phonon rate calculator could supply realistic cooling times in place of the idealized parameters of Nimje et al. This would be a theory-only extension of a 2023 analysis, and I did not find it done.
- **Intermediate-band and up-conversion TPV.** I found no 2018–2026 primary source in this pass. These threads appear thin and may be low-yield.

### Gaps
- No verified sources on upconversion or downconversion TPV, or on intermediate-band TPV (2018–2026).
- No verified techno-economic numbers (for example $/kWh, LCOS) for TPV storage from a primary paper.

---

## Q6. Which purely computational papers are publishable now, in which venues, and which are already done?

### Takeaway
"Done" theory areas:
- coupled FE + drift-diffusion (PRApplied 2021);
- analytic near-field light-management limits (Papadakis/Fan 2021);
- hot-carrier TPV detailed balance (2023);
- thermophotonic requirements and thermodynamic bounds (SEMSC 2025, PRApplied 2025);
- front-contact effects (2024);
- many inverse-design emitter papers.

The open, toolkit-matched opportunities centre on **quantum structures**, which recent theory has largely skipped:
- QW and IC absorbers in high-reflectance, thin-cell and near-field regimes;
- QW active regions for thermophotonic LEDs;
- the temperature limits of ISB emitters;
- realistic LO-phonon hot-carrier TPV;
- parasitic free-carrier absorption limits on out-of-band reflectance.

### Cited Findings (what is already done, with venue evidence)
- Coupled FE + Poisson–drift-diffusion for TPV and thermoradiative cells: **Phys. Rev. Applied** 15, 054035 (2021). — [arXiv 2101.04746](https://arxiv.org/abs/2101.04746v1)
- Analytic thermodynamics of near-field light management, thin InAs above 50% (Papadakis/Orenstein/Yablonovitch/Fan, 2021). — [arXiv 2107.10705](https://arxiv.org/abs/2107.10705)
- Hot-carrier TPV detailed balance (2023). — [arXiv 2311.04795](https://arxiv.org/abs/2311.04795)
- Thermophotonic requirements: **SEMSC** 239, 111635. Dual radiative heat-engine bounds: **PRApplied** 23, 034023 (2025). Near-field TPX with 1D PN junctions: **SEMSC** 2025. AlGaAs PIN for TPX: **APL** 2023. — [CORDIS](https://cordis.europa.eu/project/id/951976/results/es)
- Front-metal-grid effects in near-field TPV (arXiv 2024). — [arXiv 2412.04258](https://arxiv.org/html/2412.04258v1)
- Zero-gap TPV concept and modeling: **Energy Environ. Sci.** (2025). — [RSC](https://pubs.rsc.org/en/content/articlehtml/2025/ee/d4ee04604h)
- Experimental and record venues: **Nature** (LaPotin 2022); **Joule** (Tervo 2022, Roy-Layinde 2024); **Nat. Commun.** (Mittapally 2021); **ACS Photonics** (Nielsen 2022 thermoradiative); **IEEE J. Photovoltaics** (IC-TPV 2017); **SEMSC** (InAs/InAsSb T2SL TPV 2026). — sources as above.

### Candidate theory/computation papers (fit to the toolkit; experiment needed? prior art?)

1. **QW-limited TPV in the air-bridge / high-R_oob regime.**
   - Content: detailed balance + Auger + SRH for strain-balanced InGaAs/InGaAsP or InGaAsSb MQW absorbers (0.5–0.75 eV) under 1200–1500 °C spectra, with R_oob 95–99.5% and full photon recycling. Compare against bulk 0.74/0.9 eV cells. Include excitonic band-edge absorption, 2D DOS, TE/TM selection, and the number-of-wells trade-off.
   - Experiment: not needed.
   - Prior art: QW-TPV advantages were argued in the 1990s ([OSTI](https://www.osti.gov/biblio/577804)). No 2018–2026 re-analysis in the air-bridge regime was found (not proven absent).
   - Venues: PRApplied, JAP, IEEE JPV, SEMSC.
2. **Quantum-corrected coupled FE + transport for QW cells in near-field / thin-film TPV.**
   - Content: extend the Callahan 2021 framework with Schrödinger–Poisson subbands and capture/escape, testing whether QWs realize Papadakis' thin-cell Voc gain.
   - Experiment: not needed.
   - Prior art: the bulk version is done (PRApplied 2021). No QW version was found.
   - Venues: PRApplied, ACS Photonics, JAP.
3. **Interband-cascade TPV, near-field IC-TPV, and IC thermoradiative / negative-luminescence devices.**
   - Content: per-stage current matching, photon recycling, and Auger; voltage-adding to beat series resistance at W/cm² levels.
   - Experiment: not needed for a modeling paper. OU devices exist ([OSTI 1497660](https://www.osti.gov/biblio/1497660)), so a later Yang-group collaboration is natural.
   - Prior art: IC-TPV experiments and efficiency-limit SPIE papers exist. Near-field IC and IC thermoradiative modeling was not found.
   - Venues: PRApplied, JAP, IEEE JPV, IEEE JQE.
4. **QW versus DH active regions for thermophotonic LEDs and electroluminescent cooling.**
   - Content: Auger-limited EQE, near-field coupling of QW emission, and the 90–95% EQE threshold.
   - Experiment: not needed.
   - Prior art: Sadi et al. 2025 do not treat QWs ([Aalto](https://acris.aalto.fi/ws/portalfiles/portal/80226279/Prospects_and_requirements_for_thermophotonic_waste_heat_energy_harvesting.pdf)). The Aalto "parametric study of highly-efficient LEDs for thermophotonic cooling" ([URN](https://urn.fi/URN:NBN:fi-fe2020060240148), title-level) should be checked before claiming novelty.
   - Venues: PRApplied, JAP, SEMSC, APL.
5. **Temperature limits of ISB/QW selective and electrically switchable thermal emitters for low-temperature TPV and TPX.**
   - Content: density matrix + depolarization + LO-phonon dephasing + thermal subband population + PhC/planar-cavity TM optics.
   - Experiment: not needed.
   - Prior art: Noda's experiments ([Nat. Mater. 2014](https://www.nature.com/articles/nmat4043)). No theory of the high-temperature limit was found.
   - Venues: ACS Photonics, PRApplied, Opt. Express, JAP.
6. **Hot-carrier TPV with realistic QW LO-phonon cooling and hot-phonon bottleneck.**
   - Content: extend Nimje et al. 2023 with computed LO-phonon rates.
   - Experiment: not needed.
   - Prior art: the idealized version is done; the realistic QW version was not found.
   - Venues: PRApplied, JAP, Joule (if a system-level result).
7. **Out-of-band reflectance limits from free-carrier / intervalence absorption in doped contact layers and substrates.**
   - Content: multilayer optics + Drude/IVBA models; "what limits R_oob above 99%?"
   - Experiment: not needed, though data comparison is useful.
   - Prior art: partly done in Ge TPV modeling ([arXiv 2602.08761](https://papers.cool/arxiv/2602.08761)) and in group-internal analyses. A general design-rule paper was not found.
   - Venues: SEMSC, JAP, IEEE JPV.
8. **Zero-gap / high-index-spacer TPV with QW or low-bandgap cells.**
   - Content: conduction versus radiation trade-off with optimized spacers.
   - Experiment: not needed.
   - Prior art: the concept and a-Si modeling are done ([EES 2025](https://pubs.rsc.org/en/content/articlehtml/2025/ee/d4ee04604h)). The QW-cell variant is open.
   - Venues: IJHMT, JQSRT, PRApplied.
9. **Tutorial or review: "Quantum structures in thermal-photonic energy conversion."**
   - Content: QW-TPV, IC-TPV, ISB emitters, QW-LED thermophotonics, thermoradiative devices.
   - Experiment: not needed.
   - Prior art: general reviews exist (thermal emission engineering 2024, nanoscale radiation APL 2023, TPV application reviews). No QW-focused review was found.
   - Venues: J. Appl. Phys. (Tutorial), J. Photonics Energy, Prog. Quantum Electron.
10. **Lower-novelty options.** Generic inverse design of metal/dielectric emitters (crowded: [GT](https://repository.gatech.edu/entities/publication/0b3902c2-0c66-4495-87a9-0b59460e8702), [PearSAN](https://arxiv.org/pdf/2412.19284)). Generic system storage models (Antora, Fourth Power, Datas, AIChE 2024 already active).

### Inferences
- The strongest solo-theory niche is the intersection the field has skipped: **quantum-structure physics × modern TPV and thermophotonics regimes**. The regimes are high R_oob, thin absorbers, near-field, and EQE above 95% LEDs. This uses the researcher's toolkit (SP + nonparabolicity, depolarization, LO phonons, density-matrix optics, multilayer TM solver) almost one-to-one.
- Candidates 1, 3 and 5 also create a natural later bridge to OU experiments through R. Q. Yang's IC-TPV devices.
- **Venue fit:**
  - PRApplied is the established home for coupled-transport and thermodynamic-bound TPV theory (2021 and 2025 examples).
  - SEMSC is the home for TPX requirement and device-modeling papers.
  - Joule is effectively reserved for records or system-level impact.
  - J. Photonics Energy and JAP are reasonable for tutorial-style QW papers.

### Gaps
- Novelty checks were search-level only. Before writing, run targeted Google Scholar and arXiv checks for: "quantum well" + "air-bridge" TPV; "near-field" + "interband cascade"; "intersubband" + "thermophotovoltaic"; "quantum well" + "thermophotonic"; "hot carrier TPV" + "LO phonon."
- Venue scope statements (for example J. Photonics Energy or IJHMT acceptance of pure device-physics TPV theory) were not verified from journal pages.
- Not verified in this session: Burger et al. Joule 2020 review numbers, the Fan et al. Nature 2020 air-bridge 32% paper, the Harder thermophotonics work, and the Lipson/Xiao results.
