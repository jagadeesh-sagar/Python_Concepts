'''
Maximum sum of k consecutive elements

k -consecutive so remember whenever we get subarray , k conse,substring, at most k use sliding window 
'''

def consecutive_elements(list1:list,k:int):

    max_sum=sum(list1[:k])
    window_sum=max_sum

    for i in range(k,len(list1)):

        window_sum=window_sum+list1[i]-list1[i-k]
        max_sum=max(max_sum,window_sum)
    print(max_sum,window_sum)

# consecutive_elements(list1=[1, 9, -1, -2, 7, 3],k=2)

'''
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


here i need to take care of whether the char is seen or not it means i need to use dict(hashmap) 
to ensure that if a given substring has seen char stop before adding that char itself and store its length
check the max substring

-> use two pointers+hasmap

'''

def long_substring(s:str)->int:
    seen={}
    left,right=0,0
    list1=list(s)
    max_sum=0
    local_sum=0

    if len(s)==1:
            return len(s)

    while(right!=len(list1)):

        if (seen.get(list1[right]) and seen.get(list1[right])==1):

            seen[list1[right]]=seen.get(list1[right])-1

            while right!=left and list1[left]!=list1[right]:
                   seen[list1[left]]=seen.get(list1[left])-1

                   left+=1

            if list1[left]==list1[right]: 
                 left+=1
        else:
            seen[list1[right]]=seen.get(list1[right],0)+1
            right+=1

        local_sum=right-left
        max_sum=max(local_sum,max_sum)

    print(local_sum,max_sum,seen,left)

'''
 whever there is chance of hashmap(dict or set) in sliding window rather than using pure two pointers try to use this way for finding elements
while s[right] in seen and seen[s[right]] > 0:
=> use “in” 
'''

# print(long_substring(s='pwwkew'))


def long_substring(s: str) -> int:

    seen = {}

    left = 0
    best = 0

    for right, char in enumerate(s):

        # repeated character inside window
        if char in seen and seen[char] >= left:
            left = seen[char] + 1

        seen[char] = right

        best = max(best, right - left + 1)

    return best


# print(long_substring("pwwkew"))


'''
Minimum window substring - Find smallest substring containing all characters input and output

| String `s`            | Target `t` | Output    |
| --------------------- | ---------- | --------- |
| `"ADOBECODEBANC"`     | `"ABC"`    | `"BANC"`  |
| `"a"`                 | `"a"`      | `"a"`     |
| `"a"`                 | `"aa"`     | `""`      |
| `"aa"`                | `"aa"`     | `"aa"`    |
| `"thisisateststring"` | `"tist"`   | `"tstri"` |


'''

def min_window(s:str,t:str)->str:
    left=0
    target={}
    char=''
    
    if not s or not t:
        return ""
    
    for i in t:
        target[i]=target.get(i,0)+1

    window={}

    have=0
    need=len(target)
    print(need)

    result=[-1,-1]
    result_len=float('inf')

    for right in range(len(s)):
         char=s[right]

         window[char]=window.get(char,0)+1

        # valid frequency matched
         if char in target and window[char]==target[char]:
              have+=1

        # valid window found
         while have==need:
              
            if right-left+1<result_len:
                   result=[left,right]
                   result_len=right-left+1

            window[s[left]]-=1

            if s[left] in target and window[s[left]]<target.get(s[left]):
                 have-=1
            left+=1
              
    l,r=result

    return s[l:r+1] if result_len != float("inf") else ""

# print(min_window(s='ADOBECODEBANC',t='ABC'))

''''
LeetCode 209 — 
Minimum Size Subarray Sum

Find the smallest length of a contiguous subarray whose sum is greater than or equal to the target.


| Target | Input Array         | Output |
| ------ | ------------------- | ------ |
| `7`    | `[2,3,1,2,4,3]`     | `2`    |
| `4`    | `[1,4,4]`           | `1`    |
| `11`   | `[1,1,1,1,1,1,1,1]` | `0`    |
| `15`   | `[1,2,3,4,5]`       | `5`    |
| `6`    | `[1,2,3,4]`         | `2`    |

'''

