file = open("day5.txt")
state, proc = file.read().split("\n\n")
cols = state.split("\n")
labels = list(map(lambda x: int(x), filter(lambda x: len(x)>0 and x != ' ',cols[-1].split(' '))))
stax = list(map(lambda x: x[1:-1:4], reversed(cols[:-1])))
stacks, stacks2 = {}, {}
for l in labels:
    stacks[l], stacks2[l] = [], []
for row in stax:
    for idx,l in enumerate(labels):
        c = row[idx]
        if c != ' ':
            stacks[l].append(c)
            stacks2[l].append(c)
moves = [(int(s.split(' ')[1]), int(s.split(' ')[3]), int(s.split(' ')[5])) for s in proc.split("\n")]
for m in moves:
    quant, frm, to = m
    chunk2 = []
    for q in range(quant):
        char = stacks[frm].pop()
        stacks[to].append(char)
        char2 = stacks2[frm].pop()
        chunk2.append(char2)
    chunk2.reverse()
    stacks2[to].extend(chunk2)
    
str1, str2 = "", ""
for l in labels:
    str1 += stacks[l][-1]
    str2 += stacks2[l][-1]
print(str1, str2)
file.close()