from src.aoc2024.day4 import *


ex1 = """MMMSXXMASM
         MSAMXMSMSA
         AMXSXMAAMM
         MSAMASMSMX
         XMASAMXAMM
         XXAMMXXAMA
         SMSMSASXSS
         SAXAMASAAA
         MAMMMXMMMM
         MXMXAXMASX"""


def test_pt1():
    val = pt1([list(line.strip()) for line in ex1.split('\n')])
    assert val == 18


def test_pt2():
    val = pt2([list(line.strip()) for line in ex1.split('\n')])
    assert val == 9
