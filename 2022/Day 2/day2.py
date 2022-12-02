def score(theirs, mine):
    mine = ord(mine) - ord('X')
    theirs = ord(theirs) - ord('A')
    if mine == theirs:
        return 3 + (mine+1)
    elif mine == (theirs+1)%3:
        return 6 + (mine+1)
    else:
        return 0 + (mine+1)

def mine2(theirs, need):
    mine = 0
    theirs = ord(theirs) - ord('A')
    if need == 'X':
        mine = (theirs-1)%3
    elif need == 'Y':
        mine = theirs
    elif need == 'Z':
        mine = (theirs+1)%3
    return chr(mine + ord('X'))

file = open("day2.txt")
sum1,sum2 = 0,0
for pair in file.read().split("\n"):
    if len(pair) > 0:
        sum1 += score(pair[0], pair[2])
        sum2 += score(pair[0], mine2(pair[0],pair[2]))
print(sum1, sum2)
file.close()