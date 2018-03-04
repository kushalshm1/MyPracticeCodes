# i = 0
def series_sum(n):
    i = 0
    add = 0
    while(i<n):
        add = add + 1/n
        n = n+3
        i = i+1
    return add