# Parked for a later stage (N1 paper, before submission)

Saved on 10 October 2026 at the author's request. None of these blocks further research.

0. URGENT for N1 (11 Oct 2026): the comparison was revised. With the Stark off field restricted to fields where the
   single-period model is valid and then optimized, Stark on/off QPM overtakes the triple well above ~3 W, and an
   ordinary ADQW with both segment fields optimized (opposite polarities, Stark-detuned segments) is 1.3-2.0x more
   efficient than the best triple-well pattern (studies/n1_paper/stark_valid.py, stark_offscan.py, twofield_qpm.py,
   twofield_tw.py, twofield_best.py; N1 Secs. 4.6-4.7, abstract and conclusion rewritten). Item 1 below is now
   essential: Vurgaftman et al., Solid State Commun. 100, 663 (1996), "Detuned intersubband resonances for broadband
   field-modulated second-harmonic generation", may already describe the winning field-detuned pattern. Also consider
   whether N1 should be reframed around bias-programmed QPM (sign reversal + field detuning) rather than the triple
   well alone, and a multi-period model for fields above ~100-140 kV/cm (interperiod hybridization).
   UPDATE 12 Oct 2026: Vurgaftman et al., SSC 100, 663 (1996) read (author-supplied scan). It uses a UNIFORM field to
   tune the coherence length (switch-off at -25 kV/cm; >=1% from 9 to 20 um) and does not alternate polarity or
   reverse chi2, so the bipolar ADQW pattern is not anticipated; N1 now describes it accurately. Yu et al., Sci. Adv.
   2025 demonstrated bias-programmed chi2 phase by Stark detuning in a metasurface (cited in N1). Both strengthen the
   case for reframing N1 around bias-programmed QPM; the decision remains the author's.
