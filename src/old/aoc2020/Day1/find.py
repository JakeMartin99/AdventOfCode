def pair(nums):
    numIter = 0
    l = len(nums)
    print("Pair: ")
    for i in range(l-1, 0-1, -1):
        num1 = nums[i]
        for j in range(l):
            numIter += 1
            num2 = nums[j]
            if num1 + num2 == 2020:
                print(str(num2) + ", " + str(num1) + " : " + str(num1 * num2))
                print("For " + str(l) + " nums, took " + str(numIter) + " iterations\n")
                return
            elif num1 + num2 > 2020:
                break

def triple(nums):
    numIter = 0
    l = len(nums)
    print("Triple: ")
    for i in range(l-1, 0-1, -1):
        num1 = nums[i]
        for j in range(l):
            num2 = nums[j]
            num3 = nums[0]
            for k in range(j):
                numIter += 1
                num3 = nums[k]
                if num1 + num2 + num3 == 2020:
                    print(str(num3) + ", " + str(num2) + ", " + str(num1) + " : " + str(num1 * num2 * num3))
                    print("For " + str(l) + " nums, took " + str(numIter) + " iterations")
                    return
            if num1 + num2 + num3 > 2020:
                break

file = open("day1.txt")
nums = [int(x) for x in file.read().split("\n") if x != '']
nums.sort()
file.close()
pair(nums)
triple(nums)
