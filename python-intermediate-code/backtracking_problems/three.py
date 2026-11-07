'''
77. Combinations

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.


Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.

Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
'''

def combine(n: int, k: int) -> list[list[int]]:

    result=[]
    path=[]

    def backtrack(start,end):
        if len(path)==k:
            result.append(path.copy())
            return

        for i in range(start,end):
            path.append(i)
            backtrack(i+1,end)

            path.pop()

    backtrack(1,n+1)
    return result



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

def permute(self, nums: list[int]) -> list[list[int]]:

    result=[]
    path=[]

    used=[False]*len(nums)

    def backtrack(path):

        if len(path)==len(nums):
            result.append(path.copy())
            return 

        for i in range(len(nums)):
            if used[i]:
                continue

            used[i]=True

            path.append(nums[i])
            backtrack(path)

            path.pop()
            used[i]=False

    backtrack(path)

    return result



def subsetsWithDup(nums: list[int]) -> list[list[int]]:

    current=[]
    result=[]
    path=[]
    
    nums.sort()

    def backtrack(index):
        # if path not in result:
        current.append(path.copy())
            # result_set.add(path.copy())

        for i in range(index,len(nums)):

            path.append(nums[i])
            backtrack(i+1)
            path.pop()

    backtrack(0)

    for paths in current:
        if paths not in result:
            result.append(paths)

    return result

# print(subsetsWithDup(nums=[1,2,2]))

'''
39. Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []




'''

def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    result=[]
    current=[]

    def backtrack(index,path):
        if sum(current)==target:
            result.append(current.copy())
            return
        if sum(current)>target:
            return

        for i in range(index,len(candidates)):
            current.append(candidates[i])

            if sum(current)<target:    
               backtrack(i,path=current)
            else:
                backtrack(i+1,path=current)
            current.pop()

    backtrack(0,path=current)

    return result

# print(combinationSum(candidates=[2,3,6,7], target = 7))



def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    result=[]
    current=[]
    candidates.sort()

    def backtrack(index,remaining_target):
        if remaining_target==0:
            result.append(current.copy())
            return
        if remaining_target<0:
            return

        for i in range(index,len(candidates)):
            if candidates[i]>remaining_target:
                continue
            current.append(candidates[i])
            backtrack(i,remaining_target-candidates[i])
            current.pop()

    backtrack(0,remaining_target=target)

    return result

# print(combinationSum2(candidates=[2,3,6,7], target = 7))



def letterCombinations(digits: str) -> list[str]:

    if not digits:
        return []
    result=[]
    path=[]
    phone_keypad = {
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
        "*": "+",
        "0": " ",
        "#": ""
    }

    def backtrack(index):
        if index==len(digits):
            result.append("".join(path))
            return

        for char in phone_keypad[digits[index]]:
            path.append(char)
            backtrack(index+1)
            path.pop()

    backtrack(0)
    return result


# print(letterCombinations(digits="23"))
