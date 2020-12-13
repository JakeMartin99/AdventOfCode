file = open("day11.txt")
def equals(l1: list, l2: list) -> bool:
    for i in range(len(l1)):
        for j in range(len(l1[i])):
            if l1[i][j] != l2[i][j]:
                return False
    return True
seats = [[c for c in line] for line in file.read().split('\n')[:-1]]
seats2 = [[seat for seat in row] for row in seats]
seatstore = [[None for seat in row] for row in seats]
seatstore2 = [[None for seat in row] for row in seats2]
while not equals(seats, seatstore):
    seatstore = [[seat for seat in row] for row in seats]
    for i in range(len(seats)):
        for j in range(len(seats[0])):
            if seatstore[i][j] != '.':
                adj_occp = 0
                if 0<=i-1<len(seats) and 0<=j-1<len(seats[0]) and seatstore[i-1][j-1] == '#': adj_occp += 1
                if 0<=i-1<len(seats) and seatstore[i-1][j] == '#': adj_occp += 1
                if 0<=i-1<len(seats) and 0<=j+1<len(seats[0]) and seatstore[i-1][j+1] == '#': adj_occp += 1
                if 0<=j-1<len(seats[0]) and seatstore[i][j-1] == '#': adj_occp += 1
                if 0<=j+1<len(seats[0]) and seatstore[i][j+1] == '#': adj_occp += 1
                if 0<=i+1<len(seats) and 0<=j-1<len(seats[0]) and seatstore[i+1][j-1] == '#': adj_occp += 1
                if 0<=i+1<len(seats) and seatstore[i+1][j] == '#': adj_occp += 1
                if 0<=i+1<len(seats) and 0<=j+1<len(seats[0]) and seatstore[i+1][j+1] == '#': adj_occp += 1
                if seatstore[i][j] == 'L' and adj_occp == 0: seats[i][j] = '#'
                if seatstore[i][j] == '#' and adj_occp >= 4: seats[i][j] = 'L'
print("Part 1: " + str(sum([row.count('#') for row in seats])))

p=False
def exp_check(h, k, i, j, arr):
    if p: print('  => exp_check' + str((j, i, k, h)))
    if arr[i+h][j+k] == '.':
        if p:print('\t', end='')
        return exp_check(h, k, i+h, j+k, arr) if 0<=i+h+h<len(seats2) and 0<=j+k+k<len(seats2[0]) else 0
    if p:print('\t' + '~> ' + str(arr[i+h][j+k]) + ", " + str((j+k, i+h)))
    if arr[i+h][j+k] == '#': return 1
    return 0
while not equals(seats2, seatstore2):
    seatstore2 = [[seat for seat in row] for row in seats2]
    if p:print(20*'~')
    if p:
        for seat in seats2:
            [print(c, end='') for c in seat]
            print()
    for i in range(len(seats2)):
        for j in range(len(seats2[0])):
            if seatstore2[i][j] != '.':
                adj_occp2 = 0
                if p:print('\n\n' + str((j, i)) + ':')
                if i>0 and j>0: adj_occp2 += exp_check(-1, -1, i, j, seatstore2)
                if i>0: adj_occp2 += exp_check(-1, 0, i, j, seatstore2)
                if i>0 and j<len(seats2[0])-1: adj_occp2 += exp_check(-1, 1, i, j, seatstore2)
                if j>0: adj_occp2 += exp_check(0, -1, i, j, seatstore2)
                if j<len(seats2[0])-1: adj_occp2 += exp_check(0, 1, i, j, seatstore2)
                if i<len(seats2)-1 and j>0: adj_occp2 += exp_check(1, -1, i, j, seatstore2)
                if i<len(seats2)-1: adj_occp2 += exp_check(1, 0, i, j, seatstore2)
                if i<len(seats2)-1 and j<len(seats2[0])-1: adj_occp2 += exp_check(1, 1, i, j, seatstore2)
                if seatstore2[i][j] == 'L' and adj_occp2 == 0: seats2[i][j] = '#'
                if seatstore2[i][j] == '#' and adj_occp2 >= 5: seats2[i][j] = 'L'
                if p:print("adj: " + str(adj_occp2))
print("Part 2: " + str(sum([row.count('#') for row in seats2])))
file.close()
