file = open("day8.txt")
code = file.read().split('\n')
code = [(line[0:3], int(line[4:]) if line[3] == '+' else int(line[3:])) for line in code]
file.close()
def compute(code) -> int:
    acc, iptr = 0, 0
    visited = []
    while iptr < len(code):
        visited.append(iptr)
        if(code[iptr][0] == "acc"):
            acc += code[iptr][1]
            iptr += 1
        elif(code[iptr][0] == "jmp"):
            iptr += code[iptr][1]
        elif(code[iptr][0] == "nop"):
            iptr += 1
        if iptr in visited:
            break
    return (acc, visited[-1])
solve = compute(code)
print("Part 1: " + str(solve[0]))
for i in range(0, len(code)):
    saveop = code[i]
    code[i] = ("nop" if saveop[0] == "jmp" else ("jmp" if saveop[0] == "nop" else "acc"), saveop[1])
    solve2 = compute(code)
    if solve2[1] == len(code) - 1:
        break
    else:
        code[i] = saveop
print("Part 2: " + str(solve2[0]))
