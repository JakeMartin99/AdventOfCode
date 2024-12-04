import re


def pt1(instr: str) -> int:
    regex = r'mul\(([0-9]+),([0-9]+)\)'
    return sum(map(lambda ins: int(ins[0]) * int(ins[1]), re.findall(regex, instr)))


def pt2(instr: str) -> int:
    regex = r'(don\'t\(\))|(do\(\))|(mul\(([0-9]+),([0-9]+)\))'
    enabled, total = True, 0
    for ins in re.findall(regex, instr):
        if ins[0] != "":
            enabled = False
        elif ins[1] != "":
            enabled = True
        elif ins[2] != "":
            total += int(ins[3]) * int(ins[4]) if enabled else 0
        else:
            raise ValueError("Invalid instruction:", ins)
    return total


def main():
    with open("../../inputs/aoc2024/day3.txt", "r") as f:
        instr = "".join([line for line in f.readlines()])
    print("Pt 1:", pt1(instr))
    print("Pt 2:", pt2(instr))


if __name__ == "__main__":
    main()
