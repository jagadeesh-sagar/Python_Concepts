'''
856. Score of Parentheses

Given a balanced parentheses string s, return the score of the string.
The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 
Example 1:

Input: s = "()"
Output: 1

'''

def scoreOfParentheses(s: str) -> int:

    stack=[0]
    val=0
    for ch in s:

        if ch == "(":
            stack.append(0)
        else:
            val=stack.pop()

            if val==0:
                score=1
            else:
                score=2*val

            stack[-1]+=score

    return stack

scoreOfParentheses(s="(()(()))")


'''
1190. Reverse Substrings Between Each Pair of Parentheses

You are given a string s that consists of lower case English letters and brackets.
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any brackets.

Example 1:
Input: s = "(abcd)"
Output: "dcba"

Example 2:
Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.

'''

def reverseParentheses(s:str)->str:

    stack=[]
    # char=""
    temp=[]

    for ch in s:
        if ch!=")" :
            stack.append(ch)
        if ch==")":
            while stack[-1]!="(":
                element=stack.pop()  
                # char+=element
                temp.append(element)  # o(1)
        
            stack.pop()
            # for c in char:
            #     stack.append(c)
            # char=''   
            stack.extend(temp) 
            temp=[]  
             
    return "".join(stack)


'''
For better understanding !! 👇
example walkthrough of (ed(et(oc))el)

Start with (ed(et(oc))el).
Reverse oc -> co : (ed(etco)el).
Reverse etco -> octe : (edocteel)
Reverse edocteel -> leetcode : leetcode
'''

# print(reverseParentheses(s="(ed(et(oc))el)"))


'''
1614. Maximum Nesting Depth of the Parentheses

Example 1
Input : "(1+(2*3)+((8)/4))+1"
Output: 3

"Find the maximum number of open parentheses at any point while scanning the string."
'''

def maxDepth(s:str)->int:

    stack=[0]  # simply i can use a variable too (here it is not even a stack)
    max_depth=0

    for ch in s:
        if ch=="(":
            stack[-1]+=1
            max_depth=max(max_depth,stack[-1])

        if ch==")":
            stack[-1]-=1

    return max_depth

# print(maxDepth(s= "(1)+((2))+(((3)))"))

'''
394. Decode String

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"


'''

def decodeString(s: str)->str:

    char=""
    stack=[]
    number=0
    number_char=''

    for ch in s:
        if ch!="]":
            stack.append(ch)

        else:
            while stack and ord(stack[-1])>57:
            
                if stack[-1]=='[':
                    stack.pop()
                else:
                    char+=stack.pop()

            while stack and ord(stack[-1])<58:
                number_char+=stack.pop()

            number_char=number_char[::-1]
            number=int(number_char)
            number_char=''

            char*=number
            char=char[::-1]

            for c in char:
                stack.append(c)
            char=''

    return "".join(stack),stack

print(decodeString(s= "3[a]2[bc]"))
'''
chatgpt cleaner approach
'''

def decodeString_2(s: str)->str:

    stack = []

    for ch in s:

        if ch != "]":
            stack.append(ch)
            continue

        substring = []

        while stack[-1] != "[":
            substring.append(stack.pop())

        stack.pop()        # remove [

        digits = []

        while stack and stack[-1].isdigit():
            digits.append(stack.pop())

        repeat = int("".join(reversed(digits)))

        decoded = "".join(reversed(substring)) * repeat

        stack.extend(decoded)

    return "".join(stack)