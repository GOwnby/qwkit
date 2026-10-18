# Emerging material platforms for quantum wells and quantum-confined heterostructures (2018–Oct 2026): state of the art, open problems, and computation-only paper opportunities for a 1D Schrödinger–Poisson / density-matrix toolkit

Scope note for the report writer. About 50 search and fetch calls were used. Where only a search-result title or a conference abstract was seen, the item is labeled **[title-level]** or **[abstract-level]**. Items in "Inferences" marked **[background knowledge, not verified this session]** come from prior knowledge and need checking before they are cited. The researcher's toolkit (1D Schrödinger–Poisson with nonparabolicity, depolarization, LO-phonon rates, density-matrix optics, waveguide modes, coupled-mode propagation) is called "the toolkit" below.

## Q1. Complex-oxide quantum wells and 2DEGs (SrTiO3/LaAlO3, BaSnO3/LaInO3 and other stannates, KTaO3, SrVO3/SrTiO3, EuO, Ga2O3 alloys): what is measured, what is predicted, what is open?

### Takeaway
Oxide intersubband (ISB) optics is a small field with few experiments. The one firm result is room-temperature ISB absorption in SrTiO3/LaAlO3 multiple QWs (Ortmann, Demkov, Belkin et al., ACS Nano 2018), reaching toward 1.55 µm across a ~2.4 eV conduction-band offset. BaSnO3 QWs have been proposed and modeled for near-IR-to-visible ISB and "giant" χ(2) (Demkov group; Belgrade group), but these exist mostly as conference abstracts and a thesis. The polar LaInO3/BaSnO3 interface (2DEG, ~1.6 eV offset, mobility >2000 cm²/V·s at 10 K, MBE BaSnO3 from the Schlom lineage that Paik belongs to) has been studied only for transport. Nobody appears to have treated it as an optical quantum well. That is the clearest computation-only opening tied to a local growth capability.

