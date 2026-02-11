'''
Strings are immutable- all methods returns a new string
Most methods are O(n) 
-"in" operator in O(n*m) for substring search

'''

s='jagadeesh'

print(s[0])
print(s[-1])
print(s[:3])
print(s[::2]) #step 2 (skip evry 2nd element)
print(s[::-1])  # reverse

# String Methods - Case Conversion

print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())

# Searching & Finding

stext='hello world'

print(stext.find('o'))  # 4- first occurence index(retuns -1 if not found)
print(stext.rfind('o')) # 7 - last occurence
print(stext.index('o')) # just like find() but raises ValueError if not found
stext.count('o') # 2 no of occurences
print(stext.startswith('hel'))
print(stext.endswith('ld'))

# Replacing & Removing

full_name='Gobburi Jagadeesh'
print(full_name.replace('Ja','ja'))
print(full_name.replace('a','A',1)) #max replace only 1 time
print(full_name.strip())  # removes whitespaces at both end

# Splitting & Joining

text='hello world,python\n'\
   'hel dskn'

print(text.split())
print(text.split(','))
print(text.splitlines())  #split by line breaks

alpha="a,b,c"
print(alpha.partition(','))  #split at first occurence  

print('-'.join(['a','b']))
print(' '.join(['hello','world']))

snum='hello123'

print(snum.isalpha())
print(snum.isdigit())
print(snum.isalnum())
print(snum.islower())
print(snum.isdecimal())
print(snum.isidentifier())

#  Special Operations
print('--------------------------------------')

s1 = "hello"
s2 = "world"
print(s1 + s2)                # "helloworld" - concatenation
print(s1 * 3)                 # "hellohellohello" - repetition
print(s1 < s2)   # True - lexicographic comparison ,Lexicographical order is based on Unicode values
print(s1 == s2)               # False - equality

import string
# # string.ascii_letters   # 'abcd...xyzABC...XYZ'
# # string.ascii_lowercase # 'abcd...xyz'
# # string.ascii_uppercase # 'ABC...XYZ'
# # string.digits          # '0123456789'
# # string.hexdigits       # '0123456789abcdefABCDEF'
# # string.octdigits       # '01234567'
# # string.punctuation     # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
# # string.whitespace      # ' \t\n\r\x0b\x0c'
# # string.printable       # All printable characters

# print(punctuation('hello,'))



text='hello jagadeesh,hello jagadeesh,jagadeesh is such a good guy;'
# newtext=text

# for i in text:
#      if i in string.punctuation:
#            print(i)
#            newtext=newtext.replace(i,' ')
# print(newtext)

# //////////////////////////////////////////////////////////////

# Create a map: all punctuation becomes 'M'
# 2 arguemtns are used for replcament ,2 arguments should be of same size
table = str.maketrans(string.punctuation, ' ' * len(string.punctuation))  
clean_text=text.translate(table)
print(clean_text)

# 3 -> 2 are of replacement ,3 arg is for deletions  (operations happen in ord(A) (asci) soo fast) 
name='Jagadeesh sagar is such nut'
t=str.maketrans('j','J','n')
tr=name.translate(t)

print(tr)