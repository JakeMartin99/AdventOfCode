file = open("day6.txt")
groups = file.read().split('\n\n')
file.close()
num = sum([len(set(x.replace('\n', ''))) for x in groups])
print("Part 1: " + str(num))
an_set = [x.split('\n') for x in groups]
def solve(x):
    return [min([1 if c in row else 0 for row in x]) for c in set("".join(x))]
num2 = sum([sum(solve(x)) for x in an_set])
print("Part 2: " + str(num2))
