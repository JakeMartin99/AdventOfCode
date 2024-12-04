from src.aoc2024.day3 import *


ex1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
ex2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def test_pt1():
    val = pt1(ex1)
    assert val == 161


def test_pt2():
    val = pt2(ex2)
    assert val == 48
