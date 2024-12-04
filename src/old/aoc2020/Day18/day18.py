file = open("day18.txt")
data = file.read().replace(' ', '').split('\n')[:-1]
file.close()
def solve(prob: str)->int:
    if '(' in prob:
        right_i = prob.find(')')
        left_i = right_i - prob[right_i::-1].find('(')
        return solve(prob[:left_i] + str(solve(prob[left_i+1:right_i])) + prob[right_i+1:])
    else:
        op_loc = min(prob.find("+"), prob.find("*"))
        if op_loc < 0: op_loc = max(prob.find("+"), prob.find("*"))
        if op_loc < 0:
            return int(prob)
        left = int(prob[0:op_loc])
        op = prob[op_loc]
        next_loc = min(prob[op_loc+1:].find("+"), prob[op_loc+1:].find("*"))
        if next_loc < 0: next_loc = max(prob[op_loc+1:].find("+"), prob[op_loc+1:].find("*"))
        if next_loc < 0: next_loc = len(prob) - op_loc - 1
        right = int(prob[op_loc+1:op_loc+1+next_loc])
        num = left+right if op == '+' else left*right
        return solve(str(num) + prob[op_loc+1+next_loc:])
def solve2(prob: str)->int:
    if '(' in prob:
        right_i = prob.find(')')
        left_i = right_i - prob[right_i::-1].find('(')
        return solve2(prob[:left_i] + str(solve2(prob[left_i+1:right_i])) + prob[right_i+1:])
    elif '+' in prob:
        op_loc = prob.find('+')
        next_loc = min(prob[op_loc+1:].find("+"), prob[op_loc+1:].find("*"))
        if next_loc < 0: next_loc = max(prob[op_loc+1:].find("+"), prob[op_loc+1:].find("*"))
        if next_loc < 0: next_loc = len(prob) - op_loc - 1
        right = int(prob[op_loc+1:op_loc+1+next_loc])
        prev_loc = op_loc-1 - min(prob[op_loc-1::-1].find('+'), prob[op_loc-1::-1].find('*'))
        if prev_loc >= op_loc: prev_loc = op_loc-1 - max(prob[op_loc-1::-1].find('+'), prob[op_loc-1::-1].find('*'))
        if prev_loc >= op_loc: prev_loc = -1
        left = int(prob[prev_loc+1:op_loc])
        return solve2(prob[0:prev_loc+1] + str(left + right) + prob[op_loc+next_loc+1:])
    else:
        op_loc = min(prob.find("+"), prob.find("*"))
        if op_loc < 0: op_loc = max(prob.find("+"), prob.find("*"))
        if op_loc < 0:
            return int(prob)
        left = int(prob[0:op_loc])
        op = prob[op_loc]
        next_loc = min(prob[op_loc+1:].find("+"), prob[op_loc+1:].find("*"))
        if next_loc < 0: next_loc = max(prob[op_loc+1:].find("+"), prob[op_loc+1:].find("*"))
        if next_loc < 0: next_loc = len(prob) - op_loc - 1
        right = int(prob[op_loc+1:op_loc+1+next_loc])
        num = left+right if op == '+' else left*right
        return solve2(str(num) + prob[op_loc+1+next_loc:])
ans1 = [solve(prob.replace(' ', '')) for prob in data]
print("Part 1: " + str(sum(ans1)))
ans2 = [solve2(prob.replace(' ', '')) for prob in data]
print("Part 2: " + str(sum(ans2)))
