import random

def dice():
    while True:
        number = random.randrange(1,6)
        print(number)
        answer = str(input("Do you want to re roll(Y/N:\n"))
        if answer == "Y":
            break
        else:
            continue


dice()