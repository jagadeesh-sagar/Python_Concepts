
def subarraysDivByK(nums: list[int], k: int) -> int:

    count=0
    prefix_map={0:1}
    prefix_sum=0

    for num in nums:
        prefix_sum+=num
        rem=prefix_sum%k  

        if rem <0:
           rem=((prefix_sum%k)+k)%k  

        count+=prefix_map.get(rem,0)
        prefix_map[rem]=prefix_map.get(rem,0)+1
    
    return count

'''

if two prefix has same rem than the array between the is divsible 
(it is divisible thats why so rem is added from last prefix to current_prefix)
'''        
# subarraysDivByK(nums = [4,5,0,-2,-3,1], k = 5)


def numberOfSubarrays(nums: list[int], k: int)->int:

    count=0
    prefix_map={0:1}
    prefix_sum=0
    c=0

    for num in range(len(nums)):
        if nums[num]%2==0:
            prefix_sum+=0
        else:
            prefix_sum+=1

        count+=prefix_map.get(prefix_sum-k,0)
        prefix_map[prefix_sum]=prefix_map.get(prefix_sum,0)+1

    return count   

numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2)


'''
930. Binary Subarrays With Sum

Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
A subarray is a contiguous part of the array.

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15

'''

def numSubarraysWithSum(nums:list[int],goal: int)->int:

    count=0
    prefix_map={0:1}
    prefix_sum=0

    for num in range(len(nums)):
        prefix_sum+=nums[num]
        count+=prefix_map.get(prefix_sum-goal,0)
    
        prefix_map[prefix_sum]=prefix_map.get(prefix_sum,0)+1
    print(prefix_map,count)


# numSubarraysWithSum(nums=[1,0,1,0,1], goal = 2)


'''

Longest Subarray with Sum K

Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
Output: 6
Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. 
The length of the longest subarray with a sum of 15 is 6.

Input: arr[] = [-5, 8, -14, 2, 4, 12], k = -5
Output: 5
Explanation: Subarrays with sum = -5 are [-5] and [-5, 8, -14, 2, 4].
The length of the longest subarray with a sum of -5 is 5.

Input: arr[] = [10, -10, 20, 30], k = 5
Output: 0
Explanation: No subarray with sum = 5 is present in arr[].


'''

def longestSubarray(arr,k):

    prefix_sum=0
    prefix_map={0:-1} # use -1 soo that it wont collide with indexes

    index=0
    max_length=0

    for num in range(len(arr)):

        prefix_sum+=arr[num]

        if prefix_sum-k in prefix_map:
            index=prefix_map[prefix_sum-k]
            max_length=max(max_length,num-index)

    
        prefix_map[prefix_sum]=prefix_map.get(prefix_sum,num)

    return max_length

longestSubarray(arr=[10, 5, 2, 7, 1, -10], k = 15)