'''
290. Word Pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
 

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Explanation:
The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

'''


def wordPattern(pattern,s:str):

    pattern_len=len(pattern)
    string=s.split(' ')
    str_len=len(string)

    if pattern_len!=str_len:
        return False
    
    d={}
    d2={}
    
    for i in range(pattern_len):
        # print(d,'hi')
        if not d.get(pattern[i]):
            if d2.get(string[i]):
                return False
            else:
                d[pattern[i]]=string[i]
                d2[string[i]]=pattern[i]

        elif d[pattern[i]]!=string[i]:
            return False
    
    return True

'''
i mapped a->b and b->a by using two dict it hepled to mee to check bijection correctnes
'''

# print(wordPattern(pattern='abc',s="dog cat pot"))

'''
560. Subarray Sum Equals K
Solved

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

nums=[3,4,7,2,-3,1,4,2],k=7
output :4

'''


def subarray_sum_k(nums: list[int],k:int)->int:
    count=0
    prefix_sum=0

    prefix_map={0:1}

    for num in nums:
        prefix_sum+=num
        count+=prefix_map.get(prefix_sum-k,0)  # if any prefix exists after subtracting the nums , then all nums are in prefix array
        prefix_map[prefix_sum]=prefix_map.get(prefix_sum,0)+1

    return count

'''
prefix sum are used mainly :(instead of O(n) to O(1)
"Sum betwenn L and R
"count element in range " 
"Cummulative values"
"One-time preprocessing + many range queries

https://claude.ai/share/dc021858-ab4d-4ed0-a02f-8f7247d05f73

'''

# print(subarray_sum_k(nums=[1,0,1,0,1],k=2))
