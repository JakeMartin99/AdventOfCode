def solve(s, low_c, up_c, l_bound, u_bound) -> int:
    # print("s: " + s + ", low: " + str(l_bound) + ", upper: " + str(u_bound))
    if len(s) == 1:
        if s[0] == low_c:
            #print("ANS: " + str(l_bound))
            return l_bound
        else:
            #print("ANS: " + str(l_bound))
            return u_bound
    elif s[0] == low_c:
        return solve(s[1:], low_c, up_c, l_bound, (u_bound + l_bound)//2)
    elif s[0] == up_c:
        return solve(s[1:], low_c, up_c, (u_bound + l_bound)//2 + 1, u_bound)
def toId(seat) -> int:
    row_s = seat[0:7]
    col_s = seat[7:]
    #print("~"*20)
    #print(seat + ": " + row_s + ", " + col_s)
    return 8*solve(row_s, 'F', 'B', 0, 127) + solve(col_s, 'L', 'R', 0, 7)

file = open("day5.txt")
seats = file.read().split('\n')
file.close()
ids = [toId(seat) for seat in seats]
print("Part 1: " + str(max(ids)))
#Test line: [print(toId(x)) for x in ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]]
ids.sort()
my_id = ids[0]
for id in ids[1:]:
    my_id += 1
    if my_id < id:
        break
print("Part 2: " + str(my_id))
