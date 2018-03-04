import random



for n in range(1,1000):
    number = random.randrange(0, 10000)
    if number % 2 == 0:
        print(number,"Even")
    else:
        print(number,"Odd")

