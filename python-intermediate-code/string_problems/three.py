'''
Find longest palindromic substring

Input: "babad"
Output: "bab" (or "aba" — both valid)
Input: "cbbd"
Output: "bb"

Input: "banana"
Output: "anana"

Input: "a"
Output: "a"
Input: "abc"
Output: "a" (or "b" or "c")
'''

def palindrome(string1:str)->str:
   
    n=len(string1) 
    longest_palindrome=''


    for i in range(len(string1)):
        left=i
        right=left+1
        evn_palindrome=''
        odd_palindrome=''
     
     # even
        while(left>=0 and right<n and string1[left]==string1[right]):
           
            evn_palindrome=string1[left:right+1]
            if len(longest_palindrome)<len(evn_palindrome):
                longest_palindrome=evn_palindrome 
            left-=1
            right+=1
     
     # odd
        left,right=i,i
        while(left>=0 and right<n and string1[left]==string1[right]):
         
            odd_palindrome=string1[left:right+1]
            if len(longest_palindrome)<len(odd_palindrome):
                longest_palindrome=odd_palindrome 
            left-=1
            right+=1
    return longest_palindrome if longest_palindrome!='' else string1[0]
        
print(palindrome(string1='banana'))



def palindrome_2(s: str) -> str:  # its chatgpt code
    longest = ""

    for i in range(len(s)):

        # Odd length palindrome
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > len(longest):
                longest = s[left:right+1]
            left -= 1
            right += 1

        # Even length palindrome
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > len(longest):
                longest = s[left:right+1]
            left -= 1
            right += 1

    return longest

print(palindrome_2(s='banana'))





