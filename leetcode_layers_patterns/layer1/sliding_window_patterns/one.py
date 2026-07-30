'''
395. Longest Substring with At Least K Repeating Characters

Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

if no such substring exists, return 0.

 

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
 

'''
from collections import Counter

def longestSubstring(s,k):

    max_unique=len(set(s))
    result=0

    for curr_uniq in range(1,max_unique+1):
        freq=[0]*26  # freq table for 26 alphabets
        left=0
        right=0
        unique=0

        count_at_least_k=0

        while(right<len(s)):

            if unique<=curr_uniq:  # expand the current window if current window unique chars less than for loop (curr_uniq)

                idx=ord(s[right])-ord('a')
                
                if freq[idx]==0:  # calculating current window uniques
                    unique+=1

                freq[idx]+=1  # inseriting freq of chars

                if freq[idx]==k:
                    count_at_least_k+=1
                
                right+=1

            else: # unique chars are more than that are for current loop soo.. shrink window from left

                idx=ord(s[left])-ord('a')

                if freq[idx]==k:
                    count_at_least_k-=1
                
                freq[idx]-=1

                if freq[idx]==0:  # calculating current window uniques
                  unique-=1

                left+=1

            if unique==curr_uniq and unique==count_at_least_k:
                result=max(result,right-left)

    return result

# print(longestSubstring(s='aaabb',k=3))

'''
1004. Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined


[0,0,1,1,1,0,0]=>k=0=>3
'''

def longestOnes(nums,k):

    left=0
    right=0
    n=len(nums)
    max_windows_size=0
    windows_size=0
    z=0
   

    while(right<n):

      # expand the window by making zeros flips
        if nums[right] == 0: 
            z += 1

        # if flips are more than limit than shrink the window 
        while z > k:  
            if nums[left] == 0:
                z -= 1
            left += 1

        windows_size=right-left+1

        max_windows_size=max(max_windows_size,windows_size)

        right+=1
        
    return max_windows_size

print(longestOnes(nums= [1,1,1,0,0,0,1,1,1,1,0],k=2))

        # print(f'flips:{flips} ,maxflips:{max_flips},right:{right} ,left:{left}')
        # print(left,right,z,'windows:',windows_size)


'''
1234. Replace the Substring for Balanced String

You are given a string s of length n containing only four kinds of characters: 'Q', 'W', 'E', and 'R'.
A string is said to be balanced if each of its characters appears n / 4 times where n is the length of the string.
Return the minimum length of the substring that can be replaced with any other string of the same length to make s balanced. If s is already balanced, return 0.

 

Example 1:

Input: s = "QWER"
Output: 0
Explanation: s is already balanced.
Example 2:

Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
Example 3:

Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER". 

'''
# QWERQWQQ

def balancedString(s: str) -> int:
    from collections import Counter

    count=Counter(s)
    n=len(s)

    target=n//4

    if all(count[ch]==target for ch in "QWER"):return 0

    left=0
    ans=n

    for right in range(n):
        count[s[right]]-=1 # char entering window decrease the freq of it 

        while(count['Q']<=target and
              count['W']<=target and
              count['E']<=target and
              count['R']<=target 
              ):
            
            ans=min(ans,right-left+1)
            # print(left)
            count[s[left]]+=1 # char leaving thr window so increase the freq of it 
            left+=1
    return ans

'''
the main idea here is that find the substring that we have to change .
for that use sliding window :
1. Increase the window 
2. If the window is subtracted from the main string if all "QWER" in the remainig string obeys the target value 
then it is valid window substring that has to be replaced

3.remember the length of substring 
4. Shrink the window and find explore to find new window

'''


print(balancedString("QWER"))       # 0
print(balancedString("QQWE"))       # 1
print(balancedString("QQQW"))       # 2
print(balancedString("QQQQ"))       # 3
print(balancedString("QQQQWERR"))   # 2
print(balancedString("WQWRQQQW"))   # 3