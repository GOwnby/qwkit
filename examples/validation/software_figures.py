"""Figures for the qwkit software paper: (1) validation against analytic limits and a published benchmark,
(2) an end-to-end example (the N1 triple-well study). Writes PDFs to paper_software/figures/ and timing.json."""
import sys, os, json, time
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.join(here, "..", "..")
sys.path.insert(0, root); sys.path.insert(0, os.path.join(root, "tests"))
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from qwkit import core, sp, scattering as sc, propagation as pr
from test_analytic_extra import finite_well_levels

out = os.path.join(root, "paper_software", "figures"); os.makedirs(out, exist_ok=True)
BLUE, ORANGE, AQUA, RUST = "#2a78d6", "#eb6834", "#1baf7a", "#9c3d12"
INK, INK2, GRID, MUTED = "#0b0b0b", "#52514e", "#e4e3df", "#9b9a95"
plt.rcParams.update({"font.family": "serif", "font.serif": ["STIX Two Text", "STIXGeneral", "DejaVu Serif"],
                     "mathtext.fontset": "stix", "font.size": 8.5, "axes.labelsize": 8.5, "axes.titlesize": 8.5,
                     "xtick.labelsize": 7.5, "ytick.labelsize": 7.5, "legend.fontsize": 7.0, "axes.linewidth": 0.6,
                     "axes.edgecolor": INK2, "xtick.color": INK2, "ytick.color": INK2, "axes.labelcolor": INK,
                     "lines.linewidth": 1.5, "savefig.bbox": "tight", "savefig.pad_inches": 0.02, "pdf.fonttype": 42})
HW = 1.23984 / 10
TW = [(58, "well"), (14, "barrier"), (34, "well"), (14, "barrier"), (58, "well")]
AD = [(64, "well"), (10, "barrier"), (29, "well")]

def clean(ax):
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    ax.grid(axis="y", color=GRID, lw=0.5); ax.set_axisbelow(True)

def label(ax, s): ax.text(-0.17, 1.03, s, transform=ax.transAxes, fontsize=9.5, fontweight="bold", va="bottom")

def well_levels(L, nonparabolic, dz=0.5):
    pad = 300.0; n = int(round((L + 2 * pad) / dz)); z = (np.arange(n) + 0.5) * dz
    inside = (z > pad) & (z < pad + L)
    V = np.where(inside, 0.0, 0.52); m = np.where(inside, 0.043, 0.075); Eg = np.where(inside, 0.75, 1.45)
    E, _ = core.solve_states(z, V, m, Eg, nstates=3, nonparabolic=nonparabolic)
    return E

