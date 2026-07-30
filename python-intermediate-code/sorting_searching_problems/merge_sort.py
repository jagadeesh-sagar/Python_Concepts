'''
Merge sort is type of Divide and conquer method (comparison based sorting)

always O(nlogn)

=> 
'''

def merge(A,lb,mid,ub):

    i=lb
    j=mid+1
    k=lb
    b=[0]*len(A)

    while(i<=mid and j<=ub):
        if A[i]<=A[j]:
            b[k]=A[i]
            i+=1
        else:
            b[k]=A[j]
            j+=1
        k+=1
    
    while(i<=mid):
        b[k]=A[i]
        i+=1
        k+=1

        
    while(j<=ub):
        b[k]=A[j]
        j+=1
        k+=1
    
    for k in range(lb,ub+1):
        A[k]=b[k]

def Mergesort(A,lb,ub):
    

    if lb<ub:
        mid=(lb+ub)//2
        Mergesort(A,lb,mid)
        Mergesort(A,mid+1,ub)
        merge(A,lb,mid,ub)


A = [15, 5, 24, 8, 1, 13, 16, 10, 20]

Mergesort(A, 0, len(A) - 1)

print(A)

