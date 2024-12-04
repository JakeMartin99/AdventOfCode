file = open("day1.txt")
nums = [sum([int(s) for s in g.split("\n") if len(s)>0]) for g in file.read().split("\n\n") if len(g)>0]
print(max(nums))
file.close()
print(sum(sorted(nums, reverse=True)[0:3]))