import math
file = open("day9.txt")
moves = file.read().split('\n')
file.close()
steps = []
for m in moves:
    dir, count = m.split(' ')
    steps.extend([dir]*int(count))
head, tail, ltail = {0:(0,0)}, {0:(0,0)}, {0:[(0,0)]*9}
t_ = 0
for s in steps:
    hx, hy = head[t_]
    tx, ty = tail[t_]
    lt = ltail[t_]
    t_ += 1
    if s == 'L':
        hx -= 1
    elif s == 'R':
        hx += 1
    elif s == 'U':
        hy += 1
    elif s == 'D':
        hy -= 1
    else:
        print(s)
    dx, dy = hx - tx, hy - ty
    if abs(dx) == 2 or abs(dy) == 2:
        tx += int(math.copysign(1, dx)) if dx != 0 else 0
        ty += int(math.copysign(1, dy)) if dy != 0 else 0
    head[t_] = (hx, hy)
    tail[t_] = (tx, ty)

    comp_x, comp_y = hx, hy
    ltail[t_] = []
    for seg in lt:
        sx, sy = seg
        dx, dy = comp_x - sx, comp_y - sy
        if abs(dx) == 2 or abs(dy) == 2:
            sx += int(math.copysign(1, dx)) if dx != 0 else 0
            sy += int(math.copysign(1, dy)) if dy != 0 else 0
        ltail[t_].append((sx, sy))
        comp_x, comp_y = sx, sy

print(len(set(tail.values())))
print(len(set([v[8] for v in ltail.values()])))