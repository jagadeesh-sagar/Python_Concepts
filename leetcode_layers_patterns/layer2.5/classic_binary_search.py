'''

'''

def binary_search(nums:int,target:int):
    low=0
    n=len(nums)
    high=n-1

    if target>nums[-1]:
        return n

    while(low<=high):
        mid=(low+high)//2

        if nums[mid]==target:
            return mid 
        if nums[mid]>target:
            high=mid-1
        else:
            low=mid+1

    return low

# print(binary_search(nums=[2,3,4,6,8,9,11,14,17,23,43,54,65,77],target=23))


'''

1. If the element DOES NOT exist

Both `bisect_left` and `bisect_right` behave **exactly the same way**:
Within the range: They return the proper insertion index to keep the list sorted.
Larger than all elements: They both return the exact **length of the array** (`len(arr)`).
Smaller than all elements: They both return `0`.

2. If the element DOES exist (The Duplicate Rule)**

This is the only time their logic splits. 
`bisect_right` cares about moving past duplicates, while `bisect_left` stops at the very first one.

`bisect_left`: Returns the index of the **first** occurrence of that number.
`bisect_right`: Returns the index **after the last** occurrence of that number.

Example

If you have `arr = [10, 20, 20, 20, 30]`:

* `bisect_left(arr, 20)` → Returns **`1`** (points to the *first* 20).
* `bisect_right(arr, 20)` → Returns **`4`** (points to the 30, right *after* the last 20).


'''
from bisect import bisect_left,bisect_right

num=[2,3,4,6,8,9,11,14,17,23,43,54,65,77]

# print(bisect_right(num,11)-bisect_left(num,6))  # to find the range of elements
# print(bisect_right(num,10),bisect_left(num,10))


'''

35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
'''


def searchInsert(nums:list[int],target:int):

    from bisect import bisect_left,bisect_right

    return bisect_left(nums,target)

# print(searchInsert(nums=[1,3,5,6],target=7))
# print(binary_search(nums=[1,3,5,6],target=2))

'''
153. Find Minimum in Rotated Sorted Array


Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
'''

def findMin(nums): #this is O(n)

    left=0
    right=1

    while(right<len(nums)):
        if nums[left]>nums[right]:
            return nums[right]
        left+=1
        right+=1

    return nums[0]

# print(findMin(nums=[3,4,5,6]))


def findmin2(nums): 

    high=len(nums)-1
    low=0
    ans=float('inf')

    if len(nums)==1:
        return nums[0]

    if nums[low]<=nums[high]:
        return nums[0]

    while(low<=high):

        mid=(low+high)//2

        if nums[0]<=nums[mid]:# it means we are in still increaing path not found the rotated point
            low=mid+1 # soo expand
        else: # we find the point of array that is rotated 
            ans=min(ans,nums[mid])
            high=mid-1 # explore whether there is min number (to find statrting point)

    return ans

# print(findmin2(nums=[6,7,1,2,3,4,5]))

'''
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
 For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
 
'''

def search(nums,target):  # this logic is correct but becoz of pivot finding it becomes O(n)

    n=len(nums)
    right=1
    left=0
    pivot=0

    while (right<n):  # the main goal to seperate array at the pivot element
        if (nums[left]>nums[right]):
            pivot=right
        right+=1
        left+=1

    low=0
    high=pivot-1

    # we search the target element at before pivot element part of array
    while(low<=high):

        mid=(low+high)//2

        if nums[mid]==target:
            return mid 
        if nums[mid]>target:
            high=mid-1
        else:
            low=mid+1

    low=pivot
    high=n-1

    # if we cant find target in non pivot array then we search here
    while(low<=high):

        mid=(low+high)//2

        if nums[mid]==target:
            return mid 
        if nums[mid]>target:
            high=mid-1
        else:
            low=mid+1

    return -1  # if we cant find target in the array

# print(search(nums=  [1,2,3,4,5,6], target = 4))


def search2(nums,target):  # we removed pivot soo O(logn)
    n=len(nums)
    left=0
    right=n-1

    while(left<=right):
        mid=(left+right)//2

        if nums[mid]==target:
            return mid

        if nums[left]<=nums[mid]:  # the first half is sorted
            if nums[left]<=target<nums[mid]:
                right=mid-1
            else:
               left=mid+1

        else:
            if nums[right]>=nums[mid]: #second half is sorted
                if nums[right]>=target>nums[mid]:
                    left=mid+1
                else:
                    right=mid-1

    return -1
# print(search2(nums=  [4,5,6,7,0,1,2], target = 5))



'''
540. Single Element in a Sorted Array

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10
'''

def singleNonDuplicate(nums:list[int]):  # we are using parity here

    n=len(nums)

    left=0
    right=n-1

    if n==1:
        return nums[0]

    while(left<=right):

        mid=(left+right)//2

        if nums[mid]==nums[mid-1]:
            if mid%2==0:
                right=mid-2
            else:
                left=mid+1

        elif mid<n-1 and nums[mid]==nums[mid+1] :
            if mid%2==0:
                left=mid+2
            else:right=mid-1

        if mid<n-1 and nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]:
            return nums[mid]
        else:
            if mid==n-1 and nums[mid]!=nums[mid-1]:
                return nums[mid]

'''
for each pair before pivot the 1st elment parity is even and 2nd is odd

after the pivot element the it becomes viceversa

so from the mid element check whether it falls in which parity 
if pair is odd->even then move left ( as we crossed the pivot)
if pair is even->odd then move right (as we not crossed the pivot)

the 2 codes done the same thing but below one (chatgpt) simplifed the edge conditions

'''

print(singleNonDuplicate(nums=[1]))

def singleNonDuplicatre2(nums):

    n=len(nums)

    left=0
    right=n-1

    while(left<right):

        mid=(left+right)//2

        if mid%2==1:  # always forcing mid to be at even
            mid-=1

        if nums[mid]==nums[mid+1]:
            left=mid+2
        else:
            right=mid

    return nums[left]

print(singleNonDuplicatre2(nums=[3,3,7,7,10,11,11]))
