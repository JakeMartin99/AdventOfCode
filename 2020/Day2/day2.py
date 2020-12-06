file = open("day2.txt")
lines = [l for l in file.read().split("\n") if l]
file.close()
total1 = 0
total2 = 0
for line in lines:
    div = line.split(":")
    passwd = div[1].strip(' ')
    c = div[0][-1]
    (low, high) = div[0].split(' ')[0].split('-')
    num = passwd.count(c)
    if int(low) <= num and num <= int(high): total1 += 1
    if bool(passwd[int(low) - 1] == c) ^ bool(passwd[int(high) - 1] == c): total2 += 1

print("\nPart 1: " + str(total1))
print("Part 2: " + str(total2))
