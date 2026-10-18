"""MAT-04 scoping: how much do collective (depolarization) effects move and change the 'giant chi(2)' of BaSnO3/BaO
double quantum wells (Li, Hamze and Demkov, Phys. Rev. B 104, 235419 (2021): 4 and 7 unit-cell BaSnO3 wells, one BaO
barrier layer, about 1e19 cm^-3 average doping)? Self-consistent Hartree with qwkit.sp, BaSnO3 (m 0.19, Kane gap
1/0.56 eV, eps 20) and BaO barriers (offset 1.74 eV as in Li et al.; mass and barrier thickness unknown: 0.4 or 1.0 m0,
2.5 or 5.5 A), sheet density 4.5e12 cm^-2 (1e19 cm^-3 over the wells), 300 K, 10 meV linewidth; depolarization with
eps_inf 3.3 or 4.3 (BaSnO3, Stanislavchuk 2012 / Krishnaswamy 2017). Reports the transition energies with and without
depolarization and the largest |chi(2)| and its pump energy for pump energies above 0.12 eV (above the BaSnO3 LO
phonons; below, the polar-phonon background, not included here, dominates). Writes scoping.json."""
import json, os, itertools
import numpy as np
from multiprocessing import Pool
from qwkit import sp, core as q

here = os.path.dirname(os.path.abspath(__file__))
UC = 4.116


def job(args):
    tb, mb, einf = args
    q.add_material("well", 0.0, 0.19, 1.0 / 0.56, eps=20.0)
    q.add_material("barrier", 1.74, mb, 4.0, eps=34.0)
    lay = [(4 * UC, "well"), (tb, "barrier"), (7 * UC, "well")]
    ns = 1e19 * 11 * UC * 1e-8
    out = dict(tb=tb, mb=mb, eps_inf=einf, ns=ns)
    hws = np.arange(0.12, 0.70, 0.001)
    for dep in (False, True):
        o = sp.chi2_sc(lay, 0.0, 0.3, ns_cm2=ns, T=300.0, spacer=200.0, doping="wells", depol=dep,
                       pad_material="barrier", m_dos=0.19, eps_depol=einf)
        Et = o["Et"]; E = o["E"]
        ch = np.array([abs(sp.chi2_depol(Et, o["Z"], o["rho"], h, 0.010, o["N"])) for h in hws])
        i = int(np.argmax(ch))
        # chi(2) normalized to the well-averaged density 1e19 cm^-3 (Li et al.'s convention) instead of the box average
        scale = 1e19 / o["N"]
        out["depol" if dep else "bare"] = dict(E=(E - E[0])[:5].tolist(), E21=float(Et[1, 0]), E31=float(Et[2, 0]),
                                               E32=float(Et[2, 1]), chi_max_nm=float(ch[i] * scale / 1000), hw_max=float(hws[i]),
                                               Z=np.asarray(o["Z"])[:3, :3].tolist())
    b, d = out["bare"], out["depol"]
    print(f"tb {tb} mb {mb} eps_inf {einf}: E21 {1000 * b['E21']:.0f}->{1000 * d['E21']:.0f} meV, E31 {1000 * b['E31']:.0f}->"
          f"{1000 * d['E31']:.0f} | |chi2|max {b['chi_max_nm']:.0f} nm/V at {1000 * b['hw_max']:.0f} meV -> {d['chi_max_nm']:.0f} nm/V at "
          f"{1000 * d['hw_max']:.0f} meV", flush=True)
    return out


if __name__ == "__main__":
    jobs = list(itertools.product((2.5, 5.5), (0.4, 1.0), (3.3, 4.3)))
    with Pool(int(os.environ.get("NPROC", "2"))) as pool:
        res = pool.map(job, jobs, chunksize=1)
    json.dump(res, open(os.path.join(here, "scoping.json"), "w"), indent=1)
