[, , e, c] = process.argv;
p = c.split(',').map(([x, y, s, q]) => ({x: +x, y: +y, s, q, n: (x << 2) ^ 7 * (y << 3) ^ 5, d: 0}))

function gen_n(n) {
    n = BigInt(n);
    n ^= n << 13n;
    n ^= n >> 17n;
    n ^= n << 5n;
    return Number(n) % (1 << 30)
}

u = n => n < 0 ? 7 : n % 8

for (let j = 0; j < +e; j++) {
    p.map(({x, y, s, q, n}, i) => {
        let m = p[i]
        s == 'S' && m.d++
        m.d == 14 && (m.s = 'R')
        m.n = gen_n(n)
        if (q != 1) {
            let [a, b] = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]][m.n % 4].map(x => u(x))

            if (p.every(({x, y}) => a != x || b != y)) {
                m.x = a
                m.y = b
            }
        }
        s == 'H' && p.some(p => p.s == 'S' && [u(m.x - 1), m.x, u(m.x + 1)].includes(p.x) && [u(m.y - 1), m.y, u(m.y + 1)].includes(p.y)) && (m.s = 'S')
    })
}

for (y = 0; y < 8; y++) {
    for (x = 0; x < 8; x++) {
        d = p.find(o => o.x == x && o.y == y);
        process.stdout.write(d ? d.s : '.')
    }
    console.log()
}
