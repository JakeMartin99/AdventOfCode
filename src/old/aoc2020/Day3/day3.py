file = open("day3.txt")
lines = []
lines2_1 = []
lines2_5 = []
lines2_7 = []
lines2_2 = []
i=0
for line in file.read().split("\n"):
    if line:
        lines.append(line[(i*3) % len(line)])
        lines2_1.append(line[(i) % len(line)])
        lines2_5.append(line[(i*5) % len(line)])
        lines2_7.append(line[(i*7) % len(line)])
        if i%2 == 0:
            lines2_2.append(line[int(i/2) % len(line)])
        i+=1

print("Part 1: " + str(lines.count('#')))
print("Part 2: ")
a = lines2_1.count('#')
b = lines.count('#')
c = lines2_5.count('#')
d = lines2_7.count('#')
e = lines2_2.count('#')
print("\ta: " + str(a))
print("\tb: " + str(b))
print("\tc: " + str(c))
print("\td: " + str(d))
print("\te: " + str(e))
print("Mult: " + str(a*b*c*d*e))
