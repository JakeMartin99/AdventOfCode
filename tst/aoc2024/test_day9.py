from src.aoc2024.day9 import *


ex1 = "2333133121414131402"


def test_pt1():
    val = pt1([int(c) for c in ex1], verbose=True)
    assert val == 1928


def test_pt2():
    val = pt2([int(c) for c in ex1], verbose=True)
    assert val == 2858
