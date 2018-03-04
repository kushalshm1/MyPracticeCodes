# # import math

# # # n = 500
# # # def sum(n):
# # #     #Summing all the digits of n
# # #     last = n%10
# # #     n = n/10
# # #     sum = last+sum

# # sum = 0
# # i = 0
# # n = 9043834058437589437534324342
# # arr = []
# # sub = 0
# # while(n>0.1):    
# #     x = n%10
# #     arr.append(x)
# #     n = int(n/10)
# # arr.reverse()
# # i = 0
# # add = 0
# # while(i<len(arr)):
# #     add = add + arr[i]
# #     i = i+1

# # while(add<100 and add>1):
# #     sub = ]

# # n = sub
# # print(n)

# # # print(add)
# # # print(arr)


# # return():
# # return 5

# # time = 4
# # water(time):
# #     x = int(time*0.5)
# #     return x


# # def even_or_odd(number):
# #     if(number%2==0):
# #         return "Even"
# #     else:
# #         return "Odd"

# # list = [1,2,3]
# # def describeList(list):
# #     if(len(list)==0):
# #         return "Empty"
# #     elif(len(list)>1):
# #         return "More"
# # arr = [1,2,3]
# # def min(arr):
# #     arr.sort()
# #     return arr[0]

# # def max(arr):
# #     arr.sort()
# #     return arr[len(arr)]

# # def make_negative( number ):
# #     if(number<0):
# #         return number*(-1)
# #     elif(number==0):
# #         return 0
# #     else:
# #         return number


# #_________________________________________________________________________________________________

# #Creating Dictionary

# # list1 = [1, 2, 3, 4, 5]
# # list2 = [123, 234, 456]
# # d = {'a': [], 'b': []}
# # d['a'].append(list1)
# # d['a'].append(list2)
# # print(d)
# # d = {'a':[],'b':[]}

# # a = 097
# # z = 122













# #------------------------------------------------------------------------------------------------
# #Dumbphone Keypad Smulation
# import string
# # alphabetDict = {}
# alphabets = []
# alphabets = list(string.ascii_lowercase)
# values = [0]*len(alphabets)
# alphabets.append(" ")
# print(alphabets)
# i = 2
# j = 22
# k = 222
# l = 7777
# iIndex = 0
# jIndex = 1
# kIndex = 2
# count = 0
# m = 0
# n = 0
# while(count<6):
#     values[iIndex] = i
#     values[jIndex] = j 
#     values[kIndex] = k

#     iIndex = iIndex + 3
#     jIndex = jIndex + 3
#     kIndex = kIndex + 3

#     i = i+1
#     j = j+11
#     k = k+111
#     count = count+1
# values[18] = 7777
# values[19] = 8
# values[20] = 88
# values[21] = 888
# values[22] = 9
# values[23] = 99
# values[24] = 999
# values[25] = 9999
# # print(values)
# values.append(0)
# print(values)
# text = "abcdef"

# textToList = []
# textToList = list(text)
# finalValue = []
# asciiValuesArray = []
# print(textToList)

# # i = 0
# # j = 0
# # while(i<len(alphabets)):
# #     j = 0
# #     if(alphabets[i]==textToList[j]):
# #         finalValue.append(values[i])
# #         j = j+1
# #         # else:

# #     i = i+1
# i = 0
# j = 0
# while(i<len(textToList)):
#     if(textToList[i]==alphabets[j]):
#         finalValue.append(values[j])
#         j = 0
#         i = i+1
#     else:
#         j = j+1
# i = 97
# j = 0
# while(j<=25):
#     asciiValuesArray.append(i)
#     i = i+1
#     j = j+1

# # print(asciiValuesArray)
# # print(len(asciiValuesArray))
# # while(i<len(textToList)):
# #     if(textToList[i]==alphabets[j]):
# #         finalValue.append(values[j])
# #         i = i+1
# #     else:
# #         j = j+1
# # finalValue.insert(5, "Kushal")

# # x = finalValue[i]
# # z = finalValue[i-1]
# # y = x/z
# # z = int(x/y)
# # print(z)
# # tempZ = list(str(z))
# # print(tempZ)
# i = 0
# x = 0
# y = 0
# z = 0
# tempZ = []
# # counter = 1
# while(i<len(finalValue)):
#     x = finalValue[i]
#     z = finalValue[i-1]
#     y = x/z
#     z = int(x/y)
#     tempZ = list((z))
#     if(len(tempZ)==1):
#         # while(counter<=9):
#         if(z==):
#             finalValue.insert(i,'p')
#             break
#             # counter = counter + 1
#     if(len(tempZ)==2):
#         if(z%11==0):
#             finalValue.insert(i,'p')
#     if(len(tempZ)==3):
#         if(z%111==0):
#             finalValue.insert(i,'p')
#     if(len(tempZ)==4):
#         if(z%1111==0):
#             finalValue.insert(i,'p')
#     i = i+1

# print(finalValue)
# #--------------------------------------------------------------------------------------------------:
# import numpy as np 


# #Kata: Mean vs Median ||CodeWars||
# def mean_vs_median(numbers):
#     if(len(numbers)%2!=0):
#         median = np.median(numbers)
#         mean = np.mean(numbers)
#         if(median>mean):
#             return 'median'
#         elif(mean>median):
#             return 'mean'
#         else:
#             return 'same'

#Kata: Decimal to Binary logical conversion ||CodeWars||
# n = 123

# def single_digit(n):
#     test = list(str(n))
#     remArray = []
#     divInt = 1
#     if(len(test)>1):
#         while(divInt>0):
#             divInt = n
#             divInt = int(n/2)
#             rem = n%2
#             remArray.append(rem)
#             n = int(n/2)
#             add = sum(remArray)
#         listAdd = list(str(add))
#         while(len(listAdd)==1):
#             divInt = add
#             divInt = int(add/2)
#             rem = add%2
#             remArray.append(rem)
#             add = int(add/2)
#             listAdd = list(str(add))
#         return sum(remArray)
#     else:
#         return n


import string  
def single_digit(n):
    test = list(str(n))
    remArray = []
    listAdd = []
    add = 10
    listAdd = [0]*10
    if(len(test)>1):
        if(len(listAdd)>1):
            while(add>0):
                add = n
                add = int(n/2)
                rem = n%2
                remArray.append(rem)
                n = int(n/2)
                add = sum(remArray)
                listAdd = list(str(add))
        else:
            return add 
    else:
        return n


print(single_digit(13434))