1. Read in full, through the OU library (exact references, from L. R. Ram-Mohan's publication list):
   (a) J. R. Meyer, C. A. Hoffman, F. J. Bartoli and L. R. Ram-Mohan, "Intersubband second-harmonic generation with
       voltage-controlled phase matching", Appl. Phys. Lett. 67, 608-610 (1995), doi:10.1063/1.115404.
   (b) I. Vurgaftman, J. R. Meyer and L. R. Ram-Mohan, "Detuned intersubband resonances for broadband
       field-modulated second-harmonic generation", Solid State Commun. 100, 663-667 (1996),
       doi:10.1016/0038-1098(96)00493-0 (DOI as recorded earlier; check on the publisher page).
   Also worth a look if the library has them (same group, 1996): "Phase matching in waveguide-mode intersubband
   chi(2)(2w) devices", CLEO/QELS 1996 Technical Digest Vol. 9, pp. 274-275; and J. R. Meyer et al., "Momentum-space
   reservoir for enhancement of intersubband second-harmonic generation", IEEE J. Quantum Electron. 31, 706-714
   (1995) (saturation suppression; relevant to NL-02).
   If either (a) or (b) analyses symmetric coupled wells with bias-polarity reversal, cite it with the patents in Sec. 1.
   STATUS 12 Oct 2026: (b) DONE (no polarity reversal; see item 0). (a) STILL NEEDED: the file supplied as (a) was a
   different paper by the same four authors, "Type-II quantum-well lasers for the mid-wavelength infrared", Appl.
   Phys. Lett. 67, 757-759 (1995). The DOI listed above for (a) was never verified and is withdrawn. Request: the
   paper titled "Intersubband second-harmonic generation with voltage-controlled phase matching", Appl. Phys. Lett.
   vol. 67, starting page 608 (1995), same four authors (listed as entry 11 of Ram-Mohan's nonlinear-optics
   publication list; cited as ref. 13 of the SSC paper). Search the APL table of contents for vol. 67 by page 608.
2. DONE 11 Oct 2026: U.S. Patent 5,289,309 inventor is Jean-Paul Pocholle (the Thomson-CSF co-author of Delacourt
   and Papuchon, e.g. Julien et al., Appl. Phys. Lett. 53, 116 (1988), lists "J. P. Pocholle"; Google Patents'
   "Jean-Claude" is a transcription error). Bibliography now "J.-P. Pocholle".
3. Deposit this archive on GitHub + Zenodo for a DOI and cite it where the paper says the package is
   supplied with the article.
4. Ask one colleague who did not do the work to attack the central claim.

5. DONE 12 Oct 2026 (PDF supplied): see docs/LIT_REVIEW_2026-10-12.md. Bias rotates the chi2 phase by detuning
   (cardioid); the pi offset is geometric (flipped meta-atoms); it is a local phase grating, not propagation QPM.
   The companion THG paper is S. Park, J. Yu, G. Boehm, M. A. Belkin, J. Lee, Light Sci. Appl. 13, 169 (2024),
   doi:10.1038/s41377-024-01517-y (identified from ref. 15 of the Sci. Adv. paper). The file supplied for it was a
   different LSA paper (Zhou et al., LSA 13, 242 (2024), liquid-crystal singlets); the THG paper is only needed for
   NL-31 (below), open access. Original entry: Exact reference (verified 12 Oct 2026; open access, so the PDF is free from the publisher):
   J. Yu, J. Kim, H. Chung, J. Son, G. Boehm, M. A. Belkin and J. Lee, "Full complex amplitude control of
   second-harmonic generation via electrically tunable intersubband polaritonic metasurfaces", Science Advances
   11(30), eadw8852 (2025), doi:10.1126/sciadv.adw8852 (UNIST / TU Munich). NOT the 2025 yeast DNA-repair paper by
   another Yu. Question for N1: does the bias reverse the chi(2) sign/phase, and is it a local metasurface phase
   grating rather than propagation QPM? Companion paper to cite: "Electrically tunable third-harmonic generation
   using intersubband polaritonic metasurfaces", Light Sci. Appl. 13 (2024), doi:10.1038/s41377-024-01517-y
   (article number and author list still to be confirmed; publisher pages rate-limited this session).

## qwkit software paper (paper 1 of the programme), parked steps

6. Publish the code: run `tools/export_public.sh`, review the public tree (drop the "Project folder contents"
   README section), create the GitHub repository, push, confirm CI passes on Linux/macOS/Windows, tag v0.5.0,
   and archive the release on Zenodo for a DOI. Cite the URL and DOI in the software paper's Availability section.
7. Choose the software-paper venue. JOSS (2026 rules) needs six months of public development history, evidence
   of research use and an AI-usage disclosure section, so it is not possible before about April 2027.
   Alternatives: SoftwareX or Computer Physics Communications (both require a code-metadata table and a public
   repository; check their current AI-use policies), or Journal of Computational Electronics.
8. Add an ORCID (paper and CITATION.cff) and a contact e-mail (code of conduct, paper) if the venue requires them,
   plus any funding / competing-interest / data-availability declarations the venue asks for.
9. Post the N1 manuscript as a preprint (or submit it) so the software paper can cite it as more than
   "in preparation".

## NL-02 (saturation-limits paper) and N1 follow-up, parked steps

10. DONE 11 Oct 2026 (`studies/n1_paper/detuned_qpm.py`, N1 new Table 4 and text): with each scheme at its own best
    red detuning, the triple well gives 1.6-1.7x growth reversal and 1.9-6.6x Stark QPM at 10 W, 1.06-1.23x and
    1.25-4.6x at 4 W, and is comparable at 1.26 W (0.84-1.03x growth reversal; 0.95x detuned Stark at 5e11).
    Abstract and conclusion updated. Original item: repeat its QPM-scheme comparison (Table 3) with a red-detuned pump. NL-02 shows the
    resonant 10 W operating point lies beyond the conservative rate-equation limit (~4 W) and that tuning the pump
    25-35 meV below resonance gives 3-6x higher efficiency inside that limit (`studies/nl02/hw_scan.py`).
11. DONE 12 Oct 2026 (thesis supplied, read in full): the thesis DOES contain the symmetric-ladder special case of
    Theorem 1 (Eq. 9.15, Omega T2/e, independent of dipole magnitude, density and detuning), a length-limited bound
    (Eq. 9.37) and the numerical no-ceiling observation (Fig. 9.6). NL-02 rewritten to credit them; the general
    identity, Theorem 2, closed-form slope, detuning rule and validations remain new; new length_bound.py generalizes
    Eq. 9.37. Krakofsky author list: still to complete. Original entry: Before submitting NL-02: obtain and read in full Almogy & Yariv, Opt. Lett. 19, 1828 (1994), Almogy's 1995
    Caltech thesis, and Vurgaftman, Meyer & Ram-Mohan, IEEE JQE 32, 1334 (1996); confirm that neither states the
    identity |chi2|^2 = Q a_w a_2w, the Rabi bound, or the waveguide no-ceiling result, and adjust the
    prior-work paragraph if they do. Complete the author list of Krakofsky et al., Nat. Photon. 20, 699 (2026).
12a. DONE 11 Oct 2026: Vurgaftman, Meyer & Ram-Mohan, IEEE JQE 32, 1334 (1996) read and compared in NL-02.
    DONE 12 Oct 2026: Almogy thesis (contains the JNOPM material as Chs. 5-9). Optional only: the JNOPM paper itself
    and a "J. Opt. Soc. Am. B, in press" paper by Almogy & Yariv, "Fundamental limits of resonantly-enhanced
    second-harmonic generation", which a search did not find in print. Originally listed: Almogy & Yariv, J. Nonlinear Opt. Phys. Mater. 4, 401-458 (1995), doi 10.1142/S0218863595000173,
    and Almogy's 1995 Caltech thesis, "Quantum Well Intersubband Transitions: Nonlinear Optics, Refractive Index and
    Infrared Modulation" (doi 10.7907/3qj9-9777; free PDF at https://thesis.library.caltech.edu/3642/ but blocked from
    this workspace) - the remaining places where a prior form of the
    identity or of the limits could appear; also Almogy & Yariv, Opt. Lett. 19, 1828 (1994).