def fig_validation():
    timing = {}
    fig, axs = plt.subplots(2, 2, figsize=(6.6, 4.6), gridspec_kw=dict(wspace=0.38, hspace=0.55)); axs = axs.ravel()
    # (a) finite well vs BenDaniel-Duke analytic
    ax = axs[0]; Ls = np.arange(40, 161, 10)
    an = [finite_well_levels(L, 0.52, 0.043, 0.075) for L in Ls]
    for k, c in enumerate((BLUE, ORANGE, AQUA)):
        Lk = [L for L, a in zip(Ls, an) if len(a) > k]; ak = [a[k] * 1e3 for a in an if len(a) > k]
        ax.plot(Lk, ak, color=c, lw=1.2)
        num = [well_levels(L, False)[k] * 1e3 for L in Lk]
        ax.plot(Lk, num, "o", color=c, ms=2.6, mfc="white", mew=0.8)
        npb = [well_levels(L, True)[k] * 1e3 for L in Lk]
        ax.plot(Lk, npb, color=c, lw=0.8, ls=(0, (2, 1.5)))
    ax.set_xlabel("Well width (Å)"); ax.set_ylabel("Subband energy (meV)")
    from matplotlib.lines import Line2D
    ax.legend([Line2D([], [], color=INK2, lw=1.2), Line2D([], [], color=INK2, marker="o", ls="", ms=2.6, mfc="white"),
               Line2D([], [], color=INK2, lw=0.8, ls=(0, (2, 1.5)))],
              ["analytic (parabolic)", "qwkit (parabolic)", "qwkit (nonparabolic)"], frameon=False, fontsize=7, loc="upper right")
    ax.set_ylim(0, 640)
    clean(ax); label(ax, "(a)")
    # (b) exact odd symmetry of chi(2) in a self-consistent symmetric triple well
    ax = axs[1]; Fs = np.arange(5, 101, 5); mag, res = [], []
    t0 = time.time()
    for F in Fs:
        p = sp.chi2_sc(TW, float(F), HW, ns_cm2=5e11)["chi"]; m_ = sp.chi2_sc(TW, -float(F), HW, ns_cm2=5e11)["chi"]
        mag.append(abs(p) / 1e3); res.append(abs(p + m_) / abs(p))
    timing["sc_chi2_per_point_s"] = (time.time() - t0) / (2 * len(Fs))
    ax.semilogy(Fs, np.maximum(res, 1e-16), "s", color=ORANGE, ms=3)
    ax.set_xlabel("Field $F$ (kV/cm)"); ax.set_ylabel(r"$|\chi^{(2)}(F)+\chi^{(2)}(-F)|\,/\,|\chi^{(2)}(F)|$")
    ax.set_ylim(1e-16, 1e-2); ax.axhline(1e-6, color=INK2, lw=0.6, ls=(0, (4, 3)))
    ax.text(100, 2e-6, "test tolerance", ha="right", va="bottom", fontsize=7, color=INK2)
    ax.text(0.03, 0.06, "symmetric triple well, self-consistent\n" + rf"$|\chi^{{(2)}}|$ up to {max(mag):.0f} nm/V", transform=ax.transAxes, fontsize=7, color=INK2)
    clean(ax); label(ax, "(b)")
    # (c) LO-phonon lifetime vs width, GaAs/Al0.3Ga0.7As, with the published benchmark point
    ax = axs[2]; Ws = np.arange(80, 181, 10); taus = []   # E2 at least 20 meV below the barrier top
    for W in Ws:
        z = (np.arange(int((W + 600) / 0.5)) + 0.5) * 0.5
        V = np.where((z > 300) & (z < 300 + W), 0.0, 0.2138)
        E, psi = core.solve_states(z, V, np.full_like(z, 0.07), np.full_like(z, 1.42), nstates=3, nonparabolic=False)
        dE = E[1] - E[0]
        taus.append(1e12 / sc.lo_rate(z, psi[:, 1], psi[:, 0], dE, T=0.0, hwlo=0.036, eps_inf=10.89, eps_s=12.5, m_eff=0.07)
                    if dE > 0.036 else np.nan)
    ax.plot(Ws / 10, taus, color=BLUE)
    ax.plot([10.0], [0.834], "D", color=ORANGE, ms=4)
    ax.annotate("published value\n(10 nm, 0.83 ps)", xy=(10.0, 0.834), xytext=(12.0, 1.0), fontsize=7, color=INK2,
                arrowprops=dict(arrowstyle="-", color=INK2, lw=0.5))
    ax.set_xlabel("GaAs well width (nm)"); ax.set_ylabel(r"$\tau_{21}$, LO-phonon emission (ps)")
    clean(ax); label(ax, "(c)")
    # (d) coupled-mode limits: phase mismatch (sinc^2) and sign-reversal QPM ((2/pi)^2 of perfect PM)
    class Stub:
        def populations(self, I1, I2): return None
        def chi(self, rho): return 50e-9
        def alpha(self, rho): return 0.0, 0.0
    WG = dict(n1=3.2, n2=3.3, G1=0.4, G2=0.5, O_um=0.05, abg1_cm=0.0, abg2_cm=0.0, t_stack_um=1.5, w_um=15.0,
              Lcoh_um=20.0, lam1_um=10.0)
    ax = axs[3]; P1 = 1e-6
    rs = pr.propagate(Stub(), WG, P1, "sign", L_max_um=200.0, steps_per_lcoh=64)
    rn = pr.propagate(Stub(), WG, P1, "none", L_max_um=200.0, steps_per_lcoh=64)
    K = rs["K"]; x = rs["x_um"] * 1e-6; dk = np.pi / 20e-6; norm = (K * 50e-9 * P1 * 200e-6) ** 2
    ax.plot(rs["x_um"], rs["P2"] / norm, color=BLUE, lw=1.1, label="QPM, numerical")
    ax.plot(rs["x_um"], (2 / np.pi) ** 2 * (x / 200e-6) ** 2, color=INK2, lw=0.8, ls=(0, (2, 1.5)), label=r"$(2/\pi)^2$ envelope")
    ax.set_xlabel(r"Distance ($\mu$m)"); ax.set_ylabel("SH power (normalized)")
    ax.legend(frameon=False, fontsize=7, loc="lower right"); clean(ax); label(ax, "(d)")
    ins = ax.inset_axes([0.1, 0.45, 0.42, 0.27])
    ins.plot(rn["x_um"], rn["P2"] / norm * 1e3, color=ORANGE, lw=1.0)
    ins.plot(rn["x_um"][::5], ((np.sin(dk * x / 2) / (dk / 2)) ** 2 / (200e-6) ** 2 * 1e3)[::5], "o", color=ORANGE, ms=1.6, mfc="white", mew=0.6)
    ins.set_title(r"no QPM, $\times10^{3}$ (circles: sinc$^2$)", fontsize=6.5, pad=2)
    ins.tick_params(labelsize=6)
    fig.savefig(os.path.join(out, "fig_validation.pdf")); plt.close(fig)
    return timing

