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

# print(wordPattern(pattern='abc',s="dog cat cat"))
# pattern ="abc" s="bca"
