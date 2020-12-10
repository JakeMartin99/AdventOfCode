import math
file = open("day10.txt")
data = [int(x) for x in file.read().split('\n')[:-1]]
data.append(0)
data.sort()
file.close()
data.append(data[-1] + 3)
difs= []
for i in range(len(data)-1):
    difs.append(data[i+1] - data[i])
print("Part 1: " + str(difs.count(1)*difs.count(3)))
ones = ""
for c in str(difs):
    if c == '1' or c == '3': ones += c
ones = [sum([math.comb(len(s)-1, n) for n in range(3)]) for s in ones.split('3') if len(s) > 1]
x = 1
for num in ones:
    x *= num
print("Part2: " + str(x))
