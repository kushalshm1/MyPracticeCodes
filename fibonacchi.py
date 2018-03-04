arr = []
y = 0
for x in range(0,1000):
    arr.append(x)
arrOne = [0]*1000
i=0
for x in range(0,999):
    arrOne[i] = arr[i]+arr[i+1]
    i=i+1
print(arr)

i = 0
j = 0
k = 1
y = []
x = []
z = 0

for n in range(0,10):
    y.append(n)

for a in range(0,9):
    z = y[j] + y[k]
    z = z + y[i]
    x.append(z)
    i = i+1
    j = j+1
    k = k+1

print(x)

