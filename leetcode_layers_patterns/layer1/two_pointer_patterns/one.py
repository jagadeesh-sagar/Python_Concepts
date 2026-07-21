'''

LeetCode 259 — 3Sum Smaller

Problem

Given an integer array nums and an integer target, return the number of index triplets (i, j, k) such that:

0 <= i < j < k < n
nums[i] + nums[j] + nums[k] < target


nums = [-2, 0, 1, 3]
target = 2

nums = [3, 1, 0, -2]
target = 4

nums = []
target = 0
'''

def three_sumsmaller(nums:list,target:int):

    n=len(nums)
    count=0
    nums.sort()

    for i in range(0,n-2):
        j=i+1
        k=n-1

        while(j<k):

            if nums[i]+nums[j]+nums[k]>=target:
                k-=1  # looking for smaller values
            else: # left corner
                count=count+k-j # as numbers from (j to k) are 3rd element that can form triplets
                j=j+1
    return count

'''
3rd element was intelligent calculated decremented k element sum is greater then idea is that elements from k will be higher
soo move to left (there is hope that values will smaller)

when we find k element that make sum smaller then target then all the elements from j to k are also valid 3rd triplets

'''

print(three_sumsmaller(nums=[],target=0))

'''
leetcode 360 — Sort Transformed Array 

You're given:

nums = sorted array
a, b, c

Apply:

f(x)=ax**2+bx+c

to every element and return the transformed values in sorted order.

nums = [-4, -2, 2, 4]
a = 1
b = 3
c = 5

f(-4) = 16 - 12 + 5 = 9
f(-2) = 4 - 6 + 5 = 3
f(2)  = 4 + 6 + 5 = 15
f(4)  = 16 + 12 + 5 = 33

return [3, 9, 15, 33]

=> its special case it invloves graph representation  the q.e forms a parabloa  (U shape)

if a>0 the u shape (up side):
    then transformed values at end are high from both sides

if a<0 then u shape (down side)
    then transformed values at end are smallest

consider each end a pointer then place the elments

'''

def transformed(a,b,c,nums):
    left=0
    n=len(nums)
    right=n-1
    result=[0]*n

    if a>=0:
        idx=n-1
        while(left<=right):
            
            right_value=a*nums[right]**2+b*nums[right]+c
            left_value=a*nums[left]**2+b*nums[left]+c

            if right_value>left_value:
                result[idx]=right_value
                right-=1
            else:
                result[idx]=left_value
                left+=1
            idx-=1
    else:
        idx=0

        while(left<=right):
            
            right_value=a*nums[right]**2+b*nums[right]+c
            left_value=a*nums[left]**2+b*nums[left]+c

            if right_value<left_value:
                result[idx]=right_value
                right-=1
            else:
                result[idx]=left_value
                left+=1
            idx+=1

    return result

print(transformed(a=1,b=3,c=5,nums=[-4,-2,2,4]))