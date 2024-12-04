file = open("day10.txt")
instr = file.read().split('\n')
file.close()

cycle, X = 1, 1
sig_str = []
crt = []
for ins in instr:
    i = ins.split(' ')
    if i[0] == "addx":
        crt.append('#' if X-1 <= (cycle-1)%40 <= X+1 else '.')
        if cycle - 20 >= 0 and (cycle - 20) % 40 == 0: sig_str.append(cycle * X)
        cycle += 1
        crt.append('#' if X-1 <= (cycle-1)%40 <= X+1 else '.')
        if cycle - 20 >= 0 and (cycle - 20) % 40 == 0: sig_str.append(cycle * X)
        cycle += 1
        X += int(i[1])
    elif i[0] == "noop":
        crt.append('#' if X-1 <= (cycle-1)%40 <= X+1 else '.')
        if cycle - 20 >= 0 and (cycle - 20) % 40 == 0: sig_str.append(cycle * X)
        cycle += 1
print(sum(sig_str))
idx = 0
for r in range(6):
    for c in range(40):
        print(crt[idx], end="")
        idx += 1
    print()