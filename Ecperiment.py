import numpy as np 
import matplotlib.pyplot as plt
import math
# import random
p = 0.7
q = 1-p
N = 10
i = 0
j = 0
size = 10000
arrValue = [0]*size 
arrProb  = [0]*size

def binomial(k):
    one    = math.factorial(N)
    two    = math.factorial(N-k)*math.factorial(k)
    three  = math.pow(p,k)*math.pow(q,(N-k))
    return (one*(two**(-1)))*three

# print(binomial(1))
# j = 0
# add = 0
while(i<size):
    add = 0
    probGen = np.random.rand()
    j = 0
    while(add<=probGen):
        add = add + binomial(j)
        j = j +1
        # arrValue[i] = arrValue[i]+1
    arrValue[i] = j
    arrProb[i] = binomial(j)  
    i = i+1

# arrValue = arrValue.sort()
# arrProb = arrProb.sort()
# print(binomial(10))
print((arrValue))
print(arrProb)

# print(len(arrProb))
# print(len(arrValue))
# print(arrProb)

plt.bar(arrValue,arrProb)
plt.show()
