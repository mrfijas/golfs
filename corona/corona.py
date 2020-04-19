from sys import argv

R = range
X = 'S'
I = int
_, e, f = argv


def g(n): n ^= n << 13; n ^= n >> 17; n ^= n << 5; return n % (1 << 30)
def d(p): x, y = p[0];n = p[3] % 4; return (x + 1 if not n else x - 1 if n == 1 else x) % 8, (y + 1 if n == 2 else y - 1 if n == 3 else y) % 8


z = [[(I(s[0]), I(s[1])), s[2], s[3] == '1', (I(s[0]) << 2) ^ 7 * (I(s[1]) << 3) ^ 5, 14] for s in f.split(',')]

for i in R(I(e)):
	for p in z:
		if p[1] == X:
			p[4] -= 1
			if not p[4]: p[1] = 'R'
		p[3] = g(p[3])

		if not p[2] and not any(d(p) == o[0] for o in z): p[0] = d(p)
		j = p[0]
		if p[1] == 'H' and any(o[1] == X and j[0] - 1 <= o[0][0] <= j[0] + 1 and j[1] - 1 <= o[0][1] <= j[1] + 1 for o in z): p[1] = X

for i in R(64): print(next((m[1] for m in z if m[0] == (i % 8, I(i / 8))), '.'), end='' if i % 8 != 7 else '\n');
