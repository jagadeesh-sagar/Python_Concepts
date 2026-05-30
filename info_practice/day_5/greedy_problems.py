'''
LC 53 — max subarray (Kadane's)

mple 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

'''

def kadens_max_sum(nums):

    local_max=0
    global_max=float('-inf')

    for i in range(len(nums)):

        if nums[i]>local_max+nums[i]:
            local_max=nums[i]
        else:
            local_max=local_max+nums[i]

        global_max=max(global_max,local_max)

    return global_max

# print(kadens_max_sum(nums=[1]))

'''
169. Majority Element


Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''

def majorityElement(nums):
    
    candidate=0
    count=0

    for i in nums:
        if count==0:
            candidate=i
        if i==candidate:
            count+=1
        else:
            count-=1

    if nums.count(candidate) > len(nums) // 2:
        return candidate

# print(majorityElement(nums=[2,2,1,1,1,3,3,1]))


'''
55. Jump Game

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

'''

def canJump(nums:list):
    goal=len(nums)-1

    for index in range(len(nums)-1,-1,-1):
        if(nums[index]+index)>=goal:
            goal=index
    if goal==0:
        return True
    return False

# print(canJump(nums=[1]))

'''
[4,1,0,5,0,0,0,2]


'''


def canJump2(nums:list):

    l,r=0,nums[0]
    if len(nums)<=1:
        return 0
    count=1

    while(r<len(nums)-1):
        count+=1
        nxt=max(i+nums[i] for i in range(l,r+1))
        l,r=r,nxt
        
    return count

    
print(canJump2(nums=[1,2,1,1,1]))