### Cited Findings
**SrTiO3/LaAlO3 (STO/LAO) QWs, measured**
- Ortmann, Nookala, He, Gao, Lin, Posadas, Borisevich, Belkin, Demkov, "Quantum confinement in oxide heterostructures: Room-temperature intersubband absorption in SrTiO3/LaAlO3 multiple quantum wells," *ACS Nano* 12(8), 7682–7689 (2018), doi:10.1021/acsnano.8b01293. Room-temperature ISB absorption "on the order of hundreds of meV," approaching 1.55 µm, and tunable by changing STO well width by a single unit cell. The paper cites a "giant 2.4 eV conduction band offset," includes theory reported to agree with experiment, and uses STEM/EELS for structure. — [ORNL record](https://impact.ornl.gov/en/publications/quantum-confinement-in-oxide-heterostructures-room-temperature-in/)
- Related STO/LAO QW talks, **[title-level]**: "Optical and Electrical Control of Confined Electrons in SrTiO3/LaAlO3 Quantum Well Heterostructures" (APS March Meeting 2018) — [APS](https://meetings-archive.aps.org/mar/2018/a13/3). "Quantum confinement in transition metal oxide quantum wells" (ORNL record) — [ORNL](https://impact.ornl.gov/en/publications/quantum-confinement-in-transition-metal-oxide-quantum-wells/). "Optical properties of transition metal oxide quantum wells" (APS 2015) — [APS mirror](https://https-meetings--archive-aps-org-443.webvpn1.xju.edu.cn/mar/2015/q13/5/)
- The UT-Austin thesis (below) states the problem with STO: its "large effective mass" (4.2 m_e used in its solver) gives small subband spacing, and the STO/LAO offset is about 2.3 eV. — [Jang MA thesis, UT Austin 2023](https://fileserver-az.core.ac.uk/download/604297958.pdf)

**BaSnO3 QWs, mostly predicted**
- Jang, Li, Demkov, Posadas (UT Austin) with Zollner and Hettige (NMSU), "Near infrared to visible intersubband transitions in all-oxide quantum wells using BaSnO3," APS March Meeting 2023 **[abstract-level]**. Gives BaSnO3 m* ≈ 0.2 m_e, gap ≈ 3.1 eV, mobility ≈ 150 cm²/V·s. Al2O3/BaSnO3 multi-QWs proved hard to grow, so the group moved to MgO barriers. — [APS abstract](https://meetings-archive.aps.org/mar/2023/yy07/4)
- The underlying MA thesis (Suyeong Jang, UT Austin, Dec 2023; advisors Demkov and Lai) gives the following.
  - Structure: Al2O3/STO/BSO/Al2O3 grown by MBE on STO.
  - Simulated ISB (Poisson–Schrödinger): a 3 u.c. BSO well has four bound states, with E12 reaching the yellow visible. A 10 u.c. well has nine states.
  - Parameters: m*(BSO) ≈ 0.19 m0, m*(STO) 4.2 m_e, m*(Al2O3) 0.4 m_e. CBO(BSO/STO) = 0.49 eV (XPS). CBO(BSO/Al2O3) ≈ 3.5 eV.
  - Measurements: no ISB absorption was measured. Only Tauc-gap blue shifts were seen: 3.69 eV (10 u.c.), 3.80 eV (6 u.c.), 3.87 eV (3 u.c.).
  - Stated gaps: nonparabolicity, phonons and χ(2) are not treated. m* may change with doping and strain. The top Al2O3 barrier is amorphous.
  - The thesis is internally inconsistent about well thicknesses.
  — [thesis PDF](https://fileserver-az.core.ac.uk/download/604297958.pdf)
- Li, Demkov (UT Austin) and Hamze (Samsung), "Tunable giant non-linear optical susceptibility in BaSnO3 quantum wells," APS 2022 **[abstract-level]**. Combines mesoscopic and microscopic simulations. The abstract gives no numerical χ values. — [APS abstract](https://meetings-archive.aps.org/mar/2022/g71/8)
- "Design of wide bandgap Al2O3/BaSnO3 quantum well," APS 2022 **[title-level]** — [APS](https://meetings-archive.aps.org/mar/2022/g71/9)
- Stanojević, Radovanović, Vuković (Univ. Belgrade), "Calculation of intersubband absorption in n-doped BaSnO3 quantum wells," NUSOD 2022 **[abstract-level]**. Studies BaO/BaSnO3 QWs (La-doped) and tunes ISB with well width and applied field. The excerpt gives no numbers. — [NUSOD 2022](https://nusod2022.polito.it/?p=16002)

**LaInO3/BaSnO3 polar interface (Schlom/Char; DFT by Draxl)**
- Lee, Cho, Park, Kim, Schlom, Char, "Observation of Mobility Above 2000 cm²/V s in 2DEG at LaInO3/BaSnO3 Interface by Electric-Double-Layer Gating," *Adv. Electron. Mater.* (2024), 2400811, doi:10.1002/aelm.202400811.
  - Growth: 110 nm BaSnO3 by adsorption-controlled MBE on MgO, plus 5 nm LaInO3 by PLD.
  - Mobility: ~2100 cm²/V·s at 10 K and 1262 at 150 K.
  - Sheet density: up to ~10¹⁴ cm⁻² under gating. The paper's figures are internally inconsistent: 6.5–7.0×10¹³ at 2 K and 8 V.
  - CBO(BSO/LIO): ~1.6 eV (cited).
  - Confinement length: ~1–2 nm, from earlier Poisson–Schrödinger work.
  - No optical or ISB measurements. — [Schlom group PDF](https://schlom.mse.cornell.edu/sites/default/files/research%20pdfs/Adv%20Elect%20Materials%20-%202024%20-%20Lee%20-%20Observation%20of%20Mobility%20Above%202000%20cm2%20V%20s%20in%202DEG%20at%20LaInO3%20BaSnO3%20Interface%20by_0.pdf)
- Aggoune & Draxl, "Tuning two-dimensional electron (hole) gases at LaInO3/BaSnO3 interfaces: Impact of polar distortions, termination, and thickness," *npj Comput. Mater.* (DOI 10.1038/s41524-021-00646-x; the journal name is inferred from the DOI). DFT plus many-body theory.
  - The 2DEG sits in the dispersive Sn-5s conduction band.
  - A 2D hole gas of O-p character localizes in LaInO3.
  - The 2DEG density reaches 0.5 e per unit-cell area as polar distortions decay with LaInO3 thickness.
  - Octahedral tilts create a depolarization field that changes the critical thickness. — [arXiv 2103.07216](https://arxiv.org/abs/2103.07216)
- "2DEG state at LaInO3/BaSnO3 interface" (APS 2019) **[title-level]** — [APS](https://meetings-archive.aps.org/mar/2019/e45/3)

**Hanjong Paik (OU)**
- Assistant Professor, OU ECE, since 2022.
- Previously at Cornell: postdoc and research associate with van Dover and Schlom, then PARADIM research staff scientist from 2017.
- Techniques: reactive MBE, PLD, sputtering. Materials: oxides, nitrides, alloys, with a focus on "materials-by-design" perovskite oxides.
— [OU faculty page](https://ou.edu/coe/ece/people/faculty/hanjong-paik)

**SrVO3/SrTiO3 metallic QWs**
- ARPES on metallic quantum-well states in SrVO3 ultrathin films (KEK / U. Tokyo, Yoshimatsu/Kobayashi lineage) **[title-level]**:
  - "Origin of the anomalous mass renormalization in metallic quantum well states of correlated oxide SrVO3" — [arXiv 1409.3625](https://ar5iv.arxiv.org/html/1409.3625)
  - "Emergence of quantum critical behavior in metallic quantum-well states of strongly correlated oxides" — [arXiv 1706.02433](https://ar5iv.arxiv.org/html/1706.02433)
  - KEK 2023 highlight — [KEK PF 2023](https://www2.kek.jp/imss/pf/science/publ/pfhl/2023/23hl1_2.pdf)

**KTaO3**
- Subband structure of a 2DEG at the polar surface of KTaO3, measured by ARPES (2012) **[title-level]** — [arXiv 1111.2782](https://pdf.arxiv.org/pdf/1111.2782); [St Andrews record](https://research-portal.st-andrews.ac.uk/en/publications/subband-structure-of-a-two-dimensional-electron-gas-formed-at-the/)
- 2021 discovery of 2D superconductivity at KTaO3 (111) interfaces (EuO/KTaO3 and LaAlO3/KTaO3), reported as forming at higher temperature than earlier oxide-interface superconductors **[title-level, news]** — [phys.org Feb 2021](https://phys.org/news/2021-02-two-dimensional-superconductivity-anisotropic-potassium-tantalate.html)
- "Superfluid stiffness of a KTaO3-based two-dimensional electron gas" **[title-level]** — [arXiv 2204.09094](https://arxiv.org/pdf/2204.09094)
- No KTaO3 ISB-optics paper turned up in these searches.

**Oxide IR photonics (phonon polaritons rather than ISB)**
- Xu, Crassee, …, Hwang, Kuzmenko, Liu, "Highly confined epsilon-near-zero and surface phonon polaritons in SrTiO3 membranes" (arXiv 2403.08500, 2024; a PMC version exists).
  - Sample: 100 nm freestanding STO membrane, studied by FTIR and synchrotron near-field nanospectroscopy (SINS).
  - Symmetric/antisymmetric mode splitting produces ENZ and Berreman modes.
  - Surface phonon polaritons are about 10× more confined than in bulk.
  — [arXiv](https://arxiv.org/abs/2403.08500); [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11150425/)

**Ga2O3 / (AlGa)2O3 QWs (oxide or ultra-wide-gap)**
- Lyman & Krishnamoorthy, "Theoretical Investigation of Optical Intersubband Transitions and Infrared Photodetection in β-(AlxGa1-x)2O3/Ga2O3 Quantum Well Structures," doi:10.1063/5.0001917 (AIP journal; exact title not confirmed).
  - Method: a first-principles design-space map.
  - Range: ISB from ~1–3 µm out to >30 µm.
  - Prediction: room-temperature QWIP detectivity ~10¹¹ Jones at 1.55 µm.
  - This is a direct precedent for a computation-only oxide ISB paper. — [arXiv 2001.07299](https://arxiv.org/abs/2001.07299v2)

### Inferences
- **Precedent.** Computation-only oxide ISB papers are publishable. Lyman & Krishnamoorthy (AIP, 2020) is a pure-theory ISB/QWIP design paper on an emerging oxide.
- **The BaSnO3 niche is "claimed but not closed."** The Demkov group has an MA thesis and APS abstracts, and the Belgrade group a NUSOD abstract. In these searches I found no peer-reviewed full paper on BaSnO3 QW ISB or χ(2) with nonparabolicity, depolarization and LO-phonon linewidths. Before committing, search Google Scholar for "Li, Demkov, BaSnO3 nonlinear" (2022–2025) and "Stanojević BaSnO3 Optical and Quantum Electronics."
- **LaInO3/BaSnO3 as a "polar oxide nitride."** The LaInO3/BaSnO3 interface has a polarization discontinuity, a ~1.6 eV CBO, a 1–2 nm confined 2DEG, a light Sn-5s mass and gateable density up to ~10¹⁴ cm⁻². That parallels the GaN/AlGaN polarization-field toolkit.
  - The polar field makes the confining potential intrinsically asymmetric, so χ(2) for ISB difference-frequency and second-harmonic generation (DFG/SHG) is nonzero without compositional stepping.
  - Opportunity 1 below builds on this.
  - I found no paper on ISB absorption, χ(2), or electrically tunable (EDL-gated) ISB at this interface.
  - The toolkit can do it: 1D SP with a sheet polarization charge, nonparabolic Sn-5s band, depolarization shift, and density-matrix χ(2).
- **Hard parameter problems for oxide QWs.** These are where a careful 1D paper adds value.
  - *(a) STO permittivity.* STO's static permittivity depends on field and temperature (≈300 at room temperature, rising to ~10⁴ at low T) **[background knowledge, not verified this session]**. A Poisson solver with ε(E,T) is required, which ordinary III-V codes lack.
  - *(b) Orbital anisotropy.* STO t2g orbitals give anisotropic masses. dxy is light in-plane and heavy along z; dxz/dyz are heavy in one in-plane direction and light along z **[background]**. ISB selection rules and the z-mass differ per orbital, so a 1D EMA code can run one Schrödinger problem per orbital with its own m_z.
  - *(c) BaSnO3 nonparabolicity.* Reported BSO m* ranges ~0.19–0.4 m0 and increases with carrier density **[background]**. The thesis flags this as an uncertainty.
  - *(d) Polar phonons.* Polar LO phonons in perovskites are strong, and some modes are soft (STO). Fröhlich coupling is large and polaron mass renormalization is relevant. LO-phonon ISB lifetimes in oxide QWs appear uncomputed.
- **Natural experimental partners.**
  - *Paik:* his adsorption-controlled BaSnO3 MBE (PARADIM/Schlom lineage) plus OU's MBE/PLD tools match BaSnO3/LaInO3 and BaSnO3/SrTiO3 superlattices, so a theory paper that specifies growth-realistic structures (unit-cell thicknesses, La doping) is a natural seed.
  - *Venkatesan:* PLD complex oxides and his history in LaAlO3/SrTiO3 interfaces and SrTiO3 electronics **[background, not verified this session]** match STO/LAO and SrVO3 work.
- **SrVO3 / KTaO3 / EuO.**
  - SrVO3 QWs are correlated metals (mass renormalization ~2–3×; ARPES QW states). Their optical response is ENZ/plasmonic rather than classic ISB. A 1D EMA model is a crude approximation, and DMFT-level inputs would need to be borrowed from the literature.
  - KTaO3 has strong 5d spin–orbit coupling. Its J=3/2 bands need multiband k·p for credible ISB selection rules, which is beyond a single-band 1D code without extension.
  - EuO (ferromagnetic semiconductor with an exchange-split conduction band) would allow spin-polarized ISB **[background]**. Nothing was searched or found in this session.

### Gaps
- Exact ISB energies and well widths in Ortmann 2018 (the ACS Nano full text was not retrieved), and the theory they used (single-band vs multi-orbital).
- Whether the Demkov-group BaSnO3 χ(2) and ISB work appeared as peer-reviewed papers (2022–2026), and with what χ(2) values. The Belgrade NUSOD work may have become an *Opt. Quantum Electron.* paper; not verified.
- No source found for KTaO3, EuO or SrVO3 ISB or mid-IR plasmonic QW optics, or for BaSnO3 LO-phonon energies, ε∞ or ε0 values. These must come from the literature before any calculation.
- Thomas Venkatesan's current OU research focus was not searched, so the collaboration link is inferred only.
- No search covered PARADIM publication lists 2024–2026 for new stannate superlattices (e.g., SrSnO3, BaSnO3/SrSnO3).

## Q2. III-nitrides (GaN/AlN, ScAlN/GaN, AlGaN; polarization fields; near-IR ISB; UV LEDs; InGaN QW solar cells)

### Takeaway
GaN/AlN near-IR ISB at 1.55 µm is mature and now used in nonlinear metasurfaces. Lattice-matched Sc0.14Al0.86N/GaN QWs are a new (2024–2025) ISB platform whose polarization constants are uncertain. Measured net polarization rises faster with Sc than theory predicts, which is a clean computational inverse problem. Deep-UV AlGaN QWs are limited by p-doping, TM emission (valence-band reordering) and degradation, and some of these problems need 6-band k·p, which the toolkit lacks. A GaN THz QCL, which would cover the 5–12 THz GaAs reststrahlen gap, has still not been demonstrated.

### Cited Findings
- **ScAlN/GaN.** Abdin, Gopakumar, Kumar, Manfra, Malis (Purdue), "Enhanced Near-Infrared Absorption in Lattice-Matched Sc0.14Al0.86N/GaN Multi-Quantum Wells: Growth Optimization and Insights into Polarization Parameters" (APS March 2025) **[abstract-level]**.
  - Structures: strain-free MBE MQWs on c-plane GaN.
  - ISB: 515–709 meV as well width shrinks from 7 to 1.5 nm.
  - Growth: above 600 °C, interface roughness red-shifts the narrowest wells.
  - Polarization: "net polarization increases with Sc composition faster than previous theoretical predictions." — [APS abstract](https://meetings-archive.aps.org/smt/2025/mar-q39/6/); related outputs [NSF PAR (Malis)](https://par.nsf.gov/search/author:%22Malis,%20Oana%22), [NSF PAR 10594000](https://par.nsf.gov/biblio/10594000)
- **GaN/AlN nonlinear metasurface.** Mundry, Spreyer, Jmerik, Ivanov, Zentgraf, Betz, "A nonlinear metasurface combining telecom-range intersubband transitions in GaN/AlN quantum wells with resonant plasmonic antenna arrays" (arXiv 2105.09726, 2021). Shows SHG at normal incidence from ISB plus antennas; the antennas alone give no SHG. — [arXiv](https://www.arxiv.org/abs/2105.09726)
- **Cubic GaN/AlN.** "Linear and nonlinear behaviour of near-IR intersubband transitions of cubic GaN/AlN multi quantum well structures" (Paderborn; polarization-free zinc-blende nitrides) **[title-level]** — [Paderborn record](https://ris.uni-paderborn.de/record/4810)
- **GaN THz QCL.** Design and Monte Carlo literature exists, e.g., "Recent progress toward realizing GaN-based THz quantum cascade laser" (SPIE 8993) **[title-level]** — [SPIE](https://spiedigitallibrary.org/conference-proceedings-of-spie/8993/89930G/Recent-progress-toward-realizing-GaN-based-THz-quantum-cascade-laser/10.1117/12.2039214.full); Paiella-group Monte Carlo (JAP 2009) **[title-level]** — [BU PDF](https://www.bu.edu/paiella/files/2021/08/JAP_Monte_Carlo_2009.pdf); a 2025 PMC article on GaN/AlGaN THz QCLs **[title-level; not retrieved, captcha]** — [PMC12371103](https://pmc.ncbi.nlm.nih.gov/articles/PMC12371103/)
- **Deep-UV AlGaN/AlN QWs.** D. Jena, "Deep-UV photonic devices enabled by distributed polarization doping," *Proc. SPIE* 13896, 1389602 (2026), plenary, doi:10.1117/12.3095300.
  - Active regions: QWs a few nm thick with 50–100% Al.
  - Lasers: electrically injected deep-UV LDs since 2019, down to ~270 nm (271.8 nm cited).
  - Valence band: above ~60% Al the crystal-field band rises to the top, giving TM, in-plane emission that is hard to extract from LEDs.
  - Dopants: Mg is ~180 meV deep in GaN and too deep in AlN; Si is ~250 meV deep in AlN; n-AlGaN works up to ~80% Al.
  - Polarization doping: graded layers give p/n doping via polarization (DPD) plus graded-index optical confinement.
  - Open problems: shallow AlN acceptors, DPD design, laser-diode and far-UVC LED degradation, light extraction, and 3D hole gases. — [Jena 2026 PDF](https://djena.engineering.cornell.edu/papers-new/2026/jena2026deep.pdf)
- **InGaN QW solar cells.** Literature found at title level only:
  - "Polarization Boosts GaN/InGaN Solar Cell Performance" **[title-level, trade press]** — [Compound Semiconductor](https://compoundsemiconductor.net/article/87169/Polarization_Boosts_GaN_InGaN_Solar_Cell_Performance)
  - The EU SOLARIN project report (Valdueza-Felip) **[title-level]** — [CORDIS PDF](https://cordis.europa.eu/docs/results/331/331745/final1-s-valdueza-felip-final-summary-report-solarin.pdf)
  - arXiv 2202.03510 **[title-level, content not checked]** — [arXiv](https://arxiv.org/pdf/2202.03510)

### Inferences
- **ScAlN/GaN inverse problem.** Fitting spontaneous plus piezoelectric polarization of ScAlN from published ISB energies vs well width is a pure SP-plus-nonparabolicity problem. The method: self-consistent depolarization, then ISB peak positions, then a global fit of P_sp(x).
  - The Purdue team is doing this themselves, so novelty depends on adding something they have not: data from several groups, an uncertainty analysis, or the consequences for χ(2) and THz QCL designs in ScAlN.
  - Risk: moderate, because it may be scooped by the experimental group.
- **High-novelty nitride target.** The most novel nitride target for a 1D toolkit is ScAlN/GaN or ScAlN/AlGaN lattice-matched THz and mid-IR QCL and χ(2) design.
  - Lattice matching removes strain-relaxation limits, while the large and uncertain polarization drives asymmetry.
  - A sensitivity study across the published range of polarization constants (a design that is "robust to polarization uncertainty") would be new as far as these searches show.
  - It needs no experiment. Venues: JAP, Phys. Rev. Applied.
- **Deep-UV LED problems are mostly outside the toolkit.** Valence-band ordering and TE/TM ratio need 6×6 k·p with strain. The toolkit could still address polarization-graded DPD layers with 1D Poisson, but Jena's group has covered this heavily, so novelty is low.
- **InGaN QW PV.** Open problems (phase separation, polarization fields reducing carrier extraction, indium-rich wells) are well trodden. A detailed-balance study of polarization-field QW absorption and escape is feasible but low novelty unless paired with a new concept, e.g., N-polar or ScAlN barriers. **[Inference; not checked against 2023–2026 literature]**
- **Parameter uncertainty matters.** GaN/AlN parameters (LO phonon ~90 meV, m* ~0.2 m0, CBO ~1.75–2 eV) are reasonably known **[background]**. ScAlN's m*, CBO and polarization are the uncertain inputs.

### Gaps
- No quantitative published value (in the sources seen) for the "faster than predicted" Sc-dependence of polarization.
- No direct 2023–2026 review on InGaN QW solar cells was retrieved, so the open problems listed are inference.
- Status of GaN THz QCL experiments in 2024–2026 was not verified (PMC article blocked).

## Q3. Group IV (Ge/SiGe, GeSn, Si/SiGe ISB and interband QWs; CMOS photonics)

### Takeaway
n-type Ge/SiGe L-valley quantum cascade structures gave the first group-IV THz intersubband electroluminescence (3.4 and 4.9 THz, 2021). A laser has not yet been reported in the sources found. Because Ge and Si are nonpolar, there is no Fröhlich LO-phonon scattering. Lifetimes are set by deformation-potential, intervalley and interface-roughness scattering, so the toolkit's LO-phonon module must be replaced, not reused. GeSn/SiGeSn ISB is mostly at the theory and early-growth stage.

### Cited Findings
- Stark, Mirza, Persichetti, Montanari, Markmann, Beck, Grange, Birner, Virgilio, Ciano, Ortolani, Corley, Capellini, Di Gaspare, De Seta, Paul, Faist, Scalari, "THz intersubband electroluminescence from n-type Ge/SiGe quantum cascade structures," doi:10.1063/5.0041327 (2021; *Appl. Phys. Lett.* per DOI prefix, not confirmed).
  - Transitions: L-valley, in Ge/Si0.15Ge0.85 grown by UHV-CVD on Si.
  - Emission: EL at 3.4 and 4.9 THz, with Δf/f ≈ 0.2.
  - Problem flagged: two peaks indicate "suboptimal injection." The abstract compares efficiency with an analogous GaAs device (one order of magnitude). — [arXiv 2101.05518](https://arxiv.org/abs/2101.05518v1); press [innovations-report](https://innovations-report.com/physics-and-astronomy/lights-on-for-silicon-photonics)
- Persichetti et al., "Intersubband transition engineering in the conduction band of asymmetric coupled Ge/SiGe quantum wells," *Crystals* 10, 179 (2020), DOI 10.3390/cryst10030179 (journal inferred from DOI). Twenty-module asymmetric coupled QWs, with subband energy and overlap engineered and compared with THz spectroscopy. — [arXiv 2002.05074](https://arxiv.org/abs/2002.05074)
- Si/SiGe QC emitters for THz (Paul et al.) **[title-level]** — [Glasgow eprints 202772](https://eprints.gla.ac.uk/202772); EU FLASH project results **[title-level]** — [CORDIS 766719](https://www.cordis.europa.eu/project/id/766719/results/it)
- GeSn/SiGeSn ISB **[title-level only]**: an MDPI *Electronics* 2024 paper — [MDPI 13/21/4142](https://www.mdpi.com/2079-9292/13/21/4142); NTU and Hokkaido records — [NTU](https://dr.ntu.edu.sg/server/api/core/bitstreams/aebcd60e-0ad2-45dc-8148-527492a37e5e/content), [Hokkaido](https://eprints.lib.hokudai.ac.jp/dspace/handle/2115/60344)

### Inferences
- **Fit to the toolkit.** A 1D EMA code can treat L-valley Ge QWs grown on (001), because all four L valleys share the same m_z (~0.12 m0, quantization-direction mass) **[background]**. Strain shifts and Γ/Δ valley crossings set the barrier, and nonparabolicity matters less.
  - The hard part is scattering: acoustic plus optical deformation potentials, L–Γ and L–X intervalley scattering, and interface roughness (dominant in SiGe).
  - Adding a deformation-potential optical-phonon rate (~37 meV Ge optical phonon) is a moderate code extension.
- **Ge/SiGe QCL design.** Several groups (Grange/nextnano, Virgilio, Paul) already do nonequilibrium Green's function (NEGF) and density-matrix design, so novelty is low to moderate. A potential niche is χ(2) and DFG in asymmetric Ge/SiGe coupled QWs for CMOS-compatible THz generation, since Ge lacks bulk χ(2) and ISB-resonant χ(2) is the only source. **[Not checked for prior art]**
- **GeSn.** Γ-valley wells in strained or relaxed GeSn are candidates for mid-IR ISB with a lighter mass. Parameter uncertainties are large: GeSn bowing, Γ/L ordering versus Sn content and strain, and the CBO. A 1D code needs these from k·p or DFT literature. Treat this as a parameter-sensitivity paper.

### Gaps
- No 2023–2026 Ge/SiGe QCL lasing claim was found in these searches. Status not verified.
- No peer-reviewed GeSn ISB measurement was confirmed.

## Q4. Antimonides and II–VI (InAs/AlSb, InAs/GaSb T2SL, HgTe/CdTe, ZnO/MgZnO, CdSe nanoplatelets)

### Takeaway
- **ZnO/MgZnO.** Nonpolar m-plane ZnO/MgZnO gave the first ZnO THz ISB electroluminescence (8.5 THz, inside GaAs's 8–9 THz reststrahlen gap, observed up to room temperature; ACS Photonics 2021). A ZnO THz QCL is still open.
- **CdSe nanoplatelets.** These colloidal QWs show narrow, polarized near-IR ISB absorption (900–1600 nm) with atomically defined thickness (Nat. Commun. 2019), which makes them an ideal test bed for nonparabolicity and dielectric-confinement models.
- **Antimonides and HgTe.** These are mature (short-wavelength InAs/AlSb QCLs, HgCdTe THz stimulated emission). New theory there would need a sharper angle.

### Cited Findings
- **ZnO/MgZnO.** Meng, Hinkov, Biavan, Hoang, Lefebvre, Hugues, Stark, Franckié, Torres-Pardo, Tamayo-Arriola, Bajo, Hierro, Strasser, Faist, Chauveau, "Terahertz Intersubband Electroluminescence from Nonpolar m-Plane ZnO Quantum Cascade Structures," *ACS Photonics* 8(1), 343–349 (2021), doi:10.1021/acsphotonics.0c01641.
  - Emission: EL ~8.5 THz, linewidth ~20 meV at 110 K, observed up to room temperature.
  - Context: GaAs cannot reach 8–9 THz (reststrahlen).
  - Outlook: "an important step toward the realization of ZnO-based THz quantum cascade lasers." — [UCM repository](https://docta.ucm.es/entities/publication/41aea113-9dbc-4cae-9a26-c95dc5e723b2/full); [UPM OA](https://oa.upm.es/86760)
- **CdSe nanoplatelets.** Diroll, Chen, Coropceanu, Williams, Talapin, Guyot-Sionnest, Schaller, "Polarized near-infrared intersubband absorptions in CdSe colloidal quantum wells," *Nat. Commun.* 10 (2019), doi:10.1038/s41467-019-12503-z.
  - Absorption: ISB features with widths of 30–200 meV, tunable by thickness over 900–1600 nm.
  - Carrier population: appears under photoexcitation or bias.
  - Dynamics: hot-carrier and Auger effects; two-color excitation allows sub-picosecond carrier-temperature modulation. — [RePEc record](https://ideas.repec.org/a/nat/natcom/v10y2019i1d10.1038_s41467-019-12503-z.html); [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6778118/)
- "Autler-Townes splitting and linear dichroism in colloidal CdSe nanoplatelets driven by near-infrared pulses" **[title-level]** — [Bohrium](https://bohrium.dp.tech/paper/arxiv/9810038)
- **InAs/AlSb short-wavelength QCLs** **[title-level]** — [Vilnius thesis record](https://epublications.vu.lt/object/elaba:1922893); [HAL: Quantum Cascade Lasers in the InAs/AlSb Material System](https://hal.archives-ouvertes.fr/hal-01427143); (Ga,In)As/Al(As,Sb) MQWs for ISB below 3.5 µm — [HZDR](https://www.fzd.de/publications/Publ-5303)
- **HgTe/CdTe** **[title-level]**: "Stimulated emission in HgCdTe-based quantum wells: toward continuous wave lasing in THz range" — [CyberLeninka](https://cyberleninka.ru/article/n/stimulated-emission-in-hgcdte-based-quantum-wells-toward-continuous-wave-lasing-in-thz-range); Ioffe journal item — [Ioffe](https://j.ioffe.ru/articles/viewPDF/55141)

### Inferences
- **ZnO THz QCL design.** A density-matrix design for an m-plane ZnO/MgZnO THz QCL is directly within the toolkit's scope. Required parameters, all from the literature **[background]**:
  - ZnO m* ~0.24–0.28 m0
  - LO phonon ~72 meV, with strong Fröhlich coupling
  - Mg-dependent CBO
  - nonpolar m-plane, which removes built-in fields
  The Faist group (Franckié) already models this, so novelty needs a specific angle: temperature performance limited by the large LO energy, or comparison with GaN m-plane designs.
- **CdSe NPL ISB energies.** Computing these versus monolayer number with Kane nonparabolicity, finite barriers set by ligands, and self-consistent depolarization is a clean 1D EMA problem. Experimental data already exist, so no new experiment is needed. Check whether Diroll et al. or follow-ups already did this; the abstract alone does not say. Inputs: CdSe m* ≈ 0.11–0.13 m0, E_P, ligand barrier height, dielectric mismatch **[background]**.
- **InAs/AlSb and InAs/GaSb.** Highly nonparabolic InAs (the toolkit already supports nonparabolicity) with a ~2 eV InAs/AlSb CBO **[background]** is the closest extension of the existing InGaAs/InAlAs parameterization.
  - This lowers the barrier to entry, but the field is mature: Baranov/Teissier QCLs and type-II superlattice (T2SL) detectors.
  - Type-II InAs/GaSb superlattices need 8-band k·p for interband absorption, so they are out of scope for the 1D single-band code.
- **HgTe/CdTe** (inverted bands, topological) needs 8-band k·p. Poor fit.

### Gaps
- Specific 2022–2026 InAs/AlSb or HgTe papers were not retrieved beyond titles.
- Whether CdSe NPL ISB has been modeled with nonparabolic EMA was not checked.

## Q5. 2D and layered (vdW multilayer QWs: TMDs, InSe, black phosphorus; 2025–2026 TMD ISB results; 2D Ruddlesden–Popper halide perovskites; MXenes)

### Takeaway
Few-layer vdW crystals act as atomically quantized quantum wells.
- ISB transitions were first imaged in WSe2 (s-SNOM, Nat. Nanotechnol. 2018).
- In 2024 they were gate-tuned in few-layer InSe by over 250 meV (Nano Lett.).
- In 2026 they were electrically tuned by over 100 meV in 3–7-layer WSe2 via electronic Raman scattering (ACS Nano).

Theory in these papers is phenomenological (a modified infinite well fitted to a single m_z, plus Stark-shift polynomials). That leaves room for a proper self-consistent multivalley model with depolarization and χ(2) under displacement field. Ruddlesden–Popper perovskites are well-developed "natural QWs" whose dielectric-confinement theory is mature, which makes them a weaker fit.

### Cited Findings
- Wutz, Zhang, Hofmann, Faria Junior, Lu, Soul, Bao, Watanabe, Taniguchi, Fabian, Bange, Lupton, Lin, "Electrical Control of Intersubband Transitions in Few-Layer WSe2 Multivalley Quantum Wells Probed by Electronic Raman Scattering," *ACS Nano* 20, 4018–4026 (2026), doi:10.1021/acsnano.5c08378.
  - Tuning: over 100 meV electrical tuning. In 3L WSe2 the shift exceeds 0.1 eV for a field change under 0.1 V/nm.
  - Valleys: shift magnitude ordering VB(Γ) > CB(Q) > VB(K). E0 matches Schmidt et al. 2018 within 10 meV for 4L and 5L.
  - Fitted parameters: Γ-valley m_z = 1.03 m_e from the fit versus 1.08 m_e from DFT; interlayer distance 6.477 Å.
  - Model: a modified infinite well with phenomenological ν, and E(F) = E0 − μ(F−F0) + α(F−F0)²/2.
  - Open problems: moiré effects in twisted double bilayers, nonmonotonic Raman intensity, VB(K) above 3L, near-field (sub-diffraction) extension. — [Regensburg ePub PDF](https://epub.uni-regensburg.de/78725/1/electrical-control-of-intersubband-transitions-in-few-layer-wse2-multivalley-quantum-wells-probed-by-electronic-raman.pdf); [Nature Index record](https://www.nature.com/nature-index/article/10.1021/acsnano.5c08378)
- Prior works as cited in Wutz et al. **[cited-in-paper level]**: Schmidt et al., *Nat. Nanotechnol.* 13, 1035 (2018), s-SNOM ISB in WSe2 — also [arXiv 1806.09519](https://arxiv.org/pdf/1806.09519) and [nanoGUNE news](https://www.nanogune.eu/en/nano-imaging-intersubband-transitions-few-layer-2d-materials); Zultak et al., *Nat. Commun.* 2020, few-layer InSe QWs; Saigal et al., *PRL* 2024, moiré-miniband excitations in twisted WSe2. — [Wutz PDF](https://epub.uni-regensburg.de/78725/1/electrical-control-of-intersubband-transitions-in-few-layer-wse2-multivalley-quantum-wells-probed-by-electronic-raman.pdf)
- Shcherbakov, Voigt, Memaran, Liu, Wang, Watanabe, Taniguchi, Smirnov, Balicas, Zhang, Lau, "Giant Tunability of Intersubband Transitions and Quantum Hall Quartets in Few-Layer InSe Quantum Wells" (arXiv 2312.03228; *Nano Lett.* 2024 per Wutz et al. citation). Second-subband energy is tuned by "as much as 350%," over 250 meV, via thickness and displacement field. Proposed applications: tunable IR/THz sources, detectors and modulators. — [arXiv](https://arxiv.org/abs/2312.03228v1); [MagLab PDF](https://public.magnet.fsu.edu/AToth/NSF%20publication%20access/2024/03%20Newly%20Entered%20Pubs%20March%202024/2024%20Cited/2024_Giant%20Tunability%20of%20Intersubband%20Transitions.pdf)
- Zultak et al., "Ultra-thin van der Waals crystals as semiconductor quantum wells," *Nat. Commun.* 2020 **[title-level]** — [Springer](https://link.springer.com/10.1038/s41467-019-13893-w)
- **Ruddlesden–Popper perovskites** **[title-level]**:
  - "Composite Nature of Layered Hybrid Perovskites: Assessment on Quantum and Dielectric Confinements and Band Alignment" (Even/Katan group) — [HAL 01719873](https://hal.archives-ouvertes.fr/hal-01719873)
  - LANL ACS Nano 2018 on 2D perovskite QWs — [LANL PDF](https://cnls-www.lanl.gov/~serg/postscript/acsnano.7b08202.pdf)
  - "Strongly bound excitons in Ruddlesden-Popper 2D perovskites" (APS 2018) — [APS](https://meetings-archive.aps.org/mar/2018/c37/1)
  - Photonics Research 12(3), 563 (2024) — [researching.cn](https://www.researching.cn/articles/OJ98f4015cd6ff1fe)
  - Oriented low-n formamidinium RP solar cells (2025) — [SARI CAS](https://sari.cas.cn/kycg/paper/202504/t20250424_7610564.html)
  - RP passivation layer in a 21.4% inverted cell (trade press) — [pv-magazine](https://www.pv-magazine.com/?p=31653)

### Inferences
- **High-value opportunity: a self-consistent multivalley ISB plus χ(2) model of gated few-layer InSe and WSe2.**
  - Method: a layer-resolved 1D Schrödinger–Poisson in the "quasi-continuum" EMA limit, or a 1D tight-binding chain (one site per layer, which is easy to add to a 1D code).
  - Physics: displacement-field-induced asymmetry, depolarization shift, and resonant χ(2) for SHG/DFG.
  - Prior art: the 2024 and 2026 experiments used phenomenological fits (infinite well plus μ, α). No paper computing resonant ISB χ(2) in gated few-layer InSe or WSe2 turned up in this session, though it may exist. Search "second harmonic intersubband InSe few-layer theory" before committing.
  - Inputs: m_z (WSe2 Γ ≈ 1.03–1.08 m_e; InSe m_z from DFT literature), interlayer spacing (6.477 Å for WSe2), out-of-plane permittivity ε_zz, and doping and displacement-field range.
  - Needs no experiment. Venues: PRB, Phys. Rev. Applied, 2D Materials. ACS Photonics only if device-level, e.g., a waveguide-integrated modulator using the toolkit's waveguide and coupled-mode modules.
- **Black phosphorus:** its anisotropic mass is suitable but it degrades in air. Not searched here.
- **Ruddlesden–Popper perovskites.** These are natural QWs with organic barriers, where effective-mass barriers are ill-defined. Dielectric confinement with image charges dominates, and exciton binding is hundreds of meV. Theory is mature (Even/Katan, LANL). A 1D EMA plus image-potential extension could do detailed-balance PV for RP n-series, but the payoff is low. ISB in doped RP perovskites appears unexplored (not searched specifically), but doping these materials is experimentally difficult.
- **MXenes:** metallic, not QWs in the usual sense. Not searched; low fit.

### Gaps
- Whether a resonant ISB χ(2) theory for few-layer TMDs or InSe exists (2020–2026) was not verified.
- InSe out-of-plane mass value not retrieved.
- No MXene or black-phosphorus QW sources searched.

## Q6. Ultra-wide-gap and other (Ga2O3, diamond, AlN/hBN)

### Takeaway
β-(AlGa)2O3/Ga2O3 ISB has a theory-only precedent (SWIR to far-IR, QWIP ~10¹¹ Jones predicted). AlN/AlGaN deep-UV QWs are device-relevant but k·p-limited. hBN-based QWs and hBN/GaN ISB–phonon-polariton coupling exist only at the conference or early-growth level. No diamond QW ISB source turned up.

### Cited Findings
- **Ga2O3:** Lyman & Krishnamoorthy (2020); see Q1 for details. — [arXiv 2001.07299](https://arxiv.org/abs/2001.07299v2)
- **AlGaN/AlN:** Jena 2026 (deep-UV, DPD); see Q2. — [Jena 2026](https://djena.engineering.cornell.edu/papers-new/2026/jena2026deep.pdf)
- "Investigation of intersubband-phonon polariton transitions in hBN/GaN heterostructure" (SPIE 11274, 2020) **[title-level]** — [SPIE](https://biomedicaloptics.spiedigitallibrary.org/conference-proceedings-of-spie/11274/112741A/Investigation-of-intersubband-phonon-polariton-transitions-in-hBNGaN-heterostructure/10.1117/12.2546983.full)
- "Growth and properties of hexagonal boron nitride based alloys and quantum wells" (Texas Tech, 2020) **[title-level]** — [TTU PDF](https://www.depts.ttu.edu/ece/Nanophotonics/papers\2020-Growth%20and%20properties%20of%20hexagonal%20boron%20nitride%20based%20alloys%20and%20quantum%20wells.pdf)
- APS 2024 and 2025 sessions on UWBG interfaces **[title-level]** — [APS 2024 T05](https://meetings-archive.aps.org/mar/2024/t05/); [APS 2025 Q39](https://archive.aps.org/smt/2025/mar-q39/2)

### Inferences
- **Ga2O3 follow-ups the toolkit can do.** Lyman & Krishnamoorthy treated the energies and QWIP metrics. Not done in these searches:
  - *(i) LO-phonon ISB lifetimes in Ga2O3 QWs.* β-Ga2O3 is monoclinic with many polar IR-active modes **[background]**, so lifetimes need a multi-mode Fröhlich sum, which extends the toolkit's single-LO rates.
  - *(ii) A depolarization-corrected absorption line shape.*
  - *(iii) χ(2) in step or asymmetric (AlGa)2O3 wells.*
  - *(iv) A THz/mid-IR QCL feasibility study.*
  All need no experiment. Venues: JAP, APL Materials.
  Key uncertainties: CBO versus Al content (limited Al solubility in the β phase), anisotropic m*, and ε∞/ε0 tensors **[background]**.
- **Oxide-grower link.** Ga2O3 MBE is in Paik's "oxides/nitrides" scope only by general description. Not verified.
- **Diamond, hBN/AlN.** Diamond QWs are not practical (no lattice-matched barrier); hBN QWs are early-stage. Low priority for a 1D EMA code.

### Gaps
- Whether Ga2O3 QW LO-phonon lifetime or χ(2) papers appeared in 2021–2026 was not checked.
- No diamond QW source found.

## Q7. Cross-platform synthesis: ranked computation-only paper opportunities (experiment needed? already done?), code fit, parameter inputs, venues, and links to Paik and Venkatesan

### Takeaway
The best opportunities pair three things: a material with existing experimental anchors but only phenomenological or abstract-level theory, physics the toolkit already handles (polarization or built-in fields, nonparabolicity, depolarization, LO-phonon rates, density-matrix χ(2)), and, as a bonus, OU growth capability. The top three are:
1. Polar LaInO3/BaSnO3 and BaSnO3-based QWs: ISB, χ(2) and LO-phonon lifetimes.
2. SrTiO3/LaAlO3 ISB with field- and temperature-dependent permittivity and multi-orbital masses.
3. Self-consistent ISB and χ(2) in gated few-layer InSe/WSe2.

### Cited Findings
- **Anchors for opportunity 1:** BaSnO3/LaInO3 2DEG with 1.6 eV CBO, ~2000 cm²/V·s, and EDL-gated density — [Lee et al. 2024](https://schlom.mse.cornell.edu/sites/default/files/research%20pdfs/Adv%20Elect%20Materials%20-%202024%20-%20Lee%20-%20Observation%20of%20Mobility%20Above%202000%20cm2%20V%20s%20in%202DEG%20at%20LaInO3%20BaSnO3%20Interface%20by_0.pdf); DFT polar-discontinuity physics — [Aggoune & Draxl](https://arxiv.org/abs/2103.07216); BSO QW ISB/χ(2) only at abstract or thesis level — [APS 2022](https://meetings-archive.aps.org/mar/2022/g71/8), [APS 2023](https://meetings-archive.aps.org/mar/2023/yy07/4), [NUSOD 2022](https://nusod2022.polito.it/?p=16002), [Jang thesis](https://fileserver-az.core.ac.uk/download/604297958.pdf)
- **Anchor for opportunity 2:** measured room-temperature ISB in STO/LAO — [Ortmann et al. 2018](https://impact.ornl.gov/en/publications/quantum-confinement-in-oxide-heterostructures-room-temperature-in/)
- **Anchors for opportunity 3:** [Wutz et al. 2026](https://epub.uni-regensburg.de/78725/1/electrical-control-of-intersubband-transitions-in-few-layer-wse2-multivalley-quantum-wells-probed-by-electronic-raman.pdf); [Shcherbakov et al. 2024](https://arxiv.org/abs/2312.03228v1)
- **Precedent that pure-theory emerging-oxide ISB papers publish in AIP journals:** [Lyman & Krishnamoorthy 2020](https://arxiv.org/abs/2001.07299v2)
- **OU growth capability (MBE/PLD/sputtering, PARADIM/Schlom background):** [Paik OU page](https://ou.edu/coe/ece/people/faculty/hanjong-paik)

### Inferences
Opportunity table. All rows need **no experiment**. "Done?" reflects only what these searches found; do a final Scholar check before starting.

| # | Paper idea | Done? | Code fit | Key inputs (and uncertainty) | Venue | Growth link |
|---|---|---|---|---|---|---|
| 1 | **ISB absorption, χ(2) (SHG/DFG) and LO-phonon lifetimes at the polar LaInO3/BaSnO3 interface and in BaSnO3/LaInO3 superlattices, vs EDL-gated density.** The polarization charge gives intrinsic asymmetry, like nitrides. | Not found for LIO/BSO. BSO/Al2O3, MgO, BaO ISB and χ(2) exist only at abstract or thesis level. | 1D SP + nonparabolicity + depolarization + density-matrix χ(2): fully in scope. Add a sheet polarization charge. | m*(BSO) 0.19–0.4 m0 with density-dependent nonparabolicity (uncertain); CBO BSO/LIO ~1.6 eV; LIO polarization/bound charge (from DFT, ~0.5 e/u.c. limit); ε∞, ε0 and LO energies of BSO and LIO (not found here); LIO mass. | Phys. Rev. Applied, PR Materials, APL Materials | Paik (BSO MBE); Venkatesan (PLD LIO) |
| 2 | **SrTiO3/LaAlO3 MQW ISB revisited.** Multi-orbital (dxy vs dxz/dyz m_z), field- and temperature-dependent ε(E,T) in Poisson, depolarization. Predict strong temperature dependence of ISB energy and linewidth. | Measured plus theory in Ortmann 2018. A temperature/ε(E)-resolved ISB prediction was not found. | 1D SP per orbital (in scope). Nonlinear ε needs a Poisson-solver modification. | STO t2g masses (light ~0.7, heavy ~6–14 m0 [background]); ε(E,T) model (Landau–Devonshire fits from the literature); CBO 2.3–2.4 eV; STO LO phonons (several polar modes, incl. ~100 meV LO4 [background]). | PRB, PR Materials | Venkatesan (LAO/STO, PLD) |
| 3 | **Self-consistent ISB plus resonant χ(2) in displacement-field-gated few-layer InSe and WSe2** (layer-discretized 1D model). Proposes a gated vdW ISB modulator or SHG device; adds waveguide coupling with the toolkit's coupled-mode module. | Experiments 2018/2024/2026 with phenomenological fits. χ(2) theory not found. | 1D layer-chain or EMA: in scope. Multivalley (Q, K, Γ) needs separate m_z per valley. | m_z (WSe2 Γ 1.03–1.08 m_e; InSe from DFT); d = 6.477 Å (WSe2); ε_zz; valley offsets from DFT. | PRB, Phys. Rev. Applied, 2D Mater. | None at OU |
| 4 | **β-(AlGa)2O3/Ga2O3 QWs: multi-mode polar-phonon ISB lifetimes, line shapes, χ(2), QCL feasibility.** | Energies and QWIP done (2020). Lifetimes, χ(2) and QCL not found. | In scope. Extend the LO-phonon module to multiple anisotropic modes. | Anisotropic m* (~0.28 m0 [background]); CBO(x); IR mode set and oscillator strengths (literature, DFT). | JAP, APL Materials | Paik (oxide/nitride MBE, general) |
| 5 | **ScAlN/GaN lattice-matched ISB and THz/mid-IR QCL designs robust to polarization-constant uncertainty**, plus a global refit of P_sp(Sc) from published ISB data. | Purdue measures and fits their own data (2025 abstract). Design-robustness study not found. | In scope (nitride SP with polarization is standard). | P_sp, e_ij for ScAlN (contested); m*, CBO (uncertain); GaN LO 92 meV [background]. | APL, JAP | Paik (nitride sputtering/MBE capacity, unverified) |
| 6 | **m-plane ZnO/MgZnO THz QCL density-matrix design** (8–9 THz, beyond the GaAs reststrahlen band). | EL demonstrated 2021. Laser not achieved. The Faist group models internally. | In scope (polar LO phonon, nonpolar plane, no built-in field). | ZnO m* ~0.24–0.28, LO ~72 meV, MgZnO CBO(x) [background]. | Phys. Rev. Applied, JAP | Venkatesan (ZnO PLD history, unverified) |
| 7 | **CdSe nanoplatelet ISB vs monolayer count**: nonparabolicity and dielectric-confinement benchmark. | Measured 2019. Rigorous EMA fit not verified. | In scope. | CdSe m*, E_P, ligand barrier, ε mismatch. | J. Phys. Chem. C, PRB | None |
| 8 | **Ge/SiGe L-valley ISB χ(2)/DFG for CMOS THz generation.** | EL 2021. χ(2) design not checked. | Needs deformation-potential scattering added. | L m_z ~0.12, offsets vs Ge content, interface roughness parameters. | Phys. Rev. Applied | None |
| 9 | **SrVO3/SrTiO3 metallic QW ENZ/plasmon tuning by thickness** (correlated-metal QWs). | ARPES QW states known. Optical QW-ENZ theory not searched. | Partial: needs a Drude/nonlocal or hydrodynamic extension and DMFT-renormalized mass from the literature. | Renormalized mass (2–3×), plasma frequency, thickness. | ACS Photonics, APL Materials | Paik/Venkatesan (SrVO3 MBE/PLD) |

- **Suggested sequencing.**
  - #1 offers the best combination of novelty, local relevance and code readiness. It is also a natural "proposal seed" for later Paik collaboration: specify unit-cell-exact growth recipes and the predicted spectra an FTIR/Brewster-angle measurement would show.
  - #2 is a strong second if paired with Venkatesan.
  - #3 is a fast PRB-style paper independent of local growth.
- **What a 1D EMA code cannot credibly do** (k·p or DFT needed):
  - valence-band and TM/TE physics in AlGaN deep-UV QWs
  - type-II InAs/GaSb superlattice interband absorption
  - HgTe inverted bands
  - KTaO3 strong spin–orbit subbands
  - RP perovskite excitons with image charges (needs extension)
  - first-principles band offsets and polarization constants for any new oxide pair
  The workflow is to take those inputs from published DFT and propagate their uncertainty, rather than compute them.
- **Novelty strategy without experiment.** For each platform, make parameter uncertainty a headline result: report ISB energies, χ(2) and lifetimes as bands over the plausible m*/CBO/ε ranges. That gives experimentalists a falsifiable map and makes a theory-only paper more defensible to referees.

### Gaps
- None of the "Done?" entries was confirmed against Google Scholar or Web of Science. This session's searches are not exhaustive, especially for 2025–2026 peer-reviewed follow-ups of the Demkov BaSnO3 abstracts and any TMD ISB χ(2) theory.
- No source found for numerical BaSnO3, LaInO3 or Ga2O3 phonon and dielectric parameters. These must be gathered before any calculation.
- Venkatesan's current OU capabilities (ZnO, SrVO3, LAO/STO) are asserted from background knowledge only.
