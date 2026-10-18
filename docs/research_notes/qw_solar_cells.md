# Quantum-well and related quantum-structure solar cells (2018 to Oct 2026): open threads and theory/computation opportunities for a solo researcher

Scope note: about 45 search/fetch calls. Items marked **[title-level]** were seen only as a search-result title or abstract stub; I did not read the full text. "Not found" means my searches did not turn it up. It does not mean the work has never been done. A full literature check (Scopus/Web of Science, plus forward citations of the anchor papers) is needed before any submission.

---

## Q1. Strain-balanced MQW cells in III–V and multijunction cells (records, escape vs recombination, radiative limits and photon recycling, thin cells and light trapping, radiation hardness)

### Takeaway
Strain-balanced GaInAs/GaAsP superlattices ("thick QW" stacks of 80–300 periods) hold the one-sun records for 2J (32.9%) and 3J (39.5%) cells and give 34.2% AM0 (NREL, France/Steiner/Geisz). The experimental groups say themselves that carrier extraction and recombination in these stacks are not captured by standard drift-diffusion. Several effects remain unexplained: Voc loss with stack thickness, ERE and photon recycling in thick stacks, and the radiation-induced Voc/FF collapse in space cells. These are modeling gaps that a Schrödinger–Poisson plus escape-rate plus optics toolkit can address directly.

