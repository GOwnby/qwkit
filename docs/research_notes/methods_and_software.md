# Methods, theory and software gaps in quantum-well optoelectronics (2018–Oct 2026): publishable pure-theory, computation, software and benchmark papers for a solo theorist

Verification labels used throughout:
- **[F]** = abstract or landing page fetched and read in this session.
- **[T]** = verified at title/snippet level only (search-result title and URL; content not read).
- **[K]** = from background knowledge, NOT verified in this session. These appear only in Inferences/Gaps and must be checked before citing.

Search coverage: about 30 tool calls (web search plus fetch). SciPost pages were blocked by an anti-bot wall, so the kdotpy facts come from arXiv. No paywalled full texts were read. "Not found" means not found in these searches; it does not prove absence.

---

## Q1. Band structure: multiband k.p, spurious solutions, operator ordering, interfaces, strain/piezo, atomistic vs continuum, parameter uncertainty

### Takeaway
Multiband k.p for QWs is mature, but four things are still handled ad hoc and leave room for papers: spurious solutions, operator ordering (Burt–Foreman) with interface terms, nitride wurtzite ellipticity, and parameter uncertainty. Recent work states that it pays "careful attention" to spurious solutions without a standard procedure. No systematic uncertainty-quantification study propagating the Vurgaftman–Meyer parameter spreads into QW observables turned up in these searches. Atomistic tight-binding work (UCC/Tyndall group) shows continuum k.p misses alloy-fluctuation localisation in InGaN QWs. That leaves a gap for cheap "continuum-plus-disorder" methods and benchmark comparisons.

