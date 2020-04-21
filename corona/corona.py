from sys import argv

R = range
X = 'S'
I = int
_, e, f = argv


def g(n): n ^= n << 13; n ^= n >> 17; n ^= n << 5; return n % (1 << 30)
def q(p): x, y = p[0];n = p[3] % 4; return (x + 1 if not n else x - 1 if n == 1 else x) % 8, (y + 1 if n == 2 else y - 1 if n == 3 else y) % 8


z = [[(I(a), I(b)),c, d == '1', (I(a) << 2) ^ 7 * (I(b) << 3) ^ 5, 14] for a,b,c,d in f.split(',')]

for i in R(I(e)):
	for p in z:
		a,b,c,d,e=p
		if b == X:p[4] -= 1
		if not e: p[1] = 'R'
		p[3] = g(d)

		if not c and all(q(p) != o[0] for o in z): p[0] = q(p)
		j = a
		if b == 'H' and any(k == X and j[0] - 1 <= o[0] <= j[0] + 1 and j[1] - 1 <= o[1] <= j[1] + 1 for o,k,_,_,_ in z): p[1] = X

for i in R(64): print(next((m[1] for m in z if m[0] == (i % 8, I(i / 8))), '.'), end='' if i % 8 != 7 else '\n');
