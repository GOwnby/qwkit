# TPV-05 scoping notes (11 October 2026)

Go/no-go: **go**. No paper found that computes how bias-switched (carrier-depletion) ISB emitters degrade from 300 K
to 500-1000 K (thermal filling of subband 2, barrier escape, free-carrier/intrinsic background, LO dephasing,
nonparabolicity, depolarization), or couples ISB emissivity (Kirchhoff) into TPV / thermoradiative / TPX detailed
balance with interband-cascade (IC) or T2SL cells. [V] = checked against abstract/full text; [M] = metadata to verify.

Anchors
- Inoue, De Zoysa, Asano, Noda, Nat. Mater. 13, 928 (2014), doi:10.1038/nmat4043 [V]: emissivity 0.74 -> 0.24 by
  carrier extraction; 600 kHz cutoff.
- De Zoysa et al., Nat. Photon. 6, 535 (2012), doi:10.1038/nphoton.2012.146 [V]: energy recycling, ~150 C.
- Inoue et al., Phys. Rev. B 91, 235316 (2015), doi:10.1103/PhysRevB.91.235316: Q matching (radiative vs absorption Q,
  bias-tuned) at fixed temperature - the framework to extend to temperature.
- Inoue et al., IEICE Trans. Electron. E101-C, 545 (2018), doi:10.1587/transele.E101.C.545 [V]: ISB absorption Q~10;
  Q = 101 at 296 C; bias-switched Q = 72 at 200 C, ~3x suppression at -10 V.
- GaN/AlGaN (Kang, Inoue, Asano, Noda): APL 110, 181109 (2017), doi:10.1063/1.4983020; AIP Adv. 8, 015221 (2018),
  doi:10.1063/1.5019387 [V] (Q = 101 at 800 C); ACS Photonics 6, 1565 (2019), doi:10.1021/acsphotonics.9b00440
  (electrical modulation up to ~500 C, 50 kHz).
- Asano et al., Opt. Express 17, 19190 (2009), doi:10.1364/OE.17.019190 [V].

Linewidth / temperature (all <= 400 C; no 500-1000 K theory)
- Berland et al., APL (2010), doi:10.1063/1.3456528 (AlN/GaN ISB energy shift -6 meV RT -> 400 C).
- Unuma et al., J. Appl. Phys. 93, 1586 (2003), doi:10.1063/1.1535733 (linewidth mechanisms; roughness dominates).
- Warburton et al., PRL 80, 2185 (1998); Li & Ning, PRL 91, 097401 (2003); Ning & Li, Proc. SPIE 5352, 284 (2004)
  (LO in/out-scattering cancellation); Delteil et al., PRL 109, 246808 (2012) (multisubband plasmon linewidth stable
  77-300 K); Huppert et al., arXiv:1510.03209 (radiatively broadened emitters).

Other switchable emitters: graphene (Brar, Nat. Commun. 6, 7032 (2015); Siegel 2024; Shiue 2019), GST (Du, LSA 6,
e16194 (2017)), Pt nanowire Joule (Wojszvzyk, Nat. Commun. 12, 1492 (2021)), Si p-n theory (Assawaworrarit, Song,
Fan, arXiv:2511.18962, no temperature dependence). Reviews: Chu et al., Nanophotonics (2024),
doi:10.1515/nanoph-2023-0754.

Cells: Lotfi et al., IEEE J. Photovolt. 7, 1462 (2017), doi:10.1109/JPHOTOV.2017.2713415 (IC-TPV 0.4 eV, 9.6%);
Huang et al., J. Appl. Phys. 124, 023101 (2018), doi:10.1063/1.5030904; Huang PhD (OU 2020; ~0.2 eV cells tested
under an IC laser at 17-36 W/cm^2); thermoradiative IC T2SL diodes, APL Energy 3, 026101 (2025).

Detailed balance: Legendre & Chapuis, arXiv:2402.07527 (dual radiative engines; 600 K source); Giteau, Picardi,
Papadakis, arXiv:2507.19864 (TR bounded by TPV); DeSutter, Bernardi, Francoeur, arXiv:1509.01319 (optimal emitter
spectra); Matsuura et al., arXiv:2402.08253 (measured TR efficiency < 1e-4 %).

Design notes: GaAs ISB emitters at ~9 um (0.13 eV) sit below IC gaps (0.2-0.4 eV); GaN/AlN at ~4 um (0.3 eV) match
them and have demonstrated 800 C operation -> natural vehicle for 500-1000 K. Main III-As risk: reverse leakage and
intrinsic carriers limit depletion contrast; make it an explicit model output.
