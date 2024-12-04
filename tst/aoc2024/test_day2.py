from src.aoc2024.day2 import *


ex1 = """7 6 4 2 1
         1 2 7 8 9
         9 7 6 2 1
         1 3 2 4 5
         8 6 4 4 1
         1 3 6 7 9"""


def test_pt1():
    val = pt1([list(map(int, line.strip().split(" "))) for line in ex1.split('\n')])
    assert val == 2


def test_pt2():
    val = pt2([list(map(int, line.strip().split(" "))) for line in ex1.split('\n')])
    assert val == 4
