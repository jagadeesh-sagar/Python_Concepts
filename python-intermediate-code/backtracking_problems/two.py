'''

Find all combinations that sum to target
nums = [2,3,6,7]
target = 7   =>   [[2,2,3], [7]]

'''

def sum_combination(nums:list[int],n:int)->list[list[int]]:
    current=[]
    result=[]

    def backtracking(start,path):

        if sum(current)==n:
            result.append(current[:])
            return

        for i in range(start,len(nums)):

            current.append(nums[i])

            if sum(current)<n:
                backtracking(start=i,path=current)
            else:
                backtracking(start=i+1,path=current)

            current.pop()

    backtracking(0,[])
    return result

# print(sum_combination(nums=[2,3,6,7],n=7))



def sum_combination(nums: list[int], target: int):
    '''
    chatgpt answer
    
    '''

    result = []
    current = []

    def backtrack(start, remaining):

        # found valid combination
        if remaining == 0:
            result.append(current[:])
            return

        # invalid path
        if remaining < 0:
            return

        for i in range(start, len(nums)):

            current.append(nums[i])

            # reuse same element
            backtrack(i, remaining - nums[i])

            current.pop()

    backtrack(0, target)

    return result
