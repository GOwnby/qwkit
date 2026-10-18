# Changelog

## 0.7.0 (15 Oct 2026)
- `propagation.propagate_path`: coupled-mode SHG along an arbitrary sequence of saturable media, one per step (for
  electrically programmed gratings: chi(2), absorption, saturation and dk change with the local bias); records the
  complex amplitudes and phase; reproduces `propagate_segments` (test added).
- `electrodes.field_profile` and `electrodes.top_potential_array`: exact Fourier solution of Laplace's equation for
  an arbitrary top-plane potential (any electrode pattern, gaps with linear ramps); reduces to `field_map` for the
  periodic pattern and to V/d for a wide electrode (test added).
- `propagation.Medium.populations`: the level-resolved relaxation matrix is built once (1.4x faster; same results).
- Research: N2 programmable intersubband gratings (`studies/n2`).

## Earlier on 15 Oct 2026 (package code unchanged)
- Research: MAT-03 data verified (`studies/mat03/digitization/`), all MAT-03 outputs regenerated from
  `lee_fig3b_v2.json`; trapping reading tested and withdrawn (`trapping.py`: Fermi-level shift, required trap entropy,
  linear programme over trap spectra), fixed-slow-fraction reparametrization (`localization.py`).
- Software paper brought to 0.6.2; METH-01 placed as a standalone methods note.

## 0.6.2 (14 Oct 2026)
- New `qwkit.transport`: low-temperature multisubband transport of a 2DEG. Elastic scattering at the Fermi level by
  sheets and slabs of point charges, charged threading dislocations and interface roughness, with static
  multisubband RPA screening (intrasubband Lindhard polarizabilities acting on intra- and intersubband elements) and
  the coupled Boltzmann equations of Siggia and Kwok; nonparabolic density-of-states masses; `hall()` gives the Hall
  density and mobility of parallel subband channels at zero or finite field. Tests against an independent quadrature
  of the single-subband integrals (Coulomb, roughness) and of the Hall algebra.
- `transport.mobilities(eps_cap=...)`: dielectric boundary between the 2DEG side and a cap (bare potential of cap
  charges scaled by 2 eps / (eps + eps_cap), image term in the screening). FIX before release: the coupled relaxation
  equations used k_j / k_i instead of the velocity ratio v_j / v_i (matters when the subband masses differ);
  `transport.relax` is now separate and tested against a direct angular solution of the Boltzmann equation.
- `transport.magnetotransport`: coupled-subband magnetotransport (momentum balance with the Siggia-Kwok relaxation
  matrix), reducing to parallel Drude channels without intersubband coupling; `transport.magnetoresistance`.
- `core.kane_valence`: the light-particle partner is now discretized exactly as the solver discretizes H(E) (half-point
  mass = mean of node masses, wall points included); two-band overlaps drop from ~1e-5 to ~1e-13. Kane dipoles change
  by ~2e-4 relative (earlier Kane checks unaffected at their quoted precision).
- `core.lowdin_localized(ebuf=...)`: optional energy buffer (METH-01: >= 0.5 eV; a fixed number of states spans less
  energy in a larger box). Default behaviour unchanged.
- Research: MAT-03 analysis of the frozen-gate Hall data of Lee et al. (`studies/mat03`); METH-01 methods note on
  one-band dipoles (`studies/meth01`); N2 programmable-grating groundwork (`studies/n2`); MAT-04 scoping.

## 0.6.1 (13 Oct 2026)
- FIX (affects N1, NL-02, NL-05, MS-02, TPV-05): Loewdin orthonormalization of the localized states only
  (`sp.prepare`, `core.analyze`, `sens.observables`, `thermal.emitter_state`) gave the topmost localized state spurious
  dipoles when few states are localized, because it cannot be orthogonalized against the states left out. For the
  64/10/29 A double well in the 200 A box (three localized states) z13 came out 8.77 A against 8.22 A from the two-band
  Kane states, and |chi2| about 8% too large; the earlier Kane checks used a 100 A box with four localized states,
  where the error is ~1%. New `core.lowdin_localized`: the localized states are orthonormalized together with at least
  `nbuf` = 10 box states above them (solved at the converged potential if needed), then truncated; the dipoles now
  agree with the Kane metric to <= 0.7% and do not depend on the box (`studies/kane/box_scan.py`; test added).
  `sens.observables` orthonormalizes all model states before selecting (model.nstates should exceed the kept count by
  about ten); `thermal.emitter_state` orthonormalizes its whole box basis. `sp.chi2_sc(sc=False)` now stores m, Eg.
- `interface.solve(nd_cap=...)`: optional ionized-donor density in the cap (a function of z), e.g. oxygen vacancies
  created by an electrolyte; the positive sheets carry the rest of the charge (Gauss-law test added).
- Research: MAT-02 electrolyte-gating study (`studies/mat02`).

