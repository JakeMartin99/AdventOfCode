from sympy.ntheory.modular import solve_congruence
file = open("day13.txt")
s_time = int(file.readline())
buses = file.readline().replace('\n','')
file.close()
buses1 = [int(x) for x in buses.replace('x,','').split(',') if x]
waits = [bus-(s_time % bus) for bus in buses1]
res1 = (min(waits), buses1[waits.index(min(waits))])
print( "Part 1: " + str( (res1, res1[0]*res1[1]) ) )
buses2 = buses.split(',')
offs = []
for i in range(len(buses2)):
    if buses2[i] != 'x': offs.append(i)
res2 = solve_congruence(*zip(offs, buses1))
print("Part 2: " + str((res2, res2[1]-res2[0])))
