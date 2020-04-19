from sys import argv


def g(n): n ^= n << 13; n ^= n >> 17; n ^= n << 5; return n % (1 << 30)


def d(p): x, y = p[0];n = p[3] % 4; return (x + 1 if not n else x - 1 if n == 1 else x) % 8, (y + 1 if n == 2 else y - 1 if n == 3 else y) % 8


z = [[(int(s[0]), int(s[1])), s[2], s[3] == '1', (int(s[0]) << 2) ^ 7 * (int(s[1]) << 3) ^ 5, 0] for s in argv[2].split(',')]

for i in range(int(argv[1])):
    for p in z:
        if p[1] == 'S': p[4] += 1
        if p[1] == 'S' and p[4] == 14: p[1] = 'R'
        p[3] = g(p[3])

        if not p[2]:
            n = d(p)
            if not any(n == o[0] for o in z): p[0] = n
        if p[1] == 'H' and any(o[1] == 'S' and p[0][0] - 1 <= o[0][0] <= p[0][0] + 1 and p[0][1] - 1 <= o[0][1] <= p[0][1] + 1 for o in z): p[1] = 'S'

r=range(8)
for y in r:
    for x in r:
        c = '.'
        for m in z:
            if m[0] == (x, y): c = m[1]
        print(c, end='')
    print()