12. NL-02 venue: Phys. Rev. Applied, Optica or Opt. Express (check each venue's AI-use policy first).

## NL-05 (collective-effects paper), parked steps

13. DONE 11 Oct 2026: Zaluzny, Phys. Rev. B 51, 9757 (1995) and Phys. Rev. B 47, 3995 (1993) read in full (library
    copies supplied). PRB 51, 9757 already contains the excited-state factor (his c(omega), kappa_exc = alpha32bar/alpha22)
    and the energy-substitution = diagonal-approximation statement; NL-05 now credits this, reproduces his GaAs step-well
    example (`studies/nl05/zaluzny95.py`: optimum step height and photon energy within 1.2 meV; enhancement 2.10 vs his
    2.5) and shows the diagonal Hartree terms reduce it to 1.87. PRB 47, 3995 (two-level, intensity-dependent shift,
    remark on the static space-charge field) is cited in Sec. 8. The "Bondarenko & Zaluzny, JPCM 12, 8267 (2000)"
    citation was wrong (that page range is an unrelated 2001 paper) and has been removed. An ETDEWEB/OSTI record titled
    "Effects of the Coulomb interaction on intersubband doubling and difference-frequency mixing in asymmetric double
    quantum wells" (osti.gov/etdeweb/biblio/20114215) exists but its journal is unidentified; if the library can find
    it, read it and compare with NL-05. Optional: Zaluzny, Acta Phys. Pol. A 90, 1118 (1996); Todorov & Sirtori on
    overlap-coupled intersubband plasmons.
14. DONE 12 Oct 2026 (PDF supplied by the author): Krieguer & Todorov, arXiv:2412.08297 (v1, 11 Dec 2024), Sec. II B
    read in full. Three-subband GaAs/Al0.3Ga0.7As double wells, only the ground subband occupied, flat bands (no
    donor Hartree potential), static/population terms averaged out in cavity geometry, chi2 proportional to d23
    (no permanent-dipole terms). They find the optimum moves from the single-particle doubly resonant 2.7/1/8.3 nm
    to the collective double resonance 3.6/1/7.4 nm, with ~3x the single-particle chi2 at 1.8e12 cm^-2, and that in
    strong coupling polariton-matched designs (Eq. 188) beat doubly resonant ones (40 vs ~6 W^-1). NL-05 now has a
    benchmark subsection (`studies/nl05/krieguer24.py`, Table 2): design shift reproduced; enhancement 2.42 vs ~3;
    planar permanent-dipole and diagonal-Hartree differences quantified; intro and discussion statements corrected.
    No journal version found as of Oct 2026.
15. Open questions flagged in NL-05: the factor of up to ~2 between TDH and the quasi-static rate model above
    3 MW/cm^2 at 2e12 cm^-2; exchange-correlation (TDLDA) and k-resolved in-plane nonparabolicity (NL-28);
    static permittivity for the charge-transfer field. NL-05 venue: Phys. Rev. B (check its AI-use policy).

Other submission items (venue, template, AI-use policy, e-mail/funding line) are in SUBMISSION_CHECKLIST.md.

## MS-02/MS-03 (sensitivities, UQ and growth-tolerant design), parked steps

16. Venue: Comput. Phys. Commun., J. Comput. Electron. or Phys. Rev. Applied (check each AI-use policy first).
17. Optional strengthening, not needed for submission: Sobol indices for the resonant quantities (Saltelli
    estimator, ~10^4 forward solves); Anderson mixing in `sens.Model.forward` (the forward solve, not the tangents,
    dominates cost); Sternheimer (bordered tridiagonal) application of the resolvents for O(nN^2) tangents;
    co-design of thicknesses and nominal bias for trimming; a second design study on the triple well.
18. The ADQW and triple-well designs come from the unpublished N1 manuscript; post or submit N1 first so MS-02 can
    cite it.

## TPV-05 (switchable ISB thermal emitters), parked steps

19. GaN/AlN wells: add polarization fields to the solver and repeat the study; this is where the switching limits
    found for arsenide wells should lift (Noda-group GaN emitters: 800 C static, ~500 C modulated).
20. Model the actual Noda device (p-n diode, p-GaAs hole absorption, 10 V, 473 K, measured Q_r and Q_abs from
    Inoue et al., PRB 91, 235316 (2015)) for a sharper validation of the contrast.
21. Optional: thermally averaged LO dephasing with vertex corrections; L valleys from a multivalley Schroedinger
    solve; quantum-well (excitonic) interband background; a measured thermo-optic coefficient for the resonator.
22. Venue: Phys. Rev. Applied, ACS Photonics or J. Appl. Phys. (check AI-use policies).

## New threads opened by the 12 Oct 2026 literature review (docs/LIT_REVIEW_2026-10-12.md)

23. NL-31 (new paper): collective intersubband effects in electrically programmable chi2 metasurfaces. Benchmarks:
    Yu et al., Sci. Adv. 11, eadw8852 (2025) (SHG, cardioid), Park et al., LSA 13, 169 (2024) (THG; PDF needed,
    open access, doi:10.1038/s41377-024-01517-y), Yu et al., Nat. Photon. 16, 72 (2022). Scoping
    (studies/scoping/yu25.py): at 1.47e12 cm^-2 per period the TDH response changes the chi2(V) trajectory from a
    near-cardioid to one winding around the origin, and qwkit's Stark slope is 2x the measured one, as the authors
    note. Questions: equal Stark coefficients for dressed (depolarization-shifted) transitions; single-meta-atom 2pi
    coverage from collective effects; self-consistent field screening in the doped 500-nm stack.
24. N1 extension: "cardioid" triple wells (equal Stark coefficients for E21 and E32) as the active medium for bipolar
    Stark QPM: exact pi phase difference at equal |chi2| for +V and -V. Compare with the bipolar ADQW of N1 Sec. 4.7.
25. MS-01/MAT benchmark: Almogy thesis Ch. 10 coupled-well charge-transfer modulator (GaAs/Al0.4Ga0.6As 9/3/10.8 nm,
    storage well doped 2e18 in 4 nm, 42.2 nm period barriers, 50 periods): measured transfer per volt 15% above
    Hartree (exchange), population-dependent blue shift and broadening. Tests qwkit's bias + XC treatment.
26. TPV-06 (candidate): ISB emissivity switching by intra-period charge transfer (Almogy-type coupled wells) instead
    of depletion; avoids the generation leakage that limits TPV-05's depletion switches above 320-740 K.

## MAT-01 (LaInO3/BaSnO3 2DEG intersubband optics), parked steps

27. READ BEFORE SUBMISSION (could not be opened here): the 2026 Physical Review B article with DOI
    10.1103/8z9v-d6s9, titled "Small effective mass deep all-oxide quantum wells based on ..." (vol. 113, issue 7 table of
    contents). Probably the journal version of the Demkov-group BaSnO3 quantum-well work (Jang MA thesis 2023). Check
    whether it reports MEASURED intersubband absorption in BaSnO3 wells; if so, compare and position MAT-01 against it.
28. The Li, Hamze & Demkov (PRB 104, 235419, 2021) Supplemental Material holds their layer thicknesses, BaO parameters
    and solver details; with it their chi(2) spectra could be reproduced as a code benchmark (main text insufficient).
29. LaInO3 infrared phonons (TO/LO, eps_inf) are unknown; a DFPT calculation or IR ellipsometry would allow interface
    and cap phonons in the lifetime model.
30. DONE 13 Oct 2026: all studies re-run after the boundary, Loewdin-order and solver changes; manuscripts updated:
    N1 (symmetric-well comparison now limited to the 140 kV/cm validity range, shaded in Fig. 2a; ADQW bipolar range
    +-60-120 kV/cm; rerun_n1.sh completed), NL-05 (above-band-edge resonances flagged and excluded from headline
    ranges), NL-02 (four numbers), MS-02 (cost claims rebuilt on the matrix-free tangents, item 34).
31. DONE 13 Oct 2026 (sentences in all five papers). Kane two-band metric (12 Oct 2026, core.kane_valence / kane_dipoles, test added). The one-band nonparabolic states
    overlap by up to 0.08 in InGaAs/InAlAs ADQWs; as two-component Kane states they are orthogonal to < 6e-4 with no
    Loewdin step. Dipole products z12 z23 z13 differ from the Loewdin values by -1 to -3% (64.5/18/36.5: -0.9%,
    70/12/32: -0.9%, 58/14/34: -3.3%). Also fixed: core.analyze and sp.prepare now Loewdin-orthonormalize all localized
    states before truncating (truncating first changed z13 by up to 4% with nkeep). Each manuscript (N1, NL-02, NL-05,
    MS-02, MAT-01) needs one check sentence with its own numbers; MAT-01: studies/mat01/kane_check.py (DONE, in text);
    III-V: studies/kane/kane_check_all.py (peak ground-state chi2 of the ADQWs changes by -0.2 to -2.8% with Kane
    dipoles; localized-state two-band overlaps < 1e-4). Valence components carried into
    the Hartree kernel as well (studies/mat01/kane_rpa.py): MAT-01 collective centroids -2.2 to -2.6%. Same check
    for the III-V TDH results (NL-05 depolarization shifts) still to do; the density in Poisson could include |phi|^2.
32. NEW THREAD (MAT-01 revision, 12 Oct 2026): electrostatics of electrolyte gating through a polar cap. With the gate
    charge on the surface of a 5 nm LaInO3 cap (eps 24, CBO 1.6 eV), the cap surface reaches the Fermi level after
    only 1.6-2.5e13 cm^-2 of added density (studies/mat01/gating.py; eps 50: 2.6-4.2e13; 2 nm cap: 3.0-4.7e13),
    yet Lee et al. (Adv. Electron. Mater. 2400811) report ~1e14 cm^-2 with DEME-TFSI on 5 nm LIO. Candidate
    explanations: field-dependent (nonlinear) LIO permittivity, larger offset, charge trapped at/near the LIO surface
    (Hall would count mobile surface carriers), electrochemical (oxygen-vacancy) doping. Possible short paper
    "MAT-02": what ISB spectroscopy (field at the interface) can tell apart; needs the LIO dielectric response
    and the published n(V_G), mu(V_G) curves of Lee et al. (ask the user for the full PDF + SI if pursued).
33. MAT-01 fixes of 12 Oct 2026 evening (all MAT-01 studies re-run): interface Poisson half-cell offset (E21 +4-6 meV at
    1e14, grid-independent now), discontinuous depletion charge (self-consistency oscillated, residuals up to 20 meV),
    Loewdin truncation (top-state spurious dipoles), median instead of centroid as the location measure (the centroid
    of omega-weighted Lorentzians is window-biased by up to 25-75%).
34. MS-02 after the boundary fix and the 5-8x faster forward solver: the paper's cost headline ("Jacobian ~1/10 of a
    forward solve") had become false (~1x). Fixed 13 Oct 2026 by making qwkit.sens matrix-free (tridiagonal
    reduced resolvents + GMRES on the Hartree feedback); MS-02 re-run (studies/ms02, pre_matrixfree/ keeps the
    previous outputs) and manuscript to be updated with the new timings and the dense-vs-matrix-free comparison.
    Also fixed: observables kept the lowest nkeep states instead of the most localized ones (59/200 TW UQ samples).
