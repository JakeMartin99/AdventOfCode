file = open("day4.txt")
sum1, sum2 = 0, 0
for pair in file.read().split("\n"):
    r1, r2 = pair.split(",")
    r1, r2 = r1.split('-'), r2.split('-')
    if (int(r2[0]) <= int(r1[0]) and int(r1[1]) <= int(r2[1])) or (int(r1[0]) <= int(r2[0]) and int(r2[1]) <= int(r1[1])):
        sum1 +=1
    if int(r2[0]) <= int(r1[0]) <= int(r2[1]) or int(r2[0]) <= int(r1[1]) <= int(r2[1]):
        sum2 +=1
    elif int(r1[0]) <= int(r2[0]) <= int(r1[1]) or int(r1[0]) <= int(r2[1]) <= int(r1[1]):
        sum2 += 1
print(sum1, sum2)
file.close()