import ast as a, subprocess as s, sys as y, autopep8 as b, random as r, importlib as i
from functools import reduce

class PAF:
    def __init__(self, f):
        self.f = f

    def r(self):
        with open(self.f, 'r+') as f:
            c = f.read()
        self._t(c)
        f.seek(0)
        f.write(self._b(c))
        f.truncate()
        print("[✓] Fixed!")

    def _t(self, c):
        try:
            a.parse(c)
            print("[✓] No errors!")
        except SyntaxError as e:
            print(f"[!] Error: {e}")

    def _b(self, c):
        return b.fix_code(c)

    def _q(self, c):
        x = {line.split()[1]: line for line in c.splitlines() if line.startswith(('import', 'from'))}
        return '\n'.join(line for line in c.splitlines() if line.split()[1] in x and self._u(line.split()[1], c))

    def _u(self, imp, c):
        return imp in c

    def _m(self, c):
        m = {i for i in c.split() if i.isidentifier() and not self._g(i)}
        for mod in m:
            if self._a(mod):
                s.check_call([y.executable, "-m", "pip", "install", mod])
                print(f"[✓] Installed: {mod}")
        return c

    def _g(self, mod):
        try:
            i.import_module(mod)
            return True
        except ImportError:
            return False

    def _a(self, mod):
        return input(f"[!] Missing: {mod}. Install it? (y/n): ").strip().lower() == 'y'

    def _p(self, c):
        t = a.parse(c)
        for n in a.walk(t):
            if isinstance(n, a.FunctionDef) and not a.get_docstring(n):
                c = c.replace(n.name + '(', f'"""{n.name}() function"""\n' + n.name + '(')
        return c

    def _f(self, c):
        return reduce(lambda x, y: x.replace(y, '') if 'True |' in x else x, c.splitlines(), c)

if __name__ == "__main__":
    f = input("Path: ").strip()
    PAF(f).r()
