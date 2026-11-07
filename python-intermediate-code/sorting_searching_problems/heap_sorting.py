'''
Heap sort (using Heapify method)(bottom -up approch)   O(n log n)

https://chatgpt.com/s/t_6a58b257d6d4819184776755ff11ec05

the logic is simple we build the heap tree in such a way that parent has higher values then its children 
and then we remove that parent and keep another element there (second highest) 
=> the reason to use n//2 is to avoid leaf node as they are not parents and we can't do heapfy

=>the logic is for every parent (node) and its child we heapify then at last we remove root node (here moving back of list) 
and get next max and remove and continue

=>in this logic of delete we dont actually delete anything we just move that highest element to the last of arr
here we use heapfiy to find the max elements and move them back (2 code)

=> we move root node to the back of arr 

////////////////////////////////////////////////////////

Phase 1 — build the heap (parent/child heapify, bottom-up)

for i in range(n//2, -1, -1):
    maxHeapify(A, n, i)

Every non-leaf node gets checked against its children and swapped down if it violates max-order, 
working from the lowest parents up to the root. End result: A[0] is guaranteed the maximum of the whole array.

Phase 2 — repeatedly remove the root, shrink, re-heapify

for i in range(n, 0, -1):
    A[0], A[i] = A[i], A[0]
    maxHeapify(A, i - 1, 0)

'''

def maxHeapify(A:list[int],n:int,i:int):
    largest=i
    left=2*i+1
    right=2*i+2

    if (left<n and A[largest]<A[left]):
        largest=left

    if (right<n and A[largest]<A[right]):
        largest=right

    if largest!=i:
        A[largest],A[i]=A[i],A[largest]
        maxHeapify(A,n,largest)


def heapSort(A: list[int]):
    n = len(A)

    for i in range(n//2,-1,-1):
        maxHeapify(A,n,i)

    # for i in range(n-1, 0, -1):  # 2 code
    #     A[0], A[i] = A[i], A[0]
    #     maxHeapify(A, i - 1, 0)


A=[4, 10, 3, 5, 1]
heapSort(A)
print(A)
