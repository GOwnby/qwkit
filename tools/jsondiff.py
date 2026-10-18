"""Numeric diff of two JSON files: prints leaf paths whose values changed by more than a relative tolerance."""
import json, sys, math

def walk(a, b, path, out, tol):
    if isinstance(a, dict) and isinstance(b, dict):
        for k in a:
            if k in b:
                walk(a[k], b[k], path + [str(k)], out, tol)
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            out.append(("/".join(path), f"len {len(a)} -> {len(b)}", None)); return
        for i, (x, y) in enumerate(zip(a, b)):
            walk(x, y, path + [str(i)], out, tol)
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)) and not isinstance(a, bool):
        if a == b: return
        if not (math.isfinite(a) and math.isfinite(b)): out.append(("/".join(path), a, b)); return
        rel = abs(b - a) / max(abs(a), abs(b), 1e-300)
        if rel > tol: out.append(("/".join(path), a, b))

a, b = json.load(open(sys.argv[1])), json.load(open(sys.argv[2]))
tol = float(sys.argv[3]) if len(sys.argv) > 3 else 0.005
out = []; walk(a, b, [], out, tol)
for p, x, y in out[: int(sys.argv[4]) if len(sys.argv) > 4 else 80]:
    print(f"{p}: {x} -> {y}" + (f"  ({(y-x)/abs(x)*100:+.1f}%)" if isinstance(x, (int, float)) and isinstance(y, (int, float)) and x else ""))
print(f"# {len(out)} values changed by more than {tol*100:.1f}%")
