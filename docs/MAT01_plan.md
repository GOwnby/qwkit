# MAT-01 plan: intersubband optics of the polar LaInO3/BaSnO3 2DEG (12 Oct 2026)

Go decision: docs/MAT01_literature.md. Prior theory (Li-Hamze-Demkov PRB 104, 235419 (2021); Stanojevic et al.
OQE 55, 383 (2023); Jang MA thesis 2023) treats La-doped BaSnO3/BaO wells with parabolic bands, fixed linewidth, no
depolarization and no phonons. Nobody has treated the polar LIO/BSO 2DEG optically. Open check: PRB 113 (2026)
doi:10.1103/8z9v-d6s9 ("Small effective mass deep all-oxide quantum wells ...") could not be opened.

## Physics the paper must get right
1. The 2DEG is dense: n_s = 1e13-1.5e14 cm^-2 (EDL gating), E_F up to ~1 eV, several subbands occupied, strong
   nonparabolicity (beta 0.25-0.56 1/eV). In-plane nonparabolicity spreads single-particle ISB lines over hundreds of meV.
2. eps_inf ~ 4 and large n_s put the response deep in the multisubband-plasmon regime: depolarization shifts of
   hundreds of meV and Coulomb line narrowing (Delteil et al. PRL 2012 physics). Needs k-resolved RPA, not k = 0 TDH.
3. Three polar LO modes (19, 52, 90 meV; per-mode Froehlich weights from the factorized dielectric function); at low
   n_s ISB-plasmon/LO-phonon coupling via eps_b(omega); LO-limited ISB lifetimes with and without 2DEG screening.
4. The triangular polar well is asymmetric: chi(2) is intrinsic and gate-tunable; E31/E21 ~ 1.8 near double resonance.
5. Parameter uncertainty is large (m*, beta, eps, CBO, depletion charge, interface charge placement): Monte Carlo bands.

## Code (qwkit)
- `qwkit/interface.py`: self-consistent single-heterointerface 2DEG: Kane-nonparabolic Schroedinger, nonparabolic
  in-plane DOS per subband, sheet density n_s fixed (gate), positive charge split between interface (polarization) and
  LIO surface (gate), uniform depleted acceptors N_A over N_dep/N_A, optional LDA exchange-correlation
  (Hedin-Lundqvist), finite temperature.
- `qwkit/krpa.py`: k-resolved RPA (TDH) linear and second-order response with in-plane nonparabolic dispersions,
  Fermi occupations per k-shell, Hartree kernel S_abcd, background eps_b(omega) with phonons. Must reduce to
  qwkit.tdh exactly for a single k-shell (test).
- `scattering.lo_rate` generalized to several LO modes with per-mode weights, optional Thomas-Fermi 2D screening.
- Tests for each.

## Studies (studies/mat01)
1. subbands.py: E_n, E_F, occupations, extent vs n_s (1e13-1.5e14), compared with DFT (Aggoune & Draxl 2021: extent
   1-2 nm, m 0.24) and the Char-group PS model (Kim 2019).
2. linear.py: single-particle vs RPA absorption (loss function) vs n_s; plasmon energies, widths, Coulomb narrowing;
   low-n_s phonon coupling.
3. lifetimes.py: multimode LO ISB scattering vs n_s; screening bounds; comparison with transport ħ/tau.
4. chi2.py: bare and collective chi(2) vs n_s and photon energy; comparison with InGaAs ADQW of N1/NL-02.
5. uq.py: Monte Carlo over the parameter ranges of MAT01_literature.md; bands on the headline predictions.
6. paper_figures.py; manuscript paper_mat01 (no proposed-experiment section; predictions stated as such).