35. MS-01 (qwkit software paper) must be brought up to date before submission: new modules (interface, krpa,
    thermal, sens matrix-free), Kane two-band dipoles, 55 tests, the bug fixes of 12-13 Oct 2026 (CHANGELOG).
36. FOUND 13 Oct 2026 (number audits): buffered Loewdin. Orthonormalizing only the localized states (sp.prepare,
    core.analyze, sens.observables, thermal.emitter_state up to 0.6.0) gives the top localized state spurious dipoles
    when few states are localized: ADQW 64/10/29 in the 200 A box has 3 localized states and z13 came out 8.77 A
    against 8.22 (two-band Kane) and 8.26-8.28 (Loewdin over the box states as well); |chi2| ~8% too large; TW z14 5%
    too large; the earlier Kane checks (100 A box) hid it (studies/kane/box_scan.py). Fixed in qwkit 0.6.1
    (core.lowdin_localized: Loewdin over the localized states plus >= 10 box states above them, residual vs Kane
    <= 0.7%; sens: model.nstates raised to ADQW 10, TW 12 in studies/ms02/common.py; test added). Full regeneration
    of N1, NL-02, NL-05, TPV-05, MS-02 started 13 Oct 20:03 (studies/queue_lowdin.sh, outputs before the fix in
    studies/pre_lowdinfix/). Afterwards: jsondiff, update every manuscript (the Kane sentences of N1/NL-05/MS-02 must
    be redone: the -8.8% / -8.1% differences were mostly this artefact), MS-02 timings (validate2 re-run first on an
    idle machine; design4 wall times must be checked for contention with the MAT-02 runs), MAT-01 III-V reference
    (done: 3490 -> 3480, 555 -> 554 nm^2/V).
