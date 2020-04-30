let {argv: [, , e, c], stdout: v} = process;
p = c.split`,`.map(([x, y, s, q]) => ({x: +x, y: +y, s, q, n: (x << 2) ^ 7 * (y << 3) ^ 5, d: 14}))

g = n => {
    n = BigInt(n);n ^= n << 13n;n ^= n >> 17n;n ^= n << 5n;
    return Number(n) % (1 << 30)
}

u = n => n < 0 ? 7 : n % 8
t = (r, l) => [u(r - 1), r, u(r + 1)].includes(l)
f='S'
for (j = +e; j; j--) {
    p.map(m => {
        let {x, y, s} = m
        s == f && m.d--
        m.d || (m.s = 'R')
        m.n = g(m.n)
        if (!+m.q) {
            [a, b] = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]][m.n % 4].map(x => u(x))

            if (p.every(c => a^c.x || b^c.y)) {
                m.x = a
                m.y = b
            }
        }
        s == 'H' && p.some(p => p.s == f && t(m.x,p.x) && t(m.y,p.y)) && (m.s = f)
    })
}

for (x = 0; x < 64;) v.write((p.find(o =>o.x==x%8&& o.y == ~~(x / 8))||{s:'.'}).s + (x++%8==7?"\n":''))