## 0.6.0 (13 Oct 2026)
- `sens`: matrix-free implicit tangents (default): reduced resolvents by shifted tridiagonal LU solves with
  projection and refinement, and the Hartree feedback (I - K) dV_H = b by GMRES (5 iterations typical), instead of
  full eigendecompositions and an explicit N x N density response. 6x faster on the N1 double well, identical to
  1e-12; `dense=True` keeps the old path (test added). `observables(nkeep=...)` now keeps the nkeep MOST LOCALIZED
  states (was: the lowest nkeep, which could pick a delocalized box state); `core.localized_fraction`.
- Research (MAT-01 second revision): exact k = 0 time-dependent Hartree mode analysis (`studies/mat01/meanmode.py`,
  oscillator-strength-weighted mean absorption energy, collective blue-shift factor), medians instead of centroids,
  electrolyte-gating electrostatics with a quantized onset (`gating.py`), cap-thickness and cap-offset mode checks
  (`capmodes.py`, `capmodes2.py`), supporting numbers (`extras.py`), checks table (`appendix_table.py`) and a number
  collector (`collect_numbers.py`).
- FIX `interface.hartree`: the ionized-acceptor charge was discontinuous in the depletion width (a cell was fully
  charged when w_d fell in its left half), which made the self-consistency oscillate at the depletion edge (residuals up
  to 20 meV at some densities); each cell now carries the fraction of its width inside the depletion layer, and the
  solver converges in a few iterations. `interface.solve` returns the final residual (`resid`).
- FIX `interface.hartree`: the potential was integrated to the right edge of each cell (cumsum(E) dz), which put
  every value half a cell to the right and lowered the cap by F dz/2 relative to the well; it is now integrated to the
  cell centres (second order). At 1e14 cm^-2 E21 rises by 4-6 meV and becomes grid-independent (dz/2 changes it by
  < 0.1 meV instead of 1.5-3 meV). `interface.solve(sigma_int=...)`: fixed interface sheet with the remaining positive
  charge on the cap surface (electric-double-layer gating).
- `core.kane_valence`, `core.kane_dipoles`: two-component Kane states (orthogonal without Loewdin); `core.analyze`
  and `sp.prepare` Loewdin-orthonormalize all localized states before truncating.
- `core.solve_states` and `interface.subband_dispersion` compute only the requested eigenpair at each iteration
  (`core._solve(..., first=k)`): identical states, 5-8x faster for large state sets. Timings quoted in MS-02 change.
- FIX (MAT-01 studies, `studies/mat01/common.extend`): the nonparabolic subbands are Loewdin-orthonormalized as a set
  that extends 0.6 eV (at least 12 states) beyond the kept range and only then truncated; orthonormalizing the
  truncated set gave its topmost states spurious dipoles (up to 3% of the 1->n oscillator strength when the set was
  capped). Cap raised from 60 to 90 subbands.
- FIX `core._solve`: the box ends were zero-flux (Neumann) boundaries, although documented as hard walls; they are now
  Dirichlet (psi = 0 one step beyond each end), and `sens` uses the same end terms. Bound states of padded structures
  are unchanged (< 1e-4 meV for 100 A pads); box (continuum) states shift, and the spurious states localized at the box
  edges disappear. TPV-05 check: peak ISB absorption +0.4 to +3.3%, continuum population roughly halved; the affected
  studies are being re-run.
- `core.solve_states`: secant iteration for the energy-dependent mass (faster, same fixed point).
- `interface`: exact in-plane band-edge masses of the energy-dependent-mass Hamiltonian and nonparabolicity fitted to
  the exact subband dispersion (two-stage self-consistency); `subband_dispersion`, `bandedge_masses`, `xc_kernel`.
- `krpa`: only pairs with an occupation difference carry coherences (with Hartree feedback from the others at 2w),
  optional adiabatic local XC kernel (`set_xc`), batched second order; `scattering`: `form_factor`,
  `screening_factor` (static RPA with Coulomb form factors), `lo_rate_k` (angular integral, nonparabolic final DOS,
  Pauli blocking).
- New module `qwkit.interface` (MAT-01): self-consistent 2DEG at a single polar heterointerface (Kane-nonparabolic
  subbands with consistent in-plane dispersion and density of states, Fermi-level pinning by compensating acceptors,
  interface/cap positive sheet, optional Hedin-Lundqvist exchange-correlation, Anderson mixing with retry).
- New module `qwkit.krpa`: k-resolved time-dependent Hartree (RPA) linear and second-order response with in-plane
  nonparabolic dispersions and a frequency-dependent (polar-phonon) background; reduces exactly to `qwkit.tdh` for one
  shell. `phonon_eps`, `froehlich_weights` (per-mode Froehlich factors). `scattering.lo_rate` gains per-mode weights and
  Thomas-Fermi screening; `lo_rate_modes`, `tf_wavevector`. Tests: 51.
