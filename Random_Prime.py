import random

for n in range(1,1000):
    number = random.randrange(1,10000)
    for n in range(1,number):
        if number%n == 0:
            print(number,"Non Prime")
            break
        else:
            print(number,"Prime")
            break