def fig_example():
    timing = {}
    fig, axs = plt.subplots(1, 3, figsize=(7.2, 2.15), gridspec_kw=dict(wspace=0.5))
    # (a) self-consistent band profile and states of the triple well at +55 kV/cm
    ax = axs[0]; t0 = time.time()
    o = sp.chi2_sc(TW, 55.0, HW, ns_cm2=5e11); timing["sc_solution_s"] = time.time() - t0
    r = o["r"]; E, psi, Z, rho = sp.prepare(r); zc = 0.5 * (r["active"][0] + r["active"][1])
    ax.plot((r["z"] - zc) / 10, (r["V"] - E[0]) * 1e3, color=INK2, lw=0.8)
    for k, c in enumerate((BLUE, MUTED, ORANGE, AQUA)):
        d = psi[:, k] ** 2 / (psi[:, k] ** 2).max() * 45; Ek = (E[k] - E[0]) * 1e3
        ax.fill_between((r["z"] - zc) / 10, Ek, Ek + d, color=c, alpha=0.4, lw=0)
    ax.set_xlim(-18, 18); ax.set_ylim(-80, 450); ax.set_xlabel("$z$ (nm)"); ax.set_ylabel("Energy (meV)")
    ax.set_title(f"$F$ = 55 kV/cm, $|\\chi^{{(2)}}|$ = {abs(o['chi'])/1e3:.1f} nm/V", fontsize=7.2)
    for k, c in enumerate((BLUE, MUTED, ORANGE, AQUA)):
        ax.text(17, (E[k] - E[0]) * 1e3 + 6, str(k + 1), color=c, fontsize=7, ha="right")
    clean(ax); label(ax, "(a)")
    # (b) LO-phonon-resolved saturation of chi(2) vs a single 1 ps time
    ax = axs[1]
    for lay, F, c, name in ((TW, 55.0, BLUE, "triple well"), (AD, 0.0, ORANGE, "ADQW")):
        oo = sp.chi2_sc(lay, F, HW, ns_cm2=5e11); Ee, ps, _, _ = sp.prepare(oo["r"])
        t0 = time.time(); R = sc.rate_matrix(oo["r"]["z"], ps, Ee); timing[f"rate_matrix_{name.replace(' ', '_')}_s"] = time.time() - t0
        st = sp.state_set(oo); m1 = pr.Medium(st, HW, R=R); m2 = pr.Medium(st, HW)
        I = np.logspace(8, 11.3, 60)
        ax.semilogx(I / 1e10, [abs(m1.chi(m1.populations(i, 0))) * 1e9 for i in I], color=c, label=f"{'TW' if name == 'triple well' else name}, LO rates")
        ax.semilogx(I / 1e10, [abs(m2.chi(m2.populations(i, 0))) * 1e9 for i in I], color=c, lw=0.8, ls=(0, (2, 1.5)),
                    label=f"{'TW' if name == 'triple well' else name}, 1 ps")
    ax.set_xlabel("Local pump intensity (MW/cm$^2$)"); ax.set_ylabel(r"$|\chi^{(2)}|$ (nm/V)")
    ax.legend(frameon=False, fontsize=7, loc="upper right"); clean(ax); label(ax, "(b)")
    # (c) end-to-end: peak conversion efficiency vs pump (from the N1 study outputs)
    ax = axs[2]; d = os.path.join(here, "data")       # copies of the N1 study outputs (studies/n1_paper)
    B = json.load(open(os.path.join(d, "propagation_lo.json")))["results"]
    S = json.load(open(os.path.join(d, "stark_valid.json")))["results"]      # Stark QPM, optimized valid off field
    BF = [dict(ns=b["ns"], P=b["P"], eta=b["adbip"]) for b in json.load(open(os.path.join(d, "bipolar_fair.json")))["best"]]
    def series(R, des, sch):
        rr = sorted([q for q in R if abs(q["ns"] - 5e11) < 1 and q.get("design", des) == des and q.get("scheme", sch) == sch],
                    key=lambda q: q["P"]); return [q["P"] for q in rr], [q["eta"] * 100 for q in rr]
    for (P, e), c, ls, lab in ((series(B, "tw", "sign"), BLUE, "-", "triple well, sign-reversal QPM"),
                               (series(BF, "ad", "bipolar"), AQUA, "-", r"ADQW, bipolar $\pm F$"),
                               (series(S, "ad", "stark"), ORANGE, "-", "ADQW, Stark QPM"),
                               (series(B, "ad", "sign"), RUST, (0, (5, 1.5)), "ADQW, growth-reversed (ideal)"),
                               (series(B, "ad", "perfect"), MUTED, (0, (3, 2)), "ADQW, perfect PM (bound)")):
        ax.loglog(P, e, color=c, ls=ls, lw=1.2, label=lab)
    oo = sp.chi2_sc(TW, 55.0, HW, ns_cm2=5e11); Ee, ps, _, _ = sp.prepare(oo["r"])
    med = pr.Medium(sp.state_set(oo), HW, R=sc.rate_matrix(oo["r"]["z"], ps, Ee))
    wg = dict(n1=3.231, n2=3.338, G1=0.395, G2=0.514, O_um=0.0531, abg1_cm=3.25, abg2_cm=0.16, t_stack_um=1.512,
              w_um=15.0, Lcoh_um=23.4, lam1_um=10.0)
    t0 = time.time()
    rr = pr.propagate(med, wg, 1.26, "sign", eta_e=0.92, L_max_um=500.0)
    timing["propagation_500um_s"] = time.time() - t0; timing["propagation_500um_steps"] = len(rr["x_um"]) - 1
    ax.set_xlabel("Pump power (W)"); ax.set_ylabel("Peak conversion efficiency (%)")
    ax.set_ylim(1e-3, 300); ax.legend(frameon=False, fontsize=6.4, loc="upper left", handlelength=1.8, labelspacing=0.3); clean(ax); label(ax, "(c)")
    fig.savefig(os.path.join(out, "fig_example.pdf")); plt.close(fig)
    return timing

if __name__ == "__main__":
    t = fig_validation(); t.update(fig_example())
    json.dump(t, open(os.path.join(out, "..", "timing.json"), "w"), indent=1); print(t)
