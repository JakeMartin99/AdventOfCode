def validate(lst: list[chr]) -> int:
    return 1 if (lst[0] == 'M' and lst[1] == 'A' and lst[2] == 'S') else 0


def pt1(grid: list[list[chr]]) -> int:
    total, width, height = 0, len(grid[0]), len(grid)
    for y in range(height):
        for x in range(width):
            if grid[y][x] == 'X':
                if y-3 >= 0:
                    north = [grid[y-i][x] for i in range(1,4)]
                    total += validate(north)
                if y-3 >= 0 and x+3 < width:
                    northeast = [grid[y-i][x+i] for i in range(1,4)]
                    total += validate(northeast)
                if x+3 < width:
                    east = [grid[y][x+i] for i in range(1,4)]
                    total += validate(east)
                if y+3 < height and x+3 < width:
                    southeast = [grid[y+i][x+i] for i in range(1,4)]
                    total += validate(southeast)
                if y+3 < height:
                    south = [grid[y+i][x] for i in range(1,4)]
                    total += validate(south)
                if y+3 < height and x-3 >= 0:
                    southwest = [grid[y+i][x-i] for i in range(1,4)]
                    total += validate(southwest)
                if x-3 >= 0:
                    west = [grid[y][x-i] for i in range(1,4)]
                    total += validate(west)
                if y-3 >= 0 and x-3 >= 0:
                    northwest = [grid[y-i][x-i] for i in range(1,4)]
                    total += validate(northwest)
    return total


def pt2(grid: list[list[chr]]) -> int:
    total, width, height = 0, len(grid[0]), len(grid)
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            if grid[y][x] == 'A':
                corners = grid[y-1][x+1], grid[y+1][x+1], grid[y+1][x-1], grid[y-1][x-1]
                if corners.count('M') == 2 and corners.count('S') == 2 and corners[0] != corners[2]:
                    total += 1
    return total


def main():
    with open("../../inputs/aoc2024/day4.txt", "r") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    print("Pt 1:", pt1(grid))
    print("Pt 2:", pt2(grid))


if __name__ == "__main__":
    main()
