import numpy as np


#1.
def Vandermonde(arr,N):
    m=np.array([i**j for i in arr for j in range(N,0,-1)]).reshape(arr.size,N)
    print(m)
x=np.array([1,2,3,4,5])
Vandermonde(x,4)






#2.
def average(arr,w):
    l=[]
    for i in range(0,arr.size-w+1):
        s=0
        for j in range(i,i+w):
            s=s+arr[j]
        avg=s/w
        l.append(avg)
    y=np.array(l)
    print(y)
x=np.array([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150])
average(x,3)
            


