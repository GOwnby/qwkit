"""Scoping study (new thread NL-31): electrically tunable complex chi(2) of the coupled triple well of
Yu et al., Sci. Adv. 11, eadw8852 (2025): In0.53Ga0.47As/In0.52Al0.48As 5/4.2/1.2/2.5/2.5/1.5/5 nm (barriers 5, 1.2,
2.5, 5 nm), first well doped 3.5e18 cm^-3 (1.47e12 cm^-2 per period), 23 periods = 500 nm, biased -5...+5 V.
Their design: E21 = E32 = 126.5 meV at 0 V with equal Stark coefficients, so chi(2)(V) at hw = 126.5 meV traces a
cardioid. Measured IST 97.9-131.6 meV over -5..5 V (3.37 meV/V), about half the designed field per volt.
Questions: (1) does qwkit reproduce E21 = E32 and equal Stark tuning? (2) with 1.47e12 cm^-2 per period, how far do
the depolarization/collective (TDH) corrections move the resonances and distort the cardioid?
Flat-band states (donors in the electron's own well: Hartree potential small), uniform field F = V / 500 nm.
Writes yu25.json."""
import os, sys, json
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, "..", ".."))
import numpy as np
from qwkit import core, tdh

NS = 3.5e18 * 4.2e-7          # cm^-2 per period
LP = 5 + 4.2 + 1.2 + 2.5 + 2.5 + 1.5      # nm per period without the outer 5 nm (periods share it)
GAM = 0.008
HW0 = 0.1265
VARIANTS = {"2.5": [(50, "barrier"), (42, "well"), (12, "barrier"), (25, "well"), (25, "barrier"), (15, "well"), (50, "barrier")],
            "2.0": [(50, "barrier"), (42, "well"), (12, "barrier"), (25, "well"), (20, "barrier"), (15, "well"), (50, "barrier")]}


def states(layers, F):
    z, V0, m, Eg, act = core.build(layers, pad=60.0, dz=0.25)
    V = core.potential(z, V0, act, F)
    E, psi = core.solve_states(z, V, m, Eg, nstates=4)
    keep = np.arange(len(E))
    E, psi = E[keep][:3], psi[:, keep][:, :3]
    psi = core.orthonormalize(z, psi)
    return z, E, psi, 0.5 * (act[0] + act[1]), act


def chi(layers, F, hw, kernel):
    z, E, psi, zc, act = states(layers, F)
    N = NS / (LP * 1e-7)
    m = tdh.TDH(z, psi, E, [1.0, 0, 0], NS, N, gamma=GAM, eps_r=13.9, zc=zc, kernel=kernel)
    return m, E


if __name__ == "__main__":
    out = {}
    Fs = np.linspace(-100, 100, 41)                     # kV/cm (5 V over 500 nm = 100 kV/cm)
    hws = np.arange(0.06, 0.30, 0.0005)
    for name, L in VARIANTS.items():
        rows = []
        for F in Fs:
            r = dict(F=float(F))
            for kern in (False, True):
                m, E = chi(L, F, HW0, kern)
                Z = m.Z
                c = m.chi2(HW0)
                a = np.array([abs(m.alpha(h)) for h in hws])
                peaks = [float(hws[j]) for j in range(1, len(a) - 1) if a[j] > a[j - 1] and a[j] > a[j + 1] and a[j] > 0.02 * a.max()]
                tag = "full" if kern else "bare"
                r[tag] = dict(chi_re=float(c.real), chi_im=float(c.imag), abs_peaks_meV=[1e3 * p for p in peaks])
            r["E21"] = float(1e3 * (E[1] - E[0])); r["E32"] = float(1e3 * (E[2] - E[1]))
            r["Zprod"] = float(abs(Z[0, 1] * Z[1, 2] * Z[0, 2]))
            rows.append(r)
        out[name] = rows
        r0 = rows[len(Fs) // 2]
        sl21 = np.polyfit(Fs, [r["E21"] for r in rows], 1)[0]; sl32 = np.polyfit(Fs, [r["E32"] for r in rows], 1)[0]
        print(f"variant {name}: 0 V E21 {r0['E21']:.1f} meV E32 {r0['E32']:.1f} meV; Stark slopes {sl21*20:.2f} / {sl32*20:.2f} meV per V "
              f"(1 V = 20 kV/cm); ISB absorption peaks 0 V bare {r0['bare']['abs_peaks_meV']} full {r0['full']['abs_peaks_meV']}", flush=True)
        for tag in ("bare", "full"):
            c = np.array([r[tag]["chi_re"] + 1j * r[tag]["chi_im"] for r in rows])
            ph = np.unwrap(np.angle(c))
            print(f"   {tag}: |chi2| range {abs(c).min():.0f}-{abs(c).max():.0f} pm/V, phase span {np.degrees(ph.max()-ph.min()):.0f} deg, "
                  f"min|chi|/max|chi| {abs(c).min()/abs(c).max():.3f}", flush=True)
    json.dump(out, open(os.path.join(here, "yu25.json"), "w"), indent=1)
