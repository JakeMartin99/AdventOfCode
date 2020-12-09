file, L = open("day9.txt"), 25
data = [int(x) for x in file.read().split('\n')[:-1]]
file.close()
preamb = data[0:L]
for num in data[L:]:
    pre_sums = [[x+y for x in preamb] for y in preamb]
    if any([num in x for x in pre_sums]):
        preamb.pop(0)
        preamb.append(num)
    else:
        print("Part 1: " + str(num))
        break
for i in range(0, len(data)-1):
    for j in range(1+i, len(data)):
        if sum(data[i:j+1]) == num:
            print("Part 2: " + str(min(data[i:j+1]) + max(data[i:j+1])))
            exit()