def min_size(nums:list[int],target:int)->int:
     left=0
     sum=0
     result=float('inf')

     for right in range(len(nums)):
        sum=sum+nums[right]
            
        while(sum>=target):
 
            result=min(result,right-left+1)
            print(left,right,result)
            sum=sum-nums[left]
            left+=1

     return result if result !=float('inf') else 0

'''
in above 2 qxns whenever u see min sliding window  do this things
expand the right pointer to meet target

and shrink window by increasing the left pointer to find any min sol in that window and slide over the list
'''
                  
               
# print(min_size(nums=[5,1,3,5,10,7,4,9,2,8],target=15))

'''
Longest Repeating Character Replacement

| Input       | k   | Output |
| ----------- | --- | ------ |
| `"ABAB"`    | `2` | `4`    |
| `"AABABBA"` | `1` | `4`    |
| `"AAAA"`    | `2` | `4`    |
| `"ABCDE"`   | `1` | `2`    |
| `"BAAAB"`   | `2` | `5`    |

'''

def long_repeating(s:str,k:int)->int:


    d={}
    window_size=0
    max_freq=0
    left=0
    result=0

    for right in range(len(s)):
        d[s[right]]=d.get(s[right],0)+1
        max_freq=max(max_freq,d.get(s[right]))

        window_size=right-left+1

        if window_size-max_freq>k:
            d[s[left]]-=1
            left+=1
        result=max(result,right-left+1)
                
    return result
                          
# print(long_repeating(s="AAAABBBB",k=6))


'''

567. Permutation in String

| s1        | s2                | Output  |
| --------- | ----------------- | ------- |
| `"ab"`    | `"eidbaooo"`      | `True`  |
| `"ab"`    | `"eidboaoo"`      | `False` |
| `"adc"`   | `"dcda"`          | `True`  |
| `"hello"` | `"ooolleoooleh"`  | `False` |
| `"xyz"`   | `"afdgzyxksldfm"` | `True`  |
| `"a"`     | `"ab"`            | `True`  |

'''

def permutation_str(s1:str,s2:str)->bool:
     
    d1={}
    d2={}

    right=len(s1)-1
    left=0

    window_size=right

    for i in s1:
        d1[i]=d1.get(i,0)+1

    while(right<len(s2)):
        if s2[right] and s2[left] in d1:

            while(left<=right and s2[left] in d1):
                d2[s2[left]]=d2.get(s2[left],0)+1
                left+=1

            if d1==d2:
                return True
            else:
                d2={}
                left=right-window_size
        
        right+=1
        left+=1
    return False
    
# print(permutation_str(s1='adc',s2='dcda'))


def permutation_str_2(s1: str, s2: str) -> bool:
    '''
    chatgpt
    '''

    if len(s1) > len(s2):
        return False

    d1 = {}
    d2 = {}

    # frequency of s1
    for char in s1:
        d1[char] = d1.get(char, 0) + 1

    window = len(s1)

    # first window
    for i in range(window):
        d2[s2[i]] = d2.get(s2[i], 0) + 1

    if d1 == d2:
        return True

    left = 0

    # slide window
    for right in range(window, len(s2)):

        # add new character
        d2[s2[right]] = d2.get(s2[right], 0) + 1

        # remove old character
        d2[s2[left]] -= 1

        # clean zero counts
        if d2[s2[left]] == 0:
            del d2[s2[left]]

        left += 1

        if d1 == d2:
            return True

    return False


# print(permutation_str("adc", "dcda"))
 

'''
container with most water -leetcode 11

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Input: height = [1,1]
Output: 1
 
'''

def most_water(nums:list[int])->int:

    max_volume=0
    left=0
    right=len(nums)-1

    while(left<right):
        height=min(nums[left],nums[right])
        volume=(right-left)*height

        max_volume=max(max_volume,volume)

        if nums[left]>nums[right]:
            right-=1
        else:
            left+=1
        print(height,volume,max_volume)
    print(max_volume)

most_water(nums=[1,1])