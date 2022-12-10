def priority(char):
    o = ord(char)
    if ord('A') <= o <= ord('Z'):
        return o - ord('A') + 27
    else:
        return o - ord('a') + 1

chars = [chr(o) for o in range(ord('A'), ord('Z')+1)]
chars.extend([chr(o) for o in range(ord('a'), ord('z')+1)])
file = open("day3.txt")
sum1, sum2 = 0, 0
group = ['','','']
for ruck in file.read().split("\n"):
    l = len(ruck)
    if l > 0:
        comp1 = ruck[0:l//2]
        comp2 = ruck[l//2:]
        do1, do2 = True, False
        if group[0] == '':
            group[0] = ruck
        elif group[1] == '':
            group[1] = ruck
        elif group[2] == '':
            group[2] = ruck
            do2 = True
        for c in chars:
            if do1 and c in comp1 and c in comp2:
                sum1 += priority(c)
                do1 = False
            if do2 and all([c in g for g in group]):
                sum2 += priority(c)
                do2 = False
                group = ['','','']
            if not do1 and not do2:
                break
print(sum1, sum2)
file.close()