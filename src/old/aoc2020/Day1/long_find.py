# Imports
import random, math
# Pick random number for the sum
sumrand = random.randrange(2000, 2000000)
print("\nSum To Find: " + str(sumrand))
# Create list with a random selection of nums up to the sum
nums = []
for x in range(int( 10 ** (math.log(sumrand, 10) - 2) ), int( sumrand - (10 ** (math.log(sumrand, 10) - 2)) )):
    if random.random() > 0.99: nums.append(x)

#nums.sort()
# Run pair matching algo
l = len(nums)
print(str(round(100*l/sumrand, 2)) + "% full set!\n")
end = False
numIter = 0
print("Pair: ")
for i in range(l-1, 0-1, -1):
    num1 = nums[i]
    for j in range(l):
        numIter += 1
        num2 = nums[j]
        if num1 + num2 == sumrand:
            print(str(num2) + ", " + str(num1) + " : " + str(num1 * num2))
            end = True
            break
        elif num1 + num2 > sumrand:
            break
    if end:
        break
print("For " + str(l) + " nums, took " + str(numIter) + " iterations, power of " + str(round(math.log(numIter, l),3)) + "\n")

# Run triple matching algo
end = False
numIter = 0
print("Triple: ")
for i in range(l-1, 0-1, -1):
    num1 = nums[i]
    for j in range(l):
        num2 = nums[j]
        num3 = nums[0]
        for k in range(j):
            numIter += 1
            num3 = nums[k]
            if num1 + num2 + num3 == sumrand:
                print(str(num3) + ", " + str(num2) + ", " + str(num1) + " : " + str(num1 * num2 * num3))
                end = True
                break
        if num1 + num2 + num3 > sumrand or end:
            break
    if end:
        break
print("For " + str(l) + " nums, took " + str(numIter) + " iterations, power of " + str(round(math.log(numIter, l),3)) + "\n")
