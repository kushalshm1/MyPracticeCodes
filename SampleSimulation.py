import random
import numpy as np
import matplotlib.pyplot as plt

possible = 6
dice = 2
size = possible*dice
mean = []
frequency = []

i = 0
while(i<size):
    d1    = random.randint(1,6)
    d2    = random.randint(1,6)
    avg   = (d1+d2)/2
    mean.append(avg)
    # index = ((mean[i]*2)-1)
    # frequency.append(index)
    i = i+1

# print(frequency)

mean.sort()
print(mean)
i = 0
j = 0

# plt.bar(frequency,mean)
# plt.show()
print(freq)