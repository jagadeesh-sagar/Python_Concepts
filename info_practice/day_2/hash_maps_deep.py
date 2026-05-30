'''
LC 1 — two sum

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

'''

def two_sum(nums:list[int],target:int)->list[int]:
    seen={}
    complement=0

    for j in range(len(nums)):
        complement=target-nums[j]
        if complement in seen:
            return([j,seen[complement]])
        seen[nums[j]]=j
    

# two_sum(nums=[3,3,5,16],target=6)

'''
49. Group Anagrams

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

'''
def group_anagrams(strs:list[int])-> list[list[str]]:

    d={}

    for word in strs:
        arranged_word=''.join(sorted(word))

        if arranged_word in d:
            d.get(arranged_word).append(word)
        else:
            d[arranged_word]=[word]

    return list(d.values())
    #   from collections import defaultdict
    #   groups = defaultdict(list)
    #   for s in strs:
    #         key = tuple(sorted(s))
    #         print(key)
    #         groups[key].append(s)
    #         # print(groups)
    #   return list(groups.values())
# print(group_anagrams(strs=["eat","tea","tan","ate","nat","bat"]))

from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)

    for word in strs:

        count = [0] * 26

        for ch in word:
            count[ord(ch) - ord('a')] += 1

        groups[tuple(count)].append(word)

    return list(groups.values())

'''
347. Top K Frequent Elements
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]

'''

def top_k_elements(nums:list[int],k:int)-> list[int]:

    from collections import Counter

    d=Counter(nums)
    # print(d.most_common(2))
    result=[]

    top_freq=tuple(sorted(d.values(),reverse=True)[:k])
    for key ,value in d.items():
        if value in top_freq:
            result.append(key)

    return result

top_k_elements(nums=[1,1,1,1,2,2,2,3,4],k=2)

'''
LC 128 — longest consecutive sequence
Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3


'''

def longest_consecutive(nums:list[int])->int:

  
    max_count=0
    count=0
    set_nums=set(nums)

    for num in set_nums:
        if num-1 not in set_nums:
            current = num
            count = 1
            while(current+1 in set_nums):
                current+=1
                count+=1
       
            max_count=max(max_count,count)
    return max_count

'''
here we are iterated through the set in leetcode because thw test cases are too big

and set loop removed duplicate saved a lot of time

'''
           
# print(longest_consecutive(nums=[1,0,1,2]))


'''
LeetCode 560 — Subarray Sum Equals K

Find the total number of contiguous subarrays whose sum equals k.

| nums                 | k   | Output |
| -------------------- | --- | ------ |
| `[1,1,1]`            | `2` | `2`    |
| `[1,2,3]`            | `3` | `2`    |
| `[3,4,7,2,-3,1,4,2]` | `7` | `4`    |
| `[1,-1,0]`           | `0` | `3`    |
| `[5]`                | `5` | `1`    |

'''

def subarray_sum_k(nums: list[int],k:int)->int:
    count=0
    prefix_sum=0

    prefix_map={0:1}

    for num in nums:
        prefix_sum+=num
        count+=prefix_map.get(prefix_sum-k,0)
        prefix_map[prefix_sum]=prefix_map.get(prefix_sum,0)+1


    return count
'''
continus sum and check remainig exists then sub array exists if yes increase count
'''


# print(subarray_sum_k(nums=[3,4,7,2,-3,1,4,2],k=7))

'''

387. First Unique Character in a String

 

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1

'''

def first_unique(s:str)->int:
    from collections import Counter

    d=Counter(s)

    for i in range(len(s)):
        if d.get(s[i])==1:
            return (i)
    return -1

# print(first_unique(s=''))

'''
443. String Compression

aaabbc->a3b2c1

'''

def string_has_comp(s:str)->str:
    from collections import Counter

    d=Counter(s)
    result=''

    for key,value in d.items():
        c=str(key)+str(value)
        result=result+c
    

    return result
'''
we can solve this with two pointers approach too
'''

string_has_comp(s='aaabbc')

def string_compression(chars: list[str])->int:
    '''
    this particular question output and input are little bit diff in leetcode

    443. String Compression
    
    '''

    right,left=0,0
    result=[]
    count=0

    while(right<len(chars)):
        result.append(chars[right])

        while(right<len(chars) and chars[left]==chars[right]):
            count=count+1
            right+=1
        result.append(str(count))
        count=0
        
            # if right!=0 or chars
        # chars[]
            
        left=right
    return result

print(string_compression(chars=["a","a","b","b","c","c","c"]))
        # result=