### Cited Findings
- 2023, Murphy, O'Reilly and Broderick: radiative recombination in broken-gap InAs/GaSb superlattices computed with an 8-band k.p Hamiltonian plus a semi-analytical plane-wave expansion. The authors state they pay "careful attention to the identification and mitigation" of spurious solutions. The abstract gives no general recipe. DOI 10.1088/1361-6463/ad015d (J. Phys. D series, inferred from the DOI prefix). [F] — [arXiv:2310.18194](https://arxiv.org/abs/2310.18194)
- A 2009 Springer paper (vol. 40, issues 14–15, pp. 1169–1174) titled "Operator ordering, ellipticity and spurious solutions in k·p calculations of III-nitride nanostructures". Keywords: finite elements, wurtzite, nitride. The authors were not shown on the page. Volume and pages are consistent with Opt. Quantum Electron. (NUSOD issue), but that is not confirmed. [F, metadata only] — [ETH Research Collection](https://www.research-collection.ethz.ch/entities/publication/cebe5e8d-c6b4-43b5-9035-a1b01a4d0472)
- Older anchors on spurious solutions and boundary conditions:
  - "Spurious solutions in the multiband effective mass theory applied…" (DTU) [T] — [DTU Orbit](https://orbit.dtu.dk/en/publications/spurious-solutions-in-the-multiband-effective-mass-theory-applied/)
  - "General boundary conditions for the envelope function in multiband k.p model" [T] — [arXiv:cond-mat/0112359](https://arxiv.org/pdf/cond-mat/0112359)
  - "Real-space Hamiltonian method for low-dimensional semiconductor heterostructures" [T] — [arXiv:1105.6309](https://arxiv.org/pdf/1105.6309)
  - "Development of an eight-band theory for quantum-dot heterostructures" [T] — [arXiv:cond-mat/0109275](https://arxiv.org/pdf/cond-mat/0109275)
  - Durham thesis "Theory of the electronic states of semiconductor heterostructures" [T] — [Durham e-theses](https://etheses.durham.ac.uk/id/eprint/4495/)
- New k.p parameterisations are still appearing for new materials, e.g. "Multiband k·p theory for hexagonal germanium" (2023). So parameterising multiband k.p for an emerging material is a live, publishable theory activity. [T] — [arXiv:2310.17366](https://arxiv.org/pdf/2310.17366)
- Review-type source on multiband k.p for nanostructures: "Simulating the electronic properties of semiconductor nanostructures using multiband k·p models" (TIB repository). [T] — [TIB](https://oa.tib.eu/renate/handle/123456789/9423)
- Atomistic vs continuum:
  - "Atomistic analysis of the impact of alloy and well-width fluctuations on the electronic and optical properties of InGaN/GaN quantum wells" [T] — [arXiv:1501.05482](https://arxiv.org/pdf/1501.05482)
  - "Atomistic description of wave function localization effects in InxGa1-xN alloys and quantum wells" [T] — [UCC](https://research.ucc.ie/en/publications/atomistic-description-of-wave-function-localization-effects-in-in/)
  - Both show alloy and well-width fluctuations matter in nitride QWs beyond virtual-crystal continuum models.
- First-principles band alignment for heterostructures is still active in 2026: "First-principles predictions of band alignment in strained Si/Si1-xGex and Ge/Si1-xGex heterostructures" (Mar 2026) [T] — [arXiv:2603.13219](https://arxiv.org/pdf/2603.13219). Also "Increasing valley splitting in Si/SiGe by practically achievable heterostructure profiles" (Mar 2026) [T] — [arXiv:2603.19769](https://arxiv.org/pdf/2603.19769). These show that a profile-engineering theory paper (no experiment) is a live genre in 2026.
- Uncertainty quantification: a direct search ("uncertainty quantification band parameters heterostructure simulation k.p sensitivity") returned no paper doing UQ/sensitivity analysis of Vurgaftman-type parameters for III-V QW optoelectronic observables. Results were SiGe band alignment and hex-Ge k.p, not UQ. — [search results incl. arXiv:2603.13219](https://arxiv.org/pdf/2603.13219)

### Inferences
- **Paper opportunity A1: "Spurious-solution-free 8-band (and 14-band) k.p for QWs: a reproducible benchmark and decision guide."**
  - Content: compare Foreman rescaling of the Kane energy E_P, Burt–Foreman ordering, discretisation choices (FD staggered grid, FEM, plane-wave/Fourier) and the ellipticity criteria. Use standard structures: GaAs/AlGaAs, InGaAs/InAlAs, InAs/GaSb T2SL, and wurtzite InGaN.
  - Experiment needed: no.
  - Prior work: done piecemeal (2009 nitride paper above; 2023 InAs/GaSb paper treating it as a side issue). No unified open benchmark was found [inference from searches].
  - Venues: J. Comput. Electron., Comput. Phys. Commun., Opt. Quantum Electron. (NUSOD-type).
- **Paper opportunity A2: global sensitivity / UQ of QW observables to band parameters.**
  - Parameters: Vurgaftman 2001/2003 spreads for band offsets, Luttinger parameters, E_P, deformation potentials, bowing.
  - Methods: Sobol indices or polynomial chaos.
  - Observables: subband energies, intersubband dipole, QCL gain, ISB transition energy, T2SL gap.
  - Experiment needed: no.
  - Prior work: not found → apparently open (verify with Scopus).
  - Strong fit for qwkit, since 1D solves are cheap. Venues: J. Appl. Phys., PR Applied (if tied to design robustness), Semicond. Sci. Technol.
- **Paper opportunity A3: continuum-plus-disorder (localisation-landscape or random-alloy effective-mass) vs published atomistic TB results for InGaN QWs.**
  - Experiment needed: no. Benchmark against published TB data.
  - Prior work: landscape-theory approaches exist [K: Filoche, Piccardo, Weisbuch, Speck et al., PRB 2017; Li et al. 2017]. A systematic accuracy map vs TB across well widths and compositions appears less done [inference].
- Interface (Burt "ħ²/2m" ordering and interface-dipole) terms for thin wells (<3 nm) remain parameter-starved. A paper extracting interface-term magnitudes from published DFT/TB band edges, then fitting k.p interface delta-terms, is feasible without experiment [inference].

### Gaps
- Could not verify authors of the 2009 nitride operator-ordering paper. [K: likely Veprek, Steiger, Witzigmann.]
- Classic anchors not verified this session [K]:
  - Burt, J. Phys.: Condens. Matter 4, 6651 (1992)
  - Foreman, PRB 56, R12748 (1997)
  - Vurgaftman, Meyer and Ram-Mohan, J. Appl. Phys. 89, 5815 (2001)
  - Vurgaftman and Meyer, J. Appl. Phys. 94, 3675 (2003) (nitrides)
  - Birner et al. (nextnano), IEEE TED 54, 2137 (2007)
  - Bastard; Chuang
  - Kolokolov/Ram-Mohan on spurious solutions
- No quantitative recent survey of empirical pseudopotential vs k.p for <3 nm wells was found.
- 14-band k.p (Pfeffer–Zawadzki type) QW benchmarks were not searched specifically.

---

## Q2. Transport/kinetics: NEGF, density matrix, Monte Carlo; escape; hot carriers; interface roughness and alloy scattering; e–e scattering

### Takeaway
Commercial nextnano.NEGF now lists LO and acoustic phonons, charged impurities, interface roughness, alloy disorder and electron–electron scattering. There is still no widely used open-source QCL NEGF code; the search found only generic NEGF packages. Electron–electron scattering in NEGF beyond simple approximations (self-consistent GW) has been done for nanotubes but is costly. QW-solar carrier escape and the hot-carrier phonon bottleneck are treated by reviews as multi-factor, unresolved mechanisms. All of this points to benchmark papers, reduced models and open-code contributions that need no experiment.

### Cited Findings
- **nextnano.NEGF (commercial).**
  - Scattering listed: LO phonon, acoustic phonon, charged impurity, interface roughness, alloy, electron–electron.
  - The C# "classic" version is Windows-only and deprecated; the C++ version runs on Windows/Linux. Documentation is "currently being updated and migrated".
  - The page gives no literature references for the implemented physics.
  - [F] — [nextnano.NEGF overview](https://www.nextnano.com/docu/nextnano.NEGF/overview/index.html)
- **NEGF + Bayesian optimisation for THz QCLs (PR Applied 13, 034025, 2020).**
  - Bayesian optimisation converges faster and more reliably than a genetic algorithm. It helped reach the 210 K record for THz QCLs.
  - Two-well designs are better for high temperature; three-well designs are more robust to thickness variations. Period thickness must be controlled to within a few percent.
  - Code availability not stated on the page.
  - [F] — [PR Applied 13, 034025](https://link.aps.org/doi/10.1103/PhysRevApplied.13.034025); [ETH PDF](https://www.research-collection.ethz.ch/bitstream/20.500.11850/406403/3/PhysRevApplied.13.034025.pdf). A companion "Bayesian optimization of quantum cascade detectors" exists. [T] — [ETH](https://www.research-collection.ethz.ch/entities/publication/eb634318-0bac-490f-b1b7-101998472c04)
- Standard review of QCL modelling: "Modeling techniques for quantum cascade lasers" (rate equations, density matrix, Monte Carlo, NEGF). [T] — [arXiv:1412.3563](https://arxiv.org/pdf/1412.3563)
- Electron–electron scattering in NEGF:
  - "Simple electron-electron scattering in non-equilibrium Green's function simulations" (2016) gives a simplified approach. [T] — [arXiv:1602.03997](https://arxiv.org/pdf/1602.03997)
  - Deuschle, Backman, Luisier and Cao (2023) ran ab initio NEGF with self-consistent GW to get Auger recombination, hot-carrier relaxation and impact ionisation, for carbon nanotubes only, not QWs. [F] — [arXiv:2307.05297](https://arxiv.org/abs/2307.05297)
- Open NEGF software found is generic (molecular/nanoscale), not QCL-specific:
  - funegf (PyPI) [T] — [PyPI funegf](https://pypi.org/project/funegf)
  - RUQT (Rowan) [T] — [GitHub RUQT](https://github.com/EPHoy-QC/RUQT_beta)
  - ecosyste.ms NEGF topic list [T] — [ecosyste.ms](https://repos.ecosyste.ms/topics/negf)
  - A search for an open Lund/Wacker QCL NEGF code returned nothing QCL-specific.
- **Density-matrix models are being used to train ML surrogates (2026).**
  - The Belgrade/Leeds groups used a DM model (self-consistent Schrödinger–Poisson plus kinetic balance, equithermal subband approximation) for a two-well THz QCL operating at 261 K.
  - The authors note that background doping, interdiffusion and layer-thickness fluctuations are not modelled, and that LO-phonon non-radiative scattering limits high-temperature operation.
  - [F] — [Nanomaterials 16(11), 651 (2026)](https://www.mdpi.com/2079-4991/16/11/651)
- **Hot carriers and phonon bottleneck.**
  - Zhang, Conibeer, Liu, Zhang and Guillemoles, Prog. Photovolt. 30(6), 581–596 (2022), DOI 10.1002/pip.3557: PBE plays "the most decisive role" in reducing thermalisation.
  - Mechanisms depend on carrier density, band structure, phonon dispersion and confinement.
  - MQWs are the "most promising" material system for hot-carrier solar cells.
  - [F] — [IP Paris portal](https://researchportal.ip-paris.fr/en/publications/review-of-the-mechanisms-for-the-phonon-bottleneck-effect-in-iiiv/)
- Related hot-carrier theory and experiment:
  - "Theoretical Insights into Next-Generation Hot Carrier Solar Cells" [T] — [RUG](https://research.rug.nl/en/publications/theoretical-insights-into-next-generation-hot-carrier-solar-cells/)
  - "Hot carrier exploitation strategies and model for efficient solar cell applications" [T] — [Heriot-Watt](https://researchportal.hw.ac.uk/en/publications/hot-carrier-exploitation-strategies-and-model-for-efficient-solar/)
  - "Hot carriers and phonon relaxation processes in InAs/AlAsSb quantum wells" (SPIE 11681) [T] — [SPIE](https://nanophotonics.spiedigitallibrary.org/conference-proceedings-of-spie/11681/116810P/Hot-carriers-and-phonon-relaxation-processes-in-InAs-AlAsSb-quantum/10.1117/12.2576948.full)
  - "Quantitative optoelectronic measurements of carrier thermodynamics properties in quantum well hot carrier solar cell" (experimental) [T] — [HAL INSA Rennes](https://hal-insa-rennes.archives-ouvertes.fr/hal-02402286)
  - Conibeer talk "Hot Carrier Solar Cells: Phonon Bottlenecks to slow Carrier Cooling" (APVI 2023) [T] — [APVI PDF](https://apvi.org.au/solar-research-conference/wp-content/uploads/2023/02/Conibeer-Hot-Carrier-Solar-Cells-Phonon-Bottlenecks-to-slow-Carrier-Cooling.pdf)
- Carrier escape from QWs in solar cells:
  - Toprasertpong et al., "Carrier Escape Time and Temperature-Dependent Carrier Collection Efficiency of Tunneling-Enhanced Multiple Quantum Well Solar Cells" [T] — [ResearchGate PDF](https://researchgate.net/profile/Kasidit-Toprasertpong/publication/257304028_Carrier_Escape_Time_and_Temperature-Dependent_Carrier_Collection_Efficiency_of_Tunneling-Enhanced_Multiple_Quantum_Well_Solar_Cells/links/56b6391908ae44bb33079865/Carrier-Escape-Time-and-Temperature-Dependent-Carrier-Collection-Efficiency-of-Tunneling-Enhanced-Multiple-Quantum-Well-Solar-Cells.pdf)
  - Aeberhard, "Spectral properties of photogenerated carriers in quantum well solar cells" (NEGF) [T] — [arXiv:0912.0592](https://arxiv.org/pdf/0912.0592)
  - "Thermo-tunneling design for quantum well photovoltaic converter" patent US9450123 [T] — [Google Patents](https://patents.google.com/patent/US9450123)

### Inferences
- **Paper opportunity B1: "Open, minimal QCL/QWIP transport benchmark suite."**
  - Content: 3–5 canonical published structures with digitised published experimental J–V/gain as reference. Cross-compare rate equations, density matrix (qwkit-style), and published NEGF/MC results.
  - Experiment needed: no new experiment; uses published data.
  - Prior work: the 2014 review compares methods conceptually. No open, versioned benchmark dataset was found.
  - Venues: J. Comput. Electron., Comput. Phys. Commun., Opt. Quantum Electron.
- **Paper opportunity B2: reduced-order e–e scattering for ISB density-matrix models.**
  - Content: compare Hartree, simple statistical NEGF-like e–e (cf. arXiv:1602.03997) and a full Boltzmann e–e rate in a 1D tool. Quantify its effect on gain and linewidth vs doping.
  - Experiment needed: no.
  - Prior work: partially done inside NEGF codes; not available as an open, documented module [inference].
- **Paper opportunity B3: interface-roughness and alloy-disorder scattering parameter sensitivity.**
  - IR parameters (Δ, Λ) are typically fitted per paper. A UQ study of IR-limited linewidth and QCL performance vs (Δ, Λ) correlation function (Gaussian vs exponential) is feasible without experiment, extending A2. Novelty plausible but not verified.
- **Paper opportunity B4: QW-solar escape-rate theory.**
  - Content: unified thermionic + phonon-assisted + sequential-tunnelling escape vs field/temperature in a Schrödinger–Poisson framework with open boundaries (complex absorbing potential or transfer matrix for quasi-bound lifetimes). Compare to published Toprasertpong data.
  - Experiment needed: no.
  - Prior work: partially done (Aeberhard NEGF; Toprasertpong semi-empirical). A lightweight open model calibrated across published datasets appears missing [inference].
- **Paper opportunity B5: hot-phonon bottleneck in MQWs, rate-equation/Boltzmann theory with confined + interface phonons and LO-phonon lifetime (Klemens/anharmonic decay).**
  - The 2022 review names the factors but implies no consensus model.
  - Experiment needed: no, if compared to published TRPL/CW-PL hot-carrier temperatures.
  - Prior work: partly done by Conibeer and Guillemoles groups.

### Gaps
- Could not confirm whether any QCL-specific NEGF code is open-source as of 2026. [K: Wacker's Lund NEGF code was used widely but historically was not public; Grange's code and Kubis's NEMO5/NEMO-based work are not open source; Franckié's "aftershoq" Python optimisation wrapper is reported open on GitHub. Unverified.]
- Authors of arXiv:1602.03997 were not confirmed. [K: Winge, Franckié, Verdozzi, Wacker, Pereira.]
- No 2020–2026 review of interface-roughness modelling in QCLs was retrieved.
- Electron escape in QWIPs (photoconductive gain theory) was not searched specifically.

---

## Q3. Many-body optics: depolarisation, multisubband plasmons, excitons in QWs for solar/TPV, nonlinear many-body response, non-Lorentzian lineshapes

### Takeaway
The multisubband-plasmon (MSP) framework from the Paris group (Vasanelli, Todorov, Sirtori) is established. A 2023 J. Appl. Phys. perspective lays out physics, material and application paths, including ultrastrong coupling to cavities and phonons. Intersubband lineshape theory beyond Lorentzian has old anchors but no modern open implementation was found. A qwkit-style code with Ando depolarisation already sits at the entry point of this literature. Extending it to full MSP diagonalisation, plasmon–phonon coupling, and non-Lorentzian/inhomogeneous lineshapes is directly publishable.

### Cited Findings
- **Montes Bajo, Chauveau, Vasanelli, Delteil, Todorov, Sirtori and Hierro, "Perspectives and opportunities with multisubband plasmonics", J. Appl. Phys. 134, 010901 (2023).**
  - MSPs are presented as a platform for collective and exotic effects and new device concepts.
  - High densities may enable ultrastrong coupling of MSPs with cavity modes or semiconductor phonons.
  - [F] — [UPM repository](https://oa.upm.es/86098/)
- "Quantum model of coupled intersubband plasmons" (Pegolotti et al., PRB 2014 [K]). [T] — [arXiv:1407.3923](https://ar5iv.labs.arxiv.org/html/1407.3923)
- "Quantum Theory of Multisubband Plasmon–Phonon Coupling", Photonics 7(1), 19 (2020). [T] — [HAL](https://hal.sorbonne-universite.fr/hal-02553732v1); [MDPI mirror](https://0-www-mdpi-com.brum.beds.ac.uk/2304-6732/7/1/19)
- Vasanelli talk "Dense light" at KITP. [T] — [KITP PDF](https://www.on.kitp.ucsb.edu/online/denselight-c15/vasanelli/pdf/Vasanelli_DenseLight15Conf_KITP.pdf)
- Intersubband lineshape anchors:
  - "Lineshape analysis of intersubband transitions in multiple quantum wells" (MRS) [T] — [Cambridge](https://resolve.cambridge.org/core/journals/mrs-online-proceedings-library-archive/article/abs/lineshape-analysis-of-intersubband-transitions-in-multiple-quantum-wells/E486CA21CBEC938A843F7ABB68288AC1)
  - A PRB 66, 125303 (2002) paper surfaced for intersubband lineshape/roughness. Title not confirmed. [T] — [arXiv:cond-mat/0208195](https://arxiv.org/pdf/cond-mat/0208195)
- Excitons and absorption in nanostructured solar cells beyond the generalised Planck formula: Aeberhard, "Microscopic theory of absorption and emission in nanostructured solar cells: Beyond the generalized Planck formula". [T] — [arXiv:0912.1450](https://arxiv.org/pdf/0912.1450)

### Inferences
- **Paper opportunity C1: open MSP solver.**
  - Content: dipole-representation Hamiltonian for N subbands with Löwdin-orthonormalised states and depolarisation plus exchange-correlation. Validate against the Paris group's published spectra for highly doped GaAs, InGaAs and ZnO wells.
  - Experiment needed: no; reproduce published experiments.
  - Prior work: theory done by the Paris group; no open-source implementation found [inference]. Venues: PRB (if a new physics angle is added), JOSS/SoftwareX (software).
- **Paper opportunity C2: MSP–LO-phonon coupling in polar wells (GaN, ZnO, InAs) with Fröhlich coupling.**
  - Builds on the Photonics 2020 theory. Adding nonparabolicity and multiple wells is straightforward with qwkit's existing modules.
  - Experiment needed: no.
  - Prior work: partially done (Photonics 2020).
- **Paper opportunity C3: non-Lorentzian ISB lineshapes.**
  - Content: a consistent many-body + inhomogeneous (thickness and doping fluctuation) + nonparabolicity lineshape model. Compare Lorentzian, Voigt, and dephasing-plus-depolarisation lineshapes (Ando's sum-rule-consistent formulation). Fit published spectra.
  - Experiment needed: no.
  - Prior work: old literature exists; not unified or open [inference].
- **Paper opportunity C4: second-order nonlinear ISB response with depolarisation and MSP effects.**
  - Content: chi(2) with collective shifts. How does depolarisation detune the double-resonance condition in coupled-QW SHG designs? Directly uses qwkit's chi(2) and saturation modules.
  - Experiment needed: no.
  - Prior work: possibly treated in older ISB nonlinear literature [K: Rosencher, Bois]. Novelty for the MSP-regime chi(2) seems unverified → check.

### Gaps
- Did not retrieve the specific "open problems" list inside the JAP 2023 perspective (abstract only).
- Excitons in QWs for TPV specifically: no 2018–2026 theory paper found in these searches.
- Did not find modern theory papers on excitonic effects in QW solar cells' radiative limits.

---

## Q4. Open-source codes and reproducibility; JOSS/CPC/SoftwareX; benchmarks

### Takeaway
The open ecosystem is fragmented. kdotpy (SciPost Phys. Codebases, 2024–25) covers lattice k.p of the Kane model. Aestimo 1D (Comput. Mater. Sci. 2021) and PyNitride cover 1D Schrödinger–Poisson. ErwinJr2 covers QCL design. Solcore (J. Comput. Electron. 2018) and Sesame (NIST, 2018) cover solar cells. Commercial nextnano covers NEGF. Missing: an open, tested, documented 1D ISB-optics stack (depolarisation, LO-phonon rates, chi(2), waveguide) with a published benchmark dataset, and an open QCL NEGF. qwkit fits that gap, so a JOSS or Comput. Phys. Commun. paper is realistic.

### Cited Findings
- **kdotpy** (Beugeling et al., Würzburg; Molenkamp group).
  - Python, k·p on a lattice, Kane model for zinc blende. Command-line inputs for materials, dimensions, magnetic field and temperature.
  - SciPost Phys. Codebases 47 (DOI 10.21468/SciPostPhysCodeb.47; arXiv 2024).
  - [F] — [arXiv:2407.12651](https://arxiv.org/abs/2407.12651); [project site](https://gitpages.physik.uni-wuerzburg.de/kdotpy/web/); [PyPI](https://pypi.org/project/kdotpy/)
- **Aestimo 1D**, "General-purpose open-source 1D self-consistent Schrödinger–Poisson solver", Comput. Mater. Sci. 186 (2021). Includes tutorials. [T] — [Gazi University record](https://avesis.gazi.edu.tr/yayin/4d70de09-17fc-4bd8-8c3d-9f41708e813f/general-purpose-open-source-1d-self-consistent-schrodinger-poisson-solver-aestimo-1d); [tutorial notebook](https://nbviewer.org/github/aestimosolver/aestimo/blob/master/tutorials/Aestimo_tutorial1.ipynb)
- **PyNitride** scientific package (nitride heterostructures). [T] — [docs](https://pynitride.readthedocs.io/en/latest/)
- **HADOKEN**, an open-source package for electron confinement in nanowires. [T] — [arXiv:2203.05233](https://arxiv.org/pdf/2203.05233)
- **ErwinJr2**, a QCL design tool (Princeton/Gmachl lineage) on PyPI. [T] — [PyPI](https://pypi.org/project/ErwinJr2); [docs](https://erwinjr2.readthedocs.io/)
- **Solcore**, "a multi-scale, Python-based library for modelling solar cells and semiconductor materials" (J. Comput. Electron. 2018; DOI 10.1007/s10825-018-1171-3). [T] — [arXiv:1709.06741](https://arxiv.org/abs/1709.06741); [docs](https://solcore5.readthedocs.io/en/latest/index.html)
- **Sesame**, "a 2-dimensional solar cell modeling tool" (Gaury, Haney et al., NIST). [T] — [arXiv:1806.06919](https://arxiv.org/pdf/1806.06919); [NIST](https://www.nist.gov/node/1577896)
- **nextnano.NEGF** is commercial. Platform and documentation status: see Q2. [F] — [nextnano docs](https://www.nextnano.com/docu/nextnano.NEGF/overview/index.html)

### Inferences
- **Paper opportunity D1: qwkit software paper.**
  - JOSS requires an open repository, tests, documentation and a short paper. CPC/SoftwareX want a longer methods description plus validation.
  - Differentiator: an integrated ISB-optics chain (Kane nonparabolic SP → Löwdin → depolarisation → LO-phonon rates → chi(2)/saturation → TM waveguide → coupled-mode SHG). Aestimo, kdotpy and ErwinJr2 do not appear to offer this full chain (inferred from their descriptions).
  - Experiment needed: no.
  - Prior work: not done for this feature set.
- **Paper opportunity D2: cross-code benchmark ("same structure, five codes").**
  - Codes: qwkit vs Aestimo vs kdotpy vs ErwinJr2 vs nextnano (if licence permits) on subband energies, dipoles, ISB absorption and LO-phonon lifetimes for canonical structures. Publish the dataset on Zenodo.
  - Experiment needed: no.
  - Prior work: not found.
  - Venues: J. Comput. Electron., Comput. Phys. Commun., Semicond. Sci. Technol.
- **Paper opportunity D3: tutorial/review "Reproducible intersubband device modelling in Python".**
  - Pedagogical, tied to the Vurgaftman–Lumb–Meyer textbook chapters. Venues: J. Appl. Phys. Tutorial, Eur. J. Phys., Am. J. Phys.
  - Experiment needed: no.

### Gaps
- Did not verify whether PyQW, QClan, NEMO5 or kwant releases relevant to QWs changed in 2018–2026. No QW-specific JOSS paper was found by search. [K: kwant is a tight-binding transport code (Groth et al., NJP 2014); NEMO5 is licensed via nanoHUB.]
- Did not verify the Sesame journal (possibly Comput. Phys. Commun. 2019; a PMC record PMC7047709 exists [T]).
- No public benchmark dataset for QCL/QWIP simulations was found.

---

## Q5. Machine learning: surrogates, inverse design, differentiable solvers, Bayesian optimisation

### Takeaway
ML for QCLs has moved from Bayesian optimisation with NEGF (ETH, 2020) to neural-network surrogates.
- Princeton, 2024: an MLP on a 10-layer design reached a 1.5× figure of merit (FoM) over the baseline.
- Belgrade/Leeds, 2026: ANN, Random Forest and XGBoost surrogates trained on a 62k-sample density-matrix dataset.

Every surrogate found is local, trained around one reference design. None reports uncertainty-aware predictions, robustness to growth fluctuations, or a physics-differentiable solver. A differentiable Schrödinger–Poisson (autodiff / adjoint eigenvalue sensitivity) for heterostructure inverse design was not found in 2018–2026 searches. Older inverse-scattering design exists.

### Cited Findings
- **Correa Hernandez and Gmachl (arXiv:2406.07755, 2024).**
  - Model: MLP predicting the laser-transition FoM from layer thicknesses and field.
  - Data: random perturbations of a 10-layer design. Screened about 907 million designs in 8 h on a laptop, vs 27,000 designs in 32 h with a 1D Schrödinger solver.
  - Result: FoM rose from 94.7 to 141.2 eV ps Å².
  - Error: 5–15% for lasing structures, 35–70% for non-lasing.
  - [F] — [arXiv:2406.07755](https://arxiv.org/abs/2406.07755)
- Further Princeton ML-QCL items:
  - "Application of machine learning to quantum cascade laser design" [T] — [Princeton](https://collaborate.princeton.edu/en/publications/application-of-machine-learning-to-quantum-cascade-laser-design/)
  - "Machine learning for quantum cascade laser design and optimization" [T] — [Princeton](https://collaborate.princeton.edu/en/publications/machine-learning-for-quantum-cascade-laser-design-and-optimizatio/)
  - Navy SBIR topic N20A-T003, "Fully Automated QCL Design Aided by Machine Learning with up to 100X Design Cycle Time Reduction" [T] — [navysbir.com](https://www.navysbir.com/n20_A/N20A-T003.htm)
- **Stojković et al., Nanomaterials 16(11), 651 (May 2026).**
  - Data: 62,250 DM-simulated samples, ±40% layer variation, 17.5–27.5 kV/cm.
  - Results: the ANN beat Random Forest and XGBoost (standardised RMSE 0.04–0.22 vs 0.16–0.55). Screened about 44 million configurations in about 5 min (~90,000× speed-up).
  - Limits: a single reference device and a fixed lattice temperature.
  - [F] — [MDPI](https://www.mdpi.com/2079-4991/16/11/651)
- **Bayesian optimisation with NEGF for THz QCLs:** PR Applied 13, 034025 (2020) [F] — [APS](https://link.aps.org/doi/10.1103/PhysRevApplied.13.034025). Also BO for quantum cascade detectors [T] — [ETH](https://www.research-collection.ethz.ch/entities/publication/eb634318-0bac-490f-b1b7-101998472c04)
- **Classical inverse design of heterostructures by inverse scattering:**
  - "Design of semiconductor heterostructures with preset electron reflectance by inverse scattering techniques" [T] — [arXiv:cond-mat/9903445](https://arxiv.org/abs/cond-mat/9903445)
  - "Electron Wave Filters from Inverse Scattering Theory" [T] — [arXiv:cond-mat/9606209](https://ar5iv.arxiv.org/html/cond-mat/9606209)
- A search for "differentiable Schrödinger solver heterostructure inverse design quantum well" returned only these 1996–1999 inverse-scattering papers and Aestimo. No autodiff heterostructure solver was found. — [search results](https://arxiv.org/pdf/cond-mat/9903445)

### Inferences
- **Paper opportunity E1: differentiable 1D Schrödinger–Poisson.**
  - Content: JAX/PyTorch, with analytic eigenvalue and eigenvector derivatives (Hellmann–Feynman / adjoint) through nonparabolicity and self-consistency. Use gradient-based inverse design of ISB transition energy, dipole, chi(2) and QCL FoM; compare to BO and ML surrogates on identical targets.
  - Experiment needed: no.
  - Prior work: not found → apparently open.
  - Venues: npj Comput. Mater., PR Applied, Comput. Phys. Commun.
- **Paper opportunity E2: robust / uncertainty-aware inverse design.**
  - Content: optimise expected performance under monolayer thickness fluctuations, interdiffusion and doping errors, using Monte Carlo or polynomial chaos. Both the 2020 BO paper (period control to a few percent) and the 2026 surrogate paper (fluctuations not modelled) flag this.
  - Experiment needed: no.
  - Prior work: partially (BO robustness comparison of two- vs three-well designs).
- **Paper opportunity E3: open benchmark dataset for heterostructure ML.**
  - Content: millions of qwkit-computed structures with labels (energies, dipoles, LO lifetimes, chi(2)), plus standard train/test splits. Similar in spirit to materials-ML datasets.
  - Experiment needed: no.
  - Prior work: not found. Venues: Scientific Data, npj Comput. Mater., Mach. Learn.: Sci. Technol.
- ML for QWIP or QW-solar inverse design: nothing found in these searches. Probably less saturated than QCLs [inference, not verified].

### Gaps
- Did not search ML for QWIP/QCD absorption design or MQW solar cells specifically.
- Did not verify the AIP Advances (Oct 2024) DOAJ item [T, title unknown] — [DOAJ](https://doaj.org/article/af76100731db45b9a091c5920f6a8b3c).
- Did not check physics-informed neural networks (PINNs) for Schrödinger–Poisson in heterostructures.

---

## Q6. Detailed balance / thermodynamics (Shockley–Queisser, generalised Planck, reciprocity) for quantum structures

### Takeaway
Detailed-balance theory for QW solar cells and TPV has classic anchors:
- generalised Planck / reciprocity (Kirchartz, Rau);
- NEGF "beyond generalised Planck" (Aeberhard);
- new formulations (Georgia Tech).

Hot-carrier MQW cells are still debated (phonon-bottleneck mechanisms). Efficiency-limit papers with new physics ingredients are still being posted in 2026 (TMD hot-carrier/multiplication limits), so this genre is publishable without experiment. Proper confinement, excitonic absorption edges and QW-specific escape and thermalisation need care.

### Cited Findings
- Aeberhard, "Microscopic theory of absorption and emission in nanostructured solar cells: Beyond the generalized Planck formula" [T] — [arXiv:0912.1450](https://arxiv.org/pdf/0912.1450)
- "A New Generalized Detailed Balance Formulation to Calculate Solar Cell Efficiency Limits" (Georgia Tech) [T] — [GT repository](https://repository.gatech.edu/entities/publication/e6451ea4-dff0-4918-ad62-d7433bc0076a)
- Kirchartz thesis "Generalized detailed balance theory of solar cells" [T] — [YouScribe listing](https://www.youscribe.loungeup.com/catalogue/documents/savoirs/generalized-detailed-balance-theory-of-solar-cells-elektronische-1436157)
- "Fundamental Efficiency Limits of TMD Solar Cells" (arXiv 2605.00451, 2026): thermodynamic limits including carrier multiplication and hot-carrier effects. [T; landing-page summary only] — [Emergent Mind](https://www.emergentmind.com/papers/2605.00451)
- MQWs are named "the most promising" hot-carrier absorbers, but PBE mechanisms are multi-factor. [F] — [Zhang et al. 2022](https://researchportal.ip-paris.fr/en/publications/review-of-the-mechanisms-for-the-phonon-bottleneck-effect-in-iiiv/)
- Experimental quantification of carrier thermodynamics in QW hot-carrier cells (INSA Rennes/IPVF lineage) [T] — [HAL](https://hal-insa-rennes.archives-ouvertes.fr/hal-02402286)

### Inferences
- **Paper opportunity F1: detailed-balance limits for MQW solar/TPV cells with realistic confined absorption.**
  - Content: Schrödinger–Poisson subband absorption with excitonic Sommerfeld enhancement, finite well count, escape efficiency (from B4), and photon recycling and reciprocity. Vary well depth and number; give TPV-specific emitter temperatures.
  - Experiment needed: no.
  - Prior work: partially done historically [K: Barnham, Araújo/Martí debate on QW-cell limits in the 1990s–2000s]. A modern open, reproducible treatment for TPV appears missing [inference].
  - Venues: PR Applied, J. Appl. Phys., Prog. Photovolt. (theory).
- **Paper opportunity F2: hot-carrier MQW limit with phonon-bottleneck rate and energy-selective contacts modelled from subband physics.**
  - Experiment needed: no.
  - Prior work: partially (Conibeer and Guillemoles groups).
- **Paper opportunity F3: reciprocity (Rau) check for QW cells using qwkit absorption plus a simple drift-diffusion escape.** Verify where reciprocity breaks (incomplete escape). A tutorial-grade paper. Experiment needed: no.

### Gaps
- Did not retrieve 2018–2026 QW-TPV-specific detailed-balance papers. [K: TPV records by NREL/MIT (Omair et al., Nature 2022) use bulk-like junctions, not QWs.]
- Classic anchors not verified this session [K]:
  - Shockley and Queisser, J. Appl. Phys. 32, 510 (1961)
  - Würfel, J. Phys. C 15, 3967 (1982)
  - Rau, PRB 76, 085303 (2007)
  - Ross and Nozik (1982) on hot-carrier cells
  - Barnham and Duggan, J. Appl. Phys. 67, 3490 (1990)

---

## Q7. Which of these can a solo theorist turn into papers now, and in which venues?

### Takeaway
The best near-term papers with no experiment and qwkit-ready tooling:
1. A JOSS/CPC software paper for qwkit (D1).
2. A UQ/sensitivity paper on band parameters → ISB/QCL observables (A2/B3).
3. A differentiable or robust inverse-design paper (E1/E2), positioned against the 2020 BO-NEGF and the 2024/2026 ML surrogates.
4. An open MSP + depolarisation + chi(2) many-body ISB optics paper (C1/C4).
5. A cross-code benchmark dataset (D2/E3).

All rely only on published experimental data for validation. Each needs a novelty check in Scopus/Web of Science, because most "not found" judgements here come from a limited web search.

### Cited Findings
- SciPost Physics Codebases accepted a pure k·p software paper (kdotpy). That is evidence that QW software papers are publishable as standalone contributions. [F] — [arXiv:2407.12651](https://arxiv.org/abs/2407.12651)
- Comput. Mater. Sci. published a 1D Schrödinger–Poisson solver paper (Aestimo 1D, 2021). [T] — [Gazi record](https://abs.gazi.edu.tr/yayin/4d70de09-17fc-4bd8-8c3d-9f41708e813f/general-purpose-open-source-1d-self-consistent-schrodinger-poisson-solver-aestimo-1d)
- J. Comput. Electron. published Solcore (2018). [T] — [Springer ESM link](https://media.springernature.com/original/springer-static/esm/art%3A10.1007%2Fs10825-018-1171-3/MediaObjects/10825_2018_1171_MOESM1_ESM.pdf)
- PR Applied published a design-optimisation (BO + NEGF) paper without a new growth experiment as its main contribution. Note: the device record itself was experimental. [F] — [PR Applied 13, 034025](https://link.aps.org/doi/10.1103/PhysRevApplied.13.034025)
- Nanomaterials (MDPI) published a pure-simulation ML surrogate paper in 2026. [F] — [MDPI](https://www.mdpi.com/2079-4991/16/11/651)
- arXiv preprints of pure-theory ML design (Princeton 2024) [F] — [arXiv:2406.07755](https://arxiv.org/abs/2406.07755); J. Appl. Phys. Perspectives (MSP 2023) [F] — [UPM](https://oa.upm.es/86098/)

### Inferences
Ranked opportunity table. Experiment = whether new measurements are required. Status = based on this session's searches.

| # | Paper | Experiment? | Status | Venue(s) |
|---|---|---|---|---|
| D1 | qwkit software paper (integrated ISB-optics chain) | No | Not done | JOSS (fast); CPC/SoftwareX (longer) |
| A2/B3 | Global sensitivity/UQ of QW/QCL/QWIP observables to band and IR parameters | No | Not found | J. Appl. Phys.; Semicond. Sci. Technol.; PR Applied |
| E1 | Differentiable 1D SP with nonparabolicity for gradient inverse design | No | Not found | npj Comput. Mater.; CPC; PR Applied |
| E2 | Robust (fluctuation-aware) heterostructure design vs BO/ML baselines | No | Partially (BO 2020 robustness remarks) | PR Applied; IEEE JQE; Opt. Express |
| C1/C2 | Open MSP solver + MSP–phonon coupling with nonparabolicity | No (reproduce published spectra) | Theory done by Paris group; no open code found | PRB; JOSS |
| C4 | chi(2) under depolarisation/MSP regime | No | Unverified novelty | PRB; Opt. Express; IEEE JQE |
| A1 | Spurious-solution benchmark across 8/14-band discretisations | No | Piecemeal | J. Comput. Electron.; OQE |
| D2/E3 | Cross-code benchmark + open ML dataset | No | Not found | J. Comput. Electron.; Sci. Data; MLST |
| B4 | QW-solar escape-rate model unified across mechanisms | No (fit published data) | Partially (Aeberhard NEGF; Toprasertpong) | J. Appl. Phys.; Prog. Photovolt. |
| F1/F2 | Detailed-balance limits for MQW TPV / hot-carrier with subband physics | No | Partially (classic); modern open version missing | PR Applied; J. Appl. Phys. |
| A3 | Landscape/disorder continuum vs atomistic TB for InGaN QWs | No | Partially | PRB; J. Appl. Phys. |
| D3 | Tutorial: reproducible ISB modelling in Python | No | Not found | J. Appl. Phys. Tutorials; Eur. J. Phys. |

- Things a solo theorist should avoid or only approach via collaboration:
  - A full open QCL NEGF code: a large engineering effort that competes with nextnano.NEGF and group codes.
  - Self-consistent GW in NEGF: high cost; only demonstrated for nanotubes (2307.05297).
  - Experimental-validation claims for new device records.
- Venue fit (inference):
  - JOSS: short paper, requires the software be primary and open.
  - CPC/SoftwareX: methods plus validation.
  - J. Comput. Electron.: numerical methods for devices.
  - PRB: needs a physics result, not just a code.
  - PR Applied: needs device relevance and design insight.
  - IEEE JQE / Opt. Quantum Electron.: device-modelling tradition (NUSOD).
  - Semicond. Sci. Technol.: parameter/UQ studies.

### Gaps
- Not checked: whether JOSS accepts code that duplicates Aestimo/ErwinJr2 functionality. JOSS reviews "substantial scholarly effort" and novelty of software; check JOSS review criteria directly.
- No venue acceptance statistics or APCs were retrieved.
- Novelty of each "not found" opportunity must be confirmed with a bibliographic database. Web search here was limited to about 30 queries and fetches, and several pages (SciPost, paywalled publishers) were inaccessible.
