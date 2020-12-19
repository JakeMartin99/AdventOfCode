file = open("day17.txt")
cube = [file.read().split('\n')[:-1]]
hypercube = [[x for x in cube]]
file.close()
p=False
def update(cube, s, i, j):
    curr = cube[s][i][j]
    neighbors = [cube[s2][i2][j2] for s2 in range(s-1, s+2) for i2 in range(i-1, i+2) for j2 in range(j-1, j+2) if not (s2==s and i2==i and j2==j) and 0<=s2<len(cube) and 0<=i2<len(cube[s2]) and 0<=j2<len(cube[s2][i2])]
    active_n = neighbors.count('#')
    return '#' if (curr == '#' and 2<=active_n<=3) or (curr == '.' and active_n==3) else '.'
def update2(hypercube, c, s, i, j):
    curr = hypercube[c][s][i][j]
    neighbors = [hypercube[c2][s2][i2][j2] for c2 in range(c-1, c+2) for s2 in range(s-1, s+2) for i2 in range(i-1, i+2) for j2 in range(j-1, j+2) if not (c2==c and s2==s and i2==i and j2==j) and 0<=c2<len(hypercube) and 0<=s2<len(hypercube[c2]) and 0<=i2<len(hypercube[c2][s2]) and 0<=j2<len(hypercube[c2][s2][i2])]
    active_n = neighbors.count('#')
    return '#' if (curr == '#' and 2<=active_n<=3) or (curr == '.' and active_n==3) else '.'
for z in range(1,7):
    d_len = len(cube[0][0]) + 2
    cube = [['.' + s + '.' for s in slice] for slice in cube]
    cube = [['.' * d_len] + slice + ['.' * d_len] for slice in cube]
    box = ['.'*d_len]*d_len
    cube = [box] + cube + [box]
    temp_cube = [[s for s in slice] for slice in cube]
    for s in range(len(cube)):
        for i in range(len(cube[s])):
            acc = ""
            for j in range(len(cube[s][i])):
                acc += update(cube, s, i, j)
            temp_cube[s][i] = acc
    cube = [[s for s in slice] for slice in temp_cube]
print("Part 1: " + str(sum([sum([s.count('#') for s in slice]) for slice in cube])))
if p:
    print()
    for c in hypercube:
        for slice in c:
            for s in slice:
                print(s)
            print()
        print('-' * 50)
    print('~'*50 + '\n' + '~'*50)
for z in range(1,7):
    d_len = len(hypercube[0][0][0])+2
    hypercube = [[['.' + s + '.' for s in slice] for slice in c] for c in hypercube]
    blank_line = '.'*d_len
    hypercube = [[[blank_line] + slice + [blank_line] for slice in c] for c in hypercube]
    blank_sheet = ['.'*d_len]*d_len
    hypercube = [[blank_sheet] + c + [blank_sheet] for c in hypercube]
    blank_cube = [['.'*d_len]*d_len]*(d_len-2)
    hypercube = [blank_cube] + hypercube + [blank_cube]
    temp_hyper = [[[s for s in slice] for slice in c] for c in hypercube]
    for c in range(len(hypercube)):
        for s in range(len(hypercube[c])):
            for i in range(len(hypercube[c][s])):
                acc = ""
                for j in range(len(hypercube[c][s][i])):
                    acc += update2(hypercube, c, s, i, j)
                temp_hyper[c][s][i] = acc
    hypercube = [[[s for s in slice] for slice in c] for c in temp_hyper]
    if p:
        for c in range(len(hypercube)):
            for slice in range(len(hypercube[c])):
                print("z=" + str(slice - len(hypercube[c])//2) +", w=" + str(c - len(hypercube)//2))
                for s in range(len(hypercube[c][slice])):
                    print(hypercube[c][slice][s])
                print()
            print('-' * 50)
        print('~'*50 + '\n' + '~'*50)
print("Part 2: " + str(sum([sum([sum([s.count('#') for s in slice]) for slice in c]) for c in hypercube])))
