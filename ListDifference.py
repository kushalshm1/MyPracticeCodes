

a = [0,2,2,3,4,5,5,4,5,7,5,6]
b = [0,1,2,5,7]
i = 0
j = 0
indexes = []
# print(len(a))
# print(len(b))

while j<len(b):
    i = 0
    while i<len(a):
        if a[i]*b[j] ==  a[i]**a[i]:  
            # del a[i]
            indexes.append(i)
        i = i+1
    j = j+1
i = 0
indexes.sort()

print(indexes)
# while i<(length-1):
#     index = indexes[i]
#     del a[index]
#     i = i+1
i = 0
add = sum(a)

while i<len(indexes):
    index = indexes[i]
    a[index] = add
    i = i+1
print(a)
i = 0
while i<len(a):
    if a[i]/add == 1 or a[i]/add == 0:
        del a[i]
    else:
        i = i+1
    # i = i+1


print(a)
# print(indexes)

#This above try failed because it only works when values are not repeating 


