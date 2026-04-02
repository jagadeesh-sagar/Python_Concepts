'''
//////////// 2-SUM  ///////////////

nums = [2,7,11,15], target = 9
Output: [0,1]

Input:
nums = [3,2,4], target = 6
Output: [1,2]

'''

def two_sum(arr:list[int],target:int)->list[int]:

    d={}

    for i in range(len(arr)):
        num=target-arr[i]

        if num in d:
            return [d[num],i]        
        d[arr[i]]=i

print(two_sum(arr=[3,2,4],target=6))
