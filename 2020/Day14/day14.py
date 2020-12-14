file = open("day14.txt")
f = file.read().split('\n')[:-1]; file.close()
mask = "0"
store1, store2 = {}, {}
for line in f:
    if line[0:4] == "mask":
        mask = line[7:][::-1]
    elif line[0:3] == "mem":
        data = line.split(' = ')

        loc = int(data[0][data[0].find('[')+1:data[0].find(']')])
        loc2 = bin(loc)[2:][::-1]
        if len(loc2) != len(mask): loc2 += '0' * (len(mask)-len(loc2))
        m_loc = "".join([loc2[i] if mask[i]=='0' else ('1' if mask[i] == '1' else 'X') for i in range(len(mask))][::-1])
        xct = m_loc.count('X'); current = xct * '0'

        num = int(data[1])
        num1 = bin(num)[2:][::-1]
        if len(num1) != len(mask): num1 += '0' * (len(mask)-len(num1))
        m_num = "".join([num1[i] if mask[i]=='X' else mask[i] for i in range(len(mask))][::-1])
        store1[loc] = int(m_num, 2)
        for i in range(2**xct):
            temp_mloc = m_loc
            for c in current: temp_mloc = temp_mloc[:temp_mloc.find('X')] + c + temp_mloc[temp_mloc.find('X')+1:]
            store2[int(temp_mloc, 2)] = num
            current = bin(int(current, 2) + 1)[2:]; current = (xct-len(current))*'0' + current

print("Part 1: " + str(sum([store1[key] for key in store1])))
print("Part 2: " + str(sum([store2[key] for key in store2])))
