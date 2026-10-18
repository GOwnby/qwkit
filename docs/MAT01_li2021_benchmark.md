# Benchmark extraction: Li, Hamze & Demkov, PRB 104, 235419 (2021)

**Source.** W. Li, A. K. Hamze, A. A. Demkov, "Tunable giant nonlinear optical susceptibility in BaSnO3 quantum wells", *Phys. Rev. B* 104, 235419 (2021), doi:10.1103/PhysRevB.104.235419. Accepted manuscript at https://link.aps.org/accepted/10.1103/PhysRevB.104.235419. I opened it in four WebFetch passes on 12 Oct 2026.

**Scope of what I could read.**
- **Main text:** 20 pages, 5 figures, no tables.
- **Supplemental Material** (ref. [48], Secs. I–VIII): fetch refused (permission timeout). Almost all reproduction parameters live there.
- **Figures:** WebFetch returns text only, so I could not view any figure. None of the quantities below that "appear only in a figure" could be read, and I give no guessed readings. Those cells say "figure only, not read".

**Bottom line.** The main text is not enough to reproduce their calculation. The following are absent from the main text: BaO effective mass, BaO and BSO dielectric constants, unit-cell lengths, cladding thickness, doping location, temperature, solver boundary conditions, and all subband energies and dipole elements. They are in SM Secs. II, V–VIII and Figs. 1–2 and 5. The SM PDF needs institutional access.

## (1) Layer sequences

| Structure | Text quote / content | Where |
|---|---|---|
| DQW (blue spectrum in Fig. 5a) | "four- and seven-unit-cell thick BSO wells, separated by a one-unit-cell thick BaO barrier". Sequence: BaO(thick) / BSO 4 u.c. / BaO 1 u.c. / BSO 7 u.c. / BaO(thick). | Text before Fig. 1; Fig. 1 |
| TQW (green spectrum in Fig. 5a) | "three-, four-, and six-unit-cell thick BSO wells, separated by two one-unit-cell thick BaO barriers". Sequence: BaO / BSO 3 / BaO 1 / BSO 4 / BaO 1 / BSO 6 / BaO. | Fig. 2 |
| Additional DQW (red spectrum in Fig. 5a) | "an additional DQW with three- and six-unit-cell thick BSO wells". The barrier is presumably 1 u.c. BaO, but this is not stated. | Fig. 5(a) discussion |
| Cladding | "Both the DQW and the TQW are placed between thick BaO barrier layers." No thickness is given. | Text |
| Unit-cell lengths | **Not given in the main text.** It says only "Since the lattice parameters of BSO and BaO are fixed". | — |
| Order of wells relative to +z | Not stated in the text (Fig. 1a/2a schematics only, not read). | Figure only, not read |

Assumptions you will need (not from the paper):
- BSO cubic a = 4.116 Å, so 4 u.c. = 16.5 Å and 7 u.c. = 28.8 Å.
- "One unit cell of BaO" is ambiguous. For rock-salt BaO, a = 5.52 Å, giving one rock-salt cell ≈ 5.5 Å, or a single BaO plane spacing ≈ a/2 ≈ 2.8 Å. If the DFT stack is coherent with BSO in-plane, a 1-u.c. barrier is likely about 2–5.5 Å.
- This ambiguity matters strongly for the tunnel coupling. Get it from SM Sec. II / VII.

## (2) Material parameters

| Parameter | Value in paper | Where |
|---|---|---|
| BSO m* | "For bulk perovskite BSO we calculate the electron effective mass of m*=0.17m0" (DFT); "0.19m0" quoted as experiment. Which value enters the Poisson–Schrödinger (PS) solver is not stated explicitly; 0.17 is implied. | Text before Eq. (1) |
| CB offset BSO/BaO | "large CB offset (~ 1.74 eV)" | Introduction |
| BSO/Al2O3 offset (outlook only) | "3.5 eV [69]" (ref. 69: Guo, Jang, Li, Demkov, unpublished) | Conclusion |
| BaO m* | **Not in the main text** (SM) | — |
| ε of BSO and BaO | **Not in the main text** (SM Sec. V). Eq. (2) contains only the vacuum ε0. | — |
| Nonparabolicity | None. Eq. (1) is parabolic: E_n = E_{n,z} + ħ²k∥²/(2m*). In-plane parabolicity is checked in Figs. S5 and S9. | Eq. (1) |
| BSO breakdown field | "~ 2 MV/cm" | Text |

## (3) Doping, temperature, solver

| Item | Paper | Where |
|---|---|---|
| Doping | "To model doped QWs with only the ground state occupied, we use average doping densities" N_e = 10¹⁹ cm⁻³ (DQW) and 5×10¹⁸ cm⁻³ (TQW). Fig. 1 caption: "Fermi level ... in the conduction band due to the La doping density of 10¹⁹ cm⁻³". The text says La-doped BSO; which layers are doped is not stated. | Text after Eq. (2); Figs. 1, 2 captions |
| Fermi level | Marked in Figs. 1(a) and 2(a); no number given | Figure only, not read |
| Temperature | Not stated | — |
| Solver | "PS solver [51]". Ref. [51] is Harrison & Valavanis, *Quantum Wells, Wires and Dots*, 4th ed. (Wiley 2016), i.e. probably the QWWAD-style 1D solver. La-doping treatment is in SM Sec. V. Boundary conditions are not stated. | Text |
| Validation | DFT (supercell details in SM Secs. II, VII, VIII) and maximally localized Wannier tight-binding projected on Sn sites. "Four bounded quantum levels" in the DQW. PS (red) and DFT (black) level spacings compared in Fig. 1(a) and 2(a). | Fig. 1 caption |

