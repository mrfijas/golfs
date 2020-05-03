<?php
[, $e, $c] = $argv;

// 012345
// xysqnd

$p = array_map(
    function ($e) {
        return [+$e[0], +$e[1], $e[2], $e[3], ($e[0] << 2) ^ 7 * ($e[1] << 3) ^ 5, 14];
    },
    explode(',', $c)
);

function free($x, $y)
{
    global $p;
    foreach ($p as $m) {
        if ($m[0] == $x && $m[1] == $y) return false;
    }

    return true;
}

function mod($n)
{
    return $n < 0 ? 7 : $n % 8;
}

function new_cords($p)
{
    $x = $p[0];
    $y = $p[1];
    switch ($p[4] % 4) {
        case 0:
            $x++;
            break;
        case 1:
            $x--;
            break;
        case 2:
            $y++;
            break;
        case 3:
            $y--;
    }

    return [mod($x), mod($y)];
}

for (; $e; $e--) {
    foreach ($p as $i => $_) {
        $w = &$p[$i];
        $w[2] == 'S' && $w[5]--;
        $w[5] || $w[2] = 'R';
        $n = $w[4];
        $n ^= $n << 13;$n ^= $n >> 17;$n ^= $n << 5;
        $w[4] = $n % (1 << 30);
        [$x, $y] = new_cords($w);
        if ($w[3] != '1' && free($x, $y)) {
            $w[0] = $x;
            $w[1] = $y;
        }

        $x = $w[0]; $y = $w[1];
        foreach ($p as $m) {
            if (
                $m[2] == 'S' &&
                in_array($m[0], [mod($x - 1), $x, mod($x + 1)]) &&
                in_array($m[1], [mod($y - 1), $y, mod($y + 1)])
            ) {
                $w[2] == 'H' && $w[2] = 'S';
            }
        }
    }
}

for ($i = 0; $i < 64; $i++) {
    $x = $i % 8;
    $y = floor($i / 8);
    $dot = '.';
    foreach ($p as $m) {
        if ($m[0] == $x && $m[1] == $y) {
            $dot = $m[2];
        }
    }
    echo $dot . ($i % 8 == 7 ? "\n" : '');
}
