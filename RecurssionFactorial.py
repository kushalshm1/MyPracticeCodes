
# import math

# def fact(k):
#     if k==1 or k==0:
#         return 1
#     else:
#         return (k*fact(k-1))
#     print(k)        


# fact(5)



def factorial(n):
    if (n <= 1):
        return 1
    else:
        return(n*factorial(n-1))
n = 924
print(factorial(n))

