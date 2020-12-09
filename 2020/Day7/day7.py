def rem_num(l):
    newl = []
    for item in l:
        if item != "noother":
            newl.append((int(item[0]), item[1:]))
    return newl
def paths(graph, goal):
    matches = [key for key in graph if goal in graph[key][1]]
    [[matches.append(p) for p in paths(graph, m)] for m in matches]
    return matches
def sub_bags(graph, start) -> int:
    subs = graph[start]
    return 1 + sum([(num * sub_bags(graph, name)) for num, name in subs])

file = open("day7.txt")
lines = file.read().replace(" ", "").replace(".", "").split('\n')
file.close()
rules = {line[0:line.find("bags")]:rem_num(line[line.find("contain")+7:].replace("bags", "").replace("bag", "").split(',')) for line in lines}
rules1 = {key:([num for num, name in rules[key]],[name for num, name in rules[key]]) for key in rules}
print("Part 1: " + str(len(set(paths(rules1, "shinygold")))))
print("Part 2: " + str(sub_bags(rules, "shinygold")-1))
