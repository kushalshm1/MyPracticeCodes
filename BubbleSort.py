import random
arr = [0]*10

for x in range(0,10):
    arr[x] = random.randrange(1,50)
temp = 0
print(arr)
len = len(arr)
i = 0
j = 1

for x in range(len):    
    for y in range(len-i-1)
        if arr[i] < arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i = i+2
            j=j+2
        

        

print(arr)