37. N1 reframing (after item 36): the paper's own results make the bipolar-biased ordinary ADQW the most efficient
    electrical scheme (1.8-2.4x the triple well above 1 W) through Stark-detuning phase reversal (the mechanism of
    Yu et al., Sci. Adv. 11, eadw8852 (2025), in metasurfaces); the triple well's value is the exact sign grating.
    Title/abstract/contributions/conclusion to be reframed around "electrically written QPM" with both mechanisms.
    Meyer et al. APL 67 (1995) (voltage-controlled true phase matching, uniform field) is not needed to prove any
    finding; reading it before submission would secure the novelty statements.
38. MAT-02 started 13 Oct 2026 (studies/mat02): interface.solve gained nd_cap (ionized donors in the cap, e.g.
    electrolyte-created oxygen vacancies; Gauss test added). gate_map.py: where the added positive charge must sit
    for n0 = 5e12 -> n_s = 3e13 ... 1.2e14 without cap filling; donor sheets within ~6 A of the interface at 7e13
    (compensated, eps 24); pure double-layer gating needs offsets > 2.5 eV above 5e13, beyond the gap-difference
    bound (~1.9-2 eV); even a field-free cap fills at 1.08e14 (compensated). Next: clean case, spectra.py (ISB
    observables per scenario; Gauss makes the well side blind to where the positive charge sits unless the cap fills),
    UQ of the required x_max over the MAT-01 parameter ranges, manuscript.
39. 14 Oct 2026 status of item 36: N1, NL-02, NL-05, TPV-05 manuscripts updated to 0.6.1 outputs (N1 reframed:
    "Electrically written quasi-phase matching ...: bias-reversed asymmetric and mirror-symmetric quantum wells");
    NL-02 ladders now read from qwkit_validation.json (were hard-coded pre-fix values); stepwell.py reads the ADQW
    from tables.json; TPV-05 got collect_numbers.py + audit_extras.py (three wrong claims corrected: depolarization
    shift 0.2-5.5 meV, k=0 vs full dispersion 10-15% wider line, 2D DOS factor 2.6). MS-02 rerun finishing; then:
    design4 wall times must be re-measured on an idle machine (they ran concurrently with MAT-02 jobs), MS-02 and
    the software paper's sens timing sentence (line ~190) updated, kane_check_all.log regenerated (ms02 rerun does it).
