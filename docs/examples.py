"""Worked examples from the qwkit user guide. Run from the repository root: python3 docs/examples.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
from qwkit import core, sp, scattering, waveguide, electrodes, propagation

HW = 1.23984 / 10                                   # photon energy (eV) of a 10 um pump
TW = [(58, "well"), (14, "barrier"), (34, "well"), (14, "barrier"), (58, "well")]
AD = [(64, "well"), (10, "barrier"), (29, "well")]

# 1. Self-consistent chi(2) of the triple well at 55 kV/cm and of the ADQW at 0 V
tw = sp.chi2_sc(TW, 55.0, HW, ns_cm2=5e11)
ad = sp.chi2_sc(AD, 0.0, HW, ns_cm2=5e11)
print("1. |chi2| triple well %.1f nm/V, ADQW %.1f nm/V" % (abs(tw["chi"]) / 1e3, abs(ad["chi"]) / 1e3))
print("   triple-well subbands (meV above ground):", np.round((tw["E"] - tw["E"][0]) * 1e3, 1))

# 2. Symmetry check: chi(2) is odd in F for a symmetric structure
m = sp.chi2_sc(TW, -55.0, HW, ns_cm2=5e11)
print("2. chi2(+F) + chi2(-F) = %.2e pm/V (should be ~0)" % abs(tw["chi"] + m["chi"]))

# 3. LO-phonon lifetimes
E, psi, Z, rho = sp.prepare(tw["r"])
R = scattering.rate_matrix(tw["r"]["z"], psi, E)
print("3. triple-well lifetimes: 2->1 %.2f ps, 3->2 %.2f ps, 3->1 %.2f ps" % (1e12 / R[1, 0], 1e12 / R[2, 1], 1e12 / R[2, 0]))

# 4. Saturable medium: chi(2) and absorption versus local pump intensity
med = propagation.Medium(sp.state_set(tw), HW, R=R)
for I in (0.0, 1e10, 3e10):                          # W/m^2 (1e10 W/m^2 = 1 MW/cm^2)
    r_ = med.populations(I, 0.0)
    print("4. I = %.0f MW/cm2: |chi2| %.1f nm/V, alpha(w) %.0f 1/cm" % (I / 1e10, abs(med.chi(r_)) * 1e9, med.alpha(r_)[0] / 100))

# 5. Planar waveguide: TM0 modes at 10 and 5 um, confinement, coherence length
layers = [dict(material="Au", t_um=0.1), dict(material="InP", t_um=2.0), dict(material="InGaAs", t_um=0.9),
          dict(material="stack", t_um=1.512, frac_well=150 / 378), dict(material="InGaAs", t_um=0.9),
          dict(material="InP", t_um=12.0, N=1e17)]
m1 = waveguide.tm_modes(layers, 10.0, 0.02, 1)[0]; m2 = waveguide.tm_modes(layers, 5.0, 0.02, 1)[0]
z0 = 0.1 + 2.0 + 0.9; z1 = z0 + 1.512
print("5. n_eff %.3f / %.3f, Gamma %.2f / %.2f, loss %.2f / %.2f 1/cm, Lcoh %.1f um" % (
      m1["neff"].real, m2["neff"].real, waveguide.overlap(m1, z0, z1), waveguide.overlap(m2, z0, z1),
      m1["alpha_cm"], m2["alpha_cm"], 10.0 / (4 * (m2["neff"].real - m1["neff"].real))))

# 6. Electrode field and QPM coefficient for an ideal sign-reversing medium
Lam, d = 46.9e-6, 5.31e-6
x, Ey = electrodes.field_map(Lam, d, 29.0, 2e-6, 0.5 * d, nx=1024, nmax=201)
chi_x = np.sign(Ey)
print("6. plateau field %.1f kV/cm; QPM coefficient of sign(F) = %.3f (ideal 2/pi = %.3f)"
      % (np.abs(Ey).max() / 1e5, electrodes.qpm_coefficient(x, chi_x, Lam), 2 / np.pi))

# 7. Saturated SHG propagation with sign-reversal QPM
wg = dict(n1=3.231, n2=3.338, G1=0.395, G2=0.514, O_um=0.0531, abg1_cm=3.25, abg2_cm=0.16,
          t_stack_um=1.512, w_um=15.0, Lcoh_um=23.4, lam1_um=10.0)
res = propagation.propagate(med, wg, 1.26, "sign", eta_e=0.92, L_max_um=500.0)
print("7. 1.26 W pump: peak SH conversion %.3f%% at %.0f um" % (res["eta"] * 100, res["L_opt_um"]))
