'''

763. Partition Labels

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]
 
'''

def partitionLabels(s):
    d={}

    for i in range(len(s)):
        d[s[i]]=i
    left=0
    result=[]
    right=0

    while(right<len(s)):
        sub_range=d[s[right]]

        while(right<=sub_range):
            if d[s[right]]>sub_range:
                sub_range=d[s[right]]

            right+=1
        total_sub_length=right-left
        result.append(total_sub_length)
        left=right

    return result



partitionLabels(s='eccbbbbdec')


'''
992. Subarrays with K Different Integers

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 
'''


def subarraysWithKDistinct(nums,k):
    '''
    link: https://leetcode.com/problems/subarrays-with-k-different-integers/solutions/235235/C++Java-with-picture-prefixed-sliding-window/
    link: https://leetcode.com/problems/subarrays-with-k-different-integers/solutions/235235/C++Java-with-picture-prefixed-sliding-window/comments/251836/
    '''

    d={}
    current_winodow_unique=0
    unique=0
    right,left=0,0

    while right<len(nums):

        d[nums[right]]=d.get(nums[right],0)+1

        if len(d)>k:  # shrinking left window as distinct values are crossed k
                        # in my code i tried to achieve this i can able to properly use current_window_variable
            d.pop(nums[left])
            left+=1
            current_winodow_unique=0  #its new window so start new

        while d[nums[left]]>1: 
             # we are shrinking the window unitl non-duplicates occur . rmving duplicates still haves same distinct valuse
             # so even removed subarrays is also valid soo increment the "current_winodow_unique"
                                # then remove left value and incerement .minimize wind as much as possible
            d[nums[left]]-=1
            current_winodow_unique+=1 # remembering all possible good subarrays
            left+=1

        right+=1 

        if len(d)==k: # whenever we found sufficent distinct k values 
            unique+=current_winodow_unique+1
            print(d)

    return unique

# print(subarraysWithKDistinct(nums=[5,7,5,2,3,3,4,1,5,2,7,4,6,2,3,8,4,5,7],k=7))



'''
longest-substring-with-at-most-k-distinct-characters
'''

def long_substring(s,k):

    if k ==0: return 0

    d={}
    best_string=0
    str_len=0
    left,right=0,0

    while(right<len(s)):

        d[s[right]]=d.get(s[right],0)+1

        while len(d)>k:

            d[s[left]]-=1
            if d[s[left]]==0:
                del d[s[left]]
            left+=1

        str_len=(right-left)+1
        best_string=max(best_string,str_len)
        
        right+=1

    return best_string

print(long_substring(s='aabbcc',k=2))  #ababcc





    