- Research: MAT-01 study (`studies/mat01/`, `paper_mat01/`).
- Literature review of 12 Oct 2026 (`docs/LIT_REVIEW_2026-10-12.md`): NL-02 credits Almogy's thesis results and adds
  `studies/nl02/length_bound.py` (generalized length-limited bound); N1 describes Vurgaftman et al. SSC 1996 and Yu et al.
  Sci. Adv. 2025 accurately; scoping of the Yu metasurface triple well (`studies/scoping/yu25.py`).
- New module `qwkit.thermal` (TPV-05): temperature-dependent material data (Varshni gaps, Gamma-L separations, L-valley
  masses), intrinsic density, `emitter_state` (self-consistent period at T with continuum states and an L-valley
  reservoir), `isb_alpha` (k-resolved in-plane nonparabolic line shape), `linewidth` (LO phonons), `interband_alpha`
  (Urbach tail), `emitter_spectrum` (coupled-mode emissivity plus slab background), `leakage`, `tpv` (two-surface
  detailed balance). Five tests: 42 tests.
- Research: TPV-05 study (`studies/tpv05/`, `paper_tpv05/`). NL-05: Krieguer-Todorov three-subband benchmark
  (`studies/nl05/krieguer24.py`).
- New module `qwkit.sens`: exact parameter sensitivities of the one-period self-consistent Schroedinger-Poisson
  model by implicit differentiation (static density response of the nonparabolic eigenproblems, Fermi-level
  constraint, complex-step permittivity derivative of the Hartree map, erf-smoothed interfaces); `Model.forward`,
  `Model.tangents`, `observables`, `observable_jacobian` (semi-analytic post-processing, Richardson-extrapolated).
  Tests against finite differences for energies, states, occupations and observables, including a case with the
  mass floor active: 37 tests.
- Research: MS-02/MS-03 study (`studies/ms02/`, `paper_ms02/`): verification and cost, full and group-wise Monte
  Carlo uncertainty propagation, optimizer comparison, window-weighted robust design, bias-scan trimming.
- New module `qwkit.tdh`: time-dependent Hartree (RPA) response of a doped period with the drive referenced to
  the displacement field; `hartree_kernel`, `TDH.response/chi1/chi2/alpha` (second order in the frequency domain)
  and `TDH.evolve` (fourth-order Runge-Kutta real-time integration with exact harmonic windows; default run
  length set by the slowest excited-state lifetime). Three tests (bare limit, Ando energy, real time vs second
  order): 34 tests.
- Research: NL-05 study (`studies/nl05/`, `paper_nl05/`): collective second-order response, pathway factors,
  kernel geometry, design survey, double counting, saturation with real-time TDH and controls.
- `core.dipoles` now Loewdin-orthonormalises the states by default (`orthonormal=True`), so off-diagonal dipoles of
  raw nonparabolic states no longer depend on the coordinate origin; new `core.orthonormalize`. Results of
  `core.analyze`, `sp.prepare` and everything built on them are unchanged (they already orthonormalised).
  New regression test (mirror-image structures, origin shift): 31 tests.
- Research: NL-02 study (`studies/nl02/`, `paper_nl02/`): dimensionless three-level ladder model with QPM,
  an independent full three-level density-matrix propagation solver, and validation against qwkit.
- Bibliography fix in the N1 manuscript (title of Vurgaftman et al., Solid State Commun. 100, 663).

## 0.5.0 (2026-10-10)
- Packaging: `pyproject.toml` (pip-installable), MIT license, citation metadata, contributing guide,
  code of conduct, continuous-integration workflow.
- `qwkit.add_material()` registers new materials; `sp.state_set()` converts a self-consistent result
  into the input of `propagation.Medium`.
- Validation suite extended to 30 tests: analytic finite well (BenDaniel-Duke) with grid convergence,
  phase-mismatched coupled-mode limit, 2D Fermi-Dirac closed form, infinite-well depolarisation shift,
  Gauss's law across a dielectric interface, cross-section scaling with refractive index, mode normalisation.
- Fixed: the Hartree solver imposed the zero-mean condition on the field instead of the displacement, so D was
  not continuous at dielectric interfaces (changes |chi(2)| by at most about 0.1%).
- Fixed: `propagation.Medium(nref=...)` was ignored in the absorption cross-sections.
- New arguments: `pad_material` (core.build, sp), `m_dos` and `eps_depol` (sp); `self_consistent` warns when it
  does not converge; `scattering.rate_matrix` accepts T = 0; `core.wkb_escape_time` requires `active`.
- Docstrings for all public functions; validation examples in `examples/validation/`; `tools/export_public.sh`.

## 0.4.0 (2026-10-10)
- `scattering`: Froehlich LO-phonon intersubband rates with detailed balance; benchmark against a
  published GaAs value.
- `propagation`: level-resolved relaxation in `Medium`; `propagate_segments` for media that change
  from segment to segment; fixed the sampling of the QPM sign at segment edges in `propagate`.

## 0.3.0
- Planar TM waveguide solver, electrode fields, saturable coupled-mode SHG propagation.

## 0.2.0
- Self-consistent Schroedinger-Poisson with depolarisation; Fermi-Dirac populations.
