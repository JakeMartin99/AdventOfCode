file = open("day15.txt")
nums = [int(x) for x in file.read().replace('\n', '').split(',')]
file.close()
map, last_key, was_new = {}, None, True
for turn in range(len(nums)):
    map[nums[turn]] = (turn, -1)
for turn in range(len(nums),30000000):
    if was_new:
        if not 0 in map:
            map[0] = (turn, -1)
            was_new = True
        else:
            map[0] = (turn, map[0][0])
            was_new = False
        last_key = 0
    else:
        n = map[last_key][0] - map[last_key][1]
        if not n in map:
            map[n] = (turn, -1)
            was_new = True
        else:
            map[n] = (turn, map[n][0])
            was_new = False
        last_key = n
    if turn == 2020-1:
        print("Part 1: " + str(last_key))
    elif turn == 30000000-1:
        print("Part 2: " + str(last_key))
