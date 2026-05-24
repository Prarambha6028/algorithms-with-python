import numpy as np
n=3
m=6
p=[0,1,2,4]#profit
w=[0,2,3,3]#weight
array = np.zeros((n + 1, m + 1), dtype=int)
def knapsack(arr,p,w1,n,m):
    for i in range(1,n+1):
        for w in range(1,m+1):
            if w1[i]>w:
                arr[i][w]=arr[i-1][w]
            else:
                arr[i][w]=max(arr[i-1][w],p[i]+arr[i-1][w-w1[i]])
    return arr

a=knapsack(array,p,w,n,m)
print(a)