## (4) Quoted energies and susceptibilities

| Quantity | Value | Condition | Where |
|---|---|---|---|
| Number of bound levels in DQW | 4 | zero bias, N_e = 1e19 | Fig. 1 caption |
| Subband energies, transition energies, dipole elements | **Not given numerically** (arrow labels in Figs. 1a and 2a) | — | Figure only, not read |
| DQW SHG process 1 | pump (operating frequency, "OF") **0.55 eV**, red arrows in the Fig. 5(b) top panel | zero bias (implied) | Text |
| DQW SHG process 2 | pump **0.25 eV**, black arrows | zero bias (implied) | Text |
| Zero-bias spectrum | Unequal level spacing "splits \|χ(2)zzz(2ω,ω,ω)\| spectrum into two peaks near 0.25 eV". Peak magnitude is shown against a dashed semiconductor reference line of 10⁻⁸ m/V = 10 nm/V. | zero bias | Fig. 5(a), not read |
| Max χ(2)zzz | **"up to 200 nm/V and 100 nm/V under negative and positive bias, respectively"**. The bias magnitude and photon energy for these maxima are **not stated in the text**. The sign convention for Ez is not defined. | biased | Text, Fig. 5(a) |
| Max χ(3) | "up to 8000 nm²/V²" (abstract). Photon energy and field are not stated beyond the THG case below. | — | Abstract |
| TQW THG | "Applying external bias of Ez = -100 kV/cm" brings THG into resonance at OF **~200 meV**, output **600 meV**. Fig. 5(c) shows THG of the TQW with and without bias. | Ez = −100 kV/cm | Text, Fig. 5(c) |
| Operating range | OF "ranges from 0 to 600 meV", output "up to 1200 meV". Semiconductor QW comparison: OF ~150 meV, output ~300 meV. | — | Text |
| Comparison | χ(2) "up to four times larger than that reported for the semiconductor QWs [19]". Semiconductor reference values: χ(2) ~10⁻⁸ m/V, χ(3) ~10⁻¹⁴ m²/V² (AlInAs/GaInAs, ref. [22]). | — | Introduction, conclusion |

## (5) χ(2) formula and damping

Eq. (2), as extracted. The PDF text garbled some sub- and superscripts, so I reconstructed them:

χ(2)_ijk(2ω,ω,ω) = N_e/(ε0 ħ²) Σ_{lmn} (ρ_ll⁽⁰⁾ − ρ_mm⁽⁰⁾) μ^i_ln μ^j_nm μ^k_ml × { 1/[(ω_nl − 2ω − iγ_nl)(ω_ml − ω − iγ_ml)] + 1/[(ω_nm + 2ω + iγ_nl)(ω_ml − ω − iγ_ml)] }

What the formula includes:
- **Prefactor:** N_e/(ε0ħ²), where N_e is the "average doping density" (volume density, cm⁻³), and there is no explicit e³. The "μ" are called the "dipole matrix", so they presumably already include e (μ = e⟨z⟩). The units then come out in m/V.
- **Populations:** they are included through the differences ρ_ll⁽⁰⁾ − ρ_mm⁽⁰⁾ of the unperturbed density matrix. Only the ground state is occupied, so ρ11 = 1 and all others are 0.
- **No local-field or depolarization correction** appears.
- **Possible transcription error:** the second term's denominator mixes γ_nl with ω_nm. This may be how the manuscript prints it or a text-extraction artefact; check it against the published PDF.
- **Component:** only zzz is used, and only zzzz for χ(3).
- **χ(3):** no equation in the main text ("Details ... Supplemental Material Sec. VI").
- **Damping:** "We set γ_nl = 10 meV for the damping term", the same for all pairs. It is compared with "γ_nl = 7.5 − 8.5 meV in Ref. [19]". It is described as representing "excited electrons in other non-QW bands, intraband motion, etc."

## Reproduction plan given the missing data
1. Get the SM (APS supplemental for 10.1103/PhysRevB.104.235419) through institutional access, or ask the coordinator to allow journals.aps.org/prb/supplemental.
2. Until then, use these assumptions and treat agreement as qualitative:
   - m* = 0.17 m0 in both BSO and BaO;
   - ΔEc = 1.74 eV;
   - a_BSO = 4.116 Å; BaO barrier of 1 u.c. = 2.8 Å and 5.5 Å as two bracketing cases;
   - flat-band (N_e only sets populations);
   - ρ11 = 1, γ = 10 meV.
3. Targets to check against:
   - DQW has 4 bound states;
   - two χ(2) peaks in pump energy near 0.25 eV, plus a process at 0.55 eV;
   - zero-bias |χ(2)| of order 10 nm/V;
   - |χ(2)| ≤ 200 nm/V under bias, with fields well below 2 MV/cm (−100 kV/cm is the only field quoted).
