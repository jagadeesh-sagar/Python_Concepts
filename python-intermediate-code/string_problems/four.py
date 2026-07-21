'''
Check if one string is a rotation of another 
- "waterbottle" is rotation of "erbottlewat"

Input: "aaab", "abaa"
Output: True
Input: "aaab", "aaba"
Output: True
Input: "aaab", "baaa"
Output: True

Input: "", ""
Output: True
Input: "a", "a"
Output: True
Input: "a", "b"
Output: False

Input: "aaaa", "aaaa"
Output: True
Input: "abc", "abc"
Output: True


'''

def string_rotation(s1:str,s2:str)->bool:
    if len(s1)!=len(s2):
        return False
    if s1=='' and s2=='':
        return True
    left,right=0,0
    
    for right in range(len(s1)):
        while(left<len(s1) and s1[left]!=s2[right]):
            left+=1
        sub_str=left-right
        rotated_str=s1[sub_str:]+s1[:sub_str]

        if rotated_str==s2:
            return True
    return False

# print(string_rotation(s1='a',s2='a'))

def string_rotation_2(s1:str,s2:str)->bool:

    if len(s1)!=len(s2):
        return False
    if s1=='':
        return True
    
    s3=s1+s1
    str_len=len(s1)

    for left in range(len(s3)):
        if s3[left:left+str_len]==s2:
            return True

print(string_rotation_2(s1='',s2=''))


def string_rotation_3(s1:str,s2:str)->bool:

    if len(s1)!=len(s2):
        return False

    return s2 in (s1+s1)

print(string_rotation_3(s1='',s2=''))

def string_rotation(s1:str,s2:str)->bool:

    c='jaggu'
    name=''

    for i in range(len(s1)):
        name=s1[i::]+s1[:i]

        if name==s2:
            return True

    return False
print(string_rotation(s1='waterbottle',s2='erbottlewat'))