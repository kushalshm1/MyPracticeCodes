def positive_sum(arr):
    
    def sum(arr):
        add = 0
        i = 0
        while(i<len(arr)):
            add = add+arr[i]
            i = i+1
    add = 0
    if(len(arr)==0):
        return  0
    elif(sum(arr)==0):
        return 0
    else:
        i = 0
        while(i<len(arr)):
            if(arr[i]<0):
                del arr[i]
            i = i+1
        
        #Getting sum of array
        i = 0
        while(i<len(arr)): 
            add = add+arr[i]
            i = i+1
        print(arr)
        print(add)
        return add
    