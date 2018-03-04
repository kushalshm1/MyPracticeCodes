number = int(input("Enter number to be checked:\n"))

if(number>1):
    for i in range(2,number):
        if(number%i==0):
            print("Your Number is not a prime Number")
            break
        else:
            print("It is a prime number")
            break
else:
    print("Please enter number greater than 1")