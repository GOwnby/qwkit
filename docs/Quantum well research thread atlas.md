# Intersubband physics anchors a solo quantum-well research programme

About seventy raw ideas from the five topic notes and the earlier frontier survey reduce to **58 de-duplicated entries: 51 actionable papers and 7 parked or avoided directions**. **45 of the 51 need no new experiment.** What separates them is less novelty than toolkit reach. qwkit v0.4 already runs the full conduction-band intersubband (ISB) chain. So nonlinear-optics, ISB-emitter and oxide/2D intersubband papers can start now. Nearly every solar-cell and thermophotovoltaic (TPV) device paper, by contrast, first needs valence-band states, interband absorption and escape or transport modules that qwkit lacks.

The strongest papers that can be written now are six:
- a qwkit software paper;
- saturation-limited efficiency and contrast bounds for ISB nonlinear devices, going beyond the two-level Maxwell–Bloch formulas the field still uses ([Krakofsky et al. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12617711));
- a collective (TDHF/RPA) second-order response beyond Ando;
- differentiable, fluctuation-aware inverse design of bias-switchable stacks (no automatic-differentiation heterostructure solver turned up in the notes' searches);
- temperature limits of electrically switchable ISB thermal emitters for low-temperature TPV;
- ISB absorption and χ(2) at the polar LaInO3/BaSnO3 interface, which has been studied only for transport ([Lee et al. 2024](https://schlom.mse.cornell.edu/sites/default/files/research%20pdfs/Adv%20Elect%20Materials%20-%202024%20-%20Lee%20-%20Observation%20of%20Mobility%20Above%202000%20cm2%20V%20s%20in%202DEG%20at%20LaInO3%20BaSnO3%20Interface%20by_0.pdf)) and sits next to Hanjong Paik's oxide MBE.

Together these make an 18–24-month programme. It runs from tool, to limits, to many-body physics, to design, to energy, to new materials, and ends with proposed experiments at OU. The most valuable energy threads should come in a second wave, after one shared interband module exists. These are:
- hot-carrier thermalisation in type-II InAs/AlAsSb wells, checked against published OU data;
- a device model for 80–300-period strain-balanced superlattices that explains NREL's unexplained ~10 mV Voc loss ([France et al. 2022](https://nrel.gov/docs/fy23osti/83983.pdf));
- reciprocity breakdown in multiple-quantum-well (MQW) cells.

Before N1 is submitted, two items must be read and cited:
- **J. Yu, J. Kim, H. Chung, J. Son, G. Boehm, M. A. Belkin & J. Lee, Sci. Adv. 11, eadw8852 (2025), doi:10.1126/sciadv.adw8852**, on full complex-amplitude electrical control of ISB SHG in polaritonic metasurfaces. Only its metadata was retrieved, and it is the closest prior art to bias-polarity sign reversal ([Nature Index record](https://www.nature.com/nature-index/article/10.1126/sciadv.adw8852)).
- **Park et al., Light Sci. Appl. 13, 169 (2024)**, which showed electrically induced phase gratings in ISB third-harmonic generation ([Park et al. 2024](https://link.springer.com/10.1038/s41377-024-01517-y)).

Every "not found" novelty call rests on roughly 30–55 web-search calls per area. Confirm each one in Scopus or Web of Science before writing.

## qwkit reaches every intersubband question but few interband ones

The reuse column in the master table follows from what qwkit v0.4 contains:
- 1D Schrödinger–Poisson with Kane nonparabolicity
- Löwdin orthonormalisation
- Ando depolarisation
- Fröhlich LO-phonon rates
- density-matrix χ(2)
- multilevel saturation rate equations
- a planar TM waveguide solver
- an electrode Laplace solver
- coupled-mode SHG with quasi-phase matching (QPM) and segmented media

All of it is parameterised for InGaAs/InAlAs.

The reuse labels mean:
- **"Full":** the paper needs only these modules plus a new material parameter set.
- **"Extension":** the paper adds one or two modules inside the same 1D framework. Examples are hole subbands, transfer-matrix tunnelling, thermal subband populations, polarisation sheet charges, multi-mode Fröhlich sums, a layer-chain Hamiltonian, or a JAX port.
- **"New code":** the paper needs a new solver class, such as multiband k·p, drift-diffusion, fluctuational electrodynamics, real-time TDSP, RCWA/FDTD or NEGF.

This split explains most of the ranking below. The nonlinear, ISB-emitter, polariton and emerging-material ISB papers score "Full" or light "Extension". The solar and TPV device papers need hole states, interband absorption with excitonic edges, escape/tunnelling rates and some drift-diffusion.

That gap is not a reason to abandon the energy threads. It is a reason to build one interband/escape module once and reuse it. The same module serves:
- the superlattice device model (SC-01);
- reciprocity breakdown (SC-04);
- two-step photon upconversion (SC-05);
- QW absorbers in air-bridge TPV (TPV-01);
- thermophotonic QW LEDs (TPV-04).

There is also a cheaper route. Solcore already gives Python 8-band k·p and Chuang-method QW absorption with TE/TM matrix elements and excitons. Its stated weakness is the absence of open boundaries, so unbound states come out wrong ([Solcore](https://ar5iv.arxiv.org/html/1709.06741)). Coupling qwkit's escape physics to Solcore's interband absorption, rather than rewriting k·p, is the effort-minimising path. It also forbids framing any paper as "a new QW solar-cell solver".

## Nonlinear intersubband optics: experiments now outrun a two-level theory

### State of the art

Polaritonic ISB metasurfaces are the most active experimental front. A 2025 review puts MQW χ(2) and χ(3) **3–5 orders of magnitude above natural crystals**, with ISB dipoles of about 100 D. The benchmark results it cites are:
- **χ(2)_eff ≈ 55 nm/V** (Lee et al., Nature 2014);
- **0.14% SHG power efficiency** at 1–10 W pump;
- Kerr χ(3) above 10⁻¹³ m²/V² with sub-2 ps response;
- saturable reflection dropping from ~0.64 to below 0.1 between ~100 kW/cm² and ~10 MW/cm².

The same review still uses a simplified two-level Maxwell–Bloch model. Its stated bounds are:
- power-limiter contrast ΔR ≤ 1/(1 + 2γ_aγ_2/Ω²)²;
- a maximum Rabi frequency of **Ω_max ≈ 0.26 ω_q**, against the 0.13 ω_q used to date;
- a warning that saturation already matters at ~50 kW/cm², so "pump, material and photonics must be co-optimized" ([Krakofsky et al. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12617711)).

Electrical control has advanced quickly. Park et al. reported:
- **|χ(3)_zzzz| = 7.15×10⁻¹⁴ m²/V²** at 9 µm;
- **450% modulation depth**, **~1.1π phase tuning** and ±10.7° beam steering in ISB THG;
- a four-subband Poisson–Schrödinger model, whose predicted Stark tuning overshot the measurement (attributed to nonuniform Schottky band bending);
- RC-limited bandwidth of only **~3.38 MHz** ([Park et al. 2024](https://link.springer.com/10.1038/s41377-024-01517-y)).

The 2025 Science Advances paper extends this to full complex-amplitude SHG control ([Nature Index record](https://www.nature.com/nature-index/article/10.1126/sciadv.adw8852)).

The review calls THz DFG from ISB metasurfaces "only theoretical". That conflicts with a CLEO 2024 report of **continuous-wave THz DFG** that beats photomixers at 2.5–5 THz. Its reported χ(2) > 10⁵ pm/V has a garbled exponent and should be treated with caution ([Krakofsky et al., CLEO 2024](https://portal.fis.tum.de/en/publications/continuous-wave-terahertz-difference-frequency-generation-from-in/)).

Time-dependent Schrödinger–Poisson work predicts an intensity-driven redshift, because the dipole shrinks and the depolarisation shift is suppressed. That coherent nonlinearity is distinct from incoherent saturation ([Cominotti et al., PRB 2023](https://arxiv.org/abs/2109.00285)).

### Adjacent fronts

**Quantum cascade lasers (QCLs).** Monolithic ring QCLs now host:
- free-running dark solitons ([Opačak et al., Nature 2024](https://link.springer.com/article/10.1038/s41586-023-06915-7));
- DC-driven bright solitons of **~1 ps at 8.3 µm** ([Kazakov et al., Nature 2025](https://ideas.repec.org/a/nat/nature/v641y2025i8061d10.1038_s41586-025-08853-y.html)).

Their microscopic inputs are still poorly understood:
- The Bloch-gain Kerr coefficient (~10⁻¹⁵ m²/W) comes with a dispersive lineshape whose origin is "not well understood" ([Opačak et al., PRL 2021](https://ar5iv.labs.arxiv.org/html/2102.08167)).
- NEGF gives linewidth-enhancement factors of 0.1–1. Two-level models reach only ~0.04, and density-matrix approximations can get the sign wrong at the gain peak ([Franckié et al.](https://ar5iv.labs.arxiv.org/html/2207.09222)).

**ISB polaritons and quantum ISB optics.** ISB polaritons now show:
- stimulated coherent scattering ([Knorr et al., PRL 2022](https://pred.uni-regensburg.de/id/eprint/58228/));
- spontaneous polariton–LO-phonon scattering, though at an "extremely low" rate ([Goulain et al. 2025](https://arxiv.org/abs/2509.13843)).

Quantum ISB optics remains theory. The leading proposal is photon-exchange-bound bound-to-continuum polaritons with Rydberg-like giant nonlinearities ([Oliveira & Ciuti 2025](https://arxiv.org/abs/2510.24421)).

**Interband χ(2) and modulators.** On the interband side:
- Asymmetric AlGaAs/GaAs coupled wells reached **2750 pm/V** at 1550→775 nm, more than 7× bulk GaAs. Growth interruptions pushed them toward ideal-interface predictions ([Ramesh et al. 2026](https://arxiv.org/abs/2602.23246)).
- A coupled-well metasurface reached **~14 nm/V effective** ([Fathi et al. 2026](https://arxiv.org/abs/2604.15476)).
- Unipolar Stark modulators carry **10 Gbit/s at 9 µm** ([Dely et al.](https://arxiv.org/abs/2110.06572)).
- GaN/AlN ISB switches measured Isat ≈ 9.6 W/µm² against a 3.9 W/µm² theory. A claimed 30× reduction in coupled wells was never demonstrated ([Li et al. 2007](https://www.bu.edu/paiella/files/2021/08/OE_AlGaN_ISB_PumpProbe.pdf)).

### Open problems

Four problems stand out:
- rigorous multilevel bounds for conversion efficiency and switching contrast;
- many-body second-order response at high doping;
- time-modulated, nonreciprocal metasurfaces, which have been proposed but not demonstrated (the closest analogue is a superconducting JoFET metasurface, [Taravati 2024](https://arxiv.org/abs/2409.08137));
- interface-tolerance analysis for engineered χ(2).

### Where N1 sits

Bias-polarity sign-reversal QPM itself was anticipated by US 4,880,297 (1989) and US 5,289,309 (1994). N1's novelty is narrower:
- **the design:** the mirror-symmetric triple well, which reaches 53% of an optimised asymmetric double quantum well (ADQW) at 55 kV/cm;
- **the comparison:** saturation-aware, giving 1.9–4.7× over realistic Stark QPM and 1.0–1.9× over an ideal growth-reversed ADQW above ~1 W.

The Science Advances 2025 paper controls the SHG phase locally in a metasurface rather than through propagation QPM. That distinction must be verified from the full text and stated explicitly in N1. Park et al. 2024 must be cited as the precedent for electrically written phase gratings.

## Quantum-well solar cells: 39.5% records, but no validated device model

### Records and the unexplained losses

Strain-balanced GaInAs/GaAsP superlattices with up to 300 periods hold the one-sun records:
- **39.5% (3J)** and **32.9% (2J)**, with **34.2% AM0** ([NREL](https://research-hub.nrel.gov/en/publications/record-efficiency-multijunction-solar-cells-with-strain-balanced-/));
- a **27.2% certified** GaAs-QW single junction at Voc 1.040 V ([Steiner et al. 2021](https://nrel.gov/docs/fy21osti/80198.pdf)).

France et al. thinned the barriers from 170 Å GaAsP to 20 Å GaP and found three things they could not fully explain ([France et al. 2022](https://nrel.gov/docs/fy23osti/83983.pdf)):
- tunnelling and thermionic lifetimes become equivalent at **~5 nm** barrier thickness;
- thickening the GaInAs from 850 to 2550 nm cut the gap by 15 meV but Voc by 25 mV, and the extra **~10 mV is "not identified"**;
- whether GaP-barrier stacks are optically thick without a rear reflector is "not known".

Neither NREL paper reports external radiative efficiency (ERE) or per-well absorption. Temperature- and suns-dependent work on the same devices concludes the field must "move beyond simple drift-diffusion models" ([Ahmed et al., JAP 2025](https://research-hub.nrel.gov/en/publications/charge-carrier-extraction-and-recombination-effects-in-gainasgaas/)).

Radiation hardness is a clean modelling target ([Hubbard, SPW 2023](https://spw.aerospace.org/files/2023/06/2023-04_5_EG1_S.-Hubbard_Presentation.pdf)). After 1 MeV electrons at 10¹⁵ cm⁻², QW single junctions:
- keep 92% of Jsc against 81% for controls;
- lose Voc from 0.996 to 0.760 V;
- retain only **60% of efficiency against 72%**.

### Next-generation concepts remain at proof of principle

The OU-led hot-carrier line is the most relevant here:
- Type-II InAs/AlAsSb wells reached a steady-state hot-electron temperature of **490 K**, with thermalisation stretched "from picoseconds to nanoseconds" ([Esmaielpour et al., Sci. Rep. 2018](https://researchconnect.suny.edu/en/publications/enhanced-hot-electron-lifetimes-in-quantum-wells-with-inhibited-p/)).
- Thicker barriers tune the phonon bottleneck ([Esmaielpour et al., APL 2021](https://www.aip.org/scilights/photovoltaic-power-generation-can-be-improved-by-keeping-the-electrons-hot)).
- Valley photovoltaics, done at OU, did not exceed the single-gap limit. The cause was valley-degeneracy mismatch at the heterointerface ([Esmaielpour et al., Nature Energy 2020](https://link.springer.com/article/10.1038/s41560-020-0602-0)).

The theory behind these is still generic. Makhfudz et al. model type-I wells with simple bands and find a non-monotonic thickness dependence once hot LO phonons and screening are included ([Makhfudz et al. 2022](https://arxiv.org/abs/2209.13218)). A 2025 review notes "some debate" on thermalisation pathways ([Afshari et al. 2025](https://pubs.rsc.org/en/content/articlepdf/2025/el/d5el00063g)). An InGaAs/AlInAs single-QW energy-selective contact gave Voc 0.28 V without hot-carrier operation, and its authors say the confined level must be redesigned ([Boyer-Richard et al. 2024](https://www.epj-pv.org/articles/epjpv/full_html/2024/01/pv20240018/pv20240018.html)).

Two-step photon upconversion (TPU) cells reach **5.1%** against a 46.8% detailed-balance limit. The Kobe group lists the optimal interface field (16.6 kV/cm gave a ~45% IR-induced EQE boost) and the tunnelling/extraction balance as open ([Watanabe et al. 2021](https://da.lib.kobe-u.ac.jp/da/kernel/90008540/90008540.pdf)). Intermediate-band absorption is known to depend strongly on band filling, more than two orders of magnitude for E_L ([Ramiro et al., PRB 2017](https://link.aps.org/accepted/10.1103/PhysRevB.96.125422)). Yet intermediate-band and ratchet limits still use idealised step absorptivities ([Zhang & Krich 2020](https://arxiv.org/abs/1909.07874)).

### Records elsewhere do not use QWs

As far as the notes found, the leading cells outside all-III–V multijunctions do not use QWs:
- the Fraunhofer III–V/Si triple junction at **36.1%** ([Fraunhofer ISE](https://www.ise.fraunhofer.de/en/press-media/news/2023/silicon-based-multijunction-solar-cell-reaches-record-efficiency-of361-percent.html));
- perovskite/Si at **35.2%** ([pv magazine 2026](https://pv-magazine-usa.com/2026/06/08/all-solar-cell-efficiencies-at-a-glance-updated-7/)).

Pure 2D Ruddlesden–Popper "quantum-well" perovskites sit near 20–21%, and are modelled mostly with SCAPS ([RSC 2026](https://pubs.rsc.org/en/content/articlehtml/2026/ya/d5ya00364d)). One unresolved point: efficiency tables v67 appeared in Prog. Photovolt. ([ISFH](https://isfh.de/en/publications/solar-cell-efficiency-tables-version-67)), but pv magazine reports v68 "in Joule". Verify the venue before citing.

### Implications for this researcher

The **highest-fit solar paper is hot-carrier kinetics in type-II InAs/AlAsSb**. It reuses the nonparabolic SP and Fröhlich modules, it is checked against published OU data, and it connects directly to Santos and Mishima's MBE.

The **highest-impact solar paper is the thick-superlattice device model**, where NREL and the Sellers group have published the unexplained numbers. It needs the most new code and faces direct competition from the experimental groups, so it belongs in the second wave. Sellers now appears in University at Buffalo listings and co-authors with NREL's France. That is an inference from listings, not a confirmed arrangement.

## Thermophotovoltaics: 44% records, with quantum structures largely absent

### Far-field records and what limits them

Far-field TPV has reached:
- **41.1%** with a 1.4/1.2 eV tandem at ~2400 °C and 2.39 W/cm² ([LaPotin et al. 2022](https://arxiv.org/abs/2108.09613));
- **38.8%** with 0.74 eV GaInAs at 1850 °C and 3.78 W/cm² ([Tervo et al. 2022](https://arxiv.org/abs/2207.00565));
- **~44%** (43.8% for 0.90 eV InGaAs at 1435 °C) with a near-99%-reflective air-bridge cell ([pv magazine 2024](http://pv-magazine-usa.com/2024/05/28/u-s-scientists-develop-air-bridge-thermophotovoltaic-cells-with-44-efficiency/)).

The limits are out-of-band reflectance, parasitic free-carrier absorption, series resistance and emitter durability. The first calorimetric Ge TPV measurement (7.3%) identified free-carrier absorption in the doped substrate as the dominant loss ([Datas group 2026](https://papers.cool/arxiv/2602.08761)). Commercial pull is real:
- Fourth Power plans a 25 MW / 250 MWh graphite unit and a 1 MWh pilot ([MIT News 2026](https://news.mit.edu/2026/turning-extreme-heat-large-scale-energy-storage-0318));
- Antora claims >40% cells from a 2 MW/yr line ([Antora](https://antoraenergy.com/tpv)).

### Near-field TPV and thermophotonics

Near-field TPV is still below ~15% efficiency ([Jeyar et al. 2024](https://arxiv.org/html/2412.04258v1)). NREL scaled it to a 0.28 cm² pair at a 150 nm gap, giving ~25× the far-field power ([Selvidge et al. 2024](https://arxiv.org/abs/2408.01295)). A zero-vacuum-gap spacer doubles far-field power density but calls for cells below 0.7 eV ([Habibi et al., EES 2025](https://pubs.rsc.org/en/content/articlehtml/2025/ee/d4ee04604h)).

Thermophotonics (LED + PV) still has no functional device. GaAs efficiency falls from 63% to 18% as EQE drops from 100% to 95%, and the requirements analysis does not discuss QW active regions ([Sadi et al.](https://acris.aalto.fi/ws/portalfiles/portal/80226279/Prospects_and_requirements_for_thermophotonic_waste_heat_energy_harvesting.pdf)).

### QW and ISB structures are nearly dormant in TPV

QW-TPV has been almost dormant since 2018. The live quantum-structure threads are very-low-gap cells:
- OU's interband-cascade TPV: a 3-stage ~0.4 eV cell gave **9.6%** at 300 K (pre-window, ~2017) ([OSTI](https://www.osti.gov/biblio/1497660)), with later ~0.2 eV multistage devices ([OU QDL](https://sites.create.ou.edu/qdlou/2023/05/23/multistage-interband-cascade-thermophotovoltaic-devices-with-0-2-ev-bandgap));
- Montpellier's 0.23 eV InAs/InAsSb barrier cells: Voc ~75 mV at 273 K, no efficiency reported ([pv magazine 2026](http://www.pv-magazine.com/2026/08/24/very-low-bandgap-thermophotovoltaics-for-operation-at-higher-temperatures/)).

Theory favours thin absorbers. Photon recycling lets cells thin down and shed Auger volume, and a thin InAs near-field cell exceeds 50% at a 1100 K emitter ([Papadakis et al. 2021](https://arxiv.org/abs/2107.10705)). Coupled fluctuational-electrodynamics/drift-diffusion models exist for bulk cells only ([Callahan et al. 2021](https://arxiv.org/abs/2101.04746v1)).

On the emitter side, Noda's carrier-depletion ISB emitter switched emissivity from **0.74 to 0.24**, about 10⁴× faster than thermal modulation ([Inoue et al., Nat. Mater. 2014](https://www.nature.com/articles/nmat4043)). No theory of how such emitters behave at 500–1000 K turned up.

Hot-carrier TPV has an idealised detailed-balance treatment claiming near-Carnot efficiency near maximum power ([Nimje et al. 2023](https://arxiv.org/abs/2311.04795)), but realistic QW cooling physics has not been added.

### The opening for this researcher

The open niche is the intersection the field skipped: quantum-structure physics in modern TPV regimes. The emitter paper (TPV-05) is the only TPV entry that reuses qwkit almost entirely. It also creates a natural pairing with Rui Q. Yang's interband-cascade cells, whose mid-IR band edges match ISB emission.

## Methods and software: open codes are fragmented, and none is differentiable

### The open-code landscape

The open ecosystem covers pieces but not the ISB-optics chain:
- **kdotpy** covers lattice k·p and was published in SciPost Phys. Codebases ([kdotpy](https://arxiv.org/abs/2407.12651)).
- **Aestimo 1D** covers 1D Schrödinger–Poisson and was published in Comput. Mater. Sci. 2021 ([Aestimo](https://avesis.gazi.edu.tr/yayin/4d70de09-17fc-4bd8-8c3d-9f41708e813f/general-purpose-open-source-1d-self-consistent-schrodinger-poisson-solver-aestimo-1d)).
- **ErwinJr2** covers QCL design ([PyPI](https://pypi.org/project/ErwinJr2)).
- **Solcore** and **Sesame** cover solar cells ([Sesame](https://arxiv.org/pdf/1806.06919)).
- **NEGF** with LO/acoustic phonons, interface roughness, alloy disorder and e–e scattering exists commercially in nextnano ([nextnano.NEGF](https://www.nextnano.com/docu/nextnano.NEGF/overview/index.html)).

No open, tested chain combining depolarisation, LO-phonon rates, χ(2), saturation and waveguides was found. That is the qwkit software paper's justification.

### Design optimisation and machine learning

Design work has moved quickly:
- **Bayesian optimisation with NEGF** helped reach the 210 K THz-QCL record. The same study found period thickness must be held within a few percent ([PR Applied 2020](https://link.aps.org/doi/10.1103/PhysRevApplied.13.034025)).
- **An MLP surrogate** screened ~907 million designs in 8 h and raised a figure of merit from 94.7 to 141.2 eV ps Å² ([Correa Hernandez & Gmachl 2024](https://arxiv.org/abs/2406.07755)).
- **A 2026 ANN surrogate** trained on 62,250 density-matrix samples gave a ~90,000× speed-up ([Stojković et al. 2026](https://www.mdpi.com/2079-4991/16/11/651)).

Every surrogate is local to one reference design and ignores growth fluctuations. The only "inverse design" heterostructure hits were 1996–1999 inverse-scattering papers ([cond-mat/9903445](https://arxiv.org/abs/cond-mat/9903445)). No differentiable Schrödinger–Poisson solver turned up.

### Unsettled band-structure methods

Several basics remain unsettled:
- Spurious-solution handling is still ad hoc. A 2023 8-band InAs/GaSb study pays "careful attention" to it without giving a general recipe ([Murphy et al. 2023](https://arxiv.org/abs/2310.18194)).
- No uncertainty-quantification study propagating band-parameter spreads into QW observables was found.
- Self-consistent GW inside NEGF has been demonstrated only for carbon nanotubes ([Deuschle et al. 2023](https://arxiv.org/abs/2307.05297)).

### Many-body ISB optics

The multisubband-plasmon framework is established theory with a 2023 perspective ([Montes Bajo et al., JAP 2023](https://oa.upm.es/86098/)) and a plasmon–phonon coupling extension ([Photonics 2020](https://hal.sorbonne-universite.fr/hal-02553732v1)). Neither has an open implementation. qwkit's Ando module is the entry point to both, and to the "beyond Ando" second-order paper.

## Emerging platforms: oxides, nitrides and vdW wells have little self-consistent theory

### Oxides: the best local fit

Oxide ISB optics has one firm experiment: room-temperature ISB absorption approaching 1.55 µm in SrTiO3/LaAlO3 MQWs, across a ~2.4 eV conduction-band offset ([Ortmann et al., ACS Nano 2018](https://impact.ornl.gov/en/publications/quantum-confinement-in-oxide-heterostructures-room-temperature-in/)).

BaSnO3 wells exist only as claims at APS-abstract, thesis and conference level:
- "giant" χ(2) ([APS 2022](https://meetings-archive.aps.org/mar/2022/g71/8));
- near-IR-to-visible ISB with m* ≈ 0.2 m_e ([APS 2023](https://meetings-archive.aps.org/mar/2023/yy07/4));
- field-tuned ISB ([NUSOD 2022](https://nusod2022.polito.it/?p=16002)).

The underlying thesis measured no ISB absorption and lists nonparabolicity, phonons and χ(2) as untreated ([Jang 2023](https://fileserver-az.core.ac.uk/download/604297958.pdf)).

The polar LaInO3/BaSnO3 interface has been studied only for transport. It shows:
- a ~1.6 eV offset;
- **~2100 cm²/V·s at 10 K**;
- gate-tuned densities up to ~10¹⁴ cm⁻² (the paper's figures are internally inconsistent on the exact value) ([Lee et al. 2024](https://schlom.mse.cornell.edu/sites/default/files/research%20pdfs/Adv%20Elect%20Materials%20-%202024%20-%20Lee%20-%20Observation%20of%20Mobility%20Above%202000%20cm2%20V%20s%20in%202DEG%20at%20LaInO3%20BaSnO3%20Interface%20by_0.pdf));
- a DFT-predicted 2DEG of up to 0.5 e per unit-cell area in the dispersive Sn-5s band ([Aggoune & Draxl](https://arxiv.org/abs/2103.07216)).

That makes LaInO3/BaSnO3 a polarisation-asymmetric optical quantum well with nonzero χ(2) and no compositional stepping, which is exactly qwkit's domain. Paik brings adsorption-controlled BaSnO3 MBE from the Schlom/PARADIM lineage to OU ECE ([OU](https://ou.edu/coe/ece/people/faculty/hanjong-paik)). A pure-theory precedent exists: β-(AlGa)2O3/Ga2O3 ISB and QWIP design predicted ~10¹¹ Jones at 1.55 µm ([Lyman & Krishnamoorthy 2020](https://arxiv.org/abs/2001.07299v2)).

### Nitrides and group IV

- **ScAlN/GaN.** Lattice-matched Sc0.14Al0.86N/GaN wells show ISB at 515–709 meV, and net polarisation rises with Sc "faster than previous theoretical predictions". This is a clean inverse problem, but Purdue is fitting its own data ([Abdin et al. 2025](https://meetings-archive.aps.org/smt/2025/mar-q39/6/)).
- **GaN/AlN.** Telecom ISB is now combined with plasmonic antennas for SHG ([Mundry et al.](https://www.arxiv.org/abs/2105.09726)).
- **Deep-UV AlGaN.** The problems are p-doping and valence-band ordering, which need k·p ([Jena 2026](https://djena.engineering.cornell.edu/papers-new/2026/jena2026deep.pdf)).
- **Ge/SiGe.** n-type L-valley Ge/SiGe gave the first group-IV THz ISB electroluminescence at 3.4 and 4.9 THz, with "suboptimal injection" ([Stark et al. 2021](https://arxiv.org/abs/2101.05518v1)). Asymmetric coupled Ge/SiGe wells have been engineered ([Persichetti et al. 2020](https://arxiv.org/abs/2002.05074)). Ge is nonpolar, so lifetimes need deformation-potential scattering, not Fröhlich.

### Other platforms

- **ZnO.** m-plane ZnO/MgZnO emitted at **8.5 THz** up to room temperature, inside the GaAs reststrahlen gap, but no laser yet ([Meng et al. 2021](https://docta.ucm.es/entities/publication/41aea113-9dbc-4cae-9a26-c95dc5e723b2/full)).
- **CdSe nanoplatelets.** They show 900–1600 nm ISB with atomically defined thickness ([Diroll et al. 2019](https://ideas.repec.org/a/nat/natcom/v10y2019i1d10.1038_s41467-019-12503-z.html)).
- **Few-layer van der Waals wells.** ISB has been tuned electrically by more than 100 meV in WSe2 ([Wutz et al., ACS Nano 2026](https://epub.uni-regensburg.de/78725/1/electrical-control-of-intersubband-transitions-in-few-layer-wse2-multivalley-quantum-wells-probed-by-electronic-raman.pdf)) and by more than 250 meV in InSe ([Shcherbakov et al. 2024](https://arxiv.org/abs/2312.03228v1)). Both use phenomenological infinite-well fits. No resonant χ(2) theory under displacement field was found.

## Master table: every paper opportunity, de-duplicated and ranked

### Legend

The columns use these labels:
- **Reuse:** Full, Ext (extension) or New (see the qwkit section).
- **Experiment:** No; Opt (optional proposed experiment written into the paper); Collab (needs a partner's data or devices).
- **Prior-art status:** NF (not found in the notes' searches); Partial (named partial prior art); Incumbent (strong competing group); Unchecked (no search done).
- **Effort, for one person:** S ≤3 months, M 3–6, L 6–12, XL >12.
- **Priority:** P1 start within 12 months; P2 strong but second wave or collaborator-dependent; P3 opportunistic; P4 park or avoid.

Entries tagged [E] come from the earlier frontier survey. Merged sources appear in brackets.

| ID | Title | Area | Gap and why it is open | Calculation | qwkit reuse | Needs experiment? | Prior-art check status | Target venue | Effort | Priority |
|---|---|---|---|---|---|---|---|---|---|---|
| NL-01 | Interface and monolayer tolerance of bias-sign-reversal χ(2) designs | Nonlinear | Bank/Khurgin found interface abruptness limits engineered χ(2); no tolerance study for sign-reversal stacks | Monte Carlo over interdiffusion profiles and ±1 ML errors; χ(2) magnitude, sign, QPM duty error | Full | No | NF | Fold into N1, or Opt. Express / JOSA B | S | P1 (fold into N1) |
| NL-02 | Saturation-limited efficiency and contrast bounds for ISB conversion in waveguides and polaritonic metasurfaces [E1 + switch/limiter bounds + model-hierarchy benchmark] | Nonlinear | Field uses two-level Maxwell–Bloch bounds (ΔR, Ω_max ≈ 0.26 ω_q); saturation caps total power; no multilevel bound | Multilevel saturation + DM χ(2) + TM modes + coupled-mode; compare two-level MB, multilevel DM, TDSP | Full (TDSP arm Ext) | No | NF (only two-level formulas in 2025 review) | PR Applied / Optica | M | P1 |
| NL-03 | Electrically programmable QPM for THz DFG, benchmarked against CW metasurface DFG [E2 + metasurface DFG theory] | Nonlinear | CW THz DFG from metasurfaces is conference-level only; no programmable-QPM waveguide THz design found | Three-level DM χ(2) at THz, THz free-carrier and phonon loss, segmented QPM | Ext (THz loss and dispersion) | Opt (Belkin/TUM-type) | Partial (QCL intracavity DFG lineage, unchecked) | PR Applied / APL Photonics | M | P2 |
| NL-04 | Mid-IR photon pairs from bias-programmed QPM [E6] | Nonlinear | Quantum ISB light is almost all theory; no ISB SPDC design found | SPDC joint spectral amplitude from χ(2) + QPM + waveguide dispersion; loss and thermal-noise floor | Ext (JSA, noise) | No | Unchecked (interband telecom pairs proposed 2026) | Optica Quantum / PR Applied | M | P2 |
| NL-05 | Collective (TDHF/RPA) second-order response beyond Ando: depolarisation detuning of double resonance [E4 + many-body χ(2)] | Nonlinear / Methods | Ando is a linear correction; TDSP shows intensity-dependent collective shifts; χ(2) in the multisubband-plasmon regime unverified | Second-order TDHF/RPA in subband basis; compare with DM χ(2) + Ando; TDSP spot checks | Ext | No | Partial (older Rosencher/Bois work unverified) | PRB | M | P1 |
| NL-06 | Floquet Stark-modulated ISB metasurfaces for nonreciprocity and frequency shifting | Nonlinear | Nonreciprocal ISB routers proposed but not demonstrated; RC limit 3.38 MHz | Time-modulated DM + coupled-mode; RC and capacitance from electrode solver | Ext | No | NF (only JoFET analogue) | Nanophotonics / ACS Photonics | M–L | P2 |
| NL-07 | Non-perturbative ISB harmonic generation (THG, 5HG, HHG) via multi-subband TDSP | Nonlinear | No QW-specific HHG found; Cominotti TDSP limited to the coherent shift | Real-time Schrödinger–Poisson with continuum and depolarisation | New (real-time solver) | No | NF (search-level) | PRB | L | P3 |
| NL-08 | Bandwidth and figure-of-merit bounds for ISB Stark modulators | Nonlinear | 10 Gbit/s devices exist; no general FoM or bound paper | Stark coefficient vs insertion loss, tunnelling time, patch capacitance | Full | No | NF | PR Applied / IEEE JQE | S–M | P2 |
| NL-09 | Doubly resonant two-photon QWIP/QCD for ps autocorrelation of ring-QCL solitons | Nonlinear | 68 GHz soliton crystals uncharacterised; 1 ps pulses need quadratic detectors | Two-photon rates, LO lifetimes, photoconductive gain | Ext (gain and transport) | Opt | Partial (two-photon QWIPs exist at HZDR) | PR Applied / Opt. Express | M | P2 |
| NL-10 | Microscopic Kerr, Bloch-gain lineshape and LEF design maps for ring-QCL solitons | Nonlinear | Bloch lineshape "not well understood"; DM can get the LEF sign wrong | k-resolved DM with counter-rotating terms, validated against published NEGF | Ext (transport DM) | No | Incumbent (TU Wien, ETH, Harvard) | PRL / PRB | L | P3 |
| NL-11 | Polariton–LO-phonon stimulated scattering design maps toward ISB polariton lasing | Nonlinear | Rate "extremely low"; no broad design-space study | Hopfield coefficients × Fröhlich rates over well and cavity parameters | Full / light Ext | No | Partial (Colombelli/Carusotto custom model) | PR Applied | M | P2 |
| NL-12 | Materials-specific Rydberg-like ISB polariton blockade (Oliveira–Ciuti mechanism) | Nonlinear | Proposal is model-level; no U/γ estimate for real wells | Bound-to-continuum oscillator strengths, Bohr radius, U/γ for InGaAs, GaAs and InAs/AlSb in patch cavities | Ext (discretised continuum) | No | NF; originators may follow up | PRB / PRL | M | P2 (time-sensitive) |
| NL-13 | Squeezed light from QCLs with sub-shot-noise pumping: cascade Langevin model | Nonlinear | Excess noise and detector mismatch block quantum QCL light | Multilevel rate equations + Langevin noise; compare published data | Ext | No | Partial (Grillot ICL models) | PR Applied / Opt. Express | M | P3 |
| NL-14 | Near-IR transfer of sign-reversal QPM: InAs/AlSb and GaN/AlN coupled wells, including low-Isat designs | Nonlinear / Materials | GaN Isat 9.6 vs 3.9 W/µm² theory; claimed 30× reduction undemonstrated; InAs/AlSb triple well unexplored | Reparameterisation; nitride polarisation fields; Isat and QPM efficiency | Ext (parameters, sheet charge) | No | Partial (older nitride simulations) | Opt. Express / JAP | M | P2 |
| NL-15 | Bias-switchable interband χ(2) sign in mirror-symmetric coupled wells for electrically poled 1550→775 nm QPM | Nonlinear | Bank/Khurgin designs are fixed-asymmetric (2750 pm/V); no switchable-sign interband scheme found | Multiband k·p interband χ(2) with excitons | New (k·p) | No (Collab upside with Bank) | NF; Incumbent risk high | Optica / APL Photonics | L | P2 |
| NL-16 | Transmissive and all-dielectric ISB nonlinear metasurfaces | Nonlinear | Review asks for transmissive, low-loss designs | RCWA/FDTD + DM χ(2) | New | No | Partial | Nanophotonics | L | P4 |
| MS-01 | qwkit: an open, validated intersubband-optics chain in Python (with tutorial notebooks) | Methods | No open code combines depolarisation, LO rates, χ(2), saturation and waveguides | Docs, tests, validation against published spectra and lifetimes | Full | No | NF for this feature set | JOSS (short), CPC (long) | S | P1 |
| MS-02 | Differentiable, fluctuation-aware inverse design of bias-switchable heterostructures [E3 + autodiff SP + robust design + χ(2) surrogate] | Methods / Nonlinear | No autodiff SP found; ML surrogates are local and fluctuation-blind | JAX port; adjoint eigen-derivatives through nonparabolicity and self-consistency; robust objective; compare with BO and MLP | Ext (JAX port) | No | NF (BO 2020, MLP 2024, ANN 2026 bound novelty) | npj Comput. Mater. / PR Applied | M–L | P1 |
| MS-03 | Global sensitivity and UQ of QW observables to band and interface-roughness parameters | Methods | No UQ of standard parameter spreads found | Sobol / polynomial chaos on ISB energy, dipole, χ(2), LO lifetime, roughness linewidth | Full (roughness linewidth Ext) | No | NF | JAP / Semicond. Sci. Technol. | S–M | P1 (or fold into MS-02) |
| MS-04 | Cross-code benchmark and open labelled heterostructure dataset [benchmark + dataset + transport suite] | Methods | No versioned benchmark or ML dataset | Same structures across qwkit, Aestimo, kdotpy, ErwinJr2; Zenodo release | Full | No | NF | J. Comput. Electron. / Sci. Data | M | P2 |
| MS-05 | Open multisubband-plasmon solver with plasmon–LO-phonon coupling and nonparabolicity | Methods | Theory by Paris group; no open code | Dipole-representation Hamiltonian, Fröhlich coupling, multiple wells | Ext | No | Partial (Photonics 2020) | PRB / JOSS | M | P2 |
| MS-06 | Unified non-Lorentzian ISB lineshapes (many-body, inhomogeneous, nonparabolic) | Methods | Old fragments, no unified open model | Lineshape model fitted to published spectra | Ext | No | Partial | JAP / PRB | M | P3 |
| MS-07 | Reduced-order e–e scattering module for ISB density-matrix models | Methods | Most codes stop at Hartree | Hartree vs simplified NEGF-like vs Boltzmann e–e | Ext | No | Partial | J. Comput. Electron. | M | P3 |
| MS-08 | Spurious-solution-free 8/14-band k·p benchmark and decision guide | Methods | Handled ad hoc per paper | Multiple discretisations on standard structures | New (k·p) | No | Partial (piecemeal) | J. Comput. Electron. / OQE | L | P3 (prerequisite for NL-15) |
| MS-09 | Continuum-plus-disorder vs atomistic TB for InGaN QWs | Methods | Accuracy map vs TB missing | Landscape theory in 2D/3D | New | No | Partial | PRB | L | P4 |
| MS-10 | Open QCL NEGF code | Methods | No open QCL NEGF | Full NEGF | New | No | Incumbent (commercial and group codes) | — | XL | P4 (avoid) |
| SC-01 | Escape-to-device model for 80–300-period strain-balanced superlattices [device model + escape-rate theory] | Solar | ~10 mV unexplained Voc loss; 5 nm tunnel/thermionic crossover; drift-diffusion judged inadequate | SP + thermionic, tunnelling and LO-assisted escape + capture + SRH/radiative + photon recycling + drift-diffusion | Ext + New (holes, interband, drift-diffusion) | No (Collab upside: France, Sellers) | Partial (Connolly, Toprasertpong, Aeberhard NEGF) | JAP / IEEE JPV / Prog. Photovolt. | L | P2 |
| SC-02 | Hot-carrier thermalisation in type-II InAs/AlAsSb QWs with real band structure and hot-phonon kinetics [hot-carrier solar + phonon bottleneck] | Solar | Existing kinetic model is generic type-I; pathways debated | Nonparabolic type-II SP, LO/interface-phonon rates, hot-phonon non-equilibrium, overlap-limited radiative rate → Tc(P), Q | Ext (holes, type-II, phonon reabsorption) | No (Collab upside: Santos, Mishima) | NF for type-II; check Ferry/ASU, Cavassilas | PR Applied / JAP / J. Phys. D | M–L | P1 |
| SC-03 | Hot-carrier MQW limit with subband-designed energy-selective contacts | Solar | SQW contact gave Voc 0.28 V without hot-carrier operation; level needs redesign | Resonant-tunnelling transmission + detailed balance using SC-02 thermalisation coefficient | Ext (transfer matrix) | No | Partial (Conibeer, Guillemoles) | EPJ PV / Prog. Photovolt. | M | P2 |
| SC-04 | Reciprocity and ERE breakdown in MQW solar cells | Solar | Aeberhard treated bulk ultrathin cells; record QW papers report no ERE | EQE(V) and EL(V) with QCSE, η_coll(V), TE/TM emission; Rau-error map | Ext (interband, escape) | No | NF for MQW | PR Applied | M–L | P2 |
| SC-05 | Field-dependent two-step photon upconversion: escape vs tunnelling and the TM intraband step | Solar | Kobe lists optimal field and extraction balance as open; 5.1% vs 46.8% | SP + tunnelling escape + DM ISB (TM) + detailed balance; QW vs QD | Ext | No | NF | JAP / PR Applied | M | P2 |
| SC-06 | QW intermediate-band and ratchet limits with realistic ISB absorptivity (depolarisation, filling) | Solar | Limits use idealised step absorptivities despite strong filling dependence | DM ISB + Ando + self-consistent filling inside detailed balance | Ext (light) | No | Unchecked vs Imperial theses, Luque/Martí | PR Applied / Prog. Photovolt. | M | P2 (highest reuse in solar) |
| SC-07 | End-of-life radiation modelling of QW space cells | Solar | QW cells keep Jsc but retain 60% vs 72% efficiency | Poisson/drift-diffusion with fluence-dependent carrier removal and lifetime; QW placement | New (drift-diffusion) | No | NF | IEEE JPV / SEMSC | M | P3 |
| SC-08 | Inverse design of strain-balanced QW stacks for current matching (AM1.5G, AM0, EOL; III–V/Si middle cell) | Solar | No QW-stack inverse design found | SC-01 model + MS-02 optimiser | New (after SC-01) | No | NF | Solar RRL / IEEE JPV | M | P3 |
| SC-09 | Luminescent coupling in GaInP/GaAs-QW tandems | Solar | QW edge 1.351 eV below host; no QW-specific LC study | Coupling fractions and mismatch tolerance | New (simple) | No | NF | IEEE JPV | S–M | P3 |
| SC-10 | Review and open dataset: strain-balanced QW cells after 39.5% | Solar | No post-2022 review | Meta-analysis of Voc, Woc, per-well Jsc | n/a | No | NF | Prog. Photovolt. / JAP Tutorial | M | P3 |
| SC-11 | Valley-photovoltaic heterointerface theory | Solar | OU's valley PV was limited by degeneracy mismatch | Multivalley transport and interface design | New | Opt (OU MBE) | Unchecked | PR Applied | L | P3 |
| SC-12 | 2D Ruddlesden–Popper perovskites as MQW absorbers: n-dependent PV limit | Solar | SCAPS-only device papers; mature exciton theory elsewhere | Image-charge EMA + detailed balance | New | No | Unchecked (large exciton literature) | Solar RRL | M | P4 |
| TPV-01 | QW absorbers in air-bridge, high-reflectance TPV: detailed balance with Auger and photon recycling | TPV | Thin absorbers win under recycling; no 2018–2026 QW re-analysis | Interband QW absorption + Auger + reflector cavity, vs bulk 0.74/0.9 eV | Ext + New (interband, Auger) | No | NF | PR Applied / JAP | M–L | P2 |
| TPV-02 | Quantum-corrected coupled fluctuational electrodynamics + transport for QW near-field cells | TPV | Coupled FE + drift-diffusion exists for bulk only | FE + SP + capture/escape | New (FE) | No | NF | PR Applied | L | P3 |
| TPV-03 | Interband-cascade TPV: near-field, thermoradiative and negative-luminescence operation | TPV | Near-field IC-TPV and IC thermoradiative modelling not found | Per-stage current matching, recycling, Auger; absorption from Yang group or 8-band k·p | New (or borrowed absorption) | Collab (R. Q. Yang) | Partial (SPIE limit papers) | PR Applied / IEEE JPV | L | P2 |
| TPV-04 | QW vs double-heterostructure active regions for thermophotonic LEDs and electroluminescent cooling | TPV | Requirements paper omits QWs; EQE > 90–95% needed | Radiative, Auger and SRH balance, extraction, near-field QW dipole coupling | Ext + New | No | Partial (check Aalto parametric LED study) | PR Applied / SEMSC | M–L | P2 |
| TPV-05 | Temperature limits of narrowband, bias-switchable ISB thermal emitters for low-temperature TPV and TPX [TPV emitter + E7] | TPV | Noda switched 0.74→0.24 near room temperature; no 500–1000 K theory | DM + Ando + thermal subband population + LO dephasing + nonparabolicity + TM cavity; Kirchhoff emissivity into detailed balance with IC-TPV/T2SL cells | Full (+ thermal populations) | No (Opt: Yang IC cells) | NF | ACS Photonics / PR Applied | M | P1 |
| TPV-06 | Hot-carrier TPV with QW LO-phonon cooling and hot-phonon bottleneck | TPV | Nimje et al. use idealised cooling | Feed SC-02 rates into hot-carrier TPV detailed balance | Ext (after SC-02) | No | NF | PR Applied | S–M | P2 |
| TPV-07 | What limits out-of-band reflectance above 99%: free-carrier and intervalence absorption in doped layers | TPV | Ge model names FCA dominant; no general design rules | Multilayer TMM + Drude/IVBA | Ext (TMM) | No | Partial (Ge 2026 model) | SEMSC / JAP | S–M | P3 |
| TPV-08 | Zero-gap high-index-spacer TPV with QW or low-gap cells | TPV | Concept and a-Si modelling done | Conduction vs radiation trade-off | New | No | Partial | IJHMT / JQSRT | M | P4 |
| TPV-09 | Tutorial: quantum structures in thermal-photonic energy conversion | TPV | No QW-focused review | Synthesis | n/a | No | NF | JAP Tutorial / J. Photonics Energy | M | P3 |
| MAT-01 | ISB absorption, χ(2) and LO-phonon lifetimes at polar LaInO3/BaSnO3 interfaces and superlattices vs EDL-gated density | Materials | Interface studied only for transport; BaSnO3 ISB/χ(2) only at abstract or thesis level | SP with polarisation sheet charge, nonparabolic Sn-5s band, Ando, DM χ(2), Fröhlich, parameter-uncertainty bands | Ext (parameters, sheet charge, density-dependent mass) | Opt (Paik MBE; Venkatesan PLD) | NF; check Demkov and Belgrade follow-ups | PR Applied / PR Materials / APL Materials | M | P1 |
| MAT-02 | SrTiO3/LaAlO3 MQW ISB with multi-orbital masses and field- and temperature-dependent permittivity | Materials | Measured 2018; no temperature or ε(E)-resolved prediction | Per-orbital SP; nonlinear Poisson | Ext (nonlinear Poisson) | Opt (Venkatesan) | Partial (Ortmann 2018 theory) | PRB / PR Materials | M | P2 |
| MAT-03 | Self-consistent ISB and resonant χ(2) in displacement-field-gated few-layer InSe and WSe2 [gated vdW χ(2)] | Materials / Nonlinear | Experiments use infinite-well fits; no χ(2) theory found | Layer-chain/EMA SP, per-valley m_z, Ando, DM χ(2), waveguide modulator | Ext (layer chain) | No | NF (search-level) | PRB / 2D Mater. | M | P2 |
| MAT-04 | β-(AlGa)2O3/Ga2O3 wells: multi-mode polar-phonon lifetimes, lineshape, χ(2), QCL feasibility | Materials | Energies and QWIP metrics done (2020); lifetimes and χ(2) not | Multi-mode anisotropic Fröhlich sum | Ext | No | Partial | JAP / APL Materials | M | P2 |
| MAT-05 | ScAlN/GaN polarisation refit from published ISB data, plus polarisation-robust QCL and χ(2) designs | Materials | Measured polarisation rises faster than theory | Global P_sp(x) fit with UQ; robust designs | Ext (nitride parameters) | No | Incumbent (Purdue fitting own data) | APL / JAP | M | P3 |
| MAT-06 | m-plane ZnO/MgZnO THz QCL design at 8–9 THz | Materials | EL demonstrated; no laser | DM transport design | Ext (QCL transport) | No | Incumbent (Faist group) | PR Applied / JAP | L | P3 |
| MAT-07 | CdSe nanoplatelet ISB vs monolayer count: nonparabolicity and dielectric benchmark | Materials | Measured 2019; rigorous EMA fit unverified | Kane EMA + ligand barrier + image potential + Ando | Ext (light) | No | Unchecked | J. Phys. Chem. C / PRB | S | P2 |
| MAT-08 | Ge/SiGe symmetric coupled wells: bias-switched χ(2) for CMOS-compatible THz/mid-IR [E5] | Materials / Nonlinear | Ge has no bulk χ(2); EL shown 2021; no switchable-χ(2) design checked | L-valley SP + deformation-potential and intervalley scattering | New (scattering) | No | Unchecked | PR Applied | M–L | P2 |
| MAT-09 | GeSn/SiGeSn ISB parameter-sensitivity map | Materials | Γ/L ordering and offsets uncertain | UQ across literature parameters | Ext | No | Unchecked | JAP | M | P3 |
| MAT-10 | SrVO3/SrTiO3 metallic-QW ENZ and plasmon tuning | Materials | ARPES QW states known; optics not searched | Drude/hydrodynamic with renormalised mass | New | Opt (Paik/Venkatesan) | Unchecked | ACS Photonics | M | P4 |
| MAT-11 | KTaO3, EuO, HgTe, deep-UV AlGaN valence physics, InAs/GaSb T2SL interband absorption | Materials | Need k·p or DFT beyond a 1D single-band code | — | New | — | — | — | XL | P4 (avoid without k·p) |

### Count, merges and collaboration hooks

The table holds 58 entries: 51 actionable papers plus 7 parked or avoided directions (NL-16, MS-09, MS-10, SC-12, TPV-08, MAT-10, MAT-11). Of the 51, six list an optional proposed or collaborative experiment as their primary mode (NL-03, NL-09, SC-11, TPV-03, MAT-01, MAT-02). The other 45 need no experiment, though several note a collaborative upside.

All seven earlier frontier-survey ideas survive as merged entries:
- E1 → NL-02
- E2 → NL-03
- E3 → MS-02
- E4 → NL-05
- E5 → MAT-08
- E6 → NL-04
- E7 → TPV-05

Several papers pair theory with a proposed or collaborative experiment. Each is written as a theory paper with a measurement-ready prediction section:
- **MAT-01** (Paik): unit-cell-exact BaSnO3/LaInO3 recipes and predicted Brewster-angle FTIR spectra vs gate density.
- **MAT-02** and **MAT-10** (Venkatesan): PLD SrTiO3/LaAlO3 and SrVO3.
- **TPV-03** and **TPV-05** (Rui Q. Yang): IC-TPV cells as receivers for ISB emitters.
- **SC-02**, **SC-03** and **SC-11** (OU MBE, Santos and Mishima): hot-carrier InAs/AlAsSb and valley structures.
- **SC-01** (France and Sellers): published and unpublished MQW data.
- **NL-03** and **NL-09** (Belkin/TUM, Lee/UNIST-type metasurface groups).
- **NL-15** (Bank).

## A six-paper programme from toolkit to OU growth

### Why these six

The sequence below takes the highest-ranked papers that can start with qwkit as it stands. Each builds a module or result the next one needs. N1 sits in front: clear its parked checks and submit it, ideally folding NL-01's tolerance analysis in as a robustness section.

| Order | ID | Paper | Why it sits here | qwkit reuse | Approx. months (solo, overlapping) | Venue | OU or external hook |
|---|---|---|---|---|---|---|---|
| 0 | N1 (+NL-01) | Bias-polarity sign-reversal QPM with mirror-symmetric triple wells | Complete; needs the prior-art checks below | Full | 0–2 | As planned | — |
| 1 | MS-01 | qwkit software paper | Makes every later paper reproducible and citable; low effort, fast review | Full | 0–3 | JOSS | — |
| 2 | NL-02 | Saturation-limited efficiency and contrast bounds, waveguide and metasurface | Direct sequel to N1's saturation-aware comparison; reuses every module; answers the review's two-level gap | Full | 2–7 | PR Applied / Optica | Belkin/Lee-type metasurface data for comparison |
| 3 | NL-05 | Second-order TDHF/RPA beyond Ando | Tests whether NL-02's high-doping bounds survive collective effects; physics depth for a PRB | Ext | 6–11 | PRB | — |
| 4 | MS-02 (+MS-03) | Differentiable, fluctuation-aware inverse design of bias-switchable stacks | Uses NL-02 and NL-05 objectives; JAX port speeds every later study; releases the dataset | Ext | 9–15 | npj Comput. Mater. / PR Applied | — |
| 5 | TPV-05 | Temperature limits of switchable ISB thermal emitters in low-temperature TPV | First energy paper with near-full reuse; bridges to IC-TPV | Full | 13–17 | ACS Photonics / PR Applied | Rui Q. Yang (optional proposed test) |
| 6 | MAT-01 | LaInO3/BaSnO3 polar-interface ISB and χ(2) | Moves the whole chain to a new material with local growth; ends in a proposed experiment | Ext | 15–21 | PR Applied / APL Materials | Paik (MBE), Venkatesan (PLD) |

### How the sequence fits together

Every step reuses the same validated chain, so the cumulative investment stays near one codebase. The programme reads as one argument:
- **Tool:** an open tool (1).
- **Limits:** what bias-programmable ISB nonlinear devices can ultimately do (2).
- **Physics:** whether many-body effects move those limits (3).
- **Design:** how to design stacks that reach them under real growth tolerances (4).
- **Energy:** the same physics as a thermal emitter (5).
- **Materials:** a new oxide platform grown at OU (6).

### Swap-ins

SC-02 (hot-carrier InAs/AlAsSb) is the first alternate. It is P1 on novelty and local fit, but it needs hole and type-II extensions. Run it in parallel with step 4, or let it replace step 6 if Paik's group cannot commit to BaSnO3/LaInO3 growth within the window.

The second wave, from about month 18, should build the shared interband/escape module, ideally by coupling to Solcore's interband absorption. That module unlocks the solar and TPV device cluster: SC-04, SC-05, SC-06, TPV-01 and SC-01.

Time-sensitive items can jump the queue if the originating groups go quiet: NL-12 (Oliveira–Ciuti materials estimate) and NL-15 (interband switchable χ(2)).

## Verification checks still required before each paper

### N1 and the six sequence papers

Each row lists the checks that decide go or no-go. All "not found" claims need a Scopus or Web of Science search plus forward citations of the anchor papers named.

| Paper | Prior-art checks | Inputs to gather | Go / no-go criterion |
|---|---|---|---|
| N1 | Read the full text of Yu et al., Sci. Adv. 11, eadw8852 (2025): does it reverse the χ(2) sign by bias, and is it propagation QPM or local metasurface phase? Cite Park et al., LSA 13, 169 (2024) for electrically written phase gratings. Restate the US 4,880,297 / US 5,289,309 differentiation. Cite CLEO 2024 CW THz DFG if THz is discussed. | Interdiffusion and ±1 ML tolerance runs (NL-01) for a robustness section | Go if Sci. Adv. 2025 is local phase control, not waveguide QPM with a triple-well design; otherwise reframe novelty around saturation-aware efficiency |
| MS-01 | JOSS scope and "substantial scholarly effort" criteria; overlap with Aestimo, ErwinJr2, kdotpy feature sets | Public repository, test suite, documentation, validation cases against published spectra and LO lifetimes | Go if the integrated depolarisation → χ(2) → waveguide chain is demonstrably absent from existing codes |
| NL-02 | Forward citations of Krakofsky 2025 and Mann et al. Optica 2021; arXiv 2403.15911 full text; any 2025–2026 multilevel saturation-bound paper | Published metasurface saturation curves (ΔR vs intensity) and waveguide SHG data for validation | Go unless a multilevel, nonparabolic bound paper already exists |
| NL-05 | Rosencher/Bois-era χ(2) many-body papers; forward citations of Cominotti PRB 2023 and the Montes Bajo JAP 2023 perspective | High-doping χ(2) or SHG spectra to show where Ando-level DM fails | Go if no second-order TDHF/RPA ISB treatment with a depolarisation-detuning result exists |
| MS-02 | Forward citations of the BO-NEGF 2020, MLP 2024 and Stojković 2026 papers; search "differentiable Schrödinger–Poisson", "JAX heterostructure", "adjoint eigenvalue quantum well" | Benchmark targets from those papers to compare on identical objectives | Go unless an autodiff SP heterostructure optimiser is published |
| TPV-05 | Noda-group 2015–2026 follow-ups; GaN/AlGaN ISB emitters; "intersubband" + "thermophotovoltaic"; thermal-emission reviews | Noda 2014 device structure for validation; IC-TPV and T2SL cell EQE (Yang group, Montpellier) | Go if no theory of high-temperature ISB emitter linewidth and switching contrast exists |
| MAT-01 | Google Scholar: "Li Demkov BaSnO3 nonlinear" (2022–2026), "Stanojević BaSnO3 Optical and Quantum Electronics", "LaInO3 BaSnO3 intersubband"; PARADIM 2024–2026 stannate superlattices | BaSnO3 and LaInO3 ε∞, ε0, LO energies; density-dependent BaSnO3 mass; LaInO3 bound charge; growth-realistic thicknesses from Paik | Go if no peer-reviewed BaSnO3-QW χ(2) paper with nonparabolicity and phonons exists and Paik confirms the structures are growable |

### Remaining P1 and P2 papers

The other P1/P2 papers need lighter but specific checks before work starts:
- **SC-02:** search for NEGF or Boltzmann InAs/AlAsSb models by Ferry (ASU) and Cavassilas (Marseille), and for forward citations of Makhfudz 2022. Extract the measured thermalisation coefficients from the OU papers' full text.
- **SC-01:** read the Joule 2022 and Ahmed 2025 full texts for fitted escape and recombination rates. Search forward citations of France 2022.
- **SC-04:** check forward citations of Aeberhard PRL 2017 for MQW extensions. Search for a Sugiyama-group QFLS/EL analysis after 2018.
- **SC-05:** look for Kobe 2023–2026 TPU follow-ups beyond the JSAP 2024 abstracts.
- **SC-06:** check the Imperial QW-IB and photon-ratchet theses and the Luque/Martí reviews.
- **SC-03:** read the full Boyer-Richard 2024 design parameters.
- **TPV-01:** search "quantum well" + "air-bridge" TPV.
- **TPV-03:** confirm Rui Q. Yang's 2022–2026 IC-TPV publications and whether the group will share absorption spectra.
- **TPV-04:** read the Aalto "parametric study of highly-efficient LEDs for thermophotonic cooling".
- **TPV-06:** search forward citations of Nimje 2023.
- **NL-03:** check QCL intracavity DFG theory and the CLEO 2024 journal follow-up.
- **NL-04:** search "intersubband spontaneous parametric down-conversion".
- **NL-06:** check time-modulated ISB metasurfaces after Taravati 2024.
- **NL-08:** check the Sirtori-group modulator papers' bandwidth analyses.
- **NL-09:** read the HZDR two-photon QWIP papers.
- **NL-11:** check Colombelli/Carusotto design work after Goulain 2025.
- **NL-12:** check Ciuti-group follow-ups to arXiv 2510.24421.
- **NL-14:** look for InAs/AlSb or GaN/AlN coupled-well QPM proposals.
- **NL-15:** check the latest Bank/Khurgin and Capasso 2026 outputs.
- **MS-03:** search "uncertainty quantification" + "k·p" + "intersubband" in Scopus.
- **MS-04:** check JOSS/Zenodo for existing heterostructure benchmarks.
- **MS-05:** confirm no open multisubband-plasmon code exists from the Paris group.
- **MAT-02:** read the Ortmann 2018 full text for its theory model.
- **MAT-03:** search "second harmonic intersubband InSe few-layer theory".
- **MAT-04:** search Ga2O3 QW LO-phonon lifetime and χ(2) papers from 2021–2026.
- **MAT-07:** check Diroll 2019 follow-ups for nonparabolic EMA fits.
- **MAT-08:** search Ge/SiGe ISB χ(2)/DFG prior art.

P3 and P4 entries need the same database search, plus a competitor scan, only if promoted.

## Conclusion

The mapping changes one strategic premise. The researcher's comparative advantage is intersubband physics carried from microscopic rates all the way to propagation, not quantum wells in general. The fields with the biggest headline numbers, 39.5% solar and 44% TPV, are where qwkit currently reaches least. The places where theory clearly lags experiment are polaritonic metasurfaces, switchable thermal emitters and oxide or vdW wells with only phenomenological fits. These are where qwkit already reaches furthest, and where a solo theorist can publish fastest with the least competition.

The six-paper sequence turns that advantage into a body of work that ends in OU growth proposals. Building one shared interband module in year two then turns the energy threads from expensive one-offs into a cluster of four or five papers. They would share code, validation data and OU experimental partners: Santos/Mishima, Yang and Paik. The main risk is not running out of ideas but being scooped on a few time-sensitive ones. Four groups are working close to these threads: Belkin/Lee on electrical χ(2) control, Ciuti on ISB blockade, Bank/Khurgin on interband χ(2), and Purdue on ScAlN. So the database checks above should run before each start date, not after.
