magicNumber = 17

# Ok this program finds a magic number
print(5+4)

#Break here
print("Kushal"+"Sharma")
print("Kushal",17)
for n in range(101):
    if n is magicNumber:
        print(n,"is the magic number")
        break
    else:
        print(n)


#Continue here

numbersTaken = [2,9,13,12,17]

print("Here are the numbers that are still available")

for n in range(1,30):
    if n in numbersTaken:
        continue
        print(n)
    else:
        print(n)