'''
Binary search implementation
2,3,4,6,8,9,11,14,17,23,43,54,65,77

time complexity : O(log n) ,O(1) space
# For n=1,000,000 elements → at most 20 steps

'''

def binary_search(list1:list[int],n:int):
    low=0
    high=len(list1)-1

    while(low<=high):
        mid=(low+high)//2

        if list1[mid]==n:
            return mid
        if list1[mid]<n:
            low=mid+1
        else:
            high=mid-1
    return -1

print(binary_search(list1=[2,3,4,6,8,9,11,14,17,23,43,54,65,77],n=23))
        