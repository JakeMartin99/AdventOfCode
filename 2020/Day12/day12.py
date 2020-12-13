file = open("day12.txt")
data = [(x[0], int(x[1:])) for x in file.read().split('\n')[:-1]]
ang = 0
pos = [0, 0]
waypt, pos2 = [10, 1], [0, 0]
for (c, num) in data:
    if c == 'N':
        pos[1] += num
        waypt[1] += num
    elif c == 'S':
        pos[1] -= num
        waypt[1] -= num
    elif c == 'E':
        pos[0] += num
        waypt[0] += num
    elif c == 'W':
        pos[0] -= num
        waypt[0] -= num
    elif c == 'L':
        ang += num
        if ang < 0: ang += 360
        if ang >= 360: ang -= 360
        if num == 90: waypt = [-1*waypt[1], waypt[0]]
        elif num == 180: waypt = [-1*waypt[0], -1*waypt[1]]
        elif num == 270: waypt = [waypt[1], -1*waypt[0]]
    elif c == 'R':
        ang -= num
        if ang < 0: ang += 360
        if ang >= 360: ang -= 360
        if num == 90: waypt = [waypt[1], -1 * waypt[0]]
        elif num == 180: waypt = [-1*waypt[0], -1*waypt[1]]
        elif num == 270: waypt = [-1*waypt[1], waypt[0]]
    elif c == 'F':
        if ang == 0: pos[0] += num
        if ang == 180: pos[0] -= num
        if ang == 90: pos[1] += num
        if ang == 270: pos[1] -= num
        pos2 = [pos2[0] + (num*waypt[0]), pos2[1] + (num*waypt[1])]

print("Part 1: " + str((pos, abs(pos[0]) + abs(pos[1]))))
print("Part 2: " + str((pos2, abs(pos2[0]) + abs(pos2[1]))))
file.close()
