import regex as reg
file = open("day19.txt")
data = file.read().split('\n\n')
file.close()
rules = data[0].split('\n')
msgs = data[1].split('\n')[:-1]
rulemap = {int(rule.split(': ')[0]) : rule.split(': ')[1] for rule in rules}
def propogate(rule)->str:
    nums = rulemap[rule].split(' ')
    s = ""
    for n in nums:
        n2 = n if n[-1] != '+' else n[:-1]
        try:
            N = int(n2)
            s += propogate(N)
        except:
            s += n2
        if n[-1] == '+': s += '+?'
    if '|' in nums: s = '(' + s + ')'
    return s.replace('"', '')
zerorule = "^(" + propogate(0) + ")$"
#"42 | 42 8", "42 31 | 42 11 31"
rulemap[8], rulemap[11] = "42+", "42 (?1)* 31"
zero2 = "^(" + propogate(0) + ")$"
print("\n1: " + zerorule)
print("\n2: " + zero2)
print("\nPart 1: " + str(sum([1 if reg.search(zerorule, m) else 0 for m in msgs])))
print("Part 2: " + str(sum([1 if reg.search(zero2, m) else 0 for m in msgs])))
