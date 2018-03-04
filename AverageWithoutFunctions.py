def find_average(arr):
    length = len(arr)
    add = 0
   
    for i in range(0,length):
        add = add + arr[i]
    if(length>0):
        avg = add/length
    else:
        avg = 0
    return avg