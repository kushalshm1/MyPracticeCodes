num = 12345

def digitize(num): #Main Function
    def length(num): #Function to find Length of the digit
        j = 0    
        while(num>0.1):    #Num>0.1 because 1/10 is 0.1 and it won't go further if there is a value less than 0.1
            if num>0.1:
                num = num/10
                j = j+1
            else:
                break
        return j
#     print(length(num))
    limit = length(num)
    arr = []
    i = 0
    #Reversing the digit and the adding the reversed ones to array named as "arr"
    while i<limit: 
      x = num%10
      arr.append(x)
      num = int(num/10)
      i = i+1
    return arr

print(digitize(num))