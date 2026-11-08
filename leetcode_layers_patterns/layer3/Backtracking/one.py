'''
78. Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

'''

def subsets(nums: list[int]) -> list[list[int]]:
    result=[]
    current=[]

    def backtracking(start):
        result.append(current[:])
        print(current,start)

        for i in range(start,len(nums)):
            current.append(nums[i])
            backtracking(i+1)
            current.pop()
    
    backtracking(0)
    return result

# print(subsets(nums=[1,2,3]))

'''
46. Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

'''

def permute(nums:list[int]) -> list[list[int]]:

    result=[]
    current=[]
    visited=len(nums)*[False]

    def backtracking(current):

        if len(current)==len(nums):
            result.append(current.copy())
            return

        for i in range(len(nums)):
            if visited[i]:
                continue

            visited[i]=True

            current.append(nums[i])
            backtracking(current)
            current.pop()
            visited[i]=False
 
    backtracking(current)

    return result,visited


print(permute(nums=[1,2,3]))

