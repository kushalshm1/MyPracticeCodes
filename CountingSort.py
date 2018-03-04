import random

quantity = 100
upLimitRandom = 10
arr = [0]*quantity
i = 0

#Generating Random Numbers

for x in range(0,(quantity-1)):
    arr[x] = random.randrange(1,upLimitRandom)

# print(arr)

#Sorting Random Numbers

maxValue = max(arr)
countingArr = [0]*maxValue
sortedArr = [0]*quantity

while i<quantity:
    index = arr[i]
    countingArr[index] = countingArr[index]+1 
    i = i+1

print(countingArr)


