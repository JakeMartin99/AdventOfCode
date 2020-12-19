file = open("day16.txt")
data = [x.split('\n') for x in file.read().split('\n\n')]
file.close()
rules = [x.split(': ')[1].split(' or ') for x in data[0]]
rulenames = [x.split(': ')[0] for x in data[0]]
rules = [[tuple([int(y) for y in x[0].split('-')]), tuple([int(y) for y in x[1].split('-')])] for x in rules]
def rulesfail(num: int) -> bool:
    ret = True
    for i in range(len(rules)):
        r1, r2 = rules[i][0], rules[i][1]
        if r1[0] <= num <= r1[1] or r2[0] <= num <= r2[1]:
            ret = False
    return ret
myticket = [int(x) for x in data[1][1].split(',')]
tickets = [[int(y) for y in x.split(',')] for x in data[2][1:-1]]
sum = 0
tickets2 = [myticket]
for ticket in tickets:
    rem__ticket = False
    for val in ticket:
        if rulesfail(val):
            sum += val
            rem__ticket = True
    if not rem__ticket: tickets2.append(ticket)
print("Part 1: " + str(sum))
fieldvals = [[t[i] for t in tickets2] for i in range(len(tickets2[0]))]
def rulescheck(num: int, rule: int) -> bool:
    r1, r2 = rule[0], rule[1]
    return (r1[0] <= num <= r1[1] or r2[0] <= num <= r2[1])
map = {}
for r in range(len(rules)):
    map[rulenames[r]] = []
    for f in range(len(fieldvals)):
        if all([rulescheck(val, rules[r]) for val in fieldvals[f]]):
            map[rulenames[r]].append(f)
while any([len(map[key])>1 for key in map]):
    end = True
    for key in map:
        if len(map[key])==1:
            for key2 in map:
                if key2 != key and map[key][0] in map[key2]:
                    map[key2].remove(map[key][0])
                    end = False
    if end: break
for key in map: map[key] = map[key][0]
mult = 1
for key in map:
    if key.split(' ')[0] == "departure":
        mult *= myticket[map[key]]
print("Part 2: " + str(mult))
