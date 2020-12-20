file = open("day19.txt")
data = file.read().split('\n\n')
file.close()
rules = data[0].split('\n')
msgs = data[1].split('\n')[:-1]
rulemap = {int(rule.split(':')[0]) : rule.split(':')[1] for rule in rules}
for key in rulemap:
    l1 = [[int(i) if i.isdigit() else i[1] for i in e.split(' ') if i] for e in rulemap[key].split('|')]
    rulemap[key] = l1
def propogate(rule):
    #return [[propogate(val) if type(val)==int else val for val in set] for set in rulemap[rule]]
    if len(rulemap[rule]) == 1:
        if len(rulemap[rule][0]) == 1:
        return "(" + propogate(rulemap[rule][0][0]) + " and " + propogate(rulemap[rule][0]) + ")"
    elif len(rulemap[rule]) == 2:
        return propogate(rulemap[rule][0]) + " or " + propogate(rulemap[rule][1])
[print(rule, ':', rulemap[rule]) for rule in rulemap]
zerorule = propogate(0)
print(zerorule)
