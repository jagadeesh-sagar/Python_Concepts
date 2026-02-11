import string

# Reverse a string
def reverse_string(name:str)->str:
    rev_name=name[::-1]
    return rev_name

rev_str=reverse_string('jagadeesh')
print(rev_str)

# to check palindrome
def palindrome(name:str)->str:
    if name == reverse_string(name):
        return True
    else:
        return False
    
print(palindrome('level'))

# Count vowels and consonants in a string

vowels=['a','e','i','o','u']
word='anushkasen'
vowels_count=0
consonants_count=0

for i in word:
    if i in vowels:
        vowels_count+=1
    else:
        consonants_count+=1

print(vowels_count,consonants_count)