40. Parked, small: (a) TPV-05 emitter.py uses AlGaAs nonparabolicity energy 1.84 eV, noda_check.py 1.80 (0.2 meV in
    the GaAs peak) - unify; sweep.py docstring cites a nonexistent gamma0_sens.py. (b) thermal.inplane_masses k = 0
    masses are lighter than the exact band-edge masses at 1000 K (0.056/0.076 vs 0.065/0.096); TPV-05 now states the
    full-dispersion effect (line 10-15% wider, peak -8%, ratio unchanged); consider switching thermal to exact
    in-plane dispersion. (c) docs/guide.tex user guide is out of date (25 tests, no extension modules). (d) NL-05:
    the ~110 meV Fermi-energy estimate has no stored output.
41. MAT-02 referee-style review (14 Oct 2026) found: the "field-free" case left the change of the depletion charge
    on the cap surface (compensated margins 0.12-0.17 eV too small); fixed with interface.solve(rest_to=...) and
    common2.solve_placed; Lee et al.'s vacancy remark is general (they interpret their data as EDL accumulation);
    7.0e13 (10 K) and 1.08e14 (150 K) are the same frozen gate state (n drops on cooling); the 1.08e14 limit must use
    150 K; clean case now on the 0.5 A grid; ISB "signature" claims to be restated (E-bar vs Hall density is not
    universal); Galazka2021 bib entry was the wrong paper (fixed in MAT-01 and MAT-02). All MAT-02 studies re-running.
42. MAT-03 (14 Oct 2026, studies/mat03, paper_mat03, qwkit 0.6.2 transport.py). Lee et al. main text only (SI
    unavailable): Fig. 3b, Fig. 3a (5-8 V) and Fig. 5a (MR at 2 K, 3/5/7 V) digitized. Two independent reviews.
    Round 1: Siggia-Kwok velocity factor fixed; dielectric boundary eps_cap; coupled magnetotransport; 4 V/6 V data;
    protocol (measured while warming, DEME-TFSI T_g 182 K). Round 2: coupled subbands = independent Drude eigenmodes
    (identity, tested), so the MR bound is posed over all 2- and 3-channel sets matching sigma and the FITTED n_H
    (mr.py): at 7 V a flat MR needs >= 22-24% of electrons below 200 cm^2/Vs (2 channels: 26-29% below 22-48);
    5 V unconstrained. Coulomb scattering (both limits of the unidentified scattering, matched rows) gives n_H/n_tot
    0.92-1.00 / 0.97-0.99 / 0.96-1.00 at 5/7/8 V. Conclusion: ~2e13 cm^-2 immobile (trapped/localized) electrons at
    7 V; [superseded by item 48: the trap-release reading fails at fixed charge]. R_s upturn at
    7-8 V not WL (MR cusp: WL 2-4%). Conductance bound vs MAT-02 x_max: consistent within ~1.5 (clean, Z=1);
    compensated BSO needs 3-8x less scattering (eps 24). Reviewer's venue: Comment on Lee et al. (Adv. Electron.
    Mater.), or short JAP / PR Materials paper. MAT-02's drop paragraph updated to match.
43. METH-01 (14 Oct 2026, studies/meth01, paper_meth01), revised after review: fixed potentials, bound = below the
    barrier edge; exact discrete two-band partner (overlaps 1e-13). Raw 2-8% (origin-dependent), norm-only 5-14%
    (worse), L-bound top-state 5-7% (chi2 +9%, box-independent), 0.5 eV buffer <= 0.76%, fixed 2/10-state buffers
    degrade with box (to 5.8% / 1.4%), complete one-band Loewdin converges to its own limit 0.25-0.49% off (0.16-0.26%
    with uniform hbar^2 Eg / 2m*). Reviewer's venue advice: fold into the software paper (MS-01) or a short JAP note;
    user decision.
44. qwkit 0.6.2 (14 Oct 2026): transport (Coulomb/dislocation/roughness, RPA screening, Siggia-Kwok with v_j/v_i,
    eps_cap boundary, coupled magnetotransport), exact discrete kane_valence, lowdin_localized(ebuf), 66 tests.
    Earlier manuscripts cite 0.6.1 (their outputs unchanged at quoted precision).
45. N2 groundwork (studies/n2): chimap.json (ADQW -140..140, TW -100..100 kV/cm state sets, 93/98 valid), grating.py
    (small-signal segment propagation, validated against propagation.propagate_segments to 1e-3; phase-following
    synthesis + coordinate refinement). tuning.py (small signal, ns 5e11): programming each electrode's bias
    (continuous set) beats the fixed N1 grating by 1.9x (ADQW) / 2.2x (TW) at the design wavelength and 4-9x when
    detuned 20-50 meV; binary +-F programming only retunes; pitch 2-8 um hardly matters. Next: saturated
    propagation (W-level pumps, N1 regime), bandwidth (chirp) study, then the THz DFG module (P3.C4).
