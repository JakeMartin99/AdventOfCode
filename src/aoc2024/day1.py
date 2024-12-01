def pt1(lst1: list[int], lst2: list[int]) -> int:
    sort1, sort2 = sorted(lst1), sorted(lst2)
    assert len(sort1) == len(sort2)
    return sum([abs(pair[0] - pair[1]) for pair in zip(sort1, sort2)])

def pt2(left: list[int], right: list[int]) -> int:
    counts, total = {}, 0
    for l in left:
        if l not in counts:
            counts[l] = right.count(l)
        total += l*counts[l]
    return total

def main():
    with open("../../inputs/day1.txt", "r") as f:
        lst = [tuple(map(int, line.strip().split("   "))) for line in f.readlines()]
        left, right = [p[0] for p in lst], [p[1] for p in lst]
    print("Pt 1:", pt1(left, right))
    print("Pt 2:", pt2(left, right))


if __name__ == "__main__":
    main()
