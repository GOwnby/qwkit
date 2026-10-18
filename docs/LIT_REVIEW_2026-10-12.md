# Literature review, 12 October 2026 (papers supplied by the author)

Five PDFs were supplied. Three are the requested papers; two are not.

## 1. G. Almogy, PhD thesis, Caltech (1995), doi:10.7907/3qj9-9777 (251 pp., scanned; OCR'd in full)

"Quantum Well Intersubband Transitions: Nonlinear Optics, Refractive Index and Infrared Modulation."
Parts: I self-consistent SP model (exchange, nonparabolicity, temperature, voltage boundary conditions);
II ISB-induced refractive index (birefringence measurement; ISB-induced phase matching, Ch. 4);
III non-perturbative ISB nonlinear optics (Ch. 5-9); IV monolithic QWIP + coupled-well modulator (Ch. 10).

Findings relevant to our papers:
- **NL-02 (now revised).** Ch. 9 contains, for the small-signal ladder: optimum length with alpha_2w = 2 alpha_w
  (Eqs. 9.11-9.13); efficiency at that length = |chi2| E / (e Im chi1(2w)) (Eq. 9.14); for equal ground-state dipoles,
  equal detunings and equal widths, |E_2w/E_w| = Omega_21 T2 / e, independent of the dipole magnitudes, density and
  detuning (Eq. 9.15) -- the symmetric special case of NL-02 Theorem 1 (exactly: eta* = e^-2 (hbar Omega_23/2 gamma)^2).
  Sec. 9.2.3 states in words that the ratio of SHG to absorption is at best unchanged by detuning. Eq. 9.37: an
  intensity-independent upper limit on the SH intensity generated in a given length, from the saturated two-photon
  coherence (sup = 1/[2(1+3T1/T2)]). Fig. 9.6 / Sec. 9.6: on resonance, conversion keeps growing with pump intensity
  when the length grows (25% needs ~100 absorption lengths and >100 Is) -- the numerical form of NL-02's "no ceiling".
  Figs. 9.7-9.9: opposite-sign ("anti-phase-matched") detuning pays at high intensity, especially with external phase
  matching; optimal SH detuning ~ sqrt(2) x pump Rabi frequency. Eq. 9.26: chi2_eff vanishes at mu12/mu01 = 1/sqrt2
  (already cited in NL-02 via LEOS'94).
  Not in the thesis: the general identity |chi2|^2 = Q alpha_w alpha_2w for arbitrary dipoles/widths/detunings,
  g(u) and zeta, NL-02 Theorem 2 (length-independent bound for arbitrary saturation and QPM), the closed-form
  high-intensity slope and its ceiling condition, the detuning rule, and the real-structure validation.
  Action taken: NL-02 intro, contributions, Theorem 1, Secs. 4-6 and discussion rewritten to credit these results;
  new script `studies/nl02/length_bound.py` generalizes Eq. 9.37 to arbitrary ladders (reproduces it exactly for the
  symmetric ladder, T1/T2 = 1-50) and shows the optimum resonant devices above 3 Is sit at 1.4-2.5x the minimum
  length allowed by the bound.
- **Publications listed in the thesis:** Almogy & Yariv, Opt. Lett. 19, 1828 (1994); Almogy, Segev & Yariv,
  Opt. Lett. 19, 1192 (1994); Almogy, Shakouri & Yariv, APL 63, 2720 (1993); Almogy & Yariv, "Resonantly-enhanced
  nonlinear optics of intersubband transitions", JNOPM (in press; = JNOPM 4, 401 (1995)); Almogy & Yariv,
  "Fundamental limits of resonantly-enhanced second-harmonic generation", J. Opt. Soc. Am. B, "in press" (not found
  in a search; possibly never published); QELS'95 paper QWJ2 (found, added to NL-02).
- **Ch. 4 (ISB-induced phase matching):** transition placed half-way between w and 2w compensates bulk GaAs
  mismatch; three-level variant uses opposite detunings; the transition-induced coherence length can drop below
  10 um. Already cited in NL-02/N1 via Opt. Lett. 19, 1192.
- **Ch. 10 (new benchmark):** 50-period GaAs/Al0.4Ga0.6As coupled-well charge-transfer modulator (9 nm well / 3 nm
  barrier / 10.8 nm storage well doped 2e18 in 4 nm, 42.2 nm period barriers), bias -13..+20 V; measured population
  transfer per volt 15% above Hartree, accounted for by exchange; transition blue-shift and broadening with
  population. A quantitative test of qwkit's self-consistent bias + exchange-correlation treatment (MS-01/MAT), and an
  alternative switching mechanism for TPV-05 (charge transfer without depletion).

## 2. I. Vurgaftman, J. R. Meyer, L. R. Ram-Mohan, Solid State Commun. 100, 663-667 (1996) (scanned; OCR'd)

Full title: "Detuned intersubband resonances for broadband field-modulated second-harmonic generation in a
waveguide." InGaAs/InAlAs ADQW 64.5/18/36.5 A, 100 A period barriers, 5e11 cm^-2, Gamma 5 meV, 9 um active region
in a 10 um waveguide (Delta n = 0.06). 14% at 10.6 um, 20 MW/cm^2, 50 um; both transitions red-detuned (delta < 0)
so the resonant index offsets the bulk + waveguide mismatch. A *uniform* field of -25 kV/cm (22.5 V) shortens the
coherence length and switches the SH off; +32 kV/cm raises 12.4 um conversion from 0.15% to 2.3%; >= 1% from 9 to
20 um with the optimum field; proposes separate active and "phase-match" regions.
- **N1 item 0 answered:** the paper does not use segment-wise or alternating-polarity fields and does not reverse the
  sign of chi2; it modulates the coherence length. N1's bipolar ADQW pattern is not anticipated, but the paper must
  be described accurately (done: N1 Sec. 1 and "Mechanism and prior art").
- Its ref. 13 is "Meyer, Hoffman, Bartoli and Ram-Mohan, Appl. Phys. Lett. 1995, 608", cited for field tuning of
  E12 and for ISB index compensation -- consistent with how N1 describes Meyer1995APL (still unread).
- NL-02 already compares with the 14% prediction (via the JQE paper); title corrected in both bibliographies.

## 3. J. Yu, J. Kim, H. Chung, J. Son, G. Boehm, M. A. Belkin, J. Lee, Sci. Adv. 11, eadw8852 (2025)

Triple coupled well In0.53Ga0.47As/Al0.48In0.52As 5/4.2/1.2/2.5/2(.5)/1.5/5 nm (text and figure differ on the third
barrier), first well 3.5e18 cm^-3 (1.47e12 cm^-2/period), 23 periods (500 nm), designed so E21 = E32 = 126.5 meV with
equal Stark coefficients -> chi2(V) at fixed hw traces a cardioid. Two X-shaped meta-atoms per cell, flipped in plane
(geometric pi offset), each with its own bias: 0-30 nm/V magnitude and 0-2pi phase; ~100% SH on/off modulation over
8.7-10.8 um; electrically programmed SH amplitude and phase gratings (18 um supercell), 1 kHz switching. Measured IST
97.9-131.6 meV over -5..5 V (3.37 meV/V); "effective voltage in the simulation ~half the applied voltage".
- **N1 question answered:** the bias does not reverse the sign of chi2 by itself; it rotates the phase through
  detuning (cardioid), and the pi offset is geometric. It is local phase control in a 500-nm film, not propagation
  QPM. It is, however, the first direct experimental demonstration of bias-programmed chi2 phase by Stark detuning,
  which supports N1's mechanism (cited in N1).
- **Companion THG paper identified from its ref. 15:** S. Park, J. Yu, G. Boehm, M. A. Belkin, J. Lee,
  "Electrically tunable third-harmonic generation using intersubband polaritonic metasurfaces",
  Light Sci. Appl. 13, 169 (2024), doi:10.1038/s41377-024-01517-y.
- **Scoping (studies/scoping/yu25.py):** qwkit with the figure's 2.0-nm barrier gives E21 = 117, E32 = 122 meV and
  Stark slopes 6.6 / 5.9 meV/V (twice the measured 3.37 meV/V, matching their "half the voltage" remark). At
  1.47e12 cm^-2 the depolarization shift is +8.5 meV and the collective (TDH) response changes the chi2(V)
  trajectory qualitatively (phase span 268 deg bare vs ~490 deg collective, i.e. the trajectory winds around the
  origin; peak |chi2| 0.6x). New thread NL-31.

## 4. Wrong papers supplied

- `Paper-APL1995-1stWQWTheory.pdf` is J. R. Meyer, C. A. Hoffman, F. J. Bartoli, L. R. Ram-Mohan, "Type-II
  quantum-well lasers for the mid-wavelength infrared", Appl. Phys. Lett. 67, 757-759 (1995) -- not the requested
  APL 67, 608-610 SHG paper. The DOI previously given (10.1063/1.115404) was not verified and may be what led to the
  wrong paper; it is now dropped from the request. Not relevant to the programme beyond background.
- `s41377-024-01608-w.pdf` is Zhou et al., "Electrically tunable planar liquid-crystal singlets for simultaneous
  spectrometry and imaging", Light Sci. Appl. 13, 242 (2024) -- not the THG paper (that is s41377-024-01517-y).
