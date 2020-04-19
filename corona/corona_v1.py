from dataclasses import dataclass, field
from sys import argv
from typing import Tuple

@dataclass
class P:
    p: Tuple
    s: str
    q: bool
    z = 0
    n: int = field(init=False)

    def __post_init__(t): t.n = (t.p[0] << 2) ^ 7 * (t.p[1] << 3) ^ 5


def g(n): n ^= n << 13; n ^= n >> 17; n ^= n << 5; return n % (1 << 30)


def d(p): x, y = p.p;n = p.n % 4; return (x + 1 if not n else x - 1 if n == 1 else x) % 8, (y + 1 if n == 2 else y - 1 if n == 3 else y) % 8


z = [P((int(s[0]), int(s[1])), s[2], s[3] == '1') for s in argv[2].split(',')]

for i in range(int(argv[1])):
    for p in z:
        if p.s == 'S': p.z += 1
        if p.s == 'S' and p.z == 14: p.s = 'R'
        p.n = g(p.n)

        if not p.q:
            n = d(p)
            if not any(n == o.p for o in z): p.p = n
        if p.s == 'H' and any(o.s == 'S' and p.p[0] - 1 <= o.p[0] <= p.p[0] + 1 and p.p[1] - 1 <= o.p[1] <= p.p[1] + 1 for o in z): p.s = 'S'

for y in range(8):
    for x in range(8):
        c = '.'
        for m in z:
            if m.p == (x, y): c = m.s
        print(c, end='')
    print()
