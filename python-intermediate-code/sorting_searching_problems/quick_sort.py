'''
https://chatgpt.com/s/t_6a58b4ac1428819197cc514c770629bd

quick sort is type of divide and conquer (comparison based sorting) (avg O(nlogn)) worst O(n2)

here we choose and number and called it as a pivot and follows some rules:
1.if start(lb) element is lower thatn pivot then increment
2.if end (ub) element is higher than pivot then decrement
3.if rule 1 & rule 2 fails that means the number at the both positions causing issue to sorting
so swap them
4. after all both start and end element cross each other we understood that upto that the pivot is element is sorted
so we leave that and take new pivot element by diving the array into 2 from pivot
eventually the array moves to one number .. this partiotns continue unitl the last one elment in array

https://chatgpt.com/s/t_6a59b7b425e4819186deb67648cd973f  => partition part


'''


def partition(A,lb,ub):
    pivot=A[lb]
    start=lb
    end=ub

    while(start<end):

        while (start<=ub and A[start]<=pivot):
            start+=1
        
        while(A[end]>pivot):
            end-=1
        
        if start<end:
            A[start],A[end]=A[end],A[start]

    A[lb],A[end]=A[end],A[lb]

    return end

def quickSort(A,lb,ub):
    
    if lb<ub:
        loc=partition(A,lb,ub)
        quickSort(A,lb,loc-1)
        quickSort(A,loc+1,ub)


A = [7, 6, 10, 5, 9, 2, 1, 15, 7]

quickSort(A, 0, len(A) - 1)

print(A)