46. MAT-04 scoping (studies/mat04, 14 Oct 2026). Prior art found: Li/Hamze/Demkov PRB 104, 235419 (2021); Jin, Jang,
    Guo, Li, Posadas, Demkov, "Small effective mass deep all-oxide quantum wells based on BaSnO3", PRB 113, 075112
    (2026) (abstract not obtained; likely Al2O3/BaSnO3 growth + offsets, no chi2 or depolarization); Stanojevic,
    Vukovic, Radovanovic, Opt. Quantum Electron. 55, 383 (2023) (BSO/BaO ISB absorption); Jang APS 2022/2023 and MA
    thesis 2023. No paper includes depolarization or polar-phonon effects for BSO wells. scoping.py (Li's DQW,
    4.5e12 cm^-2): depolarization shifts E21 by 2-36 meV and E31 by 27-47 meV; peak |chi2| changes x0.8-2.0; the
    unknown BaO barrier thickness (2.5 vs 5.5 A) and mass (0.4 vs 1.0 m0) change |chi2| from 6 to 279 nm/V. A
    MAT-04 paper needs Li's Supplemental Material (barrier parameters) and ideally the PRB 113 full text.
47. MAT-03 data verification (15 Oct 2026, studies/mat03/digitization/VERIFICATION.md). Fig. 3b re-digitized by
    marker centroids and checked against Fig. 4 (mu vs n at 10/150 K) and Lee's text: 4-8 V within 0.6% (n) and
    1.5% (mu); 5 V verified three ways (<= 1.5%). Corrections: 4 V mu at 10 K 517 -> 435 (hidden in Fig. 3b), 6 V
    from Fig. 4 at 10/150 K. Dense Fig. 5a MR: 2->7 T change -0.12 (5 V) / -0.06 (7 V) points vs -0.07/-0.08 used
    (inside the 0.5/1.0-point tolerances). All MAT-03 outputs regenerated from lee_fig3b_v2.json (old: pre_digv2/).
48. MAT-03 trapping explanation FAILED verification (15 Oct 2026, studies/mat03/trapping.py, localization.py;
    independent agent review, two rounds). At fixed total charge, removing the Hall-density deficit from the band
    lowers E_F by 40-52 / 91-103 / 171-182 meV (vs E1; 5/7/8 V). A fixed-level trap fills on cooling only with entropy
    S >= dE_F/dT: 11-35 k_B (E1) or 21-65 k_B (interface edge) already between 2 and 10 K (third law: impossible).
    LP (any level spectrum, freezing temperatures, S -40..+5 k_B, three references, tol 2%): for |S| <= 2 k_B the
    fewest traps are 5e12 / 5e14 / 1.5e16 / >1e18 cm^-2 at 4/5/7/8 V (interface: 5.9e14 sites); the deficit itself
    only for S <= -10 (7 V) / -20 (8 V) k_B (LP sign; paper uses S_t = -S). The first LP version scanned S on the wrong side and mislabelled solver
    failures (reviewer); fixed. The old release-counting estimate ignored the E_F shift and was wrong. A fixed slow
    fraction (two-channel reparametrization) needs a metal-like slow channel (7-31 e^2/h at 10-50 K at 7 V) that
    switches off below 10 K, and predicts a 4.9% R_xy bend at 8 V, 50-100 K, in tension with Lee's "linear at all
    temperatures". Paper now says: 2 K immobile quarter at 7 V is required; how it forms at fixed charge is open.
    MAT-02's drop paragraph aligned. Open: Lee's SI Hall resistances (S2, S3) would test the 8 V prediction directly;
    the conductance bound (Sec. 4.3) assumes all n_tot in the 2DEG.
49. METH-01 placement decided (15 Oct 2026): standalone short methods paper (target J. Comput. Electron.; JAP as
    alternative), the methods reference for the dipole procedure of every application paper; the software paper
    (MS-01) now cites it and summarizes rather than repeats it. Software paper brought to qwkit 0.6.2 (twelve
    modules, transport module and validation row, 66 tests, MAT-03 in research use). Application papers (N1, NL-02,
    NL-05, TPV-05, MS-02, MAT-01) may cite METH-01 for the Kane/Loewdin check at submission time.
50. Delivery convention (user, 15 Oct 2026): deliver the framework as numbered zips: 1-roadmap.zip (roadmap,
    supplementary documents, LITERATURE_STATUS.md, qwkit package, tests, tools, docs), then one zip per paper,
    2-papers.zip, 3-papers.zip, ... in programme order; a new paper gets the next number
    (tools/package_framework.py). Literature not found or bought is tracked in the Roadmap doc and LITERATURE_STATUS.md.
51. N1 CONSISTENCY ITEM (found by N2 and its review, 15 Oct 2026; studies/n2/n1_check.py). N1 scaled all electrical
    patterns by the TW electrode factor (eta_e = 0.92). With actual fringing fields (electrode 5.31 um above ground,
    three stack heights) in N1's own conventions (no index saturation, no breakdown limit), at 5e11 cm^-2 and the
    design energy: N1's best ADQW pair (-100,+120) gives 0.296% at 1.26 W (N1 scaled: 0.353%), but re-choosing the
    pair under realistic fields, (+80,-40), restores 0.345%; at 10 W the realistic optimum (+120,-80) is 2.31% (N1
    scaled 2.14%); TW 0.197% / 1.01% (N1 0.190% / 0.970%). N1's ordering stands; its best ADQW pairs change, and
    they put 117-127 V across a 2 um gap (> 0.5 MV/cm lateral breakdown). N1 also omits the saturation of the ISB
    index in dk (0.2-3% here). Before submission: re-evaluate N1's electrical schemes with field profiles and a
    breakdown limit (n2 machinery), at both densities and all detunings, and replace the eta_e scaling.
