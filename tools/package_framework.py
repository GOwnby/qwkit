"""Package the research framework as numbered zips (delivery convention of 15 Oct 2026):
  1-roadmap.zip    roadmap, index, open items, notes, literature tracking, the qwkit package, tests, tools, docs;
  2-papers.zip ... one zip per paper in programme order: its PDF, LaTeX source folder and study folder(s).
A new paper gets the next number. Superseded outputs kept for audit (pre_* folders) are included as long as each zip
stays under 29 MB; otherwise they are left out and the zip says so.
Usage: python3 tools/package_framework.py OUTDIR"""
import os, sys, zipfile, fnmatch, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIMIT = 29e6
PAPERS = [  # (id, pdf, source folders, study folders)
    ("MS-01_software", ["qwkit_software_paper.pdf", "qwkit_user_guide.pdf"], ["paper_software"], ["studies/kane"]),
    ("METH-01", ["METH01_paper.pdf"], ["paper_meth01"], ["studies/meth01"]),
    ("N1", ["N1_paper.pdf"], ["paper"], ["studies/n1", "studies/n1_paper", "studies/rerun_n1.sh"]),
    ("NL-02", ["NL02_paper.pdf"], ["paper_nl02"], ["studies/nl02", "studies/rerun_nl02.sh"]),
    ("NL-05", ["NL05_paper.pdf"], ["paper_nl05"], ["studies/nl05", "studies/rerun_nl05.sh"]),
    ("MS-02", ["MS02_paper.pdf"], ["paper_ms02"], ["studies/ms02", "studies/rerun_ms02.sh", "studies/rerun_ms02_rest.sh"]),
    ("TPV-05", ["TPV05_paper.pdf"], ["paper_tpv05"], ["studies/tpv05", "studies/rerun_tpv05.sh"]),
    ("MAT-01", ["MAT01_paper.pdf"], ["paper_mat01"], ["studies/mat01", "studies/rerun_mat01.sh"]),
    ("MAT-02", ["MAT02_paper.pdf"], ["paper_mat02"], ["studies/mat02", "studies/rerun_mat02.sh"]),
    ("MAT-03", ["MAT03_paper.pdf"], ["paper_mat03"], ["studies/mat03"]),
    ("N2", ["N2_paper.pdf"], ["paper_n2"], ["studies/n2"]),
]
ROADMAP = ["FRAMEWORK_INDEX.md", "LATER_STAGE.md", "SUBMISSION_CHECKLIST.md", "README.md", "CHANGELOG.md", "CITATION.cff",
           "LICENSE", "CODE_OF_CONDUCT.md", "CONTRIBUTING.md", "MANIFEST.in", "pyproject.toml", "Research_Roadmap.pdf",
           "LITERATURE_STATUS.md", "docs", "qwkit", "tests", "tools", "examples",
           "studies/scoping", "studies/mat04", "studies/pre_lowdinfix", "studies/queue_bcfix.sh", "studies/queue_lowdin.sh",
           "studies/queue_phase2.sh", "studies/*.log", ".zenodo.json", ".gitignore", ".github"]
SKIP = ["*/__pycache__/*", "*.pyc", "*.aux", "*.out", "*.toc", "*.blg", "*.synctex.gz", "*.fls", "*.fdb_latexmk", "*/.git/*"]


def files(paths, with_pre=True):
    out = []
    exp = []
    for p in paths:
        exp += [os.path.relpath(q, ROOT) for q in glob.glob(os.path.join(ROOT, p))] if "*" in p else [p]
    for p in exp:
        full = os.path.join(ROOT, p)
        if os.path.isfile(full):
            out.append(p); continue
        if not os.path.isdir(full):
            continue
        for d, _, fs in os.walk(full):
            for f in fs:
                rel = os.path.relpath(os.path.join(d, f), ROOT)
                if any(fnmatch.fnmatch("/" + rel, pat) for pat in SKIP):
                    continue
                if not with_pre and any(part.startswith("pre_") for part in rel.split(os.sep)):
                    continue
                out.append(rel)
    return sorted(set(out))


def write(zpath, rels, note=None):
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for r in rels:
            z.write(os.path.join(ROOT, r), os.path.join("qwkit", r))
        if note:
            z.writestr("qwkit/PACKAGE_NOTE.txt", note)
    return os.path.getsize(zpath)


def build(name, paths, outdir):
    zp = os.path.join(outdir, name)
    size = write(zp, files(paths, True))
    if size > LIMIT:
        size = write(zp, files(paths, False), "Superseded outputs (pre_* folders) were left out to keep this zip under "
                     "the 30 MB transfer limit; they remain in the working repository.\n")
        return size, False
    return size, True


if __name__ == "__main__":
    outdir = sys.argv[1] if len(sys.argv) > 1 else "."
    os.makedirs(outdir, exist_ok=True)
    rows = [("1-roadmap.zip", "roadmap and supplementary documents, qwkit", *build("1-roadmap.zip", ROADMAP, outdir))]
    k = 2
    for pid, pdfs, src, st in PAPERS:
        if not os.path.exists(os.path.join(ROOT, pdfs[0])):
            continue
        name = f"{k}-papers.zip"
        rows.append((name, pid, *build(name, pdfs + src + st, outdir))); k += 1
    for name, what, size, pre in rows:
        print(f"{name:16s} {what:45s} {size / 1e6:6.1f} MB{'' if pre else '  (pre_* outputs left out)'}")
