import ast as a

class F:
    def __init__(s, p): s.p = p

    def R(s): 
        with open(s.p) as f: return f.readlines()

    def W(s, c):
        with open(s.p, "w") as f: f.writelines(c)

    def S(s, c):
        try: a.parse("".join(c)); print("[✓] No Errors."); return 1
        except SyntaxError as e: print(f"[!] Error: {e}"); return 0

    def U(s, c):
        t, u, n = a.parse("".join(c)), set(), []
        [u.add(x.id) for x in a.walk(t) if isinstance(x, a.Name)]
        [n.append(l) if not (l.startswith(("import ", "from ")) and l.split()[1] not in u) else None for l in c]
        return n

    def X(s, c):
        o, d = [], 0
        for l in c:
            L, l = l.strip(), l.rstrip() + ":\n" if L.startswith(("if ", "elif ", "else", "for ", "while ", "def ", "class ")) and not L.endswith(":") else l
            l = l.rstrip() + ")\n" if L.count("(") > L.count(")") else l
            l = l.rstrip() + "]\n" if L.count("[") > L.count("]") else l
            l = l.rstrip() + "}\n" if L.count("{") > L.count("}") else l
            d = d + 4 if L.endswith(":") else max(0, d - 4) if L == "" else d
            o.append(" " * d + l.lstrip())
        return o

    def I(s, c): return [l.rstrip() + "\n" for l in c]

    def P(s):
        c = s.R()
        if not s.S(c): print("[!] Fixing..."); c = s.X(c)
        s.W(s.I(s.U(c)))
        print("[✓] Fixed.")

if __name__ == "__main__":
    F(input("File: ").strip()).P()
