from src.aoc2024.day1 import *


ex1 = [(3, 4),
       (4, 3),
       (2, 5),
       (1, 3),
       (3, 9),
       (3, 3)]


def test_pt1():
    val = pt1([p[0] for p in ex1], [p[1] for p in ex1])
    assert val == 11


def test_pt2():
    val = pt2([p[0] for p in ex1], [p[1] for p in ex1])
    assert val == 31
