'''
300. Longest Increasing Subsequence
Given an integer array nums, return the length of the longest strictly increasing subsequence.4

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

'''
from bisect import bisect_left,bisect_right
def lengthOfLIS(nums):
    n=len(nums)
    dp=[1]*n

    for i in range(n):
        for j in range(i):
            if nums[i]>nums[j]:
                dp[i]=max(dp[i],dp[j]+1)
    return dp


# print(lengthOfLIS(nums = [10, 9, 2, 5, 3, 7, 101, 18]))


def lengthOfLIS2(nums):
    tail=[]

    for num in range(len(nums)):
        pos=bisect_left(tail,nums[num])
        if pos==len(tail):
            tail.append(nums[num])
        else:
            tail[pos]=nums[num]

    return len(tail)

# print(lengthOfLIS2(nums = [10, 9, 2, 5, 3, 7, 101, 18]))
'''
LC 315

'''
def countSmaller(nums: list[int]):
    '''
    o(n2) overall bcoz of insert
    '''

    n=len(nums)
    sorted_nums=[]
    result=[0]*n

    for i in range(n-1,-1,-1):
        pos=bisect_left(sorted_nums,nums[i])

        sorted_nums.insert(pos,nums[i])
        sorted_length=len(sorted_nums)
        if pos==0:
            result[i]=0

        else:
            tail=sorted_length-(pos)
            result[i]=sorted_length-tail

    return result

'''
this 2 qxns are solved in dp and this qxn can be solved using merge sort O(n logn)

'''

countSmaller(nums=[2,-1,0,-1])

