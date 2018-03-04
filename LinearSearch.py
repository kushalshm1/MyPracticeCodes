import string
import random


# n = 20
# arr = [0]*n
# search = 20

# for x in range(1,100):
#     arr.append(x)

# #Searching

# for y in range(1,100):
#     if(arr[y] == search):
#         print(y)
#         break

#Monk Problem HackerEarth.com 
arr = list(string.ascii_lowercase)
arrCaps = list(string.ascii_uppercase)
random.shuffle(arr)

# for x in range(a,z):
#     arr.append(x)


# print(arr)
# print(arrCaps)

# Now Searching for Vowels
for i in range(0,26):
    if arr[i] == "a" or arr[i] == "e" or arr[i] == "i" or arr[i] == "o" or arr[i] == "u":
        print(arr[i],'Index: ',i)
    # else:
    #     print("None")