52. N2 drafted (15 Oct 2026; paper_n2/, studies/n2/, N2_paper.pdf, zip 12). Electrically programmable ISB SHG
    gratings with realistic electrode fields (Laplace, electrode 5.31 um above ground), lateral-breakdown limit,
    index saturation and pump depletion; benchmarks optimized under the same fields (and, separately, under abrupt
    fields with the same search). Design energy, 5e11 cm^-2: programmed / best periodic 1.20-1.22 (ADQW, 0.01-10 W;
    0.431% at 1.26 W, 2.76% at 10 W) and 1.08-1.43 (TW); with abrupt fields 1.31-1.80 at 1.26-10 W, so fringing
    removes 41-74% of the extra gain. 1e11 cm^-2: 1.21-1.39 (ADQW), 1.15-1.55 (TW), devices 0.3-0.6 mm.
    Tuning (-40..+10 meV, 1.26 W): reprogrammed / retuned fixed device 1.20-1.80 (ADQW), 1.12-1.62 (TW); the TW is
    better 10 meV below the N1 design energy even as a fixed device. Array: pitch 2-8 um adequate (the 2 um loss is
    the breakdown limit of 1 um gaps, as a 4 um array with 1 um gaps shows); nine evenly spaced levels (+-74 V) give
    97% of all biases; the breakdown limit costs 6%. Two agent review rounds, all findings addressed.
    Open: patterns are local optima (realistic refinement cannot add electrodes), so gains are lower bounds; 2D
    electrostatics ignore ridge-edge fringing; level placement not optimized; venue (Phys. Rev. Applied or Opt.
    Express) after N1 (P1.4) and N1 item 51. Difference-frequency extension waits for the qwkit DFG module (P3.C4).
53. Pre-review pass (20 Oct 2026; working folder QW_research, one repository per paper, Zenodo v1.0.0 DOIs).
    Self-containment: in its own folder, NL-02, N1, N2 and MAT-03 could not run their figure/number scripts, and the
    MAT-02 re-computation scripts could not start, because they read modules or outputs of companion studies. The
    needed files are now copied into each folder at the same relative path, with README_UPSTREAM.md naming the origin
    archive and the generating script (N1: 5 files from nl02; NL-02: 7 from n1_paper; N2: 9 from n1_paper and 1 from
    nl02; MAT-02: 3 modules from mat01; MAT-03: mat01/common.py and 2 mat02 outputs). Checked by running prove_paper.py
    and starting every study script in an isolated copy of each folder. Not redistributable and not included: the
    600 dpi crops of Lee et al.'s figures used by studies/mat03/digitization (the digitized JSON values are included).
    Manuscripts: Data and code availability statement before the references (qwkit DOI and the paper's own DOI);
    own-work and qwkit citations replaced by the Zenodo records (ZENODO_CITATIONS.bib); dates 20 Oct 2026; MAT-01
    parameter table no longer overflows the margin; software paper's availability section updated (public repo).
    Meyer et al. APL 67, 608 (1995) read in full: N1 and N2 wording revised (SUBMISSION_CHECKLIST); unverified DOIs of
    Meyer 1995 (APL and IEEE JQE) removed. OPEN: (a) publish a new release of each paper repository (the v1.0.0
    archives lack these changes) and decide between version and concept DOIs in the statements; (b) N1 item 51.
54. N1 item 51 RESOLVED (20-21 Oct 2026). All electrically written schemes of N1 (triple well at 55 kV/cm and
    bias-optimized, bipolar ADQW, Stark on/off, the two-field optimization, the detuned-pump comparison and the
    sensitivity table) are now propagated through the electrode fields (N2 field model, three stack heights, media on
    a 5 kV/cm bias grid; bias maps added at 1e10, 3e10, 2e11 cm^-2) with a 188 kV/cm breakdown limit between
    neighbouring electrodes, instead of the 0.92 electrode factor (studies/n1_paper/realfield_*.py, rerun_realfield.sh;
    N1 conventions otherwise kept: no index saturation, segments one coherence length). The conclusions stand: bipolar
    ADQW (+-55-90 kV/cm) best above 1 W, 1.4-2.4x the bias-optimized triple well (was 1.7-2.2x); triple well 1.9-2.4x
    Stark at 1.26 W, 1.2-1.8x at 10 W, 1.9-9.7x growth reversal; best two-field ADQW pairs (+70,-50) and (+100,-80)
    kV/cm (as in N2). Tables 3-6, Fig. 5, abstract, discussion and conclusion updated; N2's companion paragraph updated.
    Repositories: concept DOIs and new releases via update_repos.sh / use_concept_dois.py in QW_research.