### Cited Findings
**Records and device numbers**
- NREL 3J inverted metamorphic cell GaInP / GaAs-with-QWs / GaInAs: **39.5% at one sun (AM1.5G)**, **34.2% AM0**, with "up to 300 quantum wells" in the middle cell. Published in *Joule*, May 2022. — [StatNano/NREL news](https://statnano.com/world-news/92761/Quantum-well-solar-cell-clocks-world-record-efficiency-of-almost-40-); [pv-magazine 2022](https://pv-magazine.com/2022/05/19/quantum-well-superlattices-for-a-new-world-record-cell-efficiency-of-39-5); [NREL research hub record](https://research-hub.nrel.gov/en/publications/triple-junction-solar-cells-with-395-terrestrial-and-342-space-ef-4/) [title-level for the Joule paper]
- NREL MRS 2022 abstract: the target band edge is about 930 nm, reached with strained Ga0.9In0.1As kept about 10 nm thick to avoid relaxation. Superlattices have up to 300 strain-balanced GaInAs/GaAsP pairs. Results: **32.9% 2J** and **39.5% 3J** at one sun. — [NREL research hub, NREL/PR-5900-81351](https://research-hub.nrel.gov/en/publications/record-efficiency-multijunction-solar-cells-with-strain-balanced-/)
- Steiner, France, Buencuerpo, Geisz, Nielsen, **Pusch**, Olavarria, Young, **Ekins-Daukes** (48th IEEE PVSC 2021), with UNSW–NREL co-authorship:
  - Wells are Ga0.894In0.106As, 85 Å, with GaAs0.902P0.098 barriers (85 Å on each side). Up to 80 wells. Net average stress ≤12 MPa, while individual layers carry coherent stress 35–70× larger.
  - QW band edge 1.351 eV vs 1.414 eV for GaAs.
  - GaAs-QW single junction **27.2 ± 0.2%** certified, Voc 1.040 V, Jsc up to 31.5 mA/cm².
  - GaInP/GaAs-QW tandem **32.9 ± 0.5%**, average Woc 0.36 V.
  - The paper says radiative and nonradiative rates "remain in the same ratio as in the baseline cell", but reports no ERE.
  - Gold back reflector. Photon recycling is not analyzed.
  - — [NREL/CP-5900-80198](https://nrel.gov/docs/fy21osti/80198.pdf)
- France, Selvidge, Mukherjee, Steiner, *J. Appl. Phys.* 132, 184502 (2022):
  - **Baseline:** 80×(85 Å GaInAs / 170 Å GaAsP), with thermionic-emission-dominated transport.
  - **Barrier-thinning series** (i-region fixed at 2 µm): from 170 Å GaAs0.9P0.1 down to **20 Å GaP**. The GaInAs fraction rises from 32% to 80%.
  - **Tunneling vs thermionic emission:** the two carrier lifetimes are "equivalent at about 5 nm" barrier thickness.
  - **Thick stacks:** up to 300 repeats and about 4.5 µm i-region.
  - **Best single junction:** Voc 1.035 V, FF 83.5%, Woc 0.31 V.
  - **2J:** 184 GaInAs/GaP repeats (modeled gap 1.34 eV). **29.2 ± 0.4% AM0** (1000 W/m², 28 °C) and 32.9% AM1.5G. Voc 2.486 V, FF 84.7%.
  - **Unexplained Voc loss:** going from 850 to 2550 nm of GaInAs lowered the gap by 15 meV but Voc by 25 mV. The extra ~10 mV loss is "not identified".
  - **Collection:** "depends on the nonradiative lifetime in the quantum wells".
  - **Open question:** whether GaP-barrier stacks can be optically thick without a rear reflector is "not known".
  - **Not reported:** ERE and per-well absorption.
  - — [NREL/JA 83983 (JAP 2022)](https://nrel.gov/docs/fy23osti/83983.pdf)
- Ahmed, Sudhakaran, Almutairi, Khan, Whiteside, Petrou, **France**, **Sellers**, *J. Appl. Phys.* 138, 013103 (2025). They studied temperature- and suns-dependent PL and PV in record-type GaInAs/GaAsP MQW cells, separating thermal escape from tunneling and radiative from nonradiative recombination, and fitted a multi-mechanism two-diode model. They conclude the field must "move beyond simple drift-diffusion models of p-n junctions". — [NREL research hub](https://research-hub.nrel.gov/en/publications/charge-carrier-extraction-and-recombination-effects-in-gainasgaas/); [NSF PAR](https://par.nsf.gov/biblio/10612552) [abstract-level; no numbers seen]
- RIT / Hubbard group (Space Power Workshop 2023):
  - **Design:** 25-period In0.10Ga0.90As/GaAs0.9P0.1 (about 29 nm period, 340 ppm strain).
  - **50×QW + 14× DBR single junction:** Jsc +2.0 mA/cm², Voc −15 mV, η +0.9% abs. The DBR raises per-well current from about 26 to 40 µA/cm².
  - **Dual junction AM0:** 23.9% → 27.5%.
  - **Radiation, 1 MeV e⁻ at 1×10¹⁵ cm⁻²:**
    - QW single junction: Jsc retains 92% (vs 81% for control), but Voc drops from 0.996 to 0.760 V. EOL efficiency retention is only 60%, vs 72% for control.
    - 2J remaining factors, control vs QW: Jsc 0.85 vs 0.93, Voc 0.92 vs 0.86, FF 0.98 vs 0.91, η 0.77 vs 0.73.
  - **Stated open issues:** EOL Voc loss from carrier removal and higher J02, QW placement, and strain on offcut substrates.
  - **Modeling claim:** QW cells run about 15 °C cooler with sub-gap rejection (projected).
  - — [Hubbard SPW 2023 slides](https://spw.aerospace.org/files/2023/06/2023-04_5_EG1_S.-Hubbard_Presentation.pdf)
- EU RadHard project (Fraunhofer ISE, AZUR, Thales, Airbus, CEA; 2018–2021): a 4J radiation-hard space cell. The visible page does not mention QWs. — [Fraunhofer ISE RadHard](https://www.ise.fraunhofer.de/en/research-projects/radhard.html)
- Current efficiency tables:
  - **Version 67** (Green, Dunlop, Yoshita, Kopidakis, Bothe, Siefer, Hao, Jiang) appeared in *Prog. Photovolt.* in 2026, DOI 10.1002/pip.70068. — [ISFH listing](https://isfh.de/en/publications/solar-cell-efficiency-tables-version-67)
  - pv-magazine (June 2026) describes **Version 68** as "published in *Joule*". Its listed records include perovskite/Si 35.2% (1 cm²) and a GaInP/GaInAs/Ge non-concentrator module at 34.4% (Fraunhofer ISE/AZUR/temicon). It names no QW-specific records. — [pv-magazine USA 2026-06-08](https://pv-magazine-usa.com/2026/06/08/all-solar-cell-efficiencies-at-a-glance-updated-7/)
  - **Possible conflict / venue change:** v67 is in Prog. Photovolt. while v68 is reported in Joule. I could not verify this from the primary source.

**Older modeling anchors (still the standard references)**
- Connolly, Ballard, **Barnham**, Bushnell, Tibbits, Roberts, "Efficiency limits of quantum well solar cells" (arXiv:1006.1835). Dark current at concentrator-relevant bias is radiative-dominated, so QWSCs "are inherently subject to the fundamental radiative efficiency limit". The model uses an analytic QE with confined DOS. — [arXiv:1006.1835](https://arxiv.org/abs/1006.1835)
- Also from the Connolly/Imperial lineage: "Simulating multiple quantum well solar cells" — [arXiv:1006.1851](https://arxiv.org/pdf/1006.1851) [title-level], and "Analytical models of bulk and quantum well solar cells and relevance of the radiative limit" — [arXiv:1110.1561](https://arxiv.org/pdf/1110.1561) [title-level]
- "Modelling of GaAsP/InGaAs/GaAs strain-balanced MQW solar cells" (UPV) — [RiuNet](https://riunet.upv.es/entities/publication/6bdd0efd-be6a-41ef-920a-6186222ac2db/full) [title-level]
- Tokyo (Sugiyama/Nakano) and Kobe (Kita/Asahi) line on carrier transport:
  - Toprasertpong et al. developed a carrier time-of-flight method (TRPL with a buried probe QW under forward bias). They found average drift velocity linear in field, so an MQW can be treated as a "quasi-bulk material with low effective mobility". DOI 10.1063/1.4927612 (APL 2015). — [arXiv:2006.00180](https://arxiv.org/abs/2006.00180)
  - Related: an "effective drift mobility approximation in MQW solar cell" (SPIE 9743) — [SPIE](https://neurophotonics.spiedigitallibrary.org/conference-proceedings-of-spie/9743/974315/Effective-drift-mobility-approximation-in-multiple-quantum-well-solar-cell/10.1117/12.2209611.full) [title-level]
  - "Carrier escape time and temperature-dependent carrier collection efficiency of tunneling-enhanced MQW solar cells" — [ResearchGate PDF](https://researchgate.net/profile/Kasidit-Toprasertpong/publication/257304028_Carrier_Escape_Time_and_Temperature-Dependent_Carrier_Collection_Efficiency_of_Tunneling-Enhanced_Multiple_Quantum_Well_Solar_Cells/links/56b6391908ae44bb33079865/Carrier-Escape-Time-and-Temperature-Dependent-Carrier-Collection-Efficiency-of-Tunneling-Enhanced-Multiple-Quantum-Well-Solar-Cells.pdf) [title-level]
- A SPIE 11275 (2020) paper, "Trade-off study on the radiative efficiency and carrier transport…" in MQW cells, exists. — [SPIE](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/11275/112750Q/Trade-off-study-on-the-radiative-efficiency-and-carrier-transport/10.1117/12.2546279.full) [title-level; page blocked]
- QW waveguide solar cell patents exist, so light trapping via guided modes in QW stacks is prior art. — [USPTO 8921687](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8921687); [USPTO 10062793](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10062793) [title-level]

### Inferences
- **The core open modeling problem is a validated, physics-based device model for 80–300-period superlattices.** It would combine thermionic plus tunneling escape, QW capture, in-well SRH and radiative recombination, and photon recycling and reabsorption across the stack. It should reproduce:
  - the barrier-thickness crossover near 5 nm (France 2022),
  - the unexplained ~10 mV extra Voc loss in thick stacks,
  - the temperature and suns dependence in Ahmed 2025.

  The researcher's toolkit (SP with nonparabolicity for confined levels and wavefunction overlap, LO-phonon rates for capture and escape) covers the microscopic inputs. What is missing is a minibands-vs-hopping transport layer. As GaP barriers approach 2 nm, the stack becomes a superlattice with minibands, and the right transport picture (sequential tunneling vs miniband vs effective-mobility "quasi-bulk") is unsettled in the published work I found.
- **The radiation result is a clean theory target.** QW cells keep current but lose more Voc and FF at EOL. This suggests carrier removal shifts the field profile in the thick i-region, plus J02 growth. A Poisson-coupled model with fluence-dependent background doping and lifetime could test whether moving the QWs or adding back-surface field and doping profiles recovers EOL efficiency. RIT lists "compensation and QW placement" as open.
- **ERE and photon recycling in thick MQW stacks is unquantified in the NREL papers I read.** Neither reports ERE or per-well absorption. A detailed-balance/Rau-type analysis using measured EQE, combined with a TM/TE-resolved optical model (QW HH transitions are TE-dominated, so emission is anisotropic), is publishable and needs no new experiment if it uses published EQE/JV data.
- **Local fit.** The OU/Sellers/Santos/Mishima ecosystem works on exactly these devices. The OU MBE group (Mishima, Santos) co-authors the hot-carrier QW papers, and the Nature Energy 2020 work was done at OU. Sellers now appears under University at Buffalo listings and co-authors with NREL's France. These are natural later experimental partners. This is an inference from affiliations in listings, not a confirmed current arrangement.

### Gaps
- I could not confirm whether the 47.1% six-junction concentrator record (Geisz et al. 2020) uses QWs, so it is not claimed here.
- No 2024–2026 QW-specific record beyond 39.5% 3J / 32.9% 2J turned up. I did not determine whether efficiency tables v67/v68 list a QW cell explicitly.
- No published ERE value for record QW cells was found.
- No full text was read for the Joule 2022 paper or Ahmed 2025, so their fitted escape and recombination rates are unknown here.
- The status of thin-film (substrate-removed) QW cells with textured or nanophotonic back reflectors in 2022–2026 was not established.

---

## Q2. QW intermediate band, two-step photon upconversion (TPU), ratchets, hot-carrier QW absorbers, phonon-bottleneck engineering

### Takeaway
These concepts remain at proof-of-principle efficiencies: TPU at about 5% device efficiency, hot-carrier QW cells without above-SQ demonstration. The theory is fragmented. Detailed-balance limits exist for idealized IB, ratchet and TPU. Rate-equation thermalization models exist for generic QWs. What is missing is a kinetic model that links the real QW band structure (type-II overlap, intersubband selection rules, LO/acoustic phonon dispersion mismatch) to measurable device JV, Tc and Voc. The researcher's toolkit (LO-phonon rates, depolarization and density-matrix intersubband response, TM waveguide) matches these gaps unusually well.

### Cited Findings
**Hot-carrier QW absorbers (OU/Sellers/Santos/Mishima/Whiteside line, with Guillemoles/Suchet at IPVF)**
- **Esmaielpour et al., *Sci. Rep.* 8, 12473 (2018), type-II InAs/AlAsSb QW.**
  - Thermalization is limited by the radiative lifetime of poorly overlapping electrons, plus phonon reabsorption aided by InAs/AlAsSb phonon-dispersion mismatch.
  - This extends the thermalization time "from picoseconds to nanoseconds".
  - Steady-state hot-electron temperature reaches **490 K** at room temperature.
  - — [SUNY ResearchConnect](https://researchconnect.suny.edu/en/publications/enhanced-hot-electron-lifetimes-in-quantum-wells-with-inhibited-p/)
- **Esmaielpour, Durant, Dorman, Whiteside, Garg, Mishima, Santos, Sellers, Guillemoles, Suchet, *APL* (2021).** In InAs/AlAs0.16Sb0.84 superlattices, thicker AlAsSb barriers slow hot-carrier relaxation through a phonon bottleneck, so phonon management can be tuned by design. — [AIP Scilight](https://www.aip.org/scilights/photovoltaic-power-generation-can-be-improved-by-keeping-the-electrons-hot)
- **Esmaielpour, Dorman, Ferry, Mishima, Santos, Whiteside, Sellers, *Nature Energy* 5, 336 (2020): "valley photovoltaics".**
  - Hot carriers scattered into L valleys are collected in InGaAs/AlInAs heterostructures (Eg 0.75 eV) at voltages set by the upper valley (about 1.25 V ideal).
  - Efficiency does *not* exceed the single-gap limit. This is attributed to valley-degeneracy mismatch at the n⁺-AlInAs/n-InGaAs interface.
  - Work done at OU, with theory by Ferry (ASU).
  - — [Nature Energy](https://link.springer.com/article/10.1038/s41560-020-0602-0)
- **Piyathilaka, …, Sellers, Bristow (arXiv:2112.14502).** AC photoconductivity in InAs/AlAsSb MQWs shows a "metastable regime" with higher photoconductivity and slightly lower (Auger-limited) mobility. The ambipolar diffusion length is >0.5 µm at room temperature. — [arXiv:2112.14502](https://www.arxiv.org/abs/2112.14502)
- Related: SPIE 11681 "Hot carriers and phonon relaxation processes in InAs/AlAsSb QWs" — [SPIE](https://nanophotonics.spiedigitallibrary.org/conference-proceedings-of-spie/11681/116810P/Hot-carriers-and-phonon-relaxation-processes-in-InAs-AlAsSb-quantum/10.1117/12.2576948.full) [title-level]; OU thesis "Type-II quantum well hot carrier solar cells" — [SHAREOK](https://shareok.org/items/e431354e-2027-4039-a0ef-b2bc8ad90e8a) [title-level]; "Hot-carrier dynamics in InAs/AlAsSb MQWs" — [arXiv:2103.03839](https://ar5iv.labs.arxiv.org/html/2103.03839) [title-level]
- **Zhang, Conibeer, Liu, Zhang, Guillemoles, *Prog. Photovolt.* 30, 581 (2022)** (review of phonon-bottleneck mechanisms in III–V). Low-dimensional structures enhance the bottleneck: "Multiple quantum wells seem the most promising material system for hot carrier solar cells." — [IP Paris portal](https://researchportal.ip-paris.fr/en/publications/review-of-the-mechanisms-for-the-phonon-bottleneck-effect-in-iiiv/)
- **Makhfudz, Cavassilas, Giteau, Esmaielpour, Suchet, Daré, Michelini, *J. Phys. D* (2022), DOI 10.1088/1361-6463/ac94dd** (theory, steady-state electron–phonon rate equations).
  - Thermalization power density is lower in QWs than in bulk, which they call confinement-enhanced hot-carrier effect.
  - Intra-subband scattering dominates thin wells, and inter-subband scattering grows with thickness.
  - Including non-equilibrium LO phonons and screening makes the thickness dependence **non-monotonic**.
  - — [arXiv:2209.13218](https://arxiv.org/abs/2209.13218)
- **Hirst, …, Sugiyama, Ekins-Daukes (IEEE PVSC 2011)** (older anchor). Strain-balanced InGaAs/GaAsP QWs showed hot populations beyond 2 ns, and higher Tc in deep wells, attributed to confinement suppressing thermalization. — [IP Paris portal](https://researchportal.ip-paris.fr/en/publications/hot-carrier-dynamics-in-ingaasgaasp-quantum-well-solar-cells/)
- **Energy-selective contacts: Boyer-Richard, …, Suchet, Lombez, Durand, *EPJ Photovolt.* 15, 38 (2024).**
  - InGaAs absorber on InP with an InGaAs/AlInAs single-QW energy-selective contact (E1 ≈ 0.186 eV, 0.52 eV barrier).
  - The SQW device reached Voc 0.28 V under AM1.5G, with an S-shaped JV from tunneling.
  - The authors state hot-carrier operation was *not* demonstrated and the confined level must be redesigned.
  - — [EPJ PV 2024](https://www.epj-pv.org/articles/epjpv/full_html/2024/01/pv20240018/pv20240018.html)
- **Afshari, …, Sellers, Furis, *EES Solar* 1, 828 (2025)** (perovskite, but states the open issues). Tc reaches about 5000 K at high fluence and cooling is bias-dependent. The authors note "some debate in the community" on thermalization pathways and say the roles of acoustic phonons, polarons and hot-phonon reabsorption are unresolved. They also note that recent III–V QW studies show acoustic phonons improve modeling. — [EES Solar 2025](https://pubs.rsc.org/en/content/articlepdf/2025/el/d5el00063g)

**TPU / IB / ratchet**
- **Asahi et al., "Two-step photon up-conversion solar cells", *Nat. Commun.* 8, 14962 (2017)** (anchor; Kobe/Kita group). — [Nature Communications](https://link.springer.com/article/10.1038/ncomms14962); [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5384214/) [title-level here]
- **Watanabe, Asahi, Zhu, Kita, *JAP* 130, 085701 (2021).**
  - **Structure:** Al0.3Ga0.7As/GaAs hetero-interface TPU cell with an InAs QD layer to relax intraband selection rules.
  - **Doping series:** modulation-doped to set the interface field (11–32 kV/cm). At 16.6 kV/cm the IR-induced EQE boost was about 45%, while 32 kV/cm loses carriers to tunneling.
  - **Voltage:** ΔVoc exceeds the diode-equation prediction ("voltage boost").
  - **Device:** AM1.5G gives **5.1%** (Jsc 12 mA/cm², Voc 0.76 V).
  - **Cited limits:** about 46.8% detailed-balance for both TPU and ideal IB.
  - **Stated open issues:** optimal field, the tunneling/extraction balance, and behavior under broadband (not laser) excitation.
  - — [Kobe repository PDF](https://da.lib.kobe-u.ac.jp/da/kernel/90008540/90008540.pdf)
- **Sogabe, Hung, Tamaki, Tomić, Yamaguchi, Ekins-Daukes, Okada, *Commun. Phys.* 4 (2021)** (Okada, Tokyo). "Experimental demonstration of energy-transfer ratchet intermediate-band solar cell" (Er-doped GaAs). — [DOAJ](https://doaj.org/article/2d6ad72f1abc482fbc15df8ec7b388ad)
- **Zhang & Krich, *J. Appl. Phys.* (2020), DOI 10.1063/5.0005416.** The electronically coupled upconverter (ECUC) and the quantum ratchet solar cell have equal detailed-balance limits, and the ECUC is less sensitive to nonradiative recombination. — [arXiv:1909.07874](https://arxiv.org/abs/1909.07874)
- Imperial theses on QW-IB and photon-ratchet IB cells — [Spiral: QW IB solar cells](https://spiral.imperial.ac.uk/entities/publication/9d9ee2c9-7f21-44ea-9ce5-a704bd1b737f); [Spiral: photon ratchet IB](https://spiral.imperial.ac.uk/entities/publication/9cc7e5b3-f027-4e74-812a-648a5c639a16); "Lifetime enhancement for multi-photon absorption in IB solar cells" — [arXiv:1612.06666](https://ar5iv.labs.arxiv.org/html/1612.06666) [title-level]
- **IB absorption depends on IB filling** (Ramiro, …, Luque, Martí, *PRB* 96, 125422, 2017; GaSb/GaAs QDs). Photo-filling raises the E_L absorptivity by more than two orders of magnitude and lowers E_H by about one order. This filling dependence is what a self-consistent QW-IB model must include. — [APS accepted manuscript](https://link.aps.org/accepted/10.1103/PhysRevB.96.125422)

### Inferences
- **The highest-fit opportunity for this researcher is hot-carrier thermalization in type-II InAs/AlAsSb QWs.** The Makhfudz 2022 rate-equation model is generic (type-I, simple bands). The open, toolkit-ready extension:
  - SP with nonparabolicity (InAs is strongly nonparabolic) for the real type-II band alignment;
  - LO-phonon emission and absorption rates with confined/interface phonon modes, plus hot-phonon non-equilibrium;
  - the electron–hole overlap-limited radiative rate.

  The aim is a computed Tc vs absorbed power and a thermalization coefficient Q, compared directly with the published 490 K / ns-lifetime data (Sci. Rep. 2018) and the barrier-thickness trend (APL 2021). This needs no new experiment and explicitly addresses the debate flagged in Afshari 2025 and Zhang/Conibeer 2022.
- **TPU at a hetero-interface is essentially a field-dependent escape and intersubband problem.** The Kobe group explicitly lists the optimal interface field and the tunneling-vs-extraction tradeoff as open. An SP plus tunneling-escape plus density-matrix intersubband (TM-polarized) absorption model, fed into detailed balance, could map efficiency vs field and doping, and could show whether QWs (rather than QDs) can provide the intraband step given the TM selection rule. The waveguide TM-mode solver is directly relevant for coupling light into intersubband transitions in a thin TPU cell.
- **QW-based IB/ratchet modeling with real intersubband oscillator strengths, depolarization shift and IB filling is not found in my searches.** Most IB limits use idealized step absorptivities. A paper on "realistic QW intersubband absorptivity, including depolarization/plasma shift and filling, in IB/ratchet detailed balance" appears open, but needs a careful check against Imperial theses (Ito 2014) and Luque/Martí reviews.
- **Valley photovoltaics needs a theory paper** quantifying the valley-degeneracy-mismatch loss at heterointerfaces and designing interfaces to avoid it. The Nature Energy paper states the mismatch is not fundamental but did not demonstrate this.

### Gaps
- No 2023–2026 TPU-cell efficiency above 5.1% was found. Later Kobe work (JSAP 2024 abstracts) was seen only at title level ([JSAP 2024 abstract](https://pub.confit.atlas.jp/en/event/jsap2024s/presentation/24a-12J-2)).
- No measured thermalization coefficient Q values for InAs/AlAsSb were retrieved in full text.
- No demonstrated hot-carrier cell beating the single-junction limit was found. The EES Solar 2025 paper gives only the >60% theoretical promise.
- Whether a full NEGF or Boltzmann treatment of InAs/AlAsSb hot carriers (Ferry/ASU, Cavassilas/Marseille) already exists for the specific OU samples was not verified.

---

## Q3. QWs in III–V-on-Si and perovskite/III–V tandems; 2D Ruddlesden–Popper perovskite "quantum wells"; nanowire/QD vs QW

### Takeaway
The leading III–V/Si cells (Fraunhofer 36.1%) and perovskite tandems do not use QWs as far as I found. QW bandgap engineering is used in all-III–V multijunctions, and QWs for current matching in tandems is an old concept. 2D RP perovskites are physically multi-QW absorbers: about 20–21% efficiency in pure 2D RP vs about 35% for perovskite/Si. Their open questions (exciton binding, dielectric confinement, transport across spacers) are QW physics, but the PV literature handles them mostly with SCAPS-type drift-diffusion.

### Cited Findings
- **Fraunhofer ISE/AMOLF Si-based triple junction:** **36.1%**, GaInP / GaInAsP on a TOPCon Si bottom cell with a metal/polymer nanocoating back reflector (EU PVSEC, Sept 2023). No QWs are mentioned. — [Fraunhofer ISE press release](https://www.ise.fraunhofer.de/en/press-media/news/2023/silicon-based-multijunction-solar-cell-reaches-record-efficiency-of361-percent.html)
- **Perovskite/Si:** 35.2% (1 cm²) and 34.3% (261 cm²) cells, both LONGi, per efficiency tables v68. — [pv-magazine USA 2026](https://pv-magazine-usa.com/2026/06/08/all-solar-cell-efficiencies-at-a-glance-updated-7/)
- **Wide-gap 1.7–1.9 eV III–V top cells for Si tandems** (SPIE 10527, 2018). — [SPIE](https://journals.spiedigitallibrary.org/conference-proceedings-of-spie/10527/105270C/Design-of-wide-bandgap-17-eV-19-eV-III-V/10.1117/12.2290053.full) [title-level]
- **GaAsP/Si tandem at 25%.** — [TaiyangNews](https://taiyangnews.info/technology/25-efficiency-for-gaaspsi-tandem-solar-cell) [title-level]
- **Older anchor on QW current matching in tandems:** "Strained and strain-balanced quantum well devices for high-efficiency tandem solar cells". — [HAL via Loughborough](https://vufind.lboro.ac.uk/PrimoRecord/cdi_hal_primary_oai_HAL_hal_02635403v1) [title-level]
- **2D RP perovskites** (2026 *RSC Advances/Energy Advances*-type paper, SCAPS-1D, n = 5 (MTEA)₂(MA)₄Pb₅I₁₆):
  - Simulated "upper limit" 20.79% (Voc 1.49 V, Jsc 17.17 mA/cm²).
  - Cites experimental benchmarks: Shao et al., *Adv. Mater.* 34, 2107211 (2022), ">21% efficiency stable 2D perovskite solar cells"; Dong et al., *Angew. Chem.* 64, e202501210 (2025), ">20%".
  - QW physics noted only qualitatively: low-ε spacers give dielectric confinement and large exciton binding.
  - Acknowledged limits: no ion migration or degradation, a single defect level, and orientation assumed.
  - — [RSC 2026, d5ya00364d](https://pubs.rsc.org/en/content/articlehtml/2026/ya/d5ya00364d)
- **RP layers as passivation:** an inverted perovskite cell with an RP passivation layer reached 21.4% (pv-magazine). — [pv-magazine](https://www.pv-magazine.com/?p=31653) [title-level]
- **Nanowire cells:** GaAsP single-nanowire cells on Si exceed 10%. — [KU](https://test01.ku.dk/:obvius/pureproxy/3974268/da/publications/surface-passivated-gaasp-single-nanowire-solar-cells-exceeding-10) [title-level]. No 2024–2026 nanowire record was verified.
- **QD vs QW in space cells (RIT):** 20 QD layers cost about 30 meV Voc but give limited current per layer and are hard to strain-balance. QWs give more Jsc with minimal BOL Voc loss. — [Hubbard SPW 2023](https://spw.aerospace.org/files/2023/06/2023-04_5_EG1_S.-Hubbard_Presentation.pdf)

### Inferences
- **III–V/Si:** QWs could tune the middle-cell gap (for example GaInAsP → GaAs:QW) for current matching to Si without metamorphic grading, as NREL did for GaAs. A computational design study (detailed balance plus realistic QW absorption and escape) of "QW-tuned middle cells for III–V/Si 3J" is plausible. I did not find it in my searches, but it is a natural extension of NREL's work and may exist in conference proceedings.
- **Perovskite/III–V tandems with QW bottom cells** are thin in the literature I found. A 4-terminal perovskite/GaAs-QW detailed-balance study is easy to do but of modest impact.
- **2D RP "quantum wells" is the largest open theory niche in this question.** Its quantum-confinement and dielectric-confinement physics maps onto the researcher's SP and excitonic and dielectric toolset. But RP PV papers are mostly materials-chemistry, and electron-structure modeling there is dominated by DFT. A paper connecting a well-width (n) dependent effective-mass/dielectric-confinement model to a detailed-balance + exciton-dissociation PV limit as a function of n could be novel. A prior-art check against the RP exciton literature (Blancon, Even, Katan, Mohite groups) is mandatory; not checked here.

### Gaps
- No verified data on whether any perovskite/III–V tandem record cell uses QWs.
- No 2024–2026 III–V/Si result with QWs was found.
- The current certified record for pure 2D RP cells was not verified from a primary source.
- No systematic QW vs QD vs nanowire comparison paper from 2018–2026 was found.

---

## Q4. Luminescent coupling, radiative efficiency, ERE, reciprocity (Rau), EL-based characterization of QW cells

### Takeaway
Rau-type reciprocity relies on assumptions that are known to break in nanostructured and ultrathin cells (Aeberhard PRL 2017). QW cells add more failure modes: bias-dependent QCSE shifts of the absorption edge, escape-limited collection, and polarization-anisotropic emission. Yet the record QW-cell papers report neither ERE nor luminescent-coupling analysis. A theory paper on "when EQE↔EL reciprocity holds for MQW cells" is a strong, experiment-free target.

### Cited Findings
- **Aeberhard, *PRL* 118, 247702 (2017).** Reciprocity assumes local absorption/emission balance, optical isotropy and non-degenerate quasi-equilibrium.
  - In ultrathin absorbers, the strongly bias-dependent built-in field changes the electronic structure, so short-circuit EQE cannot reproduce the EL spectrum.
  - Shown with NEGF for coupled photons and carriers.
  - — [arXiv:1702.02344](https://export.arxiv.org/abs/1702.02344)
- **Related reciprocity papers:**
  - SPIE 10099 "Photovoltaic reciprocity and quasi-Fermi level splitting in nanostructure-based…" — [SPIE](https://spiedigitallibrary.org/conference-proceedings-of-spie/10099/100990W/Photovoltaic-reciprocity-and-quasi-Fermi-level-splitting-in-nanostructure-based/10.1117/12.2251221.full) [title-level]
  - "Generalized reciprocity relation in p-i-n junction solar cells" — [HAL](https://hal.archives-ouvertes.fr/hal-02383533) [title-level]
  - "Quantum-kinetic perspective on photovoltaic device operation in nanostructure-based solar cells" — [arXiv:1707.03887](https://arxiv.org/pdf/1707.03887) [title-level]
  - "Simulation of nanostructure-based high-efficiency solar cells: challenges, existing approaches and future directions" — [arXiv:1304.1957](https://arxiv.org/pdf/1304.1957) [title-level]
- **Record QW-cell papers do not report ERE.** Steiner 2021 reports only that radiative and nonradiative rates "remain in the same ratio as in the baseline"; France 2022 reports "Radiative efficiency/ERE: not reported". — [NREL 80198](https://nrel.gov/docs/fy21osti/80198.pdf); [NREL 83983](https://nrel.gov/docs/fy23osti/83983.pdf)
- **Connolly/Barnham:** QWSC dark current at high injection is radiative-dominated, an older claim that set the "radiative limit" framing. — [arXiv:1006.1835](https://arxiv.org/abs/1006.1835)
- **Ahmed et al. 2025** separates radiative and nonradiative recombination via suns- and temperature-dependent PL/PV in GaInAs/GaAsP MQWs, so data of this type exist in the literature. — [NREL research hub](https://research-hub.nrel.gov/en/publications/charge-carrier-extraction-and-recombination-effects-in-gainasgaas/)

### Inferences
- **Paper idea: "Reciprocity and its breakdown in strain-balanced MQW solar cells".** Compute EQE(V) and EL(V) with the researcher's SP plus density-matrix absorption, including:
  - field-dependent Stark shifts,
  - escape-limited collection efficiency η_coll(V),
  - TE/TM-anisotropic emission into the escape cone and guided modes (the TM waveguide solver handles this).

  Then quantify the error in Voc and ERE extracted via Rau's relation. This needs no experiment; published NREL/RIT EQE and JV curves can be used for plausibility. It is related to but distinct from Aeberhard 2017, which treats a bulk ultrathin GaAs p-i-n with NEGF, not MQWs with escape.
- **Luminescent coupling in GaInP/GaAs-QW tandems** is relevant because the QW band edge (1.351 eV) sits below the GaAs host. Top-cell emission is fully absorbed, but QW emission is largely transmitted to the bottom subcell in a 3J or lost. A model of LC fractions and their effect on current-mismatch tolerance in QW-based 2J/3J is plausible. No dedicated QW-LC paper was found in my searches (gap).

### Gaps
- No direct search hits for a luminescent coupling study specific to strain-balanced QW multijunctions (the query returned generic LC items).
- No measured ERE for the 39.5% cell was found.
- Whether the Sugiyama/Tokyo group published EL/PL-based quasi-Fermi-level splitting in MQW cells after 2018 was not verified.

---

## Q5. Which purely computational papers are publishable now, where, and which have been done?

### Takeaway
Several experiment-free papers look viable and fit the toolkit closely. The strongest:
1. Type-II InAs/AlAsSb hot-carrier thermalization with real band structure and LO-phonon kinetics.
2. A unified escape/tunneling/recombination plus photon-recycling device model for thick strain-balanced superlattices, benchmarked to NREL's published numbers.
3. Reciprocity/ERE breakdown in MQW cells.
4. Field-dependent TPU and QW-IB detailed balance with realistic intersubband absorption (TM-coupled).
5. A tutorial/review plus open dataset of QW-cell records and parameters.

Open-source frameworks (Solcore) already cover QW absorption with k·p, so a "new QW solver" paper alone would not be novel.

### Cited Findings (prior art that bounds novelty)
- **Solcore** (Alonso-Álvarez, Wilson, Pearce, Führer, Farrell, Ekins-Daukes; *J. Comput. Electron.*) is a Python library with:
  - 8-band k·p strain,
  - a 1D Schrödinger solver,
  - QW absorption via Chuang's method (2D JDOS, TE/TM matrix elements, excitons).

  Stated limits: no quantum transmitting boundary method (QTBM), so unbound states are incorrect; closed or periodic boundaries; non-self-consistent parameters; hole-level differences vs 8-band nextnano. — [arXiv:1709.06741](https://ar5iv.arxiv.org/html/1709.06741); [PyPI solcore](https://pypi.org/project/solcore/)
- **Already done (models):**
  - Analytic QWSC efficiency-limit and dark-current models (Connolly/Barnham, about 2010) — [arXiv:1006.1835](https://arxiv.org/abs/1006.1835)
  - Rate-equation QW thermalization (Makhfudz 2022) — [arXiv:2209.13218](https://arxiv.org/abs/2209.13218)
  - ECUC/ratchet detailed balance (Zhang & Krich 2020) — [arXiv:1909.07874](https://arxiv.org/abs/1909.07874)
  - NEGF reciprocity in ultrathin cells (Aeberhard 2017) — [arXiv:1702.02344](https://export.arxiv.org/abs/1702.02344)
  - Effective-mobility MQW transport (Toprasertpong) — [arXiv:2006.00180](https://arxiv.org/abs/2006.00180)
  - Two-diode multi-mechanism fit of MQW cells (Ahmed 2025) — [NREL hub](https://research-hub.nrel.gov/en/publications/charge-carrier-extraction-and-recombination-effects-in-gainasgaas/)
  - SCAPS modeling of 2D RP cells (2026) — [RSC](https://pubs.rsc.org/en/content/articlehtml/2026/ya/d5ya00364d)
- **Reviews already done:** phonon-bottleneck/hot-carrier QWs (Zhang, Conibeer et al., *Prog. Photovolt.* 2022) — [IP Paris](https://researchportal.ip-paris.fr/en/publications/review-of-the-mechanisms-for-the-phonon-bottleneck-effect-in-iiiv/). Two-step photon upconversion overview (Kobe) — [Asahi publication list](https://www.research.kobe-u.ac.jp/eng-photonics/asahi/paper.html) [title-level]. I found no 2022–2026 review dedicated to strain-balanced QW cells after the 39.5% record.
- **Inverse design / ML:** searches for "machine learning inverse design quantum well solar cell" returned only generic thin-film or metasurface ML work (e.g., a transfer-learning thin-film solar cell paper, [PMC6430788](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6430788/)). I found no QW-stack inverse-design paper.
- **Venues as seen in this literature:**
  - J. Appl. Phys.: France 2022; Ahmed 2025; Watanabe 2021; Zhang & Krich 2020
  - Prog. Photovolt.: Zhang/Conibeer review 2022; efficiency tables v67
  - EPJ Photovoltaics: Boyer-Richard 2024
  - J. Phys. D: Makhfudz 2022
  - PRL: Aeberhard 2017
  - Sci. Rep. / APL: Esmaielpour 2018 / 2021
  - J. Comput. Electron.: Solcore
  - Joule: 39.5% record

### Candidate papers (needs experiment? / already done?)

| # | Paper idea | Toolkit fit | Needs experiment? | Prior art found | Suggested venue (inference) |
|---|---|---|---|---|---|
| 1 | Hot-carrier thermalization in type-II InAs/AlAsSb QWs: SP (nonparabolic InAs) → LO/interface-phonon rates with hot-phonon non-equilibrium → steady-state Tc(P), Q; compare with published 490 K data and barrier-thickness trend | Excellent (SP, nonparabolicity, LO-phonon rates) | No (uses published OU data); OU MBE samples available later | Generic type-I QW model by Makhfudz 2022; no type-II InAs/AlAsSb-specific kinetic model found | Phys. Rev. Applied / JAP / J. Phys. D |
| 2 | Device model for 80–300-period GaInAs/GaAsP and GaInAs/GaP superlattices: escape (thermionic + tunneling, including the ~5 nm crossover), capture, in-well SRH and radiative recombination, minibands at 2 nm GaP, photon recycling; explain the extra ~10 mV Voc loss and the FF/J02 trends | Very good (SP, tunneling, escape); needs a transport layer | No (fit NREL published JV/EQE/series data) | Experimental groups explicitly call for this (Ahmed 2025); older Connolly analytic models; Toprasertpong effective mobility. No full superlattice model reproducing France 2022 found | JAP / IEEE J. Photovolt. / Prog. Photovolt. |
| 3 | Reciprocity/ERE breakdown in MQW cells: bias-dependent QCSE absorption and η_coll(V), TE/TM-anisotropic emission; errors in Rau-derived Voc/ERE | Very good (density-matrix optics, TM waveguide) | No | Aeberhard 2017 (bulk ultrathin, NEGF); no MQW-specific treatment found | PRL-adjacent / Phys. Rev. Applied |
| 4 | EOL radiation modeling of QW space cells: fluence-dependent carrier removal and lifetime → field collapse in thick i-region; optimal QW placement and doping for EOL | Good (SP/Poisson) | No (use RIT published BOL/EOL numbers) | RIT lists it as open; no modeling paper found | IEEE J. Photovolt. / Sol. Energy Mater. Sol. Cells |
| 5 | TPU hetero-interface cell: field-dependent escape vs tunneling + intersubband (TM) absorption + detailed balance; optimal interface field; QW vs QD intraband step | Excellent (density-matrix intersubband, depolarization, TM waveguide) | No | Kobe group lists the optimal field as open; ideal TPU limit 46.8% exists | JAP / Phys. Rev. Applied |
| 6 | QW-IB / ratchet detailed balance with realistic intersubband absorptivity (depolarization shift, filling-dependent absorption) | Excellent | No | Idealized IB/ratchet limits exist (Zhang & Krich 2020; Imperial theses); realistic-QW version not found (needs a careful check) | Phys. Rev. Applied / Prog. Photovolt. |
| 7 | Valley-PV interface theory: valley-degeneracy mismatch at InGaAs/AlInAs and design rules | Moderate (needs multi-valley transport) | No | Stated limitation in Nature Energy 2020; theory follow-ups not verified | Phys. Rev. Applied |
| 8 | Inverse design of QW stacks (well/barrier thickness, composition, count, placement, back reflector) for target subcell current at fixed strain budget, under AM1.5G/AM0/EOL | Very good | No | No QW-stack inverse-design paper found | Solar RRL / Prog. Photovolt. / IEEE JPV |
| 9 | Open benchmark dataset plus meta-analysis of QW-cell records 1990–2026 (Voc, Woc, Jsc per well, number of wells, ERE where available) with Solcore-compatible inputs | Good | No | No such dataset found | Sol. Energy Mater. Sol. Cells / Scientific Data-type |
| 10 | Tutorial/review: "Strain-balanced QW solar cells after 39.5%: physics, models, open problems" (anchored on Vurgaftman/Lumb/Meyer Ch. 15) | Excellent | No | Older reviews exist (Barnham era); no post-2022 review found | Prog. Photovolt. / J. Appl. Phys. Tutorial |
| 11 | 2D RP perovskites as MQW absorbers: n-dependent confinement plus dielectric confinement plus exciton dissociation in a detailed-balance PV limit | Good (SP, dielectric) | No | SCAPS-only device papers; exciton physics literature large (not checked) | Solar RRL / JPCL-type (risky) |
| 12 | QW-tuned middle cells for III–V/Si 3J (current matching to Si without metamorphic layers) | Good | No | Not found; concept is old (QW current matching) | IEEE JPV / Solar RRL |

### Inferences
- **Priority by novelty × fit × no-experiment:** #1, #2, #3, #5 are the strongest. #10 (tutorial) is the safest first publication and positions the researcher; #9 can be bundled with #10.
- **Do not frame any paper as "a new QW solar-cell solver".** Solcore already provides k·p, Schrödinger and QW absorption in Python. Novelty must come from physics the toolkit adds and Solcore lacks: open-boundary or escape, nonparabolic SP self-consistency, LO-phonon kinetics, depolarization and intersubband density-matrix response, TM-mode waveguide coupling.
- **Experimental partners for later validation.** The OU MBE group (Santos, Mishima) and Whiteside, plus Sellers (now apparently Buffalo) with France (NREL), are the active experimental line on both hot-carrier InAs/AlAsSb QWs and GaInAs/GaAsP MQW extraction. This is a direct route from a theory paper to experiment.

### Gaps
- Journal scope and fit were inferred from where similar papers appeared, not checked against current author guidelines. Prog. Photovolt. reportedly changed handling of the efficiency tables (v68 in Joule per pv-magazine), unverified.
- No systematic forward-citation search was done on the anchor papers (Connolly 2010, Aeberhard 2017, Makhfudz 2022, France 2022, Ahmed 2025). Ideas #1–#6 must be checked against 2023–2026 citing papers before writing.
- The full text of Joule 2022 (39.5%) and Ahmed 2025 was not read, so the exact parameter sets usable for benchmarking were not extracted.
- QW-based TPV (also covered in Vurgaftman et al. Ch. 15) and nonlinear QW devices were not researched here.
