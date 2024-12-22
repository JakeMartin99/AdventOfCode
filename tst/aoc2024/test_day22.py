from src.aoc2024.day22 import *


ex1 = [1, 10, 100, 2024]
ex2 = [1, 2, 3, 2024]


def test_pt1():
    val = pt1(ex1)
    assert val == 37327623


def test_pt2():
    val = pt2(ex2)
    assert val == 23

