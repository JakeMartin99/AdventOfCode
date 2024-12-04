def pt1(reports: list[list[int]]) -> int:
    total = 0
    for report in reports:
        deltas = [report[i+1] - report[i] for i in range(len(report)-1)]
        if all([1 <= delta <= 3 for delta in deltas]) or all([-1 >= delta >= -3 for delta in deltas]):
            total += 1
    return total


def pt2(reports: list[list[int]]) -> int:
    total = 0
    for report in reports:
        deltas = [report[i+1] - report[i] for i in range(len(report)-1)]
        if all([1 <= delta <= 3 for delta in deltas]) or all([-1 >= delta >= -3 for delta in deltas]):
            total += 1
        else:
            for i in range(len(report)):
                deltas_v2 = [d for d in deltas]
                if i == 0:
                    deltas_v2.pop(0)
                elif i == len(deltas):
                    deltas_v2.pop(-1)
                else:
                    new_delta = deltas_v2[i-1] + deltas_v2[i]
                    deltas_v2[i] = new_delta
                    deltas_v2.pop(i-1)
                if all([1 <= delta <= 3 for delta in deltas_v2]) or all([-1 >= delta >= -3 for delta in deltas_v2]):
                    total += 1
                    break
    return total


def main():
    with open("../../inputs/day2.txt", "r") as f:
        reports = [list(map(int, line.strip().split(" "))) for line in f.readlines()]
    print("Pt 1:", pt1(reports))
    print("Pt 2:", pt2(reports))


if __name__ == "__main__":
    main()
