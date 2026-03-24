# Find all permutations of a string

'''https://claude.ai/share/e3753f0b-497e-4fae-a267-bddc7df0c873  ->refer the link for recursion visulization

'''
def permuations(name):
    if len(name)==1:
        return name
    result=[]
    for i in range(len(name)):             
        char=name[i]
        remaining=name[:i]+name[i+1:]
        print(f'remaining: {remaining}')

        for p in permuations(remaining):
            print(char+p)
            result.append(char+p)
    return result

# c=permuations(name='abc')
# print(c)

# ///////////////////////////////////
from itertools import permutations

# print([''.join(p) for p in permutations("abc")])

# /////////////////////////////////////If You Want In-Place Style (Backtracking)///////////////////
def permute(chars, l, r, result):
    if l == r:
        result.append(''.join(chars))
        return

    for i in range(l, r + 1):
        chars[l], chars[i] = chars[i], chars[l]
        permute(chars, l + 1, r, result)
        chars[l], chars[i] = chars[i], chars[l]  # backtrack


# s = "abc"
# result = []
# permute(list(s), 0, len(s) - 1, result)
# print(result)

# /////////////////////////////////////////
'''
Longest substring without repeating characters
'''

def longest_no_repeat(stri):
    seen:dict={}
    left=0
    best=0

    for R,char in enumerate(stri):
        if char in seen and seen[char]>=left:
            left=seen[char]+1
            
        seen[char]=R
        best=max(best,R-left+1)
    print(stri[::best])


# longest_no_repeat(stri='abcabcbb')
# ////////////////////////////////////////////

'''
String compression - "aaabbcccc" → "a3b2c4"
'''
def string_compression(name:str):
    if not name:  # Handle empty string
       return ""

    new_string=''
    count=1

    for i in range(len(name)):

        if i+1< len(name) and name[i]==name[i+1]:
            count+=1
        else:
            new_string+=name[i]+str(count)
            count=1

    return new_string

print(string_compression(name='aaabbcccc'))

# ///////////////////////////////////////
