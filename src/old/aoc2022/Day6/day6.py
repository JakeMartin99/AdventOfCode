file = open("day6.txt")
s = file.read()
file.close()
last3, last13 = [], []
ans1, ans2 = -1, -1
for idx,c in enumerate(s):
    if len(last3) < 3:
        last3.append(c)
    elif ans1 == -1 and c not in last3 and len(set(last3)) == 3:
        ans1 = idx + 1
    else:
        last3.append(c)
        last3.pop(0)
    if len(last13) < 13:
        last13.append(c)
    elif ans2 == -1 and c not in last13 and len(set(last13)) == 13:
        ans2 = idx + 1
    else:
        last13.append(c)
        last13.pop(0)
    if (ans1 != -1 and ans2 != -1):
        break
print(ans1, ans2)