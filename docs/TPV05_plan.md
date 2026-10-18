# TPV-05 working plan (drafted 11 October 2026, while MS-02 studies run)

Title (working): Temperature limits of narrowband, bias-switchable intersubband thermal emitters for low-temperature
thermophotovoltaics.

## Question
Carrier-depletion ISB emitters (Noda: emissivity 0.74 -> 0.24 near 300-570 K, GaAs; GaN up to ~770 K) are the only
electrically switchable narrowband thermal emitters with GHz-class potential. How do their peak emissivity, Q,
spectral selectivity and switching contrast degrade from 300 to 1000 K, which mechanism sets the limit in each
material system, and what TPV efficiency and power density do they then give with 0.2-0.4 eV interband-cascade cells?

## Model (qwkit reuse + new pieces)
1. Active region: self-consistent SP (qwkit.sp / sens) at temperature T (Fermi-Dirac, nonparabolic), Ando-shifted
   ISB absorption (density matrix), thermal populations of upper subbands (rho1 - rho2 factor).
2. Linewidth gamma(T): LO-phonon emission/absorption rates (qwkit.scattering, Bose factors) + interface roughness
   (constant, calibrated to 300 K data) + in-plane nonparabolicity inhomogeneous broadening, computed by
   k-resolving E12(k) over the thermal distribution (new, small).
3. Carrier escape: thermionic emission over the barrier and fraction of electrons in barrier/continuum states
   (3D density of barrier states at T); these carriers give Drude free-carrier absorption (qwkit.waveguide.drude),
   i.e. broadband background emissivity.
4. Intrinsic carriers of the well/barrier/cladding at T (n_i(T), Varshni gaps) -> interband + free-carrier
   background (dominant risk for InGaAs above ~600 K).
5. Emitter optics: single-mode coupled-mode theory, A(w) = 4 g_rad g_abs / ((w - w0)^2 + (g_rad + g_abs + g_bg)^2),
   with g_abs from the ISB susceptibility and confinement, g_bg from free carriers; Q matching as in Inoue et al.
   PRB 91, 235316 (2015). Optional: transfer-matrix slab on a mirror for an unpatterned reference.
6. Switching: on state n_s; off state depleted to n_off(T), floored by thermal generation/leakage (estimate from
   thermionic current vs sweep-out); contrast and modulation depth vs T.
7. Detailed balance: emitter at T_e, cell at 300 K, spectral emissivity into the cell (view factor 1, far field);
   cell: E_g 0.2-0.4 eV, EQE and external radiative efficiency (ERE) as parameters (IC-TPV: Lotfi 2017, Huang 2018);
   efficiency = P_el / (P_rad absorbed + parasitic); compare ISB emitter vs blackbody vs ideal band-pass.

## Material systems
- In0.53Ga0.47As/In0.52Al0.48As on InP (in qwkit; offset 0.52 eV): ISB up to ~0.3 eV; escape-limited.
- In0.53Ga0.47As/AlAs0.56Sb0.44 on InP (offset ~1.6 eV; add to qwkit.core.MAT): ISB 0.3-0.5 eV, matches IC cells.
- GaAs/Al0.3Ga0.7As (Noda reference, 9 um / 0.13 eV): validation case against Inoue 2014/2018.
- GaN/AlN: deferred (needs polarization fields); discuss qualitatively, cite Kang et al. 2017-2019.

## Validation targets
- Inoue et al. Nat. Mater. 2014: 0.74 -> 0.24 contrast; IEICE 2018: Q = 101 at 296 C, Q = 72 bias-switched at 200 C.
- ISB linewidth vs T data (<= 400 C, e.g. Berland 2010 energy shift).

## Deliverables
Temperature-limit map (emissivity peak, Q, contrast vs T for each material); dominant mechanism per regime; TPV
efficiency/power at max power vs T_e for 0.2/0.3/0.4 eV cells; design rules (doping, well width, barrier material).
No proposed experiment needed (optional: test with Yang-group IC cells).
