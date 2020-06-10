<?php

error_reporting(E_ERROR);
echo "<pre>";
function getJumpPath($n = 5) {

    $chp = [];
    for ($i = 1; $i <= $n; $i++) {
        for ($k = 1; $k <= $i; $k++) {
            $chp[$i][$k] = $k;
        }
    }
    return $chp;
}

removeFirst(getJumpPath(), 5, 4, 2);
function getCheesLeve($ch) {
    if (empty($ch)) {
        return 0;
    }
    $cout = 0;
    foreach ($ch as $key => $val) {
        if (is_array($val)) {
            $cout += count($val);
        }
    }
    return $cout;
}

// 已删除列表
function moveChess($chp, $delList, $detx, $dety, $x, $y, $xR, $yR, $deep = 1, &$records = []) {

    // 删除元素
    unset($chp[$x][$y]);
    unset($chp[$xR][$yR]);
    $chp[$detx][$dety] = $dety;
    $delList[$x][$y] = $y;
    $delList[$xR][$yR] = $yR;
    unset($delList[$detx][$dety]);
    $c = getCheesLeve($chp);

    //判断剩下元素
    if ($c == 1) {
        $records [] = "  { $c }  $x, $y=> $detx, $dety ";
        return $chp;
    }
    $capable = [];
    foreach ($delList as $key => $value) {
        if (count($value) > 0) {
            foreach ($value as $v) {
                $t_m = getCapableChess($chp, $key, $v);
                $capable = array_merge($capable, $t_m);
            }
        }
    }
    if (!count($capable)) {
        return false;
    }
    foreach ($capable as $a) {
        $r = moveChess($chp, $delList, $a[4], $a[5], $a[0], $a[1], $a[2], $a[3], ++$deep, $records);
        if ($r == false) {
            continue;
        } else {
            $records [] = "  { $c }  $x, $y=> $detx, $dety ";
            return $r;
        }
    }
}

function removeFirst($chp, $n, $x = 1, $y = 1) {
    //移除第一课棋子
    unset($chp[$x][$y]);

    $capableList = getCapableChess($chp, $x, $y, $n);
    $records = [];
    foreach ($capableList as $i => $a) {
        moveChess($chp, [$x => [$y => $y]], $x, $y, $a[0], $a[1], $a[2], $a[3], 1, $records[$i]);
        $records[$i] = array_reverse($records[$i]);
    }
    print_r($records);
}

function getCapableChess($chp, $x = 1, $y = 1, $n = 5) {
    $xUp = $x + 2;
    $xDown = $x - 2;
    $yUp = $y + 2;
    $yDown = $y - 2;
    $result = [];

    // 正左
    if ($yDown > 0) {
        $chp[$x][$yDown] && $chp[$x][$yDown + 1] && $result[] = [$x, $yDown, $x, $yDown + 1, $x, $y];
    }
    // 正右
    if ($yUp <= $n && $x >= $yUp) {
        $chp[$x][$yUp] && $chp[$x][$yUp - 1] && $result[] = [$x, $yUp, $x, $yUp - 1, $x, $y];
    }
    // 左上
    if ($xDown > 0 && $yDown > 0) {
        $chp[$xDown][$yDown] && $chp[$xDown + 1][$yDown + 1] && $result[] = [$xDown, $yDown, $xDown + 1, $yDown + 1, $x, $y];

    }
    // 左下
    if ($xUp <= $n) {
        $chp[$xUp][$y] && $chp[$xUp - 1][$y] && $result[] = [$xUp, $y, $xUp - 1, $y, $x, $y];
    }
    // 右下
    if ($yUp <= $n && $xUp <= $n) {
        $chp[$xUp][$yUp] && $chp[$xUp - 1][$yUp - 1] && $result[] = [$xUp, $yUp, $xUp - 1, $yUp - 1, $x, $y];
    }
    // 右上
    if ($xDown > 0 && $xDown >= $y) {
        $chp[$xDown][$y] && $chp[$xDown + 1][$y] && $result[] = [$xDown, $y, $xDown + 1, $y, $x, $y];
    }
    return $result;
}

echo "</pre>";
